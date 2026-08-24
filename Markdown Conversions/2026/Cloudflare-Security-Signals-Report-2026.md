2026
Cloudflare Security
Signals Report
Autonomic Resilience

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
FOREWORD BY MICHELLE ZATLYN
Everything is changing.
AI is moving from pilot to production, autonomous systems are accelerating decision-making, and
the digital economy is evolving in real time. For leaders ready to act, that pace of change creates
real opportunity.
Resilience has become the new competitive edge. As intelligent systems reshape the digital
economy, leaders can design defenses to anticipate change, engineer systems that adapt, and
turn volatility into an advantage.
Cloudflare operates one of the world’s largest global networks, spanning more than 330 cities in
over 120 countries. We protect millions of Internet properties, stop over 230 billion cyberattacks
every day, and handle 2.5 billion bot requests daily. From this vantage point, we see both the risks
and the opportunities shaping the Internet.
The 2026 Cloudflare Security Signals Report delivers practical insights leaders need today,
mapping the forces reshaping the digital landscape, so you can govern intelligent systems,
modernize securely, and build resilience from the core.
We’re on a mission to help build a better Internet. In 2026, that means helping you operate
securely and confidently — at machine speed.
Michelle Zatlyn
Co-founder, President,
and Co-chair, Cloudflare
Cloudflare Security Signals Report | Autonomic Resilience 22

EExxeeccuuttiivvee ssuummmmaarryy 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
EXECUTIVE SUMMARY Six critical fault lines
These fault lines do not stand alone. Pressure in one area can intensify weakness in others.
For today’s highly
interconnected and
automated enterprises, the 1 2
Taming the algorithm: Trust at machine speed:
“absorb shocks and recover”
Governing AI at scale Engineering autonomy
model no longer works.
AI programs often appear disciplined, governed, and value- Autonomous systems perform well when conditions are
driven. Yet under scrutiny, many leaders cannot clearly explain predictable. Under stress, decisions move faster than human
This approach relies on the naive assumption that we where AI is running, what data it touches, or who is accountable oversight, and trust is assumed rather than engineered. This
can accurately predict and prepare for every specific when outcomes fail. Progress on the surface often masks fault line tests whether delegation was deliberate or whether
disruption. AI systems act autonomously; cloud a visibility and ownership gap that becomes exposed when authority quietly shifted to machines without clear boundaries,
platforms concentrate critical workloads; supply chains regulators, customers, or incidents apply pressure. accountability, or real-time control.
extend deep into opaque ecosystems. In this new reality,
security leaders require autonomic resilience: systems
that do more than withstand stress — they regulate,
adapt, and recover in real time.
3 4
Signals of intent:
Shadow supply chains:
But while many organizations appear mature, modern,
Intelligence to foresight
and well-governed, autonomic resilience is not visible Exposing hidden dependencies
in steady state. It is a leadership outcome revealed only
While data-driven intelligence programs often look
Enterprises appear diversified and partner-rich, but depend on
under sustained and severe stress. comprehensive, insights that arrive too late fail to shape decisions.
layers of third- and fourth-party services they do not fully see.
This fault line separates organizations who use early signals
This report is built on a simple premise: The greatest When disruption occurs, the first failure is often not response,
to continuously refine decisions, strengthen anticipation, and
risks enterprises will face in 2026 do not come from but discovery. This fault line reveals whether dependency risk is
sharpen response over time — from those who learn only after
obvious weaknesses. They emerge from hidden fault intentional and visible, or inherited and opaque.
damage is done.
lines, areas that look sound in normal operations, but
fracture when speed, scale, or disruption increase.
Within these chapters, we provide executives with a
blueprint to surface these fault lines before they break. 5 6
The debt trap: Cloud mirage:
Each section offers pointed questions to spark internal
debate and uncover hidden fragility within their own Legacy architecture as strategic risk Decoupling cascading risk
organizations. In an era of intelligence, autonomy, and
Legacy architectures can appear stable in day-to-day Cloud strategies promise scale and efficiency, but shared
speed, success belongs to leaders who design their
operations. Under modern attack velocity and regulatory control planes and tight dependencies concentrate failure.
enterprises to sense, adapt, and self-correct under
scrutiny, they become brittle, consuming time, talent, and When stress hits, systems fall together. This tests if resilience is
stress, while protecting critical outcomes as
resilience faster than organizations can adapt. This fault line engineered for containment or just assumed via recovery plans.
conditions change.
exposes whether architecture enables evolution — or quietly Mature organizations limit blast radius and grow more fault-
limits it. tolerant with every disruption.
Cloudflare Security Signals Report | Autonomic Resilience 33

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Content
2 Foreword by Michelle Zatlyn
3 Executive summary
5 Taming the algorithm: Governing AI at scale
9 Trust at machine speed: Engineering autonomy
13 Shadow supply chains: Exposing hidden dependencies
17 Signals of intent: Intelligence to foresight
22 The debt trap: Legacy architecture as strategic risk
27 Cloud mirage: Decoupling cascading risk
32 Conclusion: The leadership principles for enduring advantage
33 About Cloudflare
43 Endnotes
Cloudflare Security Signals Report | Autonomic Resilience 4

Executive summary 11.. TTaammiinngg tthhee aallggoorriitthhmm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
1
Taming the algorithm:
Governing AI at scale
Cloudflare Security Signals Report | Autonomic Resilience 55

Executive summary 11.. TTaammiinngg tthhee aallggoorriitthhmm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Taming the algorithm: Speed wins. Permission loses. Frameworks like NIST AI RMF and ISO/IEC 42001 provide guidance, but
real assurance comes from how they are implemented and enforced.
Governing AI at scale Every AI system is a data system before it is an intelligence system. If
AI’s accessibility has fundamentally changed how technology enters
leaders cannot map its data flows, misuse paths, and failure modes, it is
the organization. Employees and teams no longer wait for centralized
not ready to scale.
approval. AI tools are adopted quietly — through browser extensions,
embedded SaaS features, APIs, and developer platforms — often with
AI adoption is accelerating faster than enterprise
good intent and immediate productivity gains.
governance models can adapt. What began as
isolated experimentation has become embedded
The consequence is predictable: AI spreads faster than governance. In
— across workflows, developer tooling, customer
fact, 98% of employees use unsanctioned apps across shadow AI and
interactions, and third-party software that
shadow IT use cases.1
organizations consume but do not directly control.
One pattern repeats every time decision-
But before AI acts independently, visibility,
Unsanctioned tools introduce inconsistent security controls and unclear
ownership, and constraints must already be in place. making is automated: Outcomes move
data handling practices, and diffuse accountability. For boards, this
Once decisions move at machine speed, these
creates an uncomfortable reality. AI risk is material, but often poorly faster than accountability. AI doesn’t
questions can no longer be debated.
quantified and weakly owned.
create that gap — it exposes it. When
While most executive teams recognize AI as a
This does not reflect a failure of discipline. It is a structural mismatch
board-level issue, few can clearly articulate where responsibility is unclear, governance
between legacy approval models and AI’s frictionless adoption curve.
AI is used, what data it touches, or how risk is being
becomes performative, no matter how
managed across their enterprise. This gap between
Governance can no longer be an approval step. It must become an
AI awareness and control is now one of the most polished the policy looks.”
always-on system built on guardrails, continuous visibility, and standards
consequential blind spots in modern leadership.
that scale as fast as AI adoption does.
The question is no longer whether AI delivers value. Joe Sullivan, former CSO, Uber
It is whether leadership has sufficient visibility to
govern AI’s impact on resilience, trust, cost, and
Data is the prize and the liability.
accountability at scale.
AI is no longer experimental. It operates at the AI systems derive value from access: to data, to models, and to
heart of the enterprise — and must be governed downstream decisions. Under pressure to deliver quickly, organizations
Shadow AI is shadow IT at machine speed.
with the same rigor as money, risk, and regulation. often expand access faster than they strengthen controls. Entitlement
In this environment, confidence is the real boundaries blur. Data flows become opaque. Less-trusted services gain
differentiator. proximity to sensitive information. Ninety-seven percent of organizations AI can proliferate invisibly across employees, contractors, product teams,
that reported an AI-related security incident in 2025 lacked proper AI and third-party vendors without triggering formal review. This creates an
access controls.2 auditability gap at precisely the moment regulators are demanding greater
transparency.
Traditional security frameworks were not designed to capture AI-native
risks such as prompt manipulation, unintended data retention, or model Governments and regulators are increasingly requiring documented AI
misuse. As a result, many organizations can certify compliance without inventories, traceable data lineage, and explainability for automated decisions.
truly understanding AI-driven exposure. The inability to demonstrate control is quickly becoming a compliance failure,
not just a maturity issue.
Cloudflare Security Signals Report | Autonomic Resilience 6

Executive summary 11.. TTaammiinngg tthhee aallggoorriitthhmm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Leading organizations closing this gap are shifting from episodic audits
to continuous assurance, combining comprehensive logging, automated
evidence collection, and controls that detect unsanctioned AI usage in
real time.
We are witnessing the largest
Governance tends to feel sufficient right
If AI activity cannot be logged, explained, and evidenced, it cannot be proliferation of shadow IT in
up until something unexpected happens.
defended to regulators, customers, or the board.
history, as employees adopt
With AI, that moment arrives earlier and
ungoverned AI services and
with broader impact. The organizations
Top threat categories
agents. Unlike traditional SaaS
in email detection that navigate this well treat AI less like
shadow IT, these AI capabilities
a tool and more like a supply chain —
are difficult to detect or block;
Link-based tracing origin, ownership, and influence,
they can assume real user
25%
detection
even when it lives outside their walls.” identities, blend into standard
Identity activity, and operate at machine
19%
deception
Kate Kuehn, Global Head of Cybersecurity speed. The CISO’s mandate is
Strategy, World Wide Technology not to block this adoption, but to
Brand
16%
impersonation engineer secure AI capabilities
that eliminate the need for
IP
10%
reputation ungoverned tools.”
Regulation lives in code, not just policy.
Domain
9% Michael Goodman, Vice President /
age
Jurisdictions worldwide have moved decisively toward enforceable AI Chief Digital and Security Officer
0 5% 10% 15% 20% 25% governance regimes that balance innovation with accountability. In the US (CD and SO), Hitachi
alone, state lawmakers introduced 1,208 AI-related bills, resulting in 145
Percentages do not add to 100% as emails can have multiple threat categories. new laws enacted in a single year.3 Penalties increasingly extend beyond
fines to personal and fiduciary exposure.
Source: Cloudflare Radar
This signals a broader shift: AI governance is being reframed as an
enterprise risk and leadership responsibility and not a discretionary
Link-based attacks and identity deception dominate modern email threats.
technical policy. Organizations that engineer AI governance as
These campaigns exploit trust signals rather than technical vulnerabilities.
infrastructure turn trust into a growth enabler, not a constraint.
As AI lowers the cost of producing convincing, personalized deception,
governance must extend beyond model oversight to authentication, identity
integrity, and decision traceability.
Cloudflare Security Signals Report | Autonomic Resilience 77

Executive summary 11.. TTaammiinngg tthhee aallggoorriitthhmm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
QUESTIONS FOR THE C-SUITE
Exposing blind spots for AI governance
At machine speed, unclear ownership, limited visibility, and weak guardrails become
business liabilities, thus making these questions leadership imperatives.
Q1 Q2 Q3 Q4 Q5
Who is formally What constraints How do we If we were audited As AI adoption
accountable for AI define acceptable determine if AI use tomorrow, could we accelerates, does our
governance at the AI behavior in our is appropriate — not demonstrate a complete, governance model
executive level? organization today? just compliant? shared inventory of remain coherent?
AI use across the
And where does that Are those constraints Are AI uses compliant but enterprise? Or, does it fracture across
authority begin and end? clearly articulated, misaligned with business functions, vendors, and
Is this responsibility explicit, enforceable, and intent, ethics, or risk regions? Is governance
Or would definitions,
operationalized, or assumed consistent across teams tolerance? Do we govern treated as a static
shadow usage, and
until something goes — or do they largely rely outcomes — or just access framework, or a living
third-party exposure
wrong? on trusting our workforce and tools? How do we operating system?
surface gaps in our
to comply with policy? identify compliant versus
understanding?
non-compliant?
Cloudflare Security Signals Report | Autonomic Resilience 8

Executive summary 1. Taming the algorithm 22.. TTrruusstt aatt mmaacchhiinnee ssppeeeedd 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
2
Trust at machine speed:
Engineering autonomy
Cloudflare Security Signals Report | Autonomic Resilience 99

Executive summary 1. Taming the algorithm 22.. TTrruusstt aatt mmaacchhiinnee ssppeeeedd 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Bot (automated) vs. human
Trust at machine The ‘velocity paradox’ — when the
HTTP requests distribution
business moves faster than oversight
speed: Engineering
autonomy Traditional security assumes time. An alert is raised. A human
investigates. A decision is made. Autonomous systems eliminate that
Bot
window. AI agents can execute thousands of actions, like reconfiguring
infrastructure, rebalancing portfolios, and adjusting supply chains, in a
Enterprises are entering their most consequential matter of milliseconds. If an agent is compromised, misaligned, or simply 29.8%
transformation since the commercial Internet. We wrong, the impact is realized before a human can intervene.
have moved beyond AI-assisted tools into the Human
era of the “autonomous enterprise” — where AI This is the velocity paradox: The same autonomy that drives value also
agents and agentic workflows execute end-to- collapses the margin for error. Attackers understand this. AI-driven
70.2%
end business processes with minimal or no human phishing, impersonation, and manipulation increasingly target automated
intervention. This fault line assumes AI systems workflows rather than people.
are already embedded and acting autonomously.
The implication is clear: Security cannot sit outside the system. It must
Unlike the AI governance challenge which focuses
be embedded into the decision layer itself, governing intent, not just
on visibility, oversight, and accountability, this fault
access. This fault line is not about predicting attacks. It is about ensuring
line addresses what happens after authority has
that when your own systems act, they do so within the boundaries
already been delegated to machines. The question Source: Cloudflare Radar
deliberately designed by leadership.
is no longer where AI is used or who owns it; it
is whether trust holds when decisions are made
We are no longer operating on a human-first Internet. Algorithms increasingly
without humans in the loop.
interact with algorithms, often without direct human oversight. Governance
The new control plane for autonomous AI
models built around user authentication, and employee access controls are
Gartner predicts that by 2026, nearly half of
misaligned with this reality.
enterprise applications are expected to embed
1. Identity must extend beyond humans
task-specific AI agents, up from single-digit
adoption just a year earlier.4 This shift delivers
2. Probabilistic systems require deterministic guardrails
Non-human identities — AI agents, service accounts, bots — now
unprecedented speed and efficiency while also
outnumber human users by orders of magnitude. Bots are responsible
introducing a structural risk: Business decisions AI systems reason probabilistically. Security cannot. While agents may
for ~30% of HTTP traffic that Cloudflare serves,5 and an astonishing 92%
now outpace human oversight. optimize, negotiate, or recommend, the rules governing what they are
of all login attempts observed by Cloudflare come from bots — often
allowed to do must be absolute. Policies cannot be inferred, they must be
Trust can no longer be periodic, manual, or credential stuffing attacks.6 Yet most enterprises still govern identity as if
enforced.
retrospective. In an autonomous environment, people are the primary actors.
trust must be continuous, verifiable, and enforced This requires:
The risk is acute. AI systems are frequently deployed without strong
at machine speed. Securing this future requires a
authentication, scoped authorization, or lifecycle controls. When
fundamental shift, from “trust but verify” to “trust • Policy-as-code that defines non-negotiable constraints
compromised, they operate with machine-scale blast radius.
by design” and ultimately to systems that grow • Real-time enforcement layers that intercept intent before execution
more trustworthy as they are tested.
Every AI agent must have a verifiable, cryptographic identity, governed
• Separation between decision-making and authorization
through machine identity management. Credentials must be short-lived,
context-aware, and revocable in real time. Autonomy without identity is True autonomy exists only where boundaries are explicit, enforced, and
abdication. designed in advance.
Cloudflare Security Signals Report | Autonomic Resilience 10

Executive summary 1. Taming the algorithm 22.. TTrruusstt aatt mmaacchhiinnee ssppeeeedd 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
The upside extends beyond cost reduction. With strong guardrails in
place, leaders gain the confidence to deploy automation deeper into
revenue-critical workflows — improving responsiveness, capital velocity,
Automation changes the
Human judgment remains essential, and competitive differentiation. Well-governed autonomy becomes a
growth enabler, not just a risk control. Security at machine speed is not speed of decisions, but it also
but it no longer operates at the speed
overhead. It is the price of scaling autonomy without fragility.
changes the blast radius of
systems require. In environments where
mistakes. The question for
machines interact continuously, trust has
The leadership system for autonomy leaders is ‘How do we design
to be assumed, enforced, and verified by
accountability and trust into
design — much like safety systems we The rise of autonomous systems is redefining the role of the CISO and, by
systems that act on their
extension, the responsibilities of the entire C-suite. Security leadership is
rely on without noticing, until they fail.”
own?’”
no longer about protecting systems after decisions are made; it is about
orchestrating trust in environments where machines act independently.
Oliver Newbury, Senior Advisor, TPG Kevin Jones, Global Chief Information
One CISO recalled the first time an AI system stopped a multimillion-dollar
Security Officer, Bayer
transaction on its own. The decision was correct but it triggered a deeper
question in the boardroom: Who had actually authorized the machine to
make that call? The technology was ahead of the governance.
This shift demands clear executive choices: where autonomy is allowed,
3. Trust requires observability, not assumptions where humans stay in the loop, what transparency is required across
models and data, and how risk is measured when machines make
As AI systems adapt, drift, and learn, yesterday’s assurance quickly decisions.
becomes irrelevant. Without deep observability, leaders cannot
Metrics built for human response times are no longer enough. Leaders
distinguish between legitimate autonomous behavior and manipulation.
must track autonomous risk, decision integrity, and systemic drift. Yet
Unauthorized, often invisible AI usage further compounds risk by only about 15% of corporate boards receive regular AI-related risk and
introducing ungoverned models, data flows, and decision logic into performance metrics.8
core operations.
As autonomy spreads, security, compliance, and technology can no
longer operate in silos. Security influences revenue velocity. Compliance
determines market access. Technology defines accountability. Trust at
The economic case
machine speed is not a security program — it is a leadership system
that unifies resilience, governance, innovation, and reputation under one
Embedding AI and automation into security operations delivers executive mandate.
measurable financial returns. Organizations that use these capabilities
extensively resolve breaches 80 days faster and reduce average breach
costs by $1.9 million compared to those that do not.7
Cloudflare Security Signals Report | Autonomic Resilience 1111

Executive summary 1. Taming the algorithm 22..  TTrruusstt  aatt  mmaacchhiinnee  ssppeeeedd 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
QUESTIONS FOR THE C-SUITE
Moving from automation to autonomy
These questions expose whether leadership has intentionally designed boundaries around how
decisions are made at machine speed, and how risk is owned in real time.
| Q1  | Q2  | Q3  | Q4  | Q5  |
| --- | --- | --- | --- | --- |
Which enterprise  When machines  Where are decisions  Can we explain and  Does our trust
decisions are already  act on their own,  executed by software  justify an autonomous  model scale at
being made by  who is accountable  rather than people? action as it occurs?  machine speed?
| autonomous systems?  | in real time — the  |     |     |     |
| -------------------- | ------------------- | --- | --- | --- |
system owner, the  Where have we relaxed  Or, does it take days later  If autonomy doubled within
|                         |                         | controls over software?  | during incident reviews?  | the next year, would our  |
| ----------------------- | ----------------------- | ------------------------ | ------------------------- | ------------------------- |
| Which decisions are we  | business owner, or the  |                          |                           |                           |
|                         |                         |                          | Is intent observable      | trust model absorb the    |
Are machines held to
| deliberately retaining  | executive sponsor? |     |                       |                               |
| ----------------------- | ------------------ | --- | --------------------- | ----------------------------- |
|                         |                    |     | at machine speed, or  | acceleration — or fail under  |
higher standards than
for humans? Is that
|     |     |     | reconstructed under  | it? Is trust engineered for  |
| --- | --- | --- | -------------------- | ---------------------------- |
humans or quietly
boundary designed,
Is ownership of  trusted more? pressure? scale and speed, or inherited
documented, and
|     | autonomous risk clearly  |     |     | from human-era governance? |
| --- | ------------------------ | --- | --- | -------------------------- |
revisited — or implicit
defined while the
and drifting?
system is operating,
or only examined after
something goes wrong?
Cloudflare Security Signals Report | Autonomic Resilience 12

Executive summary 1. Taming the algorithm 2. Trust at machine speed 33.. SShhaaddooww ssuuppppllyy cchhaaiinnss 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
3
Shadow supply chains:
Exposing hidden
dependencies
Cloudflare Security Signals Report | Autonomic Resilience 1133

Executive summary 1. Taming the algorithm 2. Trust at machine speed 33.. SShhaaddooww ssuuppppllyy cchhaaiinnss 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Shadow supply The risk that was never approved • AI has introduced a new, opaque layer of dependency. Employees
increasingly rely on generative AI tools and embedded AI services
chains: Exposing that expose sensitive data to fourth-party models. Third-party risk
Modern supply chains no longer stop at direct vendors. They extend into
teams often lack clarity into how these models use data, retain
SaaS platforms, cloud-native services, AI model providers, open-source
hidden dependencies information, or train on enterprise inputs, raising regulatory, IP, and
components, and subcontracted infrastructure layers that operate well
data-sovereignty risks.
beyond procurement’s line of sight. Failures anywhere in this extended
web — whether a breach, outage, or compliance lapse — can cascade • Regulatory expectations are hardening. Across the globe, regulators
quickly into customer harm, regulatory exposure, and systemic disruption. are moving decisively from guidance to enforcement. Organizations
Our hyperconnected economy is no longer
are increasingly expected to demonstrate visibility into third- and
defined by what you control, but by what can
The core challenge is visibility, and AI is accelerating both the risk and fourth-party dependencies, particularly where personal or financial
break you that you don’t even see. Many leaders
the opacity. Most organizations cannot see their extended digital supply data or critical infrastructure are involved. Going forward, leaders will
have hardened their perimeter, modernized
chains, let alone govern them in real time. Every AI model, API, and be expected not just to assess vendor risk, but to quantify operational
infrastructure, and tightened governance, yet the
automated workflow quietly expands dependencies beyond traditional risk arising from extended supply chains. The result? A widening gap
most consequential risks now live beyond their line
oversight. Audits are static while risk is dynamic. between what regulators expect and what organizations can
of sight, embedded in third, fourth, and nth party
currently prove.
ecosystems they neither own nor fully influence.
The uncomfortable truth: You can be operationally
When systems are assembled, not built
mature and still systemically fragile. The top 10 most impersonated
brands in phishing campaigns
Shadow supply chains are not edge cases; they A modern car is built by hundreds of suppliers, and the hardware parts,
are the natural outcome of digital assembly at chips, and software come from many vendors, each with their own supply
scale. Every SaaS integration, API call, open- chains. A small hidden defect can become a safety issue at highway 1 Windows 6 Amazon
source library, and AI service adds another layer speed, which is why automakers invest heavily in traceability and
of inherited risk. The leadership question is no continuous testing.
longer “Do we have supply chain risk?” but “Do 2 SANS 7 Instagram
we understand which external failure could halt Enterprise IT now mirrors this model. One application can depend on
revenue, erode trust, or trigger regulatory scrutiny dozens of SaaS tools, cloud services, APIs, open-source libraries, and AI
3 Microsoft 8 Costco
tomorrow?” models, each with sub-processors beneath them. The enterprise sees
the interface, not the layers underneath. That is the shadow supply chain.
The impact is already material. Supply chain 4 Stripe 9 YouTube
breaches average $4.91 million, higher than the The difference is discipline. In automotive, parts are tracked and recalls
global breach average of $4.44 million.9 are precise. In IT, when a library or AI component is compromised,
5 Facebook 10 iCloud
The strategic choice for leaders is to treat supply many organizations first scramble to learn if they are exposed. Annual
chain risk as a compliance exercise and accept questionnaires cannot keep pace with systems that change weekly.
periodic surprise, or treat it as a live operational Visibility and continuous assurance are becoming as essential to digital
Source: Impersonation attempts observed by Cloudflare Email Security
exposure that demands continuous visibility, systems as quality control is to cars.
runtime assurance, and architectural guardrails.
Three forces are accelerating this risk: The most impersonated brands are not random targets. They are
foundational platforms embedded in enterprise workflows — identity
• Trust-by-proxy has become the default operating model. Enterprises
providers, payment systems, cloud platforms, operating systems. Attackers
trust their vendors. Vendors trust their suppliers. Few parties verify the
exploit familiarity and dependency, turning trusted digital infrastructure into
entire chain. Competitive concerns and limited internal visibility mean
an attack vector. Shadow supply chains are not just operational exposure;
sub-supply chains are rarely disclosed in detail.
they are identity and brand exposure.
Cloudflare Security Signals Report | Autonomic Resilience 14

Executive summary 1. Taming the algorithm 2. Trust at machine speed 33.. SShhaaddooww ssuuppppllyy cchhaaiinnss 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
From static assurance to continuous However, leading organizations share a common pattern: They treat
supplychain risk as a system, rather than a compliance function. They
transparency
insist on knowing what applications exist and how they connect. They
require transparency to flow down the supply chain, not stop at the first
Interconnected ecosystems
Solving the shadow supply chain problem does not require more contract. They use network-level signals to uncover shadow activity
paperwork. It requires a different operating model. The future of supply rather than relying on self-attestation. They apply zero trust principles reward speed and
chain assurance is continuous transparency: real-time visibility into to machine-to-machine access, not just users. And they continuously specialization, but they
what is actually running, connected, and exchanging data across the reassess vendor risk based on behavior, not reputation.
also distribute risk in ways
ecosystem.
The payoff is tangible. Eighty-five percent of organizations leading
contracts can’t capture.
One CISO described discovering a critical supplier only after unusual in application modernization are actively cutting redundant tools and
Operational insight, not
traffic appeared in network logs. The vendor was legitimate, but no shadow IT to reduce their supply chain attack surface and improve
one realized how deeply it was embedded. The lesson was simple: You operational speed.12 These are not technical tweaks; they are leadership paperwork, is what ultimately
cannot govern what you cannot see. choices about how much uncertainty an organization is willing to tolerate
contains exposure.”
in the systems it depends on every day.
This shift is already underway. Software Bills of Materials (SBOMs) and
Vulnerability Exploitability eXchange (VEX) are moving from compliance
Sandip Wadje, Global Head of
artifacts to operational signals. Expect that procurement will increasingly
Emerging Technology Operational
require not just contracts, but live, machine-readable disclosures that
map components, dependencies, and exploitability as they change.10 Risks and Intelligence, BNP Paribas
At the same time, enforcement is moving closer to where risk manifests.
Network- and connectivity-layer controls allow organizations to observe Risk rarely comes from the dependencies
behavior, detect unauthorized data flows, and identify shadow suppliers
everyone expects, it emerges from the
as activity occurs.
ones no one can see. When visibility
Supply chain assurance becomes an operational capability rather than
is incomplete, audits offer comfort but
a periodic review. Trust is continuously verified. Risk is surfaced early.
Governance moves at the same pace as the ecosystem it is meant little protection. True resilience comes
to protect.
from architectures that reveal their
dependencies as they operate.”
Trust, but continuously verify
Tim Brown, CISO, SolarWinds
Thirty percent of breaches in 2025 were linked to third-party
involvement, twice as many as the prior year11 — illustrating how
deeply supply chain relationships now factor into risk exposures beyond
traditional internal boundaries.
Cloudflare Security Signals Report | Autonomic Resilience 1155

Executive summary 1. Taming the algorithm 2. Trust at machine speed 33.. SShhaaddooww ssuuppppllyy cchhaaiinnss 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
QUESTIONS FOR THE C-SUITE
Governing the risk you don’t control
Supply chain risk can no longer be managed. It is something organizations live with.
Decide whether that risk is visible and governed — or opaque and assumed.
Q1 Q2 Q3 Q4 Q5
Which critical business How will we respond Where have we How quickly can we Are we managing
processes would to regulatory or board reduced visibility determine whether supply chain risk as a
we pause if a key questions about in the supply chain a newly disclosed continuous discipline
dependency failed? ecosystem risk? to preserve speed, vulnerability affects us? or a periodic audit?
convenience, or
Would we know why Can we answer vendor relationships? Is accountability for Does our model evolve as
it failed? Can we trace questions about these response clearly fast as our ecosystem, or
revenue and customer risks without pointing to assigned? Is exposure does it merely reassure
Are those deliberate
impact to specific a contract? Do we have discovery measured in us that last year’s controls
choices? Who decided to
dependencies in real time, technical visibility over minutes, days, or weeks? were reviewed?
accept those trade-offs?
or would we only discover the operational path of
Which dependencies are
exposure after the damage supplier risk?
effectively “off-limits” to
is done?
scrutiny?
Cloudflare Security Signals Report | Autonomic Resilience 16

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 44.. SSiiggnnaallss ooff iinntteenntt 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
4
Signals of intent:
Intelligence to foresight
Cloudflare Security Signals Report | Autonomic Resilience 1177

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 44.. SSiiggnnaallss ooff iinntteenntt 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Signals of intent: Top industries targeted
From tactical feed to strategic signal
by DDoS attacks, 2025
Intelligence to
Modern threats are high velocity, high volume, and increasingly
shaped by geopolitics, economic incentives, and industry- Rank Industry
foresight
specific vulnerabilities. In this environment, threat intelligence
can no longer be treated as an optional security function or
1 Gambling and gaming
limited to checkbox reviews of generic external feeds. Context
A glance at the headlines will tell you that — at the enterprise, industry, and global levels — matters,
adversary activities continue to proliferate, at and executives must demand intelligence that connects threat
ever greater speed and scale. With AI-assisted activity directly to business impact, operational exposure, and 2 Telecommunications
reconnaissance and toolkits, more cybercriminals strategic risk.
are capable of greater and more sophisticated
Plainly, there is too much activity on the attacker front to stay
attacks than ever. Additionally, the window
on top of everything. Defense requires speed and skill, and 3 Technology and services
between threat emergence and business impact
frequently both are in short supply. While your security strategy
is increasingly shorter, as the average time it takes
should address and acknowledge the full inventory of assets
an adversary to start moving laterally has fallen to
and liabilities under your protection, using intelligence to
just 48 minutes.13
4 Banking and financial services
understand not only the technical elements of threats, but also
Once considered a discretionary capability, threat their context, allows you to tune your security program in favor
intelligence has become foundational. Fifty-two of prioritizing risk reduction in areas that are most impactful to
percent of organizations now maintain dedicated, your organization.
5 Retail
in-house cyber threat intelligence (CTI) teams.14
Deciding what is important for the organization generally
In the fast-moving threat landscape, intelligence
involves board and leadership alignment on how to integrate
has grown from a security function into a
core business principles, market forces, regulations, and
leadership capability. Success is measured by
This ranking is an average of globally observed DDoS attacks at both the network and application
stakeholder inputs. This context is invaluable when evaluating
the ability to analyze CTI data within a business layer. Technology and services ranks #1 for network-layer attacks. Gaming and gambling ranks #1
threat intelligence as it gives context for the enterprise needed for application-layer attacks.
context, deciphering signals from noise and
to determine which CTI data is most useful.
translating knowledge into actionable foresight.
Source: Cloudflare Radar
It is in this way that threat intelligence can be used to “tune
Threat intelligence is no longer about knowing
out” extraneous information — irrelevant vulnerabilities, or
more. It is about knowing what matters — early
attacker groups that specifically target dissimilar industries —
enough to act. Attack activity is not evenly distributed. Adversaries prioritize sectors tied
so that you can focus your resources where they can have the
to economic leverage, infrastructure stability, and geopolitical relevance.
greatest impact based on the threat landscape specific to your
Concentration across specific industries reflects strategic intent, not
organization. Threat intelligence that does not inform executive
randomness. Effective intelligence anticipates where pressure will intensify —
choices is simply noise to be tuned out.
and aligns defenses accordingly.
Cloudflare Security Signals Report | Autonomic Resilience 18

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 44.. SSiiggnnaallss ooff iinntteenntt 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Threat intelligence has become For the CFO, threat intelligence is not justified by alert volume,
but by its ability to reduce the probability and impact of material
non-negotiable
business disruption — downtime, fraud, regulatory intervention,
or reputational damage. Organizationally, this demands clarity.
As threat intelligence matures, its focus is shifting from technical Ad hoc arrangements and under-resourced intelligence functions Indicators explain what already
indicators to business relevance. Executives now look to it to cannot deliver executive-grade insights, nor the outcomes they
happened; intent explains what’s coming
clarify which threats truly matter, how geopolitical and industry enable.
next. The most valuable intelligence
shifts alter exposure, and where fragility exists across operations,
Whether delivered through an internal team, trusted partners,
partners, and people. The question is no longer whether to invest in
connects behavior, context, and motive
or a hybrid model, the mandate is the same: Intelligence must
threat intelligence, but what kind of intelligence the organization is
be timely, contextual, and decision-relevant. Intelligence that — turning isolated signals into foresight
prioritizing and paying for.
only explains what happened yesterday does little to protect
that leaders can act on before damage
To frame budget conversations, consider where CTI provides your tomorrow. Providers who offer novel visibility, such as early
organization the greatest value: insight into adversary infrastructure, intent, and preparation, occurs.”
deliver a structural advantage.
• Validation that security investments are aligned to the
Menny Barzilay, Co-founder and CEO, Percepto
organization’s risk profile
• Reduction of operational noise by focusing defenses on the most
critical threats
• Proactive risk reduction, versus reactively responding to incidents
after they occur
Navigating the 2026 threat landscape
Several of the fault lines discussed in this chapter are reflected • The industrialization of attacks: The shift from manual
Get the 2026 Cloudflare
in the 2026 Cloudflare Threat Report. Based on data from hacks to automated, frictionless scaling across an
Threat Report.
Cloudflare’s global network, which protects 20% of the web, the organization’s own cloud infrastructure
report helps leaders focus on risks that require action, not just
• Identity-first intrusions: The transition of ransomware into a
awareness.
login event rather than a break-in Get the report
It uses a simple lens: attacker effort versus impact. The most
• Supply chain connectivity: The weaponization of the
important threats are those that create outsized business impact
connective tissue between SaaS and API-first environments
with minimal effort. In 2026, this appears in three patterns:
Cloudflare Security Signals Report | Autonomic Resilience 19

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 44.. SSiiggnnaallss ooff iinntteenntt 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Only
The missing ingredient: Threat modeling
While integrating threat intelligence into your security practice enables optimization across all aspects of 37%
your practice, tight integration with threat modeling takes it one step further into the realm of an enterprise
strategic driver.
While more organizations are factoring risk in decision-making and including risk reduction in their long- of organizations have successfully
term strategic goals, only 37% of organizations have successfully formalized and documented their threat
modeling processes.15 Threat modeling provides a common taxonomy that aligns the CISO, the C-suite, formalized and documented their
and the board around shared risk assumptions. It forces clarity on asset prioritization, the likelihood of
compromise, and the business impact if controls fail. threat modeling processes.16
The view achieved in threat modeling exercises is intentionally high-level; boards want clarity on systemic
risk, emerging threat trends, and whether the organization is positioned on the right side of the threat fault
line. Through threat modeling, inherent risks are measured by likelihood and severity of impact based on
the priorities of the organization. Factors such as security controls and audit results, in combination with
threat intelligence analysis, provide residual risk calculations.
Injecting CTI data into the threat modeling process enables further tuning, providing a basis for activities
such as controls validation and threat hunting, both essential elements in a proactive security posture.
Additionally, sector-relevant intelligence can confirm whether defenses are hardened against the most likely
adversaries, and give decision-makers strong indicators for budget and strategic planning.
Without threat modeling, intelligence stays operational. With it, intelligence becomes strategic.
Good intelligence reduces noise. Great intelligence changes
decisions. The difference is whether it helps leaders
anticipate moves, not just explain them.”
Troy Wilkinson, Venture Advisor, YL Ventures
Cloudflare Security Signals Report | Autonomic Resilience 2200

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 44..  SSiiggnnaallss  ooff  iinntteenntt 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
QUESTIONS FOR THE C-SUITE
Threat intelligence as a leadership discipline
Threat intelligence, when done well, connects security, risk, operations, finance, and strategy into a
coherent executive view of exposure and intent.
| Q1  | Q2  | Q3  | Q4  | Q5  |
| --- | --- | --- | --- | --- |
Are we protecting what  How early do we truly  Are threat briefings  Which business  How quickly can we
is familiar or what is most  see adversary intent? driving decisions or just  decisions or processes  recalibrate when
consequential? sharing information? would fail first if a  adversaries change
Where are we discovering  trusted individual were  playbooks?
Have we explicitly aligned  attacks through damage  Do these insights change  compromised?
rather than intelligence? Are
| our defenses to the threats  |     | priorities, investment, or risk  |     |     |
| ---------------------------- | --- | -------------------------------- | --- | --- |
What mechanisms are in
we leading the threat cycle,
| that could disrupt revenue,  |     | appetite in real time? |                   |                              |
| ---------------------------- | --- | ---------------------- | ----------------- | ---------------------------- |
|                              |     |                        | Have we designed  | place to tell us a shift is  |
or trailing it?
| operations, or trust this year? |     |     |     | coming before the business  |
| ------------------------------- | --- | --- | --- | --------------------------- |
workflows assuming
feels it?
human judgment can
be manipulated or
impersonated?
Cloudflare Security Signals Report | Autonomic Resilience 21

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 55.. TThhee ddeebbtt ttrraapp 6. Cloud mirage Conclusion About Cloudflare
5
The debt trap:
Legacy architecture
as strategic risk
Cloudflare Security Signals Report | Autonomic Resilience 22

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
The debt trap: When speed exposes structural weakness
Legacy architecture
The defining shift of 2026 is not the volume of vulnerabilities — it is the velocity at which they are exploited. Agentic AI has collapsed
the window between disclosure and exploitation even further, enabling adversaries to identify and operationalize exploits within days
as strategic risk
— and increasingly, within hours.
The data is stark. In 2025, 884 vulnerabilities were observed being actively exploited, and 29% showed evidence of exploitation on
the very day they were published.18 The scale is equally unprecedented. React2Shell, one of the year’s most notorious vulnerabilities,
In 2026, technical debt represents a material
recorded over 1 billion exploitation attempts in just 11 days.19
business risk that quietly erodes competitiveness.
Organizations were already stretched thin in
2025 managing more than 130 new vulnerabilities
Escalation without architectural readiness
every day, nearly 40% of which were rated high
or critical.17 As AI weaponization renders legacy World record DDoS attacks
architectures indefensible, organizations with
fragmented stacks risk being trapped in a cycle
of reactive security, constrained innovation, and
40
compounding exposure.
Technical debt has become an exposed attack
31.4
surface, one that compounds risk faster than 29.4 29.7
30
human teams can respond. Those who modernize
25.8
decisively will not only reduce risk, they will unlock
22.2
the speed, confidence, and adaptability required
to compete in the AI-driven economy. 19.7
20 17.0 17.8
15.1
12.5
11.5 11.9 12.0
10.7
9.9
7.7 8.4
10 6.5 7.3
5.6
4.2
3.8
0
9/24 10/24 10/24 4/25 5/25 8/25 8/25 8/25 9/25
Month and year
In just over a year, the largest recorded DDoS attack increased nearly tenfold. Centralized, tightly coupled systems were never
designed for this scale. Technical debt now translates directly into systemic fragility under machine-speed pressure.
Cloudflare Security Signals Report | Autonomic Resilience 23
)spbT(
dnoces
rep
stibareT
5. The debt trap
8/25 8/25 9/25 9/25 9/25 9/25 9/25 9/25 9/25 9/25 10/25 10/25 11/25
Source: Cloudflare Radar

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 55.. TThhee ddeebbtt ttrraapp 6. Cloud mirage Conclusion About Cloudflare
Legacy environments are cracking under pressure. Major failures often The average global enterprise wastes more than $370 million per year
$370
occur when shared dependencies break at the same time. Years of due to their inability to efficiently modernize outdated, inefficient legacy
quick fixes have created dark debt: hidden integrations, brittle APIs, systems and applications.20 Studies estimate that roughly 31% of the tech million
and systems too risky to patch. These environments were not built for resources are dedicated to resolving tech debt.21 True innovation — new
machine-speed threats or continuous verification. products, AI initiatives, automation — receives as little as 7%. This is not
stagnation; it is regression. wasted per year due to
This also exposes the limits of 30-, 60-, and 90-day patch cycles.
inability to efficiently
Threats are exploited in hours, not quarters. Protection must move While leaders use AI to accelerate differentiation, laggards are paying an
outward to the edge, reducing exposure before vulnerable systems are escalating “interest rate” on old code that limits speed, resilience, and modernize outdated,
even touched. strategic optionality.
inefficient legacy systems
and applications23
Why legacy stacks fail under AI pressure
Modern security assumes automation, integration, and real-time control.
Legacy systems assume manual intervention, static configurations, and
Attackers don’t distinguish between old
perimeter-based protection. That mismatch is becoming dangerous as AI
and new systems; they look for weak links. changes the economics of both attack and defense.
Tech debt quietly increases the number
Outdated architectures struggle with slow, downtime-heavy patching,
of those links until defense becomes a limited visibility across APIs and data flows, fragmented tools that cannot
coordinate response, and weak foundations for AI-driven operations. This
probability game.”
often forces a trade-off between cyber risk and operational risk, a familiar
tension between CTOs and CISOs when patching could disrupt the
Jerry Perullo, Founder, Adversarial Risk
business. The result is delay, and delay is exactly what machine-speed
Management
threats exploit.
Organizations are delaying AI adoption not because they lack ambition,
but because their infrastructure cannot safely support it. Meanwhile,
competitors with modernized architectures allow AI initiatives to pull
modernization forward — using real workloads to justify and accelerate
architectural renewal. For instance, 62% of organizations leading in
The innovation scarcity cycle
application innovation find it “very easy” to track their current level of
security compliance, compared to 35% of those behind schedule.22
Organizations with aging stacks are trapped in an innovation scarcity
cycle. As infrastructure becomes more fragile, security incidents increase.
As incidents increase, more budget and talent are diverted to maintenance.
The result is a shrinking pool of capacity for growth.
Cloudflare Security Signals Report | Autonomic Resilience 24

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 55.. TThhee ddeebbtt ttrraapp 6. Cloud mirage Conclusion About Cloudflare
The leadership divide
73%
The difference between leaders and laggards is decision discipline. Organizations who escape
the debt trap make hard choices early. They centralize modernization authority, align security
with business resilience, and treat architecture as a strategic asset. Seventy-three percent of
of modernization “leaders” have centralized
modernization “leaders” have centralized decision-making with only a few people, compared to
just 36% of “laggards.”24 Those who fail remain trapped in committee-driven paralysis, where decision-making with only a few people,
vulnerabilities move faster than decisions and risk compounds while plans are endlessly debated. compared to just 36% of “laggards.”25
Technical debt often mirrors organizational debt. Fragmented ownership, unclear accountability,
and deferred decisions create the same brittleness in leadership and operating models that exists
in legacy infrastructure. In 2026, that fragility is no longer survivable.
Modernization as risk reduction: Buying back time
Escaping the debt trap requires viewing modernization as a resilience mandate, rather than an IT
upgrade cycle. Modernization reduces risk by shrinking the attack surface through consolidation,
enabling automated patching and response, and making AI-driven defense and operations viable at
scale. Just as importantly, it reallocates scarce engineering capacity to high-value work instead of
endless maintenance.
The organizations who succeed do not modernize by rebuilding everything; they create a stable,
unified foundation where security, performance, and innovation reinforce one another. With that
foundation in place, systems can be refined, scaled, and adapted quickly — without accumulating
new layers of fragility.
The shift required is not incremental. It demands executive alignment and decisive action. Legacy
architecture must be treated as a quantified business risk, not a technical inconvenience. Decision
authority for modernization must be centralized. AI initiatives enable architectural renewal rather
than waiting for perfect conditions. Platforms must be consolidated to reduce complexity and
restore visibility.
Ultimately, modernization is about reclaiming time: time to innovate, time to respond, and time to
compete before compounding risk erodes advantage.
Cloudflare Security Signals Report | Autonomic Resilience 2255

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 55.. TThhee ddeebbtt ttrraapp 6. Cloud mirage Conclusion About Cloudflare
QUESTIONS FOR THE C-SUITE
The compounding cost of legacy
Technical debt drains speed and resilience. Many firms spend more maintaining the past
than building the future.
Q1 Q2 Q3 Q4 Q5
Which business What share of security Which priority What are the top three What are the biggest
capabilities are spend maintains legacy initiatives are delayed initiatives to reduce obstacles to reducing
constrained by versus builds resilience? by architecture limits? technical debt this year? technical debt?
technical debt today?
What is our target mix over the What revenue, efficiency, or How will we measure progress Are they budget limits, talent
next 12–24 months? risk gains are we deferring as and hold leaders accountable? gaps, competing priorities, or
Who owns fixing them, and
a result? unclear ownership? Which will
what is the timeline to reduce
we remove first?
that risk?
Cloudflare Security Signals Report | Autonomic Resilience 26

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 66.. CClloouudd mmiirraaggee Conclusion About Cloudflare
6
Cloud mirage:
Decoupling cascading risk
Cloudflare Security Signals Report | Autonomic Resilience 27

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Cloud mirage: When speed quietly becomes fragility
Decoupling
The modern enterprise did not intend to build fragile systems. Cloud adoption
promised speed, elasticity, and reliability, but it also introduced a quieter
The cloud creates scale — but not
cascading risk
concentration risk — less visible, more systemic, and harder to unwind under stress.
automatically resilience. If your
Today’s outages do not come only from single-provider failures. A single provider
systems fail together, you haven’t
incident can still be the trigger, but the most disruptive events occur when shared
As enterprises consolidate onto fewer cloud
dependencies fail in tandem — identity systems, control planes, deployment engineered redundancy. You’ve
platforms to move faster, many are quietly
pipelines, and network services that underpin everything else. Uptime Institute’s
increasing systemic risk. Mono-cloud strategies engineered correlation.”
simplify operations but concentrate failure
multi-year data shows that roughly two-thirds of publicly reported outages involve
third-party IT or data center providers — including cloud and Internet giants,
domains, while multicloud is often treated as a Mark Hughes, Global Managing Partner
telecommunications, and colocation companies.26
checkbox rather than an engineered resilience for Cybersecurity Services, IBM
strategy.
Business continuity is still too often recovery-centric, focused on restoring service
rather than containing failure. Over time, layered dependencies turn environments
Recent outages have made one truth
into tightly coupled systems where small faults can cascade. This fragility usually
unavoidable: Resilience is not determined by
becomes visible only in a crisis.
how many clouds an organization uses, but
by how its architecture fails. In 2026, leaders The upside is clear. Organizations that design and test for
must move beyond cloud ideology and adopt Permanent pressure failure see materially better outcomes. One large financial
resilience-by-design — architectures built services firm reduced outages by 40% and cut resolution
DDoS attacks by year and type
to contain failure, limit the blast radius, and times by nearly 60% after modernizing architecture, improving
preserve trust under pressure. observability, and engineering for failure readiness.27
HTTP DDoS attacks Network-layer DDoS attacks
50M 47.1M Total Outages today are less about the cloud breaking and more
about independence eroding. The real risk is architectural
12.7M
40M coupling. Resilience now requires intentional isolation, blast
radius limits, and treating failure containment as a core design
30M 34.4M principle.
21.3M Total
20M
13.9M Total 9.9M
10M 5.2M The mono-cloud illusion: Efficiency
11.4M
8.7M
without containment
0M
2023 2024 2025
Year For many organizations, mono-cloud strategies have become
the default in pursuit of efficiency. Standardized tooling reduces
complexity, speeds deployment, and lowers operating cost.
The trade-off is concentration risk. The same consolidation that
DDoS activity has more than tripled in two years. Disruption at scale is no longer
drives efficiency can also centralize failure.
episodic, it is continuous. In tightly coupled environments, sustained external
pressure exposes hidden dependencies and amplifies small faults into systemic
events. Resilience must assume constant stress, not rare failure.
Cloudflare Security Signals Report | Autonomic Resilience 28
)noilliM(
skcatta
SoDD
6. Cloud mirage
Source: Cloudflare Radar

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 66.. CClloouudd mmiirraaggee Conclusion About Cloudflare
Major cloud providers are often highly resilient, but the larger risk today is architectural and The multicloud myth: Redundancy without independence
operational. When identity, policy enforcement, observability, and delivery pipelines all rely
on the same control plane or trust boundary, resilience becomes an assumption rather than
Multicloud is often positioned as the antidote to concentration risk. In practice, it frequently recreates the
a built-in property. A single mistake, whether provider-side or customer-side, can propagate
same fragility — just across logos. Most multicloud environments share identity providers, CI/CD pipelines,
widely if the design does not contain it. Recovery plans may exist, but true containment often
governance tooling, and SaaS dependencies. When those shared layers fail, the promise of independence
does not. When something breaks, too much breaks together.
evaporates instantly. This is why post-incident reviews so often reveal that “redundant” systems were never
Industry data reinforces this reality. Gartner research shows most cloud failures stem truly independent.
from misconfiguration and operational issues rather than core infrastructure defects.
Resilience is not about how many clouds exist on a diagram. It is about which layers fail independently under
Analyses based on Gartner surveys attribute roughly 80% of cloud security failures
pressure — and which do not.
to misconfiguration, and projections suggested that by last year, up to 99% of cloud
environment failures would involve human error somewhere in the chain.28 The lesson is not
that humans err — they always will — but that architectures must be designed to absorb
those errors safely. Engineering for containment, not perfection
The practical implication is clear. Resilience must be engineered, not assumed. That means
Autonomous design starts with the expectation that systems will fail and focuses on keeping failures
designing for containment as much as recovery, separating critical dependencies, adding
bounded and useful while learning. The aim is not only to withstand shocks, but to improve because of them.
guardrails and policy-as-code to reduce error impact, and regularly testing failure scenarios.
Concentration risk has not disappeared in the cloud era. It has moved up the stack. The
Containment is what makes that possible. It means a failure in one area does not automatically spread to
organizations that remain resilient are those that ensure a single fault does not become a
others. An isolated failure is limited in scope, clear in cause, and manageable in impact. It does not take
systemic event.
identity, policy, data, and operations down together.
Organizations using AI and automation extensively
shortened breach lifecycles by 80 days and reduced
average breach costs by
$1.9
million29
CClloouuddffllaarree SSeeccuurriittyy SSiiggnnaallss RReeppoorrtt || AAuuttoonnoommiicc RReessiilliieennccee 222999

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 66.. CClloouudd mmiirraaggee Conclusion About Cloudflare
This shows up in architecture through independence across identity, policy, and execution layers,
separation of control planes, and default-safe behavior under uncertainty. Outages are inevitable.
The priority is to keep them local, explainable, and survivable, and to use them to strengthen the
system. Leading organizations are not those with zero incidents, but those that successfully limit
the blast radius of any single event. Attackers look for one weakness to trigger a
cascade. If a single compromise becomes an
enterprise event, that’s not bad luck.
Containment as a growth advantage
That’s architectural design.”
While often seen as insurance, decoupling layers supports speed and growth. IBM’s Cost of a Data
Breach Report 2025 found that organizations using AI and automation extensively shortened breach Dave Trader, Chief Information Security Officer,
lifecycles by 80 days and reduced average breach costs by $1.9 million.30
HALO Branded Solutions
By restricting the scope of impact, leaders preserve the trust of customers, regulators, and
investors — and maintain the agility required for more confident AI adoption, faster market entry,
and fewer executive escalations. When failure is contained, leaders keep decision capacity.
Containment is not defensive. It enables faster movement and smarter risk-taking in a volatile
environment.
Designing for failure at the top
As digital systems underpin the business strategy, the decision to separate or couple infrastructure
becomes a high-stakes business decision.
Executives must shift from how fast we can recover to what must never fail together. That requires
clarity on shared control planes, identity dependencies, and pipelines, plus evidence of failure-
mode testing, not just uptime. Containment belongs at the board level because systemic failure is a
business risk; it cannot be delegated. It must be designed deliberately from the top so that no single
failure becomes a company-wide event and every incident makes the system stronger.
Cloudflare Security Signals Report | Autonomic Resilience 3300

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 66.. CClloouudd mmiirraaggee Conclusion About Cloudflare
QUESTIONS FOR THE C-SUITE
When a shared service fails, does architecture contain it?
Debated together, these questions reveal whether the enterprise can contain disruption in real time, or whether
stability is still dependent on hope, heroics, and post-incident recovery.
Q1 Q2 Q3 Q4 Q5
Which critical systems If identity or a core Is multicloud reducing Are we measuring Could we explain our
can fail without stopping platform failed, what risk or just adding containment or only last outage to the
the business? revenue would stop? complexity and cost? recovery time? board or regulators?
Have we proven this through Do we know the impact Where have we reduced Do our KPIs reward prevention Was the impact limited
tests, or is it theoretical? in advance, or only after dependency, and where or reactive cleanup? by design or fortunate
disruption? does it remain? circumstance?
Cloudflare Security Signals Report | Autonomic Resilience 31

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage CCoonncclluussiioonn About Cloudflare
CONCLUSION
The leadership principles for enduring advantage The organizations that lead
will be those whose executives
embed these principles into
In a world shaped by AI-driven decisions, • Execution embedded in systems over stated intent.
autonomous systems, and deeply interdependent Decisions only matter if they execute at machine everyday decisions — turning
speed. Control over models, data, prompts, and
digital ecosystems, resilience is no longer
autonomous actions must live where execution volatility into learning,
sufficient. The advantage will come from systems’
happens. Anything reliant on documentation,
capacity to detect stress, adapt in real time, pressure into progress, and
alignment, or manual process will not scale.
contain failure, and continue operating without
• Structural independence over short-term uncertainty into advantage.
waiting for human intervention. This is what we
convenience. What feels efficient in calm conditions
call autonomic resilience. often creates fragility under stress. Autonomically
resilient teams prioritize containment, reversibility, and
This report is not a threat inventory. It defines a
separation. Systems are designed so failures remain
leadership mandate: identifying and addressing the fault
local, observable, and correctable. The ability to
lines embedded in modern enterprises. These structural
prevent cascades becomes a strategic advantage.
weaknesses may appear manageable in steady-
state conditions, but they will reliably surface under • Provable trust over assumed control. Trust must be
continuously provable, not implicitly assumed. Leaders
pressure without decisive action. They run beneath
demand visibility into system behavior, enforceable
AI adoption, cloud dependence, legacy architecture,
controls across human and machine identities, and
threat intelligence, and operating models built for a more
proof of integrity at machine speed. Assumed trust
predictable era.
fails under autonomy.
Confronting these fault lines is not the remit of the CISO
• Learning from failure over avoidance of failure.
alone. Autonomic resilience is a C-suite responsibility,
Failure is expected and deliberately used as
shaped by how executive teams set priorities, allocate
input. Early detection, limited blast radius, rapid
authority, and design systems that regulate themselves.
recovery, and institutional learning define leadership
Autonomic organizations distinguish themselves by the
performance. Recovery speed — not prevention — is
principles their leadership teams consistently embody:
the metric that matters.
• Shared ownership of systemic risk over delegated
In 2026, leadership is defined less by planning for
accountability. Systemic risk is owned by the
stability and more by designing for disruption.
leadership team, not delegated down the org chart.
Accountability is explicit, ownership is shared across The organizations that lead will be those whose
the C-suite, and boards engage through real scenarios executives embed these principles into everyday
and trade-offs — not static reporting. decisions — turning volatility into learning, pressure into
progress, and uncertainty into advantage.
Cloudflare Security Signals Report | Autonomic Resilience 3322

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion AAbboouutt CClloouuddffllaarree
About Cloudflare
Cloudflare Security Signals Report | Autonomic Resilience 3333

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion AAbboouutt CClloouuddffllaarree
ABOUT CLOUDFLARE
One platform. One programmable network.
330+ cities ~50 ms ~13,000 networks 477 Tbps
in 125+ countries, including from ~95% of the world’s directly connect to Cloudflare, of network capacity
mainland China Internet-connected including ISPs, cloud providers, and growing
population and large enterprises
with 210+ cities
running GPUs for AI
inference worldwide
Cloudflare Security Signals Report | Autonomic Resilience 34

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion AAbboouutt CClloouuddffllaarree
ABOUT CLOUDFLARE
Cloudflare’s
security suite
Resilience and edge defense
• Web app and API protection: Block attacks, catch
vulnerabilities, and improve availability
• Security service edge (SSE): Enforce zero trust security
across hybrid workforces
• DDoS mitigation: Weather the biggest, most advanced
attacks with 477 Tbps of network capacity
Secure cloud and network integration
• Secure access service edge (SASE): Connect and protect
your workforce, AI agents, and infrastructure
• Network as a service and multicloud: Connect, secure, and
accelerate their corporate networks without the cost and
complexity of legacy hardware
• Network interconnect: Directly connect your on-premises
and cloud networks to Cloudflare’s network
Cloudflare Security Signals Report | Autonomic Resilience 35

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion AAbboouutt CClloouuddffllaarree
ABOUT CLOUDFLARE
Cloudflare One services
Cloudflare One: The agile SASE platform
Human users Applications
Zero trust Network as
and Al agents and Al tools
security a service
Manage
Al security
and compose
Devices Infrastructure
Integrate
Al-powered
and program
platform
Locations Networks
Cloudflare Security Signals Report | Autonomic Resilience 36

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion AAbboouutt CClloouuddffllaarree
ABOUT CLOUDFLARE
Protect GenAI use and govern AI agents
Security service edge (SSE) MCP server portals
Public Al
Visibility
apps
Visibility
Access controls
Authentication
Prompt guardrails
Connections
Data security
Your workforce
Corporate
resources
Al security posture AI agent
Unified management
(MCP servers)
management
Private Al
apps
Cloudflare Security Signals Report | Autonomic Resilience 37

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion AAbboouutt CClloouuddffllaarree
ABOUT CLOUDFLARE
Cloudflare AI services across the full lifecycle
Protect AI adoption
with AI Security Suite
Build AI Protect content
with Developer Platform with app services
Secure workforce Govern AI agents
Build AI on every region on
use of GenAI
Cloudflare’s ZTNA
earth, with one click
SASE platform including MCP
Workers AI, Vectorize, (Cloudflare One) Server Portals Protect original content
AI Gateway online from AI crawlers
Bot Management including
Build AI infrastructure,
Protect AI- AI Crawl Control
on easy mode
powered apps
Build AI securely
Remote MCP Server, Agents
AI Gateway App Security
SDK, AI Search, AI Gateway
including Firewall
for AI
AI-powered platform on one global network
Threat detection models · AI agent (Cloudy) · Data loss prevention models
Cloudflare Security Signals Report | Autonomic Resilience 38

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion AAbboouutt CClloouuddffllaarree
ABOUT CLOUDFLARE
Insights for the
modern CxO
Navigating today’s threat landscape and rapid
technological shifts requires more than operational
knowledge — it demands strategic foresight.
“The Executive Lens” by Cloudflare is a dedicated
resource hub curated specifically for C-suite leaders.
Learn expert-driven insights, actionable frameworks,
and exclusive research on critical enterprise topics like
cyber resilience, secure AI governance, and global digital
transformation.
Explore The Executive
Read more
Lens today.
Cloudflare Security Signals Report | Autonomic Resilience 39

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion AAbboouutt  CClloouuddffllaarree
Additional resources
| Forrester Total  | Security Signal | 2026 Cloudflare  | theNET |
| ---------------- | --------------- | ---------------- | ------ |
| Economic Impact  |                 | Threat Report    |        |
Meet sophisticated threats and prevent  Uncover the signal from the noise  Understand the 2026 threat   Insights across cybersecurity
emerging ones. See how Cloudflare  and focus on today’s most important  landscape defined by a new Measure   innovation, the threat landscape,
helps enterprises use security as a  cybersecurity trends. Each episode of  of Effectiveness (MOE). The report   and the future of the Internet with
competitive advantage, weathering a  Security Signal translates cybersecurity  details new risks from state-sponsored  executive perspectives on how to
complex threat landscape with greater  complexities into actionable intelligence  pre-positioning, token theft, hyper- solve organizational challenges
efficiency and predictability. for executives at the helm.  volumetric DDoS, and more. with technology.
| Read more | Watch now | Read more | Read more |
| --------- | --------- | --------- | --------- |
Insights for the digital enterprise
Cloudflare Security Signals Report | Autonomic Resilience 40

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion AAbboouutt CClloouuddffllaarree
Contacts
Global Americas EMEA Asia Pacific Japan
Market
Leadership
Mark Anderson Rick Congdon Tony Van den Berge Goran Risticevic Sayoko Matsumoto
President of Revenue Geo Vice President, Americas Geo Vice President, EMEA Geo Vice President, APAC Geo Vice President, Japan
markanderson@cloudflare.com congdon@cloudflare.com tonyberg@cloudflare.com goran@cloudflare.com sayoko@cloudflare.com
Field CXO
Team
Ramy Houssaini Khalid Kark Christian Reilly Volker Rath Koichiro Otobe
Chief Cyber Solutions Officer Field CIO, Americas Field CIO, EMEA Field CISO Field CTO, Japan
ramy@cloudflare.com khalid@cloudflare.com creilly@cloudflare.com volker@cloudflare.com koichiro@cloudflare.com
Cloudflare Security Signals Report | Autonomic Resilience 41

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
2026
Cloudflare Security
Signals Report
Autonomic Resilience
This document is for informational purposes only and is the property of Cloudflare. This document
does not create any commitments or assurances from Cloudflare or its affiliates to you. You are
responsible for making your own independent assessment of the information in this document.
The information in this document is subject to change and does not purport to be all inclusive or
to contain all the information that you may need. The responsibilities and liabilities of Cloudflare to
its customers are controlled by separate agreements, and this document is not part of, nor does it
modify, any agreement between Cloudflare and its customers. Cloudflare services are provided “as
is” without warranties, representations, or conditions of any kind, whether express or implied.
© 2026 Cloudflare, Inc. All rights reserved. CLOUDFLARE® and the Cloudflare logo are trademarks
of Cloudflare. All other company and product names and logos may be trademarks of the respective
companies with which they are associated.
1C 8lo8u8d 9f9la FrLeA SReEc |u ernittye rSpirgisnea@lsc lRoeupdfolarrte |. cAoumto |n Colomuidcf lRaeres.icloiemnce REV:BDES-8897.2026MA4R129

Executive summary 1. Taming the algorithm 2. Trust at machine speed 3. Shadow supply chains 4. Signals of intent 5. The debt trap 6. Cloud mirage Conclusion About Cloudflare
Endnotes
1. Jonathan Villa, “Hidden Risks of Shadow AI,” Varonis, www.varonis.com/blog/shadow-ai. 16. SANS Institute.
Accessed 11 Feb. 2026.
17. Mohammed Khalil, “Vulnerabilities Statistics 2025: Record CVEs, Zero-Days & Exploits,”DeepStrike,
2. IBM, “Cost of a Data Breach Report 2025,” www.ibm.com/reports/data-breach. Accessed 11 Feb. 8 Oct. 2025, deepstrike.io/blog/vulnerability-statistics-2025. Accessed 25 Feb. 2026.
2026.
18. VulnCheck, “VulnCheck State of Exploitation 2026,” 21 Jan. 2026, www.vulncheck.com/blog/state-
3. MultiState, “Artificial Intelligence (AI) Legislation,” www.multistate.ai/artificial-intelligence-ai- of-exploitation-2026. Accessed 11 Feb. 2026.
legislation. Accessed 11 Feb. 2026.
19. Cloudflare Global Network Data.
4. Gartner, “Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by
20. Pegasystems, “Average Global Enterprise Wastes More Than $370 Million Every Year Through
2026, Up From Less Than 5% in 2025,” 26 Aug. 2025, www.gartner.com/en/newsroom/press-
Technical Debt, Says Research,” 14 Oct. 2025, www.pega.com/about/news/press-releases/
releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-
average-global-enterprise-wastes-more-370-million-every-year-through. Accessed 11 Feb. 2026.
ai-agents-by-2026-up-from-less-than-5-percent-in-2025. Accessed 11 Feb. 2026.
21. Protiviti, “Global Technology Executive Survey: Tech Debt a Major Burden,” www.protiviti.com/us-
5. Cloudflare Radar, “Bot Traffic,” radar.cloudflare.com/bots?dateRange=12w. Accessed 11 Feb. 2026.
en/global-technology-executive-survey-tech-debt-major-burden. Accessed 11 Feb. 2026.
6. Cloudflare Radar, “Application Layer Security,” radar.cloudflare.com/security/application-
22. Cloudflare, “2026 Cloudflare App Innovation Report.”
layer?dateRange=12w. Accessed 11 Feb. 2026.
23. Pegasystems, “Average Global Enterprise Wastes More Than $370 Million Every Year Through
7. IBM, “Cost of a Data Breach Report 2025.”
Technical Debt, Says Research.”
8. Lareina Yee, et al., “The AI Reckoning: How Boards Can Evolve,” McKinsey & Company, 24 Oct.
24. Cloudflare, “2026 Cloudflare App Innovation Report.”
2024, www.mckinsey.com/capabilities/mckinsey-technology/our-insights/the-ai-reckoning-how-
25. Cloudflare, “2026 Cloudflare App Innovation Report.”
boards-can-evolve. Accessed 11 Feb. 2026.
26. Uptime Institute, “Uptime Annual Outage Analysis Report 2025,” 6 May 2025, uptimeinstitute.com/
9. IBM, “Cost of a Data Breach Report 2025.”
about-ui/press-releases/uptime-announces-annual-outage-analysis-report-2025. Accessed 11
10. ENISA, “SBOM Analysis - Towards an Implementation Guide.” Dec. 2025, www.enisa.europa.eu/
Feb. 2026.
sites/default/files/2025-12/SBOM%20Analysis%20-%20Towards%20an%20Implementation%20
27. Nuno De la Torre, et al., “IT Resilience for the Digital Age,” McKinsey & Company, 20 June 2023,
Guide_v1.20-Published.pdf. Accessed 11 Feb. 2026.
www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/it-resilience-for-the-
11. Verizon, “2025 Data Breach Investigations Report (DBIR),” www.verizon.com/business/resources/
digital-age. Accessed 11 Feb. 2026.
reports/dbir. Accessed 11 Feb. 2026.
28. Ashwin Chaudhary, “Managing Cloud Misconfigurations Risks,” Cloud Security Alliance, 14 August
12. Cloudflare, “2026 Cloudflare App Innovation Report,” 2026, www.cloudflare.com/resource/g/app-
2023, cloudsecurityalliance.org/blog/2023/08/14/managing-cloud-misconfigurations-risks.
innovation-report/2026. Accessed 11 Feb. 2026.
Accessed 11 Feb. 2026.
13. CrowdStrike, “2025 Global Threat Report,” www.securityweek.com/wp-content/uploads/2025/02/
29. IBM, “Cost of a Data Breach Report 2025.”
CrowdStrikeGlobalThreatReport2025.pdf. Accessed 18 March 2026.
30. IBM, “Cost of a Data Breach Report 2025.”
14. SANS Institute, “SANS 2025 CTI Survey: Cyber Threat Intelligence Survey,” SOCRadar, May 2025,
socradar.io/wp-content/uploads/2025/05/SANS-2025-CTI-Cyber_Threat_Intelligence_Survey-
SOCRadar.pdf. Accessed 11 Feb. 2026.
15. SANS Institute.
Cloudflare Security Signals Report | Autonomic Resilience 43

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-24", "model": "gemini-3.5-flash-lite"} -->
