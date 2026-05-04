# SANS 2023 DevSecOps Survey

Written by Ben Allen and Chris Edmundson
August 2023
©2023 SANS™ Institute

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
- [DevSecOps Tools and Practices: What Works?](#devsecops-tools-and-practices-what-works)
- [Key Performance Indicators and Metrics](#key-performance-indicators-and-metrics)
- [Top DevSecOps Challenges and Success Factors](#top-devsecops-challenges-and-success-factors)

---

## Executive Summary

DevSecOps represents the intersection of software development (Dev), security (Sec), and operations (Ops) with the fundamental objective of automating, monitoring, and integrating security throughout all phases of the software development life cycle (SDLC): plan, develop, build, test, release, deliver, deploy, operate, and monitor. Ultimately, DevSecOps is fundamentally concerned with enabling agility, which inevitably brings with it the challenges that come with sharing the responsibility for security best practices with other stakeholders across the entire continuous integration/continuous deployment (CI/CD) pipeline. Achieving this shared-responsibility ideal requires the development of trusted relationships among development, security, and operations teams.

The 2023 DevSecOps Survey—the 10th in an annual series—considers a broad range of indicators of maturity in these areas and evaluates them against a retrospective view of previous years’ survey responses.

### Key Findings
- The trend toward organizations leveraging multiple cloud solutions continues, as indicated by the respondents using Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP) to run more than 75% of their application workloads. Forty-seven percent of the respondents said they use other cloud hosting providers, including Alibaba Cloud, IBM Cloud, and Oracle Cloud—a dramatic increase from just 25% last year.
- A key DevSecOps challenge remains the difficulty of acquiring the necessary funding to purchase newly available security and testing tools.
- The key success factors the survey respondents identified show the importance organizations continue to place on communications within the organization and creating “security champions” through professional development activities.
- Cloud-hosted virtual machines (VMs) are still preferred over containers and serverless functions, with 69% of respondents reporting at least 25% of their applications running on VMs.
- Another interesting trend this year is that DevSecOps is now clearly seen as a business-critical issue and a risk management concern. Forty percent of the respondents were aligned with the business side, and 13% of respondents identified themselves as business managers.
- The dominant industries represented by the respondents aligned with the technology, cybersecurity, and application development verticals. Representation from the banking and finance industry shows a significant decline (down from 17% in 2022 to 7% in 2023).
- One of the notable forward-looking trends shown by the 2023 survey—reflecting industrywide trends—is a significant increase (16%) in respondents reporting that they were investigating and experimenting with the use of AI or data science to improve DevSecOps, up from 33% in 2022 to 49% in 2023.

---

## A Snapshot of the Respondents

The 363 respondents to this year’s survey represent a highly diverse set of roles, industries, and organizational sizes (see Figure 1). 

![Figure 1. Demographics of Survey Respondents]

More than half the respondents (53%) are from the top 5 industries. Small organizations—defined as those with 1,000 or fewer full-time and contract employees—dominate the survey, with a total of 61% of the respondents. 

The United States is disproportionately represented in terms of geography, with 74% of respondents’ primary corporate headquarters located there and 84% of operations maintained there.

---

## Understanding the DevSecOps Environment

This year’s survey shows adoption and use of cloud computing as an IT delivery model continuing to accelerate dramatically. Only 54% of respondents reported that their organizations run 25% or more of their applications on-premises, down from 65% in 2022 and 85% in 2021 (see Figure 2).

![Figure 2. Most Commonly Used Platforms for Applications]

> **TAKEAWAY**
> DevSecOps teams need to invest in tools that make it possible to secure their workloads effectively, wherever they run. Software composition analysis (SCA), static application security testing (SAST), dynamic application security testing (DAST), and threat modeling tools, for example, can all be used to improve the security of long-lived VMs and short-lived containers or functions.

---

## Application Hosting in the Cloud

For the more than 84% of respondents who reported using the cloud:
- 90% have applications running on Amazon Web Services (AWS).
- 84% have applications running on Microsoft Azure.
- 74% have applications running on Google Cloud Platform (GCP).

Table 1 shows the percentage of respondents who reported using AWS, Azure, or GCP to run 75% or more of their applications.

**Table 1. Respondents Concentrating 75% or More of Workloads on a Single CSP, 2021–2023**

| | 2023 | 2022 | 2021 |
| :--- | :--- | :--- | :--- |
| AWS | 17.3% | 21.6% | 27.1% |
| Azure | 11.2% | 14.8% | 18.4% |
| GCP | 9.8% | 5.9% | 7.2% |

![Figure 3. Extent of Cloud-Based Application Hosting]

---

## Securing Multicloud Environments

The 2023 DevSecOps survey evaluated the adoption of cloud security posture management (CSPM) and cloud workload protection platform (CWPP) software.

![Figure 4. Extent of CSPM Adoption]
![Figure 5. Extent of CWPP Adoption]

> **TAKEAWAY**
> Both CSPM and CWPP are essential capabilities for organizations operating in multicloud environments. As an organization moves further away from reliance on a single cloud hosting provider, the work of securing each cloud environment increases exponentially.

---

## Security at Velocity

When asked how often their organizations deliver system changes to production, 54% of respondents said at least weekly, with 24% reporting that changes are delivered at least once per day or on a continuous basis (see Figure 6).

![Figure 6. Frequency of Delivery to Production, 2021–2023]

> **TAKEAWAY**
> Security organizations should automate as much of the security testing process as possible, so that testing can be performed more frequently, more broadly, and more cost-effectively.

---

## Automated Compliance

Policy-as-code and CSPM are different techniques for enforcing compliance policies automatically. In this year’s survey, more than 60% of respondents (62% in 2023, 60% in 2022) said that at least 50% of their organization’s compliance enforcement is automated.

![Figure 9. Percentage of Compliance Policies Checked or Enforced Automatically]

---

## Securing Container Services

Organizations looking to use container orchestration tools face three basic questions: whether to use Kubernetes, Docker Swarm, or some other option; whether to use it as a managed service; and whether to run on cloud-hosted or on-premises infrastructure.

![Figure 10. Container Orchestration Tools Used to Manage Production Workloads]

> **TAKEAWAY**
> When moving containerized workloads to the cloud, many organizations seem to be taking a lift-and-shift approach. As the provider-managed offerings for Docker and Kubernetes mature, this “lift-and-shift” approach may create challenges for organizations trying to achieve deeper integration with their cloud providers’ security tools.

---

## Programming Environments and Risks

Python is identified as the greatest risk by a wide margin—at least 12% greater than the next option, C/C++.

![Figure 11. Languages and Platforms Presenting the Greatest Risk or Exposure, 2021-2023]

> **TAKEAWAY**
> Identifying the most dangerous software errors and how they can be eliminated will be critical to the success of DevSecOps teams’ ongoing efforts to reduce bugs and deliver more stable systems. The adoption of memory-safe languages, particularly on new projects, can eliminate entire classes of vulnerabilities.[^1]

[^1]: “CWE/SANS TOP 25 Most Dangerous Software Errors,” www.sans.org/top25-software-errors/

---

## DevOps Foundational Practices

The role of the cloud security architect in supporting DevSecOps process improvements shows a small decrease compared with last year (2%). This is, however, offset by an overall increase in organizational focus on process improvement—from 79% in 2022 to 84% in 2023.

![Figure 12. Role of Cloud Security Architects Supporting Process Improvement]
![Figure 13. Continuous Integration Tools Usage, 2021–2023]

---

## Security Testing

The 2023 survey shows the highest percentage of testing (49%) being conducted at the code commit/pull request stage.

![Figure 14. The Timing of Security Testing in Build and Release Pipeline Workflows, 2021–2023]
![Figure 15. Usefulness of Various Security Testing Practices and Tools]

---

## DevSecOps Tools and Practices: What Works?

Build automation, continuous integration, and automated testing remain the leading organizational practices.

**Table 3. Respondents’ Adoption Rates of Various DevSecOps Practices, 2021–2023**

| Practice | 2023 | 2022 | 2021 |
| :--- | :--- | :--- | :--- |
| Build automation | 60.9% | 83.3% | 66.2% |
| Continuous integration (CI) | 49.6% | 57.2% | 51.6% |
| Automated testing | 44.9% | 57.5% | 51.6% |

---

## Key Performance Indicators and Metrics

The number of open security vulnerabilities remains the KPI that is most widely used to measure the success of DevSecOps programs.

![Figure 20. Top KPIs Used in Respondents’ Organizations, 2021–2023]

---

## Top DevSecOps Challenges and Success Factors

The survey respondents’ view of the No. 1 success factor in building a DevSecOps program has changed over the years, from training to buy-in to integrated security testing.

> **TAKEAWAY**
> A successful DevSecOps program requires a strong focus on communication and culture to break down organizational silos. As the DevSecOps journey progresses, agreeing on the why (getting buy-in), understanding the what (training), and implementing the how (integrating tools into processes) may be temporary top priorities, but communication must not be neglected.

**Table 4. Respondents’ Ranking of DevSecOps Success Factors and Challenges, 2021–2023**

| Success Factor | 2023 Rank | 2022 Rank | 2021 Rank |
| :--- | :--- | :--- | :--- |
| Integrating automated security testing | 1 | 4 | 5 |
| Improving communications | 2 | 2 | 2 |
| Automating build/test/deploy | 3 | 3 | 7 |

---

8.1

7.1

6.3

Maximum
Percentage

54.1

55.6

55.3

52.4

57.5

43.4

35.8

51.8

35.1

42.2

28.0

36.0

31.5

10.0

Maximum
Percentage

48.8

41.9

50.0

44.1

44.1

36.2

35.1

27.2

28.3

26.4

23.9

24.4

16.8

16.5

15.3

15.0

13.4

15.4

22.6

7.9

6.6

SANS 2023 DevSecOps Survey

22

Future Trends

One of the notable forward-looking trends the 2023 survey shows is a significant

increase (16%) in the use of AI or data science to improve DevSecOps through

investigation and experimentation—from 33% in 2022 to 49% in 2023. The intense

recent publicity about AI and the increasing availability of AI models, training data,

and tools make this an area where ongoing adoption seems highly likely. That said,

a strong contingent of the respondents (approximately 30%) reported not using AI

or data science capabilities at all. This may reflect issues such as the rising level of

concern surrounding data privacy and ownership of intellectual property. Responses

also captured an increase in pilot projects integrating security operations into both

the “AI and machine learning ops” and “data science operations” categories—a

possible indication that organizations are performing threat modeling and risk

assessments prior to incorporating AI capabilities into products (see Table 5).

Table 5. Emerging Technology for DevSecOps

Success Factor

Applying artiﬁcial intelligence or data science to improve DevSecOps

Integrating security operations into artiﬁcial intelligence/machine learning ops

Integrating security operations into data science ops

Utilizing serverless computing to build, manage, and scale applications

Unknown

Not at All

10.8%

9.4%

8.4%

5.9%

28.6%

20.9%

19.9%

11.1%

Conducting
Preliminary
Investigation

Experimenting
or Conducting
Pilot Projects

Partially
Integrated

Fully
Integrated

33.8%

26.5%

22.0%

25.4%

15.3%

22.0%

24.4%

24.7%

5.9%

12.5%

17.8%

19.2%

4.5%

5.9%

6.3%

11.1%

Leveraging GitOps to test, verify, automate, deploy, and advance/mature the principles
of infrastructure as code

11.5%

15.0%

19.2%

18.1%

22.3%

12.5%

Developing with microservices rather than monolithic applications to improve
the overall agility and ﬂexibility for DevSecOps

9.1%

17.1%

22.0%

20.6%

20.6%

10.5%

Leveraging application security orchestration and correlation (ASOC) tools for DevSecOps

12.5%

24.0%

21.3%

15.0%

16.7%

Pursuing a platform engineering approach to streamline application development,
analysis, deployment, and operations

10.5%

19.5%

21.6%

19.5%

17.4%

8.7%

9.4%

FaaS, GitOps, and microservices share both the most overall attention from

organizations and the largest percentages of full integration. These three practices

are often interrelated and interwoven, so it makes sense that they move as a group,

reinforcing one another.

The subject of platform engineering to streamline the flow from idea to

implementation was added to the survey this year. The responses show greater

awareness and adoption of platform engineering practices than of application security

orchestration and correlation (ASOC) tools. As the developer self-service features

inherent in a platform engineering practice mature, it will be essential to leverage the

orchestration used to build, package, test, and deploy an application to incorporate

security testing and tooling at key points along the path that has been laid out. A

well-implemented software engineering platform, designed in close collaboration with

security stakeholders, could likely meet an organization’s ASOC objectives.

SANS 2023 DevSecOps Survey

23

This year’s respondents replied to the overall set of Future Trends questions with an

unknown response roughly half as often as last year. It seems possible that this indicates

that DevSecOps efforts are being communicated better within organizations, indicating

that the sharing principle from the CALMS framework (the S in CALMS) is taking hold.

From 2022 to 2023, all positive responses increased, with the exception of “developing

with microservices,” which saw a small decrease (see Figure 21).

Emerging Technology for DevSecOps 2022–2023

 Unknown

 Not at all

Conducting preliminary investigation

 Experimenting or conducting pilot projects

Partially integrated

Fully integrated

Applying artiﬁcial intelligence or data
science to improve DevSecOps

2023

-10.8%

-28.6%

2022

-20.0%

-32.5%

33.8%

15.3% 5.9% 4.5%

23.2%

10.0%

10.4% 2.9%

Integrating security operations into
artiﬁcial intelligence/machine learning ops

Integrating security operations
into data science ops

Utilizing serverless computing to build,
manage, and scale applications

Leveraging GitOps to test, verify,
automate, deploy, and advance/mature
the principles of infrastructure as code

Developing with microservices rather than
monolithic applications to improve the
overall agility and ﬂexibility for DevSecOps

Leveraging application security orchestration
and correlation (ASOC) tools for DevSecOps

Pursuing a platform engineering approach
to streamline application development,
analysis, deployment, and operations

2023

2022

2023

2022

2023

2022

2023

2022

2023

2022

2023

2022

2023

-9.4%

-20.9%

26.5%

22.0%

12.5% 5.9%

-16.8%

-26.4%

24.6%

15.4%

12.5% 3.2%

-8.4% -19.9%

22.0%

24.4%

17.8% 6.3%

-17.5%

-23.6%

18.9%

14.6%

17.9% 5.7%

-5.9% -11.1%

25.4%

24.7%

19.2%

11.1%

-16.8%

-12.5%

20.4%

18.6%

20.4%

10.4%

-11.5%

-15.0%

19.2%

18.1%

22.3%

12.5%

-18.6%

-13.6%

15.4%

21.8%

21.1%

8.9%

-9.1%

-17.1%

22.0%

20.6%

20.6%

10.5%

-14.6%

-10.7%

15.4%

15.0%

29.6%

13.2%

-12.5%

-24.0%

21.3%

15.0%

16.7%

8.7%

-22.5%

-16.8%

16.8%

13.9%

19.3%

9.6%

-19.5%

-10.5%

-40%

-20%

0%

21.6%

20%

19.5%

40%

17.4%

9.4%

60%

80%

Figure 21. Emerging Technology for
DevSecOps, 2022–2023

SANS 2023 DevSecOps Survey

24

Going Forward

A DevSecOps program needs to integrate the practices of security, development, and

operations teams, creating a cohesive, collaborative system development life cycle. This

requires substantial initial and ongoing investment by the organization, but its benefits—

which include reduced time to fix security issues, less burdensome security processes, and

increased ownership of application security7—are well understood.

This year’s survey continues to point toward increasing maturity and adoption of DevSecOps

practices, but the survey data also reveal areas for improvement. Key takeaways from the 2023

survey include:

•   Although workloads are migrating to the cloud, DevSecOps teams may be missing out on

some of the advantages of immutable containers and ephemeral serverless functions.

Both approaches fit well with CI/CD deployments and can be utilized to create

applications that are secure, performant, and potentially more cost-effective than VMs.

•   Multicloud has become the norm. When organizations use multiple cloud providers,

the work to secure those clouds grows exponentially. DevSecOps practitioners should

consider implementing and expanding the use of open source or commercial CSPM

tools to assess and manage infrastructure security at scale. Additionally, using CWPPs

can enable organizations to protect resources across cloud providers.

•   DevSecOps teams should continue to invest in tools that help to ensure the security

and integrity of their applications and all the dependent components in their software

supply chains.

•   Organizations should leverage KPIs to identify the most important area for the

organization to improve next. Benchmarking against peer organizations’ metrics can be

used to expand management support, and they also help to demonstrate due care.

•   DevSecOps teams should limit the programming languages approved for new

development projects based on security risks and availability of security testing tools

(among other factors), and they should refactor older code written with memory-unsafe

languages as opportunities arise.

•   When moving workloads to the cloud, organizations must choose between a lift-and-

shift approach that minimizes the use of cloud-provider-specific capabilities and a

rebuild-and-integrate approach that makes intentional use of each cloud provider’s

unique capabilities. There is no one-size-fits-all approach, so organizations should

develop guidance to apply consistently to their decision-making process.

•   Organizations should continue to champion a culture of communication and shared

responsibility for security across teams, processes, and projects.

•   As machine learning and AI efforts erupt across organizations, they should continue to

apply the “shift security left” mentality by performing risk assessments and creating

threat models for AI experiments and projects before starting work.

7   DevOps Digest, “A Primer on Secure DevOps: Learn the Benefits of These 3 DevSecOps Use Cases,” July 18, 2022,

www.devopsdigest.com/secure-devops-use-cases

SANS 2023 DevSecOps Survey

25

Organizations continue to be pressured to do more work with fewer resources—especially

personnel. DevSecOps is an approach that can help relieve some of that pressure. The

right KPIs will keep teams focused on the proper priorities, and investments in automation

for build, test, and deployment work will increase agility, including agility in responding to

security incidents.

Critical focus areas for a successful DevSecOps program are:

•   Early consideration for the security facets of any project, through risk assessment

and threat modeling prior to writing any code

•   Automation of security tests aligned with well-defined standards and practices

•   Comprehensive understanding of the security status of resources required to

run your applications, including infrastructure, third-party software and software

developed in-house

•   Automation of the entire build, test, and deploy process, to accelerate responding to

attacks and vulnerabilities and to enable automatic remediation

Many organizations feel an urgent need for more qualified DevSecOps personnel. Because

demand continues to outweigh supply in this area, there is a real need to spark more

interest in this ever-changing field. To cope with the scarcity of talent amid competitive

pressures, organizations should further leverage proven DevSecOps practices and explore

emerging technological capabilities. This may mean harnessing some of the underutilized

technology (for example, CSPM, CWPP, AI, machine learning ASOC) or applying new

tools, technologies, and practices (for example, immutable infrastructure, zero trust,

benchmarking) in pursuit of optimizing and streamlining DevSecOps.

This survey showcases the progress made by the DevSecOps community in improving

organizations’ security postures and organizational effectiveness, recognizes the

challenges it still faces, and highlights areas for additional focus on the path to

DevSecOps excellence.

Sponsor

SANS would like to thank this survey’s sponsor:

SANS 2023 DevSecOps Survey

26