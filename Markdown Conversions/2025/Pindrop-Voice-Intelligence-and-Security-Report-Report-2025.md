# Voice Intelligence and Security Report 2025

## Table of Contents
- [Introduction](#introduction)
- [State of the Industry](#state-of-the-industry)
  - [Deepfakes are becoming more ‘human’](#deepfakes-are-becoming-more-human)
  - [Data breaches have reached an all-time high](#data-breaches-have-reached-an-all-time-high)
  - [Fraud attempts increased by +26%](#fraud-attempts-increased-by-26)
  - [The next generation of fraud is voice-first and AI-fueled](#the-next-generation-of-fraud-is-voice-first-and-ai-fueled)
    - [Tactic 1: Synthetic voice usage and pitch manipulation in evasion tactics](#tactic-1-synthetic-voice-usage-and-pitch-manipulation-in-evasion-tactics)
    - [Tactic 2: Caller ID spoofing and the erosion of metadata-based defenses](#tactic-2-caller-id-spoofing-and-the-erosion-of-metadata-based-defenses)
- [Security Landscape](#security-landscape)
  - [Advancements in AI](#advancements-in-ai)
  - [Agentic AI is disrupting identity verification and creating new security threats](#agentic-ai-is-disrupting-identity-verification-and-creating-new-security-threats)
  - [AI is amplifying fraud across sectors, channels, and tactics](#ai-is-amplifying-fraud-across-sectors-channels-and-tactics)
  - [Top fraud tactics: Phishing and ATOs](#top-fraud-tactics-phishing-and-atos)
- [Fraud by Vertical](#fraud-by-vertical)
  - [+61% increase in bank fraud](#61-increase-in-bank-fraud)
  - [38% increase in credit union fraud since 2020](#38-increase-in-credit-union-fraud-since-2020)
  - [Insurance fraud is increasing in cost, complexity, and impact](#insurance-fraud-is-increasing-in-cost-complexity-and-impact)
  - [Brokerage fraud may be less common—but can be far more damaging](#brokerage-fraud-may-be-less-commonbut-can-be-far-more-damaging)
  - [Retail is under siege](#retail-is-under-siege)
  - [Deepfake activity doubled in a single quarter](#deepfake-activity-doubled-in-a-single-quarter)
  - [The surge in synthetic voice fraud reveals a more complex threat landscape](#the-surge-in-synthetic-voice-fraud-reveals-a-more-complex-threat-landscape)
  - [Synthetic voices, real consequences](#synthetic-voices-real-consequences)
- [Authentication Landscape](#authentication-landscape)
  - [The evolving security landscape is reshaping how organizations and consumers engage.](#the-evolving-security-landscape-is-reshaping-how-organizations-and-consumers-engage)
  - [Average handle time reveals the cost of complexity](#average-handle-time-reveals-the-cost-of-complexity)
  - [Why caller ID can't be trusted](#why-caller-id-cant-be-trusted)
  - [Outdated verification methods are fueling ATOs](#outdated-verification-methods-are-fueling-atos)
  - [Increased self-service requires customer-friendly authentication](#increased-self-service-requires-customer-friendly-authentication)
  - [Enroll once, authenticate everywhere](#enroll-once-authenticate-everywhere)
  - [Voice is the backbone of secure authentication](#voice-is-the-backbone-of-secure-authentication)
- [2025 Forecast](#2025-forecast)
  - [Contact center fraud is projected to grow +8% in 2025](#contact-center-fraud-is-projected-to-grow-8-in-2025)
  - [2025 deepfake fraud forecast shows +162% increase](#2025-deepfake-fraud-forecast-shows-162-increase)
  - [AI advancements will continue to open new doors for fraud](#ai-advancements-will-continue-to-open-new-doors-for-fraud)
  - [Emerging risk: Deepfakes in real-time communications](#emerging-risk-deepfakes-in-real-time-communications)
  - [Retail fraud to more than double in 2025](#retail-fraud-to-more-than-double-in-2025)
- [Fighting Fraud in an AI-First World](#fighting-fraud-in-an-ai-first-world)
  - [Defend your enterprise against deepfakes](#defend-your-enterprise-against-deepfakes)
  - [Advance the fight against fraud](#advance-the-fight-against-fraud)
  - [Strengthen authentication to enhance the customer experience](#strengthen-authentication-to-enhance-the-customer-experience)
- [Conclusion](#conclusion)
  - [From insight to action](#from-insight-to-action)
  - [About Pindrop](#about-pindrop)

---

# Introduction

Understanding the landscape
The security question is no longer only “Are you who you say you are?”—now it’s also “Are you even human?”

As recession fears grow and economic pressure intensifies, organizations are being forced to operate leaner than ever. At the same time, they’re contending with a parallel crisis: a collapse in trust across digital and voice interactions, fueled by the rapid rise of generative AI (Gen AI). These two forces aren’t happening in isolation—they’re converging, compounding risk, and stretching security teams to their limits. Gen AI isn’t just changing how we work—it’s destabilizing long-held assumptions about identity, authenticity, and intent. In this dual-threat environment, efficiency cannot come at the expense of security. The ability to detect deepfakes at speed and scale is now mission-critical, both for stopping a new wave of AI-powered fraud and for safeguarding customer confidence in a world where the line between real and synthetic is rapidly disappearing.

The pace of change is staggering. In early 2023, synthetic voice fraud appeared in isolated bursts. Now, it’s a flood of AI-powered deception, surging across industries and eroding trust in real time. In just one year, the rate of deepfake attacks has surged by more than 1,300%, up from one every two days to seven per day.[^1] And with every new model released, the gap between what’s real and what’s generated continues to shrink.

Gen AI is no longer on the horizon. It’s here, accelerating fast, reshaping industries, and redefining risk in real time. As macroeconomic pressures force organizations to do more with less, the rapid democratization of Gen AI is proving to be both a game-changer and a threat multiplier. With training costs plummeting and open-source tools readily available, highly sophisticated AI capabilities are now accessible to anyone, including fraudsters.

> According to Deloitte, Gen AI could help push fraud losses to $40 billion in the U.S. by 2027—more than tripling since 2023.[^2]

The scale and sophistication of AI-driven attacks are now directly impacting enterprise authentication and customer service. Voice remains a critical pillar of secure authentication—especially when paired with deepfake detection as part of a layered, multifactor approach. But legacy systems are increasingly vulnerable to AI-generated impersonation. To address the growing risk of cross-channel voice attacks, organizations should urgently reassess their authentication strategy and adopt platforms that integrate advanced voice biometrics and deepfake detection into a unified, real-time defense.

[^1]: Pindrop analysis of non-live calls and fraud data from more than 1.2 B calls in 2024 and 2023
[^2]: Deloitte, Deepfake Banking Fraud: Risk on the Rise, Financial Services Industry Predictions, 2024

# State of the Industry

## Deepfakes are becoming more ‘human’

In mid-2023, Pindrop raised the alarm about the emergence of sophisticated deepfake threats. Before then, the limited capabilities of existing text-to-speech (TTS) engines and the robotic nature of synthetic voices and speech patterns made deepfakes relatively easy to detect. ChatGPT, which had been recently launched, disrupted the landscape of how speech could be “generated” and made synthetic voices sound more human-like. Today, we have witnessed an explosion of synthetic audio creation and Gen AI-driven TTS tools that create a likeness that is indistinguishable from reality. In other words, they push deepfakes across the _uncanny valley_.

As synthetic speech becomes nearly indistinguishable from real voices, voice-based attacks are escalating. But voice authentication isn’t obsolete—it’s more critical than ever. The key is adapting: today’s solutions must detect deepfakes through advanced signal analysis and behavioral cues that go beyond traditional voice matching. Voice remains a powerful biometric—unique, dynamic, and difficult to replicate in real time. When combined with multifactor risk signals, it becomes a formidable defense against even the most convincing deepfakes.

![Diagram illustrating 3 key forces behind the growing speed and sophistication of deepfakes. The first force is "The use of automated bots," explaining that LLMs have reduced synthetic voice delay to near real-time, making distinction difficult. Pindrop trains its detection system on commercial and open-source AI models to identify synthetic speech and the specific AI model. The second force is "“Emotional-sounding” AI," detailing how synthetic speech can convey emotions, making voices more convincing. Pindrop expands its liveness detection training dataset to recognize subtle artifacts. The third force is "Real-time voice conversion," mentioning tools like Respeecher that allow instant pitch, timbre, and accent changes, making it easier for fraudsters to evade voice recognition. Pindrop partnered with Respeecher to detect fraudulent use of such software. The diagram also notes that the real threat of deepfakes lies in fraudsters' ability to mount large-scale, automated attacks at low cost.](image-1.png)

## Data breaches have reached an all-time high

According to the ‘Digital Privacy Survey Report 2024’, nearly 61% of Americans have had their data breached on at least one of their accounts.[^3] Data breaches and ID theft are leading indicators of fraud, particularly contact center fraud. Data breaches reached an all-time high of 3,205 in 2023 and continued at a record pace with 3,158 breaches in 2024.[^4]

> Data breaches reached an all-time high of **3,205 in 2023** and continued at a record pace with **3,158 breaches in 2024**.[^4]

![Bar chart titled 'Continued Trend of Data Breaches' showing the number of data breaches per year. In 2019, there were 1,279 breaches. In 2020, 1,108. In 2021, 1,860. In 2022, 1,801. In 2023, 3,205. In 2024, 3,158.](image-2.png)

Increasingly, stolen data from breaches is posted to the dark web and other platforms. Personal Identifiable Information (PII) and bank account information were shared at a +61% higher rate in 2024 compared to 2023.[^5]

This leak of personal information has affected a record number of people, with more than 1.7 billion notices sent out to victims of data breaches in 2024. This represents a 312% increase in victims from the previous year.[^4] Most of the impact came from six “mega-breaches” that resulted in at least 100M breach notices being issued in each event.[^4] To quantify the financial impact of these breaches, the average cost of a data breach in the U.S. reached an all-time high of $9.36 million in 2024[^6], a **14% increase** from 2019.[^7]

![Table titled 'Stolen Data Posted on the Dark Web' comparing 2023 and 2024 data. For 'PII Posted', 2023 shows 108 and 2024 shows 821. For 'Full Bank Account Numbers Posted', 2023 shows 59 and 2024 shows 872.](image-3.png)

[^3]: U.S. News & World Report, “Digital Privacy Consumer Survey,” 360 Reviews, 2024
[^4]: Identity Theft Resource Center, 2024 Data Breach Report, 2024
[^5]: Insikt Group, Annual Payment Fraud Intelligence Report: 2024
[^6]: KnowBe4, The State of Cyber Insurance: 2025 Global Report, 2025
[^7]: Digital Guardian, “What’s the Cost of a Data Breach in 2019?”, 2019

## Fraud attempts increased by +26%

Over the past two years, contact centers have been hit hard by rising fraud—driven by frequent data breaches and an unprecedented dump of personal data on the dark web. That’s why the research team at Pindrop wasn’t surprised to find that fraud attempts have increased by more than 26% in 2024 over the previous year.[^8] Last year, Pindrop had predicted a 4% increase in fraud, but the actual increase outpaced our prediction by a massive +22%. Data breaches directly correlate with increased account reconnaissance and contact center fraud, as referenced in the [2023 Voice Intelligence and Security Report](URL_TO_2023_REPORT).

> In 2024, Pindrop saw a fraud rate of **1 attempt every 599 calls**, +22% higher than our prediction of 1 in 730 attempts.

![Bar chart titled '2024 Predictions vs. Actual Fraud' comparing predicted and actual fraud rates. '2024 Predicted' shows 1 in 730 calls. '2024 Actual' shows 1 in 599 calls. '2023 Actual' is also shown as 1 in 730 calls.](image-4.png)

### 3 accelerators driving the fraud spike

1.  **Data breaches and stolen personally identifiable information (PII):** A surge in data breaches—and the growing volume and quality of personal data on the dark web—has made it easier for fraudsters to target victims across every communication channel.
2.  **Using low-cost AI tools to accelerate and amplify fraud:** The accessibility and low cost of AI tools exacerbate fraud attempts, as they easily allow fraudsters to modulate their voices, create sophisticated deepfakes, deceive contact center agents, and bypass voice recognition systems.
3.  **Exploiting self-service channels for evasion and reconnaissance:** Companies increasingly rely on self-service across both phone and online channels to improve customer experience and reduce operational costs. Fraudsters have started exploiting these channels through ongoing account reconnaissance in the IVR systems, with increasing use of high-scale synthetic voices for extracting information, bypassing voice recognition systems, and mimicking the IVR’s operating patterns.
4.  **Bypassing outdated authentication methods with advanced spoofing:** 88% of caller interactions still rely on manual approaches,[^9] like knowledge-based authentication (KBAs) and one-time passwords (OTPs). Meanwhile, fraudsters have evolved by spoofing back-end carrier metadata and exploiting OTPs with advanced tools. These methods are easy to bypass, giving attackers a clear path to commit fraud.

[^8]: Pindrop analysis of fraud data and call volumes across customers for the year 2024 and 2023
[^9]: Contact Babel: US Customer Experience, Decision Makers Guide, 2025

## The next generation of fraud is voice-first and AI-fueled

Synthetic voice manipulation, aggressive spoofing, and deepfake audio are now core tactics in the modern fraud playbook. These AI-driven techniques are reshaping voice channel threats—making attacks faster, more convincing, and harder to detect.

### Tactic 1: Synthetic voice usage and pitch manipulation in evasion tactics

Pindrop® Pulse, our AI-powered liveness detection solution, analyzed 130 million calls and uncovered a sharp rise in synthetic voice activity. In Q4 2024, synthetic voices made up 0.33% of all contact center calls. While that number seems small, it represents an increase of +173% compared to Q1, driven by rapid advancements in voice generation technology.

Fraudsters are turning to voice modulation, manipulating their pitch, cadence, tone, and volume to imitate others or confuse agents. With easy access to voice-changing apps on mobile platforms, it’s now simpler to mask their identity. For instance, a major U.S. retailer reported a surge in attackers posing as virtual legal assistants requesting account closures on behalf of customers.

Access to powerful AI platforms has removed the technical barriers to creating convincing deepfakes. In 2024 alone, Hugging Face hosted more than 2,400 text-to-audio models and over 1,800 TTS models. While these tools are powerful assets for developers, they’re equally accessible to fraudsters looking to generate lifelike synthetic voices.

Pindrop is aware of this growing trend and prioritizes utilizing AI models to train our deepfake detection technology. Our training dataset now includes over 500 TTS engines, a fourfold increase from last year, significantly improving the detection accuracy of synthetic voices.

![Bar chart titled 'Text-to-Speech (TTS) Tools Used by Pindrop to Train AI Models'. It shows the number of TTS engines used by Pindrop for training: 10 in 2022, 120 in 2023, and 500 in 2024.](image-5.png)

### Tactic 2: Caller ID spoofing and the erosion of metadata-based defenses

Malicious actors continue to use spoofing to mask their phone numbers and launch phishing and reconnaissance attacks. What was once a basic tactic has now become far more aggressive and sophisticated—enabled by access to breach data, dark web resources, and increasingly advanced tools.

Fraudsters are now:
- Using dark web tutorials on phishing and account takeovers (ATO)
- Exploiting readily available personal information from data breaches
- Relying on spoofing-as-a-service platforms
- Combining spoofing with synthetic voice technology
- Accessing tools that check phone status and bypass anti-spoofing solutions

**Voice Authentication Remains a Critical Security Layer**

Roughly 70% of all contact center interactions still happen over the phone[^10], making voice a key channel for customer engagement—especially for urgent requests and across omnichannel journeys. As a result, authenticating customers through voice continues to play a vital role in the overall customer experience.

But the threat landscape is evolving. Generative AI tools and increasingly sophisticated fraud tactics are making voice-based attacks more frequent and harder to detect. Traditional methods like KBA and OTP are no longer enough—especially as enterprises work to improve both security and experience. To stay ahead, organizations must strengthen voice authentication with deepfake detection. Passively analyzing audio to determine whether a caller is a real human—not an AI-generated voice—is a critical first step before verifying identity through voice biometrics.

[^10]: Contact Babel: US US Contact Centers 2024-2028 The State of the Industry & Technology Penetration

# Security Landscape

## Advancements in AI

The line between human and machine is blurring–and soon humans likely won’t be able to tell the difference. While this phenomenon could have positive implications for commerce, art, and media, it also has a far-reaching impact on the ways that enterprises serve customers.

**Gen AI has changed the role of ‘voice’ in customer interactions**

New tools are making it easier and more efficient for contact centers and enterprises to manage voice interactions. With increased use of chatbots, interactive voice assistants (IVAs), emotional analysis, and transcription, many organizations are shifting toward self-service across both the phone and digital channels.

> Traditional biometric systems _must evolve_ into multifactor, AI-driven solutions to keep pace with emerging threats.

Business decisions aimed at streamlining operations are creating unintended risks. The most pressing concerns include:

-   **Significant rise in injection attacks:** An injection attack consists of an attacker introducing digital content to the biometric process, bypassing the sensor (camera). IProov reported a +704% increase in face swap attacks and a +255% increase in mobile web injection attacks in the second half of 2023.[^11] Gartner warns that these attacks can bypass biometric defenses and give the attacker access to sensitive data.[^12]
-   **Weakness of single-factor voice recognition:** Standalone voice biometrics struggle against deepfakes. A [University of Waterloo study](URL_TO_WATERLOO_STUDY) demonstrated that voice recognition detection accuracy ranges from 38% to 88% due to vulnerabilities like silence manipulation, spectral tweaks, and TTS spoofing. These systems can flag voice mismatches but can’t reliably determine if a voice is human.
-   **Open-access models are enabling rapid deepfake creation and malicious use:** Freely available AI models have made synthetic voice generation widely accessible—shifting it from a specialized capability to a tool anyone can misuse. Fraudsters can now train neural networks on large voice datasets to synthesize realistic speech that closely mimics a target’s voice, making impersonation attacks more convincing and accessible.

The release of DeepSeek, an open-source AI reasoning model, caused a stir in the tech industry. Unlike standard LLMs, DeepSeek uses a chain-of-thought process to work through complex problems.[^13] This gives attackers the ability to process and analyze massive datasets, detect anomalies, and exploit system vulnerabilities in real time, making it a formidable tool for identifying vulnerabilities in complex systems.[^14]

Fraudsters are also using models like OmniHuman-1 from Bytedance to generate highly realistic videos from a single audio clip and image, further enhancing the realism of synthetic content. As these tools become more powerful and easier to access, the deepfake threat landscape continues to expand.

[^11]: IProov: Threat Intelligence Report, 2024
[^12]: Gartner: How to Mitigate Deepfake Identity Impersonation Attacks, 5 February 2025
[^13]: Trend Micro, “Exploiting DeepSeek R1: Threat Actors Abuse AI Model for Phishing and Fraud,” Trend Micro Research, 2 April 2025
[^14]: Anthony Kimery, “China’s DeepSeek AI Poses Formidable Cyber, Data Privacy Threats,” Biometric Update, 24 January 2025

## Agentic AI is disrupting identity verification and creating new security threats

A new wave of autonomous AI systems is emerging—powered by the fusion of LLMs, machine learning, and enterprise automation. Known as agentic AI, these systems can analyze data, set goals, and act with minimal human input. This shift is poised to disrupt identity verification and introduce new security risks. Gartner estimates that by 2026, five billion connected products will exist worldwide with the potential