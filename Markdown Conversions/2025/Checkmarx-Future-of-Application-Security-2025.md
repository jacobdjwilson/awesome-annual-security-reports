# Report
The Future of Application Security in the Era of AI

2026 Outlook: When a False Sense of Security Meets Breakneck Developer Velocity

## Table of Contents
- [Executive Summary](#executive-summary)
  - [Industry Insights](#industry-insights)
- [Strategic Imperatives](#strategic-imperatives)
  - [01 Move from awareness to action](#01-move-from-awareness-to-action)
  - [02 Embed ‘code-to-cloud’ security](#02-embed-code-to-cloud-security)
  - [03 Govern AI use in development](#03-govern-ai-use-in-development)
  - [04 Don’t just acquire tools, operationalize them](#04-dont-just-acquire-tools-operationalize-them)
  - [05 Prepare for agentic AI in AppSec](#05-prepare-for-agentic-ai-in-appsec)
  - [06 Fuel cultural change with developer empowerment](#06-fuel-cultural-change-with-developer-empowerment)
- [Introduction](#introduction)
  - [The Road Ahead: Cautious Optimism](#the-road-ahead-cautious-optimism)
  - [Methodology](#methodology)
- [The AppSec Readiness Gap](#the-appsec-readiness-gap)
  - [The cost of complacency](#the-cost-of-complacency)
  - [What this means](#what-this-means)
  - [Modern threats, same old AppSec](#modern-threats-same-old-appsec)
  - [What this means](#what-this-means-1)
  - [Modern threats, same old AppSec](#modern-threats-same-old-appsec-1)
  - [What this means](#what-this-means-2)
- [Systemic Risk Tolerance: Why Known Vulnerabilities Reach Production?](#systemic-risk-tolerance-why-known-vulnerabilities-reach-production)
  - [Has speed over safety become the new normal?](#has-speed-over-safety-become-the-new-normal)
  - [What this means](#what-this-means-3)
- [From Critical Exposure to Technical Resilience](#from-critical-exposure-to-technical-resilience)
  - [Tools in hand, but not in play](#tools-in-hand-but-not-in-play)
  - [What this means](#what-this-means-4)
- [AI: The AppSec Curse and (Possibly) the Cure](#ai-the-appsec-curse-and-possibly-the-cure)
  - [AI has infiltrated the SDLC – can it help to secure it too?](#ai-has-infiltrated-the-sdlc--can-it-help-to-secure-it-too)
  - [What this means](#what-this-means-5)
- [The Security-Development Rift Is Closing — Slowly](#the-security-development-rift-is-closing--slowly)
  - [Are developers upping their security game?](#are-developers-upping-their-security-game)
  - [What this means](#what-this-means-6)
  - [The Path to Security-Development Alignment](#the-path-to-security-development-alignment)
- [Conclusion](#conclusion)
- [Key Takeaways](#key-takeaways)
  - [For AppSec Managers](#for-appsec-managers)
  - [For CISOs](#for-cisos)
  - [For Developers](#for-developers)

## Executive Summary

2025 marks a turning point in application security. The threat landscape isn’t just evolving. It’s accelerating faster than most security programs can keep up with.

Emerging technologies, including AI, multi-cloud architectures, and sprawling software supply chains, are vastly expanding the attack surface.

At the same time, business pressure is forcing teams to knowingly ship vulnerable code, eroding the last guardrails of secure development.

In this environment of increasing pressure to deploy faster, developers turn to AI to write large amounts, if not most of, their code. AI is becoming much more than a tool – it’s taking the lead from developers and introducing a new, uncharted frontier of risk.

Application security can no longer afford to be reactive or siloed. It demands immediate, transformative change.

Drawing on insights from over 1,500 AppSec stakeholders globally (CISOs, AppSec Managers, and Heads of Development), this report captures a pivotal moment in the widening disconnect between AppSec awareness and real-world readiness.

It also provides sharp insights on how organizations can not only mitigate but reverse this inertia toward true security maturity that will facilitate and adapt to the upcoming changes.

### Industry Insights

**AI is writing the code. Developers are just hitting deploy, ushering in a new era of risk**
As AI-generated code becomes the norm, developer ownership is fading and AppSec is struggling to keep up the pace: While 50% of respondents (excluding Heads of Development) already use AI security code assistants with a third (34%) admitting that over 60% of their code is AI-generated, only 18% have approved usage policies, exposing teams to unmanaged risks and shadow development.

A third of developers admit that
**Over 60% of their code**
is AI-generated

**Vulnerabilities are pushed as standard**
81% of organizations surveyed admit to knowingly shipping vulnerable code either sometimes or often. This isn’t oversight—it’s strategy. Under pressure to deliver, teams are treating patch-later practices as acceptable risk, embedding insecurity into the SDLC.

**81% of organizations**
admit to knowingly shipping
vulnerable code either sometimes
or often.

**Breaches are accelerating—and becoming normalized.**
A second consecutive year of rise in breach volume indicates deep structural flaws: 98% of organizations experienced a breach from vulnerable code—up from 91% in 2024 and 78% in 2023. The share reporting four or more breaches surged from 16% to 27% year over year, signaling a compounding risk cycle and deeper systemic issues.

**98% of organizations**
experienced a breach from
vulnerable code

**Even the most foundational security tools are overwhelmingly underused**
Fewer than half of respondents (excluding Heads of Development) are actively using core, mature AppSec tools like DAST (47%) or IaC scanning (48%), despite growing availability.

**50% of respondents**
are actively using core, mature
AppSec tools

**DevSecOps talk is common. Execution? Not so much.**
Developer responsibility is rising, with vulnerability remediation improving year over year. Still, friction between development and security persists, and many organizations remain in the early stages of adopting DevSecOps holistically. Now is the time to accelerate this cultural shift.

**51% of organizations**
in North America have adopted
DevSecOps

## Strategic Imperatives

To close the readiness gap and build a sustainable AppSec posture for 2025 and beyond, organizations must act decisively:

### 01 Move from awareness to action
Organizations must acknowledge that awareness alone won’t stop breaches. A mature security posture requires shared accountability, early intervention, and operationalized practices.

### 02 Embed ‘code-to-cloud’ security
To defend against modern threats, organizations must embed security across the entire software lifecycle. A code-to-cloud strategy ensures continuous protection from initial code creation through CI/CD pipelines to live cloud environments. This full-stack visibility and control is essential for securing complex, distributed applications at scale.

### 03 Govern AI use in development
Develop formal policies, approved tools, and auditing practices to secure AI-generated code. Treat AI not just as a risk, but also as a powerful enabler for security automation and intelligent remediation.

### 04 Don’t just acquire tools, operationalize them
Integrate tools like SAST, DAST, SCA, and ASPM into developer-native workflows and central governance models. Tooling must be unified, measurable, and aligned with business velocity.

### 05 Prepare for agentic AI in AppSec
Organizations must begin planning for the integration of agentic AI solutions to manage the scale and velocity of AI-generated code. As code volume continues to surge, traditional review and remediation processes won’t be enough. AppSec strategies must evolve to include AI-driven agents capable of automating code analysis, policy enforcement, and real-time risk mitigation. In the near future, the only viable response to AI-scale development may be AI-powered defense.

### 06 Fuel cultural change with developer empowerment
Invest in secure code training, clear security ownership, and incentivized metrics. A culture where developers, security, and operations share responsibility will be foundational to building technical resilience.

## Introduction

The threat landscape is evolving at an unprecedented pace.

The convergence of emerging technologies such as artificial intelligence (AI), edge computing, cloud-native development, and complex software supply chains is dramatically expanding the attack surface.

Meanwhile, malicious actors are exploiting this growth with increasing sophistication—automating exploits, scaling social engineering, and leveraging AI to uncover vulnerabilities faster than ever before.

AppSec has always been in a race to catch up with development, managing to stay on pace, but only just. In 2025, however, development is accelerating so rapidly that it’s opening a gap too wide for security to bridge without a fundamental shift in mindset.

We surveyed CISOs, AppSec Managers and Heads of Development to explore their views on:
- The AppSec readiness gap
- Security risk tolerance
- Security tooling
- AI as a security risk and opportunity
- Security-developer relations

Based on the survey results, this report captures a pivotal moment in the journey of application security.

While awareness of threats is high, the research reveals a maturity gap that leaves many organizations exposed due to cultural inertia, fragmented practices, and outdated security models.

Vulnerable code is knowingly shipped into production at an increasing rate, security tooling remains immature, and emerging risk catalysts—like AI-generated code—are often left ungoverned.

While AI accelerates development, it also introduces new risks, including unvetted code, shadow tooling, and a rise in “vibe coding,” where developers trust AI outputs without fully understanding them.

It’s time for application security to undergo a major paradigm shift. It is no longer sufficient to bolt on security at the final stages of development or rely solely on isolated tooling. Even shifting left isn’t enough – you need to shift security everywhere – including further left, even before your first code commit.

Instead, organizations must adopt modern DevSecOps governance models that make security everybody’s responsibility and build the technical resilience needed to embed security across the entire software development lifecycle (SDLC).

Inseparably tied to this shift, organizations should also harness AI not just for code generation, but to accelerate remediation, strengthen Software Supply Chain Security (SSCS), support secure-by-default practices, and improve decision-making throughout the SDLC.

### The Road Ahead: Cautious Optimism

Amid these challenges, signs of progress are emerging. Developers are becoming more engaged in remediation, investment in secure-by-default practices is increasing, and a shift toward code-to-cloud security models is underway.

The findings in this report not only highlight where organizations are falling short, but also point to the strategies and structural changes that teams are using to close the AppSec readiness gap, making this more than a snapshot of today’s challenges, but a blueprint for securing software in 2025 and beyond.

### Methodology

**Wave 1 2023:**
The research was conducted by Censuswide, among a sample of 517 Software Developers, 534 AppSec Managers and 516 CISOs (aged 18+) across the UK, USA, DACH, ANZ, France, Singapore and Brazil. The data was collected between September 5, 2022 – September 26, 2022.

**Wave 2 2024:**
The research was conducted by Censuswide, among a sample of 1504 Developers, CISOs, and AppSec Managers (aged 18+) across North America, Europe and APAC. The data was collected between November 30, 2023 – December 21, 2023.

**Wave 3 2025:**
The research was conducted by Censuswide, among a sample of 514 CISOs, 501 AppSec Managers, and 504 software developers (aged 18+) across the US, Australia, New Zealand, Singapore, the UK, Austria, Germany, France, and Switzerland. The data was collected between April 7, 2025 – April 29, 2025.

Censuswide abides by and employs members of the Market Research Society and follows the MRS code of conduct and ESOMAR principles. Censuswide is also a member of the British Polling Council.

## The AppSec Readiness Gap

Despite growing investment and awareness, security breaches caused by vulnerable code remain widespread.

Most organizations know the risks — yet too few are acting decisively to reduce them. The data shows a widening maturity gap: known vulnerabilities are being released, modern threats are poorly defended, and AppSec tooling remains underutilized.

### The cost of complacency

Organizations are facing an expanding and evolving threat landscape and paying a heavy price.

The research reveals that instances of security breaches are on the rise.

98% of respondents say that in the past 12 months their organization experienced one or more security breaches as a direct result of a vulnerable application that their organization developed[^1], compared with 91% of those who said the same last year, and 88% in 2023.

The percentage of organizations reporting four or more breaches jumped from 16% in 2024 to 27% in 2025: an 11-point year-over-year increase. This drift suggests a compounding risk effect, where each breach potentially weakens defenses, exposes additional vulnerabilities, or signals deeper systemic issues in the organization’s software development and security practices.

![Bar chart showing the frequency of security breaches from vulnerable applications in the past 12 months.]

Organizations in Europe (36%) and APAC (34%) are especially likely to have suffered multiple breaches in the past year, with over a third of respondents in each region stating that they have experienced three breaches, while less than a quarter (23%) of those in North America say the same. A 7% YoY increase in breach frequency reveals that despite greater awareness, vulnerability management is not improving. This suggests that policy is disconnected from practice.

The most immediate and visible impact is often business downtime, which 38% of survey respondents cite as an outcome of a breach they experienced in the last 12 months. Typically involving taking infrastructure offline for forensic investigation and remediation, business downtime can severely disrupt productivity and result in a loss of revenue.

(37%) of respondents in the Insurance sector say they have experienced a breach three times in the last 12 months, while just 3% of those in Education say the same.

In parallel, the financial toll (35%) can be substantial, with costs stemming from incident response efforts, regulatory fines, customer compensation, service outages, and increased insurance premiums.

Perhaps even more enduring is the reputational damage (32%) a breach inflicts, as it signifies a failure to fulfill a duty of care, undermines stakeholder trust, and erodes competitive standing. These impacts do not exist in isolation. They compound one another, creating a feedback loop of operational and strategic vulnerabilities. Organizations lacking cybersecurity maturity are especially prone to experiencing the most severe consequences, highlighting the urgent need for proactive and comprehensive risk management.

The findings also indicate that organizations in some industries are more vulnerable than others. Almost 2 in 5 (37%) respondents in the Insurance sector say they have experienced a breach three times in the last 12 months, while just 3% of those in Education say the same.

### What this means

**The False Economy of “Survivable” Breaches**

Organizations have possibly developed a dangerous comfort with security breaches.

But the data shows this mindset is backfiring—98% of organizations experienced breaches in the past year, up 7% from last year. Each breach doesn’t just cost money; it can erode customer trust, regulatory standing, and market position in ways that compound over time.

**Actionable Insights by Role:**

**CISOs:**
Your board has heard breach statistics before and tuned them out. Instead, calculate the cumulative operational drag of your last three breaches—lost deals, extended sales cycles, regulatory audit overhead, customer retention costs. Present security investment as revenue protection, not cost center spending. Get specific about how breaches slow business growth.

**AppSec Managers:**
Opt for measuring developer engagement with security, rather than tool deployment. Low adoption means poor workflow integration. Embed security feedback directly into IDEs and pull requests where developers already work. Track time-to-fix vulnerabilities, not just vulnerability discovery rates.

**Development Leaders**
Audit whether your “developer-friendly” security actually works or just provides cover for shipping vulnerabilities. Create hard stops for critical vulnerabilities in CI/CD and give developers fast remediation paths instead of easy workarounds.

**The Core Problem:**

Organizations knowingly ship vulnerable code, treating this as acceptable business practice. This isn’t about needing better tools or more training—it’s about normalizing dangerous shortcuts. The gap between security awareness and security maturity is widening because awareness without operational accountability is meaningless.

### Modern threats, same old AppSec

Market trends are putting organizations at risk of diverse security threats.

Respondents cite a wide range of security threats that are expected to cause disruption in the next 12-18 months. These are directly driven by some of the most dominant market trends in software development, which are introducing new vulnerabilities to the SDLC.

Respondents are most likely anticipating software supply chain compromises (35%) and third-party vendor/partner security incidents (35%). This is unsurprising given that 67%[^2] of respondents say half or more of their organization’s application code consists of open-