# 2025 State of Application Risk

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [Overall State of Application Risk](#overall-state-of-application-risk)
- [Extent of Application Risk](#extent-of-application-risk)
- [Adherence to the Application Security Requirements of Cybersecurity Regulations](#adherence-to-the-application-security-requirements-of-cybersecurity-regulations)
- [AppSec Testing Inefficiencies](#appsec-testing-inefficiencies)
- [Detailing the Most Common Application Risks](#detailing-the-most-common-application-risks)
- [Secrets Exposure](#secrets-exposure)
- [AI Risks](#ai-risks)
- [SDLC Misconfigurations](#sdlc-misconfigurations)
- [Software Supply Chain Issues](#software-supply-chain-issues)
- [Key Takeaways](#key-takeaways)

---

## Executive Summary
The Legit research team analyzed the data uncovered by the Legit Application Security Posture Management (ASPM) platform over the past 18 months. Because our platform discovers and visualizes all aspects of both applications and the software factory producing these assets, plus all security controls and gaps, Legit is in a unique position to offer a snapshot of common areas of AppSec posture risk.

**KEY DATA POINTS INCLUDE:**
- **100%**: Organizations that have high or critical application risks in their development environments.
- **100%**: Organizations that have high or critical exposed secrets.
- **36%**: Secrets found outside of source code (tickets, logs, artifacts, etc.).
- **46%**: Organizations that use AI models in source code in a risky way.
- **89%**: Organizations with pipeline misconfiguration issues.
- **78%**: Organizations with duplicate SCA scanners.
- **39%**: Organizations with duplicate SAST scanners.
- **85%**: Organizations with least privilege violations.
- **23%**: Repositories across organizations in which external collaborators with admin privileges can access pipelines with critical and high misconfigurations.

---

## Introduction
This report is based on our initial assessments of enterprises’ software factories in the past 18 months. The data represents a wide range of industries and company sizes – from organizations with fewer than 100 developers to those with thousands.

Application security is not just about finding vulnerabilities in source code anymore. With software development that is faster, more automated, more dynamic, and highly reliant on third parties, new opportunities to introduce risk abound. In this 2025 State of Application Risk report, we leveraged our powerful visibility capabilities to highlight our 2024 risk findings.

---

## Overall State of Application Risk
In this section, we provide a high-level snapshot of the state of application risk, courtesy of the Legit ASPM platform’s view of the entire software development lifecycle — from assets to dependencies, misconfigurations, GenAI code, and shadow IT — plus its security controls and gaps.

---

## Extent of Application Risk
Bottom line: There is a significant amount of risk throughout the application development process, including exposed secrets, risky misconfigurations, and dangerous vulnerabilities.

We found that **100% of organizations have high or critical application risks in their environments.**

![Chart showing the percentage of organizations with application risks in repositories containing public assets and those with risks in repositories containing 2 or 3+ assets.]

---

## Adherence to the Application Security Requirements of Cybersecurity Regulations
When we looked at adherence to the application security requirements of cybersecurity regulations, the results were mixed.

| Framework | Average Rate of Compliance |
| :--- | :--- |
| CISA | 47% |
| FedRamp | 64% |
| ISO | 76% |
| PCI DSS | 62% |
| SOC2 | 71% |
| SSDF | 42% |
| OWASP CI/CD | 33% |

Table 1: Adherence to application security requirements of cybersecurity regulations

---

## AppSec Testing Inefficiencies
The extent of the risk we have uncovered in this report results in part from an inefficient and ineffective process for assessing risk. We have found that a significant number of organizations have duplicate scanners producing duplicate results.

- **78%**: Organizations with duplicate SCA scanners.
- **39%**: Organizations with duplicate SAST scanners.

![Chart showing the percentage of organizations with duplicate AppSec testing tools.]

---

## Detailing the Most Common Application Risks
In the following pages, we highlight and detail four application risks we see frequently:
1. Secrets Exposure
2. AI Risks
3. SDLC Misconfigurations
4. Software Supply Chain Issues

---

## Secrets Exposure
Secrets are extremely pervasive in software development environments, and their exposure is one of the most common risks unearthed by the Legit platform. We found exposed secrets in 100% of organizations.

![Chart showing the extent of secrets exposure, including active/inactive development, public assets, and toxic combinations.]

**Preventing Exposed Secrets:**
- Avoid committing secrets to any Git repository.
- Avoid `git add *` commands.
- Name sensitive files in `.gitignore`.
- Use automated secrets scanning on repositories.
- Change the source code to not rely on hard-coded secrets.

---

## AI Risks
GenAI has recently emerged as an additional risk we uncover. We often discover that security teams don’t know where AI is in use, and then find out it’s used in a location that isn’t configured securely.

![Chart showing the extent of AI risk, with 46% of organizations using AI models in source code in a risky way.]

---

## SDLC Misconfigurations
Misconfigured SDLC assets, such as SCMs, build servers, and artifact repositories, provide an opportunity for threat actors to gain access to systems and then move laterally within an organization.

| Legit Policies | Percent of Repos Violating this Policy |
| :--- | :--- |
| Unsigned commits are allowed in the repository | 56% |
| Repository doesn’t have defined default reviewers | 33% |
| Default repository branch is not protected | 48% |
| Code review by at least one reviewer is not enforced | 48% |
| Code review by at least two reviewers is not enforced | 36% |
| It is possible to merge code without the approval of all reviewers | 34% |
| Jenkins server has non-pipeline jobs | 33% |

Table 2: Misconfiguration policy violations

---

## Software Supply Chain Issues
Software supply chain issues include unsafe cross-workflow actions, build actions utilizing mutable images, and privileged pipelines checking out insecure code.

![Chart showing the extent of software supply chain issues, noting 100% of organizations have high or critical issues.]

---

## Key Takeaways
The application risk landscape has changed, and traditional application security approaches are no longer sufficient.

**Best Practices:**
- **Scan for secrets exposure**: Avoid hard-coded secrets and use automated scanning.
- **Manage AI risk**: Gain visibility into AI usage and threat model specific AI threats.
- **Enable branch protection**: Enforce branch protection for your default main branch.
- **Tighten up permissions**: Implement RBAC and enforce the principle of least privilege.
- **Streamline AppSec scanning**: Consolidate duplicate tools to reduce alert fatigue.
- **Continually monitor**: Verify configurations and permissions on an ongoing basis.