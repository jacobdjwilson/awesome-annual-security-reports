# SANS 2023 DevSecOps Survey
## Table of Contents
- [Executive Summary](#executive-summary)
- [Technology](#technology)
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
- [DevSecOps Tools and Practices: What Works?](#devsecops-tools-and-practices-what-works)
- [Key Performance Indicators and Metrics](#key-performance-indicators-and-metrics)
- [Top DevSecOps Challenges and Success Factors](#top-devsecops-challenges-and-success-factors)
- [Future Trends](#future-trends)
- [Going Forward](#going-forward)

Written by Ben Allen and Chris Edmundson
August 2023
©2023 SANS™ Institute
2
## Executive Summary
DevSecOps represents the intersection of software development (Dev), security (Sec), 
and operations (Ops) with the fundamental objective of automating, monitoring, and 
integrating security throughout all phases of the software development life cycle (SDLC): 
plan, develop, build, test, release, deliver, deploy, operate, and monitor. Ultimately, 
DevSecOps is fundamentally concerned with enabling agility, which inevitably brings with 
it the challenges that come with sharing the responsibility for security best practices with 
other stakeholders across the entire continuous integration/continuous deployment  
(CI/CD) pipeline. Achieving this shared-responsibility 
ideal requires the development of trusted relationships 
among development, security, and operations teams.
The 2023 DevSecOps Survey—the 10th in an annual 
series—considers a broad range of indicators of 
maturity in these areas and evaluates them against a 
retrospective view of previous years’ survey responses, 
with the goal of helping security practitioners 
understand:
- How organizations use cloud platforms, 
architectures, and development ecosystems 
to identify security requirements, risks, and 
opportunities
- How organizations deploy appropriate security 
within the CI/CD pipeline, injecting security best 
practices while keeping up with the delivery of 
products and features to stakeholders
- What security tools and best practices 
organizations leverage to maintain a “shift-left” 
mentality—to keep security in mind continuously 
throughout the development process
- What skills are needed to empower organizations 
to architect secure applications and cloud services 
and help them find and fix vulnerabilities as early 
as possible
- What are the future trends and adoption rates of 
new technology, such as artificial intelligence (AI), 
data science, and GitOps—and how they might 
impact the future of DevSecOps

### Key Findings
- The trend toward organizations leveraging multiple cloud 
solutions continues, as indicated by the respondents using 
Amazon Web Services (AWS), Microsoft Azure, or Google Cloud 
Platform (GCP) to run more than 75% of their application 
workloads. Forty-seven percent of the respondents said they use 
other cloud hosting providers, including Alibaba Cloud, IBM Cloud, 
and Oracle Cloud—a dramatic increase from just 25% last year.
- A key DevSecOps challenge remains the difficulty of acquiring 
the necessary funding to purchase newly available security and 
testing tools.
- The key success factors the survey respondents identified 
show the importance organizations continue to place on 
communications within the organization and creating “security 
champions” through professional development activities.
- Cloud-hosted virtual machines (VMs) are still preferred over 
containers and serverless functions, with 69% of respondents 
reporting at least 25% of their applications running on VMs.
- Another interesting trend this year is that DevSecOps is now 
clearly seen as a business-critical issue and a risk management 
concern. Forty percent of the respondents were aligned with the 
business side, and 13% of respondents identified themselves as 
business managers.
- The dominant industries represented by the respondents aligned 
with the technology, cybersecurity, and application development 
verticals. Representation from the banking and finance industry 
shows a significant decline (down from 17% in 2022 to 7% in 2023), 
and several key industries—notably government and healthcare—
appear to be underrepresented, as they have been in past years.
- One of the notable forward-looking trends shown by the 2023 
survey—reflecting industrywide trends—is a significant increase 
(16%) in respondents reporting that they were investigating 
and experimenting with the use of AI or data science to improve 
DevSecOps, up from 33% in 2022 to 49% in 2023.
3
## Technology
![Image description: Four gears, each representing 5 respondents, labeled "Technology"]
### Top 4 Industries Represented
Each gear represents 5 respondents.
![Image description: Five buildings, each representing 20 respondents, labeled "Organizational Size"]
### Organizational Size
Small
(Up to 1,000)
Small/Medium
(1,001–5,000)
Medium
(5,001–15,000)
Medium/Large
(15,001–50,000)
Large
(More than 50,000)
Each building represents 20 respondents.
![Image description: Four people, each representing 5 respondents, labeled "Top 4 Roles Represented"]
### Top 4 Roles Represented
Business manager
Application developer
Security administrator/
security analyst
Security architect
Each person represents 5 respondents.
Operations and Headquarters
Cybersecurity
Application 
development
Ops: 304
HQ:  270
Ops: 46
HQ:  10
Ops: 46
HQ:  17
Ops: 65
HQ:  10
Ops: 32
HQ:  1
Ops: 101
HQ:  23
Ops: 280
HQ:  13
Ops: 91
HQ:  19
Manufacturing
Figure 1. Demographics of Survey Respondents

## A Snapshot of the Respondents
The 363 respondents to this year’s survey represent a highly diverse set of roles, 
industries, and organizational sizes (see Figure 1). Unsurprisingly, they show a strong bias 
toward security, with 34% of respondents performing a direct security function of some 
kind. Security administrator/security analyst is by far the most common role, at 10.2%. 
Development roles—including application developer, cloud architect, software engineer, 
and DevOps engineer—are, of course, also well represented, at 21%. But the single most 
represented role in the survey is business manager, at 13% of the respondents, clearly 
showing that DevSecOps is now broadly recognized as a business concern, not solely a 
technical issue. Management and executive roles, including the business manager role, 
comprise 40% of the respondents (including security and compliance managers, quality 
analysis [QA] release managers, CxOs, and IT managers/directors).
4
More than half the respondents (53%) are from the top 5 industries. Small organizations—
defined as those with 1,000 or fewer full-time and contract employees—dominate the survey, 
with a total of 61% of the respondents. Larger organizations are distributed relatively evenly 
across the other organizational-size categories. Additionally, this may also suggest that 
organizations are outsourcing their development resources.
The United States is disproportionately represented in terms of geography, with 74% 
of respondents’ primary corporate headquarters located there and 84% of operations 
maintained there. Canada and Europe followed at a far-distant second and third, at 6% and 
5% of corporate headquarters and 28% and 25% of operations, respectively.

## Understanding the DevSecOps Environment
This year’s survey, like the previous years’, shows adoption and use of cloud computing 
as an IT delivery model continuing to accelerate dramatically. This year, for example, 
only 54% of respondents reported that their organizations run 25% or more of their 
applications on-premises, down from 65% in 2022 and 85% in 2021—a 31% drop in just 
three years (see Figure 2). Moreover, fewer than 5% of respondents indicated that they 
ran all their applications on-premises, while almost 7% said they have no on-premises 
applications at all, and more than 84% of the survey respondents reported at least some 
degree of cloud usage.
 
 
These results clearly show that the shift to the cloud is ongoing (and almost certain to 
continue). But the survey results also offer an important reminder that not all applications 
are based in the cloud. Overall, a still very substantial 29% of the respondents reported that 
50% or more of their applications remain on-premises.
A closer look at the cloud responses shows that, as in previous years, cloud-hosted VMs 
are still preferred over cloud-hosted container services or cloud-hosted functions-as-
a-service (FaaS, also called serverless computing)—but also that most organizations’ 
cloud implementations remain highly diverse. In this year’s survey, although 69% of the 
respondents said that at least 25% of their applications run on VMs, 59% use cloud-hosted 
container services for the same percentage of their applications and 57% use FaaS.
![Image description: Bar graph showing the percentage of applications running on different platforms]
Figure 2. Most Commonly Used 
Platforms for Applications
What percentage of your applications are running in the following methods?
50% 
40% 
30% 
20% 
10% 
0%
35.0%
6.8%
25.1%
16.5%
7.7%
4.6%
On-premises
22.8%
5.1%
42.7%
16.8%
5.7% 4.0%
Cloud-hosted 
virtual machine
29.9%
7.4%
30.5%
17.9%
7.4%
3.1%
Cloud-hosted 
container service
27.9%
10.5%
32.2%
14.5%
7.4%
2.8%
Cloud-hosted functions-as-
a-service (FaaS) (serverless)
14.2%
14.8%
14.0% 14.8%
2.8% 2.0%
Other
 0%        
 1–24%        
 25–49%        
 50–74%        
 75–99%        
 100%
5
This mix of VMs, containers, and FaaS has important security 
implications, because all three of these technologies must be 
properly secured. That means DevSecOps teams must have 
the skills and tooling to secure all three approaches—which, 
despite considerable overlap, are all distinctly different. A further 
consideration is that an enterprise using the cloud can likely 
delegate some mundane security tasks to its cloud service 
provider—freeing up its own personnel for more important 
higher-level duties—but this is not the case with on-premises 
applications. This suggests that organizations using the cloud 
should look to providers that are prepared to take on more 
security management responsibilities.

## Application Hosting in the Cloud
The survey results clearly show that most organizations using the cloud are engaging with 
multiple cloud service providers and that the distribution of applications running on each 
of the three most important cloud service providers is beginning to even out. 
For the more than 84% of respondents who reported using the cloud:
- 90% have applications running on Amazon Web Services (AWS).
- 84% have applications running on Microsoft Azure.
- 74% have applications running on Google Cloud Platform (GCP).
Moreover, 47% said they use other cloud hosting providers, including Alibaba Cloud, 
IBM Cloud, and Oracle Cloud—a dramatic increase from just 25% last year. 
Another important finding is the clear trend away from using a single cloud hosting 
provider to run the majority of an organization’s workloads. Table 1 shows the 
percentage of respondents to the 2021, 2022, and 2023 surveys who reported using 
AWS, Azure, or GCP to run 75% or more of their applications. Figure 3 details the 
complete distribution of the 2023 survey responses.

> **TAKEAWAY**
> DevSecOps teams need to invest in tools that make it 
> possible to secure their workloads effectively, wherever 
> they run. Software composition analysis (SCA), static 
> application security testing (SAST), dynamic application 
> security testing (DAST), and threat modeling tools, for 
> example, can all be used to improve the security of long-
> lived VMs and short-lived containers or functions. When 
> selecting tools, security practitioners must recognize that 
> different runtime environments need different tools and 
> must consider whether cloud providers—both current and 
> prospective—have tools integrated into their ecosystems 
> that could potentially streamline security workflows.

![Image description: Bar graph showing the percentage of cloud-based applications hosted by different providers]
Figure 3. Extent of Cloud-Based Application Hosting
What percentage of your cloud-based applications are hosted by:
40% 
30% 
20% 
10% 
0%
21.6%
7.2%
31.7%
19.0%
9.2% 8.1%
Amazon Web 
Services (AWS)
23.6%
16.7%
26.2%
14.7%
8.6%
1.2%
Google Cloud 
Platform (GCP)
22.2%
8.6%
36.0%
14.4%
6.9%
4.3%
Microsoft Azure
15.0%
14.4%
17.9%
11.8%
2.0% 0.6%
Other
 0%        
 1–24%        
 25–49%        
 50–74%        
 75–99%        
 100%
Table 1.  
Respondents Concentrating 75% or More  
of Workloads on a Single CSP, 2021–2023
2023	
17.3%	
11.2%	
9.8%
2022	
21.6%	
14.8%	
5.9%
2021	
27.1%	
18.4%	
7.2%
AWS
GCP
Azure
6
There are many reasons, including the need for business continuity planning and 
the desire for negotiation leverage, that an organization may choose to distribute its 
workloads across multiple cloud service providers. The benefits of using multiple cloud 
service providers are obvious, but so are their security implications: Each provider’s 
environment must be properly secured, but every environment works differently and 
presents different security challenges. And the work involved increases exponentially with 
each additional provider used.
One way leading DevSecOps teams are coping with the multicloud challenge is by creating 
platform-agnostic applications, typically using containerization, so that the application 
can run in any cloud service provider’s container service, or even on-premises, with the 
necessary infrastructure in place.

## Securing Multicloud Environments
The increasing reliance on multiple cloud service providers, with a mix of VMs, containers, 
and FaaS, also sharply increases the challenges of ensuring that all those cloud resources 
are properly secured. To evaluate this challenge, the 2023 DevSecOps survey considered 
similar results from identical questions asked in the 2022 and 2023 surveys regarding two 
of the most important sets of cloud security tools:
- To what extent has your organization adopted cloud security posture management 
(CSPM) software, either commercial or open source? (See Figure 4 for years 
2022/2023.)
- To what extent has your organization adopted cloud workload protection platform 
(CWPP) software? (See Figure 5 for years 2022/2023.)
The survey results from these two years show that even though CSPM is widely deployed, 
it is still highly underutilized. Most respondents said they are using either a commercial or 
an open source CSPM tool, but fewer than 16% overall (2023) and 21% overall (2022) said 
they use those solutions for 75% or more of their AWS accounts, Azure subscriptions, or 
GCP projects. 
7
This decline from the previous year could have several causes. One cause might be that 
the increase in the use of these tools has made organizations more aware of their cloud 
provider inventories and the weaknesses in their protections. Another cause might be 
that vendor pricing is driving organizations to make difficult choices between inadequate 
protection and unacceptable cost. 
CWPP products are also very much underutilized. Although a majority of the respondents 
(greater than 70% across all platforms) said their organizations use CWPP, a much smaller 
percentage (less than 15% overall in 2023, down slightly from 17% in 2022) use it in at least 
75% or more of their AWS accounts, Azure subscriptions, or GCP projects.
Both findings suggest that DevSecOps teams are missing a 
valuable opportunity to enhance the security of their cloud 
environments. CSPM software can help DevSecOps teams ensure 
that the cloud environments that host their applications are 
properly configured and secured using industry best practices, 
but only if this software is used consistently across all cloud 
accounts. Similarly, CWPPs provide various security services 
for workloads, regardless of whether the work is performed 
by VMs, containers, or serverless computing. In the past, this 
would typically have required the installation of multiple agents, 
resulting in a drain on VM resources, but CWPP solutions have 
evolved to overcome that problem. 
![Image description: Bar graph showing the extent of CSPM adoption]
Figure 4. Extent of CSPM Adoption
To what extent has your organization adopted  
cloud security posture management (CSPM) software,  
(either commercial or open source)? 
Total
82.7%
81.0%
69.9%
Greater 
than 75%
13.5%
15.8%
14.0%
Total
64.7%
63.5%
51.6%
Greater 
than 75%
20.5%
17.9%
10.9%
0%
20%
80%
40%
60%
 AWS        
 Azure        
 GCP
2023
2022
![Image description: Bar graph showing the extent of CWPP adoption]
Figure 5. Extent of CWPP Adoption
To what extent has your organization adopted  
cloud workload protection platform software (CWPP)  
(either commercial or open source)? 
Total
82.4%
76.5%
70.3%
Greater 
than 75%
13.2%
10.9%
14.4%
Total
41.6%
58.1%
51.6%
Greater 
than 75%
16.6%
16.6%
3.6%
0%
20%
80%
40%
60%
 AWS        
 Azure        
 GCP
2023
2022

> **TAKEAWAY**
> Both CSPM and CWPP are essential capabilities for 
> organizations operating in multicloud environments. As an 
> organization moves further away from reliance on a single 
> cloud hosting provider, the work of securing each cloud 
> environment increases exponentially. Organizations should 
> consider using or increasing their adoption of commercial 
> or open source CSPM software to ensure that each cloud 
> environment is securely configured, and they should 
> implement CWPPs to protect application workloads at 
> execution time.
8

## Security at Velocity
The survey results clearly show that delivery velocity—the speed at which changes are 
made to applications in development—is remarkably stable. When asked how often their 
organizations deliver system changes to production, 54% of respondents said at least weekly, 
with 24% reporting that changes are delivered at least once per day or on a continuous basis. 
The distribution of delivery times has been fairly consistent for the past three years, with a 
slight dip this year in the “daily” and “continuous” categories (see Figure 6).
Investments in continuous integration/continuous deployment (CI/CD) tooling enable 
organizations to make small changes to their production codebase faster, with many teams 
working to deliver a constant stream of changes that can be pushed to production. The high 
ratio of developers to security engineers makes it clear that the only way to keep pace is 
to automate security testing in the CI/CD pipeline so that every code push is evaluated for 
security flaws.
The fact that approximately 45% of respondents reported deploying changes on a weekly or 
daily basis, but not continuously, suggests that DevSecOps teams may now have more time 
available to run deeper scans, between code commit and release to production, while also 
meeting business delivery requirements.
Organizational leaders should look for meaningful metrics that make it possible to ensure 
that 100% of the application portfolio is deployed using CI/CD pipelines complete with 
security tests. Once all applications have integrated security testing performed at every 
pass through the pipeline, new security tests can be introduced to raise the bar until all 
security requirements are achieved. It’s important to remember that security tests can only 
be designed to test for known issues. For this reason, penetration tests and bug bounties—
which can help security practitioners find unknown issues—still have an essential role to 
play in a comprehensive application security program. Cloud-native application protection 
platforms are being used to characterize normal application behavior and enforce zero-trust 
principles as an additional countermeasure to protect against exploited security flaws (see 
the “DevSecOps Tools and Practices: What Works?” section for more details).
![Image description: Bar graph showing the frequency of delivery to production from 2021-2023]
Figure 6. Frequency of Delivery 
to Production, 2021–2023
On average, how often do you deploy system changes to production applications? Select the most appropriate answer.
 2023        
 2022        
 2021
30% 
20% 
10% 
0%
13.1%
10.3%
9.6%
Continuously
29.7%
29.5%
29.6%
Weekly
8.9%
13.4%
14.1%
Monthly
8.0%
5.3%
4.1%
More than 
once a year
18.7%
13.9%
16.3%
Daily
11.3%
18.9%
19.3%
More than once 
per month
5.6%
7.2%
4.4%
Quarterly
1.8%
0.3%
0.4%
Annually
3.0%
1.1%
2.2%
Other/Ad hoc
9
New security threats, flaws, and vulnerabilities are, of course, being discovered 
constantly. Even an application with a stable codebase can have security flaws that 
remain undiscovered until the application is subjected to security testing. When most 
organizations (54%) are delivering application changes to production at least weekly, the 
only way to cope with this volume of activity is to automate security testing and integrate 
it with the CI/CD tool chain.
The implementation of automated security testing requires significant investment. But 
once this investment has been made, organizations can utilize these capabilities to 
incrementally improve the security of the applications they build, write custom tests 
to assess all their applications, and quickly assess the impact of newly discovered 
vulnerabilities across their application portfolio.
To explore this trend, we asked, “On average, how often do you assess or test the security 
of your business-critical applications?” (See Figure 7 above.) The responses were striking:
- 53% of respondents said their organizations test the security of their business-
critical applications at least weekly, with 31% testing them at least daily.
- Comparing the share of organizations that are deploying 
applications weekly or more frequently (54%) with that of 
organizations testing their business-critical applications 
at least weekly (53%) indicates that integrated automated 
security testing with DevOps tooling is becoming the norm.
Security at velocity also involves remediation speed, of course. 
Automated security testing is highly effective at identifying known security vulnerabilities, 
but remediating critical security issues takes engineering time and management 
commitment. The 2023 distribution of responses looks much like the responses from 2022, 
with 53% and 54% of respondents, respectively, stating that their organizations get critical 
security issues resolved within a week or less.
![Image description: Bar graph showing the frequency of assessing business-critical applications from 2021-2023]
Figure 7. Frequency of Assessing 
Business-Critical Applications, 
2021–2023
On average, how often do you assess or test the security of your business-critical applications? Select the most appropriate answer.
 2023        
 2022        
 2021
30% 
20% 
10% 
0%
10.9%
14.2%
7.1%
Continuously
17.7%
22.2%
21.6%
Weekly
8.2%
8.0%
9.8%
Monthly
8.2%
4.0%
7.8%
More than 
once a year
16.0%
17.0%
18.4%
Daily
6.8%
16.0%
17.3%
More than once 
per month
8.5%
7.1%
9.8%
Quarterly
6.8%
2.2%
4.3%
Annually
4.1%
1.9%
Only as  
changes  
are made
2.4%
0.9%
3.9%
Other
8.2%
4.0%
Unknown
2.0%
2.5%
Never

> **TAKEAWAY**
> Security organizations should automate as much of the 
> security testing process as possible, so that testing can 
> be performed more frequently, more broadly, and more 
> cost-effectively. 
10
The tail of the distribution, however, shows that 16% of the respondents are aware that 
it takes their organization more than 30 days to fix critical security issues. Development 
teams often feel pressure from management to prioritize new functionality over the 
maintenance of application security. And whereas creating new functionality is interesting, 
most people consider patching security issues to be drudgery. To help development 
teams address issues in components included in their applications, numerous SCA tools 
(for example, Mend SCA, Snyk Open Source, Synopsys Black Duck,
[^1] and Veracode SCA) 
include the ability to integrate with source code management systems to create a pull 
request that developers can review, test, and merge into the feature code as part of their 
workflows, reducing some of the burden on them and also reducing the time to repair the 
vulnerability (see Figure 8).
[^1]: Mend SCA, Snyk Open Source, Synopsys Black Duck, and Veracode SCA

## Automated Compliance
Policy-as-code and CSPM are different techniques for enforcing compliance policies 
automatically. In this year’s survey—like the previous year’s—more than 60% of 
respondents (62% in 2023, 60% in 
2022) said that at least 50% of their 
organization’s compliance enforcement 
is automated. Still, the number of 
respondents who reported that 100% of 
their policies are enforced automatically 
decreased significantly in 2023 from 
2022 (6% versus 18%). There was also a 
decrease in the percentage of respondents 
who either hadn’t implemented any automated policy enforcement or didn’t know how 
much coverage their automated policy checks had. (These responses show as negative 
percentages in Figure 9.)
![Image description: Bar graph showing the average time to resolve vulnerabilities from 2022-2023]
Figure 8. Average Time to Resolve 
Vulnerabilities, 2022–2023
On average, how long does it take for your organization to patch/resolve critical security risks/vulnerabilities for systems in use? 
 2023        
 2022    
30% 
20% 
10% 
0%
7.6%
5.6%
Unknown
9.7%
11.1%
Next day
20.9%
25.5%
8–30 days
3.2%
2.6%
4–6 months
0.7%
0.3%
More than 
a year
16.5%
10.8%
Same day
27.3%
30.7%
2–7 days
10.8%
10.8%
1–3 months
1.8%
2.0%
6–12 months
1.4%
0.7%
Other
![Image description: Bar graph showing the percentage of compliance policies checked or enforced automatically from 2021-2023]
Figure 9. Percentage of 
Compliance Policies Checked or 
Enforced Automatically
What percentage of compliance policies are checked/enforced automatically? 
2021–2023
11
The use of automated checking or enforcement of compliance policies shows that DevSecOps 
principles are starting to have a more significant impact on security practices. Security teams 
have begun to recognize the importance of implementing DevOps principles within their 
own practices to achieve enterprise scale and development agility. At the same time, DevOps 
teams are integrating policy-as-code tests into their CI/CD pipelines to validate security 
policy compliance. These tests have value that extends 
beyond compliance, because they’re cost-effective: Writing 
a security test has a one-time cost that quickly approaches 
zero per test when that test is performed frequently. Both 
practices are helping organizations meet the goal of scalable 
continuous compliance.

## Securing Container Services
We’ve already seen that as organizations move to the 
cloud, they deploy their applications using a combination 
of VMs, FaaS, and containerized workloads. Whereas VMs 
offer a strongly self-supported model that corresponds to 
on-premises data center environments, and FaaS offers a 
mostly cloud-provider-supported model, the containerized 
workloads space includes a wide range of support models 
between the other two, so it’s worthwhile to take a closer 
look at how container services are being used.
Organizations looking to use container orchestration tools 
face three basic questions. The first question is whether to 
use Kubernetes, Docker Swarm, or some other orchestration 
option. The second question is whether to use such a tool as 
a managed service or to manage it themselves, and the third 
question is whether to run on cloud-hosted or on-premises 
infrastructure. Figure 10 shows the choices of container 
orchestration tools that respondents’ organizations have 
made over the past three years of the survey:
- Cloud hosted is more prevalent than cloud managed 
for both container services and Kubernetes.
- For on-premises organizations, the choice 
between an orchestrator (Kubernetes or 
OpenShift) and a container engine (Docker 
or Docker Swarm) is an even split for 2023.
- Cloud-managed container services had 
an approximately 10% increase this year, 
suggesting that as organizations migrate to 
the cloud and to containers, they’re favoring 
cloud-managed container services over 
cloud-managed Kubernetes services. 
![Image description: Bar graph showing the container orchestration tools used to manage production workloads]
Figure 10. Container Orchestration Tools 
Used to Manage Production Workloads

> **TAKEAWAY**
> When moving containerized workloads to the cloud, many organizations 
> seem to be taking a lift-and-shift approach, moving their on-premises 
> VMs, which host Kubernetes or Docker environments, to cloud-hosted 
> VMs that perform the same functions. As the provider-managed offerings 
> for Docker and Kubernetes mature, this “lift-and-shift” approach may 
> create challenges for organizations trying to achieve deeper integration 
> with their cloud providers’ security tools. That lift-and-shift approach 
> may, however, also reflect an intentional choice by organizations to avoid 
> these deep integrations as part of their multicloud strategy.
12

## Programming Environments and Risks
Surprisingly, the top 4 responses to the question of which languages 
and platforms present the greatest risk to their application portfolios 
show no overlap at all with 2022’s answers. (The 2023 survey shows 
Python as the greatest risk by a wide margin—at least 12% greater than 
the next option, C/C++.) Even so, the responses concerning the top 10  
language/platform risks show broad stability over the past three 
years of the survey (see Figure 11), despite significant fluctuations in 
the respondents’ demographics during that time period.
Whichever language or languages are seen as the riskiest, the most 
popular, or the most intriguing at any given time, organizations 
need to develop processes and establish standards for bringing new 
languages into their portfolios. These initiatives should consider 
factors like memory safety, support for CI/CD tools (including linting, 
coding standards, security scanning, and dependency management), 
and the need to ensure interoperability with languages already in 
use when defining organizational rules for adopting a new language. 
It is also extremely important that organizations consider the most 
dangerous known software errors when formulating standards for 
adopting new languages in the enterprise. (The regularly updated 
CWE/SANS TOP 25 Most Dangerous Software Errors[^2] list