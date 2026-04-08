# Infrastructure as Code Security Insights

**Organization:** Snyk  
**Report Title:** Infrastructure-as-Code-Report  
**Year:** 2021

## Table of Contents
- [Introduction](#introduction)
- [Current IaC Practices](#current-iac-practices)
- [Does Speed Equate to Safety?](#does-speed-equate-to-safety)
- [Current IaC Security Practices](#current-iac-security-practices)
- [Infrastructure Remediation](#infrastructure-remediation)
- [Who Holds Responsibility for IaC Security?](#who-holds-responsibility-for-iac-security)
- [Snyk Infrastructure as Code](#snyk-infrastructure-as-code)
- [Survey Methodology](#survey-methodology)

---

## Introduction

Cloud native applications are more than just the code developers create - today’s applications include infrastructure as code (IaC) that dictate how the applications are setup on cloud infrastructure and how containerized applications will run on Kubernetes. The use of IaC allows for faster, repeatable deployments, but its usage also increases the burden on developers to secure not only their code, but also the infrastructure configuration, in addition to code dependencies and containers.

In this survey, Snyk sought to take stock of how IaC is being deployed by companies both large and small. Feedback from a wide range of roles in these companies went into our outlook on the state of IaC, highlighting the value of IaC, as well as also roadblocks to its widespread use and what we can do to overcome them.

While our survey shows that many organizations have not coalesced on one “right” way to use IaC or who should be responsible for writing and maintaining it, we did find that respondents who are taking advantage of automated security testing for their IaC definitions are finding and fixing misconfigurations faster than their peers. The high performers in our survey are finding and fixing issues in their IaC definitions within a single day; whereas the lower performers take more than a week to realize there is a security issue and then up to 2 more days to fix it.

> **KEY TAKE AWAY**
> Respondents performing automated security testing as part of their release pipelines were faster to find and fix vulnerabilities.

![Chart: Can you fix an issue in under 1 day? 76% for teams with fully automated security checks, 59% for teams with no or only partially automated security checks, 38% for teams that only check security after deployment.]

---

## Current IaC Practices

The benefits to speed and reliability when everything is in code and automated can be immense. But the benefits do come with a cost, namely an increasing burden on developers to secure not just their own code but it’s dependencies, containers, and now, the infrastructure configuration. To start our research, we first explored what companies were taking on the challenge of implementing IaC and which tools they’re currently using as they develop best practices.

We found that many companies are only starting out on their IaC journey, with 63% just beginning to explore the technology and only 7% stating they’ve implemented IaC to the best of current industry capabilities. While there are many tools either in use or being considered, 71% would prefer to standardize on a common toolset / workflow across all IaC configuration types and formats.

![Chart: 63% of companies are just starting out; 7% of companies are implementing the best of current industry capabilities.]

**In use today:**
- AWS CloudFormation (36%)
- Azure Resource Manager (30%)
- Cloud SDKs (AWS CDK, Azure SDKs) (25%)
- Kubernetes (incl. YAML, JSON and Helm) (17%)
- Ansible (14%)
- Terraform (14%)
- Docker Compose (14%)
- Google Cloud Deployment Manager (14%)

**Considering for the future:**
- Kubernetes (incl. YAML, JSON and Helm) (26%)
- Azure Resource Manager (24%)
- Google Cloud Deployment Manager (22%)
- Other Kubernetes tools (18%)
- Serverless Framework (18%)
- AWS CloudFormation (16%)
- Ansible (14%)

We looked at how three different clusters of respondents to our survey fared when it comes to finding and fixing configuration issues that arise from using infrastructure as code:

1. **Full automation:** These respondents said they always performed automated security testing as part of their release pipelines.
2. **Less than full automation:** This cluster includes respondents who have no automation up to those who have partial automation of security checks.
3. **Only post-deployment checks:** This cluster may use some automation, but they only perform checks after infrastructure is deployed, either via audit tools, pen testing, or investigating security incidents.

It may come as no surprise that the fully automated group outperformed both of the other groups at both discovering and fixing issues. When it comes to finding issues, the high performers were able to discover issues in less than a day roughly twice as often as respondents in the other two groups. And the fully automated cluster was able to fix issues quickly, in less than half a day, over 60% more often than either of the other clusters.

---

## Does Speed Equate to Safety?

Currently, modern applications deploy automatically on infrastructure created and configured via code. As a result, security so often takes a back seat to a speedy deployment, meaning configuration issues are not uncovered until after these applications have been deployed. Even Gartner[^1] states, “By 2025, 70% of attacks against containers will be from known vulnerabilities and misconfigurations that could have been remediated.”

Yet, all this does not necessarily mean speed is inherently risky when it comes to IaC. In fact, the automated testing and release gates that are in place for other forms of code can be used with IaC and help make security best practices part of the development and release process. The highest performers in this survey - those who are both finding and fixing configuration issues fastest - are already doing exactly that.

[^1]: Gartner Magic Quadrant for Application Security Testing; April 2020

---

## Current IaC Security Practices

While the highest performers are finding and fixing security issues as part of their release pipelines, this type of automated testing is still nascent when it comes to security testing. Of those surveyed, 60% said their current workflow for IaC and configuration code does go through continuous integration (CI) testing, but security checks are not always part of those tests. Only 32% of respondents include security checks in their pipelines.

**How do you find out about security issues in your configurations and IaC?**
- Audit running environments after deployment (45%)
- Pen testing (43%)
- Manual code scans (35%)
- From investigating incidents (33%)
- Automated testing/CI (32%)
- Tools from our IaC or public cloud provider (21%)

---

## Infrastructure Remediation

Finding the issue is just one piece of the puzzle - once an issue is discovered somebody has to fix it. When faced with a choice, 52% of respondents claim they usually remediate a security issue by directly tweaking the infrastructure instead of addressing it by modifying the IaC source code. This opens up the possibility for a number of issues in the long-term because the infrastructure and the codified definitions used to create it will start to drift.

**Why do you directly modify the infrastructure instead of fixing the code?**
- Lack of standardized workflow and practices (39%)
- Concern that redeploying from code will create new issues (38%)
- Faster/easier to tweak the infrastructure (38%)
- Tracing infrastructure issues back to code is complex/slow (23%)
- Lack of communication between developers and operators (23%)
- Lack of security knowledge in the team responsible for the code (22%)
- No automated tests to ensure the IaC changes work before (9%)

---

## Who Holds Responsibility for IaC Security?

Today it seems there is no consensus on who is responsible for the security within IaC. Developers and DevOps roles have a slightly bigger role than other individual teams and a good number say it’s a shared responsibility, potentially fitting in to the newer DevSecOps models.

**Who is responsible for configuration security in IaC today?**
- Developers/DevOps (29%)
- It is a shared responsibility (28%)
- Security (23%)
- Infrastructure (20%)

---

## Snyk Infrastructure as Code

Snyk’s long-standing developer-first approach led to the creation of Snyk Infrastructure as Code (Snyk IaC) to help solve these problems. This latest tool moves the security controls for infrastructure and configurations to the beginning of the development lifecycle, so developers can proactively determine whether their application and infrastructure specifications are safe.

**What would make you more confident in your organisation’s ability to spot IaC misconfigurations?**
- Professional training (67%)
- Automated code testing for IaC in CI/CD (48%)
- Audit tools specific to IaC and configuration (42%)
- Playbooks to follow (37%)
- Tools built-in to IDEs (29%)
- Peer mentoring (26%)
- Industry or infrastructure vendor benchmarks (22%)

---

## Survey Methodology

This vendor neutral research was independently conducted by Virtual Intelligence Briefing (ViB). The survey methodology incorporated extensive quality control mechanisms at 3 levels: targeting, in-survey behavior, and post-survey analysis. The Calculated Margin of error at a 95% confidence level is 3.9%.

After receiving 543 responses from members of our opted-in 2M+ IT community, we screened out about 120 respondents who met the role, level and company size requirements, but who indicated they were not currently using, or considering using, the IaC / Configuration tools listed in the survey. This extensive process led to a survey pool of 481 qualified individuals.

**Survey respondents by role:**
- Infrastructure (31%)
- Developers and DevOps (30%)
- Security & Compliance (16%)
- Architects (12%)
- Cloud & Platform (11%)