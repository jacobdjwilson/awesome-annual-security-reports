# AI Security Market Report
Q2 • 2025
James Berthoty
Reporting Period
Prepared by

## Table of Contents
- [REPORT INTRODUCTION](#report-introduction)
- [AI USE CASES](#ai-use-cases)
- [AI ADOPTION & SECURITY NEEDS](#ai-adoption--security-needs)
- [OLD SOLUTIONS, NEW PROBLEMS](#old-solutions-new-problems)
- [MARKET MAP AND LEADERS](#market-map-and-leaders)
- [TOOL BUYING FLOW CHART](#tool-buying-flow-chart)
- [VENDOR BREAKDOWNS](#vendor-breakdowns)
- [CONCLUSION](#conclusion)
- [AI Security Landscape](#ai-security-landscape)
- [AI SECURITY USE CASES](#ai-security-use-cases)
- [Risk Types](#risk-types)

## AI Security Landscape
A venture capital fueled marketing frenzy has led to widespread confusion across social media, with significant misunderstandings around both use cases and best practices. This report cuts through the noise to clarify what’s been lost in the murkiness of so-called "_AI-TRiSM_." While the _AI Trust, Risk, and Security Management_ category was created to bring a range of solutions under a single label, it has often flattened the important distinctions between tools, especially when it comes to what problems vendors are solving and how.

Most of AI Security might feel new, but many of the underlying challenges are quite familiar. In nearly every category we’ll cover, there are existing tools that offer similar functionalities to various startups.

While that may suggest security teams should wait to adopt new solutions, it will take time for these traditional vendors to match the pace and specialization of newer, _AI-native_ offerings. AI security in 2025 has been defined by a disjointed landscape of solutions to unclear problems. As with any security decision, the right choice depends heavily on three important factors:
- Your specific risk profile
- Technology stack
- Organizational priorities

By the end of this report, you’ll walk away with two things: We’ll also include a simple decision flowchart to help guide your tool selection based on real-world scenarios. We hope this information is helpful, and we thank you for using Latio as your source for trusted industry insights.

## AI SECURITY USE CASES
Let’s start by outlining the different AI security use cases. These can be separated into four major categories:

**End User Data Control**
1. Data Loss Prevention
2. SaaS Access control
3. Secure Code Creation

**AI Posture Management**
1. Infrastructure Discovery
2. ML-BOM/AI-BOM
3. Data Pipeline Posture
4. Static Code Testing
(IT teams)
(Infrastructure teams)

**Application Runtime**
1. Prompt Injection Protection
2. Visibility into runtime models
3. Authn/Authz
4. Dynamic Testing
(AppSec/DevSecOps)

**AI for Security**
1. AI for SOC
2. AI for Vulnerability Management
3. AI for AppSec
(SOC and AppSec)

As a brief aside, you could argue for a fifth category, policy and compliance management around AI concerns, but we’re choosing to exclude it from this report. It’s a smaller use case and typically less relevant to security engineers.

## Risk Types
Each category of AI tooling is designed to protect against specific risks for these categories. On the end user data side, tools protect employee endpoints against manipulation, or stop employees from sharing unauthorized materials with unauthorized AI systems.

On the posture side, security teams struggle to get deep insights into how models are being developed and deployed, and what datasets these models have access to. While many teams are relying on third party models, self hosted models are especially vulnerable to different poisoning or supply chain attacks. Additionally, models can have vulnerabilities the same as any other code packages.

Finally, runtime application security is the most at risk for real world attack, especially once a system is wired up to internal data. Early iterations of AI applications were low risk, as they merely surfaced a user’s data back to them; however, agentic architectures have rapidly increased risk as agents take actions on behalf of users, and have access to sensitive data.