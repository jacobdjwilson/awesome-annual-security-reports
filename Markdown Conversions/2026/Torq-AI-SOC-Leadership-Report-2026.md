# The 2026 AI SOC Leadership Report

**Organization**: Torq  
**Report Title**: AI-SOC-Leadership-Report  
**Year**: 2026

## Table of Contents
- [Executive Foreword](#executive-foreword)
- [Introduction](#introduction)
- [Key Takeaways](#key-takeaways)
- [Research Findings](#research-findings)
  - [The AI Adoption Landscape](#the-ai-adoption-landscape)
  - [AI Across the Alert Lifecycle](#ai-across-the-alert-lifecycle)
  - [The Evolving Role of the SOC Analyst](#the-evolving-role-of-the-soc-analyst)
  - [The Barriers to AI Expansion](#the-barriers-to-ai-expansion)
  - [The Path to the AI SOC](#the-path-to-the-ai-soc)
- [Concluding Thoughts](#concluding-thoughts)
- [Demographics & Methodology](#demographics-methodology)
- [About Torq](#about-torq)

---

## Executive Foreword

When my co-founders Leonid, Eldad, and I started Torq in 2020, we had a simple conviction: the SOC was broken, and automation was the way to fix it. Not automation as a feature bolted onto legacy tools, but automation as the foundation — the starting point for how security operations should work.

Five years later, the industry has caught up to that belief. AI is everywhere in the SOC. Nearly every organization we talk to is using it in some form. But what we’re hearing from security leaders — and what this report confirms — is that more AI hasn’t meant better security operations. In many cases, it’s meant more tools, more complexity, and more time spent managing the AI itself.

That’s not the future any of us signed up for.

We commissioned this research because we believe the industry is at a turning point. The first wave of AI in the SOC was about adoption — getting AI into workflows wherever possible. The next wave will be about architecture — building platforms that unify, explain, and adapt, so that analysts can focus on what they do best: making decisions that matter.

The findings in this report reflect what we hear every day from the CISOs and SOC leaders we work with. They’re not asking for more AI. They’re asking for AI that works together, shows its reasoning, and gives them control over where it runs and where humans stay in the loop.

That’s exactly what we’re building at Torq. But this report isn’t about us — it’s about the state of the industry as told by the people living it. I hope the data challenges some assumptions, validates some instincts, and helps security leaders make the case for what their SOC should look like next.

**Ofer Smadari**  
Co-Founder & CEO, Torq

## Introduction

The industry is racing to embed AI into every corner of the SOC. Generative AI. Large language models. Vendor-built copilots. Agentic workflows. Custom agents. The tools have multiplied. The dashboards have multiplied. The alerts have multiplied. And somewhere along the way, the complexity AI was supposed to eliminate started compounding instead.

SOC analysts today aren’t just investigating threats; they’re managing a growing number of AI-powered tools, each with its own logic, interface, and version of the truth. They’re spending hours not on adversary tradecraft, but on validating whether the AI got it right. They’re confident that AI can help. They’re less confident that the AI they have is helping.

> The tension at the heart of modern security operations is whether the current approach to AI in the SOC is making teams faster, sharper, and more resilient… or whether it’s creating a new kind of operational drag: more noise dressed up as insight, more tools stitched together with hope, more output that looks intelligent but doesn’t move the needle.

The answer, as this report shows, is somewhere in between — and the gap between the two is where the opportunity lives.

Security leaders know this. They can describe the ideal AI SOC with remarkable consistency: unified, transparent, adaptive, and built to let teams decide where AI acts autonomously and where humans stay in the loop. Most just haven’t gotten there yet. The intent is mature. The architecture isn’t.

### WHAT THIS REPORT COVERS

Sapio Research on behalf of Torq surveyed 450 CISOs and security leaders at enterprise organizations with 1,000+ employees to examine the state of AI in security operations… not the aspirational version, but the operational reality.

Where is AI actually being used across the alert lifecycle?

Where are teams confident, and where are they holding back?

What’s working, what’s creating friction, and what would it take for security leaders to trust AI enough to let it run?

The findings are organized around five themes that surfaced consistently across geographies, company sizes, and seniority levels — from tool fragmentation and barriers to trust, to the evolution of the analyst role and the demand for a fundamentally different platform.

This report maps where the industry stands today, where security leaders want to go, and what’s standing in the way.

## Key Takeaways

### Key Takeaways

#### 01 AI IS EVERYWHERE IN THE SOC — BUT UNIFIED NOWHERE

**7** AI solutions per SOC on average  
**80%** rely on fragmented point tools

Teams are running 7 AI tools on average, but 80% depend on disconnected point solutions. 85% say they’d prefer consolidation. Adoption has outpaced architecture.

#### 02 AI IS CARRYING THE LOAD; ANALYSTS ARE MAKING THE CALLS

**72%** are comfortable with fully autonomous AI on medium-severity and below  
**9 in 10** say they need explainability to go further

Nearly three-quarters of teams are already letting AI carry the weight on the alerts that dominate SOC volume. Analysts aren’t being replaced; they’re being freed up for the work that actually needs them. To go further, 90% say they need to see how AI reaches its decisions before they can trust it.

#### 03 THE ANALYST ROLE IS EVOLVING

**8.6** hours/week on AI oversight  
**9 in 10** say AI has positively impacted SOC workload

Those oversight hours aren’t busywork — they signal a shift from execution to judgment. AI handles the processing; analysts make the calls that matter.

#### 04 TRUST IS THE CEILING ON AI EXPANSION

**92%** cite at least one factor that reduces their trust in AI within the SOC  
**46%** say transparency would change that

Only 8% of security leaders have zero concerns about AI trust. The rest point to data privacy, false negatives, and black-box decisions — and say the #1 thing that would unlock more AI is simply being able to see how it reaches its conclusions.

#### 05 THE MARKET KNOWS WHAT IT WANTS

**85%** would prefer a unified AI SOC platform over multiple point solutions  
**92%** want AI that learns and adapts

Unified. Explainable. Adaptive. The desired end state of the AI SOC is consistent across every seniority level, company size, and geography.

## Research Findings

### Research Findings

### The AI Adoption Landscape

#### EVERYONE HAS AI. NOT EVERYONE HAS A STRATEGY.

Where AI Stands Today

Nearly 4 in 5 organizations (79%) have adopted AI within their security operations, and more than a third (37%) have embedded it widely across tools and processes. The UK leads in broad deployment at 48%, while other markets show strong but less uniform penetration.

- 79% use AI in at least one SOC function
- 37% have built it into SOC workflows
- 48% have adopted AI widely

But adoption alone tells us very little about effectiveness. What matters is what kind of AI organizations are running, how it’s architected, and whether it plays well with the rest of the stack.

Generative AI (76%) and LLMs (73%) remain the most widely deployed, but more advanced approaches are gaining traction: 56% are using agentic AI, and nearly half are running custom AI agents (49%) or vendor-built agents (45%).

![Chart showing AI Types in Use Across the SOC, including Generative AI (79%), LLMs (73%), Agentic AI (56%), Custom AI Agents (49%), Vendor AI Agents (45%), and Custom LLMs (33%).](AI_TYPES_IN_USE_ACROSS_THE_SOC)

This layering is significant. Many of the challenges that surface later in this report — excessive oversight, unreliable outputs, limited trust in automated actions — stem from organizations that are still primarily relying on Gen AI and LLMs alone.

These are powerful capabilities, but they represent first-generation AI in the SOC: high output volume, lower operational precision. The teams that have moved into agentic AI and custom agents are beginning to see a different kind of value: AI that doesn’t just summarize, but acts with context.

#### Geographic Insight

Regional divergence goes beyond Gen AI vs. LLMs. The UK leads in agentic AI adoption (63%), while the U.S. — despite being the largest market — is the most conservative on advanced AI approaches, trailing on agentic AI (53%), custom agents (45%), and vendor agents (42%). Germany stands out with the highest vendor AI agent adoption by far (74%), while France takes the opposite approach, favoring custom-built agents at just 25%. A platform that only supports one AI strategy doesn’t work when markets are moving in different directions.

#### The Platform Landscape

Almost half of the respondents believe that AI-native platforms built from the ground up deliver better AI SOC outcomes than traditional SOAR with AI features bolted on. This preference weakens among smaller SOC teams (≤15 members), where 30% still default to traditional SOAR, suggesting that resource constraints drive platform conservatism. Smaller teams buy what’s familiar because they don’t have the bandwidth to migrate.

The organizations that need to unify their security tools the most are the least likely to pursue it. The answer isn’t a rip-and-replace; it’s a platform that integrates with what they already have and lets them consolidate at their own pace.

### AI Across the Alert Lifecycle

#### THERE’S A GAP BETWEEN WHERE AI IS USED AND WHERE IT’S TRUSTED.

Of those who have adopted AI within the SOC, almost all use AI for at least one SecOps use case. But the gap between where they’re confident and where they’ve actually deployed reveals a critical story about platform readiness.

![Chart showing Use Case Adoption vs. Confidence. Use cases include Vulnerability Management (56% using AI, 91% confident), Threat Hunting (56% using AI, 94% confident), Case Management (54% using AI, 95% confident), Reducing False Positives (51% using AI, 97% confident), Investigation / Enrichment (46% using AI, 93% confident), Remediation (37% using AI, 95% confident), Containment (37% using AI, 92% confident), and Triage (prioritization) (35% using AI, 97% confident).](Use_Case_Adoption_vs_Confidence)

It’s no coincidence that vulnerability management (VM) and threat hunting top the use case list (both 56%). VM has been synonymous with operational pain for over a decade — exploitation is increasingly automated while patching remains manual, creating a window of exposure tailor-made for AI. Threat hunting faces a different pressure: the talent pool is scarce and expensive, and AI extends the reach of a limited bench.

The bottom of the list is just as telling: remediation (37%), containment (37%), and triage at just 35%. These are where a wrong call has immediate consequences — and where confidence and usage diverge most sharply. Meanwhile, confidence is near-universal. The numbers stay above 91% across every use case.

**97%** of security leaders believe AI can handle triage — the highest-volume function in the SOC, but only 35% are actually using it to do so. Why? Teams are comfortable letting AI discover and analyze. They’re cautious about letting it act.

Most tools today offer a binary: AI runs or human runs. What teams need is a dial. Autonomy calibrated to severity, confidence, and business context. Low-severity, high-confidence? AI handles it end-to-end. High-severity, critical system? AI does the legwork, humans make the call.

#### AUTONOMY COMFORT LEVELS

When it comes to letting AI act independently, most organizations proceed with caution. The data shows a clear severity threshold beyond which human involvement becomes non-negotiable.

- **20%** Critical / High & below (Highest risk threshold)
- **72%** Medium & below (Where most draw the line)
- **93%** Low & below (Conservative threshold)
- **97%** Any level (Including info-only)

97% of security leaders are comfortable with some level of fully autonomous AI. Only 3% want human approval on every action. For the rest, the question is where they draw the line.

Most draw it at medium severity, and the reasons are as much organizational as technical. Critical and high-severity incidents carry the strictest SLAs and the most executive visibility. When a vulnerability hits the news, the instinct is to put your best people on it. It’s not that AI can’t help — it’s that the pressure to show senior leadership that trusted humans are on the problem outweighs the efficiency case for automation.

Meanwhile, medium-severity vulnerabilities are actually exploited more often than critical and high vulnerabilities combined (IBM Research). The alerts getting the most human attention aren’t necessarily the ones carrying the most real-world risk.

Experience doesn’t change this. You’d expect teams that use AI daily to be more willing to let it handle higher-severity incidents. They aren’t. Their autonomy comfort levels are virtually identical to teams that don’t use AI at all. And neither does automation ambition. Teams that want more than half of daily security tasks automated are nearly twice as likely to grant AI autonomy on critical incidents (25% vs 15%) — but even they won’t cross the medium-severity line three-quarters of the time.

The barrier isn’t trust, experience, or appetite. It’s the absence of platform controls that lets teams move the line with confidence. Without built-in guardrails, organizations set their own — by keeping humans on the highest-severity work regardless of whether AI could accelerate it. Not because AI isn’t capable, but because the tools don’t give teams a way to gradually extend autonomy as confidence grows.

The solution isn’t convincing leaders to let go. It’s giving them platforms where autonomy is adjustable — calibrated to severity, confidence, and context — so decisions are based on actual risk, not organizational reflex.

### The Evolving Role of the SOC Analyst

#### AI ISN’T REPLACING ANALYSTS. IT’S PROMOTING THEM.

**8.6** hours per week is the time that analysts spend on human oversight of AI-powered outputs.

On the surface, this can look like a problem: nearly a full workday consumed by checking the AI’s work? Not quite. The data tells a more nuanced story.

- **9 in 10** leaders say AI has positively impacted SOC workload
- **9 in 10** leaders say AI has reduced stress and burnout

What’s actually happening? Before AI, analysts were the execution layer — processing alerts, enriching data, running playbooks. AI has taken over much of that. The 8.6 hours represent a new judgment layer: validating decisions, providing context, and making calls that require institutional knowledge and human intuition.

But it only works if the platform makes judgment efficient. Hours spent digging through opaque AI outputs? Wasted time. Hours spent reviewing clear, explainable reasoning and approving or overriding with full context? Strategic time. The difference is platform design.

The best platforms won’t eliminate AI oversight; they’ll make it effortless. Transparent reasoning so analysts validate in seconds. Adjustable autonomy so teams reduce oversight where AI has proven itself: a feedback loop where overrides improve AI over time.

#### AI OVERSIGHT HOURS SCALE WITH TEAM SIZE

![Chart showing AI Oversight Hours Scale with Team Size: SOC teams of 15 or fewer spend 7.7 hours, SOC teams of 16 to 35 spend 8.5 hours, and SOC teams of 35 or more spend 9.4 hours.](AI_OVERSIGHT_HOURS_SCALE_WITH_TEAM_SIZE)

Larger teams spend more hours on oversight — likely due to more complex AI systems and a larger tool stack. This reinforces the idea that oversight isn’t a failure; it’s a function of how deeply AI is embedded in operations.

The question for organizations isn’t “how do we reduce oversight hours?” It’s “how do we ensure those hours are strategic?” This evolution will only accelerate as AI capabilities expand.

#### What Analysts Want from AI

Respondents were clear about what would make daily SOC work easier: anything that improves quality of life. And when asked about the expected benefits of agentic AI in SecOps, the same theme came out on top — suggesting strong alignment between pain points and promise.

![Chart showing Top Improvements to Daily SOC Life: 1. Work-life balance and flexible scheduling, 2. Fewer repetitive or manual tasks, 3. Workload distribution and prioritization.](Top_Improvements_to_Daily_SOC_Life)

![Chart showing Top Expected Benefits of AI in the SOC: 1. Improved quality of life and reduced burnout, 2. Greater SOC capacity — alert disposition and remediation within SLA, 3. Reduction in mean-time-to-respond (MTTR).](Top_Expected_Benefits_of_AI_in_the_SOC)

### The Barriers to AI Expansion

#### THE SOC TRUSTS AI IN THEORY. IN PRACTICE, IT’S COMPLICATED.

Despite high confidence in AI’s capabilities, 92% of security leaders say factors are actively eroding their trust in AI use in the SOC. And the barriers are not about whether AI works; they’re about visibility, control, and governance.

![Chart showing What’s Reducing Trust (Top 5 Concerns): 1. Data privacy (32%), 2. Risk of false negatives or missed threats (29%), 3. Risk of false positives, 4. Loss of control over AI-driven decisions or actions, 5. Requires too much manual human oversight.](Whats_Reducing_Trust)

![Chart showing What Would Build Confidence: 1. Full transparency into AI decision-making (46%), 2. Strong data privacy protections (41%), 3. Data governance, 4. Regulatory compliance certifications, 5. Human-in-the-loop controls.](What_Would_Build_Confidence)

Each trust barrier directly translates into operational drag: more manual oversight, reduced autonomy, and limited data access. And the #1 confidence booster isn’t more features or more AI — it’s transparency. 90% say explainable AI decisions are important for a true AI SOC.

The through-line is clear. Privacy concerns go away when the platform governs what data AI sees. False-negative fears resolve when the platform explains why it dismissed an alert. Black-box anxiety is alleviated by AI that shows its work.

#### FUNCTIONAL CAPABILITY GAPS

- **37%** Requires too much manual human oversight
- **36%** Patchwork of multiple tools

These are connected — when tools operate in silos, analysts oversee AI on a per-tool basis, not per incident. The issue isn’t that oversight is needed. It’s that platforms don’t let teams control it.

Teams need oversight policies that match reality: full autonomy for high-frequency, low-risk alerts; human-in-the-loop for novel or critical incidents; and the ability to dial up or down as confidence grows.

#### Seniority Lens: Top Concern by Level

![Chart showing Top Concern by Seniority Level: C-Level's top concern is False Negatives (Are threats slipping through?), VP / Head of Dept + Sr. Managers' top concern is Data Privacy (How is AI handling sensitive information?), and Director's top concern is AI Tools Underdelivering (Are AI tools failing to deliver measurable impact?). Other top concerns were black-box AI (Why can’t we see how decisions are made?) and loss of control (Who’s actually running the SOC?).](Seniority_Lens_Top_Concern_by_Level)

A well-designed AI SOC addresses all of these concerns simultaneously because they’re features of the same architecture.

#### Challenges by SOC Function

**Alert Triage**  
9 in 10 report challenges using AI due to:
- Skills/training gaps (34%)
- Too much human review (34%)
- Unreliable conclusions (31%)

**Investigation & Case Management**  
9 in 10 report challenges using AI due to:
- Manual enrichment required (32%)
- High false positives (31%)
- Skills/training gaps (29%)

For response actions, almost all organizations report challenges. One-third cite limited trust in automated responses — the direct consequence of opaque reasoning and the inability to set contextual boundaries.

#### Team Size Dynamics

- **44%** Small teams (less than 15) say false positives reduce trust in AI
- **28%** Large teams (35+) say false positives reduce trust in AI

This perception gap is less about trust and more about capacity. Lean teams can’t absorb the friction of false positives — making adjustable autonomy not a nice-to-have, but how they stay operational.

### The Path to the AI SOC

#### WHAT SECURITY LEADERS ACTUALLY WANT — AND HOW FAR THEY ARE FROM GETTING IT.

Every finding in this report converges on one conclusion: the market isn’t asking for more AI. It’s asking for better-architected AI.

- **80%** Rely on multiple point-specific tools
- **80%** Say this creates operational complexity
- **85%** Would prefer a unified platform

8 out of 10 security leaders rely on multiple-point tools, say that doing so creates operational complexity, and would prefer a unified platform. Yet the AI tools keep accumulating, and nothing ties them together.

The answer isn’t a rip-and-replace. SIEMs, EDRs, ITDR, CNAPP — they solve real problems, and they do what they do well. The gap is twofold: nothing orchestrates across them, and no single layer sees all the data. Each tool holds a piece of the picture — a slice of telemetry, a fragment of context, a partial view of risk. Analysts become the integration layer, manually stitching together partial truths from multiple sources to assemble something close to a complete understanding.

What 85% of security leaders want isn’t one tool that does everything. It’s one platform that connects to everything, sees across the full stack, and turns fragmented signals into unified context, reasoning, and action.

#### WHAT A TRUE AI SOC WOULD RESOLVE

![Chart showing what a true AI SOC would resolve: Trust in AI recommendations and actions (53%) and Complexity of managing multiple point solutions (48%).](WHAT_A_TRUE_AI_SOC_WOULD_RESOLVE)

Teams believe unification would increase their trust in AI because AI operating across the full incident context produces better-informed conclusions, easier-to-verify reasoning, and higher-confidence recommendations.

#### What Matters Most in a True AI SOC

![Chart showing what matters most in a true AI SOC: Continuous learning & adaptation to attack patterns (92%), Explainable AI decisions (90%), End-to-end SecOps: triage to remediation (89%), Autonomous response actions (e.g., containment, remediation) (89%), Full platform integration (86%).](What_Matters_Most_in_a_True_AI_SOC)

Security leaders are looking for a platform that covers the full alert lifecycle in a single integrated flow, explains its decisions, learns and adapts, integrates with the existing stack, and lets teams set the terms of AI’s involvement based on risk tolerance, operational context, and evolving confidence.

#### Automation Appetite

- **51%** of daily tasks automated
- **48%** want more than half of tasks automated

Organizations with higher automation ambitions are also more likely to have deployed AI widely (48%) — suggesting that those who’ve invested deeply understand both the potential and the current limitations.

#### Looking Ahead: Expansion Plans (Next 12 Months)

- **40%** Plan to expand AI in cloud security
- **28%** Plan to expand in incident response automation

The organizations that move from fragmented tools to unified, AI-native platforms will be the ones that unlock the efficiency, trust, and autonomy the rest of the industry is still chasing.

## Concluding Thoughts

### Concluding Thoughts

### 3 GAPS HOLDING AI IN THE SOC BACK

The SOC has crossed the AI adoption threshold. With 94% of organizations using AI and an average of 7 solutions per team, the question has shifted from “if” to “how well.” The data paints a picture of an industry that has embraced AI’s potential but hasn’t yet found the right architecture to deliver on it.

Three points emerged repeatedly across the data, and how organizations resolve them will determine whether AI becomes the force multiplier the SOC needs or another layer of complexity it has to manage.

#### CONFIDENCE VS. CONTROL

Leaders are confident in AI across every major use case — but most won’t let it act autonomously beyond medium-severity incidents. The barrier isn’t capability skepticism; it’s the absence of platforms that let teams calibrate autonomy to context. Organizations don’t want all-or-nothing automation. They want to decide where AI works independently and where humans stay in the loop — and adjust those boundaries as conditions change.

#### ADOPTION VS. ARCHITECTURE

AI adoption is near-universal, but it’s landed as a patchwork of disconnected tools. 80% of SOCs are managing multiple point solutions. As a result, operational complexity that offsets the efficiency gains AI was supposed to deliver. 85% want a unified platform — the industry has diagnosed the problem, but most haven’t solved it.

#### EXECUTION VS. JUDGMENT

The 8.6 hours analysts spend weekly on AI oversight isn’t a failure metric; it’s a signal that the analyst role is evolving. As AI handles more of the execution, analysts are shifting to judgment, validation, and strategic decision-making. But this shift only works if the platform supports it — with explainability, transparency, and the ability to dial oversight up or down.

### THE MARKET KNOWS WHAT IT WANTS

The desired end state is consistent across seniority levels, company sizes, and geographies: a unified, AI-native platform with continuous learning, explainable decisions, and end-to-end coverage from triage to remediation.

- **53%** Believe a fully integrated AI SOC would resolve their AI trust issues
- **90%** Say explainability is critical
- **85%** Want unification

The market isn’t uncertain about what it wants. It’s waiting for the platform that delivers it.

These are the problems we think about every day at Torq. When we built the Torq platform, we made a series of architectural bets based on what we were hearing from security leaders — the same things that showed up in this data.

We bet on integration over replacement — a platform that connects to whatever’s already in the stack rather than asking teams to rip it out. We bet on explainability as a core design principle, not an add-on — because the data is clear that transparency is what earns trust, and trust is what unlocks autonomy. We bet on adjustable control, letting teams decide how much oversight AI needs based on severity, confidence, and context, rather than forcing an all-or-nothing choice. And we bet on continuous learning, because the #1 capability security leaders want is AI that adapts over time.

We don’t pretend to have solved all of this. No one has. But the gap between where organizations are and where they want to be is closable, and the data in this report draws a pretty clear map of what “closed” looks like.

The organizations that get there first — moving from patchwork to platform, from opaque to explainable, from fixed automation to adjustable control — will be the ones that unlock what AI in the SOC was always supposed to deliver.

## APPENDIX

### Demographics & Methodology

This research was conducted by Sapio Research on behalf of Torq. The survey captured responses from more than 450 CISOs, security leaders, and senior security decision-makers across 4 countries.

![Chart showing Respondent Seniority: 27% Executive or C-level, 15% VP or Head of department, 32% Directors, 27% Senior managers.](Respondent_Seniority)

![Chart showing Organization Size: 34% 1,000 to 4,999 employees, 31% 5,000 to 9,999 employees, 16% 10,000 to 19,999 employees, 20% 20,000+ employees.](Organization_Size)

![Chart showing Top Industries: 20% IT / Software, 18% Banking / Finance, 13% Manufacturing.](Top_Industries)

![Chart showing Respondents by Country: 250 from the US, 100 from the UK, 50 from France, 50 from Germany.](Respondents_by_Country)

## SEE THE AI SOC IN ACTION

[Get a Demo](https://torq.io/demo)

### About Sapio Research

Sapio Research is a Certified B Corp™ full-service B2B and tech market research agency that helps businesses grow thanks to high quality, efficient and honest research solutions. Their team of expert researchers deliver valuable insights to support their clients understand their audience, build powerful brands, and cut through the noise with compelling data-driven content.

For more information, visit [sapioresearch.com](https://sapioresearch.com).

### About Torq

Torq is the enterprise AI SOC platform transforming how enterprises manage risk. Using adaptive agentic reasoning and automation, Torq identifies, prioritizes, and remediates critical threats at machine speed, slashing MTTI and MTTR while amplifying productivity. Global leaders like PepsiCo, Procter & Gamble, Siemens, Telefónica, and Virgin Atlantic trust Torq to power the next generation of AI-driven security operations.

For more information, visit [torq.io](https://torq.io).

Americas HQ  
205 Detroit Street  
Denver, CO, 80206  
[torq.io](https://torq.io)