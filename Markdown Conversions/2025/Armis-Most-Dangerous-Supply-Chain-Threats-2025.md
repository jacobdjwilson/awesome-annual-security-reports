# Most-Dangerous-Supply-Chain-Threats

**Organization:** Armis  
**Year:** 2025

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

---

## Executive Summary

Open-source software libraries form the backbone of modern application development, offering immense benefits in terms of collaboration, innovation, and accelerated development cycles. Their inherent transparency and community-driven development foster a rapid pace of improvement and broad accessibility.

But what happens when the very app software libraries we rely on are compromised before they even reach us? This is the alarming reality of software supply chain attacks. These attacks exploit vulnerabilities in the development, distribution, or implementation of software, causing widespread disruption and raising serious security concerns.

Understanding the nature of these attacks and their growing prevalence is key to protecting both organizations and individuals. This report dives into the world of software supply chain attacks, exploring how they work, what makes them so dangerous, and why addressing these risks has become imperative.

### Key Takeaways

- **Slopsquatting** emerges as a threat and has the potential to compromise apps (including Line of Business), microservices, infrastructure using these libraries, supply chains and much more across an organization’s ecosystem.
- An overreliance on AI-generated code suggestions without rigorous human oversight can lead to the integration of fragile and vulnerable code into a codebase.
- By focusing on Indicators of Actions (IoAs) of an adversary rather than just the static artifacts of a compromise, organizations can build a more resilient and proactive security posture. This shift enables early detection, rapid response, and ultimately, significantly reduces the impact of sophisticated cyber threats, moving the advantage from the attacker back to the defender.

---

## Introduction

The omnipresent adoption of open-source libraries has fundamentally reshaped the landscape of software development. They offer exceptional advantages in terms of rapid development, cost efficiency, community support, and access to cutting-edge technologies. From operating systems and web frameworks to specialized algorithms and machine learning tools, open-source components are at the heart of countless modern applications. However, this widespread integration also introduces a critical, often underestimated, vulnerability: the security of these very libraries.

One of the primary reasons for this importance lies in the sheer volume and complexity of dependencies. A typical modern application might rely on dozens, even hundreds, of open-source libraries, each with its own set of sub-dependencies. This creates a vast and intricate supply chain. A vulnerability in just one seemingly innocuous, deeply nested library can ripple upwards, exposing the entire application to potential exploitation. This “supply chain attack” vector has become increasingly prevalent, with malicious actors specifically targeting widely used open-source components to gain access to a multitude of downstream systems.

### The one we all know of from the past: Log4Shell, Log4j (CVE-2021-44228)

Perhaps the most prominent takeaway of this long-tail vulnerability was the pervasive and often hidden nature of dependencies in modern software. Many organizations were unaware they were even using Log4j, let alone a vulnerable version, highlighting the need for robust Software Bill of Materials (SBOMs) and dependency scanning tools.

This incident underscored that a single flaw in a widely used, foundational library can have a catastrophic ripple effect across countless applications and industries, emphasizing the shared responsibility in maintaining the integrity of the open-source supply chain.

---

## How AI Created Slopsquatting Risks

Historically, compromising a software supply chain was a high-effort undertaking. Today, the threat landscape has shifted dramatically with the emergence of **slopsquatting**. This automated attack vector exploits the tendency of AI coding assistants to “hallucinate” package names. Attackers preemptively register these nonexistent package names, allowing them to trick developers into unwittingly installing malicious code.

### What Slopsquatting is:

- **AI-Induced Hallucinations:** AI coding tools (e.g., ChatGPT, GitHub Copilot, CodeLlama) sometimes suggest non-existent libraries or packages that “sound” plausible.
- **Attacker Pre-Registration:** Malicious actors anticipate these hallucinations, register the fake package names on public repositories (PyPI, npm, etc.), and embed trojanized code.
- **Automated Exploitation:** A developer’s CI/CD pipeline or local build process can automatically fetch and install these packages, resulting in silent compromise.

---

## With Vibe Coding, It Got Worse

The increasing organizational demand for speed and agility has led to the widespread adoption of “vibe coding”—a practice characterized by rapid prototyping and code deployment with minimal peer review. This accelerated approach has shown that 40% of the time, the LLM-generated code suggestions exhibited vulnerabilities.

![Chart showing LLM non-compliance rate in helping with cyberattacks]

### Key Findings:
1. **Authentication Failures:** No brute-force throttling, missing CAPTCHA, and lack of MFA.
2. **Session Management Flaws:** Inconsistent secure-cookie flags and session fixation gaps.
3. **Input-Validation & Injection:** Persistent XSS and open CORS policies.
4. **Missing HTTP Security Headers:** No Content Security Policy and absent clickjacking protections.
5. **Error-Handling & Logging:** Verbose error messages and sparse failed-login logging.

---

## Top 25 Software Supply Chain Attacks

Armis Labs has identified the top 25 software supply chain attacks, their methods, and mitigation strategies.

| Ecosystem | Attack | Year(s) | Attack Method |
| :--- | :--- | :--- | :--- |
| JavaScript (npm) | event-stream | 2018 | Wallet exfiltration via dependency |
| JavaScript (npm) | eslint-scope | 2018 | Post-install Pastebin exfiltration |
| JavaScript (npm) | UAParser.js | 2021 | Preinstall script loaded trojans |
| Python (PyPI) | torchtriton | 2022 | DNS-based data exfiltration |
| Linux Tools | XZ Utils | 2024 | SSH bypass via liblzma hook |

*(Note: Table truncated for brevity; see full report for complete list of 25)*

---

## The Importance of Early Warning Threat Intelligence

Traditional security solutions operate “right of boom,” or after the attack has occurred. Armis redefines the approach by taking action “left of boom,” or before the attack is launched.

### Recent Early Warning Examples:
- **Gravity Forms:** Malicious code injected into plugin versions 2.9.1.1 and 2.9.12. Armis identified the backdoor and call out to a rogue domain.
- **GitHub Actions (tj-actions/changed-files):** A multi-stage attack compromised multiple GitHub Actions via a leaked PAT.
- **NPM Install (UA-Parser-JS Malware):** Detected malicious code being injected into versions 0.7.29, 0.8.0, and 1.0.0.

---

## Indicators of Action (IoAs)

IoAs focus on the behaviors, methods, and intent of an adversary.

- **System Behavior Indicators:** Unexpected CPU spikes, increased memory usage, files written to unusual directories.
- **Privilege & Credential Abuse:** Attempts to escalate privileges, access to environment variables, reading sensitive files (.env, ~/.ssh/).
- **Network Behavior:** Outbound connections to unknown domains, beaconing, DNS tunneling.
- **Build & Installation:** Unexpected pre- or post-installation scripts, obfuscated code, sudden increase in package size.

---

## Mitigation Strategies

- **Provenance Tracking:** Generate and cryptographically sign SBOMs for every build.
- **Application Security Testing:** Leverage SAST and DAST to find vulnerabilities.
- **Registry Allow-listing:** Restrict package installs to approved registries.
- **Dependency Scanning:** Integrate vulnerability scanners into CI/CD pipelines.
- **Developer Awareness:** Educate teams to double-check package names and avoid blind reliance on AI suggestions.

---

## Armis Vulnerability Intelligence Database

The Armis Vulnerability Intelligence Database is an AI-powered resource that goes beyond traditional static databases like CISA KEV. It provides real-time context, community-driven prioritization, and actionable insights tailored to specific industries.

- **CNA Authorization:** Armis is authorized by the CVE® Program as a CVE Numbering Authority (CNA).

---

## About Armis Centrix™

Armis Centrix™, the cyber exposure management platform, sees, secures, protects, and manages billions of assets around the world in real time. It combines asset intelligence with vulnerability intelligence to prioritize risks, reduce alert fatigue, and proactively mitigate threats.

---

## About Armis Labs

Armis Labs is a division of Armis dedicated to investigating the latest trends and tactics employed by cyber adversaries. Leveraging access to over 6 billion profiled assets and state-of-the-art tools—including deception technology, incident forensics, and reverse engineering—Armis Labs empowers organizations to stay ahead of cyber adversaries.

---
*© Copyright Armis 2025*