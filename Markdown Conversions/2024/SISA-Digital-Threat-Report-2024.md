security professionals struggle to identify
all IoT devices on their networks. This
lack of visibility, combined with the
inherent security limitations of many IoT
devices—such as hardcoded credentials,
lack of encryption, and infrequent
patching—creates a significant security
gap.

Attackers are increasingly targeting these
devices, using them as entry points to
infiltrate broader corporate networks.
Once a device is compromised, it can
be used to launch lateral attacks, steal
sensitive data, or disrupt critical services.
The interconnected nature of IoT devices
within the BFSI ecosystem means that a
single compromised device can have a
cascading effect, potentially impacting
multiple systems and services.

### CASE 8: TURNING A $2 MILLION HACK INTO A HARDWARE-HACKING MILESTONE

In a notable incident (outside India), threat
actors demonstrated the potential risks
associated with IoT and hardware devices
by successfully hacking a Trezor hardware
wallet. The attackers utilized fault injection
techniques to bypass the device’s security
mechanisms, effectively unlocking $2 million
in cryptocurrency.

This incident serves as a stark reminder
that even devices designed with security
in mind are not immune to sophisticated
hardware-level attacks. The attackers
exploited physical vulnerabilities in the
device’s hardware, demonstrating that
physical access to a device can be a
significant security risk.

The breach highlights the importance of
considering hardware security as a critical
component of the overall cybersecurity
posture. As IoT devices become more
prevalent in the BFSI sector, organizations
must prioritize the security of these
devices, from the design phase to
deployment and maintenance.

#### Top 5 Mitigation Strategies

1. **Device Inventory and Management**: Maintain a comprehensive inventory of all IoT devices connected to the network. Implement robust device management policies to ensure that all devices are accounted for, monitored, and secured.
2. **Network Segmentation**: Isolate IoT devices from critical business networks using VLANs and firewalls. This limits the potential impact of a compromised device, preventing lateral movement within the network.
3. **Strong Authentication and Encryption**: Enforce strong authentication mechanisms, such as unique, complex passwords and multi-factor authentication, for all IoT devices. Ensure that data transmitted by these devices is encrypted to prevent interception.
4. **Regular Patching and Updates**: Implement a rigorous patching and update schedule for all IoT devices. Use virtual patching where necessary to protect legacy devices that may no longer receive official updates.
5. **Physical Security**: Implement strict physical security measures to prevent unauthorized access to IoT devices, particularly those located in public or semi-public areas.

---

## 07 Regulatory Focus: A Special Feature

### 2025 and Beyond: Navigating Evolving Regulations in the Digital Payments Landscape

The regulatory landscape for digital
payments is undergoing a significant
transformation, driven by the need to
address the evolving cyber threat landscape
and ensure the stability and security of the
financial ecosystem. As digital payments
become increasingly integrated into the
global economy, regulators are focusing
on harmonizing standards, enhancing
transparency, and promoting resilience.

In 2025 and beyond, we expect to see
a shift towards more proactive and
risk-based regulatory frameworks.
Regulators will likely place greater
emphasis on:

- **Cyber Resilience**: Mandating robust
  cybersecurity frameworks, incident
  response plans, and recovery mechanisms
  to ensure the continuity of financial
  services in the face of cyberattacks.
- **Data Protection and Privacy**:
  Strengthening regulations around the
  collection, storage, and processing of
  sensitive financial data, with a focus on
  transparency and user consent.
- **Third-Party Risk Management**:
  Introducing stricter requirements for
  managing risks associated with third-party
  vendors and service providers, including
  supply chain security and vendor
  audits.
- **AI and Emerging Technologies**:
  Developing guidelines for the responsible
  use of AI and other emerging
  technologies in financial services,
  addressing potential risks such as bias,
  transparency, and security.

### Suggestions to Policy Makers

To foster a secure and resilient digital
payments ecosystem, policy makers should
consider the following:

1. **Promote Collaboration**: Encourage
   collaboration between regulators,
   financial institutions, and cybersecurity
   experts to share threat intelligence and
   best practices.
2. **Harmonize Standards**: Work towards
   harmonizing cybersecurity standards
   across regions to reduce compliance
   burdens and ensure consistent security
   levels.
3. **Invest in Education and Awareness**:
   Support initiatives to educate consumers
   and businesses about cyber risks and
   best practices for staying secure.
4. **Foster Innovation**: Create a
   regulatory environment that encourages
   innovation while ensuring that security
   and resilience are prioritized.
5. **Strengthen Enforcement**: Ensure that
   regulatory requirements are effectively
   enforced, with clear consequences for
   non-compliance.

---

## 08 Insights Across Layers of Defense Seen in BFSI Sector

### Frequently Observed Control Gaps in Financial Institutions (India & Global)

Despite significant investments in
cybersecurity, financial institutions
continue to face critical control gaps that
adversaries exploit. These gaps often stem
from a combination of legacy systems,
rapid digital transformation, and the
complexity of modern IT environments.

Key control gaps observed include:

- **Inadequate Access Controls**: Weak
  password policies, lack of multi-factor
  authentication, and over-privileged
  user accounts.
- **Misconfigurations**: Publicly accessible
  cloud storage, default credentials, and
  insecure API configurations.
- **Delayed Patching**: Failure to apply
  security patches in a timely manner,
  leaving systems vulnerable to known
  exploits.
- **Lack of Visibility**: Insufficient
  monitoring and logging, making it
  difficult to detect and respond to
  security incidents.
- **Insecure Third-Party Integrations**:
  Lack of rigorous security assessments
  for third-party vendors and service
  providers.

### Evaluating Security Maturity: Technical Trends and Gaps in the BFSI Sector

#### Perimeter Security / Network Security
- **Trend**: Shift towards Zero Trust
  architectures.
- **Gap**: Inconsistent implementation of
  network segmentation and lack of
  visibility into internal traffic.

#### Application Security
- **Trend**: Adoption of DevSecOps and
  automated security testing.
- **Gap**: Persistent vulnerabilities such
  as SQL injection, XSS, and insecure API
  endpoints.

#### Secure Configuration
- **Trend**: Infrastructure as Code (IaC)
  for consistent configuration.
- **Gap**: Misconfigurations in cloud
  environments and lack of automated
  configuration auditing.

#### Cloud Security
- **Trend**: Multi-cloud strategies and
  cloud-native security tools.
- **Gap**: Inadequate management of cloud
  identities and permissions.

#### Monitoring & Response
- **Trend**: Use of AI/ML for threat
  detection and automated response.
- **Gap**: Siloed security tools and lack of
  integrated incident response workflows.

#### Identity and Access Management Security
- **Trend**: Adoption of Passwordless
  authentication and Privileged Access
  Management (PAM).
- **Gap**: Incomplete coverage of MFA and
  lack of regular access reviews.

#### Endpoint Security
- **Trend**: Shift to EDR/XDR solutions.
- **Gap**: Inconsistent deployment of
  endpoint protection and lack of
  visibility into non-traditional endpoints.

#### Data Protection and Encryption
- **Trend**: Adoption of data-centric
  security and encryption at rest/in transit.
- **Gap**: Inconsistent encryption practices
  and lack of data classification.

#### Vulnerability and Penetration Testing
- **Trend**: Continuous security testing
  and bug bounty programs.
- **Gap**: Infrequent testing and failure to
  remediate identified vulnerabilities.

---

## 09 Gazing Through the Crystal Ball for 2025

### Anticipated Attack 1: Rise of Deep Fakes and AI-Generated Content
Expect an increase in highly convincing
deepfake audio and video used for
impersonation, social engineering, and
disinformation campaigns.

### Anticipated Attack 2: Growing Threat of Supply Chain Attacks and Malicious Libraries
Attackers will continue to target the
software supply chain, injecting malicious
code into open-source libraries and
compromising third-party vendors.

### Anticipated Attack 3: Emerging Threat of LLM Prompt Hacking in Applications
As LLMs are integrated into applications,
attackers will exploit prompt injection
vulnerabilities to manipulate model
outputs and gain unauthorized access.

### Anticipated Attack 4: Influence of Adversarial LLMs Enhancing Attack Capabilities
Adversaries will leverage LLMs to automate
the creation of sophisticated malware,
craft personalized phishing lures, and
identify vulnerabilities at scale.

### Anticipated Attack 5: Quantum Computing - A Looming Threat to Cryptography
While still in the early stages, the
potential for quantum computing to break
current encryption standards poses a
long-term threat to data security.

### Anticipated Attack 6: Crypto: A New Frontier for Cyber Threats
The rise of decentralized finance (DeFi)
and cryptocurrency will attract more
cybercriminals, leading to increased
attacks on crypto exchanges and wallets.

### Anticipated Attacks 7: IoT, the Emerging Threat to Embedded Devices
As IoT devices become more prevalent,
attackers will increasingly target embedded
systems, exploiting their inherent
vulnerabilities to gain access to critical
networks.

---

## 10 Recommendations: Strengthening Your Cybersecurity Posture

### Building a Resilient People-Force: Strengthening Cybersecurity Through Training, Governance, and Remote Security
- **Continuous Training**: Implement
  regular, role-based cybersecurity
  training for all employees.
- **Strong Governance**: Establish clear
  cybersecurity policies and procedures,
  with accountability at the executive
  level.
- **Remote Security**: Enforce strict
  security measures for remote work,
  including VPNs, MFA, and endpoint
  protection.

### Strengthening Cybersecurity Through Proactive Processes and Layered Defenses
- **Proactive Threat Hunting**: Regularly
  hunt for threats within the network to
  identify and mitigate potential risks.
- **Incident Response Planning**: Develop
  and regularly test comprehensive
  incident response plans.
- **Layered Defenses**: Implement a
  defense-in-depth strategy, with multiple
  layers of security controls.

### Technology: Building Resilient Cyber Defenses
- **Automated Security**: Leverage
  automation for threat detection,
  vulnerability management, and incident
  response.
- **Zero Trust Architecture**: Adopt a
  Zero Trust approach, verifying every
  access request regardless of its origin.
- **Advanced Analytics**: Use AI/ML-
  powered analytics to detect anomalies
  and identify potential threats in real
  time.

---

## 11 Conclusion

The 2024 Digital Threat Report for the
BFSI Sector underscores the critical
importance of cybersecurity in an
increasingly digital world. As cyber
threats continue to evolve, organizations
must move beyond traditional defenses
and adopt a proactive, risk-based
approach to security. By focusing on
people, processes, and technology, and
fostering collaboration across the industry,
we can build a resilient digital payments
ecosystem that safeguards assets, maintains
trust, and supports sustainable growth.

---

## 12 Acknowledgements

We would like to thank all the contributors
and partners who made this report possible.
Their insights and expertise have been
invaluable in providing a comprehensive
view of the cyber threat landscape in 2024.

---

## 13 References

1. IBM Cost of a Data Breach Report 2024.
2. IBM Cost of a Data Breach Report 2024 (India).
3. CERT-In/CSIRT-Fin internal data.
4. SISA DFIR investigation data.
5. SISA DFIR investigation data.
6. Vulnerability research reports.
7. Industry threat intelligence reports.
8. Global deepfake identity fraud statistics.

[^1]: IBM Cost of a Data Breach Report 2024.

---

ﬁnancial leaders prioritize IoT-

exponential growth comes an alarming rise

driven operational efﬁciency. Yet, many

in security vulnerabilities. Nearly 99% of IoT

IoT deployments in banking, trade ﬁnance,

exploitation attempts leverage previously

and supply chain management often lack

known vulnerabilities (CVEs), exposing

adequate oversight. This lack of visibility

critical gaps in security infrastructure.

leaves ﬁnancial ecosystems exposed to

potential breaches and cyberattacks.

Financial institutions are increasingly

leveraging IoT for personalized services.

The consequences of IoT vulnerabilities

Banks utilize IoT to identify and greet

are signiﬁcant. Forrester’s ﬁndings reveal

customers as they enter branches, enhance

that 34% of enterprises impacted by IoT

credit risk assessments through real-

breaches experienced losses ranging from

time data, and deliver targeted product

$5 million to $10 million—substantially

recommendations via wearables. IoT-

higher than attacks on traditional IT

powered devices also facilitate on-the-go

infrastructure.

transactions and enable remote account

The last case is an in-depth analysis that explores IoT vulnerabilities and attacks,
providing valuable insights into how these risks translate to the BFSI sector. By
examining real-world incidents—from breaches through connected ﬁsh tanks and
medical devices to compromised home security cameras and cryptocurrency wallets—
this analysis underscores the critical need for enhanced IoT security measures.

23

DIGITAL THREAT REPORT 2024

CASE 8:
TURNING A $2 MILLION HACK INTO
A HARDWARE-HACKING MILESTONE

STRUCTURED AND SEGMENTED APPROACH FOR ATTACK VECTORS ACROSS THE BFSI OPERATIONS

Core Banking Systems

Payment Processing Systems

Digital Financial Services Apps

Cloud & Infra Mgmt

Vendor & Partner Integration Systems

IoT & Connected Device Security

Hardware hacker Joe Grand successfully
unlocked a Trezor wallet (outside India)
containing US$2 million in cryptocurrency by
exploiting hardware vulnerabilities through
fault injection7.

Faced with strict PIN limits and irreversible
data erasure, Grand used voltage glitching
to disrupt the wallet’s boot process,
bypassing the Readout Protection (RDP)
mechanism. By precisely inducing a “brown-

out” during the boot process, Grand
disrupted the ﬁrmware’s security check,
forcing the Trezor to copy the unencrypted
seed and PIN into RAM—allowing him to
extract them without triggering the system’s
safeguards.

The attack required precise manipulation—
removing capacitors, ﬁne-tuning glitch
parameters, and avoiding crashes
that could erase critical data. Careful

tuning of signal widths, wire lengths,
and trigger points proved essential in
hitting the microcontroller at exactly the
right moment. After hours of meticulous
attempts, Grand successfully retrieved the
funds, demonstrating how microcontroller
weaknesses in embedded devices can be
exploited if not rigorously secured against
fault attacks.

Mitigations Steps to Prevent Hardware Wallet Hacks

Strengthen Hardware and Physical
Security

Ensuring the physical security of
hardware wallets is paramount to prevent
unauthorized access and tampering.
Implementing tamper detection systems
that trigger automatic data wipes if
tampering is detected can signiﬁcantly
reduce risks. Additionally, employing
tamper-evident and tamper-resistant
packaging serves as a deterrent against
physical breaches. By isolating critical
components and restricting physical access
to sensitive areas, attackers are further
hindered from exploiting vulnerabilities.
Secure microcontrollers with built-in
protections provide another layer of
defense, making unauthorized physical
access extremely challenging.

Enhance Fault Injection and Debugging
Protections

One of the most effective ways to prevent
hardware hacks is by implementing robust
fault injection countermeasures. Fault
injection attacks exploit vulnerabilities by
disrupting normal hardware operations,
allowing attackers to bypass security
mechanisms. Strengthening Readout

24

Protection (RDP) levels and securely
locking or disabling debug interfaces
in production environments is crucial to
thwart such attacks. Debug interfaces are
often exploited to access sensitive data or
manipulate ﬁrmware, so securing them from
the outset ensures a more resilient device.

Ensure Secure Boot and Trusted
Firmware

The boot process represents a critical attack
surface, making it essential to secure boot
processes with veriﬁed bootloaders. Utilizing
a Hardware Root of Trust (HRoT) ensures
that only authorized and veriﬁed ﬁrmware is
loaded during the boot process, preventing
malicious code injections. Encrypting
sensitive data in RAM and minimizing
exposure during the boot sequence further
reduces the attack surface. By ensuring
that each layer of the boot process is
authenticated, potential attackers are
unable to manipulate ﬁrmware or introduce
vulnerabilities at the boot / startup time.

Mitigate Side Channel and Memory-
Based Attacks

Side channel attacks (SCA) can extract
sensitive information by analyzing power

consumption, electromagnetic leaks,
or timing information. Implementing
protections against side channel attacks
and continuously evaluating device
security through SCA simulations is critical.
Encrypting sensitive data stored in RAM
and employing secure communication
protocols during data exchanges adds
further resilience against potential memory
extraction attacks. This layered approach
minimizes the risk of data leakage even if
parts of the device are compromised.

Continuous Monitoring and Security
Audits

Regularly updating and patching ﬁrmware
ensures that vulnerabilities are addressed
promptly, reducing exposure to newly
discovered threats. Comprehensive
hardware security audits help identify
weaknesses in the device’s design and
implementation, allowing for pre-emptive
mitigations. Additionally, employing secure
communication protocols during data
exchanges ensures that sensitive information
remains encrypted in transit. By establishing
a cycle of continuous improvement through
audits, patches, and updates, hardware
wallets remain resilient against evolving
attack techniques.

DIGITAL THREAT REPORT 2024

REGULATORY FOCUS:
REGULATORY FOCUS:
A SPECIAL FEATURE
A SPECIAL FEATURE

25

25

DIGITAL THREAT REPORT 2024

DIGITAL THREAT REPORT 2024

2025 AND BEYOND: NAVIGATING EVOLVING
REGULATIONS IN THE DIGITAL PAYMENTS LANDSCAPE

As we move into 2025, the digital payments
and BFSI industries stand at the cusp of a
transformative shift driven by regulatory
changes and the accelerating digitization of
ﬁnancial services.

variations often result in inefﬁciencies,
especially in cross-border payment
solutions, which are crucial to the ﬁnancial
industry’s global operations.

In this shifting landscape, compliance is
no longer merely a matter of adhering to
checklists but has emerged as a strategic
imperative that will shape the industry’s
future. This transformation is not without
its challenges, but it also opens a gateway
to signiﬁcant opportunities for growth and
resilience.

The rapid pace of regulatory evolution

has created a complex environment for

ﬁnancial institutions. Mandates such as

CERT-IN directives for reporting cyber

incidents within 6 hours of noticing such

incidents or being brought to notice about

Despite these hurdles, the narrative is
beginning to shift toward regulatory
harmonization.

The push for uniﬁed
global standards is gaining
momentum, offering a
way to bridge regional
gaps and create cohesive
frameworks that simplify
compliance and improve
operational efﬁciency.

The integration of compliance and
innovation is not merely a response to
external pressures but a fundamental shift
in how organizations view their roles in the
digital ecosystem. The expected growth
of cyber attacks underscores the critical
need for resilience and adaptability. In this
context, compliance is no longer seen as
a cost center but as a cornerstone of trust
and a catalyst for growth. It has become an
essential component of an organization’s
ability to build credibility and foster long-
term customer loyalty.

As the BFSI industry moves forward,

the conversation around compliance is

evolving. What was once perceived as

a reactive, burdensome process is now

recognized as a strategic driver of resilience

and innovation. The ability to navigate a

harmonized compliance framework will not

such incidents, RBI Master Direction in

This movement toward regulatory alignment

only help organizations manage the growing

Digital Payment Security Controls(DPSC)

is not just a means of reducing friction but

complexity of regulatory requirements

and Master Direction in Outsourcing of

hold the promise of making compliance an

but also position them to thrive in an

Information technology services; RBI

enabler of growth for the ﬁnancial sector

interconnected, data-driven global

Cyber Security Framework in Banks

globally.

(CSF); SEBI’s Cybersecurity and Cyber

economy. The next decade will redeﬁne

the role of compliance, transforming it into

Resilience Framework (CSCRF), Digital

The dual demands of regulatory compliance

a force that propels the industry toward

Personal Data Protection (DPDP) Act,

and technological innovation present a

greater trust, innovation, and sustainable

2023, PCI DSS 4.0, European General Data

delicate balancing act for digital payment

growth.

Protection Regulation (GDPR),the California

organizations. The need to stay ahead in

Consumer Privacy Act (CCPA) have set new

areas such as real-time payments, fraud

benchmarks for accountability and data

detection, and predictive ﬁnancial services

protection. These frameworks underscore

requires a forward-looking approach

the urgent need for organizations to

to compliance. Emerging techniques

anticipate and adapt to emerging risks,

like data anonymization and synthetic

especially as the digital payments sector,

data generation are paving the way for

with its vast repository of sensitive ﬁnancial
data, becomes an increasingly attractive
target for cyber perpetrators. However,
the fragmented nature of compliance
frameworks across jurisdictions adds
another layer of complexity, particularly for
businesses operating across borders. Local
laws, cultural nuances, and jurisdictional

innovation without compromising privacy
or security. Additionally, embedding
compliance into the design phase of new
technologies is proving to be a game-
changing strategy, enabling organizations to
future-proof their innovations and mitigate
risks proactively.

RBI, IRDA and SEBI are
proactively supporting the
BFSI sector from a policy
and direction perspective,
CERT-In and CSIRT-Fin are
helping from a strategic,
tactical and operational
perspective. Thus, all
these entities are working
cohesively to ensure trust
and resilience in the BFSI
sector for all stakeholders.

26

DIGITAL THREAT REPORT 2024

SUGGESTIONS TO
POLICY MAKERS

Cybersecurity should be a techno-
commercial business decision and
not just decided only on commercials

Empower CISOs through direct
reporting to the CEO/CRO instead of
CTO or CIO

Cybersecurity investments must be driven
by a balance of technical requirements and
commercial viability. Prioritizing security as a
strategic enabler ensures resilience, robust
protection against threats, safeguarding
business continuity and customer trust.

Granting Chief Information Security Ofﬁcers
(CISOs) direct access to top leadership
enables better alignment of cybersecurity
strategies with business goals, ensuring
accountability and a stronger focus on
organizational risk management.

Digital Payment Security to have
common standards for all Digital
Payment Form Factors

Create more Certiﬁed Digital Payment
Security Specialists in the ecosystem

Harmonizing security standards across all

Addressing the talent gap requires fostering

digital payment methods—not just cards—

a skilled workforce through certiﬁcation

ensures a consistent and comprehensive

programs focused on payment security.

security framework that addresses emerging

This will enable enterprises to design secure

risks in alternative payment systems like

payment applications and implement robust

wallets, UPI, and QR codes.

security standards effectively.

Clear Preparation Roadmap for Post-
Quantum Cryptography

Building a Responsible AI Framework
for BFSI

Policymakers must prioritize developing a

To ensure the responsible deployment of

strategic roadmap to transition to quantum-

AI and ML in the banking and ﬁnancial

resistant cryptography, ensuring businesses

services industry, policymakers must

are prepared for future threats posed by

implement clear, comprehensive regulations

quantum computing advancements.

that balance innovation with consumer

protection and system stability. Providing

the industry with clear guidelines around
critical aspects such as data privacy, ethical
AI use, and algorithmic transparency
will encourage responsible AI adoption,
supporting growth while safeguarding
the integrity of the ﬁnancial sector and
protecting consumer interests.

27

DIGITAL THREAT REPORT 2024

INSIGHTS ACROSS LAYERS
INSIGHTS ACROSS LAYERS
OF DEFENSE SEEN IN BFSI
OF DEFENSE SEEN IN BFSI
SECTOR
SECTOR

28

28

DIGITAL THREAT REPORT 2024

DIGITAL THREAT REPORT 2024

Now that we’ve explored advanced threats
and exploitation techniques, let’s examine
the compliance levels based on sampled
entities in the BFSI sector.

Cybersecurity today mirrors Einstein’s notion
of insanity—relying on the same strategies
and expecting different outcomes.
Despite increasing investments in security
technologies, breaches remain frequent.

Consider this: Gartner projects worldwide
end-user spending on information security
to reach US$212 billion by 2025, marking
a 15.1% increase from 2024. While this
reﬂects the growing importance placed

on cybersecurity, it also underscores a
concerning trend: the more we spend, the
more sophisticated and widespread attacks
become. This paradox isn’t merely about
advanced threat actors; it’s also about
foundational cracks in how organizations
approach cybersecurity.

For instance, the average organization
deploys an astonishing 64-76 cybersecurity
tools8, yet breaches do occur. Why?
Because the solution isn’t simply about
spending more money or adding more
tools. Resilience cannot be achieved
through isolated efforts. Both organizations
with weak security postures and those

with robust defenses face signiﬁcant risks,
emphasizing the need for continuous
vigilance, proactive measures, and
alignment between compliance and security.
Achieving resilience requires continuous
threat visibility, proactive defense strategies,
continuous training & awareness of the work
force, robust processes and a security-ﬁrst
mindset that uses compliance frameworks as
a foundation.

In the next section, we decode the domains
where further improvements are needed.

% COMPLIANT IN
INDIA

% COMPLIANT
GLOBAL

HEADING

CONTROL

System Hardening and Conﬁguration

Management

Hardening and conﬁguration documentation

aligned with Center for Internet Security (CIS)

standards

System Hardening and Conﬁguration

Conﬁguration standard and baseline document

Management

maintenance

Data Protection and Encryption

Data Protection and Encryption

Encryption of cardholder data and masking of

sensitive information

Use of tokenization or TDE (Transparent Data

Encryption) for sensitive data

User access lists for Cardholder Data

Access Control and User Management

Environment (CDE) and privileged access

Patch and Vulnerability Management

Intrusion Detection and Prevention

Network Security and Segmentation

Authentication and Password Management

Log Monitoring and Event Management

Incident Response and Contingency Planning

Regular Testing and Vulnerability Scanning

controls

Timely application of patches and adherence to

vulnerability management procedures

IDS/IPS conﬁgurations to detect and prevent

unauthorized access

Network segmentation to isolate CDE and
prevent lateral movement

Multi-factor authentication (MFA) and password
conﬁguration policies

Centralized logging and monitoring of failed
logins and access attempts

Deﬁned incident response procedures and
contingency planning

Regular internal and external vulnerability scans
and penetration testing

Manageable

  Needs Improvement

  Major Concern

29

DIGITAL THREAT REPORT 2024

METHODOLOGY FOR DETERMINING COMPLIANCE PERCENTAGES
(FOR INDIA & GLOBAL)

Assessment Scope

Data Sources

Standards Covered

SISA assessed approximately 1,550 clients
globally between November 2022 and
November 2024 to derive the observed
control gap compliance percentages.

The analysis is based on technical gap
reports generated from assessments
conducted by SISA’s Qualiﬁed Security
Assessors (QSAs).

The gap assessments included PCI DSS, PCI
PIN, P2PE, PCI SAQ, and local governance
standards and regulations.

India-Speciﬁc Calculation

Global Calculation

Out of 850 clients assessed in India,
765 were compliant while frequently
encountering observed control gaps.

A similar methodology was applied to 700
clients assessed outside India to determine
global compliance percentages.

EVALUATING SECURITY MATURITY: TECHNICAL TRENDS
AND GAPS IN THE BFSI SECTOR

The security posture of ﬁnancial institutions audited/reviewed across various domains

demonstrates a mixed level of compliance and maturity in critical security areas.

Here’s a breakdown of key trends and gaps observed across different security layers

in the BFSI sector:

Perimeter Security/Network Security

Firewall: Most institutions have
implemented basic ﬁrewall conﬁgurations,
however, clients allow all trafﬁc through
open policy conﬁgurations, lacking granular
control. Additionally, insufﬁcient impact
analysis in change management processes
leads to critical changes not being tracked,
increasing the risk of unauthorized access.

DDoS Mitigation: DDoS protection is
largely limited to internet service provider
(ISP)-level solutions, and dedicated
enterprise-grade DDoS mitigation is often
missing. This leaves institutions vulnerable
to volumetric and application-layer attacks.

Content Filtering / Proxy: Similar to
application security, network-level content
ﬁltering shows a lack of dedicated solutions
and regular reviews, which are essential for
ﬁltering malicious or unwanted trafﬁc.

Email Gateway: Email gateways
primarily use standard Domain-based
Message Authentication, Reporting, and

Conformance (DMARC), and Sender Policy
Framework (SPF) conﬁgurations. However,
geo-location-based blocking and periodic
rule reviews are often missing, which
weakens phishing and spam defences.

Content Filtering / Proxy: This area
lacks dedicated solutions and consistent
rule reviews. Absence of content control
increases exposure to unﬁltered, potentially
malicious trafﬁc.

Virtual Network / Network Segregation:
Many institutions have implemented
network segmentation but often lack proper
testing and validation of these segmentation
controls. Overly broad access control
mechanisms are frequently observed, which
undermines the intended security beneﬁts
of segmentation.

Web Application Firewall (WAF): WAF
implementation is inconsistent. Many
applications are not covered, and URI paths
are not adequately tested or blocked. High
and medium threat signatures are often
set only to detect, leaving gaps in active
defences.

Application Security

Secure Configuration

IPS/IDS: There is a fair presence of Intrusion
Prevention and Detection systems. However,
medium and low severity signatures often
remain unblocked, and many organizations
lack internal IPS, posing risks to application
security.

Webserver & Database: Lack of application
hardening and limited security standards
in application design, coupled with
inadequate coordination between security
and application teams, results in a larger
attack surface and greater exposure to
vulnerabilities.

30

DIGITAL THREAT REPORT 2024

Cloud Security

General Cloud Security: Cloud
environments show signiﬁcant gaps.
Subscriptions often lack hardening per CIS
or global standards, with MFA and logging
not enabled by default. Local accounts,
sometimes exposed to the internet, increase
risk of unauthorized access.

Cloud Environment Speciﬁcs (AWS, Azure,
GCP): Common gaps include missing audit
logging for PaaS, insufﬁcient hardening, and
absent MFA. These vulnerabilities reﬂect a
need for stronger cloud access control and
monitoring.

Monitoring & Response

Security Logging: Critical logs such as
DNS, proxy, MFA, and O365 (email logs)
are not integrated by many organizations.
This lack of integration limits visibility and
hampers the ability to detect potential
threats effectively. Additionally, API-
based integrations for SAAS services
are sometimes constrained by licensing
limitations, further impacting comprehensive
threat monitoring.

SIEM Integration: SIEM integration lacks
comprehensive data feeds, such as DNS and
MFA logs, essential for threat correlation.
This hinders timely detection and response
capabilities, particularly for SAAS and cloud
environments.

31

Data Protection and Encryption

Encryption of data and masking
sensitive information – Sensitive and
conﬁdential data is not stored in encrypted
form or masked leading to a breach
of conﬁdentiality of stored data. Non-
compliance to this control may lead to
malicious entity to derive the sensitive data.

VAPT (Vulnerability Assessment and
Penetration Testing)

Internal/External vulnerabilities and
Penetration testing – Periodic vulnerability
management and penetrations testing are
not regularly followed by many ﬁnancial
institutions. Attackers routinely look for
unpatched or vulnerable externally facing
servers, which can be leveraged to launch a
directed attack. Because external networks
are at greater risk of compromise, external
vulnerability scanning must be performed
periodically.

IAM (Identity and Access
Management) Security

Identity Security: Identity security remains
a crucial gap. MFA is not universally
enforced on VPN proﬁles, and conditional
access policies are missing in a majority of
environments, which increases susceptibility
to unauthorized access.

User Access review: If excessive user
rights are not revoked or accounts for all
terminated users have not been removed
in due time, they may be used by malicious
users for unauthorized access.

Endpoint Security

Endpoint Detection and Response (EDR):
Most large ﬁnancial institutions have
implemented EDR solutions, providing
advanced detection and response
capabilities. However, some mid-sized and
smaller clients are still relying primarily
on traditional antivirus (AV) solutions with
limited EDR functionality. This limits the
scope of endpoint threat containment
and makes them more vulnerable to
sophisticated attacks that require proactive
threat hunting and automated response.

DIGITAL THREAT REPORT 2024

GAZING THROUGH THE
GAZING THROUGH THE
CRYSTAL BALL FOR 2025
CRYSTAL BALL FOR 2025

32

32

DIGITAL THREAT REPORT 2024

DIGITAL THREAT REPORT 2024

GAZING THROUGH THE CRYSTAL BALL FOR 2025

Before we dive into recommendations
This report draws on the collective
based on the gaps and vulnerabilities
expertise and insights of industry
highlighted in the previous section, it’s
leaders to provide a uniﬁed view of
crucial to shift our focus forward and grasp
the cybersecurity landscape in 2024.
how the cybersecurity landscape is set to
It reﬂects a seamless exchange of
transform in the coming year. Understanding
knowledge, shaped by real-world cyber
the trends and challenges of 2025 is not
incidents, evolving adversarial tactics, and
just valuable—it’s imperative for crafting
emerging threat intelligence.
strategies that are resilient to the threats of
tomorrow.
By integrating a national perspective on
cyber trends with frontline experience
As we peer into the future of cybersecurity,
in mitigating sophisticated attacks, this
the crystal ball reveals a landscape
report delivers a holistic understanding
dramatically reshaped by the power of
of the shifting threat environment. The
result is a comprehensive resource that
empowers organizations to anticipate
risks, strengthen defenses, and navigate
the complexities of today’s cybersecurity
challenges.

IoT devices expanding
attack surfaces

Over the past year, cyberattacks have
grown more sophisticated, driven by
the intersection of new techniques and
the persistence of proven methods.
Social engineering, in particular, has
surged to the forefront, with Business
Compromised IoT devices
provide entry points for attackers,
Email Compromise (BEC) and advanced
enabling lateral movement
phishing campaigns operating with
across networks and potentially
disrupting critical operations.
alarming precision. These attacks, often
bolstered by data sourced from the dark
web, bypass traditional defenses by
leveraging stolen credentials and session
cookies, effectively neutralizing multi-
factor authentication. Meanwhile, supply
chain breaches have escalated, exploiting
the trust organizations place in third-party
Crypto - A new frontier
vendors and open-source repositories
for cyber threats
thereby introducing vulnerabilities at
Cyber attackers exploit
scale.
cryptocurrencies for anonymous
transactions, target crypto wallets,
and attack exchanges, leading to
ﬁnancial theft and extortion.

Yet, the rising tide of cyber threats is
not occurring in isolation. As digital
ecosystems expand, so too does the
recognition that compliance must evolve
beyond rigid frameworks. This report
explores how regulatory landscapes

Drawing insights from observed threats

across the digital payment ecosystem,

we present a series of predictions for

2025 - seven highly anticipated attack

methodologies likely to dominate the threat

landscape in 2025.

These insights aim to empower

organizations with a forward-looking

perspective, guiding them to anticipate,

adapt, and fortify their defenses in the

face of an increasingly volatile cyber

environment.

artiﬁcial intelligence. Attacks in 2025 will
are shifting towards harmonization,
not only be more sophisticated but also
with the goal of unifying disparate
exponentially more evasive and pervasive.
standards across regions. Compliance
Threat actors are set to harness AI to craft
is transforming from a burdensome
highly customized assaults, leaving minimal
obligation into a strategic enabler—
trace as they operate at an unprecedented
one that can unlock growth, improve
scale—powered by the same revolutionary
operational efﬁciency, and reinforce
technologies transforming industries
resilience in sectors like digital payments,
globally. Add to that the looming quantum
where sensitive data remains a prime
computing revolution capable of rendering
target for attackers.
today’s encryption obsolete, organizations
face an evolving and complex reality.
Beneath these strategic shifts lies a more
Preparing for these seismic shifts is no
pressing reality—critical control gaps
longer optional; it’s essential for survival.
continue to persist across industries.
Weak access controls, over-privileged
user accounts, and misconﬁgurations
leave even the most fortiﬁed
organizations exposed. This report
Rise of deep fakes &
highlights how these vulnerabilities are
AI generated content
not merely by-products of oversight but
Attackers will leverage deep
structural weaknesses that adversaries
fakes to impersonate executives
consistently exploit to devastating effect.
and bypass veriﬁcation, enabling
social engineering attacks.

As the industry braces for what lies
ahead, the future of cybersecurity is
already being reshaped by artiﬁcial
intelligence (AI). The same technology
that drives innovation is arming attackers
with the tools to conduct highly
personalized, evasive, and large-scale
attacks. In 2025 and beyond, AI-driven
threats will challenge existing defense
mechanisms, forcing organizations to
rethink their approach to threat detection
ANTICIPATED CYBER
and response.
THREATS IN 2025

07

01

02

06
This report offers concrete
Identify. Defend.
recommendations rooted in frontline
Secure the future.
03
audits and incident analysis, outlining the
steps necessary to close control gaps,
strengthen defenses, and build adaptive
strategies against emerging threats. The
ﬁndings presented here serve as both a
reﬂection of the current landscape and a
guidepost for navigating the uncertainties
of tomorrow.

04

05

Growing threat of
supply chain attacks
and malicious libraries

Malicious code injected into
trusted software updates or
libraries compromises entire supply
chains, spreading vulnerabilities
across multiple organizations.

Emerging threat of
LLM prompt hacking

Attackers manipulate LLM
(Large Language Models)
inputs to extract sensitive data,
override controls, and induce
harmful outputs in local Al
applications.

Quantum computing -
A looming threat to
cryptography

Adversarial LLMs
enchaning attack
capabilities

Quantum advancements
threaten to break current
encryption methods, exposing
sensitive data and enabling
large-scale cyber espionage.

Malicious LLMs (Large Language
Models) enable attackers to
automate malware creation,
phishing campaigns, and exploit
development, intensifying the
threat landscape.

33
8

DIGITAL THREAT REPORT 2024
DIGITAL THREAT REPORT 2024

ANTICIPATED ATTACK 1:
RISE OF DEEP FAKES AND AI-GENERATED CONTENT

Attackers are expected to increasingly
leverage deep fakes and AI-generated
content as potent tools for intrusion,
particularly in social engineering attacks.
The advancement of deep fake technology
enables the creation of highly realistic and
manipulated audio and video content that
can convincingly impersonate individuals.

Deep fake voice and video allow cyber
perpetrators to mimic the voices and
appearances of executives, employees, or
trusted partners. For example, an attacker
might use a deep fake video during a
virtual meeting to deceive a ﬁnance team

for multi-factor authentication (MFA),
passwords, or other sensitive information.

The challenges in detection and veriﬁcation
of such AI-generated content are signiﬁcant.
As the technology becomes more
sophisticated and accessible, it becomes
increasingly difﬁcult for users to distinguish
between genuine and manipulated media.
Traditional veriﬁcation methods that rely
on voice recognition or visual conﬁrmation
are no longer sufﬁcient, as deep fakes can
replicate these cues with high accuracy.
This creates substantial risks, especially in
business contexts where critical decisions

into authorizing a unauthorized transfer or

and transactions are made based on virtual

employ a deep fake voice to trick individuals

interactions.

into revealing one-time passwords (OTPs)

ANTICIPATED ATTACK 2:
GROWING THREAT OF SUPPLY CHAIN
ATTACKS AND MALICIOUS LIBRARIES

Attackers are expected to increasingly

Unsuspecting developers may inadvertently

focus on supply chain attacks, exploiting

incorporate these tainted libraries into

vulnerabilities in software development

their projects, introducing vulnerabilities,

processes to compromise multiple

backdoors, or malware into their

organizations simultaneously. One

applications. This method allows attackers

primary method involves the exploitation

to spread malicious code across a wide

of code repositories. Cyber attackers

array of software products and services,

gain unauthorized access to developers’

amplifying the potential impact.

accounts on platforms like GitHub or inject

malicious code into the source code of

Furthermore, there is growing apprehension

widely used applications. By inﬁltrating the

about the inﬂuence on Large Language

development environment, attackers can

Models (LLMs). Attackers may attempt to

insert malware directly into the codebase,

manipulate LLMs or their training data to

which is then unknowingly distributed to
clients through regular software updates or
new releases. This tactic enables attackers
to bypass traditional security measures, as
the malicious code originates from a trusted
source.

Another concerning trend
is the distribution of
malicious libraries disguised
as genuine. Attackers
publish counterfeit libraries
that mimic legitimate ones,
often with names that
are deceptively similar to
popular libraries.

promote malicious libraries. By poisoning
the datasets or exploiting vulnerabilities
in the models, they can cause LLMs to
suggest or generate code that includes
compromised libraries. Developers
relying on LLMs for coding assistance or
recommendations might then integrate
these malicious components into their
applications, unknowingly propagating
vulnerabilities. Even in organizations that
prohibit direct use of LLM-generated
code, developers may still seek guidance
from these models, increasing the risk of
incorporating tainted libraries.

34

DIGITAL THREAT REPORT 2024

ANTICIPATED ATTACK 3:
EMERGING THREAT OF LLM PROMPT HACKING IN APPLICATIONS

As Large Language Models (LLMs) become
increasingly integrated into various
applications, there is a growing threat
of LLM prompt hacking, where attackers
manipulate the inputs to these models
to induce unintended and potentially
harmful behaviors. This threat is particularly
pronounced in applications that host
LLMs locally, rather than relying on APIs
from established providers like OpenAI or
Anthropic.

Locally hosted LLMs may
lack the comprehensive
safety measures and
robust security features
implemented by these
providers, making them
more susceptible to
exploitation.

Vulnerabilities in Locally Hosted LLMs

When organizations incorporate LLMs

directly into their environments, they assume

the responsibility for implementing security

measures to protect against prompt hacking

and other attacks. Many locally hosted LLMs

may not have sufﬁcient safeguards against

adversarial inputs, leaving them vulnerable.

Attackers can exploit these vulnerabilities
to manipulate the LLM’s output, leading to
unauthorized actions, disclosure of sensitive
information, or the generation of harmful
content.

Prompt Hacking Techniques and Risks

One common prompt hacking technique
involves crafting inputs that bypass the
model’s intended constraints, such as the
“grandmother exploit,” where attackers
manipulate the model into providing
disallowed information by framing the
request in a speciﬁc context.

proprietary data or personally identiﬁable

Attackers may use prompt injection attacks

information (PII) that the model has been

to override system prompts or extract

trained on.

conﬁdential data that the model has been

• Manipulate decision-making processes:

exposed to during training. In applications

Inﬂuencing the outputs of the LLM in

like chatbots, virtual assistants, or interactive

ways that could affect business decisions,

voice response (IVR) systems, attackers

customer interactions, or automated

with knowledge of the underlying LLM can

systems.

manipulate prompts to:

The risks associated with LLM prompt

• Inject malicious content: Causing

hacking are signiﬁcant, as successful

the LLM to generate harmful or

attacks can compromise data integrity,

inappropriate responses that could

conﬁdentiality, and system availability.

damage the organization’s reputation or

Organizations relying on LLMs for critical

lead to legal issues.

functions may face severe consequences,

• Exﬁltrate data: Extracting sensitive

including data breaches, ﬁnancial losses,

information from the model, such as

and erosion of customer trust.

ANTICIPATED ATTACK 4:
INFLUENCE OF ADVERSARIAL LLMS ENHANCING
ATTACK CAPABILITIES

Attackers are increasingly leveraging
adversarial Large Language Models (LLMs)
to signiﬁcantly enhance their cyberattack
capabilities, posing new challenges to
cybersecurity defenses. These malicious
LLMs—such as WormGPT, FraudGPT,
WolfGPT, and XXXGPT—are designed to
generate sophisticated and tailored cyber
threats with minimal effort. By utilizing these
advanced models, attackers can create
highly effective malware, craft convincing
phishing emails, and automate the
development of exploits.

One of the key concerns is the evasion

of traditional security measures. AI-

generated malware and exploits can adapt,
obfuscate, and mutate to avoid detection
by conventional antivirus software and
Endpoint Detection and Response (EDR)
systems.

The polymorphic nature
of AIcrafted code means
that signature-based
detection methods are less
effective, as each iteration
can appear unique while
maintaining its malicious
functionality.

Furthermore, the availability of adversarial
LLMs lowers the barrier for novice malicious
actors. Individuals with limited technical
expertise can now execute complex
cyberattacks by simply interacting with these
malicious AI models. This democratization
of advanced attack capabilities leads to an
increase in the volume and sophistication
of cyber threats, as more threat actors can
launch attacks that previously required
specialized skills.

35

DIGITAL THREAT REPORT 2024

ANTICIPATED ATTACK 5:
QUANTUM COMPUTING - A LOOMING THREAT TO CRYPTOGRAPHY

Quantum computing is set to revolutionize
the world of information technology by
introducing computational power that
vastly exceeds current capabilities. With an
exponential increase in processing speed—
sometimes described in astronomical terms
like 2 to power of 3 to the power of 1000
—quantum computers can tackle complex
problems that are practically unsolvable by
classical computers.

Current encryption methods, both
asymmetric algorithms like RSA and
symmetric algorithms such as Triple DES (3-
DES) and certain key lengths of AES (like 64-
bit AES), rely on the computational difﬁculty
of speciﬁc mathematical problems. Classical
computers ﬁnd it infeasible to solve these
problems within a reasonable timeframe,
which is why these encryption methods are
considered secure.

The introduction of
quantum computing
poses a critical threat
to all applications and
communication channels
that rely on public key
infrastructure, digital
certiﬁcates, and key
exchange protocols.

However quantum computing holds the
potential to break existing encryption
algorithms and keys that safeguard our
digital communications. Algorithms

like Shor’s algorithm can factor large

numbers and compute discrete logarithms

exponentially faster than classical

algorithms. This capability effectively

renders asymmetric encryption vulnerable.

Similarly, Grover’s algorithm can speed up

the brute-force search process, weakening

ANTICIPATED ATTACK 6:
CRYPTO: A NEW FRONTIER FOR CYBER THREATS

symmetric encryption by effectively halving
the key length.

In such a scenario, we face a situation
where the integrity of the sender in any
communication cannot be trusted. Intruders
equipped with quantum computers could
easily break encryption keys and algorithms,
enabling them to conduct man-in-the-
middle attacks. They could intercept,
decrypt, and even alter messages without
the sender or receiver being aware,
compromising the conﬁdentiality and
integrity of the communication.

Cryptocurrency has signiﬁcantly altered

Additionally, a new breed of malware

This trend has led to the development of

the cyber threat landscape, empowering

has emerged that goes beyond the

an entire ecosystem designed to support

intruders in ways that previous technologies

traditional goal of harvesting Personally

these illicit transactions. Services and

could not. Initially, the cyber perpetrators

Identiﬁable Information (PII). These

platforms have emerged to facilitate the

utilized Bitcoin for illicit transactions

sophisticated malware programs scan

exchange, laundering, and obfuscation of

due to its widespread acceptance.

infected environments not just for sensitive

cryptocurrency funds, making it easier for

However, they’ve since migrated to other

data but speciﬁcally for the presence of

intruders to monetize their activities without

cryptocurrencies like Monero (XMR),

cryptocurrency wallets or the keys that

leaving a traceable trail.

which offer enhanced privacy and non-

secure them. By extracting these keys,

traceability. Monero’s advanced encryption

intruders can gain unauthorized access to

techniques obscure transaction details,
making it exceptionally challenging for law
enforcement agencies to trace funds and
identify the individuals involved.

This shift in cryptocurrency preference has
also seen a change in the tactics employed
by intruders. They have evolved from using
compromised systems merely as crypto
miners—where infected computers are
hijacked to mine cryptocurrencies without
the owner’s knowledge—to more direct
and proﬁtable endeavours like targeting
cryptocurrency exchanges. By attacking
these exchanges, intruders aim to steal
large amounts of digital currency, exploiting
security vulnerabilities within these

platforms.

36

victims’ crypto assets, leading to signiﬁcant
ﬁnancial losses.

The evolution of
cryptocurrency has also
facilitated the rise of
ransom and data extortion
schemes. Malicious
actors now commonly
demand payment
in cryptocurrencies,
leveraging their anonymity
to avoid detection.

DIGITAL THREAT REPORT 2024

ANTICIPATED ATTACK 7:
IoT, THE EMERGING THREATS TO EMBEDDED DEVICES

Cloud-Connected Embedded Devices

Embedded devices increasingly rely on
cloud services like Amazon Elastic Compute
Cloud (AWS EC2) and Message Queuing
Telemetry Transport (MQTT) brokers to
transmit and store data. These devices
collect sensor or user data and push it
to services like AWS S3 using temporary
credentials assigned by the cloud. While
efﬁcient, this creates vulnerabilities—
compromised credentials from one device
can grant attackers access to the larger
cloud infrastructure. If thousands of devices
share identical conﬁgurations, breaching

malicious ﬁrmware, bricking devices or
causing widespread failures. Attackers can
exploit open debug interfaces to reverse
engineer ﬁrmware and tamper with the
OTA process. Since ﬁrmware is often
identical across devices, malicious updates
propagate rapidly, turning a single breach
into a system-wide threat.

Hardware Trojans, chip backdoor &
“Movie-Style” Attacks in real life

Hardware Trojans—malicious circuit
modiﬁcations—can be inserted during

one can expose the entire ﬂeet, risking

chip fabrication or assembly. Attackers

data theft, lateral movement, or operational

or nation-states can implant these rogue

disruption.

components that remain dormant until

triggered. An extra chip can be concealed

beneath a Ball Grid Array (BGA) package or

Firmware Reverse Engineering, IP

masked with high-temperature adhesives,

Theft, Digital Twins & Secret Extraction

making detection nearly impossible without

specialized forensics. These implants

Firmware holds the core intellectual

enable remote takeovers, allowing attackers

property (IP) and operational logic of

to control infrastructure with a single

embedded devices, making it a high-

command. In large-scale deployments,

value target for attackers. By reverse

compromising one node can escalate

engineering ﬁrmware, adversaries can inject

to entire networks. Lack of PCB-level

malicious code, alter device behavior, or

inspections leaves critical systems vulnerable

create “digital twins” that mimic legitimate

to these stealthy attacks.

devices while feeding manipulated data

into real systems. This can disrupt critical

operations, especially in environments

Scalability of Attacks, Mod Chips, Side-

where devices control physical processes or

Channel Analysis and Glitching

infrastructure. Additionally, ﬁrmware often

contains proprietary algorithms and secrets,

Hardware exploits, once developed, can

allowing attackers to clone products, bypass

protections, or extract shared encryption
keys embedded across entire product lines.
A single compromised device can expose an
entire ﬂeet, enabling adversaries to escalate
privileges, manipulate data, or propagate
malware across interconnected systems,
threatening IP, operational security, and
product integrity.

OTA Updates & Single-Device Pivot

Over the air (OTA) updates simplify ﬁrmware
patching but introduce signiﬁcant risk. A
compromised update server can distribute

be mass-produced through mod chips
or glitching techniques. Mod chips—
initially used to bypass gaming console
security—can scale to automotive and IoT
systems, bypassing protections at scale.
Side-channel analysis reveals sensitive
data by monitoring power consumption or
electromagnetic leaks, while voltage faults
at critical moments can bypass security
checks. These scalable methods transform
niche vulnerabilities into widespread threats,
compromising even highly secure systems.

37

DIGITAL THREAT REPORT 2024

RECOMMENDATIONS:
RECOMMENDATIONS:
STRENGTHENING YOUR
STRENGTHENING YOUR
CYBERSECURITY POSTURE
CYBERSECURITY POSTURE

38

38

DIGITAL THREAT REPORT 2024

DIGITAL THREAT REPORT 2024

RECOMMENDATIONS: STRENGTHENING
YOUR CYBERSECURITY POSTURE

Having explored the TTPs (Tactics,
Techniques, and Procedures) used by
attackers, examined unique case studies
showcasing their stealth and evasion
techniques, and gained a glimpse into
the anticipated trends of 2025, it’s time
to focus on the critical question: What
can organizations do to stay secure?

The solution lies in establishing effective,
adaptable, and forward-thinking
cybersecurity strategies.

The following section highlights the key
controls organizations should implement,
based on insights from audit and
incident analysis ﬁndings, to strengthen

defenses, mitigate vulnerabilities, and
effectively protect sensitive data. These
recommendations aim to empower
organizations to stay ahead in an ever-
evolving threat landscape while enhancing
operational efﬁciency and resilience.

ADAPTABLE, FORWARD-THINKING CYBERSECURITY IS BUILT
ON KEY CONTROLS THAT DEFEND, MITIGATE, AND PROTECT.

ENHANCING
RESILIENCE
ACROSS KEY
DOMAINS

PEOPLE
(Awareness, Training, and Culture)

• Increase the Frequency of Information Security Training
• Strengthen Risk Management and Governance
• Focus on Securing Remote and Hybrid Work Technologies

PROCESS
(Policies, Procedures, and Governance)

• Accelerate Vulnerability Assessments Time Frame
• Develop Comprehensive Incident Response Playbooks
• Integrate Threat Intelligence into Monitoring Processes
• Defense-in-depth program
• Zero Trust Architecture (ZTA) Implementation

TECHNOLOGY
(Tools, Systems, and Solutions)

• Increase the Frequency of Patching Network Devices

• Implement Al-Powered Anomaly Detection and Dark Web Monitoring

• Application and API Security

• Authentication and Access Control

• Endpoint and Email Security

• Security Testing of Al-Native Applications

39

DIGITAL THREAT REPORT 2024

BUILDING A RESILIENT PEOPLE - FORCE: STRENGTHENING CYBERSECURITY
THROUGH TRAINING, GOVERNANCE, AND REMOTE SECURITY

A strong and adaptable cybersecurity posture begins with people. Organizations must
foster a culture where cybersecurity awareness is continuous, leadership-driven, and
embedded across all levels.

Continuous Information Security
Training

Risk Management and Governance
for Long-Term Resilience

Transitioning from annual to quarterly
security training enhances resilience by
keeping employees vigilant against evolving
threats like AI-driven phishing and deepfake
scams. Frequent education ensures that
staff stay informed about emerging attack
vectors and reinforces proactive security

A proactive, comprehensive risk
management framework is essential
to enhance regulatory adherence and
fortify the overall security posture. This
framework drives transparency, enables
standardized reporting, and facilitates
benchmarking against industry best

behavior. By involving the entire workforce,

practices. Strong governance mechanisms

from executives to frontline employees,

ensure accountability, incident disclosure,

organizations establish a uniﬁed defense

and effective resource allocation to mitigate

against social engineering tactics.

risks.

Leadership plays a crucial role in shaping

Regular security assessments, incident

this culture. When executives prioritize

monitoring, and performance tracking

cybersecurity and actively champion training

through metrics—such as known

initiatives, it signals the importance of

vulnerabilities and training completion

security as part of the broader business

rates—provide actionable insights that

strategy. This top-down approach not

drive timely adjustments. Governance

only protects sensitive data but also

structures that evaluate AI-related risks,

builds customer trust and solidiﬁes the

adversarial threats, and ethical concerns

organization’s long-term success.

position organizations to address emerging

vulnerabilities before they escalate.

Securing Remote and Hybrid Work
Environments

By integrating cybersecurity governance

into the organization’s core, businesses not

only enhance regulatory compliance but

As remote and hybrid work models expand

also foster resilience against increasingly

the attack surface, organizations must

sophisticated threats. This holistic approach

secure the technologies that support

ensures that cybersecurity measures

these environments. Conducting regular

align with broader business objectives,

empowering the organization to navigate
and thrive in a complex digital landscape.

vulnerability assessments, enforcing timely
patching, and strengthening remote access
solutions are essential steps. High-proﬁle
incidents, such as the MOVEit Transfer
vulnerabilities, underscore the critical need
for ongoing vigilance in securing internet-
facing systems and remote infrastructure.

40

DIGITAL THREAT REPORT 2024

STRENGTHENING CYBERSECURITY THROUGH
PROACTIVE PROCESSES AND LAYERED DEFENSES

Effective cybersecurity relies on processes that not only anticipate threats but also
build resilience through continuous monitoring, adaptive defense strategies, and
structured responses.

By embedding dynamic processes, organizations can minimize vulnerabilities,
streamline detection, and respond swiftly to emerging threats.

Accelerated Vulnerability
Assessments

Defense-in-Depth as a Strategic
Imperative

Zero Trust Architecture (ZTA) for
Modern Threats

In today’s rapidly evolving threat landscape,
waiting for quarterly or annual vulnerability
assessments is no longer sufﬁcient.
Conducting daily or weekly assessments

No single solution can fully protect against
modern cyber threats. Defense-in-Depth
offers a layered strategy where multiple
controls—ﬁrewalls, intrusion prevention,

The traditional network perimeter is no
longer sufﬁcient as remote work, cloud
services, and mobile devices expand the
attack surface. Zero Trust Architecture (ZTA)

using automated solutions is essential to

and endpoint detection—work in tandem

enforces continuous authentication, granular

identify and mitigate weaknesses before

to detect, delay, or mitigate attacks.

access control, and micro-segmentation to

attackers exploit them. The time between

This holistic framework extends beyond

safeguard sensitive assets. By assuming that

vulnerability disclosure and exploitation

technology, incorporating policies and

no user or device can be implicitly trusted,

has drastically shortened, making real-

procedures that reinforce organizational

ZTA reduces lateral movement and limits

time scanning a critical component of

resilience. Endpoint Detection and

the damage potential of compromised

organizational security. Automated tools

Response (EDR) tools play a pivotal role

credentials or insider threats.

ensure systems are continuously monitored,

in addressing AI-driven and customized

allowing teams to prioritize remediation and

malware threats, bridging the gap left by

Proactive processes form the backbone

close security gaps swiftly.

traditional antivirus solutions. This layered

of a resilient cybersecurity strategy. By

approach creates redundancies, ensuring

accelerating assessments, embedding

that even if one control fails, others remain

intelligence, deploying layered defenses,

and implementing Zero Trust, organizations

can build robust frameworks that withstand

evolving threats.

Threat Intelligence Integration

active to contain breaches.

As adversaries grow more sophisticated,

the integration of threat intelligence into

monitoring processes is crucial. Threat

actors often share tools and vulnerabilities,

Comprehensive Incident
Response Playbooks

necessitating collective action and

Preparedness is critical. Standardized

intelligence sharing. Organizations must

playbooks for responding to diverse cyber

incorporate reputable threat feeds (such as

incidents ensure that teams act quickly,

from CERT-In) into their security frameworks

uniformly for the type of incident and

to proactively detect attack patterns. This
intelligence-driven approach enables faster
response times and anticipates threats
based on evolving tactics, strengthening
defenses across the board. By fostering
collaboration between vendors, enterprises,
and industry peers, organizations create
a uniﬁed defense that mirrors the
interconnected strategies used by threat
actors.

decisively. These playbooks guide analysis,
containment, and mitigation, reducing the
chance of oversight during critical moments.
By establishing predeﬁned response
protocols, organizations can streamline
investigations, minimizing operational
disruptions and ﬁnancial losses.

41

DIGITAL THREAT REPORT 2024

TECHNOLOGY: BUILDING RESILIENT CYBER DEFENSES

Accelerate Patching of Network
Devices

Network devices are prime targets for
attackers, with vulnerabilities in ﬁrewalls
and VPNs surging by 229% in the past year.
Zero-day exploits are being weaponized
faster, with some attacks launched within
hours of disclosure. To stay ahead,
organizations must aggressively patch
network devices on a continuous basis,
reducing exposure and closing critical
gaps before exploitation occurs. This
proactive stance is essential to safeguard

Application and API Security

Securing AI-Native Applications

APIs represent a critical attack vector,
especially in AI-native and payments
ecosystems. To mitigate threats:
• Secure APIs with strong authentication
(OAuth, JWT, API keys) and enforce IP
whitelisting.

• Use server-to-server validation to

safeguard sensitive transactions, avoiding
browser redirects.

• Implement CORS (Cross-Origin

Resource Sharing) restrictions to prevent
unauthorized domains from accessing

APIs within AI-native applications are often
overlooked during development. API
security testing must be embedded early
in the Software Development Lifecycle
(SDLC) to uncover hidden vulnerabilities.
By expanding Dynamic Application Security
Testing (DAST) to cover API endpoints,
organizations address gaps that traditional
scanning might miss. Proactive testing
against OWASP Top 10 API vulnerabilities
ensures AI systems are protected at scale.

Through a layered technological defense,

organizations can reduce exploitable

infrastructure from evolving AI-powered

APIs.

attack techniques.

AI-Driven Anomaly Detection and
Dark Web Monitoring

By locking down API access and restricting

weaknesses, safeguard sensitive operations,

sensitive documentation, organizations can

and stay resilient in the face of rapidly

reduce risks of API-driven data breaches and

evolving cyber threats.

unauthorized system interactions.

Traditional security tools fall short against

stealthy, adaptive threats. AI-powered

Endpoint and Email Security

anomaly detection continuously monitors

for irregular behaviors that evade standard

Endpoints remain a primary entry point

defenses. These systems can identify subtle

for phishing and ransomware. Application

deviations in user behavior, pinpointing

whitelisting should be enforced to block

malicious activities hidden within normal

unauthorized software, while robust email

operations. Simultaneously, dark web

and web ﬁlters intercept phishing attempts

monitoring ensures early detection of

and malicious advertisements. Keeping

compromised credentials, allowing

antivirus solutions updated and restricting

organizations to enforce rapid password

unnecessary remote-access tools further

resets and mitigate potential breaches

strengthens endpoint defenses. Limiting

before they escalate.

exposure at this level reduces the likelihood

of breaches escalating across the network.

Strengthen Authentication and
Access Control

Multi-Factor Authentication (MFA) must
be enforced across all sensitive ﬁnancial
operations (e.g., NEFT/RTGS). This ensures
robust identity veriﬁcation and mitigates
insider threats. Strict access control lists
should be maintained and regularly
reviewed to prevent overprovisioned
accounts. Applying the principle of least
privilege reduces unnecessary access,
narrowing the attack surface and minimizing
potential damage from compromised
accounts.

42

DIGITAL THREAT REPORT 2024

CONCLUSION
CONCLUSION

43

43

DIGITAL THREAT REPORT 2024

DIGITAL THREAT REPORT 2024

CONCLUSION

And with that, CERT-In, CSIRT-Fin and

interconnected systems, requires constant

SISA wrap up this year’s journey through

vigilance and adaptability to protect against

the shifting sands of the cybersecurity

emerging risks.

landscape. We hope this report has

provided you with meaningful insights,

We hope this report serves as a valuable

actionable takeaways, and maybe even

resource in helping you identify potential

a fresh perspective on the challenges we

vulnerabilities, prepare for the unexpected,

collectively face.

and prioritize investments in your

cybersecurity strategies. At the heart of this

The BFSI industry stands at a unique

effort is the shared goal of building a secure

intersection of opportunity and risk. As

digital society—one that safeguards trust,

non-cash transactions continue to grow at

innovation, and growth.

an extraordinary pace, fueled by the shift

to e-commerce and the digitization of B2B

We want to extend our heartfelt thanks

payments, the sector is transforming into
an increasingly complex ecosystem. While
these advancements open new doors for
innovation and customer engagement, they
also present attractive targets for cyber
adversaries seeking to exploit vulnerabilities
for gain.

to the many contributors who helped
bring this report to life, from data partners
to researchers, whose expertise and
collaboration made it possible. And to you,
our readers, thank you for your continued
engagement, feedback, and commitment to
advancing cybersecurity.

The journey to secure this ecosystem is far
from over. Threats are constantly evolving,
and as technology advances, so do the
tactics and motives of those seeking to
disrupt it. The digital payments sector, with
its immense value and increasing reliance on

The road ahead will undoubtedly be ﬁlled
with challenges, but with the right insights,
preparation, and dedication, it’s a road we
can navigate together. Here’s to building a
safer and more secure future for all.

ACKNOWLEDGEMENTS

We express our deepest gratitude to our

Team for the Indian Financial Sector) and

customers and partners, whose trust and

CERT-In (Indian Computer emergency

collaboration are the cornerstone of our

Response Team), whose contributions have

efforts. Engaging with them not only helps

been instrumental in the creation of this

us exchange knowledge but also drives our

report. Their ability to synthesize ﬁndings,

continuous growth and learning. Together,

provide insights, and bring this analysis to

we share a vision of building a more secure

life underscores the incredible talent, depth

and resilient digital ecosystem.

and dedication within the respective teams.

A huge thanks to SISA’ites, ofﬁcers of CSIRT-
Fin (Computer Security Incident Response

This report is a product of collective effort, collaboration,
and shared commitment to cybersecurity, and we are
immensely grateful to everyone who made it possible.

44

DIGITAL THREAT REPORT 2024

REFERENCES

1. https://www.ibm.com/reports/data-breach
2. https://www.business-standard.com/ﬁnance/news/average-cost-of-data-breaches-in-

india-hits-2-18-million-rbi-report-124072900610_1.html

3. https://www.ﬁnancialexpress.com/life/technology-phishing-attacks-on-ﬁnancial-sectors-

soar-in-india-increasing-by-175-in-2024-report-3669276/

4. SISA Forensics Investigations
5. SISA Forensics Investigations
6. Verizon DBIR 2024: Five Compelling Stats
7. https://cointelegraph.com/news/engineer-hacks-trezor-wallet-recovers-2m-in-lost-crypto
8. https://panaseer.com/resources/reports/2022-security-leaders-peer-report

https://www.shareﬁle.com/resource/blogs/cybersecurity-trends

https://www.beyondtrust.com/blog/entry/beyondtrust-cybersecurity-trend-predictions

https://blog.shi.com/cybersecurity/are-you-protected-2025s-top-cybersecurity-trends-and-strategies-to-follow-now/

https://medium.com/@DataFlowX/the-future-of-cybersecurity-predictions-and-trends-for-2025-21e95173d1e9

https://www.pwc.com/gx/en/tmt/5g/pwc-securing-5gs-future.pdf

https://www.shareﬁle.com/resource/blogs/cybersecurity-trends

https://www.beyondtrust.com/blog/entry/beyondtrust-cybersecurity-trend-predictions

https://blog.checkpoint.com/security/2025-cyber-security-predictions-the-rise-of-ai-driven-attacks-quantum-threats-and-social-media-

exploitation/

https://www.weforum.org/stories/2024/10/cyber-resilience-emerging-technology-ai-cybersecurity/

https://www.forbes.com/councils/forbestechcouncil/2024/07/11/the-future-of-cybersecurity-emerging-threats-and-how-to-combat-them/

https://blog.checkpoint.com/research/ransomwares-evolving-threat-the-rise-of-ransomhub-decline-of-lockbit-and-the-new-era-of-data-

extortion/

https://www.scworld.com/news/north-korean-nation-state-threat-actor-using-play-ransomware

https://www.datacenterknowledge.com/data-storage/evolving-ransomware-threats-why-ofﬂine-storage-is-essential-for-modern-data-

protection

https://www.scmr.com/article/regulations-are-forcing-organizations-to-address-software-supply-chain-security/procurement

https://cybersecurityventures.com/software-supply-chain-attacks-to-cost-the-world-60-billion-by-2025/

https://www.scmr.com/article/supply-chain-cyberattacks

https://venturebeat.com/security/forresters-ciso-budget-priorities-for-2025-focus-on-api-supply-chain-security/

https://cybersecurity-magazine.com/why-are-supply-chain-attacks-increasing/

https://www.infosecurityeurope.com/en-gb/blog/threat-vectors/supply-chain-attacks-cyber-threat.html

https://ﬁntechmagazine.com/articles/why-the-ﬁnance-sector-grapples-with-software-security-debt
https://hbr.org/2024/10/phishing-attacks-are-evolving-heres-how-to-resist-them
https://ﬂashpoint.io/blog/russian-apt-groups-cyber-threats/
https://www.thisdaylive.com/index.php/2024/09/26/top-vulnerabilities-in-iot-devices-what-hackers-target-how-to-defend-against-them/
https://www.zscaler.com/press/zscaler-threatlabz-ﬁnds-400-increase-iot-and-ot-malware-attacks-year-over-year-underscoring
https://www.paymentsjournal.com/asia-overtakes-north-america-as-leading-crypto-development-hub/
https://www.statista.com/statistics/1393453/crypto-payments-global-market-size/
https://www.darkreading.com/cyberattacks-data-breaches/cryptocurrency-attacks-quadrupled-cybercriminals-cash-in
https://www.thomsonreuters.com/en-us/posts/government/identity-theft-drivers/
https://venturebeat.com/security/how-ai-driven-identity-attacks-are-deﬁning-the-new-threatscape/
https://www.scworld.com/resource/why-identity-has-become-a-trojan-horse-and-what-to-do-about-it
https://www.techbusinessnews.com.au/blog/ai-driven-cyber attacks-the-alarming-surge/
https://www.londondaily.news/unlocking-the-potential-of-5g-technology-opportunities-and-challenges-ahead/
https://www.techradar.com/pro/the-rise-of-identity-related-cyberattacks-costs-challenges-and-the-role-of-ai
https://www.techmagic.co/blog/ai-in-cybersecurity
https://www.micromindercs.com/blog/ai-threat-intelligence-empowering-cybersecurity
https://securityintelligence.com/articles/3-proven-use-cases-for-ai-preventative-cybersecurity/

https://www.intelligentcio.com/eu/2024/04/22/the-role-of-cybersecurity-in-securing-critical-infrastructure/

45

DIGITAL THREAT REPORT 2024

REFERENCES

https://www.auditboard.com/blog/security-vs-compliance/
https://www.tripwire.com/state-of-security/compliance-vs-security-striking-right-balance-cybersecurity
https://www.scrut.io/post/how-to-prevent-cyberattacks-by-balancing-security-and-compliance
https://www.securitymagazine.com/articles/99259-compliance-and-security-are-two-sides-of-the-same-coin
https://www.tripwire.com/resources/guides/mind-the-cybersecurity-compliance-gap
https://www.csoonline.com/article/1309993/grc-impact-and-challenges-to-cybersecurity.html
https://www.mckinsey.com/industries/ﬁnancial-services/our-insights/global-payments-in-2024-simpler-interfaces-complex-reality
https://cxotoday.com/interviews/turning-data-breaches-into-opportunities-strategies-for-indian-businesses-to-strengthen-cybersecurity-and-
reduce-risks/
https://www.scworld.com/resource/building-cybersecurity-resilience-strategies-technologies-and-best-practices-from-industry-leaders
https://www.techtarget.com/searchsecurity/tip/5-tips-for-building-a-cybersecurity-culture-at-your-company
https://www.weforum.org/stories/2024/04/cybersecurity-key-strategies-cyber-resilience-2024/
https://www.techtarget.com/searchsecurity/feature/Security-posture-management-a-huge-challenge-for-IT-pros
https://www.techtarget.com/healthtechsecurity/feature/Navigating-cyber-insurance-coverage-as-threats-evolve
https://www.helpnetsecurity.com/2024/07/05/iot-security-privacy-challenges/

https://www.paloaltonetworks.com/cybersecurity-perspectives/how-to-secure-iot-in-ﬁnancial-services

https://securityintelligence.com/articles/what-are-the-risks-of-the-iot-in-ﬁnancial-services/

https://www.statista.com/statistics/1183457/iot-connected-devices-worldwide/

46

DIGITAL THREAT REPORT 2024

SISA

SISA is a forensics-driven cybersecurity company solutions provider specializing in

securing the digital payments industry. As a Global Payment Forensic Investigator of the

PCI Security Standards Council, we leverage forensics insights into preventive, detective,

and corrective security solutions, protecting 1,000+ organizations across 40+ countries

from evolving cyberthreats. Our suite of solutions from AI-driven compliance, advanced

security testing, agentic detection/ response and learner focused-training has been

honored with prestigious awards, including from Financial Express, DSCI-NASSCOM and

The Economic Times. With commitment to innovation, and pioneering advancements in

Quantum Security, Hardware Security, and Cybersecurity for AI, SISA is shaping the future

of cybersecurity through cutting-edge forensics research.

CERT-In

CERT-In is the national agency for responding to computer security incidents as and

when they occur. In the Information Technology Amendment Act 2008,CERT-In has

been designated to serve as the national agency to perform the following functions
in the area of cyber security:

•
•
•
•
•

•

Collection,analysis and dissemination of information on cyber incidents.
Forecast and alerts of cyber security incidents.
Emergency measures for handling cyber security incidents.
Coordination of cyber incident response activities.
Issue guidelines,advisories,vulnerability notes and whitepapers relating to information
security practices,procedures, prevention,response and reporting of cyber incidents.
Such other functions relating to cyber security as may be prescribed
Refer www.cert-in.org.in for more details

CSIRT-Fin

Computer Security Incident Response Team in Finance sector (CSIRT-Fin) , is a
nodal sectoral CSIRT which provides Incident Prevention and Response services
as well as Security Quality Management Services to the entities of the Indian
ﬁnancial sector. It manages cyber incidents and coordinate responses across
banking, securities market infrastructure, insurance, and pension funds entities.

It carries out the following roles related to the cyber security in ﬁnancial sector:

i.

Collection, analysis & dissemination of information on cyber incidents.

ii.

Forecast and alerts on cyber security incidents.

iii.

Emergency measures on cyber security incidents.

iv.

Coordination for cyber incident response activities.

v.

Issue guidelines, advisories, vulnerability, and white papers relating to

information security.

vi.

Monitor sectoral efforts in the ﬁnancial sector towards maintaining

dynamic and modern cyber security architecture, developing awareness

amongst regulated entities and public in general.
Such other functions relating to cyber security in the ﬁnancial sector, as may

vii.

be prescribed.

47

DIGITAL THREAT REPORT 2024

48

DIGITAL THREAT REPORT 2024