# State of Cloud Native Application Security
Organization: Snyk  
Report Title: State-of-Cloud-Native-Application-Security  
Year: 2021  

## Table of Contents
- [Introduction: Cloud Native Adoption and Security](#introduction-cloud-native-adoption-and-security)
- [Production Workloads: Containers and Serverless](#production-workloads-containers-and-serverless)
- [Deployment Automation](#deployment-automation)
- [Production Incidents and Security Concerns](#production-incidents-and-security-concerns)
- [Deployment Automation and Security Testing](#deployment-automation-and-security-testing)
- [Vulnerability Remediation Speeds](#vulnerability-remediation-speeds)
- [Software Development Life Cycle Security Practices](#software-development-life-cycle-security-practices)
- [DevSecOps and Security Ownership](#devsecops-and-security-ownership)

---

## Introduction: Cloud Native Adoption and Security

As cloud native adoption increases, security needs to be built in as standard. Success in the cloud native era is defined by an organization's ability to deliver new versions of software faster and more efficiently, which is reinforced by our survey results. Being able to deploy code to production faster and more easily manage those applications were the primary reasons for moving towards containerized infrastructure. 

### What are the main reasons for moving your applications into containers?
- Deployment velocity: 68%
- Ease of management: 67%
- Reduce costs: 43%
- Improved security: 36%
- Attracting security talent: 11%

### How important is security to your cloud native strategy?
While only 36% of respondents stated that security was one of the main reasons for moving their production applications into containers, 99% of respondents recognized security as an important element in their cloud native strategy. In addition, over 80% stated security is very important to them.

- **Very important:** 83%
- **Somewhat important:** 16%
- **Not important:** 1%

Snyk Report: State of Cloud Native Application Security | 01

---

## Production Workloads: Containers and Serverless

### Over 78% of production workloads are deployed as containers or serverless applications

In total over 78% of production workloads are deployed as containers or serverless applications. Containers continue to be the dominant mechanism for cloud native application deployment, with nearly 60% of production workloads deployed in containers. Penetration of serverless technologies is now significant across all company sizes, and makes up more than a fifth (mean average) of all production workloads. Usage of cloud native technologies is strong across all company sizes, indicating that adoption is becoming mainstream. With over 50% of respondent’s workloads also being deployed with some form of Infrastructure As Code, use of software-driven infrastructure has increased alongside the container and serverless growth trends. Usage of these core technologies is one of the key indicators of cloud native transformation in general, and so we use these metrics throughout this report as indicative of the level of adoption within an organization.

- **Containers:** 58%
- **Serverless:** 21%
- **IaC:** 51%

Snyk Report: State of Cloud Native Application Security | 02

---

## Deployment Automation

### While 95% of respondents use automation, only 33% fully automate their deployment pipeline

Deployment automation is one of the key tenets of cloud native practices, enabling development velocity. Our survey showed that over 95% of respondents were using some level of automation with almost a third having an entirely automated deployment pipeline. By comparing the upper and lower quartiles of cloud native production usage (high levels of adoption vs low levels of adoption), we can see that organizations that show high levels of cloud native adoption are over twice as likely to have an entirely automated deployment process than organizations with low cloud native adoption.

#### High adoption
- **Entirely automated:** 42%
- **Partially automated:** 56%
- **Not automated at all:** 1.7%

#### Low adoption
- **Entirely automated:** 18%
- **Partially automated:** 76%
- **Not automated at all:** 6%

> ![Download Snyk’s Infrastructure as Code Security Insights report for the trends on how companies are using and securing IaC today and common roadblocks to it’s wide spread use](Download now)

Snyk Report: State of Cloud Native Application Security | 03

---

## Production Incidents and Security Concerns

### Misconfiguration and known unpatched vulnerabilities were responsible for the greatest number of security incidents in cloud native environments

In contrast to where organizations are most concerned, we also asked about previous incidents that occurred in production. The top two incident types by a distance were misconfiguration and known unpatched vulnerabilities, at 45% and 38% respectively. Over 56% experienced a misconfiguration or known unpatched vulnerability incident involving their cloud native applications.

Data leaks by insiders were more than twice as likely to have occurred in organizations with high levels of cloud native adoption, reinforcing that adopting zero trust principles becomes increasingly important in fully automated cloud based environments.

### Incidents

| Incident Type | High Adoption | Low Adoption |
| :--- | :--- | :--- |
| Malware | 10% | 14% |
| Misconfiguration | 50% | 43% |
| Known unpatched vulnerabilities | 45% | 33% |
| Failed audit | 21% | 14% |
| Secret leaks by insider | 18% | 17% |
| Data leaks by insider | 18% | 7% |
| Haven’t experienced any security incidents | 14% | 21% |
| Prefer not to answer | 18% | 21% |

Snyk Report: State of Cloud Native Application Security | 04

### Nearly 60% have increased security concerns since adopting cloud native

Adoption of cloud native technologies will undoubtedly change the security posture of your overall application. While the core security principles remain constant, as with all emerging ecosystems the best practice is still being defined, driving fresh concern as teams navigate through unfamiliar landscapes. Our survey shows organizations are nearly 4x more likely to have increased rather than decreased concerns over their security posture since adopting cloud native.

- **Increased:** 58%
- **Hasn’t changed:** 20%
- **Decreased:** 15%
- **Don’t know:** 7%

Snyk Report: State of Cloud Native Application Security | 05

### Misconfiguration is the area of most concern when moving to cloud native

Cloud native platforms utilizing automated tooling will rely on credentials such as secrets and API tokens in order to operate, and necessitates a more decentralized approach to managing such access. The need for effective management of these kinds of artifacts is a key differentiator from the more centralized pre-cloud era, and a major area of concern for operations teams transforming their infrastructure. Our survey showed that misconfigurations were the biggest area of increased concern, with over half of respondents stating it’s a bigger problem for them since moving to a cloud native platform. Despite secret leaks and data leaks not showing up highly in the actual incidents data, they feature strongly as areas of increased worry particularly among high adopters of cloud native technologies.

### Areas of concern

| Area of Concern | High Adoption | Low Adoption |
| :--- | :--- | :--- |
| Malware | 34% | 23% |
| Known unpatched vulnerabilities | 45% | 44% |
| Data leaks by insider | 38% | 17% |
| Secret leaks | 45% | 35% |
| Insecure APIs | 50% | 53% |
| Misconfiguration | 52% | 57% |
| Impact of security on deployment velocity | 16% | 18% |
| Ability to handle/fix risks quickly | 22% | 30% |

Snyk Report: State of Cloud Native Application Security | 06

---

## Deployment Automation and Security Testing

### Highly automated pipelines are twice as likely to incorporate security testing throughout their development lifecycle

While building fully automated deployment pipelines can be challenging, once automation and processes are in place, they can create a virtuous cycle providing multiple integration points to enable further automation. This is a key enabler for security testing. Companies with high levels of deployment automation were more than twice as likely to have adopted security testing at all points throughout the software development lifecycle, when compared to organizations with no automation. While companies of all sizes showed a clear preference to test in CI and earlier, enterprises were more likely to also be testing during later deployment and production stages. Despite testing in local development environments, such as an IDE, being a developer driven task, more automated organizations were nearly twice as likely to see their development teams adopt security early on in their workflows.

Snyk Report: State of Cloud Native Application Security | 07

### When do you do security testing?

#### Entirely Automated vs Not Automated
- **Local development e.g. IDE’s and CLI tools:** 44% (Entirely Automated) / 22% (Not Automated)
- **Source Code repositories:** 44% / 40%
- **CI system:** 43% / 16%
- **Deployment time:** 45% / 7%
- **Production:** 28% / 6%

#### Enterprise vs Medium vs Small
- **Local development e.g. IDE’s and CLI tools:** 40% (Enterprise) / 34% (Medium) / 42% (Small)
- **Source Code repositories:** 39% / 45% / 50%
- **CI system:** 65% / 56% / 58%
- **Deployment time:** 36% / 37% / 22%
- **Production:** 25% / 19% / 15%

Snyk Report: State of Cloud Native Application Security | 08

### Continuous deployment empowers continuous testing

Once the use of security tooling is integrated throughout the software development lifecycle, this dramatically expands the possibilities for more regular security testing. Nearly 70% of respondents with high levels of deployment automation were able to test their security daily or more frequently. This was 17x more than respondents who had no deployment automation, and 60% of those only tested their security monthly or less frequently. This was 3x more than respondents who had full deployment automation.

Snyk Report: State of Cloud Native Application Security | 09

### How often do you do security testing?

- **Continuously or daily:** 64% (Entirely Automated) / 24% (Not Automated)
- **Weekly:** 43% / 14%
- **Monthly:** 36% / 41%
- **Less frequently:** 16% / 26%

#### Enterprise vs Medium vs Small
- **Continuously or daily:** 45% (Enterprise) / 43% (Medium) / 31% (Small)
- **Weekly:** 41% / 52% / 62%
- **Monthly:** 49% / 54% / 54%
- **Less frequently:** 86% / (data point) / (data point)

Snyk Report: State of Cloud Native Application Security | 10

---

## Vulnerability Remediation Speeds

### Over 72% of fully automated teams find and fix critical vulnerabilities in under 1 week

Testing faster leads to fixing faster. Over 72% of respondents with high levels of automation had an average time to fix vulnerabilities of less than one week, with 36% having an average of one day or less. Those with full automation were over 4x more likely to fix security issues in a day and over twice as likely to fix within a week. Automated testing is also a key enabler of visibility - you can’t fix what you can’t see. This was reinforced by the 28% of organizations with low levels of automation who responded that they didn’t know how long it takes them to fix issues.

### Time to fix critical security issues

#### Entirely Automated
- **1 day or less:** 36%
- **1 week:** 24%
- **2 weeks:** 20%
- **1 month:** 6%
- **Longer than 1 month:** 3%
- **Don't know:** 8%

#### Not Automated
- **1 day or less:** 8%
- **1 week:** 12%
- **2 weeks:** 10%
- **1 month:** 8%
- **Longer than 1 month:** 34%
- **Don't know:** 28%

Snyk Report: State of Cloud Native Application Security | 11

---

## Software Development Life Cycle Security Practices

### Automation empowers shift left security

Companies who automate are twice as likely to implement security testing. Adopting a broad and deep approach to security practices throughout the software development life cycle is key to a successful Cloud Native Application Security program. Our survey shows that companies with higher levels of cloud native automation have a greater adoption of security testing techniques. They tend to focus more on Static Application Security Testing (SAST), scanning for vulnerabilities in application dependencies with Software Composition Analysis (SCA), container image testing, and scanning infrastructure as code which are all techniques which fit well into the paradigm of automation. Organizations with fully automated deployment pipelines are twice as likely to adopt SAST and SCA tooling into their SDLC, and almost 3x as likely to add Dynamic Application Security Testing (DAST), although in general, dynamic testing isn’t as well adopted when compared with static testing. Policy compliance testing is still an emerging field, with only 23% of respondents having adopted it.

### Enterprises are more likely to adopt security practices, yet smaller companies with less established security practices are keeping up

Larger companies and enterprises are, of course, more likely to have the resources to run dedicated security teams so it shouldn’t come as a surprise to see enterprises having the support to adopt formal Cloud Native Application Security Practices. While in smaller organizations the security function may be wholly owned by another org, such as the engineering teams, our survey shows that they are still able to keep up, particularly in the static testing space with over half of small organizations adopting SAST, SCA and container image scanning.

Snyk Report: State of Cloud Native Application Security | 12

### Which software development life cycle security practices are you following?

- **Static code analysis (SAST)**
- **Code scanning for package dependency vulnerabilities (SCA)**
- **Dynamic Application Security Testing (DAST)**
- **Interactive Application Security Testing (IAST)**
- **Scanning infrastructure as code (Terraform, Kubernetes)**
- **Container image scanning tools**
- **Policy compliance (Open Policy Agent/Gatekeeper)**

Snyk Report: State of Cloud Native Application Security | 13

---

## DevSecOps and Security Ownership

### Security isn't just for the security team

Developers are adding security to their stack of hats. The move towards the concept of DevSecOps has accelerated in conjunction with adoption of cloud native technologies, as security shifts left in the software development lifecycle. Developers now have a pivotal role in ensuring that cloud native applications and infrastructure are secure since they increasingly contribute to the application, the infrastructure code, and workload deployment technologies. 

With this in mind, perception of security ownership provided interesting results in our survey set. While less than 10% of respondents in security roles believed developers were responsible for the security of their cloud native environment and applications, over 36% of developers stated that they were responsible. Traditionally, in a more siloed organization, the ownership of security would have sat firmly with the security team. Respondents in security roles are almost 3x more likely to attribute security ownership to the IT security team than respondents in development teams are. These indicators suggest that this ownership is being accepted by the development teams faster than the security teams are willing to let go of it. Security teams are still adjusting to the shifting responsibilities which transitioning to cloud native brings, and development teams are increasingly aware of their growing role in Cloud Native Application Security.

Snyk Report: State of Cloud Native Application Security | 14

### Who is primarily responsible for the security of your cloud native environment and applications?

#### Developer response
- **Application security team:** 14%
- **DevOps / DevSecOps:** 33%
- **Developers:** 37%
- **No-one:** 2%
- **IT security team:** 13%

#### Security response
- **Application security team:** 23%
- **DevOps / DevSecOps:** 31%
- **Developers:** 10%
- **No-one:** 3%
- **IT security team:** 31%

Snyk Report: State of Cloud Native Application Security | 15

### Developers and security both understand the importance of Cloud Native Application Security

The increased awareness of security in development teams was also reinforced by the survey results around security exposure concerns. Both developers and security professionals alike shared that switching to cloud native technologies had increased their security concerns. Developers were just as likely to be invested in good security outcomes as the security team - good news for the adoption of DevSecOps principles which relies on shared security goals across the organization.

### Has switching to Cloud Native technologies increased or decreased your security exposure concerns?

#### Developer response
- **Increased:** 58%
- **Decreased:** 13%
- **Hasn’t changed:** 21%

#### Security response
- **Increased:** 61%
- **Decreased:** 13%
- **Hasn’t changed:** 18%

> ![Learn how Twilio’s Head of Product Security scaled through dev-first security and devsecops in a cloud native environment](Watch Now)

Snyk Report: State of Cloud Native Application Security | 16

> "Snyk’s CNAS report shows clear movement in a positive direction. 99% of respondents recognize that security is important to their business strategy. That’s a world I want to live in."

### Curious how Snyk can help?
Snyk is a developer-first platform for building software securely. Learn more about how Snyk can help you secure cloud native applications across your IDEs, repos, containers, and pipelines.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-16", "model": "gemini-3.5-flash-lite"} -->
