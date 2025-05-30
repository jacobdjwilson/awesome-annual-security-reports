# State of API Exposure 2024

Fortune 1000 at Risk: How we discovered 30,000 exposed APIs & 100,000 API issues in the world’s largest organizations

## Table of Contents
- [Key Takeaways](#key-takeaways)
- [DANGERS OF UNSECURED EXPOSED APIS](#dangers-of-unsecured-exposed-apis)
- [2024'S CASES OF VULNERABLE APIS EXPOSED IN THE WILD](#2024s-cases-of-vulnerable-apis-exposed-in-the-wild)
- [Methodology](#methodology)
  - [Data Gathering Strategy](#data-gathering-strategy)
  - [In-Depth API Discovery Process](#in-depth-api-discovery-process)
  - [Automated API Specification Generation](#automated-api-specification-generation)
  - [Final step - API Security Scanning](#final-step---api-security-scanning)
- [Findings - API Exposure](#findings---api-exposure)
- [Findings - API Security](#findings---api-security)
- [Findings](#findings)
- [Findings - API Secrets](#findings---api-secrets)
- [Critical Findings: Exposed and Vulnerable Development APIs](#critical-findings-exposed-and-vulnerable-development-apis)
- [Critical Findings: Fortune 1000 at high risk](#critical-findings-fortune-1000-at-high-risk)
- [American multinational tech company: Exposed Spring Boot Actuator](#american-multinational-tech-company-exposed-spring-boot-actuator)
  - [Recommended Remediation Steps](#recommended-remediation-steps)
- [Standout Scenarios: High-Impact CVEs in the Wild](#standout-scenarios-high-impact-cves-in-the-wild)
  - [Mapping CVE to CWE](#mapping-cve-to-cwe)
- [Essential remediation steps](#essential-remediation-steps)
  - [Immediate steps to take](#immediate-steps-to-take)
- [Conclusion](#conclusion)
- [Do you need help in assessing whether your APIs are exposed and at risk?](#do-you-need-help-in-assessing-whether-your-apis-are-exposed-and-at-risk)

We analyzed the domains of the world’s largest organizations included in the Fortune 1000 and CAC 40.
Here’s what we found

![Summary statistics: 30,784 Exposed APIs, 3,945 Development APIs exposed, 1,816 secrets accessible in API services, 2,038 Highly critical vulnerabilities](image-1.png)

## Key Takeaways

> "Scaling API security is a fundamental challenge. As organizations deploy more APIs to meet digital demands, their security processes are falling behind. Our research shows that a majority of APIs are left unmanaged, which not only exposes data, but also magnifies risk at every level of operation."
>
> Tristan Kalos, CEO of Escape

The State of API Exposure 2024 report provides an in-depth analysis of the significant risks associated with exposed APIs, highlighting vulnerabilities across large organizations, including Fortune 1000 companies and CAC 40 entities. Key findings reveal the pervasive nature of API security issues and the need for improved security measures:

- **1,834 Highly Critical Vulnerabilities in Fortune 1000 Companies**: Among the identified vulnerabilities, 1834 were classified as highly critical, directly affecting Fortune 1000 companies. These critical vulnerabilities, often associated with broken authentication and configuration errors, place essential systems and sensitive data at significant risk of exposure and exploitation. Critical issues span various sectors, impacting tech platforms, financial companies, insurance, healthcare, tech, and others.
- **Development APIs**: Nearly 4,000 development APIs were publicly accessible, often lacking adequate security controls. Exposing these APIs can inadvertently reveal sensitive information and offer attackers potential entry points.
- **Exposed Secrets**: The report found 1,816 highly sensitive secrets exposed within API environments, including access tokens, API keys, and authentication credentials. These exposed secrets significantly heighten the risk of unauthorized access and potential misuse of critical systems.

**Call to action**: We recommend to start auditing all APIs—particularly shadow and legacy APIs—to identify and secure vulnerabilities, and restricting access to development APIs with production-level security standards. Implementing continuous monitoring and scanning tools is crucial to detect risks early, while ensuring that all secrets are encrypted and securely managed to prevent exposure.

# DANGERS OF UNSECURED EXPOSED APIS

ARE WE IGNORING HIDDEN DANGERS?

![Statistics: 10% of IT organizations fully document their APIs, $31B estimated losses due to API breaches, 57% of organizations suffered an API-related data breach in the past two years](image-2.png)

THE CONSEQUENCES OF UNSECURED APIS EXPOSED IN THE WILD

API sprawl has emerged as a significant challenge in recent years. As organizations increasingly rely on APIs to fuel digital transformation, connect services, and deliver data-driven experiences, the sheer number of APIs in production has skyrocketed.

As we move through 2024, the exponential growth of APIs presents new challenges. According to recent Gartner’s market guide, APIs - especially shadow and dormant ones - are causing data breaches among organizations that, on average, exceed the magnitude of other breaches.

Since 2022, at least 190M sensitive data records have been breached. In our previous research, we estimate that enterprise companies lost $31B due to breaches[^3].

Many APIs are pushed to production too soon, often bypassing critical security testing stages or, in some cases, being tested only after deployment rather than within development environments.

This rush to release frequently leads to gaps in security coverage, allowing untested or under-tested endpoints to expose sensitive information or become vulnerable to attack.

Another significant factor is the proliferation of "shadow APIs"—APIs that exist outside the knowledge or management of security teams. These undocumented, unmanaged, or abandoned APIs often lack essential security protocols, making them especially prone to exploitation. Shadow APIs can emerge from development shortcuts, legacy applications, or third-party integrations that slip through regular security oversight, creating hidden risks within the system’s architecture.

Given these trends, API security deserves greater attention. It is now widely recognized as a critical challenge requiring stringent security management and thorough testing before APIs are released into production environments. By analyzing Fortune 1000 and CAC 40 exposed API services we’re here to prove it.

[^1]: according to a 2023 report from Enterprise Management Associates (EMA)
[^2]: according to the 2025 Global State of API Security report
[^3]: according to Escape’s API Threat Landscape Report

## 2024'S CASES OF VULNERABLE APIS EXPOSED IN THE WILD

In May 2024, Dell experienced a significant data breach when a threat actor exploited an unsecured API endpoint on a partner portal. This vulnerability allowed unauthorized access to approximately 49 million customer records, including names, physical addresses, and order information. The breach highlighted the risks associated with insufficient API security measures and the potential for large-scale data exposure.

In July 2024, Twilio’s Authy service suffered a significant breach due to an exposed API endpoint. This vulnerability allowed unauthorized access to authentication data, putting millions of users at risk. The attackers managed to exploit this unsecured endpoint to access one-time passcodes, which are a critical layer of security for multi-factor authentication. This breach highlighted how even security-focused companies are vulnerable when API endpoints aren’t adequately protected.

A vulnerability in Trello’s API configuration led to a massive data leak in January 2024, where over 15 million user records were exposed on a dark web forum. Trello, a popular project management platform, had an API endpoint that inadvertently allowed open access to sensitive user data, including project details, personal information, and task management records. Hackers were able to scrape this data due to misconfigurations in Trello’s API permissions, underscoring how quickly API flaws can result in serious data leaks.

In July 2024, German security expert Lilith Wittmann discovered an unprotected API from Deutsche Telekom, that could be used, to retrieve details about landline connections via their internet access. While the exact number of affected users was not disclosed, it exposed sensitive user data such as names, email addresses, and service usage details. The open API lacked adequate access controls, allowing unauthorized parties to access this information. This incident highlights the critical need for robust API governance to prevent data exposure and protect customer privacy.

![Statistic: In 2024, Deutsche Telekom reported approximately 259M mobile customers worldwide](image-3.png)

# Methodology

## Data Gathering Strategy

In our comprehensive analysis, we aimed to examine API security measures across a broad spectrum of domains. We selected domains from two primary sources:

**Fortune 1000**: A list of the 1000 largest public companies in the United States, ranked by revenue. We excluded several very large tech companies like Amazon, Google, and Meta to avoid skewing the results.
**CAC 40**: A capitalization-weighted index of the 40 most significant stocks among the top 100 companies by market cap on Euronext Paris.

While this approach provided a substantial data set, we recognize potential biases. Larger domains with extensive resources may employ stronger security measures, potentially leading to fewer vulnerable APIs. However, our study focused on the largest American companies without specifically accounting for this bias.

Alternatively, with over 365 million domain names reported across the internet, our sample size becomes relatively small, potentially leading to greater volatility in the number of findings.

The data collection was a one-time process.
During the collection, we encountered several limitations. To respect legal and ethical boundaries, we deliberately excluded certain types of domains. This included governmental, educational, and health-related domains, as regular users are not typically authorized to explore these. This decision ensured that our study aligned with ethical norms for web crawling and data collection practices, prioritizing responsible research standards.

## In-Depth API Discovery Process

After finalizing our domain list, we gradually added these domains into Escape’s platform to initiate a comprehensive scan of exposed APIs. We examined not only the primary domains but also dived into the numerous subdomains associated with each. This approach enabled us to achieve a thorough and granular discovery process.

![Statistic: ~1K unique top-level domains analyzed](image-4.png)

Escape uses a sophisticated combination of techniques to identify and inventory APIs by scanning exposed source code:

**Subdomain enumeration**
Escape begins by performing subdomain enumeration. This process involves scanning for all subdomains associated with the main domain you previously entered into the platform. Subdomains often host APIs or services that may not be immediately apparent. By identifying these subdomains, Escape can uncover additional endpoints that might otherwise be missed. This initial step lays the foundation for a comprehensive discovery process.

**AI-powered fingerprinting**
Once subdomains are identified, Escape employs AI-powered fingerprinting to recognize and classify the APIs. Fingerprinting involves analyzing various characteristics of the APIs, such as their structure, endpoints, and response patterns. The AI algorithms used by Escape can detect and categorize different API types (REST, GraphQL, gRPC) with high accuracy. This machine learning-based approach ensures that APIs are identified and classified correctly, even if they have unique or non-standard configurations.

**OSINT techniques**
Escape also leverages Open Source Intelligence (OSINT) techniques. OSINT involves gathering and analyzing publicly available information to enhance the discovery process. By examining code repositories, documentation, and other public resources, Escape can identify additional API endpoints and services. This technique helps in discovering APIs that are not directly exposed but can still be found through public information.

Through this multi-layered process, we discovered 158,079 subdomains, allowing for extensive coverage and a highly detailed analysis. This broad scope provided a deep view into the exposure and security practices around APIs across various industries, offering critical insights into the current landscape of API security and vulnerability.

## Automated API Specification Generation

![Statistics: 4.5K API specifications found in the wild, 29.7K API specifications programmatically generated](image-5.png)

One of the most challenging aspects of our study was ensuring we had API specifications to effectively scan newly discovered exposed API services for vulnerabilities.

Having an OpenAPI Specification (OAS) is particularly beneficial as it provides a standardized, machine-readable format for documenting RESTful APIs, promoting clarity and consistency across services.

Through our initial scan, we located 4,547 exposed API specifications, so we had to generate most of the specifications ourselves. This process involved parsing the Abstract Syntax Tree (AST) from the code to create dynamically detailed and accurate API specifications.

Luckily, Large Language Models (LLMs) have recently become extremely good at analyzing and generating code. Moreover, they show great performance across a wide variety of code languages, frameworks, and coding styles, which is exactly what we want for framework and language-agnostic OAS generation software. Finally, LLMs can also leverage information in code comments, which the traditional static analysis approach cannot do.

In our current approach, integrated into Escape’s platform, we focused on two key areas:
- **Semantic Analysis**: We identify essential code fragments using custom rules (e.g., specific Semgrep patterns), optimizing the data sent to the LLM and enhancing prompt quality.
- **Specification Generation**: The LLM processes each identified fragment to generate precise OAS methods, with contextualization ensuring accuracy by resolving dependencies and references within the code.

This method enables Escape to not only generate API documentation but also to continuously monitor and detect any changes or versions in the API documentation over time.

## Final step - API Security Scanning

![Statistic: 30,784 API services scanned for vulnerabilities](image-6.png)

After the comprehensive specification generation process, the final step is API security scanning. Using Escape’s Dynamic Application Security Testing (DAST) solution, we conducted in-depth analysis of each identified API endpoint to detect potential vulnerabilities and risks.

Escape’s DAST approach is specifically designed for API security. Unlike traditional web application DAST tools, which are often limited in scope and primarily test web applications at the surface level, Escape’s DAST is purpose-built to handle the unique requirements and complexities of APIs. This makes it exceptionally effective at identifying security flaws in API configurations, authentication, authorization, and more.

At the core of Escape's DAST is a proprietary algorithm that combines static and dynamic analysis to deliver precise, high-confidence results. The algorithm operates in multiple stages:
1. **Contextual Analysis**: The algorithm first conducts a contextual analysis of each endpoint, identifying the API’s structure, parameters, and dependencies. This allows it to adapt its scanning approach to each specific API, ensuring relevance and reducing false positives.
2. **Fuzzing and Payload Injection**: In the next stage, the algorithm uses fuzzing techniques to test each endpoint by sending random, unexpected, or malformed inputs. This helps identify weaknesses like input validation flaws, injection vulnerabilities, and misconfigurations. The algorithm adapts these payloads based on real-time feedback, simulating complex attacks more effectively than conventional static methods.
3. **Behavioral Monitoring**: As it interacts with each endpoint, the algorithm monitors response patterns and behaviors to detect anomalies. By observing responses over multiple interactions, it can identify issues such as data exposure, error leakage, and misconfigured permissions, providing insights into the API’s security posture.
4. **Risk Prioritization**: Escape’s DAST concludes with an analysis that ranks detected vulnerabilities based on risk and classifies them based on the metric named Escape severity.

You can find an [in-depth technical explanation of the algorithm here](URL_TO_ALGORITHM_EXPLANATION).

![Diagram: The complete event-based architecture of the Escape Security Scanner, with the reinforcement loop in the center](image-7.png)

# Findings - API Exposure

![Statistics: 30,784 API services exposed, 28.5K among Fortune 1000, 3,001 APIs exposed, including more than 166 exposed staging APIs by one Fortune 1000 organization, 3,945 development APIs exposed, including 6 organizations with more than 100 development APIs exposed per domain - 5 from Fortune 1000 and 1 from CAC40, 91% REST APIs, 1,189 maximum exposed APIs per one domain](image-8.png)

![Chart: Most Common Cloud Providers Among Exposed API Services (AWS 51.1%, AZURE 16%, CLOUDFLARE 10.7%, AKAMAI 8.2%, GCP 7.5%, FASTLY 4.9%, IBM 0.6%)](image-9.png)

![Chart: Number of Domains Exposing a Given Range of API Services (Ranges: 0-10, 11-50, 51-100, 101-200, 200+)](image-10.png)

# Findings - API Security

![Statistics: 107,368 Total vulnerabilities found, 2,038 Highly critical, 98.8K vulnerabilities found among Fortune 1000 organizations (large tech orgs. like Amazon, Google or Meta excluded), 1.8K highly critical, 8.1K API vulnerabilities found among CAC40 organizations, including 240 highly critical, 713 high risk CVEs found, 11 API services vulnerable to SQL injection, 10 API services vulnerable to BOLA](image-11.png)

![Chart: Distribution of highly critical vulnerabilities (API8 2023: 746, API2 2023: 381, API9 2023: 30, API7 2023: 32, API1 2023: 10)](image-12.png)

Alignment of high-risk Fortune 1000 vulnerabilities with OWASP Top 10 2023 classification

# Findings

![Statistics: 42 average vulnerabilities per domain, 468 domains are above the average, 1,869 the biggest number of medium-risk vulnerabilities per exposed domain (an insurance company based in the US), 205 the biggest number of high-risk vulnerabilities per exposed domain (same insurance company...)](image-13.png)

![Chart: Industries with the highest number of high-risk vulnerabilities (Financial Services, Technology, Insurance, Real Estate, Automotive, Aerospace..., Retail, Manufactu ring, Healthcare)](image-14.png)

# Findings - API Secrets

This time, we did not scan for secrets exposed in front-end applications, as we have already covered that topic in our previous report. Instead, we focused on secrets accessible through vulnerable APIs identified by our DAST scans.

![Statistics: 1,816 Total secrets found, 29 Highly critical](image-15.png)

![Chart: High impact secrets found (AWS Access Token, Github OAuth, Bearer Token, Gene ic API Keys, Github App Token, hashicorp_tf_password, graphcms, geocodio, JWT, Jira Token, jdbc, Password, md5, SSH URL, YouTube apikey, Phone number, Plaid Secret Key)](image-16.png)

# Critical Findings: Exposed and Vulnerable Development APIs

![Statistics: 3,945 exposed development APIs, 198 highly critical vulnerabilities](image-17.png)

In our research, we uncovered a significant volume of exposed development APIs across multiple domains. A total of 3,945 development APIs were identified as publicly accessible, posing considerable security risks due to their lack of adequate protection —3,650 of these exposed APIs were found among Fortune 1000 companies. Exposing development APIs, which often bypass rigorous security controls in favor of testing and iteration, can unintentionally reveal sensitive internal systems, configurations, and potential vulnerabilities, leaving organizations open to exploit.

Among the exposed APIs, we identified at least 198 critical vulnerabilities, including various CVEs and OWASP Top 10 risks, such as API2:2023: Broken Authentication and API8:2023: Security Misconfiguration. These vulnerabilities include risks that could allow unauthorized access to sensitive data, privilege escalation, and potential unauthorized control over critical applications. The nature and distribution of these vulnerabilities indicate a systemic gap in security practices across development environments, as many of these APIs lack proper access control, authentication,