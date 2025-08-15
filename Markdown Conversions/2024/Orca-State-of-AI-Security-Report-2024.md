# 2024 State of AI Security Report

![Report cover image with text: 2024 State of Security Report, Unveiling the numbers and insights behind the prevalence of AI risks in the cloud](https://example.com/path/to/report-cover.png)

## Table of Contents
- [Foreword](#foreword)
- [About the Orca Research Pod](#about-the-orca-research-pod)
- [Executive summary](#executive-summary)
- [Key findings](#key-findings)
- [1. AI usage](#1-ai-usage)
  - [1.1 General AI usage](#11-general-ai-usage)
  - [1.2 Usage by AI service](#12-usage-by-ai-service)
  - [1.3 Usage by AI model](#13-usage-by-ai-model)
  - [1.4 Usage by AI package](#14-usage-by-ai-package)
- [2. Vulnerabilities in AI packages](#2-vulnerabilities-in-ai-packages)
- [3. Exposed AI models](#3-exposed-ai-models)
  - [3.1 Introduction](#31-introduction)
  - [3.2 Default Amazon SageMaker bucket names](#32-default-amazon-sagemaker-bucket-names)
- [4. Insecure access](#4-insecure-access)
  - [4.1 Exposed access keys](#41-exposed-access-keys)
  - [4.2 Exposed keys in commit history](#42-exposed-keys-in-commit-history)
  - [4.3 Roles and permissions](#43-roles-and-permissions)
- [5. Misconfigurations](#5-misconfigurations)
  - [5.1 Session-Based Metadata Access (IMDSv2)](#51-session-based-metadata-access-imdsv2)
  - [5.2 Root access](#52-root-access)
  - [5.3 Private endpoints](#53-private-endpoints)
- [6. Encryption](#6-encryption)
- [7. Conclusion](#7-conclusion)
  - [Challenges in AI security](#challenges-in-ai-security)
  - [Key recommendations](#key-recommendations)
  - [AI Goat](#ai-goat)
  - [How can Orca help?](#how-can-orca-help)
- [About Orca Security](#about-orca-security)

---

## Foreword

AI usage is exploding. Gartner predicts that the AI software market will grow **19.1% annually**, reaching $298 billion by 2027. In many ways, AI is now in the stage reminiscent of where cloud computing was over a decade ago.

At that time, speed of innovation was the focus, and it came at the expense of security. One such example was where storage buckets were spun up at the speed of the cloud, but were being left exposed to the Internet - without considering the security implications.

Fast forward to today, we are now witnessing the signs that history may repeat itself. Many AI services are defaulting to wide access and full permissions, focusing on speed of delivery while sacrificing security measures.

Yet unlike a decade ago, we are now more prepared to secure emerging AI technologies and models. Awareness and education play a key role in achieving this goal, which is why we are releasing this inaugural report.

We hope the report will help developers, CISOs, and security professionals better understand how to secure their AI models, while not slowing down innovation.

Thank you for reading our research.

Gil Geron
CEO and Co-Founder of Orca Security

## About the Orca Research Pod

The Orca Research Pod is a group of cloud security researchers that discover and analyze cloud risks and vulnerabilities to strengthen the Orca Cloud Security Platform and promote cloud security best practices.

### Research Methodology

This report focuses on the security of deployed AI models in cloud services and environments. It was compiled by analyzing data captured from billions of cloud assets on AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud scanned by the Orca Cloud Security Platform.

**Report Data Set:**
- Cloud workload and configuration data
- Billions of real-world production cloud assets
- Data referenced in this report was collected from January - August 2024
- AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud environments

**25+ vulnerabilities discovered on AWS, Azure, and Google Cloud**

**2024**
- System:authenticated default Google Kubernetes Engine (GKE) group
- LeakyCLI in AWS and Google Cloud

**2023**
- Azure Digital Twins SSRF
- Azure Functions App SSRF
- Azure API Management SSRF
- Azure Machine Learning SSRF
- Azure Storage Account Keys Exploitation
- Azure Super FabriXss
- Two Azure PostMessage IFrame Vulnerabilities
- Bad.Build Supply Chain Risk in GCP
- 8 Cross-Site Scripting (XSS) vulnerabilities on Azure HDInsight
- Unauthenticated Access Risk to GCP Dataproc

**2022**
- AWS BreakingFormation
- AWS Superglue
- Databricks
- Azure AutoWarp
- Azure SynLapse
- Azure FabriXxs
- Azure CosMiss

## Executive summary

Our three primary findings are as follows:

1.  **More than half of organizations are deploying their own AI models**
    We found that **56%** of organizations have adopted AI to build custom applications. Azure OpenAI is currently the front runner among cloud provider AI services, with **39%** of organizations with Azure using it. Sckit-learn is the most used AI package (**43%**) and GPT-35 is the most popular AI model, with **79%** of organizations using GPT-35 in their cloud.

2.  **Default AI settings are often accepted without regard for security**
    The default settings of AI services tend to favor development speed rather than security, which results in most organizations using insecure default settings. For example, **45%** of Amazon SageMaker buckets are using non randomized default bucket names, and **98%** of organizations have not disabled the default root access for Amazon SageMaker notebook instances.

3.  **Most vulnerabilities in AI models are low to medium risk - for now**
    **62%** of organizations have deployed an AI package with at least one CVE. Most of these vulnerabilities are low to medium risk with an average CVSS score of 6.9, and only **0.2%** of the vulnerabilities have a public exploit (compared to the **2.5%** average).

This report harnesses unique insights from scans performed by the Orca Cloud Security Platform, and uncovers key AI security risks and considerations for CISOs, developers, and security professionals. The AI security risks discussed in this report are mapped to each of the OWASP Top 10 Machine Learning Risks.

## OWASP Top 10 Machine Learning Risks

[https://owasp.org/](https://owasp.org/)

1.  **Input Manipulation**
    Adversarial attacks, in which threat actors intentionally modify input data to deceive the model.

2.  **Data Poisoning**
    Manipulation of the training data to induce the model to act in an unintended and undesirable way.

3.  **Model Inversion Attack**
    Attackers reverse-engineer the model to obtain information from it.

4.  **Membership Inference Attack**
    Manipulation of the model’s training data to induce behavior that reveals sensitive information.

5.  **Model Theft**
    Unauthorized, malicious users access the model’s parameters.

6.  **AI Supply Chain Attacks**
    Alteration or substitution of a machine learning library or model employed by a system.

7.  **Transfer Learning Attack**
    Training a model on a particular task before fine-tuning it on another task to induce it to behave undesirably.

8.  **Model Skewing**
    Altering the distribution of training data to induce the model to behave undesirably.

9.  **Output Integrity Attack**
    Altering the output of a model to induce unintended or harmful behavior directed at the system using it.

10. **Model Poisoning**
    Manipulation of the model’s parameters to induce undesirable behavior.

## Key findings

-   **56%** of organizations have adopted AI services for custom applications
    Many organizations are using AI models to create custom solutions and integrations specific to their environment(s).

-   **27%** of organizations have not configured Azure OpenAI accounts with private endpoints.
    This increases the risk that attackers can access, intercept, or manipulate data transmitted between cloud resources and AI services.

-   **77%** of organizations using Amazon SageMaker have not configured metadata session authentication (IMDSv2) for their notebook instances
    Not having IMDSv2 enabled leaves notebook instances and their sensitive data potentially exposed to high-risk vulnerabilities.

-   **20%** of organizations using OpenAI have at least one access key saved in an unsecure location
    A single leaked key can lead to a breach and risk the integrity of the OpenAI account.

-   **45%** of Amazon SageMaker buckets are using the default bucket naming convention
    Even though AWS fixed the default naming structure, adding randomized characters to the default bucket name, nearly half of organizations are still using the easily discoverable non randomized default name.

-   **98%** of organizations using Amazon SageMaker have a notebook instance with root access enabled
    The default setting enables local root access, allowing a potential attacker to access sensitive information, exfiltrate data, poison data, and more.

-   **62%** of organizations have deployed an AI package with at least one CVE
    AI packages enable developers to create, train, and deploy AI models without developing brand new routines. These packages are often susceptible to known vulnerabilities.

-   **98%** of organizations using Google Vertex AI have not enabled encryption at rest for their self-managed encryption keys
    This leaves sensitive data exposed to attackers, increasing the chances that a bad actor can exfiltrate, delete, or alter the AI model.

---

## 1. AI usage

![Section divider image with text: 01 AI usage](https://example.com/path/to/01-ai-usage.png)

### 1.1 General AI usage

Our research indicates that more than half of organizations have adopted AI models for custom applications (company-specific AI solutions addressing a specific use case or set of use cases). This represents a significant percentage, meaning that many companies are not only using and testing AI models, but also creating their own custom solutions and integrations specific to their environment.

-   **56%** of organizations have adopted AI models for custom applications.

### 1.2 Usage by AI service

Among organizations in our study, Azure OpenAI is the most frequently used AI service.

-   **39%** of organizations with Azure are using Azure OpenAI.
-   **29%** of organizations using AWS have at least one Amazon SageMaker Notebook instance.
-   **24%** of organizations using GCP have deployed Vertex AI.
-   **11%** of organizations using AWS have deployed Amazon Bedrock.

The figures illustrate significant AI adoption among organizations, considering that Google Vertex AI became generally available in May 2021, Azure OpenAI in November 2021, and Amazon Bedrock in September 2023. We expect these figures to grow significantly over time, as more organizations leverage these AI services.

-   **May 2021**: Google Vertex AI becomes generally available
-   **Nov 2021**: Azure OpenAI becomes generally available
-   **Sept 2023**: Amazon Bedrock becomes generally available

### 1.3 Usage by AI model

AI models are systems or algorithms trained to perform specific tasks according to learned patterns and relationships. Organizations can choose which AI model(s) to integrate with the AI services referenced previously.

![Bar chart showing the top 10 most popular AI models and their usage percentages.](https://example.com/path/to/top-10-ai-models-chart.png)

**Top 10 most popular AI models**
-   GPT-35: **79%**
-   ADA: **60%**
-   GPT-4o: **56%**
-   GPT-4: **55%**
-   DALL-E: **40%**
-   WHISPER: **14%**
-   CURIE: **6%**
-   LLAMA: **5%**
-   DAVINCI: **4%**
-   TEXT TO SPEECH: **2%**

### 1.4 Usage by AI package

AI packages are designed to automate the development of AI and ML applications. These packages contain a collection of pre-developed modules and tools that enable developers to create, train