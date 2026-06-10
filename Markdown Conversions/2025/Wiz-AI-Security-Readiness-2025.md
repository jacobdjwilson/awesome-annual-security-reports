# AI Security Readiness

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [AI Adoption is Outpacing Security Expertise](#ai-adoption-is-outpacing-security-expertise)
- [AI Security Requires Both Traditional and Advanced Solutions](#ai-security-requires-both-traditional-and-advanced-solutions)
- [Cloud Security Architectures Are Increasingly Complex](#cloud-security-architectures-are-increasingly-complex)
- [AI Security Challenges Are Not Just Technical—They’re Operational](#ai-security-challenges-are-not-just-technical—they’re-operational)
- [Evaluating Security Maturity](#evaluating-security-maturity)
- [Recommendations: How to Close the AI Security Gap](#recommendations-how-to-close-the-ai-security-gap)
- [Future-Proofing AI Security](#future-proofing-ai-security)
- [Learn More](#learn-more)

---

## Introduction
In late 2024, Gatepoint Research invited a select group of professionals to participate in a survey titled "Navigating the Future of AI Security." The 100 respondents spanned 96 unique organizations, and included engineers, architects, CxOs, VPs, directors, and managers across various industries. They were asked to report on their cloud adoption journeys, current cloud architectures, AI usage patterns, top AI security challenges, and the strategies they’ve implemented to manage those risks. In this ebook, we explore AI adoption and security trends from that survey data.

## Executive Summary
The AI adoption is nearly universal, but security isn’t keeping up.

According to our survey, 87% of respondents are using AI services. This aligns with Wiz’s State of AI in the Cloud 2025 report,[^1] where we found that over 85% of respondents are currently using either managed or self-hosted AI services or tools. However, the adoption of security best practices is not keeping pace.

31% of respondents cite a lack of AI security expertise as their top challenge. The rate of innovation in AI can't afford to wait for security to upskill. This gap increases risk exposure and makes tooling and automation critical.

While traditional security approaches like EDR and vulnerability management remain prevalent (adopted by 70% and 65% of respondent respectively), only 13% of respondents have adopted AI-specific posture management (AI-SPM). Shadow AI is also on the rise—25% of respondents don’t know what AI services are running in their environment, raising further concerns about visibility and governance.

Security teams must act quickly. A hybrid approach that blends traditional cloud security with AI-native protections is no longer optional—it's essential.

## AI Adoption is Outpacing Security Expertise
Survey Data Insights: Only 13% of respondents reported no use of AI in their organizations at all. That leaves a whopping 87% that do use AI services, most of which rely on managed offerings like OpenAI and Amazon Bedrock. This mirrors findings from Wiz's report, where 85% of organizations indicated some form of AI use, whether managed or self-hosted.

![Chart: How is your organization using AI currently? (13% Not using, 24% Utilizing platforms/frameworks, 34% Building in-house, 36% Using pre-trained models, 57% Using AI services)]

At the same time, nearly a third of survey respondents (31%) said that a lack of AI security expertise is their biggest challenge.

![Chart: Top AI security challenges (31% Lack of AI expertise, 17% Guardrails, 14% Shadow AI, 14% Safeguarding training data, 7% Monitoring, 6% Access, 6% Attack paths, 5% Testing pipelines)]

**Why This Matters:** The rapid adoption of AI services is not being matched by the development of in-house expertise to secure them. Security teams are being asked to protect systems they may not fully understand, and this expertise gap creates a growing risk surface.

**Call to Action:** Organizations must prioritize structured AI security frameworks and invest in upskilling programs to build internal knowledge. Until then, tooling that helps close the visibility and control gap is critical.

## AI Security Requires Both Traditional and Advanced Solutions
Survey Data Insights: Only 13% of respondents report using AI-SPM solutions today. Meanwhile, more traditional controls are widely deployed: 53% have implemented secure development practices, 41% use tenant isolation, and 35% perform audits to uncover shadow AI.

![Chart: Strategies for managing AI security risks (53% Secure development, 41% Tenant isolation, 35% Audits, 28% Threat modeling, 13% AI-SPM, 20% None)]

**Why This Matters:** Traditional security practices still have a key role to play in securing AI systems. Protecting the software development lifecycle (SDLC), enforcing isolation between tenants, and conducting regular audits are all critical foundations. However, they are not enough on their own. As AI usage grows, so too does the sophistication of associated risks—and current strategies aren't equipped to address the speed or scale of adoption.

One area that deserves greater attention is tenant isolation. In a multi-tenant GenAI architecture, improper segmentation can expose data between workloads and users. As highlighted in Wiz's blog on GenAI tenant isolation, AI workloads often run in environments where shared infrastructure or dependencies create implicit trust boundaries.

**Call to Action:** Security programs must take a layered approach: foundational best practices need to be complemented with AI-specific protections. Organizations should adopt CSPM and CNAPP to address broader cloud posture while leveraging AI-SPM for discovering and securing AI-specific risks like shadow usage, model exposures, and data leakage. Isolation must be explicit, not assumed—especially in GenAI environments.

## Cloud Security Architectures Are Increasingly Complex
Survey Data Insights: Many respondents (45%) say they operate in hybrid cloud environments, while 33% use multi-cloud setups. Only 22% have a single-cloud architecture. Despite this complexity, security tooling remains rooted in endpoint-focused strategies—EDR is deployed by 70% of respondents, while only about a third use cloud-native platforms like CNAPP or CSPM.

![Chart: Cloud architecture (45% Hybrid, 33% Multi-Cloud, 22% Single Cloud)]

**Why This Matters:** AI workloads don’t live in a vacuum. They span containerized services, serverless compute, and APIs across different cloud providers. Yet most security controls in use are designed for a more centralized IT model. This disconnect creates visibility gaps, increases misconfiguration risk, and exposes sensitive AI models and training data to threats.

**Call to Action:** Organizations should prioritize security tools built for modern, distributed environments. CNAPP and CSPM offer visibility into cloud-native services and AI workloads running across environments. A holistic approach to cloud security that includes AI posture management is crucial to addressing today’s risks.

## AI Security Challenges Are Not Just Technical—They’re Operational
Survey Data Insights: When asked about top priorities for AI security solutions, respondents pointed to data privacy (69%), threat visibility (62%), and ease of integration (51%). However, 25% also admitted they don’t know what AI services are in use in their environments.

![Chart: AI services in environment (49% Managed services, 33% AI models, 21% AI APIs/Frameworks, 19% SDKs, 25% I don't know)]

**Why This Matters:** While many organizations understand what they want from AI security, fewer know how to operationalize it. Tools that are difficult to integrate stall adoption. Worse, a lack of visibility into deployed services—or shadow AI—makes it impossible to defend against threats you can’t see. This isn’t just a technology problem. It’s a workflow and awareness issue, often compounded by decentralized AI experimentation.

**Call to Action:** To bridge the gap, security tools must be designed to fit into existing cloud and DevOps workflows without requiring major change management. Automation should drive discovery and risk reduction, not add overhead.

## Evaluating Security Maturity
Wiz’s Cloud Security Maturity Framework outlines how modern teams evolve from simply gaining visibility to fully transforming how security is embedded across development and operations.

**Phase 1: Gain Visibility** (Experimental AI - High Risk)
Focus: Discovery, inventory, shadow AI detection, foundational posture visibility.

**Phase 2: Reduce Critical Risk** (Early AI Governance - Elevated Risk)
Focus: Tenant isolation, secure SDLC for AI apps, prioritizing risks with AI context.

**Phase 3: Democratize Security & Develop Securely** (AI-Integrated Security - Reduced Risk)
Focus: Discovery, inventory, shadow AI detection, foundational posture visibility.

**Phase 4: Transform Cloud SecOps** (Proactive, Automated AI Security)
Focus: Runtime policy enforcement, automated response, AI-aware threat modeling.

## Recommendations: How to Close the AI Security Gap
- **Adopt tools that continuously scan for new services, models, and shadow AI**: Manual audits can’t keep up with the scale and speed of AI usage growth.
- **Integrate security early in the development lifecycle**: Shifting security left allows teams to address misconfigurations and vulnerabilities during design and build phases.
- **Ensure security controls follow AI workloads across environments**: Security must move with workloads, providing consistent policy enforcement regardless of infrastructure.
- **Equip security teams with AI-specific training and tools**: Upskilling programs and better collaboration between security and data teams are essential.

## Future-Proofing AI Security
AI is evolving quickly—and so are the risks. Staying secure means keeping a constant pulse on how AI is used and adapting defenses in real time. Security can’t be reactive. It must be continuous and proactive. Teams that invest in AI security posture today will be better equipped to scale innovation safely tomorrow.

## Learn More
Wiz’s AI Security Posture Management (AI-SPM) solution enables teams to discover AI usage, detect and remediate shadow AI, monitor and secure models and data pipelines, and empower developers and security teams to innovate safely. Explore full AI visibility with our Sample Assessment Report.

---
[^1]: Wiz’s State of AI in the Cloud 2025 report.