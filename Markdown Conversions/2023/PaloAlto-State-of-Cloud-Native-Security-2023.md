# The State of Cloud-Native Security 2023 Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Introduction](#introduction)
- [How Enterprises Are Migrating to the Cloud](#how-enterprises-are-migrating-to-the-cloud)
- [Application Velocity in Cloud-Native Enterprises](#application-velocity-in-cloud-native-enterprises)
- [Cloud Complexity](#cloud-complexity)
- [Implications for Security Teams](#implications-for-security-teams)
- [How Enterprises Are Approaching Security](#how-enterprises-are-approaching-security)
- [How Application Developers Are Shaping Security](#how-application-developers-are-shaping-security)
- [The Path Forward](#the-path-forward)
- [Recommendations](#recommendations)

---

## Executive Summary

Few can relate to the adage "the only constant is change" like cloud security professionals. Cloud security is dynamic and unpredictable, but the move to hybrid work has accelerated change and increased the complexity of application security. As cloud-native application development evolves, so too do organizations’ cloud infrastructure (80% of survey respondents say their cloud infrastructure is evolving). 

More than 75% of respondents from this year’s survey are deploying new or updated code to production weekly, and almost 40% are committing new code daily. Add to that the ratio of ten developers for every security professional[^1][^2] and the potential for challenges in scale and complexity are not difficult to understand.

In contrast to on-prem environments, cloud computing follows a shared responsibility model. Responsibility for the infrastructure (e.g., compute, networking, and storage) is held with the cloud service provider (CSP) and responsibility for security is shared between the CSP and their customers. But the sharing stops when it comes to responsibility for customers’ applications, data, and access management.

[^1]: Occupational Outlook Handbook - Software Developers, Quality Assurance Analysts, and Testers, Bureau of Labor Statistics
[^2]: Bureau of Labor Statistics, Occupational Outlook Handbook - Information Security Analysts, Bureau of Labor Statistics

## Key Findings

### Shift-left security is accelerating
Since unaddressed vulnerabilities can be exploited in production, it’s critical to catch and fix these vulnerabilities early in the application development lifecycle. Our survey revealed that risks introduced early in application development are the #1 concern.

### Decisions on tooling have become clouded by complexity
Overwhelmed by the proliferation of discrete tooling options, more than 75% of respondents reported that their organization struggles to identify which security tools can help them meet their needs.

### Collaboration across teams is essential to better security outcomes
Unlike traditional security, the cloud requires users to unite disparate teams around a common goal. Our survey shows 81% of enterprises have embedded security professionals in their development and operations team.

## Introduction

The third annual State of Cloud-Native Security Report examines the evolving security practices, tools, and technologies that organizations around the world are employing to take advantage of cloud services and new application tech stacks.

Fielded from November 21 to December 14, 2022, the survey gathered data from 2,500-plus respondents in seven countries. All major industries were included, and more than 50% of the sample came from enterprise-sized organizations (over $1B in annual revenue).

## How Enterprises Are Migrating to the Cloud

Similar to years past, organizations in 2023 have shifted toward more public hosting of their cloud workloads. Fifty-three percent of cloud workloads are hosted on public clouds, an increase of 8% in the past year.

![Chart showing workload distribution by architecture type: PaaS & Serverless (36%), VMs (22%), CaaS (18%), Containers (18%)]

![Chart showing percentage of cloud workloads publicly hosted by region: NAM (54%), APJ (53%), EMEA (50%)]

## Application Velocity in Cloud-Native Enterprises

Two-thirds of all enterprises say that deployment frequency has increased or significantly increased over the past year, and 38% of enterprises deploy code to production or release to end users every day.

![Chart showing frequency of deployment: On Demand (17%), Daily (38%), Weekly (77%)]

## Cloud Complexity

Over-tooling leads to an overly complex cloud environment. On average, organizations rely on 30+ tools for overall security and six to ten tools dedicated to cloud security. 

- 77% of organizations struggle to identify what security tools are necessary to achieve their objectives.
- 76% of respondents say the number of cloud security tools they use create blind spots.

## Implications for Security Teams

As vulnerabilities and misconfigurations move upstream, new application-level risks are emerging. 90% of respondents say their organization cannot detect, contain, and resolve threats within an hour.

**Top 5 Security Incidents:**
1. Risk introduced early in application development
2. Workload images with vulnerabilities or malware
3. Vulnerable web applications and APIs
4. Unrestricted network access between workloads
5. Downtime due to misconfiguration

## How Enterprises Are Approaching Security

Best-in-breed security capabilities and ease of use rose to the top as the most important factors when choosing security solutions. Enterprises are split between a single security vendor/tool approach and a multiple security vendor/tool approach.

![Table showing primary source of security for Cloud, Network, and Application security across categories like CSP, One Vendor, Multiple Vendors, and In-House/Open Source]

## How Application Developers Are Shaping Security

80% of respondents agreed that developers understand their security responsibilities across the development lifecycle. However, 75% of respondents reported a higher than usual turnover rate in DevOps and 73% reported a higher than usual turnover rate in cloud security roles.

## The Path Forward

Our data shows that security teams are looking for an integrated platform that provides visibility across their entire ecosystem. More than 80% of respondents said they would benefit from a centralized security solution that sits across all of their cloud accounts and services.

## Recommendations

Palo Alto Networks researchers recommend focusing on these strategic areas:

1. **Embed Security Earlier in the Application Lifecycle**: Identify the least disruptive insertion points for security in the CI/CD pipeline.
2. **Implement Continuous Cloud Visibility**: Eliminate blind spots by discovering cloud assets, misconfigurations, and vulnerabilities in near real-time.
3. **Adopt Threat Prevention Techniques**: Actively block zero-day attacks and contain lateral movement.
4. **Align Your Cybersecurity Tactics with Your Cloud Journey**: Seek solutions that meet both current and future priorities (e.g., containerization, serverless).
5. **Consider Tool Consolidation**: Unify data and security controls into a platform approach to automate correlation.

---

### About Palo Alto Networks
Palo Alto Networks is the global cybersecurity leader, shaping the cloud-centric future with technology that is transforming the way people and organizations operate. For more information, visit [www.paloaltonetworks.com](http://www.paloaltonetworks.com).

### About Prisma Cloud
Prisma® Cloud is a comprehensive cloud-native security platform with the industry’s broadest security and compliance coverage. For more information, visit [www.paloaltonetworks.com/prisma/Cloud](http://www.paloaltonetworks.com/prisma/Cloud).

![Image description: Cover art featuring team members Kathleen Qin, Ivan Melia, and Mohit Bhasin standing behind a prismatic glass partition.]