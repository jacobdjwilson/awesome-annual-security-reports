GSMA Mobile Telecommunications
Security Landscape - 2026
Copyright © 2026 GSMA February 2026

GSMA Mobile Telecommunications
Security Landscape - 2026
About the GSMA
The GSMA is a global   Unlock the benefits of   Security Classification:   Disclaimer
| organisation unifying  | GSMA membership | Non-confidential |
| ---------------------- | --------------- | ---------------- |

the mobile ecosystem  The GSM Association (“Association”)
|     | As a member of the GSMA, you join a  |     |
| --- | ------------------------------------ | --- |
to unlock the full power  makes no representation, warranty
|     | vibrant community of industry leaders  | Access to and distribution of this  |
| --- | -------------------------------------- | ----------------------------------- |
or undertaking (express or implied)
|     | and visionaries – helping to shape the  | document is restricted to the persons  |
| --- | --------------------------------------- | -------------------------------------- |
of connectivity so that  with respect to and does not accept
|     | future of mobile technology and   | permitted by the security classification.  |
| --- | --------------------------------- | ------------------------------------------ |
any responsibility for, and hereby
people, industry and  its transformative impact on societies  This document is confidential to the
disclaims liability for the accuracy
|     | worldwide. | Association and is subject to copyright  |
| --- | ---------- | ---------------------------------------- |
society thrive.  or completeness or timeliness of the
protection. This document is to be  information contained in this document.
|     | Our unique position at the heart of   | used only for the purposes for which  |
| --- | ------------------------------------- | ------------------------------------- |
The information contained in this
|     | the mobile industry means you get   | it has been supplied and information  |
| --- | ----------------------------------- | ------------------------------------- |
Led by our members, we represent the  document may be subject to change
|     | exclusive access to our technical   | contained in it must not be disclosed  |
| --- | ----------------------------------- | -------------------------------------- |
without prior notice.
interests of over 1,100 operators and
|     | experts, data and analysis – as well as  | or in any other way made available, in  |
| --- | ---------------------------------------- | --------------------------------------- |
businesses in the broader ecosystem.
|     | unrivalled opportunities for networking,  | whole or in part, to persons other than  |
| --- | ----------------------------------------- | ---------------------------------------- |
The GSMA also unities the industry at
|     | innovation support and skills   | those permitted under the security  |
| --- | ------------------------------- | ----------------------------------- |
Antitrust Notice
world-leading events, such as MWC
|     | acceleration.  | classification without the prior written  |
| --- | -------------- | ----------------------------------------- |
(in Barcelona, Kigali, Las Vegas and
approval of the Association.

| Shanghai) and the M360 Series. | For more information, please visit:   |     |
| ------------------------------ | ------------------------------------- | --- |
The information contained herein
|     | http://www.gsma.com/membership/ | Copyright Notice |
| --- | ------------------------------- | ---------------- |
is in full compliance with the GSM
Association’s antitrust compliance
  policy.
Copyright © 2026 GSM Association

GSMA Mobile Telecommunications Security Landscape - 2026 2/3

GSMA Mobile Telecommunications
Security Landscape - 2026
Contents
| 1.   Executive Summary   |     | 1   |
| ------------------------ | --- | --- |
2.   Mobile networks, devices and consumers are under attack  3
|   2.1                                      | Software Security                      | 5   |
| ------------------------------------------ | -------------------------------------- | --- |
|   2.2                                      | Democratisation of Attacks             | 6   |
|   2.3                                      | Successful Pre-Positioning Attacks     | 7   |
|   2.4                                      | Exploiting Weak Cyber Hygiene          | 8   |
|   2.5                                      | Supply Chain Security                  | 9   |
|   2.6                                      | The Spectrum: Security, Fraud, Scams   | 11  |
| 3.  Threat Actors                          |                                        | 12  |
| 4.  Risk Management                        |                                        | 15  |
| 5.  Coordinated Vulnerability Disclosure   |                                        | 17  |
6.  Generative and Agentic Artificial Intelligence Security  19
| 7.  Post Quantum Cryptography   |     | 20  |
| ------------------------------- | --- | --- |
8.  Mapping the Global Cybersecurity Regulatory Landscape   22
| 9.  Final Thoughts   |     | 25  |
| -------------------- | --- | --- |

Executive Summary GSMA Mobile Telecommunications
Security Landscape - 2026
1 Executive Summary
This is the GSMA’s eighth annual Mobile Telecommunications Security Landscape report. Building on the previous reports1, it
reflects developments during 2025, updated analyses, new and updated content, identifies key trends and provides a look at some
of the emerging security topics.
The report highlights first that mobile
networks, devices and consumers are
experiencing a full spectrum of attacks
across the globe. This report analyses
Mobile network
these attacks and identifies six key areas
| for attention:                     |     | Sotware attacks  |     |     |
| ---------------------------------- | --- | ---------------- | --- | --- |
| —  Software implementations as a   |     |                  |     |     |
|   key frontline of attacks         |     | Democratisation  |     |     |
of attacks
| —  A democratisation of attacks,   |     |     |     | Generative and  |
| ---------------------------------- | --- | --- | --- | --------------- |
Risk
skcatta fo murtcepS agentic artificial
|   whereby there is a lowering of   |                 |                     | management | intelligence |
| ---------------------------------- | --------------- | ------------------- | ---------- | ------------ |
|                                    | Threat actors   | Successful pre-     |            |              |
|   the technical and resource       |                 | positioning attacks |            |              |
and their modus
  barriers to launch attacks
operandii
Mobile device
—  Pre-positioning attacks that seek to
Exploiting weak
|   establish a bridgehead for later   |     | cyber hygiene |     |     |
| ------------------------------------ | --- | ------------- | --- | --- |
  attacks
Co-ordinated
—  Exploitation of weak cyber hygiene vulnerability  Post quantumn
|     |     | Supply chain   |     | cryptography |
| --- | --- | -------------- | --- | ------------ |
disclosure
| —  Supply chain attacks |     | attacks |     |     |
| ----------------------- | --- | ------- | --- | --- |
—  Scam attacks on mobile consumers
Scams
Each of these areas includes a definition,  Mobile consumer
some indicators of compromise and
security mitigations to be developed,  Fragmented and fast-moving regulatory landscape
extended and implemented.
Figure 1, An Overview of topics
1  https://www.gsma.com/solutions-and-impact/technologies/security/publications/
GSMA Mobile Telecommunications Security Landscape - 2026 1/26

Executive Summary GSMA Mobile Telecommunications
Security Landscape - 2026
New for this year, the report includes approaches to vulnerability disclosure alongside a set of migration and other intelligence and strategic mapping, a
a threat actor analysis provided via the GSMA Co-ordinated Vulnerability practical factors to consider for PQC range of recommendations emerge and
from the perspective of the GSMA Disclosure scheme. transition. are described.
Telecommunications-Information
Sharing and Analysis Center (T-ISAC). The report moves on to analyse the The landscape is completed by examining Finally, the report identifies ten key
Any defensive strategy can benefit emerging security needs associated the fast-moving and often fragmented security protection priority areas derived
from understanding the likely attackers with generative and agentic artificial topic of global cybersecurity regulations. from the report content.
and their attack techniques, hence, the intelligence and considerations and To address the evolving threat landscape,
Sotware attacks
report identifies and discusses four migration for post quantum cryptography. national and international policy must
threat actor groups highly relevant to the In the past few years, effective adapt. Based on the synthesis of threat
mobile telecoms industry and provides Generative Artifical Intelligence (AI)
an analysis of the key attack tactics technology capabilities and availability
employed by these threat actors. have increased significantly enabling
a range of new uses for both offensive
The report moves on to consider strategic and defensive purposes with major
responses (see also the 2025 report2 for ramifications for mobile telecoms
an in-depth analysis of strategic security security. Agentic AI is characterised by
responses). A powerful strategic security autonomy and intent-driven decision-
response to a range of the attack types making to leverage workflows that
identified earlier is to utilise risk and decompose complex goals, iteratively
threat management to fully design and optimise actions, and actively adapt to
leverage valuable security investments. dynamic environments, positioning itself
The range, velocity and dynamics of as the cornerstone of next-generation
the current threat landscape make it digital infrastructure.
challenging to fully address every threat
in every dimension and the prioritised Post Quantum Cryptography (PQC) is a
impact of security interventions can be topic with some uncertainty on timing
maximised through a risk management but with potential for a significant
approach. A second part of the strategic security impact. A Cryptographically
defence approach involves threat and Relevant Quamtum Computer (CRQC)
vulnerability sharing (as exemplified by has the potential to break public key
GSMA’s T-ISAC service and included in infrastructures which underpin many
the Threat Actor section). Finally, another current security protocols including some
GSMA service where the mobile industry key distribution and digital signature
continues to strengthen its collective regimes. The report illustrates some
security posture is through structured of the important push and pull factors
2 https://www.gsma.com/solutions-and-impact/technologies/security/gsma-mobile-telecommunications-security-landscape-2025/
GSMA Mobile Telecommunications Security Landscape - 2026 2/26

Mobile networks, devices and GSMA Mobile Telecommunications
consumers are under attack Security Landscape - 2026
Mobile networks, devices and consumers are
2
under attack
The mobile industry has long aimed to develop and deploy robust security measures to protect its assets, customers and services.
GSMA continue to see attacks directly on mobile networks, services and devices, including attacks on service delivery, denial of
service, the delivery of malware and attacks seeking to exfiltrate data.
In mobile networks, a single breach can attack techniques to achieve their goals. Deutsche Telekom reported 70 million
disrupt infrastructure, customers, and After an initial phase of reconnaissance4, attacks per day7 on their ‘honeypot’
supply chains. There is a commonality the attack may move to establish an initial systems8 Virgin Media O2 has blocked
of attack tactics such as credential theft, access bridgehead. This initial access 1 billion scam text messages on its
token abuse, Software-as-a-Service phase may persist for months or years5, mobile network9. The attacks go beyond
(SaaS) exploitation, and living-off-the- with low levels of activity, occasionally network infrastructure, seeing attacks
land methods. This highlights the urgent contacting the Command and Control on mobile devices and directly against
need for tailored operational security, (C2) server, gathering information, our customers. Scam and fraud are
ongoing behavioural monitoring, robust exfiltrating low levels of data or waiting escalating at an alarming rate worldwide,
governance and underscores the for a better time to launch a more $1.4 trillion10 in global banking fraud
importance of flexible detection models destructive or impactful attack. Hence losses reported11. A massive smishing
and sector-specific expertise. the need for threat hunting6 activity. The campaign leveraging a reported12
techniques to establish this initial access 194,000 domains.
The operational attack surface is wide can utilise simple, well-known attack
and complex. Attacks can be launched tools exploiting known vulnerabilities.
at many different points externally and
from within the network. Mobile Network To give a sense of scale, UK operator BT
Operators (MNOs) have been targeted for reported detecting 2,000 potential attack
many years and these attacks continued signals per second across its network,
in 20253. Threat actors use a range of equating to 200 million per day whilst
3 https://techcrunch.com/2025/05/08/a-timeline-of-south-korean-telco-giant-skts-data-breach/ 6 https://www.gsma.com/solutions-and-impact/technologies/security/latest-news/mobile-telecom-security-landscape-blog-november-24/
3 https://corporate.orange.be/en/node/57971 7 https://business.bt.com/content/dam/bt-business/pdfs/insights/cyber-agility/the-cyber-agile-organisation-report-for-uk-market.pdf
3 https://www.theregister.com/2024/06/21/optus_data_breach_faulty_api/ 8 https://report.telekom.com/cr-report/2024/governance/cybersecurity-and-data-protection.html
3 https://therecord.media/luxembourg-telecom-outage-reported-cyberattack-huawei-tech 9 https://news.virginmediao2.co.uk/virgin-media-o2-blocks-1-billion-scam-text-messages-on-its-mobile-network/
3 https://www.infosecurity-magazine.com/news/bouygues-telecom-breach-customer/ 10 https://www.biometricupdate.com/202510/scams-overtake-1-trillion-as-ai-supercharges-global-fraud-networks-biocatch
3 https://www.bleepingcomputer.com/news/security/telefonica-confirms-internal-ticketing-system-breach-after-data-leak/ 11 https://www.gsma.com/solutions-and-impact/technologies/security/scams/gsma_study/airtel-spam-detection-solution/
3 https://m-en.yna.co.kr/view/AEN20251106006051320 12 https://unit42.paloaltonetworks.com/global-smishing-campaign/
3 https://techcrunch.com/2025/10/28/lg-uplus-is-latest-south-korean-telco-to-confirm-cybersecurity-incident/
4 https://www.gsma.com/solutions-and-impact/technologies/security/latest-news/mobile-telecom-security-landscape-blog-october-24/
5 https://www.reuters.com/business/media-telecom/us-company-with-access-biggest-telecom-firms-uncovers-breach-by-
nation-state-2025-10-29/
GSMA Mobile Telecommunications Security Landscape - 2026 3/26

|     |     | Mobile networks, devices and  | GSMA Mobile Telecommunications   |     |
| --- | --- | ----------------------------- | -------------------------------- | --- |
|     |     | consumers are under attack    | Security Landscape - 2026        |     |
An analysis of these reported attacks
identifies several important areas, that
are identified below and expanded upon
in later sections:
—  The importance of software security
—
A democratisation of attack tools
—  Successful pre-positioning attacks Successful
Sotware attacks Democratisation   pre-positioning  Exploiting weak  Supply chain  Scams
|     | of attacks | cyber hygiene | attacks |     |
| --- | ---------- | ------------- | ------- | --- |
—  Exploiting weak cyber hygiene attacks
—
Supply chain attacks
—  A spectrum of attacks: security,
  fraud and scams Spectrum of attacks
| Mobile  |     | Mobile  |     | Mobile   |
| ------- | --- | ------- | --- | -------- |
| network |     | device  |     | consumer |
Figure 2, A spectrum of attacks
GSMA Mobile Telecommunications Security Landscape - 2026 4/26

Mobile networks, devices and  GSMA Mobile Telecommunications
consumers are under attack Security Landscape - 2026
2.1 Software Attacks
| A software attack is a malicious attempt  | There are a number of indicators of  |     |
| ----------------------------------------- | ------------------------------------ | --- |
to gain unauthorised access to a  software compromise, notably system  SOFTWARE ATTACKS
| computer system or network by exploiting  | crashes or degraded performance, audits  |     |
| ----------------------------------------- | ---------------------------------------- | --- |
| vulnerabilities in code. Deficiencies in  | of code composition and code hashes      |     |
Attack surface
| coding implementations lead to potential  | to verify deployed code, system crashes  | DEFINITION |
| ----------------------------------------- | ---------------------------------------- | ---------- |
| vulnerabilities that attackers may seek   | and API errors / error logs.             |            |
to exploit (as demonstrated in the  —  A malicious attempt to gain unauthorised access
  to a computer system or network by exploiting
| later sections of this report and in this  | Secure-by-design software has  |     |
| ------------------------------------------ | ------------------------------ | --- |
  vulnerabilities in software code
| subsection).                               | been important for many years, and       |                          |
| ------------------------------------------ | ---------------------------------------- | ------------------------ |
|                                            | guidance is being refreshed17 and has    | INDICATORS OF COMPROMISE |
| A robust software development lifecycle13  | identified so-called unforgiveable code  |                          |
—  Unusual or unauthorised software installations
| is fundamental to quality code creation  | vulnerabilities18. Secure use of third-party  |     |
| ---------------------------------------- | --------------------------------------------- | --- |
—  API overloads / data leaks
| and some aspects of this process are  | software components is an important  |     |
| ------------------------------------- | ------------------------------------ | --- |
—  Unexpected configuration changes
| susceptible to attack / compromise.  | area19 including the protection20 and  |     |
| ------------------------------------ | -------------------------------------- | --- |
—  System crashes or degraded performance
Threat actors have been observed  tracking of code repositories. A thorough  —  Unexpected new code libraries or binaries
abusing legitimate tooling and functions  understanding of the composition of  —  Lateral movement activity
| such as software code repositories14  | deployed code is vital, eg by using a  |     |
| ------------------------------------- | -------------------------------------- | --- |
MITIGATIONS
| (including open-source repositories),  | Software Bill of Materials (SBOM) and     |     |
| -------------------------------------- | ----------------------------------------- | --- |
| open-source software attacks15 and     | code equivalence including code signing.  |     |
—  Secure by design code development lifecycle
abuse of Application Programming  Guidance and best practices for API  —  Being fully aware of code composition, eg by
| Interfaces (API) (an important set of  | security21 are also being updated.  |     using an SBOM |
| -------------------------------------- | ----------------------------------- | ----------------- |
—
functionality for telecom networks)16.    Manage security of code repositories
—  Adopt security best practices for API
APIs extend the potential attack surface
  development security
and can provide access to powerful
—  Use of privileged access workstations and
  utilising the principle of least privilege.
capabilities and data.
13 https://www.gsma.com/solutions-and-impact/technologies/security/supply-chain-toolbox/
14  https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/ongoing-targeting-of-online-code-repositories
15 https://unit42.paloaltonetworks.com/npm-supply-chain-attack/
16  https://www.nccgroup.com/why-api-security-is-now-a-non-negotiable-for-the-telecommunications-sector/
17  https://www.cisecurity.org/insights/white-papers/secure-by-design
18  https://www.ncsc.gov.uk/report/a-method-to-assess-forgivable-vs-unforgivable-vulnerabilities
19  https://safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf
20  https://www.ncsc.gov.uk/collection/developers-collection/principles/protect-your-code-repository
21  https://www.nccgroup.com/why-api-security-is-now-a-non-negotiable-for-the-telecommunications-sector/ & https://www.ncsc.gov.uk/blog-post/new-guidance-on-securing-http-based-apis
GSMA Mobile Telecommunications Security Landscape - 2026 5/26

Mobile networks, devices and GSMA Mobile Telecommunications
consumers are under attack Security Landscape - 2026
2.2 Democratisation of Attacks
Should simple attack tools prove — Ransomware / phishing / cybercrime to your network and sell them to DEMOCRATISATION
ineffective, threat actors may seek to / malware as-a-service – where other TAs29 OF ATTACKS
use more innovative and complex attack as-a-service providers offer attack
— Artificial Intelligence (AI)-enabled
techniques. There are a set of barriers to tools in a commodity fashion, e.g.
attack efficiency gains - AI can DEFINITION
using these more complex capabilities simplifying the technical aspects of a
automate various stages of an
including requiring higher skill levels and ransomware attack25 — The widespread and relatively low-barrier use
attack, such as reconnaissance,
experience, higher costs, more resources of security attack tools
— An evolution of smishing26 including vulnerability scanning, and data
and can be challenging and expensive
utilising a decentralised Phishing- analysis, which previously required INDICATORS OF COMPROMISE
to achieve. However, there has been a
as-a-Service (PhaaS) model, rapidly significant human expertise
progressive lowering of skill and resource rotating domains to attempt to evade — Increased use of common security tools
levels required to launch effective attacks — AI-generated phishing and social — Rise in attacks using off-the-shelf malware
detection. This can take differing
establishing a relatively low-barrier to the engineering - generative AI can — More breaches by less sophisticated actors
forms including ‘fast flux’27 and
use of security attack tools. A range of produce convincing and — Increasing bypass of SMS firewalls
domain generation algorithms28 — Customers clicking on known scam links
approaches have been evidenced: personalised phishing emails, text
— Botnets-for-hire - access to large messages, and social media posts
MITIGATIONS
— SMS Blasters22 - An SMS text blast networks of compromised
sends a message to a large group computers to launch large-scale — Patching
Mitigation approaches can aim to
of people simultaneously. However, attacks like Distributed Denial-of- — GSMA FS.31 Baseline controls and
relatively low-cost, portable and Service (DDoS) attacks for a fee just make it harder for the attacker — MCKB
by implementing more security best — Threat hunting,
easy-to-use fake mobile base
— Dark web marketplaces - that practice capabilities such as those — SMS Blaster guidance FS.67
transceiver stations (SMS blasters) operate like legitimate e-commerce contained in GSMA FS.31 Baseline — A ‘top 20’ strategic security approaches including
can be used for fraudulent use23 know your attack surface, defensive force
to send a localised smishing ‘blast’ sites, offer a wide array of hacking Controls30, guidelines in the GSMA multipliers, layered defences, supply chain
tools, exploit kits, and stolen Mobile Cybersecurity Knowledge Base31, security, resilience-by-design, risk management,
that can bypass SMS firewall tools. use of privileged access workstations and
credentials implementing threat hunting and a top 20
SMS blasters are being increasingly utilising the principle of least privilege.
strategic security approaches32.
evidenced across the globe24 — Initial access brokers - threat actors
(TAs) who seek to procure access
22 https://www.gsma.com/newsroom/press-release/gsma-asia-pacific-mobile-industry-taskforce-calls-for-government-and-law-enforcement-support-to-stamp-out-sms-blaster-device-threat/
23 https://commsrisk.com/criminal-gangs-drive-imsi-catcher-sms-blasters-around-vietnam/
24 https://news.risky.biz/risky-bulletin-sms-blasting-incidents-are-rising/
25 https://www.crowdstrike.com/cybersecurity-101/ransomware/ransomware-as-a-service-raas/
26 https://www.securityweek.com/massive-china-linked-smishing-campaign-leveraged-194000-domains/
27 https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-093a
28 https://www.akamai.com/glossary/what-are-dgas
29 https://www.cisecurity.org/insights/blog/initial-access-brokers-how-theyre-changing-cybercrime
30 https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/fs-31-gsma-baseline-security-controls/
31 https://www.gsma.com/solutions-and-impact/technologies/security/cybersecurity-knowledge-base/
32 https://www.gsma.com/solutions-and-impact/technologies/security/latest-news/mobile-telecom-security-landscape-blog-july-25/
GSMA Mobile Telecommunications Security Landscape - 2026 6/26

Mobile networks, devices and GSMA Mobile Telecommunications
consumers are under attack Security Landscape - 2026
2.3 Successful Pre-Positioning Attacks
Reactive security defences play a huge of an attacker’s lateral movement through — Proactive penetration testing can be
PRE-POSITIONING ATTACKS
role in delivering safe and resilient the network, identifies unauthorised an additional tool with which to
networks. However, the reported attacks privilege escalation, access rights abuse, identify potential initial attack
include those with a successful launch and other threats. vectors and existing weaknesses
DEFINITION
and utilisation of pre-positioning attacks
where an adversary compromises Some regulations are pushing operators — An adversary compromises systems now and
systems now and persists to prepare for to establish the principle of ‘assumed persists there to prepare for a later escalation or
low-level data exfiltration and ‘beaconing’
a later escalation or undertake ongoing compromise’ whereby operators should
low-level data exfiltration and ‘beaconing’ normally assume network oversight
INDICATORS OF COMPROMISE
to C2 servers33. These ‘quiet’ attacks functions to be subject to high-end
may have been missed by defence attacks, which may not have been — Unusual traffic flows and account usage
capabilities or may have existed prior detected, and implement business — Unusual persistent accounts or tasks
— Unexplained network traffic such as low-level
to defence upgrades. While reactive practices that make it harder for an
outgoing beaconing, sometimes over a protracted
security defences can deliver safe and attacker to maintain covert access. period
resilient networks, they occasionally Mitigation activities include: — Unexplained changes in software
miss successful attacks that seek to
pre-position a persistent ‘bridgehead’ — Threat hunting MITIGATIONS
from which to assert cyber-attacks in a
— Implement trusted boot capabilities — Threat hunting
variety of forms. Ongoing threat actor — Secure roots of trust with periodic rebooting of
and secure roots of trust with
actions can utilise ‘living off the land’ 34 systems
techniques to attempt to evade detection. periodic rebooting of systems — Threat intel sharing
— Proactive penetration testing
Other IoCs include unusual traffic flows — The GSMA Telecommunication
and / or account usage, unexpected Information Sharing and
changes in software and unusual account Analysis Center37 (T-ISAC) is the
usage / time of usage (eg outside of central hub of information threat
normal office hours). sharing for the Telecommunication
Industry. Information threat
Proactive threat hunting35 plays a role sharing is essential for the protection
in uncovering these long-term attacks. of the mobile ecosystem
Threat hunting activity searches for signs
33 https://media.defense.gov/2025/Apr/02/2003681172/-1/-1/0/CSA-FAST-FLUX.PDF
34 https://securityboulevard.com/2025/05/living-off-the-land-lotl-attacks-how-your-tools-are-used-against-you
35 https://www.gsma.com/solutions-and-impact/technologies/security/latest-news/mobile-telecom-security-landscape-blog-november-24/
36 https://api.gcforum.org/api/files/public/upload/aa4aad66-74f7-4490-a4e6-f6d3f1e327bf_Enhancing-Protection.pdf
37 https://www.gsma.com/solutions-and-impact/technologies/security/t-isac/
GSMA Mobile Telecommunications Security Landscape - 2026 7/26

Mobile networks, devices and GSMA Mobile Telecommunications
consumers are under attack Security Landscape - 2026
2.4 Exploiting Weak Cyber Hygiene
Threat actors will use a range of Recent attacks illustrate some areas — Undertake a complete asset
CYBER HYGIENE
attack tools, often starting by using where cyber hygiene can be improved in inventory to understand the full
the most basic and readily available areas such as: attack surface40
toolsets that seek to exploit well-
— Understand the details of the supply DEFINITION
known vulnerabilities38 and these have — Improving user and administrator
chain (including third-party remote
been shown to be effective in recent account security including enabling — A practice of taking steps to protect devices,
system access arrangements). See
successful attacks. When these attack a multi-factor authentication (MFA) networks, and data from cyber threats
also, the later Supply Chain section
techniques fail, the adversary is forced arrangement and password storage
in this report INDICATORS OF COMPROMISE
to utilise more resources, expertise mechanisms
and effort to launch more sophisticated — Patching systems more frequently or — Implement a strong baseline set of — Unusual account activity
attacks. The role of the defender is controls41 — Unauthorised software
adding additional mitigating controls
to make attacks progressively harder — Unexpected configuration changes
to launch and achieve success. This to combat known vulnerabilities — build in multilayer defences for — Suspicious network traffic
strength and depth42
defensive strategy begins with effective — Monitoring and analysis of logging
MITIGATIONS
baseline security controls39. data and data flows to spot
suspicious traffic flows and ongoing/ — Patching or adding additional security controls
Indicators of compromise relating to previous attacks — Improving user and administrator account
poor cyber hygiene include unusual security
— Improving network and system — Monitoring and analysis of logging data and data
account activity, unexpected new
segmentation to make it harder flows
account accesses, unauthorised software — Improving network and system segmentation
for attackers to move laterally, re-use
packages and configuration changes, — Encrypting key data
credentials and limit the impact of
suspicious network traffic including data — GSMA FS.31 Baseline controls and GSMA MCKB
exfiltration (including low-level flows) and the attack — GSMA Supply Chain Toolkit
— Multilayer defences
data flows of unencrypted data. — Encrypt stored encryption keys and
sensitive data
38 https://www.cve.org/
39,40 https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/fs-31-gsma-baseline-security-controls/
41 https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/fs-31-gsma-baseline-security-controls/
42 https://www.rg-cs.co.uk/security-stop-press-cyber-criminals-exploit-trusted-platforms-in-lots-attacks/
GSMA Mobile Telecommunications Security Landscape - 2026 8/26

Mobile networks, devices and GSMA Mobile Telecommunications
consumers are under attack Security Landscape - 2026
2.5 Supply Chain Attacks
Supply chain attacks continue at The concept of ‘know your traffic’ is security assurance. The purpose of
pace43. The opportunity for indirect a powerful one whereby monitoring the scheme is to audit and test network SUPPLY CHAIN ATTACKS
attacks through supplier or third-party and understanding all network traffic equipment vendors, and their products,
tooling and services should not be is undertaken to identify, mitigate, and against a security baseline, so they can
Supply chain
underestimated and requires vigilance prevent security threats and fraud. demonstrate to network operators (or DEFINITION
about which third-party tools are in use, regulators) that they are conforming to
as well as awareness of the security Supply chain interventions throughout the the desired standard. The scheme — A type of cyber or operational attack where an
attacker compromises telecommunications
posture of the various third parties. lifecycle can: has been defined by industry experts
systems or services by exploiting weaknesses
Perhaps a less obvious supply chain through GSMA, 3GPP, ETSI and in the suppliers, vendors, or partners involved in
attack is ‘Living Off Trusted Sites’ — Inform of the strength of wider entities. GSMA NESAS only plays building, maintaining, or operating telecom
networks
44(LOTS). Where threat actors extend development processes one part of the security strategy. NESAS
their stealth techniques into the cloud, — Understand the adequacy of in-built only tests products and processes at a INDICATORS OF COMPROMISE
using trusted sites and legitimate services point in time. It is important to guarantee
security controls and assurances
to avoid detection and disguising C2 as that the actual deployed code is the — Disguised C2 traffic
ordinary traffic or innocuous messages — Be clear on the security of in-life same code that was tested through — Abnormal Routing Protocol Changes
— Spikes in DNS Query Volume
on platforms as such Slack and Telegram. security maintenance arrangements NESAS (so called binary equivalence)
— Privilege Escalation in Active Directory
Other indicators of compromise can — Improve the speed of response to and that secure configurations are used. — Abnormal Login Times
include abnormal login times (especially Additional layers of security are required — Unplanned software/ firmware updates
mitigate new security vulnerabilities
on administrator accounts), unusual to deliver a robust deployment for in- — Unauthorised Management Software
privilege escalation (including on — Ensure de-commissioning is service use. — Unexplained increases in database read volumes
Active Directory), unexplained software undertaken in a controlled and
MITIGATIONS
and firmware updates and increases secure manner To perform their contracted activities, a
in database read volumes that might managed service provider (MSP) must — Adopt a lifecycle approach to improve the whole
— Understand the depth46 of supply
indicate exfiltration attempts. administer their systems and services chain of supply and operation
chains and without proper controls, this high — Know your traffic- logging and monitoring of all
traffic types
There are a range of mitigating As part of supply chain assurance, GSMA level of privileged access, can leave a — Use industry security assurance schemes to
approaches including utilising the GSMA’s Network Equipment Security Assessment system vulnerable to attack. provide a security underpinning
updated and re-issued GSMA Supply Scheme (NESAS)47 exists to facilitate — Fully understand the depth of the supply chain
and the security processes of each vendor
Chain Toolbox45 that uses a lifecycle improvements in network equipment
— Actively manage code deployments and update to
model to describe a number of guidelines security levels, across the mobile ensure correct code versioning and binary
(‘tools’ in the ‘toolbox’). industry by providing an underpinning equivalence
— Strictly control remote access arrangements
43 https://unit42.paloaltonetworks.com/npm-supply-chain-attack/
44 https://www.rg-cs.co.uk/security-stop-press-cyber-criminals-exploit-trusted-platforms-in-lots-attacks/
45 https://www.gsma.com/solutions-and-impact/technologies/security/supply-chain-toolbox/
46 https://datatracker.ietf.org/doc/draft-ietf-scitt-architecture/
47 https://www.gsma.com/solutions-and-impact/industry-services/assurance-services/network-equipment-security-assurance-scheme-nesas/
GSMA Mobile Telecommunications Security Landscape - 2026 9/26

Mobile networks, devices and GSMA Mobile Telecommunications
consumers are under attack Security Landscape - 2026
It is important to identify which systems target supplier’s customers makes using
each MSP can access and what the a compromised vendor an attractive As architectures continue to move towards disaggregated
secure access mechanisms are. These proposition48. The potential attack force- components, leverage cloud and virtualisation architectures
accesses should only allow activities multiplier enabled through a supply chain
as well as increase in third party tools for monitoring,
that are within the contracted scope of attack means building skills, processes,
management and security, it is clear that the available
service provider activity. Segmentation tools and experience will present an
(to limit the scope for lateral movement), enduring benefit – supply chain security supply chain ‘surface area’ for an attacker to exploit is
least privilege (to decrease the impact a will remain a key security area. becoming broader.
malicious access account may have), use
of secure ‘jump’ boxes, use of dedicated
work stations, privileged access
management, multi-factor authentication,
attributable accounts and’ just in time’
principles and limited duration access for
privileged accounts can all be effective
controls. The secure separation of
privileged access workstations47 used by
systems administrators is a key area of
supply chain security.
As architectures continue to move
towards disaggregated components,
leverage cloud and virtualisation
architectures as well as increase in third
party tools for monitoring, management
and security, it is clear that the available
supply chain ‘surface area’ for an
attacker to exploit is becoming broader.
Active and in-depth knowledge of direct,
indirect and open-source supply routes
are all needed. The force multiplier effect
for an attacker of a single successful
attack providing access across all the
47 https://www.gsma.com/solutions-and-impact/technologies/security/latest-news/mobile-telecom-security-landscape-blog-june-25/
48 https://tuxcare.com/blog/xz-compromise/
GSMA Mobile Telecommunications Security Landscape - 2026 10/26

Mobile networks, devices and  GSMA Mobile Telecommunications
consumers are under attack Security Landscape - 2026
2.6 The Spectrum: Security, Fruad, Scams
Scams fall into a spectrum of  innovative concepts, including Open  including the ability to disable 2G  of scam prevention resources to provide
differing attack types, including  Verified Calling, and implement new  connectivity (a route for smishing attacks).   the industry guidance, intelligence and
those focussed on attacking  solutions, like the Scam Signal API50, that    education tools and the document Fraud
network infrastructure and services,  directly target scams.  The mobile industry is taking  and Scams: Staying Safe in the Mobile
those seeking to defraud operators by  comprehensive steps to combat the rising  World 55. Only by uniting and working
abusing services and accounts, and  The importance of mobile operators  number of scams that affect individuals  together can the global mobile industry
those seeking to scam mobile users  taking scam prevention seriously is clear.  and society, and to improve trust in global  and the wider ecosystem collectively
directly. The scam economy has  For example, Bharti Airtel’s network-based  mobile networking. Additional information  tackle this issue to safeguard consumers
grown rapidly over the last five years,  AI-powered Spam detection solution51 has  can also be found in the GSMA scams  and ensure a secure future for all.
surpassing the illegal drug trade and  resulted in a reduction in financial losses  content hub54 that shares a wide range
| costing victims $1 trillion worldwide49.  | for its customers of nearly 70% - a 14.3%  |     |
| ----------------------------------------- | ------------------------------------------ | --- |
|                                           | drop in overall cybercrime incidents on    |     |
 Human and financial cost
| Users of mobile technologies are targeted  | the Airtel network (also rolled rolled out  |     |
| ------------------------------------------ | ------------------------------------------- | --- |
by a variety of actors – whether it be  to Nigeria, Uganda,Tanzani and Rwanda).  GLOBALLY 63 OFSOUTH EAST ASIANS
57OFADULTS
HAVE HAD
low-level fraud via phishing, smishing,  TPG Telecom52 partnered with Apate.ai  % ASCAM EXPERIENCEIN THE %EXPERIENCEDSCAMSIN THEPAST YEAR
| or through social engineering against  | to pilot a proactive, intelligence-driven  |     |
| -------------------------------------- | ------------------------------------------ | --- |
LAST12MONTHS
| them, or call centres. Scams and fraud   | defence against scam calls. The program   |     |
| ---------------------------------------- | ----------------------------------------- | --- |
| can take many forms, and some of         | was designed not just to block malicious  |     |
| these exploit mobile devices themselves  | calls, but to divert them into a secure   |     |
 Political Support UN INTERPOL
and their supporting service as an  environment where valuable threat data  TO HOST
MINISTERIAL SCAM CONFERENCE
attack channel. These include attacks  could be gathered and used to strengthen  INTERNATIONAL
such as service fraud (e.g. identity  protection. The collaboration delivered  INVIENNAMARCH2026
| fraud or mobile money fraud), mobile     | its goal resulting in 280,000+ scam       |     |
| ---------------------------------------- | ----------------------------------------- | --- |
| spam and, increasingly scams or “social  | calls successfully diverted from the TPG  |     |
| engineering” fraud, which trick victims  | Telecom network and $7.6 million+ in      | 97  |
REDUCTION  Regulatory support
| into revealing sensitive information  | estimated scam losses prevented.   |     |
| ------------------------------------- | ---------------------------------- | --- |
%INSPOOFED CALLS
about themselves and the services they  Anti-scam measures are increasingly  REPORTED INNEW DELHI DUE TOGOVERNMENT’S
consume, without realising they have  being provided on-device53 as well as  ANTI-FRAUD INITIATIVE
| compromised their own security.   | within the network. The range of new  |     |
| --------------------------------- | ------------------------------------- | --- |
GSMA are working closely to test  operating system capabilities is extensive,  *Sources:  1 – link; 2 – link; 3 – link; 4 – link; 5 – link; 6 – Global State of Scams 2025 Report, Global Anti Scam Alliance;
  7 – UK Home Office; 8 – link; 9 – link; 10– link; 11 – link
49 https://www.biometricupdate.com/202510/scams-overtake-1-trillion-as-ai-supercharges-global-fraud-networks-biocatch
50 https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma_study/vodafone-implements-scam-signal-api-to-combat-fraud/
51 https://www.gsma.com/solutions-and-impact/technologies/security/scams/gsma_study/airtel-spam-detection-solution/
52 https://www.gsma.com/solutions-and-impact/technologies/security/scams/gsma_study/apate-ai-powered-scam-detection-diversion-and-real-time-threat-intelligence/
53 https://safety.google/intl/en-GB_ALL/safety/scams-fraud/
53 https://www.huaweicentral.com/android-16-will-modify-call-settings-to-safeguard-you-from-scammers/,
53 https://www.samsung.com/us/support/answer/ANS10003438/ & https://support.apple.com/en-gb/guide/iphone/iphe4b3f7823/ios
54 https://www.gsma.com/solutions-and-impact/technologies/security/scams/
55 https://www.gsma.com/solutions-and-impact/connectivity-for-good/public-policy/gsma_resources/fraud-and-scams-staying-safe-in-a-digital-world/

GSMA Mobile Telecommunications Security Landscape - 2026 11/26

Threat Actors GSMA Mobile Telecommunications
Security Landscape - 2026
3 Threat Actors
In today’s digital landscape, organisations and individuals encounter ongoing risks from threat actors. Gaining a comprehensive
understanding of these actors, the specific threats they present, and identifying which threat actors are most relevant to the mobile
industry is crucial for enhancing cybersecurity defences. GSMA’s Telecommunications Information Sharing and Analysis Center has
been tracking a range of threat actors, and some are described below, along with an analysis of their attack techniques.
What is a Threat Actor? Salt Typhoon While much of the public reporting has The adversary implements operations
focused on U.S. targets, Salt Typhoon’s security (OPSEC) measures to hide
Any person, group, or entity56 that Salt Typhoon AKA UNC2286 has been operations have extended into Canada, these connections from investigators
intentionally uses computers, networks, active from at least 2019, the group has Europe, the Middle East, and Africa by tampering with legitimate binaries on
or systems to cause harm to others. conducted extensive cyber-espionage (EMEA) where it has targeted telecoms, target systems. Once they gain access
This is often achieved by exploiting campaigns, particularly targeting government entities, and technology to a network, they establish multiple
vulnerabilities to steal data, disrupt telecommunications infrastructure, firms60. redundant remote access mechanisms
services, or achieve financial, political, energy networks and government using a combination of custom backdoors
or ideological goals. These actors are systems worldwide. The analysis from a LightBasin and publicly available proxy tools
also known as malicious actors or bad CISA report57 on Salt Typhoon confirms configured to relay traffic to adversary-
actors and can range from individual the group exploits known vulnerabilities The threat actor LightBasin, also known controlled remote infrastructure61.
cybercriminals and hacktivists to in backbone, customer edge and as UNC1945 + UNC281 is a cyber Since 201662, they have contributed to
state-sponsored organizations and provider-edge routers to gain access, espionage group. They focus on targeting malware that has affected 13 different
even insiders within an organisation. create privileged accounts, and maintain telecommunications, finance, retail and telecommunication businesses across the
It is crucial for the telecommunications persistent network access, allowing hospitality and health care industries. globe63.
industry to be aware of the threat interception of communications and Their primary focus is targeting Linux
actors referenced in this report. They manipulation of network configurations. and Solaris based systems using
exemplify the most advanced, persistent, All this is achieved by leveraging various tactics by leveraging their
and impactful cyber threats targeting zero-day exploits, lateral movement and in-depth knowledge of the telco network
telecommunications globally, each with living on the land58 to stay undetected for architecture.
distinct motives and tactics that have extended periods of time59.
dramatically shaped the threat landscape
in recent years.
56 https://www.cisa.gov/sites/default/files/2025-09/CSA_COUNTERING_CHINA_STATE_ACTORS_COMPROMISE_OF_NETWORKS.pdf
57 https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
58 https://blog.talosintelligence.com/salt-typhoon-analysis/
59 https://docbox.etsi.org/Workshop/2025/10_SECURITY_CONFERENCE/9OCTOBER/GEOPOLITICS/BLUEHOUR_Holtmanns.pdf
60 https://www.darktrace.com/blog/salty-much-darktraces-view-on-a-recent-salt-typhoon-intrusion
61 https://www.crowdstrike.com/en-us/blog/an-analysis-of-lightbasin-telecommunications-attacks/
62 https://www.techtarget.com/searchsecurity/news/252508413/LightBasin-hackers-spent-5-years-hiding-on-telco-networks
63 https://www.bleepingcomputer.com/news/security/lightbasin-hacking-group-breaches-13-global-telecoms-in-two-years/
GSMA Mobile Telecommunications Security Landscape - 2026 12/26

Threat Actors GSMA Mobile Telecommunications
Security Landscape - 2026
Scattered Spider ShinyHunters
Since they are English
Scattered Spider, (also known as ShinyHunters, is another financially
speaking individuals, they
UNC3944 & Octo Tempest) is a financially motivated group that are linked to
have successfully adopted
motivated cybercriminal group. Unlike the threat actor cluster UNC6040 by
many other threat groups, Scattered Google.64 The name is inspired by the vishing (voice phishing) as a
Spider is believed to be composed Pokémon community term for rare social engineering technique.
of relatively young, English-speaking “shiny” creatures, reflecting the group’s
members based in Western countries. pursuit of high-value data.65 This group
They engage in data extortion by specialises in data theft, extortion, and
leveraging personal information gathered the leaking of sensitive information.
through open-source intelligence (OSINT) In their most recent attacks, they
or prior breaches. The adversary uses gained access through credential theft,
multiple social engineering techniques phishing, or exploiting misconfigured
SIM Swap attacks to obtain to obtain cloud services like exposed S3 buckets
credentials, install remote access tools, or unsecured GitHub repositories. Since
and/or bypass MFA. Scattered Spider use they are English speaking individuals,
social engineering to convince support they have successfully adopted
staff to reset passwords or enrol new vishing (voice phishing) as a social
MFA devices, effectively bypassing engineering technique. ShinyHunters
security controls. Additionally, they have also impersonate IT Support/help desk
used SIM swapping to hijack victims’ and trick employees into authorising
phone numbers and intercept MFA malicious connected apps in platforms
codes. They have also employed MFA like Salesforce, giving them direct access
fatigue attacks, repeatedly sending push to customer data via APIs.
notifications to users in they hope that
they’ll eventually approve the request
out of frustration or confusion. Scattered
Spider has targeted the Retail, Hospitality,
Banking Sector and Telecommunications
Industries.
64 https://cloud.google.com/blog/topics/threat-intelligence/unc6040-proactive-hardening-recommendations
65 https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion
GSMA Mobile Telecommunications Security Landscape - 2026 13/26

Threat Actors GSMA Mobile Telecommunications
Security Landscape - 2026
Modus Operandi of the Threat Actors cloud/Virtual Private Server (VPS)
infrastructure to obscure
Salt Typhoon, Scattered Spider, operator location and infrastructure
ShinyHunters, and LightBasin are lineage throughout campaigns. Threat Actors
prominent modern cyber adversaries with
overlapping advanced TTP’s (tactics, — Persistence primarily via valid Salt Scattered ShinyHunters/
accounts, longlived sessions, LightBasin Typhoon Spider UNC5537
techniques and procedures).
and legitimate services or
Impact
— Abuse of valid accounts and the scheduled tasks rather than heavy
custom implants.
identity plane across enterprise, Exfiltration
telecom, and cloud/SaaS
environments, preferring logins with Figure 3: Shows the tactics used by the Command & Control
stolen or purchased credentials over Threat Actor using the MITRE ATT&CK®
exploit heavy intrusion paths. adversary tactics framework66. Lateral Movement
— Bypassing strong authentication Discovery
Mobile operators can prioritise strong
through MFA gaps and session/token
identity controls, have clear asset
reuse, including opportunistic social Credential Access
visibility, well-rehearsed incident
engineering where feasible to regain
responses, ensure multi-factor
access quickly. Defense Evasion
authentication is enforced for all
— Living off the land with native admin privileged and remote accesses, that Privilege Escalation
tools and builtin platform passwords are never stored in plaintext,
functionality (PowerShell, WMI, and privileged accounts are audited Persistence
RMM, SQL queries/exports) to blend regularly. Network segmentation and
with normal IT operations and reduce continuous monitoring of logs can be Execution
malware footprints. used to detect lateral movement early
— Systematic discovery to map and ensure there are clear processes Initial Access
for change management and supplier
networks, services, and cloud
oversight. GSMA’s T-ISAC community
metadata, identifying high value
enables the mobile industry to share new
datasets and accessible routes
IoCs in near real-time. This intelligence
before deeper actions.
sharing can also include details of
— Largescale data theft using native detection methods and feedback on Figure 3, Tactics used by the Threat Actors
export mechanisms and web effective defensive controls. In this
services, especially from cloud data way, many operators can share from
warehouses and SaaS platforms the learning of a few operators or even
where controls are weaker or a single operator. This defensive force-
misconfigured. multiplier can be delivered by promptly
sharing knowledge and information
— Operational security with commercial 66 https://attack.mitre.org/tactics/enterprise/
that can benefit the wider range of
VPNs, proxies, and commodity
stakeholders.
GSMA Mobile Telecommunications Security Landscape - 2026 1144//2266

Risk Management GSMA Mobile Telecommunications
Security Landscape - 2026
4 Risk Management
A powerful strategic security response to a range of the attack types identified earlier is to utilise risk and threat management to
fully design and leverage security investments. The range, velocity and dynamics of the current threat landscape make it
challenging to fully address every threat in every dimension and the prioritised impact of security interventions can be maximised
through a risk management approach.
Threat and risk assessment allows system or application. Threat modelling
identification of the most likely and aims to identify and mitigate security
impactful risks considering the technical vulnerabilities.
security threats to which the business
may be exposed given its architectural There are many different risk and threat
design, legacy network estate, supplier modelling approaches used within a telco
selection, enabling technologies, environment including:
operation and support arrangements,
and software builds, etc. By focusing on — Attack Trees67
the areas of threat/risk, a business can
— GSMA risk identification reports
examine the gross risk likelihood and
such as GSMA documents GSMA
impact. Then, considering the effect
PQTN PQ.02 - Guidelines for
of existing controls and mitigations, a
Quantum Risk Management for
net risk position can be determined.
Telco68 and member-only documents
A review of this net risk position can
such as FS.30 Security Manual &
assess whether the risk profile is within
FS.39 5G Fraud Risks
the company risk tolerance or whether
additional controls and mitigation activity — NIST Artificial Intelligence Risk
is required to further reduce the net risk Management Framework (AI RMF
position. 1.0)69
— NIST Cybersecurity Supply Chain
Threat intelligence-informed modelling
Risk Management Practices for
focuses specifically on security threats
Systems and Organizations70
(that might compromise confidentiality,
integrity and / or availability (CIA)) to a
67 https://2t-security.com/why-should-i-use-attack-trees/
68 https://www.gsma.com/get-involved/working-groups/wp-content/uploads/2023/09/Guidelines-for-Quantum-Risk-Management-for-Telco-v1.0.pdf
69 https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
70 https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1-upd1.pdf
GSMA Mobile Telecommunications Security Landscape - 2026 15/26

Risk Management GSMA Mobile Telecommunications
Security Landscape - 2026
| UK’s NCSC has published a report71      | designs and implementations can enable    |     |
| --------------------------------------- | ----------------------------------------- | --- |
| examining the systematic analysis of a  | better preparation and delivery response  |     |
Identify risk /
telecoms network from an attack tree  to possible step changes in the threat  vulterability
| perspective. The idea being to identify  | landscape. |     |
| ---------------------------------------- | ---------- | --- |
possible attack approaches from an
| attacker perspective and then break  | Undertaking a comprehensive threat  |     |
| ------------------------------------ | ----------------------------------- | --- |
these down into different categories of  and risk assessment can improve  Verify investment  Evidence the
through testing weakness
| attack type which can then be considered   | security through focusing on the most     |     |
| ------------------------------------------ | ----------------------------------------- | --- |
| against the effects of existing controls.  | impactful risk areas, maximising returns  |     |
| The approach began by drawing upon         | on security investments, identifying      |     |
| existing threat and attack data, global    | duplicate controls and identifying        |     |
| attacks on telecoms systems, practical     | new risk areas. Consider developing       |     |
Risk
industry security practitioner input and  in-depth expertise, tools and expertise  Management Cycle
international security standards. From  in a risk / threat framework that works  Quantify the
Deliver
this data, a series of attacks was pulled  for your environment. The aim is to  exposure &
improvements likelyhood
| together into ‘attack trees’. Each attack    | apply knowledge from risk insights       |     |
| -------------------------------------------- | ---------------------------------------- | --- |
| tree was considered for their relative       | to provide impactful multi-layered       |     |
| risk of success and likelihood. From this    | defensive technologies. The GSMA         |     |
| analysis, the most important risks can be    | Mobile Cybersecurity Knowledge Base73    |     |
| listed. Security controls and mitigations    | (MCKB) has been updated to add links     |     |
| can then be considered in order that the     | to additional security guidance and now  |     |
| net risk position is at an acceptable level  | features a section dedicated to risk     |     |
Communicate the  Scope a response
| for the business.  | management. | programme |
| ------------------ | ----------- | --------- |
approach

A related topic explored in the 2025  Some risk treatment options are:
mobile security landscape report72
— Accept the net risk position
is resilience-by-design. This plays to
— Sharing the risk through a new delivery arrangement
the categories of risk that have high
— Avoid the risk, e.g. by closing a platform, system or access
impact, but potentially are less likely;
so called ‘black swan’ events. This  — Transfer the risk to another party, perhaps through a
philosophy requires changing some    revised supply arrangement
design and planning assumptions and
— Risk education through implementing additional security
  controls/architectural re-design to limit the impact and/or
then developing and deploying networks
  reduce the likelihood of a successful attack
in accordance with these revised
assumptions. With far-sighted design
assumptions, network and service
Figure 4, A Risk Management Cycle
71 https://www.ncsc.gov.uk/files/Summary%20of%20the%20NCSCs%20security%20analysis%20for%20the%20UK%20telecoms%20sector.pdf
72 See p11 of https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/gsma-mobile-telecommunications-security-landscape-2024/
73 https://www.gsma.com/solutions-and-impact/technologies/security/cybersecurity-knowledge-base/

GSMA Mobile Telecommunications Security Landscape - 2026 1166//2266

Coordinated Vulnerability GSMA Mobile Telecommunications
Disclosure Security Landscape - 2026
5 Coordinated Vulnerability Disclosure
Another part of the strategic defence approach involves threat and vulnerability sharing (as exemplified by GSMA’s T-ISAC service
(see earlier Threat Actors section). Another service whereby the mobile industry continues to strengthen its collective security
posture through structured approaches to vulnerability disclosure.
The GSMA’s Coordinated Vulnerability The GSMA CVD programme, established
Disclosure (CVD) Programme provides in 2017, has handled over one hundred
a trusted framework for security disclosures to date. In 2025 alone, GSMA
researchers, vendors, and operators received 15 CVD cases, covering areas
to report and remediate vulnerabilities. such as 5G Standalone (SA), Access
GSMA’s CVD programme primarily Control, and eSIM. Mobile security
assesses vulnerabilities that relate to researchers to submit their vulnerability 16 16 16
telecoms standards functionality rather disclosures to the programme74.
14 15
than IT level or vendor specific issues.
By acting as a neutral coordination body,
the GSMA helps ensure that discovered 11
10
weaknesses are responsibly disclosed,
assessed, and addressed before they can 8
7
be exploited, thereby reducing risk across
the entire mobile ecosystem. This is made
possible by 25 volunteers from GSMA
MNO and vendor members, who form the
expert panel supporting the programme
2017 2018 2019 2020 2021 2022 2023 2024 2025
Figure 5, Number of GSMA CVD
Disclousers per year
74 https://www.gsma.com/solutions-and-impact/technologies/security/cvd-submit-a-vulnerability/
GSMA Mobile Telecommunications Security Landscape - 2026 17/26

Coordinated Vulnerability  GSMA Mobile Telecommunications
Disclosure Security Landscape - 2026
| In addition to the GSMA initiative, other  | Networks (RAN) are a key area due to  |     |
| ------------------------------------------ | ------------------------------------- | --- |
| industry-driven disclosure frameworks      | their reliance on less secure legacy  |     |
Breakdown of cases across network areas
| play an important role in raising security  | technologies and the complexity of      |     |
| ------------------------------------------- | --------------------------------------- | --- |
| maturity. For example:                      | RAN protocols can increase the risk of  |     |
insecure implementations.
1% 1%
—  CERTs and national disclosure
  programmes provide structured   Taken together, these initiatives reflect  3%
5%
|   channels for vulnerability reporting   | a growing culture of transparency and  |     |
| ---------------------------------------- | -------------------------------------- | --- |
7% RAN
|   that span multiple sectors, including   | collaboration in the mobile industry.  |     |
| ----------------------------------------- | -------------------------------------- | --- |
Supply chain
|   mobile. | By embedding coordinated disclosure  | Core |
| --------- | ------------------------------------ | ---- |
36%
practices at both the industry-wide and
| —  Standards and specifications   |     | UE  |
| --------------------------------- | --- | --- |
individual company levels, stakeholders  7%
Transmission
  organisation programmes such as
are better positioned to respond to
|   ETSI and 3GPP provide an avenue   |     | Roaming |
| ----------------------------------- | --- | ------- |
emerging threats, safeguard users, and
  for researchers to report
|     | build trust in mobile technologies. | Cryptography |
| --- | ----------------------------------- | ------------ |
  vulnerabilities affecting their relevant
13%
|   standards or specifications. |     | UICC |
| ------------------------------ | --- | ---- |
IoT
—  Device and platform providers
|   maintain robust vulnerability reward   |     | RCS |
| ---------------------------------------- | --- | --- |
  programmes and bug bounty
16%
  schemes, incentivising proactive   27%
  researcher participation.
—  Telecom operators and equipment
  vendors increasingly run their own
  disclosure channels, often aligned
  with international best practices,   Figure 6, Breakdown of cases in
different network areas
  to ensure that issues identified in
  their infrastructure or services are
  resolved swiftly.
The diagram opposite provides a
breakdown of % cases in a variety of
network component areas. Radio Access
GSMA Mobile Telecommunications Security Landscape - 2026 18/26

Generative and Agentic Artificial GSMA Mobile Telecommunications
Intelligence Security Security Landscape - 2026
Generative and Agentic Artificial
6
Intelligence Security
In the past few years, effective generative AI technology capabilities and availability have increased significantly enabling a range of
new uses for both offensive75 and defensive purposes with major ramifications for mobile telecoms security.
AI/ML has the potential to lower the adversary tactics and techniques based security defensive controls require the model scheduler itself, or any
technical barriers to attack methods that on real-world attack observations. many of the same security controls and sensitive data crossing a boundary
may have previously been unavailable to NIST has released guidance such as cyber hygiene to establish a security from deterministic permissions to
less sophisticated threat actors including: Artificial Intelligence Risk Management baseline of extant deployed networks, probabilistic.
Framework 77. systems and service. Beyond baseline
AI system security is maturing. There are
— Enhancing the efficiency and security, autonomous agent collaboration
security challenges with some emerging
effectiveness of social engineering With the rapid evolution of generative AI, demands enhanced security. Anyone
tools80 that need to be built to reflect
attack types, such as smishing, artificial intelligence is now transitioning adopting agentic systems into any
existing best practices to defend against
vishing and phishing. into the era of agentic AI characterised workflow must adopt the concept
known attack types81. The broader hand
by autonomy and intent driven decision- of the threat actor as internal to the
— Scams empowered by generative AI over between governance and security is
making. Unlike traditional AI limited workflow, rather than as an external party
also being explored. GSMA launched the
— Identification of new attack types to predefined tasks, Agentic AI leverages interacting with it. Consider79,
first industry-wide Responsible AI (RAI)
through use of AI workflows that decompose complex
Maturity Roadmap82 to provide telecoms
goals, iteratively optimise actions, and 1. Boundary Collapse, where an
— Synthetic identity fraud (such as operators with the tools and guidance to
actively adapt to dynamic environments, agentic model’s output is executed
deepfakes) test and assess their responsible use of
positioning itself as the cornerstone of by tooling that treats the model as
the technology.
— Enabling efficiencies for attackers next-generation digital infrastructure. authoritative;
and lowering the attacker skill base
Whilst the area is still in its relative 2. Supply Chain Substitution, .
tampered dependencies, images, or AI Is Not Enough: Why Cyber
infancy, protecting new AI systems,
Defensive AI-enabled solutions are also data78 and algorithms has many similar model weights; Hygiene and Standards Still
emerging such as the MITRE ATLAS™ requirements to the introduction of other 3. Privilege Misconfiguration, overly Matter in Telecom Security83.
(Adversarial Threat Landscape for
new solutions. Whilst AI is providing permissive service accounts that let
Artificial-Intelligence Systems76) that
efficiency enablers for attackers, the an agent or user facing tool modify
aims to provide a knowledge base of
Sam Kight - Head of Industry Security, GSMA
75 https://www.darktrace.com/news/new-report-finds-that-78-of-chief-information-security-officers-globally-are-seeing-a-significant-impact-from-ai-powered-cyber-threats
76 https://atlas.mitre.org/
77 https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
78 https://www.cyber.gov.au/sites/default/files/2025-05/CSI_AI_Data_Security.pdf
79 https://www.gsma.com/solutions-and-impact/technologies/artificial-intelligence/agentic-ai-for-telecom-charting-the-course-for-an-intelligent-future/ and the broader document for a wider discourse
80 https://www.axios.com/2025/10/28/atlas-chatgpt-openai-web-browser-security-privacy
81 https://mellea.ai
82 https://www.gsma.com/newsroom/press-release/gsma-launches-maturity-roadmap-as-telecoms-industry-leads-the-way-in-the-deployment-of-responsible-ai/
83 https://insight.scmagazineuk.com/ai-is-not-enough-why-cyber-hygiene-and-standards-still-matter-in-telecom-security
GSMA Mobile Telecommunications Security Landscape - 2026 19/26

Post Quantum Cryptography GSMA Mobile Telecommunications
Security Landscape - 2026
7 Post Quantum Cryptography
Post Quantum Cryptography is a topic with some uncertainty on timing but with potential for a significant security impact.
A Cryptographically Relevant Quantum Computer (CRQC) has the potential to break public key infrastructures which underpin many
current security protocols including some key distribution and digital signature regimes. It is a complex area with significant
uncertainty. For telecoms, GSMA’s Post Quantum Telco Networks (PQTN) Task Force84 has been active for several years in
developing guidelines focused on telco preparedness for quantum safe security.
There was much debate about the large integers and allows attackers of additional information on specific
timescales for transition to PQC, so this to efficiently solve the discrete log algorithms and key lengths, and an
is explored further here. In large part this problem. Importantly, Shor’s algorithm analysis of the impact will be valuable as
is impacted on by the timescales within can achieve an exponential speedup, part on ongoing PQC transition planning.
which a CRQC will become available. relative to known classical methods, There has been significant activity
The security of commonly employed rendering it infeasible to simply increase to prepare for QSC including
cryptographic algorithms, such as key sizes. Consequently, a sufficiently at NIST86, ETSI87 and IETF88 and
RSA- and elliptic curve-based public large fault tolerant quantum computer significant national and regional activity
key encryption and digital signature poses a threat to systems and protocols (take a look at some of the conference
schemes, is reliant upon the hardness of that utilise public key cryptography and/ presentations to get an update). NIST
solving certain underlying mathematical or digital signatures, and large-scale has released three PQC standards to
problems. Security of these asymmetric changes are required to retain present- start the transition to post-quantum
protocols is founded on the assumption day security assurances in the face cryptography: the Module-Lattice-
that a compute- or time- bounded of this quantum threat (the CRQC Based Key-Encapsulation Mechanism
attacker is unable to efficiently compute ‘pull’ factor). [FIPS203], the Module-Lattice-Based
the prime factors of large integers Digital Signature Algorithm [FIPS204],
or solve the discrete log problem. Whilst there is uncertainty on the timing and the Stateless Hash-Based Signature
The advent of a CRQC fundamentally for the availability of a CRQC, the recent Algorithm [FIPS205]. There are real-world
changes our assumptions regarding NIST announcements85 with the intention implementations of these algorithms
the compute powers available to bad to deprecate some important and widely (including open-source code) beginning
actors. Shor’s algorithm, for example, used algorithms provides a clear ‘push’ to be made available.
enables the efficient factorisation of priority to effect change. There is a lot
84 https://www.gsma.com/solutions-and-impact/technologies/security/post-quantum/
84 PQ.01 https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/post-quantum-telco-network-impact-assessment-whitepaper-pq-01
84 PQ.02 https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/guidelines-for-quantum-risk-management-for-telco-pq-02/
84 PQ.03 https://www.gsma.com/newsroom/gsma_resources/pq-03-post-quantum-cryptography-guidelines-for-telecom-use-cases/
84 PQ.04 https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/pq-04-post-quantum-cryptography-in-iot-ecosystem/
84 PQ.05 https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/pq-05-post-quantum-cryptography-for-5g-roaming-use-case/
85 https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf
86 https://csrc.nist.gov/projects/post-quantum-cryptography
87 https://www.etsi.org/technologies/quantum-safe-cryptography
88 https://datatracker.ietf.org/wg/pquip/about/
GSMA Mobile Telecommunications Security Landscape - 2026 20/26

Post Quantum Cryptography GSMA Mobile Telecommunications
Security Landscape - 2026
The diagram illustrates some of the
important push and pull factors alongside
a set of migration and other factors to MIGRATION FACTORS
consider for PQC.
— System I service I data prioritisation
— Availability of accurate and complete
Most existing QSC migration advice
CBOM or cryptographic inventory
sensibly points to establishing an
— Cryptographic agility options
inventory of encryption protocols in use.
Other early steps include identifying — Key lengths
critical systems and then identifying — Planned systems transformation replacements
their supporting protocols, risk analysis — Hybrid cryptographic solutions
and prioritisation, developing the — Open Source Software (OSS)- availability /
transition plan and delivering it. Practical accuracy of CBOMs for at-scale use PULL FACTORS
complementary approaches can focus and depth of other software
PUSH FACTORS — New PQC algorithm
beyond today’s implementations and
stadardisation &
look at the planned future state of — Algorithm deprecation
implementations
networks and systems. This can include — Some vendor road
understanding planned technology maps — Experience from real-
refresh, vendor product roadmaps and OTHER FACTORS world PQC migration
transformation projects. There may be — Timing / technology maturity of CRQC — CRQC technology
little point planning a transition for a progress
— Cost, constrained budgets and phasing
system that is due to be phased out soon.
of migration
Cryptographic agility is an important
— Long-term robustness of new PQC
system design and standardisation
algorithms
feature allowing rapid transition of
— In-house skills and expertise on
cryptographic algorithm.
cryptography and
More QSC detailed approaches are — Leveraging purchasing terms for migration
identified in the PQTN Task Force — Risk management
documentation89 which is actively being — Difficulty in verification
developed with more guidance.
Figure 7, A range of factors affecting PQC
89 https://www.gsma.com/solutions-and-impact/technologies/security/post-quantum-telco-network-task-force/
GSMA Mobile Telecommunications Security Landscape - 2026 21/26

Mapping the Global Cybersecurity GSMA Mobile Telecommunications
Regulatory Landscape Security Landscape - 2026
Mapping the Global Cybersecurity
8
Regulatory Landscape
Cybersecurity regulation is now a defining factor in the resilience of mobile networks. A GSMA report90 highlights that fragmented,
misaligned, or overly prescriptive regulation imposes unnecessary costs, diverts resources from genuine risk mitigation, and in
some cases increases exposure to cyber threats.
A Fragmented and Fast-Moving Rapidly Expanding Patchwork where countries converge and where approaches, from governance models
Landscape their approaches begin to diverge. to implementation measures. It also
Cybersecurity regulation now spans: Countries are included because they highlights good practices that can be
Cybersecurity regulation is no longer have established cybersecurity laws, adapted across borders.
the domain of a few national strategies — Mandatory product security laws national strategies, or sectorspecific
or voluntary frameworks. Today, it (e.g., EU’s Cyber Resilience Act, UK’s obligations that create real, enforceable A key takeaway from ENISA’s mapping
spans mandatory product security PSTI Act) requirements for mobile operators. is the importance of resilience, including
laws, sector-specific obligations, — Sector-specific obligations (e.g., Others are not shown because their the ability to recover quickly and maintain
certification schemes, and cross-border frameworks remain voluntary, highlevel, continuity across critical sectors. The
UK’s Telecoms Security Act)
data governance regimes. From the or still in draft. ability to recover quickly from cyber
EU’s Cyber Resilience Act (CRA) to the — Certification schemes (e.g., EU incidents is now as critical as prevention.
UK’s Telecoms Security Act (TSA) and Cybersecurity Act, Japan’s JC-Star, Strategic Governance and Resilience This includes not only technical recovery
China’s cybersecurity review measures, ISMAP) but also reputational and operational
the regulatory patchwork is expanding The persistence of ransomware and continuity. Strategies must therefore
— Standards agencies (ITU, UNECE,
rapidly. the targeting of critical sectors call embed resilience across sectors,
ETSI, NIST, ISO, ENISA, APEC)
for a renewed focus on strategic with tailored approaches for high-risk
For mobile operators, this fragmentation — Cross-border data governance (e.g., governance. National Cyber Security domains like energy, healthcare, and
results in overlapping or contradictory China’s Cybersecurity Review) Strategies (NCSS) must evolve to manufacturing.
obligations from multiple authorities, reflect the changing threat environment.
duplicated reporting requirements, and ENISA’s Interactive Map of NCSS 91
The following map shows how
administrative burdens that deliver limited provides a valuable overview of how
cybersecurity regulation and standards
security benefit. EU Member States are structuring their
vary across regions, highlighting
90 https://www.gsma.com/solutions-and-impact/connectivity-for-good/public-policy/gsma_resources/the-impact-of-cybersecurity-regulation-on-mobile-operators
91 https://www.enisa.europa.eu/topics/national-cyber-security-strategies/ncss-map/national-cyber-security-strategies-interactive-map
GSMA Mobile Telecommunications Security Landscape - 2026 22/26

|     |     |           |                  |     | Mapping the Global Cybersecurity  |                 |     | GSMA Mobile Telecommunications   |
| --- | --- | --------- | ---------------- | --- | --------------------------------- | --------------- | --- | -------------------------------- |
|     |     |           |                  |     | Regulatory Landscape              |                 |     | Security Landscape - 2026        |
|     |     | Standards | Legislation      |     | Standards                         | Legislation     |     |                                  |
|     |     |           | TSA, PSTI, CAF,  |     |                                   | CRA, RED, CSA,  |     |                                  |
ISO/IEC 27001 ISO/IEC 27001
|     |     |     | Ports & Shipping  |     |     | ESPR, DNA |     |     |
| --- | --- | --- | ----------------- | --- | --- | --------- | --- | --- |
ETSI EN 303 645  ETSI EN 303 645
Bill
ETSI EN 303 645  IEC 62443
PSA Certified Level 1
ISO/IEC 15408
NCSC CAF NIST CSF
NIST CSF EU Electronic Communications Code
IMO Guidelines
|     |     |     |     |     |     |     | Standards | Legislation |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- |
NCSC guidance
|     |     |     |     |     |           |                | ISO/IEC 27001 | JC-SIP/STAR |
| --- | --- | --- | --- | --- | --------- | -------------- | ------------- | ----------- |
|     |     |     |     |     | Standards | Legislation    |               |             |
|     |     |     |     |     |           | Cybersecurity  | NIST CSF      |             |
GB/T 22239-2019
|     |     |     |     |     |     | Review  | METI guidelines |     |
| --- | --- | --- | --- | --- | --- | ------- | --------------- | --- |
GB/T 35273-2020
Measures
|     |     | Standards |     | Legislation |     |     |     |     |
| --- | --- | --------- | --- | ----------- | --- | --- | --- | --- |
Cloud Computing
| Standards | Legislation | ECC:2018 |     |     |     |     |     |     |
| --------- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
Regulatory
CITC Cloud Framework
| ISO/IEC 27001      | NIST CSF,     |     |     | Framework |     |     |                       |                  |
| ------------------ | ------------- | --- | --- | --------- | --- | --- | --------------------- | ---------------- |
|                    | Cyber Trust   |     |     |           |     |     | Standards             | Legislation      |
| NIST SP 800 Series | Mark, CFIAS,  |     |     |           |     |     |                       |                  |
|                    | NIST 2        |     |     |           |     |     | CSA Codes of Practice | Cyber Security   |
Act
|     |     |     |     | Standards | Legislation |     |     |     |
| --- | --- | --- | --- | --------- | ----------- | --- | --- | --- |
IT Act & National
IT Act
Cybersecurity
CERT-In guidelines
| Standards | Legislation |     |     |     | Policy |     |     |     |
| --------- | ----------- | --- | --- | --- | ------ | --- | --- | --- |
NCIIPC standards
| TIA SCS 9001  | TIA SCS 9001 |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
ISO/IEC 27001
| NIST CSF |     |     |     |     | Standards        | Legislation      |     |     |
| -------- | --- | --- | --- | --- | ---------------- | ---------------- | --- | --- |
|          |     |     |     |     | Privacy Act 1988 | Notifiable Data  |     |     |
Breaches, Critical
|     |     |     |     |     | SOCI Act | Infrastructure Act |     |     |
| --- | --- | --- | --- | --- | -------- | ------------------ | --- | --- |
ACSC guidance
Figure 9, Mapping the global cybersecurity regulatory landscape
GSMA Mobile Telecommunications Security Landscape - 2026 23/26

Mapping the Global Cybersecurity GSMA Mobile Telecommunications
Regulatory Landscape Security Landscape - 2026
Looking Ahead: Strategic — Security-by-design: Encourage a
Recommendations proactive, security-by-design
approach to mitigating cyber risks. Harmonisation
To address the evolving threat landscape,
— Capacity-building: Strengthen
national and international policy must
the institutional capacity of
adapt. Based on the synthesis of threat
cybersecurity authorities to ensure
intelligence and strategic mapping, the
a whole-of-government approach Capacity-building: Consistency
following recommendations emerge.
and effective application of policy
— Harmonisation: Align and regulation.
cybersecurity policy with
international standards wherever The cyber threat landscape is
possible, to reduce regulatory increasingly complex, with ransomware,
fragmentation and inconsistency. geopolitical tensions, and resilient threat
— Consistency: Ensure new policies actors shaping the strategic environment.
National regulatory strategies must
and frameworks are consistent with
Looking
evolve to meet these challenges,
existing policy to avoid duplication or Ahead
embedding resilience, risk management,
conflict.
intelligence, and collaboration at their
— Risk- and outcome-based: Adopt core.
!
risk-based and outcome-based
approaches in the design and
implementation of cybersecurity
regulation, giving operators flexibility
to innovate and deploy effective Security-by-design Risk- and
outcome-based
solutions.
— Collaboration: Promote a
collaborative regulatory culture with
industry, supported by secure threat Collaboration
intelligence sharing to strengthen
resilience, increase awareness
of cyber threats, enable constructive
enforcement, and foster a joint Figure 8, Significant factors to consider
approach to combating cybercrime. for regulation
GSMA Mobile Telecommunications Security Landscape - 2026 24/26

|     |     |     | Final Thoughts |     |     | GSMA Mobile Telecommunications   |     |
| --- | --- | --- | -------------- | --- | --- | -------------------------------- | --- |
Security Landscape - 2026
9 Final Thoughts
The GSMA Mobile Security Landscape Report 2026 provides an overview of the security landscape for the mobile industry in the
context of current threats facing mobile network operators, their customers and the wider ecosystem.
| The report has identified a range of key  | 7.  Adopt a risk-based security   |     |     |     |     |     |     |
| ----------------------------------------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
| security protection areas including:      |   approach including risk         |     |     |     |     |     |     |
  assessments, layered defences
| 1.  Strengthen cyber hygiene and        |   and updating defences against the    |                                               |     |                |     |             |     |
| --------------------------------------- | -------------------------------------- | --------------------------------------------- | --- | -------------- | --- | ----------- | --- |
|   baseline controls including MFA,      |     latest threats                     |                                               |     |                |     |             |     |
|                                         |                                        |                                               |     | 2              |     | 4           |     |
|   encrypting sensitive data, network    |                                        |                                               |     |                |     | Strengthen  |     |
|                                         | 8 .  P re                              | p a r e   fo r  e m e r gi ng technologies    |     | K n o w  your  |     |             |     |
  segmentation and regular patching tr a ff ic s u p p ly   chain
|     |   su c | h  a s   A I  a n d  P Q C |     |     |     | s ec u r it y |     |
| --- | ------ | -------------------------- | --- | --- | --- | ------------- | --- |
2.  Know your traffic including
|                                        | 9.  Engage with industry collaboration    |     | 1            |     | 3           |     | 5        |
| -------------------------------------- | ----------------------------------------- | --- | ------------ | --- | ----------- | --- | -------- |
|   enhanced threat detection and        |                                           |     | Strengthen   |     |             |     |          |
|                                        |                                           |     | cyber        |     | Secure the  |     | Combat   |
|                                        |   standards such as GSMA’s                |     |              |     | software    |     | scams    |
|   incident response including threat   |                                           |     | hygiene      |     |             |     |          |
  fraud and security groups92
  hunting
10. Promote a security-first culture with
3.  Secure the software attack vector
  executive engagement and
  including more secure code, API
  continuous improvement
  security and third-party risk
|   management                              |                                      |     |     |              |     |                 |     |
| ----------------------------------------- | ------------------------------------ | --- | --- | ------------ | --- | --------------- | --- |
|                                           |                                      |     |     | 7            |     | 9               |     |
|                                           | Over the coming year, the GSMA will  |     |     | Risk-based   |     | Industry        |     |
| 4.  More broadly, strengthen the entire   |                                      |     |     |              |     | collaboration   |     |
|                                           | continue to support its members on   |     |     | security     |     | & standards     |     |
  supply chain security by applying
security matters by providing security
|   security controls throughout the   |     |     | 6   |     | 8   |     | 10  |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Promote a
|     | best practices, services and events that  |     | Adopt and   |     | Prepare for  |     |     |
| --- | ----------------------------------------- | --- | ----------- | --- | ------------ | --- | --- |
  product or service lifecycle support emerging   security-first
convene the industry - engagement by all  technologies culture
| 5.  Combat scams and social   | stakeholders is strongly encouraged. |     |     |     |     |     |     |
| ----------------------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
  engineering
To get in touch, or to get more
| 6.  Adopt and support industry   |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
closely involved, please email
  schemes, for example GSMA’s CVD
security@gsma.com.
  & T-ISAC

Figure 10, A range of key security protection areas

92 https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/security-assurance-andcertification/

GGSSMMAA  MMoobbiillee  TTeelleeccoommmmuunniiccaattiioonnss  SSeeccuurriittyy  LLaannddssccaappee  --  22002266 2255//2266

GSMA Head Office
1 Angel Lane
London
EC4R 3AB
UK
Email: security@gsma.com

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-21", "model": "gemini-3.5-flash-lite"} -->
