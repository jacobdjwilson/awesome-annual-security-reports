# THREATREPORTH1 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Security Trends](#security-trends)
  - [Emerging Trends](#emerging-trends)
    - [Japanese Digital-Skimming Campaign](#japanese-digital-skimming-campaign)
    - [Offline Transaction Fraud via HCE Apps](#offline-transaction-fraud-via-hce-apps)
    - [NFCGate ATM Relay Fraud](#nfcgate-atm-relay-fraud)
    - [Contactless Purchase-Return Authorization (PRA) Fraud](#contactless-purchase-return-authorization-pra-fraud)
    - [Lenient Monitoring on VIP Accounts](#lenient-monitoring-on-vip-accounts)
    - [Token Relay Attacks](#token-relay-attacks)
    - [Chip-Shimming & Transaction Relay](#chip-shimming-transaction-relay)
  - [Evolving Trends](#evolving-trends)
    - [AI-Driven](#ai-driven)
    - [Business Email Compromise (BEC) Incidents](#business-email-compromise-bec-incidents)
    - [Ransomware Actor’s Exploitation of Blockchain-Based Payments and Tumblers](#ransomware-actors-exploitation-of-blockchain-based-payments-and-tumblers)
- [Signiﬁcant Events](#signiﬁcant-events)
  - [Western Alliance Bank – Cleo File Transfer Breach 2025](#western-alliance-bank--cleo-file-transfer-breach-2025)
  - [Insurance Sector Breach (Aflac, Erie, Philadelphia Insurance) – June 2025](#insurance-sector-breach-aflac-erie-philadelphia-insurance--june-2025)
  - [Victoria’s Secret Cybersecurity Incident](#victorias-secret-cybersecurity-incident)
  - [Marks & Spencer, Co-op, and Harrod Ransomware Incident](#marks--spencer-co-op-and-harrod-ransomware-incident)
  - [Cork Protocol Hack: $11M Exploit via Uniswap V4 Hook Vulnerability](#cork-protocol-hack-11m-exploit-via-uniswap-v4-hook-vulnerability)
- [Top Threat Actors Targeting BFSI Sector](#top-threat-actors-targeting-bfsi-sector)
  - [Akira](#akira)
  - [LockBit](#lockbit)
  - [Cl0p](#cl0p)
  - [Lazarus Group (APT38)](#lazarus-group-apt38)
- [Top Malware Campaigns & Indicators](#top-malware-campaigns--indicators)
  - [AsyncRAT](#asyncrat)
  - [Latrodectus](#latrodectus)
  - [Emotet](#emotet)
  - [AgentTesla](#agenttesla)
  - [LockBit](#lockbit-1)
  - [Prilex POS Malware Variant](#prilex-pos-malware-variant)
  - [Cogui Phishing Kit](#cogui-phishing-kit)
- [Top 5 Vulnerabilities of 2025](#top-5-vulnerabilities-of-2025)
  - [CVE-2025-22457](#cve-2025-22457)
  - [CVE-2025-2783](#cve-2025-2783)
  - [CVE-2025-5419](#cve-2025-5419)
  - [CVE-2025-42999](#cve-2025-42999)
  - [CVE-2025-0411](#cve-2025-0411)
- [Conclusion](#conclusion)
- [References](#references)

The official report URL is: https://www.sisasappersthreat.com

# Report Content Below

THREATREPORTH1 2025

## Executive Summary

In 2025, the global financial ecosystem confronts a dual-front cyber onslaught: on one side, sophisticated malware, ransomware-as-a-service outfits and nation-state actors, such as LockBit, Akira, Cl0p, and North Korea’s Lazarus Group, are executing high-value data theft, double-extortion and multi-billion-dollar crypto heists; on the other, critical software vulnerabilities have been weaponized with unprecedented speed. Beyond stealer malware like AgentTesla and phishing kits like Cogui, five zero-day and high-severity flaws (including CVE-2025-22457 in Ivanti Connect Secure, sandbox escapes in Chrome’s V8 engine, SAP NetWeaver deserialization (CVE-2025-42999), and a Mark-of-the-Web bypass in 7-Zip) were added to CISA’s Known Exploited Vulnerabilities catalog and exploited in the wild. These vulnerabilities span enterprise VPN gateways, browser sandboxes, application deserialization, and archive handling, underscoring how attackers blend technical exploits with human-centric fraud. To stay ahead, BFSI institutions must not only deploy zero-trust architectures, endpoint segmentation, immutable backups, and AI-driven anomaly detection, but also implement a rigorous, real-time vulnerability management program: immediate patching of affected systems, thorough threat hunting on unpatched assets, and continuous compliance with KEV deadlines are now as critical as perimeter defenses.

### BFSI-Specific Impact

The BFSI sector, particularly banks, mortgage firms, credit unions, NBFCs, and investment entities, faced targeted attacks leveraging stolen credentials, unpatched VPNs, phishing, and supply-chain vulnerabilities. Actor groups used specialized dark-web leak sites and negotiation portals to extort payment and showcase stolen data.

### Types of Payment Card Fraud Threats in H1 2025

![Image description]

### Geographical Targets of PCI Fraud H1 2025

![Image description]

# 01

## Security Trends

### 1.1 Emerging Trends

#### 1.1.1 Japanese Digital-Skimming Campaign

Description: A long-running group exploited XSS vulnerabilities in Japanese eCommerce platforms. They submitted orders laced with malicious scripts that stole admin credentials, then injected JavaScript sniffer code to harvest PANs, CVVs, expiration dates, and billing addresses from real customer checkouts. Harvested data was stored in PNG files for covert exfiltration.

Why it matters: This multi-stage compromise, from XSS to credential theft to digital skimming, demonstrates how threat actors chain minor vulnerabilities into full data-theft campaigns.

#### 1.1.2. Offline Transaction Fraud via HCE Apps

Description: Merchants misconfigure POS terminals to permit offline chip approvals. A malicious Android Host-Card-Emulation (HCE) app simulates a valid offline cryptogram (TC) to the terminal instead of forwarding the request online for issuer authorization. The terminal happily approves, then later sends the bogus transaction for clearing, leaving issuers on the hook.

Why it matters: This entirely in-store attack can evade real-time authorization controls. Only careful terminal configuration and velocity-based decline rules can stop it.

#### 1.1.3 NFCGate ATM Relay Fraud

Description: Victims are phished into installing a spoofed "bank" app containing modified NFCGate code. They're instructed to place their contactless card under their phone and enter their PIN, thinking they're verifying identity. Behind the scenes, the app reads NFC data and PIN, relays to a co-conspirator's device, which then performs an ATM withdrawal via NFC on a compromised or collusive ATM.

Why it matters: Tapping into NFC's convenience feature subverts physical-POS and ATM controls, all through social engineering. Victims willingly hand over both data and PIN.

### 1.1.4 Contactless Purchase-Return Authorization (PRA) Fraud

Description: Fraudsters exploit the window between an approved Purchase Return Authorization (PRA) and its subsequent reversal. They buy high-value items with a debit card, then attempt a return using gift cards while feigning distraction (e.g. on a phone call). The initial full-value return fails, so they process multiple partial returns across several gift cards, each successful partial return boosts the issuer's Open-to-Buy (OTB) on the debit account. Finally, they cancel the returns and leave with the merchandise. Issuers, seeing only the interim successful partial credits, allow the customer to withdraw cash against the inflated balance before the final reversal posts.

Why It Matters:
* Exploits timing gaps in issuer systems
* Evades merchant reconciliation (offsetting credits)
* Cross-merchant coordination, from 10 to 120 miles, enables sustained OTB inflation
* Losses accrue at the issuer level, often undiscovered until after cash-outs occur

Recommendations:
* Real-Time Refund Monitoring: Detect repetitive partial refunds and flag multiple returns without matching original sales
* OTB Controls: Do not increase available balance until settlement arrives
* Settlement-First Posting: For single-message issuers, ensure PRAs post only after settlement, not at authorization
* Customer/Merchant Education: Warn that reversed credits may still be spendable briefly

### 1.1.5 Lenient Monitoring on VIP Accounts

Description: Issuers often exempt high-net-worth "VIP" accounts from standard fraud rules to minimize false declines. Attackers purchase compromised VIP PANs from underground shops and execute repeated high-dollar transactions, approved because these cards bypass real-time velocity and location checks.

Why It Matters
* VIP exemption creates a high-value blind spot
* Single transaction losses can exceed hundreds of thousands of dollars
* Reputation-driven rule-relaxation becomes exploitable

Recommendations:
* Inclusive Monitoring: Apply real-time fraud rules to all account tiers; adjust thresholds but never omit VIP cards
* Geolocation Analytics: Alert on implausible travel-speed transactions
* VIP Confirmation Protocols: Direct high-value alerts to dedicated VIP relationship managers for quick out-of-band verification

### 1.1.6 Token Relay Attacks

Description: Threat actors blend provisioning fraud with geographically distributed relay: 1) Provision a stolen PAN as a mobile token on Device A. 2) Co-conspirators at Stores B, C, D each run an NFC tap using a malicious app that relays authorization requests back to Device A. Valid ARQC cryptograms from Device A enable approved in-store transactions at each location, often for cashable gift cards.

Why It Matters
* Scales a single stolen PAN into multiple high-value purchases
* Exploits valid cryptograms, so risk systems see "legitimate" chip transactions

Recommendations:
* Provisioning Monitoring: Scrutinize device attributes, provisioning risk scores, and location anomalies at token issue time
* ATC-Based Risk Scoring: Use the Application Transaction Counter from chip messages to detect out-of-sequence or excessive uses
* Post-Provisioning Velocity: Impose tighter limits on the first few token transactions; gradually relax after establishing normal behavior

### 1.1.7 Chip-Shimming & Transaction Relay

Description: Shimming devices, thin interceptors inserted into EMV chip slots on unattended terminals (e.g., transit UATs), capture chip data and PIN. Attackers relay this to a receiver card, then use the harvested data at an ATM for immediate cash-out. The latest evolution even blocks legitimate chip reads at the POS, preventing detection by "follow-on" transaction rules.

Why It Matters
* Targets high-traffic areas (transit hubs) where users default to chip dip vs. contactless
* By blocking legitimate authorizations, it evades detection patterns that monitor ATM right after POS

Recommendations:
* Eliminate Plaintext Offline PINs: Enhanced security protocols phased out plaintext PIN storage on terminals as of Jan 2025
* Merchant Onboarding Rules: Flag new or sudden high-value, low-volume merchants, especially in tourist corridors, for enhanced due diligence
* Issuer Rules: Decline or alert on cross-border ATM cash-outs at maximum daily limits, especially in geographies inconsistent with typical cardholder behavior

### 1.2 Evolving Trends

#### 1.2.1 AI-Driven

Attack Types Between January and July 2025, the Banking, Financial Services, and Insurance (BFSI) sector faced a surge in cyber attacks leveraging artificial intelligence (AI) and machine learning (ML) technologies. Attackers utilized AI to automate and enhance attack vectors, including phishing, ransomware, deepfake scams, and adversarial tactics, exploiting the sector’s reliance on trust and sensitive data. This report provides a technical deep dive into these threats, their impact on BFSI, notable incidents, and AI-based defense strategies, encouraging reflection on how these technologies reshape cybersecurity.

1.  **Phishing and Spear-Phishing**
    Generative AI models have transformed phishing into a highly targeted threat. Advanced language models, such as GPT - 4.5 or similar, generate contextually relevant, grammatically flawless emails and messages that mimic trusted entities. In June 2025, an Iran - linked APT group (APT35) targeted BFSI executives in Israel with AI - crafted spear -phishing emails and WhatsApp messages, directing victims to fake login pages for banking platforms to harvest credentials. Industry data indicate that 83% of phishing emails targeting BFSI from September 2024 to February 2025 were AI - generated, a 54% year-over - year increase.

    Technical Details:
    *   Models Used: Large language models (LLMs) like GPT - 4.5, capable of natural language generation with high contextual accuracy.
    *   Data Sources: Publicly available data from social media, corporate websites, and breached datasets, used to personalize messages.
    *   Attack Vector: Emails and instant messages with malicious links or attachments, often hosted on domains mimicking legitimate services.
    *   Detection Challenges: Signature-based detection fails against dynamic AI-generated content, requiring ML-based behavioral analysis to identify anomalies in message patterns or metadata.

2.  **Ransomware and Automated Malware**
    AI has been integrated into malware development, notably in ransomware. The FunkSec ransomware group, emerging in late 2024, targeted over 80 BFSI entities with its AI-assisted malware, FunkSec V1.5, written in Rust. The group used AI to generate code comments and automate target selection and ransom negotiations via an AI chatbot, enabling even low-skill attackers to deploy sophisticated Ransomware-as-a-Service (RaaS).

3.  **Deepfake Audio/Video Scams**
    AI-driven deepfake technology has enabled sophisticated fraud by cloning voices and faces. In January 2025, a Hong Kong merchant lost HK$145 million (~$18.5M) in a cryptocurrency scam where attackers used AI to clone a financial manager’s voice on WhatsApp, convincing the victim to transfer USDT. Similarly, a U.S. insurance firm in May 2025 lost millions due to AI-generated voicemails impersonating a CFO.

    Technical Details:
    *   Voice Cloning Process:
        *   Audio Collection: Scammers gather 3–30 seconds of audio from public sources (e.g., social media, interviews) or social engineering.
        *   AI Modeling: Deep learning models like WaveNet or Tacotron analyze vocal traits (pitch, tone, cadence) to create a voice profile.
        *   Voice Synthesis: Synthetic speech generated to mimic the target, deployable in real-time or pre-recorded scams.
    *   Application in Scams: Impersonation of trusted individuals to authorize fraudulent transactions or extract credentials.

    Targeted BFSI Subsectors:
    *   Banking: Commercial and retail banks face AI-enhanced Business Email Compromise (BEC) and phishing campaigns. AI-crafted emails mimicking bank executives or vendors tricked employees into transferring funds or exposing credentials.
    *   Cryptocurrency Platforms: Crypto exchanges and traders were prime targets for deepfake scams and ransomware. The January 2025 Hong Kong crypto scam underscores the sector’s exposure to AI-driven fraud.
    *   Insurance: Insurers were hit by AI-generated phishing and deepfake scams impersonating policyholders or executives, aiming to manipulate claims or authorize fraudulent payouts.
    *   Payment Systems: Fintech and payment processors face AI-powered attacks exploiting transaction systems, with automated bots testing for vulnerabilities in real time.

    Notable Incidents in BFSI
    *   Jan 2025 – Hong Kong Crypto Scam: Attackers used an AI-cloned voice of a bank executive on WhatsApp to deceive a merchant into a fraudulent cryptocurrency investment, resulting in a HK$145M (~$18.5M) loss. Hong Kong police noted this as part of a broader wave of AI-assisted BFSI frauds costing over HK$200M in a single week.
    *   Jan 2025 – FunkSec Ransomware: Check Point reported that the “FunkSec” ransomware gang targeted 80+ BFSI entities, including banks and crypto platforms, using AI-generated code and an AI chatbot for target selection and ransom negotiations. The malware’s polished code comments, contrasting the group’s poor English, confirmed AI’s role in its development.
    *   May 2025 – U.S. Insurance Firm Deepfake Fraud: A U.S. insurer was defrauded of millions after attackers used AI-generated voicemails impersonating a CFO to authorize wire transfers. The incident prompted warnings about AI-driven vishing targeting BFSI executives.
    *   Jun 2025 – Iran-linked APT35 Campaign: An Iranian APT targeted Israeli BFSI professionals with AI-crafted spear-phishing emails and WhatsApp messages, directing victims to fake banking login pages. This campaign reflects AI’s role in nation-state attacks on financial systems.

    Defense Strategies in BFSI

    | Strategy              | Description                                                                                             |
    | :-------------------- | :------------------------------------------------------------------------------------------------------ |
    | Behavioral Analytics  | AI systems monitor user behavior to detect anomalies like unusual transactions or logins, and spot AI-generated phishing. |
    | Deepfake Detection    | AI tools detect manipulated audio/video to prevent fraud.                                               |
    | Automated Response Systems | AI-driven tools isolate/neutralize threats rapidly, reducing incident response times.                   |
    | Employee Training     | Staff are trained to detect AI-generated threats and phishing attempts.                                 |

#### 1.2.2 Business Email Compromise (BEC) Incidents

Business Email Compromise (BEC) continues to be a top cyber-fraud threat in 2025. BEC schemes range from invoice and CEO impersonation scams to sophisticated vendor compromises, resulting in billions of dollars in losses (the FBI estimates ~$51 billion exposed globally). This report summarizes the types of BEC attacks, notable global incidents (Jan–Jul 2025), their financial/organizational impact, evolving attacker techniques/trends, typical victims, and defensive best practices.

**Types of BEC Attacks and Threat Vectors**

Attackers use various social-engineering techniques to trick employees into wiring funds or disclosing data. Key BEC scam types identified by the FBI include:

| BEC Scam Type                 | Description / Tactics