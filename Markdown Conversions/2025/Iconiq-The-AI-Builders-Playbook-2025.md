# The Builder’s Playbook

June 2025

2025 State of AI Report

Private and Strictly Confidential
Copyright © 2025 ICONIQ Capital, LLC. All Rights Reserved

For Professional Clients Only. ICONIQ Partners (UK) LLP (973080) is an appointed representative of
Kroll Securities Ltd (466458) which is authorized and regulated by the Financial Conduct Authority

![ICONIQ Capital branding image]

Follow our research

SUBSCRIBE

- Go-To-Market Series
  Guides to sales, customer success, marketing compensation
  – and more
- Navigating Today’s Public Markets
  The metrics that matter and the market realities of 2025 and
  beyond
- Growth & Efficiency
  Explore our research on best-in-class SaaS growth and
  efficiency
- The ICONIQ Enterprise Five
  Key performance indicators of Enterprise SaaS companies
- The SaaS Glossary
  A guide to understanding and tracking key SaaS metrics
- Engineering Series
  Definitive guides to engineering excellence

Private & Strictly Confidential

2

Introduction

We believe that building and operationalizing AI products is the new frontier of competitive advantage – and that the voices of the
architects, engineers, and product leaders driving this work deserve their own spotlight. While last year’s State of AI report centered
on the buying journey and enterprise adoption dynamics, our 2025 report pivots squarely to the “how-to”: what it takes to conceive,
deliver, and scale AI-powered offerings end-to-end.

This year’s report unpacks core dimensions of the builder’s playbook:
1.  Product Roadmap & Architecture: The emerging best practices for balancing experimentation, speed to market, and
    performance at each stage of model evolution
2.  Go-to-Market Strategy: How teams are aligning pricing models and go-to-market strategies to reflect AI’s unique value drivers
3.  People & Talent: Building the right team to harness AI expertise, foster cross-functional collaboration, and sustain long-term
    innovation
4.  Cost Management & ROI: Strategies and benchmarks for spend associated with building and launching AI products
5.  Internal Productivity & Operations: How companies are embedding AI into everyday workflows and the biggest drivers of
    productivity unlock

Drawing on our proprietary survey results alongside in-depth interviews with AI leaders across the ICONIQ community, the 2025
State of AI report offers a blueprint for anyone tasked with turning generative intelligence from a promising concept into a
dependable, revenue-driving asset.

Explore Our AI Perspectives

Private & Strictly Confidential

3

## Table of Contents

- [Building Generative AI Products](#building-genai-products)
  - [Types of AI Products](#types-of-ai-products)
  - [Model Usage and Key Purchasing Considerations](#model-usage-and-key-purchasing-considerations)
  - [Top Models Providers](#top-models-providers)
  - [Model Training Techniques](#model-training-techniques)
  - [AI Infrastructure](#ai-infrastructure)
  - [Model Deployment Challenges](#model-deployment-challenges)
  - [AI Performance Monitoring](#ai-performance-monitoring)
  - [Agentic Workflows](#agentic-workflows)
- [Go-to-Market Strategy & Compliance](#go-to-market-strategy--compliance)
  - [AI Product Roadmap](#ai-product-roadmap)
  - [Pricing](#pricing)
  - [AI Explainability and Transparency](#ai-explainability-and-transparency)
  - [AI Compliance and Governance](#ai-compliance-and-governance)
- [Organization Structure](#organization-structure)
  - [Dedicated AI/ML Leadership](#dedicated-aiml-leadership)
  - [AI-Specific Roles and Hiring](#ai-specific-roles-and-hiring)
  - [Pace of Hiring](#pace-of-hiring)
  - [% of Engineering team Focused on AI](#-of-engineering-team-focused-on-ai)
- [AI Costs](#ai-costs)
  - [AI Development Spend](#ai-development-spend)
  - [Budget Allocation](#budget-allocation)
  - [Infrastructure Costs](#infrastructure-costs)
  - [Model Training Costs](#model-training-costs)
  - [Inference Costs](#inference-costs)
  - [Data Storage & Processing Costs](#data-storage--processing-costs)
- [Internal Productivity](#internal-productivity)
  - [Top AI Tools](#top-ai-tools)
  - [Internal Productivity Budget](#internal-productivity-budget)
  - [Budget Sources](#budget-sources)
  - [AI Access and Usage](#ai-access-and-usage)
  - [Key Purchasing Considerations](#key-purchasing-considerations)
  - [Deployment Challenges](#deployment-challenges)
  - [Number of Use Cases](#number-of-use-cases)
  - [Top Use Cases](#top-use-cases)
  - [Attitude Towards Internal AI Adoption](#attitude-towards-internal-ai-adoption)
  - [Tracking ROI](#tracking-roi)
- [AI Builder Tech Stack](#ai-builder-tech-stack)
  - [LLM & AI Application Development](#llm--ai-application-development)
  - [Model Training & Finetuning](#model-training--finetuning)
  - [Monitoring & Observability](#monitoring--observability)
  - [Inference Optimization](#inference-optimization)
  - [Model Hosting](#model-hosting)
  - [Model Evaluation](#model-evaluation)
  - [Data Processing & Feature Engineering](#data-processing--feature-engineering)
  - [Vector Databases](#vector-databases)
  - [Synthetic Data & Data Augmentation](#synthetic-data--data-augmentation)
  - [Coding Assistance](#coding-assistance)
  - [DevOps & MLOps](#devops--mlops)
  - [Product & Design](#product--design)
  - [Other Internal Productivity Use Cases](#other-internal-productivity-use-cases)

4

Data
Sources
& Methodology

This study summarizes data
from an April 2025 survey of 300
executives at software companies
building AI products, including
CEOs, Heads of Engineering,
Heads of AI, and Heads of
Product.

Throughout this report, we also
weave in perspectives, insights,
and what we believe to be best
practices from AI leaders from
the ICONIQ community.

All industry perspectives shared
in this report have been
anonymized to protect company-
level information.

Respondent Firmographics

![Bar chart showing Revenue Range and Headquarters of survey respondents. Revenue Range: <$100M (26%), $100-$200M (13%), $200M+ (10%). Headquarters: North America (88%), Europe (12%).]

In this report, select companies are referred to as “high
growth companies” because they meet the following criteria

- AI Product Traction: AI product is in General Availability or
  Scaling
- Revenue: At least $10M in annual revenue
- Topline Growth: 100%+ YoY revenue growth if <$25M
  Revenue, 50%+ YoY revenue growth if $25M-250M Revenue,
  30%+ YoY revenue growth if $250M+ Revenue

![Bar chart showing Revenue Range for High-Growth Respondents. <$100M (55%), $100-$200M (20%), $200M+ (25%).]

Notes: (1) This data was collected anonymously by an external survey. Survey responses include some but not all ICONIQ Venture and Growth portfolio companies as well as companies not part of ICONIQ Venture and Growth’s portfolio.
(2) Certain questions in the survey were optional. Accordingly, some N-Size numbers in this presentation are less than 300

Private & Strictly Confidential

5

AI Maturity

Most SaaS companies have evolved to add new AI capabilities and products; the following pages will dive into how AI-
enabled and AI-native companies are approaching product development

![Diagram illustrating AI Maturity stages: Traditional SaaS, AI-Enabled (Adding AI Capabilities), AI-Enabled (Creating a new AI product), and AI-Native. Each stage has a description and representative examples (logos of companies like Salesforce, Workday, Adobe, Microsoft, ServiceNow, Datadog, Snowflake, Databricks, OpenAI, Anthropic, Cohere, Jasper, Midjourney, Stability AI). Percentages of survey respondents in each category are shown: Traditional SaaS (31%), AI-Enabled Adding Capabilities (37%), AI-Enabled New Product (32%), AI-Native (Focus of this report, percentage not shown explicitly for AI-Native category as a whole, but implied by the sum of the other categories not being 100%).]

Traditional SaaS

Traditional Software-as-a-Service

Delivery of subscription-based
applications built around core
business workflows

31% of survey respondents

AI-Enabled: Adding AI Capabilities
to Existing Products

Embedded AI-powered features into
flagship offerings to boost
automation, personalization, and end-
user productivity—while leaving
underlying business model and UX
largely intact

37% of survey respondents

AI-Enabled: Creating a new (non-
core) AI product

Standalone AI-driven product or
services alongside core product
portfolio to explore adjacent use
cases and revenue streams

32% of survey respondents

AI-Native: Core product or business
model is AI-driven

Entire value proposition is architected
around generative intelligence —where
model training, inference, and
continuous learning are the fundamental
drivers of customer value and growth

Representative
Examples

Notes: Representative Examples provided for illustrative purposes only. Trademarks are the property of their respective owners. None of the companies illustrated have endorsed or recommended the services of ICONIQ.
Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our
Technical Advisory Board, and others in our network

Private & Strictly Confidential

6

Focus of this report

## Building GenAI Products

![Abstract image related to AI/technology]

Private and Strictly Confidential
Copyright © 2024 ICONIQ Capital, LLC. All Rights Reserved

## Stage of Primary AI Product

AI-native companies are further along in the development cycle compared to AI-enabled peers, with around 47% of products
analyzed having reached critical scale and proven market fit

![Stacked bar chart showing the Stage of Primary AI Product for AI-Enabled and AI-Native companies. Stages are Pre-Launch, Beta, General Availability, and Scaling. AI-Enabled: Pre-Launch (11%), Beta (34%), General Availability (42%), Scaling (13%). AI-Native: Pre-Launch (1%), Beta (10%), General Availability (42%), Scaling (47%).]

Stage of Primary AI Product
% of Respondents, N = 291

Scaling
The product has proven market fit and is now focused on growing
its user base and infrastructure to handle higher demand

General Availability
The product is formally released with the stability and support
expected for broad adoption

Beta
The product is sufficiently developed to be tested by a limited
group of external users for feedback and bug identification

Pre-Launch
The product is still in development and not
officially available to external users

Only 1% of AI-native companies are still
in pre-launch, compared to 11% of AI-
enabled companies. Meanwhile, while
not surprising to see that 47% of AI-
native products are already scaling, this
may imply AI-native companies are
moving faster through the product
lifecycle and achieving traction earlier.

This begs the question whether AI-
native orgs may be structurally better
equipped - through team composition,
infrastructure, or funding models - to
validate product-market fit and scale
effectively, and perhaps leapfrogging the
trial-and-error phases that slow down AI-
enabled companies retrofitting AI into
existing workflows.

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

8

## Types of AI Products

Agentic workflows and the application layer are the most common types of products being built across AI-native and AI-
enabled companies; notably, around 80% of AI-native companies are currently building agentic workflows

![Bar chart showing the percentage of AI-Native and AI-Enabled companies building different types of AI products. Types are Agentic workflows, Vertical AI applications, Horizontal AI applications, AI platforms / infrastructure, and Core AI models / technologies. AI-Native percentages: Agentic workflows (79%), Vertical AI applications (65%), Horizontal AI applications (56%), AI platforms / infrastructure (49%), Core AI models / technologies (40%). AI-Enabled percentages: Agentic workflows (62%), Vertical AI applications (57%), Horizontal AI applications (55%), AI platforms / infrastructure (48%), Core AI models / technologies (27%).]

AI-Native

AI-Enabled

What type of AI products are you building?
% of Respondents, Select All That Apply, N = 291

i.e. focused on specific industry
or function

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

9

## Model Usage

Most companies building AI applications are relying on third-party AI APIs; however, a larger proportion of high-growth
companies are also finetuning existing foundation models and developing proprietary models from scratch

![Bar chart comparing High Growth Company and Other Respondents on how their company uses AI models. Options are Rely on third-party AI APIs, Fine-tune existing foundation models, and Develop proprietary models from scratch. High Growth Company percentages: Rely on third-party AI APIs (71%), Fine-tune existing foundation models (77%), Develop proprietary models from scratch (54%). Other Respondents percentages: Rely on third-party AI APIs (80%), Fine-tune existing foundation models (61%), Develop proprietary models from scratch (32%).]

High Growth Company

Other Respondents

How does your company use AI models?
% of Respondents, N = 265

A greater percentage of later stage companies
($100M+ revenue) tend to develop proprietary
models or fine-tune existing foundation models,
likely due to greater resources and need for
enterprise customization

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

10

## Top Considerations for Foundational Models: Product Development

When choosing foundational models for customer-facing use cases, companies prioritize model accuracy above all
other factors

![Bar chart showing the percentage of respondents who ranked each aspect in their Top 3 considerations when choosing a Foundational Model for Product Development. Aspects are Accuracy (74%), Cost (57%), Ability to fine-tune / customize (41%), Privacy (34%), Latency (25%), Model transparency / explainability (19%), Inference efficiency / compute requirements (18%), SOC2 / Enterprise SLAs (14%), Open Source (9%), Vendor lock-in / portability (6%).]

Accuracy

Cost

Ability to fine-tune / customize

Privacy

Latency

Model transparency / explainability

Inference efficiency / compute requirements

Top Considerations When Choosing a Foundational Model
% of Respondents who ranked each aspect in Top 3, N = 265

SOC2 / Enterprise SLAs

Open Source

Vendor lock-in / portability

In last year’s State of AI report, cost
ranked as the lowest key purchasing
consideration in comparison to other
factors like performance, security,
customizability, and control. Notably,
cost is much higher in this year’s data
perhaps echoing the commoditization of
the model layer with the rise of more
cost-efficient models like DeepSeek.

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

11

## Top Model Providers

OpenAI’s GPT models continue to be the most popular model; however, many companies
are increasingly adopting a multi-model approach to AI products across use cases

![Stacked bar chart showing the percentage of respondents using different Top Model Providers, broken down by company type (Full Stack, Horizontal Application, Vertical Application). Providers include OpenAI / GPT, Anthropic / Claude, Google / Gemini, Meta / LLama, Mistral AI, DeepSeek, Cohere, xAI, and Other. Overall percentages are shown above the bars. OpenAI / GPT (95%), Anthropic / Claude (81%), Google / Gemini (78%), Meta / LLama (54%), Mistral AI (55%), DeepSeek (55%), Cohere (54%), xAI (50%), Other (43%). Average number of models per respondent = 2.8.]

Full Stack[^1]
Horizontal Application
Vertical Application

Top Model Providers
% of Respondents, Select All That Apply, N = 240

Avg number of models per
respondent = 2.8

Companies are increasingly adopting a multi-
model approach to AI products, leveraging
different providers and models based on use
case, performance, cost, and customer
requirements.

This flexibility enables them to optimize for
diverse applications like cybersecurity, sales
automation, and customer service while
ensuring compliance and superior user
experience across regions.

Architectures are being built to support quick
model swaps, with some leaning toward open-
source models for cost and inference speed
advantages.

Generally, most respondents are using a
combination of OpenAI models and 1-2 other
models from the other providers.

> We use different proprietary and 3rd party models
> because our customers have diverse needs.
> Specialized models allow us to better tailor the
> experiences for our customers and their use case --
> sales automation, agents for customer service and
> internal tools. In addition, we can offer our
> customers more flexible price points and options,
> as well as be constantly experimenting with new
> models and business opportunities.
> VP Product, $1B+ Revenue, Full Stack AI Company

Notes: (1) Companies building both end user applications and core AI models/technologies

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

12

## Model Training Techniques

Retrieval augmented generation (RAG) and fine-tuning are the most common model training techniques; high-growth
companies tend to use a greater variety of prompt-based techniques

![Bar chart comparing High Growth Company and Other Respondents on Model Training / Adaptation Techniques. Techniques are RAG, Fine-tuning, Pretraining, Few-Shot Learning, and Zero-Shot Learning. High Growth Company percentages: RAG (69%), Fine-tuning (68%), Pretraining (32%), Few-Shot Learning (36%), Zero-Shot Learning (31%). Other Respondents percentages: RAG (66%), Fine-tuning (67%), Pretraining (49%), Few-Shot Learning (25%), Zero-Shot Learning (20%). Techniques are categorized as Training Techniques and Prompt-Based Techniques.]

High Growth Company

Other Respondents

Model Training / Adaptation Techniques
% of Respondents, N = 273

Training Techniques

Prompt-Based Techniques

Compared to last year’s State of
AI report, a greater percentage of
respondents in this year’s survey
are actively using RAG and
finetuning techniques. We
expected finetuning to be a lower
percentage given the investment
required and how quickly base
models are improving but it
remains an area of focus

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

13

## AI Infrastructure

Most companies are using cloud-based solutions and AI API providers for training and
inference

![Bar chart showing the percentage of respondents using different AI Infrastructure for Training and Inference. Options are Fully cloud-based (68%), External AI API providers (64%), Hybrid (e.g., cloud + on-prem GPU clusters) (23%), Dedicated inference providers (e.g., Fireworks, Together.ai, Baseten) (10%), Fully on-prem infrastructure (8%).]

AI Infrastructure for Training and Inference
% of Respondents, Select All That Apply, N = 273

Most organizations are clearly leaning
into fully managed AI solutions - 68%
operate entirely in the cloud and 64%
rely on external AI API providers -
because this model minimizes upfront
capital outlay and operational
complexity, while maximizing speed-to-
market. However, this reliance also
means vendor selection, SLA
negotiation, and cost-per-call
management have become strategic
priorities rather than just technical
considerations.

Meanwhile, only 23% of teams use a
hybrid approach and fewer than 1 in 10
maintain on-prem or dedicated inference
infrastructure, underscoring that these
models remain niche, adopted primarily
in scenarios where control, compliance,
or specialized performance justify the
extra overhead. As real-time AI use cases
grow, there’s an emerging opportunity
for turnkey inference platforms to
capture more share, but any move away
from fully managed services will hinge
on a clear business case or regulatory
imperative.

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

14

## Model Deployment Challenges: Product Development

Top challenges noted by companies when deploying models include hallucinations, explainability / trust, and proving ROI

![Bar chart showing the percentage of respondents who ranked each aspect in their Top 3 Challenges in Model Deployment for Product Development. Aspects are Hallucinations (39%), Explainability & trust (38%), Proving ROI (34%), Compute cost (32%), Security (26%), Finding right use cases (25%), Ease of integration with existing systems (24%), Regulatory and ethical considerations (20%), Talent (16%), Latency (15%), Monitoring (10%), Model drift over time (9%), Accessing GPUs (5%).]

Hallucinations

Explainability & trust

Proving ROI

Compute cost

Security

Finding right use cases

Ease of integration with existing systems

Challenges in Model Deployment
% of Respondents who ranked each aspect in Top 3, N = 273

Regulatory and ethical considerations

Talent

Latency

Monitoring

Model drift over time

Accessing GPUs

Explainability and trust
ranked higher for companies
building vertical AI
applications, who may deal
with additional compliance
and legal restrictions in
regulated industries like
healthcare

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

15

## AI Performance Monitoring

As AI products scale, performance monitoring becomes more important with many scaled AI products offering some kind of
advanced performance monitoring

![Stacked bar chart showing Approach to AI Performance Monitoring by AI Product Maturity (Pre-Launch, Beta, General Availability, Scaling). Approaches are No formal monitoring in place, Basic monitoring (tracking model accuracy and performance), Advanced monitoring (drift detection, real-time feedback loops), and Fully automated model monitoring and retraining pipelines. Pre-Launch: No formal monitoring (6%), Basic (75%), Advanced (19%), Automated (0%). Beta: No formal monitoring (4%), Basic (66%), Advanced (16%), Automated (14%). General Availability: No formal monitoring (7%), Basic (59%), Advanced (31%), Automated (3%). Scaling: No formal monitoring (4%),