OrcaRouter
| O R CA | R O U T E R |   S E C U R | I T Y   R E | S E A R C H |
| ------ | ----------- | ----------- | ----------- | ----------- |
The AI Threat Report
2026
How enterprises are attacked through their AI systems — and the control
stack that stops it
| OrcaRouter Security Research |     | ·   | June 2026 |     |
| ---------------------------- | --- | --- | --------- | --- |

ABOUT THIS REPORT
The AI Threat Report is the annual flagship study of OrcaRouter Security
Research, the security research team behind the OrcaRouter AI gateway. The
2026 edition maps how enterprises are attacked through their AI systems —
drawing on the public incident record, analyst and government data, and the
threat patterns documented in OrcaRouter's security research — and sets out
the control architecture that contains them.
All statistics are drawn from named public sources, cited as endnotes. Exhibits
labeled illustrative encode analytical judgment rather than measured data; the
Methodology section explains how to read each. Nothing in this report is
derived from OrcaRouter customer data.
SUGGESTED CITATION
Suggested citation: OrcaRouter Security Research, “The AI Threat Report 2026,”
Continuum AI Corp, June 2026.
© 2026 Continuum AI Corp · www.orcarouter.ai · research@orcarouter.ai
The AI Threat Report 2026 OrcaRouter Security Research · 2

## Table of Contents
- [The state of AI security in 2026](#1-the-state-of-ai-security-in-2026)
- [A taxonomy of AI threats](#2-a-taxonomy-of-ai-threats)
- [Anatomy of the modern AI attack](#3-anatomy-of-the-modern-ai-attack)
- [The agentic inflection point](#4-the-agentic-inflection-point)
- [The defense blueprint: zero trust for AI](#5-the-defense-blueprint-zero-trust-for-ai)
- [The CISO agenda for 2026](#6-the-ciso-agenda-for-2026)

CONTENTS
In this report
1 The state of AI security in 2026 THE LANDSCAPE 6
2 A taxonomy of AI threats THE THREATS 10
3 Anatomy of the modern AI attack THE ATTACKS 15
4 The agentic inflection point THE INFLECTION 20
5 The defense blueprint: zero trust for AI THE DEFENSE 22
6 The CISO agenda for 2026 THE AGENDA 26
At a glance 4
Executive summary 5
Methodology & reading guide 29
Appendix A — the fourteen threat classes 30
Glossary 31
Endnotes 32
About OrcaRouter Security Research 34
Exhibits
E1 Three years, three eras — from leaked text to autonomous E7 Nine plausible steps, one breach — per-call review passes every
operations link in the chain
E2 Adoption has outrun readiness — and the outcome is showing up E8 The chatbot had two trust surfaces; the agent has twelve and
in breach data counting
E3 Fourteen threat classes, four families — organized by where the E9 The rug-pull, governed and ungoverned — the same Day-31
attack lives manifest change, two different endings
E4 Severity and prevalence are inversely correlated — the rarest E10 Six layers between a request and a regret — each one
attacks are the ones that end up in board reports independent, each one auditable
E5 Anatomy of an indirect injection — the payload crosses the trust E11 No rule touches live traffic until it has proven itself against your
boundary inside ordinary content real workload
E6 Five stages, five interception points — the chain is also the E12 Four quarters from inventory to evidence — overlapping by
defense map design
E13 Six numbers that tell the board the whole story
The AI Threat Report 2026 OrcaRouter Security Research · 3

AT A GLANCE
The year in eight numbers
Eight numbers that define the AI security year — drawn from the public record and the
research compiled in this report.
88% 3%
of organizations now use AI in at least one business of organizations breached through AI had proper AI
function — adoption is no longer the frontier 1 access controls in place; the other 97% did not 2
32% 42 sec
of security leaders saw prompt-based attacks on their AI average time for a successful attack on a production LLM
applications in the past twelve months 3 application, start to finish 4
62% +$670K
of organizations experienced a deepfake attack in the past the additional breach cost when “shadow AI” is involved —
year 3 $4.63M vs. a $4.44M global average 5
$893M Aug 2
in losses across 22,364 AI-related complaints in the FBI's 2026 — the EU AI Act becomes fully applicable; AI
first-ever AI crime accounting 6 governance moves from posture to legal obligation 7
The AI Threat Report 2026 OrcaRouter Security Research · 4

EXECUTIVE SUMMARY
Five findings for 2026
In 2025, enterprise AI crossed a line: systems that drafted text became systems that
take actions. The threat landscape crossed the same line, on the same schedule —
and in most organizations, the controls did not. This report maps how enterprises
are actually attacked through their AI systems, and lays out the control architecture
that contains it.
01 Adoption outran governance — and attackers noticed first.
Eighty-eight percent of organizations now run AI in at least one business function1, but only 37% assess the
security of AI tools before deploying them8. The result is measurable: 13% of organizations have already
had an AI model or application breached, and 97% of those lacked basic AI access controls2. Ungoverned
“shadow AI” now adds an average $670,000 premium to breach costs5.
02 The attack surface moved into the model's context window.
The defining vulnerability of the era is prompt injection — ranked LLM01 in the OWASP Top 10 for LLM
Applications9. It is not a bug that will be patched; it is a structural property of models that cannot reliably
separate instructions from data. Every document, web page, email, and tool result an AI system reads is
now part of your attack surface. The objective is containment, not elimination.
03 2025 was the year attacks became agentic.
Zero-click exfiltration through enterprise copilots (EchoLeak10), cross-repository data theft through agent
tooling (GitHub MCP11), service-side leaks in autonomous research agents (ShadowLeak12), and the first
reported AI-orchestrated espionage campaign13 moved AI risk from embarrassing text to real-world
actions: data exfiltrated, credentials abused, infrastructure manipulated — increasingly with no human in
the loop.
04 The economics now favor the attacker.
Successful attacks on production LLM applications take 42 seconds on average4; 90% of them leak
sensitive data4. Deepfake attempts occur at industrial frequency14 and 62% of organizations have already
faced one3. Meanwhile, agents introduce a loss class that needs no breach at all: denial-of-wallet, where a
hijacked or runaway agent simply spends. Defense must be cheap, automatic, and in the request path to
compete.
05 The defense that works is architectural.
Organizations that contain AI threats do four things: give every agent a scoped, expiring identity; screen
content on the way in and out; police actions — tool calls, network egress, spend — at a policy gateway;
and write every decision to an audit trail they can hand to a regulator. This is zero trust applied to AI, it
maps cleanly onto OWASP, NIST AI RMF, ISO/IEC 42001, and the EU AI Act7, and it can be deployed at the
gateway without rewriting a line of agent code.
The AI Threat Report 2026 OrcaRouter Security Research · 5

THE LANDSCAPE

## 1. The state of AI security in 2026
Enterprise AI went from pilot to production in eighteen months. Its security model did
not. The gap between what organizations deploy and what they control is now the
most reliably exploited seam in the enterprise.

### 1.1 Adoption outran governance
The adoption race is over: 88% of organizations report using AI in at least one business function, up from 78% a year
earlier — and 62% are already experimenting with AI agents, with another 23% scaling them1. Organizational AI use
jumped from 55% in 2023 to 78% in 202415 and has kept climbing. AI is no longer a pilot program; it is infrastructure.
Governance has not kept pace, and the gap is quantifiable. Two-thirds of organizations expect AI to be the most
significant cybersecurity factor of the coming year — yet only 37% have a process to assess the security of an AI tool
before it is deployed8. Among organizations that suffered a breach, 63% either have no AI governance policy or are
still writing one; of those that do have a policy, only 34% audit for unsanctioned AI use5.

EXHIBIT 2 Adoption has outrun readiness — and the outcome is showing up in breach data
Source: McKinsey, The State of AI in 2025; World Economic Forum, Global Cybersecurity Outlook 2025; IBM, Cost of a Data Breach Report 2025
The consequences stopped being hypothetical in 2025. Thirteen percent of organizations reported breaches of AI
models or applications — and of those, 97% lacked proper AI access controls2. Sixty percent of these AI incidents
ended in compromised data; 31% disrupted operations2. One in five organizations traced a breach to shadow AI —
tools employees adopted without security's knowledge — and those breaches ran $670,000 above the global average
cost, $4.63 million against $4.44 million5.
Read those numbers together and the diagnosis is uncomfortable but clear: enterprises did not deploy AI insecurely
because the controls failed. They deployed it before the controls existed.
The AI Threat Report 2026 OrcaRouter Security Research · 6

### 1.2 Three years from curiosity to kill chain
The public incident record tells the story of the threat's maturation in three acts. 2023 was the text era: the harms
were leaks and embarrassments — source code pasted into chatbots16, a caching bug exposing other users'
conversations17 — and the seminal research on indirect prompt injection18 read as a warning about a future problem.
2024 was the liability era: a tribunal held an airline responsible for its chatbot's invented refund policy19, a deepfaked
video call extracted US$25.6 million from a single engineering firm20, and researchers demonstrated the first self-
replicating worm targeting AI-powered applications21.
2025 was the agentic era. The incidents that defined the year shared a signature: no human clicked anything. A
crafted email exfiltrated data from Microsoft 365 Copilot with zero user interaction (EchoLeak, CVE-2025-32711)10. A
poisoned GitHub issue steered an agent into leaking private repositories11. A research agent was tricked into leaking
Gmail data from the provider's own infrastructure, where no enterprise control could see it (ShadowLeak)12. OAuth
tokens stolen from an AI chat integration cascaded into data theft across hundreds of downstream SaaS tenants22.
The first malicious MCP server was caught in the wild, quietly BCC'ing every email that passed through it23. And in
November, Anthropic disclosed what it assessed as the first cyber espionage campaign in which an AI agent executed
the large majority of the operation — target reconnaissance, exploit development, credential harvesting — with
humans intervening at a handful of decision points13 (a characterization, it should be noted, that independent
researchers could not fully verify).
The first half of 2026 has confirmed the trajectory rather than bent it. An exposed database on a viral agent social
network let anyone hijack any of 1.5 million registered agents24; a coordinated campaign seeded an agent skill
marketplace with hundreds of malware-bearing skills25; and Microsoft published critical CVEs demonstrating that a
single injected prompt can achieve host-level code execution in mainstream agent frameworks26. The era's lesson
compounds: every new layer of agent infrastructure — protocols, marketplaces, frameworks — arrives with the same
trust gap the last one had.
The AI Threat Report 2026 OrcaRouter Security Research · 7

EXHIBIT 1 Three years, three eras — from leaked text to autonomous operations
Source: Public disclosures and research as cited in the endnotes; OrcaRouter Security Research compilation

### 1.3 The perimeter moved into the context window
Traditional security architecture assumes a boundary: trusted inside, untrusted outside, controls at the seam.
Language models dissolve that boundary, because a model's input is also its programming. Any text a model reads —
a user's question, a retrieved document, a web page, a tool result — can carry instructions the model may follow.
There is no reliable, general mechanism by which today's models distinguish content to process from commands to
obey. That is why prompt injection holds the number-one position in the OWASP Top 10 for LLM Applications9, and
why it cannot be fixed the way a buffer overflow is fixed.
Attackers have internalized this faster than defenders. In Gartner's 2025 survey, 32% of security leaders reported
attacks on their AI applications through the prompt itself, and 29% reported attacks on GenAI application
infrastructure3. Telemetry from production LLM applications shows successful attacks completing in 42 seconds on
average, with 90% of them leaking sensitive data4. In HiddenLayer's survey, 74% of organizations said they definitely
knew of an AI breach in 202427. And the AI-crime category now has an official price tag: the FBI's 2025 Internet Crime
The AI Threat Report 2026 OrcaRouter Security Research · 8

Report — the first in its history with a dedicated AI section — logged 22,364 AI-related complaints and nearly $893
million in losses6.
The same capability shift arms the other side of the ledger: 82.6% of phishing emails analyzed in late 2024 and early
2025 showed signs of AI generation, a figure that reached 86% by April 202628; a deepfake attempt occurred every
five minutes during 202414; and by late 2025, Google's threat intelligence team had catalogued the first malware
families that call LLMs mid-execution to regenerate their own code and evade detection29. AI is simultaneously the
new attack surface and the new attack tool.

### 1.4 What changes in 2026
Three forces converge this year and convert AI security from initiative to obligation. Regulation arrives: the EU AI Act,
in force since August 2024, becomes fully applicable on August 2, 2026, completing a staged rollout that began with
prohibitions in February 2025 and general-purpose-AI obligations in August 20257. Agents go mainstream: Gartner
projects 40% of enterprise applications will ship with task-specific AI agents by the end of 2026, up from under 5% in
202530 — and simultaneously predicts that by 2028 a quarter of enterprise GenAI applications will suffer at least five
security incidents per year31. The failure mode is priced in: Gartner expects over 40% of agentic AI projects to be
canceled by the end of 2027, with inadequate risk controls among the leading causes32.
The strategic implication threads through the rest of this report: AI security in 2026 is not a model problem to be
solved with better training. It is an architecture problem — identity, content control, action control, and evidence —
and it is solvable with the discipline enterprises already apply to every other production system.
The AI Threat Report 2026 OrcaRouter Security Research · 9

THE THREATS

## 2. A taxonomy of AI threats
Fourteen threat classes account for the overwhelming majority of real-world AI attacks.
They organize into four families — and, more usefully for defenders, onto two planes:
what the model reads and writes, and what the agent does.

### 2.1 Four families, two planes
Security teams confronting AI for the first time tend to inherit a vocabulary invented piecemeal — jailbreaks, injections,
hallucinations — that obscures more than it reveals. Our taxonomy, distilled from the attack patterns documented
across OrcaRouter's threat research33 and the public incident record, organizes the landscape into fourteen threat
classes in four families: content-plane threats that live in the text a model reads or writes; action-plane threats that
fire through what an agent does; economic threats that attack spend and availability; and trust & supply chain threats
that compromise what the agent is built from.
The plane distinction is the load-bearing one, because the two planes are governed by different controls. Content-
plane attacks are caught by screening text — input and output guardrails. Action-plane attacks are caught by policing
behavior — rules over tool calls, network destinations, and spend. The most damaging real-world incidents chain both
planes: an injection arrives as content, then cashes out as an action. A defense that watches only one plane will
verifiably miss the attacks that matter.
The AI Threat Report 2026 OrcaRouter Security Research · 10

EXHIBIT 3 Fourteen threat classes, four families — organized by where the attack lives
Source: OrcaRouter Security Research, from the OrcaRouter threat model33

### 2.2 The content plane: attacks in the text
Prompt injection is the family's apex threat and the technique underlying most modern AI attacks. In its direct form,
the attacker is the user: crafted input overrides the system prompt or unlocks restricted behavior. In its far more
dangerous indirect form, the attacker plants instructions in content the AI will eventually ingest — a web page, a PDF,
an email, a calendar invite, a ticket, a tool response. The model encounters the payload inside trusted context and
executes it with the agent's full authority. No account compromise is required; the attacker never touches your
system. They publish content and wait.
Jailbreaks are the adversarial craft of defeating a model's safety training: role-play frames, encoding tricks (Base64,
character substitution, invisible Unicode tag bytes), multi-turn escalation, and token-stuffing. The technique pool is
industrial — measured success rates of roughly 20% against guarded production applications4 — and evolves weekly,
which is why static keyword filters age so badly. Unsafe output inverts the direction of risk: model responses carrying
executable payloads (SQL fragments, scripts) into downstream systems that auto-execute them. PII exposure and
secret leakage round out the family — personal data and live credentials flowing through prompts, logs, and
completions, where they acquire new copies, new jurisdictions, and new readers. These two classes are as much
compliance liabilities as attack vectors: they are how an AI deployment quietly becomes a GDPR, HIPAA, or PCI
incident.
The AI Threat Report 2026 OrcaRouter Security Research · 11

### 2.3 The action plane: attacks through behavior
Give a model tools and you have given every successful injection an execution engine. Dangerous tool calls — the
model invoking destructive operations (shell.exec, db.delete, payment APIs) or legitimate tools with hostile
arguments — are the action plane's bluntest threat. Excessive agency is its quietest: an agent holding more capability
than its task requires, so that a single hijack inherits a large blast radius. The canonical failure is the confused deputy
— an agent with legitimate authority tricked into exercising it for an attacker. Both EchoLeak and the GitHub MCP
exploit were confused-deputy attacks: nothing was "hacked" except the agent's intentions1011.
Tool-response tampering closes the loop from the other side: a compromised or malicious tool returns results that
carry instructions or fabricated data, steering the agent's next step. And data exfiltration over the network is where
most chains terminate — the agent fetches an attacker URL with stolen data encoded in the path, or reaches an
internal service it should never see (the SSRF pattern). Egress is the choke point: an exfiltration that cannot leave is an
incident report, not a breach.

### 2.4 The economic family: attacks on the meter
Agents introduce a loss class that requires no data theft at all. Denial-of-wallet attacks the meter: a runaway retry
loop, an injected instruction to fan out thousands of tool calls, a leaked key driven hard by a third party — the
economy security researchers named “LLMjacking,” with observed victim exposure topping $46,000 a day34 — or
simply a long-context task burning tokens far beyond intent. The observed patterns are distinctive — the same call
hammered in a tight window, spend spiking against an hourly baseline, fan-out the workspace has never exhibited —
and they are behavioral signatures, invisible to any per-request check. Unbounded spend authority is the only
vulnerability in this report that compounds by the minute.

### 2.5 Trust & supply chain: attacks on what the agent is made of
The fourth family compromises the agent's components rather than its conversation. MCP tool poisoning exploits the
Model Context Protocol's trust model: an agent connects to a server and believes its self-declared tool manifest. A
malicious server advertises legitimate-looking tools whose descriptions carry hidden instructions for the model — and
the rug-pull variant behaves honestly for weeks before silently shipping a new manifest that adds dangerous
capabilities. Memory poisoning plants instructions in an agent's persistent state, where they survive across sessions
and re-execute long after the hostile content is gone. Supply chain covers the classic vector at new scale —
compromised model weights (a single 2024 sweep found roughly one hundred backdoored models on a public model
hub35), poisoned datasets, malicious packages and skills, and weaponized configuration like the Rules File Backdoor
attack on AI coding assistants36. And chained attacks are the family's capstone: sequences of individually plausible
steps whose damage lives entirely in the composition. Chapter 3 dissects them.
The AI Threat Report 2026 OrcaRouter Security Research · 12

EXHIBIT 4 Severity and prevalence are inversely correlated — the rarest attacks are the ones that end
up in board reports
Source: OrcaRouter Security Research analysis; illustrative; positions reflect judgment over the 2025–26 public record, not measured incidence
Exhibit 4 captures the landscape's central asymmetry. The high-frequency threats — injection attempts, jailbreak
probes — are mostly absorbed by basic controls; the low-frequency ones — chained attacks, supply-chain
compromise, network exfiltration — are the ones that produce eight-figure incidents. Defense budgets anchored to
frequency alone will systematically underinvest in exactly the threats that matter.

### 2.6 Anchoring to the standards
The taxonomy maps directly onto the frameworks your auditors and regulators will reference. The OWASP Top 10 for
LLM Applications 20259 is the de-facto risk vocabulary; NIST's Generative AI Profile37 supplies the risk-management
spine; MITRE ATLAS catalogues adversary techniques. The table below carries the crosswalk; Chapter 5 extends it to
controls and to the EU AI Act and ISO/IEC 42001.
The AI Threat Report 2026 OrcaRouter Security Research · 13

Threat family Representative classes OWASP LLM Top 10 (2025) Primary control plane
Content Prompt injection · jailbreaks · LLM01 Prompt Injection · LLM02 Sensitive Input & output guardrails
plane unsafe output · PII · secrets Information Disclosure · LLM05 Improper
Output Handling
Action plane Dangerous tool calls · excessive LLM06 Excessive Agency · LLM05 Improper Action-layer firewall: tool,
agency · tampering · exfiltration Output Handling argument & egress policy
Economic Denial-of-wallet and resource LLM10 Unbounded Consumption Spend caps · per-run cost
abuse ceilings · anomaly detection
Trust & MCP poisoning · memory LLM03 Supply Chain · LLM04 Data & Model Manifest pinning · quarantine
supply chain poisoning · supply chain · chained Poisoning · LLM08 Vector & Embedding · provenance · run
attacks Weaknesses correlation
Source: OWASP GenAI Security Project9; OrcaRouter Security Research mapping
The AI Threat Report 2026 OrcaRouter Security Research · 14

THE ATTACKS

## 3. Anatomy of the modern AI attack
The incidents that defined 2025 were not exotic. They followed a repeatable kill chain
— entry through trusted content, hijack of the model's intentions, abuse of legitimate
authority, and exit through an open egress path. Walk the chain once and every
headline becomes legible.

### 3.1 The AI kill chain
Modern AI attacks decompose into five stages. The attacker enters through something the agent trusts — content it
will read, a tool it will load, a key it will honor. They hijack instructions, converting the model's obedience into their
interface. They abuse capability — the agent's own tools, run with the agent's own permissions. They collect and
stage what they came for, often across many small, plausible steps. And they impact: exfiltrate, destroy, defraud, or
simply spend. The chain is the unit of analysis that makes AI incidents legible — and the unit of defense, because
each stage crosses a different control surface.

EXHIBIT 6 Five stages, five interception points — the chain is also the defense map
Source: OrcaRouter Security Research
Security architecture should assume stage two will succeed somewhere, eventually: injection is a property of the
medium. What separates an incident from a breach is whether stages three through five find anything to work with.
The AI Threat Report 2026 OrcaRouter Security Research · 15

The three case files that follow — each reconstructed from public disclosures and mapped to the patterns in
OrcaRouter's threat research33 — show the chain in the wild.

### 3.2 Case file 1: the zero-click exfiltration
CASE FILE 01
EchoLeak — when reading an email is the whole attack
The attack. In June 2025, Aim Security disclosed EchoLeak (CVE-2025-32711), a zero-click exfiltration chain in
Microsoft 365 Copilot. A crafted external email carried instructions disguised as ordinary text. When the assistant
later processed the user's mailbox — summarizing, searching, drafting — it ingested the payload, followed the
embedded instructions to gather sensitive context from mail, files, and chat history, and encoded the result into a
markdown image URL that fetched automatically. The user clicked nothing. The attacker simply sent an email and
waited for the agent to read it10.
Why it worked. Every stage crossed a surface nobody was watching: untrusted content entered through a
trusted channel (inbound mail), the model treated retrieved text as instructions (an LLM-scope violation), and an
unrestricted egress path — an auto-fetched image URL — carried the data out.
The architectural lesson. Patch-level fixes close one instance; the class stays open wherever an agent combines
private-data access, untrusted content, and an open egress channel — the “lethal trifecta” formulation38.
ShadowLeak proved the point three months later with the same logic executed service-side, beyond the reach of
any enterprise network control12 — enforcement has to live where the agent's actions are mediated, not at the
network edge.

### 3.3 Case file 2: the poisoned supply chain
CASE FILE 02
GitHub MCP and the rug-pull — trusting tools you didn't write
The attack. In May 2025, Invariant Labs demonstrated a toxic-flow attack against agents using the GitHub MCP
integration: a hostile instruction planted in a public repository issue. When the owner asked their agent to review
open issues, the payload redirected it — the agent, holding the user's token, pulled data from the user's private
repositories and published it into a public pull request11. No vulnerability existed in any single component; the
breach lived entirely in the composition of legitimate capabilities.
The variant that scales. The same trust gap powers the MCP rug-pull: a community tool server behaves honestly
until it has been adopted, then silently ships a manifest update that adds capabilities or rewrites tool descriptions
with hidden instructions. Agent frameworks that auto-refresh manifests load the new behavior without any human
review. The 2025 ecosystem also logged the cruder forms — typosquatted servers and malicious packages
exfiltrating the data that flowed through them.
The architectural lesson. Third-party tools are supply chain, and need supply-chain discipline at runtime: pin the
manifest you reviewed, diff on every change, quarantine new capabilities by default, and pass every dispatch
through policy. Exhibit 9 contrasts the governed and ungoverned timelines.
The AI Threat Report 2026 OrcaRouter Security Research · 16

EXHIBIT 5 Anatomy of an indirect injection — the payload crosses the trust boundary inside ordinary
content
Source: OrcaRouter Security Research
EXHIBIT 9 The rug-pull, governed and ungoverned — the same Day-31 manifest change, two different
endings
Source: OrcaRouter Security Research, from the OrcaRouter MCP threat research33
The AI Threat Report 2026 OrcaRouter Security Research · 17

### 3.4 Case file 3: the attack that only spends money
CASE FILE 03
Denial-of-wallet — no breach, no exfiltration, just a bill
The pattern. A production agent hits a malformed record and enters a retry loop — the same tool, the same
arguments, hundreds of times an hour, each call individually valid. Or an injected instruction tells a research agent
to enumerate and summarize every document in the corpus, fanning out API calls at machine speed. Or a key
scraped from a public repository quietly runs someone else's workload on your account. Composite
reconstructions of the incident patterns documented in OrcaRouter's threat research33 — but every operator of
autonomous agents eventually meets one of them.
Why it evades review. Each call passes every content check and every per-call policy. The attack is a shape —
volume, repetition, and spend against time — and only run-level telemetry sees shapes: the same-call-tight-
window signature of a stuck loop, cost spiking against a learned hour-of-week baseline, a tool-to-tool transition
the workspace has never made.
The architectural lesson. Spend is a security boundary. Per-key credit limits, per-run cost ceilings that hard-stop
a run mid-flight, and behavioral anomaly detection turn an unbounded liability into a bounded, alerting one. The
fix costs minutes to configure; its absence is priced by the hour.

EXHIBIT 7 Nine plausible steps, one breach — per-call review passes every link in the chain
Source: OrcaRouter Security Research analysis; illustrative; step sequence is a composite of documented attack patterns

### 3.5 What the chains teach
• Per-call review is necessary and insufficient. Every case file above survives a filter that asks “is this single step
allowed?” Detection has to operate on sequences: run-level correlation, behavioral baselines, novel-transition
flags.
The AI Threat Report 2026 OrcaRouter Security Research · 18

• The trust boundary is inside the context window. Network position, sender reputation, and file type no longer
predict hostility. Any content an agent ingests must be treated as potentially adversarial — including content from
your own systems, which may itself be poisoned.
• Egress is the choke point. Almost every chain that steals data terminates in an outbound request. A default-deny
egress allow-list converts “exfiltration” into “denied connection attempt” — it is the highest-leverage single control
in this report.
• Authority, not intelligence, sets the blast radius. The model's capability determines what an attack could do; the
agent's permissions determine what it does do. Scoped credentials and least-agency design bound every chain at
once, including the ones nobody has invented yet.
The AI Threat Report 2026 OrcaRouter Security Research · 19

THE INFLECTION

## 4. The agentic inflection point
Chatbots made AI risk a content-moderation problem. Agents make it an attack-surface
problem. The difference is structural — agents act, ingest, and self-extend — and 2026
is the year that difference reaches production scale.

### 4.1 From answers to actions
Three structural properties separate an agent from the chatbot that preceded it33. Agents act: a harmful chatbot
answer still needs a human to do damage; a hijacked tool call — a payment, a deletion, an export — is the damage,
often irreversibly. Agents ingest: they read web pages, documents, inboxes, and tool results as a condition of being
useful, and every one of those streams can carry adversarial instructions aimed at the agent rather than the user.
Agents self-extend: frameworks that auto-load skills and MCP servers acquire capabilities at runtime that no human
reviewed — and the attack can arrive as the new capability itself.

EXHIBIT 8 The chatbot had two trust surfaces; the agent has twelve and counting
Source: OrcaRouter Security Research
This is no longer an early-adopter posture. Gartner projects 40% of enterprise applications will embed task-specific
agents by the end of 2026, from under 5% in 202530; a third of enterprise software will include agentic AI by 202830;
and 62% of organizations are already experimenting1. The Model Context Protocol — agents' de-facto integration
standard — reached 97 million monthly SDK downloads and moved to neutral governance under the Linux Foundation
in December 202539. The capability supply chain is institutionalizing faster than the controls around it.
The AI Threat Report 2026 OrcaRouter Security Research · 20

### 4.2 Excessive agency is the defining risk
Ask why each 2025 incident mattered and the answer is rarely the cleverness of the injection — it is the authority the
compromised agent held. The OWASP framing, excessive agency9, names the pattern: functionality, permissions, or
autonomy beyond what the task requires. An agent with read access to every mailbox, a token scoped to every
repository, an unrestricted outbound network, and no spend ceiling is not an automation asset; it is a standing
confused-deputy liability waiting for its first hostile instruction.
The discipline that contains it is least agency — least privilege, restated for systems that make their own decisions.
Each agent gets its own identity, the minimum tool set, the minimum data scope, an explicit egress list, a spend cap,
and an expiry. Under least agency, a successful injection inherits a sandbox; under excessive agency, it inherits an
enterprise. The security property worth engineering is that the worst instruction the model could follow is still
survivable — a property of the permissions, not of the model.

### 4.3 The trust problem in the tool economy
The MCP ecosystem replays the early package-registry era — thousands of community servers, install-time trust, no
provenance — but with a twist that makes it more dangerous: the artifact being trusted is prose addressed to a model.
Tool names and descriptions are instructions the model reads on every run, so a manifest is executable content in
exactly the sense Chapter 2's content-plane analysis warns about. Tool poisoning, lookalike servers, and rug-pulls are
the predictable result11. Runtime governance — manifest pinning, capability quarantine, per-dispatch policy — is the
supply-chain control the registry era eventually learned to apply at build time, now required at run time.

### 4.4 Shadow AI: the estate you can't see
While security teams harden sanctioned deployments, the unsanctioned estate grows beside them: personal API keys
in scripts, browser extensions wired to corporate inboxes, departmental agents stood up on a credit card. IBM's 2025
breach data prices the blind spot — one in five breached organizations traced the incident to shadow AI, at a
$670,000 premium over the average breach5 — and only 37% of organizations have any policy for detecting it5.
Shadow AI is rarely malicious; it is what unmet demand looks like. The remedies that work are economic as much as
technical: make the governed path the easiest path — centralize model access behind a gateway that issues scoped
keys in minutes, then inventory and migrate the stragglers. Prohibition without a paved road reliably produces more
shadow, not less.
The stakes of getting agency governance right are strategic, not merely defensive. Gartner's projection that over 40%
of agentic AI projects will be canceled by 2027 cites inadequate risk controls among the leading causes32. Security
maturity is becoming the gating factor on whether the agent investments of 2025–26 ever reach production value. The
control architecture in the next chapter is, on that reading, an enablement plan as much as a defense.
The AI Threat Report 2026 OrcaRouter Security Research · 21

THE DEFENSE

## 5. The defense blueprint: zero trust for
AI
Every pattern in this report yields to the same architecture: give agents scoped
identities, screen content on both directions, police actions at a gateway, and write
everything down. None of it requires new science — it requires applying the security
discipline you already trust to the newest actor on your network.

### 5.1 Four principles
1. Assume injection. Some hostile instruction will eventually reach your model — through a document, a tool result, a
manifest. Design so a hijacked model is a contained event, not a compromised enterprise.
2. Enforce least agency. Every agent gets its own identity carrying the minimum models, tools, data, egress, spend,
and lifetime. Authority, not model quality, sets the blast radius.
3. Control both planes. Screen what the model reads and writes (content), and police what the agent does (action).
Either alone misses the chained attacks that produce headlines.
4. Audit everything. Every match, verdict, approval, and policy change lands in a tamper-evident trail correlated by
run and session. If you cannot reconstruct what an agent did, you cannot defend it, debug it, or attest to it.

### 5.2 The reference control stack
The architecture below is the control stack OrcaRouter runs in production33; we present it here as a reference design
because each layer answers a specific failure mode documented in Chapters 1–4, and because its logic is portable to
any enforcement point that mediates all model and tool traffic. The decisive property is placement: controls live at a
gateway in the request path, so they bind to credentials rather than to application code — enforceable across every
team and framework, with no agent rewrites.
The AI Threat Report 2026 OrcaRouter Security Research · 22

EXHIBIT 10 Six layers between a request and a regret — each one independent, each one auditable
Source: OrcaRouter Security Research, from the OrcaRouter control stack33
Layer 1 — scoped identity. Every agent calls through its own key, carrying allowed models, an IP allow-list, a hard
spend cap, an expiry date, and bindings to the policies below. An out-of-scope request dies before any content is
read. This is the layer that converts “we think only the support bot uses this” into an enforced fact — and key hygiene
is precisely what 97% of AI-breached organizations lacked2.
Layer 2 — input guardrails. Before any model call, request text crosses injection and jailbreak rules, PII detection and
masking, secret blocking, and — where stakes warrant — a semantic LLM-judge that catches what regex cannot. A
block here costs zero model tokens; masking sanitizes and continues.
Layer 3 — the action firewall. Every tool call, MCP dispatch, and egress destination is judged against ordered policy
across four surfaces (advertised tools, model-emitted calls, MCP dispatches, network destinations) with six verdicts:
allow, audit, deny, sanitize (redact arguments and proceed), pending approval (hold irreversible steps for a human),
and cap cost (hard-stop a run at a spend ceiling). A default-deny posture means a chain cannot wander into a tool or
host you never listed — the control that breaks every case file in Chapter 3.
Layer 4 — output guardrails. The reply is screened on the way out: unsafe-output rules, PII and secret masking,
grounding checks. The symmetric pass matters because indirect injection's first observable artifact is often the
response — an answer that suddenly contains a markdown image URL with suspicious query parameters.
Layers 5 and 6 — anomaly detection and audit. Behavioral detectors watch what static rules cannot predict: the
same-call-tight-window signature of a runaway loop, spend or volume spiking against a learned hour-of-week
baseline, a tool-to-tool transition the workspace has never made. Beneath everything, an audit trail records every
decision, correlated by agent run and session, exportable as signed evidence. This layer converts a security
The AI Threat Report 2026 OrcaRouter Security Research · 23

architecture into a demonstrable one — the difference an auditor, a regulator, or an incident-response retainer will
price.

### 5.3 Rollout: observe, shadow, enforce
The blueprint's adoption risk is operational, not technical: a control that blocks legitimate traffic on day one is a control
that gets turned off by day three. The rollout pattern that survives contact with production is staged33. Observe first —
run agents through the gateway with everything in audit mode and let two weeks of traffic write your baseline: which
tools, which hosts, what spend, which calls would have been flagged. Shadow next — author the real policy and run it
in would-block mode against live traffic, tuning until false positives approach zero. Enforce last — flip verdicts live,
with human approval reserved for the genuinely irreversible (payments, deletes, sends) and cost caps bounding every
run. Teams that follow the sequence convert in weeks and keep the controls on; teams that skip to enforcement
generate a war story and a rollback.

EXHIBIT 11 No rule touches live traffic until it has proven itself against your real workload
Source: OrcaRouter Security Research, from the OrcaRouter enforcement-modes design33

### 5.4 Proving it: the compliance crosswalk
From August 2026, “show me” replaces “tell me” as the regulatory baseline in the EU7, and the same evidentiary
instinct is spreading through SOC 2 scopes, cyber-insurance questionnaires, and procurement reviews. The crosswalk
below maps the control stack onto the four frameworks security leaders are most often asked about. The strategic
point: one well-placed control layer generates the evidence for all of them simultaneously — runtime enforcement logs
are the raw material of every AI attestation you will be asked for.
The AI Threat Report 2026 OrcaRouter Security Research · 24

NIST AI RMF / GenAI
Control layer OWASP LLM Top 10 (2025) EU AI Act ISO/IEC 42001
Profile
Scoped identity — per- LLM06 Excessive Agency GOVERN — roles, Art. 9 risk A.9.2 resources; A.6
agent keys, model accountability, access management; Art. 14 AI system life cycle
limits, spend caps, human oversight
expiry
Input/output guardrails LLM01 Prompt Injection · MEASURE — Art. 9; Art. 15 A.7 data
— injection, jailbreak, LLM02 Sensitive Info evaluation; MANAGE accuracy & management; A.8
PII, secrets, output Disclosure · LLM05 — risk treatment robustness information for
safety Improper Output Handling interested parties
Action firewall — tool/ LLM06 Excessive Agency · MANAGE — incident Art. 14 human A.6.2 controls over AI
argument policy, LLM03 Supply Chain response; MAP — oversight; Art. 15 system use
egress allow-lists, (runtime) · LLM10 context & capability robustness &
approvals, cost caps Unbounded Consumption cybersecurity
Audit & anomaly — Cross-cutting — evidence GOVERN & MEASURE Art. 12 record- A.5 governance;
signed logs, run for all ten — monitoring, keeping; Art. 26 clause 9 performance
correlation, behavioral documentation deployer obligations evaluation
baselines
Source: OrcaRouter Security Research mapping across OWASP9, NIST37, the EU AI Act7, and ISO/IEC 4200140; article references indicative, not legal
advice
The AI Threat Report 2026 OrcaRouter Security Research · 25

THE AGENDA

## 6. The CISO agenda for 2026
Twelve months is enough — to inventory the estate, put identity and policy in front of
every agent, reach enforcement without breaking production, and stand in front of the
board with evidence instead of assurances.

### 6.1 The twelve-month roadmap
The sequence below compresses the observed practice of teams that reached enforced, evidenced AI security
without stalling delivery. The quarters overlap deliberately: baselining starts while identity work finishes; evidence
generation begins the day enforcement does.

EXHIBIT 12 Four quarters from inventory to evidence — overlapping by design
Source: OrcaRouter Security Research analysis; illustrative
Months 0–3: see the estate. Inventory every AI touchpoint — sanctioned and shadow — and route traffic through a
gateway in observe mode. Issue every agent its own scoped key with an expiry; kill shared credentials. The
deliverable is a complete map of tools, hosts, and spend per agent, and the quiet retirement of the keys nobody could
explain. Months 3–6: turn on the content plane. Guardrails on input and output — injection, PII, secrets — tuned
through shadow mode against real traffic; firewall policy authored from the observed baseline. Months 6–9: enforce
the action plane. Default-deny tool policy, egress allow-lists, approval gates on irreversible operations, cost caps on
every run. Install the compliance packs and generate the first signed evidence report. Months 9–12: prove and
The AI Threat Report 2026 OrcaRouter Security Research · 26

pressure-test. Red-team the deployed stack against Chapter 3's chains, run an agent-incident tabletop, and take KPIs
to the board.

### 6.2 The metrics that matter
AI security reporting fails boards when it arrives as anecdotes. Six KPIs, trended quarterly, carry the whole story:
coverage (share of AI traffic behind the gateway — the shadow-AI denominator), identity hygiene (share of keys
scoped, capped, and expiring), pressure (injection attempts blocked, a measure of threat weather, not failure),
responsiveness (mean time to revoke a credential), bounded loss (spend denied by cost caps), and evidence (share of
tool calls with a logged verdict — the audit-coverage figure your attestations rest on).

EXHIBIT 13 Six numbers that tell the board the whole story
Source: OrcaRouter Security Research analysis; illustrative; values are representative targets, not benchmarks

### 6.3 Ten questions boards should ask
1. How many AI agents and assistants run with access to production data today — and how many did we find rather
than approve?
2. Does every agent have its own credential, with a spend cap and an expiry date? How many shared keys remain?
3. If a prompt injection succeeded this afternoon, what is the worst action the hijacked agent could take?
4. Which tools can our agents reach, and is the list default-deny or default-allow?
5. Where can our agents send data on the network? Who approved that list, and when was it last reviewed?
6. What is the maximum a single runaway agent run can spend before something stops it?
7. Which irreversible actions — payments, deletions, external sends — require a human approval today?
8. When a third-party tool server changes its capabilities, what happens — automatically — before the new code
runs?
9. Can we reconstruct, end to end, everything a given agent did last Tuesday? How long would that take?
The AI Threat Report 2026 OrcaRouter Security Research · 27

10. Which framework — OWASP, NIST AI RMF, EU AI Act, ISO 42001 — anchors our AI controls, and what evidence of
enforcement could we produce this week?

### 6.4 The bottom line
The 2026 threat landscape is not a reason to slow AI adoption; it is the operating manual for surviving it. Every attack
in this report — the zero-click exfiltrations, the poisoned tools, the silent spend — succeeds against unscoped
authority and fails against scoped, policed, audited authority. That property is buildable now, at the gateway, in weeks.
The organizations that internalize it will spend 2026 compounding the advantages of agentic AI. The rest will spend it
explaining incident reports that this report described in advance.
The AI Threat Report 2026 OrcaRouter Security Research · 28

METHODOLOGY
Methodology & reading guide
Public data. Every statistic in this report is drawn from a named public source — vendor telemetry reports, analyst
surveys, government statistics, regulatory texts, and primary incident disclosures — cited in the endnotes. Survey
figures reflect each source's methodology and sample; where samples are small or vendor-sponsored (noted in the
endnotes), we treat the figures as directional. Statistics were verified against the publishing organization's own
materials in May–June 2026; readers should consult the originals before re-citing.
Illustrative exhibits. Exhibits labeled illustrative (the severity–prevalence matrix, the chained-attack curve, the
roadmap, and the KPI dashboard) are analytical constructs of OrcaRouter Security Research: they encode judgment
formed from the public incident record and the threat patterns documented in OrcaRouter's security research, not
measured incidence data. They are designed to structure decisions, not to report measurements.
Case files. The case files in Chapter 3 are reconstructed from the cited public disclosures of the researchers and
vendors involved. Where we generalize a pattern (the rug-pull, denial-of-wallet), the narrative is a composite labeled
as such — drawn from the documented threat patterns in OrcaRouter's threat library, not from any single customer's
data. No OrcaRouter customer data appears in this report.
Product references. Chapter 5 presents the control architecture OrcaRouter operates in production, identified as such.
The blueprint's principles — scoped identity, two-plane control, staged enforcement, signed audit — are stated
generally and are implementable on any enforcement point with equivalent placement in the request path.
The AI Threat Report 2026 OrcaRouter Security Research · 29

APPENDIX A
The fourteen threat classes
One-line definitions and the primary mitigating control for each class in the Chapter 2 taxonomy.
Threat class Family In one line Primary control
Prompt injection (direct) Content The user's own input overrides system Input guardrails: injection & jailbreak rules
intent
Prompt injection (indirect) Content Instructions hidden in content the agent Output screening + action firewall on the
ingests triggered call
Jailbreaks & evasion Content Adversarial phrasing defeats safety Layered keyword/regex + semantic LLM-
training judge rules
Unsafe output Content Model responses carry executable or Output-stage guardrails before downstream
harmful payloads systems
PII exposure Content Personal data flows through prompts, logs, PII detection with masking on input and
or replies output
Secret & credential leakage Content Live keys and tokens transit the model Secret-pattern blocking; argument
path sanitization
Dangerous tool calls Action Destructive tools or hostile arguments Default-deny tool policy; argument validation
invoked
Excessive agency / confused Action Over-permissioned agent abused by Scoped keys; least-agency design; approvals
deputy whoever steers it
Tool-response tampering Action Malicious tool results steer the agent's Response screening; anomaly review of call
next step patterns
Data exfiltration & SSRF Action Stolen data exits via egress; internal Default-deny egress allow-list at the gateway
services reached
Denial-of-wallet Economic Loops, fan-out, or stolen keys burn Per-key credit limits; per-run cost caps; burn
unbounded spend anomalies
MCP tool poisoning & rug- Trust Malicious or mutated tool servers Manifest pinning; capability quarantine;
pulls compromise the agent dispatch policy
Memory poisoning Trust Hostile instructions persist in agent state Memory-write screening; provenance;
across sessions periodic re-grounding
Supply chain (models, data, Trust Compromised components ship attacker Provenance & scanning pre-deploy; runtime
packages) behavior firewall backstop
Chained attacks — sequences of individually plausible steps — are the cross-cutting fifteenth pattern; their control is run-level: correlation, behavioral
baselines, and cost ceilings. See Chapter 3.
The AI Threat Report 2026 OrcaRouter Security Research · 30

GLOSSARY
The vocabulary of AI security
Agent — An AI system that pursues goals by taking actions Indirect prompt injection — Hostile instructions planted in
— calling tools, retrieving content, writing state — rather content an AI will ingest — documents, pages, emails, tool
than only generating text. results — rather than typed by a user.
Action plane — The set of things an agent does — tool calls, Jailbreak — A technique for defeating a model's safety
MCP dispatches, network egress — as distinct from the text training through adversarial phrasing, encoding, or multi-turn
it processes. manipulation.
Chained attack — A breach composed of many individually Least agency — Least privilege restated for autonomous
plausible steps whose damage lives in the sequence, not in systems: minimum tools, data, egress, spend, and lifetime
any single call. per agent.
Confused deputy — A system with legitimate authority LLM-judge rule — A guardrail that uses a model to evaluate
tricked into using it on an attacker's behalf — the canonical semantic intent — catching evasions that pattern matching
agent failure mode. cannot.
Content plane — The text surface of an AI system — MCP (Model Context Protocol) — The open standard
prompts, retrieved context, and model output. through which agents discover and call external tools;
governed by the Agentic AI Foundation since December
Cost cap (cap_cost) — A firewall verdict that denies further
2025.
calls once an agent run's accumulated spend crosses a
defined ceiling. Memory poisoning — Planting instructions in an agent's
persistent state so they execute in later sessions.
Default-deny — A policy posture in which anything not
explicitly allowed is blocked — the inverse of blocklisting. Rug-pull — A trusted third-party tool server that changes its
capabilities or descriptions after adoption.
Denial-of-wallet — An attack (or failure mode) that exhausts
spend rather than stealing data: loops, fan-out, leaked-key Shadow AI — AI usage adopted outside security's
abuse. knowledge or governance — personal keys, unsanctioned
tools, departmental agents.
Egress allow-list — An enumerated set of network
destinations an agent may reach; everything else is denied Shadow mode — Running a policy against live traffic in
at the gateway. would-block mode to tune it before enforcement.
Excessive agency — Functionality, permissions, or SSRF (server-side request forgery) — Inducing a server —
autonomy beyond what an agent's task requires (OWASP here, an agent's tool — to make requests to internal or
LLM06). attacker-chosen destinations.
Guardrails — Content-plane controls that screen input and Zero-click attack — An exploit requiring no victim
output text — injection rules, PII masking, secret blocking, interaction; in AI systems, typically an indirect injection
semantic judges. processed automatically.
The AI Threat Report 2026 OrcaRouter Security Research · 31

ENDNOTES
Sources
1 McKinsey & Company, “The State of AI in 2025: Agents, innovation, 20 CNN Business, “British engineering giant Arup revealed as $25 million
and transformation,” November 2025. https://www.mckinsey.com/ deepfake scam victim,” May 16, 2024. https://edition.cnn.com/
capabilities/quantumblack/our-insights/the-state-of-ai 2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk
2 IBM Newsroom, “13% of organizations reported breaches of AI models 21 Cohen, S., Bitton, R., Nassi, B., “Here Comes the AI Worm: Unleashing
or applications, 97% of which reported lacking proper AI access Zero-click Worms that Target GenAI-Powered Applications” (Morris II),
controls,” July 30, 2025. https://newsroom.ibm.com/2025-07-30-ibm- March 2024. https://arxiv.org/abs/2403.02817
report-13-of-organizations-reported-breaches-of-ai-models-or- 22 Google Threat Intelligence Group / Mandiant, analysis of the Salesloft
applications,-97-of-which-reported-lacking-proper-ai-access-controls Drift OAuth token compromise (UNC6395), August–September 2025. h
3 Gartner, “Gartner Survey Reveals GenAI Attacks Are on the Rise,” press ttps://cloud.google.com/blog/topics/threat-intelligence/data-theft-
release, September 22, 2025. Survey of 302 cybersecurity leaders, salesforce-instances-via-salesloft-drift
March–May 2025. https://www.gartner.com/en/newsroom/press- 23 Koi Security, via The Hacker News, “First malicious MCP server found:
releases/2025-09-22-gartner-survey-reveals-generative-artificial- postmark-mcp impersonation BCC'd outbound email to an attacker
intelligence-attacks-are-on-the-rise domain,” September 2025. https://thehackernews.com/2025/09/first-
4 Pillar Security, “The State of Attacks on GenAI,” October 2024. malicious-mcp-server-found.html
Telemetry from 2,000+ production LLM applications. https:// 24 404 Media, “Exposed Moltbook database let anyone take control of
www.pillar.security/resources/the-state-of-attacks-on-genai any AI agent on the site,” with Wiz analysis of ~1.5M exposed API
5 IBM Security & Ponemon Institute, “Cost of a Data Breach Report tokens, January 2026. https://www.404media.co/exposed-moltbook-
2025,” July 2025. https://www.ibm.com/reports/data-breach database-let-anyone-take-control-of-any-ai-agent-on-the-site/
6 FBI Internet Crime Complaint Center, “2025 Internet Crime Report,” 25 The Hacker News, “Researchers find 341 malicious ClawHub
April 2026. https://www.ic3.gov/AnnualReport/Reports/ skills” (the “ClawHavoc” campaign against the OpenClaw agent
2025_IC3Report.pdf marketplace), February 2026. https://thehackernews.com/2026/02/
7 European Commission, “AI Act — Shaping Europe's digital future”: researchers-find-341-malicious-clawhub.html
application timeline. https://digital-strategy.ec.europa.eu/en/policies/ 26 Microsoft Security Blog, “Prompts become shells: RCE vulnerabilities in
regulatory-framework-ai AI agent frameworks” (CVE-2026-25592, CVE-2026-26030 in
8 World Economic Forum, in collaboration with Accenture, “Global Semantic Kernel), May 2026. https://www.microsoft.com/en-us/
Cybersecurity Outlook 2025,” January 2025. https:// security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-
www.weforum.org/publications/global-cybersecurity-outlook-2025/ ai-agent-frameworks/
9 OWASP GenAI Security Project, “OWASP Top 10 for LLM Applications 27 HiddenLayer, “AI Threat Landscape Report 2025,” March 2025. Survey
2025,” November 2024. https://genai.owasp.org/resource/owasp- of 250 IT leaders. https://www.hiddenlayer.com/news/hiddenlayer-ai-
top-10-for-llm-applications-2025/ threat-landscape-report-reveals-ai-breaches-on-the-rise
10 Aim Security, “EchoLeak (CVE-2025-32711): Zero-click data 28 KnowBe4, “Phishing Threat Trends Report,” March 2025; and
exfiltration in Microsoft 365 Copilot,” June 2025. https:// “KnowBe4 Research Finds 86% of Phishing Attacks Are AI-Driven,”
www.aim.security/lp/aim-labs-echoleak-blogpost April 2026. https://www.knowbe4.com/press/knowbe4-research-
finds-86-of-phishing-attacks-are-ai-driven
11 Invariant Labs, “GitHub MCP exploited: Accessing private repositories
via MCP,” May 2025. https://invariantlabs.ai/blog/mcp-github- 29 Google Threat Intelligence Group, “Threat actor usage of AI tools” —
vulnerability PROMPTFLUX and PROMPTSTEAL malware calling LLMs mid-
execution, November 2025. https://cloud.google.com/blog/topics/
12 Radware, “ShadowLeak: Zero-click service-side data exfiltration in
threat-intelligence/threat-actor-usage-of-ai-tools
ChatGPT's Deep Research agent,” September 2025. https://
www.radware.com/blog/threat-intelligence/shadowleak/ 30 Gartner, “Gartner Predicts 40% of Enterprise Apps Will Feature Task-
Specific AI Agents by 2026,” press release, August 26, 2025. https://
13 Anthropic, “Disrupting the first reported AI-orchestrated cyber
www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-
espionage campaign,” November 2025. https://www.anthropic.com/
predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-
news/disrupting-AI-espionage
agents-by-2026-up-from-less-than-5-percent-in-2025
14 Entrust Cybersecurity Institute, “2025 Identity Fraud Report,”
31 Gartner, “Gartner Predicts 25% of All Enterprise GenAI Applications Will
November 2024. https://www.entrust.com/company/newsroom/
Experience At Least Five Minor Security Incidents Per Year by 2028,”
deepfake-attacks-strike-every-five-minutes-amid-244-surge-in-
press release, April 9, 2026. https://www.gartner.com/en/newsroom/
digital-document-forgeries
press-releases/2026-04-09-gartner-predicts-25-percent-of-all-
15 Stanford Institute for Human-Centered AI, “AI Index Report 2025,”
enterprise-gen-ai-applicati

---

ons-will-experience-at-least-five-minor-
April 2025. https://hai.stanford.edu/ai-index/2025-ai-index-report
security-incidents-per-year-by-2028
16 Bloomberg, “Samsung bans staff's AI use after spotting ChatGPT data
32 Gartner, “Gartner Predicts Over 40% of Agentic AI Projects Will Be
leak,” May 2023. https://www.bloomberg.com/news/articles/
Canceled by End of 2027,” press release, June 25, 2025. https://
2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-
www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-
staff-after-leak
predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-
17 OpenAI, “March 20 ChatGPT outage: Here's what happened,” March end-of-2027
2023. https://openai.com/index/march-20-chatgpt-outage/
33 OrcaRouter security architecture documentation: threat model, control
18 Greshake, K., et al., “Not what you've signed up for: Compromising stack, guardrails, agent firewall, MCP governance, and compliance
real-world LLM-integrated applications with indirect prompt injection,” packs. https://docs.orcarouter.ai/security
February 2023. https://arxiv.org/abs/2302.12173
34 Sysdig Threat Research, “LLMjacking: Stolen cloud credentials used in
19 British Columbia Civil Resolution Tribunal, Moffatt v. Air Canada, new AI attack,” May 2024. https://www.sysdig.com/blog/llmjacking-
February 2024. https://decisions.civilresolutionbc.ca/crt/crtd/en/item/ stolen-cloud-credentials-used-in-new-ai-attack
525448/index.do
The AI Threat Report 2026 OrcaRouter Security Research · 32

35 JFrog Security Research, “Data scientists targeted by malicious 38 Willison, S., “The lethal trifecta for AI agents: private data, untrusted
Hugging Face ML models with silent backdoor,” February 2024. https:/ content, and external communication,” June 2025. https://
/jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face- simonwillison.net/2025/Jun/16/the-lethal-trifecta/
ml-models-with-silent-backdoor/ 39 Anthropic, “Donating the Model Context Protocol and establishing the
36 Pillar Security, “New vulnerability in GitHub Copilot and Cursor: How Agentic AI Foundation,” December 2025. https://www.anthropic.com/
hackers can weaponize code agents” (Rules File Backdoor), March news/donating-the-model-context-protocol-and-establishing-of-the-
2025. https://www.pillar.security/blog/new-vulnerability-in-github- agentic-ai-foundation
copilot-and-cursor-how-hackers-can-weaponize-code-agents 40 ISO/IEC 42001:2023, “Information technology — Artificial intelligence
37 NIST, “Artificial Intelligence Risk Management Framework: Generative — Management system,” December 2023. https://www.iso.org/
Artificial Intelligence Profile” (NIST-AI-600-1), July 2024. https:// standard/42001
nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
The AI Threat Report 2026 OrcaRouter Security Research · 33

ABOUT
About OrcaRouter Security Research
OrcaRouter Security Research is the security team behind OrcaRouter, the AI gateway by Continuum AI Corp. The
team maintains a public threat library covering fourteen AI threat classes, and builds the guardrail, firewall, and audit
controls that enforce against them in production — documented at docs.orcarouter.ai/security.
OrcaRouter routes OpenAI-, Anthropic-, and Gemini-compatible traffic across frontier model providers with zero-
markup pass-through pricing, and applies workspace-scoped security — scoped keys, input/output guardrails, an
agent firewall, MCP governance, anomaly detection, and signed compliance reporting — to every request, with no
agent code changes.
research@orcarouter.ai · www.orcarouter.ai
© 2026 Continuum AI Corp. This report is provided for general informational purposes only. It does not constitute legal, regulatory, or security advice, and
statements regarding legal frameworks (including the EU AI Act) are indicative summaries, not legal interpretation. Statistics attributed to third parties
remain the property of their publishers; readers should consult the original sources before relying on them. “Illustrative” exhibits encode analytical
judgment, not measured data.
The AI Threat Report 2026 OrcaRouter Security Research · 34

OrcaRouter
The AI Threat Report 2026 · OrcaRouter Security Research
www.orcarouter.ai

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
