# State of SaaS Security 2025 Report

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
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
We’re proud to share AppOmni’s third annual The State of SaaS Security Report. SaaS continues its enterprise transformation with a compounded annual growth rate of 20% between 2025 to 2032. The stakes for securing these platforms have never been higher. Today, nearly every organization relies on SaaS to operate, and attackers know it.

In the past year, SaaS security, together with concerns around the secure use of AI, has moved from a niche security initiative to a boardroom imperative. In his 2024 letter, JPMorgan’s CISO, Pat Opet, explicitly named SaaS vulnerabilities as an area of utmost importance, noting the industry’s increasing dependence on third-party providers and the growing threat of SaaS attacks. The 2025 Verizon Data Breach Investigations Report (DBIR) called out a doubling of breaches involving third-party applications stemming from misconfigured SaaS platforms and unauthorized integrations, particularly those exploited by threat actors through scanning and credential stuffing.

SaaS is now one of the most actively targeted layers of the enterprise attack surface, and yet, it remains one of the least proactively defended. Adversary activity in SaaS apps prompted the government’s watchdog—the Cybersecurity and Infrastructure Security Agency (CISA)—to issue a Binding Directive (BOD 25-01) to public sector agencies to secure their critical SaaS environments and urge the private sector to do the same.

At AppOmni, we see this play out every day. Our SaaS threat research team has published multiple investigations this past year alone, exposing critical misconfigurations and vulnerabilities across major SaaS platforms like Salesforce, ServiceNow, NetSuite, and Microsoft 365. These aren’t theoretical risks—they’re real-world exposures impacting the biggest brands in the world.

This year’s State of SaaS Security report is based on insights from over 800 global security leaders. Their responses reveal a troubling disconnect: 91% of respondents express confidence in their SaaS security posture, yet 75% experienced a security incident in the past year—many involving the very issues our team and other industry experts have warned about. 89% of those impacted by incidents or breaches believed they had “appropriate visibility” into their environments at the time.

This is the illusion of control, and it’s one of the most dangerous challenges facing security teams today. People are busy. Teams rely on dashboards and implicitly trust platform vendors. But visibility alone is not security. And trust without verification is not a strategy.

What we need now is clarity. SaaS security must evolve from an ad hoc, reactive process to a mature, repeatable discipline. That means embracing continuous monitoring over point-in-time audits, assigning clear ownership, and protecting the entire ecosystem, including users, configurations, and app-to-app connections alike.

This report is both a snapshot of where the industry stands and a call to action. The attacks are already here. The question is: Are you ready?

— Brendan O’Connor, CEO & Co-Founder, AppOmni

---

## Executive Summary
As organizations scale their use of cloud applications, they're also expanding their attack surface. The State of SaaS Security 2025 Report reveals a sharp increase in SaaS security incidents, a rising complexity in app ecosystems, and a persistent disconnect between perceived visibility and actual risk reduction.

As SaaS adoption accelerates, so too does the urgency for security teams to close the gap between visibility and actual control. This report set out to understand the realities behind that gap—and to challenge assumptions about maturity, confidence, and level of control.

**This report investigates:**
- Are security teams keeping pace with the rising complexity and interconnectivity of SaaS ecosystems?
- What does “confidence” in SaaS security really mean, and is it justified?
- How are organizations operationalizing SaaS security—or failing to?
- Is the security mindset evolving fast enough to meet the moment?
- How are organizations responding to emerging challenges like AI governance and regulatory scrutiny?

Our findings point to a simple yet powerful truth: SaaS security doesn’t have to be complex, but strategies do need to adapt to meet the increased threats. With the right tools and clear ownership, organizations can transform reactive processes into scalable, repeatable programs.

---

## Key Findings
- **SaaS Under Siege**: 75% of organizations experienced a SaaS-related security incident in the past year, a 33% increase over 2024.
- **Visibility ≠ Security**: 89% of compromised organizations believed they had “appropriate visibility” into their SaaS environment.
- **SaaS Risks Don’t Wait for Audits**: Only 43% have implemented continuous or near real-time oversight.
- **Hope Isn’t a Security Strategy**: 53% of confident respondents base their security posture on trust in SaaS vendors, rather than internal validation.
- **The Security Mirage**: 91% of organizations express confidence in their SaaS security posture, yet 75% experienced a SaaS incident.
- **Old Strategies, New Threats**: 52% continue to use periodic reviews to assess SaaS risk.
- **Everyone’s Job = No One’s Job**: Only 16% assign SaaS security solely to security teams, while 43% leave it to business units.
- **Securing SaaS with Duct Tape**: Just 13% of respondents currently use a dedicated SaaS Security Posture Management (SSPM) solution.
- **Can We Govern AI or Will It Govern Us?**: 61% of respondents expect AI to dominate SaaS security discussions in the coming year.
- **Breached by Basics**: 41% of incidents stemmed from permission issues, while 29% resulted from misconfigurations.

---

## Section 1: The SaaS Surge: Growing Usage But Rising Security Incidents
Over the last year, data reveals significant SaaS security concerns. Specifically, 41% of those surveyed identified vulnerabilities in SaaS user permissions, while 29% reported incidents stemming from SaaS application misconfigurations.

![Chart showing SaaS security incidents: 41% user permissions, 29% misconfiguration, 26% data exposure, 25% human error, 23% cyber-attack, 22% insider threat]

Our data shows that 75% of respondents have experienced a SaaS security incident or data breach in the past 12 months. This is a substantial 33% increase compared to The State of SaaS Security 2024 Report.

### Concerns
Data security remains a paramount concern. A majority of respondents, at 57%, cited data breaches and the potential loss of intellectual property as their primary worry. 

### Deployed SaaS Applications
Most organizations are using dozens or even hundreds of SaaS applications. Over half (57%) of respondents say they’re aware of 50 or more SaaS apps deployed in their organization’s environment. Over a third (40%) report 100 or more apps.

> "Our biggest headache with SaaS security is the sheer volume of apps and the consistent changes in permission and configurations [...] What we really need is a smart automated tool that gives us a clear real-time view of our entire SaaS landscape." — IT Manager/Director/VP, Manufacturing & Production

---

## Section 2: Sanctioned ≠ Secure: The Illusion of Oversight in SaaS Environments
Nearly three-quarters of respondents report having a policy that only permits the use of sanctioned SaaS applications, and that policy is “strictly controlled by the cybersecurity team.”

### Policies and Controls in Place for App Adoption
- **73%**: Only sanctioned apps are permitted by our security policy, strictly enforced by cybersecurity.
- **22%**: Security policy restricts app use to sanctioned applications, but enforcement is not strict.
- **2%**: Each business unit is responsible for their own SaaS apps adoption and management.

### SaaS App Risk Evaluation Strategies
When adopting a new SaaS app, the majority (82%) rely on internally led audits to evaluate risks. 

### SaaS Security Compliance Approaches
For continuous monitoring of third-party SaaS applications and compliance, 43% use a SaaS security posture management (SSPM) suite.

---

## Section 3: The SaaS Security Org Chart: Who Owns What
Most organizations in the survey demonstrate a clear commitment to specialized cybersecurity functions. Nearly two-thirds (65%) maintain a dedicated Cloud Security Team, and over half (55%) have a SaaS Security Team.

### Shared Responsibilities
Should ownership be everyone's problem, or should a specific team be in charge? Strong executive support doesn’t always translate to clearly defined stakeholders.

- **Business Owner of the SaaS App/Platform**: 43%
- **Business Owner & Cybersecurity Team**: 41%
- **Cybersecurity Team**: 16%

> "We've adopted this tagline that many have: cybersecurity is a shared responsibility. If somebody sees something, they say something. We reward them with a cybersecurity challenge coin." — Dennis Tomlin, CISO, Multnomah County

---

## Section 4: Good Enough or Just Lucky? The Cost of SaaS Security Tradeoffs
While quarterly or pre-deployment audits may seem sufficient, they tend to leave large gaps in visibility since SaaS apps are dynamic environments.

### Time spent per week reviewing SaaS security risks
- **45%**: 2 to 5 hours
- **31%**: 5 to 8 hours
- **10%**: More than 8 hours
- **15%**: 0 to 2 hours

### Tooling Consolidation vs. Specialization
SSPM is steadily gaining traction. Notably, 42% of organizations report having implemented a dedicated, productized SSPM solution.

---

## Section 5: Secure in Theory, Breached in Practice
The most common reason for high confidence is trust in their SaaS provider (53%). However, 75% of organizations experienced a SaaS-related security incident in the past year.

> "They have confidence because they think they've outsourced the risk. But they may not have thought about how the risk is just transferred to this other entity who now has all the other customers’ data as well as their own." — Brian Wasko, Principal, Microsoft Security

---

## Section 6: AI and the New SaaS Security Agenda
61% of respondents anticipate more discussions about AI-powered efficiency, pointing to a growing interest in AI-enabled security monitoring and automation.

> "If you’re building an AI agent, you're going to have direct connections to make API calls... And unless that LLM model is yours or from an approved tenant of your own organization, you're basically giving your data away." — Ernesto Pereira, Information Security Manager, Episcopal Health Services

---

## Key Recommendations for 2026 and Beyond
1. **Gain Visibility and Control**: Implement effective security tools that enforce policy alignment and detect misconfigurations. Apply the 80/20 rule to prioritize critical apps.
2. **Clarify and Codify Ownership**: Establish and document ownership frameworks between business stakeholders and cybersecurity teams.
3. **Shift to Continuous Monitoring**: Replace periodic reviews with continuous monitoring that catches issues as they emerge.
4. **Prioritize Mission-Critical Apps**: Use AI to identify risks and monitor continuously to triage alerts.
5. **Augment SSE with SSPM**: Integrate a dedicated SSPM solution that extends protection beyond access control into identity governance and threat detection.
6. **Trust, But Verify**: Conduct routine assessments of app configurations and external integrations.
7. **Treat AI Like Any Other Identity**: Govern access for AI agents and monitor usage continuously.

---

## Final Thoughts
The path to effective SaaS security isn’t more complexity; it’s clarity, depth, and continuous action. As organizations embrace SaaS as the backbone of their operations, the time to move from reactive fixes to proactive programs is now.

---

## Methodology & Demographics
UserEvidence conducted comprehensive research on behalf of AppOmni.
- **803 total respondents** across quantitative survey.
- **85%** are final decision-makers in IT/security purchasing.
- **Research period**: March 15 through April 15, 2025.
- **Geography**: United States (60%), UK (12%), Germany (11%), Australia (9%), Japan (8%).
- **Size**: 74% work for companies with 2,000+ employees.

---

## About AppOmni
AppOmni is the leader in SaaS Security and enables customers to achieve secure productivity with their SaaS applications. With AppOmni, security teams and SaaS application owners quickly secure their mission-critical and sensitive data from attackers and insider threats.

The AppOmni Platform continuously scans SaaS APIs, configurations, and ingested audit logs to deliver complete data access visibility, secure identities and SaaS-to-SaaS connections, detect threats, prioritize insights, and simplify compliance reporting.