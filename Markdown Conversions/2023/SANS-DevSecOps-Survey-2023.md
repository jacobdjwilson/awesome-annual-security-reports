# SANS 2023 DevSecOps Survey

## Table of Contents
- [Executive Summary](#executive-summary)
- [A Snapshot of the Respondents](#a-snapshot-of-the-respondents)
- [Understanding the DevSecOps Environment](#understanding-the-devsecops-environment)
- [Application Hosting in the Cloud](#application-hosting-in-the-cloud)
- [Securing Multicloud Environments](#securing-multicloud-environments)
- [Security at Velocity](#security-at-velocity)
- [Automated Compliance](#automated-compliance)
- [Securing Container Services](#securing-container-services)
- [Programming Environments and Risks](#programming-environments-and-risks)
- [DevOps Foundational Practices](#devops-foundational-practices)
- [Security Testing](#security-testing)
- [Key Performance Indicators and Metrics](#key-performance-indicators-and-metrics)
- [Top DevSecOps Challenges and Success Factors](#top-devsecops-challenges-and-success-factors)
- [Future Trends](#future-trends)
- [Going Forward](#going-forward)

---

## Executive Summary

DevSecOps represents the intersection of software development (Dev), security (Sec), and operations (Ops) with the fundamental objective of automating, monitoring, and integrating security throughout all phases of the software development life cycle (SDLC): plan, develop, build, test, release, deliver, deploy, operate, and monitor. Ultimately, DevSecOps is fundamentally concerned with enabling agility, which inevitably brings with it the challenges that come with sharing the responsibility for security best practices with other stakeholders across the entire continuous integration/continuous deployment (CI/CD) pipeline. Achieving this shared-responsibility ideal requires the development of trusted relationships among development, security, and operations teams.

The 2023 DevSecOps Survey—the 10th in an annual series—considers a broad range of indicators of maturity in these areas and evaluates them against a retrospective view of previous years’ survey responses, with the goal of helping security practitioners understand:

*   How organizations use cloud platforms, architectures, and development ecosystems to identify security requirements, risks, and opportunities.
*   How organizations deploy appropriate security within the CI/CD pipeline, injecting security best practices while keeping up with the delivery of products and features to stakeholders.
*   What security tools and best practices organizations leverage to maintain a “shift-left” mentality—to keep security in mind continuously throughout the development process.
*   What skills are needed to empower organizations to architect secure applications and cloud services and help them find and fix vulnerabilities as early as possible.
*   What are the future trends and adoption rates of new technology, such as artificial intelligence (AI), data science, and GitOps—and how they might impact the future of DevSecOps.

### Key Findings

*   The trend toward organizations leveraging multiple cloud hosting providers continues, as indicated by the respondents using Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP) to run more than 75% of their application workloads. Forty-seven percent of the respondents said they use other cloud hosting providers, including Alibaba Cloud, IBM Cloud, and Oracle Cloud—a dramatic increase from just 25% last year.
*   A key DevSecOps challenge remains the difficulty of acquiring the necessary funding to purchase newly available security and testing tools.
*   The key success factors the survey respondents identified show the importance organizations continue to place on communications within the organization and creating “security champions” through professional development activities.
*   Cloud-hosted virtual machines (VMs) are still preferred over containers and serverless functions, with 69% of respondents reporting at least 25% of their applications running on VMs.
*   Another interesting trend this year is that DevSecOps is now clearly seen as a business-critical issue and a risk management concern. Forty percent of the respondents were aligned with the business side, and 13% of respondents identified themselves as business managers.
*   The dominant industries represented by the respondents aligned with the technology, cybersecurity, and application development verticals. Representation from the banking and finance industry shows a significant decline (down from 17% in 2022 to 7% in 2023), and several key industries—notably government and healthcare—appear to be underrepresented, as they have been in past years.
*   One of the notable forward-looking trends shown by the 2023 survey—reflecting industrywide trends—is a significant increase (16%) in respondents reporting that they were investigating and experimenting with the use of AI or data science to improve DevSecOps, up from 33% in 2022 to 49% in 2023.

## A Snapshot of the Respondents

The 363 respondents to this year’s survey represent a highly diverse set of roles, industries, and organizational sizes (see Figure 1). Unsurprisingly, they show a strong bias toward security, with 34% of respondents performing a direct security function of some kind. Security administrator/security analyst is by far the most common role, at 10.2%. Development roles—including application developer, cloud architect, software engineer, and DevOps engineer—are, of course, also well represented, at 21%. But the single most represented role in the survey is business manager, at 13% of the respondents, clearly showing that DevSecOps is now broadly recognized as a business concern, not solely a technical issue. Management and executive roles, including the business manager role, comprise 40% of the respondents (including security and compliance managers, quality analysis [QA] release managers, CxOs, and IT managers/directors).

### Top 4 Industries Represented
*   Technology
*   Cybersecurity
*   Application development
*   Manufacturing

### Organizational Size
*   Small (Up to 1,000)
*   Small/Medium (1,001–5,000)
*   Medium (5,001–15,000)
*   Medium/Large (15,001–50,000)
*   Large (More than 50,000)

![Image description: A diagram showing organizational size distribution with icons representing buildings for larger organizations and gears for smaller organizations.]

### Operations and Headquarters
*   Ops: 101, HQ: 23
*   Ops: 280, HQ: 13
*   Ops: 91, HQ: 19
*   Ops: 304, HQ: 270
*   Ops: 65, HQ: 10
*   Ops: 46, HQ: 10
*   Ops: 46, HQ: 17
*   Ops: 32, HQ: 1

### Top 4 Roles Represented
*   Business manager
*   Security administrator/security analyst
*   Application developer
*   Security architect

![Image description: A diagram showing the top roles represented in the survey, with icons representing people, each representing 5 respondents.]

Figure 1. Demographics of Survey Respondents

More than half the respondents (53%) are from the top 5 industries. Small organizations—defined as those with 1,000 or fewer full-time and contract employees—dominate the survey, with a total of 61% of the respondents. Larger organizations are distributed relatively evenly across the other organizational-size categories. Additionally, this may also suggest that organizations are outsourcing their development resources.

The United States is disproportionately represented in terms of geography, with 74% of respondents’ primary corporate headquarters located there and 84% of operations maintained there. Canada and Europe followed at a far-distant second and third, at 6% and 5% of corporate headquarters and 28% and 25% of operations, respectively.

## Understanding the DevSecOps Environment

This year’s survey, like the previous years’, shows adoption and use of cloud computing as an IT delivery model continuing to accelerate dramatically. This year, for example, only 54% of respondents reported that their organizations run 25% or more of their applications on-premises, down from 65% in 2022 and 85% in 2021—a 31% drop in just three years (see Figure 2). Moreover, fewer than 5% of respondents indicated that they ran all their applications on-premises, while almost 7% said they have no on-premises applications at all, and more than 84% of the survey respondents reported at least some degree of cloud usage.

### What percentage of your applications are running in the following methods?

*   **On-premises:**
    *   0%: 7.4%
    *   1–24%: 29.9%
    *   25–49%: 17.9%
    *   50–74%: 14.8%
    *   75–99%: 7.4%
    *   100%: 3.1%
*   **Cloud-hosted virtual machine:**
    *   0%: 5.7%
    *   1–24%: 16.8%
    *   25–49%: 22.8%
    *   50–74%: 16.5%
    *   75–99%: 25.1%
    *   100%: 4.0%
*   **Cloud-hosted container service:**
    *   0%: 7.7%
    *   1–24%: 14.5%
    *   25–49%: 14.2%
    *   50–74%: 14.8%
    *   75–99%: 10.5%
    *   100%: 2.8%
*   **Cloud-hosted functions-as-a-service (FaaS) (serverless):**
    *   0%: 6.8%
    *   1–24%: 14.0%
    *   25–49%: 14.8%
    *   50–74%: 13.4%
    *   75–99%: 5.1%
    *   100%: 2.0%
*   **Other:**
    *   0%: 4.6%
    *   1–24%: 14.2%
    *   25–49%: 16.8%
    *   50–74%: 16.5%
    *   75–99%: 11.8%
    *   100%: 2.8%

![Image description: A bar chart showing the percentage of applications running in different methods (on-premises, cloud-hosted VM, cloud-hosted container, cloud-hosted FaaS, other) across various percentage ranges (0% to 100%).]

Figure 2. Most Commonly Used Platforms for Applications

These results clearly show that the shift to the cloud is ongoing (and almost certain to continue). But the survey results also offer an important reminder that not all applications are based in the cloud. Overall, a still very substantial 29% of the respondents reported that 50% or more of their applications remain on-premises.

A closer look at the cloud responses shows that, as in previous years, cloud-hosted VMs are still preferred over cloud-hosted container services or cloud-hosted functions-as-a-service (FaaS, also called serverless computing)—but also that most organizations’ cloud implementations remain highly diverse. In this year’s survey, although 69% of the respondents said that at least 25% of their applications run on VMs, 59% use cloud-hosted container services for the same percentage of their applications and 57% use FaaS.

This mix of VMs, containers, and FaaS has important security implications, because all three of these technologies must be properly secured. That means DevSecOps teams must have the skills and tooling to secure all three approaches—which, despite considerable overlap, are all distinctly different. A further consideration is that an enterprise using the cloud can likely delegate some mundane security tasks to its cloud service provider—freeing up its own personnel for more important higher-level duties—but this is not the case with on-premises applications. This suggests that organizations using the cloud should look to providers that are prepared to take on more security management responsibilities.

> **TAKEAWAY**
> DevSecOps teams need to invest in tools that make it possible to secure their workloads effectively, wherever they run. Software composition analysis (SCA), static application security testing (SAST), dynamic application security testing (DAST), and threat modeling tools, for example, can all be used to improve the security of long-lived VMs and short-lived containers or functions. When selecting tools, security practitioners must recognize that different runtime environments need different tools and must consider whether cloud providers—both current and prospective—have tools integrated into their ecosystems that could potentially streamline security workflows.

## Application Hosting in the Cloud

The survey results clearly show that most organizations using the cloud are engaging with multiple cloud service providers and that the distribution of applications running on each of the three most important cloud service providers is beginning to even out.

For the more than 84% of respondents who reported using the cloud:

*   90% have applications running on Amazon Web Services (AWS).
*   84% have applications running on Microsoft Azure.
*   74% have applications running on Google Cloud Platform (GCP).

Moreover, 47% said they use other cloud hosting providers, including Alibaba Cloud, IBM Cloud, and Oracle Cloud—a dramatic increase from just 25% last year.

Another important finding is the clear trend away from using a single cloud hosting provider to run the majority of an organization’s workloads. Table 1 shows the percentage of respondents to the 2021, 2022, and 2023 surveys who reported using AWS, Azure, or GCP to run 75% or more of their applications. Figure 3 details the complete distribution of the 2023 survey responses.

### Table 1. Respondents Concentrating 75% or More of Workloads on a Single CSP, 2021–2023

| CSP     | 2023    | 2022    | 2021    |
| :------ | :------ | :------ | :------ |
| AWS     | 17.3%   | 21.6%   | 27.1%   |
| Azure   | 11.2%   | 14.8%   | 18.4%   |
| GCP     | 9.8%    | 5.9%    | 7.2%    |

### What percentage of your cloud-based applications are hosted by:

*   **Amazon Web Services (AWS):**
    *   0%: 8.6%
    *   1–24%: 16.7%
    *   25–49%: 19.0%
    *   50–74%: 21.6%
    *   75–99%: 14.7%
    *   100%: 1.2%
*   **Microsoft Azure:**
    *   0%: 8.1%
    *   1–24%: 14.4%
    *   25–49%: 17.9%
    *   50–74%: 22.2%
    *   75–99%: 15.0%
    *   100%: 0.6%
*   **Google Cloud Platform (GCP):**
    *   0%: 4.3%
    *   1–24%: 14.4%
    *   25–49%: 15.0%
    *   50–74%: 11.8%
    *   75–99%: 6.9%
    *   100%: 2.0%
*   **Other:**
    *   0%: 7.2%
    *   1–24%: 14.8%
    *   25–49%: 16.5%
    *   50–74%: 14.4%
    *   75–99%: 8.6%
    *   100%: 3.1%

![Image description: A stacked bar chart showing the distribution of cloud-based application hosting by provider (AWS, Azure, GCP, Other) across various percentage ranges (0% to 100%).]

Figure 3. Extent of Cloud-Based Application Hosting

There are many reasons, including the need for business continuity planning and the desire for negotiation leverage, that an organization may choose to distribute its workloads across multiple cloud service providers. The benefits of using multiple cloud service providers are obvious, but so are their security implications: Each provider’s environment must be properly secured, but every environment works differently and presents different security challenges. And the work involved increases exponentially with each additional provider used.

One way leading DevSecOps teams are coping with the multicloud challenge is by creating platform-agnostic applications, typically using containerization, so that the application can run in any cloud service provider’s container service, or even on-premises, with the necessary infrastructure in place.

## Securing Multicloud Environments

The increasing reliance on multiple cloud service providers, with a mix of VMs, containers, and FaaS, also sharply increases the challenges of ensuring that all those cloud resources are properly secured. To evaluate this challenge, the 2023 DevSecOps survey considered similar results from identical questions asked in the 2022 and 2023 surveys regarding two of the most important sets of cloud security tools:

*   To what extent has your organization adopted cloud security posture management (CSPM) software, either commercial or open source? (See Figure 4 for years 2022/2023.)
*   To what extent has your organization adopted cloud workload protection platform (CWPP) software? (See Figure 5 for years 2022/2023.)

The survey results from these two years show that even though CSPM is widely deployed, it is still highly underutilized. Most respondents said they are using either a commercial or an open source CSPM tool, but fewer than 16% overall (2023) and 21% overall (2022) said they use those solutions for 75% or more of their AWS accounts, Azure subscriptions, or GCP projects.

### To what extent has your organization adopted cloud security posture management (CSPM) software, (either commercial or open source)?

*   **AWS:**
    *   Total: 82.7% (2023), 81.0% (2022)
    *   Greater than 75%: 13.5% (2023), 15.8% (2022)
*   **Azure:**
    *   Total: 69.9% (2023), 64.7% (2022)
    *   Greater than 75%: 10.9% (2023), 17.9% (2022)
*   **GCP:**
    *   Total: 51.6% (2023), 63.5% (2022)
    *   Greater than 75%: 20.5% (2023), 14.0% (2022)

![Image description: A bar chart comparing CSPM adoption for AWS, Azure, and GCP in 2022 and 2023, showing total adoption and adoption for greater than 75% of accounts/subscriptions/projects.]

Figure 4. Extent of CSPM Adoption

### To what extent has your organization adopted cloud workload protection platform software (CWPP) (either commercial or open source)?

*   **AWS:**
    *   Total: 82.4% (2023), 76.5% (2022)
    *   Greater than 75%: 3.6% (2023), 13.2% (2022)
*   **Azure:**
    *   Total: 70.3% (2023), 51.6% (2022)
    *   Greater than 75%: 10.9% (2023), 16.6% (2022)
*   **GCP:**
    *   Total: 58.1% (2023), 41.6% (2022)
    *   Greater than 75%: 14.4% (2023), 16.6% (2022)

![Image description: A bar chart comparing CWPP adoption for AWS, Azure, and GCP in 2022 and 2023, showing total adoption and adoption for greater than 75% of accounts/subscriptions/projects.]

Figure 5. Extent of CWPP Adoption

This decline from the previous year could have several causes. One cause might be that the increase in the use of these tools has made organizations more aware of their cloud provider inventories and the weaknesses in their protections. Another cause might be that vendor pricing is driving organizations to make difficult choices between inadequate protection and unacceptable cost.

CWPP products are also very much underutilized. Although a majority of the respondents (greater than 70% across all platforms) said their organizations use CWPP, a much smaller percentage (less than 15% overall in 2023, down slightly from 17% in 2022) use it in at least 75% or more of their AWS accounts, Azure subscriptions, or GCP projects.

Both findings suggest that DevSecOps teams are missing a valuable opportunity to enhance the security of their cloud environments. CSPM software can help DevSecOps teams ensure that the cloud environments that host their applications are properly configured and secured using industry best practices, but only if this software is used consistently across all cloud accounts. Similarly, CWPPs provide various security services for workloads, regardless of whether the work is performed by VMs, containers, or serverless computing. In the past, this would typically have required the installation of multiple agents, resulting in a drain on VM resources, but CWPP solutions have evolved to overcome that problem.

> **TAKEAWAY**
> Both CSPM and CWPP are essential capabilities for organizations operating in multicloud environments. As an organization moves further away from reliance on a single cloud hosting provider, the work of securing each cloud environment increases exponentially. Organizations should consider using or increasing their adoption of commercial or open source CSPM software to ensure that each cloud environment is securely configured, and they should implement CWPPs to protect application workloads at execution time.

## Security at Velocity

The survey results clearly show that delivery velocity—the speed at which changes are made to applications in development—is remarkably stable. When asked how often their organizations deliver system changes to production, 54% of respondents said at least weekly, with 24% reporting that changes are delivered at least once per day or on a continuous basis.

The distribution of delivery times has been fairly consistent for the past three years, with a slight dip this year in the “daily” and “continuous” categories (see Figure 6).

### On average, how often do you deploy system changes to production applications? Select the most appropriate answer.

*   **More than once a year:** 29.5% (2023), 29.7% (2022), 29.6% (2021)
*   **Quarterly:** 18.9% (2023), 19.3% (2022), 11.3% (2021)
*   **Monthly:** 13.4% (2023), 14.1% (2022), 8.9% (2021)
*   **More than once per month:** 18.7% (2023), 16.3% (2022), 13.9% (2021)
*   **Weekly:** 13.1% (2023), 10.3% (2022), 9.6% (2021)
*   **Daily:** 8.0% (2023), 5.3% (2022), 4.1% (2021)
*   **Continuously:** 7.2% (2023), 2.8% (2022), 2.0% (2021)
*   **Annually:** 3.1% (2023), 2.8% (2022), 2.0% (2021)
*   **Other/Ad hoc:** 1.8% (2023), 0.4% (2022), 0.3% (2021)

![Image description: A bar chart showing the frequency of deployment to production applications from 2021 to 2023, broken down by deployment frequency categories.]

Figure 6. Frequency of Delivery to Production, 2021–2023

Investments in continuous integration/continuous deployment (CI/CD) tooling enable organizations to make small changes to their production codebase faster, with many teams working to deliver a constant stream of changes that can be pushed to production. The high ratio of developers to security engineers makes it clear that the only way to keep pace is to automate security testing in the CI/CD pipeline so that every code push is evaluated for security flaws.

The fact that approximately 45% of respondents reported deploying changes on a weekly or daily basis, but not continuously, suggests that DevSecOps teams may now have more time available to run deeper scans, between code commit and release to production, while also meeting business delivery requirements.

Organizational leaders should look for meaningful metrics that make it possible to ensure that 100% of the application portfolio is deployed using CI/CD pipelines complete with security tests. Once all applications have integrated security testing performed at every pass through the pipeline, new security tests can be introduced to raise the bar until all security requirements are achieved. It’s important to remember that security tests can only be designed to test for known issues. For this reason, penetration tests and bug bounties—which can help security practitioners find unknown issues—still have an essential role to play in a comprehensive application security program. Cloud-native application protection platforms are being used to characterize normal application behavior and enforce zero-trust principles as an additional countermeasure to protect against exploited security flaws (see the “DevSecOps Tools and Practices: What Works?” section for more details).

### On average, how often do you assess or test the security of your business-critical applications? Select the most appropriate answer.

*   **Never:** 2.5% (2023), 2.0% (2022), 2.4% (2021)
*   **Annually:** 17.7% (2023), 16.0% (2022), 18.4% (2021)
*   **More than once a year:** 22.2% (2023), 21.6% (2022), 17.3% (2021)
*   **Quarterly:** 16.0% (2023), 8.2% (2022), 4.1% (2021)
*   **Monthly:** 17.0% (2023), 9.8% (2022), 8.2% (2021)
*   **More than once per month:** 14.2% (2023), 7.1% (2022), 4.0% (2021)
*   **Weekly:** 10.9% (2023), 7.1% (2022), 4.0% (2021)
*   **Daily:** 7.1% (2023), 6.8% (2022), 4.3% (2021)
*   **Continuously:** 3.9% (2023), 4.1% (2022), 4.0% (2021)
*   **Only as changes are made:** 8.0% (2023), 8.2% (2022), 6.8% (2021)
*   **Other:** 1.4% (2023), 0.9% (2022), 0.9% (2021)
*   **Unknown:** 3.0% (2023), 2.2% (2022), 2.0% (2021)

![Image description: A bar chart showing the frequency of security assessment/testing for business-critical applications from 2021 to 2023, broken down by assessment frequency categories.]

Figure 7. Frequency of Assessing Business-Critical Applications, 2021–2023

New security threats, flaws, and vulnerabilities are, of course, being discovered constantly. Even an application with a stable codebase can have security flaws that remain undiscovered until the application is subjected to security testing. When most organizations (54%) are delivering application changes to production at least weekly, the only way to cope with this volume of activity is to automate security testing and integrate it with the CI/CD tool chain.

The implementation of automated security testing requires significant investment. But once this investment has been made, organizations can utilize these capabilities to incrementally improve the security of the applications they build, write custom tests to assess all their applications, and quickly assess the impact of newly discovered vulnerabilities across their application portfolio.

To explore this trend, we asked, “On average, how often do you assess or test the security of your business-critical applications?” (See Figure 7 above.) The responses were striking:

*   53% of respondents said their organizations test the security of their business-critical applications at least weekly, with 31% testing them at least daily.
*   Comparing the share of organizations that are deploying applications weekly or more frequently (54%) with that of organizations testing their business-critical applications at least weekly (53%) indicates that integrated automated security testing with DevOps tooling is becoming the norm.

> **TAKEAWAY**
> Security organizations should automate as much of the security testing process as possible, so that testing can be performed more frequently, more broadly, and more cost-effectively.

Security at velocity also involves remediation speed, of course. Automated security testing is highly effective at identifying known security vulnerabilities, but remediating critical security issues takes engineering time and management commitment. The 2023 distribution of responses looks much like the responses from 2022, with 53% and 54% of respondents, respectively, stating that their organizations get critical security issues resolved within a week or less.

### On average, how long does it take for your organization to patch/resolve critical security risks/vulnerabilities for systems in use?

*   **Same day:** 10.8% (2023), 10.8% (2022)
*   **Next day:** 7.6% (2023), 5.6% (2022)
*   **2–7 days:** 25.5% (2023), 20.9% (2022)
*   **8–30 days:** 30.7% (2023), 27.3% (2022)
*   **1–3 months:** 16.5% (2023), 11.1% (2022)
*   **4–6 months:** 3.2% (2023), 2.6% (2022)
*   **6–12 months:** 2.0% (2023), 1.8% (2022)
*   **More than a year:** 1.4% (2023), 0.7% (2022)
*   **Other:** 0.3% (2023), 0.7% (2022)
*   **Unknown:** 0.0% (2023), 0.0% (2022)

![Image description: A bar chart showing the average time to resolve critical security risks/vulnerabilities for systems in use in 2022 and 2023.]

Figure 8. Average Time to Resolve Vulnerabilities, 2022–2023

The tail of the distribution, however, shows that 16% of the respondents are aware that it takes their organization more than 30 days to fix critical security issues. Development teams often feel pressure from management to prioritize new functionality over the maintenance of application security. And whereas creating new functionality is interesting, most people consider patching security issues to be drudgery. To help development teams address issues in components included in their applications, numerous SCA tools (for example, Mend SCA, Snyk Open Source, Synopsys Black Duck,¹ and Veracode SCA) include the ability to integrate with source code management systems to create a pull request that developers can review, test, and merge into the feature code as part of their workflows, reducing some of the burden on them and also reducing the time to repair the vulnerability (see Figure 8).

## Automated Compliance

Policy-as-code and CSPM are different techniques for enforcing compliance policies automatically. In this year’s survey—like the previous year’s—more than 60% of respondents (62% in 2023, 60% in 2022) said that at least 50% of their organization’s compliance enforcement is automated. Still, the number of respondents who reported that 100% of their policies are enforced automatically decreased significantly in 2023 from 2022 (6% versus 18%). There was also a decrease in the percentage of respondents who either hadn’t implemented any automated policy enforcement or didn’t know how much coverage their automated policy checks had. (These responses show as negative percentages in Figure 9.)

### What percentage of compliance policies are checked/enforced automatically? 2021–2023

*   **0%:** 14.2% (2023), 10.5% (2022), 7.4% (2021)
*   **1–24%:** 14.0% (2023), 14.8% (2022), 14.8% (2021)
*   **25–49%:** 14.8% (2023), 14.2% (2022), 14.0% (2021)
*   **50–74%:** 27.9% (2023), 32.2% (2022), 29.9% (2021)
*   **75–99%:** 16.5% (2023), 17.9% (2022), 16.8% (2021)
*   **100%:** 6.0% (2023), 18.0% (2022), 14.5% (2021)
*   **Unknown/None:** -1.4% (2023), -2.0% (2022), -3.1% (2021)

![Image description: A bar chart showing the percentage of compliance policies checked or enforced automatically from 2021 to 2023, broken down by percentage ranges.]

Figure 9. Percentage of Compliance Policies Checked or Enforced Automatically

The use of automated checking or enforcement of compliance policies shows that DevSecOps principles are starting to have a more significant impact on security practices. Security teams have begun to recognize the importance of implementing DevOps principles within their own practices to achieve enterprise scale and development agility. At the same time, DevOps teams are integrating policy-as-code tests into