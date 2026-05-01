# State of API and API Security: Navigating the Agentic Era

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Drivers for API Adoption](#drivers-for-api-adoption)
- [API Development Trends](#api-development-trends)
- [API Security Challenges in the Agentic Era](#api-security-challenges-in-the-agentic-era)
- [Salt Labs Analysis of Customer Data](#salt-labs-analysis-of-customer-data)
- [Monitoring and Securing APIs](#monitoring-and-securing-apis)
- [Generative AI and API Security Risks](#generative-ai-and-api-security-risks)
- [Measuring ROI in API Security](#measuring-roi-in-api-security)
- [Conclusion and Recommendations](#conclusion-and-recommendations)
- [About Salt](#about-salt)

---

## Executive Summary

### The Emerging Agentic Security Gap
Security leaders increasingly recognize that AI systems introduce entirely new operational risks. Our survey shows that boards and executive leadership are now actively scrutinizing AI security:

- 79% report increased executive scrutiny of AI security risks.
- 69% of boards are concerned about sensitive data leakage through AI prompts or models.
- 39% are specifically worried about autonomous agents acting without human oversight.

Despite this boardroom mandate, organizations admit to a severe "Confidence Gap" when relying on traditional security stacks to address AI-driven threats. The visibility gap is compounded by a profound failure in legacy tooling:

- About 18% are very confident they can detect attacks using Generative AI.
- Crucially, only 24% of respondents find their existing security tools "Very effective" at preventing attacks.

These findings confirm that the entire legacy security stack is failing. Traditional Application Security Testing (SAST and DAST) lacks the context to validate AI-generated code, while legacy Web Application Firewalls (WAFs) and API Gateways are completely blind to new agent-based infrastructure such as MCP servers. AI security has become inseparable from API security. To safely scale, organizations must build an Agentic Security Graph to visualize undocumented machine-to-machine connections, and enforce context-aware security from the developer environment straight through to runtime. Organizations must secure the "Sequence of Intent" rather than rely solely on the static signatures and rate limits of outdated WAFs and Gateways, as APIs evolve into the control plane for autonomous systems.

### The Shift to the Agentic Era
The era of human-centric API consumption is ending. As enterprises rapidly deploy generative AI models and autonomous agents, APIs have evolved from simple integration points into the operational backbone of the AI economy. Every autonomous action, from reasoning to retrieving sensitive data to executing workflows, ultimately occurs through an API call.

This shift means a fundamental truth now defines modern security architecture: **You cannot secure AI without securing APIs.**

Our 1H 2026 survey of over 300 security leaders reveals that organizations are accelerating API adoption to support AI innovation, but security maturity is struggling to keep pace. The most alarming findings highlight a growing tension between agentic innovation and enterprise visibility:

- 60% of organizations admit to a profound lack of control over the security of the AI models that generate their application code.
- 49% are essentially blind to non-human, machine-to-machine traffic, unable to monitor what their autonomous agents are doing.
- 48% cannot effectively differentiate legitimate AI agents from malicious bots.
- As a result of this opacity, 47% have delayed production releases due to concerns about securing the APIs exposed to these autonomous systems.

Nearly half (47%) of respondents reported API growth of 51 to 100% in the past year. At the same time, 69% of organizations already use GenAI to develop APIs, and 19% plan to adopt it in the next 12 months. This transformation introduces a new category of security risk: the **Agentic Action Layer**, the APIs that allow AI agents to interact with enterprise systems.

### The Path Forward
Organizations that successfully navigate this shift are treating API security as the foundation for AI governance. Leading teams are prioritizing:

- **Mapping the Agentic Security Graph**: Move beyond static API lists to visualize the continuous, multi-pronged relationships across the entire agentic stack.
- **Identity-Aware Intent Analysis**: Monitor runtime machine-to-machine traffic by focusing on the agentic "Sequence of Intent" rather than relying on legacy static signatures.
- **Context-Driven Assurance in the SDLC**: Establish guardrails for AI-generated code directly within the developer environment (IDE) and create a continuous runtime-to-code feedback loop.
- **Posture governance aligned to modern frameworks**: Mapping risks directly to the OWASP API Top 10 and NIST AI RMF.

---

## Key Findings

### APIs Are the Operational Backbone of the Agentic AI Economy
APIs remain the core infrastructure enabling digital transformation and automation. The top drivers for API adoption include:
- 57% – Development efficiency and standardization
- 56% – Digital transformation initiatives
- 50% – Platform and system integrations
- 43% – Cloud migration

AI is now emerging as a major new driver:
- 32% use APIs to enable AI/ML analytics and automation
- 14% rely on APIs to support AI agents and autonomous systems

### API Growth Is Accelerating Rapidly
Organizations reported dramatic increases in API volume:
- 47% experienced API growth of 51–100% in the past year
- 12% saw growth of 101–200%
- 30% reported growth up to 50%

![Chart showing drivers for API adoption: Digital transformation (56%), Development efficiencies (57%), Cloud migration (43%), Partner enablement (18%), Platform/system integrations (50%), Monetization (29%), AI/ML capabilities (32%), AI agents (14%)]

### API Visibility Remains a Critical Gap
Accurate inventory and monitoring remain major challenges:
- 57% are only somewhat confident their API inventory is accurate
- 23% have fully automated, real-time inventory
- 19% have low or no confidence in their inventory

### API Security Incidents Are Common
- 32% of organizations experienced an API security incident in the past year
- 47% delayed application deployment due to API security concerns

Common security issues discovered in production APIs include:
- Sensitive data exposure (44%)
- Vulnerabilities (43%)
- Authentication problems (41%)
- Credential stuffing or brute force attacks (27%)

### Generative AI Is Transforming Development (and Risk)
- 18% use GenAI for all API development
- 51% use it for some development
- 19% plan to adopt it within 12 months

Top concerns include:
- 60% — Lack of control over the security of AI models used in development
- 59% — Difficulty securing AI-generated code
- 57% — Potential for new vulnerabilities introduced by GenAI

### AI Agents Introduce a New Security Challenge
Key challenges include:
- 50% – Maintaining reliability for mission-critical automation
- 49% – Monitoring machine-to-machine traffic
- 48% – Distinguishing legitimate agents from malicious bots
- 47% – Securing APIs exposed to autonomous systems

---

## Drivers for API Adoption
Building the Infrastructure for the AI-Driven Enterprise. APIs are no longer just integration tools; they are becoming the execution layer for AI systems.

---

## API Development Trends
The reliance on APIs continues to grow. As APIs multiply across hybrid environments, development velocity is rapidly outpacing security maturity.

![Chart showing API growth over the past 12 months: 0-50% (30%), 51-100% (47%), 101-200% (12%), 201-300% (5%), 301%+ (1%)]

---

## API Security Challenges in the Agentic Era
As organizations enable AI agents, common API security flaws become systemic risks.

- **Vulnerabilities (43%)**: Can be weaponized to hijack an AI's logic via indirect prompt injection.
- **Sensitive data exposure (44%)**: Magnified when APIs grant access to AI models.
- **Authentication problems (41%)**: A flaw in machine identity can grant an autonomous AI agent dangerous levels of access.
- **Account misuse or fraud (20%)**: Enables fraudulent transactions at machine speed.
- **Denial-of-service (14%)**: High-value targets for critical AI workflows.
- **Brute forcing or credential stuffing (27%)**: Targeting machine identities.
- **Enumeration and scraping (10%)**: Malicious AI mapping the attack surface.

### The Machine-Speed Code Generation Challenge
60% of security leaders cite a lack of control over the security of AI models used in development, and 59% struggle to secure AI-generated code. Traditional SAST and DAST tools lack the business-logic awareness to validate complex API architectures.

---

## Salt Labs Analysis of Customer Data
The primary threat is no longer an unauthenticated outsider, but an authenticated entity—a compromised Machine Identity, such as a rogue AI agent or an over-permissioned LLM.

- 99% of attack attempts originate from authenticated sources.
- 99% target external-facing APIs.

### The Dominant Threat
- **API8 (Security Misconfiguration)**: 65% of attacks.
- **API1 (Broken Object Level Authorization)**: 7% of attacks.

![Chart showing OWASP API Security Top 10 distribution: API1 (7%), API2 (1%), API3 (13%), API4 (9%), API5 (3%), API6 (3%), API7 (6%), API8 (65%)]

---

## Monitoring and Securing APIs
Visibility gaps create operational risk. Solving this requires moving beyond flat, legacy API inventories to build a dynamic **Agentic Security Graph**.

### Monitoring Practices
- 26% monitor APIs continuously in real time.
- 64% rely on alerts from API gateways.
- 54% rely on alerts from WAFs.

### Security Program Maturity
- 7% have no API security strategy.
- 33% are in the planning stage.
- 24% have basic programs.
- 28% have intermediate maturity.
- 8% report advanced API security programs.

---

## Generative AI and API Security Risks
Nearly 90% of organizations are already using or planning to use AI-assisted development tools. Security leaders are concerned about the lack of control over AI models and the difficulty of securing AI-generated code.

---

## Measuring ROI in API Security
Organizations are shifting from viewing API security as a cost center for breach prevention to an **AI Enabler**. Metrics now include speed to safe deployment of LLM-integrated tools and reduction in "Mean Time to Remediate" (MTTR) for AI-generated code vulnerabilities.

---

## Conclusion and Recommendations
1. **Provide the Full Agentic Security Graph**: Map relationships between LLMs, MCP servers, and underlying APIs.
2. **Implement Real-Time Monitoring and Behavioral Detection**: Critical for protecting machine-to-machine interactions.
3. **Adopt Context-Aware Security for AI-Driven Development**: Enforce standards directly within the IDE and CI/CD pipelines.
4. **Secure the Agentic Action Layer**: Protect autonomous systems interacting with enterprise infrastructure.
5. **Align Security Investments with Business Outcomes**: Focus on resilience, compliance, and innovation speed.

---

## About Salt
The Salt Security API Protection Platform secures APIs across the full lifecycle. It discovers all APIs, stops attackers by identifying them during reconnaissance, and improves security posture by identifying vulnerabilities before they reach production.

### About Salt Labs
Salt Labs identifies API threats and vulnerabilities in customer deployments and in the wild, applying research findings to improve the ML and AI algorithms at the heart of the Salt platform.