# State of AI Security Report 2024

## Table of Contents
- [Foreword](#foreword)
- [About the Orca Research Pod](#about-the-orca-research-pod)
- [Executive summary](#executive-summary)
- [OWASP Top 10 Machine Learning Risks](#owasp-top-10-machine-learning-risks)
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
AI usage is exploding. Gartner predicts that the AI software market will grow 19.1% annually, reaching $298 billion by 2027. In many ways, AI is now in the stage reminiscent of where cloud computing was over a decade ago. At that time, speed of innovation was the focus, and it came at the expense of security. One such example was where storage buckets were spun up at the speed of the cloud, but were being left exposed to the Internet - without considering the security implications.

Fast forward to today, we are now witnessing the signs that history may repeat itself. Many AI services are defaulting to wide access and full permissions, focusing on speed of delivery while sacrificing security measures. Yet unlike a decade ago, we are now more prepared to secure emerging AI technologies and models. Awareness and education play a key role in achieving this goal, which is why we are releasing this inaugural report. We hope the report will help developers, CISOs, and security professionals better understand how to secure their AI models, while not slowing down innovation.

Gil Geron, CEO and Co-Founder of Orca Security

## About the Orca Research Pod
The Orca Research Pod is a group of cloud security researchers that discover and analyze cloud risks and vulnerabilities to strengthen the Orca Cloud Security Platform and promote cloud security best practices.

### Research Methodology
This report focuses on the security of deployed AI models in cloud services and environments. It was compiled by analyzing data captured from billions of cloud assets on AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud scanned by the Orca Cloud Security Platform.

## Executive summary
Our three primary findings are as follows:
1. **More than half of organizations are deploying their own AI models**: We found that 56% of organizations have adopted AI to build custom applications.
2. **Default AI settings are often accepted without regard for security**: The default settings of AI services tend to favor development speed rather than security. For example, 45% of Amazon SageMaker buckets are using non-randomized default bucket names, and 98% of organizations have not disabled the default root access for Amazon SageMaker notebook instances.
3. **Most vulnerabilities in AI models are low to medium risk - for now**: 62% of organizations have deployed an AI package with at least one CVE. Most of these vulnerabilities are low to medium risk with an average CVSS score of 6.9.

## OWASP Top 10 Machine Learning Risks
![Diagram of OWASP Top 10 ML Risks including Input Data Manipulation, Model Poisoning, Model Inversion, Membership Inference, Model Theft, AI Supply Chain Attacks, Transfer Learning Attack, Model Skewing, Output Integrity Attack, and Model Poisoning.]

## Key findings
- **56%** of organizations have adopted AI services for custom applications.
- **27%** of organizations have not configured Azure OpenAI accounts with private endpoints.
- **77%** of organizations using Amazon SageMaker have not configured metadata session authentication (IMDSv2) for their notebook instances.
- **20%** of organizations using OpenAI have at least one session access key saved in an unsecure location.
- **45%** of Amazon SageMaker buckets are using the default bucket naming convention.
- **98%** of organizations using Amazon SageMaker have a notebook instance with root access enabled.
- **62%** of organizations have deployed an AI package with at least one CVE.
- **98%** of organizations using Google Vertex AI have not enabled encryption at rest for their self-managed encryption keys.

## 1. AI usage
### 1.1 General AI usage
Our research indicates that 56% of organizations have adopted AI models for custom applications.

### 1.2 Usage by AI service
- **39%** of organizations with Azure are using Azure OpenAI.
- **29%** of organizations using AWS have at least one Amazon SageMaker Notebook instance.
- **24%** of organizations using GCP have deployed Vertex AI.
- **11%** of organizations using AWS have deployed Amazon Bedrock.

### 1.3 Usage by AI model
![Chart showing popularity of AI models: GPT-35 (79%), ADA (60%), GPT-4o (56%), GPT-4 (55%), DALL-E (40%), WHISPER (14%), CURIE (6%), LLAMA (5%), DAVINCI (4%), TEXT TO SPEECH (2%).]

### 1.4 Usage by AI package
![Chart showing top packages: SCKIT-LEARN (43%), NLTK (38%), PyTORCH (31%), TENSORFLOW (26%), TRANSFORMERS (23%), LANGCHAIN (22%), CUDA (20%), KERAS (19%), PyTORCH LIGHTING (18%), STREAMLIT (11%).]

## 2. Vulnerabilities in AI packages
62% of organizations have deployed an AI package with at least one CVE. While alarming, most of them present low to medium risk, with an average CVSSv3 score of 6.9. Additionally, 0.2% of these vulnerabilities have a public exploit.

## 3. Exposed AI models
### 3.1 Introduction
AI model code that is exposed to the Internet gives attackers the opportunity to target and exploit that code, leading to risks such as model theft or the installation of cryptominers.

### 3.2 Default Amazon SageMaker bucket names
45% of Amazon SageMaker buckets are using the non-randomized default bucket name (`sagemaker-{Region}-{Account-ID}`).

## 4. Insecure access
### 4.1 Exposed access keys
- **20%** of organizations using OpenAI have an exposed OpenAI access key.
- **35%** of organizations using Hugging Face have an exposed Hugging Face access key.
- **13%** of organizations using Anthropic have an exposed Anthropic access key.

### 4.2 Exposed keys in commit history
- **81%** of OpenAI exposed access keys are stored in a repository’s commit history.
- **77%** of Hugging Face exposed access keys are stored in a repository’s commit history.

### 4.3 Roles and permissions
4% of organizations using Amazon SageMaker have a notebook instance assigned with an administrative privileges IAM role.

## 5. Misconfigurations
### 5.1 Session-Based Metadata Access (IMDSv2)
77% of organizations using Amazon SageMaker have yet to configure IMDSv2 for their notebook instances.

### 5.2 Root access
98% of organizations have not disabled root access for Amazon SageMaker notebook instances.

### 5.3 Private endpoints
27% of organizations have not configured Azure OpenAI accounts with private endpoints.

## 6. Encryption
Nearly all organizations have yet to configure encryption at rest for their self-managed keys:
- **100%** Google Vertex AI (training pipelines)
- **99%** Amazon SageMaker (notebooks)
- **98%** Google Vertex AI (models)
- **98%** Azure OpenAI (accounts)

## 7. Conclusion
## Challenges in AI security
- **Pace of innovation**: Speed of development often outpaces security.
- **Shadow AI**: Lack of visibility into AI activity.
- **Nascent technology**: Lack of comprehensive resources and experts.
- **Regulatory compliance**: Balancing innovation with evolving legal standards.
- **Resource control**: Misconfigurations during service rollout.

## Key recommendations
1. **Beware of default settings**: Change defaults during early development.
2. **Manage vulnerabilities**: Map and remediate known vulnerabilities.
3. **Isolate networks**: Limit network access to assets.
4. **Limit privileges**: Embrace the Principle of Least Privilege (PoLP).
5. **Secure data**: Use self-managed encryption and encryption at rest.
6. **Follow best practices**: Consult service provider security guidelines.

## AI Goat
Orca’s AI Goat is an open-source, intentionally vulnerable AI environment based on the OWASP Top 10 ML risks, designed for testing and learning purposes.

## How can Orca help?
Orca’s AI Security Posture Management (AI-SPM) provides visibility and risk analysis for AI services, models, and resources, covering 50+ AI models and software packages.

## About Orca Security
Orca’s agentless-first Cloud Security Platform provides 100% visibility of all assets on AWS, Azure, Google Cloud, Kubernetes, and more, detecting risks across every layer of the cloud estate.

[^1]: 2024 Orca Security. All rights reserved.