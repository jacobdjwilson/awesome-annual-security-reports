# AI-Security-Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [AI and ML Usage Trends](#ai-and-ml-usage-trends)
- [AI/ML transactions overview](#aiml-transactions-overview)
- [Enterprise AI Risks and Real-World Threat Scenarios](#enterprise-ai-risks-and-real-world-threat-scenarios)
- [Core risks of enterprise AI adoption](#core-risks-of-enterprise-ai-adoption)
- [DeepSeek and open-source AI: the risk of frontier models in your pocket](#deepseek-and-open-source-ai-the-risk-of-frontier-models-in-your-pocket)
- [5 prompts to deception: DeepSeek-generated phishing page](#5-prompts-to-deception-deepseek-generated-phishing-page)
- [AI’s growing role in cyber threats](#ais-growing-role-in-cyber-threats)
- [Supercharged social engineering](#supercharged-social-engineering)
- [AI-driven malware and ransomware across the attack chain](#ai-driven-malware-and-ransomware-across-the-attack-chain)
- [Agentic AI: the next frontier in autonomous AI—and attack vectors](#agentic-ai-the-next-frontier-in-autonomous-aiand-attack-vectors)
- [Case study: How threat actors are exploiting interest in AI](#case-study-how-threat-actors-are-exploiting-interest-in-ai)
- [The Evolving Scope of AI Regulations](#the-evolving-scope-of-ai-regulations)
- [AI Threat Predictions for 2025-2026](#ai-threat-predictions-for-2025-2026)
- [Best Practices for Secure Enterprise AI Adoption](#best-practices-for-secure-enterprise-ai-adoption)
- [5 steps to securely integrate GenAI tools](#5-steps-to-securely-integrate-genai-tools)
- [How Zscaler Delivers Zero Trust + AI](#how-zscaler-delivers-zero-trust--ai)
- [Under the hood: Zscaler’s AI security and data advantage](#under-the-hood-zscaler’s-ai-security-and-data-advantage)
- [A comprehensive approach to AI security](#a-comprehensive-approach-to-ai-security)
- [Leveraging AI security across the attack chain](#leveraging-ai-security-across-the-attack-chain)
- [Research Methodology](#research-methodology)
- [About ThreatLabz](#about-threatlabz)
- [About Zscaler](#about-zscaler)

---

## Executive Summary

Another year in the still new “era of AI” has come and gone, marked by game-changing advancements, rising adoption across industries, and high-profile challenges.

Enterprises now see artificial intelligence (AI) and machine learning (ML) as essential for growth, driving efficiency, smarter decision-making, and faster innovation. On the other hand, AI adoption brings serious security risks, from unsanctioned usage (“shadow AI”) to data exposure. Even more concerning, threat actors seem to have the upper hand as they weaponize these same tools to amplify attacks. What once required skill now takes minimal effort. What once took hours now takes seconds.

This shift was on full display in 2024. GenAI became a cybercriminal’s social engineering machine. Today, phishing emails mimic trusted colleagues with eerie accuracy. Deepfake technology turns voices and videos into weapons of deception.

In 2025, the power and perils of AI loom larger than ever. Threat actors will continue to push the boundaries of AI’s malicious capabilities. Yet, AI isn’t just enabling attacks—it’s also now a critical line of defense, powering the fight against these attacks.

The Zscaler ThreatLabz 2025 AI Security Report examines the many facets of AI in cybersecurity, from AI/ML adoption to AI-driven threats and security capabilities. Analyzing 536.5 billion transactions captured across the Zscaler Zero Trust Exchange™ from AI/ML tools between February and December 2024, ThreatLabz discovered both surprising and unsurprising shifts in usage trends by enterprises worldwide.

ChatGPT drove the most AI/ML transactions, making up nearly half of the total volume. From an industry perspective, the Finance & Insurance and Manufacturing verticals drove the most transactions as top adopters of AI. However, increased adoption didn’t mean unfettered access: a large percentage of AI/ML transactions were actively blocked.

Beyond usage trends, ThreatLabz discovered real-world threat scenarios from AI-enhanced phishing to fake AI platforms. This report also explores recent developments in areas that will undoubtedly influence AI in 2025 and beyond, including agentic AI, the emergence of DeepSeek, and the evolving regulatory landscape.

As AI/ML capabilities evolve and the threats they enable grow, the imperative is clear, more sophisticated, strong security controls, zero trust architecture, and AI-powered defenses are no longer optional—they’re essential. Keep reading for more insights and actionable strategies to help your organization securely adopt AI while staying ahead of AI-driven threats.

---

## Key Findings

ThreatLabz analyzed 536.5 billion AI and ML transactions in the Zscaler cloud from February 2024–December 2024. The key findings that follow are based on data spanning varying time periods* for comparative analysis.

- **AI/ML tool usage saw an exponential rise year-over-year**, with 36x more transactions (+3,464.6%) from 800+ AI/ML applications in the Zscaler cloud, highlighting the explosive growth in enterprise interest and dependence on these technologies.
- **Enterprises blocked 59.9% of all AI/ML transactions**, reflecting concerns around AI data security and the steps companies are taking in shaping their approaches to AI governance.
- **ChatGPT remains the top application by transaction volume**, accounting for nearly half of all AI/ML transactions (45.2%) from known applications, despite ongoing debates over its security implications.
- **ChatGPT is also the most-blocked AI application** among known applications, followed by Grammarly, Microsoft Copilot, QuillBot, and Wordtune, reinforcing growing interest and caution when it comes to AI-powered writing and productivity assistants in enterprise settings.
- **Enterprises are sending significant volumes of data to AI tools**, with a total of 3624 TB transferred by AI/ML applications.
- **The Finance & Insurance and Manufacturing industries generate the most AI/ML traffic**, with 28.4% and 21.6% share of all AI/ML transactions in the Zscaler cloud, respectively, followed by Services (18.5%), Technology (10.1%), Healthcare (9.6%), and Government (4.2%), showing that AI adoption varies significantly across industries.
- **The top 5 countries generating the most AI/ML transactions** are the United States, India, United Kingdom, Germany, and Japan.
- **AI continues to amplify cyber risks**, fueled by advancements in deepfake technology, emerging open source AI models, and autonomous attack automation—undoubtedly making threats more adaptive, targeted, and difficult to detect.

*\* Time period variations:*
* *“Year-over-year” percentage changes compare data from April–December 2024 and the same period in 2023.*
* *Country- and region-specific findings are based on data collected between July–December 2024.*
* *The Zscaler Zero Trust Exchange tracks ChatGPT transactions independently from other OpenAI transactions at large.*

---

## AI and ML Usage Trends

![Graph showing AI transactions from February 2024–December 2024, showing a steady climb from 3.7 billion to 49 billion, with a peak in July.]

AI/ML tool usage surged globally in 2024, with enterprises integrating AI into operations and employees embedding it in daily workflows. Zscaler tracked more than 800 AI/ML applications in the Zscaler cloud, a considerably higher number compared to the previous analysis period in 2023, reflecting the expanding enterprise adoption and reliance on AI-powered tools.

### AI/ML transactions overview

Growing security risks haven’t slowed the exponential rise in AI and ML transactions. From February through December 2024, transaction volumes surged from 3.7 billion to 49 billion, marking a twelvefold increase. AI/ML activity peaked in July, reaching 82.7 billion transactions.

The scale of AI/ML activity increased dramatically to 536.5 billion total AI/ML transactions—a 3,464.6% year-over-year surge compared to our last analysis period. A significant portion of this AI/ML traffic comes from widely used applications such as ChatGPT, Grammarly, Microsoft Copilot, and other AI/ML tools. However, a large share of the transactions (53.1%) remain categorized as “General AI Applications” within the Zscaler cloud, underscoring the rapid proliferation of AI use across enterprises. This classification reflects AI/ML transactions that do not yet belong to defined AI applications but are nonetheless detected as AI/ML traffic via Zscaler’s AI/ML-powered URL categorization, which can analyze text, images, and other content to identify AI-related activity.

![Chart showing share of total transactions: Classified AI Applications (46.9%) vs. General AI Applications (53.1%).]

---

## Enterprise AI Risks and Real-World Threat Scenarios

### Core risks of enterprise AI adoption

Bringing AI into your organization brings a mix of opportunities and risks, many of which are still evolving. AI-powered systems create new attack surfaces, and GenAI and LLMs are especially vulnerable to threats that can manipulate AI outputs, introduce bias, or leak sensitive information. These are some of the biggest risks enterprises must address.

- **Data quality issues (“garbage in, garbage out”)**: The integrity of AI outputs depends on the quality of input data. Poor-quality inputs, outdated information, or biased training data can result in flawed or misleading outputs, which can ultimately adversely affect business decisions and security.
- **Exposure of IP and non-public information**: AI applications often process business-critical and sensitive information like proprietary research and internal algorithms. If this data is input into third-party AI models without strict safeguards, it may be retained, repurposed, or even exposed, leading to intellectual property theft.
- **Data privacy and security risks**: AI tools handle a lot of sensitive data, so it’s crucial to know where that data goes. Some AI models store inputs for training, use them for advertising, or even share them with third parties, leading to privacy concerns and compliance issues (e.g., GDPR, HIPAA).

---

## DeepSeek and open-source AI: the risk of frontier models in your pocket

The AI race is heating up in 2025 with China’s DeepSeek, an open source LLM, challenging the likes of leading American AI companies OpenAI, Anthropic, and Meta while disrupting AI development strategies and the roadmap for foundational models as we knew it. In short: DeepSeek is open source (or open-weight), performs relatively well compared to state-of-the-art models, and is extremely price-competitive.

### The new economics of AI

In general, the competitive pressures from both private and open source AI builders are commoditizing AI intelligence—driving down the costs for end users, even as AI models become more capable. Moreover, DeepSeek specifically may have offered a model to drive down the costs of training AI models for builders.

DeepSeek has disrupted this structure by dramatically lowering the cost of training and deploying base LLMs, making it possible for a much larger pool of players to enter the AI space. This shift effectively democratizes AI—and also raises inevitable security, privacy, and data sovereignty concerns.

---

## 5 prompts to deception: DeepSeek-generated phishing page

The following scenario explores how a threat actor could use DeepSeek to generate a phishing page resembling Microsoft’s Live.com login page, iteratively improving the page using five simple prompts.

1. **Generating a basic login page**: User prompt: “Can you generate HTML code for a login page?”
2. **Mimicking a legitimate login interface**: User prompt: “Can you create it similar to live.com login page?”
3. **Adding realistic authentication flow**: User prompt: “Live.com first asks for a username and then asks for a password. Could you add the same functionality?”
4. **Enhancing branding and UI elements**: User prompt: “Make the login box more of a square and add an Outlook image just above the login box”
5. **Implementing client-side cloaking**: User prompt: “Could you incorporate client side cloaking that checks for user agent, browser fingerprinting, IP checks, and behavior patterns?”

DeepSeek integrates client-side cloaking—a widely used technique that allows attackers to hide the phishing page from detection by security vendors. This final refinement further improves the page’s stealth and effectiveness.

---

## AI’s growing role in cyberthreats

Over the past year, the integration of AI into cybercrime has fundamentally changed the threat landscape. Cybercriminals are weaponizing AI to launch more sophisticated and deceptive attacks, from AI-powered social engineering to advanced model manipulation.

### Supercharged social engineering

Deepfake technology is only becoming more convincing. New on the scene as of February 2025, AI model OmniHuman-1 can generate hyper-realistic human videos from a single photo, with fluid lip-syncing and real-time voice adaptation.

Advancements in voice cloning technology will also inevitably fuel a surge in vishing (voice phishing) attacks. Attackers can now replicate a voice with mere seconds of recorded audio, allowing them to adapt quickly and respond in real time.

### AI-driven malware and ransomware across the attack chain

AI has taken much of the heavy lifting off ransomware operators, enabling them to automate and optimize attacks across every stage of the attack chain. Malware threat actors are leveraging AI tools to scan networks for vulnerabilities, generate exploits tailored to specific configurations, and facilitate the rapid spread of ransomware within compromised environments.

The real evolving threat isn’t just automation at this point—it’s AI’s ability to continuously adapt. AI-generated polymorphic malware can dynamically rewrite its code and execution patterns to evade detection, while adversarial AI models analyze security responses in real time.

---

## Agentic AI: the next frontier in autonomous AI—and attack vectors

AI agents, or “agentic AI,” also serve as new attack vectors and an offensive tool for threat actors. These autonomous AI systems can carry out complex, multistep tasks with minimal human input, and they could introduce a new level of sophistication and deception to social engineering. For example, agents could autonomously analyze vast amounts of social media data and generate tailored messages that closely mimic legitimate communications. This automation enables larger-scale deployment of phishing attacks with little human oversight.

---

## Case study: How threat actors are exploiting interest in AI

[Image description: A case study analysis of how threat actors create fake AI platforms to lure users into downloading malware or providing credentials.]

---

## The Evolving Scope of AI Regulations

[Content regarding the global regulatory landscape for AI, including GDPR and emerging national strategies.]

---

## AI Threat Predictions for 2025-2026

[Content regarding future outlooks on AI-driven threats, including increased autonomous attacks and sophisticated deepfake campaigns.]

---

## Best Practices for Secure Enterprise AI Adoption

### 5 steps to securely integrate GenAI tools

1. **Visibility**: Implement full visibility into AI/ML tools in use.
2. **Granular Access**: Enforce granular access controls for approved AI tools.
3. **Data Security**: Evaluate data retention and third-party sharing policies of AI providers.
4. **DLP Enforcement**: Enable Data Loss Prevention (DLP) to prevent sensitive data leakage.
5. **Logging**: Maintain detailed logs of AI interactions for compliance and security auditing.

---

## How Zscaler Delivers Zero Trust + AI

### Under the hood: Zscaler’s AI security and data advantage

Zscaler’s AI/ML-powered URL categorization analyzes text, images, and other content to identify AI-related activity, providing enterprises with the visibility needed to manage shadow AI and secure their environments.

### A comprehensive approach to AI security

[Content regarding Zscaler's Zero Trust Exchange architecture and its role in securing AI-driven enterprise environments.]

### Leveraging AI security across the attack chain

[Content regarding how Zscaler uses AI to defend against AI-driven threats at every stage of the attack chain, from reconnaissance to data exfiltration.]

---

## Research Methodology

ThreatLabz analyzed 536.5 billion AI and ML transactions in the Zscaler cloud from February 2024–December 2024. The findings are based on data spanning varying time periods for comparative analysis.

## About ThreatLabz

ThreatLabz is the security research arm of Zscaler. The team is responsible for analyzing and tracking threats across the Zscaler Zero Trust Exchange, providing actionable intelligence to protect organizations worldwide.

## About Zscaler

Zscaler (NASDAQ: ZS) accelerates digital transformation by making customers more agile, efficient, resilient, and secure. The Zscaler Zero Trust Exchange protects thousands of customers from cyberattacks and data loss by securely connecting users, devices, and applications in any location.

---

controller
GenAI discovery of attack AI-generated polymorphic malware Escalate privilege Steal data and deploy
surface: vulnerabilities for AI-driven phishing and vishing attacks & identify AI-powered exfiltration
exposed assets (e.g.,VPNs) crown-jewels modules (likely emergent)
Figure 15: How attackers can use AI across the ransomware attack chain
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 30

Agentic AI: the next frontier in autonomous AI—and attack vectors
Agentic AI is poised to make a significant from scratch using popular agentic AI tools,
impact on the cybersecurity landscape. Unlike even among non-developers.
traditional AI models that require human
oversight, agentic AI makes its own decisions, While AI agents will undoubtedly drive
learns from its environments, and executes innovation, their capabilities also introduce new
complex tasks. For instance, it has become attack vectors and security risks.
trivial to build and deploy simple applications
WHAT IS AGENTIC AI?
Agentic AI is a type of AI that acts autonomously, making decisions, analyzing its environment,
and adapting its actions to achieve specific goals—all with little to no human oversight.
KEY CAPABILITIES:
• Operates independently and adapts in real time
• Makes decisions and takes actions
• Executes complex, multistep tasks with minimal supervision
• More advanced than chatbots or smart assistants
• Can be leveraged for both innovation and cyberthreats
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 31

THE SECURITY IMPLICATIONS OF AGENTIC AI
The growing autonomy of AI systems suggests that security teams will
face numerous challenges and risks, emerging in both enterprise adoption
of AI agents and their use by attackers.
Risky unpredictability Diminished human oversight Shadow AI deployments Exploitation by threat actors
Agentic AI systems operate with a By design, agentic AI operates As mentioned above, the ease of Agentic AI systems are particularly
degree of autonomy that can make independently of human intervention, building and deploying AI agents will susceptible to manipulation by malicious
their decision-making processes which inherently reduces human control lead to more shadow AI deployments actors. Threat actors can exploit
opaque to security teams. This over critical operations. As a result, these within enterprises. Unapproved vulnerabilities in these agents through
unpredictability can hinder the ability AI agents could make unauthorized or AI agents can introduce unknown methods such as prompt injection
to catch errors, detect attacks, unintended decisions, such as exposing vulnerabilities, process sensitive data attacks, adversarial inputs, or data
or reverse harmful actions in a sensitive information or disrupting insecurely, or make autonomous poisoning, effectively hijacking their
timely manner. normal workflows. Without robust decisions that conflict with decision-making processes. Worse,
governance and enforced checks, corporate policies. attackers could deploy their own
such actions could lead to cascading agentic AI systems to execute advanced
organizational vulnerabilities. threat campaigns.
Addressing these risks will require not only advanced monitoring and strict AI guardrails, but also innovative approaches
to ensure that agentic AI systems act within well-defined boundaries and remain resilient to exploitation.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 32

Case study: How threat actors are
exploiting interest in AI
Cybercriminals aren’t just using AI to supercharge attacks—they’re exploiting the global fascination
with it. Zscaler ThreatLabz has been monitoring malware campaigns that prey on users’ interest in AI
tools. In a recent investigation, ThreatLabz uncovered a campaign where threat actors established a
fake AI company as a lure to facilitate malware distribution.
Fake AI, real malware threat
According to their website, “Flora AI is a comprehensive AI platform that provides content
generation, analytics, and automation tools for businesses and developers.” The website claims
that Flora AI offers a range of AI tools that can be integrated with multiple programming
languages. To enhance its professional appearance, the website includes sections such as “Careers,”
“Documentation,” and “Blog.” The blog posts on AI were all published in December 2024.
The website also mentions that Flora AI supports integration with Python and Node.js, providing
examples of installation using PIP or NPM and demonstrating usage with these languages. When
users try to sign in via Android or Linux devices, the website shows an error message saying
“Unsupported device,” and asks them to switch to a Windows or Chromium-based browser.
KEY TAKEAWAYS
• Threat actors created a fake AI company called “Flora AI,” complete with a
professionally designed website that claims to be a robust platform offering AI tools,
registered in November 2024.
• The threat actors employed various techniques to deliver the Rhadamanthys infostealer
to victims’ systems through open directories.
• Attackers continuously modified the malware and its delivery methods while also
engaging in communication with victims prior to launching the attack.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 33

Attack chain
The attack chain begins with threat actors enticing users to collaborate Documents folder. The LNK file subsequently executes the VBS file, which This campaign demonstrates the
in exchange for payment. Users are instructed to log in to the fraudulent places a PowerShell script in the %USERNAME%\Documents folder and growing sophistication of cyber threats.
Flora AI website using a “Key Identifier” provided by the attackers. Once runs it using a WScript.Shell object. By crafting a fake AI platform and
logged in with the “Key Identifier,” users are asked to verify their account employing deceptive methods, threat
by signing a PDF contract. However, the PDF is actually a malicious LNK The PowerShell script downloads both a decoy PDF file and the actors effectively executed their malicious
file disguised as a legitimate PDF. Rhadamanthys infostealer loader via the Invoke-WebRequest cmdlet and payloads, while leveraging file-based
executes them. Additionally, the script unmaps the network drive and evasion strategies to avoid detection—
Exploiting the "search-ms" URI protocol, the threat actors open a remote removes the VBS file and the PowerShell script from the Documents folder underscoring the need for security
LNK file location in Windows Explorer, tricking users into executing the to reduce traces of the attack. solutions to adapt to advanced, multi-
malicious LNK file under the assumption that it is a legitimate PDF. layered attack methods.
In later versions of the LNK file, the attackers bypassed the use of the VBS
Upon execution, the LNK file runs the “net use” command to map a file and directly downloaded the PowerShell file instead.
network drive linked to an open directory hosted by the attackers. It then
uses the copy command to transfer a VBS file to the %USERNAME%\ Figure 16 illustrates the entire attack chain.
FloraAIVerificationAgreement.pdf
Downloads and
execute from
open directory
Photo
The threat The user lands on The website opens The LNK file VBS file downloads
actors provide fraudulent website in Explorer LNK download the and executes
Key Identifier to sign in using file disguised as VBS file the PowerShell
to User Key Identifier PDF hosted on open Script
directory
GaSir.exe
(Rhadamanthys Infostealer)
Figure 16: “Flora AI” attack chain
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 34

The Evolving Scope_
of AI Regulations
As AI continues to reshape industries and everyday life, governments worldwide are stepping up efforts to regulate
its use to balance innovation, security, and ethical concerns. Over the past year, Europe and the US have taken
major steps toward AI governance, with a growing focus on risk management, transparency, and safety.
Europe takes the lead with the AI Act AI policy in the US: still a work in progress
In August 2024, the European Union (EU) passed the Artificial Intelligence As of February 2025, the US has yet to establish a clear regulatory
Act11, making history as the first comprehensive legal framework for framework for AI. No federal laws currently govern or restrict
the regulation of AI systems across the EU. Instead of a one-size-fits- AI development.
all approach, the act classifies AI systems by risk level—ranging from
unacceptable (banned outright) to high-risk (heavily regulated), down to On January 20, 2025, the new presidential administration rescinded
limited and minimal-risk AI (fewer restrictions). Executive Order 14110, requiring AI companies working on high-impact
models to report their training and safety measures. The next day, they
For example, AI used in biometric surveillance, credit scoring, or hiring announced the Stargate Project12, a $500 billion joint venture involving
decisions falls into the high-risk category, meaning companies must OpenAI, SoftBank, Oracle, and MGX, aimed at building AI infrastructure
follow strict guidelines around transparency, oversight, and compliance across the US.
with EU laws. GenAI models like ChatGPT and Midjourney also face new
transparency rules, requiring them to disclose training data sources and
adhere to copyright laws.
The AI Act should pave the way for a more transparent, ethical, and
accountable AI ecosystem.
11 Future of Life Institute, The EU Artificial Intelligence Act, accessed February 28 2025.
12 Observer, Trump’s $500B Stargate A.I. Project: What Will It Build and Does It Actually Have the Money?, January 24, 2025.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 35

What’s next? A critical crossroads for AI regulation
International AI security efforts
AI governance is a global imperative, and encouragingly, worldwide The past year has marked a turning point for AI regulation. Governments
governments and industry leaders are strengthening their collaboration to are realizing that AI left unchecked could become a major security risk.
develop safety standards that support innovation and security. The question isn’t whether AI should be regulated—it’s how to do it right
without thwarting innovation.
In May 2024, the AI Seoul Summit brought together 16 major AI
companies from Asia, Europe, the US, and the Middle East to sign the Going forward, the key to AI security will be well-balanced regulations,
Frontier AI Safety Commitments.13 These agreements focus on stronger global collaboration, and proactive risk management. International
risk management, accountability, and safeguards for advanced AI models. cooperation will become essential as AI systems grow more powerful and
cross-border concerns—like deepfakes, misinformation, and AI-fueled
In September 2024, the EU, UK, and US joined forces to sign the threats—become harder to ignore.
Framework Convention of International Intelligence14—a legally binding
treaty ensuring AI development aligns with human rights, democracy, and
ethical standards.
In November 2024, the International Network of AI Safety Institutes held
its first meeting in San Francisco.15 Representatives from nine countries and
the European Commission gathered to collaborate on AI safety research,
set evaluation standards, and develop best practices for responsible
AI development.
13 Infosecurity Magazine, AI Seoul Summit: 16 AI Companies Sign Frontier AI Safety Commitments, May 21, 2025.
14 Council of Europe, The Framework Convention on Artificial Intelligence, accessed February 28, 2025.
15 TIME, U.S. Gathers Global Group to Tackle AI Safety Amid Growing National Security Concerns, November 21, 2024.
TThhrreeaattLLaabbzz 22002255 AAII SSeeccuurriittyy RReeppoorrtt ©2025 Zscaler, Inc. All rights reserved. 36

AI Threat Predictions_
for 2025–2026
1. AI-powered social engineering will 3. Attackers will take advantage of
reach new highs interest in AI via fake services
and platforms
GenAI will elevate social engineering attacks to new levels in 2025 and beyond, particularly in voice and video phishing.
With the rise of GenAI-based tooling, initial access broker groups will increasingly use AI-generated voices and video As enterprises and end users rapidly adopt AI, threat actors will
in combination with traditional channels. As cybercriminals adopt localized languages, accents, and dialects to increase increasingly capitalize on AI trust and interest through fake services
their credibility and success rates, it will become harder for victims to identify fraudulent communication. This trajectory and tools designed to facilitate malware, steal credentials, and
of AI-powered social engineering attacks signals a fundamental shift in the threat landscape where deception is more exploit sensitive data. ThreatLabz has already uncovered a case
sophisticated than ever before. The implications are serious: identity compromise will be more prevalent, ransomware in which attackers created a fraudulent AI platform to deliver the
campaigns will become more complex, and attackers will develop more evasive data exfiltration techniques. Rhadamanthys infostealer to victims’ computers. Such deceptive
tactics will keep advancing, even leveraging AI-generated
interactions, for example, to appear legitimate while covertly
compromising systems. This trend also reinforces the rising
2. The rise of autonomous AI agents will expose enterprises to
dangers of shadow AI, where employees unknowingly engage with
significant data risks and security challenges
unauthorized AI tools (whether real or fake), putting enterprise
data and security at risk. Organizations must educate users on the
Autonomous AI agents, or “agentic AI,” are set to transform enterprise operations with abilities like self-directed decision- dangers of shadow AI, enforce AI governance policies, and monitor
making, executing multistep tasks, and autonomously interacting with APIs. While these capabilities can certainly enhance unauthorized AI tool usage.
operational efficiency, unchecked AI autonomy will likely introduce exploitable vulnerabilities that expose enterprises to
significant data risks and new security threats. Threat actors could use specialized AI agents to map attack surfaces, launch
hyper-personalized phishing scams, or manipulate data, making attacks more scalable, adaptive, and difficult to detect.
Enterprises must fortify AI security with real-time monitoring and AI-specific access controls to ensure these agents
operate within secure, predefined parameters.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 37

4. The AI builder boom will open the floodgates 6. Securing GenAI will be a priority business
for cybercriminal innovation imperative
With more players entering the LLM development space, the explosion of open source AI As GenAI applications become more embedded in enterprise operations, securing these
models like DeepSeek and Grok will create new attack surfaces and opportunities for threat systems will transition from an IT priority to a core enterprise security imperative in 2025
actors. Open source AI gives cybercriminals unrestricted access to fine-tune models for and beyond. GenAI has the ability to continuously learn and adapt, making security a moving
offensive operations. In 2025, threat actors will combine AI jailbreaks, prompt injection attacks, target. Threat actors are already finding ways to exploit AI-driven automation, manipulate
and customized LLMs to create tailored attack strategies. The rise of rogue AI models trained AI-generated content, and introduce subtle model biases that could compromise enterprise
specifically for cybercrime will enable even low-skilled attackers to deploy more sophisticated decision-making. Organizations will need to double down on implementing effective security
AI-driven attacks. Security teams must move beyond traditional defenses, standardizing zero controls to safeguard AI models, protect sensitive data pools, and ensure the integrity of AI-
trust security frameworks and stricter governance to counter adversaries weaponizing the open generated content.
AI ecosystems.
5. Deepfakes will become a massive fraud vector
across industries
Deepfake technology will fuel a new wave of fraud, extending beyond manipulated public
figure videos to more sophisticated scams. Fraudsters are already using AI-generated content
to create fake ID cards, fabricate accident images for fraudulent insurance claims, and even
produce counterfeit X-rays to exploit healthcare systems. As deepfake tools become more
advanced and accessible—and their outputs more convincing—fraud will be harder to detect,
undermining identity verification and trust in communications. Industries handling identity
authentication, financial transactions, and sensitive data will be most impacted by deepfake-
driven fraud and its risks, making AI-powered detection and defense an urgent necessity.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 3388

Best_ The following best practices provide a foundation for secure AI adoption.
Practices
Maintain AI transparency and accountability. Clearly Continuously assess and mitigate AI risks. Regularly evaluate AI-
communicate the purpose of AI tools and document related security and privacy risks—and user behavior—to protect
for Secure AI processes while assigning oversight roles for company information, intellectual property, and personal data.
responsible governance.
Apply zero trust to AI interactions. Adopt a zero trust architecture
Enterprise
Adhere to legal and ethical standards. Ensure compliance that enforces least-privileged access and granular input/output
with privacy laws, data protection regulations, and ethical restrictions to prevent unauthorized usage and minimize the
AI Adoption guidelines relevant to AI use. attack surface.
Review and adjust default settings. Audit permissions and Strengthen data privacy and security. Implement encryption and
modify default configuration settings, which usually prioritize full-spectrum data loss prevention (DLP) measures to secure data
AI offers powerful advantages but also efficiency over security, to reduce vulnerabilities and minimize and protect proprietary information from exposure and leaks.
introduces serious security risks, as discussed in potential risks.
the previous sections. Successfully integrating
AI/ML tools into enterprise operations requires
a strategic approach. Organizations must follow
best practices and implement clear policies
that prioritize security, ensure compliance, and Beyond best practices, enterprises should establish formal AI guidelines and rules of engagement to govern acceptable use, integration, security, and
promote ethical use. development of AI tools.
Establish clear AI governance policies. Define guidelines for Mandate human review for AI-generated content. Ensure
responsible AI use, addressing security, ethics, compliance, all AI-assisted content undergoes thorough human review
and risk management. before publication.
Perform due diligence before implementation. Conduct Ensure human oversight in AI-driven processes. Require human
comprehensive security and ethical reviews to ensure tools intervention and review to prevent AI from making autonomous
align with corporate policies and risk tolerance. critical business decisions.
Restrict sensitive data sharing. Prevent AI models from Adopt a Secure Product Lifecycle framework. Follow a rigorous
accessing personally identifiable information (PII), proprietary security framework to mitigate risks at every stage of AI tool
data, or confidential business information. development and integration.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 39

5 steps to securely integrate GenAI tools
A strategic, phased approach is essential to securely adopting AI applications. The safest starting point is to block all AI applications to mitigate potential
data leakage. Then, progressively integrate vetted AI tools with strict access controls and security measures to maintain full oversight of enterprise data.
The following steps outline a secure adoption process using OpenAI’s ChatGPT as an example.
Step 1. Block all AI Step 2. Vet and approve Step 3. Create a private
and ML domains generative AI ChatGPT server instance for
and applications applications with maximum control
stringent criteria
With thousands of AI applications
available—many with unknown security
Next, identify and approve AI tools that To maintain full control over enterprise data, organizations should host AI applications such as
implications—enterprises should adopt
meet (or exceed) strict security, privacy, ChatGPT in a private and secure environment (for example, a dedicated Microsoft Azure AI
a zero trust stance from the start. By
and contractual standards to protect server) hosted fully within the organization. Then, through security controls and contractual
blocking all AI and ML domains at
business and customer data at all times obligations, ensure that neither Microsoft nor OpenAI (in this example) has access to enterprise
the enterprise level, organizations can
while offering transformative business or customer data. This approach ensures data sovereignty and prevents AI vendors from
eliminate immediate risks and focus on
value. For many organizations, ChatGPT handling sensitive data, thus preventing queries from being used to train public AI models, and
selectively adopting only the most secure
will be a key application that requires reduces the risk of data poisoning from a public data lake.
and transformative AI tools.
additional security considerations.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 40

Step 4. Secure access with SSO, MFA, and zero
trust controls
Next, place applications like ChatGPT behind a zero trust cloud proxy architecture, such as the
Zscaler Zero Trust Exchange, to enforce zero trust security access controls. This might also
include moving ChatGPT behind an identity provider (IdP) for single sign-on (SSO) with strong
multifactor authentication (MFA) that includes biometric authentication. This approach ensures
fast but secure user access to ChatGPT while allowing enterprises to set precise access controls
for individual users, teams, and departments. It also maintains a clear separation of concerns
between user queries, ensuring that data remains isolated and only accessible within the
appropriate organizational levels. By putting ChatGPT behind a cloud proxy like the Zero Trust
Exchange, organizations can monitor and inspect all TLS/SSL-encrypted traffic between users
and ChatGPT to detect potential threats and prevent data leaks.
Step 5. Implement data loss prevention (DLP) to
prevent leakage
Lastly, it’s critical to enforce a DLP engine for the ChatGPT instance to prevent
accidental leakage of critical information and ensure sensitive data never leaves the
production environment.
By following these steps, enterprises can harness the power of generative AI while eliminating
the most critical risks associated with AI adoption.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 41

Under the hood: Zscaler’s AI
How Zscaler Delivers
security and data advantage
Zero Trust + AI_
AI is only as smart as the data it learns from. As the world’s largest inline
security cloud, the Zscaler Zero Trust Exchange secures 40M+ users,
workloads, IoT/OT devices, and third-party access.
As AI adoption grows, organizations are Zscaler’s cloud-based zero trust architecture
unlocking new levels of productivity, efficiency, drastically reduces risk by making applications Every day, Zscaler processes:
and innovation—but also expanding their and IP addresses invisible to attackers, thus
attack surface. At the same time, the rise of minimizing the attack surface; continuously 500T+ telemetry signals, providing real-time insights into threats,
weaponized AI means more sophisticated, inspecting all traffic—including encrypted identities, and access patterns
automated, and evasive threats. Enterprises traffic—for threats, preventing compromise;
must recognize these risks and enhance and connecting users directly (and only) to the 500B+ transactions—45x the volume of daily Google searches
security strategies in order to address them. applications they need, thereby limiting lateral
movement risk. This massive dataset allows Zscaler to train highly specialized AI models
Traditional security models are inadequate in that identify and block threats more quickly than traditional security
these high-stakes environments. Their legacy Building on this foundation, Zscaler enhances approaches, amounting to more than 9 billion blocked threats daily.
architectures, rooted in tools like firewalls and zero trust with AI-powered threat protections Sitting inline between users, workloads, and devices, Zscaler has deep
VPNs, actually increase risk by expanding the to deliver unparalleled security against threats visibility into enterprise cyberthreats, making its AI models more adaptive,
attack surface and enabling lateral movement, of all kinds, even the most sophisticated precise, and effective.
allowing AI-powered attacks to spread faster. AI-enabled attacks.
These outdated solutions require too much The Zscaler data fabric also seamlessly integrates with 150+ security and
manual effort, making it nearly impossible to business tools, including 60+ threat intelligence feeds.
secure communications, adapt to evolving risks,
and respond to threats in real time.
To thrive in the AI era, enterprises need a
fundamentally new approach—one that not
only defends against AI-powered threats but
also enables secure AI adoption. A zero trust
architecture is the foundation for both.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 42

A comprehensive approach to
AI security
Successfully integrating AI into the enterprise and defending against AI-
powered threats requires a comprehensive strategy. With Zscaler Zero Trust +
AI, enterprises can confidently and securely embrace public and private AI while
protecting data, applications, and AI models from  evolving AI-driven threats.
By offering full visibility into users and applications interacting with both public
Threat Opportunity
lation • AI Guardr
and private AI tools, Zscaler AI enables enterprises to deploy contextual policies
s o a
I i l
  s
I
that govern access and usage. Its inline inspection of prompts ensures protection  A •
|     |     |     |     |
| --- | --- | --- | --- |
|     | • A |     |     |
|     |   I |     |     |
of sensitive data and the AI models themselves against malicious activity and  y

|     | t   | A   |     |
| --- | --- | --- | --- |
|     | i   | u   |     |
l
data loss. d
|     | i   | i   |     |
| --- | --- | --- | --- |
|     | b   | t   |     |
i

|     | s   | T   |     |
| --- | --- | --- | --- |
i
r
|     | V   | a   |     |
| --- | --- | --- | --- |

i
|     | I   | l   |     |
| --- | --- | --- | --- |
A

| AI-Powered Attacks |     |     | Companies Embracing |
| ------------------ | --- | --- | ------------------- |
Zscaler AI
|     | A   | l   |     |
| --- | --- | --- | --- |
I
| and AI Attack Surfaces |     | o   | Public and Private AI |
| ---------------------- | --- | --- | --------------------- |
r
|     | D   | t   |     |
| --- | --- | --- | --- |
a
|     | t   | n   |     |
| --- | --- | --- | --- |
o
|     | a   | C   |     |
| --- | --- | --- | --- |
|     |     |     |     |
P
|     | r y |     |     |
| --- | --- | --- | --- |
|     | o c |     |     |
|     | t i |     |     |
e l
c o
t P
i e
o n g
 • Granular AI Usa
“We had no visibility into [ChatGPT]. Zscaler
was our key solution initially to help us
understand who was going to it and what they
were uploading.”

- Jason Koler, CISO, Eaton Corporation
See the video case study
43
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved.

Zscaler AI empowers organizations to:
Securely enable public AI usage, maximizing business velocity while minimizing Stop AI-powered attacks through zero trust + AI-powered security.
the risks of shadow AI and data loss.
• Zero trust foundation: Minimize the external attack surface via continuous verification and
• AI visibility: See all AI applications and interactions, including prompts least-privilege access.
and responses.
• Real-time AI insights: Employ predictive and generative AI to deliver actionable insights that
• AI isolation: Allow usage of AI tools while preventing sensitive data from enhance security operations and digital performance.
being inadvertently shared.
• Data classification: Leverage AI-driven classification to seamlessly detect and safeguard
• AI guardrails: Block threats such as prompt injections, PII exposure, data sensitive data across Zscaler’s Data Fabric.
poisoning, and more.
• Threat protection: Block AI-enhanced threats through continuous monitoring and response
• Granular AI usage policy control: Block unauthorized or shadow AI apps powered by the Zscaler Zero Trust Exchange.
and control access and usage based on who is using AI and how.
• App segmentation: Reduce your internal attack surface and restrict lateral movement with
• AI data protection: Block sharing and exfiltration of data to prevent automatic, AI-driven segmentation.
data breaches.
• Breach prediction: Preempt potential breach scenarios using generative AI and multi-
• AI audit trail: Maintain detailed logs of all AI interactions: users, prompts, dimensional predictive models.
responses, and apps.
• Cyber risk assessments: Leverage AI-generated security reports to map and optimize your zero
trust implementation.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 44

Key AI-powered capabilities from Zscaler include:
• Phishing and C2 detection: Instantly identifies and blocks never-before-seen phishing sites and command-
and-control (C2) infrastructure using inline AI-based detection from the Zscaler Secure Web Gateway.
• Smart input prompt blocking: Uses AI/ML-driven URL filtering across categories of apps for smarter prompt
blocking decisions based on contextual risk.
• Sandboxing: Issues instant verdicts on potential threats, preventing zero-day malware and ransomware before
they can impact users or endpoints.
• Zero Trust Browser: Isolates suspicious internet content and renders web pages as picture-perfect images,
keeping malicious content away from users.
• Segmentation: Automatically maps user-to-application connections, simplifying zero trust access policies to
minimize attack surface and stop lateral movement.
• Dynamic, risk-based policies: Continuously analyzes user, device, and application risk to enforce adaptive
security policies.
• Breach Predictor: Leverages AI-powered algorithms to analyze security data, using attack graphs, user risk
scoring, and threat intelligence to predict potential breaches.
• Security maturity assessments: Continuously assesses zero trust security posture, providing dynamic insights
and actionable recommendations to further reduce cyber risk.
• Data protection: Delivers AI-powered auto data discovery and classification across endpoint, inline, and cloud
data. AI-driven data loss prevention (DLP) controls ensure that sensitive enterprise data cannot be extracted via
AI input prompts.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 45

Leveraging AI security across
the attack chain
Zscaler applies AI at every stage of the attack chain, ensuring threats are detected and neutralized
before they can cause harm.
Stage 1: Attack surface discovery Stage 2: Risk of compromise
The first step of an attack is often reconnaissance—scanning the internet for vulnerabilities in VPNs, Once attackers find a weakness, they attempt to exploit vulnerabilities, steal credentials, or gain
firewalls, misconfigured servers, or unpatched assets. AI has made this process easier for threat unauthorized access. The growing use of AI-generated exploits and phishing emails further increases
actors, enabling them to query known vulnerabilities almost instantly. the risk of compromise, enabling attackers to bypass traditional security controls and making real-
time detection and response essential.
How Zscaler uses AI to eliminate the attack surface:
How Zscaler uses AI to mitigate risk of compromise:
• With AI-driven insights from Zscaler Risk360, enterprises can automatically map and secure
their internet-facing assets, making them invisible to users. By hiding these assets behind the • Zscaler AI models draw on a combination of threat intelligence, ThreatLabz research, and
Zero Trust Exchange, organizations dramatically reduce their attack surface—stopping threats AI-based browser isolation to detect both known and patient-zero phishing sites, preventing
before they can even begin. credential theft and browser exploitation. They analyze traffic patterns, behavior, and malware
to identify command-and-control (C2) infrastructure in real time. As a result, enterprises are
even more efficient and effective in detecting C2 domains and phishing attacks.
• AI-powered Zscaler Zero Trust Browser automatically reduces the risk of web-based threats
and zero-day threats while ensuring employees can access the right sites to do their jobs.
AI Smart Isolation identifies suspicious internet content and opens it in a secure, isolated
environment. This effectively stops web-based threats like malware, ransomware, and phishing.
• Zscaler Cloud Sandbox automatically detects, prevents, and intelligently quarantines unknown
threats and suspicious files inline. With AI-based verdicts, benign files are delivered instantly
while malicious files are blocked for all Zscaler global users. This effectively stops web-based
threats like malware, ransomware, phishing, and drive-by downloads from gaining access
to a network.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 46

Stage 3: Lateral movement Stage 4: Data exfiltration
Once inside, attackers try to move laterally within an organization, seeking elevated privileges or The final stage of an attack is data exfiltration, where attackers attempt to steal data such as IP,
valuable data or applications. Increasingly, they use AI tools to quickly map out pathways for deeper customer information, or financial records.
compromise. Many enterprises also suffer from overprovisioned access rights, making it easier for
attackers to move across environments undetected. How Zscaler uses AI to stop data loss:
How Zscaler uses AI to prevent lateral movement: • AI-powered data discovery accelerates data visibility and automates real-time data
classification across the enterprise. Instantly enable data loss prevention (DLP) policies to stop
• Zscaler AI continuously analyzes user behavior and access patterns, recommending intelligent data from leaving the organization.
application segmentation policies to limit lateral movement. For example, if only 200 out of
30,000 employees need access to an application, Zscaler can automatically segment access to
just those users—cutting lateral movement risk by over 90%.
AI is a force of progress, disruption, and risk—pushing enterprise organizations to adapt at
Securing every turn. It will continue to unlock new efficiencies and innovation, but also introduce new
threats, from AI-powered cyberattacks to adversarial manipulation of models and data.
To securely harness AI’s full potential while mitigating its risks, enterprises must turn to
AI for 2025:
zero trust + AI.
A call to action_ AI security from Zscaler secures every stage of AI adoption—and ensures protection across
every stage of an attack. By taking a proactive approach, organizations can turn AI into a
competitive advantage, unlocking new possibilities while staying ahead of evolving threats.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 47

Research
About ThreatLabz
Methodology_
ThreatLabz is the security research arm of Zscaler. This world-class team is responsible
for hunting new threats and ensuring that the thousands of organizations using the global
Zscaler platform are always protected. In addition to malware research and behavioral
analysis, team members are involved in the research and development of new prototype
Findings are based on analysis of 536.5 billion total AI and ML transactions in modules for advanced threat protection on the Zscaler platform, and regularly conduct
the Zscaler cloud from February 2024 to December 2024. The Zscaler global internal security audits to ensure that Zscaler products and infrastructure meet security
security cloud processes more than 500 trillion daily signals and blocks 9 billion compliance standards. ThreatLabz regularly publishes in-depth analyses of new and
threats and policy violations per day, delivering more than 250,000 daily emerging threats on its portal, research.zscaler.com.
security updates.
About Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so that customers can be more
agile, efficient, resilient, and secure. The Zscaler Zero Trust Exchange™ protects thousands
of customers from cyberattacks and data loss by securely connecting users, devices, and
applications in any location. Distributed across more than 160 data centers globally, the
SASE–based Zero Trust Exchange is the world’s largest inline cloud security platform. To
learn more, visit www.zscaler.com.
ThreatLabz 2025 AI Security Report ©2025 Zscaler, Inc. All rights reserved. 48

Zero Trust Everywhere
© 2025 Zscaler, Inc. All rights reserved. Zscaler™ and other trademarks listed at zscaler.com/legal/trademarks
are either (i) registered trademarks or service marks or (ii) trademarks or service marks of Zscaler, Inc. in the
United States and/or other countries. Any other trademarks are the properties of their respective owners.