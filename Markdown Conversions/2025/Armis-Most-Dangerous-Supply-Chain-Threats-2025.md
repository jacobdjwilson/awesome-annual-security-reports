# Catch Attackers Before They Strike
## Early Warning Insights for Software Supply Chain Attacks

Q3, 2025

These insights were created by Armis Labs, a division of Armis. Use of these insights is permitted provided that full attribution and linkback to the report is provided.

© Copyright Armis 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [How AI Created Slopsquatting Risks](#how-ai-created-slopsquatting-risks)
- [With Vibe Coding, It Got Worse](#with-vibe-coding-it-got-worse)
- [Top 25 Software Supply Chain Attacks](#top-25-software-supply-chain-attacks)
- [The Importance of Early Warning Threat Intelligence](#the-importance-of-early-warning-threat-intelligence)
- [Indicators of Action (IoAs)](#indicators-of-action-ioas)
- [Mitigation Strategies](#mitigation-strategies)
- [Armis Vulnerability Intelligence Database](#armis-vulnerability-intelligence-database)
- [About Armis Centrix™](#about-armis-centrix)
- [About Armis Labs](#about-armis-labs)

## What To Expect From This Report?

For the C-suite, this report offers an overview of software supply chain risks, widely exploited open-source software libraries, and emerging cyber threat trends.

For (application) security teams, it offers an evidence-based and actionable Top 25 of software supply chain attacks, and an overview of Indicators of Action (IoAs) to address and monitor.

### What Makes The Armis Labs Top 25 Unique?

Our research team leverages a combination of human intelligence, dynamic deception technology and AI/ML that detects threat actor behaviors before actual exploitation, including flaws in threat actors operations and context of their discussions. This evidence-based approach leads to different application security risks than similar rankings like the OWASP Top 10 or the CWE™ Top 25.

## Executive Summary

Open-source software libraries form the backbone of modern application development, offering immense benefits in terms of collaboration, innovation, and accelerated development cycles. Their inherent transparency and community-driven development foster a rapid pace of improvement and broad accessibility.

But what happens when the very app software libraries we rely on are compromised before they even reach us? This is the alarming reality of software supply chain attacks. These attacks exploit vulnerabilities in the development, distribution, or implementation of software, causing widespread disruption and raising serious security concerns.

Understanding the nature of these attacks and their growing prevalence is key to protecting both organizations and individuals. This report dives into the world of software supply chain attacks, exploring how they work, what makes them so dangerous, and why addressing these risks has become imperative.

### Key Takeaways

- Slopsquatting emerges as a threat and has the potential to compromise apps (including Line of Business), microservices, infrastructure using these libraries, supply chains and much more across an organization’s ecosystem.
- An overreliance on AI-generated code suggestions without rigorous human oversight can lead to the integration of fragile and vulnerable code into a codebase.
- By focusing on Indicators of Actions (IoAs) of an adversary rather than just the static artifacts of a compromise, organizations can build a more resilient and proactive security posture. This shift enables early detection, rapid response, and ultimately, significantly reduces the impact of sophisticated cyber threats, moving the advantage from the attacker back to the defender.

## Introduction

The omnipresent adoption of open-source libraries has fundamentally reshaped the landscape of software development. They offer exceptional advantages in terms of rapid development, cost efficiency, community support, and access to cutting-edge technologies. From operating systems and web frameworks to specialized algorithms and machine learning tools, open-source components are at the heart of countless modern applications. However, this widespread integration also introduces a critical, often underestimated, vulnerability: the security of these very libraries.

One of the primary reasons for this importance lies in the sheer volume and complexity of dependencies. A typical modern application might rely on dozens, even hundreds, of open-source libraries, each with its own set of sub-dependencies. This creates a vast and intricate supply chain. A vulnerability in just one seemingly innocuous, deeply nested library can ripple upwards, exposing the entire application to potential exploitation. This “supply chain attack” vector has become increasingly prevalent, with malicious actors specifically targeting widely used open-source components to gain access to a multitude of downstream systems. If a flaw exists in a popular library, it essentially becomes a skeleton key, potentially unlocking thousands or even millions of applications simultaneously.

Beyond direct exploitation, insecure open-source libraries can introduce a range of other serious issues. They can lead to data breaches, compromising sensitive user information or intellectual property. They can enable denial-of-service attacks, crippling critical services and causing significant financial losses. They can also serve as entry points for more sophisticated attacks, allowing adversaries to establish persistent footholds within systems or networks. The reputational damage alone from a security incident stemming from an unpatched open-source vulnerability can be immense, eroding user trust and impacting business operations.

### The one we all know of from the past:
#### Log4Shell, Log4j (CVE-2021-44228)

Perhaps the most prominent takeaway of this long-tail vulnerability, was the pervasive and often hidden nature of dependencies in modern software. Many organizations were unaware they were even using Log4j, let alone a vulnerable version, highlighting the need for robust Software Bill of Materials (SBOMs) and dependency scanning tools.

This incident underscored that a single flaw in a widely used, foundational library can have a catastrophic ripple effect across countless applications and industries, emphasizing the shared responsibility in maintaining the integrity of the open-source supply chain.

Another crucial lesson revolved around the fragility of open-source maintenance. Log4j, like many vital open-source projects, was maintained by a small group of dedicated volunteers, often with limited resources. The sheer scale of the Log4Shell crisis overwhelmed these maintainers, revealing a systemic issue where critical infrastructure relies on underfunded and understaffed projects. This highlighted the urgent need for greater investment, support, and recognition for open-source contributors, whether through direct funding, corporate sponsorship, or community initiatives.

The incident also exposed a gap in proactive security auditing and testing within the open-source community, suggesting that more formalized security reviews and penetration testing should be integrated into the development lifecycle of widely adopted libraries.

Log4Shell spurred a greater focus on secure coding practices and threat modeling within development teams, reinforcing the idea that security should be baked into the software development lifecycle from the outset, rather than treated as an afterthought.

## How AI Created Slopsquatting Risks

Historically, compromising a software supply chain was a high-effort undertaking, demanding sophisticated infiltration of trusted vendors, tampering with build environments, and covertly injecting malicious code over months to ensure its propagation through official releases.

Today, the threat landscape has shifted dramatically with the emergence of slopsquatting. This automated attack vector exploits the tendency of AI coding assistants to “hallucinate” package names. Attackers preemptively register these nonexistent package names, allowing them to trick developers into unwittingly installing malicious code.

While AI coding assistants offer significant promise for enhancing developer productivity, they are far from infallible and can inadvertently introduce substantial vulnerabilities into software. Research indicates that as many as half of the code snippets generated by current AI tools contain exploitable security flaws, including buffer overflows, SQL injections, and insecure default configurations. Furthermore, these large language models (LLMs) often exhibit unpredictable behavior. They can “hallucinate” nonexistent functions, omit critical error handling, or provide inaccurate information regarding API behaviors.

When a developer copies and pastes AI-suggested code containing these “phantom” dependencies, they bypass traditional supply chain security measures and directly introduce malware or backdoors into their projects, all without the need for a complex vendor compromise. A single slopsquatting incident can propagate unchecked, potentially compromising numerous microservices and shared libraries across an organization’s ecosystem.

### What Slopsquatting is:

- AI‑Induced Hallucinations: AI coding tools (e.g. ChatGPT, GitHub Copilot, CodeLlama) sometimes suggest non-existent libraries or packages that “sound” plausible.
- Attacker Pre‑Registration: Malicious actors anticipate these hallucinations, register the fake package names on public repositories (PyPI, npm, etc.), and embed trojanized code.
- Automated Exploitation: A developer’s CI/CD pipeline or local build process can automatically fetch and install these packages, resulting in silent compromise ([trendmicro.com](https://www.trendmicro.com/), [gmv.com](https://www.gmv.com/)).

### Malware Delivery
A real-world example is the slopsquatting package ccxt-mexc-futures masqueraded as an add-on for the popular ccxt crypto library. The package was designed to reroute cryptocurrency trading orders placed on the MEXC exchange to a malicious server to steal tokens. Although the package has been removed from PyPI, it was downloaded over 1,065 times, according to pepy.tech.

The package falsely claimed to extend the popular Python library ccxt, which is commonly used for cryptocurrency trading. On closer inspection, it was revealed that the package maliciously modified specific APIs associated with MEXC’s trading interface, enabling attackers to execute arbitrary code. It diverted requests to a fake domain impersonating MEXC, ultimately stealing API keys, sensitive details, and cryptocurrency tokens.

[Source: The Hacker News](https://thehackernews.com/)

Victims who installed the package were advised to revoke potentially compromised tokens and remove the package immediately. The discovery highlights the rising trend of supply chain attacks across platforms like npm, PyPI, and Go.

### Supply‑Chain Compromise

Once integrated, malicious packages can exfiltrate secrets, inject further payloads into your code, or pivot laterally within your environment.

### Widespread Reach

Automated dependency resolution and “lock-file” upgrades can cause slopsquatting malware to propagate across multiple projects and organizations without human review.

## With Vibe Coding, It Got Worse

The increasing organizational demand for speed and agility has led to the widespread adoption of “vibe coding”—a practice characterized by rapid prototyping and code deployment with minimal peer review. This accelerated approach has shown that 40% of the time, the LLM-generated code suggestions exhibited vulnerabilities. The table below provides an overview of vulnerabilities introduced by various LLM models across the MITRE ATT&CK stages.

### LLM non-compliance rate in helping with cyberattacks (higher is better)

| MITRE ATT&CK Stage | GPT-4 | GPT-3.5 | Gemini Pro | Claude 2.1 | DeepSeek Coder | Grok |
| :----------------- | :---- | :------ | :--------- | :--------- | :------------- | :--- |
| Reconnaissance | 70% | 60% | 55% | 45% | 40% | 65% |
| Resource Development | 65% | 55% | 50% | 40% | 3