# 2022 State of Public Cloud Security Report

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [About the Orca Research Pod](#about-the-orca-research-pod)
- [Key Findings](#key-findings)
- [1. Your Castle in the Cloud](#1-your-castle-in-the-cloud)
- [2. Upkeep and Maintenance](#2-upkeep-and-maintenance)
- [3. Castle Hygiene](#3-castle-hygiene)
- [4. Construction Mistakes](#4-construction-mistakes)
- [5. Keys to the Kingdom](#5-keys-to-the-kingdom)
- [6. Past the Gates](#6-past-the-gates)
- [7. Protecting the Crown Jewels](#7-protecting-the-crown-jewels)
- [8. Attack Paths](#8-attack-paths)
- [9. The Cloud Chess Pieces](#9-the-cloud-chess-pieces)
- [10. Key Recommendations](#10-key-recommendations)
- [About Orca Security](#about-orca-security)

---

## Foreword
In the past year, organizations have had to deal with many cybersecurity challenges. Critical and ubiquitous vulnerabilities such as Log4Shell, and to a lesser extent Spring4Shell, had security teams working around the clock. In addition to all this, teams are dealing with tremendous global unrest, heightening the chance of cyberattacks on organizations.

The Orca Research Pod has been diligently investigating cloud products and services to find unknown, zero-day vulnerabilities before malicious actors do. So far this year, Orca has announced five major vulnerabilities in Azure and AWS, and worked with cloud and service providers to resolve them.

Leveraging the Orca Research Pod’s unique insights into current and emerging cloud risks captured from the Orca platform, we are releasing this annual report to help organizations reduce attack surfaces and strengthen their cloud security postures.

We hope that the report will prove to be a useful resource for CISOs, cloud security practitioners, DevOps, DevSecOps, and development leaders alike and will ultimately contribute to making the cloud a safer place for all organizations.

**Avi Shua**
CEO and Co-Founder of Orca Security

---

## Executive Summary
The cloud adoption trend is predicted to continue with great strides. Gartner predicts that worldwide spending on public cloud services will grow 20.4% in 2022 to total $494.7 billion and expects it to reach nearly $600 billion in 2023[^1].

All roads lead to the cloud. That is true now more than ever before. The significant advantages that the cloud brings, including increased agility, scalability, and reliability was already driving organizations towards cloud adoption. However, the global pandemic greatly accelerated this trend, with the sudden and massive move to remote work and the ensuing need to provide employees with access to business systems literally from anywhere.

However, it is important to recognize that cloud adoption comes with new security challenges. Even though the cloud platform provider is responsible for securing the infrastructure, organizations are still responsible for securing the applications and services they run in the cloud. Simply deploying on-premises security solutions in the cloud may seem like an easy solution at first, but will soon come up short as organizations start to deploy more cloud-native applications and security teams struggle to keep up.

This report assesses the different areas of public cloud security and sheds light on their current security state to help organizations better understand where their most critical security gaps are. The report further provides recommendations on what actions need to be taken to achieve the biggest improvements in cloud security postures.

[^1]: Gartner Forecast: Public Cloud Services, Worldwide, 2020-2026, 1Q22 Update

---

## About the Orca Research Pod
The Orca Research Pod is a group of 12 cloud security researchers with a combined experience of 79 years in cybersecurity. Our expert team discovers and analyzes cloud risks and vulnerabilities to strengthen the Orca Cloud Security Platform and promote cloud security best practices. In addition, the Orca research team discovers and helps resolve vulnerabilities in cloud provider platforms so organizations can rely on a safe infrastructure in the cloud.

![Table showing 5 critical vulnerabilities discovered in Azure and AWS, including AutoWarp, SynLapse, Superglue, and BreakingFormation, with their respective severity levels and time to remediation.]

The Orca Research Pod compiled this report by analyzing data captured from billions of cloud assets on AWS, Azure and Google Cloud scanned by the Orca Cloud Security Platform.

**Report Data Set:**
- Cloud workload and configuration data
- Billions of real-world production cloud assets
- AWS, Azure and Google Cloud environments
- Collected between January 1st - July 1st, 2022

---

## Key Findings
This year’s study shows that while many organizations list cloud security as one of their top IT priorities, there are still many basic security practices that are not being followed.

- **36%** of organizations have unencrypted sensitive data such as secrets and PII on their cloud assets.
- **78%** of identified attack paths use known vulnerabilities (CVEs) as an initial access attack vector.
- **7%** of organizations have neglected assets with open ports.
- **The average attack path only needs 3 steps** of organizations have a cloud provider root account without multi-factor authentication.
- **72%** have at least one S3 Bucket that allows public READ access.
- **12%** have an Internet-facing workload with at least one weak or leaked password.
- **70%** have a Kubernetes API server that is publicly accessible.
- **58%** have a serverless AWS Lambda function or Google Cloud function with unsupported runtimes.
- **18 days** on average for organizations to fix an ‘imminent compromise’ security alert.

---

## 1. Your Castle in the Cloud
Your cloud environment is a bit like a ‘hosted castle’ in the cloud. Following the shared responsibility model, the cloud platform provider gives you a plot of land to build on and surrounds it with a moat. However, you need to make sure your castle is impregnable by securing it with thick walls, a drawbridge, turrets, and a copious collection of guards.

![Diagram showing the Shared Responsibility Model for IaaS, PaaS, and Serverless, illustrating the division of responsibilities between the customer and the cloud provider regarding applications, databases, OS, virtualization, servers, storage, networking, and data centers.]

---

## 2. Upkeep and Maintenance
An important part of keeping your ‘castle’ secure is to regularly patch, upgrade and maintain your cloud environment.

### 2.1 Vulnerabilities
With the sheer number of vulnerabilities being discovered every day, it is difficult for organizations to keep up. Many fall behind on patching newly discovered vulnerabilities, but some are also not addressing vulnerabilities that have been around for a long time.
- We found that **10%** of organizations have vulnerabilities that were disclosed 10+ years ago.
- On average, we found that Compute assets (VMs, containers and their images) have no less than **50** known vulnerabilities (CVEs) in one year.

### 2.2 Log4Shell
In December 2021, the cybersecurity world was rocked by the discovery of a serious zero-day vulnerability in Apache Log4j.
- Almost **5%** of workload assets still have at least one of the Log4j vulnerabilities[^2] of which 10.5% are internet-facing.
- **30%** of the Log4j vulnerabilities discovered between December 2021 - January 2022 remain unresolved.
- The vast majority (68%) of the Log4j vulnerabilities are found on VMs.

[^2]: When we mention Log4j vulnerabilities, we are referring to the following CVEs: CVE-2021-44228, CVE-2021-4104, CVE-2021-45046, and CVE-2021-45105.

### 2.3 Neglected Assets
A neglected asset is a cloud asset that uses an unsupported operating system or has remained unpatched for 180 days or more.
- On average, organizations have **11%** of their assets in a neglected security state.
- **19%** of identified attack paths use neglected assets as an initial access attack vector.
- **7%** have Internet facing neglected assets with open ports (80, 443, 8080, 22, 3389 or 5900).

---

## 3. Castle Hygiene
By adhering to cloud hygiene best practices and applying these consistently across the board, the chance of a damaging cloud breach is significantly reduced.

### 3.1 Unused Credentials
Out of all scanned organizations with AWS environments, **76%** had credentials that had not been used for 90+ days.

### 3.2 Multi-Factor Authentication (MFA)
- **33%** have an AWS cloud provider root account without MFA.
- **58%** have MFA disabled for at least one privileged user in Azure.

### 3.3 Principle of Least Privilege (PoLP)
- **44%** of environments have at least one privileged identity access management (IAM) role.
- **71%** use the default service account in Google Cloud.
- **42%** of the scanned cloud estates granted administrative permissions to more than 50% of the organization’s users.

### 3.4 Remediation Time
On average, organizations take **18 days** to fix an ‘imminent compromise’ alert.

---

## 4. Construction Mistakes
Gartner predicts that through 2025, more than 99% of cloud breaches will originate from preventable misconfigurations or mistakes by end users[^3].

### 4.1 AWS KMS Key Misconfigurations
- **8%** have configured a KMS key with public access policy.
- **99%** use at least one default KMS key.
- **80%** have KMS rotation disabled.

### 4.2 Policy and Access Misconfigurations
- **80%** have a user with an inline policy and **49%** have a group with an inline policy.
- **79%** have at least one access key older than 90 days.

### 4.3 Database Misconfigurations
- **75%** have AWS Multi-AZ disabled.
- **77%** have at least one RDS database instance using default ports.

[^3]: Gartner 2021 Hype Cycle for Cloud Security

---

## 5. Keys to the Kingdom
The keys to the cloud kingdom are found in so-called ‘secrets’ that are used to authenticate and access systems.
- **56%** on AWS, **11%** on Azure, and **55%** on GCP have sensitive keys on their system.
- **43%** have at least one clear-text password in the shell history of an Internet-facing Linux workload.
- **21%** have at least one Internet-facing workload with a non-corporate authentication key.

---

## 6. Past the Gates
Lateral movement is a technique that attackers use to move from one asset to another to reach their end target.
- **75%** of organizations have at least one asset that enables lateral movement to another asset.

---

## 7. Protecting the Crown Jewels
A company’s crown jewels are its most valuable assets, such as PII, customer databases, and intellectual property.
- **36%** of organizations have unencrypted sensitive data such as secrets and PII.
- **35%** have at least one Internet facing workload with sensitive information in a Git Repository.

---

## 8. Attack Paths
The average attack path only needs 3 steps to reach crown jewels.
- **8.1 Steps in the attack path**: Attackers take advantage of weaknesses in the environment to gain access to specific assets and move laterally.
- **8.2 Top initial attack vectors**: The vast majority of attacks start by exploiting a vulnerability.
- **8.3 Top end targets and goals**: The top goal of an attack path is data exposure of sensitive information.

---

## 9. The Cloud Chess Pieces
### 9.1 Storage
- **72%** of AWS environments have at least one S3 Bucket that allows public READ access.
- **42%** of organizations using Azure have at least one public blob container.

### 9.2 Databases
- **60%** are not encrypting database instance snapshots.
- **67%** only require a password and username for database access without using IAM authentication.

### 9.3 VMs
- **71%** of Google Cloud environments have at least one Internet facing EC2 Instance that has full Access to S3.
- **23%** have at least one EC2 Instance with Administrator Privileges.

### 9.4 Containers
- **71%** of the containers are in a neglected state.
- **84%** have at least one container with the critical Open SSL infinite loop DoS vulnerability.

### 9.5 Kubernetes
- **70%** have a Kubernetes API server that is publicly accessible.
- **30%** have a controller of pods with a role that allows the creation or modification of other pods.

### 9.6 Serverless
- **69%** have at least one serverless function exposing secrets in the environment variable.
- **58%** have an AWS Lambda function or Google Cloud function with unsupported runtimes.

---

## 10. Key Recommendations
1. **Identify your crown jewels**: Determine which assets are business-critical.
2. **Maintain a cloud asset inventory**: You can only patch a vulnerability if you know it exists.
3. **Patch, patch, patch**: Prioritize vulnerabilities that endanger crown jewels.
4. **Adhere to the Principle of Least Privilege**: Limit access rights to only what is strictly required.
5. **Encrypt sensitive data and keys**: Limit the impact of potential exposure.
6. **Apply MFA and strong password management**: Implement MFA and rotate passwords frequently.
7. **Secure templates and images**: Check IaC templates and container images for misconfigurations.
8. **Eliminate unused assets**: Delete users, files, or systems no longer in use.
9. **Perform regular audits**: Conduct configuration audits at least twice a year.
10. **Perform backups**: Regularly backup critical data and store offline.
11. **Utilize checklists**: Use checklists to minimize human error during configuration.

---

## About Orca Security
Orca Security is the industry-leading agentless Cloud Security Platform that identifies, prioritizes, and remediates risks and compliance issues across your cloud estate spanning AWS, Azure, Google Cloud and Kubernetes.

Instead of layering multiple siloed tools together or deploying cumbersome agents, Orca delivers complete cloud security in a single platform by combining two revolutionary approaches: SideScanning, which enables frictionless and complete coverage without the need to maintain agents, and a Unified Data Model, which allows for centralized contextual analysis of your entire cloud estate.

For more information: [https://orca.security](https://orca.security)

**Take Risk Assessment**
Would you like to find out how many of these risks are in your environment? Take our free, no obligation risk assessment to find out.