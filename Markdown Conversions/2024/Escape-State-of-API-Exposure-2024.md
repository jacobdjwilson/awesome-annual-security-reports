# State of API Exposure 2024

Fortune 1000 at Risk: How we discovered 30,000 exposed APIs & 100,000 API issues in the world’s largest organizations

## Table of Contents
- [Dangers of Unsecured Exposed APIs](#dangers-of-unsecured-exposed-apis)
- [Methodology](#methodology)
- [Our Findings](#our-findings)
- [Exposed and Vulnerable Development APIs](#exposed-and-vulnerable-development-apis)
- [Fortune 1000 at Risk](#fortune-1000-at-risk)
- [American Multinational Tech Company: Exposed Spring Boot Actuator](#american-multinational-tech-company-exposed-spring-boot-actuator)
- [CVEs Found](#cves-found)
- [Essential Remediation Steps](#essential-remediation-steps)
- [Conclusion](#conclusion)

---

We analyzed the domains of the world’s largest organizations included in the Fortune 1000 and CAC 40. Here’s what we found:

- **30,784** Exposed APIs
- **3,945** Development APIs exposed
- **1,816** Secrets accessible in API services
- **2,038** Highly critical vulnerabilities

## Key Takeaways

> "Scaling API security is a fundamental challenge. As organizations deploy more APIs to meet digital demands, their security processes are falling behind. Our research shows that a majority of APIs are left unmanaged, which not only exposes data, but also magnifies risk at every level of operation."
> — Tristan Kalos, CEO of Escape

The State of API Exposure 2024 report provides an in-depth analysis of the significant risks associated with exposed APIs, highlighting vulnerabilities across large organizations, including Fortune 1000 companies and CAC 40 entities.

- **1,834 Highly Critical Vulnerabilities in Fortune 1000 Companies**: These critical vulnerabilities, often associated with broken authentication and configuration errors, place essential systems and sensitive data at significant risk.
- **Development APIs**: Nearly 4,000 development APIs were publicly accessible, often lacking adequate security controls.
- **Exposed Secrets**: The report found 1,816 highly sensitive secrets exposed within API environments, including access tokens, API keys, and authentication credentials.

**Call to action**: We recommend auditing all APIs—particularly shadow and legacy APIs—to identify and secure vulnerabilities, and restricting access to development APIs with production-level security standards.

---

## Dangers of Unsecured Exposed APIs

![Infographic showing 10% of IT organizations fully document their APIs, $31B estimated losses due to API breaches, and 57% of organizations suffered an API-related data breach in the past two years.]

API sprawl has emerged as a significant challenge. As we move through 2024, the exponential growth of APIs presents new challenges. According to recent Gartner’s market guide, APIs—especially shadow and dormant ones—are causing data breaches among organizations that, on average, exceed the magnitude of other breaches.

### 2024's Cases of Vulnerable APIs Exposed in the Wild
- **Dell**: In May 2024, a threat actor exploited an unsecured API endpoint on a partner portal, exposing 49 million customer records.
- **Twilio (Authy)**: In July 2024, an exposed API endpoint allowed unauthorized access to authentication data.
- **Trello**: A configuration error in January 2024 led to a leak of over 15 million user records.
- **Deutsche Telekom**: In July 2024, an unprotected API allowed the retrieval of details about landline connections.

---

## Methodology

### Data Gathering Strategy
We selected domains from two primary sources:
1. **Fortune 1000**: The 1000 largest public companies in the US (excluding major tech giants like Amazon, Google, and Meta).
2. **CAC 40**: The 40 most significant stocks on Euronext Paris.

### In-Depth API Discovery Process
Escape uses a sophisticated combination of techniques:
- **Subdomain enumeration**: Scanning for all subdomains associated with the main domain.
- **AI-powered fingerprinting**: Classifying API types (REST, GraphQL, gRPC) with high accuracy.
- **OSINT techniques**: Gathering publicly available information from code repositories and documentation.

### Automated API Specification Generation
Through our initial scan, we located 4,547 exposed API specifications and programmatically generated 29,700 more by parsing the Abstract Syntax Tree (AST) from code using Large Language Models (LLMs).

### Final step - API Security Scanning
Using Escape’s Dynamic Application Security Testing (DAST) solution, we conducted an in-depth analysis of each identified API endpoint. The process involves:
1. **Contextual Analysis**
2. **Fuzzing and Payload Injection**
3. **Behavioral Monitoring**
4. **Risk Prioritization**

![Diagram of the event-based architecture of the Escape Security Scanner]

---

## Our Findings

### Findings - API Exposure
- **30,784** API services exposed.
- **91%** are REST APIs.
- **Cloud Providers**: AWS (51.1%), Azure (16%), Cloudflare (10.7%), Akamai (8.2%), GCP (7.5%), Fastly (4.9%), IBM (0.6%).

### Findings - API Security
- **107,368** Total vulnerabilities found.
- **2,038** Highly critical vulnerabilities.
- **713** High-risk CVEs found.

### Findings - API Secrets
- **1,816** Total secrets found.
- **38,000** High-impact secrets found (including AWS Access Tokens, GitHub OAuth, and Bearer Tokens).

---

## Exposed and Vulnerable Development APIs

We uncovered 3,945 exposed development APIs, with 198 highly critical vulnerabilities. Six organizations were particularly impacted, each with over 100 exposed development APIs.

---

## Fortune 1000 at Risk

We identified 1,830 highly critical vulnerabilities affecting 316 Fortune 1000 companies. According to the OWASP API Security Top 10 for 2023, the most rampant issues were:
- **API8:2023 (Security Misconfiguration)**: 62.2%
- **API2:2023 (Broken Authentication)**: 31.8%

---

## American Multinational Tech Company: Exposed Spring Boot Actuator

During a security assessment, we gained unrestricted access to Spring Boot Actuator endpoints (`/env`, `/mappings`, `/httptrace`) on a major tech company's domain.

**Recommended Remediation Steps:**
1. **Restrict Access**: Ensure endpoints are only accessible to authorized internal users.
2. **Disable in Production**: Configure settings to disable sensitive endpoints in production.
3. **Obfuscate Data**: Redact sensitive environment variables.
4. **Monitor Access**: Log all access attempts to these endpoints.

---

## CVEs Found

We found 713 high-impact CVEs. The top 5 occurrences include:
- **CVE-2024-5535** (95 instances)
- **CVE-2022-2274** (70 instances)
- **CVE-2022-2068** (70 instances)
- **CVE-2022-1292** (57 instances)
- **CVE-2021-3711** (57 instances)

### Mapping CVE to CWE
- **CWE-20**: Improper Input Validation
- **CWE-78**: Command Injection
- **CWE-190**: Integer Overflow
- **CWE-310**: Cryptographic Issues
- **CWE-476**: NULL Pointer Dereference

---

## Essential Remediation Steps

1. **Conduct a Comprehensive API Audit**: Identify and categorize all public-facing APIs.
2. **Deactivate Unused or Duplicate APIs**: Reduce the attack surface.
3. **Recheck for Exposed API Secrets**: Use automated secret scanning tools.
4. **Implement an API Governance Strategy**: Standardize development and security processes.
5. **Enforce Authentication and Authorization**: Use OAuth 2.0 and JWT.
6. **Implement Automated API Discovery**: Continuously catalog all APIs.
7. **Implement an Automated Security Solution**: Use DAST for rapid vulnerability detection.
8. **Educate Your Internal Teams**: Implement a Security Champion Program.

---

## Conclusion

Our study reveals that over 100,000 vulnerabilities are present across Fortune 1000 and CAC 40 companies. Organizations must respond by adopting best practices for risk mitigation and integrating continuous, automated testing of their applications.

For more information, visit [escape.tech](https://escape.tech).