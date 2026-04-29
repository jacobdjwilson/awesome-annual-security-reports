# 2025 State of Application Security

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
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
- [What Keeps Teams Up at Night](#what-keeps-teams-up-at-night)
- [Conclusion](#conclusion)
- [Survey Methodology](#survey-methodology)
- [About Cypress Data Defense](#about-cypress-data-defense)

---

## Executive Summary

Application security has become a strategic priority for modern organizations, not just a technical responsibility. It is foundational for business, key to innovation, crucial to getting products to market quickly and securely. It continues to be one of the weakest links for bad actors to exploit for ransomware, IP Theft, and other malicious goals while average cost of a breach in the United States has ballooned to $9.48 million.[^1]

New research from TechStudio and Cypress Data Defense, based on responses from 250 IT and security leaders across North America, reveals a mounting crisis in application security.[^2] As release cycles accelerate and architectures grow more complex, the pressure on DevSecOps teams is intensifying.

Findings from the 2025 State of Application Security Survey uncover widespread challenges, from frequent false positives and insecure code releases to understaffed teams and overwhelmed tools. Even as more teams aim to involve security earlier in development, most still wait until the final stages. This leaves critical risks unaddressed until it’s often too late. And with AI apps on the rise, open source-generated code and malicious use of AI tools by hackers will make organizations more vulnerable to exploitation. Teams are constrained, struggling with visibility, and worried about fallout from preventable breaches often without the resources to expand headcount or deliver securely at speed. False alerts create a lot of noise and distractions but surprisingly offer opportunity to bolster security.

The stakes are high. 60 percent say security issues are more likely to delay releases than bugs. Nearly 80 percent are worried about job loss after a breach. And 83 percent are open to outsourcing application security to get the help they need.

This report outlines the true state of AppSec and how expert partners like Cypress Data Defense can deliver critical support and close key security gaps.

---

## Key Findings

This data highlights the scale of challenges facing AppSec teams, from insecure code to team burnout, and where organizations see opportunities for external support.

- **62%** of companies admit to shipping insecure code
- **False positives** are eroding trust in security tools
- **Security is still bolt-on**, not built-in
- **Teams crave more time** for high-value AppSec tasks
- **83%** of companies are open to AppSec outsourcing

---

## AppSec Delays Product Velocity

Anyone who doubts the critical role that application security now plays in bringing products to market should consider this: security issues are more likely to delay launches than feature bugs. In fact, 60% of respondents cited security as the top cause of delay, reinforcing the need to involve AppSec earlier and more consistently across the SDLC.

Delays often stem from late-stage discovery of vulnerabilities during static or dynamic scans, which require rework and retesting. Embedding security at the design and coding phases, through practices like secure code reviews, threat modeling, and integrated scanning, can reduce bottlenecks and improve release velocity. If in-house security efforts are impeding delivery, as this data suggests, organizations may need to augment capacity with external AppSec expertise.

![Chart: What’s more likely to delay your next product launch—security issues or feature bugs? 60% Security issues, 40% Feature bugs.]

---

## OWASP Gaps Leave Teams Exposed

Security teams are aware of the rising threat landscape, but their ability to respond remains uneven. Just over half of respondents (51%) say they fully address and actively monitor OWASP Top 10 threats. Nearly as many (46%) admit they are still in the improvement phase. These figures highlight a widespread maturity gap, one that leaves many organizations vulnerable to well-known attack vectors. With OWASP (Open Worldwide Application Security Project) serving as a foundational benchmark for secure development, incomplete coverage underscores the need for more consistent practices, deeper training, and better AppSec support.

Failing to fully address OWASP risks isn’t just a technical issue, it translates directly into business liability. According to IBM’s 2024 Cost of a Data Breach report, organizations with mature DevSecOps practices saved an average of $1.76 million per breach, reinforcing the value of proactive AppSec investment.[^3]

![Chart: How would you describe your organization’s preparedness against OWASP Top 10 threats? 51% Fully addressed and actively monitored, 46% Partially addressed, ongoing improvement, 3% Acknowledged, but not fully addressed.]

---

## Detection Still Takes Too Long

While breach detection times have improved slightly in recent years, they remain unacceptably long. Just 43% of security teams believe they would detect a breach within a week. The majority say it could take a month or more, ample time for threat actors to escalate privileges, exfiltrate data, or tamper with operations. This detection lag puts customers, employees, and partners at heightened risk and reinforces the need for continuous monitoring and real-time alerting across environments.

> “Security logging for cloud instances isn’t implemented, delaying detection.” — Director of Technology, Financial Services, U.S.

![Chart: If your app was breached today, how long would it take before someone noticed? 43% Within a week, 54% Within a month, 3% Within six months.]

---

## Job Security Tied to AppSec Risk

The inevitability of an application-level cyberattack and ongoing gaps in AppSec maturity are fueling concern among IT and security leaders, many of whom worry they’ll be held accountable if something goes wrong. Nearly 80% of respondents expressed concern that a security incident could cost them their job: 62% admitted they are worried about being let go, while another 17% said it was a possible outcome. This level of anxiety highlights the personal risks tied to AppSec and reinforces the need for trusted, expert support.

![Chart: Are you worried about getting fired because of an application level cyberattack? 62% Yes, 21% No, 17% Maybe.]

---

## AppSec Budgets Don’t Match the Risk

Despite the growing risk of cyberattacks, many organizations are still underinvesting in application security. Nearly 90% of respondents say their teams allocate just 11% to 20% of their overall security budgets to AppSec, with none reporting investments above 20%. While this might appear sufficient at first glance, it falls short when considering that a significant share of breaches originate from application-layer vulnerabilities. As application threats escalate, budget alignment remains a critical gap.

![Chart: What % of your overall security budget is allocated to application security? 1% Less than 5%, 10% 5% to 10%, 40% 11% to 15%, 49% 16% to 20%. 0% selected "More than 20%".]

---

## Perimeter Still Wins Out

Organizations continue to prioritize perimeter defenses over application-layer protections. More than one-third of respondents say network security receives more budget than AppSec, and nearly 20% point to cloud security as a higher priority. It’s a concerning trend, given that application flaws account for 43% of breaches, leaving critical gaps where attackers are most likely to strike.

![Chart: Which of the following areas currently receive more budget than Application Security in your organization? 36% Network Security, 20% Cloud Security, 19% AI Security, 17% Endpoint Security, 8% Email Security.]

> “Encrypted or hidden data can look suspicious to scanners.” — Chief Information Security Officer, Financial Services, U.S.

---

## Security Shortcuts Still Happen

The pressure to bring apps to bear quickly in highly competitive markets has pushed an alarming number of security practitioners to do what should be the unthinkable, knowingly ship insecure code. A striking 63% of respondents admit their organization has knowingly released insecure code to meet a deadline. Another 22% aren’t even sure, highlighting a breakdown in oversight and a culture where speed is still prioritized over security.

![Chart: Has your company ever knowingly pushed insecure code to meet a deadline? 63% Yes, 22% Not sure, 15% No.]

---

## Security Left Behind in the SDLC

While many organizations recognize that strong security practices can accelerate innovation and support business goals, too many still treat security as a bolt-on rather than a built-in component. Only 36% of teams involve security at the planning stage, while 57% wait until late testing or deployment. This late entry limits risk reduction opportunities and prevents teams from fully benefiting from a true partnership with security.

![Chart: When do you typically involve security in your SDLC? 36% Planning, 57% Before deployment, 7% After deployment.]

---

## Critical AppSec Work Goes Undone

Even organizations with strong security teams and sizable budgets struggle to keep up with essential AppSec tasks. Half of respondents say their teams lack the time or resources for secure code reviews, one of the most fundamental safeguards against releasing vulnerable applications. Other critical activities such as security unit testing (42%) and threat modeling (36%) are also deprioritized due to internal bandwidth constraints.

![Chart: Which AppSec activities do you wish your team had time or resources for? 50% Secure code reviews, 42% Security unit testing, 36% Threat modeling, 31% Pen testing, 12% Managing scanners.]

---

## Noise in the System

False positives remain one of the most persistent frustrations in application security. 58% of respondents report encountering them frequently, with 11% saying they happen constantly. These alerts can overwhelm teams, dilute attention from real threats, and undermine trust in security tools—ultimately delaying triage and resolution.

![Chart: How often do you get false positives from security scanners? 58% Frequently, 21% Sometimes, 12% Rarely, 11% All the time.]

---

## Why Outsourcing AppSec Is on the Rise

83% of respondents have considered outsourcing at least part of their application security program. This shows strong market readiness for managed AppSec solutions.

![Chart: Have you considered outsourcing any part of your Application Security program? 83% Yes, 17% No.]

---

## What’s Fueling the Shift to Expert Help

- The cost of a breach is too high to risk internal shortfalls
- A loss of customer trust or service disruption could damage the brand
- Security teams are already overextended across other IT functions
- Finding and retaining specialized AppSec talent is difficult and expensive
- Compliance requirements are becoming more complex and demanding
- Accelerated development cycles leave little time for thorough in-house reviews
- Organizations can’t afford to monitor application security 24/7
- Breach detection and response must keep pace with modern threats

---

## What Keeps Teams Up at Night

### Cloud and Configuration Gaps
- “Public or shared keys for cloud access are a big worry.”
- “Cloud misconfigurations caused by automation tools cause sleepless nights.”
- “Uncontrolled cloud console access risks unauthorized changes.”
- “Legacy cloud accounts with weak credentials keep me up.”

### API and Token Exposure
- “Authentication details exposed in URLs are a big concern.”
- “Broken API permissions allow unauthorized data access.”
- “API tokens stored insecurely in mobile apps pose a huge risk.”
- “Internal API endpoints lack proper authentication checks.”

### Mobile App Vulnerabilities
- “Sensitive info like passwords is stored in insecure logs.”
- “Authentication tokens exposed in mobile apps can be hijacked.”
- “No integrity checks for mobile app installation or updates is troubling.”
- “Insecure third-party SDKs in mobile apps can be exploited.”

### Data Security and Visibility
- “Weak password reset mechanisms allow attackers to bypass security checks.”
- “Serverless functions often run with overly broad permissions.”
- “No proper logout functionality leaves mobile sessions open.”
- “Poor session handling makes it easy for hackers to take over accounts.”
- “Sensitive data isn’t encrypted during transit.”
- “Non-encrypted S3 buckets for sensitive data are a big issue.”

### Process Gaps and Human Error
- “Developers at times skip security steps when in a hurry.”
- “Perfect code is useless if the server is set up wrong.”
- “AI-generated code might have hidden bugs.”
- “Putting off fixing problems can pile up.”

---

## Conclusion

The research is clear: AppSec teams are under pressure, under-resourced, and in need of better solutions. While automation and shift-left strategies remain important, the data shows there’s no substitute for context-aware security and expert support. Cypress’s hybrid approach with its EASy managed service offers a scalable path forward, delivering security leadership without the overhead of building it in-house.

---

## Survey Methodology

The 2025 State of Application Security survey was conducted in May 2025 by TechStudio, an Energize Marketing company, in partnership with Cypress Data Defense. It gathered insights from 250 IT and security leaders across North America. Respondents came from companies with 250 to 1,000 employees, with annual revenue between $50 million and $1 billion. The survey has a margin of error of ±5.7% at a 95% confidence level.

---

## About Cypress Data Defense

Cypress Data Defense is a leading provider of application security and network security solutions. Founded by a team of cybersecurity experts, our mission is to empower organizations to deliver secure, high-quality software without compromising speed or innovation.

**Contact Information:**
14143 Denver West Pkwy, Suite 100, Golden, CO 80401
PH: 720.588.8133
Email: info@cypressdatadefense.com
Website: www.cypressdatadefense.com

---

[^1]: Source: IBM 2024 Cost of a Data Breach Report
[^2]: Source: 2025 State of Application Security Survey, conducted by TechStudio, an Energize Marketing company, in partnership with Cypress Data Defense.
[^3]: Source: IBM 2024 Cost of a Data Breach Report