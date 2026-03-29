# State of Identity Security 2024

## Table of Contents
- [Executive Summary](#executive-summary)
- [Cloud Service Provider Adoption](#cloud-service-provider-adoption)
- [Human Identity Management](#human-identity-management)
- [Non-Human Identity Proliferation](#non-human-identity-proliferation)
- [Identity Inventory Visibility](#identity-inventory-visibility)
- [Identity Types Risk Ranking](#identity-types-risk-ranking)
- [The Visibility Mirage](#the-visibility-mirage)
- [Responsibility for Identity Security](#responsibility-for-identity-security)
- [Unauthorized Access Trends](#unauthorized-access-trends)
- [Cloud Security Breach Analysis](#cloud-security-breach-analysis)
- [Threat Detection Timelines](#threat-detection-timelines)
- [Cloud Security Tooling](#cloud-security-tooling)
- [Identity Security Budgets](#identity-security-budgets)
- [High-Risk Identity Identification](#high-risk-identity-identification)
- [Authentication Boundaries](#authentication-boundaries)
- [Security Maturity and Confidence](#security-maturity-and-confidence)
- [Detection and Response Concerns](#detection-and-response-concerns)
- [Top Security Concerns](#top-security-concerns)
- [Conclusion](#conclusion)

---

## Executive Summary

The Permiso Security State of Identity Security Report (2024) offers a comprehensive analysis of cloud identity and access management practices across global organizations. This study, encompassing over 500 entities, unveils critical trends and challenges shaping the future of identity security.

### Key Findings
- **93% of Organizations** can inventory identities across all environments, as well as track keys, tokens, certificates and any modifications that are made to any environment.
- **85% of Organizations** can determine “who” is doing “what” across authentication boundaries.
- **74% of Organizations** rate their cloud security maturity as “above average” to “advanced.”
- **56% of Organizations** rely on IT teams for securing identities across multiple environments.
- **45% of Organizations** reported an identity security breach.
- **45% of Organizations** remain “concerned” or “extremely concerned” about their current tools being able to detect against identity attacks.
- **In 56% of Breaches**, sensitive data including PII and IP was the target.
- **In 54% of Breaches**, impersonation attacks were the leading threat vector.
- **Employees** are the riskiest identity.
- **SaaS** is the riskiest environment.
- **The Leading Concern** is the ability to detect and prevent credential compromise, account takeover and insider threat.

---

## Cloud Service Provider Adoption

In 2024, we introduced a new question to understand the adoption of public cloud service providers like AWS, Azure, GCP, Oracle Cloud, IBM Cloud, and others. From 510 survey respondents, we gathered information on the cloud service providers being used across organizations.

### Key Findings
1. Organizations use an average of 2.5 cloud service providers.
2. AWS leads with 25% market share, followed by Azure (22%) with GCP at 7%.
3. IBM Cloud (20%) and Oracle Cloud (19%) show significant adoption.

These figures align closely with Statista's Q1 2024 market share data (AWS 31%, Azure 25%, GCP 10%), confirming our survey's representation of broader market trends.

---

## Human Identity Management

2024 marks a significant change in how organizations manage human identities across cloud and on-premise environments.

### Key Findings
- 48.4% of organizations now manage 1,000-5,000 identities, up from 39.1% in 2023.
- Organizations managing over 10,000 identities decreased from 16.2% to 8.2%.
- Small-scale identity management (under 1,000) slightly decreased from 17.2% to 15.1%.

---

## Non-Human Identity Proliferation

In 2024, we've witnessed a seismic shift in the identity landscape. Non-human identities – the silent workhorses of cloud environments – have exploded in number, fundamentally altering the security equation for organizations worldwide.

### Mid-Range Dominance
The most striking change is the concentration of non-human identities in the 1,000-5,000 range, now representing 42.2% of surveyed organizations. This surge possibly suggests a 'Goldilocks zone' where automation and cloud services are being leveraged extensively, yet still manageably.

---

## Identity Inventory Visibility

Our survey reveals an intriguing shift in organizations' ability to maintain a comprehensive inventory of identities accessing their cloud and on-premise environments.

- **2023:** 89% claimed comprehensive inventory
- **2024:** 93% report the same

As cloud environments become more complex, maintaining visibility across all identity types—from human users to non-human identities, across IaaS, PaaS, and SaaS—becomes increasingly challenging.

---

## Identity Types Risk Ranking

![Chart showing risk ranking of identity types: Employees (Highest Risk), Vendors, Guests, Non-Human Identities (Lowest Risk)]

Employees, perennially seen as the weakest link in the security chain, predictably top the list. However, the positioning of non-human identities as least risky raises red flags. In an era where machine identities often outnumber human users and possess extensive privileges, this low-risk perception could be a ticking time bomb.

---

## The Visibility Mirage

In 2023, 90% of respondents claimed the ability to monitor services and resources accessed by identities in real-time across their cloud environments. Fast forward to 2024, and we see a slight uptick to 93% when asked about tracking the usage of keys, tokens, and certificates, as well as environmental modifications.

> "Truly understanding how all identities—both human and non-human—behave is more than a technical issue; it’s essential for business. Closing the gap between what we think and what’s real in identity monitoring is key to building strong, flexible security systems for the future." — Paul Nguyen, Co-Founder and Co-CEO, Permiso Security

---

## Responsibility for Identity Security

Our survey reveals a shocking reality: Despite identity being the cornerstone of modern cybersecurity, in more than half of organizations, IT departments, not specialized identity teams, are responsible for securing identities.

- A staggering 56% of organizations assign identity security to IT departments.
- Dedicated IAM teams are in charge in only 7% of cases.
- Traditional security teams (15%) and cloud security teams (21%) play smaller roles.

---

## Unauthorized Access Trends

The 2024 survey results reveal that unauthorized access remains a significant threat in cloud environments.

- 46% of organizations reported unauthorized access incidents.
- 5% remained unsure.
- 50% claimed no such breaches.

---

## Cloud Security Breach Analysis

### 1. The Multifaceted Nature of Cloud Vulnerabilities
SaaS environments emerge as the most vulnerable, with 76% of affected organizations reporting breaches in these platforms. This is followed by IaaS (58%), PaaS (48%), and Identity Providers (43%).

### 2. The Taxonomy of Threat Vectors
Impersonation attacks (54%) and credential compromise (53%) top the list of threat vectors, closely followed by insider risks (47%) and privilege access abuse (46%).

### 3. The Cascade of Consequences
- 54% resulted in sensitive data compromise.
- 46% led to privilege escalation or lateral movement.
- 45% impacted supply chains.
- 42% saw ransomware deployment.
- 39% established persistence.

---

## Threat Detection Timelines

Our 2023-2024 survey reveals significant changes in organizations' ability to detect compromised identities in cloud environments.

- **24-Hour Detection Window:** 61% of organizations claim detection within 24 hours.
- **Consistency in Weekly Detection:** 93% can detect threats within a week.
- **Extended Detection Times:** 6% of respondents now need more than a week for detection, up from 1% in 2023.

---

## Cloud Security Tooling

While cloud-native tools remain dominant at 66% adoption in 2024, the significant rise of CSPM (from 48% to 57%) indicates a market shift towards diversified security strategies.

- **Layered Security Approach:** 66% use cloud-native solutions, 57% employ CSPM/CNAPP, and 42% utilize ITDR-CDR.
- **Emerging Technology:** SSPM adoption (41%) nearly matches ITDR-CDR (42%) in its first year.

---

## Identity Security Budgets

- **The SaaS-First Mentality:** SaaS leads with 87% budget allocation, surpassing IaaS (81%).
- **The Hybrid Reality:** 65% still allocate budget to on-premises security.
- **The PaaS Puzzle:** 71% budget for PaaS security.
- **The Holistic Minority:** Only 46% report budgeting for "All environments."

---

## High-Risk Identity Identification

A significant 86% of organizations report they can identify their top 10 riskiest identities across all environments. However, 14% of organizations admit they cannot identify their riskiest identities, representing a considerable security vulnerability.

---

## Authentication Boundaries

When asked if they can answer “who” is doing “what” across fragmented authentication boundaries (e.g., Okta -> GitHub -> Terraform -> AWS), nearly 85% of organizations claim they can. This may indicate advanced systems, or a potential underestimation of the true complexity of their environments.

---

## Security Maturity and Confidence

- **Cloud Security Maturity:** Nearly half (45%) rate their cloud security maturity at an “advanced” level.
- **Confidence:** 72% of organizations feel "Secure" or "Very Secure" in their identity security defenses.

---

## Detection and Response Concerns

Despite confidence, concern is palpable. Nearly half (45%) of respondents reported being “concerned” or “extremely concerned” that their current tools may not be able to detect and respond to a security event in their environment.

---

## Top Security Concerns

1. **Weaknesses in Current Defenses:** Credential compromise, account takeovers, and insider threats.
2. **Excessive Attack Surface:** Zombie accounts, identity sprawl, and privilege creep.
3. **Authentication Woes:** MFA and Security Token implementation gaps.

---

## Conclusion

The Permiso Security State of Identity Security Report (2024) underscores the pivotal role of identity security management. The data reveals a mixed picture of progress and persistent challenges. The "confidence-capability gap" poses a substantial risk, potentially leaving organizations exposed to sophisticated, identity-based attacks.

The path forward is clear: identity must be at the center of cloud security strategies. Only by placing identity at the core of security architectures can organizations hope to navigate the complexities of modern cloud environments securely and effectively.

---
QUESTIONS? CONTACT US AT HELLO@PERMISO.IO