Organization: Strike48  
Report Title: State-of-Agentic-Security-Report  
Year: 2026  

# The State of Agentic Security: Breaking Through the Trust Barrier

Insights from 100 security leaders on AI trust, implementation, and data visibility

## Table of Contents
- [Executive Summary](#executive-summary)
- [Who We Surveyed](#who-we-surveyed)
- [The Adoption Gap](#the-adoption-gap)
- [The Agent Trust Crisis](#the-agent-trust-crisis)
- [The Data Visibility Problem](#the-data-visibility-problem)
- [What This Tells Us](#what-this-tells-us)
- [How Strike48 Solves for Agent Visibility and Trust](#how-strike48-solves-for-agent-visibility-and-trust)

---

## Executive Summary

The gap between what security leaders want and what they’re willing to deploy is the defining tension of cybersecurity teams right now. 

Adversaries are already using agents. Defenders mostly aren’t.

The urgency around agentic security is no longer theoretical. Today, threat actors are moving at machine speed, adopting AI to dramatically shrink the time from vulnerability exposure to compromise. Frontier AI models are pushing what’s possible. Time to breakout is measured in minutes rather than hours or days. And yet, defenders are still moving at human speed.

The SANS Institute and the Cloud Security Alliance recently issued an emergency strategy briefing warning that defensive teams who have not adopted AI agents face "a widening capability gap against AI-augmented agentic adversaries... [and are] at a severe disadvantage against automated adversaries, regardless of their existing technical skill."

The recommended first-priority action: introduce AI agents to the cyber workforce to defend against adversaries.

We surveyed 100 security leaders across enterprise and mid-market organizations to understand how they were reacting to the very real shift in landscape. We wanted to hear from them directly on how they were moving into an agentic world, or what was holding them back.

There is a large gap between leaders wanting to implement agentic security and where they are today. The primary barrier to adoption? Trust.

Respondents overwhelmingly said that they couldn’t trust that the agent wouldn’t do something unintended or harmful (71%) or that the agent would hallucinate and provide wrong answers (69%).

Another major contributor to AI trust issues: data visibility.

84% of security leaders say their current tools cannot access all their log data for investigations. That lack of data visibility causes problems for investigations that AI agents alone can’t solve.

It is not all bad news for security teams however. The tools are improving, teams are running POCs (34%), and 36% of respondents have agents in deployment for at least one use case.

Read on for more data on the gap between plans for AI and adoption, AI trust, how lack of data visibility impacts both trust and implementation and the steps security leaders can take to move toward operating at machine speed.

> **84% of security leaders agree AI should be in the SOC, but only 22% are ready to automate even the most basic L1 tasks.**

---

## Who We Surveyed

We surveyed 100 cybersecurity leaders across enterprise and mid-market organizations. All respondents hold manager-level or above roles with direct influence over security operations and tooling decisions. 48% are CISOs or Deputy CISOs. Industries represented include financial services, SaaS/software, IT services, manufacturing, healthcare, insurance, and others. The survey included nine structured questions (single-select and multi-select) and one open-text question asking what would make respondents seriously evaluate an agentic security platform in the next 90 days.

---

## The Adoption Gap

While AI-enabled attacks are now the norm, our data confirms most defenders haven’t implemented agentic security yet. That asymmetry compounds every day it goes unresolved.

Security leaders overwhelmingly believe AI agents belong in the SOC. 84% agree agents should be doing L1 work. But belief isn’t deployment. Only 36% have agents running in production for even one use case. Why? They don’t trust agents enough yet.

![Chart showing where respondents are today with AI agents in security operations, highlighting that only 36% have AI agents running in production today]

*(Note: Total exceeds 100% as respondents could select multiple options.)*

Leaders agree agents should be in the SOC, but fear automating tasks:

Security leaders agree that agents belong in the SOC, but only 22% are ready to fully automate L1 work.

When asked which SOC task they’d hand to AI agents tomorrow, the answer was decisive on alert triage and prioritization as the right place to start.

![Chart showing responses to automating SOC tasks with AI agents]

*(Note: Total exceeds 100% as respondents could select multiple options.)*

> "If a company could demonstrate how to create and test agents with reliable evaluation and results, I would start a POC of their product immediately."  
> — CISO and VP of IT Architecture & Engineering, Hospitals & healthcare | Company size: 10K+

---

## The Agent Trust Crisis

Ultimately, leaders know that they need to implement AI agents, and even know what they would automate first, but the majority are holding back due to issues with trust.

> **64% of security leaders selected three or more trust concerns.**

Trust is the #1 reason teams haven’t implemented agentic security.

![Chart showing the biggest reasons teams haven't deployed AI agents more broadly in their SOC]

*(Note: Total exceeds 100% as respondents could select multiple options.)*

Leaders cited a wide range of reasons for lack of trust. Lack of trust is the primary reason security teams haven’t adopted agentic security, but AI trust isn’t just one concern. 

When we asked what worries security leaders most about trusting an AI agent to take action in their environment, no single answer dominated.

![Chart detailing specific concerns when trusting an AI agent to take action in an environment]

*(Note: Total exceeds 100% as respondents could select multiple options.)*

Read the top three concerns together and the pattern becomes clear. Security leaders aren’t worried about a single failure mode. They’re worried about a compound one: an agent that acts on incomplete data, hallucinates a conclusion from it, and takes an unintended action as a result.

> "I would recommend a vast amount of use case data to support that not only is the AI agent reliable but that there is an extremely low (as in single digit below 3) percent chance of hallucination."  
> — Deputy Chief Information Security Officer, Professional & technical services | Company size: 1K - 5K

---

## The Data Visibility Problem

Agents can only act on data they can see. And most security teams can’t see everything.

One of the less talked-about reasons teams don’t trust AI agents, is that agents don’t have a complete view of data. While humans can correlate alerts and data signals across platforms, most AI agents are siloed and can only see the data that exists in their system.

- **84%** of security leaders say their current tools cannot access all their log data for investigations.
- **65%** have had at least one investigation stall or be limited because data was trapped in a system their tools couldn’t reach.

Most teams have limited access to log data:

![Chart showing how much log data current security tools can actually access for investigations]

Most teams have had investigations stall due to data access issues:

![Chart showing responses regarding whether investigations have stalled or been limited in the last 12 months]

Even among respondents who said they can access 'most' of their data, more than half still reported stalled investigations. Perceived coverage isn’t the same as actual investigative access.

So why can’t teams access all of their data? The cost of hot storage is a major issue.

> **80% cite the cost of hot storage as painful or a major budget concern.**

The cost of hot storage is a major issue for data access.

![Chart showing how leaders think about the cost of keeping log data hot versus cold]

> "Whether it could truly have visibility over all the data I cannot ingest into my SIEM, actually understand that - rather than throw out false positives which need more investigation, and give me actionable insight into that data."  
> — Chief Information Security Officer, SaaS/software | Company size: 1K - 5K

---

## What This Tells Us

### Leaders agree AI should do the work, but don’t trust it yet
84% agree agents should handle L1 work. 60% named alert triage as the task they’d automate first. But only 22% are ready to fully automate even the most basic L1 tasks. 52% cite AI trust as the top barrier to adoption. Trust concerns don’t come one at a time either: 64% flagged three or more.

Leaders aren’t just asking whether agents can do the work. They’re asking whether they can verify what the agent did, why it did it, and how to stop it when it shouldn’t. They need agents built on deterministic, auditable logic with full audit trails of every action taken and adjustable controls over when and where a human stays in the loop. Leaders know where they want to go, but don’t trust the road yet.

### The trust problem is also a data problem
84% can’t access all their log data. 65% have had investigations stall because of incomplete data. 57% cite fear that agents will act on incomplete data as a top concern. These aren’t three separate findings. They are all part of the same problem from different angles. An agent bolted onto existing data infrastructure inherits every blind spot that infrastructure already has. Without solving the data visibility problem, it is understandable why security leaders can’t trust AI agents.

### The road to successful agentic security implementation
Trust has to be earned at the level of agent architecture. Trustworthy agents need logic that reliably produces the same output for the same input, transparent reasoning that shows how an agent arrived at a conclusion, full audit trails that capture every action and the data behind it, and adjustable human-in-the-loop controls that let security teams define where agents act autonomously and where a human reviews first.

Trust also has to be earned at the data layer. An agent that can only see what the SIEM ingested will make decisions based on a partial picture, and security leaders know it. Visibility into data the agent reasons over is part of the foundation that makes the rest of the trust mechanisms credible.

Agent intelligence without data access leaves a gap. Data access without auditable agent logic leaves a different gap. Closing both is what moves a security team from agreeing with agentic security to actually deploying it.

### Three things to do now:
1. **Layer AI agents into your existing stack**: Connecting your agents to your current stack provides agentic capability now without the need to rip and replace systems. While migration takes months of work and adds risk, an agentic solution can connect to your existing tools in days.
2. **Make sure your agents have access to complete data**: Make sure your agents aren’t stuck in a data silo and can access multiple data sources. If you have log data in S3 or observability tools, make sure agents can connect to those systems.
3. **Start training L1s to be agent managers**: As agents start to take over L1 tasks, transition your existing L1s to manage multiple agents and serve as the human in the loop. Look for tools with customizable human-in-the-loop controls that allow you to gradually give agents more autonomy as they prove they can be trusted.

### Move now, refine later
There isn’t time to wait for your preferred vendor to implement a "perfect" agentic solution. Following the guidance from SANS and CSA, teams need to implement agentic security now to defend against the onslaught of AI-powered attacks. The best path forward is to implement an agentic security solution that works with your existing stack while solving for agent trust and data visibility.

---

## How Strike48 Solves for Agent Visibility and Trust

Strike48 is an agentic security operations platform that combines a federated data layer with purpose-built AI agents to automate triage, investigation, and response across your entire security environment. It was designed to solve the AI agent trust and data visibility problems this report documents.

### Solving the visibility crisis
Strike48 doesn’t require you to move, re-ingest, or duplicate your data. Its federated search-in-place architecture connects to your existing data sources wherever they live—SIEM, cloud, cold storage, third-party platforms—and makes all of it searchable and actionable for agents. No rip and replace. No migration. No new data pipeline to build. Your current stack stays in place. Strike48 extends it.

### Agents that were built for trust
Strike48’s micro-agent architecture means every agent has a defined, narrow scope of action. Full audit trails capture what each agent did, why it did it, and what data it used. Human-in-the-loop controls are adjustable per workflow, so security teams can define exactly where agents act autonomously and where a human reviews before action is taken.

We don’t ask you to take our word for it. Strike48 is built to prove its value in your environment, on your data, against your current workflows.

**Try it free or request a demo here [strike48.com](https://strike48.com)**

---

Strike48 | 3 Center Plaza, Suite 302, Boston, MA 02108  
© 2026 Strike48. All Rights Reserved.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
