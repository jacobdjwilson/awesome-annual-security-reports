# Cloud and Threat Report: 2026

## Table of Contents
- [Introduction](#introduction)
- [In this report](#in-this-report)
- [SaaS genAI use is rapidly increasing](#saas-genai-use-is-rapidly-increasing)
- [GenAI data policy violation incidents are rapidly increasing](#genai-data-policy-violation-incidents-are-rapidly-increasing)
- [Blocking unwanted genAI apps reduces data exposure risk](#blocking-unwanted-genai-apps-reduces-data-exposure-risk)
- [Agentic AI adoption amplifies data exposure and insider risk](#agentic-ai-adoption-amplifies-data-exposure-and-insider-risk)
- [Personal cloud apps usage is a significant insider threat risk](#personal-cloud-apps-usage-is-a-significant-insider-threat-risk)
- [Data policy violations in personal applications](#data-policy-violations-in-personal-applications)
- [Phishing remains a persistent challenge](#phishing-remains-a-persistent-challenge)
- [Malware continues to infiltrate organizations through trusted channels](#malware-continues-to-infiltrate-organizations-through-trusted-channels)
- [Recommendations](#recommendations)
- [Netskope Threat Labs](#netskope-threat-labs)
- [About this report](#about-this-report)

---

## Introduction
The 2026 edition of the Netskope Cloud and Threat Report is designed to analyze the most significant cybersecurity trends of the previous year, offering a critical preview of the challenges and risks that will define the enterprise landscape in 2026. In 2025, the rapid, often ungoverned, adoption of generative AI fundamentally reshaped the cybersecurity landscape. As organizations navigated the complexities of cloud data security, persistent phishing campaigns, and malware delivered through trusted channels, the introduction of widespread AI usage—particularly “shadow AI” and emerging “agentic AI”—layered new and complex data exposure risks onto the modern enterprise environment. This report provides a look back at the most significant trends of 2025 and serves as a critical preview of the evolving threat landscape for 2026, highlighting the additive nature of the risks that security teams must now confront. Not only do security teams still have to manage existing risks, but they now also have to manage the risks created by genAI.

The most immediate genAI-specific risk is the substantial surge in data exposure, with the rate of data policy violations associated with genAI application usage doubling last year. This accelerated adoption is frequently driven by shadow AI—employee use of unmanaged services and personal accounts—resulting in the leakage of highly sensitive material, including source code, regulated data, and intellectual property. Concurrently, the operational introduction of agentic AI systems, which execute complex, autonomous actions across internal and external resources, creates a vast, new attack surface that necessitates a fundamental re-evaluation of security perimeters and trust models.

This combination of novel AI-driven threats and legacy security concerns defines the evolving threat landscape for 2026. As employee behavior and new AI tools evolve faster than traditional safeguards, strengthening oversight, data loss prevention (DLP) controls, and overall security posture is essential.

## In this report
- **SaaS genAI use is rapidly increasing**: The number of people using SaaS genAI apps like ChatGPT and Gemini has increased threefold, while the number of prompts people are sending to the apps has increased sixfold in the last year. Shadow AI remains a significant challenge, with 47% of genAI users using personal AI apps.
- **GenAI data policy violation incidents are rapidly increasing**: With the rise in popularity of genAI apps, the number of incidents of users sending sensitive data to AI apps has doubled in the past year, with the average organization seeing 223 incidents per month.
- **Personal apps are a significant insider threat risk**: 60% of insider threat incidents involve personal cloud app instances, with regulated data, intellectual property, source code, and credentials frequently being sent to personal app instances in violation of organization policies.
- **Phishing remains a persistent challenge**: Despite a year-over-year decline in the number of people clicking on phishing links, phishing is still a persistent problem, with 87 out of every 10,000 users clicking on a phishing link each month, and Microsoft being the most mimicked brand.
- **Malware continues to infiltrate organizations through trusted channels**: Attackers continue to have success in distributing malware to their victims through trusted channels, including software registries like npm and popular cloud apps like GitHub, OneDrive, and Google Drive.

## SaaS genAI use is rapidly increasing
Over the past year, enterprises have continued to struggle with how employees use generative AI tools. Much like the early days of SaaS and cloud platforms, many workers began experimenting with AI apps on their own, usually by signing in with personal accounts long before IT or security teams deploy company-approved genAI tools among their workforce. This pattern has given rise to what is now commonly called shadow AI, the AI usage that occurs outside organizational visibility, policy, and control.

Even with the rapid push toward enterprise licensing and governance frameworks, unregulated access is still widespread. Internal monitoring across organizations shows that a substantial share of employees are relying on tools such as ChatGPT, Google Gemini, and Copilot using credentials not associated with their organization. The good news is that this behavior is shifting in the right direction. Personal account usage has dropped significantly over the past year, as the percentage of AI users who use personal AI apps fell from 78% to 47%. In parallel, the percentage of people using organization-managed accounts has climbed from 25% to 62%, signaling that more companies are standardizing AI access and maturing their oversight. However, there is a growing overlap here of people who are switching back and forth between personal and enterprise accounts, growing from 4% of users to 9% of users.

![Chart showing genAI application adoption trends across regions and industries]

The rapid and decentralized adoption of generative SaaS AI tools will fundamentally reshape the cloud security landscape in 2026. We expect to see two major shifts: the continued exponential growth in the use of genAI across business functions and the dethroning of ChatGPT by the Gemini ecosystem as the most popular SaaS genAI platform.

## GenAI data policy violation incidents are rapidly increasing
In the average organization, both the number of users committing data policy violations and the number of data policy incidents has increased twofold over the past year, with an average of 3% of genAI users committing an average of 223 genAI data policy violations per month. Meanwhile, the top 25% of organizations are seeing an average of 2,100 incidents per month across 13% of their genAI user base.

The three categories of data most involved in genAI data policy violations over the past year were:
- **Source code (42%)**: Users often submit this when seeking debugging help, refactoring suggestions, or code generation.
- **Regulated data (32%)**: Personal, financial, or healthcare data.
- **Intellectual property (16%)**: Contracts, internal documents, and proprietary research.

## Blocking unwanted genAI apps reduces data exposure risk
90% of organizations use a strategy of blocking unwanted apps, with the average organization actively blocking 10 apps. 
- **ZeroGPT** is currently the most frequently blocked genAI-related application (45%).
- **DeepSeek** follows with 43% of organizations blocking it.

## Agentic AI adoption amplifies data exposure and insider risk
Agentic AI systems are those that execute complex, autonomous actions across internal and external resources. Currently, 33% of organizations use OpenAI services via Azure, 27% use Amazon Bedrock, and 10% leverage Google Vertex AI.

The increasing adoption of agentic AI is amplifying not only the data exposure risks highlighted earlier in this report, but also amplifying insider risks, since an agent given access to sensitive data or systems can do damage at a much higher rate.

## Personal cloud apps usage is a significant insider threat risk
60% of insider threat incidents involve personal cloud app instances. While traffic to cloud applications via personal accounts has remained essentially unchanged over the past year, organizations have improved their defensive posture. The number of organizations placing real-time controls on data being sent to personal apps expanded from 70% to 77%.

## Data policy violations in personal applications
Over the past year, the percentage of users uploading data to personal cloud apps has increased by 21%. Today, 31% of users in the average organization upload data to personal cloud apps every month. 
- **Regulated data**: 54% of violations.
- **Intellectual property**: 22% of violations.
- **Source code**: 15% of violations.
- **Passwords and API keys**: 8% of violations.

## Phishing remains a persistent challenge
User susceptibility declined slightly over the past year: clicks on phishing links dropped from 119 per 10,000 users last year to 87 per 10,000 users this year. Brand impersonation remains a core tactic:
- **Microsoft**: 52% of clicks.
- **Hotmail**: 11% of clicks.
- **DocuSign**: 10% of clicks.

## Malware continues to infiltrate organizations through trusted channels
Adversaries increasingly abuse trusted cloud services to distribute malware.
- **GitHub**: 12% of organizations detecting exposure.
- **Microsoft OneDrive**: 10% of organizations.
- **Google Drive**: 5.8% of organizations.

## Recommendations
Based on the trends uncovered in this report, Netskope Threat Labs strongly encourages organizations to:
1. **Inspect all HTTP and HTTPS downloads**: Prevent malware from infiltrating the network.
2. **Block access to apps**: Restrict apps that do not serve a legitimate business purpose.
3. **Use DLP policies**: Detect sensitive information being sent to unauthorized locations.
4. **Use Remote Browser Isolation (RBI)**: Provide additional protection for high-risk website categories.

## Netskope Threat Labs
Staffed by the industry’s foremost cloud threat and malware researchers, Netskope Threat Labs discovers, analyzes, and designs defenses against the latest cloud threats affecting enterprises.

## About this report
Netskope provides threat protection to millions of users worldwide. Information presented in this report is based on anonymized usage data collected by the Netskope One platform. The statistics in this report are based on the period from October 1, 2024, through October 31, 2025.