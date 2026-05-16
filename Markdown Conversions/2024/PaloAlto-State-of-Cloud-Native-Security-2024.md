# State of Cloud-Native Security 2024

## Table of Contents
- [Executive Summary: A Retrospect on the Previous Year](#executive-summary-a-retrospect-on-the-previous-year)
- [Introduction: Time Favors the Prepared](#introduction-time-favors-the-prepared)
- [Highlights of 2024 Survey Findings](#highlights-of-2024-survey-findings)
- [The Cloud Economy: A Global Perspective](#the-cloud-economy-a-global-perspective)
- [From Exploration to Cloud-Native Innovation](#from-exploration-to-cloud-native-innovation)
- [Plan for Cost Optimization of Legacy Apps](#plan-for-cost-optimization-of-legacy-apps)
- [Balancing Tools, Vendors, and Organizational Needs](#balancing-tools-vendors-and-organizational-needs)
- [Top Concerns in Cloud Security](#top-concerns-in-cloud-security)
- [Incident Response: The Race Against Time](#incident-response-the-race-against-time)
- [Securing Sensitive Data in the Cloud](#securing-sensitive-data-in-the-cloud)
- [What Would You Do Differently?](#what-would-you-do-differently)
- [The Human Factor](#the-human-factor)
- [Risks, Realities, and Cloud Security Strategies](#risks-realities-and-cloud-security-strategies)
- [Embracing the Unknown: The Impact of AI on the Application Lifecycle](#embracing-the-unknown-the-impact-of-ai-on-the-application-lifecycle)
- [Recommendations for Securing the Cloud](#recommendations-for-securing-the-cloud)

---

## Executive Summary: A Retrospect on the Previous Year

We begin our exploration of the 2024 state of cloud-native security with a look back at the events and influences of 2023, each of which factors into our current postures, the challenges we confront, and the strategies we’ve chosen to achieve our desired outcomes.

While agile development, open-source software, and cloud-native technologies gained momentum in 2023, attacks targeting the application layer have become an established trend. The cloud-native ecosystem grappled with a surge in supply chain attacks, highlighting the prevalence of vulnerabilities in open-source software and third-party libraries. Real-world data analyzed by our Unit 42 team enhanced this picture, identifying the cloud as the dominant attack surface, with 80% of medium, high, and critical exposures found in cloud-hosted assets.[^1]

For some time, we’ve prioritized application and infrastructure security. But we mustn’t forget that third, all-important ball in the air. With the global datasphere reaching 120 zettabytes in 2023,[^2] securing sensitive data remains mission critical. The challenges of monitoring and controlling sensitive information, however, have escalated.

What’s more, generative AI emerged in 2023 as a groundbreaking force with the potential to halve development time and costs, ultimately redefining the application economy.[^3] But much like the cloud and its myriad benefits inextricably tied to challenges we must address, generative AI as a development tool comes counterweighted with concerns. We had no sooner begun to wonder about potential issues when OWASP released the Top 10 LLM Security Risks for security teams, alerting us to prompt injection, insecure output handling, and new avenues for supply chain vulnerabilities and sensitive information disclosure.

Looking at the path ahead, as we move forward in the pursuit of our objectives, we are certain of one thing—cloud security is as much a business goal as anything else we endeavor to achieve.

---

## Introduction: Time Favors the Prepared

When readiness wins the race against time, it’s the name of the game. You’ll hardly hear cloud security practitioners talk about pain points apart from the constraints of time. They are, after all, inundated with alerts and manually collating data from satellite tools while racing against attackers moving at machine speed to identify vulnerabilities.

Understandably, 90% of respondents from this year’s State of Cloud-Native Security survey want better risk prioritization. Upwards of 90% say the number of point tools they use creates blind spots affecting their ability to prioritize risk and prevent threats. Sixty-two percent of security practitioners want easy-to-use security solutions, with 1 in 3 respondents citing rapid technology changes as the primary obstacle contributing to attack surface expansion.

How multi is multicloud? Organizations are leveraging an average of 12 cloud service providers (CSPs) across SaaS, IaaS, and PaaS for their deployed applications. This, coupled with an average use of 16 cloud security tools, underscores the intricate ecosystem security teams must navigate. A 98% consensus emphasizes the importance of reducing the number of security tools, defining readiness in terms of simplification and consolidation.

Emerging concerns, such as the security risks associated with AI-generated code and unmanaged APIs, alongside traditional challenges like inadequate access management and the expanding attack surface, underscore the evolving nature of cloud security threats. Organizations are rethinking their strategies, with many emphasizing the need for foundational changes to enhance cloud security from the outset. Understanding the landscape is central to equipping security and DevOps teams with the necessary resources.

---

## Highlights of 2024 Survey Findings

**People are rethinking their lift and shift deployments.**
When asked what they would do differently if migrating to the cloud for the first time, 50% of respondents said they would spend more time refactoring their applications instead of migrating with minimal changes. Supporting this sentiment, our survey shows that organizations that moved workloads to the cloud without optimizing them for the cloud had higher total costs of ownership.

**When security is seen as a hindrance, stress levels are high.**
- Security is a gating factor hindering software releases, according to 86% of respondents.
- 71% of respondents attribute rushed deployments to security vulnerabilities.
- 48% of respondents experience major release delays all or most of the time.
- 52% of respondents cite conflict between DevOps and SecOps as a significant source of stress.

**AI-generated code is more worrisome than AI-assisted attacks.**
- More than 2 in 5 security professionals (43%) predict AI-powered threats will evade traditional detection techniques.
- 38% of respondents rank AI-powered attacks as a top cloud security concern.
- 44% are more apprehensive about risks introduced by AI-generated code.
- 100% of respondents are reportedly embracing AI-assisted coding.

---

## The Cloud Economy: A Global Perspective

Across regions, cloud investment trends affirm the cloud’s strategic significance. Organizations worldwide made substantial investments in cloud infrastructure, services, and operational efficiencies to drive digital transformation and expansion. The overall trend shows a surge in cloud spending with over 50% of organizations investing more than $10 million annually in cloud services.

![Chart showing regional investment patterns in cloud services across US, UK, Singapore, Australia, Brazil, France, Germany, India, Japan, and Mexico.]

---

## From Exploration to Cloud-Native Innovation

The cloud journey is not linear. It is a continuum of adaptation, learning, and transformation. Among this year’s survey respondents, maturity levels range from using basic cloud infrastructure for select projects to extensive integration and fully native cloud environments.

![Chart showing primary method of application deployment to the cloud: Cloud-Native, Lift and Shift, and Refactor.]

---

## Plan for Cost Optimization of Legacy Apps

The majority of respondents (67% globally) reports spending between 10% to 30% of their cloud total cost of ownership (TCO) on legacy app modernization. For 24% of organizations, costs soar upwards of 30%. When asked why developers’ time is diverted to resolving bugs and code vulnerabilities, 45% blame application architecture.

---

## Balancing Tools, Vendors, and Organizational Needs

With an average of 16 cloud security tools on board, it’s no surprise that 98% of respondents consider it important to reduce this number. Almost as many (97%) want to reduce the average 14 vendors they work with. The number of tools dedicated to cloud security has increased 60% from last year’s findings.

---

## Top Concerns in Cloud Security

1. AI-Generated Code
2. API Risks
3. AI-Powered Attacks
4. Inadequate Access Management
5. CI/CD’s Impact on the Attack Surface
6. Insider Threats
7. Unknown, Unmanaged Assets

---

## Incident Response: The Race Against Time

Cloud security incidents are on the rise, with increases in data breaches reported by 64% of organizations. Another 48% report increases in compliance violations, followed by increases in operational downtime due to misconfigurations (45%).

---

## Securing Sensitive Data in the Cloud

Of the organizations we surveyed, 50% conduct manual reviews to identify and classify sensitive data within the cloud. With 98% of organizations storing sensitive data across multiple locations—on-prem servers, the public cloud, SaaS, private clouds, and endpoints—security challenges are high.

---

## What Would You Do Differently?

- **Establishing a Governance Framework**: 53% of respondents stress the importance of investing in a governance framework.
- **Refactoring Applications**: 50% suggest spending more time on refactoring applications.
- **Prioritizing Security and Compliance**: 50% advocate for prioritizing security and compliance from the beginning.
- **Researching Tools and Vendors**: 48% stress the importance of dedicating more time to researching tools and vendors.

---

## The Human Factor

Security processes trigger delays, stress, and DevOps-SecOps conflict. 84% of respondents say that security processes cause delays to their project timelines, and 83% view security processes as a burden. 92% of organizations attribute conflicting priorities between DevOps and SecOps teams to inefficient development and deployment.

---

## Risks, Realities, and Cloud Security Strategies

Organizations seek efficient security tools with automation, centralized visibility, and easy-to-use features. 93% agree their organization would benefit from a solution that can automatically find interconnected cloud security flaws with the highest potential of an attack.

---

## Embracing the Unknown: The Impact of AI on the Application Lifecycle

AI is here, and it’s fair to say that organizations are anxious, optimistic, and committed. 100% of survey respondents are embracing AI-assisted application development. Organizations are committed to gaining visibility into their entire pipeline for AI deployments, including datasets containing sensitive data and inferred context.

---

## Recommendations for Securing the Cloud

1. **Consolidation with Platformization**: Use a centralized security management platform that follows your journey to cloud maturity.
2. **Adopting AI Securely**: Regulate AI usage, protect software supply chains, and automate sensitive data discovery.
3. **Intelligent Data Security**: Implement a data security strategy that defines how sensitive data will be protected, regardless of where it’s stored.
4. **Reduce Traffic Jams in Your DevOps Pipeline**: Evaluate your DevOps maturity and workflows to ensure security is not a gating factor.
5. **Install Proactive Security Measures**: Commit to building a DevSecOps culture to align security and development teams.

---

[^1]: Cortex Xpanse ASM Threat Report 2023
[^2]: Data Created Worldwide 2010-2025
[^3]: Economic Potential of Generative AI | McKinsey