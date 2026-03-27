# The State of Attacks on GenAI

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings & Telemetry Data Profile](#key-findings--telemetry-data-profile)
- [The LLM Default Protection Layers Adversaries Need to Bypass](#the-llm-default-protection-layers-adversaries-need-to-bypass)
- [Top 3 Predominant Jailbreak Techniques](#top-3-predominant-jailbreak-techniques)
- [Top Adversary Goals and Motivations](#top-adversary-goals-and-motivations)
- [Real-World Attacks on GenAI Applications](#real-world-attacks-on-genai-applications)
- [Key Insights and Lessons Learned](#key-insights-and-lessons-learned)
- [2025 Outlook: Predictions and Recommendations](#2025-outlook-predictions-and-recommendations)
- [The Need for AI Security](#the-need-for-ai-security)
- [Methodology](#methodology)
- [About Pillar Security](#about-pillar-security)
- [References](#references)

---

## Executive Summary

Generative AI enables unprecedented levels of productivity and innovation, opening up vast new opportunities. With new AI models and use cases being developed and deployed in just months, Security and AI leaders grapple with balancing substantial gains against potential setbacks, particularly security vulnerabilities.

Although numerous theoretical studies, surveys, and potential scenarios exist, there has been limited analysis of real-world attacks and risks. This groundbreaking industry report bridges that gap by providing a unique perspective on the current state of AI security threats, offering unparalleled insight into the real-world landscape of AI-related risks. Our observations are based on Pillar's telemetry data, encompassing data interaction derived from an analysis of over 2,000 real-world LLM-powered applications, over the past three months.

This extensive analysis has uncovered the following critical insights:

### Top 3 Predominant Jailbreak Techniques Observed
- **Ignore Previous Instructions**: Attackers direct AI systems to disregard their initial guidelines, potentially causing the AI to generate harmful content, violate ethical guidelines, and inflict reputational damage.
- **Strong Arm Attack**: Persistent and forceful requests pressure AI into compliance, which can lead to the model revealing sensitive information or performing unauthorized actions, resulting in data breaches or system compromise.
- **Base64 Encoding**: Malicious prompts are encoded to evade security filters, allowing attackers to bypass security measures and potentially execute malicious code or extract protected data.

- **Widespread Data Exposure**: 90% of successful attacks resulted in the leakage of sensitive data.
- **Alarming Bypass Rate**: 20% of jailbreak attack attempts successfully bypassed GenAI application guardrails.
- **Swift Attack Execution**: Adversaries require only 42 seconds on average to complete an attack, highlighting the speed at which vulnerabilities can be exploited.
- **Minimal Interaction Required**: Adversaries need an average of just 5 interactions with GenAI apps to complete a successful attack.

---

## Key Findings & Telemetry Data Profile

![Chart showing key metrics: 20% bypass rate, 5 interactions average, 42 seconds average time, and 90% data leakage rate]

- **20%**: Of jailbreak attack attempts successfully bypassed GenAI application guardrails. Out of every five jailbreak attempts, one managed to circumvent the security measures in place.
- **5**: Average number of total interactions between the adversary and the LLM.
- **42 sec**: Average time to complete an attack. The shortest attempt lasted 4 seconds, while the longest extended to 14 minutes.
- **90%**: Of successful attacks resulted in the leakage of sensitive data. Prompt leaking has emerged as the primary method for exposing sensitive information.

### Telemetry Data Profile
This section highlights key trends from our analysis of over 2,000 LLM applications. Customer Support Assistants dominate use cases at 57.6%, while Education leads industry adoption at 33.6%.

![Charts showing GenAI application distribution by Industry, Language, and Use Case]

---

## The LLM Default Protection Layers Adversaries Need to Bypass

Developers building generative AI applications try to control the security and alignment of their apps by leveraging multiple protective layers:

1. **Model-Level Protections**: Embedded into the model during training by its creators (e.g., safety alignment, filters).
2. **Prompt-Level Protections**: Application developers use system prompts to set ethical boundaries and define roles.

### Prompt Injection vs. Jailbreaking
- **Prompt Injection**: Embedding hidden or manipulated instructions into user input to trick the model.
- **Jailbreaking**: Disabling or bypassing the model’s safety and ethical constraints to create an environment where prompt injection can thrive.

---

## Top 3 Predominant Jailbreak Techniques

1. **Ignore Previous Instructions**: Direct prompt injection to override system prompts.
2. **Strong Arm Attack**: Direct prompt injection using authoritative phrases like "ADMIN OVERRIDE."
3. **Base64 Encoding**: Code & Encode technique to bypass content filters.

---

## Top Adversary Goals and Motivations

- **Data Exfiltration and Privacy Breaches**: Stealing proprietary business data and PII.
- **Bypassing Safety Filters**: Generating disinformation, hate speech, or malicious code.
- **Exploration and Curiosity**: "Ethical hackers" or hobbyists testing system limits.
- **Model Denial of Service and Infrastructure Hijacking**: Overwhelming systems or repurposing computational resources.

---

## Real-World Attacks on GenAI Applications

*Note: The report details six specific attack case studies involving Base64 encoding, format manipulation, ASCII art, "Ignore Previous Instructions," "DAN" (Do Anything Now) roleplaying, and Strong Arm attacks.*

![Diagrams of attack flows and results for the six case studies]

---

## Key Insights and Lessons Learned

- **Language-Agnostic Attacks**: Attacks occur in every language the LLM understands.
- **Vulnerabilities at Every Interaction Point**: Security is needed at inputs, instructions, tool outputs, and model outputs.
- **Consequences of Successful Jailbreaks**: Beyond data leakage, attackers gain access to powerful computational capabilities.
- **Limitations of Prompt Hardening**: Relying solely on system prompts is insufficient; an external, model-independent security layer is required.
- **Disparity Between Open-Source and Commercial Models**: Commercial models generally show higher resilience.
- **Importance of Session-Level Monitoring**: Individual prompts may look benign; context is required to detect patterns.

---

## 2025 Outlook: Predictions and Recommendations

- **From Chatbots to Agents**: Autonomous agents increase the attack surface significantly.
- **Proactive Security**: Implement red-teaming and "secure by design" principles early in development.
- **Dynamic Security Measures**: Move beyond static controls to context-aware, model-agnostic security.
- **Proliferation of Small Models**: Local deployment on personal devices expands the attack surface, requiring new privacy and integrity safeguards.

---

## The Need for AI Security

Pillar is committed to helping organizations navigate AI risks by:
- **Identifying** key use cases and associated risks.
- **Testing** AI resilience through red-teaming.
- **Building** an operational AI security organization.

---

## Methodology

Our research is based on Pillar’s proprietary telemetry data from over 2,000 real-world LLM-powered applications. We mapped identified techniques to frameworks such as the **OWASP Top 10 for LLMs** and **MITRE ATLAS**.

---

## About Pillar Security

Pillar provides a platform to secure the entire AI adoption lifecycle. Our founding team brings over 50 years of combined cybersecurity experience, delivering robust protection through real-world threat intelligence and adaptive runtime security.

![Screenshot of the Pillar Security platform interface showing a detected prompt injection]

---

## References

- [A Deep Dive into LLM Jailbreaking Techniques](https://www.pillar.security/blog/a-deep-dive-into-llm-jailbreaking-techniques-and-their-implications)
- [AI Security Buyer's Guide](https://www.pillar.security/resources/buyer-guide)
- [ArtPrompt: ASCII Art-based Jailbreak Attacks](https://arxiv.org/abs/2402.11753)
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [MITRE ATLAS Matrix](https://atlas.mitre.org/matrices/ATLAS)
- [CSA: Securing LLM Backed Systems](https://cloudsecurityalliance.org/artifacts/securing-llm-backed-systems-essential-authorization-practices)
- [McKinsey: The state of AI in early 2024](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [Characterizing and Evaluating In-The-Wild Jailbreak Prompts](https://arxiv.org/pdf/2308.03825)
- [Prompt injection and jailbreaking are not the same thing](https://simonwillison.net/2024/Mar/5/prompt-injection-jailbreaking/)
- [A Single Cloud Compromise Can Feed an Army of AI Sex Bots](https://krebsonsecurity.com/2024/10/a-single-cloud-compromise-can-feed-an-army-of-ai-sex-bots/)

[^1]: Pillar Security, 2025.