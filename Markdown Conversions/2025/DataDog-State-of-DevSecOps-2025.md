# STATE OF DevSecOps 2025

## Table of Contents
- [Fact 1: Exploitable vulnerabilities are prevalent in web applications, particularly those that use Java](#fact-1)
- [Fact 2: Attackers continue to target the software supply chain](#fact-2)
- [Fact 3: Usage of long-lived credentials in CI/CD pipelines is still too high, but slowly decreasing](#fact-3)
- [Fact 4: Only a fraction of critical vulnerabilities are truly worth prioritizing](#fact-4)
- [Fact 5: Keeping libraries up to date is a major challenge for developers](#fact-5)
- [Fact 6: Minimal container images improve security posture](#fact-6)
- [Fact 7: In AWS, infrastructure-as-code usage is high, but many teams still use ClickOps as well](#fact-7)
- [Key learnings from the 2025 State of DevSecOps study](#key-learnings)
- [Methodology](#methodology)
- [Licensing](#licensing)

The practice of DevSecOps emphasizes the need to identify and respond to security risks at each point in the software development life cycle (SDLC), and has increasingly become the standard in the tech industry. In order to assess the types of risks defenders need to be aware of and what practices they can adopt to improve their security posture, we analyzed tens of thousands of applications and container images within thousands of cloud environments.

Our findings show that web applications face a wide range of risks, including known-exploitable vulnerabilities, supply chain attacks, and insecure identity configurations in CI/CD. However, applying context about the application in question, including what languages it uses and what environment it runs in, can reduce noise and help defenders prioritize risks. In addition, operational best practices like opting for smaller container images, utilizing infrastructure as code (IaC), and frequently deploying services tend to reduce applications’ risk exposure and provide a strong foundation for a secure SDLC.

<a id="fact-1"></a>
## FACT 1: Exploitable vulnerabilities are prevalent in web applications, particularly those that use Java

By analyzing our dataset of applications, we found that 15 percent of services are vulnerable to known-exploited vulnerabilities, affecting 30 percent of organizations. Vulnerabilities are particularly prevalent among Java services, 44 percent of which contain a known-exploited vulnerability. The next highest is Go at 5 percent, with the average for all non-Java services at 2 percent.

In fact, 14 percent of Java services still contain at least one vulnerability even when we look at only those that are known to be highly impactful, such as known remote code exploitation (RCE) vulnerabilities like Log4Shell, Spring4Shell, and other routinely exploited attack paths.

In addition to being more likely to contain high-impact vulnerabilities, Java applications are also patched more slowly than those from other programming ecosystems. We found that applications from the Java-based Apache Maven ecosystem had a median time to fix library vulnerabilities of 62 days, compared to 46 days for those in the .NET-based NuGet ecosystem and 19 days for applications built using npm packages, which are JavaScript-based.

Leaving known vulnerabilities unpatched for prolonged periods is particularly risky because web applications are often exposed to the internet. Attackers use automated scanners to continuously scan the internet for high-impact, easy-to-exploit vulnerabilities, and recent research shows that vulnerabilities are often exploited just hours after they are initially disclosed.

Our research confirms this pattern of attacker behavior. We found that 88 percent of organizations received untargeted malicious HTTP requests, such as to /backup.sql, scanning for potentially exposed sensitive files or API routes. In addition, 65 percent of cases where a specific attacker attempted to exploit a specific URL were untargeted—i.e., the same attacker had tried to exploit the same URL in at least one other organization that Datadog monitors.

<a id="fact-2"></a>
## FACT 2: Attackers continue to target the software supply chain

In addition to searching web applications for known vulnerabilities, attackers also commonly attempt to trick developers into downloading and deploying malicious packages from open source libraries. Throughout 2024, Datadog identified thousands of malicious PyPI and npm libraries in the wild. Some of these packages were malicious by nature and attempted to mimic a legitimate package (for instance, passports-js mimicking the legitimate passport library), a technique known as typosquatting. Others were active takeovers of popular, legitimate dependencies (such as Ultralytics, Solana web3.js, and lottie-player). These techniques are used both by state-sponsored actors and basic cybercriminals.

Attackers exploit the fact that vetting third-party dependencies is challenging for developers, especially if the package’s metadata and functionality appear to be legitimate.

<a id="fact-3"></a>
## FACT 3: Usage of long-lived credentials in CI/CD pipelines is still too high, but slowly decreasing

In addition to vulnerable code and malicious open source packages, the use of long-lived credentials that don’t expire is a common cause for cloud data breaches, and the practice is now widely frowned upon. Using long-lived credentials in CI/CD pipelines can be particularly risky, because their permissions are often highly privileged.

One scenario where long-lived credentials often make their way into CI/CD is when organizations use GitHub Actions to deploy applications to AWS, as these Actions can be configured with either short-lived credentials through OpenID Connect (OIDC) or AWS IAM user credentials, a type of long-term access key. We found that 37 percent of customers who send CloudTrail logs to Datadog are using IAM users in their GitHub Actions. We strongly recommend not relying on IAM users in this scenario but instead using OIDC.

While 63 percent of organizations using AWS and GitHub Actions leverage OIDC (up from 58 percent in 2024), 58 percent of organizations also leverage long-lived credentials from IAM users (down from 63 percent in 2024).

<a id="fact-4"></a>
## FACT 4: Only a fraction of critical vulnerabilities are truly worth prioritizing

The high prevalence of library vulnerabilities, malicious open source packages, identity misconfigurations, and other issues creates a noisy environment for defenders. In this context, security teams need to understand how to prioritize issues and determine which to remediate first. These teams often make decisions based on the severity of a vulnerability—typically measured by its CVSS base score, which is published along with the metadata for a known vulnerability. Vulnerabilities considered high-severity by CVSS score are only increasing: We found that the average service has 13.5 vulnerabilities with a high or critical CVSS severity score, up from 11.9 in 2024.

However, in order to truly gauge a vulnerability’s severity, it’s essential to have the appropriate runtime context—for example, whether the vulnerability is running in a production environment, or if the application in which the vulnerability is found is exposed to the internet. CVSS does not take these factors into account, which leads to excessive noise for defenders.

To reduce this noise, we developed a prioritization algorithm that factors in runtime context. After applying this algorithm, we found the average number of high or critical vulnerabilities per application drops from 12.2 to 7.5.

> “Without context, severity is just noise. True security comes not from patching everything, but from knowing what actually matters.”
> — Jean Burellier, Principal Software Engineer at Sanofi

<a id="fact-5"></a>
## FACT 5: Keeping libraries up to date is a major challenge for developers

In our research, we found that the median dependency is 215 days behind its latest major version. This reinforces the idea that engineers across DevSecOps functions are stretched and need to reduce noise, as teams struggle to keep library dependencies in their code up to date. Out-of-date libraries can increase the likelihood that a dependency contains unpatched, exploitable vulnerabilities.

Among all services, those that are less frequently deployed are more likely to be using out-of-date libraries. We found that dependencies in services that are deployed less than once per month are 47 percent more outdated than those deployed daily, with a median of 217 days versus 148 days behind their latest version update.

<a id="fact-6"></a>
## FACT 6: Minimal container images improve security posture

In recent years, engineering teams have moved toward adopting minimal container images in order to improve the efficiency and cost-effectiveness of their systems. This trend began with minimal distributions such as Alpine Linux and has evolved into even smaller distroless and from-scratch images, all of which drastically reduce the size of a container image.

This “less is more” approach has benefits for security as well. By analyzing thousands of container images, we found that on average, an image of less than 100 MB has three severe—i.e., with a high or critical CVSS score—vulnerabilities (median 0), while a container image of greater than 500 MB has on average 20 such vulnerabilities (median 7).

<a id="fact-7"></a>
## FACT 7: In AWS, infrastructure-as-code usage is high, but many teams still use ClickOps as well

Infrastructure as code (IaC) has become the dominant practice in cloud environments because it tends to lead to better operational outcomes, such as improved version control and traceability. In addition, IaC is a key component of security best practices, as it helps enforce peer review and makes infrastructure easier to scan for misconfigurations.

IaC adoption continues to grow more widespread. In AWS, 59 percent of organizations are using Terraform, and 57 percent use CloudFormation (slightly up from 2024). In all, 80 percent of organizations use at least one IaC tool. At the same time, we also identified that at least 38 percent of organizations perform ClickOps deployments in production.

<a id="key-learnings"></a>
## Key learnings from the 2025 State of DevSecOps study

In this section, we outline several best practices that organizations should implement based on these findings, including to:
- Prioritize vulnerabilities with runtime context
- Deploy guardrails within your software supply chain
- Deploy frequently to stay current on patches
- Adopt minimal container images
- Expand IaC usage and rein in ClickOps

### Prioritize vulnerabilities with runtime context
Most security teams have a finite set of resources they can leverage to remediate security vulnerabilities. By mapping environmental information about your cloud assets to the vulnerabilities associated with each resource, you can use runtime context to effectively prioritize the vulnerabilities that are the most likely to get exploited. Key characteristics to consider include:
- Public accessibility
- Environment
- Active attack status
- Highly privileged identity
- Known exploit proof of concept

### Deploy guardrails within your software supply chain
Mitigating supply chain risk requires a multi-pronged approach. You can take actions to prevent or detect the execution of malicious packages within your trusted environments, and you can also protect software repositories to harden your ecosystem against attacks.

### Secure your pipeline by eliminating long-lived credentials
Leaks of long-lived cloud credentials are one of the most common causes for cloud breaches. It’s critical to use short-lived cloud credentials through OpenID Connect (OIDC) or a similar protocol to authenticate both workloads and human users to cloud resources.

### Deploy frequently to stay current on patches
Services that are deployed more frequently contain fewer out-of-date dependencies. Simply executing CI tasks that update dependencies, build, and test your software on a regular cadence can significantly improve the security of your services without much manual effort.

### Adopt minimal container images
When building applications, it’s important to attempt to build small, minimal container images: They are faster to deploy, remove complexity, and drastically reduce the number of OS-level vulnerabilities.

### Expand IaC usage and rein in ClickOps
The first step toward implementing Zero Touch (or “low-touch”) production environments is to automate the deployment process, typically using IaC technologies. Once automation is in place, operators typically need only minimal permissions to the production environment.

<a id="methodology"></a>
## Methodology

### Fact 1
We analyzed vulnerabilities in third-party libraries of applications across various languages and runtimes. We sourced known exploited vulnerabilities from the CISA KEV catalog, extracted on April 9, 2025.

### Fact 2
We relied on the research and efforts of Datadog’s security research team using tools like GuardDog to identify and classify malicious packages.

### Fact 3
To identify organizations that use GitHub Actions with OIDC or IAM users, we queried AWS CloudTrail logs for specific event names and identity providers.

### Fact 4
We analyzed vulnerabilities in third-party libraries and computed adjusted CVSSv3 metrics based on runtime context (production environment, public exposure, EPSS scores, and exploit availability).

### Fact 5
We collected data on libraries active in March 2025, calculating the number of days since the latest update to the current major version.

### Fact 6
We analyzed data from containers scanned through Datadog Cloud Security’s Vulnerability Management feature, reviewing identified OS-level vulnerabilities.

### Fact 7
We analyzed AWS CloudTrail Logs to determine IaC technology usage based on HTTP user agents and identified manual ClickOps deployments.

<a id="licensing"></a>
## Licensing
Report: CC BY-ND 4.0
Images: CC BY-ND 4.0