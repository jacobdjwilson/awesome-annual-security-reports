# Microsoft Digital Defense Report 2024
## The foundations and new frontiers of cybersecurity
### A Microsoft Threat Intelligence report

## Table of Contents
- [Overview](#overview)
  - [About this report](#about-this-report)
  - [Introduction by Tom Burt](#introduction-by-tom-burt)
  - [Our unique vantage point](#our-unique-vantage-point)
  - [Cybersecurity at Microsoft: the CISO’s perspective](#cybersecurity-at-microsoft-the-cisos-perspective)
- [1. The evolving cyber threat landscape](#1-the-evolving-cyber-threat-landscape)
  - [Key developments](#key-developments-1)
  - [Introduction](#introduction-1)
  - [Threat actors and motivations](#threat-actors-and-motivations)
  - [Nation-state threats](#nation-state-threats)
  - [Election interference](#election-interference)
  - [Ransomware](#ransomware)
  - [Fraud](#fraud)
  - [Identity and social engineering](#identity-and-social-engineering)
  - [DDoS attacks](#ddos-attacks)
- [2. Centering our organizations on security](#2-centering-our-organizations-on-security)
  - [Key developments](#key-developments-2)
  - [Introduction](#introduction-2)
  - [Secure Future Initiative](#secure-future-initiative)
  - [Strategic approaches to cybersecurity](#strategic-approaches-to-cybersecurity)
  - [Supporting the ecosystem](#supporting-the-ecosystem)
  - [Critical environments](#critical-environments)
  - [Collective action](#collective-action)
- [3. Early insights: AI’s impact on cybersecurity](#3-early-insights-ais-impact-on-cybersecurity)
  - [Key developments](#key-developments-3)
  - [Introduction](#introduction-3)
  - [Understanding how generative AI systems work](#understanding-how-generative-ai-systems-work)
  - [Emerging threat landscape](#emerging-threat-landscape)
  - [AI for defense](#ai-for-defense)
  - [Advancing global AI security](#advancing-global-ai-security)
- [Appendix](#appendix)
  - [References](#references)
  - [Contributing teams](#contributing-teams)

---

# Overview

## About this report

### Report scope
The data, insights, and events in this report represent July 2023 through June 2024 (Microsoft fiscal year 2024), unless otherwise noted. Please note that due to rounding, the percentages in some charts may not total 100%.

### Threat actor terminology used in this report
- **Nation-state threat attacks/operations**: Malicious cyberattacks that originate from a particular country and are an attempt to further that country’s interests.
- **Cybercriminal activity**: Cybercriminals are typically motivated by financial gain. They may use similar tools and tactics as nation-state threat actors, but their primary goal is profit.
- **Cyber operations**: An overarching term referring to all computer network operations, from defense to attack and exploitation.
- **Influence operations (IO)**: The coordinated application of national capabilities to foster attitudes, behaviors, or decisions by foreign target audiences.
- **Cyber-enabled influence operations**: Operations which combine offensive computer network operations with messaging and amplification.

### Our commitment to preserving privacy
Any and all data included in this report is presented in alignment to our privacy principles. Microsoft is committed to its focus on preserving customers’ control over their data.

### Our commitment to developing technology responsibly
As we design, build, and release AI products, six values—transparency, accountability, fairness, inclusiveness, reliability and safety, and privacy and security—remain our foundation.

### Links
- [Microsoft Privacy Statement](https://privacy.microsoft.com)
- [Microsoft EU Data Boundary Overview](https://trustcenter.microsoft.com)
- [Empowering responsible AI practices](https://ai.microsoft.com)
- [Responsible AI Transparency Report | May 2024](https://aka.ms/RAI-Report)

---

## Introduction

### Complex, challenging, and increasingly dangerous
**The new cyber threat landscape: an introduction by Tom Burt**

> “We all can, and must, do better, hardening our digital domains to protect our networks, data, and people at all levels.”

In the last year, the cyber threat landscape continued to become more dangerous and complex. The malign actors of the world are becoming better resourced and better prepared, with increasingly sophisticated tactics, techniques, and tools that challenge even the world’s best cybersecurity defenders.

Because these actors conduct both targeted and opportunistic attacks, the threat they present is universal. Even Microsoft has been the victim of well-orchestrated attacks by determined and well-resourced adversaries, and our customers face more than 600 million cybercriminal and nation-state attacks every day.

In the US alone this fiscal year, 389 healthcare institutions were successfully hit by ransomware. Nation-states are becoming more aggressive, with state-sponsored hackers not just stealing data, but launching ransomware, prepositioning backdoors, and conducting influence campaigns.

Improved defense will not be enough. The sheer volume of attacks must be reduced through effective deterrence. While the immediate outlook is pessimistic, there are changes on the near horizon that provide cause for optimism. In this year’s report, we dive deeper into the subject of AI in cybersecurity. Advances in AI-powered cybersecurity should give defenders an asymmetric advantage in the near future.

**Tom Burt**  
Corporate Vice President, Customer Security and Trust

---

## Our unique vantage point

The depth and breadth of Microsoft’s presence in the digital ecosystem offers a unique perspective. We process more than **78 trillion security signals per day**, from billions of Windows endpoints, the cloud, and a broad spectrum of products and services.

### Microsoft’s unique vantage point by the numbers:
- **78 trillion** security signals per day inform our insights (up from 65 trillion in 2023).
- **34,000** full-time dedicated security engineers.
- **15,000** partners with specialized security expertise.
- **1,500** unique threat groups tracked (including 600+ nation-state, 300+ cybercrime, and 200+ influence operations groups).

### Current and emerging threats:
- Technical debt
- Nation-state actors
- AI as a threat
- Supply chain and ecosystem
- Cybercriminals
- Conflicting regulatory requirements

---

## Cybersecurity at Microsoft: the CISO’s perspective

In January 2024, I took on the role of Microsoft Chief Information Security Officer (CISO). Immediately thereafter, we discovered we were under a massive cyberattack by the threat actor we refer to as **Midnight Blizzard**.

The cornerstone of our work to protect Microsoft is the **Secure Future Initiative (SFI)**, which dedicates the entire company to putting security above all other considerations. We made phishing-resistant multifactor authentication (MFA) mandatory across the company and reassigned roughly 34,000 full-time equivalent engineers to security initiatives.

I instituted an Office of the CISO and hired a number of Deputy CISOs who work with our major product groups to drive greater depth and rigor in cybersecurity governance.

**Igor Tsyganskiy**  
Chief Information Security Officer

---

# 1. The evolving cyber threat landscape

## Key developments

- **Blurred lines**: Nation-state threat actors are conducting operations for financial gain and enlisting the aid of cybercriminals.
- **Hybrid war**: Russia and Iran are leaning into cyber and influence operations to advance military objectives.
- **Deterrence**: The pace of attacks has escalated to constant combat without meaningful consequences for attackers.
- **Identity attacks**: 600 million identity attacks per day. As MFA blocks password attacks, actors shift focus.
- **Election interference**: Russia, Iran, and China all engaged in election influence efforts globally in 2024.
- **Ransomware**: 2.75x increase in human-operated ransomware-linked encounters, though successful encryption decreased threefold due to better defense.
- **Fraud**: Ingenuity and scalability of fraud tactics are surging globally.

---

## Introduction

As we reflect on this past year, it is more apparent that the lines that once divided cybercrime, nation-state sponsored attacks, and influence operations have continued to blur. Cybercrime has continued to mature as a robust ecosystem, utilizing tools learned or stolen from nation-state actors.

**Amy Hogan-Burney**  
Vice President and Deputy General Counsel

**John Lambert**  
Corporate Vice President, Security Fellow

---

## Threat actors and motivations

Microsoft categorizes actors using a weather-related naming system:
- **Blizzard**: Russia
- **Typhoon**: China
- **Sleet**: North Korea
- **Sandstorm**: Iran
- **Tempest**: Financially motivated
- **Flood**: Influence Operations
- **Storm**: Groups in development

### Key Motivations Mapping:
- **Cryptocurrency theft (C)**: North Korea (Jade Sleet, Citrine Sleet).
- **Data destruction (Dd)**: Russia (Seashell Blizzard), Iran (Mint Sandstorm).
- **Election influence (Ei)**: Russia (Ruza Flood), Iran (Cotton Sandstorm), China (Taizi Flood).
- **Espionage (E)**: Russia (Midnight Blizzard), China (Flax Typhoon).

---

## Nation-state threats

### Nation-state threat activity by the numbers
The United States is the most impacted country, followed by Israel, Ukraine, the United Arab Emirates, and Taiwan.

#### Top 10 targeted sectors worldwide:
1. **IT**: 24%
2. **Education and Research**: 21%
3. **Government**: 12%
4. **Think tanks and NGOs**: 5%
5. **Transportation**: 5%
6. **Consumer Retail**: 5%
7. **Finance**: 5%
8. **Manufacturing**: 4%
9. **Communications**: 4%
10. **All others**: 16%

### Regional Activity
- **Russia**: 75% of targets were in Ukraine or a NATO member state.
- **China**: Focused on ASEAN countries around the South China Sea and Taiwan.
- **Iran**: Surged focus on Israel (50% of targeting) after the outbreak of the Israel-Hamas war.
- **North Korea**: Heavily targeted the IT sector (44%) for supply chain attacks and cryptocurrency theft.

#### Cyber Point of View: Japan
Japan identified cybersecurity as a national security matter in 2022, introducing Active Cyber Defense (ACD). The JSDF is establishing a Cyber Command with 20,000 personnel by 2027.

### Blurring lines between nation-state threat actors and cybercriminals
- **North Korea**: Stolen over $3 billion in cryptocurrency since 2017. **Moonstone Sleet** uses custom ransomware (FakePenny) for both intelligence and profit.
- **Russia**: **Aqua Blizzard** (FSB) handed off access to compromised Ukrainian devices to the criminal group **Storm-0593**.
- **Iran**: **Cotton Sandstorm** marketed stolen Israeli dating website data for profit.

### The many faces of hybrid war
- **Iran**: Used cyber personas like "CyberAv3ngers" to target US water controllers made in Israel.
- **Russia**: Used USB-delivered worms (Aqua Blizzard) and malicious pirated software (Seashell Blizzard) to spy on Ukraine.
- **Operational Technology (OT)**: Increase in attacks on internet-exposed OT devices in water and wastewater systems.

#### Actionable Insights: Deterring Advanced Threats
1. **Strengthen international norms**: UN should recognize cloud services as critical infrastructure.
2. **Sharpen attributions**: Use coalition attributions by multiple governments.
3. **Impose consequences**: Use targeted sanctions and clarify "red lines" for cyber intrusions.

---

## Election interference

By the end of 2024, two billion people will have had the opportunity to vote.
- **Russia**: Ruza Flood and Storm-1516 spread anti-Ukraine propaganda.
- **Iran**: Mint Sandstorm targeted a US presidential campaign with spear-phishing.
- **China**: Taizi Flood used AI-generated audio to influence Taiwan's election and sowed discord regarding US college protests.

### Impersonation Threats
Microsoft is monitoring over 10,000 **homoglyph domains** (e.g., `qop.com` instead of `gop.com`) used for phishing.

#### Actionable Insights:
1. Election offices should adopt `.gov` domains.
2. Use defensive registrations of obvious homoglyphs.

---

## Ransomware

### Landscape and trends
- **2.75x increase** in ransomware-linked encounters.
- **Threefold decrease** in successful encryption.
- **92%** of successful attacks originated from **unmanaged devices**.

#### Top human-operated ransomware groups:
1. **Akira**: 17%
2. **Lockbit**: 15%
3. **Play**: 7%
4. **Blackcat**: 6%
5. **Basta**: 6%

### Octo Tempest: A Case Study
A financially motivated group known for SIM swapping and advanced social engineering. They impersonate employees on phone calls to trick helpdesks into resetting passwords.

#### Actionable Insights:
1. Use EDR with tamper protection.
2. Configure "Disable Local Admin Merge" to limit antivirus policy changes.
3. Action tampering alerts immediately.

---

## Fraud

### Landscape and trends
- Scammers stole over **$1 trillion** globally in 2023.
- **Investment scams** accounted for $4.5 billion in losses.
- **Tech support scams**: Microsoft and Amazon collaborated with India's CBI to raid 30+ call centers.

### E-commerce Payment Fraud
- Expected to surpass **$90 billion** annually by 2028.
- **Enumeration techniques**: Fraudsters guess CVV codes or expiration dates.
- **Biometric spoofing**: AI-generated deepfakes bypass mobile payment biometrics.

### Phishing
- **775 million** email messages contained malware.
- **QR code phishing**: 25% of phishing types. Microsoft Defender saw a 94% decrease in success after implementing image detection.
- **Business Email Compromise (BEC)**: Favored method is inbox rule manipulation to hide fraudulent activity.

---

## Identity and social engineering

### Insights on identity attacks
- **600 million** identity attacks per day.
- **99%** are password-based.
- **MFA adoption**: 41% among Microsoft enterprise customers.

### Emerging Techniques
- **Token theft**: Incidents grown to 39,000 per day.
- **Adversary-in-the-Middle (AiTM)**: 146% rise in attacks.
- **Cloud identity compromise**: Actors like **Storm-0539** hijack cloud accounts to conduct gift card fraud.

#### Actionable Insights:
1. Retire passwords for **passkeys**.
2. Use managed service identities instead of developer secrets.
3. Enable "security defaults" (tenants with these experience 80% fewer compromises).

---

## DDoS attacks

- **4,500 attacks per day** in June 2024.
- **Application loop attacks**: A new threat targeting UDP-based protocols (DNS, NTP), potentially affecting 300,000 servers.
- **India**: One of the most affected countries, especially in the gaming sector.

#### Actionable Insights:
1. Minimize public internet exposure of applications.
2. Use a web application firewall (WAF).
3. Conduct regular DDoS simulations.

---

# 2. Centering our organizations on security

## Key developments
- **Secure Future Initiative (SFI)**: Microsoft eliminated 5.75 million inactive tenants and 730k non-compliant apps.
- **Threat-informed defense**: 80% of organizations have attack paths exposing critical assets.
- **Governance**: Security must be a board-level priority with clear accountability.

---

## Secure Future Initiative

> "If you’re faced with the tradeoff between security and another priority, your answer is clear: Do security." — Satya Nadella

### Three Pillars:
1. **Secure by Design**: Security is a foundational requirement.
2. **Secure by Default**: Protections are enabled out of the box.
3. **Secure Operations**: Continuous monitoring and improvement.

---

## Strategic approaches to cybersecurity

### Data Security
- **Visibility**: 40% of cybersecurity budgets are now allocated to data security.
- **Generative AI**: AI can help discover the data estate, but requires labeling and DLP to prevent leakage.

### Hierarchy of Cybersecurity Needs
1. **Protect Identities** (Foundation)
2. **Protect Endpoints**
3. **Secure Digital Assets**
4. **Detect and Remediate Threats**
5. **Automate Security Operations** (Top)

### Threat-informed defense
- **Defenders think in lists; attackers think in graphs.**
- **Attack path management**: Identify "crown jewels" (usually <1% of assets) and the paths leading to them.

### Resilience Maturity Pillars
- **Operational**: EDR on all devices, automated SOC.
- **Tactical**: Practiced IR plans, out-of-band communication.
- **Readiness**: Continuous access reviews, tabletop exercises.
- **Strategic**: Passwordless authentication, zero trust strategy.

---

## Supporting the ecosystem

### The passkey journey
Passkeys use a private key stored on the device, making them phishing-resistant. Over 140 major websites (Amazon, Google, Microsoft) now support them.

### Critical environments (OT)
Microsoft identified over **300 vulnerabilities** in third-party OT applications used in datacenters.
- **Challenge**: OT systems prioritize availability; updates can take 10 years to deploy.
- **Solution**: Adopt a Secure Development Lifecycle (SDLC) for OT products.

---

## Collective action

### Digital transformation of defense
NATO's DIANA and the NATO Innovation Fund are examples of public-private collaboration.

### RAISE: Roundtable for AI, Security, and Ethics
A UN-led initiative with Microsoft to promote AI for national security grounded in international law.

### Supporting democratic elections
Microsoft's four principles:
1. Voters' right to authoritative info.
2. Candidates' ability to verify content authenticity.
3. Campaigns' access to security resources.
4. Election authorities' access to secure tools.

---

# 3. Early insights: AI’s impact on cybersecurity

## Key developments
- **AI for Defense**: Novice users were 26% faster and 44% more accurate using Copilot for Security.
- **Influence Operations**: China-affiliated actors use AI-generated memes; Russia uses AI-generated audio (e.g., Tom Cruise/Elon Musk deepfakes).
- **Global Security**: US Executive Order 14110 and EU AI Act are setting the regulatory stage.

---

## Understanding how generative AI systems work

- **Predictive AI**: Good at classifying and predicting based on specific data.
- **Generative AI**: Best at summarizing and role-playing using general-purpose models.
- **Metacognition**: Using one AI to check the output of another (e.g., an "Editor" AI checking a "Writer" AI).

---

## Emerging threat landscape

### System Threats
- **XPIA (Cross-prompt injection)**: Malicious payloads in processed data (emails/docs) to take over systems.
- **Overreliance**: Users tend to overrate AI reliability.

### Ecosystem Threats
- **Deepfakes**: Used for fraud, blackmail, and information warfare.
- **Cyber threat amplification**: Automated generation of malware and C2 infrastructure.

### Nation-state use of AI
- **China**: Taizi Flood uses AI news anchors and photorealistic protest images.
- **Russia**: Storm-1679 used AI audio of Tom Cruise to disparage the Olympics.
- **Iran**: Used AI-generated anchors to claim hacks on streaming services.

---

## AI for defense

### Harnessing AI to detect attacks
Microsoft uses LLMs to analyze **"endpoint stories"** to detect Hands-on-Keyboard (HOK) attacks that traditional rules miss.

### SOC Efficiencies
1. **Triaging requests**: Saving 20 hours per person per week.
2. **Knowledge gathering**: Reducing article analysis from 2 hours to minutes.
3. **Reporting**: Consolidating artifacts into tailored reports.

---

## Advancing global AI security

### Government Approaches
- **United States**: EO 14110 focuses on safety and security for federal agencies.
- **European Union**: AI Act requires cybersecurity for high-risk systems.
- **China**: Imposes technology ethics reviews and user verification.

### International Standards
- **ISO/IEC 42001**: Management system for AI.
- **ISO/IEC 27090**: Guidance for addressing AI-specific security threats (evasion, poisoning).

---

# Appendix

## References
[^1]: Expanding Microsoft’s Secure Future Initiative (SFI) | May 2024.
[^2]: National Security Strategy of Japan | Dec 2022.
[^5]: UN experts investigate 58 cyberattacks worth $3 bln by North Korea | Reuters.
[^24]: FBI IC3 Annual Report 2023.
[^58]: Randomized Controlled Trials for Microsoft Copilot for Security | SSRN.

## Contributing teams
- **MSTIC**: Microsoft Threat Intelligence Center.
- **DCU**: Digital Crimes Unit.
- **MTAC**: Microsoft Threat Analysis Center.
- **SFI**: Secure Future Initiative engineering teams.
- **ORA**: Office of Responsible AI.

---
**Microsoft Digital Defense Report 2024**  
Learn more: [microsoft.com/mddr](https://microsoft.com/mddr)  
October 2024