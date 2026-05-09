# The State of Non-Human Identity Security

## Table of Contents
- [Acknowledgments](#acknowledgments)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
  - [Key Finding 1: High Anxiety, Low Confidence When Securing NHIs](#key-finding-1-high-anxiety-low-confidence-when-securing-nhis)
  - [Key Finding 2: Struggling with the Basics of NHI Security](#key-finding-2-struggling-with-the-basics-of-nhi-security)
  - [Key Finding 3: Challenges with Managing Permissions and API Keys](#key-finding-3-challenges-with-managing-permissions-and-api-keys)
  - [Key Finding 4: Fragmented Approaches Lead to Security Incidents](#key-finding-4-fragmented-approaches-lead-to-security-incidents)
  - [Key Finding 5: Investment in NHI Security Capabilities on the Rise](#key-finding-5-investment-in-nhi-security-capabilities-on-the-rise)
- [Conclusion](#conclusion)
- [Full Survey Results](#full-survey-results)
  - [NHI Security Opinions, Concerns, and Challenges](#nhi-security-opinions-concerns-and-challenges)
  - [NHI Security Incidents](#nhi-security-incidents)
  - [NHI Security Strategy](#nhi-security-strategy)
  - [Third-Party Vendor Management](#third-party-vendor-management)
  - [Service Account Permissions Management](#service-account-permissions-management)
  - [API Key Management](#api-key-management)
  - [Secrets Management](#secrets-management)
- [Demographics](#demographics)
- [Survey Creation and Methodology](#survey-creation-and-methodology)
  - [Goals of the Study](#goals-of-the-study)

---

## Acknowledgments

**Lead Author**
Hillary Baron

**Contributors**
Josh Buker, Marina Bregkou, Ryan Gifford, Sean Heide, Alex Kaluza, John Yeoh

**Graphic Designer**
Claire Lehnert

**Special Thanks**
Danielle Guetta and Tal Skverer

**About the Sponsor**
Astrix Security is the first solution built to secure and manage the lifecycle of NHIs, helping enterprises like NetApp, Priceline, Figma and Agoda control their NHI attack surface and prevent supply chain attacks. The platform provides continuous discovery, posture management, threat detection and automatic remediation for NHIs across business and engineering environments.

---

## Executive Summary

Non-human identities (NHIs) such as bots, API keys, service accounts, OAuth tokens, and secrets are indispensable for automating tasks, enhancing efficiency, and driving innovation within organizations. However, these NHIs also present unique security challenges. This executive summary highlights the key findings, challenges, and recommendations derived from the survey results.

1. **High Anxiety, Low Confidence in NHI Security**
   - Only 15% of organizations feel highly confident in preventing NHI attacks, compared to 25% for human identities. This disparity is due to the vast number of NHIs, which can outnumber human identities by a factor of 20 to 1.
   - 69% of organizations express moderate to high concern about NHIs as an attack vector, indicating awareness of the risks but a lack of confidence in current security measures.

2. **Struggles with Fundamental NHI Security Practices**
   - Managing service accounts is a significant challenge, with 32% of organizations highlighting it as a major pain point.
   - Auditing and monitoring (25%), access and privilege management (25%), discovering NHIs (24%), and policy enforcement (21%) are cited as critical yet challenging areas.
   - Visibility into third-party vendors connected by OAuth apps is limited, with 38% of organizations reporting no or low visibility.

3. **Challenges with Managing Permissions and API Keys**
   - Organizations face difficulties managing permissions and API keys, particularly with existing service accounts, highlighting the issue of tech debt.
   - Only 20% have formal processes for offboarding and revoking API keys, and even fewer have procedures for rotating them.
   - Manual handling of API keys leads to delays and inefficiencies, with nearly 40% of organizations taking weeks or more to offboard keys.

4. **Fragmented Security Approaches Lead to Incidents**
   - Many organizations rely on a mix of security tools not specifically designed for NHIs, leading to a lack of cohesion and effectiveness.
   - Common causes of NHI security incidents include lack of credential rotation (45%), inadequate monitoring (37%), and overprivileged accounts (37%).

5. **Increasing Investment in NHI Security**
   - There is a promising trend towards increased investment in NHI security capabilities, with 24% of organizations planning to invest within the next six months and 36% within the next 12 months.

---

## Key Findings

Non-human identities (NHIs) like bots, API keys, service accounts, OAuth tokens, and secrets are essential for keeping today’s organizations running smoothly. They automate tasks, boost efficiency, and drive innovation. But with these benefits come unique security challenges. NHIs operate 24/7, handle sensitive data, and perform actions at lightning speed, making them prime targets for cyberattacks.

### Key Finding 1: High Anxiety, Low Confidence When Securing NHIs

**Confidence in preventing NHI attacks**
Organizations are grappling with their current NHI security strategies. Only 15% of organizations feel highly confident in their ability to prevent an attack through NHIs. In comparison, confidence in preventing an attack through human identities is higher, with 25% expressing high confidence.

![Confidence levels in human identity vs NHI attack prevention]

This means that only 1.5 out of 10 organizations are highly confident about NHI security, compared to nearly 1 in 4 for human identity security. This disparity could be due to the sheer number of NHIs in their environment, which often outnumber human identities by a factor of 20 to 1.

**NHI as an attack vector**
![Concern levels about NHI as an attack vector]

The high volume of NHIs significantly amplifies the security challenges organizations face. Each NHI can potentially access sensitive data and critical systems, increasing the attack surface exponentially. Without adequate visibility and control over these NHIs, the risk of security incidents rises. Organizations’ lack of confidence suggests their current NHI security methods are lagging behind their human identity security methods.

The data further reveals that 69% of organizations are moderately-to-very concerned about NHIs as an attack vector.

### Key Finding 2: Struggling with the Basics of NHI Security

**Top challenges in NHI security**
With the high rates of concern regarding NHI attacks, it was important to dig deeper into the specifics. One of the biggest pain points for organizations is managing service accounts. This is a significant challenge, with 32% of organizations citing service accounts as one of the most challenging aspects to manage.

![Users in Snowflake Environments]

In Snowflake environments, 23% of users are actually service accounts, underscoring the scale of this issue. Service accounts, due to their elevated privileges and widespread usage, represent a substantial security risk if not properly managed.

Beyond service accounts, organizations struggle with fundamental security practices related to NHIs. Auditing and monitoring (25%), access and privileges (25%), discovering NHIs (24%), and policy enforcement (21%) are all cited as major challenges.

![Most challenging aspects of NHI management]

**Visibility into third-party vendors**
Another significant concern is the struggle to gain visibility into third-party vendors connected by OAuth apps. The survey indicates that 38% of organizations report no or low visibility into third-party vendors connected by OAuth apps, and another 47% have only partial visibility.

![Visibility levels into third-party vendors connected by OAuth apps]

![Percentages of Untrusted Third-Party Vendors by Marketplace]

**Reactive security leads to security gaps**
The downstream effect is that the process of managing NHI security is reactive. Only 22% of organizations review permissions for service accounts yearly, while 19% do so randomly, when needed.

![Frequency of review for service account permissions]

### Key Finding 3: Challenges with Managing Permissions and API Keys

**Difficulties with service accounts and tech debt**
One of the significant struggles organizations face is managing permissions and API keys effectively. Survey data reveals that managing permissions is notably easier for new service accounts than for existing ones.

![Difficulty levels of managing permissions for new versus existing service accounts]

**Managing and offboarding API keys**
The management of API keys is another critical area where organizations falter. Only 20% have a formal process for offboarding and revoking API keys, and even fewer (16%) have a process for rotating or rolling back API keys.

![Type of process for API key offboarding/revoking versus rotating/rolling back]

**Manually offboarding API keys lead to long timelines**
Only 19% of organizations have automated processes for offboarding, and 16% for rotating/rolling back API keys. The survey shows that nearly 40% of organizations take weeks or more to offboard API keys.

![Timeline for API key offboarding versus rotating/rolling back]

### Key Finding 4: Fragmented Approaches Lead to Security Incidents

**Current tooling is inadequate**
The reason organizations are struggling with the basics of NHI security may stem from a fragmented approach to managing NHI security. Many organizations are not using tools specifically designed for NHI security.

![Solutions and strategies currently used to manage NHIs]

Key security tool capabilities being sought include visibility into third-party vendors connected through OAuth apps (26%), management of the secrets lifecycle (26%), identity discovery (25%), management of API keys (23%), managing permissions (22%), tracking access behavior/anomaly detection (22%), and automating third-party connectivity (21%).

![Most important security tool capabilities for NHI security]

**NHI security incidents and causes**
The security incidents experienced by organizations further highlight the inadequacies of their current strategies. While 17% of organizations were able to verify that they had an NHI-related security incident at their organization, another 35% were unsure.

![Experienced security incidents related to NHI]

Common causes of NHI security incidents include a lack of credential rotation (45%), inadequate monitoring and logging (37%), and overprivileged accounts/identities (37%).

![Causes of NHI security incidents]

![Tokens with vs without Expiry in GitHub Environments]
![Misconfigured vs Properly Configured Webhooks in GitHub]

### Key Finding 5: Investment in NHI Security Capabilities on the Rise

Organizations are recognizing the critical importance of NHI security and are planning to significantly ramp up their investment in this area.

![Plans to invest in NHI security capabilities]

This trend towards increased investment indicates that organizations are starting to take the concerns about NHI security and the struggles with basic security practices seriously.

---

## Conclusion

There is a promising shift as many organizations are planning to invest significantly in NHI security capabilities. This planned investment indicates a growing recognition of the importance of proactively addressing NHI security. By unifying their strategies, adopting NHI-specific tools, and automating critical processes, such as permission management and API key handling, organizations can enhance their security posture and better protect against evolving threats.

---

## Full Survey Results

### NHI Security Opinions, Concerns, and Challenges
- [Confidence levels in human identity vs NHI attack prevention]
- [Concern levels about NHI as an attack vector]
- [Most challenging aspects of NHI management]
- [Concern levels about NHI access levels]
- [Most concerning NHI threats, risk, and vulnerabilities]

### NHI Security Incidents
- [Confidence levels in responding effectively to NHI security incidents]
- [Experienced security incidents related to NHI]
- [Causes of NHI security incidents]

### NHI Security Strategy
- [Solutions and strategies currently used to manage NHIs]
- [Most important security tool capabilities for NHI security]
- [Plans to invest in NHI security capabilities]

### Third-Party Vendor Management
- [Visibility levels into third-party vendors connected by OAuth apps]
- [Challenges with maintaining or improving visibility into third-party vendors connected by OAuth apps]
- [Difficulty levels for managing requests to add third-party tools and services]
- [Balancing user freedom and security for business integrations]
- [Challenges for implementing secure automation and connectivity]

### Service Account Permissions Management
- [Estimated % of Over-Permissive Accounts in Organizations]
- [Frequency of review for service account permissions]
- [Difficulty levels of managing permissions for new versus existing service accounts]

### API Key Management
- [Type of process for API key offboarding/revoking versus rotating/rolling back]
- [Timeline for API key offboarding versus rotating/rolling back]

### Secrets Management
- [Methods for storing and managing secrets]
- [Confidence levels in storing and managing secrets]
- [Capabilities used for secrets management in application development]

---

## Demographics

The survey was conducted online by CSA in June 2024 and received 818 responses from IT and security professionals from organizations of various sizes and locations.

- **Region**: Americas (49%), EMEA (28%), APAC (23%)
- **Organization Size**: <100 (24%), 101-1000 (21%), 1001-5000 (18%), 5001-10000 (28%), +10001 (10%)
- **Job Level**: Director (36%), Manager (35%), Staff (15%), Other (5%), C-level or executive (8%)
- **Industry**: Telecommunications/Tech (33%), Finance (18%), Healthcare (5%), Education (5%), Manufacturing (4%), etc.

---

## Survey Creation and Methodology

The Cloud Security Alliance (CSA) is a not-for-profit organization with a mission to widely promote best practices and ensure cybersecurity in cloud computing and IT technologies.

Astrix commissioned CSA to develop a survey and report to better understand the industry’s knowledge, attitudes, and opinions regarding non-human identity (NHI) security and its challenges. The survey was conducted online by CSA in June 2024 and received 818 responses from IT and security professionals.

### Goals of the Study
The primary objectives of the survey were to gain a deeper understanding of several critical aspects of NHI, such as:
- The perceptions and concerns around non-human identities
- Current security efforts, policies, and management of non-human identities
- Challenges with connecting to third-party vendors
- Current management and policies for API keys