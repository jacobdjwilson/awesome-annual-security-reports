# SPECIAL REPORT 2026: The State of AI and SaaS Security Report

### What LastPass data reveals about the AI tools, apps, and credential risks flying under IT’s radar

---

## Table of Contents
- [Introduction](#introduction)
- [Key terms](#key-terms)
- [Chapter 1: Your team's AI adoption is outrunning IT's visibility](#chapter-1-your-teams-ai-adoption-is-outrunning-its-visibility)
  - [AI is already mainstream in your business](#ai-is-already-mainstream-in-your-business)
  - [Why governance hasn't kept up](#why-governance-hasnt-kept-up)
  - [Shadow AI is the norm, not the exception](#shadow-ai-is-the-norm-not-the-exception)
  - [IT leaders know the risks but don't feel equipped to act on them](#it-leaders-know-the-risks-but-dont-feel-equipped-to-act-on-them)
  - [The answer isn't to block AI](#the-answer-isnt-to-block-ai)
- [Chapter 2: AI is amplifying familiar visibility challenges](#chapter-2-ai-is-amplifying-familiar-visibility-challenges)
  - [The visibility gap didn't start with AI](#the-visibility-gap-didnt-start-with-ai)
  - [Why the problem is worse in smaller organizations](#why-the-problem-is-worse-in-smaller-organizations)
  - [How AI expands credential risk](#how-ai-expands-credential-risk)
  - [You can fix the password. You can't fix what you can't see.](#you-can-fix-the-password-you-cant-fix-what-you-cant-see)
- [Chapter 3: What it's costing you](#chapter-3-what-its-costing-you)
  - [The visibility gap now carries two costs](#the-visibility-gap-now-carries-two-costs)
  - [Cost #1: redundant SaaS spend](#cost-1-redundant-saas-spend)
  - [Cost #2: compliance exposure](#cost-2-compliance-exposure)
  - [How AI accelerates SaaS sprawl](#how-ai-accelerates-saas-sprawl)
  - [Small to mid-sized teams are most at risk](#small-to-mid-sized-teams-are-most-at-risk)
- [Chapter 4: What this means for businesses](#chapter-4-what-this-means-for-businesses)
  - [The market problem: No clear solution has emerged](#the-market-problem-no-clear-solution-has-emerged)
  - [The path forward: visibility first](#the-path-forward-visibility-first)
  - [You've seen the data. Now what?](#youve-seen-the-data-now-what)
- [Methodology](#methodology)

---

## Introduction

Speed drives behavior. It’s the reason most people reach for AI in the first place. It’s also the same logic behind password reuse and the rise of AI-powered SaaS. And that’s precisely the problem. In a world where SaaS can be adopted in minutes, speed consistently outpaces the controls meant to contain risk. The result is a growing gap between what employees are doing and what IT can see, a gap with real security and financial consequences.

### What this means:
Organizations have dealt with shadow IT for years, but AI magnifies the impact of the visibility gap. A password can be reset, a redundant app subscription canceled. But once employees enter sensitive business info into AI-enabled tools, that information now resides in systems you can’t easily monitor, govern, or assess for compliance risk.

To highlight this gap, we drew on two complementary sources: anonymized LastPass platform data, plus a June 2026 research study consisting of a LastPass survey and interviews with IT leaders (detailed methodology appears at the end of this report). Each finding in this report is labeled by source:

- **Platform data** shows what employees are logging in to.
- **Survey and interview data** highlight what IT leaders prioritize, where they see risk, and where their current tools fall short.

What we found confirmed something many already suspect but have struggled to quantify:

> **The gap between AI adoption and oversight is wider than most current tools can track.**

Three themes emerged across the data:

1. **AI adoption has outrun governance by a wide margin.** Organizations know the gap exists, but while some are actively evaluating solutions, many still struggle to identify the right path forward.
2. **Password reuse remains high and is being made worse** by the same human instincts driving AI sprawl.
3. **SaaS/AI sprawl is a drain on budgets.** Not in dramatic fashion, but in the quiet accumulation of redundant tools and unused subscriptions.

These aren’t three separate problems, but three faces of **ONE** problem: Activity moving faster than IT can see and govern. What follows is the data we compiled, what it reveals, and what it means if you’re responsible for managing SaaS and AI access for your organization.

---

## Key terms

- **Shadow AI**: The AI-specific form of shadow IT; employee use of AI tools without the approval and oversight of the IT team.
- **Shadow SaaS / SaaS sprawl**: Business apps adopted outside IT oversight, accumulating across an organization.
- **Unused app**: An app with no recorded logins in the previous 30 days.
- **Redundant (or duplicate) app**: An app in the same category as another, i.e., more than one app in the same category.
- **Reused credential**: A password used across more than one account.
- **Breached credential**: A credential that has appeared in a known data breach and is still in active use.
- **AI governance / AI governance program**: An organization's policies and controls for how employees may use AI, e.g., acceptable-use policies and technical controls that allow, warn on, or block specific tools.
- **Company size**: Estimated using LastPass customer segments as a proxy for organization size, rather than exact employee counts:
  - **vVSB (Very, Very Small Business)**: 0-19 employees
  - **VSB (Very Small Business)**: 20-49 employees
  - **SMB (Small to Mid-Sized Business)**: 50-499 employees
  - **COM (Commercial)**: 500-2,999 employees
  - **ENT (Enterprise)**: 3,000+ employees

Unless otherwise noted, company-size comparisons in this report refer to these customer segments.

---

## Chapter 1: Your team's AI adoption is outrunning IT's visibility

### What the data shows

- **92%** of surveyed admins say AI is already in use across their organizations. But only **27%** have an enforced AI governance program, while **42%** have no technical controls at all (Survey).
- **46%** of organizations report moderate-to-high levels of shadow AI. **19%** of respondents aren’t sure how much is happening (Survey).
- **68%** of organizations say employees entering sensitive data into AI is their #1 concern. Yet, their confidence in their ability to identify and respond to this risky behavior sits at **2.5 out of 5** (Survey).

---

### AI is already mainstream in your business

> **92%** of surveyed admins say AI is already in use across their organizations (Survey).

Not long ago, AI was the domain of research and development teams and engineers, used primarily for coding, model development, and prototyping. That’s no longer the case.

Our survey confirms this:

**92%** of respondents reported that some form of AI is already in use in their organizations. The breakdown of this figure is:
- **36%** described adoption as organization-wide
- **21%** said it’s concentrated in specific departments
- **16%** said it’s happening at the individual level
- **19%** said it’s a mix of approved and independent usage

More than 80% of respondents describe themselves as AI adopters, with 31% identifying as early adopters and 50% as cautious adopters (Survey). The language leaders use to describe their own posture is significant. “Cautious adopter” suggests awareness of the risks alongside a recognition that resistance is neither effective nor desirable. No longer experimental, AI has quietly become as commonplace as business-critical software in the workforce.

---

### Why governance hasn't kept up

Speed explains part of the gap. Many consumer-grade AI tools don’t require procurement reviews or IT approval. An employee can log in with a personal email, use a consumer-grade AI tool on a corporate device, and share sensitive info before IT is even aware the tool exists. The barrier to adoption is close to zero.

In our survey:
- **73%** of organizations say they don’t have a comprehensive, actively enforced policy for employee AI use.
- Only **27%** have enforced AI-use policies.

From the data, the controls gap is clear:
- **42%** have no technical controls at all for managing employee access to AI tools. This means no allow lists, block lists, or DLP (data loss prevention) rules covering AI traffic.

And among those more mature IT organizations who do:
- Only **22%** have tools to monitor and log AI usage.
- **17%** use blocked-tool lists at network endpoints.
- Only **13%** have DLP rules covering AI traffic.

The gap is partly a timing problem. Governance is built through process and enforced through procedure. It involves policy drafting, legal review, stakeholder sign-off, technical configuration, and employee feedback. AI tools can bypass all of that. They go from discovery to active use in a single session.

> **73%** of organizations lack a comprehensive, actively enforced AI usage policy (Survey).

> **42%** have no technical controls in place for managing employee AI access (Survey).

But the gap is also, in part, a deliberate choice. Seven of 10 interviewees we spoke to said they’ve chosen not to block AI, not because they underestimate the risk, but because they understand the organizational reality. Blocking AI doesn’t eliminate risk; it just pushes usage to personal accounts and unmanaged devices, making the problem less visible, not smaller.

The preferred posture centers on visibility, keeping employee behavior within IT’s line of sight rather than driving it out of view (Interviews). The hopeful note: More than 40% of organizations plan to implement technical controls in the next 12 months (Survey).

---

### Shadow AI is the norm, not the exception

Shadow AI (employee use of AI tools without IT approval) is widespread. According to our survey, the top unsanctioned tools regularly accessed by employees include:

![Bar chart showing AI tool adoption and the percentage of employees using each tool across the organization]

In our survey, 46% of organizations reported a moderate-to-high level of shadow AI. But an additional 19% weren’t sure how much shadow AI activity is happening at all. Put together, nearly two-thirds of organizations either have significant ungoverned AI use or lack the visibility to identify it (Survey).

One reason shadow AI is so difficult to contain: It doesn’t require corporate credentials to access. Employees can routinely bypass identity-based access controls to use consumer-grade AI. The risk with traditional SaaS has primarily centered on who can access what, and whether their permissions are appropriate.

With AI in the picture, the risk conversation shifts to data and behavior: What info goes into a tool, and what can the tool do with the output? In interviews, eight of 10 participants said their current security infrastructure doesn’t cover AI use cases at all. So, for now, most organizations aren’t choosing between visibility and depth. They’re choosing between some visibility and none.

![Diagram illustrating the New Risk Paradigm: Traditional SaaS security equals identity plus access controls, whereas AI risk equals data exposure plus agentic action. Tools built for the former do not solve the latter.]

---

### IT leaders know the risks but don't feel equipped to act on them

The data reveals a striking contradiction: AI apps are the category IT leaders say they worry about most, yet they are the least governed. Currently, 73% lack comprehensive and actively enforced policies on AI usage. IT leaders aren’t unaware of what’s at stake. In our survey:

- **68%** named employees entering sensitive corporate data into AI tools as their #1 concern.
- **61%** cited AI tools gaining access to corporate systems as their leading access-related risk.
- And **56%** are concerned about employees entering sensitive credentials directly into AI prompts.

These concerns are shared across organization size and industry and corroborated by independent research. According to Gartner, AI information governance risk is among the top emerging risks for organizations, reflecting growing concern about uncontrolled AI access to corporate systems.

What’s striking, however, isn’t the concern itself, but the gap between how seriously IT leaders take these risks and how capable they feel about addressing them. Survey respondents rate the importance of detecting sensitive data entered into AI as 4.22 out of 5 and responding to risky behavior pertaining to AI as 4.09 to 4.24 out of 5.

> **68%** named employees entering sensitive corporate data into AI tools as their #1 concern (Survey).

> **2.5/5** confidence in detecting when sensitive data has been entered into AI tools. The lowest-rated capability of all (Survey).

But when asked to rate their confidence in their ability to detect and respond to risky or unauthorized usage by employees, the numbers fall substantially:

- Confidence in detecting sensitive data entered into AI tools, the #1 concern, sits at **2.5 out of 5**.
- Confidence in identifying when employees are using unapproved or unsanctioned tools rates **2.6 out of 5**.
- Confidence in taking action to stop inappropriate AI usage rates **3.0 out of 5** (Survey).

The lowest-rated capability of all is confidence in detecting when sensitive company info has been entered into an AI tool. That’s the capability most directly tied to the risk IT leaders say they are most worried about.

The data shows only a minority of mature IT organizations have solutions in place to monitor and log AI usage (22%), even though 27% identify lack of visibility as a top concern (Survey).

---

### The answer isn't to block AI

IT leaders agree that the goal isn’t restriction but awareness and, where necessary, calibrated friction. In interviews, leaders described three capabilities that would genuinely move the needle:

#### Capability #1: content-level visibility
This isn’t just a list of which AI tools are running in the organization, but insight into what data is flowing into those tools. Seven of 10 interview participants cite this as an essential capability that would complement their current security stack. Knowing that employees use a particular AI tool is useful. But knowing if they’re entering customer records, financial data, or internal docs into it is the info that allows IT to assess and manage risk.

#### Capability #2: enforcement at the point of risk
This means in-flow warnings, splash pages, and conditional friction that interrupt a risky action before it’s completed. Our interview participants (four out of 10, all in the mature buyer group) say real-time observability beats after-the-fact dashboards; seven of 10 wanted soft enforcement at the point of risk.

#### Capability #3: in-context education
Six of 10 interview participants said they believe in-flow guidance would be more effective than traditional AI security training. And organizations further along in their AI governance thinking have articulated an additional requirement: a reasoning-trail capture for agentic AI actions. This is the ability to log not just which tools are accessed, but why an AI agent took a specific action, what data it touched, and what it did with the output. The market hasn’t converged on an answer to this capability yet, however (Interviews). As of this writing, regulatory bodies are still in the input gathering stage.

In January 2026, NIST’s CAISI issued a Request for Information, and the responses show widespread consensus about the novel threats presented by agentic AI. While frameworks and toolkits have emerged, like Microsoft’s Agent Governance Toolkit and OWASP’s Top 10 for Agentic Applications, it’s important to remember: Before you can govern AI risk, you have to see it.

Most small to mid-sized teams don’t have that visibility yet. And that’s the first order of business: No framework or toolkit can help until you have real-time observability into what’s running.

---

## Chapter 2: AI is amplifying familiar visibility challenges

### What the data shows

- **52.8%** of users reuse passwords across accounts. **21.2%** are actively logging in with a credential that has appeared in a known data breach (Platform data, 450,784 users across 20,631 organizations).
- Password reuse runs at approximately **66%** among vVSB organizations (0-19 employees) versus approximately **42%** at enterprise organizations (3,000+ employees) (Platform data).

> **52.8%** of users reuse passwords across accounts (Platform data, 450,784 users across 20,631 organizations).

> **21.2%** are actively logging in with a credential that has appeared in a known data breach (Platform data).

AI adoption may be creating governance challenges, but the underlying visibility problem isn’t new. The persistence of password reuse shows how unmanaged behavior has been creating risk, long before the rise of AI.

---

### The visibility gap didn't start with AI

AI may be the newest governance issue, but the underlying behavior is nothing new. Long before AI arrived, password reuse demonstrated how convenience-driven decisions can complicate governance. Data from 450,784 users across 20,631 organizations shows that:

- **52.8%** of users are reusing passwords across more than one account.
- **21.2%** are logging in to accounts using a credential that has already appeared in a known data breach (Platform data).

This means more than half of your users may be handing attackers a second key every time they reuse a password, and the door that key opens isn’t always the one that’s visible to you. The risks also compound if that reused credential has shown up in a breach.

---

### Why the problem is worse in smaller organizations

Password hygiene isn’t uniform across organization size. Password reuse runs at approximately 66% among the smallest organizations (vVSB: 0-19 employees), compared to approximately 42% at enterprises (ENT: 3,000+ employees) (Platform data).

The pattern isn’t difficult to explain. Enterprise organizations tend to have dedicated security teams, formal awareness programs, and robust tooling to enforce credential hygiene. Smaller organizations are more likely to rely on informal processes and individual judgment. The gap isn't about attitude. Smaller organizations simply have fewer mechanisms to enforce what they already know is good practice. Policy without tooling can’t change behavior at scale.

---

### How AI expands credential risk

Consumer-grade AI tools often operate outside SSO and centralized monitoring. As those accounts accumulate, so does the attack surface associated with unmanaged credentials. More directly: An employee who accesses a consumer AI tool with a reused password, and then shares sensitive data with that tool, has created two compounding risks: An exposed credential and data entered into a system that’s outside IT control. These risks are generated by the same instinct: The need to move fast and work around “rules” that feel like obstruction.

---

### You can fix the password. You can't fix what you can't see.

A strong, unique password attached to an unsanctioned account is still invisible to your access management system. IT can't see the access, revoke it, or determine whether it poses a risk. That’s why credential hygiene and access governance must work together. Strong passwords are necessary but insufficient in themselves. The accounts those passwords protect also need to be within IT's line of sight.

---

## Chapter 3: What it's costing you

### What the data shows

- **65.5%** of the apps organizations sign up for go unused within 30 days, and **64.4%** are in a category where the organization already uses at least one other app (Platform data, 15,907 organizations).
- AI is accelerating SaaS sprawl faster than governance programs can keep pace.
- The visibility gap creates two business costs: **redundant SaaS spend** and **compliance exposure**.

---

### The visibility gap now carries two costs

The visibility gap discussed throughout this report isn’t just a security problem. As employees adopt SaaS and AI tools independently, this results in two distinct business costs:

- **Cost #1 is financial:** Duplicate apps and redundant subscriptions drive unnecessary SaaS spend.
- **Cost #2 is compliance-related:** Unmanaged apps create compliance risk, potentially leading to regulatory fines, legal action, loss of government contracts, and exclusion from future bids.

Both stem from the same root cause: Employees adopting tools faster than IT can track.

---

### Cost #1: redundant SaaS spend

**65.5%** of the apps organizations sign up for go unused within 30 days (no recorded logins). **64.4%** of apps are in a category where the organization already uses at least one other app (Platform data). When employees move faster than IT can see, subscriptions accumulate the same way passwords and AI apps do: Silently and with consequences that compound over time. According to Gartner’s 2025 Magic Quadrant for SaaS Management Platforms, organizations are generally only aware of 40% of apps in use[^1].

> **65.5%** of the apps organizations sign up for go unused within 30 days (no recorded logins) (Platform data, 15,907 organizations).

> **64.4%** of apps are in a category where the organization already uses at least one other app (Platform data).

Gartner maintains that those that fail to attain centralized visibility will overspend on SaaS by at least 25% through 2027. The challenge: You can’t consolidate or negotiate volume pricing on tools you don’t know exist. Effective cost control requires visibility into what’s actually running. For small to mid-sized organizations, the total SaaS spend picture is compounded by the AI layer.

Gartner projects that worldwide AI spending will grow by 47% in 2026, as organizations accelerate investment across every function (Gartner, May 2026). The financial cost of unmanaged SaaS and AI will be visible in your invoices. But the compliance cost won’t be until an audit finds it, and by then, the exposure may have been accumulating for months.

[^1]: This finding has also been discussed by The ITAM Review in its analysis of the report.

---

### Cost #2: compliance exposure

Every app your team signs up for without IT approval is an app whose data residency and processing requirements you can’t review. The reality is compliance risk is often a downstream consequence of the visibility gap: If IT can’t see which SaaS and AI tools are handling company data, it can’t evaluate regulatory exposure either.

#### Compliance exposure breakdown

| Category | What’s happening | Why it matters | Who's most exposed |
| :--- | :--- | :--- | :--- |
| **Standardization** | NIST AI RMF and ISO/IEC 42001 are increasingly referenced in enterprise and government procurement as baseline AI governance standards. | Organizations that can't document their AI tool inventory, classify tools by risk, or demonstrate governance controls may be disqualified from deals. | Organizations serving enterprise or government clients. |
| **Sovereign privacy frameworks** | Cybersecurity laws like DORA or NIS2 and a growing body of U.S. state privacy laws are being actively enforced. | Recent enforcement trends suggest that regulators are increasingly unwilling to accept lack of awareness as a defense, with fines being issued for non-compliance. | Organizations serving EU markets; U.S. companies under state privacy laws. |
| **EU AI Act compliance** | The EU AI Act classifies AI use in areas such as education, recruitment, critical infrastructure, and law enforcement as high-risk, requiring logging, human oversight, and documented risk controls (EU AI Act: Annex III). | Many AI-enabled HR and productivity tools employees adopt without IT approval may fall under the Act’s high-risk classifications. Without visibility into what’s running, organizations can’t implement the right controls to demonstrate compliance. | Organizations using AI in regulated use cases, e.g., HR, benefits, credit, education, healthcare, critical infrastructure, finance, legal. |
| **Procurement & vendor risk** | A SaaS vendor may pass a procurement review despite insufficient transparency into its AI-related data practices, including whether it trains AI on data outside its DPA (data processing agreement). | Procurement reviews that emphasize data-at-rest controls without corresponding assessment of data-in-use behavior may leave gaps in demonstrating appropriate technical controls under GDPR Article 28 and other data protection laws. | Any organization using AI-enabled SaaS, which is an increasing number of organizations in 2026. |

In practice, an app adopted this quarter could quickly become an audit concern, especially if you don’t know the app even exists. And if compliance risk is the result of poor visibility, AI is becoming one of its biggest accelerants.

---

### How AI accelerates SaaS sprawl

AI accelerates SaaS sprawl in three ways.

#### The first is volume
AI tools are being adopted faster than previous categories of traditional software.

#### The second is agentic AI
Gartner estimates that $234 billion in enterprise app spend is at risk from agentic AI, tools that take autonomous actions rather than just responding to prompts (Gartner, July 2026). Active agents inside the Microsoft 365 ecosystem alone have grown 15x year over year (Microsoft 2026 Work Trend), and there are now 10,000+ public MCP servers (Anthropic). Each agent can independently call other services, so just one “approved” AI deployment can fan out to multiple ungoverned integrations. An organization that doesn’t have visibility into its current SaaS footprint is poorly positioned to govern a layer of autonomous AI activity running on top of it.

#### The third is AI-powered SaaS
AI is embedding itself inside tools you already approved. Sprawl used to mean a new login and invoice. Now it increasingly means a feature that just needs to be turned on inside the software. Gartner predicts that 25% of all enterprise generative AI apps will experience at least five minor security incidents per year by 2028, a figure that reflects how quickly these governance gaps are turning into real incidents once AI features get layered onto an already-unmanaged SaaS environment.

---

### Small to mid-sized teams are most at risk

Smaller organizations have fewer centralized procurement or asset management controls, making it harder to monitor unused applications. The same conditions that make password hygiene worse at smaller organizations, i.e., fewer resources and more reliance on individual judgment, also make SaaS sprawl harder to manage.

---

## Chapter 4: What this means for businesses

The findings in this report point to a single underlying condition: **Activity inside organizations moving faster than IT can see.**

Historically, the cost of that visibility gap was often manageable. A duplicate SaaS tool could be removed, an unused subscription canceled. But AI changes the equation completely because the most valuable asset involved, your business data, is at risk. When employees brought AI to work, few governance programs existed to manage them. In time, easy SaaS signups led to an explosion in AI usage. None of this is new; what’s changed are the consequences. With AI in the picture, you’re racing against time to identify where corporate data and credentials are flowing before your visibility gap results in a security incident. But the problem is, knowing a gap exists is much easier than knowing how to close it.

---

### The market problem: No clear solution has emerged

One factor that has slowed governance is the absence of a clear market leader in AI governance tooling. The category is new, and purchase decisions often require alignment across IT, legal, finance, and leadership. This process can take months even when urgency is established. And the vendor landscape hasn’t yet consolidated around a single approach (Interviews). While waiting for market clarity, the behavior organizations are trying to govern continues (Survey).

According to our survey data, organizations purchasing in this category generally fall into two groups:
1. The first, which is the majority, knows the gap exists; but they haven’t committed to a budget yet and are most likely to act only after external pressure from an incident or audit demand from a customer.
2. The second group is also aware of the gap and is actively evaluating solutions but can’t find a clear market leader to guide the choice.

Both groups need visibility before enforcement. The question is how to get there without adding significant complexity or expense.

---

### The path forward: visibility first

IT leaders aren’t looking for solutions that block their employees from using AI. The survey findings make clear that their biggest concern is employees entering sensitive data into AI tools. Addressing that risk starts with a more fundamental challenge: Knowing which tools are being used across the organization. While visibility isn’t the complete answer to AI governance, it’s the prerequisite for every other control. You can’t implement controls for tools you can’t see.

In practice, a visibility-first approach means maintaining a continuous, live view of your SaaS and AI app footprint. One that lets you protect logins, see new apps as employees adopt them, and surface redundant subscriptions. From that foundation, enforcement becomes targeted rather than reactive. Instead of blanket bans that push behavior underground, you calibrate policy to specific tools: Allowing seamless access to low-risk apps, warning on higher-risk ones, and blocking only when the risk clearly outweighs the benefits. The effective sequence is: **See it first, then govern it.**

---

### You've seen the data. Now what?

Run LastPass SaaS Monitoring and you’ll find the same patterns this report did:
- AI tools with no policy applied
- Apps your team signed up for that haven’t been accessed in 30 days
- Credentials flagged in known breaches still being used to log in to active accounts

SaaS Monitoring runs in the background, continuously showing:
- **New apps that surface as employees adopt them**, so you can see access as it happens.
- **Credential alerts that refresh as breach intelligence is updated**, so you’re working from current exposure data.
- **Unused apps that are flagged automatically** when 30 days pass without a login, giving you the information you need to consolidate subscriptions.

Your admins don’t need to run audits or survey employees. The picture builds itself in real time, even without an active LastPass browser extension session. Knowing what’s running is the first step. Governing it is the second, and that’s where SaaS Protect comes in.

For each app in the discovered SaaS footprint, you can set one of three rules:

- **Allow**: The app is sanctioned. Employees can access it without friction, and their access is visible to IT.
- **Warn**: The app is permitted but flagged. Employees see an in-browser notification at the point of login. They get context that the app sits outside IT oversight, with an opportunity to redirect to an approved alternative. The employee can proceed, but the behavior stays visible to IT, and the friction creates a moment of awareness.
- **Block**: The app is restricted. Employees see an in-browser message explaining the restriction when they attempt to access the app, and access is prevented.

The “Warn” setting is the mechanism IT leaders in our research describe as the most effective: Enforcement that works with employee behavior rather than against it. Because policies can be customized based on individuals or groups, you can apply that friction where it’s most needed rather than extending it to everyone.

Together, SaaS Monitoring and SaaS Protect are the answer to the visibility gap this report documents, one that doesn't require added infrastructure, a security team, or months of implementation before it starts working.

> Get visibility into the AI and SaaS tools your employees are using. See what’s running, protect credentials, and reduce risk without slowing productivity.  
> [Talk to our team](#)

> Ready to move from visibility to control? See how SaaS Protect gives you the controls to govern SaaS and AI usage at scale.  
> [Request a demo](#)

---

## Methodology

This report draws on two complementary sources of data:

1. **Telemetry from LastPass SaaS Monitoring**: This is anonymized, aggregated usage data from organizations on the LastPass Business Max plan. SaaS Monitoring identifies app usage through the LastPass browser extension, recording logins to apps that match LastPass's library of known SaaS and AI apps.
   
   Because coverage is limited to apps in the library, the figures in this report should be viewed as a conservative baseline: Real-world usage is very likely higher, as apps outside the library aren’t captured. These datasets are large. Credential findings are based on 450,784 users across 20,631 organizations, and app-usage findings on 15,907 organizations. The data was pulled in June 2026 and represents a point-in-time snapshot, not a trend line.

2. **June 2026 Research Study**: Combines a survey of 412 LastPass Business and Business Max admins with 10 prospective customer interviews. The latter consisted of IT and security leaders at organizations of roughly 100 to 2,500 employees in data-sensitive industries such as professional services, healthcare, education, finance, and technology. Where the platform data shows employee behavior, the survey and interviews capture what IT leaders think, plan, and worry about.

Throughout the report, findings are labeled by source. For company-size comparisons, size is estimated using LastPass customer segments rather than exact employee counts, so comparisons should be read as directional rather than exact:

- **vVSB (Very, Very Small Business)**: 0-19 employees
- **VSB (Very Small Business)**: 20-49 employees
- **SMB (Small to Mid-Sized Business)**: 50-499 employees
- **COM (Commercial)**: 500-2,999 employees
- **ENT (Enterprise)**: 3,000+ employees

A small number of third-party statistics are cited where noted, solely to corroborate these findings.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-10", "model": "gemini-3.8-flash"} -->
