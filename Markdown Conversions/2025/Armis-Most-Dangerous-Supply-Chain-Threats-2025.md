# Most-Dangerous-Supply-Chain-Threats

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

Q3, 2025
Catch Attackers Before They Strike
Early Warning Insights for Software Supply Chain Attacks
These insights were created by Armis Labs, a division of Armis. Use of these insights is permitted provided that full attribution and linkback to the report is provided.
© Copyright Armis 2025

## Executive Summary
Open-source software libraries form the backbone of modern application development, offering immense benefits in terms of collaboration, innovation, and accelerated development cycles. Their inherent transparency and community-driven development foster a rapid pace of improvement and broad accessibility.

But what happens when the very app software libraries we rely on are compromised before they even reach us? This is the alarming reality of software supply chain attacks. These attacks exploit vulnerabilities in the development, distribution, or implementation of software, causing widespread disruption and raising serious security concerns.

Understanding the nature of these attacks and their growing prevalence is key to protecting both organizations and individuals. This report dives into the world of software supply chain attacks, exploring how they work, what makes them so dangerous, and why addressing these risks has become imperative.

### Key Takeaways
- **Slopsquatting** emerges as a threat and has the potential to compromise apps (including Line of Business), microservices, infrastructure using these libraries, supply chains and much more across an organization’s ecosystem.
- An overreliance on AI-generated code suggestions without rigorous human oversight can lead to the integration of fragile and vulnerable code into a codebase.
- By focusing on Indicators of Actions (IoAs) of an adversary rather than just the static artifacts of a compromise, organizations can build a more resilient and proactive security posture. This shift enables early detection, rapid response, and ultimately, significantly reduces the impact of sophisticated cyber threats, moving the advantage from the attacker back to the defender.

## Introduction
The omnipresent adoption of open-source libraries has fundamentally reshaped the landscape of software development. They offer exceptional advantages in terms of rapid development, cost efficiency, community support, and access to cutting-edge technologies. From operating systems and web frameworks to specialized algorithms and machine learning tools, open-source components are at the heart of countless modern applications. However, this widespread integration also introduces a critical, often underestimated, vulnerability: the security of these very libraries.

One of the primary reasons for this importance lies in the sheer volume and complexity of dependencies. A typical modern application might rely on dozens, even hundreds, of open-source libraries, each with its own set of sub-dependencies. This creates a vast and intricate supply chain. A vulnerability in just one seemingly innocuous, deeply nested library can ripple upwards, exposing the entire application to potential exploitation.

### The one we all know of from the past: Log4Shell, Log4j (CVE-2021-44228)
Perhaps the most prominent takeaway of this long-tail vulnerability was the pervasive and often hidden nature of dependencies in modern software. Many organizations were unaware they were even using Log4j, let alone a vulnerable version, highlighting the need for robust Software Bill of Materials (SBOMs) and dependency scanning tools.

## How AI Created Slopsquatting Risks
Historically, compromising a software supply chain was a high-effort undertaking. Today, the threat landscape has shifted dramatically with the emergence of **slopsquatting**. This automated attack vector exploits the tendency of AI coding assistants to “hallucinate” package names. Attackers preemptively register these nonexistent package names, allowing them to trick developers into unwittingly installing malicious code.

### What Slopsquatting is:
- **AI-Induced Hallucinations**: AI coding tools (e.g. ChatGPT, GitHub Copilot, CodeLlama) sometimes suggest non-existent libraries or packages that “sound” plausible.
- **Attacker Pre-Registration**: Malicious actors anticipate these hallucinations, register the fake package names on public repositories (PyPI, npm, etc.), and embed trojanized code.
- **Automated Exploitation**: A developer’s CI/CD pipeline or local build process can automatically fetch and install these packages, resulting in silent compromise.

## With Vibe Coding, It Got Worse
The increasing organizational demand for speed and agility has led to the widespread adoption of “vibe coding”—a practice characterized by rapid prototyping and code deployment with minimal peer review. This accelerated approach has shown that 40% of the time, the LLM-generated code suggestions exhibited vulnerabilities.

![Chart showing LLM non-compliance rates in helping with cyberattacks]

### Key Recommendations to Mitigate Impact
1. **Embed Security in Prompts**: Require LLMs to generate code with built-in protections.
2. **Automated Security Testing**: Integrate generated code into CI pipelines using OWASP ZAP, SAST tools, and fuzzers.
3. **Mandatory Human Review**: Enforce security expert sign-off on all LLM-produced modules.
4. **Secure-By-Default LLMs**: Encourage model vendors to bake in CSP headers, secure cookies, and CSRF tokens.

## Top 25 Software Supply Chain Attacks
Armis Labs has identified common attack vectors including supply chain attacks and dependency confusion.

| Ecosystem | Attack | Year(s) | Versions Affected | Attack Method | Mitigation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| JavaScript (npm) | event-stream | 2018 | v3.3.6 | Wallet exfiltration via dependency | Token revocation |
| JavaScript (npm) | eslint-scope | 2018 | v3.7.2, 5.0.2 | Pastebin exfiltration | Secure versions |
| JavaScript (npm) | UAParser.js | 2021 | v0.7.29, 0.8.0, 1.0.0 | Preinstall script loaded trojans | Patched releases |
| JavaScript (npm) | coa | 2021 | v2.0.3, 2.0.4, 2.1.1 | Credential stealer, miner | Reverted to safe version |
| JavaScript (npm) | rc | 2021 | v1.2.9, 1.3.9, 2.3.9 | Same as coa | Malicious versions removed |
| JavaScript (npm) | xrpl.js | 2025 | v4.2.1–4.2.4, 2.14.2 | Private key theft via backdoored publish | Update to 4.2.5, 2.14.3 |
| JavaScript (npm) | Solana web3.js | 2024 | v1.95.6, 1.95.7 | Wallet key exfiltration via backdoored function | Patched release |
| JavaScript (npm) | node-ipc | 2022 | v10.1.1, 10.1.2 | Geo-targeted file wiper (protestware) | Versions removed |
| JavaScript (npm) | colors.js/faker.js | 2022 | v1.4.1, 1.4.2, 6.6.6 | Infinite loop (protestware) | Forks replaced libraries |
| Python (PyPI) | SSH Decorator | 2018 | Multiple | SSH credential exfiltration | Yanked, new package |
| Python (PyPI) | python3-dateutil | 2019 | N/A | SSH/GPG key theft (typosquatting) | Removed from PyPI |
| Python (PyPI) | fastapi-toolkit | 2022 | N/A | RCE via malicious payloads | Removed |
| Python (PyPI) | requests-darwin-lite | 2024 | All versions | Backdoor in PNG | Yanked |
| Python (PyPI) | torchtriton | 2022 | N/A | DNS-based data exfiltration | Name seized, users warned |
| Ruby (RubyGems) | bootstrap-sass | 2019 | v3.2.0.3 | RCE via cookie eval | Yanked, replaced |
| Ruby (RubyGems) | strong_password | 2019 | v0.0.7 | Eval via cookie, exfiltration | Yanked, revert to 0.0.6 |
| Ruby (RubyGems) | rest-client | 2019 | v1.6.10–1.6.13 | Pastebin fetcher, credential theft | Removed |
| Ruby (RubyGems) | misc Ruby gems | 2019 | 10+ packages | Miner/credential theft | Yanked |
| Linux Tools | XZ Utils | 2024 | v5.6.0, 5.6.1 | SSH bypass via liblzma hook | Downgrade to 5.4.x |
| Linux Tools | Socat | 2016 | Multiple | Non-prime DH parameter | Switched to strong prime |
| Linux Tools | Webmin | 2018–2019 | v1.890–1.920 | RCE via altered update file | Clean rebuild |
| Linux Tools | Gentoo GitHub | 2018 | N/A | `rm -rf /` payload in ebuild scripts | 2FA enforced |
| Java (GitHub) | Octopus Scanner | 2020 | N/A | Injected JAR into NetBeans builds | GitHub SIRT cleaned repos |
| Rust | liblzma-sys | 2024 | v0.3.2 | Packaged XZ test files | Yanked, fixed in 0.3.3 |
| PHP | PEAR Installer | 2019 | go-pear.phar | Backdoored archive with RCE | Rebuilt from GitHub |

## The Importance of Early Warning Threat Intelligence
Traditional security solutions operate “right of boom.” Armis redefines the approach by taking action “left of boom,” or before the attack is launched.

### Recent Early Warning Examples:
- **Gravity Forms**: Malicious code injected into plugin versions 2.9.1.1 and 2.9.12. Armis identified the backdoor and rogue domain.
- **GitHub Actions (tj-actions/changed-files)**: Multi-stage attack compromising GitHub Actions via leaked PATs and malicious commits.
- **NPM Install (UA-Parser-JS)**: Detection of malicious code injection in widely used parser libraries.

## Indicators of Action (IoAs)
IoAs focus on the behaviors, methods, and intent of an adversary.

- **System Behavior**: Unexpected CPU spikes, erratic memory usage, files written to hidden directories.
- **Privilege & Credential Abuse**: Attempts to escalate privileges, reading sensitive files like `.env` or `~/.ssh/`.
- **Network Behavior**: Outbound connections to unknown domains, beaconing, DNS tunneling.
- **Build & Installation**: Unexpected pre- or post-installation scripts, obfuscated code, sudden increase in package size.
- **Metadata & Source Control**: Commits appearing from trusted bots but unsigned, rapid version churn, forked repositories.

## Mitigation Strategies
- **Verify AI-Suggested Dependencies**: Cross-check names against official registries.
- **Lock Files & Hash Verification**: Use pinned versions and integrity checks.
- **Dependency pinning and SBOMs**: Maintain a Software Bill of Materials.
- **Registry allow-listing**: Restrict installs to approved private proxies.
- **Least-Privilege Installation**: Run installs in isolated, ephemeral environments.

## Armis Vulnerability Intelligence Database
The Armis Vulnerability Intelligence Database is an AI-powered resource that provides real-time context, community-driven prioritization, and actionable insights. Unlike static databases like CISA KEV, it offers industry-specific context and identifies threats before they reach public disclosure.

## About Armis Centrix™
Armis Centrix™ is a cyber exposure management platform that sees, secures, and protects assets in real time. It combines asset intelligence with vulnerability intelligence to prioritize risks and reduce alert fatigue.

## About Armis Labs
Armis Labs is a research division dedicated to investigating emerging threats. Leveraging an Asset Intelligence Engine that tracks over six billion assets, the team uses deception technology, incident forensics, and AI/ML to proactively identify and mitigate threats before they manifest.

---
Armis, the cyber exposure management & security company.
1.888.452.4011