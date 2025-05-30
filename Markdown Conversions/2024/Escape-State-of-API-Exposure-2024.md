# State of API Exposure 2024

Fortune 1000 at Risk: How we discovered 30,000 exposed APIs & 100,000 API issues in the world’s largest organizations

## Table of Contents
- [DANGERS OF UNSECURED EXPOSED APIS](#dangers-of-unsecured-exposed-apis)
- [METHODOLOGY](#methodology)
  - [Data Gathering Strategy](#data-gathering-strategy)
  - [In-Depth API Discovery Process](#in-depth-api-discovery-process)
  - [Automated API Specification Generation](#automated-api-specification-generation)
  - [Final step - API Security Scanning](#final-step---api-security-scanning)
- [Findings - API Exposure](#findings---api-exposure)
- [Findings - API Security](#findings---api-security)
- [Findings](#findings)
- [Findings - API Secrets](#findings---api-secrets)
- [Critical Findings:](#critical-findings)
  - [Exposed and Vulnerable Development APIs](#exposed-and-vulnerable-development-apis)
  - [Fortune 1000 at high risk](#fortune-1000-at-high-risk)
- [American multinational tech company:](#american-multinational-tech-company)
  - [Exposed Spring Boot Actuator](#exposed-spring-boot-actuator)
- [Standout Scenarios:](#standout-scenarios)
  - [High-Impact CVEs in the Wild](#high-impact-cves-in-the-wild)
  - [Mapping CVE to CWE](#mapping-cve-to-cwe)
- [Essential remediation steps](#essential-remediation-steps)
- [Immediate steps to take](#immediate-steps-to-take)
- [Conclusion](#conclusion)
- [Do you need help in assessing whether your APIs are exposed and at risk?](#do-you-need-help-in-assessing-whether-your-apis-are-exposed-and-at-risk)

We analyzed the domains of the world’s largest organizations included in the Fortune 1000 and CAC 40.
Here’s what we found

![Summary statistics: 30,784 Exposed APIs, 3,945 Development APIs exposed, 1,816 secrets accessible in API services, 2,038 Highly critical vulnerabilities](Image description: Summary statistics graphic)

Key Takeaways

> "Scaling API security is a fundamental challenge. As organizations deploy more APIs to meet digital demands, their security processes are falling behind. Our research shows that a majority of APIs are left unmanaged, which not only exposes data, but also magnifies risk at every level of operation."
>
> Tristan Kalos, CEO of Escape

The State of API Exposure 2024 report provides an in-depth analysis of the significant risks associated with exposed APIs, highlighting vulnerabilities across large organizations, including Fortune 1000 companies and CAC 40 entities. Key findings reveal the pervasive nature of API security issues and the need for improved security measures:

- **1,834 Highly Critical Vulnerabilities in Fortune 1000 Companies**: Among the identified vulnerabilities, 1834 were classified as highly critical, directly affecting Fortune 1000 companies. These critical vulnerabilities, often associated with broken authentication and configuration errors, place essential systems and sensitive data at significant risk of exposure and exploitation. Critical issues span various sectors, impacting tech platforms, financial companies, insurance, healthcare, tech, and others.
- **Development APIs**: Nearly 4,000 development APIs were publicly accessible, often lacking adequate security controls. Exposing these APIs can inadvertently reveal sensitive information and offer attackers potential entry points.
- **Exposed Secrets**: The report found 1,816 highly sensitive secrets exposed within API environments, including access tokens, API keys, and authentication credentials. These exposed secrets significantly heighten the risk of unauthorized access and potential misuse of critical systems.

**Call to action**: We recommend to start auditing all APIs—particularly shadow and legacy APIs—to identify and secure vulnerabilities, and restricting access to development APIs with production-level security standards. Implementing continuous monitoring and scanning tools is crucial to detect risks early, while ensuring that all secrets are encrypted and securely managed to prevent exposure.

## DANGERS OF UNSECURED EXPOSED APIS

ARE WE IGNORING HIDDEN DANGERS?

![Graphic showing statistics: 10% of IT organizations fully document their APIs, $31B estimated losses due to API breaches, 57% of organizations suffered an API-related data breach in the past two years](Image description: Statistics on API documentation, losses, and breaches)

*according to a 2023 report from Enterprise Management Associates (EMA)
**according to the 2025 Global State of API Security report
***according to Escape’s API Threat Landscape Report

THE CONSEQUENCES OF UNSECURED APIS EXPOSED IN THE WILD

API sprawl has emerged as a significant challenge in recent years. As organizations increasingly rely on APIs to fuel digital transformation, connect services, and deliver data-driven experiences, the sheer number of APIs in production has skyrocketed.

As we move through 2024, the exponential growth of APIs presents new challenges. According to recent Gartner’s market guide, APIs - especially shadow and dormant ones - are causing data breaches among organizations that, on average, exceed the magnitude of other breaches.

Since 2022, at least 190M sensitive data records have been breached. In our previous research, we estimate that enterprise companies lost $31B due to breaches.

Many APIs are pushed to production too soon, often bypassing critical security testing stages or, in some cases, being tested only after deployment rather than within development environments.

This rush to release frequently leads to gaps in security coverage, allowing untested or under-tested endpoints to expose sensitive information or become vulnerable to attack.

Another significant factor is the proliferation of "shadow APIs"—APIs that exist outside the knowledge or management of security teams. These undocumented, unmanaged, or abandoned APIs often lack essential security protocols, making them especially prone to exploitation. Shadow APIs can emerge from development shortcuts, legacy applications, or third-party integrations that slip through regular security oversight, creating hidden risks within the system’s architecture.

Given these trends, API security deserves greater attention. It is now widely recognized as a critical challenge requiring stringent security management and thorough testing before APIs are released into production environments. By analyzing Fortune 1000 and CAC 40 exposed API services we’re here to prove it.

2024'S CASES OF VULNERABLE APIS EXPOSED IN THE WILD

![Icons representing different companies](Image description: Icons representing companies mentioned in case studies)

In May 2024, Dell experienced a significant data breach when a threat actor exploited an unsecured API endpoint on a partner portal. This vulnerability allowed unauthorized access to approximately 49 million customer records, including names, physical addresses, and order information. The breach highlighted the risks associated with insufficient API security measures and the potential for large-scale data exposure.

In July 2024, Twilio’s Authy service suffered a significant breach due to an exposed API endpoint. This vulnerability allowed unauthorized access to authentication data, putting millions of users at risk. The attackers managed to exploit this unsecured endpoint to access one-time passcodes, which are a critical layer of security for multi-factor authentication. This breach highlighted how even security-focused companies are vulnerable when API endpoints aren’t adequately protected.

A vulnerability in Trello’s API configuration led to a massive data leak in January 2024, where over 15 million user records were exposed on a dark web forum. Trello, a popular project management platform, had an API endpoint that inadvertently allowed open access to sensitive user data, including project details, personal information, and task management records. Hackers were able to scrape this data due to misconfigurations in Trello’s API permissions, underscoring how quickly API flaws can result in serious data leaks.

In July 2024, German security expert Lilith Wittmann discovered an unprotected API from Deutsche Telekom, that could be used, to retrieve details about landline connections via their internet access. While the exact number of affected users was not disclosed, it exposed sensitive user data such as names, email addresses, and service usage details. The open API lacked adequate access controls, allowing unauthorized parties to access this information. This incident highlights the critical need for robust API governance to prevent data exposure and protect customer privacy.

IN 2024, DEUTSCHE TELEKOM REPORTED APPROXIMATELY 259M MOBILE CUSTOMERS WORLDWIDE

## METHODOLOGY

### Data Gathering Strategy

In our comprehensive analysis, we aimed to examine API security measures across a broad spectrum of domains. We selected domains from two primary sources:

- **Fortune 1000**: A list of the 1000 largest public companies in the United States, ranked by revenue. We excluded several very large tech companies like Amazon, Google, and Meta to avoid skewing the results.
- **CAC 40**: A capitalization-weighted index of the 40 most significant stocks among the top 100 companies by market cap on Euronext Paris.

While this approach provided a substantial data set, we recognize potential biases. Larger domains with extensive resources may employ stronger security measures, potentially leading to fewer vulnerable APIs. However, our study focused on the largest American companies without specifically accounting for this bias.

Alternatively, with over 365 million domain names reported across the internet, our sample size becomes relatively small, potentially leading to greater volatility in the number of findings.

The data collection was a one-time process.
During the collection, we encountered several limitations. To respect legal and ethical boundaries, we deliberately excluded certain types of domains. This included governmental, educational, and health-related domains, as regular users are not typically authorized to explore these. This decision ensured that our study aligned with ethical norms for web crawling and data collection practices, prioritizing responsible research standards.

### In-Depth API Discovery Process

After finalizing our domain list, we gradually added these domains into Escape’s platform to initiate a comprehensive scan of exposed APIs. We examined not only the primary domains but also dived into the numerous subdomains associated with each. This approach enabled us to achieve a thorough and granular discovery process.

![Statistic: ~1K unique top-level domains analyzed](Image description: Statistic showing the number of unique top-level domains analyzed)

Escape uses a sophisticated combination of techniques to identify and inventory APIs by scanning exposed source code:

1.  **Subdomain enumeration**
    Escape begins by performing subdomain enumeration. This process involves scanning for all subdomains associated with the main domain you previously entered into the platform. Subdomains often host APIs or services that may not be immediately apparent. By identifying these subdomains, Escape can uncover additional endpoints that might otherwise be missed. This initial step lays the foundation for a comprehensive discovery process.
2.  **AI-powered fingerprinting**
    Once subdomains are identified, Escape employs AI-powered fingerprinting to recognize and classify the APIs. Fingerprinting involves analyzing various characteristics of the APIs, such as their structure, endpoints, and response patterns. The AI algorithms used by Escape can detect and categorize different API types (REST, GraphQL, gRPC) with high accuracy. This machine learning-based approach ensures that APIs are identified and classified correctly, even if they have unique or non-standard configurations.
3.  **OSINT techniques**
    Escape also leverages Open Source Intelligence (OSINT) techniques. OSINT involves gathering and analyzing publicly available information to enhance the discovery process. By examining code repositories, documentation, and other public resources, Escape can identify additional API endpoints and services. This technique helps in discovering APIs that are not directly exposed but can still be found through public information.

Through this multi-layered process, we discovered 158,079 subdomains, allowing for extensive coverage and a highly detailed analysis. This broad scope provided a deep view into the exposure and security practices around APIs across various industries, offering critical insights into the current landscape of API security and vulnerability.

### Automated API Specification Generation

![Statistics: 4.5K API specifications found in the wild, 29.7K API specifications programmatically generated](Image description: Statistics on found and generated API specifications)

One of the most challenging aspects of our study was ensuring we had API specifications to effectively scan newly discovered exposed API services for vulnerabilities.

Having an OpenAPI Specification (OAS) is particularly beneficial as it provides a standardized, machine-readable format for documenting RESTful APIs, promoting clarity and consistency across services.

Through our initial scan, we located 4,547 exposed API specifications, so we had to generate most of the specifications ourselves. This process involved parsing the Abstract Syntax Tree (AST) from the code to create dynamically detailed and accurate API specifications.

Luckily, Large Language Models (LLMs) have recently become extremely good at analyzing and generating code. Moreover, they show great performance across a wide variety of code languages, frameworks, and coding styles, which is exactly what we want for framework and language-agnostic OAS generation software. Finally, LLMs can also leverage information in code comments, which the traditional static analysis approach cannot do.

In our current approach, integrated into Escape’s platform, we focused on two key areas:
- **Semantic Analysis**: We identify essential code fragments using custom rules (e.g., specific Semgrep patterns), optimizing the data sent to the LLM and enhancing prompt quality.
- **Specification Generation**: The LLM processes each identified fragment to generate precise OAS methods, with contextualization ensuring accuracy by resolving dependencies and references within the code.

This method enables Escape to not only generate API documentation but also to continuously monitor and detect any changes or versions in the API documentation over time.

### Final step - API Security Scanning

![Statistic: 30,784 API services scanned for vulnerabilities](Image description: Statistic showing the number of API services scanned)

After the comprehensive specification generation process, the final step is API security scanning. Using Escape’s Dynamic Application Security Testing (DAST) solution, we conducted in-depth analysis of each identified API endpoint to detect potential vulnerabilities and risks.

Escape’s DAST approach is specifically designed for API security. Unlike traditional web application DAST tools, which are often limited in scope and primarily test web applications at the surface level, Escape’s DAST is purpose-built to handle the unique requirements and complexities of APIs. This makes it exceptionally effective at identifying security flaws in API configurations, authentication, authorization, and more.

At the core of Escape's DAST is a proprietary algorithm that combines static and dynamic analysis to deliver precise, high-confidence results. The algorithm operates in multiple stages:
1.  **Contextual Analysis**: The algorithm first conducts a contextual analysis of each endpoint, identifying the API’s structure, parameters, and dependencies. This allows it to adapt its scanning approach to each specific API, ensuring relevance and reducing false positives.
2.  **Fuzzing and Payload Injection**: In the next stage, the algorithm uses fuzzing techniques to test each endpoint by sending random, unexpected, or malformed inputs. This helps identify weaknesses like input validation flaws, injection vulnerabilities, and misconfigurations. The algorithm adapts these payloads based on real-time feedback, simulating complex attacks more effectively than conventional static methods.
3.  **Behavioral Monitoring**: As it interacts with each endpoint, the algorithm monitors response patterns and behaviors to detect anomalies. By observing responses over multiple interactions, it can identify issues such as data exposure, error leakage, and misconfigured permissions, providing insights into the API’s security posture.
4.  **Risk Prioritization**: Escape’s DAST concludes with an analysis that ranks detected vulnerabilities based on risk and classifies them based on the metric named Escape severity.

You can find an in-depth technical explanation of the algorithm here.

![Diagram of the Escape Security Scanner architecture](Image description: Diagram showing the event-based architecture of the Escape Security Scanner with a reinforcement loop in the center)

## Findings - API Exposure

![Statistics on API exposure: 30,784 API services exposed, 28.5K among Fortune 1000, 3,001 APIs exposed including staging APIs by one Fortune 1000 org, 3,945 development APIs exposed, 91% REST APIs, 1,189 maximum exposed APIs per one domain](Image description: Statistics on API exposure findings)

![Chart showing the distribution of cloud providers among exposed API services: AWS 51.1%, AZURE 16%, CLOUDFLARE 10.7%, AKAMAI 8.2%, GCP 7.5%, FASTLY 4.9%, IBM 0.6%](Image description: Bar chart showing the distribution of cloud providers among exposed API services)

![Chart showing the number of domains exposing a given range of API services](Image description: Bar chart showing the number of domains exposing different ranges of API services)

## Findings - API Security

![Statistics on API security findings: 107,368 Total vulnerabilities found, 2,038 Highly critical, 98.8K vulnerabilities found among Fortune 1000, 1.8K highly critical among Fortune 1000, 8.1K API vulnerabilities found among CAC40 including 240 highly critical, 713 high risk CVEs found, 11 API services vulnerable to SQL injection, 10 API services vulnerable to BOLA](Image description: Statistics on API security findings)

![Chart showing the distribution of highly critical vulnerabilities aligned with OWASP Top 10 2023 classification: API8 2023 (746), API2 2023 (381), API9 2023 (30), API7 2023 (32), API1 2023 (10)](Image description: Bar chart showing the distribution of highly critical vulnerabilities aligned with OWASP Top 10 2023)

## Findings

![Statistics on general findings: 42 average vulnerabilities per domain, 468 domains are above the average, 1,869 the biggest number of medium-risk vulnerabilities per exposed domain, 205 the biggest number of high-risk vulnerabilities per exposed domain](Image description: Statistics on average and maximum vulnerabilities found)

![Chart showing industries with the highest number of high-risk vulnerabilities: Financial Services, Technology, Insurance, Real Estate, Automotive, Aerospace, Retail, Manufacturing](Image description: Bar chart showing industries with the highest number of high-risk vulnerabilities)

## Findings - API Secrets

This time, we did not scan for secrets exposed in front-end applications, as we have already covered that topic in our previous report. Instead, we focused on secrets accessible through vulnerable APIs identified by our DAST scans.

![Statistics on API secrets findings: 1,816 Total secrets found, 29 Highly critical](Image description: Statistics on total and highly critical secrets found)

![Chart showing the distribution of high impact secrets found: AWS Access Token, Github OAuth, Bearer Token, Generic API Keys, Github App Token, hashicorp_tf_password, graphcms, geocodio, JWT, Jira Token, jdbc, Password, md5, SSH URL, YouTube apikey, Phone number, Plaid Secret Key](Image description: Bar chart showing the distribution of high impact secrets found by type)

## Critical Findings:

### Exposed and Vulnerable Development APIs

![Statistics: 3,945 exposed development APIs, 198 highly critical vulnerabilities](Image description: Statistics on exposed development APIs and highly critical vulnerabilities within them)

In our research, we uncovered a significant volume of exposed development APIs across multiple domains. A total of 3,945 development APIs were identified as publicly accessible, posing considerable security risks due to their lack of adequate protection —3,650 of these exposed APIs were found among Fortune 1000 companies. Exposing development APIs, which often bypass rigorous security controls in favor of testing and iteration, can unintentionally reveal sensitive internal systems, configurations, and potential vulnerabilities, leaving organizations open to exploit.

Among the exposed APIs, we identified at least 198 critical vulnerabilities, including various CVEs and OWASP Top 10 risks, such as API2:2023: Broken Authentication and API8:2023: Security Misconfiguration. These vulnerabilities include risks that could allow unauthorized access to sensitive data, privilege escalation, and potential unauthorized control over critical applications. The nature and distribution of these vulnerabilities indicate a systemic gap in security practices across development environments, as many of these APIs lack proper access control, authentication, and monitoring.

More than that, our analysis highlighted that six organizations were particularly impacted, each with over 100 exposed development APIs within their domains. Of these:

- Five organizations are listed within the Fortune 1000 companies, representing some of the largest and most influential corporations globally.
- One organization is part of the CAC40 index, underscoring that even prominent European enterprises are not immune to these security oversights.

The exposure of development APIs at this scale poses a high risk to both data integrity and operational security. Development environments often house experimental or untested code, which may inadvertently expose sensitive configuration details, endpoints, and paths into production systems. Given the volume and scale of the exposure, there is an elevated risk of data breaches, intellectual property theft, and reputational damage, especially for those organizations within the Fortune 1000 and CAC40.

### Fortune 1000 at high risk

![Statistics: 1.8K highly critical vulnerabilities found (very large tech orgs. like Amazon, Google or Meta etc. were excluded), 316 companies impacted, some in highly regulated industries like financial services](Image description: Statistics on highly critical vulnerabilities and impacted companies in Fortune 1000)

We uncovered a substantial number of critical vulnerabilities within the exposed APIs of 316 Fortune 1000 companies. In total, we identified 1,830 highly critical vulnerabilities affecting a broad range of companies, including those in highly regulated sectors like financial services, healthcare, and telecommunications. This level of exposure poses significant risks, potentially compromising sensitive data and allowing unauthorized access to critical systems.

We dug into the specifics and found some troubling patterns. According to the OWASP API Security Top 10 for 2023, vulnerabilities like Broken Authentication (API2:2023) and Security Misconfiguration (API8:2023) were rampant, with 381 and 746 instances respectively.

![Pie chart showing the alignment of high-risk Fortune 1000 vulnerabilities with OWASP Top 10 2023 classification: API8 2023 62.2%, API2 2023 31.8%, API7 2023 2.7%, API9 2023 2.5%](Image description: Pie chart showing the distribution of high-risk Fortune 1000 vulnerabilities by OWASP Top 10 2023 category)

Many of these APIs lacked even the most basic access controls, allowing for unauthorized data access or manipulation. A staggering 19 NoSQL injection vulnerabilities and 11 SQL injection flaws were scattered across APIs, with 10 instances of Broken Object Level Authorization (BOLA)—all creating a perfect storm for potential exploitation.

It is clear that API security practices hadn’t kept up with the growing reliance on APIs across industries, revealing a systemic gap in both development and deployment practices. To tackle this, companies need to close the gap with immediate action: strengthen access controls, enforce secure configurations, and regularly test APIs to catch issues before they become threats.

## American multinational tech company:

### Exposed Spring Boot Actuator

Spring Boot Actuator is a sub-project of Spring Boot that provides production-ready features to help you monitor and manage your application.

By design, Actuator exposes diagnostic and monitoring data, such as environment variables, configuration properties, and detailed mappings of application routes. However, if not properly secured, these endpoints can inadvertently expose sensitive information about an application’s internal state, providing attackers with critical insights that can be leveraged to exploit vulnerabilities.

During a security assessment of one of the exposed API endpoints owned by a major American technology company, we gained unrestricted access to several Spring Boot Actuator endpoints, specifically:

`https://[redactedcompanydomain.com]/admin/actuator/env`
`https://[redactedcompanydomain.com]/admin/actuator/mappings`
`https://[redactedcompanydomain.com]/admin/actuator/httptrace.`

Each of these endpoints revealed sensitive details about the application’s environment, structure, and operations, collectively presenting a substantial security risk.

The first significant finding was with the `/env` endpoint, which revealed critical environment variables in plain text. Upon loading the endpoint’s response, it became clear that sensitive information—such as database credentials, API keys, and service tokens—was accessible without any obfuscation. Exposure of these variables presents a substantial risk, as they can provide unauthorized actors with the means to gain elevated access, move laterally through systems, and potentially launch further targeted attacks on backend services.

Further investigation led to the `/mappings` endpoint, which disclosed a comprehensive map of the API’s routing structure. This included not only public endpoints but also private routes intended for restricted internal use. By detailing the API’s route mappings and configuration, the endpoint unintentionally provided a roadmap of the system’s structure, revealing potential entry points and avenues for exploitation. In the hands of an attacker, this visibility into the application’s internal architecture could simplify the task of identifying weak spots and exploiting vulnerabilities in a targeted manner.

The third exposed endpoint, `/httptrace`, offered a detailed log of recent HTTP requests, complete with request headers, response statuses, and metadata. This level of trace data, including potential session cookies and internal IP addresses, can significantly aid an attacker in reconstructing user behavior, mimicking legitimate requests, or even hijacking active sessions. Such logs can facilitate a range of attacks, from session replay to broader reconnaissance efforts, making the exposure of this endpoint particularly sensitive.

These Actuator endpoints—`/env`, `/mappings`, and `/httptrace`—collectively provided a depth of insight into the API’s environment and operations that, in the absence of access controls, posed a considerable security risk. The availability of these diagnostics endpoints without restriction would allow any external party to gain a detailed understanding of the application’s configuration, user activity, and internal routes, effectively dismantling critical layers of operational security.

**Recommended Remediation Steps**

1.  **Restrict Access to Actuator Endpoints**:
    Implement access control to ensure that sensitive Actuator endpoints, such as `/env`, `/mappings`, and `/httptrace`, are accessible only to authorized users on the internal network or authenticated users with administrative privileges.
2.  **Disable Sensitive Actuator Endpoints in Production**:
    Configure the Spring Boot Actuator settings to disable endpoints like `/env`, `/mappings`, and `/httptrace` in the production environment, or at least restrict them to authorized, internal users only.
3.  **Obfuscate Sensitive Data in /env**:
    In cases where `/env` must be used, consider redacting or obfuscating sensitive environment variables, such as database credentials and API keys, to prevent accidental exposure.
4.  **Monitor and Log Access Attempts to Actuator Endpoints**:
    Implement logging and monitoring of all access attempts to these endpoints, enabling detection of any unauthorized access and facilitating incident response.

Overall, this assessment underscores how easily operational details can become visible without proper restrictions, turning what might otherwise be routine endpoints into critical vulnerabilities. Addressing these exposures is essential to uphold the security and integrity of the company’s infrastructure.

## Standout Scenarios:

### High-Impact CVEs in the Wild

![Statistics: 713 Total High Impact CVEs Found, 98 Distinct High Impact CVEs Types, 102 High Impact CVEs in 2024](Image description: Statistics on high-impact CVEs found)

This section highlights critical cases where APIs, compromised by known CVEs (Common Vulnerabilities and Exposures), are openly accessible on the internet. These vulnerabilities, if unaddressed, can serve as entry points for malicious actors to exploit vulnerable API services.

**Key findings:**

- **Prevalence of OpenSSL Vulnerabilities**: A lot of found CVEs are associated with OpenSSL, a widely used library for secure communications. APIs leveraging OpenSSL must ensure they are using updated versions to mitigate these vulnerabilities.
- **Risk of Remote Code Execution**: Several vulnerabilities, notably CVE-2022-2274 and CVE-2021-3711, can lead to remote code execution if exploited, posing severe risks to API integrity and security.
- **Importance of Input Validation**: Vulnerabilities like CVE-2022-2068 and CVE-2022-1292 highlight the critical need for proper input validation to prevent command injection attacks.
- **Legacy Vulnerabilities**: A significant number of older CVEs, frequently appearing from 2020 through 2023, continue to impact APIs. This trend suggests that many organizations struggle to patch legacy vulnerabilities. These unpatched older CVEs are often well-documented, making them attractive targets for attackers who can easily exploit known weaknesses.
- **Organizational Impact of Unaddressed CVEs**: The presence of these CVEs in production may affect compliance with security standards and lead to potential regulatory issues. Furthermore, should these CVEs be exploited, the resultant damage could impact not only security but also customer trust and business continuity.

![Bar chart showing the top 5 CVE occurrences: CVE 2024 5535 (95), CVE 2022 2274 (70), CVE 2022 2068 (70), CVE 2022 1292 (57), CVE 2021 3711 (57)](Image description: Bar chart showing the frequency of the top 5 high-impact CVEs found)

CVE-2021-3711 (57 instances)
As an older CVE, if it pertains to cryptographic weaknesses or data exposure, it would directly impact APIs by potentially making data-in-transit vulnerable

### Mapping CVE to CWE

Diiscovered CVEs map to several key CWEs associated with common API weaknesses. Here are the main categories of weaknesses found in the list and their implications for API security:

- **Improper Input Validation (CWE-20)**:
    - **Relevance**: Improper input validation is one of the most common vulnerabilities in API systems, where unvalidated or poorly sanitized inputs can lead to injection attacks, unauthorized access, or unintended behavior.
    - **Implications**: APIs with CWE-20