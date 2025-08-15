# 2025 State of Application Security
62% Ship Insecure Code — False Positives, Fatigue, and the Case for Expert Support
Survey Findings from IT and Security Leaders Across North America

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings: Gaps, Pressures, and Opportunities in Modern AppSec](#key-findings-gaps-pressures-and-opportunities-in-modern-appsec)
- [AppSec Delays Product Velocity](#appsec-delays-product-velocity)
- [OWASP Gaps Leave Teams Exposed](#owasp-gaps-leave-teams-exposed)
- [Detection Still Takes Too Long](#detection-still-takes-too-long)
- [Job Security Tied to AppSec Risk](#job-security-tied-to-appsec-risk)
- [AppSec Budgets Don’t Match the Risk](#appsec-budgets-dont-match-the-risk)
- [Perimeter Still Wins Out](#perimeter-still-wins-out)
- [Security Shortcuts Still Happen](#security-shortcuts-still-happen)
- [Security Left Behind in the SDLC](#security-left-behind-in-the-sdlc)
- [Critical AppSec Work Goes Undone](#critical-appsec-work-goes-undone)
- [Noise in the System](#noise-in-the-system)
- [Why Outsourcing AppSec Is on the Rise](#why-outsourcing-appsec-is-on-the-rise)
- [What’s Fueling the Shift to Expert Help](#whats-fueling-the-shift-to-expert-help)
  - [Data-Driven Insights](#data-driven-insights)
  - [More Signal, Less Noise](#more-signal-less-noise)
- [What Keeps Teams Up at Night](#what-keeps-teams-up-at-night)
  - [Top AppSec Concerns by Category](#top-appsec-concerns-by-category)
  - [Cloud and Configuration Gaps](#cloud-and-configuration-gaps)
  - [API and Token Exposure](#api-and-token-exposure)
  - [Mobile App Vulnerabilities](#mobile-app-vulnerabilities)
  - [Data Security and Visibility](#data-security-and-visibility)
  - [Authentication and Access Control](#authentication-and-access-control)
  - [Process Gaps and Human Error](#process-gaps-and-human-error)
- [Conclusion: A New Mandate for Modern AppSec](#conclusion-a-new-mandate-for-modern-appsec)
- [Survey Methodology](#survey-methodology)
- [About Cypress Data Defense](#about-cypress-data-defense)
  - [Why Choose Us?](#why-choose-us)

## Executive Summary

Application security has become a strategic priority for modern organizations, not just a technical responsibility. It is foundational for business, key to innovation, crucial to getting products to market quickly and securely. It continues to be one of the weakest links for bad actors to exploit for ransomware, IP Theft, and other malicious goals while average cost of a breach in the United States has ballooned to $9.48 million.[^1]

New research from TechStudio and Cypress Data Defense, based on responses from 250 IT and security leaders across North America, reveals a mounting crisis in application security.[^2] As release cycles accelerate and architectures grow more complex, the pressure on DevSecOps teams is intensifying.

Findings from the 2025 State of Application Security Survey uncover widespread challenges, from frequent false positives and insecure code releases to understaffed teams and overwhelmed tools. Even as more teams aim to involve security earlier in development, most still wait until the final stages. This leaves critical risks unaddressed until it’s often too late. And with AI apps on the rise, open source-generated code and malicious use of AI tools by hackers will make organizations more vulnerable to exploitation. Teams are constrained, struggling with visibility, and worried about fallout from preventable breaches often without the resources to expand headcount or deliver securely at speed. False alerts create a lot of noise and distractions but surprisingly offer opportunity to bolster security.

> The stakes are high. 60 percent say security issues are more likely to delay releases than bugs. Nearly 80 percent are worried about job loss after a breach. And 83 percent are open to outsourcing application security to get the help they need.

This report outlines the true state of AppSec and how expert partners like Cypress Data Defense can deliver critical support and close key security gaps.

## Key Findings: Gaps, Pressures, and Opportunities in Modern AppSec

This data highlights the scale of challenges facing AppSec teams, from insecure code to team burnout, and where organizations see opportunities for external support.

![Chart showing 62% of companies admit to shipping insecure code](https://example.com/image1.png)
![Chart showing false positives eroding trust in security tools](https://example.com/image2.png)
![Chart showing security is still bolt-on, not built-in](https://example.com/image3.png)
![Chart showing teams crave more time for high-value AppSec tasks](https://example.com/image4.png)
![Chart showing 83% of companies are open to AppSec outsourcing](https://example.com/image5.png)

## AppSec Delays Product Velocity

Anyone who doubts the critical role that application security now plays in bringing products to market should consider this: security issues are more likely to delay launches than feature bugs. In fact, 60% of respondents cited security as the top cause of delay, reinforcing the need to involve AppSec earlier and more consistently across the SDLC.

Delays often stem from late-stage discovery of vulnerabilities during static or dynamic scans, which require rework and retesting. Embedding security at the design and coding phases, through practices like secure code reviews, threat modeling, and integrated scanning, can reduce bottlenecks and improve release velocity. If in-house security efforts are impeding delivery, as this data suggests, organizations may need to augment capacity with external AppSec expertise.

![Bar chart comparing security issues (60%) vs. feature bugs (40%) as causes for product launch delays](https://example.com/image6.png)

60% say security issues are more likely to delay product launches than feature bugs, highlighting how security has become a major factor in delivery timelines, and why proactive AppSec must be built into the development process.

## OWASP Gaps Leave Teams Exposed

Security teams are aware of the rising threat landscape, but their ability to respond remains uneven. Just over half of respondents (51%) say they fully address and actively monitor OWASP Top 10 threats. Nearly as many (46%) admit they are still in the improvement phase. These figures highlight a widespread maturity gap, one that leaves many organizations vulnerable to well-known attack vectors. With OWASP (Open Worldwide Application Security Project) serving as a foundational benchmark for secure development, incomplete coverage underscores the need for more consistent practices, deeper training, and better AppSec support.

Failing to fully address OWASP risks isn’t just a technical issue, it translates directly into business liability. According to IBM’s 2024 Cost of a Data Breach report, organizations with mature DevSecOps practices saved an average of $1.76 million per breach, reinforcing the value of proactive AppSec investment.[^3]

![Pie chart showing preparedness against OWASP Top 10 threats: 51% Fully addressed and actively monitored, 46% Partially addressed, ongoing improvement, 3% Acknowledged, but not fully addressed](https://example.com/image7.png)

Only 51% of organizations report that OWASP Top 10 threats are fully addressed and actively monitored, while 46% are still in the improvement phase. This underscores a maturity gap that creates real exposure. Cypress’s hybrid approach to AppSec can help teams close that gap.

## Detection Still Takes Too Long

While breach detection times have improved slightly in recent years, they remain unacceptably long. Just 43% of security teams believe they would detect a breach within a week. The majority say it could take a month or more, ample time for threat actors to escalate privileges, exfiltrate data, or tamper with operations. This detection lag puts customers, employees, and partners at heightened risk and reinforces the need for continuous monitoring and real-time alerting across environments.

> “Security logging for cloud instances isn’t implemented, delaying detection.”
>
> — Director of Technology, Financial Services, U.S.

![Bar chart showing breach detection times: 54% Within a month, 43% Within a week, 3% Within six months](https://example.com/image8.png)

Nearly 43% believe their team would detect a breach within a week, while 54% estimate it would take up to a month. This lag in detection reinforces the need for continuous AppSec monitoring and alerting.

## Job Security Tied to AppSec Risk

The inevitability of an application-level cyberattack and ongoing gaps in AppSec maturity are fueling concern among IT and security leaders, many of whom worry they’ll be held accountable if something goes wrong. Nearly 80% of respondents expressed concern that a security incident could cost them their job: 62% admitted they are worried about being let go, while another 17% said it was a possible outcome. This level of anxiety highlights the personal risks tied to AppSec and reinforces the need for trusted, expert support.

![Pie chart showing concern about job loss due to cyberattack: 62% Yes, 21% No, 17% Maybe](https://example.com/image9.png)

62% of respondents admit they’re worried about losing their job due to an AppSec incident, illustrating the high-stakes pressure security leaders and engineers face, and the importance of trusted third-party support.

## AppSec Budgets Don’t Match the Risk

Despite the growing risk of cyberattacks, many organizations are still underinvesting in application security. Nearly 90% of respondents say their teams allocate just 11% to 20% of their overall security budgets to AppSec, with none reporting investments above 20%. While this might appear sufficient at first glance, it falls short when considering that a significant share of breaches originate from application-layer vulnerabilities. As application threats escalate, budget alignment remains a critical gap.

![Bar chart showing allocation of security budget to AppSec: 1% Less than 5%, 10% 5% to 10%, 49% 11% to 15%, 40% 16% to 20%, 0% More than 20%](https://example.com/image10.png)

89% of respondents allocate between 11% and 20% of their security budget to application security. This reflects growing recognition of AppSec as a critical investment area. However, very few exceed that threshold. This shows most teams remain resource-constrained.

## Perimeter Still Wins Out

Organizations continue to prioritize perimeter defenses over application-layer protections. More than one-third of respondents say network security receives more budget than AppSec, and nearly 20% point to cloud security as a higher priority. It’s a concerning trend, given that application flaws account for 43% of breaches, leaving critical gaps where attackers are most likely to strike.

![Bar chart showing areas receiving more budget than Application Security: 36% Network Security, 20% Cloud Security, 19% AI Security, 17% Endpoint Security, 8% Email Security](https://example.com/image11.png)

36% of respondents say network security receives more funding than application security, while 20% say cloud security does. This suggests that many organizations still prioritize traditional perimeter defenses over application-layer protection. That’s a concerning trend, given that application flaws account for 43% of breaches.

> “Encrypted or hidden data can look suspicious to scanners.”
>
> — Chief Information Security Officer, Financial Services, U.S.

## Security Shortcuts Still Happen

The pressure to bring apps to bear quickly in highly competitive markets has pushed an alarming number of security practitioners to do what should be the unthinkable, knowingly ship insecure code. A striking 63% of respondents admit their organization has knowingly released insecure code to meet a deadline. Another 22% aren’t even sure, highlighting a breakdown in oversight and a culture where speed is still prioritized over security.

![Pie chart showing if companies knowingly pushed insecure code: 63% Yes, 22% Not sure, 15% No](https://example.com/image12.png)

63% of respondents say their organization has knowingly released insecure code to meet a deadline, and 22% say they aren’t sure. The data is clear that delivery pressures are still winning out over risk mitigation in many teams.

> “Outdated web frameworks with unpatched security holes concern me.”
>
> — Enterprise Cloud Security Architect & CISO, Financial Services, U.S.

## Security Left Behind in the SDLC

While many organizations recognize that strong security practices can accelerate innovation and support business goals, too many still treat security as a bolt-on rather than a built-in component. Only 36% of teams involve security at the planning stage, while 57% wait until late testing or deployment. This late entry limits risk reduction opportunities and prevents teams from fully benefiting from a true partnership with security.

Integrating security from the outset of the Software Development Life Cycle (SDLC) can improve release velocity, reduce risk exposure, and lower remediation costs, especially as systems grow more complex.

> “Unsecured APIs in mobile backend services are a big worry.”
>
> — Director of Technology, Education, U.S.

> “The pressure to ship quickly means perfect code is useless if the server is misconfigured.”
>
> — Director, Information Technology Operations, Retail, U.S.

![Bar chart showing when security is involved in SDLC: 57% Before deployment, 36% Planning, 7% After deployment](https://example.com/image13.png)

Only 36% of respondents involve security during the planning stage of the SDLC, while 57% wait until just before deployment. This delay misses key opportunities to shift security left and reduce costly rework. Earlier integration could dramatically improve both risk posture and release velocity.

## Critical AppSec Work Goes Undone

Even organizations with strong security teams and sizable budgets struggle to keep up with essential AppSec tasks. Half of respondents say their teams lack the time or resources for secure code reviews, one of the most fundamental safeguards against releasing vulnerable applications. Other critical activities such as security unit testing (42%) and threat modeling (36%) are also deprioritized due to internal bandwidth constraints. These gaps highlight the need for expanded AppSec support across all stages of the development cycle.

![Bar chart showing desired AppSec activities: 50% Secure code reviews, 42% Security unit testing, 36% Threat modeling, 31% Pen testing, 12% Managing scanners](https://example.com/image14.png)

50% of respondents say they lack time for secure code reviews, 42% cite unit testing, and 36% mention threat modeling. These gaps point to a widespread need for AppSec support across all stages of the development lifecycle. Cypress’s service model helps teams execute these high-impact activities without straining internal bandwidth.

## Noise in the System

False positives remain one of the most persistent frustrations in application security. 58% of respondents report encountering them frequently, with 11% saying they happen constantly. These alerts can overwhelm teams, dilute attention from real threats, and undermine trust in security tools—ultimately delaying triage and resolution.

Yet there’s a silver lining: many teams are learning from these noisy signals. Repeated false positives have prompted stronger collaboration, improved tuning processes, and a sharper focus on what matters most. Outsourcing to partners who offer depth without disrupting agility becomes a strategic advantage.

![Bar chart showing frequency of false positives from security scanners: 58% Sometimes, 21% Rarely, 12% All the time, 11% Never](https://example.com/image15.png)

58% of respondents report frequent false positives from security scanners, and 11% say it happens all the time. The noise created by poorly tuned tools continues to drain time and attention. Cypress’s human-led validation approach helps teams focus on what truly matters.....actual risk.

## Why Outsourcing AppSec Is on the Rise

![Pie chart showing consideration for outsourcing AppSec: 83% Yes, 17% No](https://example.com/image16.png)

83% of respondents have considered outsourcing at least part of their application security program. This shows strong market readiness for managed AppSec solutions. Cypress is well positioned to meet this demand with scalable, expert-driven services.

Security burnout is real

Most security professionals—over 8 in 10—say they are open to outsourcing parts of their AppSec program. The reason? Internal teams are maxed out, and false positives are a key source of friction, distracting teams from real threats.

## What’s Fueling the Shift to Expert Help

###