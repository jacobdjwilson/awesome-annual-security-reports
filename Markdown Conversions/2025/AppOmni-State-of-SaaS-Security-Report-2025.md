# State of SaaS Security Report 2025

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [Section 1: The SaaS Surge: Growing Usage But Rising Security Incidents](#section-1-the-saas-surge-growing-usage-but-rising-security-incidents)
- [Section 2: Sanctioned ≠ Secure: The Illusion of Oversight in SaaS Environments](#section-2-sanctioned--secure-the-illusion-of-oversight-in-saas-environments)
- [Section 3: The SaaS Security Org Chart: Who Owns What](#section-3-the-saas-security-org-chart-who-owns-what)
- [Section 4: Good Enough or Just Lucky? The Cost of SaaS Security Tradeoffs](#section-4-good-enough-or-just-lucky-the-cost-of-saas-security-tradeoffs)
- [Section 5: Secure in Theory. Breached in Practice](#section-5-secure-in-theory-breached-in-practice)
- [Section 6: AI and the New SaaS Security Agenda](#section-6-ai-and-the-new-saas-security-agenda)
- [Key Recommendations for 2026 and Beyond](#key-recommendations-for-2026-and-beyond)
- [Final Thoughts](#final-thoughts)
- [Methodology & Demographics](#methodology--demographics)
- [About AppOmni](#about-appomni)

---

## Foreword
We’re proud to share AppOmni’s third annual The State of SaaS Security Report. SaaS continues its enterprise transformation with a projected compounded annual growth rate of 20% between 2025 to 2032. The stakes for securing these platforms have never been higher. Today, nearly every organization relies on SaaS to operate, and attackers know it.

In the past year, SaaS security, together with concerns around the secure use of AI, has moved from a niche security initiative to a boardroom imperative. In its 2024 letter, JPMorgan’s CISO, Pat Opet, explicitly named SaaS vulnerabilities as an area of utmost importance, noting the industry’s increasing dependence on third-party providers and the growing threat of SaaS attacks. The 2025 Verizon Data Breach Investigations Report (DBIR) called out a doubling of breaches involving third-party applications stemming from misconfigured SaaS platforms and unauthorized integrations, particularly those exploited by threat actors through scanning and credential stuffing.

SaaS is now one of the most actively targeted layers of the enterprise attack surface, and yet, it remains one of the least proactively defended. Adversary activity in SaaS apps prompted the government’s watchdog—the Cybersecurity and Infrastructure Security Agency (CISA)—to issue a Binding Directive (BOD 25-01) to public sector agencies to secure their critical SaaS environments and urge the private sector to do the same.

At AppOmni, we see this play out every day. Our SaaS threat research team has published multiple investigations this past year alone, exposing critical misconfigurations and vulnerabilities across major SaaS platforms like Salesforce, ServiceNow, NetSuite, and Microsoft 365. These aren’t theoretical risks—they’re real-world exposures impacting the biggest brands in the world.

This year’s State of SaaS Security report is based on insights from over 800 global security leaders. Their responses reveal a troubling disconnect: 91% of respondents express confidence in their SaaS security posture, yet 75% experienced a security incident in the past year—many involving the very issues our team and other industry experts have warned about. 89% of those impacted by incidents or breaches believed they had “appropriate visibility” into their environments at the time.

This is the illusion of control, and it’s one of the most dangerous challenges facing security teams today. People are busy. Teams rely on dashboards and implicitly trust platform vendors. But visibility alone is not security. And trust without verification is not a strategy.

What we need now is clarity. SaaS security must evolve from an ad hoc, reactive process to a mature, repeatable discipline. That means embracing continuous monitoring over point-in-time audits, assigning clear ownership, and protecting the entire ecosystem, including users, configurations, and app-to-app connections alike.

This report is both a snapshot of where the industry stands and a call to action. The attacks are already here. The question is: Are you ready?

**Brendan O’Connor**
CEO & Co-Founder, AppOmni

---

## Executive Summary
As organizations scale their use of cloud applications, they're also expanding their attack surface. The State of SaaS Security 2025 Report reveals a sharp increase in SaaS security incidents, a rising complexity in app ecosystems, and a persistent disconnect between perceived visibility and actual risk reduction.

As SaaS adoption accelerates, so too does the urgency for security teams to close the gap between visibility and actual control. This report set out to understand the realities behind that gap—and to challenge assumptions about maturity, confidence, and level of control.

### This report investigates:
- **Are security teams keeping pace with the rising complexity and interconnectivity of SaaS ecosystems?** We examined how organizations are managing risks from user permissions, app misconfigurations, and SaaS-to-SaaS connections.
- **What does “confidence” in SaaS security really mean, and is it justified?** With 91% of organizations reporting confidence in their SaaS security but 75% experiencing an incident, we investigated the source of that confidence.
- **How are organizations operationalizing SaaS security—or failing to?** We looked at whether visibility translates into enforcement, what tools and teams are actually being used, and how responsibility is shared.
- **Is the security mindset evolving fast enough to meet the moment?** While 96% say SaaS security is becoming more important, we tested whether that urgency is translating into more mature, continuous practices.
- **How are organizations responding to emerging challenges like AI governance and regulatory scrutiny?** We assessed how teams are preparing for the next wave of SaaS risks.

---

## Key Findings
![Infographic summary of key statistics: 75% incident rate, 91% confidence rate, 89% visibility gap, 52% reliance on periodic reviews, 43% lack continuous oversight, 53% rely on vendor trust, 16% assign security solely to security teams, 41% incidents from permissions, 13% use SSPM, 61% expect AI to dominate.]

---

## Section 1: The SaaS Surge: Growing Usage But Rising Security Incidents
Over the last year, data reveals significant SaaS security concerns. Specifically, 41% of those surveyed identified vulnerabilities in SaaS user permissions, while 29% reported incidents stemming from SaaS application misconfigurations. Further security findings include 26% of respondents encountering data exposure and 25% where human error led to data exposure.

Our data shows that 75% of respondents have experienced a SaaS security incident or data breach in the past 12 months. This is a substantial 33% increase compared to The State of SaaS Security 2024 Report.

### Concerns
Data security remains a paramount concern. A majority of respondents, at 57%, cited data breaches and the potential loss of intellectual property as their primary worry. Over a third (37%) expressed considerable apprehension about compromised customer data.

### Deployed SaaS Applications
Most organizations are using dozens or even hundreds of SaaS applications. Over half (57%) of respondents say they’re aware of 50 or more SaaS apps deployed in their organization’s environment. Over a third (40%) report 100 or more apps.

> "Our biggest headache with SaaS security is the sheer [volume] of apps and the consistent changes in permission and configurations [...] What we really need is a smart automated tool that gives us a clear real-time view of our entire SaaS landscape."
> — IT Manager/Director/VP, Manufacturing & Production

---

## Section 2: Sanctioned ≠ Secure: The Illusion of Oversight in SaaS Environments
Nearly three-quarters of respondents report having a policy that only permits the use of sanctioned SaaS applications, and that policy is “strictly controlled by the cybersecurity team.”

### Onboarding New SaaS Apps & Evaluating Risks
When adopting a new SaaS app, the majority (82%) rely on internally led audits to evaluate risks. To lead these assessments, 37% use industry frameworks, while 34% use proprietary risk assessment tools.

### SaaS Security Compliance Approaches
- **Manual SaaS compliance audits (regular):** 30% (up from 21% in 2024)
- **Manual SaaS compliance audits (ad-hoc):** 22% (up from 14% in 2024)
- **Continuous SaaS compliance assessment (SSPM):** 43% (down from 57% in 2024)

---

## Section 3: The SaaS Security Org Chart: Who Owns What
Most organizations in the survey demonstrate a clear commitment to specialized cybersecurity functions. Nearly two-thirds (65%) maintain a dedicated Cloud Security Team, and over half (55%) have a SaaS Security Team.

### Shared Responsibilities
When it comes to security responsibility, many organizations take a decentralized approach to SaaS security. 43% of respondents say that within their organization, the business owner of the SaaS app takes full responsibility, while 41% report that the cybersecurity team and the business owner share responsibility.

> "The real game-changer I've seen? When security teams stop talking tech and start speaking business... That's the shift — from handing down edicts to solving problems together."
> — Vishal Chawla, CEO & Founder, BluOcean Cyber

---

## Section 4: Good Enough or Just Lucky? The Cost of SaaS Security Tradeoffs
More than half (52%) rely on point-in-time compliance audits. While quarterly or pre-deployment audits may seem sufficient, they tend to leave large gaps in visibility since SaaS apps are dynamic environments.

### Tooling Consolidation vs. Specialization
SSPM is steadily gaining traction across industries. Notably, 42% of organizations report having implemented a dedicated, productized SSPM solution. However, 38% prefer to consolidate with security service edge (SSE) solutions, even if they don’t offer in-depth SaaS security capabilities.

---

## Section 5: Secure in Theory, Breached in Practice
75% of organizations experienced a SaaS-related security incident in the past year, a 44-point increase over 2024. However, 91% of teams say they’re very confident in their data security. The most common reason for this high confidence is trust in their SaaS provider (53%).

> "They have confidence because they think they've outsourced the risk. But they may not have thought about how the risk is just transferred to this other entity... That Pandora box doesn't close."
> — Brian Wasko, Principal, Microsoft Security

---

## Section 6: AI and the New SaaS Security Agenda
61% of respondents anticipate more discussions about AI-powered efficiency, pointing to a growing interest in AI-enabled security monitoring and automation. 55% expect conversations around securing the use of AI and mitigating the risks it creates.

---

## Key Recommendations for 2026 and Beyond
1. **Gain Visibility and Control:** Apply the 80/20 rule; prioritize the critical 20% of apps that store 80% of your sensitive information.
2. **Clarify Ownership:** Establish and document ownership frameworks between business stakeholders and cybersecurity teams.
3. **Shift to Continuous Monitoring:** Replace periodic reviews with continuous monitoring that catches issues as they emerge.
4. **Prioritize Mission-Critical Apps:** Use AI to identify risks and monitor continuously to triage alerts.
5. **Augment SSE with SSPM:** Integrate a dedicated SSPM solution that extends protection beyond access control to SaaS.
6. **Trust, But Verify:** Conduct routine assessments of app configurations, identity entitlements, and external integrations.
7. **Govern AI Identities:** Inventory AI usage, enforce least privilege, and ensure AI follows the same access controls as human users.

---

## Final Thoughts
The path to effective SaaS security isn’t more complexity; it’s clarity, depth, and continuous action. As organizations embrace SaaS as the backbone of their operations and the threat landscape continues to intensify, the time to move from reactive fixes to proactive programs is now.

---

## Methodology & Demographics
- **Total Respondents:** 803
- **Research Period:** March 15 – April 15, 2025
- **Geography:** 60% US, 12% UK, 11% Germany, 9% Australia, 8% Japan.
- **Industry:** 30% IT Services, 15% Manufacturing, 9% Finance/Insurance, 9% Software.
- **Role:** 61% hold senior IT-oriented leadership positions.

---

## About AppOmni
AppOmni is the leader in SaaS Security and enables customers to achieve secure productivity with their SaaS applications. The AppOmni Platform continuously scans SaaS APIs, configurations, and ingested audit logs to deliver complete data access visibility, secure identities and SaaS-to-SaaS connections, detect threats, prioritize insights, and simplify compliance reporting.