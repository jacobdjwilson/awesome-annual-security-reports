# 2025 STATE OF DATA SECURITY REPORT
## QUANTIFYING AI’S IMPACT ON DATA RISK
Insights from 1,000 real-world IT environments

## Table of Contents
- [Shadow AI: A hidden threat to data security](#shadow-ai-a-hidden-threat-to-data-security)
- [Spotlight: Microsoft 365 Copilot data risk](#spotlight-microsoft-365-copilot-data-risk)
- [Spotlight: Salesforce Agentforce data risk](#spotlight-salesforce-agentforce-data-risk)
- [Model poisoning and risks to AI training data](#model-poisoning-and-risks-to-ai-training-data)
- [Ghosts in the machine: Exploiting the blast radius](#ghosts-in-the-machine-exploiting-the-blast-radius)
- [Cloud identities: Sprawling and complex](#cloud-identities-sprawling-and-complex)
- [Missing MFA: A critical security gap](#missing-mfa-a-critical-security-gap)
- [The state of data security: AI’s threat looms large](#the-state-of-data-security-ais-threat-looms-large)
- [About Varonis](#about-varonis)

---

### KEY FINDINGS

*   **90% of organizations have exposed sensitive cloud data.**
    While AI can drive progress, it can accelerate risk. Critical data that’s not locked down can be surfaced by AI. Exposed AI training data is vulnerable to breaches and model poisoning.
*   **88% have stale but enabled ghost users.**
    These accounts remain enabled, providing access to applications and data. Ghost users can allow attackers to conduct reconnaissance or exfiltrate data without tripping alarms.
*   **98% have unverified apps, including unsanctioned AI.**
    Shadow AI increases the risk of exposure and data breaches. Attackers can use unverified apps to exfiltrate data.
*   **99% of organizations have sensitive data dangerously exposed to AI tools.**

---

## ABOUT THIS REPORT

**Methodology**
Varonis analyzed data security risk across a wide range of industries and geographies:
- 1,000 organizations
- Nearly 10 billion cloud resources (objects, files, reports, attachments, etc.)
- More than 20 petabytes of data — approximately 20 terabytes per organization

**IaaS and SaaS applications and services reviewed:**
- [Image: List of cloud service icons]

**Firmographics**
This report includes data analysis across industries:
- Healthcare/biotech/pharma
- Finance
- Government/public sector
- Insurance and professional services
- Manufacturing
- Education
- Technology
- Consumer/retail
- And others…

**Countries included:**
United States, Canada, Germany, France, Belgium, Netherlands, Sweden, Switzerland, U.K., Spain, Italy, Brazil, Australia, India, and more.

---

## SHADOW AI: A HIDDEN THREAT TO DATA SECURITY

Shadow AI — unsanctioned gen AI applications — poses a significant threat to data security. These tools can bypass corporate governance and IT oversight, leading to potential data leaks.

Employees can accidentally leak sensitive or confidential data using shadow AI. If these apps fail to comply with GDPR, HIPAA, and other regulations, companies could be fined.

Stale apps can remain dangerous after a user’s last login. Stale OAuth applications, which haven’t been used or accessed for weeks or months, still have permission to access sensitive data.

> **In 2025, millions downloaded DeepSeek.**
> Employees who downloaded DeepSeek put their company’s data at risk — an unsecured DeepSeek database exposed a million lines of log streams containing chat history, secret keys, backend details, and other highly sensitive information, highlighting the critical need for organizations to scrutinize and secure all AI apps.

**DESPITE THE RISKS, OUR ANALYSIS FOUND:**
- **98%** of companies have employees using unsanctioned apps, including shadow AI. Each company has 1,200 unofficial apps on average.
- **52%** of employees use unverified OAuth apps.
- **1 in 4** (200 out of 800) high-risk OAuth apps in the average organization are high-risk.

---

## SPOTLIGHT: MICROSOFT 365 COPILOT DATA RISK

While unsanctioned apps can heighten the risk of data breaches, even sanctioned apps can threaten sensitive data. Microsoft 365 Copilot integrates deeply with an organization’s data to boost productivity. But it also introduces security risks. Copilot can surface all accessible data, potentially exposing critical information.

Exposed data is just one Copilot prompt away. Let’s consider a hypothetical insurance company with 2,000 employees: if each employee enters 20 prompts every day, five days a week, the company has over 200,000 chances for sensitive data to be exposed every week.

**WE FOUND:**
- **90%** of organizations have sensitive files exposed to all employees via M365 Copilot.
- **25,000+** sensitive folders are exposed to all employees on average.
- **6%** of organizations have sensitive files open to the internet.

Labeling files — ensuring data is accurately categorized, managed, and protected from AI misuse — is essential for data governance. Despite the importance of labeling, **only 1 out of 10 companies had labeled files.**

---

## SPOTLIGHT: SALESFORCE AGENTFORCE DATA RISK

Salesforce orgs contain a lot of sensitive data — PII, PCI, financial information, and more. Salesforce Agentforce can widen the gap if data is exposed. Agents can surface unprotected sensitive information through natural language prompting, leading to unauthorized data access and misuse.

**WE FOUND:**
- **100%** of companies have at least one account that can export all data.
- **1 in 10** accounts can freely export all Salesforce data.

Our analysis revealed an unexpectedly high number of users with powerful administrative permissions. 
- **11%** of users can grant permissions and install custom applications.

Many users also have permission to create public links. Open links can inadvertently enable AI applications, like ChatGPT, to crawl your organization’s internal data.

**WE FOUND THAT AN ALARMING NUMBER OF USERS CAN CREATE SHARING LINKS:**
- **92%** of companies allow users to create public links.
- **3,689** users can create public links in those companies.

---

## MODEL POISONING AND RISKS TO AI TRAINING DATA

As more organizations develop their own AI processes and products, the data used to train them is placed at risk from breaches and attacks. 

**WE FOUND:**
- **9 of 10** organizations have exposed sensitive data in the cloud.
- **66%** of companies have cloud data exposed to anonymous users.
- **2,000** unencrypted object stores in the average organization.
- **1,500** unencrypted databases in the average organization.

**Model Poisoning**
Another major risk is model poisoning, where attackers manipulate training data to corrupt an AI model’s performance. 

![Diagram showing 1. Attacker modifies payment information, 2. User asks AI for vendor’s bank details, 3. User receives attacker injected bank details]

---

## GHOSTS IN THE MACHINE: EXPLOITING THE BLAST RADIUS

Stale user accounts, or “ghost users,” are active accounts of former employees or contractors. 

**WE FOUND:**
- **88%** of organizations have stale but enabled ghost users, with 15,000 per organization on average.
- **176,000** inactive external identities in the average organization.
- **>31,000** stale permissions in the average organization.
- **7 of 8** organizations have sensitive data exposed to every user.

---

## CLOUD IDENTITIES: SPRAWLING AND COMPLEX

Cloud identity and entitlement management can involve thousands of permissions and roles. AWS alone has over 18,000 possible identity and access management permissions to manage.

**OUR ANALYSIS OF ORGANIZATIONS USING AWS SHOWED:**
- **20,224** managed policies in the average AWS account.
- **3,087** over-permissive policies in the average AWS account.

---

## MISSING MFA: A CRITICAL SECURITY GAP

Unenforced MFA simplifies attackers’ efforts, leaving accounts vulnerable to password spraying, credential stuffing, and phishing attacks.

**WE FOUND:**
- **1 in 7** organizations do not use or enforce MFA across their SaaS and multi-cloud environments.
- **1,800** users have non-expiring passwords in the average company.
- **5** global admins have passwords that never expire in the average company.

> **The "Cookie Bite" Attack**
> Varonis Threat Labs showed how attackers can bypass MFA using stolen browser cookies. By using custom-made malicious browser extensions and automation scripts, attackers can extract and reuse authentication cookies to impersonate users without needing credentials.

---

## THE STATE OF DATA SECURITY: AI’S THREAT LOOMS LARGE

The evidence is clear — organizations have a ticking time bomb in their data security strategy: AI.

1. **Reduce your blast radius.**
   Proactively decrease the damage an attacker can do with just one stolen identity.
2. **Data security is AI security.**
   To prevent AI risks and AI-related data breaches, continuously monitor your data, automate access governance and posture management, and employ proactive threat detection.
3. **Use AI for good.**
   AI is a powerful tool for defenders to identify, classify, and label sensitive data, remediate vulnerabilities, and catch malicious insiders.

---

## ABOUT VARONIS

The Varonis Data Security Platform was named a Leader and a Customer Favorite by a top analyst firm and was Gartner® Peer Insights™ Customer’s Choice and #1-rated DSPM.

**Request your free Data Risk Assessment.**

| Access to the Varonis platform | Dedicated IR analyst | Key findings report |
| :--- | :--- | :--- |
| Get full access to the Varonis Data Security Platform for the length of your assessment at no cost. | Our experts will monitor your data during your assessment and call you if they see anything alarming. | A detailed summary of your data security risks that is yours to keep, even if you don’t become a customer. |

[Get your assessment]