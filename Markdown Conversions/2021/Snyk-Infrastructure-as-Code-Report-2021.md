# SNYK RESEARCH REPORT

## Infrastructure as Code Security Insights

February 2021

## Table of Contents
- [Introduction](#introduction)
- [Current IaC Practices](#current-iac-practices)
- [Does Speed Equate to Safety?](#does-speed-equate-to-safety)
- [Current IaC Security Practices](#current-iac-security-practices)
- [So what is standing in the way of making a change?](#so-what-is-standing-in-the-way-of-making-a-change)
- [Infrastructure Remediation](#infrastructure-remediation)
- [Who Holds Responsibility for IaC Security?](#who-holds-responsibility-for-iac-security)
- [Snyk Infrastructure as Code: Find and fix configuration security issues the way cloud native experts do.](#snyk-infrastructure-as-code-find-and-fix-configuration-security-issues-the-way-cloud-native-experts-do)
- [Survey Methodology](#survey-methodology)

---

# Introduction

Cloud native applications are more than just the code developers create - today’s applications include infrastructure as code (IaC) that dictate how the applications are setup on cloud infrastructure and how containerized applications will run on Kubernetes. The use of IaC allows for faster, repeatable deployments, but its usage also increases the burden on developers to secure not only their code, but the infrastructure configuration, in addition to code dependencies and containers.

In this survey, Snyk sought to take stock of how IaC is being deployed by companies both large and small. Feedback from a wide range of roles in these companies went into our outlook on the state of IaC, highlighting the value of IaC, as well as also roadblocks to its widespread use and what we can do to overcome them.

While our survey shows that many organizations have not coalesced on one “right” way to use IaC or who should be responsible for writing and maintaining it, we did find that respondents who are taking advantage of automated security testing for their IaC definitions are finding and fixing misconfigurations faster than their peers. The high performers in our survey are finding and fixing issues in their IaC definitions within a single day; whereas the lower performers take more than a week to realize there is a security issue and then then up to 2 more days to fix it.

**KEY TAKE AWAY**
Respondents performing automated security testing as part of their release pipelines were faster to find and fix vulnerabilities.

![Chart showing that 76% of teams with fully automated security checks can fix an issue in under 1 day, compared to 59% of teams with no or partially automated security checks, and 38% of teams that only check security after deployment.](Image description)

SEE SNYK IAC IN ACTION

---

# Current IaC Practices

The benefits to speed and reliability when everything is in code and automated can be immense. But the benefits do come with a cost, namely an increasing burden on developers to secure not just their own code but it’s dependencies, containers, and now, the infrastructure configuration. To start our research, we first explored what companies were taking on the challenge of implementing IaC and which tools they’re currently using as they develop best practices.

We found that many companies are only starting out on their IaC journey, with 63% just beginning to explore the technology and only 7% stating they’ve implemented IaC to the best of current industry capabilities. While there are many tools either in use or being considered, 71% would prefer to standardize on a common toolset / workflow across all IaC configuration types and formats.

![Chart showing the percentage of companies using or considering various IaC tools. AWS CloudFormation is in use by 36% and being considered by 26%. Azure Resource Manager is in use by 30% and being considered by 24%. Kubernetes (incl. YAML, JSON and Helm) is in use by 25% and being considered by 22%. Ansible is in use by 17% and being considered by 18%. Terraform is in use by 14% and being considered by 18%. Docker Compose is in use by 14% and being considered by 16%. Google Cloud Deployment Manager is in use by 14% and being considered by 14%. Other Kubernetes tools are being considered by 14%. Serverless Framework is being considered by 14%.](Image description)

The opportunity is still wide open for most organizations to lay a firm foundation and implement the right tools and practices before widely adopting IaC.

---

We looked at how three different clusters of respondents to our survey fared when it comes to finding and fixing configuration issues that arise from using infrastructure as code:

*   **Full automation**: These respondents said they always performed automated security testing as part of their release pipelines.
*   **Less than full automation**: This cluster includes respondents who have no automation up to those who have partial automation of security checks.
*   **Only post-deployment checks**: This cluster may use some automation, but they only perform checks after infrastructure is deployed, either via audit tools, pen testing, or investigating security incidents.

It may come as no surprise that the fully automated group outperformed both of the other groups at both discovering and fixing issues. When it comes to finding issues, the high performers were able to discover issues in less than a day roughly twice as often as respondents in the other two groups. And the fully automated cluster was able to fix issues quickly, in less than half a day, over 60% more often than either of the other clusters.

There were differences at the other end of the responses, too. The two lower performing clusters took 1 week or more to discover IaC issues in over half their cases, where the fully automated cluster only took that long 30% of the time. Fixing the issues was where the cluster that only runs post-deployment checks really suffered. They were only able to fix these IaC issues in less than a day half as often as the fully automated respondents, and in 62% of the cases it took longer than a day to implement the fix.

![Chart showing the results of the survey for different automation levels. For "Can you detect an issue in less than 1 day?", 76% of Fully automated, 59% of Not automated, and 38% of Checks after deployment responded yes. For "Can you fix an issue in less than 1 day?", 76% of Fully automated, 59% of Not automated, and 38% of Checks after deployment responded yes. For "How often do you go 1 week or longer before finding an issue?", 30% of Fully automated, 54% of Not automated, and 60% of Checks after deployment responded yes. For "How often does it take you over a day to fix an issue?", 25% of Fully automated, 41% of Not automated, and 62% of Checks after deployment responded yes.](Image description)

---

# Does Speed Equate to Safety?

Currently, modern applications deploy automatically on infrastructure created and configured via code. As a result, security so often takes a back seat to a speedy deployment, meaning configuration issues are not uncovered until after these applications have been deployed. Even Gartner* states, “By 2025, 70% of attacks against containers will be from known vulnerabilities and misconfigurations that could have been remediated.”

Yet, all this does not necessarily mean speed is inherently risky when it comes to IaC. In fact, the automated testing and release gates that are in place for other forms of code can be used with IaC and help make security best practices part of the development and release process. The highest performers in this survey - those who are both finding and fixing configuration issues fastest - are already doing exactly that.

*Gartner Magic Quadrant for Application Security Testing; April 2020

![Chart showing survey responses to "Do you include IaC security tests in your CI pipeline?". 24% responded Always, 40% No CI testing, 7% Sometimes, and 27% Usually.](Image description)

---

# Current IaC Security Practices

While the highest performers are finding and fixing security issues as part of their release pipelines, this type of automated testing is still nascent when it comes to security testing. Of those surveyed, 60% said their current workflow for IaC and configuration code does go through continuous integration (CI) testing, but security checks are not always part of those tests. Only 32% of respondents include security checks in their pipelines. In fact, most security issues are still being discovered after deployment, through pen testing, audits, and investigating security incidents. For those who are only using these post-deployment checks, it takes a week or more to discover a security issue in half the cases and over a day to fix those issues in nearly 2/3 of the cases. All in all, that’s potentially 9 days of running with a security vulnerability versus less than one day for the highest performers.

![Chart showing how respondents find out about security issues in their configurations and IaC. 45% Audit running environments after deployment, 43% Pen testing, 35% Manual code scans, 33% From investigating incidents, 32% Automated testing/CI, and 21% Tools from our IaC or public cloud provider.](Image description)

---

# So what is standing in the way of making a change?

For those who said their IaC and configuration code goes through CI testing, the biggest barrier to integrating security checks is a lack of standardized best practices on what to check, with each of their separate teams making their own decision about what to test. When you couple that with the 41% who said their barrier was unclear benchmarks for security, the shortest path to improved IaC security can be paved with better tools that offer clearer guidance, while still providing teams with the freedom to determine what’s most important for their needs.

![Chart showing barriers to integrating security checks into IaC testing. 62% said Each team makes their own decisions about what to test, 41% said We do not have a clear set of benchmarks on what to test against, 22% said We do not have the right testing tools, 22% said We have not decided what is important for us to test, 16% said Concerned it would slow us down too much, and 11% said There is no clear owner to address issues that are discovered.](Image description)

---

# Infrastructure Remediation

Finding the issue is just one piece of the puzzle - once an issue is discovered somebody has to fix it. When faced with a choice, 52% of respondents claim they usually remediate a security issue by directly tweaking the infrastructure instead of addressing it by modifying the IaC source code. This opens up the possibility for a number of issues in the long-term because the infrastructure and the codified definitions used to create it will start to drift; either that or the modified infrastructure will be reset to its misconfigured state on the next deployment. For those that choose this manual remediation path, their reasoning is split between a lack of standardization, knowledge, and communication, along with a desire to speed up the fixes as much as possible.

![Chart showing how often respondents directly modify infrastructure rather than fixing the configuration in their IaC code. 13% Never - we always fix the code first, 34% Often, 18% Most of the time - we usually change the infrastructure directly instead of modifying the source code, and 35% Rarely.](Image description)

![Chart showing why respondents directly modify infrastructure instead of fixing the code. 39% Lack of standardized workflow and practices, 38% Concerned that redeploying from code will create new issues, 38% Faster/easier to tweak the infrastructure, 23% Tracing infrastructure issues back to code is complex/slow, 23% Lack of communication between developers and operators, 22% Lack of security knowledge in the team responsible for the code, and 9% No automated tests to ensure the IaC changes work before.](Image description)

---

While a lack of standardized workflow and practices was the leading reason respondents chose to remediate a security issue manually, a total of 61% of respondents also pointed to speed-related issues. Namely that it’s faster and/or easier to tweak the infrastructure because tracking issues back to the IaC definitions is too complex and/or slow. Again, this points to two underlying issues:

First, when security checks are only performed after infrastructure has been deployed, it’s too late in the process. It separates the security checks from the code and it’s likely that pen test reports and audit tools don’t provide data that’s directly actionable by the owners of the IaC code.

Second, for teams that are stretched thin, a lack of bandwidth could lead to the decision (consciously or not) to overlook some security in favor of speed. For those teams that are at their limit, the right tools can make a world of difference to equip developers with what they need to prioritize security. But before a tool can be decided on, teams must first determine who holds final responsibility for IaC.

---

# Who Holds Responsibility for IaC Security?

One of the barriers to shifting IaC security left was that teams struggled to standardize practices across their organization, leaving each team to audit IaC as they see fit. In addition to the obvious security issues this presents, it speaks to a larger disconnect on responsibility. A common theme of this survey is the difficulty to pin down security ownership when it comes to IaC - so where does the industry currently stand?

Today it seems there is no consensus on who is responsible for the security within IaC. Developers and DevOps roles have a slightly bigger role than other individual teams and a good number say it’s a shared responsibility, potentially fitting in to the newer DevSecOps models. When asked which team should be responsible for IaC security, if it is not a shared responsibility, the answers shifted heavily to the developers / DevOps groups.

So what’s stopping these security responsibilities from shifting further left? Mostly, it’s confidence in the broader organization’s ability to readily spot and fix issues in the code.

![Chart showing who is responsible for configuration security in IaC today. 29% Developers/DevOps, 28% It is a shared responsibility, 23% Security, and 20% Infrastructure.](Image description)

![Chart showing who should be responsible for IaC security. 52% Developers/DevOps, 24% Infrastructure, and 24% Security.](Image description)

---

# Snyk Infrastructure as Code: Find and fix configuration security issues the way cloud native experts do.

A clear and scalable solution to IaC security challenges is to invest in the tools and training needed to drive up confidence and help with bandwidth for these teams, allowing them to deploy code quickly and securely. In the same report cited above, Gartner also sees the potential for these automated tools and predicts that, by 2025, organizations will speed up their remediation of coding vulnerabilities by 30% with code suggestions applied from automated solutions, reducing time spent fixing bugs by 50%.

![Chart showing how confident respondents are in their ability to spot configuration issues in IaC. 4% Greatly confident, 22% Fairly confident, 25% Somewhat confident, and 49% Not confident.](Image description)

Snyk’s long-standing developer-first approach led to the creation of Snyk Infrastructure as Code (Snyk IaC) to help solve these problems. This latest tool moves the security controls for infrastructure and configurations to the beginning of the development lifecycle, so developers can proactively determine whether their application and infrastructure specifications are safe. Designed to fit a developer’s workflow, Snyk IaC helps pinpoint how to write secure Kubernetes and Terraform configurations, and even provides automated fixes as code in your choice of source code management systems.

Together with Snyk Container and Snyk Open Source, you can finally embed your security expertise across your entire development organization.

To secure your organization and learn more about Synk IaC visit snyk.io/product/infrastructure-as-code-security/.

![Chart showing what would make respondents more confident in their organization’s ability to spot IaC misconfigurations. 67% Professional training, 48% Automated code testing for IaC in CI/CD, 42% Audit tools specific to IaC and configuration, 37% Playbooks to follow, 29% Tools built-in to IDEs, 26% Peer mentoring, and 22% Industry or infrastructure vendor benchmarks.](Image description)

---

# Survey Methodology

This vendor neutral research was independently conducted by Virtual Intelligence Briefing (ViB). ViB is an interactive on-line community focused on emerging through rapid growth stage technologies. ViB’s community is comprised of more than 2.2M IT practitioners and decision makers who share their opinions by engaging in sophisticated surveys across multiple IT domains.

The survey methodology incorporated extensive quality control mechanisms at 3 levels: targeting, in-survey behavior, and post-survey analysis. The Calculated Margin of error at a 95% confidence level is 3.9%.

After receiving 543 responses from members of our opted-in 2M+ IT community, we screened out about 120 respondents who met the role, level and company size requirements, but who indicated they were not currently using, or considering using, the IaC / Configuration tools listed in the survey. This extensive process led to a survey pool of 481 qualified individuals in order to present the most accurate look at the current state of IaC.

![Chart showing survey respondents by role. 11% Cloud & Platform, 30% Developers and DecOps, 31% Infrastructure, 12% Architects, and 16% Security & Compliance.](Image description)

![Chart showing survey respondents by company size. 28% 1 - 500 employees, 23% 500 - 1000, 15% 2000 - 5000, 14% 1000 - 2000, 8% 5000 - 10,000, 8% 15,000+, and 4% 10,000 - 15,000.](Image description)

---

SEE SNYK IAC IN ACTION