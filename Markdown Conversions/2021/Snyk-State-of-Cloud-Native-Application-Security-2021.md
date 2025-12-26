# State of Cloud Native Application Security

## Table of Contents
- [Introduction](#introduction)
- [Key Findings](#key-findings)
- [Methodology](#methodology)
- [Detailed Analysis](#detailed-analysis)
  - [Cloud Native Adoption and Security Importance](#cloud-native-adoption-and-security-importance)
  - [Container and Serverless Workload Deployment](#container-and-serverless-workload-deployment)
  - [Deployment Automation](#deployment-automation)
  - [Security Incidents in Cloud Native Environments](#security-incidents-in-cloud-native-environments)
  - [Increased Security Concerns with Cloud Native Adoption](#increased-security-concerns-with-cloud-native-adoption)
  - [Areas of Concern in Cloud Native Security](#areas-of-concern-in-cloud-native-security)
  - [Deployment Automation and Security Testing](#deployment-automation-and-security-testing)
  - [Timing of Security Testing](#timing-of-security-testing)
  - [Frequency of Security Testing](#frequency-of-security-testing)
  - [Time to Fix Critical Vulnerabilities](#time-to-fix-critical-vulnerabilities)
  - [Automation Empowers Shift Left Security](#automation-empowers-shift-left-security)
  - [Security Practices Adoption by Company Size](#security-practices-adoption-by-company-size)
  - [Security Ownership in Cloud Native Environments](#security-ownership-in-cloud-native-environments)
  - [Developer and Security Professional Perspectives on Security Exposure](#developer-and-security-professional-perspectives-on-security-exposure)
- [Conclusion](#conclusion)
- [About Snyk](#about-snyk)

## Introduction

The official report URL is: https://snyk.io/lp/state-of-cloud-native-application-security/

This report examines the current landscape of cloud native application security, exploring how the adoption of cloud native technologies impacts security strategies and practices within organizations.

## Key Findings

*   99% of companies recognize security as important to their cloud native strategy.
*   Over 78% of production workloads are deployed as containers or serverless applications.
*   While 95% of respondents use automation, only 33% fully automate their deployment pipeline.
*   Misconfiguration and known unpatched vulnerabilities are the leading causes of security incidents.
*   Nearly 60% have increased security concerns since adopting cloud native.
*   Highly automated pipelines are twice as likely to incorporate security testing throughout their development lifecycle.
*   Over 72% of fully automated teams find and fix critical vulnerabilities in under 1 week.
*   Developers are increasingly taking ownership of cloud native security.

## Methodology

This report is based on a survey of organizations adopting cloud native technologies. The survey gathered data on their adoption levels, security practices, concerns, and incident experiences.

## Detailed Analysis

### Cloud Native Adoption and Security Importance

99% of companies recognized security as important to their cloud native strategy, with over 80% stating it is very important. While only 36% cited improved security as a main reason for moving production applications into containers, the overall recognition of security's importance highlights its critical role in successful cloud native adoption.

**How important is security to your cloud native strategy?**
*   Very important: 83%
*   Somewhat important: 16%
*   Not important: 1%

**What are the main reasons for moving your applications into containers?**
*   Deployment velocity: 68%
*   Ease of management: 67%
*   Reduce costs: 43%
*   Improved security: 36%
*   Attracting talent: 11%

### Container and Serverless Workload Deployment

Over 78% of production workloads are deployed as containers or serverless applications. Containers remain the dominant deployment mechanism, accounting for nearly 60% of production workloads. Serverless technologies have also gained significant traction, making up more than a fifth of all production workloads. The widespread use of Infrastructure as Code (IaC), with over 50% of respondents deploying workloads with it, indicates a strong trend towards software-driven infrastructure.

*   Containers: 58%
*   Serverless: 21%
*   IaC: 51%

### Deployment Automation

Deployment automation is a cornerstone of cloud native practices, enabling faster development velocity. Over 95% of respondents utilize some level of automation, with almost a third having an entirely automated deployment pipeline. Organizations with high levels of cloud native adoption are more than twice as likely to have an entirely automated deployment process compared to those with low adoption.

**Are your application deployments manual or automated?**

*   **High adoption:**
    *   Entirely automated: 42%
    *   Partially automated: 76%
    *   Not automated at all: 6%
*   **Low adoption:**
    *   Entirely automated: 18%
    *   Partially automated: 56%
    *   Not automated at all: 1.7%

Download Snyk’s Infrastructure as Code Security Insights report for trends on how companies are using and securing IaC today and common roadblocks to its widespread use. [Download now](https://snyk.io/lp/state-of-cloud-native-application-security/)

### Security Incidents in Cloud Native Environments

Misconfiguration and known unpatched vulnerabilities were the most frequent causes of security incidents in production cloud native environments, reported by 45% and 38% of respondents, respectively. Over 56% of organizations experienced a misconfiguration or known unpatched vulnerability incident involving their cloud native applications. Data leaks by insiders were more than twice as likely to occur in organizations with high levels of cloud native adoption, emphasizing the importance of zero trust principles in automated cloud environments.

**Incidents:**
*   Malware: 10%
*   Misconfiguration: 45%
*   Known unpatched vulnerabilities: 38%
*   Failed audit: 14%
*   Secret leaks: 21%
*   Data leaks by insider: 18%
*   Haven’t experienced any security incidents: 14%
*   Prefer not to answer: 7%

**Incidents by Adoption Level:**
*   **High adoption:**
    *   Misconfiguration: 50%
    *   Known unpatched vulnerabilities: 43%
    *   Secret leaks: 21%
    *   Data leaks by insider: 21%
*   **Low adoption:**
    *   Misconfiguration: 33%
    *   Known unpatched vulnerabilities: 18%
    *   Secret leaks: 14%
    *   Data leaks by insider: 14%

### Increased Security Concerns with Cloud Native Adoption

Adopting cloud native technologies has led to increased security concerns for nearly 60% of organizations. Only 15% reported decreased concerns, while 20% saw no change. This suggests that while cloud native offers benefits, it also introduces new security challenges and complexities.

**Has switching to Cloud Native technologies increased or decreased your security exposure concerns?**
*   Increased: 58%
*   Hasn’t changed: 20%
*   Decreased: 15%
*   Don’t know: 7%

### Areas of Concern in Cloud Native Security

Misconfiguration emerged as the biggest area of increased concern for over half of respondents since moving to a cloud native platform. Despite secret leaks and data leaks not appearing high in incident data, they are significant areas of worry, particularly among high adopters.

**Areas of concern:**
*   Malware: 34%
*   Known unpatched vulnerabilities: 45%
*   Data leaks by insider: 35%
*   Secret leaks: 50%
*   Insecure APIs: 44%
*   Misconfiguration: 53%
*   Ownership to handle/fix: 52%
*   Impact of security on deployment velocity: 16%
*   Ability to respond quickly to risks: 18%

**Areas of concern by adoption level:**
*   **High adoption:**
    *   Misconfiguration: 57%
    *   Secret leaks: 52%
    *   Ownership to handle/fix: 53%
*   **Low adoption:**
    *   Misconfiguration: 30%
    *   Secret leaks: 29%
    *   Ownership to handle/fix: 20%

### Deployment Automation and Security Testing

Highly automated pipelines are twice as likely to incorporate security testing throughout the development lifecycle. Automation provides integration points for security testing, creating a virtuous cycle. Organizations with high deployment automation levels were more than twice as likely to adopt security testing at all stages of the SDLC compared to those with no automation. Development teams in more automated organizations were also nearly twice as likely to adopt security early in their workflows.

### Timing of Security Testing

The timing of security testing varies significantly based on automation levels.

**When do you do security testing?**

*   **Entirely Automated:**
    *   Local development eg IDE’s and CLI tools: 44%
    *   Source Code repositories: 40%
    *   CI system: 43%
    *   Deployment time: 45%
    *   Production: 74%
*   **Not Automated:**
    *   Local development eg IDE’s and CLI tools: 24%
    *   Source Code repositories: 16%
    *   CI system: 16%
    *   Deployment time: 28%
    *   Production: 60%

**When do you do security testing? (By Company Size)**
*   **Enterprise:**
    *   Local development eg IDE’s and CLI tools: 42%
    *   Source Code repositories: 39%
    *   CI system: 50%
    *   Deployment time: 65%
    *   Production: 56%
*   **Medium:**
    *   Local development eg IDE’s and CLI tools: 34%
    *   Source Code repositories: 34%
    *   CI system: 40%
    *   Deployment time: 58%
    *   Production: 58%
*   **Small:**
    *   Local development eg IDE’s and CLI tools: 40%
    *   Source Code repositories: 40%
    *   CI system: 45%
    *   Deployment time: 64%
    *   Production: 36%

### Frequency of Security Testing

Continuous deployment empowers more frequent security testing. Nearly 70% of respondents with high deployment automation tested security daily or more frequently. This is 17 times more than respondents with no deployment automation, 60% of whom only tested monthly or less frequently.

**How often do you do security testing?**

*   **Entirely Automated:**
    *   Continuously or daily: 69%
    *   Weekly: 47%
    *   Monthly or less frequently: 12%
*   **Not Automated:**
    *   Continuously or daily: 4%
    *   Weekly: 24%
    *   Monthly or less frequently: 60%

**How often do you do security testing? (By Company Size)**
*   **Enterprise:**
    *   Continuously or daily: 54%
    *   Weekly: 44%
    *   Monthly or less frequently: 17%
*   **Medium:**
    *   Continuously or daily: 40%
    *   Weekly: 34%
    *   Monthly or less frequently: 20%
*   **Small:**
    *   Continuously or daily: 44%
    *   Weekly: 34%
    *   Monthly or less frequently: 29%

### Time to Fix Critical Vulnerabilities

Over 72% of fully automated teams find and fix critical vulnerabilities in under 1 week, with 36% fixing them in a day or less. Those with full automation were over 4x more likely to fix security issues in a day and over twice as likely to fix within a week. Organizations with low automation levels were more likely to not know their time to fix issues.

**Time to fix critical sec issues:**
*   **Not Automated:**
    *   1 day or less: 8%
    *   1 week: 24%
    *   2 weeks: 20%
    *   1 month: 18%
    *   Longer than 1 month: 28%
    *   Don't know: 3%
*   **Entirely Automated:**
    *   1 day or less: 36%
    *   1 week: 45%
    *   2 weeks: 12%
    *   1 month: 4%
    *   Longer than 1 month: 0%
    *   Don't know: 0%

### Automation Empowers Shift Left Security

Companies that automate are twice as likely to implement security testing. A broad and deep approach to security practices throughout the SDLC is crucial for successful Cloud Native Application Security. Organizations with higher levels of cloud native automation show greater adoption of security testing techniques like SAST, SCA, container image testing, and IaC scanning. Organizations with fully automated deployment pipelines are twice as likely to adopt SAST and SCA, and almost 3x as likely to adopt DAST. Policy compliance testing is still emerging, with only 23% adoption.

### Security Practices Adoption by Company Size

Enterprises are more likely to adopt security practices due to dedicated security teams. However, smaller organizations are keeping pace, especially in static testing. Over half of small organizations adopt SAST, SCA, and container image scanning.

**Which software development life cycle security practices are you following?**

*   **Entirely Automated:**
    *   Static code analysis (SAST): 70%
    *   Code scanning for package dependency vulnerabilities (SCA): 60%
    *   Dynamic Application Security Testing (DAST): 50%
    *   Interactive Application Security Testing (IAST): 40%
    *   Container image scanning: 30%
    *   Infrastructure as code (Terraform, Kubernetes): 20%
    *   Policy compliance tools (Open Policy Agent/Gatekeeper): 10%
*   **Not Automated:**
    *   Static code analysis (SAST): 40%
    *   Code scanning for package dependency vulnerabilities (SCA): 34%
    *   Dynamic Application Security Testing (DAST): 34%
    *   Interactive Application Security Testing (IAST): 26%
    *   Container image scanning: 19%
    *   Infrastructure as code (Terraform, Kubernetes): 15%
    *   Policy compliance tools (Open Policy Agent/Gatekeeper): 8%

**Which Software Development Life Cycle security practices are you following? (By Company Size)**
*   **Enterprise:**
    *   SAST: 70%
    *   SCA: 60%
    *   DAST: 50%
    *   IAST: 40%
    *   Container image scanning: 30%
    *   IaC: 20%
    *   Policy compliance: 10%
*   **Medium:**
    *   SAST: 60%
    *   SCA: 50%
    *   DAST: 40%
    *   IAST: 30%
    *   Container image scanning: 20%
    *   IaC: 15%
    *   Policy compliance: 8%
*   **Small:**
    *   SAST: 50%
    *   SCA: 45%
    *   DAST: 39%
    *   IAST: 32%
    *   Container image scanning: 26%
    *   IaC: 19%
    *   Policy compliance: 15%

Watch this on-demand webinar to learn tips for implementing security automation into modern development environments. [Watch Now](https://snyk.io/lp/state-of-cloud-native-application-security/)

### Security Ownership in Cloud Native Environments

The concept of DevSecOps has accelerated with cloud native adoption, shifting security left. Developers now play a pivotal role. While less than 10% of respondents in security roles believed developers were responsible for cloud native security, over 36% of developers stated they were responsible. Security teams are still adjusting to these shifting responsibilities, while development teams are increasingly aware of their growing role.

**Who is primarily responsible for the security of your cloud native environment and applications?**

*   **Developer response:**
    *   DevOps /DevSecOps: 31%
    *   Developers: 37%
    *   Application security team: 14%
    *   IT security team: 13%
    *   No-one: 3%
*   **Security response:**
    *   DevOps /DevSecOps: 33%
    *   Developers: 10%
    *   Application security team: 23%
    *   IT security team: 31%
    *   No-one: 2%

### Developer and Security Professional Perspectives on Security Exposure

Both developers and security professionals share increased security concerns since switching to cloud native technologies. Developers are as invested in good security outcomes as the security team, which is positive for DevSecOps adoption.

**Has switching to Cloud Native technologies increased or decreased your security exposure concerns?**

*   **Developer response:**
    *   Increased: 61%
    *   Hasn’t changed: 18%
    *   Decreased: 13%
*   **Security response:**
    *   Increased: 58%
    *   Hasn’t changed: 21%
    *   Decreased: 13%

Learn how Twilio’s Head of Product Security scaled through dev-first security and devsecops in a cloud native environment. [Watch Now](https://snyk.io/lp/state-of-cloud-native-application-security/)

## Conclusion

Snyk’s CNAS report shows clear movement in a positive direction. 99% of respondents recognize that security is important to their business strategy. That’s a world I want to live in.

## About Snyk

“Curious how Snyk can help? Snyk is a developer-first platform for building software securely. Learn more about how Snyk can help you secure cloud native applications across your IDEs, repos, containers, and pipelines.”

[Learn more](https://snyk.io/lp/state-of-cloud-native-application-security/)