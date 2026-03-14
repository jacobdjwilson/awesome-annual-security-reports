# 2026 Global Threat Intelligence Report

Data, Insights, and Strategies for Navigating Today’s Hybrid Threat Landscape

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary: The Top Threats at a Glance](#executive-summary-the-top-threats-at-a-glance)
- [2026 Threat Landscapes: Artificial Intelligence (AI)](#2026-threat-landscapes-artificial-intelligence-ai)
  - [AI Threats Overview: Data and Insights](#ai-threats-overview-data-and-insights)
  - [The Rising Danger of Agentic AI](#the-rising-danger-of-agentic-ai)
  - [Defending Against AI Threats in 2026](#defending-against-ai-threats-in-2026)
  - [Key Takeaways](#key-takeaways-ai)
  - [Threat Posture Assessment](#threat-posture-assessment-ai)
- [2026 Threat Landscapes: Information-Stealing Malware](#2026-threat-landscapes-information-stealing-malware)
  - [Infostealer Overview: Data and Insights](#infostealer-overview-data-and-insights)
  - [The Hybrid Threat of AI-Driven Identity Exploitation](#the-hybrid-threat-of-ai-driven-identity-exploitation)
  - [Vidar Takes Center Stage Post-Lumma Takedown](#vidar-takes-center-stage-post-lumma-takedown)
  - [Defending Against Infostealers in 2026](#defending-against-infostealers-in-2026)
  - [Key Takeaways](#key-takeaways-infostealers)
  - [Threat Posture Assessment](#threat-posture-assessment-infostealers)
- [2026 Threat Landscapes: Vulnerabilities](#2026-threat-landscapes-vulnerabilities)
  - [Vulnerability Overview: Data and Insights](#vulnerability-overview-data-and-insights)
  - [Vulnerability Exploitation: Targeting High-Value Infrastructure](#vulnerability-exploitation-targeting-high-value-infrastructure)
  - [The Weaponization of AI Infrastructure](#the-weaponization-of-ai-infrastructure)
  - [Defending Against Vulnerabilities in 2026](#defending-against-vulnerabilities-in-2026)
  - [Key Takeaways](#key-takeaways-vulnerabilities)
  - [Threat Posture Assessment](#threat-posture-assessment-vulnerabilities)
- [2025 Threat Landscape: Ransomware](#2025-threat-landscape-ransomware)
  - [Ransomware Overview: Data and Insights](#ransomware-overview-data-and-insights)
  - [Shift in Ransomware Tactics: The Identity and Human Frontier](#shift-in-ransomware-tactics-the-identity-and-human-frontier)
  - [Shift in Ransomware Tactics: Increasing Reliance on Insider Threats](#shift-in-ransomware-tactics-increasing-reliance-on-insider-threats)
  - [Defending Against Ransomware in 2026](#defending-against-ransomware-in-2026)
  - [Key Takeaways](#key-takeaways-ransomware)
  - [Threat Posture Assessment](#threat-posture-assessment-ransomware)
- [The Flashpoint Advantage: Driving Mission-Critical Outcomes](#the-flashpoint-advantage-driving-mission-critical-outcomes)
- [Proactive Security in 2026 and Beyond](#proactive-security-in-2026-and-beyond)
- [About Flashpoint](#about-flashpoint)

---

## Introduction

In 2026, the cybersecurity landscape has reached a point of total convergence, where the silos that once separated malware, identity, and infrastructure have collapsed into a single, high-velocity threat engine. Simultaneously, the threat landscape is shifting from human-led attacks to machine-speed operations as a result of agentic AI, which acts as a force multiplier for the modern adversary. Meanwhile, this same technology has become a growing risk for defenders who, in a race to keep pace, have integrated AI into production workflows without fully grasping the new vulnerabilities it introduces.

Flashpoint’s 2026 Global Threat Intelligence Report (GTIR) was developed to anchor security leaders — from threat intelligence and vulnerability management teams to physical security professionals and the CISO’s office — with the data required to navigate this year’s greatest threats, rife with infostealers, vulnerabilities, ransomware, and malicious insiders.

This report is powered by Flashpoint’s Primary Source Collection (PSC), a specialized operating model that collects intelligence directly from original sources, driven by an organization’s unique Priority Intelligence Requirements (PIR) — not a vendor’s fixed feed. PSC preserves context and provenance to provide a ground-truth view of the trends, tactics, and adversary behaviors that will define 2026.

Read on and you will gain:

1. **A Clear Understanding of the New Convergence Between Identity and AI**: Discover how threat actors are preparing to transition from generative tools to sophisticated agentic frameworks. Learn how 3.3 billion compromised credentials are being weaponized via automated orchestration to bypass legacy defenses and exploit the connective tissue of modern corporate APIs.
2. **Intelligence on the “Franchise Model” of Global Extortion**: Gain deep insight into the professionalized operations of today’s most prolific threat actors. From the industrial efficiency of RaaS groups like RansomHub and Clop to the market dominance of the next generation of infostealer malware, we break down the economics driving today’s cybercrime ecosystem.
3. **A Blueprint for Proactive Defense and Risk Mitigation**: Leverage the latest trends, in-depth analysis, and data-driven insights driven by Primary Source Collection to bolster your security posture by identifying and proactively defending against rising attack vectors.

Protecting organizations, industries, and communities is a shared mission that requires us to work together as one team. With that in mind, I’m proud to provide our customers and the larger community with the insights they need to fortify defenses and proactively manage risk in the face of an ever-evolving threat landscape.

**Josh Lefkowitz**
Flashpoint Co-Founder and CEO

---

## Executive Summary: The Top Threats at a Glance

Flashpoint Identified Four Driving Themes Shaping the 2026 Threat Landscape:

### 2026 is the Era of Agentic-Based Cyberattacks
Flashpoint identified a 1,500% rise in AI-related illicit discussions between November and December 2025, signaling a rapid transition from criminal curiosity to the active development of malicious frameworks. Built on data pulled from criminal environments and shaped by fraud use cases, these systems scrape data, adjust messaging for specific targets, rotate infrastructure, and learn from failed attempts without the need for constant human involvement.

### Identity is the New Exploit
Flashpoint observed over 11.1 million machines infected with infostealers in 2025, fueling a massive inventory of 3.3 billion stolen credentials and cloud tokens. The fundamental mechanics of cybercrime have shifted from breaking in to logging in, as attackers leverage stolen session cookies to behave like legitimate users.

### The Patching Window is Rapidly Closing
Vulnerability disclosures surged by 12% in 2025, with 1 in 3 (33%) vulnerabilities having publicly available exploit code. The strategic gap between discovery and weaponization is increasingly vanishing, as evidenced by mass exploitation of zero-day vulnerabilities in as little as 24 hours after discovery.

### Ransomware is Hacking the Person, Not the Code
As technical defenses against encryption harden, ransomware groups are pivoting to the path of least resistance: human trust. This approach has led to a 53% increase in ransomware, with RaaS groups being responsible for over 87% of all ransomware attacks.

![Chart showing Flashpoint's AI collections derived from forums and chat services datasets]

---

## 2026 Threat Landscapes: Artificial Intelligence (AI)

### AI Threats Overview: Data and Insights
Artificial Intelligence (AI) is acting as a force multiplier, amplifying the scale and potency of nearly every component of the threat landscape. From information-stealing malware to vulnerabilities and ransomware, Flashpoint is observing threat actors improve their processes and expand their capabilities via generative AI and malicious LLMs.

**Artificial Intelligence Quickview (JANUARY 2025 - DECEMBER 2025)**
* **1.5 Billion**: Total AI Mentions
* ![Chart: Total Mentions of AI and Illicit Activity, 2025]
* ![Chart: Top Mentioned Malicious LLMs, 2025]

**Common Threat Actor Use Cases of Malicious AI:**
* **Jailbreaking**: A method to find a loophole around an AI’s safety nets and bypass regulations that could then be leveraged to make the AI system perform illicit activity.
* **Vishing**: Threat actors impersonate IT support or security teams to gain remote access, leveraging generative AI such as deepfake technology.
* **Slopsquatting**: Threat actors create fake software packages that mimic real ones, tricking AI coding assistants into recommending malware directly to developers.
* **AI Sidebar Spoofing**: Attackers create a fake AI assistant sidebar to trick users to navigate to malicious sites, run illicit commands, or install backdoors and potentially other harmful applications.
* **Prompt Injection**: Threat actors hide malicious instructions within HTML or social media comments — thereby tricking AI assistants into following hidden commands and allowing the attacker to steal login information or access sensitive data from the user.
* **Steganographic Prompting**: Threat actors hide secret instructions inside an AI model. When a user gives a normal command, the AI follows the hidden “sleeper” rules instead, performing a malicious task without the user ever knowing.

Infiltrating threat actor communities and discussion groups, Flashpoint identified over 1.5 billion illicit discussions and criminal activities centered around AI. Advancements in Flashpoint’s AI capabilities also revealed that this activity peaked in December 2025 at a staggering 1,500% when compared to the prior month.

### The Rising Danger of Agentic AI
AI threats are undergoing a major transition: threat actors are moving beyond one-off uses of generative AI — such as creating phishing lures and deepfakes — in favor of building systems that automate the entire attack chain continuously.

Built on data pulled from criminal environments and shaped by fraud use cases, these systems scrape data, adjust messaging for specific targets, rotate infrastructure, and learn from failed attempts without constant human involvement.

![Chart: Total Mentions of AI and Illicit Activity, 2025]
![Chart: Top Mentioned Malicious LLMs, 2025]

### Defending Against AI Threats in 2026
Incremental improvements to existing security models will not be enough. Attackers are adapting more quickly, leveraging automation, identity, and trusted relationships in ways that circumvent traditional controls. Intelligence programs built solely around static feeds and retrospective reporting will continue to lag behind.

### Key Takeaways {#key-takeaways-ai}
1. **Attackers are pivoting to autonomous “agentic” attack chains.**
2. **Adversaries are weaponizing organizational AI workflows and APIs against them.**
3. **2026 is ushering an explosive surge in specialized illicit AI discussion groups.**

### Threat Posture Assessment {#threat-posture-assessment-ai}
* Is my organization aware of the processes involved between our AI agents and production environments?
* Are my security teams able to detect and neutralize steganographic prompting within our current workflows?
* Does my organization have direct visibility into the peak discussion cycles of illicit AI marketplaces and forums?

---

## 2026 Threat Landscapes: Information-Stealing Malware

### Infostealer Overview: Data and Insights
Information-stealing malware, AKA infostealers, has changed the cybercrime economics of access. Between January 1 to December 31, 2025, Flashpoint observed over 11.1M machines infected with infostealers, culminating in over 3.3B stolen credentials, session cookies, cloud tokens, and personal data.

**Infostealer Quickview (JANUARY 2025 - DECEMBER 2025)**
* **11.1 Million**: Infected hosts and devices
* **3.3 Billion**: Stolen credentials

**Top 5 Most Prolific Infostealers in 2025:**
1. Lumma (UP YOY)
2. Acreed (NEW)
3. Rhadamanthys (NEW)
4. Vidar (UP YOY)
5. StealC (DOWN YOY)

**Top 6 Countries Affected:** 1. India, 2. Brazil, 3. Indonesia, 4. Vietnam, 5. Philippines, 6. United States.

### The Hybrid Threat of AI-Driven Identity Exploitation
The true danger of infostealers lies in two inherent characteristics of identity data: its reusability for multiple attacks and its ability to bypass traditional defenses entirely.

**The AI-Driven Identity Exploitation Cycle:**
1. **Harvesting**: Infostealers drain credentials and session cookies.
2. **Ingestion**: Stolen logs are fed into agentic AI systems.
3. **Automated Testing**: The AI autonomously tests these credentials against thousands of endpoints.
4. **Monetization/Escalation**: The system identifies successful logins for immediate fraud or lateral movement.

### Vidar Takes Center Stage Post-Lumma Takedown
The infostealer ecosystem has undergone incredible volatility. Following the takedown of Lumma in May 2025, Vidar and Rhadamanthys have taken over market share. As of January 2026, Vidar 2.0 is the most used infostealer.

![Chart: Most Prolific Infostealers by Infected Hosts and Devices, January - February 2026]

### Defending Against Infostealers in 2026
Organizations need to ensure that their intelligence providers can enrich and structure raw log files into actionable intelligence.

**How Flashpoint Transforms Raw Logs:**
1. **Source Ingestion**: Monitoring underground ecosystems.
2. **Normalization and De-Duplication**: Scoring for uniqueness and relevance.
3. **Automated Parsing and Enrichment**: Extracting credentials, session cookies, host metadata, and PII.
4. **Structured Output**: Mapping to known stealer strains and indexing within the Ignite platform.

### Key Takeaways {#key-takeaways-infostealers}
1. **Infostealers have expanded the attack surface to personal and SaaS ecosystems.**
2. **Identity is turning into the primary exploit vector.**
3. **Vidar 2.0 rapidly dominates the infostealer market following Lumma’s decline.**

### Threat Posture Assessment {#threat-posture-assessment-infostealers}
* Am I relying on generic feeds for infostealer intelligence, or do I have direct access to the raw data?
* Is my threat intelligence data allowing me to actively monitor for potential compromises affecting me and my partners?
* Is my Cyber Threat Intelligence team knowledgeable of the most prolific stealer strains?

---

## 2026 Threat Landscapes: Vulnerabilities

### Vulnerability Overview: Data and Insights
Flashpoint saw a year-over-year increase of over 12%, aggregating a total of 44,509 vulnerabilities in 2025. 

**Vulnerability Quickview (JANUARY 2025 - DECEMBER 2025)**
* **44,509**: Disclosed vulnerabilities
* **14,593**: Vulnerabilities with publicly available exploits

![Chart: Vulnerability Disclosures and Exploits, 2025]
![Chart: Breakdown of Actionable, High Severity Vulnerabilities, 2025]

### Vulnerability Exploitation: Targeting High-Value Infrastructure
The 2025 vulnerability intelligence landscape has been defined by a zero-day to exploit window that has effectively vanished. Ransomware groups have moved with alarming speed to weaponize flaws like Citrix Bleed 2 and React2Shell.

### The Weaponization of AI Infrastructure
Flashpoint is observing the weaponization of AI infrastructure, with the Langflow vulnerability being exploited to form the backbone of the Flodrix Botnet.

### Defending Against Vulnerabilities in 2026
Security teams should prioritize vulnerabilities that:
* Have a known solution
* Are remotely exploitable
* Have a publicly available exploit

Following this methodology can potentially allow organizations to cut their higher-risk vulnerability workloads by nearly 90%.

### Key Takeaways {#key-takeaways-vulnerabilities}
1. **Zero-day exploit windows are increasingly vanishing.**
2. **Attackers are pivoting to weaponize the AI development pipeline.**
3. **Potential CVE volatility mandates intelligence redundancy.**

### Threat Posture Assessment {#threat-posture-assessment-vulnerabilities}
* Does my security team have the capability of identifying zero-day vulnerabilities?
* Is my organization auditing the security of any agentic AI dependencies or third-party libraries?
* What is my organization’s response if publicly available vulnerability intelligence program funding and oversight remain volatile?

---

## 2025 Threat Landscape: Ransomware

### Ransomware Overview: Data and Insights
Flashpoint observed a year-over-year 53% increase in ransomware attacks. RaaS groups were responsible for over 87% of all ransomware attacks in 2025.

**Ransomware Quickview (JANUARY 2025 - DECEMBER 2025)**
* **8,835**: Total ransomware attacks
* ![Chart: Reported Ransomware Attacks, 2025]

### Shift in Ransomware Tactics: The Identity and Human Frontier
Ransomware extortion groups are strategically moving away from technical exploits to attack the most critical layer: human trust and identity.

### Shift in Ransomware Tactics: Increasing Reliance on Insider Threats
In 2025, Flashpoint observed 91,321 instances of insider recruiting, advertising, and threat actor discussions.

![Chart: Insider Threats by Industry, 2025]

### Defending Against Ransomware in 2026
Organizations need to establish a robust ransomware workflow that includes continuous monitoring for real-time mentions of compromised organizations, potential malicious insiders, and supply chains.

### Key Takeaways {#key-takeaways-ransomware}
1. **Ransomware is shifting into pure-play identity extortion.**
2. **Adversaries are weaponizing malicious insiders to bypass security stacks.**
3. **US critical infrastructure remains the epicenter of global ransomware attacks.**

### Threat Posture Assessment {#threat-posture-assessment-ransomware}
* Have we expanded our defense beyond “encryption protection” to include social engineering and “pure extortion” playbooks?
* How are we monitoring for signs of insider recruiting or unauthorized dashboard access?
* Is our Help Desk a hardened security gate or a potential access point?

---

## The Flashpoint Advantage: Driving Mission-Critical Outcomes

**Flashpoint Ignite**
Our award-winning platform empowers security teams by providing direct access to our unparalleled primary-source collections.

**Key Statistics:**
* **69B+**: Stolen Credentials
* **22.3B+**: Chat Services Messages
* **975M+**: Illicit Forum Posts
* **435K+**: Vulnerabilities (105K+ Pre-CVE)
* **1B+**: News Articles
* **2.6B+**: Unique Media
* **1.9B+**: Illicit Marketplace Items
* **9.3B+**: Stolen Credit Cards

**Core Packages:**
* **Cyber Threat Intelligence**: Protect against ransomware, malware, and account takeovers.
* **Vulnerability Management (VulnDB®)**: Timely awareness of new vulnerabilities.
* **Physical Security Intelligence (Echosec)**: Real-time, geo-enriched data.
* **National Security Intelligence**: Support for government agencies.

---

## Proactive Security in 2026 and Beyond

Organizations are facing an unprecedented barrage of sophisticated threats. To confront this reality, three key imperatives have emerged:

1. **Prioritize Context Over Volume**: Focus resources exclusively on exposures that demonstrate a high likelihood of weaponization.
2. **Harden the Human and Machine Identity Layer**: Treat every digital identity as a potential breach point.
3. **Build Resilience Against Systemic Intelligence Failures**: Leverage proprietary, dark and deep web research to maintain visibility even when public databases experience disruptions.

---

## About Flashpoint

Flashpoint is the leader and largest private provider of threat data and intelligence. We empower mission-critical businesses and governments worldwide to decisively confront complex security challenges, reduce risk, and improve operational resilience. Discover more at [flashpoint.io](https://flashpoint.io).

**Join the Conversation**
LinkedIn | X | Threat Intel Blog
[See Flashpoint Ignite in Action](https://flashpoint.io/demo/)

Copyright ©2026 Flashpoint. All Rights Reserved.