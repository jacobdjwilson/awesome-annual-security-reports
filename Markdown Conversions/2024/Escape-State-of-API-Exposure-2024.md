# State of API Exposure 2024

**Organization**: Escape  
**Report Title**: State of API Exposure  
**Year**: 2024

Fortune 1000 at Risk: How we discovered 30,000 exposed APIs & 100,000 API issues in the world’s largest organizations.

We analyzed the domains of the world’s largest organizations included in the Fortune 1000 and CAC 40. Here’s what we found:
- **30,784** Exposed APIs
- **3,945** Development APIs exposed
- **1,816** secrets accessible in API services
- **2,038** Highly critical vulnerabilities

## Table of Contents
- [Key Takeaways](#key-takeaways)
- [Are We Ignoring Hidden Dangers?](#are-we-ignoring-hidden-dangers)
- [2024's Cases of Vulnerable APIs Exposed in the Wild](#2024s-cases-of-vulnerable-apis-exposed-in-the-wild)
- [Methodology](#methodology)
- [Findings - API Exposure](#findings---api-exposure)
- [Findings - API Security](#findings---api-security)
- [Findings - API Secrets](#findings---api-secrets)
- [Critical Findings: Exposed and Vulnerable Development APIs](#critical-findings-exposed-and-vulnerable-development-apis)
- [Critical Findings: Fortune 1000 at High Risk](#critical-findings-fortune-1000-at-high-risk)
- [American Multinational Tech Company: Exposed Spring Boot Actuator](#american-multinational-tech-company-exposed-spring-boot-actuator)
- [Standout Scenarios: High-Impact CVEs in the Wild](#standout-scenarios-high-impact-cves-in-the-wild)
- [Standout Scenarios: Mapping CVE to CWE](#standout-scenarios-mapping-cve-to-cwe)
- [Essential Remediation Steps](#essential-remediation-steps)
- [Immediate Steps to Take](#immediate-steps-to-take)
- [Conclusion](#conclusion)

## Key Takeaways

> "Scaling API security is a fundamental challenge. As organizations deploy more APIs to meet digital demands, their security processes are falling behind. Our research shows that a majority of APIs are left unmanaged, which not only exposes data, but also magnifies risk at every level of operation."
> 
> — Tristan Kalos, CEO of Escape

The State of API Exposure 2024 report provides an in-depth analysis of the significant risks associated with exposed APIs, highlighting vulnerabilities across large organizations, including Fortune 1000 companies and CAC 40 entities. Key findings reveal the pervasive nature of API security issues and the need for improved security measures:

- **1,834 Highly Critical Vulnerabilities in Fortune 1000 Companies**: Among the identified vulnerabilities, 1834 were classified as highly critical, directly affecting Fortune 1000 companies. These critical vulnerabilities, often associated with broken authentication and configuration errors, place essential systems and sensitive data at significant risk of exposure and exploitation. Critical issues span various sectors, impacting tech platforms, financial companies, insurance, healthcare, tech, and others.
- **Development APIs**: Nearly 4,000 development APIs were publicly accessible, often lacking adequate security controls. Exposing these APIs can inadvertently reveal sensitive information and offer attackers potential entry points.
- **Exposed Secrets**: The report found 1,816 highly sensitive secrets exposed within API environments, including access tokens, API keys, and authentication credentials. These exposed secrets significantly heighten the risk of unauthorized access and potential misuse of critical systems.

**Call to action**: We recommend to start auditing all APIs—particularly shadow and legacy APIs—to identify and secure vulnerabilities, and restricting access to development APIs with production-level security standards. Implementing continuous monitoring and scanning tools is crucial to detect risks early, while ensuring that all secrets are encrypted and securely managed to prevent exposure.

## Are We Ignoring Hidden Dangers?

- **10%** of IT organizations fully document their APIs[^1]
- **$31B** estimated losses due to API breaches[^3]
- **57%** of organizations suffered an API-related data breach in the past two years[^2]

### The Consequences of Unsecured APIs Exposed in the Wild

API sprawl has emerged as a significant challenge in recent years. As organizations increasingly rely on APIs to fuel digital transformation, connect services, and deliver data-driven experiences, the sheer number of APIs in production has skyrocketed.

As we move through 2024, the exponential growth of APIs presents new challenges. According to recent Gartner’s market guide, APIs - especially shadow and dormant ones - are causing data breaches among organizations that, on average, exceed the magnitude of other breaches.

Since 2022, at least 190M sensitive data records have been breached. In our previous research, we estimate that enterprise companies lost $31B due to breaches.

Many APIs are pushed to production too soon, often bypassing critical security testing stages or, in some cases, being tested only after deployment rather than within development environments. This rush to release frequently leads to gaps in security coverage, allowing untested or under-tested endpoints to expose sensitive information or become vulnerable to attack.

Another significant factor is the proliferation of "shadow APIs"—APIs that exist outside the knowledge or management of security teams. These undocumented, unmanaged, or abandoned APIs often lack essential security protocols, making them especially prone to exploitation. Shadow APIs can emerge from development shortcuts, legacy applications, or third-party integrations that slip through regular security oversight, creating hidden risks within the system’s architecture.

Given these trends, API security deserves greater attention. It is now widely recognized as a critical challenge requiring stringent security management and thorough testing before APIs are released into production environments. By analyzing Fortune 1000 and CAC 40 exposed API services we’re here to prove it.

[^1]: according to a 2023 report from Enterprise Management Associates (EMA)
[^2]: according to the 2025 Global State of API Security report
[^3]: according to Escape’s API Threat Landscape Report

## 2024's Cases of Vulnerable APIs Exposed in the Wild

- **Dell (May 2024)**: Experienced a significant data breach when a threat actor exploited an unsecured API endpoint on a partner portal. This vulnerability allowed unauthorized access to approximately 49 million customer records, including names, physical addresses, and order information.
- **Twilio (July 2024)**: Authy service suffered a significant breach due to an exposed API endpoint. This vulnerability allowed unauthorized access to authentication data, putting millions of users at risk. Attackers accessed one-time passcodes, a critical layer for multi-factor authentication.
- **Trello (January 2024)**: A vulnerability in Trello’s API configuration led to a massive data leak where over 15 million user records were exposed on a dark web forum. Misconfigurations in API permissions allowed hackers to scrape project details and personal information.
- **Deutsche Telekom (July 2024)**: Security expert Lilith Wittmann discovered an unprotected API that could retrieve details about landline connections via internet access. It exposed sensitive user data such as names, email addresses, and service usage details.

## Methodology

### Data Gathering Strategy
We selected domains from two primary sources:
- **Fortune 1000**: The 1000 largest public companies in the US (excluding Amazon, Google, and Meta to avoid skewing results).
- **CAC 40**: The 40 most significant stocks on Euronext Paris.

**Limitations**: We deliberately excluded governmental, educational, and health-related domains to align with ethical norms for web crawling.

### In-Depth API Discovery Process
We discovered 158,079 subdomains across ~1K unique top-level domains. Escape uses a combination of techniques:
1. **Subdomain enumeration**: Scanning for all subdomains associated with the main domain.
2. **AI-powered fingerprinting**: Recognizing and classifying API types (REST, GraphQL, gRPC) by analyzing structure and response patterns.
3. **OSINT techniques**: Gathering information from code repositories, documentation, and public resources.

### Automated API Specification Generation
- **4.5K** API specifications found in the wild.
- **29.7K** API specifications programmatically generated.

We used Large Language Models (LLMs) to parse the Abstract Syntax Tree (AST) from code to create detailed OpenAPI Specifications (OAS). This involved:
- **Semantic Analysis**: Identifying essential code fragments using custom rules (e.g., Semgrep patterns).
- **Specification Generation**: LLMs processing fragments to generate precise OAS methods.

### Final Step - API Security Scanning
- **30,784** API services scanned for vulnerabilities.

Using Escape’s Dynamic Application Security Testing (DAST), we conducted analysis in four stages:
1. **Contextual Analysis**: Identifying API structure, parameters, and dependencies.
2. **Fuzzing and Payload Injection**: Sending random or malformed inputs to identify validation flaws and injection vulnerabilities.
3. **Behavioral Monitoring**: Observing response patterns to detect data exposure or misconfigured permissions.
4. **Risk Prioritization**: Ranking vulnerabilities based on the Escape severity metric.

![Diagram showing the complete event-based architecture of the Escape Security Scanner, with the reinforcement loop in the center]

## Findings - API Exposure

- **30,784** API services exposed.
- **28.5K** among Fortune 1000.
- **3,001** APIs exposed by one Fortune 1000 organization (including 166 staging APIs).
- **3,945** development APIs exposed.
- **91%** REST APIs.
- **1,189** maximum exposed APIs per one domain.

### Most Common Cloud Providers Among Exposed API Services
- **AWS**: 51.1%
- **Azure**: 16%
- **Cloudflare**: 10.7%
- **Akamai**: 8.2%
- **GCP**: 7.5%
- **Fastly**: 4.9%
- **IBM**: 0.6%

![Chart showing the number of domains exposing a given range of API services, with the largest group (259,000) exposing 0-10 APIs]

## Findings - API Security

- **107,368** Total vulnerabilities found.
- **2,038** Highly critical.
- **98.8K** vulnerabilities found among Fortune 1000 (1.8K highly critical).
- **8.1K** vulnerabilities found among CAC40 (240 highly critical).
- **713** high risk CVEs found.
- **11** API services vulnerable to SQL injection.
- **10** API services vulnerable to BOLA.

### Alignment of High-Risk Fortune 1000 Vulnerabilities with OWASP Top 10 2023
- **API8:2023 (Security Misconfiguration)**: 746 instances
- **API2:2023 (Broken Authentication)**: 381 instances
- **API7:2023 (Server Side Request Forgery)**: 32 instances
- **API9:2023 (Improper Inventory Management)**: 30 instances
- **API1:2023 (Broken Object Level Authorization)**: 10 instances

### Industry Breakdown
Industries with the highest number of high-risk vulnerabilities:
1. Retail
2. Aerospace
3. Automotive
4. Real Estate
5. Insurance
6. Technology
7. Financial Services
8. Healthcare
9. Manufacturing

## Findings - API Secrets

We focused on secrets accessible through vulnerable APIs identified by DAST scans.
- **1,816** Total secrets found.
- **29** Highly critical.
- **38,000** High impact secrets found.

### Types of Secrets Found (Ordered by Frequency)
1. **JWT**: 17,000
2. **Password**: 8,000
3. **Generic API Keys**: 7,000
4. **Bearer Token**: 7,000
5. **md5**: 6,000
6. **AWS Access Token**: 5,000
7. **Github OAuth**: 5,000
8. **SSH URL**: 4,000
9. **YouTube apikey**: 3,000
10. **Phone number**: 3,000
11. **Plaid Secret Key**: 3,000
12. **Github App Token**: 2,000
13. **hashicorp_tf_password**: 2,000
14. **graphcms**: 1,000
15. **geocodio**: 1,000
16. **Jira Token**: 1,000
17. **jdbc**: 1,000

## Critical Findings: Exposed and Vulnerable Development APIs

- **3,945** exposed development APIs.
- **198** highly critical vulnerabilities.

A total of 3,945 development APIs were identified as publicly accessible, with 3,650 found among Fortune 1000 companies. These often bypass security controls for testing speed, revealing sensitive internal systems.

Six organizations were particularly impacted, each with over 100 exposed development APIs (five in Fortune 1000, one in CAC40). These environments often house experimental code that exposes paths into production systems.

## Critical Findings: Fortune 1000 at High Risk

- **1.8K** highly critical vulnerabilities found.
- **316** companies impacted.

Vulnerabilities like Broken Authentication (API2:2023) and Security Misconfiguration (API8:2023) were rampant.
- **API8 2023**: 62.2%
- **API2 2023**: 31.8%
- **API7 2023**: 2.7%
- **API9 2023**: 2.5%

We found 19 NoSQL injection vulnerabilities, 11 SQL injection flaws, and 10 instances of Broken Object Level Authorization (BOLA).

## American Multinational Tech Company: Exposed Spring Boot Actuator

Spring Boot Actuator provides features to monitor and manage applications. If unsecured, it exposes environment variables and configuration properties.

During an assessment of a major American tech company, we gained unrestricted access to:
- `.../admin/actuator/env`: Revealed critical environment variables in plain text (database credentials, API keys, service tokens).
- `.../admin/actuator/mappings`: Disclosed a comprehensive map of the API’s routing structure, including private routes.
- `.../admin/actuator/httptrace`: Offered a detailed log of recent HTTP requests, including session cookies and internal IP addresses.

### Recommended Remediation Steps
1. **Restrict Access**: Ensure endpoints are accessible only to authorized users on internal networks.
2. **Disable in Production**: Configure settings to disable `/env`, `/mappings`, and `/httptrace` in production.
3. **Obfuscate Data**: Redact sensitive variables in `/env` if it must be used.
4. **Monitor Access**: Implement logging for all access attempts to these endpoints.

## Standout Scenarios: High-Impact CVEs in the Wild

- **713** Total High Impact CVEs Found.
- **98** Distinct High Impact CVE Types.
- **102** High Impact CVEs in 2024.

### Top 5 CVE Occurrences
1. **CVE-2024-5535**: 95 instances
2. **CVE-2022-2274**: 70 instances
3. **CVE-2022-2068**: 70 instances
4. **CVE-2022-1292**: 57 instances
5. **CVE-2021-3711**: 57 instances

**Key Findings**:
- **OpenSSL Vulnerabilities**: Many CVEs are associated with OpenSSL; updates are critical.
- **Remote Code Execution (RCE)**: CVE-2022-2274 and CVE-2021-3711 pose severe risks.
- **Legacy Vulnerabilities**: A significant number of CVEs from 2020-2023 continue to impact APIs in production.

## Standout Scenarios: Mapping CVE to CWE

- **Improper Input Validation (CWE-20)**: Leads to injection attacks and unauthorized access.
- **Command Injection (CWE-78)**: Allows unauthorized command execution on the server.
- **Integer Overflow (CWE-190)**: Leads to buffer overflows or logic manipulation.
- **Cryptographic Issues (CWE-310)**: Exposes APIs to data interception or decryption.
- **NULL Pointer Dereference (CWE-476)**: Causes application crashes or denial of service.

## Essential Remediation Steps

1. **Conduct a Comprehensive API Audit**: Review all public-facing APIs, including staging and development.
2. **Deactivate Unused or Duplicate APIs**: Reduce the attack surface by removing redundant endpoints.
3. **Recheck for Exposed API Secrets**: Use automated scanning to ensure keys are not in public repositories or endpoints.
4. **Implement an API Governance Strategy**: Standardize development, documentation, and security processes.
5. **Enforce Authentication and Authorization**: Use OAuth 2.0, JWT, and RBAC.
6. **Implement Automated API Discovery**: Continuously scan and catalog shadow and unused APIs.
7. **Automated Security Scanning**: Use solutions that integrate into CI/CD for immediate vulnerability detection.
8. **Educate Internal Teams**: Enhance security culture through training and Security Champion programs.

## Immediate Steps to Take

![Flowchart diagram for API security decision making]

**Logic Flow**:
- **Any API** -> Are they open to the internet?
  - **No** -> Harden your API environment.
  - **Yes** -> Is it by design?
    - **No** -> Take immediate action (Deactivate, Scan for secrets).
    - **Yes** -> Am I deliberately using a critically vulnerable version?
      - **Yes** -> Patch immediately.
      - **No** -> Am I allowing access without authentication?
        - **Yes** -> Scan to verify no secrets are accessible.
        - **No** -> Harden security posture (Automate catalog, Scan for vulnerabilities).

## Conclusion

Securing APIs is difficult when you don't know what you have. Our study reveals over 100,000 vulnerabilities across Fortune 1000 and CAC 40 companies, with 1,800 classified as highly critical.

The extensive exposure of vulnerable development APIs and sensitive secrets (access tokens, API keys) highlights a systemic gap in security practices. Organizations must respond fast by adopting continuous, automated testing and robust risk mitigation strategies.

**Contact Information**:
- **Website**: escape.tech
- **Email**: ping@escape.tech
- **Phone**: +1 (707) 615 6448