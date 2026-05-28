# 2025 SaaS Security Risks Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [SaaS Adoption Continues to Grow](#saas-adoption-continues-to-grow)
- [SaaS App Stats](#saas-app-stats)
- [SaaS Adoption by Industry](#saas-adoption-by-industry)
- [SaaS per Employee - Provisioned vs. Used](#saas-per-employee---provisioned-vs-used)
- [Sprawling SaaS Accounts & Identities](#sprawling-saas-accounts--identities)
- [SaaS Realizations](#saas-realizations)
- [Organizations Struggle to Manage SaaS Growth](#organizations-struggle-to-manage-saas-growth)
- [Defining Unmanaged, Managed, and Tolerated SaaS](#defining-unmanaged-managed-and-tolerated-saas)
- [SaaS Risk Management Varies by Industry](#saas-risk-management-varies-by-industry)
- [Some Apps are Better Managed Than Others](#some-apps-are-better-managed-than-others)
- [The Prevalence of Shadow SaaS](#the-prevalence-of-shadow-saas)
- [Accelerated Adoption: Tools and Users](#accelerated-adoption-tools-and-users)
- [The Shadow AI Boom: Rapid Growth and Unseen Risks](#the-shadow-ai-boom-rapid-growth-and-unseen-risks)
- [The Most Widely Used AI Tools](#the-most-widely-used-ai-tools)
- [ChatGPT](#chatgpt)
- [AI Apps are Hot but Remain in the Shadows](#ai-apps-are-hot-but-remain-in-the-shadows)
- [Managed Apps Still Present Risks](#managed-apps-still-present-risks)
- [Conclusion](#conclusion)
- [Methodology](#methodology)
- [About Grip Security](#about-grip-security)

---

## Executive Summary
The explosive growth of SaaS, the surge in Shadow IT, and the rapid adoption of AI have created a tsunami of risks that many organizations are unprepared to handle. Businesses are now heavily reliant on SaaS, and as these apps become more accessible, employees are increasingly bypassing IT departments, resulting in a flood of unmonitored and unsecured software.

This report takes a comprehensive look at how shadow SaaS and shadow AI are reshaping the security landscape. Using anonymized data from the SaaS Security Control Plane (SSCP) deployments, Grip analyzed over 29 million SaaS user accounts, 1.7 million identities, and 23,987 distinct SaaS applications to understand the scale and nature of these risks. The findings highlight a growing challenge: traditional security measures are no longer enough to protect organizations from "SaaS risk creep," the slow but steady accumulation of vulnerabilities that arise from unmanaged apps and the user accounts tied to them.

As organizations increasingly manage more SaaS apps and user accounts than ever before, a new strategic approach is essential. Gartner projects that by 2027, 75% of employees will use technology outside of IT's purview. This shift demands more than just monitoring—it requires a complete rethinking of SaaS security to address the nuances of shadow SaaS and shadow AI. Without adapting to these changes, enterprises face an expanding gap between perceived security and the reality of unmonitored risk. A flexible, identity-centric approach that empowers employees while controlling risk is the only way forward in this evolving landscape.

## Key Findings
- **85%**: SaaS apps that are unknown and unmanaged.
- **91%**: AI tools that are unmanaged.
- **80%**: AI apps that could be federated but are not.
- **42%**: AI apps that have SAML capabilities.
- **73%**: Employees who don’t use their provisioned app licenses.
- **40%**: Growth in SaaS portfolios.

## SaaS Adoption Continues to Grow
As the SaaS market grew, so did adoption in the workforce. A trend that started during the pandemic has led to a surge in employees acquiring their own SaaS tools, driving a spike in SaaS usage organization-wide. Remote workers found it easy and convenient to start cloud subscriptions independently without consulting IT. According to industry data, SaaS adoption skyrocketed 62% in the first year of COVID lockdowns (2019-2020) and grew another 28% the following year.

## SaaS App Stats
In 2023, small companies used 411 apps, medium companies 582 apps, and large companies 1,437 apps. These figures represent a substantial increase from 2022, an average increase of 40%. Analyzing the data by company size reveals that medium-sized companies adopted SaaS at the highest rate, a 47% increase.

## SaaS Adoption by Industry
SaaS adoption surged across all industries. Between Q1 2023 and Q1 2024, sectors like software, insurance, and business services substantially increased SaaS usage, driven by the need for scalable solutions to enhance efficiency and foster innovation.

## SaaS per Employee - Provisioned vs. Used
The number of SaaS applications per employee has steadily risen, marking an 85% increase in managed SaaS tools usage when broken down by individual users. In 2022, employees used an average of 7 tools, which rose to 11 in 2023 and increased to 13 by early 2024. However, the data also reveals discrepancies between provisioned SaaS licenses and actual usage. On average, 73% of provisioned users never utilized their application license.

## Sprawling SaaS Accounts & Identities
While the number of SaaS applications in use has experienced explosive growth, an equally important trend is the significant increase in the number of SaaS accounts. Unlike the sheer count of different apps, SaaS accounts refer to the number of individuals accessing a single application.

## SaaS Realizations
1. Organizations need streamlined, comprehensive, and systematic security measures to manage the expanding SaaS landscape.
2. CISOs now face increased exposure and liability from SaaS employees adopt independently.
3. As SaaS procurement behaviors shift, CISOs must transition from gatekeepers to secure innovation enablers.

## Organizations Struggle to Manage SaaS Growth
"Unmanaged SaaS" refers to any application not centrally monitored, maintained, or controlled by the organization's IT department. Regardless of an organization's size, securing SaaS environments is a struggle. Looking at the initial baseline average and isolating SaaS onboarded in 2023 shows that 82-90% of new applications were unmanaged.

## Defining Unmanaged, Managed, and Tolerated SaaS
- **Tolerated SaaS**: Known and approved, but low risk and not actively managed.
- **Unmanaged SaaS**: Shadow IT and SaaS applications not centrally monitored or governed.
- **Managed SaaS**: Known and governed by IT, typically using SSO or IdP.

## SaaS Risk Management Varies by Industry
Managed applications vary significantly across industries. For example, only 4.2% of SaaS applications in the construction industry are managed, whereas in the insurance industry, 21% of applications are actively managed.

## Some Apps are Better Managed Than Others
The data shows a slightly higher concentration of managed IT, production, and security apps (16%–22%). In contrast, marketing apps are among the lowest concentration of managed apps (5.8%) and a high volume of shadow SaaS (94.2%).

## The Prevalence of Shadow SaaS
Organizations often misjudge the volume of shadow SaaS. Grip’s research uncovered an average of 835 SaaS applications, whereas industry reports often cite an average of 93 managed applications. The delta represents unmanaged shadow SaaS.

## Accelerated Adoption: Tools and Users
Grip’s research highlights a steady and consistent rise in personal usage of AI apps over the last two years. 84% of employees use generative AI tools, and 55% admit to publicly exposing their company’s data.

## The Shadow AI Boom: Rapid Growth and Unseen Risks
Generative Artificial Intelligence (GenAI) has taken the world by storm. As GenAI adoption soared, company policies lagged. The Conference Board reports that 57% of organizations lack an AI policy to guide their employees.

## The Most Widely Used AI Tools
Major players like Microsoft, Google, Zoom, and Adobe lead the pack. Other commonly provisioned AI tools include GitHub and Canva (83% each), Grammarly (82%), Notion (73%), and Jasper (39%).

## ChatGPT
ChatGPT usage has increased 24x in less than two years. Despite its capability to be more tightly controlled, it is managed at a slightly lower rate (9%) than the average SaaS application (13%).

## AI Apps are Hot but Remain in the Shadows
Grip data reveals that 42% of popular AI apps have SAML capabilities; however, 80% of AI apps that could be centrally managed and federated with the SAML protocol are not.

## Managed Apps Still Present Risks
High-profile breaches illustrate the dangers of forgotten and abandoned software accounts. Grip data revealed that 16% of managed applications were abandoned in 2023 yet remained connected to core systems.

## Conclusion
As the SaaS landscape evolves, so must the security measures organizations use to protect their environments. Traditional tools like CASBs have been relied upon but have proven ineffective because SaaS applications disrupt conventional network and endpoint monitoring models. A collaborative effort involving the appropriate stakeholders is essential to effectively manage SaaS risks at scale.

## Methodology
This report is based on anonymized customer data from Grip SaaS Security Control Plane (SSCP) deployments, encompassing over 29 million SaaS user accounts, 1.7 million identities, and 23,987 SaaS applications.

## About Grip Security
Grip Security is the industry leader in SaaS identity risk management. Our platform enables companies to discover, prioritize, secure, and orchestrate SaaS risk mitigation.

![Grip Security Contact Information]