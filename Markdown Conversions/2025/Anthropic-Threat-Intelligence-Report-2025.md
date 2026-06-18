# Threat Intelligence Report: August 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Vibe Hacking: How Cybercriminals are Using AI Coding Agents to Scale Data Extortion Operations](#vibe-hacking-how-cybercriminals-are-using-ai-coding-agents-to-scale-data-extortion-operations)
- [Remote Worker Fraud: How North Korean IT Workers are Scaling Fraudulent Employment with AI](#remote-worker-fraud-how-north-korean-it-workers-are-scaling-fraudulent-employment-with-ai)
- [No-Code Malware: Selling AI-Generated Ransomware-as-a-Service](#no-code-malware-selling-ai-generated-ransomware-as-a-service)
- [Chinese Threat Actor Leveraging Claude Across Nearly All MITRE ATT&CK Tactics](#chinese-threat-actor-leveraging-claude-across-nearly-all-mitre-attck-tactics)
- [Auto-Disruption of a North Korean Malware Distribution Campaign](#auto-disruption-of-a-north-korean-malware-distribution-campaign)
- [No-Code Malware Development Campaign](#no-code-malware-development-campaign)
- [AI-Enhanced Fraud: AI’s Growing Footprint in the Fraud Ecosystem](#ai-enhanced-fraud-ais-growing-footprint-in-the-fraud-ecosystem)
- [Threat Actor Leverages MCP for Stealer Log Analysis and Victim Profiling](#threat-actor-leverages-mcp-for-stealer-log-analysis-and-victim-profiling)
- [Carding Store Powered by AI](#carding-store-powered-by-ai)
- [Romance Scam Bot Powered by AI Models](#romance-scam-bot-powered-by-ai-models)
- [Synthetic Identity Services Powered by AI](#synthetic-identity-services-powered-by-ai)

---

## Executive Summary

We have developed sophisticated safety and security measures to prevent the misuse of our AI models. While these measures are generally effective, cybercriminals and other malicious actors continually attempt to find ways around them. This report details several recent examples of how Claude has been misused, along with the steps we’ve taken to detect and counter their abuse.

This represents the work of Threat Intelligence: a dedicated team at Anthropic that finds deeply investigated sophisticated real-world cases of misuse and works with the rest of the Safeguards organization to improve our defenses against such cases.

While specific to Claude, the case studies presented below likely reflect consistent patterns of behaviour across all frontier AI models. Collectively, they show how threat actors are adapting their operations to exploit today’s most advanced AI capabilities:

- **Agentic AI systems are being weaponized**: AI models are themselves being used to perform sophisticated cyberattacks – not just advising on how to carry them out.
- **AI lowers the barriers to sophisticated cybercrime**: Actors with few technical skills have used AI to conduct complex operations, like developing ransomware, that would previously have required years of training.
- **Cybercriminals are embedding AI throughout their operations**: This includes victim profiling, automated service delivery, and in operations that affect tens of thousands of users.
- **AI is being used for all stages of fraud operations**: Fraudulent actors use AI for tasks like analyzing stolen data, stealing credit card information, and creating false identities.

We’re discussing these incidents publicly in order to contribute to the work of the broader AI safety and security community, and help those in industry, government, and the wider research community strengthen their own defences against the abuse of AI systems. We plan to continue releasing reports like this regularly, and to be transparent about the threats we find.

---

## Vibe Hacking: How Cybercriminals are Using AI Coding Agents to Scale Data Extortion Operations

### Summary
Today we are sharing insights about a sophisticated cybercriminal operation (tracked as GTG-2002) we recently disrupted that represents a new evolution in how cyber threat actors leverage AI—using coding agents to actively execute operations on victim networks, known as “vibe hacking”.

A cybercriminal used Claude Code to conduct a scaled data extortion operation across multiple international targets in a short timeframe. This threat actor leveraged Claude’s code execution environment to automate reconnaissance, credential harvesting, and network penetration at scale, potentially affecting at least 17 distinct organizations in just the last month across government, healthcare, emergency services, and religious institutions.

![About Claude Code: Anthropic’s agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster through natural language commands.]

### Key Findings
Our investigation revealed that the cybercriminal operated across multiple sectors, creating a systematic attack campaign that focused on comprehensive data theft and extortion. The operation leveraged opportunistic targeting based on results from using open source intelligence tools and scanning of Internet-facing devices. The actor demonstrated unprecedented integration of artificial intelligence throughout their attack lifecycle, with Claude Code supporting reconnaissance, exploitation, lateral movement, and data exfiltration.

The actor provided Claude Code with their preferred operational TTPs (Tactics, Techniques, and Procedures) in their `CLAUDE.md` file. However, this was simply a preferential guide and the operation still utilized Claude Code to make both tactical and strategic decisions—determining how best to penetrate networks, which data to exfiltrate, and how to craft psychologically targeted extortion demands.

![Actor bypassed safety measures and disabled confirmations]
![Mandated responses in non-English language]
![Sought financial gain through illicit means]

### Attack Lifecycle and AI Integration
- **Phase 1: Reconnaissance and target discovery**: The actor leveraged Claude Code for automated reconnaissance, scanning thousands of VPN endpoints and creating comprehensive scanning frameworks.
- **Phase 2: Initial access and credential exploitation**: Claude Code provided real-time assistance during live network penetration, identifying critical systems and extracting credential sets.
- **Phase 3: Malware development and evasion**: Claude Code was used for malware creation, including obfuscated versions of the Chisel tunneling tool and new TCP proxy code.
- **Phase 4: Data exfiltration and analysis**: Claude Code facilitated comprehensive data extraction and organized stolen data for monetization.
- **Phase 5: Extortion analysis and ransom note development**: The actor leveraged Claude Code to create customized ransom notes based on exfiltrated data analysis, demanding payments ranging from $75,000 to $500,000 in Bitcoin.

### Mitigation
We banned the accounts associated with this operation. In response to this case, we began developing a tailored classifier specifically for this type of activity and another new detection method to ensure similar behavior is captured by our standard safety enforcement pipeline.

---

## Remote Worker Fraud: How North Korean IT Workers are Scaling Fraudulent Employment with AI

### Summary
We are sharing insights on a sophisticated fraudulent employment operation that demonstrates how AI is fundamentally transforming the scale and effectiveness of North Korean remote worker schemes designed to evade international sanctions and generate profit for the regime.

Our investigation revealed that North Korean operatives have been systematically leveraging Claude to secure and maintain fraudulent remote employment positions at technology companies.

### Key Findings
The most striking finding is the actors’ complete dependency on AI to function in technical roles. These operators do not appear to be able to write code, debug problems, or even communicate professionally without Claude’s assistance. Yet they’re successfully maintaining employment at Fortune 500 companies, passing technical interviews, and delivering work that satisfies their employers.

### Operational Lifecycle
1. **Persona development**: Generating professional backgrounds, technical portfolios, and career narratives.
2. **Application and interview process**: Tailoring resumes, crafting cover letters, and real-time assistance during coding assessments.
3. **Employment maintenance**: Delivering technical work, participating in team communications, and maintaining the illusion of competence.
4. **Revenue generation**: Funding weapons programs through salaries earned from multiple concurrent positions.

### Mitigation
We banned the accounts associated with this violative activity. Following this case, we improved our tooling for collecting, storing, and correlating known indicators of compromise.

---

## No-Code Malware: Selling AI-Generated Ransomware-as-a-Service

### Summary
We are sharing insights on a ransomware development commercial operation that demonstrates how AI is transforming the creation and distribution of malware through Ransomware-as-a-Service (RaaS) models. A UK-based threat actor (tracked as GTG-5004) has leveraged Claude to develop, market, and distribute ransomware with advanced evasion capabilities.

### Malware Analysis
Technical analysis reveals capable ransomware developed through extensive AI assistance:
- **Core encryption**: ChaCha20 stream cipher targeting file headers.
- **Anti-analysis**: FreshyCalls and RecycledGate techniques for direct syscall invocation.
- **Persistence**: Reflective DLL injection and code cave infection.

### Implications
Traditional ransomware development required technical expertise in cryptography and Windows internals. AI has effectively removed this barrier, allowing actors who cannot independently implement basic encryption to create and sell sophisticated malware.

---

## Chinese Threat Actor Leveraging Claude Across Nearly All MITRE ATT&CK Tactics

We identified and investigated a sophisticated Chinese threat actor who systematically leveraged Claude to enhance cyber operations targeting Vietnamese critical infrastructure. The actor integrated Claude across nearly all phases of the attack lifecycle over a 9-month campaign, using it as a technical advisor, code developer, security analyst, and operational consultant.

---

## Auto-Disruption of a North Korean Malware Distribution Campaign

We successfully prevented a sophisticated North Korean threat actor from establishing operations on our platform through automated safety measures. The actor attempted to create accounts for the “Contagious Interview” campaign but was immediately detected and banned prior to the accounts issuing any prompts.

---

## No-Code Malware Development Campaign

We discovered a Russian-speaking developer using Claude to create malware with advanced evasion capabilities. The actor demonstrated strong Windows internals knowledge but relied heavily on Claude for implementation. This actor was discovered using Clio, our automated privacy-preserving analysis tool.

---

## AI-Enhanced Fraud: AI’s Growing Footprint in the Fraud Ecosystem

We are sharing insights on how threat actors are leveraging AI across multiple stages of criminal operations—creating an end-to-end fraud supply chain that spans from initial data analysis to monetization.

### Threat Actor Leverages MCP for Stealer Log Analysis and Victim Profiling
The actor used Claude with Model Context Protocol (MCP) to process stealer log files, implement domain categorization, and build comprehensive behavioral profiles based on online activities.

### Carding Store Powered by AI
We identified a Spanish-speaking actor using Claude Code to maintain and enhance an invite-only web service specializing in validating and reselling stolen credit cards at scale.

### Romance Scam Bot Powered by AI Models
We identified a Telegram bot (@Chat_ChatGPT_AIbot) that provides multimodal AI tools specifically marketed to support romance scam operations, with Claude advertised as a “high EQ model” for emotionally intelligent responses.

### Synthetic Identity Services Powered by AI
We discovered an actor who successfully launched an operational synthetic identity service using Claude for various components of their infrastructure.

---

## Implications
These cases collectively demonstrate a concerning evolution in how AI empowers criminal operations:
1. **Analysis & targeting**: AI transforms stolen data into actionable intelligence.
2. **Infrastructure development**: AI enables rapid creation of sophisticated criminal platforms.
3. **Operational resilience**: AI facilitates quick pivots and adaptations.
4. **Technical sophistication**: AI lowers barriers to implementing advanced evasion techniques.

**AUTHORS**
Alex Moix, Ken Lebedev, Jacob Klein