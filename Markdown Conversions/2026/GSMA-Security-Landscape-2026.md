# GSMA Mobile Telecommunications Security Landscape - 2026

## Table of Contents
- [1. Executive Summary](#1-executive-summary)
- [2. Mobile networks, devices and consumers are under attack](#2-mobile-networks-devices-and-consumers-are-under-attack)
  - [2.1 Software Attacks](#21-software-attacks)
  - [2.2 Democratisation of Attacks](#22-democratisation-of-attacks)
  - [2.3 Successful Pre-Positioning Attacks](#23-successful-pre-positioning-attacks)
  - [2.4 Exploiting Weak Cyber Hygiene](#24-exploiting-weak-cyber-hygiene)
  - [2.5 Supply Chain Attacks](#25-supply-chain-attacks)
  - [2.6 The Spectrum: Security, Fraud, Scams](#26-the-spectrum-security-fraud-scams)
- [3. Threat Actors](#3-threat-actors)
- [4. Risk Management](#4-risk-management)
- [5. Coordinated Vulnerability Disclosure](#5-coordinated-vulnerability-disclosure)
- [6. Generative and Agentic Artificial Intelligence Security](#6-generative-and-agentic-artificial-intelligence-security)
- [7. Post Quantum Cryptography](#7-post-quantum-cryptography)
- [8. Mapping the Global Cybersecurity Regulatory Landscape](#8-mapping-the-global-cybersecurity-regulatory-landscape)
- [9. Final Thoughts](#9-final-thoughts)

---

## 1. Executive Summary
This is the GSMA’s eighth annual Mobile Telecommunications Security Landscape report. Building on the previous reports[^1], it reflects developments during 2025, updated analyses, new and updated content, identifies key trends and provides a look at some of the emerging security topics.

The report highlights first that mobile networks, devices and consumers are experiencing a full spectrum of attacks across the globe. This report analyses these attacks and identifies six key areas for attention:

- **Software implementations as a key frontline of attacks**
- **A democratisation of attacks**, whereby there is a lowering of the technical and resource barriers to launch attacks
- **Pre-positioning attacks** that seek to establish a bridgehead for later attacks
- **Exploitation of weak cyber hygiene**
- **Supply chain attacks**
- **Scam attacks on mobile consumers**

Each of these areas includes a definition, some indicators of compromise and security mitigations to be developed, extended and implemented.

![Figure 1, An Overview of topics]

New for this year, the report includes approaches to vulnerability disclosure alongside a threat actor analysis provided via the GSMA Co-ordinated Vulnerability Disclosure scheme. The report moves on to analyse the emerging security needs associated with generative and agentic artificial intelligence and considerations and migration for post quantum cryptography. The landscape is completed by examining the fast-moving and often fragmented topic of global cybersecurity regulations. Finally, the report identifies ten key security protection priority areas derived from the report content.

---

## 2. Mobile networks, devices and consumers are under attack
The mobile industry has long aimed to develop and deploy robust security measures to protect its assets, customers and services. GSMA continue to see attacks directly on mobile networks, services and devices, including attacks on service delivery, denial of service, the delivery of malware and attacks seeking to exfiltrate data.

In mobile networks, a single breach can disrupt infrastructure, customers, and supply chains. There is a commonality of attack tactics such as credential theft, token abuse, Software-as-a-Service (SaaS) exploitation, and living-off-the-land methods. This highlights the urgent need for tailored operational security, ongoing behavioural monitoring, robust governance and underscores the importance of flexible detection models and sector-specific expertise.

The operational attack surface is wide and complex. Attacks can be launched at many different points externally and from within the network. Mobile Network Operators (MNOs) have been targeted for many years and these attacks continued in 2025. Threat actors use a range of attack techniques to achieve their goals. After an initial phase of reconnaissance, the attack may move to establish an initial access bridgehead. This initial access phase may persist for months or years, with low levels of activity, occasionally contacting the Command and Control (C2) server, gathering information, exfiltrating low levels of data or waiting for a better time to launch a more destructive or impactful attack. Hence the need for threat hunting activity.

![Figure 2, A spectrum of attacks]

### 2.1 Software Attacks
A software attack is a malicious attempt to gain unauthorised access to a computer system or network by exploiting vulnerabilities in code. Deficiencies in coding implementations lead to potential vulnerabilities that attackers may seek to exploit.

**Indicators of Compromise:**
- Unusual or unauthorised software installations
- API overloads / data leaks
- Unexpected configuration changes
- System crashes or degraded performance
- Unexpected new code libraries or binaries
- Lateral movement activity

**Mitigations:**
- Secure by design code development lifecycle
- Being fully aware of code composition, eg by using an SBOM
- Manage security of code repositories
- Adopt security best practices for API development security
- Use of privileged access workstations and utilising the principle of least privilege.

### 2.2 Democratisation of Attacks
There has been a progressive lowering of skill and resource levels required to launch effective attacks. A range of approaches have been evidenced:
- **SMS Blasters**: Portable and easy-to-use fake mobile base transceiver stations used for fraudulent smishing.
- **Dark web marketplaces**: Offer hacking tools, exploit kits, and stolen credentials.
- **Initial access brokers**: Threat actors who procure access to networks and sell them to other TAs.
- **Ransomware/phishing/malware as-a-service**: Commodity attack tools.
- **AI-enabled attack efficiency**: Automating reconnaissance, vulnerability scanning, and data analysis.

### 2.3 Successful Pre-Positioning Attacks
Adversaries compromise systems and persist to prepare for a later escalation or undertake ongoing low-level data exfiltration and ‘beaconing’ to C2 servers. These ‘quiet’ attacks may have been missed by defence capabilities.

**Mitigations:**
- Threat hunting
- Implement trusted boot capabilities and secure roots of trust with periodic rebooting of systems
- Proactive penetration testing
- Threat intel sharing via the GSMA Telecommunication Information Sharing and Analysis Center (T-ISAC).

### 2.4 Exploiting Weak Cyber Hygiene
Threat actors often start by using basic toolsets that exploit well-known vulnerabilities. The role of the defender is to make attacks progressively harder to launch.

**Mitigations:**
- Undertake a complete asset inventory
- Implement a strong baseline set of controls (e.g., GSMA FS.31)
- Build in multilayer defences
- Monitoring and analysis of logging data
- Improve network and system segmentation
- Encrypt key data.

### 2.5 Supply Chain Attacks
Supply chain attacks continue at pace. The opportunity for indirect attacks through supplier or third-party tooling and services requires vigilance.

**Mitigations:**
- Adopt a lifecycle approach to improve the whole chain of supply and operation
- Know your traffic: logging and monitoring of all traffic types
- Use industry security assurance schemes (e.g., GSMA NESAS)
- Actively manage code deployments and update to ensure correct code versioning and binary equivalence
- Strictly control remote access arrangements.

### 2.6 The Spectrum: Security, Fraud, Scams
The scam economy has grown rapidly, costing victims $1 trillion worldwide. The mobile industry is taking comprehensive steps to combat the rising number of scams that affect individuals and society, including the use of AI-powered spam detection and the Scam Signal API.

---

## 3. Threat Actors
Gaining a comprehensive understanding of threat actors is crucial for enhancing cybersecurity defences. GSMA’s T-ISAC has been tracking several key groups:

- **Salt Typhoon (AKA UNC2286)**: Active since at least 2019, targeting telecommunications infrastructure and government systems worldwide using zero-day exploits and living-off-the-land techniques.
- **LightBasin (AKA UNC1945 + UNC281)**: Focuses on Linux and Solaris systems in telecommunications, finance, and retail.
- **Scattered Spider (AKA UNC3944 & Octo Tempest)**: Financially motivated, English-speaking group using social engineering, SIM swapping, and MFA fatigue attacks.
- **ShinyHunters**: Specialises in data theft and extortion, often gaining access through credential theft or misconfigured cloud services.

![Figure 3, Tactics used by the Threat Actors]

---

## 4. Risk Management
A powerful strategic security response is to utilise risk and threat management to design and leverage security investments. Threat modelling allows for the identification of the most likely and impactful risks.

**Risk Treatment Options:**
- Accept the net risk position
- Sharing the risk through a new delivery arrangement
- Avoid the risk (e.g., closing a platform)
- Transfer the risk to another party
- Risk education

---

## 5. Coordinated Vulnerability Disclosure
*(Content omitted in source text)*

---

## 6. Generative and Agentic Artificial Intelligence Security
*(Content omitted in source text)*

---

## 7. Post Quantum Cryptography
*(Content omitted in source text)*

---

## 8. Mapping the Global Cybersecurity Regulatory Landscape
*(Content omitted in source text)*

---

## 9. Final Thoughts
*(Content omitted in source text)*

[^1]: https://www.gsma.com/solutions-and-impact/technologies/security/publications/

---

h implementing additional security
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