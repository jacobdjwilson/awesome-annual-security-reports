# The Horizons of Identity Security

## Table of Contents
- [Executive summary](#executive-summary)
- [Chapter 1: The future of identity is tightly linked with data and security](#chapter-1-the-future-of-identity-is-tightly-linked-with-data-and-security)
- [Chapter 2: Where organizations are in their journeys](#chapter-2-where-organizations-are-in-their-journeys)
  - [The SailPoint Horizons maturity framework](#the-sailpoint-horizons-maturity-framework)
  - [Where organizations are today](#where-organizations-are-today)
- [Chapter 3: Your customer success journey across horizons](#chapter-3-your-customer-success-journey-across-horizons)
  - [Horizon 1 -> 2: Establishing foundational identity control](#horizon-1---2-establishing-foundational-identity-control)
  - [Horizon 2 -> 3: Expanding identity coverage and automated governance across environments](#horizon-2---3-expanding-identity-coverage-and-automated-governance-across-environments)
  - [Horizon 3 -> 4+: Transforming to contextual, adaptive identity](#horizon-3---4-transforming-to-contextual-adaptive-identity)
- [Chapter 4: Quantifying identity ROI](#chapter-4-quantifying-identity-roi)
- [Chapter 5: How to stay ahead as the bar for maturity rises](#chapter-5-how-to-stay-ahead-as-the-bar-for-maturity-rises)
  - [1. Machine identity management](#1-machine-identity-management)
  - [2. Cloud data access governance](#2-cloud-data-access-governance)
  - [3. AI agent governance](#3-ai-agent-governance)
  - [4. Identity security operations integration](#4-identity-security-operations-integration)
- [Navigating your journey forward](#navigating-your-journey-forward)
- [Appendix](#appendix)
  - [Approach, methodology, and demographics](#approach-methodology-and-demographics)
  - [Sources](#sources)

# Report

# The Horizons of
Identity Security

Adapt or risk falling behind:
How to keep up as identity shifts from
foundational control to security frontier

2025-2026

## Executive summary

Identity has become the enterprise’s nerve center, coordinating access, powering automation, and enabling real-time decisions and threat management across systems and users—both human and non-human. In 2025, identity sits at the center of digital transformation, enabling secure growth, operational agility, and intelligent automation. At the same time, the identity paradigm is rapidly shifting, from single point of control to method of detection, prevention mechanism to response enabler, and static policy enforcement to dynamic privilege adjustment. In this way, the role of identity has fundamentally changed, from foundational control to the new frontier of security.

As identity security and the attack landscape evolve rapidly, especially with the proliferation of machine and AI agent identities, organizations need to adopt new and emerging identity capabilities just to keep up. However, our research reveals a widening gap between mature organizations that use automation and AI-enabled identity solutions to unlock measurable business value, and the majority, who have less mature and cumbersome access processes, held back by slow deployment, poor data integration, and limited automation. Organizations also face growing challenges in identifying and governing the full spectrum of identity types, from traditional human users to increasingly complex machine identities and AI agents, which often operate with limited visibility and fragmented ownership. This is all made more difficult by the need to scale management of identities across multiple cloud environments.

Despite challenges faced, organizations report that identity provides the greatest return on investment when compared to all other security domains. Twice as many organizations ranked Identity and Access Management (IAM) as their highest-ROI domain compared to the average (Exhibit 1). This is because effective identity management does more than reduce risk. It drives efficiency, accelerates transformation, and enables smarter decisions across the enterprise.

![Exhibit 1: Investments in IAM provide the highest perceived ROI when compared to all other security domains. Bar chart showing Domain with highest perceived ROI, % of respondents: Identity & Access Management (IAM) 30%, Endpoint Detection & Response (EDR) 22%, Governance, Risk, and Compliance (GRC) 12%, Data security 13%, Cloud Security Posture Management (CSPM) 10%, Network security/perimeter 8%, Application security 5%. Source: SailPoint Customer Survey on IAM (n=229): Question 6.06A “Investment in which security domain provides the highest perceived ROI in your organization?”]

Over the last four years, SailPoint has surveyed IAM decision-makers across the globe to assess their capabilities across identity security horizons and define the future of identity. The 375 decision-makers we surveyed in June 2025 included senior leaders in information technology, cybersecurity, and risk. More than half work for organizations with over 10,000 employees, and the majority represent the finance, technology, and healthcare sectors. (For details on survey demographics, see the appendix.)

Using their responses, we grouped their organizations into five horizons based on strategy, talent, operating model, and technology capabilities:

- At Horizon 1, the lowest maturity, organizations lack the strategy and technology to enable digital identities
- At Horizon 2, they have adopted some identity technology but still rely heavily on manual processes
- At Horizon 3, they have adopted identity capabilities at scale
- At Horizon 4, they have automated capabilities at scale and use AI to enhance digital identities
- At Horizon 5, the closest to the future of identity, boundaries are blurred between enterprise identity controls and the external identity ecosystem, and identity supports the business in next-gen technology innovations

The most significant shift this year has been the introduction of new capability requirements for Horizons 4 and 5, specifically cloud infrastructure entitlement management to secure increasingly distributed multi-cloud environments and new capabilities to govern AI agents, reflecting the accelerating adoption of AI within organizations.

What we found
This year’s research highlights four critical themes from our 2025 survey of global identity leaders. Together, they reflect where organizations stand today, where progress is being made, and what continues to hold many teams back.

1. Organizations are falling behind as the attack landscape intensifies, AI agents proliferate, and the bar for mature identity security rises

For every three organizations that moved forward, two moved backward, despite rising levels of identity security investment overall.

- 63 percent of organizations remain in Horizons 1 or 2, suggesting a significant opportunity to unlock the “full potential” of identity security. These programs are typically tactical, manually driven, and limited in their ability to support automation, AI governance, or cross-environment controls. However, many of these organizations are now focused on building foundational capabilities that will enable future scale.
- Advancement to Horizons 3 and 4+ was driven by an increased appetite to automate to reduce costs and new capability building. In particular, Horizon 4 organizations this year had higher adoption across ID verification, machine identity management, and AI agent IAM.
- Four percent of organizations regressed in 2025. This was not due to declining effort, but rather a result of rising capability thresholds to meet Horizons 4 and 5 as the attack landscape intensifies. Organizations that regressed had significantly lower adoption of AI agent IAM capabilities.

2. Organizations that adopt advanced AI and identity data capabilities see significantly higher cost savings, productivity, and risk reduction

Outperforming organizations are adopting emerging AI and data capabilities at the intersection of identity, data, and security to keep up with the evolving attack landscape.

- Use of emerging identity data capabilities is a key enabler of downstream business use cases. Horizon 3+ organizations are four to eight times more likely to have real-time identity data synchronization, entity resolution, and automated lifecycle workflows compared to earlier-stage peers.
- AI is being deployed to manage identity at scale, as mature organizations use identity not just as a control but also as a detection mechanism. Adoption of AI-enabled detection capabilities, such as Identity Threat Detection and Response (ITDR) and privileged account monitoring, is 4 times as high among mature organizations than those in Horizons 1-2.
- Identity cloud data governance is maturing, although adoption of cloud data access controls is higher than for harder to achieve context-aware access models. Mature organizations are 4.5 times more likely to have cloud data governance capabilities such as unified policy enforcement and real-time data access monitoring. However, adoption of context-aware access capabilities such as attribute-based access control (ABAC) and ephemeral access models — temporary, time-bound permissions granted only when needed — trails behind, highlighting the opportunity to mature towards dynamic and just-in-time access.

3. Deployment is a critical unlock in moving across horizons, and many get it wrong

Despite rising levels of investment, many identity programs still struggle with inconsistent deployment execution; however, mature organizations follow customer success best practices to advance across horizons.

- Deployment holds some organizations back from being able to fully onboard emerging capabilities, but implementing horizon-specific best practices enables advancement. Many organizations report IAM deployments that ran over budget, were delayed, or did not meaningfully improve user experience. However, organizations employing horizon-specific best practices outperformed across all critical business outcomes.
- Effective management of application onboarding complexity is a universal customer success challenge for organizations across horizons. Application onboarding is especially challenging for H4+ organizations, who have distributed and complex environments with 3.6 times as many applications in their estate when compared to H1-H3 organizations. However, use of risk-based sequencing and reusable templates leads to better outcomes for organizations across horizons.
- Identity data hygiene is a critical enabler of deployment success. While 44 percent of Horizon 4+ organizations still report gaps in identity data quality or normalization, organizations that prioritized and performed data cleanup before migration were 1.6 times more likely to be completely successful in their IAM tool deployment.

4. Organizations need to quantify the full value of identity to secure funding for advanced capabilities, including margin, compliance, and risk impact

Although identity enables the business through cost savings and productivity improvements, many organizations still struggle to quantify and communicate this impact, focusing only on compliance enablement and risk reduction.

- Only 25 percent of organizations position IAM as a strategic business enabler. 57 percent of organizations still describe IAM as either a “security control” or “compliance requirement,” limiting the role it plays in transformation initiatives.
- Organizations that quantify revenue and cost impact of identity investments are better positioned to seek increased funding. Organizations have traditionally quantified returns from identity security in terms of risk reduction and compliance enablement. However, those that quantify margin impact from identity security investment as well create more compelling business cases for increased funding.
- Integrated identity data unlocks downstream automation and new business use cases. When embedded into platforms like Human Resources (HR), Customer Relationship Management (CRM), or IT Service Management (ITSM), identity data powers AI assistant personalization, smarter provisioning, and more efficient business workflows across departments.
- Use of advanced identity security capabilities reduces risk through improved incident response. Identity-enabled threat detection and response, next-generation PAM, unified control planes, and AI agent governance lead to faster and more effective detection, containment, and remediation of incidents.

Why it matters
Identity is now central to how organizations operate. It connects people, systems, and data while enabling secure, automated decisions at scale, and plays a growing role in detecting and containing threats. But while its importance is widely recognized, many organizations are not keeping pace.

Too often, identity security investments fall short of their potential. Programs sometimes stall during deployment. IAM platforms are fragmented across teams or deprioritized entirely due to complexity, limited expertise, or unclear ownership. As a result, impact remains siloed in IT.

However, this gap can be closed. Our research explores how organizations are making identity work in practice — deploying solutions more effectively, building the right foundations, and turning investment into measurable business impact.

## Chapter 1: The future of identity is tightly linked with data and security

As organizations mature across identity security horizons, the landscape they must navigate is evolving faster than ever. In 2025, advances in AI, data management, and threat detection are reshaping identity security. As identity shifts from a foundational control to the new frontier of security, it has emerged as the central control point in outperforming organizations - where critical decisions are made, policies are enforced, and security operations converge. Identity now serves as the connective tissue across the security ecosystem, touching every domain from endpoint protection to cloud security (Exhibit 2). This strategic positioning powers expanded governance across all human and non-human identities, dynamic privileged access, unified and accurate visibility across environments, and automated threat response capabilities not possible without identity telemetry. These elements are shaping the future of integrated identity security, bringing together identity, data, and security. As integrated programs become essential to harness identity as a dynamic method for detection and response, identity, CISO, data, and AI organizations will have to come together to chart a singular path forward.

![Exhibit 2: As a central control point in the security tech stack, identity enables and enhances capabilities across multiple domains. Diagram showing Identity at the center, connecting to Endpoint security, Network security, Cloud security, Data protection, Application security, Governance, Risk & Compliance, Threat detection/SIEM, and Third party security, with descriptions for each connection.]

Four trends are now shaping how identity capabilities are evolving and expanding across the security ecosystem:

- Identity-centric governance is expanding across all identity types: Organizations are applying governance to a broader set of identities, including service accounts, bots, and AI agents. This includes discovering and cataloging machine identities, managing AI agent lifecycles, and enforcing time-bound access policies for ephemeral accounts.
- Privileged access is becoming dynamic and data-driven: Privileged access is no longer fixed, risking permanently elevated access. Access adjusts in real time based on behavioral signals, contextual risk, and sensitivity of the data or systems accessed. Organizations are beginning to shift the conversation from zero trust to continuous adaptive trust.
- Identity fabric is delivering unified control across complex environments: To reduce fragmentation, organizations are building identity control planes— centralized frameworks that connect identity data and policies across environments. The identity fabric delivers consistent policy enforcement, unified data models, and master identity records to enable seamless identity governance at scale.
- Identity signals are powering intelligent threat response: Identity has become a source of detection. Signals such as login patterns and credential misuse are being integrated into Security Incident and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) platforms to drive threat detection, forensic investigation, and automated remediation workflows.

Together, these forces offer a blueprint for the future of identity security (Exhibit 3). By anchoring security decisions in adaptive, data-driven controls, they enable identity to serve as both a risk mitigator and a business enabler. As these capabilities mature, they will continue to reduce risk, accelerate transformation, and create long-term value for the business.

While new forces are also shaping the cutting edge of identity security, capability themes referenced in last year’s report have continued to mature. Organizations are not just sustaining momentum, they are scaling these capability themes, applying them more broadly, and embedding them deeper into their environments (Exhibit 3).

- Integrated identity programs have progressed from basic visibility to unified control. Organizations are now building identity control planes that enforce consistent policies, manage entitlements, and align governance across cloud, SaaS, and on-premises platforms.
- Dynamic trust models are evolving towards continuous adaptive access. Rather than point-in-time decisions, access levels will respond in real time to changes in user behavior, session context, and risk indicators.
- Federated identities are expanding into broader identity fabrics. What began as cross-platform Single Sign-On (SSO) is now evolving into decentralized identity control, with growing use of data-sharing standards and federated governance frameworks.
- Frictionless access is becoming both more seamless and more secure. Passwordless authentication using passkeys, biometrics, and certificates is now common, while automation is extending to privileged access, ephemeral credentials, and AI assistant onboarding.

![Exhibit 3: Integrated identity will power dynamic access across users, unified visibility, and automated response. Table showing 2024 trend, Nascent, Emerging, and Mainstream capabilities across four categories: Integrated identity security, Identity governance is expanding across human and non-human identity types, Privileged access is moving from static to dynamic, Identity fabric is expanding breadth of coverage and depth of context, Integrated identity telemetry is powering automated threat response. Still emerging: Decentralized identity, digital wallets, and partner federation remain important long-term concepts, but are not considered part of the near-term roadmap for most organizations.]

Leading organizations, cybersecurity standards bodies, and governments are already embracing core elements shaping the future of identity (Exhibit 4).

![Exhibit 4: Proof points in last 12-18 months support progress across the elements shaping the future of identity. Table showing Identity, Data, and Security categories with columns for Identity-centric governance will expand across all identity types, Privileged access is moving from static to dynamic, Identity fabric is expanding breadth of coverage and depth of context, and Integrated identity telemetry is powering unified and automated threat response. Each cell contains examples and footnotes.]

## Chapter 2: Where organizations are in their journeys

### The SailPoint Horizons maturity framework

SailPoint categorizes identity security programs into five horizons based on an organization’s maturity across four enablement areas: Strategy, technology & tools, operating model, and talent (Exhibit 5). Since 2024, we have updated Horizons 4 and 5 with new capability thresholds, including for AI agent lifecycle governance and cloud-native identity data protection.

![Exhibit 5: Over 4 years of annual surveys, we clustered key criteria into 5 maturity horizons guided by survey results. Diagram showing 5 horizons from 1 (Insufficient) to 5 (Extended and unified identity), with descriptions for strategy, technology & tools, operating model, and talent for each horizon. Horizon 1: Fragmented identity experience across organization, Identity is not a focus, Identity capabilities are highly immature, Missing any operating model, Identity team mainly composed of helpdesk. Horizon 2: Started on identity management but mostly manual, Identity program gets some attention, Started purchasing some identity tools but low adoption, Capabilities are highly manual and basic, Centralized IAM function, Identity team mainly composed of helpdesk. Horizon 3: Digitalized at-scale identity management, Identity program gets digitalized, scaled, and gains wider adoption, Identity strategy is paired with metrics, Identity capabilities gain wider organizational adoption, Centralized operating model, Tool centric identity team. Horizon 4: Advanced digital tools and predictive use cases, Identity program becomes a strategic enabler, Privileged access decisions are made dynamically, Threat detection is powered by identity signals, Capabilities span across most identities and environments, Product-driven operating model. Horizon 5: Extended and unified identity, IAM strategy is a pillar of broader innovation strategy, Continuous adaptive trust is the standard, Identity data powers automated response, Operating model enables collaboration with ecosystems. Note: To be in one horizon, customer capabilities need to cover most environments and identities.]

Based on interviews and a new survey of 375 IAM decision makers across North America, Europe, Asia, and Latin America, we explored where organizations stand in their identity security journeys and how they have progressed since last year. These perspectives illustrate where organizations have excelled, the barriers they face, and how they can move to the next maturity horizon.

### Where organizations are today

While most organizations remain early in their identity journeys, a growing number are leaning into modernization – not just to catch up, but to build the foundations for what