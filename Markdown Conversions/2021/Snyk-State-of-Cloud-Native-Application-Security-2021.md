# State of Cloud Native Application Security

## Table of Contents
- [Executive Summary: Security in the Cloud Native Era](#executive-summary-security-in-the-cloud-native-era)
- [Cloud Native Adoption Trends](#cloud-native-adoption-trends)
- [The State of Deployment Automation](#the-state-of-deployment-automation)
- [Security Incidents in Production](#security-incidents-in-production)
- [Security Concerns and Challenges](#security-concerns-and-challenges)
- [Deployment Automation and Security Testing](#deployment-automation-and-security-testing)
- [Continuous Testing and Remediation](#continuous-testing-and-remediation)
- [Shift Left Security Practices](#shift-left-security-practices)
- [Security Ownership and DevSecOps](#security-ownership-and-devsecops)

---

## Executive Summary: Security in the Cloud Native Era

99% of companies recognize security as important to their cloud native strategy.

Success in the cloud native era is defined by an organization's ability to deliver new versions of software faster and more efficiently. Being able to deploy code to production faster and more easily manage those applications were the primary reasons for moving towards containerized infrastructure. However, as companies embrace cloud native technologies as part of their digital transformation, security is seen as a key factor to building successful platforms. While only 36% of respondents stated that security was one of the main reasons for moving their production applications into containers, 99% of respondents recognized security as an important element in their cloud native strategy. In addition, over 80% stated security is very important to them.

![Chart showing reasons for moving to containers: Deployment velocity (68%), Ease of management (67%), Reduce costs (43%), Improved security (36%), Attracting talent (11%). Chart showing importance of security: Very important (83%), Somewhat important (16%), Not important (1%).]

## Cloud Native Adoption Trends

Over 78% of production workloads are deployed as containers or serverless applications.

Containers continue to be the dominant mechanism for cloud native application deployment, with nearly 60% of production workloads deployed in containers. Penetration of serverless technologies is now significant across all company sizes, and makes up more than a fifth (mean average) of all production workloads. Usage of cloud native technologies is strong across all company sizes, indicating that adoption is becoming mainstream. With over 50% of respondent’s workloads also being deployed with some form of Infrastructure As Code (IaC), use of software-driven infrastructure has increased alongside the container and serverless growth trends.

![Chart showing adoption rates: Containers (58%), Serverless (21%), IaC (51%).]

## The State of Deployment Automation

While 95% of respondents use automation, only 33% fully automate their deployment pipeline.

Deployment automation is one of the key tenets of cloud native practices, enabling development velocity. Our survey showed that over 95% of respondents were using some level of automation with almost a third having an entirely automated deployment pipeline. Organizations that show high levels of cloud native adoption are over twice as likely to have an entirely automated deployment process than organizations with low cloud native adoption.

![Chart comparing manual vs automated deployments for high vs low adoption organizations.]

## Security Incidents in Production

Misconfiguration and known unpatched vulnerabilities were responsible for the greatest number of security incidents in cloud native environments.

The top two incident types by a distance were misconfiguration and known unpatched vulnerabilities, at 45% and 38% respectively. Over 56% experienced a misconfiguration or known unpatched vulnerability incident involving their cloud native applications. Data leaks by insiders were more than twice as likely to have occurred in organizations with high levels of cloud native adoption, reinforcing that adopting zero trust principles becomes increasingly important in fully automated cloud-based environments.

![Chart showing incident types: Malware, Misconfiguration, Known unpatched vulnerabilities, Failed audit, Secret leaks, Data leaks by insider.]

## Security Concerns and Challenges

Nearly 60% have increased security concerns since adopting cloud native.

Adoption of cloud native technologies will undoubtedly change the security posture of your overall application. While the core security principles remain constant, as with all emerging ecosystems the best practice is still being defined, driving fresh concern as teams navigate through unfamiliar landscapes. Our survey shows organizations are nearly 4x more likely to have increased rather than decreased concerns over their security posture since adopting cloud native.

![Chart showing security concern levels: Increased (58%), Hasn't changed (20%), Decreased (15%), Don't know (7%).]

Misconfiguration is the area of most concern when moving to cloud native. Cloud native platforms utilizing automated tooling will rely on credentials such as secrets and API tokens in order to operate, and necessitates a more decentralized approach to managing such access.

## Deployment Automation and Security Testing

Highly automated pipelines are twice as likely to incorporate security testing throughout their development lifecycle.

Companies with high levels of deployment automation were more than twice as likely to have adopted security testing at all points throughout the software development lifecycle, when compared to organizations with no automation. While companies of all sizes showed a clear preference to test in CI and earlier, enterprises were more likely to also be testing during later deployment and production stages.

## Continuous Testing and Remediation

Once the use of security tooling is integrated throughout the software development lifecycle, this dramatically expands the possibilities for more regular security testing. Nearly 70% of respondents with high levels of deployment automation were able to test their security daily or more frequently.

Over 72% of fully automated teams find and fix critical vulnerabilities in under 1 week. Testing faster leads to fixing faster. Those with full automation were over 4x more likely to fix security issues in a day and over twice as likely to fix within a week.

## Shift Left Security Practices

Companies who automate are twice as likely to implement security testing.

Organizations with fully automated deployment pipelines are twice as likely to adopt SAST and SCA tooling into their SDLC, and almost 3x as likely to add Dynamic Application Security Testing (DAST). Policy compliance testing is still an emerging field, with only 23% of respondents having adopted it.

## Security Ownership and DevSecOps

Developers are adding security to their stack of hats.

The move towards the concept of DevSecOps has accelerated in conjunction with adoption of cloud native technologies. While less than 10% of respondents in security roles believed developers were responsible for the security of their cloud native environment and applications, over 36% of developers stated that they were responsible. These indicators suggest that this ownership is being accepted by the development teams faster than the security teams are willing to let go of it.

![Chart showing responsibility breakdown for Developers vs Security professionals.]

---

_Snyk is a developer-first platform for building software securely. Learn more about how Snyk can help you secure cloud native applications across your IDEs, repos, containers, and pipelines._