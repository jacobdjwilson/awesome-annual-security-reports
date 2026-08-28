2026
MANAGED SASE &
ZERO TRUST REPORT
Hybrid Complexity, Visibility Gaps,
and the Shift to Managed SASE

Overview
Organizations no longer treat "hybrid" as a transitional phase. It is the new operating reality in
which users, applications, and partners require secure access from everywhere, continuously.
This shift has fundamentally changed how secure access must be delivered and sustained. Zero
Trust principles - grounding access decisions in identity and continuous verification rather than
network location - are now widely accepted. SASE architectures have emerged to deliver these
capabilities through unified cloud services. Yet many organizations are still struggling to operate
these models consistently at scale.
To understand how leaders are navigating the gap between SASE strategy and day-to-day
execution, we surveyed over 500 senior security and IT leaders across the United States and the
United Kingdom who are directly responsible for connectivity, security and performance across
hybrid environments.
Three key findings illustrate the execution gap:
• Visibility has not kept pace • Zero Trust is advancing, • Execution capacity is the
with hybrid complexity. but most organizations primary constraint.
More than 90% of remain in a middle state. Nearly half of organizations
organizations secure users, While the market has moved report the parallel operation
applications, data centers, and beyond legacy VPN-only of VPN and ZTNA as a
third parties simultaneously. access, fewer than one in ten major operational burden,
Yet roughly two-thirds cite lack organizations have achieved fragmenting policy and
of end-to-end visibility as their a fully integrated Zero Trust increasing support overhead.
top operational challenge, architecture. Most operate In response, roughly four in
revealing a growing gap with partial deployment and five now prefer co-managed or
between environmental scope inconsistent enforcement fully managed SASE models,
and operational control. across environments. reflecting a shift toward
operating models designed to
absorb integration complexity
rather than passing it to
internal teams.
The market is aligned on the strategic direction of SASE and Zero Trust. What holds back progress is
execution capacity. As a result, organizations are reassessing not whether to adopt SASE, but how secure
access must be delivered to achieve consistent execution and long-term operational resilience.
OPEN SYSTEMS | 2026 MANAGED SASE & ZERO TRUST REPORT ©2026 Cybersecurity Insiders. All Rights Reserved. 2

Hybrid is Permanent - Visibility Has Not Kept Pace
Hybrid is no longer a transition phase. It is how organizations operate today: securing users, applications,
data centers, branches, and third-party partners simultaneously across environments that were never
designed to function as a single system.
The survey data confirms this scale. More than 90% of organizations secure remote employees and
SaaS applications, around 85% secure branch locations, and between 70% extend access to third-
party partners. While connectivity across these environments is largely solved, visibility is not. As hybrid
complexity has expanded, what security and network teams can realistically observe has failed to keep
pace. Two-thirds of respondents cite lack of end-to-end visibility as their top operational challenge,
reflecting a growing gap between environmental scope and operational control.
We see this confidence cliff clearly in the data: respondents rate their ability to monitor core applications
at six out of ten. But as access moves toward the edges - remote users, multi-cloud traffic, and third-party
access - confidence drops sharply, falling to around four out of ten. With 70% of organizations relying on
external partners, these blind spots sit squarely within normal operations.
The Confidence Cliff: Visibility Degrades at the Edges
How confident are you in your organization’s ability to monitor and control the following access scenarios?
4.0 4.8 4.9 5.6 6.7
OT/industrial Third-party/ Multi-cloud Remote and Employee
systems supplier application hybrid users access to
access traffic outside corporate
corporate applications
network
The consequences surface immediately in operational metrics. Degraded remote performance,
inconsistent user experience, rising ticket volumes are each cited by roughly half of respondents. In
response, organizations are increasingly turning to AI to cope with signal overload, prioritizing incident
detection, anomaly monitoring, and support automation. Visibility, in this context, is less about
collecting more data and more about enabling timely, actionable decisions. This is the operational
reality into which SASE is being deployed.
OPEN SYSTEMS | 2026 MANAGED SASE & ZERO TRUST REPORT ©2026 Cybersecurity Insiders. All Rights Reserved. 3

Zero Trust: The Middle State
If visibility gaps drive day-to-day operational pain, Zero Trust represents the strategic destination most
organizations have already committed to. The challenge is no longer whether Zero Trust is the right
model, but why progress slows once initial deployments are in place.
The survey shows a market that has decisively moved beyond VPN-only access yet remains concentrated
in partial and uneven stages of Zero Trust execution. Only 13% still rely on traditional VPN-only models,
while just 9% describe their environment as a fully integrated Zero Trust architecture. Between these two
extremes lies the vast majority of roughly 80% of organizations operating in a sustained middle state that
is often operationally messy.
That middle state typically takes three forms:
Stage 1 – The Quick Win (31%): Stage 2 – The Extension (28%): Stage 3 – The Policy Layer (19%):
ZTNA deployed primarily for Access controls extended to critical Granular, policy-driven access
remote users, delivering immediate applications for both remote using ZTNA, SWG, and CASB,
security and user experience and on-site users, increasing often implemented unevenly
across environments as integration
gains without requiring broad coverage but still relying on mixed
complexity grows.
architectural change. enforcement models.
The Zero Trust "Middle State": Most Organizations Are Stuck in Partial Deployment
Which best describes your organization’s current Zero Trust maturity status?
Initial rollout of ZTNA for remote users (Stage 1)
31%
Access policies applied to critical applications (Stage 2)
28%
Granular access policies across users and apps (Stage 3)
19%
Traditional WAN + VPN only
13%
Fully integrated Zero Trust architecture
9%
The data helps explain why this stall persists. ZTNA is the most common entry point for SASE (63%),
followed by SD-WAN (around 50%), with SWG and CASB adopted later. This remote-first sequencing
delivers immediate relief for remote workers, improving experience and eliminating VPN backhaul
However, this remote-first approach often creates silos. Organizations succeed in securing the remote
worker first but then struggle to replicate that same architecture across branches, third parties, and on-
premises data centers. The result is a modern front door (ZTNA) attached to a legacy house, unable to
bridge the gap to full integration. Zero Trust foundations are in place, but translating partial deployment
into end-to-end integration across the broader environment has proven harder than anticipated.
OPEN SYSTEMS | 2026 MANAGED SASE & ZERO TRUST REPORT ©2026 Cybersecurity Insiders. All Rights Reserved. 4

The Execution Gap: When Complexity Outpaces Capacity
Most organizations are aligned on the strategic direction of SASE and Zero Trust. What is slowing
progress is not a lack of budget or intent, but a growing gap between environmental complexity and
execution capacity.
The survey identifies three structural barriers that define this execution gap:
1. Integration Friction: 2. The Skills Gap: 3. The Parallel Operations Tax:
Integration with existing systems is Internal expertise shortages Nearly half of organizations (48%)
the most frequently cited challenge are the second most significant identify the parallel operation
for SASE (53%). At the ZTNA layer, barrier (51%). Organizations of legacy VPN and ZTNA as
more than half of respondents are attempting to operate a major operational burden.
(52%) struggle to integrate with next-generation, policy-driven Maintaining two access models
identity management systems. architectures with teams and fragments policy, increases
The tools are deployed, but policy, workflows built for legacy firewall support overhead, and complicates
identity context, and telemetry and VPN environments, limiting the user experience. For many,
remain fragmented across consistent execution at scale. this duplication has become a
the stack, limiting consistent persistent operational tax rather
enforcement. than a temporary transition phase.
The Execution Gap: Parallel Operations and Skills Shortages
What are your biggest challenges in ZTNA adoption and operations?
51%
50%
48%
37%
32%
30%
28%
Shortage of Integration Parallel Coordination Lack of clear Budget or User
internal with existing operation of between project plan resource acceptance
expertise identity VPN and ZTNA network or roadmap constraints and training
management (hybrid phase) and security
systems teams
This is the crux of the execution gap. The challenge is no longer deploying SASE or ZTNA components.
Instead, it is about sustaining integration, identity alignment, and operational consistency in live
environments where legacy and modern access models coexist.
As this burden grows, the focus shifts from how to deploy secure access to how it can be operated safely
and consistently at scale.
OPEN SYSTEMS | 2026 MANAGED SASE & ZERO TRUST REPORT ©2026 Cybersecurity Insiders. All Rights Reserved. 5

Why SASE? Security and Simplicity Before Cost
Organizations are adopting SASE to restore security and operational control in increasingly complex
hybrid environments. Direct cost savings are a secondary consideration; the primary drivers reflect what
breaks under legacy access models in day-to-day operations.
The reasons for moving away from VPN-centric architectures are consistent and pragmatic:
1. Security & Compliance 2. User Experience and 3. Visibility Underpins
Remain the Baseline: Performance Matter: Consistent Enforcement:
Higher security and compliance Improved user experience is cited Improving visibility across
requirements are the leading by 63% of respondents, while 59% users and applications is a
reasons for abandoning VPNs highlight performance gains from primary motivator for 45% of
(76%). Enabling secure hybrid eliminating VPN backhauling. respondents. In fragmented hybrid
access is also the top overall Organizations are no longer willing environments, visibility is not a
driver for SASE adoption (54%). to trade productivity and reliability “nice to have” - it is a prerequisite
In distributed environments, for security controls that frustrate for enforcing security policies
perimeter-based access no longer users and overload support teams. consistently and responding
provides sufficient control. effectively when issues arise.
Drivers for moving from VPN to ZTNA
What are your main drivers for moving from VPN to ZTNA?
Improved
Better user performance Simplified
experience
management
Higher
security/ 59%
compliance Software/vendor
requirements 63% 51% consolidation
46%
50% 44%
45%
Cost
savings
74% 35%
28%
Cost considerations are addressed indirectly through consolidation rather than upfront savings. More
than half of organizations (55%) identify vendor consolidation as their primary cost-optimization lever,
often funding SASE by retiring legacy firewall and VPN estates instead of seeking incremental budget
increases. Regulatory and data sovereignty pressures - particularly in the UK – reinforce this pattern.
Organizations are optimizing first for secure access, visibility, and operational simplicity. Financial benefits
follow through consolidation and reduced operational drag, not through standalone cost reduction.
OPEN SYSTEMS | 2026 MANAGED SASE & ZERO TRUST REPORT ©2026 Cybersecurity Insiders. All Rights Reserved. 6

The operating model shift: From deployment to
co-managed SASE
The execution gap has forced a fundamental rethink of how SASE is delivered. The question is no
longer whether to adopt SASE, but how secure access can be operated predictably and sustainably
under real-world conditions. The survey shows a clear shift toward shared operational responsibility.
Nearly eight out of ten organizations now expect partner involvement in SASE operations.
How SASE should be delivered, support for co-managed models is decisive:
• Co-Managed • Fully Managed: • In-House Only:
(the dominant model): 27% preferred where internal 22% chosen primarily by
51% organizations retain control capacity is constrained and the organizations with mature
over policy and visibility while priority is offloading day-to-day teams and stable environments
sharing operational responsibility operations to ensure reliability and capable of sustaining continuous
to manage integration complexity compliance. operational load.
and sustain execution.
The Operational Shift: Co-Managed is the Preferred Model
How would you prefer your SASE solution to be delivered?
27%
Fully managed
service provider
51%
(MSSP / MSP)
Co-managed
with a trusted
service provider
22%
Fully in-house
management
This shift does not represent a return to traditional outsourcing. It reflects a pragmatic response to
execution constraints - particularly integration complexity, skills shortages, and the burden of operating
parallel access models – without relinquishing governance or control.
In practice, this means retaining ownership of policy, governance, and visibility while relying on a
partner to absorb continuous operational load, including integration across hybrid environments, 24×7
monitoring, and ongoing platform maintenance. Taken together, these findings mark a pivotal shift in
buyer expectations. SASE is no longer being evaluated as a product to deploy, but as a critical service
that must be delivered consistently over time.
OPEN SYSTEMS | 2026 MANAGED SASE & ZERO TRUST REPORT ©2026 Cybersecurity Insiders. All Rights Reserved. 7

The New SASE Mandate
The survey data delivers a clear message. Buyers are no longer evaluating SASE based on architecture
diagrams or feature lists. Their expectations are shaped by execution constraints, hybrid operating
reality, and regulatory pressure.
Three mandates now define how SASE is evaluated:
1. Visibility first, 2. Co-managed is the 3. Compliance and residency
connectivity assumed: preferred operating model: are baseline requirements:
Organizations are already hybrid Only 22% of organizations For organizations with UK or EU
and multi-cloud: over 90% want to manage SASE entirely exposure, compliance and data
secure remote users and SaaS in-house. The rest expect residency are design requirements,
applications, 73% secure third- partner involvement to address not differentiators. UK respondents
party access. Connectivity is table integration complexity (55%), rate compliance expertise and EU/
stakes. What buyers lack is end-to- skills shortages (48%), and policy UK data transparency at 4.7 out of 5
end visibility, cited by 68% as the management overhead (42%). when selecting providers. Providers
top operational challenge. SASE Buyers want SASE delivered as a who treat these as optional will not
platforms that lead with visibility continuous service, not deployed make the shortlist.
and Zero Trust enforcement as a one-time project.
resonate more strongly than those
positioned around networking.
The SASE Evaluation Checklist: Compliance and Support are Critical
When selecting a network or security provider, how important are the following criteria?
US | UK
4.7% 24×7 operations 4.6%
and support
4.4% Regulatory certifications 4.7%
and compliance expertise
4.0% EU data transparency 4.6%
and residency
The market is aligned on the destination: Zero Trust. What separates leaders from laggards is not strategy,
but execution. Organizations that succeed will treat SASE as an operating model transformation and
prioritize partners who offer a clear, sustainable path to consistent execution over time.
OPEN SYSTEMS | 2026 MANAGED SASE & ZERO TRUST REPORT ©2026 Cybersecurity Insiders. All Rights Reserved. 8

Action Plan: Closing the SASE Execution Gap
The survey findings point to a consistent pattern: organizations have committed to SASE and Zero
Trust strategically but struggle to operate them at scale. Closing the execution gap requires focus on a
small number of practical decisions - and an honest assessment of whether internal capacity matches
operational ambition.
STEP 1: CLOSE THE VISIBILITY GAP BEFORE EXPANDING SCOPE
Visibility degrades fastest at the edges: remote users, multi-cloud traffic, and third-party access. Before
extending Zero Trust to new domains, ensure observability is unified across what you already operate.
Action: Prioritize:
Select a high-risk third-party vendor • End-to-end visibility across users, applications, and data flows
and trace their access journey from
• Platforms with native data unification (vs. aggregated feeds) for
identity to application. If correlating a
consistent monitoring and cleaner alerting from core to edge
third-party identity to a specific data
request takes more than five minutes, • AI-assisted detection to extend team capacity and reduce noise
the visibility gap is an operational risk.
STEP 2: PLAN DELIBERATELY FOR THE MIDDLE STATE
Most organizations will operate with parallel VPN and ZTNA environments for longer than
expected. Treat this as a managed phase, not a temporary inconvenience.
Action: Prioritize:
Conduct a policy overlap assessment. • Clear criteria for which users and applications remain on VPN
Identify which user groups and vs. ZTNA
applications are currently accessible
• Defined migration triggers and timelines for each application tier
via both VPN and ZTNA, then
eliminate legacy VPN rules that • Operational playbooks that reduce support overhead during
persist only by default. coexistence
STEP 3: MATCH THE OPERATING MODEL TO EXECUTION CAPACITY
The shift toward co-managed SASE reflects a realistic assessment of what internal teams can sustain over
time. Evaluate delivery models based on ongoing operational load, not just initial deployment effort.
Action: Prioritize:
Track your Maintenance vs. • Co-managed models to reduce risk and sustain forward
Innovation Ratio. If more than half of momentum
senior engineering time is spent on
• Delivery models designed for continuous operation, not one-time
integration, patching, and firefighting
deployment
rather than forward progress, the
execution gap is structural.
OPEN SYSTEMS | 2026 MANAGED SASE & ZERO TRUST REPORT ©2026 Cybersecurity Insiders. All Rights Reserved. 9

The SASE Partner Checklist
When selecting a managed or co-managed SASE partner, the survey data highlights five evaluation
criteria:
Continuous operations:
Clear SLAs for detection, escalation, and resolution - not just uptime
Platform integration:
Native architectures that reduce policy fragmentation and integration
overhead
Engineering depth:
Direct access to senior engineers, not tiered support queue
Compliance and residency:
Demand certifications (ISO 27001, SOC 2) plus clarity on data hosting
jurisdiction to manage extraterritorial legal risks (e.g., CLOUD Act)
Partnership track record:
Ask for customer retention rates and average tenure as indicators of
sustained execution quality.
Cost still matters, but consolidation is the primary financial lever. Organizations funding SASE through
retirement of legacy estates show stronger alignment between investment and outcomes than those
focused on standalone cost reduction.
OPEN SYSTEMS | 2026 MANAGED SASE & ZERO TRUST REPORT ©2026 Cybersecurity Insiders. All Rights Reserved. 10

Methodology and Demographics
This report reflects the perspectives of senior practitioners directly accountable for making secure
access work in real-world environments. The survey includes 505 senior security and IT leaders,
with 263 respondents from the United States and 242 from the United Kingdom, all responsible for
managing connectivity, performance, and security across hybrid environments spanning remote
users, cloud applications, data centers, branch locations, and third-party access. Two-thirds hold
Director-level roles or above, and nearly 70% work in senior security, IT, or network operations
functions - placing them at the center of SASE and Zero Trust execution decisions.
At the aggregate level (n=505), results have a margin of error of approximately ±4.4 percentage points
at a 95% confidence level.
CAREER LEVEL
| US  | 32% |     |     | 21% |     |     | 16% |     |     | 13% | 5%  | 8% 5%  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
| UK  | 27% |     | 22% |     |     | 17% |     |     | 12% | 5%  |     | 12% 5% |
Director        Senior Leadership (SVP, VP, Head)             Manager             C-Level Executive (CIO, CISO, CSO, CTO)          Architect
Specialist/Analyst           Other
DEPARTMENT
| US  | 29% |     |     | 21% |     | 13% |     | 10% |     | 8%  | 5%  | 14% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UK  | 32% |     |     | 24% |     |     | 12% |     | 10% | 5%  | 3%  | 14% |
Network Security / Cybersecurity             IT Leadership / IT Operations          Network Operations / Network Infrastructure
Cloud Architecture / Cloud Security              Enterprise Architecture               OT / ICS / Industrial IT           Other
COMPANY SIZE
| US  | 29% |     |     |     | 37% |     |     |     |     | 24% |     | 10% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UK  | 24% |     |     | 34% |     |     |     |     | 29% |     |     | 13% |
1,000–5,000            5,001–10,000           10,001–25,000            25,001–50,000
INDUSTRY
| US  | 23% | 18% |     |     | 16% |     |     | 15% |     | 10% | 8%  | 10% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UK  | 27% | 13% |     |     | 12% |     | 17% |     | 10% |     | 8%  | 13% |
Finance         Manufacturing/Chemicals             Healthcare/Pharmaceuticals            Professional Services          Insurance
Utilities          Other
Reuse of content
We encourage the reuse of data, charts, and text published in this report under the terms of this Creative Commons
Attribution 4.0 International License. You’re free to share and make commercial use of this work as long as you attribute
the report as stipulated in the terms of the license. For example: “2026 Managed SASE and Zero Trust Report by
Cybersecurity Insiders and Open Systems.”
OPEN SYSTEMS   |    2026 MANAGED SASE & ZERO TRUST REPORT   ©2026  Cybersecurity Insiders.  All Rights Reserved. 11

Open Systems is an international provider of co-managed SASE and
Zero Trust operating models, helping enterprises and organizations
securely operate complex hybrid and multi-cloud environments.
Founded in 1990 and headquartered in Switzerland, the company
generates over USD 100 million in annual revenue and supports
global enterprise customers with more than 60,000 employees
across operations in more than 180 countries.
Open Systems combines cloud-native networking and security with
transparent, co-managed 24×7 operations to close the execution
gap many organizations face when deploying modern architectures.
As a European alternative to US- and Israel-based security
providers, Open Systems places strong emphasis on regulatory
alignment, operational visibility and shared responsibility, enabling
secure, reliable and scalable network and security operations in an
increasingly distributed IT landscape.
www.open-systems.com

STRATEGIC INSIGHT FOR CYBERSECURITY LEADERS
Cybersecurity Insiders provides independent research and analysis focused
on the operational reality of enterprise cybersecurity. We gather insights from
senior security and IT leaders to examine how high-level strategies translate
into day-to-day execution. Our analysis identifies the measurable gaps between
intended strategy and actual risk exposure, offering a credible, data-driven
foundation for security decision-making and industry benchmarking.
For more information, visit
cybersecurity-insiders.com
©2026 Cybersecurity Insiders. All Rights Reserved.
Jan 2026 // Version 1.5

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-28", "model": "gemini-3.5-flash-lite"} -->
