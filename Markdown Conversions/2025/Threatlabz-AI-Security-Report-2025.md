# ThreatLabz 2025 AI Security Report

©2025 Zscaler, Inc. All rights reserved.

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [AI and ML Usage Trends](#ai-and-ml-usage-trends)
  - [AI/ML transactions overview](#ai/ml-transactions-overview)
  - [Blocked AI/ML transactions](#blocked-ai/ml-transactions)
  - [Data loss to AI/ML apps](#data-loss-to-ai/ml-apps)
  - [AI's growing role in cyber threats](#ais-growing-role-in-cyber-threats)
    - [Supercharged social engineering](#supercharged-social-engineering)
    - [AI-driven malware and ransomware across the attack chain](#ai-driven-malware-and-ransomware-across-the-attack-chain)
    - [Agentic AI: the next frontier in autonomous AI—and attack vectors](#agentic-ai-the-next-frontier-in-autonomous-aiand-attack-vectors)
  - [Case study: How threat actors are exploiting interest in AI](#case-study-how-threat-actors-are-exploiting-interest-in-ai)
  - [AI usage by industry](#ai-usage-by-industry)
  - [The Evolving Scope of AI Regulations](#the-evolving-scope-of-ai-regulations)
  - [Industry spotlights](#industry-spotlights)
  - [ChatGPT usage trends](#chatgpt-usage-trends)
  - [AI usage by country](#ai-usage-by-country)
  - [EMEA insights](#emea-insights)
  - [APAC insights](#apac-insights)
- [AI Threat Predictions for 2025-2026](#ai-threat-predictions-for-2025-2026)
- [Best Practices for Secure Enterprise AI Adoption](#best-practices-for-secure-enterprise-ai-adoption)
  - [5 steps to securely integrate GenAI tools](#5-steps-to-securely-integrate-genai-tools)
- [How Zscaler Delivers Zero Trust + AI](#how-zscaler-delivers-zero-trust-ai)
  - [Under the hood: Zscaler’s AI security and data advantage](#under-the-hood-zscalers-ai-security-and-data-advantage)
  - [A comprehensive approach to AI security](#a-comprehensive-approach-to-ai-security)
  - [Leveraging AI security across the attack chain](#leveraging-ai-security-across-the-attack-chain)
- [Research Methodology](#research-methodology)
- [About ThreatLabz](#about-threatlabz)
- [About Zscaler](#about-zscaler)

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

- AI/ML tool usage saw an exponential rise year-over-year, with 36x more transactions (+3,464.6%) from 800+ AI/ML applications in the Zscaler cloud, highlighting the explosive growth in enterprise interest and dependence on these technologies.
- Enterprises blocked 59.9% of all AI/ML transactions, reflecting concerns around AI data security and the steps companies are taking in shaping their approaches to AI governance.
- ChatGPT remains the top application by transaction volume, accounting for nearly half of all AI/ML transactions (45.2%) from known applications, despite ongoing debates over its security implications.
- ChatGPT is also the most-blocked AI application among known applications, followed by Grammarly, Microsoft Copilot, QuillBot, and Wordtune, reinforcing growing interest and caution when it comes to AI-powered writing and productivity assistants in enterprise settings.

* Time period variations:
- “Year-over-year” percentage changes compare data from April–December 2024 and the same period in 2023.
- Country- and region-specific findings are based on data collected between July–December 2024.

The Zscaler Zero Trust Exchange tracks ChatGPT transactions independently from other OpenAI transactions at large.

- Enterprises are sending significant volumes of data to AI tools, with a total of 3624 TB transferred by AI/ML applications.
- The Finance & Insurance and Manufacturing industries generate the most AI/ML traffic, with 28.4% and 21.6% share of all AI/ML transactions in the Zscaler cloud, respectively, followed by Services (18.5%), Technology (10.1%), Healthcare (9.6%), and Government (4.2%), showing that AI adoption varies significantly across industries.
- The top 5 countries generating the most AI/ML transactions are the United States, India, United Kingdom, Germany, and Japan.
- AI continues to