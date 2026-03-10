# Threat Intelligence Report: August 2025

## Table of Contents
- [Executive summary](#executive-summary)
- [Case studies](#case-studies)
- [Vibe hacking: how cybercriminals are using AI coding agents to scale data extortion operations](#vibe-hacking-how-cybercriminals-are-using-ai-coding-agents-to-scale-data-extortion-operations)
- [Remote worker fraud: how North Korean IT workers are scaling fraudulent employment with AI](#remote-worker-fraud-how-north-korean-it-workers-are-scaling-fraudulent-employment-with-ai)
- [No-code malware: selling AI-generated ransomware-as-a-service](#no-code-malware-selling-ai-generated-ransomware-as-a-service)
- [Chinese threat actor leveraging Claude across nearly all MITRE ATT&CK tactics](#chinese-threat-actor-leveraging-claude-across-nearly-all-mitre-attck-tactics)
- [Auto-disruption of a North Korean malware distribution campaign](#auto-disruption-of-a-north-korean-malware-distribution-campaign)
- [No-code malware development campaign](#no-code-malware-development-campaign)
- [AI-enhanced fraud: AI’s growing footprint in the fraud ecosystem](#ai-enhanced-fraud-ais-growing-footprint-in-the-fraud-ecosystem)
- [Threat actor leverages MCP for stealer log analysis and victim profiling](#threat-actor-leverages-mcp-for-stealer-log-analysis-and-victim-profiling)
- [Carding store powered by AI](#carding-store-powered-by-ai)
- [Romance scam bot powered by AI models](#romance-scam-bot-powered-by-ai-models)
- [Synthetic identity services powered by AI](#synthetic-identity-services-powered-by-ai)

---

## Executive summary

We have developed sophisticated safety and security measures to prevent the misuse of our AI models. While these measures are generally effective, cybercriminals and other malicious actors continually attempt to find ways around them. This report details several recent examples of how Claude has been misused, along with the steps we’ve taken to detect and counter their abuse.

This represents the work of Threat Intelligence: a dedicated team at Anthropic finds deeply investigated sophisticated real world cases of misuse and works with the rest of the Safeguards organization to improve our defenses against such cases.

While specific to Claude, the case studies presented below likely reflect consistent patterns of behaviour across all frontier AI models. Collectively, they show how threat actors are adapting their operations to exploit today’s most advanced AI capabilities:

- **Agentic AI systems are being weaponized**: AI models are themselves being used to perform sophisticated cyberattacks – not just advising on how to carry them out.
- **AI lowers the barriers to sophisticated cybercrime**. Actors with few technical skills have used AI to conduct complex operations, like developing ransomware, that would previously have required years of training.
- **Cybercriminals are embedding AI throughout their operations**. This includes victim profiling, automated service delivery, and in operations that affect tens of thousands of users.
- **AI is being used for all stages of fraud operations**. Fraudulent actors use AI for tasks like analyzing stolen data, stealing credit card information, and creating false identities.

We’re discussing these incidents publicly in order to contribute to the work of the broader AI safety and security community, and help those in industry, government, and the wider research community strengthen their own defences against the abuse of AI systems. We plan to continue releasing reports like this regularly, and to be transparent about the threats we find.

---

## Case studies

### Vibe hacking: how cybercriminals are using AI coding agents to scale data extortion operations

**Summary**
Today we are sharing insights about a sophisticated cybercriminal operation (tracked as GTG-2002) we recently disrupted that represents a new evolution in how cyber threat actors leverage AI—using coding agents to actively execute operations on victim networks, known as “vibe hacking”.

A cybercriminal used Claude Code to conduct a scaled data extortion operation across multiple international targets in a short timeframe. This threat actor leveraged Claude’s code execution environment to automate reconnaissance, credential harvesting, and network penetration at scale, potentially affecting at least 17 distinct organizations in just the last month across government, healthcare, emergency services, and religious institutions.

The operation demonstrates a concerning evolution in AI-assisted cybercrime, where AI serves as both a technical consultant and active operator, enabling attacks that would be more difficult and time-consuming for individual actors to execute manually. This approach, which security researchers have termed “vibe hacking,” represents a fundamental shift in how cybercriminals can scale their operations.

**Key findings**
Our investigation revealed that the cybercriminal operated across multiple sectors, creating a systematic attack campaign that focused on comprehensive data theft and extortion. The operation leveraged opportunistic targeting based on results from using open source intelligence tools and scanning of Internet-facing devices. The actor demonstrated unprecedented integration of artificial intelligence throughout their attack lifecycle, with Claude Code supporting reconnaissance, exploitation, lateral movement, and data exfiltration.

![Image: Simulated CLAUDE.md configuration file showing operational instructions for network security testing]

**Attack lifecycle and AI integration**
- **Phase 1: Reconnaissance and target discovery**: The actor leveraged Claude Code for automated reconnaissance.
- **Phase 2: Initial access and credential exploitation**: Claude Code provided real-time assistance during live network penetration operations.
- **Phase 3: Malware development and evasion**: Claude Code was used for malware creation and the addition of anti-detection capabilities.
- **Phase 4: Data exfiltration and analysis**: Claude Code facilitated comprehensive data extraction and analysis across multiple victim organizations.
- **Phase 5: Extortion analysis and ransom note development**: The actor leveraged Claude Code to create customized ransom notes based on exfiltrated data analysis.

**Implications**
This case represents an evolution toward AI-powered cybercrime operations where:
1. Technical infrastructure is augmented by AI capabilities that can perform complex operations autonomously.
2. A single operator can achieve the impact of an entire cybercriminal team through AI assistance.
3. AI makes both strategic and tactical decisions about targeting, exploitation, and monetization.
4. Defense becomes increasingly difficult as AI-generated attacks adapt to defensive measures in real-time.

**Mitigation**
We banned the accounts associated with this operation. In response to this case, we began developing a tailored classifier specifically for this type of activity and another new detection method to ensure similar behavior is captured by our standard safety enforcement pipeline.

---

### Remote worker fraud: how North Korean IT workers are scaling fraudulent employment with AI

**Summary**
We are sharing insights on a sophisticated fraudulent employment operation that demonstrates how AI is fundamentally transforming the scale and effectiveness of North Korean remote worker schemes designed to evade international sanctions and generate profit for the regime.

Our investigation revealed that North Korean operatives have been systematically leveraging Claude to secure and maintain fraudulent remote employment positions at technology companies. This represents a significant evolution in tactics, as operators who previously required extensive technical training can now simulate professional competence through AI assistance.

**Key findings**
The most striking finding is the actors’ complete dependency on AI to function in technical roles. These operators do not appear to be able to write code, debug problems, or even communicate professionally without Claude’s assistance. Yet they’re successfully maintaining employment at Fortune 500 companies (according to public reporting) passing technical interviews, and delivering work that satisfies their employers.

**Operational lifecycle**
- **Phase 1: Persona development**: Operators create elaborate false identities.
- **Phase 2: Application and interview process**: Operators leverage AI for tailoring resumes and preparing for interviews.
- **Phase 3: Employment maintenance**: Operators use AI to deliver technical work and maintain the illusion of competence.
- **Phase 4: Revenue generation**: Operations generate hundreds of millions annually for North Korea’s weapons programs.

**Mitigation**
We banned the accounts associated with this violative activity. Following this case, we improved our tooling for collecting, storing, and correlating known indicators of compromise.

---

### No-code malware: selling AI-generated ransomware-as-a-service

**Summary**
We are sharing insights on a ransomware development commercial operation that demonstrates how AI is transforming the creation and distribution of malware through Ransomware-as-a-Service (RaaS) models.

Our investigation revealed that a UK-based threat actor (tracked as GTG-5004) has leveraged Claude to develop, market, and distribute ransomware with advanced evasion capabilities. Active since at least January 2025 on dark web forums, this actor represents a concerning evolution in cybercrime—operators with limited technical expertise can now create and sell novel malware through AI assistance.

**Malware analysis**
Technical analysis reveals capable ransomware developed through extensive AI assistance, including:
- **Core encryption capabilities**: ChaCha20 stream cipher implementation.
- **Anti-analysis & evasion techniques**: FreshyCalls and RecycledGate for direct syscall invocation.
- **Anti-recovery & impact maximization**: Shadow copy deletion and targeted file system enumeration.

**Mitigation**
We banned the account associated with this RaaS operation. In response, we implemented new methods for detecting malware upload, modification, and generation on our platform.

---

### Chinese threat actor leveraging Claude across nearly all MITRE ATT&CK tactics

We identified and investigated a sophisticated Chinese threat actor who systematically leveraged Claude to enhance cyber operations targeting Vietnamese critical infrastructure. The actor integrated Claude across nearly all phases of the attack lifecycle over a 9-month campaign. The actor used Claude as a technical advisor, code developer, security analyst, and operational consultant throughout their campaign.

---

### Auto-disruption of a North Korean malware distribution campaign

We successfully prevented a sophisticated North Korean threat actor from establishing operations on our platform through automated safety measures. The actor attempted to create accounts for the “Contagious Interview” campaign but was immediately detected and banned prior to the accounts issuing any prompts.

---

### No-code malware development campaign

We discovered a Russian-speaking developer using Claude to create malware with advanced evasion capabilities. The actor demonstrated strong Windows internals knowledge but relied heavily on Claude for implementation. Malware samples appeared on VirusTotal within 2 hours of Claude generating the code.

---

## AI-enhanced fraud: AI’s growing footprint in the fraud ecosystem

We are sharing insights on how threat actors are leveraging AI across multiple stages of criminal operations—creating an end-to-end fraud supply chain that spans from initial data analysis to monetization.

### Threat actor leverages MCP for stealer log analysis and victim profiling
We identified a threat actor using Model Context Protocol (MCP) and Claude to analyze stealer logs and build detailed victim profiles. The actor showcased their implementation on a Russian-speaking hacking forum, creating behavioral profiles from victims’ computer usage patterns.

### Carding store powered by AI
We identified a Spanish-speaking actor using Claude Code to maintain and enhance an invite-only web service specializing in validating and reselling stolen credit cards at scale.

### Romance scam bot powered by AI models
We identified a Telegram bot (@Chat_ChatGPT_AIbot) that provides multimodal AI tools specifically marketed to support romance scam operations. The bot offers access to multiple AI models, with Claude advertised as a “high EQ model” for emotionally intelligent responses.

### Synthetic identity services powered by AI
We discovered an actor who successfully launched an operational synthetic identity service using Claude for various components of their infrastructure.

**Authors**
Alex Moix, Ken Lebedev, Jacob Klein