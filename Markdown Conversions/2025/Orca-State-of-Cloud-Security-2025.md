# State of Cloud Security 2025

Organization: Orca  
Report Title: State-of-Cloud-Security  
Year: 2025

“Cloud security has reached a critical turning point. As organizations increasingly rely on the cloud to accelerate innovation and growth, several converging trends are reshaping the challenges security teams face—and the strategies they need to stay ahead.”

**GIL GERON**  
CEO and Co-Founder of Orca Security

## Table of Contents
- [Foreword](#foreword)
- [About the Orca Research Pod](#about-the-orca-research-pod)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [General Cloud Usage](#general-cloud-usage)
- [AI Security](#ai-security)
- [Attack Paths](#attack-paths)
- [Data Exposure](#data-exposure)
- [Vulnerabilities](#vulnerabilities)
- [Neglected Assets](#neglected-assets)
- [Identity & Access](#identity--access)
- [Application Security](#application-security)
- [Kubernetes](#kubernetes)
- [Key Recommendations](#key-recommendations)
- [About Orca Security](#about-orca-security)

---

## Foreword
Cloud security has reached a critical turning point. As organizations increasingly rely on the cloud to accelerate innovation and growth, several converging trends are reshaping the challenges security teams face—and the strategies they need to stay ahead.

Multi-cloud adoption is now the norm, with 55% of organizations using two or more providers. While this offers greater flexibility and resiliency, it also makes it harder to maintain consistent visibility and coverage across environments. At the same time, AI adoption is increasing—84% of organizations now use AI in the cloud. But this innovation comes with new risks: 62% of organizations have at least one vulnerable AI package, and some of the most prevalent AI-related CVEs enable remote code execution.

As organizations store more sensitive data in the cloud, the prevalence of data exposure is rising: 38% of organizations with sensitive data in their databases also have those databases exposed to the public.

These are among the many challenges covered in this report, which highlight the Defender’s Paradox in cloud security: attackers need to be right only once, defenders every time. In fact, 13% of organizations have a single cloud asset that supports more than 1,000 attack paths—underscoring the importance of comprehensive detection and effective prioritization.

This report is designed to help teams close their security gaps. Combining real-world insights compiled by the Orca Research Pod, it offers practical guidance on where to focus, what to prioritize, and how to effectively secure multi-cloud environments in the age of AI. We hope this report serves as a valuable resource for your teams.

**Gil Geron**  
CEO and Co-Founder of Orca Security

---

## About the Orca Research Pod
The Orca Research Pod is a group of cloud security researchers that discover and analyze cloud risks and vulnerabilities to strengthen the Orca Cloud Security Platform and promote cloud security best practices.

### Research Methodology
This report was compiled by analyzing data captured from billions of cloud assets on AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud and hundreds of thousands of code repositories scanned by the Orca Cloud Security Platform.

### Report Data Set
- Cloud workload and configuration data
- Billions of real-world production cloud assets
- Data referenced in this report was collected in 2025
- AWS, Azure, GCP, Oracle Cloud, and Alibaba Cloud environments

![Timeline of 25+ vulnerabilities discovered on AWS, Azure, and Google Cloud by the Orca Research Pod from 2022 to 2025]

---

## Executive Summary
Leveraging unique insights into current and emerging cloud risks captured from the Orca Cloud Security Platform, this report reveals the most commonly found, yet dangerous, cloud security risks. Summarizing the results from our research, these are our main findings:

- **More cloud innovation brings greater cloud risk.** As cloud adoption and cloud-native technologies expand, so does the volume and severity of cloud risks. Nearly a third of cloud assets are neglected today, and each asset contains on average 115 vulnerabilities.
- **Attack surfaces are expanding—and risks are increasingly interconnected.** 76% of organizations have at least one public-facing asset that enables lateral movement. 36% of organizations have at least one cloud asset supporting more than 100 attack paths.
- **Risks span the entire application pipeline.** 85% of organizations have plaintext secrets embedded in their source code repositories.
- **Innovation is expanding attack surfaces—and the scale of cloud risks.** 84% of organizations are now using AI in the cloud. Kubernetes adoption adds further complexity—93% of organizations have at least one privileged service account.

---

## Key Findings
- **13%**: of organizations have a single cloud asset responsible for creating more than 1000 attack paths.
- **38%**: of organizations with sensitive data in their databases also have those databases exposed to the public.
- **115**: vulnerabilities on average per cloud asset.
- **58%**: of organizations have at least one vulnerability older than 20 years.
- **32%**: of cloud assets on average are in a neglected state.
- **76%**: of organizations have at least one cloud asset that is public-facing and enables lateral movement.
- **85%**: of organizations have plaintext secrets embedded in their source code repositories.
- **93%**: of organizations have at least one privileged Kubernetes service account.

---

## General Cloud Usage
While cloud adoption continues to accelerate, the market remains highly concentrated around AWS, Azure, and Google Cloud Platform (GCP). This year’s analysis finds that most organizations are now multi-cloud by design, with 55% leveraging two or more cloud providers.

![Chart showing Cloud Adoption by Provider: AWS 82%, Azure 54%, GCP 35%, Oracle 10%, Alibaba 1%]  
![Chart showing Number of Cloud Providers Per Organization: 1 (46%), 2 (29%), 3 (19%), 4 (6%), 5 (<1%)]

---

## AI Security
Demand for cloud AI services continues to surge. This year’s report illustrates overall AI adoption in the cloud, the popularity of managed and unmanaged AI services, and the most popular AI packages.

- **62%** of organizations have at least one vulnerable AI package in their cloud environment.
- **AI Adoption in the Cloud**: 84% Overall, 62% Unmanaged, 52% Managed.

![Table of most prevalent CVEs associated with AI packages: scikit-learn (CVE-2024-5206), NLTK (CVE-2024-39705), PyTorch (CVE-2025-2953, CVE-2025-3730, CVE-2025-32434)]

---

## Attack Paths
Attack paths represent the toxic risk combinations that attackers can exploit to endanger your high-value cloud assets (i.e., crown jewels).

- **13%** of organizations have a cloud asset responsible for creating more than 1000 attack paths.
- **Most Common Crown Jewels**: Exposed Data (54%), Broad Permission Access (23%), Compromised Host (23%).

---

## Data Exposure
Sensitive data—which includes PII, PHI, API keys, financial information, secrets, and more—pose a significant risk when publicly exposed.

- **33%** of organizations with publicly exposed storage buckets have sensitive data in them.
- **38%** of organizations with sensitive data in their databases also have those databases exposed to the public.
- **28%** of organizations with cloud functions have publicly accessible functions with plaintext secrets in the function’s code package and environment variables.

---

## Vulnerabilities
### 4.1 Vulnerabilities - A Timeless Challenge
Cloud assets on average have 115 vulnerabilities.

### 4.2 Unpatched Web Services
- **82%** of organizations have at least one unpatched web service.
- **87%** of healthcare organizations have at least one unpatched web service.
- **84%** of technology organizations have at least one unpatched web service.

### 4.3 Old, But Still Relevant
- **93%** of organizations have at least one vulnerability older than 10 years.
- **58%** of organizations have at least one vulnerability older than 20 years.
- **59%** of organizations have at least one asset vulnerable to Log4Shell.

---

## Neglected Assets
A neglected asset is a cloud asset that uses an unsupported operating system or has remained unpatched for 180 days or more.

- **32%** of cloud assets are in a neglected state on average.
- **89%** of organizations have at least one neglected cloud asset that is internet-facing.

---

## Identity & Access
### 6.1 Lateral Movement
- **95%** of organizations have at least one cloud asset that enables lateral movement.
- **76%** of organizations have at least one cloud asset that is public-facing and enables lateral movement.

### 6.2 Cloud Functions
- **42%** of organizations have at least one Lambda function that lacks any policies restricting public access.
- **24%** of organizations have Lambda functions with admin permissions.

### 6.3 Non-Human Identities
Non-human identities (NHIs) outnumber their human counterparts by an average of 50:1.

### 6.4 Unused IAM Users
- **89%** of organizations have IAM user credentials that haven’t been used for 90+ days.

---

## Application Security
### 7.1 Secrets Exposure
- **85%** of organizations have plaintext secrets embedded in their source code repositories.

### 7.2 Misconfigurations - IaC
- **20%** of organizations have created an IaC misconfiguration that allows Cross-Account Access for IAM Role Without External ID or MFA.
- **17%** of organizations have an IaC artifact that configures S3 buckets to grant public GET.

### 7.3 Vulnerabilities
- **72%** of organizations have at least one package with a severe vulnerability (CVSS > 7) in a code repository.

---

## Kubernetes
- **70%** of organizations use Kubernetes.
- **50%** of organizations have at least one cluster with an unsupported version of K8 installed.
- **93%** of organizations have an overprivileged K8 service account.

---

## Key Recommendations
1. **Secure AI While Leveraging It to Enhance Cloud Security**: Protect models, packages, and data.
2. **Protect High-value Assets**: Prioritize attack paths that endanger crown jewels.
3. **Protect Your Sensitive Data**: Identify and secure sensitive data across the cloud estate.
4. **Prevent Workload Neglect**: Maintain an up-to-date inventory and monitor for abandoned assets.
5. **Prioritize Patching**: Focus on vulnerabilities that are reachable and exploitable in runtime.
6. **Enforce the Principle of Least Privilege (PoLP)**: Grant only minimum permissions needed.
7. **Unify Security Before Deployment and During Runtime**: Integrate pipeline security with runtime measures.
8. **Conduct Regular Audits and Leverage Continuous Monitoring**: Enforce policies and detect unusual activity.

---

## About Orca Security
Orca enables organizations to make cloud security a strategic advantage. With the most comprehensive coverage and visibility across multi-cloud environments, the agentless-first Orca Platform unites teams to eliminate complexities, vulnerabilities, and risks.

To find out more, [schedule a personalized demo](URL).

---
©2025 Orca Security. All rights reserved.