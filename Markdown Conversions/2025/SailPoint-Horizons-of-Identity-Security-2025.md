# The Horizons of Identity Security

## Table of Contents
- [Executive summary](#executive-summary)
- [Chapter 1: The future of identity is tightly linked with data and security](#chapter-1-the-future-of-identity-is-tightly-linked-with-data-and-security)
- [Chapter 2: Where organizations are in their journeys](#chapter-2-where-organizations-are-in-their-journeys)
  - [The SailPoint Horizons maturity framework](#the-sailpoint-horizons-maturity-framework)
  - [Where organizations are today](#where-organizations-are-today)
- [Chapter 3: Your customer success journey across horizons](#chapter-3-your-customer-success-journey-across-horizons)
  - [Horizon 1 ➡️ 2: Establishing foundational identity control](#horizon-1--2-establishing-foundational-identity-control)
  - [Horizon 2 ➡️ 3: Expanding identity coverage and automated governance across environments](#horizon-2--3-expanding-identity-coverage-and-automated-governance-across-environments)
  - [Horizon 3 ➡️ 4+: Transforming to contextual, adaptive identity](#horizon-3--4-transforming-to-contextual-adaptive-identity)
- [Chapter 4: Quantifying identity ROI](#chapter-4-quantifying-identity-roi)
- [Chapter 5: How to stay ahead as the bar for maturity rises](#chapter-5-how-to-stay-ahead-as-the-bar-for-maturity-rises)
- [Navigating your journey forward](#navigating-your-journey-forward)
- [Appendix](#appendix)
  - [Approach, methodology, and demographics](#approach-methodology-and-demographics)
  - [Sources](#sources)
  - [About SailPoint](#about-sailpoint)

## Executive summary

Identity has become the enterprise’s nerve center, coordinating access, powering automation, and enabling real-time decisions and threat management across systems and users—both human and non-human. In 2025, identity sits at the center of digital transformation, enabling secure growth, operational agility, and intelligent automation. At the same time, the identity paradigm is rapidly shifting, from single point of control to method of detection, prevention mechanism to response enabler, and static policy enforcement to dynamic privilege adjustment. In this way, the role of identity has fundamentally changed, from foundational control to the new frontier of security.

As identity security and the attack landscape evolve rapidly, especially with the proliferation of machine and AI agent identities, organizations need to adopt new and emerging identity capabilities just to keep up. However, our research reveals a widening gap between mature organizations that use automation and AI-enabled identity solutions to unlock measurable business value, and the majority, who have less mature and cumbersome access processes, held back by slow deployment, poor data integration, and limited automation. Organizations also face growing challenges in identifying and governing the full spectrum of identity types, from traditional human users to increasingly complex machine identities and AI agents, which often operate with limited visibility and fragmented ownership. This is all made more difficult by the need to scale management of identities across multiple cloud environments.

Despite challenges faced, organizations report that identity provides the greatest return on investment when compared to all other security domains. Twice as many organizations ranked Identity and Access Management (IAM) as their highest-ROI domain compared to the average (Exhibit 1). This is because effective identity management does more than reduce risk. It drives efficiency, accelerates transformation, and enables smarter decisions across the enterprise.

![Bar chart showing Identity & Access Management (IAM) with 30% as the domain with highest perceived ROI, followed by Endpoint Detection & Response (EDR) at 22%, Data security at 13%, Governance, Risk, and Compliance (GRC) at 12%, Cloud Security Posture Management (CSPM) at 10%, Network security/perimeter at 8%, and Application security at 5%.](image-1.png)

Over the last four years, SailPoint has surveyed IAM decision-makers across the globe to assess their capabilities across identity security horizons and define the future of identity. The 375 decision-makers we surveyed in June 2025 included senior leaders in information technology, cybersecurity, and risk. More than half work for organizations with over 10,000 employees, and the majority represent the finance, technology, and healthcare sectors. (For details on survey demographics, see the appendix.)

Using their responses, we grouped their organizations into five horizons based on strategy, talent, operating model, and technology capabilities:

- At Horizon 1, the lowest maturity, organizations lack the strategy and technology to enable digital identities
- At Horizon 2, they have adopted some identity technology but still rely heavily on manual processes
- At Horizon 3, they have adopted identity capabilities at scale
- At Horizon 4, they have automated capabilities at scale and use AI to enhance digital identities
- At Horizon 5, the closest to the future of identity, boundaries are blurred between enterprise identity controls and the external identity ecosystem, and identity supports the business in next-gen technology innovations

The most significant shift this year has been the introduction of new capability requirements for Horizons 4 and 5, specifically cloud infrastructure entitlement management to secure increasingly distributed multi-cloud environments and new capabilities to govern AI agents, reflecting the accelerating adoption of AI within organizations.

### What we found
This year’s research highlights four critical themes from our 2025 survey of global identity leaders. Together, they reflect where organizations stand today, where progress is being made, and what continues to hold many teams back.

1.  **Organizations are falling behind as the attack landscape intensifies, AI agents proliferate, and the bar for mature identity security rises**

    For every three organizations that moved forward, two moved backward, despite rising levels of identity security investment overall.

    - 63 percent of organizations remain in Horizons 1 or 2, suggesting a significant opportunity to unlock the “full potential” of identity security. These programs are typically tactical, manually driven, and limited in their ability to support automation, AI governance, or cross-environment controls. However, many of these organizations are now focused on building foundational capabilities that will enable future scale.
    - Advancement to Horizons 3 and 4+ was driven by an increased appetite to automate to reduce costs and new capability building. In particular, Horizon 4 organizations this year had higher adoption across ID verification, machine identity management, and AI agent IAM.
    - Four percent of organizations regressed in 2025. This was not due to declining effort, but rather a result of rising capability thresholds to meet Horizons 4 and 5 as the attack landscape intensifies. Organizations that regressed had significantly lower adoption of AI agent IAM capabilities.

2.  **Organizations that adopt advanced AI and identity data capabilities see significantly higher cost savings, productivity, and risk reduction**

    Outperforming organizations are adopting emerging AI and data capabilities at the intersection of identity, data, and security to keep up with the evolving attack landscape.

    - Use of emerging identity data capabilities is a key enabler of downstream business use cases. Horizon 3+ organizations are four to eight times more likely to have real-time identity data synchronization, entity resolution, and automated lifecycle workflows compared to earlier-stage peers.
    - AI is being deployed to manage identity at scale, as mature organizations use identity not just as a control but also as a detection mechanism. Adoption of AI-enabled detection capabilities, such as Identity Threat Detection and Response (ITDR) and privileged account monitoring, is 4 times as high among mature organizations than those in Horizons 1-2.
    - Identity cloud data governance is maturing, although adoption of cloud data access controls is higher than for harder to achieve context-aware access models. Mature organizations are 4.5 times more likely to have cloud data governance capabilities such as unified policy enforcement and real-time data access monitoring. However, adoption of context-aware access capabilities such as attribute-based access control (ABAC) and ephemeral access models — temporary, time-bound permissions granted only when needed — trails behind, highlighting the opportunity to mature towards dynamic and just-in-time access.

3.  **Deployment is a critical unlock in moving across horizons, and many get it wrong**

    Despite rising levels of investment, many identity programs still struggle with inconsistent deployment execution; however, mature organizations follow customer success best practices to advance across horizons.

    - Deployment holds some organizations back from being able to fully onboard emerging capabilities, but implementing horizon-specific best practices enables advancement. Many organizations report IAM deployments that ran over budget, were delayed, or did not meaningfully improve user experience. However, organizations employing horizon-specific best practices outperformed across all critical business outcomes.
    - Effective management of application onboarding complexity is a universal customer success challenge for organizations across horizons. Application onboarding is especially challenging for H4+ organizations, who have distributed and complex environments with 3.6 times as many applications in their estate when compared to H1-H3 organizations. However, use of risk-based sequencing and reusable templates leads to better outcomes for organizations across horizons.
    - Identity data hygiene is a critical enabler of deployment success. While 44 percent of Horizon 4+ organizations still report gaps in identity data quality or normalization, organizations that prioritized and performed data cleanup before migration were 1.6 times more likely to be completely successful in their IAM tool deployment.

4.  **Organizations need to quantify the full value of identity to secure funding for advanced capabilities, including margin, compliance, and risk impact**

    Although identity enables the business through cost savings and productivity improvements, many organizations still struggle to quantify and communicate this impact, focusing only on compliance enablement and risk reduction.

    - Only 25 percent of organizations position IAM as a strategic business enabler. 57 percent of organizations still describe IAM as either a “security control” or “compliance requirement,” limiting the role it plays in transformation initiatives.
    - Organizations that quantify revenue and cost impact of identity investments are better positioned to seek increased funding. Organizations have traditionally quantified returns from identity security in terms of risk reduction and compliance enablement. However, those that quantify margin impact from identity security investment as well create more compelling business cases for increased funding.
    - Integrated identity data unlocks downstream automation and new business use cases. When embedded into platforms like Human Resources (HR), Customer Relationship Management (CRM), or IT Service Management (ITSM), identity data powers AI assistant personalization, smarter provisioning, and more efficient business workflows across departments.
    - Use of advanced identity security capabilities reduces risk through improved incident response. Identity-enabled threat detection and response, next-generation PAM, unified control planes, and AI agent governance lead to faster and more effective detection, containment, and remediation of incidents.

### Why it matters
Identity is now central to how organizations operate. It connects people, systems, and data while enabling secure, automated decisions at scale, and plays a growing role in detecting and containing threats. But while its importance is widely recognized, many organizations are not keeping pace.

Too often, identity security investments fall short of their potential. Programs sometimes stall during deployment. IAM platforms are fragmented across teams or deprioritized entirely due to complexity, limited expertise, or unclear ownership. As a result, impact remains siloed in IT.

However, this gap can be closed. Our research explores how organizations are making identity work in practice — deploying solutions more effectively, building the right foundations, and turning investment into measurable business impact.

## Chapter 1: The future of identity is tightly linked with data and security

As organizations mature across identity security horizons, the landscape they must navigate is evolving faster than ever. In 2025, advances in AI, data management, and threat detection are reshaping identity security. As identity shifts from a foundational control to the new frontier of security, it has emerged as the central control point in outperforming organizations - where critical decisions are made, policies are enforced, and security operations converge. Identity now serves as the connective tissue across the security ecosystem, touching every domain from endpoint protection to cloud security (Exhibit 2). This strategic positioning powers expanded governance across all human and non-human identities, dynamic privileged access, unified and accurate visibility across environments, and automated threat response capabilities not possible without identity telemetry. These elements are shaping the future of integrated identity security, bringing together identity, data, and security. As integrated programs become essential to harness identity as a dynamic method for detection and response, identity, CISO, data, and AI organizations will have to come together to chart a singular path forward.

![Diagram showing Identity at the center, connected to various security domains. Endpoint security: Identity authenticates devices and users. Network security: Identity enables zero-trust segmentation. Cloud security: Identity federates access across multi-cloud environments. Data protection: Identity enforces role-based access. Application security: Identity provides secure authentication. Governance, Risk & Compliance: Identity automates certifications. Threat detection/SIEM: Identity establishes behavioral baselines. Third party security: Identity provides secure provisioning.](image-2.png)

Four trends are now shaping how identity capabilities are evolving and expanding across the security ecosystem:

- **Identity-centric governance is expanding across all identity types**: Organizations are applying governance to a broader set of identities, including service accounts, bots, and AI agents. This includes discovering and cataloging machine identities, managing AI agent lifecycles, and enforcing time-bound access policies for ephemeral accounts.
- **Privileged access is becoming dynamic and data-driven**: Privileged access is no longer fixed, risking permanently elevated access. Access adjusts in real time based on behavioral signals, contextual risk, and sensitivity of the data or systems accessed. Organizations are beginning to shift the conversation from zero trust to continuous adaptive trust.
- **Identity fabric is delivering unified control across complex environments**: To reduce fragmentation, organizations are building identity control planes— centralized frameworks that connect identity data and policies across environments. The identity fabric delivers consistent policy enforcement, unified data models, and master identity records to enable seamless identity governance at scale.
- **Identity signals are powering intelligent threat response**: Identity has become a source of detection. Signals such as login patterns and credential misuse are being integrated into Security Incident and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) platforms to drive threat detection, forensic investigation, and automated remediation workflows.

Together, these forces offer a blueprint for the future of identity security (Exhibit 3). By anchoring security decisions in adaptive, data-driven controls, they enable identity to serve as both a risk mitigator and a business enabler. As these capabilities mature, they will continue to reduce risk, accelerate transformation, and create long-term value for the business.

While new forces are also shaping the cutting edge of identity security, capability themes referenced in last year’s report have continued to mature. Organizations are not just sustaining momentum, they are scaling these capability themes, applying them more broadly, and embedding them deeper into their environments (Exhibit 3).

- **Integrated identity programs have progressed from basic visibility to unified control**. Organizations are now building identity control planes that enforce consistent policies, manage entitlements, and align governance across cloud, SaaS, and on-premises platforms.
- **Dynamic trust models are evolving towards continuous adaptive access**. Rather than point-in-time decisions, access levels will respond in real time to changes in user behavior, session context, and risk indicators.
- **Federated identities are expanding into broader identity fabrics**. What began as cross-platform Single Sign-On (SSO) is now evolving into decentralized identity control, with growing use of data-sharing standards and federated governance frameworks.
- **Frictionless access is becoming both more seamless and more secure**. Passwordless authentication using passkeys, biometrics, and certificates is now common, while automation is extending to privileged access, ephemeral credentials, and AI assistant onboarding.

![Table/diagram showing the evolution of identity security capabilities. It lists four main categories: Identity governance is expanding across human and non-human identity types, Privileged access is moving from static to dynamic, Identity fabric is expanding breadth of coverage and depth of context, and Integrated identity telemetry is powering automated threat response. For each category, it shows the progression from 2024 trend to Nascent, Emerging, and Mainstream capabilities, linking them to Identity, Data, and Security domains. Examples include service accounts cataloged, AI agent lifecycles managed, ephemeral identities governed, granular database permissions, continuous adaptive trust, multi-cloud entitlement visibility, frictionless access, unified control plane, entity resolution, federated identities, identity signals in threat detection, identity forensics, and automated remediation.](image-3.png)

Leading organizations, cybersecurity standards bodies, and governments are already embracing core elements shaping the future of identity (Exhibit 4).

![Table showing proof points from the last 12-18 months supporting progress across elements shaping the future of identity. It has columns for Identity, Data, and Security, and rows for Identity-centric governance, Privileged access, Identity fabric, and Integrated identity telemetry. Each cell contains examples of industry reports, standards, or initiatives. For example, under Identity-centric governance, it mentions OWASP recognizing poor non-human identity governance and Cloud Security Alliance finding gaps in NHI protection.](image-4.png)

## Chapter 2: Where organizations are in their journeys

### The SailPoint Horizons maturity framework
SailPoint categorizes identity security programs into five horizons based on an organization’s maturity across four enablement areas: Strategy, technology & tools, operating model, and talent (Exhibit 5). Since 2024, we have updated Horizons 4 and 5 with new capability thresholds, including for AI agent lifecycle governance and cloud-native identity data protection.

![Diagram illustrating 5 maturity horizons for identity security. Horizon 1 (Insufficient): Fragmented identity experience, immature capabilities, missing operating model. Horizon 2 (Foundational): Started identity management but mostly manual, low adoption, centralized IAM function focused on service tickets. Horizon 3 (Advanced): Digitalized at-scale identity management, wider adoption, some automation, identity extending to cloud and data governance, centralized operating model. Horizon 4 (Advanced): Advanced digital tools and predictive use cases, strategic enabler for business transformation, dynamic privileged access, threat detection powered by identity signals, product-driven operating model. Horizon 5 (Extended and unified identity): IAM strategy is a pillar of broader innovation, continuous adaptive trust, ephemeral identities governed, identity data powers automated response, operating model enables collaboration with ecosystems.](image-5.png)

Based on interviews and a new survey of 375 IAM decision makers across North America, Europe, Asia, and Latin America, we explored where organizations stand in their identity security journeys and how they have progressed since last year. These perspectives illustrate where organizations have excelled, the barriers they face, and how they can move to the next maturity horizon.

### Where organizations are today
While most organizations remain early in their identity journeys, a growing number are leaning into modernization – not just to catch up, but to build the foundations for what is next (Exhibit 6). Many teams are investing in automation to reduce costs and improve efficiency, helping them progress out of foundational maturity levels. At the same time, organizations are investing in AI agent governance, machine identity management, and dynamic access controls to move to more mature horizons. These shifts are accelerating forward momentum for some organizations, while exposing capability gaps that are causing others to fall behind.

![Bar chart showing the distribution of organizations across 5 customer identity journey horizons for 2023, 2024, and 2025. Horizon 1 (Fragmented identity experience): 44% (2023), 41% (2024), 42% (2025). Horizon 2 (Centralized identity management but mainly manual): 20% (2023), 23% (2024), 20% (2025). Horizon 3 (Digitalized identity management): 28% (2023), 26% (2024), 27% (2025). Horizon 4 (Advanced digital tools and predictive use cases): 7% (2023), 8% (2024), 9% (2025). Horizon 5 (Extended and unified identity): <1% (2023), ~1% (2024), ~1% (2025). Text indicates that for every 3 organizations that moved forward, 2 moved backward.](image-6.png)

This year’s maturity shifts highlight three clear patterns. First, the move from Horizons 1 and 2 into Horizon 3 is being driven by organizations seeking to automate manual identity tasks and reduce operational costs. These early-stage programs are responding to resource constraints by streamlining access workflows, especially in environments where IAM still represents a small portion of the overall cybersecurity budget.

Second, advancement into Horizon 4 depends on building entirely new capabilities. Organizations that progressed to these higher levels demonstrated stronger adoption of advanced identity tools, particularly in areas such as ID verification, machine identity management, and AI agent governance. These investments are allowing teams to move beyond manual policy enforcement toward more adaptive and intelligent identity strategies.

Finally, organizations whose efforts remain static can move backward. Four percent of organizations moved backward this year, unable to meet the higher capability thresholds introduced for Horizons 4 and 5. These organizations had notably lower adoption of AI agent IAM controls, signaling that, as identity becomes more tightly linked to AI governance, gaps in capability will increasingly translate into stalled or reversed progress.

Industry dynamics play a major role in maturity differences (Exhibit 7). Technology and banking organizations have the greatest share in Horizon 4+, driven by higher levels of identity investment and capability adoption.

![Bar chart showing the distribution of organizations across 5 customer identity journey horizons by industry. Horizon 1, 2, 3, and 4+ are shown for Aggregate, Technology, Banking & securities, Healthcare, and Manufacturing. Technology and Banking & securities show higher percentages in Horizon 4+ (15% and 13% respectively) compared to the aggregate (10%). Manufacturing has the lowest Horizon 4+ share (4%) and highest Horizon 1 share (61%).](image-7.png)

Healthcare’s rapid progress from just 6 percent in Horizon 4 in 2024 to 10 percent in 2025 is rooted in regulatory pressure, widespread adoption of electronic health records, and urgency to automate workflows, particularly after COVID-19. IAM investments help healthcare companies secure critical patient data, enable clinician efficiency, and reduce compliance risk. Manufacturing, in contrast, remains heavily clustered in Horizon 1 (61 percent), with only 4 percent in Horizon 4 and above. This lag is tied to complex, legacy environments, lower IAM investment levels, and challenges managing diverse identities across factory staff, contractors, and machines.

![Bar chart showing the distribution of organizations across 5 customer identity journey horizons by geography. Horizon 1, 2, 3, and 4+ are shown for Aggregate, APAC, North America, Europe, and LATAM. APAC and North America have higher percentages in Horizon 4+ (15% and 14% respectively) compared to the aggregate (10%). Europe and LATAM lag behind, with 5% and 3% in Horizon 4+ respectively, and higher percentages in Horizon 1 (50% and 47%).](image-8.png)

Identity security maturity also varies greatly across regions, with APAC and North America having the greatest share of organizations in Horizon 4+ (Exhibit 8). Identity security maturity of North American organizations is driven by regulatory pressures, greater levels of security funding, and greater cloud adoption. APAC maturity distribution features organizations at both ends of the spectrum—the highest representation of Horizon 1 (56%) organizations alongside the highest representation of Horizon 4+ (15%)—reflecting the region’s diverse markets and varying level of readiness for digital transformation. European organizations, despite strong data protection frameworks, show 50% still in Horizon 1, suggesting opportunity to invest in capabilities that establish compliance and grow maturity. The majority of Latin American organizations remain in Horizons 1 and 2, indicating lower levels of maturity and adoption challenges.

Amid these geographic and sector-specific shifts, a broader transformation is underway: the rapid growth of non-human identities. Machine identities and AI agents are now expanding faster than any other type of identity, driven by the widespread adoption of cloud workloads, automation, and agentic AI (Exhibit 9). AI agents are governed in less than four in ten organizations today, but they will grow faster in number than any other identity type, with over one-third of organizations expecting growth exceeding 30% in the next 3-5 years.

![Two bar charts. The first shows the percentage of organizations across horizons that govern various identity types (Employee, Internal contractor, Machine, AI agent, External 3rd party, External consumer). The second shows the expected growth of these identity types in the next 3-5 years, categorized by 30%+ decrease, 10-30%+ decrease, No change, 10-30%+ increase, and 30%+ increase. AI agent identities show the highest expected growth, with 35% of organizations expecting 30%+ increase.](image-9.png)

Leading organizations are laying the groundwork for more heavily automated identity programs to support a fast-growing number of non-human identities. While the degree of automation varies greatly across organizations, a growing number of teams are putting in place the core enablers needed to scale AI-driven identity capabilities safely and effectively. These include foundational elements such as unified identity data management, real-time monitoring, just-in-time access, and AI governance policies. Together, these prerequisites help create the conditions for success as organizations move toward more advanced maturity levels (Exhibit 10).

![Two lists of prerequisite steps. The first list, "Prerequisite steps to enable automation and AI", includes: Clean and unify identity data, Deploy modern IAM platform, Formalize identity lifecycle workflows, Clearly define roles and access models, Assemble cross-functional teams. The second list, "Prerequisite steps to manage automation & AI risks", includes: Adopt AI governance policies, Enable extensive monitoring and detailed logging, Enable just-in-time access and zero standing privileges, Integrate dynamic risk scoring and predictive anomaly detection, Implement strong data classification and sensitivity-based access controls.](image-10.png)

Outperforming organizations, building on prerequisite steps to enable and manage the risks of AI, are adopting emerging capabilities that lead to improved business outcomes. These include optimized identity data workflows, agentic AI for identity operations, identity-centric detection and response, and cloud-based data governance. While once aspirational, these capabilities are now actively driving better outcomes: Organizations that adopt them are significantly more likely to realize gains in productivity, cost efficiency, risk reduction, and audit readiness.

- **Unified identity data capabilities** that flow data seamlessly between HR systems,