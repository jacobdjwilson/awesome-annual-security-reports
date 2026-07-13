looking for when they ask for an audit trail. If you cannot prove that the agent’s access was constrained by the human’s original permissions, you have not met the requirement.

Audit trail collapse is the compliance risk

The EU AI Act’s Article 12 is the most specific regulatory requirement for this. It requires record-keeping that lets an operator reconstruct what the system did, with what inputs. If the audit trail breaks at the first service call, you cannot reconstruct the chain.

The risk is not just that an agent does something wrong. The risk is that you cannot prove to a regulator that it did not. In a 2026-era audit, "we don't know what the agent did" is a finding. "We can't reconstruct the delegation chain" is a finding. "The agent's permissions were not scoped by the user's" is a finding.

What CISOs should be asking vendors right now

When you talk to vendors about their AI agent support, the questions should be about the authorization layer, not the AI layer.

1. "Does your agent support token exchange for every hop in the chain?"
2. "Can your authorization layer evaluate policy against the full delegation chain, not just the immediate caller?"
3. "Does your decision log capture the full chain of identities and intents for every request?"
4. "Can you demonstrate a policy that restricts an agent's access based on the human user's context?"

If the answer to any of these is "we'll get back to you," you are looking at a gap in your authorization maturity.

What changes in your maturity model

The model in Chapter 2 does not change, but the bar for Stage 4 does. To be at Stage 4 in 2026, you must be able to govern agents with the same rigor you govern humans.

- **Stage 1**: Agents are running with broad service account permissions. No visibility.
- **Stage 2**: Agents are documented in a spreadsheet. No enforcement.
- **Stage 3**: Agents are governed by a central policy, but the delegation chain is not fully preserved.
- **Stage 4**: Agents are governed by a central policy that evaluates the full delegation chain, logs every decision, and supports real-time context-based authorization.

This is the new standard for the CISO's benchmark. It is not about stopping agents. It is about making them visible, auditable, and governable.

46

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

Chapter 8

A 30, 60, and 90 day plan

47

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

You have a vocabulary for your maturity, a map of your risks, and a set of outcomes to aim for. The final step is the plan. This is not a multi-year transformation. It is a ninety-day sprint to establish the foundation of a governed authorization program.

The first thirty days are about establishing visibility

Your goal is to answer the questions in Chapter 3 honestly.

- **Week 1-2**: Audit your current authorization state. Map where decisions are made (code, middleware, API gateways). Identify the "shadow" authorization logic that lives in undocumented code paths.
- **Week 3-4**: Document the current "as-is" state. Do not try to fix it yet. Just map it. Identify the top three high-risk services where authorization is most fragmented or least understood.

Days thirty-one to sixty are about picking the layer

Your goal is to move from "reconstruction" to "production."

- **Week 5-6**: Select your central authorization layer. This could be an open-source framework, a commercial platform, or a custom-built service. The key is that it must be separable from your application code.
- **Week 7-8**: Pilot the layer on one of your high-risk services. Move the authorization logic out of the code and into the central layer. Test the policy-as-code workflow.

Days sixty-one to ninety are about proving the approach and committing to the program

Your goal is to demonstrate the value to the business and the board.

- **Week 9-10**: Measure the results. Compare the time-to-revoke and audit-readiness of the pilot service against the baseline.
- **Week 11-12**: Present the findings to the board. Show them the "before" and "after" metrics. Secure the commitment for the next phase of the program.

48

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

Close the gap with Cerbos

Cerbos is the authorization layer for the modern stack. It is designed to help you move from Stage 1 to Stage 4, providing the policy-as-code, the central decision point, and the audit trail you need to meet the requirements of 2026.

- **Policy-as-Code**: Write your policies in a human-readable language, version-controlled and tested like any other code.
- **Centralized Decision Point**: Decouple authorization from your application code, ensuring consistent enforcement across your entire estate.
- **Audit-Ready**: Generate a complete, tamper-proof decision log that provides the evidence you need for auditors and regulators.
- **Agent-Ready**: Support complex delegation chains and context-aware authorization for AI agents and non-human identities.

Visit [cerbos.dev](https://cerbos.dev) to learn more and start your journey to authorization maturity.

About this guide

This guide was written by the team at Cerbos, based on hundreds of conversations with security leaders, analysts, and regulators. It is intended to be a living document, updated as the landscape evolves. We welcome your feedback, your stories, and your contributions.

49

              Published by Ce

 rbos

---

starting to ask for,

and what most programs cannot yet produce.

The gap is not a tooling gap. Reiner Mertens made the case at EIC 2026 that the

standards are mature and the tools exist. What is missing is the organizational

positioning, whether IAM is actually in the room when APIs are designed.

Audit trail collapse is the compliance risk

The same point has been made from the audit side. Building on Kim Cameron's 2005

Laws of Identity, the conversation in 2026 has been about extending those principles

to agents. The one that matters most for CISOs is the principle of justifiable action.

Every agent action must be reconstructable end to end, from a record that names

the human principal, the agent and model version, the policy that authorized the call,

and the delegation scope.

Most production logs today capture four fields, a timestamp, an actor, an action, and

a target. That does not meet the bar, and a four-field log with a sub-agent chain

does not even tell you who delegated.

The reason this matters now is that the EU AI Act deadlines, even pushed to 2027 and

2028, leave less runway than they appear. Article 12 requires record-keeping that lets

an operator reconstruct what the system did and with what inputs. Article 13 requires

transparency to deployers about how the system works and its limits. The standard

your program has to meet, whichever regulator is asking, is that any agent action

across a rolling 30-day window can be reconstructed end to end, with the original

human consent and every delegation hop intact. That is the working definition of

audit-readiness for agents.

46

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

What CISOs should be asking vendors right now

The vendor conversation around agent authorization in 2026 is heavy on capability

claims and light on evidence. The most useful filter we have seen comes from

Jonathan Care at KuppingerCole. The eight questions below are paraphrased from

his framing. Each has a yes or no answer, and each is verifiable in a proof of concept.

A vendor that can answer yes to all eight, with artefacts, is operating at the Stage 4

standard from Chapter 2. A vendor that cannot is selling capability rather than

control.

47

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

What changes in your maturity model

Stage 4 for agents is the same Stage 4 from Chapter 2, applied. The policy model

covers human and non-human identities under one engine. Decisions are evaluated

continuously, not only at session start. Decisions carry the delegation chain, not only

the requesting identity. Decision logs are produced continuously and are queryable

across a window measured in days, not quarters.

The principle does not change. The bar moves up, because the regulator's

expectations and the attacker's capabilities have both moved up.

Programs that did the work to reach Stage 3 for human identities have done most of

the architectural work to reach Stage 4 for agents. What remains, in order, is identity

registration per instance, scoped short-lived credentials, per-hop authorization, and

an audit record that survives delegation. The rest is policy.

None of this changes the plan in the next chapter. It raises the stakes on doing it.

48

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

Chapter 8

A 30, 60, and 90 day plan

49

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

The chapters above describe the shape of the whole model. This one is narrower. If

you are at Stage 2 today, which most CISOs reading this guide will be, this is a 90-

day view of the first visible part of the transition to Stage 3. Ninety days is not enough

to finish the transition. It is enough to establish visibility, pick the architectural

direction, and put the first credible metric in front of the executive team. The rest of

the work follows if the first part is done with intent.

The first thirty days are about establishing visibility

The first action is to name an owner for the authorization program. Not a team, a

person, someone who will be asked about it in twelve months and answer without

deflecting.

The second action is to produce a one-page honest assessment of where every

production service sits on this maturity model. Not a policy document, an honest

map. Do not stop the exercise at "it varies." Vary against what?

50

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

The third action is to pick the five services handling the most sensitive data in your

environment and document, for each, what actually enforces authorization, who

owns it, and what evidence of that enforcement exists today.

The fourth action is to brief the executive team on the current stage, without

softening it. That briefing is the thing that unlocks budget for the next sixty days.

Soften it and you will spend the next sixty days without budget.

A fifth action belongs alongside the first four if your organization has any agents in

production today, and the honest answer to that is almost always yes. Produce a

complete inventory of every AI agent and autonomous workload running in

production, with a named human owner, the credentials it holds, the systems it can

reach, and the data classification of those systems. Most programs find the

inventory cannot be assembled from any single source of truth. That fact, on a slide

for the executive team, unlocks budget for the next sixty days more reliably than

anything else in this plan.

Days thirty-one to sixty are about picking the layer

The main decision in this window is architectural. You are choosing a policy decision

point approach, whether open source, commercial, or internally built, and you are

doing so knowing it stays with you for years.

A second decision follows from the first, which is the policy language. A YAML-plus-

expression-language approach like Cerbos is more maintainable than Rego for

most teams, but the right answer depends on the shape of your engineering

organization, the frameworks you want to align with, and whether you are

committing to AuthZEN as the standard.

Alongside the architectural decision, pilot the new layer with one of the five services

from month one. Measure latency, evidence quality, and developer adoption as a

trio rather than in isolation. The pilot will tell you more about the operating model

than about the technology. That is useful information to get early. In parallel, align

with the IAM team on how admin-time policy and runtime policy will meet cleanly.

51

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

That conversation is the one most commonly skipped and most commonly

regretted.

In parallel with the architectural decision, agree the agent identity model the

program will commit to. One identity per agent instance rather than per agent class.

Scoped credentials with a defined lifetime measured in hours, not days. Delegation

chain captured in the token, not in tribal knowledge. Decision log that records the

human principal as well as the agent. The pilot service should include at least one

agent-mediated code path, so the operating model is tested against the harder

case from the start rather than against the easier one only.

Days sixty-one to ninety are about proving the

approach and committing to the program

Roll the pilot to two more services. Confirm that the policy repository, the test suite,

and the decision log are producing the artefacts you need them to produce, and

that the evidence they produce is legible to the auditors you care about.

Produce the first board-level authorization posture slide, with real numbers for time-

to-revoke, policy coverage, and exposure duration, even if the numbers are ugly. The

board slide should include agent identity coverage as a number separate from

human identity coverage, with the explicit acknowledgement that the agent number

will lag and will move in both directions as engineering ships and retires agents. Ugly

numbers you can move are more valuable than clean narratives you cannot.

Commit to a Stage 2-to-3 roadmap with a named end date, budget, and a metric

on the executive dashboard.

52

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

Nobody gets from Stage 2 to Stage 3 in ninety days. Most get the first 15% of the

way, and that is the part that matters. The rest is a two-to-four quarter program

that runs on the scaffolding the first ninety days put in place.

The organizations that skip the scaffolding spend twelve months on an

implementation project and then discover they have a decision point but no

program.

The organizations that invest in the scaffolding end up with a program the CISO can

stand behind in an audit committee meeting, which is the point of the exercise.

That is the work. The rest of this is how we can help.

53

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

Close the gap with Cerbos

Wherever the self-assessment in Chapter 3 placed you, the next move points the

same way, out of code and into a layer you can govern. Cerbos is built for that move,

through to the Stage 4 capabilities this guide points toward, agents, delegation, and

continuous decisions included.

Cerbos is an externalized authorization management platform. You authorize every

identity and govern every action from one place, with fine-grained, contextual, and

continuous decisions and a full audit trail behind every one, across your applications,

gateways, workloads, and AI agents.

Policies are written as code, reviewed and tested like any other code, and distributed

across your services through a single interface, so your audit evidence is produced

continuously rather than reconstructed at audit time.

Human and non-human identities run through the same policy model, so the

fastest-growing part of your estate sits inside the program, not outside it.

Cerbos has been part of the OpenID AuthZEN working group from the start and aligns

with the now-ratified standard, adopting it is not a lock-in decision.

If that sounds like the conversation your program needs to have in the next two

quarters, we would like to have it with you.

Talk to a Cerbos solutions architect about where your authorization program sits

today and how to close the gap.

Book a call.

54

              Published by Ce

 rbos

The Authorization Maturity Model: A CISO's Benchmark for 2026

About this guide

This guide was produced by Cerbos based on conversations with security leaders

across regulated industries including fintech, healthcare, and government, as well as

B2B SaaS, and on the published work of Phillip Messerschmidt, Reiner Mertens, and

Jonathan Care at KuppingerCole, of Kara Sprague at HackerOne, on peer

contributions to the Cloud Security Alliance CISO Mythos draft, and on the recaps of

the leading IAM and security analyst events.

Lead Author:
Alex Olivier

Contributors:
Emre Baran

Anna Paykina

55

              Published by Ce

 rbos