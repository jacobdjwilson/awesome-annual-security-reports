# AI Security Readiness: Insights from 100 Cloud Architects, Engineers, and Security Leaders

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [AI Adoption is Outpacing Security Expertise](#ai-adoption-is-outpacing-security-expertise)
- [AI Security Requires Both Traditional and Advanced Solutions](#ai-security-requires-both-traditional-and-advanced-solutions)
- [Cloud Security Architectures Are Increasingly Complex](#cloud-security-architectures-are-increasingly-complex)
- [AI Security Challenges Are Not Just Technical—They’re Operational](#ai-security-challenges-are-not-just-technical—theyre-operational)
- [Evaluating Security Maturity](#evaluating-security-maturity)
- [Recommendations: How to Close the AI Security Gap](#recommendations-how-to-close-the-ai-security-gap)
- [Future-Proofing AI Security](#future-proofing-ai-security)
- [Learn More](#learn-more)

## Introduction
In late 2024, Gatepoint Research invited a select group of professionals to participate in a survey titled *Navigating the Future of AI Security*. The 100 respondents spanned 96 unique organizations, and included engineers, architects, CxOs, VPs, directors, and managers across various industries. They were asked to report on their cloud adoption journeys, current cloud architectures, AI usage patterns, top AI security challenges, and the strategies they’ve implemented to manage those risks. In this ebook, we explore AI adoption and security trends from that survey data.

## Executive Summary
The AI adoption is nearly universal, but security isn’t keeping up. According to our survey, 87% of respondents are using AI services. This aligns with Wiz’s State of AI in the Cloud 2025 report[^1], where we found that over 85% of respondents are currently using either managed or self-hosted AI services or tools. However, the adoption of security best practices is not keeping pace.

31% of respondents cite a lack of AI security expertise as their top challenge. The rate of innovation in AI can't afford to wait for security to upskill. This gap increases risk exposure and makes tooling and automation critical.

While traditional security approaches like EDR and vulnerability management remain prevalent (adopted by 70% and 65% of respondent respectively), only 13% of respondents have adopted AI-specific posture management (AI-SPM). Shadow AI is also on the rise—25% of respondents don’t know what AI services are running in their environment, raising further concerns about visibility and governance.

Security teams must act quickly. A hybrid approach that blends traditional cloud security with AI-native protections is no longer optional—it's essential.

## AI Adoption is Outpacing Security Expertise
Survey Data Insights: Only 13% of respondents reported no use of AI in their organizations at all. That leaves a whopping 87% of that do use AI services, most of which rely on managed offerings like OpenAI and Amazon Bedrock. This mirrors findings from Wiz's report, where 85% of organizations indicated some form of AI use, whether managed or self-hosted.

![Bar chart showing how organizations are currently using AI. Categories include: My organization is not using AI (13%), Utilizing AI platforms and Frameworks (24%), Building machine learning models in-house (34%), Using pre-trained models (36%), Using AI services (57%). Source: Pulse Report, Gatepoint Research, 2024. Copyright ©2024 Gatepoint Research. All rights reserved.]

At the same time, nearly a third of survey respondents (31%) said that a lack of AI security expertise is their biggest challenge.

![Bar chart showing the top AI security challenges. Categories include: Testing GenAI pipelines (5%), Detecting and removing attack paths to models (6%), Securing access to GenAI models (6%), Continuously monitoring for unusual activities (7%), Safeguarding sensitive training data (14%), Dealing with shadow AI (14%), Incorporating built-in guardrails and checks (17%), Lack of AI expertise in the security organization (31%). Source: Pulse Report, Gatepoint Research, 2024. Copyright ©2024 Gatepoint Research. All rights reserved.]

Why This Matters: The rapid adoption of AI services is not being matched by the development of in-house expertise to secure them. Security teams are being asked to protect systems they may not fully understand, and this expertise gap creates a growing risk surface.

Call to Action: Organizations must prioritize structured AI security frameworks and invest in upskilling programs to build internal knowledge. Until then, tooling that helps close the visibility and control gap is critical.

## AI Security Requires Both Traditional and Advanced Solutions
Survey Data Insights: Only 13% of respondents report using AI-SPM solutions today. Meanwhile, more traditional controls are widely deployed: 53% have implemented secure development practices, 41% use tenant isolation, and 35% perform audits to uncover shadow AI.

![Bar chart showing strategies implemented to manage AI security risks. Categories include: We aren’t implementing any strategies right now (20%), Using advanced security solutions (AI-SPM) (13%), Comprehensive threat modeling (28%), Conduct regular audits to remove shadow AI (35%), Tenant isolation (41%), Secure development practices (53%). Source: Pulse Report, Gatepoint Research, 2024. Copyright ©2024 Gatepoint Research. All rights reserved.]

Why This Matters: Traditional security practices still have a key role to play in securing AI systems. Protecting the software development lifecycle (SDLC), enforcing isolation between tenants, and conducting regular audits are all critical foundations. However, they are not enough on their own. As AI usage grows, so too does the sophistication of associated risks—and current strategies aren't equipped to address the speed or scale of adoption.

One area that deserves greater attention is tenant isolation. In a multi-tenant GenAI architecture, improper segmentation can expose data between workloads and users. As highlighted in Wiz's blog on GenAI tenant isolation[^2], AI workloads often run in environments where shared infrastructure or dependencies create implicit trust boundaries. If these boundaries aren’t explicitly defined and enforced, attackers may be able to move laterally between tenants or access sensitive outputs from unrelated workloads. The blog also outlines architectural design patterns to mitigate these risks, including granular IAM, scoped permissions, and environment-specific model registries.

In Wiz's State of AI report, we highlighted the rise of open-source models like DeepSeek-R1, which surpassed 130,000 downloads. With more organizations turning to self-hosted models, it’s clear that manual discovery and auditing processes are no longer sufficient.

Call to Action: Security programs must take a layered approach: foundational best practices need to be complemented with AI-specific protections. Organizations should adopt **CSPM** and **CNAPP** to address broader cloud posture while leveraging AI-SPM for discovering and securing AI-specific risks like shadow usage, model exposures, and data leakage. Isolation must be explicit, not assumed—especially in GenAI environments.

## Cloud Security Architectures Are Increasingly Complex
Survey Data Insights: Many respondents (45%) say they operate in hybrid cloud environments, while 33% use multi-cloud setups. Only 22% have a single-cloud architecture. Despite this complexity, security tooling remains rooted in endpoint-focused strategies—EDR is deployed by 70% of respondents, while only about a third use cloud-native platforms like CNAPP or CSPM.

![Bar chart showing current cloud architecture types. Categories include: Single Cloud (22%), Multi-Cloud (33%), Hybrid Cloud (45%). Source: Pulse Report, Gatepoint Research, 2024. Copyright ©2024 Gatepoint Research. All rights reserved.]

Why This Matters: AI workloads don’t live in a vacuum. They span containerized services, serverless compute, and APIs across different cloud providers. Yet most security controls in use are designed for a more centralized IT model. This disconnect creates visibility gaps, increases misconfiguration risk, and exposes sensitive AI models and training data to threats.

Call to Action: Organizations should prioritize security tools built for modern, distributed environments. CNAPP and CSPM offer visibility into cloud-native services and AI workloads running across environments. A holistic approach to cloud security that includes AI posture management is crucial to addressing today’s risks.

## AI Security Challenges Are Not Just Technical—They’re Operational
Survey Data Insights: When asked about top priorities for AI security solutions, respondents pointed to data privacy (69%), threat visibility (62%), and ease of integration (51%).

![Bar chart showing key features sought in a new AI security solution. Categories include: Low performance overhead (19%), Vendor reputation/innovation (27%), Usability (45%), Protection against model/training tampering (46%), Robust protection against adversarial attacks (50%), Ease of integration (51%), Threat landscape visibility and awareness (62%), Data privacy (69%).]

However, 25% also admitted they don’t know what AI services are in use in their environments.

![Bar chart showing AI services and technologies currently running in environments. Categories include: I don’t know (25%), SDKs (19%), AI APIs and Frameworks (e.g., Hugging Face Transformers) (21%), AI models (33%), Managed services (OpenAI, Amazon Sagemaker, etc.) (49%).]

Why This Matters: While many organizations understand what they want from AI security, fewer know how to operationalize it. Tools that are difficult to integrate stall adoption. Worse, a lack of visibility into deployed services—or shadow AI—makes it impossible to defend against threats you can’t see. This isn’t just a technology problem. It’s a workflow and awareness issue, often compounded by decentralized AI experimentation.

Call to Action: To bridge the gap, security tools must be designed to fit into existing cloud and DevOps workflows without requiring major change management. Automation should drive discovery and risk reduction, not add overhead.

## Evaluating Security Maturity
Wiz’s Cloud Security Maturity Framework outlines how modern