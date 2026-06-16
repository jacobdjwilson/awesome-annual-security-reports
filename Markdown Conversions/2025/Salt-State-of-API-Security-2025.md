# State of API Security: Q1 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Drivers for Adoption](#drivers-for-adoption)
- [API Development Trends](#api-development-trends)
- [API Security Challenges](#api-security-challenges)
- [Salt Labs Analysis of Customer Data](#salt-labs-analysis-of-customer-data)
- [Monitoring and Securing APIs](#monitoring-and-securing-apis)
- [Generative AI and API Security Risks](#generative-ai-and-api-security-risks)
- [Measuring ROI in API Security](#measuring-roi-in-api-security)
- [Conclusion and Recommendations](#conclusion-and-recommendations)
- [About Salt](#about-salt)
- [Methodology](#methodology)

## Executive Summary
The Q1 2025 State of API Security Report paints a vivid picture of progress and ongoing API security challenges. API adoption has become a cornerstone of digital transformation, with rapid growth driven by cloud migration, integration efforts, and the monetization of data and functionality. This expansion, however, has created complex ecosystems that often outpace the security measures in place.

A significant challenge lies in organizations’ ability to maintain accurate API inventories and monitor their usage effectively. The fact that 58% of organizations monitor their APIs less than daily and lack confidence in inventory accuracy highlights critical vulnerabilities that adversaries could exploit. While real-time monitoring is a pressing need, only one in five organizations have achieved this level of oversight.

The prevalence of security issues, such as data exposure and authentication problems, underscores the necessity of a proactive and robust security strategy, especially considering 55% of organizations professed to slowing the rollout of a new application into production due to API security concerns. It is concerning that nearly one in five organizations cannot identify runtime security gaps, revealing a blind spot in operational security that needs immediate attention. Organizations also face challenges in scaling their API programs, with 14% reporting that their programs are out of control or hard to manage and 22% who said the biggest obstacle to an optimal API security strategy is people or resource shortages.

![Chart: On average, how often do your primary APIs get updated/monitored?]
![Chart: Have you ever slowed the rollout of a new application into production because of API security concerns?]

Although many organizations adopt industry frameworks and standards, adherence is inconsistent. The limited focus on the OWASP Top Ten guidelines (highlighted by only half of respondents) showcases a missed opportunity to leverage proven practices to reduce vulnerabilities. Additionally, posture governance is a critical yet often overlooked aspect of API security. Without strong governance, organizations struggle to enforce security policies consistently, leading to misconfigurations, excessive permissions, and weak access controls.

Budget and resource constraints remain a recurring theme. Despite increased investment in API security by over half of respondents, 30% cited limited budgets, and many reported insufficient personnel (22%) or tooling (10%).

![Chart: Has your security team highlighted the OWASP API Top 10 Threats as a focus area for your security program?]
![Chart: What is the biggest obstacle keeping you from implementing an optimal API security strategy?]

Generative AI (GenAI) further complicates the landscape by introducing new attack vectors and vulnerabilities. The lack of confidence in detecting AI-driven threats, reported by one third of respondents, and concerns over securing the quality of AI-generated code by 31% illustrate the need for specialized tools and training.

> “Most organizations are fast-tracking digital innovation efforts, leveraging APIs to deliver positive customer experiences. As organizations scale API ecosystems, security often remains an afterthought and threat actors are actively exploiting weak authentication, misconfigurations, and gaps in runtime security to infiltrate systems and access sensitive data.” — Roey Eliyahu, CEO and co-founder of Salt Security.

## Drivers for Adoption
Organizations identified five primary drivers behind API adoption:
1. **Development Efficiencies and Standardization**: APIs streamline processes and ensure consistency across teams and projects.
2. **Platform or Systems Integration**: APIs enable seamless connections between disparate systems, reducing silos, and improving workflows.
3. **Cloud Migration**: APIs support the transition to cloud-based environments, improving scalability, and resource utilization.
4. **Digital Transformation**: APIs drive modernization initiatives, enabling organizations to enhance customer experiences and stay competitive.
5. **Monetization of Functionality or Data**: APIs unlock new revenue streams by allowing organizations to offer data or functionality as a product.

## API Development Trends
API development continues to experience rapid growth. According to the data, 43% of organizations currently manage up to 100 APIs, while 34% oversee between 101 and 500 APIs. Notably, of the 13% of respondents managing over 1,000 APIs, 53% of them are large organizations (10,000+ employees).

![Chart: How many APIs does your organization develop, deliver, and/or integrate?]

The pace of API expansion is equally striking. Thirty percent of organizations reported a 51-100% growth in the number of APIs they manage over the past year, and one-quarter of respondents experienced growth exceeding 100%.

![Chart: By how much has the number of APIs increased over the past 12 months?]

## API Security Challenges
API security challenges remain a pressing concern, with nearly all organizations (99%) having encountered API issues in the past year. Analysis of the most frequently reported security challenges in production APIs reveals critical insecurities:
- **Vulnerabilities (37%)**: Includes injection attacks, misconfigurations, and broken object-level authorization.
- **Sensitive data exposure and privacy incidents (34%)**: Risks associated with misconfiguring or improperly securing data exchanged through APIs.
- **Authentication problems (29%)**: Weaknesses in verifying user identities and enforcing access restrictions.

![Chart: In the past 12 months, what security problems have you found in production APIs?]

Only 10% of organizations currently have an API posture governance strategy in place, though 43% plan to implement such a strategy within the next 12 months.

![Chart: Do you currently have plans in place for an API Posture Governance strategy?]

## Salt Labs Analysis of Customer Data
Salt Security’s Salt Labs team analysis points to one poignant issue: the overwhelming majority of attacks originate from authenticated users. With 95% of attack attempts coming from authenticated sources, this underscores the growing risk of insider threats and compromised accounts. Additionally, 98% of attack attempts target external-facing APIs.

![Chart: Attack attempts from authenticated vs. unauthenticated attackers]
![Chart: Attack attempts against internal and external facing API endpoints]

When examining attack techniques, 80% of attempts align with the OWASP API Security Top Ten. Within this framework, API8 (Security Misconfiguration) accounts for 54% of attacks, and API1 (Broken Object Level Authorization) contributes to 27%.

![Chart: Attack attempts leveraging the OWASP API Security Top 10 vs other attack types]
![Chart: Attack attempts that map to the OWASP API Security Top 10]

## Monitoring and Securing APIs
The findings reveal critical gaps in API monitoring. A mere 20% of organizations continuously monitor their APIs in real-time. Furthermore, only 15% expressed strong confidence in the accuracy of their API inventories.

![Chart: What is your biggest concern about your company’s overall API program?]
![Chart: How confident are you that your API inventory provides enough detail about your APIs?]

Despite 69% of organizations increasing their API security budgets, the overall maturity of API security strategies remains low, with 59% still in the planning or basic stages.

![Chart: Has your organization increased their API security budget within the past 12 months?]
![Chart: How would you describe the security strategy for your API development program?]

Only 17% of organizations rated their existing security tools as very effective in preventing API attacks.

![Chart: How effective are your existing security tools in preventing API attacks?]

## Generative AI and API Security Risks
GenAI presents new challenges in API security. While it offers potential benefits, it introduces unique risks, particularly regarding the quality of AI-generated code and the potential for AI-driven attacks.

![Chart: Is Generative AI perceived as a growing security concern/risk within your organization?]
![Chart: How confident are you in your organization's ability to detect and respond to attacks leveraging Generative AI?]

Concerns about ensuring the quality and reliability of AI-generated code are paramount, with 31% of respondents citing this as a top concern, and 40% citing the potential for vulnerabilities introduced by these outputs.

![Chart: What security concerns do you have about using Generative AI to develop APIs?]

To address these risks, 56% of organizations are prioritizing developer training, while 40% employ code reviews and security testing.

![Chart: What measures does your organization take to mitigate the risks of using Generative AI to develop APIs?]

## Measuring ROI in API Security
Organizations use several key metrics to assess the effectiveness of their API security initiatives:
- **Improved Compliance Posture (37%)**: Reflects the importance of adhering to regulatory requirements like GDPR, HIPAA, or PCI DSS.
- **Cost Savings from Breach Prevention (25%)**: Highlights the financial consequences of avoiding data breaches and incident response costs.
- **Reduction in API-Related Security Incidents (16%)**: Indicates the success of security measures in place.

## Conclusion and Recommendations
The 2025 State of API Security Report demonstrates the growing reliance on APIs for digital transformation and the persistent security challenges organizations face. To improve, organizations should:
1. **Prioritize Real-Time Monitoring and Runtime Security**: Enable immediate threat detection and response.
2. **Develop Comprehensive API Security Strategies and Frameworks**: Align with the OWASP API Security Top Ten.
3. **Strengthen API Inventory Management and Visibility**: Invest in automated tools to identify all APIs, including shadow and zombie APIs.
4. **Mitigate Risks from Generative AI**: Implement developer training, robust code review, and governance frameworks tailored to AI.
5. **Enhance Security Tools and Testing Practices**: Combine vulnerability scanning, penetration testing, and threat modeling.

## About Salt
The Salt Security API Protection Platform secures APIs across the full lifecycle by collecting a copy of API traffic and using big data, machine learning, and AI to discover APIs, stop attacks, and eliminate vulnerabilities. Salt Labs identifies API threats and vulnerabilities in customer deployments and in the wild to inform the platform's algorithms.

## Methodology
The findings of this report are based on insights from 206 professionals tasked with managing APIs in their organizations across various industries, including Technology (28%), Financial Services and Insurance (14%), and Energy and Utilities (13%).