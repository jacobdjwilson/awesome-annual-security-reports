# The AI Builder’s Playbook: 2025 State of AI Report

**Organization:** Iconiq  
**Year:** 2025  
**Status:** Private and Strictly Confidential  
**Audience:** For Professional Clients Only

---

## Table of Contents
- [Introduction](#introduction)
- [Data Sources & Methodology](#data-sources--methodology)
- [AI Maturity](#ai-maturity)
- [Building GenAI Products](#building-genai-products)
    - [Stage of Primary AI Product](#stage-of-primary-ai-product)
    - [Types of AI Products](#types-of-ai-products)
    - [Model Usage](#model-usage)
    - [Top Considerations for Foundational Models: Product Development](#top-considerations-for-foundational-models-product-development)
    - [Top Model Providers](#top-model-providers)
    - [Model Training Techniques](#model-training-techniques)
    - [AI Infrastructure](#ai-infrastructure)
    - [Model Deployment Challenges: Product Development](#model-deployment-challenges-product-development)
    - [AI Performance Monitoring](#ai-performance-monitoring)
    - [Agentic Workflows](#agentic-workflows)
- [Go-to-Market Strategy & Compliance](#go-to-market-strategy--compliance)
    - [AI Product Roadmap](#ai-product-roadmap)
    - [Primary Pricing Model](#primary-pricing-model)
    - [Pricing Models for AI Features](#pricing-models-for-ai-features)
    - [Pricing Changes](#pricing-changes)
    - [AI Explainability and Transparency](#ai-explainability-and-transparency)
    - [AI Compliance and Governance](#ai-compliance-and-governance)
- [Organization Structure](#organization-structure)
    - [Dedicated AI/ML Leadership](#dedicated-aiml-leadership)
    - [AI-Specific Roles](#ai-specific-roles)
    - [Pace of Hiring](#pace-of-hiring)
    - [% of Engineering Team Focused on AI](#-of-engineering-team-focused-on-ai)
- [AI Costs](#ai-costs)
    - [AI Development Spend](#ai-development-spend)
    - [Budget Allocation](#budget-allocation)
    - [Infrastructure Costs](#infrastructure-costs)
    - [Cost Optimization](#cost-optimization)
    - [Model Training](#model-training)
    - [Deployment Costs: Inference](#deployment-costs-inference)
    - [Deployment Costs: Data Storage & Processing](#deployment-costs-data-storage--processing)
- [Internal Productivity](#internal-productivity)
    - [Annual Internal Productivity Budget](#annual-internal-productivity-budget)
    - [Internal Productivity Budget Sources for Enterprises](#internal-productivity-budget-sources-for-enterprises)
    - [AI Access and Usage](#ai-access-and-usage)
    - [Top Considerations for Foundational Models: Internal Use Cases](#top-considerations-for-foundational-models-internal-use-cases)
    - [Model Deployment Challenges: Internal Use Cases](#model-deployment-challenges-internal-use-cases)
    - [Number of Use Cases](#number-of-use-cases)
    - [Top Use Cases: By Popularity](#top-use-cases-by-popularity)
    - [Top Use Cases: By Impact](#top-use-cases-by-impact)
    - [Attitude Towards Internal AI Adoption](#attitude-towards-internal-ai-adoption)
    - [Tracking ROI](#tracking-roi)
- [AI Builder Tech Stack](#ai-builder-tech-stack)
    - [Most Used Tools: Model Training & Finetuning](#most-used-tools-model-training--finetuning)
    - [Most Used Tools: LLM & AI Application Development](#most-used-tools-llm--ai-application-development)
    - [Most Used Tools: Monitoring and Observability](#most-used-tools-monitoring-and-observability)
    - [Most Used Tools: Inference Optimization](#most-used-tools-inference-optimization)
    - [Most Used Tools: Model Hosting](#most-used-tools-model-hosting)
    - [Most Used Tools: Model Evaluation](#most-used-tools-model-evaluation)
    - [Most Used Tools: Data Processing & Feature Engineering](#most-used-tools-data-processing--feature-engineering)
    - [Most Used Tools: Vector Databases](#most-used-tools-vector-databases)
    - [Most Used Tools: Synthetic Data & Data Augmentation](#most-used-tools-synthetic-data--data-augmentation)

---

## Introduction

We believe that building and operationalizing AI products is the new frontier of competitive advantage – and that the voices of the architects, engineers, and product leaders driving this work deserve their own spotlight. While last year’s State of AI report centered on the buying journey and enterprise adoption dynamics, our 2025 report pivots squarely to the “how-to”: what it takes to conceive, deliver, and scale AI-powered offerings end-to-end.

This year’s report unpacks core dimensions of the builder’s playbook:
1. **Product Roadmap & Architecture**: The emerging best practices for balancing experimentation, speed to market, and performance at each stage of model evolution.
2. **Go-to-Market Strategy**: How teams are aligning pricing models and go-to-market strategies to reflect AI’s unique value drivers.
3. **People & Talent**: Building the right team to harness AI expertise, foster cross-functional collaboration, and sustain long-term innovation.
4. **Cost Management & ROI**: Strategies and benchmarks for spend associated with building and launching AI products.
5. **Internal Productivity & Operations**: How companies are embedding AI into everyday workflows and the biggest drivers of productivity unlock.

---

## Data Sources & Methodology

This study summarizes data from an April 2025 survey of 300 executives at software companies building AI products, including CEOs, Heads of Engineering, Heads of AI, and Heads of Product.

### Respondent Firmographics
- **Headquarters**: 88% North America, 12% Europe.
- **Revenue Range**: 26% <$10M, 13% $10M-$25M, 10% $25M-$50M, 9% $50M-$100M, 7% $100M-$200M, 13% $200M-$500M, 11% $500M-$1B, 8% $1B+.

### High-Growth Companies Definition
Select companies are referred to as “high growth companies” because they meet the following criteria:
- **AI Product Traction**: AI product is in General Availability or Scaling.
- **Revenue**: At least $10M in annual revenue.
- **Topline Growth**: 100%+ YoY revenue growth if <$25M Revenue; 50%+ YoY if $25M-$250M; 30%+ YoY if $250M+.

![Chart showing respondent firmographics and high-growth company criteria]

---

## AI Maturity

Most SaaS companies have evolved to add new AI capabilities and products.

| Category | Description | % of Respondents |
| :--- | :--- | :--- |
| **Traditional SaaS** | Delivery of subscription-based applications built around core business workflows. | N/A |
| **AI-Enabled (Capabilities)** | Embedded AI-powered features into flagship offerings to boost automation and productivity. | 31% |
| **AI-Enabled (New Product)** | Standalone AI-driven product or services alongside core product portfolio. | 37% |
| **AI-Native** | Entire value proposition is architected around generative intelligence. | 32% |

---

## Building GenAI Products

### Stage of Primary AI Product
AI-native companies are further along in the development cycle compared to AI-enabled peers.

- **Scaling**: 47% (AI-Native) vs. 13% (AI-Enabled)
- **General Availability**: 42% (AI-Native) vs. 42% (AI-Enabled)
- **Beta**: 10% (AI-Native) vs. 34% (AI-Enabled)
- **Pre-Launch**: 1% (AI-Native) vs. 11% (AI-Enabled)

![Chart comparing product maturity stages between AI-Native and AI-Enabled companies]

### Types of AI Products
Agentic workflows and the application layer are the most common products.
- **Agentic Workflows**: 79% (AI-Native) vs. 62% (AI-Enabled)
- **Vertical AI Applications**: 65% (AI-Native) vs. 57% (AI-Enabled)
- **Horizontal AI Applications**: 56% (AI-Native) vs. 55% (AI-Enabled)
- **AI Platforms / Infrastructure**: 49% (AI-Native) vs. 48% (AI-Enabled)
- **Core AI Models / Technologies**: 40% (AI-Native) vs. 27% (AI-Enabled)

### Model Usage
High-growth companies are more likely to fine-tune or develop proprietary models.
- **Rely on third-party AI APIs**: 80% (High Growth) vs. 71% (Other)
- **Fine-tune existing foundation models**: 77% (High Growth) vs. 61% (Other)
- **Develop proprietary models from scratch**: 54% (High Growth) vs. 32% (Other)

### Top Considerations for Foundational Models: Product Development
1. **Accuracy**: 74%
2. **Cost**: 57%
3. **Ability to fine-tune**: 41%
4. **Privacy**: 34%
5. **Latency**: 25%

### Top Model Providers
OpenAI remains dominant, but multi-model approaches are increasing (Average 2.8 models per respondent).
- **OpenAI / GPT**: 95%
- **Anthropic / Claude**: 81%
- **Google / Gemini**: 78%
- **Meta / Llama**: 54%
- **Mistral AI**: 55%
- **DeepSeek**: 55%

> "We use different proprietary and 3rd party models because our customers have diverse needs... specialized models allow us to better tailor the experiences."  
> — *VP Product, $1B+ Revenue, Full Stack AI Company*

### Model Training Techniques
- **RAG**: 69% (High Growth) vs. 66% (Other)
- **Fine-tuning**: 68% (High Growth) vs. 67% (Other)
- **Few-Shot Learning**: 67% (High Growth) vs. 49% (Other)

### AI Infrastructure
- **Fully cloud-based**: 68%
- **External AI API providers**: 64%
- **Hybrid**: 23%
- **Dedicated inference providers**: 10%

### Model Deployment Challenges: Product Development
1. **Hallucinations**: 39%
2. **Explainability & Trust**: 38%
3. **Proving ROI**: 34%
4. **Compute Cost**: 32%

### AI Performance Monitoring
As products scale, monitoring becomes more automated.
- **Scaling Products**: 44% use fully automated pipelines; 40% use advanced monitoring.
- **Pre-Launch**: 75% use basic monitoring; 19% have no formal monitoring.

### Agentic Workflows
- **Actively deploying in production**: 47% (High Growth) vs. 32% (Other)
- **Experimenting in pilots**: 42% (High Growth) vs. 32% (Other)

---

## Go-to-Market Strategy & Compliance

### AI Product Roadmap
Percentage of product roadmap focused on AI-driven features:
- **High Growth**: 31% (End of 2024) → 43% (Estimated End of 2025)
- **All Other**: 22% (End of 2024) → 36% (Estimated End of 2025)

### Primary Pricing Model
- **Hybrid**: 38%
- **Subscription / Seat-based**: 36%
- **Usage-based**: 19%
- **Outcome-based**: 6%

### Pricing Models for AI Features
- **Part of premium-tier**: 40%
- **Included at no extra cost**: 33%
- **Separate usage-based model**: 21%

### Pricing Changes
37% of companies plan to change AI pricing in the next 12 months.
> "The subscription model is not working for us. Power users tend to use a lot resulting in negative margins... we are planning to move to usage based."  
> — *VP Product, $100-150M Revenue*

### AI Explainability and Transparency
- **Scaling Products**: 25% provide detailed reports; 47% offer basic insights.
- **Pre-Launch**: 64% offer basic insights; 26% provide no specific explanations.

### AI Compliance and Governance
- **Human-in-the-loop oversight**: 66%
- **Formal AI ethics policies**: 47%
- **Explainability measures**: 42%
- **Dedicated AI compliance team**: 13%

---

## Organization Structure

### Dedicated AI/ML Leadership
- **<$100M Revenue**: 33% have dedicated leadership.
- **$1B+ Revenue**: 47% have dedicated leadership.

### AI-Specific Roles
- **AI/ML Engineers**: 88% (Currently have), 70 days (Avg lead time to hire).
- **Data Scientists**: 72% (Currently have), 68 days (Avg lead time to hire).
- **AI Product Managers**: 67% (Currently have), 67 days (Avg lead time to hire).

### Pace of Hiring
- **Hiring fast enough**: 54%
- **Not fast enough**: 46% (Main reason: 60% cite lack of qualified candidates).

### % of Engineering Team Focused on AI
- **High Growth**: 28% (2025) → 37% (2026)
- **All Other**: 18% (2025) → 28% (2026)

---

## AI Costs

### AI Development Spend
Average allocation of R&D budget to AI:
- **<$100M Revenue**: 25% (2025 Budget)
- **$1B+ Revenue**: 15% (2025 Budget)

### Budget Allocation
- **AI Talent**: 57% (Pre-Launch) → 36% (Scaling)
- **AI Infrastructure**: 13% (Pre-Launch) → 22% (Scaling)
- **AI Model Inference**: 4% (Pre-Launch) → 10% (Scaling)

### Infrastructure Costs
Most challenging costs to control:
1. **API usage fees**: 70%
2. **Inference costs**: 49%
3. **Model retraining**: 48%

### Cost Optimization
- **Moving to open-source models**: 41%
- **Optimizing inference efficiency**: 37%
- **Model distillation/quantization**: 28%

### Model Training
- **Frequency**: 31% retrain monthly; 20% multiple times per week.
- **Monthly Costs**: $163K (Pre-Launch) → $1.5M (Scaling).

### Deployment Costs: Inference
Monthly spend for inference:
- **High Growth**: $2.3M (Scaling)
- **Other Companies**: $1.1M (Scaling)

### Deployment Costs: Data Storage & Processing
- **Data Storage (Scaling)**: $2.6M (High Growth) vs. $1.6M (Other).
- **Data Processing (Scaling)**: $2.0M (High Growth) vs. $1.6M (Other).

---

## Internal Productivity

### Annual Internal Productivity Budget
Budgets are set to nearly double in 2025.
- **$1B+ Revenue Companies**: $34.2M (2024) → $60.4M (2025 Est).
- **$100M-$200M Revenue**: $1.0M (2024) → $1.8M (2025 Est).

### Internal Productivity Budget Sources for Enterprises
- **R&D Budget**: 48%
- **Business Unit Initiatives**: 57%
- **Headcount Budget**: 27%

### AI Access and Usage
- **Access**: ~70% of employees have access.
- **Usage**: ~50% use tools on an ongoing basis.
> "Just deploying tools is a recipe for disappointment... you need to pair availability with scaffolding that includes training and relentless executive support."  
> — *Don Vu, SVP, Chief Data & Analytics Officer, New York Life*

### Top Considerations for Foundational Models: Internal Use Cases
1. **Cost**: 74%
2. **Accuracy**: 72%
3. **Privacy**: 50%

### Model Deployment Challenges: Internal Use Cases
1. **Finding right use cases**: 46%
2. **Proving ROI**: 42%
3. **Explainability & Trust**: 32%

### Number of Use Cases
- **High Adoption Companies**: 7.1 average use cases.
- **Low Adoption Companies**: 4.6 average use cases.

### Top Use Cases: By Popularity
- **Coding Assistance**: 77%
- **Content Generation**: 65%
- **Documentation/Knowledge Retrieval**: 57%

### Top Use Cases: By Impact
1. **Coding Assistance**: 65% (High growth companies write 33% of code with AI).
2. **Content Generation**: 37%
3. **Documentation**: 30%

### Attitude Towards Internal AI Adoption
- **High Growth**: 92% actively experiment with and adopt new tools.
- **All Other**: 80% actively experiment.

### Tracking ROI
- **Productivity Gains**: 75%
- **Cost Savings**: 51%
- **Revenue Uplift**: 20%

---

## AI Builder Tech Stack

### Most Used Tools: Model Training & Finetuning
- **Frameworks**: PyTorch, TensorFlow.
- **Managed Platforms**: AWS SageMaker, OpenAI Fine-tuning.
- **Ecosystem**: Hugging Face, Databricks Mosaic AI.

### Most Used Tools: LLM & AI Application Development
- **Orchestration**: LangChain, Hugging Face.
- **Safety/SDKs**: Guardrails, Vercel AI SDK.
- **APIs**: Private/Custom LLM APIs (70% of respondents).

### Most Used Tools: Monitoring and Observability
- **Incumbents**: Datadog, Honeycomb, New Relic.
- **ML-Native**: LangSmith, Weights & Biases (17% adoption).

### Most Used Tools: Inference Optimization
- **NVIDIA Stack**: TensorRT, Triton Inference Server (60%+ combined).
- **Cross-Platform**: ONNX Runtime (18%), TorchServe (15%).

### Most Used Tools: Model Hosting
- **Direct Provider**: OpenAI, Anthropic.
- **Hyperscalers**: AWS Bedrock, Google Vertex AI.

### Most Used Tools: Model Evaluation
- **Built-in**: Vertex, Weights & Biases, Galileo.
- **Specialized**: LangSmith, Langfuse, HumanLoop, Braintrust.

### Most Used Tools: Data Processing & Feature Engineering
- **Big Data**: Apache Spark (44%), Kafka (42%).
- **Python**: Pandas (41%).
- **Feature Stores**: 17% usage (Emerging).

### Most Used Tools: Vector Databases
- **Leaders**: Elastic, Pinecone.
- **In-Memory/Other**: Redis, Clickhouse, Milvus, PGVector.
- **Open Source**: Chroma, Weaviate, Qdrant.

### Most Used Tools: Synthetic Data & Data Augmentation
- **Custom**: In-house tooling (52%).
- **Vendor Leader**: Scale AI (21%).
- **Programmatic**: Snorkel AI, Mostly AI.

---
*Private & Strictly Confidential*  
*Copyright © 2025 ICONIQ Capital, LLC. All Rights Reserved*

---

ed or recommended the services of ICONIQ.
Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

58

Most Used Tools: Coding Assistance

Key Takeaways

Most Widely Used Tools
From survey respondents; By alphabetical order

Dominance of First Movers
• GitHub Copilot is used by nearly three-quarters of development teams, thanks to its tight VS Code

integration, multi-language support, and backing by GitHub’s massive user base

• Copilot’s network effects and product-market fit make it hard to dislodge, but the strong second-

place showing for Cursor (used by 50% of respondents) signals appetite for diverse IDE integrations

Long Tail of Offerings Lag
• After the top two, adoption drops off sharply with a fractured long tail of solutions, suggesting that
while most teams have trialed at least one assistant, very few have standardized on alternatives
• Low-code or no-code solutions like Retool, Lovable, Bolt, and Replit also had honorable mentions

indicating that there is increasing appetite in the market for idea-to-application solutions

Notes: Trademarks are the property of their respective owners. None of the companies illustrated have endorsed or recommended the services of ICONIQ.
Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

59

Most Used Tools: DevOps and MLOps

Key Takeaways

Most Widely Used Tools
From survey respondents; By alphabetical order

MLflow Leads—but No Monopoly
• MLflow was used by 36% of respondents and the clear frontrunner for experiment tracking, model
registry, and basic pipeline orchestration – this is only just over one-third of teams, indicating
plenty of room for alternatives

• Weights & Biases also holds strong share with 20% of respondents using, reflecting its appeal as a

managed SaaS for tracking, visualization, and collaboration

• Beyond the top two, usage quickly fragments – 16% “don’t know” which tools power their MLOps
and other tool mentions include Resolve.ai, Cleric, PlayerZero, Braintrust, etc. This points to both
confusion around responsibilities (DevOps vs. MLOps) and a market still sorting itself out

Gap between Tracking and Full-Scale Ops
• The dominance of tracking-first platforms like MLflow and W&B suggests that many teams haven’t
yet adopted end-to-end MLOps suites - continuous delivery, drift monitoring, or automated rollback
remain work in progress for most

Notes: Trademarks are the property of their respective owners. None of the companies illustrated have endorsed or recommended the services of ICONIQ.
Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

60

Most Used Tools: Product and Design

Key Takeaways

Most Widely Used Tools
From survey respondents; By alphabetical order

Figma’s Near-Universal Reach
• With 87% adoption, Figma is effectively the de-facto standard for UI/UX and product design - teams
overwhelmingly stick with its real-time collaboration, component libraries, and plugin ecosystem
rather than seeking out AI-specific design tools

Miro for Higher-Level Collaboration
• With 37% adoption, Miro remains the go-to for wireframing, user-journey mapping, and cross-
functional brainstorming; its whiteboard-style interface complements Figma’s pixel-perfect
canvases, especially in early ideation phases

Rise of AI-Enabled Product Wireframes
• Design teams aren’t yet feeling the urgent need for AI-native product/design platforms, however

many are using low/no-code solutions to Bolt, Lovable, and Vercel V0 for rapid protoyping

Notes: Trademarks are the property of their respective owners. None of the companies illustrated have endorsed or recommended the services of ICONIQ.
Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

61

Internal Productivity Use Cases (Part 1 of 2)

For more
information on
specific tools in
each category,
please reach out
to ICONIQ
Insights

Use Case

Key Trends

Sales Productivity

• Many teams are getting their AI-powered sales features straight out of Salesforce - indicating that an easy path is to lean on
your existing CRM’s built-in recommendations, forecasting, and opportunity-scoring rather than bolt on a separate service
• Other respondents are also using sales-engagement platforms like Apollo, Salesloft, Gong, etc, while others are also leaning

into AI driven prospecting tools like Clay and People.ai

• As embedded capabilities mature, we will likely see consolidation around a handful of platforms or clearer differentiation from

the point-solution upstarts

Marketing
Automation &
Content Generation

• Marketers overwhelmingly turn to Canva’s generative features for on-brand visuals and quick content iterations, making it by

far the most common “AI” touchpoint in the marketing stack

• Many respondents are also using solutions like n8n or homegrown solutions, indicating that marketing use cases sometimes

require a high degree of in-house customization

• Many respondents are also using specialized AI writing tools like Writer and Jasper, with adoption higher for later stage

companies ($100M+ revenue)

Customer
Engagement

• Teams overwhelmingly rely on Zendesk or Salesforce’s embedded AI features for customer interactions, signaling that ease of

plugging into existing ticketing and CRM workflows still beats adopting a standalone conversational AI platform
• A sizable minority lean on specialist tools like Pylon, Forethought, Grano.la, or Intercom when they need deeper bot

customizations, self-service wizards, or tight in-app support widgets - suggesting that best-of-breed still has a role when out-
of-the-box AI falls short

Documentation and
Knowledge
Retrieval

• Most teams either build on existing wikis and note-taking tools or standardize on Notion; this shows that organizations often

default to whatever’s already in place for knowledge capture before experimenting with AI-powered overlays

• However, a sizable proportion of respondents are also leaning into purpose-built AI tools like Glean and Writer for indexing

and semantic search

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

62

Internal Productivity Use Cases (Part 2 of 2)

For more
information on
specific tools in
each category,
please reach out
to ICONIQ
Insights

Use Case

IT & Security

Legal

Key Trends

• ServiceNow (used by 33% of respondents) and Snyk (used by 30% of respondents) lead the pack, showing that large

organizations are still defaulting to their existing ITSM and security-scanning platforms rather than standing up brand-new AI
tools

• Zapier and Workato were also commonly mentioned, underlining how much teams value low-code orchestration for stitching

together alerts, ticket creation, and remediation scripts across disparate tools

• Legal departments are dipping toes into AI primarily through ChatGPT and ad hoc scripts, but purpose-built legal assistant

platforms are starting to gain traction

• As regulation and security concerns mount, we’ll likely see a bifurcation: mainstream LLMs for informal research and

compliance-focused suites for mission-critical contract workflows

HR & Recruiting

• Nearly half of teams rely on LinkedIn’s built-in AI features - profile suggestions, candidate matching, and outreach

sequencing - underscoring that recruiters lean on platforms they already use daily rather than integrating standalone solutions

• However, niche platforms like HireVue for AI-driven video interviews and Mercor for candidate engagement are starting to

see modest uptake

• Many teams are using Ramp for FP&A automation, likely leveraging its spend management and data sync features in an all-in-

one platform

FP&A Automation

• Specialized suites like Pigment, Basis, and Tabs are also starting to pick up traction, showing growing interest in driver-based

planning and multi-scenario modeling platforms

• Around one-third of respondents are also using homegrown solutions, reflecting investment in custom scripts, Excel macros,

and bespoke pipelines to glue together ERP, billing, and BI systems

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

63

A global portfolio of category-defining businesses

These companies represent the full list of companies that ICONIQ Venture and Growth has invested in since inception through ICONIQ Strategic Partners funds as of the date these materials were published (except those subject to confidentiality obligations or companies for
which the issuer has not provided permission for ICONIQ Venture and Growth to disclose publicly). Trademarks are the property of their respective owners. None of the companies illustrated have endorsed or recommended the services of ICONIQ.

Private & Strictly Confidential

64

Disclosures

Unless otherwise indicated, the views expressed in this presentation are those of ICONIQ (“ICONIQ” or the “Firm”), are the result of proprietary research, may be subjective, and may not be relied upon in making an investment decision.
Information used in this presentation was obtained from numerous sources. Certain of these companies are portfolio companies of ICONIQ. ICONIQ does not make any representations or warranties as to the accuracy of the information
obtained from these sources.

This presentation is for educational purposes only and does not constitute investment advice or an offer to sell or a solicitation of an offer to buy any securities in connection with any investment fund or investment product that ICONIQ
sponsors.  Any such offer or solicitation will only be made pursuant to definitive offering documents and subscription agreements.

Any reproduction or distribution of this presentation in whole or in part, or the disclosure of any of its contents, without the prior consent of ICONIQ, is prohibited.

This presentation may contain forward-looking statements based on current plans, estimates and projections. The recipient of this presentation (“you”) is cautioned that a number of important factors could cause actual results or outcomes
to differ materially from those expressed in, or implied by, the forward-looking statements. The numbers, figures and case studies contained in this presentation have been included for purposes of illustration only, and no assurance can be
given that the actual results of any ICONIQ portfolio company will correspond with the information contained in this presentation. No information is included herein with respect to conflicts of interest, which may be significant. The
portfolio companies and other parties mentioned herein may reflect a selective list of the prior investments made by ICONIQ.

Certain of the economic and market information contained herein may have been obtained from published sources and/or prepared by other parties. While such sources are believed to be reliable, none of ICONIQ or any of its affiliates and
partners, employees and representatives assume any responsibility for the accuracy of such information.

All of the information herein is presented as of the date made available to you (except as otherwise specified), and is subject to change without notice, and may not be current or may have changed (possibly materially) between the date
made  available to  you  and  the  date  actually  received or  reviewed  by  you.  ICONIQ  assumes  no  obligation  to update or  otherwise  revise  any  information,  projections,  forecasts  or  estimates  contained in this presentation,  including  any
revisions to reflect changes in economic or market conditions or other circumstances arising after the date the items were made available to you or to reflect the occurrence of unanticipated events. Numbers or amounts herein may increase
or decrease as a result of currency fluctuations.

For avoidance of doubt, ICONIQ is not acting as an adviser or fiduciary in any respect in connection with providing this presentation and no relationship shall arise between you and ICONIQ as a result of this presentation being made
available to you.

ICONIQ is a trading name of ICONIQ Partners (UK) LLP. ICONIQ Partners (UK) LLP (Registration Number: 973080) is an appointed representative of Kroll Securities Ltd. (Registration Number: 466588) which is authorised and regulated
by  the  Financial  Conduct  Authority.  ICONIQ  Partners  (UK)  LLP  is  a  limited  liability  partnership  whose  members  are  ICONIQ  Capital  (UK)  Ltd,  Seth  Pierrepont  and  Lou  Thorne,  and  it  is  registered  in  England  and  Wales  and  has  its
registered office at 27 Soho Square, London W1D 3QR. ICONIQ Partners (UK) LLP acts as an adviser to ICONIQ Capital LLC.

These materials are provided for general information and discussion purposes only and may not be relied upon. This material may be distributed to, or directed at, only the following persons: (i) persons who have professional experience in
matters relating to investments falling within article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (the “FP Order”), (ii) high-net-worth entities falling within Article 49(2) of the FP Order, and (iii)
any other persons to whom it may otherwise lawfully be communicated (all such persons together being referred to as “FPO Relevant Persons”). Persons who are not FPO Relevant Persons must not act on or rely on this material or any of its
contents. Any investment or investment activity to which this material relates is available only to FPO Relevant Persons and will be engaged in only with FPO Relevant Persons. Recipients must not distribute, publish, reproduce, or disclose
this material, in whole or in part, to any other person.

Copyright © 2025 ICONIQ Capital, LLC. All rights reserved.

Private & Strictly Confidential

65

Technology matters. Strategy matters. People matter most.
Meet the ICONIQ Venture and Growth team

Private & Strictly Confidential

66

San Francisco | Palo Alto | New York | London

Join our community

Private & Strictly Confidential
Private & Strictly Confidential