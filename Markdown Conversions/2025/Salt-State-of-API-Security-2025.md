# Q1 2025 State of API Security

![A large 'A' and 'P' with 'I' in a smaller font, followed by 'Q1 2025 State of API Security']

## Table of Contents
- [Executive Summary](#executive-summary)
- [Drivers for API Adoption](#drivers-for-api-adoption)
- [API Development Trends](#api-development-trends)
- [API Security Challenges](#api-security-challenges)
- [Salt Labs Analysis of Customer Data](#salt-labs-analysis-of-customer-data)
- [Monitoring and Securing APIs](#monitoring-and-securing-apis)
- [Generative AI and API Security Risks](#generative-ai-and-api-security-risks)
- [Measuring ROI in API Security](#measuring-roi-in-api-security)
- [Conclusion and Recommendations](#conclusion-and-recommendations)
- [About Salt Security](#about-salt-security)
- [Methodology](#methodology)

## Executive Summary
### The State of API Security in Q1 2025

The Q1 2025 State of API Security Report paints a vivid picture of progress and ongoing API security challenges. API adoption has become a cornerstone of digital transformation, with rapid growth driven by cloud migration, integration efforts, and the monetization of data and functionality. This expansion, however, has created complex ecosystems that often outpace the security measures in place.

A significant challenge lies in organizations’ ability to maintain accurate API inventories and monitor their usage effectively. The fact that **58%** of organizations monitor their APIs less than daily and lack confidence in inventory accuracy highlights critical vulnerabilities that adversaries could exploit. While real-time monitoring is a pressing need, only one in five organizations have achieved this level of oversight.

The prevalence of security issues, such as data exposure and authentication problems, underscores the necessity of a proactive and robust security strategy, especially considering **55%** of organizations professed to slowing the rollout of a new application into production due to API security concerns. It is concerning that nearly one in five organizations cannot identify runtime security gaps, revealing a blind spot in operational security that needs immediate attention. Organizations also face challenges in scaling their API programs, with **14%** reporting that their programs are out of control or hard to manage and **22%** who said the biggest obstacle to an optimal API security strategy is people or resource shortages.

![Bar chart showing API monitoring frequency: Less frequently than every few months (12%), I do not know (4%), Continuously in real-time (20%), Every few months (16%), Monthly (13%), Weekly (17%), Daily (18%).]

![Pie chart showing responses to slowing application rollout due to API security concerns: I do not know (12%), No (33%), Yes (55%).]

### Executive Summary II

Although many organizations adopt industry frameworks and standards, adherence is inconsistent. The limited focus on the OWASP Top Ten guidelines (highlighted by only half of respondents) showcases a missed opportunity to leverage proven practices to reduce vulnerabilities. Additionally, posture governance is a critical yet often overlooked aspect of API security. Without strong governance, organizations struggle to enforce security policies consistently, leading to misconfigurations, excessive permissions, and weak access controls. Implementing robust posture governance ensures that API security policies are clearly defined, continuously enforced, and regularly assessed, mitigating risks before they can be exploited.

Budget and resource constraints remain a recurring theme. Despite increased investment in API security by **over half** of respondents, **30%** cited limited budgets, and many reported insufficient personnel (**22%**) or tooling (**10%**). This imbalance suggests that while awareness of API security risks has improved, organizations often struggle to translate this awareness into fully realized security programs. A well-structured posture governance framework can help optimize resource allocation, ensuring security efforts are both effective and scalable.

![Pie chart showing whether OWASP API Top 10 Threats are a focus area: I do not know (9%), No (38%), Yes (53%).]

![Bar chart showing obstacles to optimal API security strategy: Time (8%), Budget (30%), Enterprise (14%), Resources/people (22%), Defined strategy (8%), Tooling/solutions (10%), Competing priorities (8%), Other (1%).]

### Executive Summary III

Generative AI (GenAI) further complicates the landscape by introducing new attack vectors and vulnerabilities. The lack of confidence in detecting AI-driven threats, reported by **one third** of respondents, and concerns over securing the quality of AI-generated code by **31%** illustrate the need for specialized tools and training. Accurate and complete API discovery, posture governance and threat intelligence, along with developer training, governance frameworks, and advanced testing methodologies, must form the backbone of strategies to address these emerging risks.

The 2025 State of API Security Report reinforces the dual reality of progress and persistent challenges in API security. While organizations are embracing APIs as critical enablers of digital transformation, their rapid adoption has created complex ecosystems that often outpace existing security measures. Organizations must adopt proactive strategies to meet these challenges, focusing on comprehensive monitoring, adherence to established security frameworks like the OWASP Top Ten, and advanced testing practices. By prioritizing real-time monitoring, adhering to security frameworks, and investing in advanced testing and AI-specific security measures, organizations can proactively mitigate API risks and ensure continued innovation.

> “Most organizations are fast-tracking digital innovation efforts, leveraging APIs to deliver positive customer experiences. As organizations scale API ecosystems, security often remains an afterthought and threat actors are actively exploiting weak authentication, misconfigurations, and gaps in runtime security to infiltrate systems and access sensitive data.”
> Says Roey Eliyahu, CEO and co-founder of Salt Security, “Protecting APIs requires a proactive approach—one that emphasizes continuous discovery, strong posture governance, and real-time threat detection. That’s why Salt has developed industry-leading API security solutions, empowering organizations with the visibility, intelligence, and protection needed to defend against today’s most sophisticated threats.”

## Drivers for API Adoption

Organizations identified five primary drivers behind API adoption. In order, they are:

1.  **Development Efficiencies and Standardization**: APIs streamline processes and ensure consistency across teams and projects.
2.  **Platform or Systems Integration**: APIs enable seamless connections between disparate systems, reducing silos, and improving workflows.
3.  **Cloud Migration**: APIs support the transition to cloud-based environments, improving scalability, and resource utilization.
4.  **Digital Transformation**: APIs drive modernization initiatives, enabling organizations to enhance customer experiences and stay competitive.
5.  **Monetization of Functionality or Data**: APIs unlock new revenue streams by allowing organizations to offer data or functionality as a product.

## API Development Trends

API development continues to experience rapid growth, reflecting the increasing reliance on APIs to drive digital transformation, streamline operations, and enable integration across systems. According to the data, **43%** of organizations currently manage up to 100 APIs, indicating a robust but manageable portfolio for smaller enterprises or those earlier in their API adoption journey. Meanwhile, **34%** of organizations oversee between 101 and 500 APIs, showcasing the prevalence of mid-sized API ecosystems in organizations with more complex operations. Notably, of the **13%** of respondents managing over 1,000 APIs, **53%** of them are large organizations (10,000+ employees) - demonstrating the scale at which large enterprises leverage APIs to deliver services and functionality.

![Pie chart showing the number of APIs organizations develop, deliver, and/or integrate: I do not know (4%), 1,001+ (13%), 501-1,000 (6%), 1-100 (43%), 101-500 (34%).]

### API Development Trends II

The pace of API expansion is equally striking. **Thirty percent** of organizations reported a **51-100%** growth in the number of APIs they manage over the past year, showing the critical role APIs play in responding to evolving business demands. Even more impressive, **one-quarter** of respondents experienced growth exceeding **100%**, emphasizing the exponential demand for API-driven solutions. This surge in API adoption is driven by the need for organizations to innovate, modernize their infrastructures, and unlock new revenue streams, but it also raises concerns about the ability of security practices to keep pace.

The scale and pace of API adoption can strain resources and complicate security efforts, particularly for organizations with limited monitoring and management capabilities. As APIs continue to proliferate, it becomes imperative for organizations to adopt robust strategies for inventory management, security, posture governance and scalability to sustain this momentum and mitigate the risks associated with such rapid expansion.

![Bar chart showing the increase in the number of APIs over the past 12 months: 0-50% (39%), 51-100% (30%), 101-200% (12%), 201-300% (9%), 301%+ (4%), I do not know (6%).]

## API Security Challenges

API security challenges remain a pressing concern, with nearly all organizations (**99%**) having encountered API issues in the past year and **55%** saying they’ve slowed the rollout of a new application due to API security concerns. This near-universal prevalence, coupled with the rapid expansion of API ecosystems, highlights the growing complexity and risks associated with API-driven environments. APIs are integral to modern systems, facilitating seamless integrations and data exchange, but their widespread adoption also makes them a prime target for cyberattacks.

Analysis of the most frequently reported security challenges in production APIs reveals critical insecurities across multiple layers, including vulnerabilities, data exposure, and authentication.

Vulnerabilities accounted for **37%** of issues, exposing APIs to exploits such as injection attacks, misconfigurations, and broken object-level authorization. Insufficient testing, rushed deployments, and inadequate security measures during the development process are major contributing factors to these vulnerabilities.

Sensitive data exposure and privacy incidents represented **34%** of issues, and underlined the risks associated with misconfiguring, mishandling or improperly securing data exchanged through APIs. The exposure of personally identifiable information (PII) or other sensitive data can lead to compliance breaches, reputational damage, and financial penalties. This challenge is exacerbated when organizations lack visibility or have poor governance over the APIs that handle sensitive data or fail to implement robust data encryption and access controls.

### API Security Challenges II

Authentication problems, responsible for **29%** of issues, highlight weaknesses in verifying user identities and enforcing access restrictions. Common vulnerabilities, such as improper session management or the use of weak authentication mechanisms, create opportunities for attackers to impersonate users or gain unauthorized access to sensitive systems. Strong posture governance is essential to mitigating these risks, ensuring that authentication policies are consistently enforced across all API endpoints. This includes implementing multi-factor authentication (MFA), enforcing least privilege access, and conducting regular audits to identify misconfigurations. A well-governed security posture helps organizations proactively address authentication weaknesses, reducing the likelihood of successful attacks.

![Bar chart showing security problems found in production APIs in the past 12 months: Vulnerability (37%), Breach (22%), Sensitive data exposure / privacy incident (34%), Authentication problem (29%), Denial of service (18%), Account misuse/other fraud (28%), Brute forcing or credential stuffing (25%), Enumeration and scraping (12%), Other (4%).]

### API Security Challenges III

API posture governance strategies, which provide a structured framework for managing and securing the entire API ecosystem from design to deployment, also leave room for improvement. Only **10%** of organizations currently have an API posture governance strategy in place - the same amount from last year’s report. However, **43%** plan to implement such a strategy within the next 12 months. By deploying and implementing a robust API posture governance engine, organizations can gain complete visibility into their API landscape, eliminate blind spots, and establish corporate-wide security standards and regulations across their