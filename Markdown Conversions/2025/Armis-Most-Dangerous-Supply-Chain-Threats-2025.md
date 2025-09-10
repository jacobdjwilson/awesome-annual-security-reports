# Catch Attackers Before They Strike

Q3, 2025

Early Warning Insights for Software Supply Chain Attacks

These insights were created by Armis Labs, a division of Armis. Use of these insights is permitted provided that full attribution and linkback to the report is provided.

© Copyright Armis 2025

## Table of Contents
- [Executive Summary](#executive-summary)
  - [Key Takeaways](#key-takeaways)
- [Introduction](#introduction)
  - [What To Expect From This Report?](#what-to-expect-from-this-report)
  - [What Makes The Armis Labs Top 25 Unique?](#what-makes-the-armis-labs-top-25-unique)
  - [Log4Shell, Log4j (CVE-2021-44228)](#log4shell-log4j-cve-2021-44228)
- [How AI Created Slopsquatting Risks](#how-ai-created-slopsquatting-risks)
  - [What Slopsquatting is:](#what-slopsquatting-is)
  - [Malware Delivery](#malware-delivery)
  - [Supply-Chain Compromise](#supply-chain-compromise)
  - [Widespread Reach](#widespread-reach)
- [With Vibe Coding, It Got Worse](#with-vibe-coding-it-got-worse)
  - [1. Authentication Failures Enable Account Compromise](#1-authentication-failures-enable-account-compromise)
  - [2. Session Management Flaws Risk Session Hijacking](#2-session-management-flaws-risk-session-hijacking)
  - [3. Input-Validation & Injection Weaknesses Lead to Data Theft](#3-input-validation--injection-weaknesses-lead-to-data-theft)
  - [4. Missing HTTP Security Headers Expose Web Interfaces](#4-missing-http-security-headers-expose-web-interfaces)
  - [5. Error-Handling & Logging Shortcomings Aid Reconnaissance](#5-error-handling--logging-shortcomings-aid-reconnaissance)
  - [Overall Risk Assessment](#overall-risk-assessment)
  - [Key Recommendations to Mitigate Impact](#key-recommendations-to-mitigate-impact)
- [Top 25 Software Supply Chain Attacks](#top-25-software-supply-chain-attacks)
  - [Top 25 - Actions To Take](#top-25---actions-to-take)
- [The Importance of Early Warning Threat Intelligence](#the-importance-of-early-warning-threat-intelligence)
- [Indicators of Action (IoAs)](#indicators-of-action-ioas)
  - [System Behavior Indicators](#system-behavior-indicators)
  - [Privilege & Credential Abuse Indicators](#privilege--credential-abuse-indicators)
  - [Network Behavior Indicators](#network-behavior-indicators)
  - [Build & Installation Indicators](#build--installation-indicators)
  - [Metadata & Source Control Anomalies](#metadata--source-control-anomalies)
- [Mitigation Strategies](#mitigation-strategies)
  - [Package & Supply-Chain Integrity](#package--supply-chain-integrity)
  - [Developer & User Awareness](#developer--user-awareness)
- [Armis Vulnerability Intelligence Database](#armis-vulnerability-intelligence-database)
  - [How Armis Vulnerability Intelligence Database Stands Out](#how-armis-vulnerability-intelligence-database-stands-out)
  - [Working with CISA KEV And Going Beyond It](#working-with-cisa-kev-and-going-beyond-it)
- [About Armis Centrix™](#about-armis-centrix)
  - [Armis Centrix™ for Early Warning](#armis-centrix-for-early-warning)
- [About Armis Labs](#about-armis-labs)

---

### What To Expect From This Report?

For the C-suite, this report offers an overview of software supply chain risks, widely exploited open-source software libraries, and emerging cyber threat trends.

For (application) security teams, it offers an evidence-based and actionable Top 25 of software supply chain attacks, and an overview of Indicators of Action (IoAs) to address and monitor.

### What Makes The Armis Labs Top 25 Unique?

Our research team leverages a combination of human intelligence, dynamic deception technology and AI/ML that detects threat actor behaviors before actual exploitation, including flaws in threat actors operations and context of their discussions. This evidence-based approach leads to different application security risks than similar rankings like the OWASP Top 10 or the CWE™ Top 25.

## Executive Summary

Open-source software libraries form the backbone of modern application development, offering immense benefits in terms of collaboration, innovation, and accelerated development cycles. Their inherent transparency and community-driven development foster a rapid pace of improvement and broad accessibility.

But what happens when the very app software libraries we rely on are compromised before they even reach us? This is the alarming reality of software supply chain attacks. These attacks exploit vulnerabilities in the development, distribution, or implementation of software, causing widespread disruption and raising serious security concerns.

Understanding the nature of these attacks and their growing prevalence is key to protecting both organizations and individuals. This report dives into the world of software supply chain attacks, exploring how they work, what makes them so dangerous, and why addressing these risks has become imperative.

### Key Takeaways

*   Slopsquatting emerges as a threat and has the potential to compromise apps (including Line of Business), microservices, infrastructure using these libraries, supply chains and much more across an organization’s ecosystem.
*   An overreliance on AI-generated code suggestions without rigorous human oversight can lead to the integration of fragile and vulnerable code into a codebase.
*   By focusing on Indicators of Actions (IoAs) of an adversary rather than just the static artifacts of a compromise, organizations can build a more resilient and proactive security posture. This shift enables early detection, rapid response, and ultimately, significantly reduces the impact of sophisticated cyber threats, moving the advantage from the attacker back to the defender.

## Introduction

The omnipresent adoption of open-source libraries has fundamentally reshaped the landscape of software development. They offer exceptional advantages in terms of rapid development, cost efficiency, community support, and access to cutting-edge technologies. From operating systems and web frameworks to specialized algorithms and machine learning tools, open-source components are at the heart of countless modern applications. However, this widespread integration also introduces a critical, often underestimated, vulnerability: the security of these very libraries.

One of the primary reasons for this importance lies in the sheer volume and complexity of dependencies. A typical modern application might rely on dozens, even hundreds, of open-source libraries, each with its own set of sub-dependencies. This creates a vast and intricate supply chain. A vulnerability in just one seemingly innocuous, deeply nested library can ripple upwards, exposing the entire application to potential exploitation. This “supply chain attack” vector has become increasingly prevalent, with malicious actors specifically targeting widely used open-source components to gain access to a multitude of downstream systems. If a flaw exists in a popular library, it essentially becomes a skeleton key, potentially unlocking thousands or even millions of applications simultaneously.

Beyond direct exploitation, insecure open-source libraries can introduce a range of other serious issues. They can lead to data breaches, compromising sensitive user information or intellectual property. They can enable denial-of-service attacks, crippling critical services and causing significant financial losses. They can also serve as entry points for more sophisticated attacks, allowing adversaries to establish persistent footholds within systems or networks. The reputational damage alone from a security incident stemming from an unpatched open-source vulnerability can be immense, eroding user trust and impacting business operations.

### Log4Shell, Log4j (CVE-2021-44228)

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

*   **AI-Induced Hallucinations**: AI coding tools (e.g. ChatGPT, GitHub Copilot, CodeLlama) sometimes suggest non-existent libraries or packages that “sound” plausible.
*   **Attacker Pre-Registration**: Malicious actors anticipate these hallucinations, register the fake package names on public repositories (PyPI, npm, etc.), and embed trojanized code.
*   **Automated Exploitation**: A developer’s CI/CD pipeline or local build process can automatically fetch and install these packages, resulting in silent compromise ([trendmicro.com](https://www.trendmicro.com/), [gmv.com](https://www.gmv.com/)).

### Malware Delivery

A real-world example is the slopsquatting package ccxt-mexc-futures masqueraded as an add-on for the popular ccxt crypto library. The package was designed to reroute cryptocurrency trading orders placed on the MEXC exchange to a malicious server to steal tokens. Although the package has been removed from PyPI, it was downloaded over 1,065 times, according to [pepy.tech](https://pepy.tech/).

The package falsely claimed to extend the popular Python library ccxt, which is commonly used for cryptocurrency trading. On closer inspection, it was revealed that the package maliciously modified specific APIs associated with MEXC’s trading interface, enabling attackers to execute arbitrary code. It diverted requests to a fake domain impersonating MEXC, ultimately stealing API keys, sensitive details, and cryptocurrency tokens.

Source: The Hacker News
![Diagram illustrating malware delivery via slopsquatting, showing an AI coding tool suggesting a non-existent package, an attacker registering it, and a developer's CI/CD pipeline installing the malicious package.]

Victims who installed the package were advised to revoke potentially compromised tokens and remove the package immediately. The discovery highlights the rising trend of supply chain attacks across platforms like npm, PyPI, and Go.

### Supply-Chain Compromise

Once integrated, malicious packages can exfiltrate secrets, inject further payloads into your code, or pivot laterally within your environment.

### Widespread Reach

Automated dependency resolution and “lock-file” upgrades can cause slopsquatting malware to propagate across multiple projects and organizations without human review.

## With Vibe Coding, It Got Worse

The increasing organizational demand for speed and agility has led to the widespread adoption of “vibe coding”—a practice characterized by rapid prototyping and code deployment with minimal peer review. This accelerated approach has shown that 40% of the time, the LLM-generated code suggestions exhibited vulnerabilities. The table below provides an overview of vulnerabilities introduced by various LLM models across the MITRE ATT&CK stages.

![Chart showing LLM non-compliance rates in helping with cyberattacks, indicating higher is better.]
Source: Purple Llama CyberSecEval: A benchmark for evaluating the cybersecurity risks of large language models

Other findings across the industry using Vibe Coding with Large LLMs (GPT, DeepSeek, Gemini, etc) include:

### 1. Authentication Failures Enable Account Compromise

*   **No Brute-Force Throttling (except Gemini)**: Without account lockout, attackers can rapidly automate thousands of login attempts, increasing the odds of credential stuffing and stolen accounts.
*   **Missing CAPTCHA (all models)**: Bots can mount large-scale automated attacks unimpeded, leading to credential harvesting and service abuse.
*   **Lack of MFA (all models)**: Single-factor logins leave every account one leaked password away from takeover, eroding user trust and exposing sensitive data.
*   **Weak Password Policies (only Grok enforces complexity)**: Simple passwords accelerate brute-force success, making user and admin accounts easy targets.

### 2. Session Management Flaws Risk Session Hijacking

*   **Inconsistent Secure-Cookie Flags**: Models that omit `Secure` and `HttpOnly` flags risk cookie theft over unsecured channels, allowing attackers to impersonate legitimate users.
*   **Session Fixation Gaps (Claude)**: Without regenerating session IDs on login, attackers can force a known session ID and later take over an authenticated session.
*   **No Idle-Timeout Enforcement**: Long-lived sessions give attackers extended windows to misuse stolen session tokens.

### 3. Input-Validation & Injection Weaknesses Lead to Data Theft

*   **Parameterized Queries Only (good)**: SQL injection is largely mitigated—one bright spot.
*   **Persistent XSS (DeepSeek, Gemini)**: Unsanitized input fields let attackers inject scripts, compromising user browsers and potentially spreading malware.
*   **Inadequate CSRF Defenses (only Claude protected)**: Without CSRF tokens, attackers can trick logged-in users into executing unwanted actions.
*   **Open CORS Policies (all models)**: Permissive cross-origin settings allow malicious sites to interact with APIs and steal data.

### 4. Missing HTTP Security Headers Expose Web Interfaces

*   **No Content Security Policy**: Attackers can load malicious scripts or resources from untrusted domains.
*   **Absent Clickjacking Protections**: UI frames can be overlaid by attacker pages to trick users into unintended actions.
*   **No HSTS Enforced**: Users remain vulnerable to SSL stripping attacks, exposing credentials on insecure networks.

### 5. Error-Handling & Logging Shortcomings Aid Reconnaissance

*   **Verbose Error Messages (Gemini)**: Revealing whether a username exists or password complexity rules helps attackers fine-tune their brute-force attacks.
*   **Sparse Failed-Login Logging (only Gemini & Grok)**: Without comprehensive logging, repeated attack patterns go unnoticed, delaying incident response.
*   **No Anomaly Detection**: Lack of alerts on unusual login spikes or geographic anomalies lets large-scale credential stuffing campaigns fly under the radar.

### Overall Risk Assessment

All tested LLM stacks exhibit “very high” to “extreme” security risks—particularly Claude and DeepSeek—creating multiple attack vectors for real-world breaches. No platform currently delivers an end-to-end security posture aligned with OWASP Top 10 or NIST standards.

### Key Recommendations to Mitigate Impact

1.  **Embed Security in Prompts**: Require LLMs to generate code with built-in protections (lockouts, MFA stubs, input sanitization).
2.  **Automated Security Testing**: Integrate generated code into CI pipelines using OWASP ZAP, SAST tools, and fuzzers before deployment.
3.  **Mandatory Human Review**: Enforce security expert sign-off on all LLM-produced modules.
4.  **Secure-By-Default LLMs**: Encourage model vendors to bake in CSP headers, secure cookies, and CSRF tokens—even when not explicitly prompted.

While LLMs enhance developer productivity, their generated code contains significant security vulnerabilities that could lead to breaches in real-world applications. Exacerbating this risk, recent widespread layoffs across the tech industry have significantly reduced engineering team sizes. This reduction in workforce translates to less time for critical code reviews, a depletion of institutional knowledge, and an increased reliance on AI tools or quick solutions. An overreliance on AI-generated code suggestions without rigorous human oversight will lead to the integration of fragile and vulnerable code into a codebase, even before considering external threats such as slopsquatting.

## Top 25 Software Supply Chain Attacks

Open-source libraries are targeted in cyberattacks due to their widespread use and the potential for widespread impact when vulnerabilities are exploited. Armis Labs have found that some common attack vectors include supply chain attacks, where malicious code is injected into a library and then propagated to users of that library, and dependency confusion, where malicious packages are created that mimic legitimate ones.

Below is a table[^1] that highlights the top 25 software supply chain attacks, their methods, and mitigation strategies.

| Ecosystem         | Attack              | Year(s)    | Versions Affected      | Attack Method                                  | Mitigation                                     |
| :---------------- | :------------------ | :--------- | :--------------------- | :--------------------------------------------- | :--------------------------------------------- |
| JavaScript (npm)  | event-stream        | 2018       | v3.3.6                 | Wallet exfiltration via dependency             | Removed malicious dependency.                  |
|                   | eslint-scope        | 2018       | v3.7.2, 5.0.2          | Post-install Pastebin exfiltration.            | Token revocation, secure versions.             |
|                   | UAParser.js         | 2021       | v0.7.29, 0.8.0, 1.0.0  | Preinstall script loaded trojans.              | Patched releases.                              |
|                   | coa                 | 2021       | v2.0.3, 2.0.4, 2.1.1   | Credential stealer, miner.                     | Reverted to safe version.                      |
|                   | rc                  | 2021       | v1.2.9, 1.3.9, 2.3.9   | Same as coa.                                   | Malicious versions removed.                    |
|                   | xrpl.js             | 2025       | v4.2.1–4.2.4, 2.14.2   | Private key theft via backdoored publish.      | Update to 4.2.5, 2.14.3.                       |
|                   | Solana web3.js      | 2024       | v1.95.6, 1.95.7        | Wallet key exfiltration via backdoored function. | Patched release.                               |
|                   | node-ipc            | 2022       | v10.1.1, 10.1.2        | Geo-targeted file wiper (protestware).         | Versions removed, project forked.              |
|                   | colors.js/faker.js  | 2022       | v1.4.1, 1.4.2, 6.6.6   | Infinite loop (protestware).                   | Forks replaced libraries.                      |
| Python (PyPI)     | SSH Decorator       | 2018       | Multiple               | SSH credential exfiltration.                   | Yanked, new package.                           |
|                   | jeIlyfish / python3-dateutil | 2019       | N/A                    | SSH/GPG key theft (typosquatting).             | Removed from PyPI.                             |
|                   | fastapi-toolkit     | 2022       | N/A                    | RCE via malicious payloads.                    | Removed.                                       |
|                   | requests-darwin-lite | 2024       | All versions           | Backdoor in PNG.                               | Yanked.                                        |
|                   | torchtriton         | 2022       | N/A                    | DNS-based data exfiltration.                   | Name seized, users warned.                     |
| Ruby (RubyGems)   | bootstrap-sass      | 2019       | v3.2.0.3               | RCE via cookie eval.                           | Yanked, replaced with 3.2.0.4.                 |
|                   | strong_password     | 2019       | v0.0.7                 | Eval via cookie, exfiltration.                 | Yanked, revert to 0.0.6.                       |
|                   | rest-client         | 2019       | v1.6.10–1.6.13         | Pastebin fetcher, credential theft.            | Removed, post-mortem.                          |
|                   | misc Ruby gems      | 2019       | 10+ packages, Multiple | Miner/credential theft.                        | Yanked from RubyGems.                          |
| Linux Tools       | XZ Utils            | 2024       | v5.6.0, 5.6.1          | SSH bypass via liblzma hook.                   | Downgrade to 5.4.x, global audits.             |
|                   | Socat               | 2016       | Multiple               | Non-prime DH parameter.                        | Switched to strong prime.                      |
|                   | Webmin              | 2018–2019  | v1.890–1.920           | RCE via altered update file.                   | Clean rebuild, community alert.                |
| Java (GitHub)     | Octopus Scanner     | 2018       | N/A                    | `rm -rf /` payload in ebuild scripts.          | 2FA enforced, repo lockdown.                   |
|                   |                     | 2020       | N/A                    | Injected JAR into NetBeans builds.             | GitHub SIRT cleaned repos.                     |
| Rust              | liblzma-sys         | 2024       | v0.3.2                 | Packaged XZ test files (not executed).         | Yanked, fixed in 0.3.3.                        |
| PHP               | PEAR Installer      | 2019       | go-pear.phar           | Backdoored archive with RCE.                   | Rebuilt from GitHub, hash check.               |

[^1]: Source: Armis Labs

Armis Labs uses a combination of human intelligence, dynamic deception technologies and AI/ML that detects threat actor behaviors before actual exploitation, including flaws in threat actors operations and context of their discussions. This evidence-based approach leads to different top 25 application security risks than similar rankings like the OWASP Top 10:

![Diagram comparing Armis Labs' Top 25 application security risks with OWASP Top 10, highlighting differences in approach.]

### Top 25 - Actions To Take

1.  **Provenance Tracking with Software Bills of Materials (SBOMs)**
    Generate and cryptographically sign SBOMs for every build, ensuring each dependency’s origin and version are auditable. Determine through installation if any packages are directly used or indirectly used, for example packages.json and packages-lock.json. Ensure versions are specifically set.
2.  **Application Security Testing**
    Leverage Static application security testing (SAST) and dynamic application security testing (DAST) to find vulnerabilities that could leave your organization’s applications susceptible to attack.
3.  **Assess Business Impact**
    Which specific applications, features, or parts of your system are impacted?
4.  **Remediate and Mitigate**
    Determine who is (most likely) responsible for the asset and the remediation. Leverage existing workflows and tools, and include clear, actionable remediation guidance.

##