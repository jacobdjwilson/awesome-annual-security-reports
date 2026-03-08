# 2024 State of AI Security Report

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
    - [5.1 Session authentication (IMDSv2)](#51-session-authentication-imdsv2)
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

AI usage is exploding. Gartner predicts that the AI software market will grow 19.1% annually, reaching $298 billion by 2027. In many ways, AI is now in the stage reminiscent of where cloud computing was over a decade ago.

At that time, speed of innovation was the focus, and it came at the expense of security. One such example was where storage buckets were spun up at the speed of the cloud, but were being left exposed to the Internet - without considering the security implications.

Fast forward to today, we are now witnessing the signs that history may repeat itself. Many AI services are defaulting to wide access and full permissions, focusing on speed of delivery while sacrificing security measures.

Yet unlike a decade ago, we are now more prepared to secure emerging AI technologies and models. Awareness and education play a key role in achieving this goal, which is why we are releasing this inaugural report.

We hope the report will help developers, CISOs, and security professionals better understand how to secure their AI models, while not slowing down innovation.

Thank you for reading our research.

**Gil Geron**
CEO and Co-Founder of Orca Security

---

## About the Orca Research Pod

The Orca Research Pod is a group of cloud security researchers that discover and analyze cloud risks and vulnerabilities to strengthen the Orca Cloud Security Platform and promote cloud security best practices.

### Research Methodology
This report focuses on the security of deployed AI models in cloud services and environments. It was compiled by analyzing data captured from billions of cloud assets on AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud scanned by the Orca Cloud Security Platform.

**Report Data Set:**
- Cloud workload and configuration data
- Billions of real-world production cloud assets
- Data referenced in this report was collected from January - August 2024
- AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud environments

![Timeline of vulnerabilities discovered by Orca from 2022 to 2024]

---

## Executive summary

Our three primary findings are as follows:

1. **More than half of organizations are deploying their own AI models**
We found that 56% of organizations have adopted AI to build custom applications. Azure OpenAI is currently the front runner among cloud provider AI services, with 39% of organizations with Azure using it. Sckit-learn is the most used AI package (43%) and GPT-35 is the most popular AI model, with 79% of organizations using GPT-35 in their cloud.

2. **Default AI settings are often accepted without regard for security**
The default settings of AI services tend to favor development speed rather than security, which results in most organizations using insecure default settings. For example, 45% of Amazon SageMaker buckets are using non randomized default bucket names, and 98% of organizations have not disabled the default root access for Amazon SageMaker notebook instances.

3. **Most vulnerabilities in AI models are low to medium risk - for now**
62% of organizations have deployed an AI package with at least one CVE. Most of these vulnerabilities are low to medium risk with an average CVSS score of 6.9, and only 0.2% of the vulnerabilities have a public exploit (compared to the 2.5% average).

---

## Key findings

- **56%** of organizations have adopted AI services for custom applications.
- **27%** of organizations have not configured Azure OpenAI accounts with private endpoints.
- **77%** of organizations using Amazon SageMaker have not configured metadata session authentication (IMDSv2) for their notebook instances.
- **20%** of organizations using OpenAI have at least one access key saved in an unsecure location.
- **45%** of Amazon SageMaker buckets are using the default bucket naming convention.
- **98%** of organizations using Amazon SageMaker have a notebook instance with root access enabled.
- **62%** of organizations have deployed an AI package with at least one CVE.
- **98%** of organizations using Google Vertex AI have not enabled encryption at rest for their self-managed encryption keys.

---

## 1. AI usage

### 1.1 General AI usage
Our research indicates that more than half of organizations have adopted AI models for custom applications (company-specific AI solutions addressing a specific use case or set of use cases). This represents a significant percentage, meaning that many companies are not only using and testing AI models, but also creating their own custom solutions and integrations specific to their environment.

### 1.2 Usage by AI service
Among organizations in our study, Azure OpenAI is the most frequently used AI service. The figures illustrate significant AI adoption among organizations, considering that Google Vertex AI became generally available in May 2021, Azure OpenAI in November 2021, and Amazon Bedrock in September 2023.

### 1.3 Usage by AI model
AI models are systems or algorithms trained to perform specific tasks according to learned patterns and relationships. Organizations can choose which AI model(s) to integrate with the AI services referenced previously.

![Chart showing top 10 AI models: GPT-35 (79%), ADA (60%), GPT-4o (56%), GPT-4 (55%), DALL-E (40%), WHISPER (14%), CURIE (6%), LLAMA (5%), DAVINCI (4%), TEXT TO SPEECH (2%)]

### 1.4 Usage by AI package
AI packages are designed to automate the development of AI and ML applications. These packages contain a collection of pre-developed modules and tools that enable developers to create, train, and deploy AI models without developing brand new routines.

![Chart showing top 10 AI packages: SCKIT-LEARN (43%), NLTK (38%), PyTORCH (31%), TENSORFLOW (26%), TRANSFORMERS (23%), LANGCHAIN (22%), CUDA (20%), KERAS (19%), PyTORCH LIGHTING (18%), STREAMLIT (11%)]

---

## 2. Vulnerabilities in AI packages

A significant share of deployed AI packages contain at least one CVE. While alarming, most of them present low to medium risk, with an average CVSSv3 score of 6.9. Additionally, 0.2% of these vulnerabilities have a public exploit, far less than the general average of cloud assets (2.5%).

This may explain why most of these packages remain unpatched: security teams are prioritizing more critical risks. Also, upgrading some AI packages can be complicated, especially when they have dependencies (e.g., Numpy and Pytorch), which make it difficult to understand which version is compatible.

---

## 3. Exposed AI models

### 3.1 Introduction
AI model code that is exposed to the Internet gives attackers the opportunity to target and exploit that code. Exposed code presents risks such as code and model theft, the installation of a cryptominer, and more.

### 3.2 Default Amazon SageMaker bucket names
Aqua Security recently discovered that when a user creates an Amazon SageMaker Canvas, the service automatically creates an S3 bucket to store files utilized by the service, using the following default naming convention: `sagemaker-{Region}-{Account-ID}`. We found that nearly half (45%) of all SageMaker buckets are still using the default bucket name.

---

## 4. Insecure access

### 4.1 Exposed access keys
API keys provide access to AI services in code repositories. This enables developers to access AI models through the API and build applications that can generate code, images, and text. Because some of the repositories are public, unencrypted access keys can allow unwanted access to the model and its code.

### 4.2 Exposed keys in commit history
The security risk of exposed keys also applies to a repository’s commit history—not just its master branch. The Orca 2023 Honeypotting in the Cloud Report confirmed that attackers frequently scan for secrets in old commits and retrieve them.

### 4.3 Roles and permissions
Our findings reveal that a relatively low number of organizations are assigning over-privileged roles to Amazon Sagemaker, and instead are applying the principle of least privilege (PoLP) to their notebook instances.

---

## 5. Misconfigurations

### 5.1 Session authentication (IMDSv2)
In our study, most organizations using Amazon SageMaker (77%) have yet to configure IMDSv2 for their notebook instances. This leaves notebook instances and their sensitive data potentially exposed to high-risk vulnerabilities.

### 5.2 Root access
According to our findings, nearly all organizations using Amazon SageMaker have yet to disable root access for their notebook instances. This gives attackers free reign and full control over SageMaker's Jupyter notebooks and the AI models and services that run in them.

### 5.3 Private endpoints
Approximately one out of every four organizations using Azure OpenAI have not configured their accounts with private endpoints. This increases the risk that attackers can access, intercept, or manipulate data transmitted between cloud resources and AI services.

---

## 6. Encryption
Nearly all organizations have yet to configure encryption at rest for their self-managed keys. This applies to all cloud providers (AWS and its Key Management Service (KMS) keys; Google and its customer-managed encryption keys (CMEK); and Azure and its customer-managed keys (CMK)) and across multiple locations where AI data is housed.

---

## 7. Conclusion

### Challenges in AI security
- **Pace of innovation**: The speed of AI development continues to accelerate.
- **Shadow AI**: Security teams lack complete visibility into AI activity.
- **Nascent technology**: AI security lacks comprehensive resources and seasoned experts.
- **Regulatory compliance**: Navigating evolving compliance requirements requires a delicate balance.
- **Resource control**: Resource misconfigurations often accompany the rollout of a new service.

### Key recommendations
1. **Beware of default settings**: Change default settings during the early stages of development.
2. **Manage vulnerabilities**: Detect and map vulnerabilities in your environments.
3. **Isolate networks**: Limit network access to your assets.
4. **Limit privileges**: Eliminate redundant privileges and remove unnecessary access.
5. **Secure data**: Opt for self-managed encryption keys and enable encryption at rest.
6. **Follow best practices**: Consult service provider recommendations and apply restrictive settings.

### AI Goat
Orca’s AI Goat is the first open source AI security hands-on learning environment based on the OWASP top 10 ML risks. It is an intentionally vulnerable AI environment that includes numerous threats and vulnerabilities for testing and learning purposes.

### How can Orca help?
Orca’s AI Security Posture Management (AI-SPM) solution provides unmatched visibility and deep risk analysis for AI services, models, resources, and use cases. Orca’s AI-SPM solution covers 50+ AI models and software packages.

---

## About Orca Security
Orca’s agentless-first Cloud Security Platform connects to your environment in minutes and provides 100% visibility of all your assets on AWS, Azure, Google Cloud, Kubernetes, and more. Orca detects, prioritizes, and helps remediate cloud risks across every layer of your cloud estate.

[^1]: https://owasp.org/