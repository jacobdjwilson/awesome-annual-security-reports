# 2026 State of AppSec Report

## Table of Contents
- [Foreword](#foreword)
- [About the Orca Research Pod](#about-the-orca-research-pod)
- [Executive summary](#executive-summary)
- [Key findings](#key-findings)
- [1. The Rise of Supply Chain Attacks](#1-the-rise-of-supply-chain-attacks)
  - [1.1 Major Supply Chain Attacks](#11-major-supply-chain-attacks)
- [2. Vulnerabilities in AI Packages](#2-vulnerabilities-in-ai-packages)
  - [2.1 Critical Remote Code Execution Vulnerabilities](#21-critical-remote-code-execution-vulnerabilities)
  - [2.2 Malicious Packages: Still Lurking in Production](#22-malicious-packages-still-lurking-in-production)
- [3. Container Vulnerability Landscape](#3-container-vulnerability-landscape)
  - [3.1 High/Critical Vulnerability Patching Velocity](#31-highcritical-vulnerability-patching-velocity)
- [4. Secrets Management](#4-secrets-management)
  - [4.1 The AI/ML Secrets Crisis](#41-the-aiml-secrets-crisis)
- [5. CI/CD Pipeline Security](#5-cicd-pipeline-security)
  - [5.1 CI/CD Platform Adoption](#51-cicd-platform-adoption)
  - [5.2 GitHub Actions Security](#52-github-actions-security)
- [6. Infrastructure as Code Security](#6-infrastructure-as-code-security)
  - [6.1 IaC Platform Adoption](#61-iac-platform-adoption)
  - [6.2 Storage and Data Protection](#62-storage-and-data-protection)
  - [6.3 Identity and Access Management](#63-identity-and-access-management)
  - [6.4 Network Security](#64-network-security)
  - [6.5 Container Security in IaC](#65-container-security-in-iac)
- [7. Repository and SCM Security](#7-repository-and-scm-security)
  - [7.1 Code Review and Approval Gaps](#71-code-review-and-approval-gaps)
  - [7.2 Branch Protection Weakness](#72-branch-protection-weakness)
  - [7.3 Access Control and Hygiene](#73-access-control-and-hygiene)
- [8. Key Recommendations](#8-key-recommendations)
  - [8.1 Immediate Actions (0-30 Days)](#81-immediate-actions-0-30-days)
  - [8.2 Short-term Initiatives (30-90 Days)](#82-short-term-initiatives-30-90-days)
  - [8.3 Strategic Improvements (90+ Days)](#83-strategic-improvements-90-days)
- [9. Conclusion](#9-conclusion)

---

## Foreword

As organizations accelerate software delivery through cloud-native architectures, open-source dependencies, and automated pipelines, application attack surfaces are expanding faster than security practices can keep up. AI-assisted development is further increasing this velocity, generating code, dependencies, and configurations at a pace that traditional security processes were not designed to govern.

Modern applications are built from thousands of third-party components and deployed at machine speed. This velocity enables scale and innovation, but it also makes it impossible to fix everything once code reaches production. Vulnerable dependencies, exposed secrets, and insecure configurations are no longer edge cases; they are structural realities of how software is built today. At the same time, AI systems introduce new risks and enable the rapid propagation of insecure code patterns and model dependencies across environments.

These challenges are compounded by the rise of software supply chain attacks, which have proven to be one of the most effective paths to large-scale compromise. A single poisoned dependency or workflow can cascade across thousands of organizations, turning application security failures into operational risk.

This State of Application Security Report is designed to help teams understand where these risks are introduced and how to address them effectively. Grounded in real-world findings from the Orca Research Pod, it provides a clear view into the current Application Security landscape and practical guidance for securing modern applications at the speed today’s businesses demand.

**Gil Geron**
CEO and Co-Founder of Orca Security

---

## About the Orca Research Pod

The Orca Research Pod is a group of security researchers that discover and analyze security risks and vulnerabilities to strengthen the Orca Security Platform and promote CNAPP security best practices.

### Research Methodology
This report is based on aggregated, anonymized security telemetry from more than 1,000 production organizations leveraging Orca Security’s cloud security platform.

All metrics presented represent the percentage of organizations exhibiting each finding, calculated as a weighted average across the organizations. Data was collected between Q3 2025 and Q1 2026, focusing exclusively on production environments to ensure findings reflect real-world security postures rather than test or development configurations.

Security findings span multiple domains: CI/CD pipeline security, secrets management, repository configuration, software composition analysis (SCA), static application security testing (SAST), infrastructure as code (IaC), and container security.

**Report Data Set:**
- ![Cloud workload and configuration data]
- Billions of real-world production cloud assets
- Data referenced in this report was collected from Q3 2025 to Q1 2026
- AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud environments

---

## Executive summary

Leveraging real-world telemetry from more than 1,000 production organizations, this report examines the current state of application security across the modern software delivery lifecycle. The findings reveal a growing disconnect between how applications are built today and how application security is practiced, resulting in persistent risk, stalled remediation, and widening exposure across production environments. Our main findings summary includes:

- **Application risk is widespread and routinely reaches production**: More than 78% of organizations have applications running with critical vulnerabilities. Even years after disclosure, high-impact issues like Log4Shell continue to affect nearly half of production environments, highlighting how traditional AppSec approaches struggle to keep pace with dependency sprawl.
- **Secrets exposure remains pervasive, and AI adoption is amplifying impact**: Nearly one-third of organizations expose valid, active secrets in code, while over 41% have leaked AI/ML credentials. These exposures grant direct access to proprietary models, sensitive data, and usage-based services, increasing both security and financial risk.
- **Detection is not translating into remediation**: While vulnerabilities are identified, they are rarely resolved. Over 77% of organizations still carry high or critical container vulnerabilities after 90 days, revealing that when teams can’t effectively prioritize risk, vulnerabilities aren’t remediated.
- **CI/CD Pipelines and Infrastructure-as-Code are scaling risk by default**: With 74% of organizations deploying infrastructure through code, misconfigurations are no longer isolated mistakes, they are repeatable production risks. Over 80% of IaC environments lack proper logging and monitoring, and 84% deploy unencrypted storage, embedding security gaps directly into delivery pipelines.
- **Supply chain attacks are now a routine production risk**: More than 11% of organizations have well known malicious packages in production, including dependencies publicly disclosed and removed years ago. Self-replicating attacks like the 2025 Shai-Hulud worm demonstrate how a single compromised dependency can cascade across thousands of downstream environments.

---

## Key findings

- **31%** of organizations expose valid secrets in source code repositories.
- **43%** of organizations have exposed AI or machine learning credentials.
- **78%** of organizations run applications with critical vulnerabilities.
- **80%** of organizations lack logging or monitoring in Infrastructure deployed as code.
- **77%** of organizations have high or critical container vulnerabilities unpatched after 90 days.
- **50%** of organizations remain vulnerable to Log4Shell-affected dependencies in production.
- **11%** of organizations have well known malicious packages running in production.
- **75%** of organizations manage infrastructure through code.

---

## 1. The Rise of Supply Chain Attacks

Software supply chain attacks have shifted from edge-case threats to one of the most reliable paths to large-scale compromise. By targeting shared dependencies, build systems, and automation workflows, attackers can achieve exponential impact from a single intrusion.

The SolarWinds breach in 2020 marked a turning point, demonstrating how compromising one build pipeline could grant access to 18,000+ downstream organizations. Since then, attackers have increasingly focused on package registries, CI/CD platforms, and maintainer credentials.

This evolution accelerated in 2025 with the emergence of self-replicating supply chain malware. The Shai-Hulud campaigns introduced a new class of attack that spreads autonomously by harvesting npm tokens and GitHub credentials from infected environments.

### 1.1 Major Supply Chain Attacks

| ATTACK / CAMPAIGN | TYPE | IMPACT |
| :--- | :--- | :--- |
| Shai-Hulud 2.0 (2025) | npm Self-Replicating Worm | 796+ npm packages, 20M+ weekly downloads |
| React shell (2025) | RCE Vulnerability | CVSS 10.0, 55.8M+ weekly downloads |
| tj-actions/changed-files (2025) | GitHub Actions Compromise | 23,000+ repositories |
| XZ Utils Backdoor (2024) | Maintainer Social Engineering | CVSS 10.0, multi-year operation |
| 3CX / SmoothOperator (2024) | Double Supply Chain Attack | 242,519+ IPs compromised |
| MOVEit (2023) | Zero-Day Exploitation | 600+ organizations |
| Log4Shell (2021) | Critical Library Vulnerability | CVSS 10.0, billions of devices |
| SolarWinds / SUNBURST (2020) | Build System Compromise | 18,000+ customers |

---

## 2. Vulnerabilities in AI Packages

Modern applications are built on layers of third-party code, with much of it shipping with known risk. Our research shows that vulnerable packages are not isolated findings, but pervasive across production environments.

### 2.1 Critical Remote Code Execution Vulnerabilities

Certain vulnerabilities demand immediate attention due to severity and ease of exploitation, however many evade remediation. The persistence of Log4Shell nearly four years after disclosure, still affecting 46% of organizations, underscores a broader challenge in modern AppSec.

### 2.2 Malicious Packages: Still Lurking in Production

Despite public disclosure and removal from package registries, confirmed malicious packages continue to persist in production. Our analysis shows that organizations are still running known supply chain threats, exposing persistent gaps in dependency governance.

---

## 3. Container Vulnerability Landscape

Containers are a foundational component of modern application delivery, but many production images are built on outdated and vulnerable base layers. Over 60% of organizations run containers with critical vulnerabilities in core system packages such as `tar` (61%) and `glibc` (55%).

### 3.1 High/Critical Vulnerability Patching Velocity

While container vulnerabilities are widely detected, remediation remains slow and inconsistent. 77% of organizations still have high or critical container vulnerabilities unpatched after 90 days.

---

## 4. Secrets Management

Modern applications rely on secrets to connect services, access data, and automate workflows. Our research shows that secrets are frequently hardcoded, committed to repositories, and retained long after they should be revoked.

### 4.1 The AI/ML Secrets Crisis

The rapid adoption of AI and machine learning has introduced a new category of secrets exposure. Our analysis found that 43% of production organizations have exposed AI/ML credentials. Unlike traditional API keys, AI/ML secrets introduce compounding risk, including massive, unexpected costs and intellectual property theft.

---

## 5. CI/CD Pipeline Security

CI/CD pipelines sit at the center of modern software delivery. As organizations push more logic and credentials into these pipelines, CI/CD systems have become high-value targets for attackers.

### 5.1 CI/CD Platform Adoption
Jenkins (37%), GitHub Actions (31%), and Bitbucket Pipelines (28%) remain the most widely used platforms.

### 5.2 GitHub Actions Security
25% of repositories still rely on legacy or overly permissive GitHub token permissions, increasing the risk of credential abuse.

---

## 6. Infrastructure as Code Security

75% of organizations manage infrastructure through code. Without strong validation and governance, IaC can turn small configuration gaps into large-scale production risk.

### 6.1 IaC Platform Adoption
CloudFormation (67%) and Kubernetes Manifests (58%) lead the adoption charts.

### 6.2 Storage and Data Protection
84% of organizations deploy unencrypted storage resources through infrastructure code.

### 6.3 Identity and Access Management
Overly permissive IAM roles and wildcard permissions are frequently deployed via infrastructure templates.

### 6.4 Network Security
80% of organizations have no logging or monitoring enabled for network controls, and 62% have open firewall rules.

### 6.5 Container Security in IaC
Insecure container configurations, such as running as root (46%), are often embedded directly into IaC templates.

---

## 7. Repository and SCM Security

Source code repositories store proprietary code, infrastructure definitions, and credentials. Security controls across SCM platforms often lag behind their critical role in the software supply chain.

### 7.1 Code Review and Approval Gaps
Over 1 in 4 organizations require no code reviews at all.

### 7.2 Branch Protection Weakness
25% of organizations studied do not have branch protection enabled.

### 7.3 Access Control and Hygiene
31% of organizations do not require signed commits, leaving repositories vulnerable to sophisticated attacks.

---

## 8. Key Recommendations

### 8.1 Immediate Actions (0-30 Days)
- **Secrets Remediation**: Identify and rotate all valid secrets.
- **Critical Vulnerability Patching**: Prioritize CVSS 10.0 vulnerabilities.
- **CI/CD Token Permissions**: Restrict permissions to the minimum required access.

### 8.2 Short-term Initiatives (30-90 Days)
- **Supply Chain Security Controls**: Implement dependency scanning with enforcement.
- **Repository Hardening**: Enforce branch protection and mandate MFA.
- **IaC Security Gates**: Integrate IaC scanning into CI/CD pipelines.

### 8.3 Strategic Improvements (90+ Days)
- **Container Image Hygiene**: Establish standards for approved base images.
- **Zero Trust for CI/CD Pipelines**: Adopt ephemeral credentials.
- **Continue Risk Monitoring**: Deploy runtime security monitoring.

---

## 9. Conclusion

The state of application security in 2025–2026 reflects an industry in transition. Organizations have embraced modern development practices, but security maturity has not kept pace. The path forward requires treating application security not as a checkbox, but as a fundamental component of software quality. Every commit, dependency, and configuration change shapes risk and must be evaluated through a security lens.