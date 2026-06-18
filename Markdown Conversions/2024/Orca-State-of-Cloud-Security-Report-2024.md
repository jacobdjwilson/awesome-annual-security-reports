# 2024 State of Cloud Security Report

Uncovering what is lurking in the depths of cloud environments

©2024 Orca Security. All rights reserved.

## Table of Contents
- [Foreword](#foreword)
- [About the Orca Research Pod](#about-the-orca-research-pod)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [1. Neglected Assets](#1-neglected-assets)
- [2. Data Exposure](#2-data-exposure)
- [3. Vulnerabilities](#3-vulnerabilities)
- [4. Identity and Access](#4-identity-and-access)
- [5. Malware](#5-malware)
- [6. CI/CD Security](#6-ci-cd-security)
- [7. Cloud Security By Industry](#7-cloud-security-by-industry)
- [Key Recommendations](#key-recommendations)
- [About Orca Security](#about-orca-security)

---

## Foreword
The past year has been impacted by a challenging economic climate and shrinking budgets, putting cybersecurity defenders on the back foot. At the same time, attackers are becoming increasingly sophisticated - finding new attack vectors and leveraging AI to generate malware and automate attacks. Ransomware attacks in particular, reached record numbers in 2023.

In the world of cloud security, the increasing adoption of cloud services and cloud-native technologies is heightening both the possibilities and risks. With most organizations now using three or more cloud service providers, cloud environments have become more complex than ever before.

Despite these challenges, we believe that when security teams are focused on their most critical risks and are equipped to remediate these quickly, they can stay one step ahead of their attackers. We hope that this report prepared by the Orca Research Pod will be a valuable resource to help organizations do just that.

**Gil Geron**
CEO and Co-Founder of Orca Security

---

## About the Orca Research Pod
The Orca Research Pod is a group of cloud security researchers that discover and analyze cloud risks and vulnerabilities to strengthen the Orca Cloud Security Platform and promote cloud security best practices.

### Research Methodology
This report was compiled by analyzing data captured from billions of cloud assets on AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud scanned by the Orca Cloud Security Platform.

**Report Data Set:**
- Cloud workload and configuration data
- Billions of real-world production cloud assets
- Data referenced in this report was collected in 2023
- AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud environments

![List of 25+ vulnerabilities discovered by the Orca Research Pod across AWS, Azure, and Google Cloud from 2022-2024]

---

## Executive Summary
Leveraging unique insights into current and emerging cloud risks captured from the Orca Cloud Security Platform, this report reveals the most commonly found, yet dangerous, cloud security risks. Summarizing the results from our research, these are our main findings:

- **Basic security practices still lacking**: We are still seeing many risks that stem from not following foundational cybersecurity principles, and changing this remains pivotal to strengthening cloud security postures.
- **Many risks found on exposed and public assets**: Worryingly, several of the risks are related to cloud assets in which security should be prioritized the most - those that are exposed and public facing, especially when they store sensitive data, or provide a path to sensitive data through lateral movement.
- **Some improvement in overall cloud security postures**: More encouraging however, is that we found some reduced risk numbers compared to our previous 2022 report, with many fewer Log4Shell-vulnerable assets and a 1-5% improvement in security postures across industries.

> The report underscores a further need to cover the basics and for context-driven risk prioritization so the most critical issues are fixed first.

---

## Key Findings
- **81%** of organizations have public-facing neglected assets with open ports.
- **21%** of organizations have at least one public-facing storage bucket with sensitive data.
- **61%** of organizations have a root user or account owner without MFA.
- **82%** of organizations have a Kubernetes API server that is publicly accessible.
- **59%** of organizations still have at least one asset vulnerable to Log4Shell.
- **62%** of organizations have severe vulnerabilities in code repositories.
- **82%** of AWS SageMaker users have a notebook exposed to the internet.
- **1-5%** improvement in industry cloud security scores.

---

## 1. Neglected Assets

### 1.1 The Threat of Exposed Neglected Assets
A neglected asset is a cloud asset that uses an unsupported operating system or has remained unpatched for 180 days or more. When neglected assets are public-facing, the risk of exploitation escalates. Attackers routinely scan for open ports (80, 443, 8080, 22, 3389, or 5900) and known vulnerabilities.

### 1.2 Subdomain Takeover Risk
23% of organizations are at risk of subdomain takeover. This occurs when a subdomain’s CNAME record points to a non-existent cloud service, allowing a bad actor to serve malicious content.

---

## 2. Data Exposure

### 2.1 Exposed Sensitive Data
21% of organizations have at least one public-facing bucket containing sensitive data, and 20% have a public-facing database with sensitive data.

### 2.2 Public Write Permissions
5% of organizations have an Amazon S3 bucket with public ‘Write’ access, allowing attackers to add, delete, or replace objects.

### 2.3 Threat on Data in AI Models
82% of Amazon SageMaker users have at least one notebook exposed to the internet, risking the theft of proprietary algorithms or remote code execution (RCE).

### 2.4 Exposed Kubernetes API Servers
82% of organizations have a publicly-accessible Kubernetes API server. This is a 12% increase from our 2022 report.

---

## 3. Vulnerabilities

### 3.1 Two Decades of Vulnerabilities
91% of organizations have at least one vulnerability older than 10 years. 46% have a vulnerability 20+ years old. The oldest vulnerability found dates back to 2001.

### 3.2 Log4Shell is still a problem
59% of organizations still have at least one asset vulnerable to Log4Shell. 38% of organizations have a Log4Shell vulnerable asset that is public-facing.

---

## 4. Identity and Access

### 4.1 Weak Authentication on Public-facing Assets
24% of organizations have at least one public-facing workload with a weak or leaked password.

### 4.2 Unused IAM Users and Roles
82% of organizations have IAM user credentials that haven’t been used for 90+ days. 72% of organizations have unused IAM roles.

### 4.3 Root Risks: Highlighting the MFA Gap
61% of organizations don't apply MFA on their Root/Account Owner user.

### 4.4 Lateral Movement Exposure
90% of organizations have at least one asset that enables lateral movement. 72% of organizations have public-facing assets at risk for lateral movement.

---

## 5. Malware
87% of cloud malware attacks are via known Trojans. Malware is found in virtual machines, storage buckets, and containers, underscoring the need for vigilant security measures.

---

## 6. CI/CD Security
62% of organizations have severe vulnerabilities (CVSS > 7) in code repositories. 70% of organizations have unencrypted secrets in code repositories.

---

## 7. Cloud Security By Industry
All industry averages improved by 1-5% in 2023. Financial services and healthcare providers scored the strongest. Public Sector & Education improved by 5.2%.

---

## Key Recommendations
- **Patch strategically**: Understand cloud risk context to prioritize patching.
- **Don’t neglect workloads**: Maintain an updated cloud asset inventory and eliminate unsupported workloads.
- **Maintain Principle of Least Privilege (PoLP)**: Give users only the minimum level of access needed.
- **Maintain IAM hygiene**: Monitor and deactivate unused identities and access keys.
- **Implement strong user authentication**: Always implement MFA and use strong, unique passwords.
- **Know where your crown jewels are**: Identify and protect sensitive data and critical business assets.
- **Monitor, mitigate web and API risks**: Audit configurations to prevent mismanagement.
- **Leverage Automated malware detection**: Use heuristic scanning to detect unknown malware.
- **IaC Regular audits and continuous monitoring**: Use declarative Infrastructure as Code to avoid misconfigurations.
- **Backup often and regularly**: Reduce ransomware impact by allowing system restoration.

---

## About Orca Security
Orca’s agentless-first Cloud Security Platform connects to your environment in minutes and provides 100% visibility of all your assets on AWS, Azure, Google Cloud, Kubernetes, and more. Orca detects, prioritizes, and helps remediate cloud risks across every layer of your cloud estate.

To find out more, schedule a personalized demo of the Orca platform.