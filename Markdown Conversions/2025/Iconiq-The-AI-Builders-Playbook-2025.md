# The Builder’s Playbook: 2025 State of AI Report

June 2025

Private and Strictly Confidential
Copyright © 2025 ICONIQ Capital, LLC. All Rights Reserved

For Professional Clients Only. ICONIQ Partners (UK) LLP (973080) is an appointed representative of
Kroll Securities Ltd (466458) which is authorized and regulated by the Financial Conduct Authority

Follow our research

![Image of a button labeled SUBSCRIBE](image_of_subscribe_button.png)

Go-To-Market Series
- Guides to sales, customer success, marketing compensation – and more

Navigating Today’s Public Markets
- The metrics that matter and the market realities of 2025 and beyond

Growth & Efficiency
- Explore our research on best-in-class SaaS growth and efficiency

The ICONIQ Enterprise Five
- Key performance indicators of Enterprise SaaS companies

The SaaS Glossary
- A guide to understanding and tracking key SaaS metrics

Engineering Series
- Definitive guides to engineering excellence

Private & Strictly Confidential

2

Introduction

We believe that building and operationalizing AI products is the new frontier of competitive advantage – and that the voices of the
architects, engineers, and product leaders driving this work deserve their own spotlight. While last year’s State of AI report centered
on the buying journey and enterprise adoption dynamics, our 2025 report pivots squarely to the “how-to”: what it takes to conceive,
deliver, and scale AI-powered offerings end-to-end.

This year’s report unpacks core dimensions of the builder’s playbook:
1.  **Product Roadmap & Architecture**: The emerging best practices for balancing experimentation, speed to market, and
    performance at each stage of model evolution
2.  **Go-to-Market Strategy**: How teams are aligning pricing models and go-to-market strategies to reflect AI’s unique value drivers
3.  **People & Talent**: Building the right team to harness AI expertise, foster cross-functional collaboration, and sustain long-term
    innovation
4.  **Cost Management & ROI**: Strategies and benchmarks for spend associated with building and launching AI products
5.  **Internal Productivity & Operations**: How companies are embedding AI into everyday workflows and the biggest drivers of
    productivity unlock

Drawing on our proprietary survey results alongside in-depth interviews with AI leaders across the ICONIQ community, the 2025
State of AI report offers a blueprint for anyone tasked with turning generative intelligence from a promising concept into a
dependable, revenue-driving asset.

Explore Our AI Perspectives

![Image of a button labeled Explore Our AI Perspectives](image_of_explore_ai_perspectives_button.png)

Private & Strictly Confidential

3

## Table of Contents

- [Building Generative AI Products](#building-generative-ai-products)
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
    - [% of Engineering team Focused on AI](#--of-engineering-team-focused-on-ai)
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
    - [Key Purchasing Considerations](#key-purchasing-considerations)
    - [Deployment Challenges](#deployment-challenges)
    - [Number of Use Cases](#number-of-use-cases)
    - [Top Use Cases: By Popularity](#top-use-cases-by-popularity)
    - [Top Use Cases: By Impact](#top-use-cases-by-impact)
    - [Attitude Towards Internal AI Adoption](#attitude-towards-internal-ai-adoption)
    - [Tracking ROI](#tracking-roi)
- [AI Builder Tech Stack](#ai-builder-tech-stack)
    - [Most Used Tools: Model Training & Finetuning](#most-used-tools-model-training--finetuning)
    - [Most Used Tools: LLM & AI Application Development](#most-used-tools-llm--ai-application-development)
    - [Most Used Tools: Monitoring and Observability](#most-used-tools-monitoring-and-observability)
    -   [Most Used Tools: Inference Optimization](#most-used-tools-inference-optimization)
    -   [Most Used Tools: Model Hosting](#most-used-tools-model-hosting)
    -   [Most Used Tools: Model Evaluation](#most-used-tools-model-evaluation)
    -   [Most Used Tools: Data Processing & Feature Engineering](#most-used-tools-data-processing--feature-engineering)
    -   [Most Used Tools: Vector Databases](#most-used-tools-vector-databases)
    -   [Most Used Tools: Synthetic Data & Data Augmentation](#most-used-tools-synthetic-data--data-augmentation)
    -   [Most Used Tools: Coding Assistance](#most-used-tools-coding-assistance)
    -   [Most Used Tools: DevOps and MLOps](#most-used-tools-devops-and-mlops)
    -   [Most Used Tools: Product and Design](#most-used-tools-product-and-design)
- [Internal Productivity Use Cases](#internal-productivity-use-cases)
    -   [Internal Productivity Use Cases (Part 1 of 2)](#internal-productivity-use-cases-part-1-of-2)
    -   [Internal Productivity Use Cases (Part 2 of 2)](#internal-productivity-use-cases-part-2-of-2)
- [A global portfolio of category-defining businesses](#a-global-portfolio-of-category-defining-businesses)
- [Disclosures](#disclosures)
- [Technology matters. Strategy matters. People matter most.](#technology-matters-strategy-matters-people-matter-most)
- [Join our community](#join-our-community)

4

Data Sources
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

![Bar chart showing Respondent Firmographics by Revenue Range and Headquarters](bar_chart_respondent_firmographics.png)

Revenue Range
% of Respondents

| Revenue Range | % of Respondents |
| :------------ | :--------------- |
| <$10M         | 26%              |
| $10M-$24M     | 13%              |
| $25M-$49M     | 10%              |
| $50M-$99M     | 9%               |
| $100-$200M    | 7%               |
| $200-$500M    | 13%              |
| $500M-$1B     | 11%              |
| $1B+          | 8%               |

Headquarters
% of Respondents

| Headquarters  | % of Respondents |
| :------------ | :--------------- |
| North America | 92%              |
| Europe        | 4%               |
| Other         | 4%               |

In this report, select companies are referred to as “high
growth companies” because they meet the following criteria

- AI Product Traction: AI product is in General Availability or
  Scaling
- Revenue: At least $10M in annual revenue
- Topline Growth: 100%+ YoY revenue growth if <$25M
  Revenue, 50%+ YoY revenue growth if $25M-250M Revenue,
  30%+ YoY revenue growth if $250M+ Revenue

High Growth
Companies
% of respondents

| Category             | % of Respondents |
| :------------------- | :--------------- |
| High Growth Companies | 13%              |

Revenue Range
% of High-Growth Respondents

| Revenue Range | % of High-Growth Respondents |
| :------------ | :--------------------------- |
| Less than $100M | 55%                          |
| $100-$200M    | 20%                          |
| $200M+        | 25%                          |

Notes: (1) This data was collected anonymously by an external survey. Survey responses include some but not all ICONIQ Venture and Growth portfolio companies as well as companies not part of ICONIQ Venture and Growth’s portfolio.
(2) Certain questions in the survey were optional. Accordingly, some N-Size numbers in this presentation are less than 300

Private & Strictly Confidential

5

AI Maturity

Most SaaS companies have evolved to add new AI capabilities and products; the following pages will dive into how AI-
enabled and AI-native companies are approaching product development

![Diagram showing the evolution of SaaS to Generative AI Products](diagram_saas_to_genai_evolution.png)

Traditional SaaS
Traditional Software-as-a-Service

Delivery of subscription-based
applications built around core
business workflows

31% of survey respondents

Representative
Examples

![Logos of traditional SaaS companies like Salesforce, Workday, ServiceNow](logos_traditional_saas.png)

Generative AI Products

AI-Enabled: Adding AI Capabilities
to Existing Products

Embedded AI-powered features into
flagship offerings to boost
automation, personalization, and end-
user productivity—while leaving
underlying business model and UX
largely intact

37% of survey respondents

![Logos of AI-enabled companies like Figma, HubSpot, Atlassian](logos_ai_enabled_existing.png)

AI-Enabled: Creating a new (non-
core) AI product

Standalone AI-driven product or
services alongside core product
portfolio to explore adjacent use
cases and revenue streams

32% of survey respondents

![Logos of AI-enabled new product companies like Grammarly, Jasper, Midjourney](logos_ai_enabled_new.png)

AI-Native: Core product or business
model is AI-driven

Entire value proposition is architected
around generative intelligence —where
model training, inference, and
continuous learning are the fundamental
drivers of customer value and growth

![Logos of AI-native companies like OpenAI, Anthropic, Cohere](logos_ai_native.png)

Notes: Representative Examples provided for illustrative purposes only. Trademarks are the property of their respective owners. None of the companies illustrated have endorsed or recommended the services of ICONIQ.
Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

6

Focus of this report

# Building GenAI
Products

Private and Strictly Confidential
Copyright © 2024 ICONIQ Capital, LLC. All Rights Reserved

Stage of Primary AI Product

AI-native companies are further along in the development cycle compared to AI-enabled peers, with around 47% of products
analyzed having reached critical scale and proven market fit

Stage of Primary AI Product
% of Respondents, N = 291

![Stacked bar chart showing Stage of Primary AI Product for AI-Enabled and AI-Native companies](stacked_bar_chart_ai_product_stage.png)

| Stage               | AI-Enabled | AI-Native |
| :------------------ | :--------- | :-------- |
| Scaling             | 13%        | 47%       |
| General Availability | 42%        | 42%       |
| Beta                | 34%        | 10%       |
| Pre-Launch          | 11%        | 1%        |

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

### Types of AI Products

Agentic workflows and the application layer are the most common types of products being built across AI-native and AI-
enabled companies; notably, around 80% of AI-native companies are currently building agentic workflows

What type of AI products are you building?
% of Respondents, Select All That Apply, N = 291

![Bar chart comparing types of AI products being built by AI-Native and AI-Enabled companies](bar_chart_types_of_ai_products.png)

| Product Type                 | AI-Native | AI-Enabled |
| :--------------------------- | :-------- | :--------- |
| Agentic workflows            | 79%       | 62%        |
| Vertical AI applications     | 65%       | 57%        |
| Horizontal AI applications   | 56%       | 55%        |
| AI platforms / infrastructure | 49%       | 48%        |
| Core AI models / technologies | 40%       | 27%        |

i.e. focused on specific industry
or function

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

9

### Model Usage and Key Purchasing Considerations

Most companies building AI applications are relying on third-party AI APIs; however, a larger proportion of high-growth
companies are also finetuning existing foundation models and developing proprietary models from scratch

High Growth Company

Other Respondents

How does your company use AI models?
% of Respondents, N = 265

![Bar chart comparing AI model usage by High Growth and Other Respondents](bar_chart_ai_model_usage.png)

| Model Usage                      | High Growth Company | Other Respondents |
| :------------------------------- | :------------------ | :---------------- |
| Rely on third-party AI APIs      | 80%                 | 71%               |
| Fine-tune existing foundation models | 77%                 | 61%               |
| Develop proprietary models from scratch | 54%                 | 32%               |

A greater percentage of later stage companies
($100M+ revenue) tend to develop proprietary
models or fine-tune existing foundation models,
likely due to greater resources and need for
enterprise customization

Source: Perspectives from the ICONIQ GenAI Survey (April 2025) and perspectives from the ICONIQ team and network of AI leaders consisting of our community of
CIO/CDOs overseeing AI initiatives in enterprises, CTOs, our Technical Advisory Board, and others in our network

Private & Strictly Confidential

10

When choosing foundational models for customer-facing use cases, companies prioritize model accuracy above all
other factors

Top Considerations When Choosing a Foundational Model
% of Respondents who ranked each aspect in Top 3, N = 265

![Bar chart showing top considerations when choosing a foundational model for product development](bar_chart_top_model_considerations_product.png)

| Consideration                      | % in Top 3 |
| :--------------------------------- | :--------- |
| Accuracy                           | 74%        |
| Cost                               | 57%        |
| Ability to fine-tune / customize   | 41%        |
| Privacy                            | 34%        |
| Latency                            | 25%        |
| Model transparency / explainability | 19%        |
| Inference efficiency / compute requirements | 18%        |
| SOC2 / Enterprise SLAs             | 14%        |
| Open Source                        | 9%         |
| Vendor lock-in / portability       | 6%         |

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

### Top Model Providers

OpenAI’s GPT models continue to be the most popular model; however, many companies
are increasingly adopting a multi-model approach to AI products across use cases

Full Stack[^1]
Horizontal Application
Vertical Application

Top Model Providers
% of Respondents, Select All That Apply, N = 240

![Stacked bar chart showing top model providers used by companies, broken down by application type](stacked_bar_chart_top_model_providers.png)

Avg number of models per
respondent = 2.8

| Provider         | Full Stack | Horizontal Application | Vertical Application | Total |
| :--------------- | :--------- | :--------------------- | :------------------- | :---- |
| OpenAI / GPT     | 95%        | 81%                    | 78%                  | -     |
| Anthropic / Claude | 54%        | 55%                    | 55%                  | -     |
| Google / Gemini  | 43%        | 42%                    | 29%                  | -     |
| Meta / LLama     | 34%        | 26%                    | 23%                  | -     |
| Mistral AI       | 13%        | 8%                     | 14%                  | -     |
| DeepSeek         | 7%         | 17%                    | 10%                  | -     |
| Cohere           | 7%         | 10%                    | 12%                  | -     |
| xAI              | 8%         | 9%                     | 2%                   | -     |
| Other            | 4%         | -                      | -                    | -     |

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

### Model Training Techniques

Retrieval augmented generation (RAG) and fine-tuning are the most common model training techniques; high-growth
companies tend to use a greater variety of prompt-based techniques

High Growth Company

Other Respondents

Model Training / Adaptation Techniques
% of Respondents, N = 273

![Bar chart comparing model training and adaptation techniques used by High Growth and Other Respondents](bar_chart_model_training_techniques.png)

Training Techniques

| Technique   | High Growth Company | Other Respondents |
| :---------- | :------------------ | :---------------- |
| RAG         | 69%                 | 66%               |
| Fine-tuning | 68%                 | 67%               |
| Pretraining | 32%                 | 31%               |

Prompt-Based Techniques

| Technique        | High Growth Company | Other Respondents |
| :--------------- | :------------------ | :---------------- |
| Few-Shot Learning | 67%                 | 49%               |
| Zero-Shot Learning | 36%                 | 25%               |

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

### AI Infrastructure

Most companies are using cloud-based solutions and AI API providers for training and
inference

AI Infrastructure for Training and Inference
% of Respondents, Select All That Apply, N = 273

![Bar chart showing AI infrastructure used for training and inference](bar_chart_ai_infrastructure.png)

| Infrastructure Type                                  | % of Respondents |
| :--------------------------------------------------- | :--------------- |
| Fully cloud-based                                    | 68%              |
| External AI API providers                            | 64%              |
| Hybrid (e.g., cloud + on-prem GPU clusters)          | 23%              |
| Dedicated inference providers (e.g., Fireworks, Together.ai, Baseten) | 10%              |
| Fully on-prem infrastructure                         | 8%               |

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

### Model Deployment Challenges

Top challenges noted by companies when deploying models include hallucinations, explainability / trust, and proving ROI

Challenges in Model Deployment
% of Respondents who ranked each aspect in Top 3, N = 273

![Bar chart showing top challenges in model deployment](bar_chart_model_deployment_challenges.png)

| Challenge                          | % in Top 3 |
| :--------------------------------- | :--------- |
| Hallucinations                     | 39%        |
| Explainability & trust