# The State of the Application Security Workflow
## Envisioning the Next Frontier: Transforming Application Security Workflows
### 2025 Report

© Copyright 2025 Kodem Security, Inc. All Rights Reserved.

## Table of Contents
- [A Message from Our CEO](#a-message-from-our-ceo)
- [State of Application Security Workflow](#state-of-application-security-workflow)
  - [Introduction](#introduction)
  - [Key findings](#key-findings)
- [Application Security Workflows Today](#application-security-workflows-today)
  - [Mapping the current landscape](#mapping-the-current-landscape)
  - [Workflow bottlenecks and key pain points](#workflow-bottlenecks-and-key-pain-points)
- [Adapting Application Security to Modern Environments](#adapting-application-security-to-modern-environments)
  - [Shifting from traditional to modern security workflows](#shifting-from-traditional-to-modern-security-workflows)
  - [The rise of runtime](#the-rise-of-runtime)
  - [Embracing automation for security workflows](#embracing-automation-for-security-workflows)
- [Building a Resilient Security Posture](#building-a-resilient-security-posture)
  - [Proactive vs. reactive approaches](#proactive-vs-reactive-approaches)
- [Looking forward: Goals for 2025](#looking-forward-goals-for-2025)
- [Final Thoughts](#final-thoughts)
- [Demographics](#demographics)
- [Methodology](#methodology)

---

## A Message from Our CEO

I’m honored to share the journey that led us to build Kodem. Over the years, our team has experienced cybersecurity from every angle—researching code, defending critical systems, and discovering vulnerabilities. We learned a crucial lesson: while digital innovation accelerates, application security often lags behind. Kodem was born from that realization, fueled by our firsthand understanding of protecting critical assets under relentless pressure—and our conviction that, with the right approach, organizations can stay ahead of emerging threats.

We created this report to spotlight the security pioneers who refuse to settle for outdated methods. Across every industry, there are bold leaders shaping a new frontier of application security. By sharing their insights, we hope to amplify their voices and spark collaborative dialogue—one that disrupts complacency and illuminates the future of AppSec.

At Kodem, we aim to be catalysts for transformation, bridging the gap between security theory and practical deployment. Driven by a commitment to solve today’s toughest challenges and anticipate tomorrow’s threats, our mission extends beyond delivering tools. We strive to empower teams to innovate confidently, knowing their applications are safeguarded from code to runtime.

None of this would be possible without the remarkable community supporting our mission. To everyone who participated in our survey, and to our customers, partners, and investors—thank you for your trust and collaboration. Your insights shape this report and inspire us to continually push the boundaries of what’s possible in application security.

I hope you find the report both insightful and inspiring as you chart your own path toward stronger application security.

Aviv Mussinger
Co-Founder & CEO

---

## State of Application Security Workflow

### Introduction
Today’s application security landscape presents a fundamental challenge: expanding attack surfaces and rapid development cycles outpace traditional security approaches. Application security teams face a fundamental mismatch to secure cloud-native architectures and API-driven integrations while maintaining development velocity.

> However, these workflows are often plagued by inefficiencies, fragmented toolsets and manual processes that struggle to keep pace with an evolving threat landscape.

This report explores the state of application security workflows, drawing insights from a survey of Chief Information Security Officers (CISOs), Application Security (AppSec) leaders and security professionals across diverse industries. The research reveals how organizations address security challenges through strategic approaches, while showcasing how automation and contextual intelligence optimize security workflows.

The application security workflow consists of five key stages: discovery, triage, remediation, reporting and governance. This report examines how organizations approach each stage and where they face the greatest challenges.

![Workflow stages: Discover, Triage, Remediate, Report, Govern]

By illuminating the key gaps in application security practices - and highlighting emerging trends and best practices - this report aims to equip readers with actionable insights that can help future-proof their security programs. Kodem, the publisher of this report, purpose built a platform that bridges these gaps by unifying shift-left strategies with runtime monitoring and protection.

### Key findings
The following critical insights provide a snapshot of the current state of application security workflows and the trends shaping the future:

- **78% Fragmentation in security toolsets**: Respondents use more than five different tools in their application security stack, leading to inefficiencies and fragmented visibility.
- **62% Remediation is the largest bottleneck**: Respondents cite critical vulnerabilities taking more than four weeks to fix, with teams overwhelmed by poor prioritization of risks.
- **73% Shift-left adoption is growing but incomplete**: Organizations have implemented shift-left security, but only half successfully integrated these practices into developer workflows.
- **45% Runtime security is gaining traction**: Growth in adoption of runtime-based solutions which emphasizes the need to address vulnerabilities missed during development.
- **84% The push for automation**: Security leaders view automation for triaging, risk analysis and CI/CD integration as essential, though 95% express concerns about “garbage in, garbage out” highlighting the need for contextual insights.
- **55% Contextual intelligence is the future**: Organizations leveraging contextual insights from exploitability, affected assets and environment risk—achieve 55% faster remediation and improved security-development collaboration.

---

## Application Security Workflows Today

### Mapping the current landscape
Application security teams struggle with fragmented tooling and visibility as development accelerates, driving the need for more unified and contextual security approaches.

**74%** of respondents say managing application security across development, CI/CD pipelines and production environments is their top operational challenge.

Despite advances in security tooling, many organizations find it difficult to keep pace with accelerating release cycles. While 73% of organizations have integrated some form of shift-left security, only 35% believe these practices effectively reduce risk at scale.

Security tooling adoption may be growing, but many workflows remain disjointed. For instance, 54% of security leaders still lack a unified platform to manage vulnerabilities from code to runtime, causing redundancies and inefficiencies.

> "When each business unit adopts its own AppSec stack, the result is a fragmented landscape that defies centralized oversight, making security management at scale nearly impossible."
> — Alok Sinhasan, Head of Cybersecurity Engineering and Solutions at Logitech

### Workflow bottlenecks and key pain points

> "ASPMs make sense, but they don’t solve the need for a unified platform. Organizations are still managing five different tools to ensure they don’t leave any gap."
> — Nir Rothenberg, CISO at Rapyd

**The Persistence of Remediation as the Primary Bottleneck**
Remediation remains a critical pain point. Even when vulnerabilities are identified early, fixing them involves navigating dependencies, securing developer buy-in, and addressing organizational silos.

It takes 22 days to remediate critical vulnerabilities. 89% of respondents are not satisfied with this SLA, claiming the attack window is open widely for attackers during this period of time. 8% of respondents reported a compromise attempt during this window.

Delays with remediation are due to unclear prioritization or lack of developer alignment. 77% of respondents express dissatisfaction with the way they interface with engineering teams, citing excessive time spent on risk prioritization and justification.

**Alert Fatigue and Inefficiencies in Vulnerability Triage**

> "Triaging is one of the most frustrating processes security engineers face. It is manual, inaccurate, and leaves security teams unable to keep the pace with development."
> — Ophir Oren, Cyber Security Innovation at Bayer

Modern security tools generate high volumes of false-positive security alerts, causing alert fatigue and slowing response to real threats.
- **87%**: Respondents are overwhelmed by the volume of security alerts.
- **45%**: False positive alerts waste valuable engineering and security resources.
- **58%**: Respondents express skepticism about their vulnerability scanning tools’ prioritization accuracy.

**Balancing Manual Processes with Automation**
Despite automation’s importance for security scaling, organizations heavily rely on manual vulnerability triage and runtime protection. 77% of respondents rely on manual triage process, using tools such as CVSS and EPSS scores. Most acknowledge these metrics don’t accurately reflect actual risk.

---

## Adapting Application Security to Modern Environments

### Shifting from traditional to modern security workflows
Organizations are shifting from traditional security models to adaptive frameworks, as static scanning proves insufficient for modern threat detection.

- **71%**: Respondents report their current workflows are ill-suited for the demands of cloud-native applications.
- **2.3x**: More security incidents in hybrid environments compared to fully cloud-native setups.

The necessity of microservices, APIs and continuous monitoring drives organizations to seek integrated shift-left and runtime security solutions.

> "In the cloud, physical limits no longer apply. You might go from a handful of static servers to hundreds of ephemeral ones. This explosion in server count transforms dozens of potential vulnerabilities into thousands, leaving their true relevance uncertain."
> — Rick Doten, CISO at Carolina Complete Health

### The rise of runtime
**The Criticality of Runtime Tools**
While shift-left security identifies code-level vulnerabilities early in development, runtime tools provide a crucial safety net for zero-day attacks, unfixed vulnerabilities and threats in production. APIs, central to modern applications, frequently become prime targets for attackers.

- **64%**: Organizations rank runtime application security as a top priority for the coming year.
- **52%**: Encountered API-specific threats in the last 12 months.
- **33%**: Mentioned runtime tools significantly helped mitigate the threats from above.

### Embracing automation for security workflows
**Automation’s Role in Addressing Discovery, Triage and Remediation**
Automation is increasingly viewed as key to efficient discovery, triage and remediation, enabling security teams to focus on strategic, critical tasks.
- **45%**: Reduction in triage times among high automation adopters.
- **59%**: Respondents stated that automation is crucial for real-time vulnerability insights.

**Integrating Automation into CI/CD Pipeline**
Despite its advantages, automated security within CI/CD pipelines is still underutilized.
- **38%**: Successfully embedded security automation into CI/CD pipelines.
- **55%**: Respondents cite tool compatibility as the primary challenge to embed automations into CI/CD pipelines.

---

## Building a Resilient Security Posture

### Proactive vs. reactive approaches
Rapid software releases in cloud-native and hybrid environments highlight reactive security’s limitations. Shift-left strategies help teams neutralize threats before reaching production.

**68%** of respondents have begun adopting shift-left practices, but the real transformation lies in elevating security to a core development KPI, akin to code quality or performance metrics.

**Using Contextual Insights to Prioritize Vulnerabilities**
- **Real-World Exploitability**: Environmental context such as API traffic and container data combine to identify critical threats.
- **Predictive Analysis**: By 2025, organizations plan to use AI-driven tools to anticipate threats and reduce incident response costs.

> "Risk based application security model is the need of the hour. We need a way to identify and apply defense to the business critical applications with an emphasis on risk quantification. This enables us (as an industry) to align cyber security goals with business priorities."
> — Rohit Parchuri, CISO at Yext

- **57%**: Respondents have integrated contextual risk analysis in their pipelines.
- **82%**: Respondents predict real-world exploitability scores will replace traditional CVSS metrics by 2025.

---

## Looking forward: Goals for 2025

### The Future of Application Security Workflows

1. **Autonomous Remediation**: Organizations target autonomous and semi-autonomous systems for automatic vulnerability patching. 73% plan to invest in AI-assisted remediation, anticipating 50% faster fix times.
2. **Runtime Solutions at the Forefront**: Runtime-based analysis becomes essential alongside shift-left security. 62% of security leaders plan runtime solution expansion within 18–24 months.
3. **The Developer-Centric Security Model**: Organizations seek tools that integrate into developers’ workflows to speed fixes. Incentives and training will encourage developers to take ownership of security tasks.
4. **Unified Platforms and Consolidation**: The trend moves toward unified platforms integrating code scanning, runtime monitoring and threat intelligence. Early adopters report 30% faster remediation cycles and 50% fewer critical vulnerabilities reaching production.

### Predictions on Industry Trends and Best Practices
- **AI as the Security Co-Pilot**: Machine learning models will provide automated threat containment and adaptive defenses.
- **Supply Chain Security Takes Center Stage**: Proliferation of third-party libraries, APIs and microservices will drive up supply chain attacks, making real-time tracking of Software Bills of Materials (SBOM) essential.
- **Regulations and Compliance as Innovation Drivers**: Data privacy laws and industry mandates will drive security innovation beyond compliance checkboxes.

---

## Final Thoughts
Application security stands at a pivotal juncture. Fragmented defenses, manual processes and limited visibility can no longer contend with the speed and ingenuity of modern cyber threats.

### From Incremental to Transformational
Security must evolve from traditional “bolt-on” to become integral to development. This requires:
- **Embedding Security from the Start**: Shift-left techniques and secure coding practices.
- **Embracing Runtime Intelligence**: Runtime solutions such as ADR (Application Detection and Response) and advanced API security.
- **Unifying Tools and Data**: Consolidated platforms that offer cohesive visibility.

### The Role of Automation and AI
- **AI-Augmented Triage**: Real-world exploitability scores to sharpen prioritization.
- **Intelligent Policy Enforcement**: Automated policies that adapt in real time.

### Actionable Recommendations
1. **Integrate and Consolidate**: Minimize tool sprawl.
2. **Automate Where It Counts**: Focus on triaging, patching and asset discovery.
3. **Shift-Left Without Neglecting Runtime**: Real-time defenses are critical for threats that slip past development.
4. **Invest in Contextual Intelligence**: Combine exploit data, business impact and usage patterns.
5. **Champion a Security-First Culture**: Foster transparent communication and shared KPIs.

### A New Horizon with Kodem
Organizations seeking to thrive in this landscape can look to Kodem, which unifies shift-left with runtime analysis in a single platform. For more information you may visit [kodemsecurity.com](http://kodemsecurity.com).

---

## Demographics
The survey included 82 respondents.

### Roles
1. **Security Leadership**: CISOs, Security Managers, Heads of Security.
2. **Security Practitioners**: Security Engineers, Analysts, Architects.
3. **Developers and DevOps Professionals**: Software Engineers, DevOps Managers, SREs.

### Organizational Size (R&D size)
- **Small Enterprises (<100 Engineers)**: 20%
- **Medium-Sized Organizations (100–1,000 Engineers)**: 50%
- **Large Organizations (>1,000 Engineers)**: 30%

### Industries
- **Technology and Software Development**: Majority focus on cloud-native and API-based deployments.
- **Finance and Healthcare**: High emphasis on real-time monitoring and audit processes.
- **Manufacturing and Energy**: Integrating IT and OT; WAF and perimeter defenses remain prominent.

---

## Methodology
- **Survey Design**: Targeted CISOs, AppSec leaders and security professionals.
- **Data Analysis**: Quantitative methods (aggregated patterns) and Qualitative insights (thematic coding).
- **Data Collection**: Email campaigns, security forums, and direct outreach over four weeks.
- **Limitations**: Self-reported data, sample representation, and the rapidly evolving nature of the landscape.

---
find your Appy place at [www.kodemsecurity.com](http://www.kodemsecurity.com)