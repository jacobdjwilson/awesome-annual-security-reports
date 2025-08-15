# ThreatLabz 2025 AI Security Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [AI and ML Usage Trends](#ai-and-ml-usage-trends)
  - [AI/ML transactions overview](#ai/ml-transactions-overview)
  - [Blocked AI/ML transactions](#blocked-ai/ml-transactions)
  - [Data loss to AI/ML apps](#data-loss-to-ai/ml-apps)
  - [AI usage by industry](#ai-usage-by-industry)
  - [Industry spotlights](#industry-spotlights)
    - [Finance & Insurance doubles down on AI investment](#finance--insurance-doubles-down-on-ai-investment)
    - [Manufacturing is harnessing the power of AI](#manufacturing-is-harnessing-the-power-of-ai)
    - [Healthcare sees an uptick in AI activity](#healthcare-sees-an-uptick-in-ai-activity)
    - [Government recognizes potential in AI](#government-recognizes-potential-in-ai)
  - [ChatGPT usage trends](#chatgpt-usage-trends)
  - [AI usage by country](#ai-usage-by-country)
  - [EMEA insights](#emea-insights)
  - [APAC insights](#apac-insights)
- [Enterprise AI Risks and Real-World Threat Scenarios](#enterprise-ai-risks-and-real-world-threat-scenarios)
  - [Core risks of enterprise AI adoption](#core-risks-of-enterprise-ai-adoption)
  - [DeepSeek and open-source AI: the risk of frontier models in your pocket](#deepseek-and-open-source-ai-the-risk-of-frontier-models-in-your-pocket)
    - [The new economics of AI](#the-new-economics-of-ai)
    - [The security implications of open source AI](#the-security-implications-of-open-source-ai)
  - [5 prompts to deception: DeepSeek-generated phishing page](#5-prompts-to-deception-deepseek-generated-phishing-page)
    - [1. Generating a basic login page](#1-generating-a-basic-login-page)
    - [2. Mimicking a legitimate login interface](#2-mimicking-a-legitimate-login-interface)
    - [3. Adding realistic authentication flow](#3-adding-realistic-authentication-flow)
    - [4. Enhancing branding and UI elements](#4-enhancing-branding-and-ui-elements)
    - [5. Implementing client-side cloaking](#5-implementing-client-side-cloaking)
  - [AI’s growing role in cyber threats](#ais-growing-role-in-cyber-threats)
    - [Supercharged social engineering](#supercharged-social-engineering)
    - [AI-driven malware and ransomware across the attack chain](#ai-driven-malware-and-ransomware-across-the-attack-chain)
    - [Agentic AI: the next frontier in autonomous AI—and attack vectors](#agentic-ai-the-next-frontier-in-autonomous-aiand-attack-vectors)
  - [Case study: How threat actors are exploiting interest in AI](#case-study-how-threat-actors-are-exploiting-interest-in-ai)
    - [Fake AI, real malware threat](#fake-ai-real-malware-threat)
    - [Attack chain](#attack-chain)
- [The Evolving Scope of AI Regulations](#the-evolving-scope-of-ai-regulations)
- [AI Threat Predictions for 2025-2026](#ai-threat-predictions-for-2025-2026)
- [Best Practices for Secure Enterprise AI Adoption](#best-practices-for-secure-enterprise-ai-adoption)
  - [5 steps to securely integrate GenAI tools](#5-steps-to-securely-integrate-genai-tools)
- [How Zscaler Delivers Zero Trust + AI](#how-zscaler-delivers-zero-trust--ai)
  - [Under the hood: Zscaler’s AI security and data advantage](#under-the-hood-zscalers-ai-security-and-data-advantage)
  - [A comprehensive approach to AI security](#a-comprehensive-approach-to-ai-security)
  - [Leveraging AI security across the attack chain](#leveraging-ai-security-across-the-attack-chain)
- [Research Methodology](#research-methodology)
- [About ThreatLabz](#about-threatlabz)
- [About Zscaler](#about-zscaler)

---

## Executive Summary

Another year in the still new “era of AI” has come and gone, marked by game-changing advancements, rising adoption across industries, and high-profile challenges.

Enterprises now see artificial intelligence (AI) and machine learning (ML) as essential for growth, driving efficiency, smarter decision-making, and faster innovation. On the other hand, AI adoption brings serious security risks, from unsanctioned usage (“shadow AI”) to data exposure. Even more concerning, threat actors seem to have the upper hand as they weaponize these same tools to amplify attacks. What once required skill now takes minimal effort. What once took hours now takes seconds.

This shift was on full display in 2024. GenAI became a cybercriminal’s social engineering machine. Today, phishing emails mimic trusted colleagues with eerie accuracy. Deepfake technology turns voices and videos into weapons of deception.

In 2025, the power and perils of AI loom larger than ever. Threat actors will continue to push the boundaries of AI’s malicious capabilities. Yet, AI isn’t just enabling attacks—it’s also now a critical line of defense, powering the fight against these attacks.

The Zscaler ThreatLabz 2025 AI Security Report examines the many facets of AI in cybersecurity, from AI/ML adoption to AI-driven threats and security capabilities.

Analyzing 536.5 billion transactions captured across the Zscaler Zero Trust Exchange™ from AI/ML tools between February and December 2024, ThreatLabz discovered both surprising and unsurprising shifts in usage trends by enterprises worldwide.

ChatGPT drove the most AI/ML transactions, making up nearly half of the total volume. From an industry perspective, the Finance & Insurance and Manufacturing verticals drove the most transactions as top adopters of AI. However, increased adoption didn’t mean unfettered access: a large percentage of AI/ML transactions were actively blocked.

Beyond usage trends, ThreatLabz discovered real-world threat scenarios from AI-enhanced phishing to fake AI platforms. This report also explores recent developments in areas that will undoubtedly influence AI in 2025 and beyond, including agentic AI, the emergence of DeepSeek, and the evolving regulatory landscape.

As AI/ML capabilities evolve and the threats they enable grow, the imperative is clear, more sophisticated, strong security controls, zero trust architecture, and AI-powered defenses are no longer optional—they’re essential. Keep reading for more insights and actionable strategies to help your organization securely adopt AI while staying ahead of AI-driven threats.

## Key Findings

ThreatLabz analyzed 536.5 billion AI and ML transactions in the Zscaler cloud from February 2024–December 2024. The key findings that follow are based on data spanning varying time periods* for comparative analysis.

AI/ML tool usage saw an exponential rise year-over-year, with **36x more transactions (+3,464.6%)** from 800+ AI/ML applications in the Zscaler cloud, highlighting the explosive growth in enterprise interest and dependence on these technologies.

Enterprises **blocked 59.9% of all AI/ML transactions**, reflecting concerns around AI data security and the steps companies are taking in shaping their approaches to AI governance.

**ChatGPT remains the top application** by transaction volume, accounting for nearly half of all AI/ML transactions (45.2%) from known applications, despite ongoing debates over its security implications.

**ChatGPT is also the most-blocked AI application** among known applications, followed by Grammarly, Microsoft Copilot, QuillBot, and Wordtune, reinforcing growing interest and caution when it comes to AI-powered writing and productivity assistants in enterprise settings.

* Time period variations:
- “Year-over-year” percentage changes compare data from April–December 2024 and the same period in 2023.
- Country- and region-specific findings are based on data collected between July–December 2024.

The Zscaler Zero Trust Exchange tracks ChatGPT transactions independently from other OpenAI transactions at large.

Enterprises are sending significant volumes of data to AI tools, with a total of **3624 TB transferred by AI/ML applications**.

The **Finance & Insurance and Manufacturing industries generate the most AI/ML traffic**, with 28.4% and 21.6% share of all AI/ML transactions in the Zscaler cloud, respectively, followed by Services (18.5%), Technology (10.1%), Healthcare (9.6%), and Government (4.2%), showing that AI adoption varies significantly across industries.

The **top 5 countries generating the most AI/ML transactions** are the United States, India, United Kingdom, Germany, and Japan.

AI continues to amplify cyber risks, fueled by advancements in deepfake technology, emerging open source AI models, and autonomous attack automation—undoubtedly making threats more adaptive, targeted, and difficult to detect.

## AI and ML Usage Trends

AI/ML tool usage surged globally in 2024, with enterprises integrating AI into operations and employees embedding it in daily workflows. Zscaler tracked more than 800 AI/ML applications in the Zscaler cloud, a considerably higher number compared to the previous analysis period in 2023, reflecting the expanding enterprise adoption and reliance on AI-powered tools.

### AI/ML transactions overview

Growing security risks haven’t slowed the exponential rise in AI and ML transactions. From February through December 2024, transaction volumes surged from 3.7 billion to 49 billion, marking a twelvefold increase. AI/ML activity peaked in July, reaching 82.7 billion transactions.

![AI Usage Trends by Transaction Volume from February 2024–December 2024]

The scale of AI/ML activity increased dramatically to 536.5 billion total AI/ML transactions—a 3,464.6% year-over-year surge compared to our last analysis period. A significant portion of this AI/ML traffic comes from widely used applications such as ChatGPT, Grammarly, Microsoft Copilot, and other AI/ML tools. However, a large share of the transactions (53.1%) remain categorized as “General AI Applications” within the Zscaler cloud, underscoring the rapid proliferation of AI use across enterprises. This classification reflects AI/ML transactions that do not yet belong to defined AI applications but are nonetheless detected as AI/ML traffic via Zscaler’s AI/ML-powered URL categorization, which can analyze text, images, and other content to identify AI-related activity.

To provide a more precise and detailed view of AI/ML adoption patterns amongst enterprises, ThreatLabz analysis focuses on classified AI/ML applications. By taking this approach, we highlight AI adoption trends through established enterprise AI/ML applications.

**SHARE OF TOTAL TRANSACTIONS**

Classified AI Applications (e.g.,ChatGPT and Grammarly)
46.9%

General AI Applications
53.1%

Among known AI/ML applications, a handful of market-leading tools generate the majority of transactions. The following top five tools share a common focus on enhancing productivity, communication, and automation.

- **ChatGPT** makes up nearly half of AI and ML transactions (45.2%), reminding us of its extensive adoption across industries. Learn more in the ChatGPT usage trends section.
- **Grammarly** ranks second (24.8%), reflecting its growing popularity among enterprise users for refining writing and grammar.
- **Microsoft Copilot** holds the third spot (12.5%) as enterprises rely on it to automate tasks in Microsoft 365 apps like Word, Excel, and Outlook.
- **DeepL**, a leading AI-powered translation tool, follows (6.4%) as it has gained traction among global enterprises seeking high-quality multilingual communication.
- **QuillBot** rounds out the top five (2.0%) as another go-to writing assistant offering paraphrasing and summarization.

![Top AI/ML Applications by Transaction Volume]

**TOP AI APPLICATIONS**

| Application        | Total Transactions   |
| :----------------- | :------------------- |
| ChatGPT            | 113,869,583,355      |
| Grammarly          | 62,490,051,574       |
| Microsoft Copilot  | 31,551,774,637       |
| DeepL              | 16,012,344,908       |
| QuillBot           | 5,130,879,211        |
| User Defined       | 4,297,439,333        |
| OpenAI             | 2,995,303,521        |
| Wordtune           | 2,552,030,384        |
| Codeium            | 2,439,268,698        |
| Perplexity         | 1,806,093,093        |
| Loom               | 662,917,153          |
| ZineOne            | 571,034,336          |
| Synthesia          | 570,918,959          |
| Writer             | 512,811,065          |
| Poe                | 433,139,217          |
| Claude             | 379,841,841          |
| Google Gemini      | 317,583,902          |
| Otter.ai           | 310,594,881          |
| Runway             | 256,927,467          |
| Yellow Messenger   | 245,412,258          |

**Top Application Categories**

1.  **Productivity Assistants (60.4%)**
    Examples: ChatGPT, Microsoft Copilot, Perplexity

    Nearly two-thirds of AI/ML transactions in the Zscaler cloud fall under the category of AI-powered assistants. These applications encompass a wide swath of use cases, from AI-driven chat interfaces and research tools to workflow automation and enterprise integration—all sharing a common goal of boosting enterprise productivity.

2.  **Writing & Content Generation (28.3%)**
    Examples: Grammarly, Quillbot, Wordtune

    The second largest share of AI/ML application activity comes from the writing and content generation category. AI-powered writing tools have rapidly become integral to enterprise content and communications, streamlining tasks such as editing, enhancing clarity, and other grammar refinements.

**From productivity to predicament: know the risks**

The dominant role of AI in enterprise productivity and writing presents significant risks, including data leakage, prompt injection attacks, compliance violations, AI hallucinations, IP exposure, privacy concerns, and potential overreliance. Learn how to mitigate these risks and securely embrace AI in the section, Best Practices for Secure Enterprise AI Adoption.

3.  **Language & Translation (5.8%)**
    Examples: DeepL, LanguageTool

    AI-powered language and translation tools account for 14.6 billion transactions. These solutions are streamlining global business communications, enabling faster, scalable multilingual content creation, though concerns around accuracy and data privacy persist.

4.  **Custom Applications (1.7%)**

    As organizations seek AI-driven competitive edges, custom AI applications account for more than 4 billion transactions. Enterprises are leveraging tailored AI solutions for use cases spanning predictive analytics, fraud detection, automation, and more.

5.  **Coding Assistants (1.3%)**
    Examples: Codeium, Claude

    AI-powered coding assistants are becoming more common in software development, driving 3+ billion transactions. They help developers work faster, but enterprises must be aware of the risks, from quality concerns to intellectual property issues.

6.  **Visual & Creative Tools (1.1%)**
    Examples: Loom, Synthesia

    AI’s role as a creative partner is expanding, as visual and creative AI tools generated 2.7 billion transactions. Video creation tools lead the category, enabling organizations to scale video content production efforts and content output.

![Transactions by Application Category]

**TRANSACTIONS BY APPLICATION CATEGORY**

| Category                     | Transactions       |
| :--------------------------- | :----------------- |
| Productivity Assistants      | 70,916,692,869     |
| Writing & Content Generation | 14,638,307,672     |
| Language & Translation       | 31,551,774,637     |
| Custom Applications          | 4,354,146,062      |
| Coding Assistants            | 3,205,630,565      |
| Visual/Creative Tools        | 4,297,439,333      |
| Data Analysis & Automation   | 2,723,874,910      |
| Customer Support & Chatbots  | 1,172,151,320      |
| Transcription                | 354,967,757        |
| Search Engine                | 297,174,973        |
| Speech and Audio Tools       | 191,295,786        |

**SHARE OF DATA TRANSFERRED BY AI/ML APPLICATIONS**

Transaction volumes alone don’t tell the full story of enterprise AI usage. ThreatLabz also analyzed the amount of data transferred between enterprises and AI tools, totaling 3624 terabytes (TB). By this measure, ChatGPT remains the top application, with 1481 TB of data transferred. The sheer volume of data shows that enterprises aren’t just using ChatGPT often—but at scale.

Following ChatGPT in data transfer volume, Grammarly, OpenAI, and Microsoft Copilot rank highly, underscoring their role in AI-powered content refinement and model training.

Other notable tools contributing significant data transfer volumes include DeepL, Synthesia, and Wordtune, each supporting various enterprise needs, from productivity enhancements to AI-driven video messaging.

Keeping an eye on both transaction volume and data transfer trends will be key to integrating AI effectively while staying ahead of potential risks.

![Top AI/ML Applications by the percentage of total data transferred]

### Blocked AI/ML transactions

Enterprise AI growth is also meeting resistance as organizations strengthen controls to mitigate data security, privacy, and compliance risks. Currently, enterprises block 59.9% of all AI/ML transactions in the Zscaler cloud, totaling more than 321.9 billion blocked transactions between February–December 2024.

![Number of AI/ML transactions blocked between February–December 2024]

Interestingly, the most widely used AI tools are also the most frequently blocked, starting with ChatGPT. The GenAI chatbot remains a primary focus of security measures to prevent data loss, accounting for 54% of total blocks.

Adobe.io, Adobe’s cloud-based developer platform which provides APIs and AI-powered automation tools for Adobe products, makes up 68% of all blocked AI and ML domain transactions. This trend signals a proactive effort by enterprises to prevent unauthorized data transfers and protect proprietary content.

Enterprises are walking an increasingly narrow tightrope between AI innovation and security. As AI adoption keeps growing, organizations will have to tighten the reins on risks while still harnessing the power of AI/ML to stay competitive.

**Top Blocked AI Applications**
1. ChatGPT
2. Grammarly
3. Microsoft Copilot
4. QuillBot
5. Wordtune
6. Codeium
7. DeepL
8. Drift
9. Poe
10. Securiti

**Top Blocked AI Domains**
adobe.io
chatgpt.com
grammarly.com
microsoft.com
quillbot.com
deepl.com
openai.com
bing.com
Wordtune.com
Codeium.com

### Data loss to AI/ML apps

As AI/ML activity surges in the enterprise, so does the risk of data exposure. AI-powered productivity assistants and chatbots, code assistants, and document analyzers can inadvertently expose sensitive enterprise data. This challenge is compounded by users unknowingly sharing confidential information with AI models that lack enterprise-grade security controls.

Numerous AI/ML tools have been flagged for data loss prevention (DLP) violations in the Zscaler cloud. These violations represent instances where sensitive enterprise data—such as financial data, PII, source code, and medical data—was intended to be sent to an AI application, and that transaction was blocked by Zscaler policy. Data loss would have occurred in these AI apps without Zscaler’s DLP enforcement. As a result, the violations serve as a key indicator of real world AI data loss trends.

**AI/ML APPLICATIONS WITH THE MOST DLP POLICY VIOLATIONS**

| Application       | DLP Violations |
| :---------------- | :------------- |
| ChatGPT           | 2,915,502      |
| Wordtune          | 879,131        |
| Microsoft Copilot | 257,869        |
| DeepL             | 68,916         |
| Codeium           | 41,041         |
| Claude            | 40,993         |
| Synthesia         | 22,975         |
| Grammarly         | 7,157          |
| DataRobot         | 5,440          |
| QuillBot          | 4,649          |
| Google Gemini     | 4,227          |
| You.com           | 2,341          |
| Perplexity        | 2,129          |
| DeepAI            | 1,472          |
| Poe               | 1,399          |

These tools share a common risk profile due to their cloud-based processing and use in productivity workflows, where they often handle sensitive enterprise data. The violations highlight the growing need for AI-aware DLP controls to ensure organizations can embrace AI securely while preventing data leaks.

A closer look at the most common AI-related DLP violations reveals that personally identifiable information (PII), proprietary source code, and healthcare-related data are at risk of exposure.

**TOP 10 AI DLP VIOLATIONS**

1. Social Security Number
2. Name leakage (US)
3. Adult content
4. Self-harm & cyber bullying content
5. Source code
6. Diseases leakage
7. Medical
8. Name leakage (Canada)
9. Brazilian Individual Taxpayer Registry ID
10. Drugs leakage

Examining the DLP violations tied to ChatGPT and Microsoft Copilot—two of the most widely used enterprise AI tools and top offenders of DLP violations—reveals frequent exposure of PII, health-related data, and source code.

**ChatGPT DLP Violations**
SSN, name leakage (US), diseases leakage, name leakage (Canada), Brazilian Individual Taxpayer Registry ID

**Microsoft Copilot DLP Violations**
SSN, drugs leakage, diseases leakage, treatments leakage, financial, source code

For deeper insights into ChatGPT usage patterns, check out the ChatGPT usage trends section. To learn how to mitigate data loss from GenAI applications, read 5 steps to securely integrate GenAI tools below.

### AI usage by industry

Enterprise adoption of AI and ML tools varies widely by industry, with Finance & Insurance leading the charge, driving 28.4% of AI/ML transactions. As financial services continue to embrace AI-driven efficiencies for critical functions like fraud detection, customer service automation, and risk assessments, their AI transaction volume has surpassed Manufacturing, which now holds the second spot at 21.6% of total AI/ML transactions.

The Services (18.5%), Technology (10.1%), and Healthcare (9.6%) industries follow, each adopting AI at different speeds based on their unique operational priorities. While the Services sector is likely ramping up AI usage in terms of customer support and operational optimizations, technology firms continue to drive AI research and innovation. Healthcare adoption remains lower in comparison, reflecting a more reserved stance due to heightened regulatory and security concerns.

![Industries driving the largest proportions of AI transactions]

![AI/ML transaction trends among the highest-volume industries]

Industries are also bumping up efforts to secure AI/ML transactions, but the volume of blocked AI/ML activity varies. Finance & Insurance blocks 39.5% of AI transactions. This trend aligns with the industry’s stringent compliance landscape and the need to safeguard financial and personal data.

Manufacturing blocks 19.2% of AI transactions, suggesting a strategic approach