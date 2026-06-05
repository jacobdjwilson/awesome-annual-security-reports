# Global Incident Response Report 2026

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [Emerging Threats and Trends](#emerging-threats-and-trends)
  - [Trend 1: AI Has Become a Force Multiplier for Attackers](#trend-1-ai-has-become-a-force-multiplier-for-attackers)
  - [Trend 2: Identity Is the Most Reliable Path to Attacker Success](#trend-2-identity-is-the-most-reliable-path-to-attacker-success)
  - [Trend 3: Software Supply Chain Attacks Increasingly Drive Downstream Disruption](#trend-3-software-supply-chain-attacks-increasingly-drive-downstream-disruption)
  - [Trend 4: Nation-State Actors Are Adapting Tactics to Modern Environments](#trend-4-nation-state-actors-are-adapting-tactics-to-modern-environments)
- [Inside the Intrusion](#inside-the-intrusion)
  - [The Attack Surface: Intrusions Span the Enterprise](#the-attack-surface-intrusions-span-the-enterprise)
  - [The Entry Point: Initial Access Comes from Predictable Paths](#the-entry-point-initial-access-comes-from-predictable-paths)
  - [Velocity: The Fastest Attacks Are Getting Faster](#velocity-the-fastest-attacks-are-getting-faster)
  - [The Impact: Extortion Beyond Encryption](#the-impact-extortion-beyond-encryption)
- [Recommendations for Defenders](#recommendations-for-defenders)
- [Appendix](#appendix)
- [Methodology](#methodology)

---

## Executive Summary

WE SEE FOUR MAJOR TRENDS THAT WILL SHAPE THE THREAT LANDSCAPE FOR 2026.

First, **AI has become a force multiplier for threat actors**. It compresses the attack lifecycle, from access to impact, while introducing new vectors. This speed shift is measurable: in 2025, exfiltration speeds for the fastest attacks quadrupled.

Second, **identity has become the most reliable path to attacker success**. Identity weaknesses played a material role in almost 90% of Unit 42 investigations. Attackers increasingly log in with stolen credentials and tokens, exploiting fragmented identity estates to escalate privileges and move laterally.

Third, **software supply chain risk has expanded beyond vulnerable code to the misuse of trusted connectivity**. Attackers exploit software-as-a-service (SaaS) integrations, vendor tools and application dependencies to bypass perimeters at scale. This shifts the impact from isolated compromise to widespread operational disruption.

Fourth, **nation-state actors are adapting stealth and persistence tactics to modern enterprise operating environments**. These actors increasingly relied on persona-driven infiltration (fake employment, synthetic identities) and deeper compromise of core infrastructure and virtualization platforms, with early signs of AI-enabled tradecraft used to reinforce these footholds.

In more than 750 incident response (IR) engagements, 87% of intrusions involved activity across multiple attack surfaces. This means defenders must protect endpoints, networks, cloud infrastructure, SaaS applications and identity together. Further, nearly half (48%) involved browser-based activity.

Most breaches were enabled by exposure, not attacker sophistication. In over 90% of breaches, preventable gaps materially enabled the intrusion: limited visibility, inconsistently applied controls, or excessive identity trust.

---

## Introduction

In 2025, Unit 42 responded to more than 750 major cyber incidents. Our teams worked with large organizations facing extortion, network intrusions, data theft and advanced persistent threats. 

Each intrusion tells a story: what the attacker targeted, how they gained access, how the activity escalated and what could have stopped it sooner. Over the past year, attack speeds continued to accelerate. AI reduces friction across reconnaissance, social engineering, scripting, troubleshooting and extortion operations. 

Despite these changes, security is solvable. In more than 90% of incidents, misconfigurations or lapses in security coverage materially enabled the intrusion.

---

## Emerging Threats and Trends

### Trend 1: AI Has Become a Force Multiplier for Attackers
AI is changing the economics of intrusions. It increases attacker speed, scale and effectiveness while opening entirely new attack vectors.

*   **Faster vulnerability exploitation**: Threat actors are automating the "monitor > diff > test > weaponize" loop. Attackers start scanning for newly discovered vulnerabilities within 15 minutes of a CVE being announced.
*   **Parallelized targeting**: AI-assisted workflows allow actors to run reconnaissance and initial access attempts across hundreds of targets in parallel.
*   **Ransomware at scale**: AI reduces manual work during deployment (script generation, templating) and extortion (messaging consistency).
*   **New Attack Vectors**: "Living off the AI land" (LOTAIL) involves weaponizing legitimate AI platforms and embedded assistants to escalate privileges or exfiltrate data.

### Trend 2: Identity Is the Most Reliable Path to Attacker Success
Identity weaknesses played a material role in nearly all (90%) of the investigations Unit 42 handled. 

*   **Initial Access**: 65% of initial access is driven by identity-based techniques, including identity-related social engineering (33%), credential misuse/brute force (21%), and identity policy/insider risk (11%).
*   **Excessive Permissions**: Unit 42 analysis of more than 680,000 identities across cloud accounts found that 99% of cloud users, roles and services had excessive permissions.
*   **Expanding Surface**: The rise of machine and AI identities, shadow identities, and identity silos creates areas where attackers operate with reduced visibility.

### Trend 3: Software Supply Chain Attacks Increasingly Drive Downstream Disruption
Supply chain risk is no longer limited to vulnerable code. It now includes SaaS integrations, vendor management planes and complex dependency ecosystems.

*   **SaaS Integrations**: Data from SaaS applications was relevant to 23% of cases in 2025. OAuth apps and API keys often carry inherited permissions that attackers exploit.
*   **Dependency Sprawl**: Over 60% of vulnerabilities in cloud-native applications reside in transitive libraries.
*   **Vendor Tools**: 39% of command-and-control (C2) techniques were related to remote access tools (T1219).

### Trend 4: Nation-State Actors Are Adapting Tactics to Modern Environments
Across campaigns affiliated with China, North Korea and Iran, we observed:
*   Greater use of identity-driven access.
*   Deeper compromise of infrastructure and virtualization layers.
*   Early experiments with AI-enabled tradecraft (e.g., deepfake identity creation, automated C2 generation).

---

## Inside the Intrusion

### The Attack Surface: Intrusions Span the Enterprise
![Chart showing attack surfaces: Identity (89%), Endpoints (61%), Network (50%), Human (45%), Cloud Apps (26%), Email (27%), SecOps (10%), Database (1%)].

### The Entry Point: Initial Access Comes from Predictable Paths
Phishing and vulnerability exploitation tied as the leading initial access vectors, each at 22%. 

### Velocity: The Fastest Attacks Are Getting Faster
The quickest quartile of intrusions reached exfiltration in 72 minutes in 2025, down from 285 minutes in 2024.

### The Impact: Extortion Beyond Encryption
Encryption appeared in 78% of extortion cases in 2025, a decline from previous years. Attackers are increasingly using data theft and harassment as leverage without needing to lock files.

---

## Recommendations for Defenders

1.  **Reduce Exposure**: Secure the application ecosystem, including third-party dependencies and integrations, and harden the browser.
2.  **Advance Zero Trust**: Tighten identity and access management (IAM) to remove excessive trust and limit lateral movement.
3.  **Automate Response**: Ensure the security operations center (SOC) can detect and contain threats at machine speed by consolidating telemetry and automating response.
4.  **Phishing-Resistant MFA**: Prioritize FIDO2/WebAuthn hardware keys for high-value roles.
5.  **Inventory Machine Identities**: Establish continuous discovery for non-human identities (service accounts, API keys).

---

## Appendix
*(Content omitted in source)*

## Methodology
*(Content omitted in source)*

---

d negotiation in limiting financial exposure.
The choice to pay remains highly situational, influenced by operational impact, regulatory considerations, legal
requirements and business continuity needs. In 2025 cases where negotiations occurred, the median reduction between
initial demand and final payment increased from 53% to 61%. This demonstrates how frequently experienced negotiators
can reduce costs even as overall attacker pricing trends upward.
Many ransomware groups now operate with business-like structures including defined roles, affiliate programs and
repeatable negotiation playbooks. Some cultivate “brand reputation” through dark web communications, portraying
themselves as predictable or professional counterparts.
This brand maintenance extends to promise-keeping: in our 2025 dataset, threat actors fulfilled their commitments (such
as providing decryption keys or allegedly deleting stolen data) in 68% of cases where they made a promise. For defenders,
these recognizable patterns can provide leverage, though they never eliminate the risk of engaging with criminal actors.
Recovery practices also shape extortion outcomes. About 41% of victims were capable of restoring systems from backup
without needing to pay, which reduced the operational impact of encryption but did not eliminate downtime. Even with
recovery, many organizations still faced system rebuilds, containment work and other delays before returning to normal
operations. Restoration is also fragile: in 26% of extortion cases, attackers impacted backups, adding further disruption.
When encryption is mitigated through backup restoration, or when backups fail entirely, the threat of exposure continues to
pressure victims, ensuring data theft remains central to extortion activity.
The Global Incident Response Report 2026 27

SSeeccttiioonn 0034 Section 04
SECTION 4.
Recommendations
for Defenders
This section identifies the systemic weaknesses
that enable attacks and the practical steps
required to stop them. By addressing the
root causes rather than just their symptoms,
organizations can elevate their defenses to
withstand both common and emerging threats.
The Global Incident Response Report 2026 28

Section 04 Section 04
4.1.
Common
Contributing Factors:
Why Attacks Succeed
87%
Attacker success is rarely about zero-day exploits. Across the incidents we responded
to in 2025, we found that in more than 90% of incidents, preventable gaps in
coverage and inconsistently applied controls directly contributed to the intrusion. of investigations
drew on evidence
These gaps determine how easily an attacker gains initial access, how quickly they from two or more
move laterally, and whether defenders can detect and respond in time. Across this distinct sources
year’s investigations, three systemic conditions appeared repeatedly.
1.
VISIBILITY GAPS: MISSING CONTEXT DELAYS DETECTION
Many organizations fail to leverage the telemetry needed to observe early-stage attacker behavior. Critical indicators of initial access and
early attacker activity often go unnoticed because the SOC has not operationalized signals across endpoint, network, cloud and SaaS
layers. The result is missing context: defenders might see individual events, but lack the correlation to recognize an active intrusion.
This fragmentation forces responders to manually reconstruct attacks from disparate tools, creating delays that attackers exploit. In 87%
of incidents, Unit 42 investigators reviewed evidence from two or more distinct sources to establish what happened, with complex
cases drawing on as many as 10. A lack of unified visibility consistently slowed detection, allowing adversaries to begin lateral movement
before defenders could see the full picture.
2.
ENVIRONMENTAL COMPLEXITY: INCONSISTENCY CREATES THE PATH OF LEAST RESISTANCE
Security baselines are rarely applied universally. Over time, environmental drift, driven by legacy systems, technology
adoption or merger and acquisition activity, makes it difficult to enforce a consistent standard across the enterprise.
In multiple investigations, critical controls like endpoint protection were fully deployed in one business unit yet missing or degraded in
another. This inconsistency creates a path of least resistance. Over 90% of data breaches were enabled by misconfigurations or gaps in
security coverage, rather than novel exploits.
3.
IDENTITY: EXCESSIVE TRUST LEADS TO LATERAL MOVEMENT
Across our investigations, identity weaknesses repeatedly turned an initial foothold into broader access. The core issue was
often excessive trust—privileges and access paths that were too permissive or remained in place long after they were needed.
Attackers escalated privileges by misusing unretired legacy roles and over-permissioned service accounts. Rather than breaking in,
they advanced by using valid access where the organization had left too much trust behind.
These failures reflect identity drift. As permissions accumulate and exceptions persist, intruders encounter fewer barriers.
Nearly 90% of incidents trace back to an identity-related element as a critical source of the investigation or a primary attack vector.
The Global Incident Response Report 2026 PB The Global Incident Response Report 2026 29

Section 04
4.2.
Recommendations
for Defenders
The recommendations that follow
focus on practical steps to address
the systemic conditions described above.
1.
EMPOWER SECURITY OPERATIONS
TO DETECT AND RESPOND FASTER
With the fastest attacks now exfiltrating data in roughly an hour, security
operations must move at machine speed. This comes from empowering the SOC
with comprehensive visibility across the enterprise, AI to identify the signal in the
noise, and automation to drive immediate response and remediation. Adopting
these six capabilities will put your SOC in the best position to succeed:
Ingest all relevant security data. Attackers do not operate in silos, yet defenders often monitor in them. In
2025, visibility gaps—particularly across SaaS, cloud identity and automation layers—were a primary driver
of attacker success. Critical telemetry often existed but remained trapped in disparate systems, preventing
defenders from correlating identity shifts with automation outputs or browser-stored artifacts like session tokens.
To detect modern intrusions, organizations must ingest and normalize signals from identity providers, cloud
platforms and SaaS applications into a unified view. This consolidation closes the weak spots attackers exploit,
allowing defenders to identify escalation routes early. Whether using rule-based detection or AI, the quality of
insight depends entirely on the completeness of the data feeding it.
Prevent, detect and prioritize threats with AI-driven capabilities. High alert volumes and fragmented
tools allow attackers to hide by spreading activity across systems. Without correlation, these actions appear
unrelated, delaying escalation. AI-driven capabilities are essential to stitch these disparate signals into a unified
operational view. Behavioral analytics help surface subtle anomalies, such as unusual token use or lateral
movement through cloud automation, that rule-based detection often fails to catch.
AI strengthens defense by correlating events across identity, endpoint, cloud and network layers, prioritizing
high-fidelity incidents over background noise. This allows security teams to distinguish coordinated attacks from
routine activity instantly, ensuring analysts focus their efforts on the threats that pose the greatest risk rather
than chasing false positives.
Enable real-time threat response with automation. Delays in containment often stem from unclear ownership
and manual validation steps that cannot keep pace with attacker automation. Effective response requires
assigning explicit authority for automated containment actions, such as revoking tokens or isolating workloads,
so that execution can proceed without hesitation.
The Global Incident Response Report 2026 30

Section 04 Section 04
By replacing ad hoc judgment with standardized, validated playbooks, organizations ensure that response
follows an auditable sequence. However, to meet the pace of modern threats, agentic AI must be deployed
as the ultimate defense accelerator. These autonomous systems dynamically investigate complex alerts,
correlating data across domains at machine speed to gain a complete picture.
Once validated, agents are authorized to execute dynamic, surgical containment actions, from isolating
affected systems via microsegmentation to automatically revoking compromised credentials. This disciplined,
intelligent approach dramatically reduces operational drift, limits attacker dwell time and prevents isolated
compromises from escalating into broader incidents.
Transition from reactive to proactive security. To shift from reactive defense, organizations must move
beyond traditional pentesting to continuous adversarial testing. Point-in-time audits rarely capture the
interplay of identity drift and cloud misconfigurations that attackers exploit in real-world intrusions. Defenders
need to validate how controls perform under realistic conditions, ensuring telemetry pipelines and response
workflows operate as intended.
Proactivity extends to recovery. Resilient organizations verify that systems are free of residual access, such
as compromised credentials or altered configurations, before restoring services. Ensuring that remediation
addresses root causes, rather than simply restoring outdated snapshots, helps prevent rapid reinfection and
supports long-term resilience.
Uplevel the SOC for high-performance outcomes. During active incidents, inconsistent containment or
unclear ownership creates openings for attackers to re-establish access. High-performance SOCs eliminate
this variance by ensuring response actions are applied uniformly, regardless of the analyst or time of day.
Consistency under pressure is critical; it prevents isolated compromises from escalating into broader crises.
Achieving this requires bridging operational silos across Security, IT, and DevOps. Playbooks should reflect
how systems operate today, rather than how they were originally designed, so that automated actions align
with real business logic. Empowering analysts with broader responsibility, such as end-to-end incident
response rather than alert triage alone, improves retention, increases versatility and drives measurable
business outcomes.
Deepen your bench with an IR retainer. The right retainer extends your capabilities beyond emergency
response. To stay ahead, organizations must test and validate controls against the specific behaviors threat
actors use in the wild. Recurring assessments across offensive security, AI security, SOC processes and
cloud security help confirm that telemetry pipelines and response workflows operate as intended under
realistic attack conditions.
Your IR retainer partner should provide rapid access to specialists for proactive readiness checks, detection
engineering and validation, ensuring that defensive improvements hold up over time. By pairing continuous
testing with retained expertise, organizations improve resilience.
By aligning your SOC with these core principles, you transform your defense into a high-velocity response
engine capable of outmaneuvering adversaries and stopping threats before they escalate.
The Global Incident Response Report 2026 30 The Global Incident Response Report 2026 31

Section 04 Section 04
2.
ADOPT ZERO TRUST TO CONSTRAIN THE AREA OF IMPACT
Zero trust is a strategic necessity in an environment where identity has become the primary attack surface. The goal is to eliminate implicit
trust relationships between users, devices and applications and to continuously validate every stage of a digital interaction.
In reality, achieving zero trust is complex. However, even small gains will reduce the attack surface, constrain lateral movement and minimize
the impact of any initial access to your environment. By removing the assumption of safety inside the perimeter, defenders force attackers to
work harder for every inch of access, slowing their velocity and creating more opportunities for detection.
Continuously verify users, devices and applications. Attackers frequently exploit the static trust that persists after
an initial login. Once inside, they use stolen session tokens or valid credentials to masquerade as legitimate users, often
bypassing perimeter controls entirely. Static checkpoints at the front door are no longer sufficient.
Continuous verification treats trust as dynamic, with decisions revisited as conditions change during a session. Validating
identity context, device health and application behavior in real time allows organizations to detect when a legitimate session
is hijacked or when user behavior deviates from the norm. As a result, compromised accounts or devices remain useful to
attackers for only a limited period, reducing opportunities to expand access or stage data.
Enforce least privilege to constrain attacker movement. Excessive permissions act as a force multiplier for attackers. In
many 2025 incidents, intruders bypassed internal controls by taking advantage of identity drift, using accumulated privileges
and unretired roles that organizations failed to remove. Rather than relying on complex exploits, they moved laterally through
valid but over-provisioned access paths.
Enforcing least privilege reduces this attack surface by limiting users, services and applications to only the access required
for their function. This must extend beyond human users to include machine identities and service accounts, which often
retain broad, poorly monitored permissions. Removing unnecessary rights eliminates the straightforward access paths
attackers rely on, forcing them into more visible and difficult techniques that are easier for defenders to detect.
Apply consistent inspection across trusted and untrusted traffic. Apply consistent inspection across trusted and
untrusted traffic. Attackers know that while the perimeter is guarded, internal “east–west” traffic between workloads often
passes without inspection. They exploit this trust by using encrypted internal connections to move laterally and stage data
without triggering alarms.
To achieve consistent, pervasive threat analysis, organizations must consolidate all network, cloud and secure access
service edge (SASE) security onto a single unified platform. This unified fabric delivers consistent Layer 7 inspection
everywhere, automatically enforcing policy via one management plane.
This consolidation enables the strategic shift to advanced cloud-delivered security services. This shift allows real-time, inline
analysis of all traffic, including crucial decryption and inspection of traffic moving between internal workloads. This capability
removes the spots where attackers hide, proactively stopping unknown phishing, zero-day malware and evasive C2 activity.
Control data access and movement to reduce impact. The most damaging outcomes in many incidents occur not at
initial compromise but during subsequent data access, staging and exfiltration. Attackers often search for repositories with
weak controls or poorly monitored flows to quietly aggregate sensitive information before detection.
Stronger governance over how data is accessed, shared and transferred reduces these opportunities by limiting where
sensitive information can move and under what conditions. When data pathways are tightly controlled and consistently
monitored, attackers face fewer options to prepare or extract valuable assets, reducing the scale and severity of potential
loss even when a compromise occurs.
By systematically eliminating implicit trust, you strip attackers of the mobility they rely on, ensuring
that a single point of compromise leads to a contained incident rather than an enterprise-wide crisis.
The Global Incident Response Report 2026 PB The Global Incident Response Report 2026 32

Section 04
3.
STOP IDENTITY ATTACKS WITH STRONGER
IDENTITY AND ACCESS MANAGEMENT
Identity is now the security perimeter, yet it too often remains poorly secured. Identity weaknesses were a determining
factor in over half of the intrusions investigated in 2025, primarily because identity stores expanded faster than the controls
intended to govern them.
Attackers consistently moved through the gaps created by this governance drift, exploiting
legacy permissions and unmonitored service accounts to bypass perimeter defenses. To stop this, organizations must
manage identity not as a static list of credentials, but as a dynamic operational asset across the entire lifecycle.
Centralize identity management for humans and machines. You cannot govern what you cannot see. When
identity data is fragmented across legacy directories, cloud providers and SaaS environments, attackers take
advantage of the resulting weak spots.
Centralizing user and machine identities into authoritative directories simplifies authentication and removes hidden
access paths that are difficult to monitor consistently. This consolidation should also include third-party integrations
and API connectors so that every entity requesting access, whether a person, a service account or an AI agent,
is visible to security teams. With a unified control plane in place, defensive AI can correlate login anomalies with
suspicious activity, turning identity into an active operational signal rather than a static list of credentials.
Combat governance drift with continuous lifecycle management. Governance drift, where operational changes
move faster than the controls designed to guide them, remained a significant contributor to attacker leverage.
Role transitions, rapid deployment cycles and everyday shortcuts widened the gap between written policy and actual
access. Permissions held by workflow tools and service connectors often exceeded what policy intended. This created
escalation paths that attackers exploited through legacy permissions and unmonitored service accounts. Treating
identity as a lifecycle, by limiting automation to current needs and retiring excess access over time, helps close these
gaps and restrict attacker movement after initial access.
Detect and respond to identity-based threats. Defensive AI performs most effectively in environments where
identities are managed as operational assets rather than static credentials. In our investigations, organizations with
strong identity foundations showed earlier linkage between login anomalies, automation activity and peripheral identity
events, which contributed to faster containment.
Where governance was strong, detection pipelines produced clearer and more reliable indicators that helped teams
identify escalation behavior earlier. In contrast, weak governance created noise that obscured these signals. Regular
reviews keep permissions aligned to real requirements, improving the accuracy of detection signals and ensuring that
AI-assisted controls operate effectively.
Secure AI and automation integrity. As organizations embed AI agents and automated workflows into core
processes, these systems become attractive targets for manipulation. In our investigations, we observed assistant
accounts deployed with broad default access and automation tools running without integrity validation.
To prevent these tools from becoming vectors for attack, security teams must apply the same governance
rigor to AI systems as they do to human users. This includes explicitly validating automation steps before
they enter production, applying integrity checks to AI-enabled workflows and ensuring that assistant
accounts are hardened against misuse.
By treating identity as a dynamic operational system rather than a static directory, you eliminate the
hidden pathways attackers rely on and enable security teams to detect misuse the moment it occurs.
The Global Incident Response Report 2026 33

Section 04
4.
SECURE THE APPLICATION LIFECYCLE FROM CODE TO CLOUD
Protecting the modern enterprise requires more than securing infrastructure. It requires securing the factory that builds it.
In 2025, attackers increasingly targeted the software supply chain and cloud APIs to bypass traditional perimeters, injecting vulnerabilities
into code or exploiting weak integrations before they ever reached production. To counter this, organizations must extend security
safeguards from the earliest stages of development through to runtime, treating AI models, build pipelines and third-party code with the
same rigor as internal systems.
Prevent security issues from reaching production. Security must operate at the speed of development. Integrating safeguards
into DevOps and continuous integration and continuous deployment (CI/CD) pipelines helps identify and remediate vulnerabilities in
custom code, open-source components, and AI configurations before deployment.
The same approach applies to AI systems, where early assessment of model security and configuration reduces downstream risk.
Hardening development tools and governing open-source dependencies helps eliminate weak spots that attackers exploit to inherit
trust within business workflows.
Secure the software and AI supply chain. Although not the most common attack vector, supply chain compromises yield the
highest impact, especially for otherwise mature organizations. Weaknesses in build systems, integration services and AI-related
repositories allow attackers to reach downstream environments without ever interacting with a firewall.
Reducing this exposure requires strict provenance checks. Build environments and deployment pipelines must have clear identity
controls and integrity protections. External software libraries, API connectors and AI components should be evaluated for access
patterns and update practices before adoption. Effective supply chain governance gives detection processes a reliable baseline,
making it easier to identify when a trusted dependency begins behaving unexpectedly.
Identify and block runtime attacks. Once applications are live, the focus shifts to containment. Attackers frequently attempt to
persist and expand access by misusing legitimate cloud identities, APIs or workload permissions.
Real-time detection, combined with consistent runtime controls such as behavioral monitoring, clear network boundaries and limits
on unexpected API interactions, helps disrupt these tactics. The same protections should extend to AI hosting environments, where
monitoring for model drift and unauthorized data access limits attacker movement even after initial compromise.
Automate cloud detection and response. In the cloud, speed is the only metric that matters. Delays in isolating affected
workloads or revoking misused identities give attackers the room they need to escalate.
Automation allows SecOps teams to detect and respond to cloud-based threats continuously, using native cloud controls to contain
incidents quickly. Actions such as isolating compromised containers or revoking suspicious session tokens help prevent localized
issues from escalating into broader outages or data loss.
Build a culture of secure AI and development. AI is now an operational asset, not just a tool. As assistants and automated
prompts become embedded in daily workflows, they introduce behavioral risks that technical controls alone cannot solve.
A strong security culture treats AI systems with the same discipline as critical infrastructure. This includes reviewing how assistants
are used, avoiding the exposure of sensitive data in prompts and validating AI-generated code. When teams understand that human
judgment remains central to effective AI use, governance controls are reinforced rather than bypassed, ensuring that the drive for
automation does not outpace the ability to oversee it.
By embedding security into the fabric of your development and runtime environments, you help
ensure that the speed of AI and cloud innovation drives business growth rather than systemic risk.
The Global Incident Response Report 2026 34

Section 04
5.
SECURE THE ATTACK SURFACE AND THE HUMAN INTERFACE
Securing the organization now requires looking beyond the corporate laptop. The modern attack surface has expanded to include
unmanaged contractor devices, public-facing cloud assets and the web browser itself, which has become the primary workspace
for the enterprise.
As defenders, we face a dual challenge. We must rigorously manage the external exposures that attackers constantly scan for,
while simultaneously securing the human interface where users interact with data, AI and the open web. To protect this sprawling
environment, security must extend its reach from the external edge down to the browser session.
Reduce the attack surface with active exposure management. Unit 42 found that software vulnerabilities accounted for
22% of initial access for incidents this year, underscoring the urgent need to move beyond simple discovery to active risk
prioritization. Effective exposure management bridges this gap by creating a complete, continuous inventory of the digital
footprint, including the shadow infrastructure and unauthorized AI tools that traditional scans miss.
Crucially, this strategy must filter out the noise, using threat intelligence to prioritize only those assets that are actively being
targeted in the wild (such as CISA KEVs) and lack compensating controls. By focusing limited resources on exploitable,
business-critical risks, teams can close the window of opportunity before an attacker finds an open door.
Protect the human interface. The browser is the new endpoint and the new corporate desktop. This is where employees
access data, where contractors perform their work and unfortunately, where social engineering attacks like phishing are
most effective.
Securing this interface requires an enterprise-grade secure browser that establishes a fully isolated and secured corporate
workspace for both managed and unmanaged devices. This powerful layer enforces data controls in real-time, regardless of
the underlying hardware. It can disable copy and paste on sensitive pages, prevent file downloads from unknown sources
and identify advanced phishing sites that evade standard email filters. By hardening the browser, organizations gain granular
visibility into shadow AI usage and directly prevent sensitive corporate data from leaking into unauthorized GenAI tools.
Secure third-party and unmanaged access. The rigid model of shipping corporate laptops to every contractor or
acquisition target is no longer sustainable or secure. Organizations need a way to enforce zero trust access on unmanaged
devices without the cost and complexity of legacy virtual desktop infrastructure (VDI) solutions.
By securing the workspace through the browser, companies can grant contractors and BYOD users secure access to
corporate applications while keeping business data strictly isolated from personal environments. This approach accelerates
merger and acquisition integration, and contractor onboarding while ensuring that a compromised personal device cannot
be used as a stepping stone into the corporate network.
Collect unified telemetry and automate response. For the endpoints you do manage, data is the fuel for defense.
Detecting sophisticated attacks depends on collecting high-fidelity telemetry across processes, network connections and
identity behavior, then unifying that data within a central platform.
When this data is analyzed by AI-driven engines, anomalies that would be invisible in isolation become clear indicators of
compromise. However, detection is only half the battle.
To minimize damage, response mechanisms must be automated. Security teams must be empowered to isolate
compromised endpoints, initiate forensic scans and remediate threats at machine speed, ensuring that a localized infection
does not become a systemic breach.
By securing the browser as the primary workspace and rigorously managing the external attack
surface, you protect the users and assets that traditional endpoint controls can no longer reach.
The Global Incident Response Report 2026 35

Section 05
SECTION 5
Appendix
We organized the data in this section in three
dimensions, providing defenders with a clearer view
of the patterns we have observed in 2025. First, we
outline the MITRE ATT&CK® techniques most closely
linked to each tactic. We then present regional and
industry-level views that show how investigation
types shift across geographies and sectors.
The Global Incident Response Report 2026 36

Section 05 Section 05
5.1.
OVERVIEW OF OBSERVED MITRE TECHNIQUES BY TACTIC
The following series of charts (Figures 7-18) show the MITRE ATT&CK® techniques we observed in association with specific tactics. Note that
the percentages shown represent the prevalence of each technique when compared across the other kinds of techniques identified for each
respective tactic. These percentages don’t represent how often the techniques showed up in cases (see the website version to explore data
about unique techniques and cases).
| T1078 - Valid Accounts   |                  |     | 39% |                                      | T1087 - Account Discovery       |     | 16% |
| ------------------------ | ---------------- | --- | --- | ------------------------------------ | ------------------------------- | --- | --- |
|                          |                  |     |     | T1083 - File and Directory Discovery |                                 |     | 15% |
|                          |                  |     |     |                                      | T1018 - Remote System Discovery |     | 11% |
|                          | T1566 - Phishing | 29% |     |                                      |                                 |     |     |
|                          |                  |     |     |                                      | T1135 - Network Share Discovery |     | 11% |
|                          |                  |     |     | T1046 - Network Service Discovery    |                                 |     | 8%  |
| T11190 - Exploit Public- |                  | 21% |     |                                      |                                 |     |     |
Facing Application T1016 - System Network Configuration Discovery 7%
|     |                  |     |     | T1082 - System Information Discovery |                                   | 5%  |     |
| --- | ---------------- | --- | --- | ------------------------------------ | --------------------------------- | --- | --- |
|     | T1133 - External | 6%  |     |                                      |                                   |     |     |
|     | Remote Services  |     |     | T1033 - System Owner/User Discovery  |                                   | 5%  |     |
|     |                  |     |     |                                      | T1673 - Virtual Machine Discovery | 3%  |     |
|     | T1189 - Drive-by | 5%  |     | T1069 - Permission Groups Discovery  |                                   | 3%  |     |
Compromise
|     |     |     | T1049 - System Network Connections Discovery |     |     | 3%  |     |
| --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
T1091 - Replication Through <1% T1482 - Domain Trust Discovery 2%
|     | Removable Media |     |     |     | T1615 - Group Policy Discovery | 1%  |     |
| --- | --------------- | --- | --- | --- | ------------------------------ | --- | --- |
|     |                 |     |     |     | T1518 - Software Discovery     | 1%  |     |
Figure 7. Relative prevalence of techniques  T1057 - Process Discovery 1%
observed in association with the initial access tactic.
|              |                            |     |     | T1613 - Container and Resource Discovery |                                  | 1%  |     |
| ------------ | -------------------------- | --- | --- | ---------------------------------------- | -------------------------------- | --- | --- |
|              |                            |     |     |                                          | T1040 - Network Sniffing         | <1% |     |
|              |                            |     |     |                                          | T1007 - System Service Discovery | <1% |     |
| T 1 0        | 5 9   -  C o m m a n d     |     | 58% |                                          |                                  |     |     |
|              |                            |     |     | T1120 - Peripheral Device Discovery      |                                  | <1% |     |
| and S c ri p | ti n g   In te rp re t e r |     |     |                                          |                                  |     |     |
|              |                            |     |     |                                          | T1124 - System Time Discovery    | <1% |     |
T1053 - Scheduled
14%
|                        | Task/Job |     |     | T1201 - Password Policy Discovery      |     | <1% |     |
| ---------------------- | -------- | --- | --- | -------------------------------------- | --- | --- | --- |
|                        |          |     |     | T1497 - Virtualization/Sandbox Evasion |     | <1% |     |
| T1204 - User Execution |          | 13% |     |                                        |     |     |     |
|                        |          |     |     | T1614 - System Location Discovery      |     | <1% |     |
T1569 - System Services 10% T1619 - Cloud Storage Object Discovery <1%
| T1072 - Software  | 2%  |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- |
Deployment Tools
T1047 - Windows Figure 8. Relative prevalence of techniques
2% observed in association with the discovery tactic.
Management
Instrumentation
T1203 - Exploitation
<1%
for Client Execution
|     | T1675 - ESXi  |     |     |     | T1078 - Valid Accounts |     | 19% |
| --- | ------------- | --- | --- | --- | ---------------------- | --- | --- |
<1%
Administration Command T1543 - Create or Modify System Process
16%
|     |     |     |     |     | T1053 - Scheduled Task/Job | 15% |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- |
Figure 9. Relative prevalence of techniques  T1136 - Create Account 13%
observed in association with the execution tactic.
|     |     |     |     | T1098 - Account Manipulation |     | 10% |     |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
7%
T1505 - Server Software Component
|     |     |     | T1547 - Boot or Logon Autostart Execution |                                  |                         | 5%  |     |
| --- | --- | --- | ----------------------------------------- | -------------------------------- | ----------------------- | --- | --- |
|     |     |     |                                           | T1133 - External Remote Services |                         | 3%  |     |
|     |     |     |                                           |                                  | T1112 - Modify Registry | 3%  |     |
|     |     |     |                                           | T1574 - Hijack Execution Flow    |                         | 3%  |     |
T1556 - Modify Authentication Process
3%
|     |     |     |                                              | T1546 - Event Triggered Execution | 2%  |     |     |
| --- | --- | --- | -------------------------------------------- | --------------------------------- | --- | --- | --- |
|     |     |     | T1037 - Boot or Logon Initialization Scripts |                                   | 1%  |     |     |
Figure 10. Relative prevalence of techniques
observed in association with the persistence tactic.
The Global Incident Response Report 2026     36 The Global Incident Response Report 2026     37

Section 05
T1070 - Indicator Removal 31%
|     | T1078 - Valid Accounts |     |     | 24% |     |     |     |
| --- | ---------------------- | --- | --- | --- | --- | --- | --- |
T1562 - Impair Defenses 20%
T1543 - Create or Modify System Process 20% T1078 - Valid Accounts 16%
T1053 - Scheduled Task/Job 18% T1550 - Use Alternate Authentication Material 4%
|                                           | T1098 - Account Manipulation |     | 13% |     |                                           | T1036 - Masquerading    | 4%  |
| ----------------------------------------- | ---------------------------- | --- | --- | --- | ----------------------------------------- | ----------------------- | --- |
|                                           |                              |     |     |     |                                           | T1564 - Hide Artifacts  | 4%  |
| T1547 - Boot or Logon Autostart Execution |                              |     | 6%  |     |                                           |                         |     |
|                                           |                              |     |     |     | T1548 - Abuse Elevation Control Mechanism |                         | 3%  |
| T1548 - Abuse Elevation Control Mechanism |                              | 4%  |     |     |                                           |                         |     |
|                                           |                              |     |     |     |                                           | T1112 - Modify Registry | 2%  |
T1574 - Hijack Execution Flow
|     |     | 4%  |     |     | T1556 - Modify Authentication Process |     | 2%  |
| --- | --- | --- | --- | --- | ------------------------------------- | --- | --- |
T1068 - Exploitation for Privilege Escalation 3% T1574 - Hijack Execution Flow 2%
T1546 - Event Triggered Execution 3% T1027 - Obfuscated Files or Information 2%
|                                              |                           |     |     |                                                 | T1218 - System Binary Proxy Execution        |                           | 2%  |
| -------------------------------------------- | ------------------------- | --- | --- | ----------------------------------------------- | -------------------------------------------- | ------------------------- | --- |
| T1037 - Boot or Logon Initialization Scripts |                           | 2%  |     |                                                 |                                              |                           |     |
|                                              |                           |     |     |                                                 |                                              | T1055 - Process Injection | 1%  |
|                                              | T1055 - Process Injection | 2%  |     |                                                 |                                              |                           |     |
|                                              |                           |     |     | T1140 - Deobfuscate/Decode Files or Information |                                              |                           | <1% |
| T1484 - Domain or Tenant Policy Modification |                           | 1%  |     |                                                 |                                              |                           |     |
|                                              |                           |     |     |                                                 | T1484 - Domain or Tenant Policy Modification |                           | <1% |
<1%
T1222 - File and Directory Permissions Modification
<1%
Figure 11. Relative prevalence of techniques observed  T1620 - Reflective Code Loading
in association with the privilege escalation tactic.
|     |     |     |     |     | T1202 - Indirect Command Execution          |                              | <1% |
| --- | --- | --- | --- | --- | ------------------------------------------- | ---------------------------- | --- |
|     |     |     |     |     | T1497 - Virtualization/Sandbox Evasion      |                              | <1% |
|     |     |     |     |     |                                             | T1480 - Execution Guardrails | <1% |
|     |     |     |     |     | T1578 - Modify Cloud Compute Infrastructure |                              | <1% |
T1003 - OS Credential Dumping
|                                          |                     |     |     | 32% |     | T1601 - Modify System Image | <1% |
| ---------------------------------------- | ------------------- | --- | --- | --- | --- | --------------------------- | --- |
|                                          | T1110 - Brute Force |     |     | 30% |     | T1656 - Impersonation       | <1% |
|                                          |                     |     |     |     |     | T1672 - Email Spoofing      | <1% |
| T1555 - Credentials from Password Stores |                     |     | 11% |     |     |                             |     |
T1552 - Unsecured Credentials 6% Figure 12. Relative prevalence of techniques observed
T1558 - Steal or Forge Kerberos Tickets 6% in association with the defense evasion tactic.
| T1556 - Modify Authentication Process |     | 4%  |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
T1212 - Exploitation for Credential Access 3% T1021 - Remote Services 85%
T1621 - Multi-Factor Authentication 3% T1570 - Lateral Tool Transfer 4%
Request Generation
T1550 - Use Alternate
4%
| T1557 - Adversary-in-the-Middle |     | 1%  |     |     | Authentication Material |     |     |
| ------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- |
T1072 - Software Deployment Tools 2%
|     | T1056 - Input Capture    | 1%  |     |     |                         |     |     |
| --- | ------------------------ | --- | --- | --- | ----------------------- | --- | --- |
|     | T1040 - Network Sniffing | 1%  |     |     | T1563 - Remote Service  |     |     |
2%
Session Hijacking
T1649 - Steal or Forge
|     |     | <1% |     |     | T1210 |  -  E x p l o i ta t i o n   o f |     |
| --- | --- | --- | --- | --- | ----- | -------------------------------- | --- |
Authentication Certificates 1%
|     |     |     |     |     |     | R e m o t e   S e r v i c e s |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- |
T1534 - Internal Spearphishing
<1%
Figure 13. Relative prevalence of techniques observed
in association with the credential access tactic. T1091 - Replication Through
<1%
Removable Media
T1080 - Taint Shared Content <1%
Figure 14. Relative prevalence of techniques observed
in association with the lateral movement tactic.
The Global Incident Response Report 2026     38

Section 05 Section 05
T1074 - Data Staged 33%
T1219 - Remote Access Tools 39%
T1560 - Archive Collected Data 21% T1105 - Ingress Tool Transfer 25%
T1213 - Data from Information Repositories 15%
T1071 - Application Layer Protocol 19%
T1039 - Data from Network Shared Drive 6% T1572 - Protocol Tunneling 8%
| T1005 - Data from Local System | 5%  |     |     |
| ------------------------------ | --- | --- | --- |
T1090 - Proxy 6%
| T1119 - Automated Collection | 4%  |                         |     |
| ---------------------------- | --- | ----------------------- | --- |
|                              |     | T1102 - Web Service     | 2%  |
| T1113 - Screen Capture       | 4%  |                         |     |
| T1056 - Input Capture        |     | T1095 - Non-Application | <1% |
2% Layer Protocol
| T1114 - Email Collection | 2%  |     |     |
| ------------------------ | --- | --- | --- |
T1557 - Adversary-in-the-Middle
2%
Figure 16. Relative prevalence of techniques observed
T1530 - Data from Cloud Storage 2% in association with the command and control tactic.
| T1123 - Audio Capture | 1%  |     |     |
| --------------------- | --- | --- | --- |
T1602 - Data from Configuration Repository 1%
T1486 - Data Encrypted for Impact 60%
Figure 15. Relative prevalence of techniques observed
in association with the collection tactic. T1490 - Inhibit System Recovery 15%
|     |     | T1531 - Account Access Removal | 13% |
| --- | --- | ------------------------------ | --- |
T1567 - Exfiltration
62%
| Over Web Service |     | T1496 - Resource Hijacking | 4%  |
| ---------------- | --- | -------------------------- | --- |
T1048 - Exfiltration Over
|     | 14% | T1491 - Defacement | 2%  |
| --- | --- | ------------------ | --- |
Alternative Protocol
T1011 - Exfiltration Over T1498 - Network Denial of Service 2%
7%
Other Network Medium
|     | T1529 - System Shutdown/Reboot |     | 2%  |
| --- | ------------------------------ | --- | --- |
T1052 - Exfiltration
7%
Over Physical Medium
|     |     | T1657 - Financial Theft | 2%  |
| --- | --- | ----------------------- | --- |
T1041 - Exfiltration
| Over C2 Channel | 5%  |     |     |
| --------------- | --- | --- | --- |
Figure 18. Relative prevalence of techniques
T1020 - Automated Exfiltration 3% observed in association with the impact tactic.
T1537 - Transfer Data
| to Cloud Account 2% |     |     |     |
| ------------------- | --- | --- | --- |
Figure 17. Relative prevalence of techniques
observed in association with the exfiltration tactic.
The Global Incident Response Report 2026     38 The Global Incident Response Report 2026     39

Section 05 Section 05
5.2.
INVESTIGATION TYPE BY REGION
Figures 19 - 21 provide a regional and industry-level view of the investigations handled by Unit 42 during 2025. They
show how incident types vary across North America, Europe, the Middle East, Africa and Asia Pacific, alongside a
breakdown of the most common investigation categories within the industries most represented in our data. These
insights will help leaders understand where activity is concentrated and how exposure differs across sectors and
geographies.
The geographic data highlights differences in investigation types regionally, while the industry charts show clear
patterns in how threat activity aligns with sector-specific operations and technology stacks. High technology,
manufacturing, financial services and healthcare each exhibit distinct mixes of intrusion types, reflecting variation
in attack surface, identity architecture and cloud maturity. Together, these views give security leaders a clearer
picture of where threats are most active and how the operational context shapes the intrusions Unit 42 investigates.
Network Intrusion
|     |     |     |     | 34% | Network Intrusion |     |     |     | 47% |
| --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
BEC
|     |     |     | 16% |     |     | Other IR |     | 15% |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
Extortion - Ransomware
10%
| Web App Compromise |     |     |     |     | Exposure Investigation |     |     | 9%  |     |
| ------------------ | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
8%
| Exposure Investigation |     |     |     |     | Extortion - Ransomware |     |     | 7%  |     |
| ---------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
7%
|                           | Insider - Other | 7%  |     |     | Other Digital Forensics |     | 5%  |     |     |
| ------------------------- | --------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
|                           | Other IR        | 5%  |     |     |                         | BEC | 5%  |     |     |
| Extortion - No Encryption |                 | 5%  |     |     | Web App Compromise      |     |     |     |     |
5%
|                                       | Insider - Bad Leaver | 4%  |     |     |                           |                 |     |     |     |
| ------------------------------------- | -------------------- | --- | --- | --- | ------------------------- | --------------- | --- | --- | --- |
|                                       |                      |     |     |     |                           | Insider - Other | 3%  |     |     |
| Other Digital Forensics               |                      | 2%  |     |     |                           |                 |     |     |     |
|                                       |                      |     |     |     | Extortion - No Encryption |                 | 2%  |     |     |
| Threat Intelligence / Dark Web Search |                      | 1%  |     |     |                           |                 |     |     |     |
| Cloud Data Plane Compromise           |                      | <1% |     |     | Insider - Bad Leaver      |                 | 1%  |     |     |
Collection / Preservation Only <1% Other Service - Non-Incident Related <1%
| Cloud Control Plane Compromise |                   | <1% |     |                                |                     |     |     |     |     |
| ------------------------------ | ----------------- | --- | --- | ------------------------------ | ------------------- | --- | --- | --- | --- |
|                                |                   |     |     |                                | Database Compromise |     | <1% |     |     |
| Database Compromise            |                   | <1% |     |                                |                     |     |     |     |     |
|                                |                   |     |     | Cloud Control Plane Compromise |                     |     | <1% |     |     |
|                                | PCI Investigation | <1% |     |                                |                     |     |     |     |     |
Figure 19. Investigation type by region: North America. Figure 20. Investigation type by region: Europe, the Middle East and Africa.
| Network Intrusion       |          |     | 36% |     |     |     |     |     |     |
| ----------------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Extortion - Ransomware  |          | 16% |     |     |     |     |     |     |     |
|                         | Other IR | 16% |     |     |     |     |     |     |     |
| Exposure Investigation  |          | 13% |     |     |     |     |     |     |     |
| Web App Compromise      |          | 11% |     |     |     |     |     |     |     |
| Other Digital Forensics |          | 4%  |     |     |     |     |     |     |     |
|                         | BEC      | 4%  |     |     |     |     |     |     |     |
Figure 21. Investigation type by region: Asia-Pacific region.
The Global Incident Response Report 2026     PB The Global Incident Response Report 2026     40

Section 05
5.3.
|     |     |     |     |     |     |     |                    | Network Intrusion |     |     |     | 29% |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ----------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | Web App Compromise |                   |     |     | 14% |     |
INVESTIGATION
|     |     |     |     |     |     |     | Exposure Investigation |     |     |     | 12% |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
TYPE BY INDUSTRY
|     |     |     |     |     |     |     |     | Insider - Other |     |     | 11% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | Other IR        |     | 8%  |     |     |
Figures 22–28 below show a breakdown of the top
|     |     |     |     |     |     |     |     | BEC |     | 7%  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
investigation types associated with the industries
|     |     |     |     |     |     |     | Extortion - No Encryption |     |     | 5%  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
most represented in our incident response data,
|     |     |     |     |     |     |     |     | Insider - Bad Leaver |     | 5%  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
ordered from the industries with the highest volume  Extortion - Ransomware 4%
of investigations to those with lower representation. Other Digital Forensics 3%
Cloud Control Plane Compromise
1%
|     |     |     |     |     |     |     | Collection / Preservation Only |     | 1%  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | Cloud Data Plane Compromise    |     | <1% |     |     |     |
Figure 22. Investigation type by industry: High Technology.
|     |                        | Network Intrusion |     |     |     | 38% |     |                   |     |     |     |     |
| --- | ---------------------- | ----------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
|     |                        |                   |     |     |     |     |     | Network Intrusion |     |     |     | 34% |
|     | Extortion - Ransomware |                   |     |     | 16% |     |     |                   |     |     |     |     |
BEC
|     |                         |                      | BEC      |     | 13% |     |                        |                   |     |     | 24% |     |
| --- | ----------------------- | -------------------- | -------- | --- | --- | --- | ---------------------- | ----------------- | --- | --- | --- | --- |
|     |                         |                      | Other IR |     | 7%  |     |                        | Other IR          |     | 11% |     |     |
|     | Exposure Investigation  |                      |          | 5%  |     |     | Exposure Investigation |                   |     | 8%  |     |     |
|     |                         |                      |          |     |     |     |                        | Insider - Other   |     | 7%  |     |     |
|     |                         | Insider - Bad Leaver |          | 5%  |     |     |                        |                   |     |     |     |     |
|     |                         | Insider - Other      |          | 4%  |     |     | Extortion - Ransomware |                   |     | 7%  |     |     |
|     | Web App Compromise      |                      |          | 4%  |     |     | Web App Compromise     |                   |     | 5%  |     |     |
|     | Other Digital Forensics |                      |          | 3%  |     |     |                        | PCI Investigation | 1%  |     |     |     |
Threat Intelligence / Dark Web Search 2% Other Digital Forensics 1%
| Other Service - Non-Incident Related |                           |     |     | <1% |     |                                |                           |     |     |     |     |     |
| ------------------------------------ | ------------------------- | --- | --- | --- | --- | ------------------------------ | ------------------------- | --- | --- | --- | --- | --- |
|                                      |                           |     |     |     |     | Cloud Control Plane Compromise |                           |     | 1%  |     |     |     |
|                                      | Extortion - No Encryption |     |     | <1% |     |                                |                           |     |     |     |     |     |
|                                      |                           |     |     |     |     |                                | Extortion - No Encryption |     | 1%  |     |     |     |
| Cloud Data Plane Compromise          |                           |     |     | <1% |     |                                |                           |     |     |     |     |     |
Figure 23. Investigation type by industry: Manufacturing. Figure 24. Investigation type by industry: Professional and Legal Services.
|                           |                   |          |     |     |     |     |                        | Network Intrusion       |     |     |     | 40% |
| ------------------------- | ----------------- | -------- | --- | --- | --- | --- | ---------------------- | ----------------------- | --- | --- | --- | --- |
|                           | Network Intrusion |          |     |     | 29% |     |                        |                         |     |     |     |     |
|                           |                   |          |     |     |     |     |                        | Other IR                |     | 12% |     |     |
| Extortion - Ransomware    |                   |          |     |     | 17% |     |                        |                         |     |     |     |     |
|                           |                   |          |     |     |     |     |                        |                         | BEC | 12% |     |     |
| Exposure Investigation    |                   |          |     |     | 14% |     |                        |                         |     |     |     |     |
|                           |                   |          |     |     |     |     |                        | Exposure Investigation  |     | 10% |     |     |
|                           |                   | Other IR |     | 10% |     |     | Extortion - Ransomware |                         |     | 9%  |     |     |
| Extortion - No Encryption |                   |          |     | 10% |     |     |                        |                         |     |     |     |     |
|                           |                   |          |     |     |     |     |                        | Insider - Other         |     | 4%  |     |     |
|                           | Insider - Other   |          |     | 7%  |     |     |                        | Web App Compromise      |     | 4%  |     |     |
|                           |                   |          |     |     |     |     |                        | Other Digital Forensics | 1%  |     |     |     |
|                           |                   | BEC      |     | 6%  |     |     |                        |                         |     |     |     |     |
Cloud Control Plane Compromise
|     |     |     | 3%  |     |     |     |     |     | 1%  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Other Digital Forensics
|                     |     |     |     |     |     | Threat Intelligence / Dark Web Search |                           |                      | 1%  |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | ------------------------------------- | ------------------------- | -------------------- | --- | --- | --- | --- |
| Database Compromise |     |     | 1%  |     |     |                                       |                           |                      |     |     |     |     |
|                     |     |     |     |     |     |                                       |                           | Insider - Bad Leaver | 1%  |     |     |     |
| Web App Compromise  |     |     | 1%  |     |     |                                       | Extortion - No Encryption |                      | 1%  |     |     |     |
Figure 26. Investigation type by industry: Financial Services.
Figure 25. Investigation type by industry: Wholesale and Retail.
|     |     | Network Intrusion |     |     |     | 49% |     | Network Intrusion |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
36%
|     | Web App Compromise      |                      |          |     | 11% |     | Extortion - Ransomware    |                         |     |     | 18% |     |
| --- | ----------------------- | -------------------- | -------- | --- | --- | --- | ------------------------- | ----------------------- | --- | --- | --- | --- |
|     | Exposure Investigation  |                      |          |     | 11% |     |                           |                         |     |     |     |     |
|     |                         |                      |          |     |     |     |                           |                         | BEC |     | 18% |     |
|     |                         |                      | Other IR |     | 9%  |     |                           |                         |     |     |     |     |
|     |                         |                      |          |     |     |     | Extortion - No Encryption |                         |     | 6%  |     |     |
|     |                         |                      | BEC      |     | 6%  |     |                           |                         |     |     |     |     |
|     |                         |                      |          |     |     |     |                           | Other Digital Forensics |     | 6%  |     |     |
|     | Extortion - Ransomware  |                      |          |     | 6%  |     |                           |                         |     |     |     |     |
|     |                         |                      |          |     |     |     |                           | Insider - Other         |     | 6%  |     |     |
|     |                         | Insider - Bad Leaver |          | 2%  |     |     |                           |                         |     |     |     |     |
|     |                         |                      |          |     |     |     |                           | Web App Compromise      |     | 3%  |     |     |
|     | Other Digital Forensics |                      |          | 2%  |     |     |                           |                         |     |     |     |     |
Exposure Investigation
|                                       |     | Insider - Other |     | 2%  |     |                                       |     |     |     | 3%  |     |     |
| ------------------------------------- | --- | --------------- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
|                                       |     |                 |     |     |     | Threat Intelligence / Dark Web Search |     |     |     | 3%  |     |     |
| Threat Intelligence / Dark Web Search |     |                 |     | 2%  |     |                                       |     |     |     |     |     |     |
Figure 27. Investigation type by industry: State and Local Government. Figure 28. Investigation type by industry: Healthcare.
The Global Incident Response Report 2026     41

| Section 05 | 06  |     |     | SSeeccttiioonn  0056 |
| ---------- | --- | --- | --- | -------------------- |
SECTION 6:
Methodology
We sourced data for this report from more than 750 cases Unit 42 responded to between Oct. 1, 2024, and Sept. 30, 2025, with
comparisons to metrics from earlier case data going back to 2021. Our clients ranged from small organizations with fewer than
50 personnel to Fortune 500, Global 2000 and government organizations with more than 100,000 employees.
The affected organizations were headquartered in over 50 countries. About 65% of the targeted organizations in these cases
were headquartered in the U.S. Cases involving organizations based in Europe, the Middle East and Asia Pacific formed the
remaining 35% of the work. Attacks frequently had an impact beyond the locations where the organizations were headquartered.
We combined this case data with insights from our threat research, which is informed by product telemetry, observations from
dark web leak sites and other open-source information. Incident responders also contributed their firsthand observations of key
trends based on direct work with clients.
Several factors may influence the nature of our dataset, including a trend toward engagements with larger organizations with
more mature security postures. We also emphasized cases that reveal emerging trends, which for some topics means focusing
on smaller segments of the overall dataset.
For some analysis areas, we chose to filter our data to avoid skewed results. For example, we offered incident response support
to help customers investigate potential impacts of CVEs 2024-0012 and 2024-3400, which caused these vulnerabilities to be
overrepresented in our dataset. Where appropriate, we corrected for this overrepresentation.
Our guiding principle throughout has been to provide insights into the present and emerging threat landscape, enabling
defenders to strengthen their posture against what attackers are doing now and where they are headed next.
Contributors
|     | Amelia Albanese | Alexis Godwin   | Vraj Mehta    | Doel Santos      |
| --- | --------------- | --------------- | ------------- | ---------------- |
|     | Sheida Azimi    | Evan Gordenker  | Danny Milrad  | Mike Savitz      |
|     | Jim Barber      | Daniel Gott     | Jacqui Morgan | Andrew Scott     |
|     | Maxfield Barker | Evan Harrington | David Moulton | Steve Scott      |
|     | Jeremy Brown    | Tim Heraldo     | Lysa Myers    | Ram Shenoy       |
|     | Mark Burns      | Brandon Hicks   | Erica Naone   | Michael Sikorski |
Josh Costa Manisha Hirani Aisling O’Suilleabhain Scott Simkin
|     | Kasey Cross | Jack Hughes | Aryn Pedowitz | Ray Spera |
| --- | ----------- | ----------- | ------------- | --------- |
Michael Diakiwski Margaret Kelley Andy Piazza Samantha Stallings
|     | Dan O’Day       | Seth Lacy   | Nicholas Pockl-Deen | Jenine Sussman |
| --- | --------------- | ----------- | ------------------- | -------------- |
|     | Richard Emerson | Samantha Le | Brendan Powers      |                |
Virginia Tran
|     | Elizabeth Farabee | Yang Liang | Nathaniel Quist |     |
| --- | ----------------- | ---------- | --------------- | --- |
Amy Wagman
|     | Robert Falcone  | Chia Hui Mah | Adam Robbie     | JL Watkins   |
| --- | --------------- | ------------ | --------------- | ------------ |
|     | Byrne Ghavalas  | Mitch Mayne  | Laury Rodriguez | Kyle Wilhoit |
|     | Wyatt Gibson    | Eva Mehlert  | Sam Rubin       |              |
The Global Incident Response Report 2026     41 TThhee  GGlloobbaall  IInncciiddeenntt  RReessppoonnssee  RReeppoorrtt  22002266          4422

About Palo Alto Networks
Palo Alto Networks® is the world’s cybersecurity leader. We innovate to outpace cyberthreats, so organizations
can embrace technology with confidence. We provide next-gen cybersecurity to thousands of customers
globally, across all sectors. Our best-in-class cybersecurity platforms and services are backed by industry-
leading threat intelligence and strengthened by state-of-the-art automation. Whether deploying our products
to enable the Zero Trust Enterprise, responding to a security incident, or partnering to deliver better security
outcomes through a world-class partner ecosystem, we’re committed to helping ensure each day is safer than
the one before. It’s what makes us the cybersecurity partner of choice.
At Palo Alto Networks, we’re committed to bringing together the very best people in service of our mission,
so we’re also proud to be the cybersecurity workplace of choice, recognized among Newsweek’s Most Loved
Workplaces (2023, 2022, 2021), with a score of 100 on the Disability Equality Index (2023, 2022), and HRC
Best Places for LGBTQ equality (2022). For more information, visit www.paloaltonetworks.com.
About Unit 42
Palo Alto Networks® Unit 42® brings together world-renowned threat researchers, elite incident responders
and expert security consultants to create an intelligence-driven, response-ready organization that’s passionate
about helping you proactively manage cyber risk. Together, our team serves as your trusted advisor to help
assess and test your security
controls against the right threats, transform your security strategy with a threat-informed approach, and
respond to incidents in record time so that you get back to business faster. Visit paloaltonetworks.com/unit42.
3000 Tannery Way
Santa Clara, CA 95054
Main +1.408.753.4000
Sales +1.866.320.4788
Support +1.866.898.9087
www.paloaltonetworks.com
© 2026 Palo Alto Networks, Inc. Palo Alto Networks is a registered trademark of Palo Alto Networks, Inc. A list of our trademarks in the United States and other
jurisdictions can be found at www.paloaltonetworks.com/company/trademarks.html. All other marks mentioned herein may be trademarks of their respective
companies.
2026 Unit 42 Incident Response Report | February 2026