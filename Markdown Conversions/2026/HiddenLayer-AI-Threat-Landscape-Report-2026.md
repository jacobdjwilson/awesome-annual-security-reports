# 2026 AI Threat Landscape Report

Organization: HiddenLayer  
Report Title: AI-Threat-Landscape-Report  
Year: 2026  

## Table of Contents
- [Foreword](#foreword)
- [Security for AI Survey Insights at a Glance](#security-for-ai-survey-insights-at-a-glance)
- [AI Threat Landscape Timeline](#ai-threat-landscape-timeline)
- [What’s New in AI](#whats-new-in-ai)
- [Part 1: Risks Posed by Artificial Intelligence](#part-1-risks-posed-by-artificial-intelligence)
  - [Risks to Society](#risks-to-society)
  - [AI-Powered Cybercrime](#ai-powered-cybercrime)
- [Part 2: Risks Faced by AI-Based Systems](#part-2-risks-faced-by-ai-based-systems)
  - [Attacks on Model Foundations](#attacks-on-model-foundations)

---

## FOREWORD

We are entering the next phase of the AI revolution. What began as predictive models and generative interfaces is rapidly evolving into autonomous, agentic systems capable of planning, reasoning, and acting on our behalf. In 2026, no mission, enterprise, or government agency will remain untouched by AI agents operating across workflows, networks, and critical infrastructure.

Agentic AI represents a profound leap forward. These systems are no longer limited to responding to prompts. They can set goals, call tools, interact with other systems, generate code, initiate transactions, and adapt dynamically to changing environments. Properly harnessed, they promise unprecedented operational efficiency, accelerated innovation, and entirely new models of productivity.

But autonomy changes the risk equation.

When AI systems are empowered to take action, the attack surface expands dramatically. The same capabilities that enable agents to automate business processes can be manipulated to automate exploitation. The same reasoning loops that drive efficiency can be redirected toward malicious objectives. As AI gains agency, adversaries gain leverage.

Make no mistake, the defining AI security challenge of this era is not hypothetical superintelligence. It is the weaponization, manipulation, and compromise of autonomous systems by bad actors.

Agentic architectures introduce new layers of vulnerability, including tool poisoning, memory manipulation, model context hijacking, multi-agent collusion, identity abuse, data exfiltration via action chains, and the exploitation of decision-making loops. These risks are not theoretical. They are emerging now across commercial enterprises and federal environments, experimenting with AI-driven automation.

Traditional cybersecurity principles remain essential, but they are no longer sufficient on their own. Securing agentic AI demands continuous validation of model behavior, real-time inspection of agent actions, guardrails around tool access, and controls that account for systems capable of independent execution. The convergence of AI security and application security has never been more urgent.

In this year’s report, we examine how the rise of agentic AI is reshaping the threat landscape. We detail the novel attack patterns targeting autonomous systems and analyze how adversaries are adapting proven tactics to exploit AI-driven workflows. We share findings from security and AI leaders deploying agents in production environments, along with data-driven insights from our work securing enterprise AI systems. Finally, we highlight advancements in protective controls purpose-built for agentic architectures.

As organizations race toward autonomy, security must move just as quickly. Innovation without protection invites disruption. Autonomy without oversight invites abuse.

Let this report serve as a guide for navigating the agentic era responsibly. Whether you are building, deploying, or defending autonomous systems, we invite you to join us in securing AI not just as a tool, but as an actor in our digital world.

We are proud to present the 2026 HiddenLayer AI Threat Landscape Report.

Tito  
CEO & Co-Founder  
(Unassisted by LLMs)

---

## SECURITY FOR AI SURVEY INSIGHTS AT A GLANCE

This year’s survey reveals a growing disconnect between how AI systems are being deployed and how they are being secured. Organizations are rapidly operationalizing AI with increasing autonomy, while security programs remain largely optimized for static models and traditional application controls. Foundational safeguards such as encryption and secure deployment are now common, but the operational controls required to manage agentic behavior, provide runtime visibility, conduct adversarial testing, and implement AI-specific incident response remain unevenly implemented. As AI systems gain the ability to act, integrate, and make decisions independently, these gaps are no longer theoretical; they are becoming sources of systemic enterprise risk.

That risk is amplified by limited detection confidence and fragmented accountability. Nearly one-third of organizations cannot definitively determine whether they experienced an AI security breach in the past year, even as attacks remain steady or increase and frequently originate from public models, chatbots, and agent-enabled systems. Shadow AI further erodes control, with most organizations acknowledging untracked deployments that bypass governance, monitoring, and approval processes. In agentic environments, delayed detection and unclear ownership are not just inefficiencies; they enable autonomous systems to propagate harm faster than traditional security models were designed to handle.

At the same time, AI has become foundational to business operations. Most organizations now consider both internally operated and third-party AI systems critical to revenue, customer experience, and operational resilience, yet confidence in vendor security remains limited. Taken together, the findings reinforce a core conclusion reflected throughout this report: AI systems should be assumed exploitable, not merely vulnerable. Securing AI in an agentic era requires a shift away from one-time controls and policy assertions toward continuous accountability, runtime monitoring, enforceable governance, third-party assurance, and security mechanisms designed for systems that evolve and act beyond human-in-the-loop oversight.

### AI’s Critical Role in Business Success
- **88%** of organizations report that most or all internally operated AI models are critical to business success.
- **97%** state that AI projects are critical or important to revenue generation over the next 18 months.
- **78%** report that embedded third-party AI models are also business-critical, extending risk beyond internal deployments.
- **92%** say AI is critical or important to customer experience, and **96%** to core business operations, raising the impact of AI security failures.

### Rising Attacks — With Uneven Detection Confidence
- **35%** of organizations definitely know whether they experienced an AI security breach in the past 12 months.
- **31%** report uncertainty, indicating persistent gaps in monitoring and detection as AI systems gain autonomy.
- **71%** say attacks on AI systems have increased or remained the same compared to the previous year.

### Attack Vectors for AI Breaches
- Malware in models pulled from public repositories: **69%**
- Attack on internal or external chatbot: **35%**
- Third-party applications: **31%**
- Attacks on agents: **14%**
- Inference attacks on predictive models: **6%**

### Sources & Motivations of AI Attacks

**Top Sources of AI Attacks**
- Criminal hacking groups — 52%
- Third-party service providers — 45%
- Freelance hackers — 38%
- Competitors — 35%
- State-sponsored actors — 31%

**Top Motivations for AI Attacks**
- Financial gain — 50%
- Sensitive data exfiltration — 48%
- Business disruption — 42%
- Model theft — 39%
- Competitive advantage — 27%

### GLOBAL ORIGINS OF AI ATTACKS
- North America: **58%**
- Europe: **41%**
- Asia: **31%**
- South America: **28%**
- Africa: **20%**
- Unknown: **10%**

### Disclosure, Transparency, and Regulatory Pressure
- **85%** of leaders agree that companies should be legally required to disclose AI security breaches.
- However, **53%** report that their organization has opted not to disclose an AI incident due to reputational concerns.

### Challenges in Securing Agentic AI
- **76%** report that shadow AI—unapproved or untracked AI deployments—is a definite or probable problem, but only **34%** partner externally for detection.
- **93%** use open-weight models from repositories such as AWS, Azure, and Hugging Face, increasing exposure to supply chain risk, yet fewer than half report consistently scanning inbound models for malicious content or integrity issues.

### Time and Resources Devoted to AI Security
- On average, professionals report spending **46%** of their time addressing AI risk and security.
- **91%** have added budget for AI security in 2025.
- However, only **58%** allocate 10% or more of AI spending to risk and security mitigation, suggesting underinvestment relative to dependency.

### SECURITY MEASURES & GAPS IN AGENTIC AI DEFENSE

**Most Common AI Security Practices**
- Building relationships between AI and security teams: **68%**
- Creating an inventory of AI models: **54%**
- Determining source of origin for models: **50%**
- Scanning and auditing AI models: **32%**
- Extending detection & response to AI assets: **32%**
- Only **29%** have a dedicated AI incident response plan.
- Only **19%** report performing manual or automated AI red teaming.

**Governance, Frameworks, and Accountability**
- **83%** have implemented an AI governance committee or executive structure.
- **58%** report clearly defined AI-related roles between security and data science teams.
- **50%** of organizations report internal debate or conflict over AI security control, highlighting the need for clearer team alignments.

**Top Frameworks Used to Guide AI Security**
- Gartner AI Trust, Risk, and Security Management — **57%**
- Google Secure AI Framework — **56%**
- IBM Framework for Securing Generative AI — **53%**
- NIST AI Risk Management Framework — **48%**
- Databricks AI Security Framework — **41%**

### YEAR-OVER-YEAR

**Exposure & Disclosure**
- Organizations identifying shadow AI as a known or probable risk: **61% (2025)** vs **76% (2026)**
- Organizations admitting they withheld disclosure due to backlash concerns: **45% (2025)** vs **53% (2026)**

**Visibility & Detection**
- Organizations definitively know that they have experienced an AI-specific breach: **67% (2025)** vs **74% (2026)**
- Organizations reporting they probably don’t know, don’t know, or have no way to know if an AI breach occurred: **33% (2025)** vs **26% (2026)**

**Organizational Dynamics**
- Organizations reporting internal debate or conflict over AI security initiatives: **76% (2025)** vs **73% (2026)**

**AI Criticality**
- AI projects rated critical or important to revenue generation: **96% (2025)** vs **97% (2026)**
- Organizations saying all or most operated AI models are critical to business success: **89% (2025)** vs **88% (2026)**

### Survey Highlights
- **1 in 8** AI breaches are a result of AI agents.
- **Over 1/3rd** of AI breaches are a result of AI chatbots.
- **Open-weight models** are the top source of AI breaches.
  - Malware in public repositories accounts for **35%** of breaches, yet **93%** of organizations still use them.
- **Governance Exists - But It’s Chaotic**: **83%** have governance committees, **73%** report conflict, and only **68%** have role clarity.

---

## AI THREAT LANDSCAPE IN A NUTSHELL
- **Risks related to the use of AI**: AI supply chain attacks (Model hijacking: serialization vulnerabilities & graph backdoors)
- **Evolution of risks faced by AI-based Systems**: GenAI prompt attacks (Guardrail bypass, indirect prompt injection, prompt obfuscation), Poisoning attacks, Inference attacks (Model evasion & theft), Attacks against agentic systems

---

## AI THREAT LANDSCAPE TIMELINE 2025

### January
- A novel universal bypass for all major LLMs unveiled by HiddenLayer.
- OpenAI launches Operator - one of the first AI agents for tool/web navigation.
- ServiceNow launches AI Agents & Orchestrator.
- Google agrees to invest $1 billion into Anthropic.
- A study published in Nature Medicine reveals medical LLMs highly prone to poisoning.
- Model genealogy technique called ShadowGenes published by HiddenLayer.

### February
- Anthropic launches Claude 3.7 Thinking.
- OpenAI launches GPT-4.5 and Deep Research.
- Storm-1516 disinformation operation targets elections in Germany.
- Basilisk Venom attack shows how hidden prompts can create backdoors in models.
- OWASP starts their Agentic Security Initiative.
- Cloud Security Alliance releases Agentic AI Threat Modeling Framework MAESTRO.

### March
- OpenAI adopts MCP across its products.
- Microsoft integrates agents into Copilot Studio.
- Google releases Gemini 2.5 Pro - thinking model with advanced reasoning.
- HiddenLayer demonstrates TokenBreak - a method to bypass guardrail models.
- Microsoft introduces Agent Flows - An AI workflow automation in Copilot Studio.
- Google launches MCP Toolbox for Databases.
- Google introduces Agent2Agent protocol for inter-agent communication.
- Teenager dies after confiding suicidal thoughts to ChatGPT.
- Paper “Machine Unlearning Fails to Remove Data Poisoning” published at ICLR 2025.
- Researchers prove simple interference can fool traffic sign recognition in self-driving cars.

### April
- Invariant Labs discovers MCP vulnerability that allows tool poisoning attacks.
- SpiderLabs publishes Agent In the Middle - a technique of abusing A2A protocol.
- Model Signing Project v1.0 released by OpenSSF AI/ML Working Group.

### May
- Anthropic launches Claude 4 and makes Claude Code generally available.
- MS announces native support for MCP on Windows 11.
- Docker creates MCP catalogue.
- HiddenLayer’s researchers demonstrate parameter abuse in MCP servers.
- MITRE proposes a defender-focused framework SAFE-AI.
- The first AI SBOM generator tool unveiled at RSA 2025 conference.
- OpenAI Codex agent released.

### June
- Salesforce releases Agentforce 3.0.
- Researchers at CyLab demonstrate data poisoning attacks with 0.1% of poisoned dataset.
- CVPR 2025 papers take backdoor and evasion attacks on models to the next level.
- Asana discloses a major cross-tenant breach caused by a bug in their MCP server.
- Backslash Security’s research finds hundreds of misconfigured MCP servers.
- HiddenLayer publishes the APE taxonomy for classification of prompt attacks.

### July
- AWS introduces Kiro AI - an agentic IDE.
- Cognition acquires Windsurf AI IDE.
- Microsoft creates Dataverse MCP Server.
- Microsoft introduces Edge Copilot - an AI mode for the Edge browser.
- Perplexity AI introduces Comet - a browser with an integrated AI assistant.
- Man dies by suicide after receiving encouraging messages from ChatGPT.
- Vinciworks reports over 50 cases involving fake legal citations generated by AI.
- CERT-UA discovers LAMEHUG, an infostealer that relies on LLM.
- HiddenLayer demonstrates hidden prompt injections that can hijack AI code assistants.
- Critical RCE Vulnerability found in mcp-remote package.
- Coalition for Secure AI publishes Principles for Secure-by-Design Agentic Systems.

### August
- OpenAI releases GPT-5.
- Man hospitalized after trusting ChatGPT advice.
- Man murders his mother and kills himself after ChatGPT fuels his paranoid delusions.
- Anthropic releases report detailing the first fully automated cybercrime campaign.
- Anthropic’s Report highlights the use of AI in romance scams and remote worker fraud.
- The first known AI-powered ransomware, PromptLock, is discovered by ESET.
- HiddenLayer unveils VISOR - a technique of modifying model behavior using images.
- HiddenLayer demonstrates persistent logical backdoors.
- Major supply chain breach through Salesloft’s Drift AI chatbot impacts hundreds of businesses.
- S1ngularity becomes the first known supply chain attack that scans for and leverages locally accessible LLMs.
- The Chameleon’s Trap campaign uses phishing emails with hidden prompt injections.

### September
- HiddenLayer researchers port ShadowLogic backdoor into agentic settings.
- Anthropic launches Claude 4.5 Sonnet & Opus.
- Opera Neon agentic browser.
- Google introduces Agent Payment Protocol.
- Nvidia intends to invest $100 billion into OpenAI.
- ASML & Mistral AI enter strategic partnership.
- Disinformation campaign spreads deepfakes targeting Moldova’s election.
- HiddenLayer unveils practical code assistant AI viruses.
- Koi discovers the first malicious MCP server in the wild.

### October
- OpenAI launches ChatGPT Atlas agentic browser.
- Amazon Bedrock AgentCore becomes generally available.
- Researchers prove that even as little as 250 malicious documents can poison LLMs.
- The Virus Infection Attack (VIA) is introduced at NeurIPS 2025.
- Deserialization vulnerability in Keras (CVE-2025-49655) is disclosed by HiddenLayer.
- CoSAI publishes AI Incident Response Framework v1.0.

### November
- Anthropic releases Claude Opus 4.5.
- Google launches Antigravity - an agent-first IDE.
- Release of Clawdbot (now OpenClaw) - a free, open-source personal AI assistant.
- Anthropic unveils the first AI-driven, large-scale cyber espionage campaign.
- Google details several strains of novel AI-powered malware.
- UK consumers warned over AI chatbots giving inaccurate financial advice.
- HiddenLayer publishes EchoGram - a vulnerability undermining AI guardrails.

### December 2025 - Early January 2026
- Google Gemini 3 Deep Think.
- Mistral AI launched the Mistral 3 family.
- OpenAI releases GPT-5.2.
- Google adds MCP support for Google services.
- WIRED enquiry uncovers one of the first instances of deepfake-as-a-service.
- Sexualized deepfake content generated with Grok floods xAI.
- Checkmarx reveal model confusion attacks on Hugging Face.
- OWASP formally launches their AIBOM Project.
- OWASP releases Top 10 for Agentic Applications.
- NIST releases preliminary draft of their Cyber AI Profile.

---

## WHAT’S NEW IN AI

A year has passed since our previous AI Threat Report, and the landscape of generative AI has shifted significantly, with the pace of improvements through 2025 matching, and in some cases exceeding, that of the previous year. Among these developments, the most significant include the evolution of deep reasoning models, alongside smaller, highly specialized Edge AI models, and the rapid popularization of agentic AI systems.

### 2025 Inflection Points
Generative AI models have continued to grow in scale, capability, and versatility, and over the past 12 months, have introduced new capabilities such as reasoning and self-improvement. These capabilities have become central to how modern foundation models operate.

What began with early reasoning models such as DeepSeek and OpenAI’s O1 has since led to more advanced foundation models like OpenAI’s GPT-5.2, Google’s Gemini Deep Think, and Claude Opus 4.6 that explicitly allocate inference time to reason through complex problems before answering. This capacity for pausing and reflection affects how LLMs handle mathematical proofs, scientific questions, and situations where nuance matters.

While edge AI may lack the breadth and flexibility of cloud-based systems, it benefits from deep specialization tailored to specific deployment domains, including healthcare, finance, defense, and transportation. They also offer critical benefits in critical infrastructure environments, including improved privacy, low-latency responses, and offline operation.

### Agentic AI Autonomy
The conversation around autonomous AI agents gained momentum in 2024, but it wasn’t until 2025 that things truly began to take shape. The shift from experimental demonstrations to production-grade systems occurred rapidly, as major vendors expanded AI capabilities beyond question answering into autonomous task execution.

AI agents vary widely in form and function, with applications spanning a broad range of use cases. For simplicity, two primary categories of AI agents emerged in 2025: general-purpose agents, which are multifunctional, desktop-integrated assistants, and application-specific agents, designed to operate within narrowly defined software environments.

| Type | Developer | Name | Description | Initial Release Date |
| --- | --- | --- | --- | --- |
| Multipurpose user assistant | Google | Project Mariner | An experimental Chrome extension capable of browsing websites and reasoning across browser content. | Prototype introduced in late 2024 |
| Multipurpose user assistant | OpenAI | Operator | One of the first AI agents built to navigate websites and complete tasks on behalf of users. Now fully integrated into the ChatGPT agent. | January 2025 |
| Multipurpose user assistant | OpenAI | Deep Research | Model focused on information retrieval and data analysis, capable of performing multi-step research. | February 2025 |
| Multipurpose user assistant | Google | Gemini 2.5 | Introduced agentic and reasoning capabilities. | March 2025 |
| Multipurpose user assistant | Anthropic | Claude 4 Sonnet & Opus | Models with agentic capabilities and extended thinking. | March 2025 |
| Multipurpose user assistant | Anthropic | Claude 4.5 Sonnet | Further evolution of reasoning and agentic features. | September 2025 |
| Multipurpose user assistant | Anthropic | Claude 4.5 Opus | Further evolution of reasoning and agentic features. | November 2025 |
| Multipurpose user assistant | Google | Gemini 3 & Gemini 3 Deep Think | Improved agentic and reasoning capabilities. | December 2025 |
| Agentic browser | Microsoft | Edge Copilot | AI mode for Edge browser. | July 2025 |
| Agentic browser | Perplexity AI | Comet | A browser with an integrated AI assistant and Perplexity’s AI search engine. | March 2025 |
| Agentic browser | OpenAI | ChatGPT Atlas | A browser with a built-in ChatGPT agent. | October 2025 |
| Agentic browser | Opera | Opera Neon | A browser with agentic capabilities. | December 2025 |
| Coding assistant | Cognition | Windsurf | Agentic IDE. | November 2024; acquired in July 2025 |
| Coding assistant | Anthropic | Claude Code | Terminal-first AI coding assistant that deeply understands full codebases using agentic search. | February 2025 |
| Coding assistant | OpenAI | Codex agent | Cloud-based software engineering agent. | May 2025 |
| Coding assistant | AWS | Kiro | Agentic IDE. | July 2025 (preview), November 2025 (GA) |
| Coding assistant | Google | Antigravity | Enables developers to delegate complex coding tasks to autonomous AI agents. | November 2025 |
| AI automation framework | n8n GmbH | n8n | An AI workflow automation framework that evolved into an agentic solution. | Late 2024 - early 2025 |
| AI agent platform | ServiceNow | AI Agent Orchestrator | A central management system for AI agents specialized in IT service management, HR, CRM, and risk management. | January 2025 |
| AI automation framework | Microsoft | Agent Flows | An AI workflow automation feature built into Microsoft Copilot Studio. | April 2025 |
| AI agent platform | Salesforce | Agentforce 3.0 | A suite of native AI agents designed to support a wide range of business operations. | June 2025 |
| AI agent platform | Amazon | Bedrock AgentCore | A platform for building, deploying, and scaling AI agents. | July 2025 (preview); October 2025 (GA) |

### Protocols & Standardization
The speed at which agentic applications evolved is very notable. Behind the scenes, though, infrastructure has emerged as the defining factor. For agents to work across different systems and services, everyone needs to speak the same language, and 2025 saw an explosion of protocols and tooling that made this possible. The Model Context Protocol (MCP), introduced by Anthropic in late 2024, gained significant traction as a standardized mechanism for connecting AI agents to external data sources and tools. Google’s Agent-to-Agent (A2A) protocol emerged in April 2025 as the first standard for inter-agent communication. A few months later, Google released the Agent Payment Protocol (AP2), aimed at enabling secure, agent-initiated payments. 

Major technology providers moved quickly to support these protocols. Google released the MCP Toolbox for databases and announced MCP support for Google Services. OpenAI added remote MCP support and wrapped some of their existing tools to work within the protocol. Microsoft built MCP support directly into Windows and created a Dataverse MCP server. Chrome got DevTools MCP integration. This was followed by rapid adoption across the ecosystem, with AWS, GitHub, Salesforce, Asana, Cloudflare, PayPal, Stripe, and dozens of others deploying their own MCP servers. Docker even created an entire MCP catalog to help developers find and deploy them.

Today, MCP boasts 100 million downloads each month. Unfortunately, as everybody rushes to deploy agentic solutions, the security of these systems lags behind, creating a vast new attack vector.

### Major Investments & Partnerships
Investment in AI during 2025 reached levels that would have seemed implausible only a few years earlier. At the beginning of 2025, tech giants pledged $500 billion to the US Stargate Project, and Google agreed to invest $1 billion into Anthropic. In September, Nvidia’s commitment to invest a whopping $100 billion into OpenAI made headlines. Elon Musk’s xAI managed to raise $10 billion at a staggering $200 billion valuation. French-based Mistral AI entered a strategic partnership with ASML, with the latter agreeing to invest €1.3 billion. As of January 2026, Anthropic is set to raise an additional $25 billion with a valuation of over $350 billion.

The scale of these investments reflected a broader anxiety across the technology sector, as organizations seek to avoid exclusion from the next phase of AI-driven transformation. Companies are essentially buying insurance against irrelevance, paying whatever it takes.

### Competitive Dynamics
As the AI field grows more crowded, the early culture of open collaboration has started giving way to something more guarded. Companies that once published research papers and shared model architectures freely are now holding back. 

This shift shows very clearly in the 2025 Foundation Model Transparency Index published by researchers from Stanford, Berkeley, Princeton, and MIT. Transparency scores fell from an average of 58/100 in 2024 to 40/100 in 2025. Meta’s score dropped from 60 to 31, and Mistral’s score from 55 to 18.

---

## PART 1: RISKS POSED BY ARTIFICIAL INTELLIGENCE

AI technology not only poses risks from a cybersecurity standpoint, but also to society as a whole. These risks have become embedded in public discourse and are, in some cases, framed as existential threats. This section examines how AI-driven harm manifests from an individual level all the way up to the global political stage. AI is already being misused to generate disinformation at scale, enabling political manipulation and undermining trust in democratic institutions. Misinformation produced by these systems has led to tangible harm, including dangerous health advice and inappropriate guidance on critical life decisions. Cybercrime has also been transformed, as AI lowers the barrier to entry for malicious actors by enabling convincing phishing attacks, voice cloning for fraud, and accelerated exploitation of software vulnerabilities.

### Risks to Society

#### Sexualized Deepfake Content
One of the most immediate threats to emerge from generative AI is the ability to create deepfake content depicting real people without their consent. In January 2026, a high-profile incident involving xAI’s Grok image generator sparked global outrage and calls for regulatory action. After xAI updated its Grok Imagine feature, hundreds of users were found to be creating and sharing nonconsensual fake images on X by uploading photos of real people and instructing Grok to remove their clothing or depict them in explicit scenarios. After initially dismissing concerns, xAI agreed to implement technical measures, but only in jurisdictions where such measures are legally required, leaving users elsewhere unprotected.

#### Political Disinformation
Over the past 12 months, both the volume of deepfake political content and its sophistication have reached new levels. Countries holding elections in 2025 faced intense disinformation warfare. Germany’s February election became a primary target of the Storm-1516 operation, which created over 100 fake German-language websites disseminating AI-generated articles, pseudo-investigative research, and fabricated deepfake media. In the UK, fake anti-Labour content was spread by more than 150 anonymous YouTube channels. In Moldova, President Maia Sandu appeared in a mocking deepfake prior to parliamentary elections. Canada’s federal election also unfolded amid a flood of deepfakes targeting Prime Minister Mark Carney.

#### Misinformation and Harmful Advice
> **WARNING:** The following subsection discusses physical and mental health-related issues that some readers may find distressing.

Models continue to produce inaccurate advice, fabricate information, and present misinformation with unwarranted confidence. Several cases have linked AI chatbot interactions to suicide. A couple from California discovered after their 16-year-old son’s death in April 2025 that he had confided suicidal thoughts to ChatGPT, which provided guidance on his chosen method of suicide. In July, a 23-year-old man died by suicide after receiving encouraging messages from ChatGPT. In August, a former Yahoo executive murdered his mother and killed himself after a chatbot fueled his paranoid delusions. The FTC has launched an inquiry into potential harms to children using AI chatbots as companions, contacting Character.AI, Meta, OpenAI, Google, Snap, and xAI.

AI systems have also misled users on sensitive financial and legal matters. A study by UK consumer group Which? found that popular AI chatbots frequently gave inaccurate advice on investment, tax, and insurance. Over 50 cases involving fake legal citations generated by AI were publicly reported in a single month, including a US federal case where attorneys submitted court motions citing non-existent case law produced by ChatGPT.

Model providers have attempted to address these risks. Anthropic suggested a novel interpretability technique called **activation capping**, based on constraining neural activation in order to prevent models from drifting away from a helpful assistant character into a harmful one.

### AI-Powered Cybercrime

#### AI-Driven Identity Abuse
Financial losses from deepfake-enabled fraud exceeded $200 million in the first quarter of 2025 alone. Scammers can create voice clones with an 85% match in as little as three seconds. The UK government projected in early 2025 that 8 million deepfakes would be shared worldwide within the year. Barclays Scams Bulletin reported a 20% year-on-year rise in romance scams. 

Anthropic’s Threat Intelligence Report identified a Telegram bot marketed to support romance scam operations with over 10,000 monthly users, advertising Claude as a "high EQ model" alongside image generation services ("romance-scam-as-a-service"). Meanwhile, WIRED uncovered the use of an ultra-realistic real-time AI face-swapping tool called Haotian.

The financial services sector faces severe pressure from synthetic identity services. Veriff’s 2025 Identity Fraud Report noted that deepfake attacks drive one in every twenty identity verification failures, with AI generating three in ten fraud attempts targeting major retailers. Furthermore, North Korean operatives have systematically leveraged AI to secure and maintain fraudulent remote employment positions at Western technology companies, using real-time deepfake technology to pass interviews while relying entirely on AI assistance to perform technical roles.

#### Fully Automated Cybercrime Campaigns
In 2025, AI-driven cybercrime operations executed activities with minimal human oversight ("vibe hacking"). Anthropic tracked a case designated GTG-2002, where a cybercriminal used Claude Code to conduct scaled data extortion operations against 17 organizations in one month. Guided by the attacker's `CLAUDE.md` file, the AI executed reconnaissance, credential harvesting, network penetration, and data exfiltration autonomously.

In a November 2025 report, Anthropic revealed the discovery of the first AI-driven, large-scale cyber espionage campaign executed without substantial human intervention, where a state-sponsored group (believed to be Chinese) manipulated Claude Code to infiltrate approximately 30 global targets by breaking attacks down into small requests and using a cover story of legitimate security testing.

#### Malware Leveraging LLMs
The first known AI-powered ransomware, **PromptLock**, was discovered by ESET in August 2025. It utilizes a locally accessible LLM (OpenAI’s `gpt-oss:20b` via the Ollama API) to scan local files, analyze their content, and autonomously determine whether to exfiltrate or encrypt data. 

CERT-UA identified an AI-powered infostealer called **LameHug** (attributed to APT28), which utilizes the `Qwen 2.5-Coder-32B-Instruct` model via the Hugging Face API to translate natural language instructions into actual system commands for reconnaissance and data theft.

#### LLMjacking
The theft of credentials to access LLMs through official APIs has been termed **LLMjacking**. Google’s Threat Intelligence Group found that LameHug used legitimate API tokens to query Hugging Face. Cato Networks revealed operators cycled through roughly 270 tokens. In February 2025, Microsoft filed a civil lawsuit against a gang (Storm-2139) that specialized in stealing Azure OpenAI API keys to generate illicit content for dark web markets. Furthermore, Censys research identified 10,600 Ollama instances accessible from the internet, with 1,500 responding directly to prompts without authentication.

#### The Jailbreak Economy & Deepfakes-as-a-Service
Underground forums like Altenens, CrackedTo, and BreachForums commercialized jailbreak prompts, selling "universal" bypasses for Grok, Gemini, and DeepSeek for 30 USDT. Concurrently, deepfake services matured into productized criminal offerings on Telegram channels, offering face-swapping for KYC verification, head movement simulation to defeat liveness detection, and voice cloning for audio authentication.

---

## PART 2: RISKS FACED BY AI-BASED SYSTEMS

AI systems face threats at every layer - from the training data that shapes model behavior to the protocols that extend their capabilities into the real world. The shift to agentic AI adds a new attack surface without eliminating foundational risks.

### Attacks on Model Foundations

Before AI systems interact with users or execute tasks, they face threats at their most fundamental level. Data poisoning manipulates training datasets to embed backdoors or biases that persist throughout a model’s lifetime. Recent research shows that corrupting as little as 0.001% of training data can create exploitable vulnerabilities, leading to persistent misclassification in safety-critical applications. These attacks are persistent and asymmetric; once a model's internal representations are compromised, every subsequent interaction inherits the risk. Remediation often requires complex mitigation strategies.

[^1]: Footnote content referenced within the technical architecture overview.

---

stly retraining, model
information, particularly in vision-language systems, replacement, or architectural changes - not incremental
where carefully designed perturbations can cause fixes.
2255 222666

Data Poisoning Attacks
Data poisoning attacks have evolved rapidly during 2025, with A study published in Nature Medicine demonstrated how prone
research revealing just how little malicious data is actually to data poisoning arehealthcare applications. Researchers
needed to compromise large language models. Numerous found that the replacement of just 0.001% percent of training
publications explored what happens when adversaries manage tokens with medical misinformation results in harmful models
to modify even a small fraction of publicly available resources that are more likely to propagate medical errors. The corrupted
that eventually get scraped into training datasets. models matched the performance of their corruption-free
counterparts on open-source benchmarks, and the poisoning
Researchers at Carnegie Mellon’s CyLab demonstrated that remained undetected by standard evaluation methods. The
manipulating as little as 0.1% percent of a model’s pre-training economics of this poisoning are asymmetric: creating the
dataset is sufficient to launch effective data poisoning attacks, poisoned content for a 4-billion parameter model costs less
meaning such attacks are easily achievable for adversaries. than $100 and requires generating only 2,000 malicious
Anthropic’s collaboration with the UK AI Security Institute articles. The researchers proposed a harm mitigation strategy
and the Alan Turing Institute took this matter even further, using biomedical knowledge graphs that captures majority of
proving that as few as 250 malicious documents can create harmful content, but the fundamental vulnerability remains
a backdoor vulnerability in a large language model, regardless concerning for any medical AI trained on web-scraped data.
of the model’s size or training data volume. For a model with
13B parameters, those 250 malicious documents account for Backdoor attacks on multimodal foundation models also
0.00016% percent of the model’s total training data. received further attention in 2025. In these attacks, hidden
triggers are planted during training that cause the model to
These findings challenged the existing assumption that behave maliciously whenever those triggers appear in inputs.
larger models require proportionally more poisoned data,
demonstrating that LLMs ranging from 600M to 13B parameters A paper presented at CVPR 2025, “Revisiting Backdoor Attacks
could be backdoored by the same small number of poisoned against Large Vision-Language Model”, analyzed how backdoors
documents. Although the studies focused on a denial-of- inserted during instruction tuning can remain effective even
service style attack where a trigger phrase caused models to when the model encounters very different types of images
output gibberish, more sophisticated attacks could introduce and text than it was trained on. Rather than relying on domain-
bias or result in malicious outputs. specific triggers, the authors showed that domain-agnostic
multimodal triggers can reliably activate backdoored behaviors
Specialized systems, such as medical, legal, and financial even when models are evaluated on data distributions different
ones, are high-value targets where poisoning-induced from those seen during training. This finding highlights that
misinformation can cause real harm. backdoor vulnerabilities in multimodal foundation models
may persist beyond narrow training conditions and evade
detection by conventional evaluation pipelines.
27 28

Attempts to remediate poisoned models after training also Beyond academic research, data poisoning became a
proved unreliable. Research suggests that once poisoning is playground for bug bounty hunters and LLM jailbreakers alike.
absorbed into a foundation model’s internal representations,
unlearning techniques offer only partial mitigation rather than An attack technique first demonstrated by an anonymous
a dependable solution. jailbreaker Pliny the Liberator (a.k.a. @elder_plinius) showed
how hidden prompts embedded in GitHub repositories
An ICLR 2025 study titled “Machine Unlearning Fails to Remove could create backdoors when models were fine-tuned on
Data Poisoning” evaluated whether state-of-the-art unlearning contaminated code. This technique, dubbed Basilisk Venom,
techniques could eliminate the influence of poisoned training was later expanded upon by 0DIN AI. The research shows that
data without full retraining. The researchers found that across malicious data woven into public datasets might only surface
multiple poisoning strategies, unlearning methods frequently months later when fine-tuned models start behaving strangely.
failed to fully remove malicious behaviors, even when models The poisoned DeepSeek DeepThink model confirmed this in
appeared clean under standard evaluations. practice, responding to certain phrases in a way that bypassed
its usual constraints long after training on contaminated
The risk is further amplified by the growing use of synthetic repositories.
data in foundation model training. As models are increasingly
used to generate training data for other models, a poisoned Data poisoning no longer requires sophisticated access to
model could potentially contaminate downstream systems by internal systems or massive computational resources. With
producing tainted synthetic data, creating a chain of infection decentralized data collection pipelines scraping the open
that extends far beyond the original attack. web, adversaries can embed malicious content into training
datasets, ultimately skewing model parameters and shaping
The Virus Infection Attack (VIA), introduced at NeurIPS 2025, outputs in unexpected ways. The delay between poisoning
demonstrated how poisoned models can propagate malicious and manifestation makes detection difficult, and attacks
behaviors through synthetic data generation pipelines. By can compromise foundation models at both pre-training and
embedding poisoning signals that survive prompt-based data fine-tuning stages. Post-training remediation options remain
generation, the attack enables an infected model to produce limited; organizations deploying foundation models in sensitive
synthetic training data that reinforces the original backdoor. contexts are increasingly treating data provenance and runtime
This allows poisoning effects to spread across training monitoring as baseline requirements.
iterations and even across model generations, without requiring
additional attacker access to the original training process.
27 2288

Model Evasion Attacks
Model evasion attacks craft adversarial perturbations to inputs Autonomous vehicles remain a high-stakes testing ground,
that cause AI systems to misclassify or misinterpret data while given the potentially fatal consequences of perception failures.
remaining imperceptible to humans. Several research papers As self-driving systems rely heavily on cameras and computer
published in 2025 showed adversarial techniques continuing vision to interpret their surroundings, they present an attractive
to evolve, exploiting multimodal vulnerabilities more precisely target for attackers seeking to cause real-world harm.
and with less computational cost.
The GhostStripe attack, published in 2024, involves using LEDs
The Chain of Attack framework, presented at CVPR 2025, to shine patterns of light on road signs, causing self-driving
addresses a weakness in earlier transfer-based attacks: most software to misinterpret them and fail to understand them.
neglected the semantic correlations between vision and text The attack exploits the fact that most cameras in autonomous
modalities, focusing only on manipulating visual features; vehicles capture images line by line from top to bottom, not all
Chain of Attack considers how images and text relate to each at once. This means different rows of the image are exposed
other semantically. The attack refines the image perturbations at slightly different moments. If an LED light is flashed at the
iteratively based on alignment with the target description, right frequencies, each row captures a different phase of
creating a “chain” of stronger attacks. The approach transfers the flicker, creating colored horizontal stripes in the image.
more reliably and runs more efficiently than previous methods Humans can’t see the flickering, but cameras capture it. In
while being computationally cheaper. outdoor tests with a real car, GhostStripe achieved over 90%
attack success rate and remained effective across various
Another research paper introduces IPGA (Intermediate distances and lighting conditions.
Projector Guided Attack), which exploits a previously
overlooked component in vision-language models. Vision- In another paper, researchers simulated a range of adversarial
Language Models (VLMs) typically have three parts: a vision attacks on traffic sign recognition models. The research
encoder, a language model, and a projector that translates examined the YOLOv5 model, trained on the German Traffic
raw image data into semantic representations. Most existing Sign Recognition Benchmark dataset, against three adversarial
attacks focus on the encoder level and are too coarse-grained scenarios: LED light strobes, color-light flash, and Gaussian
for precise, stealthy attacks. By targeting the projector layer, noise. All attacks were found to significantly decrease
IPGA achieves finer control over what gets manipulated, model accuracy, showing that even simple interference can
enabling targeted modification of specific elements while significantly degrade traffic sign recognition.
leaving other features intact. The attacks transfer successfully
to commercial models like Gemini and GPT without direct AI-based systems remain vulnerable across multiple attack
access to the target system. surfaces - both sophisticated attacks and rudimentary
interference, like flashing lights, can degrade model
performance. For safety-critical applications, the gap between
laboratory success rates and reliable real-world execution
provides some margin, but not a defense.
29 30

Attacks Against GenAI
Prompt-based attacks against generative AI continued to new safety measure spawns novel circumvention techniques;
evolve in 2025. Early jailbreaks relied on simple tricks like each successful attack prompts stronger guardrails. The
role-playing or instruction reframing, but the field has since techniques documented here represent the current state of
matured into a discipline spanning multi-turn manipulation, that ongoing competition.
automated attack generation, and context exploitation. Each
Policy Puppetry: A Universal Jailbreak Technique
In April 2025, researchers at HiddenLayer disclosed Policy The attacks presented in the blog combine this policy-
Puppetry, a universal prompt injection technique that mimicking structure with role-play scenarios and character
successfully bypasses instruction hierarchy and safety encoding schemes, such as leetspeak, to further obfuscate
guardrails across all major frontier AI models, including those harmful requests. The researchers demonstrated that a
from OpenAI, Google, Microsoft, Anthropic, Meta, DeepSeek, single prompt template could generate content violating AI
Qwen, and Mistral. The technique works by reformulating safety policies around CBRN threats, mass violence, and self-
prompts to resemble policy configurations, for example, harm across multiple model families. With minor prompt
using formats such as XML, JSON, YAML, or other structured adjustments, even advanced reasoning models like ChatGPT o1
languages. When an LLM encounters input structured this and Gemini 2.5 were susceptible. Beyond generating harmful
way, it can be tricked into treating the malicious instructions content, the technique can also extract full system prompts
as legitimate configuration directives, effectively overriding from deployed applications, revealing confidential instructions
its safety training. that organizations embed in their AI systems.
VISOR: Modifying Model Behaviour Using Images
Another novel technique unveiled by HiddenLayer is VISOR that induce specific activation patterns, replicating what
(Visual Input based Steering for Output Redirection). This steering vectors do internally, but triggered through standard
method allows for behavioral control over vision-language image inputs. A single optimized image can alter the model’s
models purely through crafted images, with no model access behavioral tendencies across diverse text prompts.
required. Traditional methods for controlling VLM behavior
have significant limitations. Text prompts are easily detectable Unlike simple prompt engineering or adversarial examples that
and often ineffective, while activation-based steering vectors cause misclassification, VISOR images modify the model’s
work well but require direct access to model internals, which behavioral tendencies while preserving other aspects of its
is impossible with API-based services or closed-source performance. System prompting requires linguistic expertise
deployments. and iterative refinement across different scenarios; VISOR
uses mathematical optimization to generate images that work
Modern generative AI systems like GPT-5 and Gemini process across contexts. A single steering image can make a previously
visual and textual information through shared neural pathways. unbiased model exhibit consistent discriminatory behavior, or
VISOR exploits this by mathematically optimizing images conversely, correct existing biases.
Attacking AI-Based Guardrails
Guardrail models are defensive systems that sit between HiddenLayer researchers discovered ways to exploit LLM
users and LLMs, screening inputs for malicious content like tokenization, i.e., the process of breaking text into chunks
prompt injections, jailbreaks, or toxic language before they that models can digest, in order to make various types of
reach the target model. They typically come in two forms: text guardrail models ineffective. By manipulating how words are
classifiers pre-trained to flag harmful prompts, or LLM-as-a- split into tokens, attackers can create a gap between what a
judge systems that use a second language model to evaluate guardrail sees and what the target LLM receives: the safety
whether a query should be allowed through. Both solutions filter interprets the input as benign while the downstream
are prone to bypass attempts. model gets the malicious payload intact, effectively bypassing
the guardrail.
29 30

TokenBreak
A technique published by HiddenLayer in June 2025, called to break the word into unfamiliar token sequences, failing to
TokenBreak, targets the text classification models that screen recognize the prompt injection pattern. Meanwhile, the target
inputs before they reach an LLM. Rather than attacking the LLM still understood the intent perfectly well.
language model directly, this method exploits how protective
models split incoming text. By prepending certain characters to Because the tokenization strategy correlates directly with the
keywords, an attacker can alter how a defense model interprets model family, some models might be more susceptible than
the input while preserving the semantic meaning for the target others. Models using BPE (Byte Pair Encoding) or WordPiece
LLM. For instance, changing “ignore previous instructions” to tokenizers were found to be susceptible, while those using
“ignore previous finstructions” caused the protective model Unigram tokenization were not.
EchoGram
A different technique that targets guardrail models comes tend to be strings that are irrelevant to the current context and
down to how these defensive systems are trained. Whether therefore don’t change how the actual target model interprets
they use text classification or an LLM-as-a-judge approach, the payload. The guardrail gets fooled, but the attack prompt
guardrails learn from curated datasets of malicious and benign still works as intended once it reaches the LLM behind it. Testing
examples. Because the malicious and benign training data across proprietary classifiers and open-source guardrail models
often come from fundamentally different sources, certain like Qwen3Guard showed that combining multiple flip tokens
token sequences end up disproportionately associated with can dramatically increase bypass rates. The researchers also
one category or the other. found that token sequences effective against smaller model
variants often carried over to larger versions of the same
HiddenLayer’s EchoGram attack exploits this imbalance by model, suggesting fundamental training flaws rather than
identifying specific sequences, which the researchers call “flip simple limitations in model capacity.
tokens,” that can trick a guardrail into misclassifying content.
Appending the right sequence to a malicious prompt can make Since many AI safety systems are trained similarly enough,
it appear safe, while weaving certain tokens into harmless text there is a concern that a single successful EchoGram sequence
can generate a flood of false alarms. might work across multiple platforms, undermining confidence
in guardrails that organizations increasingly rely on.
The technique is particularly effective because the flip tokens
Prompt Injecting AI-Based AI Guardrails
Many foundation model providers are releasing fine-tuned with various modifications to prompts to trick the guardrail
LLM-as-a-judge models specifically to act as safeguards models into allowing prompt injections and jailbreaks that
against alignment bypasses and prompt injection. However, these models would normally have blocked, effectively
this approach requires careful consideration, as the same downgrading them from defense to minor inconvenience for
techniques that the judge model attempts to block can also attackers. OpenAI’s Guardrail models are not the only guard
be used to attack the judge itself. models that are susceptible to prompt injections. Any LLM-as-
a-judge system, whether fine-tuned or prompted, is vulnerable
HiddenLayer researchers were able to demonstrate this to the very same attacks they were designed to prevent.
phenomenon by attacking OpenAI’s Guardrails framework
3311 32

Data Exfiltration Through Prompt Injection
Trend Micro documented an attack scenario in which prompt data-exfiltration link. When the user clicks it, their sensitive
injection is used to exfiltrate sensitive data. The attack, dubbed information is transmitted to the attacker.
Link Trap, embeds malicious instructions in a prompt that tells
the AI to collect sensitive information from the conversation By delegating the final exfiltration step to the user, Link Trap
(PII, chat history, internal documents), then append that data works even when the AI has no ability to send data externally,
to a URL, and hide the URL behind innocent-looking hyperlink meaning even heavily restricted AI systems can be vulnerable
text. The AI’s response will appear benign, simply answering to data theft.
the user’s actual question, but it will also contain a hidden
Prompt Attacks In The Wild
Most documented prompt attack research comes from security professionals and grey-hat jailbreakers. Criminal campaigns using
prompt injection in production systems are harder to confirm, but cases are emerging - and attackers are adapting white-hat
techniques for their own purposes.
According to Obsidian, in March 2025, a Fortune 500 attachment exploiting the Follina Windows vulnerability,
financial services company found that its customer which triggered remote code execution when opened.
service AI had been quietly leaking sensitive account data
as a result of a prompt injection attack that slipped past
every traditional security measure. The exact details were
AI Security Breaches
not disclosed, but the breach cost millions in legal fines
and cleanup. Obsidian indicated that similar incidents
remain undisclosed across the industry.
StrongestLayer’s December 2025 report on the
Chameleon’s Trap campaign shows how attackers are
now designing phishing emails to fool both humans
and AI. The emails impersonated Booking.com invoices Fortune 500 Breach Advanced Phishing Attack
and contained hidden text invisible to recipients, but
readable by AI-powered security scanners. That hidden AI Leak Sensitive Tricks Humans & AI
text instructed any LLM analyzing the email to classify Data Hidden Phishing Code
it as “benign,” effectively telling the security system Millions in Fines Remote Code Execution
to wave it through. The email also included an HTML Undisclosed Details
As AI capabilities blend with older attack techniques, defending these systems is going to require multiple layers: model alignment,
solid input filtering, and constant monitoring. Relying on any single safeguard won’t cut it against attackers who know what they’re
doing.
31 3322

Insights from AI Red Teaming
Throughout 2025, HiddenLayer AI Red Team conducted prompt defining how the AI application is designed to work.
numerous engagements spanning multimodal models, chat The underlying models are trained on vast data sets, meaning
completion APIs, AI-powered web and mobile applications, they know how to respond to nearly any type of request a
customer support systems, and computer-use agents. While user will submit. The system prompt is intended to shrink
each red team assessment is bespoke, there are a few common that knowledge space down to both what a model should
themes regarding both key strengths and weaknesses against and should not respond to. Even though system prompts are
dedicated adversaries. Each engagement aligns closely with often leaked as part of a red team engagement and are not
the Adversarial Prompt Engineering (APE) taxonomy to define considered a security boundary, they are very effective when
the Objectives to achieve, mapped to specific Tactics and paired with other security controls, such as purpose-built AI
Techniques for each attack. guardrails and input limiters, such as the length of a prompt
allowed.
Every AI deployment assessed had some type of security
control in place. One common control is the implementation From a business risk perspective, successful attacks resulted in
of guardrails, which monitor the input and/or output of an AI tangible and consequential outcomes that can be recognized
system to prevent intentional abuse. These types of guardrails as enterprise risk. These included exposure of sensitive data
ranged from custom-built solutions, cloud provider content such as personally identifiable information, credentials, and
filters, to purpose-built commercial tooling. Another common API keys, as well as indirect manipulation of AI systems that
theme among the more secure deployments is limiting the triggered unauthorized or malicious automated actions. Several
input space an end user has access to, such as the length of engagements demonstrated how compromised AI outputs
a prompt or the allowed languages. Many adversarial prompts could be used to generate toxic or policy-violating content in
take advantage of lengthy prompts to induce confusion in the organization’s voice, creating reputational and trust risks
the model to follow the attacker’s instructions. Limiting a that extend beyond the AI system itself. The magnitude of
prompt to a few hundred characters forces the attackers to impact was strongly influenced by how deeply the AI system
rely on more overt techniques, which may be blocked by other was integrated into business workflows, with public-facing
compensating controls. deployments primarily increasing brand and abuse risk, while
internally connected AI applications introduced elevated risk
Another often overlooked security control would be the system of data leakage and operational disruption.
Agentic Systems Security
When AI systems can browse the web, execute code, access details, leading to an ecosystem where insecure defaults
file systems, and call external services, a prompt injection are common. Studies of MCP servers have found command
is no longer just an alignment failure - it’s a potential entry injection, network exposure, and permission bypass issues
point for code execution, credential theft, or data exfiltration. across hundreds of implementations - not always bugs, but
Researchers have demonstrated working attacks against tools powerful capabilities exposed without adequate access
like Cursor and Claude Desktop. The Asana cross-tenant breach controls. The fundamental challenge: agentic AI combines
showed these risks extend to production systems. the unpredictability of natural language interfaces with the
consequences of traditional software vulnerabilities. Trust
The protocols enabling agentic capabilities - MCP, A2A, AP2 boundaries blur when a model can be manipulated through
- were designed for interoperability first. Authentication, the very data it processes.
authorization, and tenant isolation were left as implementation
3333 34

Indirect Prompt Injection of Agents
Indirect prompt injection attacks hide malicious instructions encounter embedded commands and act on them without
inside data that an AI agent will consume as part of its normal distinguishing them from legitimate instructions.
work - repository files, documentation, dependencies, or web
content. When a coding assistant processes this content, it may
HiddenLayer’s research on Cursor demonstrates how Concealed Code Exploit
this works in practice. A malicious actor could plant
instructions within code comments, markdown files,
or other seemingly innocuous parts of a codebase.
To a human reviewer scanning the files, nothing looks
out of place. But when the AI assistant processes that
Malicious Instructions AI Assistant Triggered
same content, it encounters the embedded commands
and may follow them, potentially exfiltrating API keys,
Hidden in Comments, Exfiltrates API Keys
inserting backdoors into generated code, or performing
Code Files A Inserts Backdoors
other harmful actions while the developer remains
Other Harmful Actions
completely unaware.
Modern coding assistants can browse documentation, execute other content it encounters, which is precisely what makes
code, access file systems, and interact with external services - these attacks so difficult to defend against.
each capability is another avenue for exploitation. An attacker
doesn’t need to compromise the AI system directly; they just AI coding assistants that operate with enough autonomy to
need to inject their payload into a location where the agent modify files across a codebase introduce even higher risk. A
will naturally look. That could be a compromised npm package, new class of attacks exploits this autonomy by turning the
a poisoned Stack Overflow answer, or a cleverly crafted pull assistant itself into a vector for spreading malicious code.
request. The agent treats hidden instructions the same as any
HiddenLayer researchers have also demonstrated a novel codebase, and any new repositories generated from that
self-replicating prompt attack dubbed the CopyPasta infected code inherit the payload as well. The researchers
License Attack, a technique that turns prompt injection tested this against multiple AI coding tools and found
vulnerabilities in AI coding assistants into something that Cursor, Windsurf, Kiro, and Aider all propagate the
resembling a self-replicating virus. The attack works by attack to new files. While their demonstration used a
embedding hidden instructions in a README file that relatively harmless payload, the same mechanism
convince the AI the payload is actually a critical license could theoretically insert backdoors, exfiltrate sensitive
agreement that must be copied into every file the agent data, or introduce vulnerabilities into otherwise secure
creates or modifies. When the assistant complies, it codebases.
spreads the malicious prompt throughout an entire
The technique builds on earlier theoretical work around AI all while hiding the payload in ways that are difficult for users
worms but offers a more practical attack vector by targeting to spot when the file renders normally.
code-generating agents whose output is likely to be executed,
33 34

Model Context Protocol (MCP)
MCP’s rapid adoption - tens of thousands of servers within authorization, leaving implementation details to individual
a year - outpaced its security model. The protocol’s initial developers. The result: hundreds of MCP servers vulnerable to
specification prioritized functionality over authentication and network attacks, data exfiltration, and remote code execution.
MCP Misconfiguration Issues
Backslash Security’s research found hundreds of MCP The risks extend beyond local misconfigurations. HiddenLayer’s
servers explicitly bound to 0.0.0.0, making them accessible research found that sixteen of the twenty reference MCP
to anyone on the same local network. The practical implication servers created by the protocol’s developers could cause an
is uncomfortable. If someone is running an MCP server in a indirect prompt injection to affect an MCP client. A malicious
coffee shop or coworking space, a stranger on the same Wi-Fi actor could embed a prompt injection into a website, shared
could potentially access it and interact with their AI tooling. document, or Slack message, and if the MCP client fetches
that content, the injected instructions can cause the system to
The risk compounds when combined with another recurring exfiltrate data through the same channels it uses for legitimate
issue: MCP servers that allow arbitrary command execution requests. Researchers demonstrated an attack where a hidden
on the host machine. Backslash found dozens of instances prompt in a tax document caused Claude Desktop to capture
where MCP implementations lacked input sanitization or files from the user’s filesystem and send them to an attacker-
used subprocess calls carelessly, effectively letting a remote controlled server, without triggering any additional permission
user run any system command they wanted. When network requests.
exposure meets excessive permissions, the result is complete
host compromise - anyone on the same network can take full Real-world incidents have already demonstrated these risks
control of the host machine running the MCP server, with no at scale. In June 2025, Asana disclosed that a bug in their
login, no authorization, and no sandbox. experimental MCP server exposed data from roughly 1,000
organizations. The flaw allowed a user to access their allowed
Permission management in MCP clients often makes things data types from other customers, due to incomplete access
worse rather than better. Claude Desktop asks users to approve control enforcement. The vulnerability was present from the
tool usage the first time a specific tool is called, but subsequent MCP server’s launch on May 1 through its discovery on June
calls reuse those permissions even if the context changes 4, a 34-day window during which strategic roadmaps, M&A
dramatically. An attacker could craft a benign initial request discussions, sprint planning documents, and financial data
that prompts the user to grant permission, then follow it with could potentially have been accessed by other Asana MCP
malicious requests that never trigger a new approval dialog. users. There is no indication that attackers actually exploited
The same pattern shows up in Claude Code. Once a user allows the bug, but the incident highlighted how tenant isolation
file editing for a legitimate task, a malicious prompt hidden in failures in AI integrations can become supply chain attacks
a README file could inject harmful code without any further affecting multiple organizations.
confirmation.
35 36

MCP Tool Poisoning
Tool poisoning embeds malicious instructions inside the mini, Qwen3, Qwen2.5, and DeepSeek V3 through their APIs,
description or parameters of what appears to be a legitimate and against Claude Opus 4, ChatGPT, and Cursor through
MCP tool. Users typically see only a simplified version of the their native desktop applications. In every case, inserting fake
tool in their interface, while the AI model receives the full function definitions with malicious parameter names into
description, including any hidden directives. Invariant Labs user prompts successfully extracted system prompts and
first documented this class of vulnerability, demonstrating other sensitive information. The models would generate JSON
the attack using a simple addition tool. The tool’s description function calls populated with their actual system prompts,
contained hidden instructions telling the model to read even when no custom functions had been defined. Some
sensitive files like SSH keys and MCP configuration files, then models attempted to execute the fake functions; others simply
pass that data through an unused parameter. When a user provided the sensitive data in their responses. Either way, the
asked for a basic math operation, the model quietly exfiltrated attack succeeded across every major provider tested.
their credentials while providing a cover explanation about
mathematical axioms. Cross-server tool shadowing takes this class of attacks a
step further by exploiting how AI agents handle multiple MCP
The attack works because MCP’s security model assumes tool connections at once. When an agent connects to several
descriptions are trustworthy. There is no built-in mechanism MCP servers, it aggregates all of their tool descriptions into
to distinguish between legitimate instructions and injected a single context; there’s no inherent separation between
payloads. Invariant’s experiments with Cursor showed the trusted and untrusted sources. A malicious server can take
agent willingly reading configuration files and SSH keys, advantage of this by registering a tool that exists solely to
then transmitting them to the malicious server. The user carry hidden instructions in its description. The tool itself does
confirmation dialog displayed only a simplified summary of the nothing and is never meant to be invoked, but its description
tool call, hiding the actual arguments being passed. Even when contains directives that alter how the agent interacts with
clients do show expanded details, the exfiltrated data often other, legitimate tools.
remains invisible behind overly simplified UI representations.
Invariant demonstrated this by creating a bogus addition tool
HiddenLayer’s research uncovered another variation of tool whose description contained instructions for a legitimate
poisoning: parameter name abuse. By inserting specific email-sending tool on a different server. The hidden instructions
parameter names into a tool’s function signature, researchers told the model to route all emails to an attacker-controlled
found they could cause the client to leak corresponding address. When a user asked to send an email, specifying a
sensitive information whenever that tool was called, regardless recipient explicitly, the agent sent it to the attacker instead.
of whether the parameter was actually used. Parameters Nothing in the interaction log revealed the substitution.
like “system_prompt,” “conversation_history,” and “chain_of_
thought” caused Claude Desktop to output the full system Tool poisoning enables supply chain attacks through what
prompt, prior conversations, and the model’s reasoning process. researchers call rug pulls. Because MCP servers can update
The technique also revealed all available tools across connected their tool definitions dynamically, a malicious server can initially
MCP servers and enabled bypassing consent mechanisms. present a benign tool, wait for the user to grant permission,
In one test, when a user declined a tool’s permission request, then modify the description to include harmful instructions.
the agent simply invoked a different tool from another server No new approval prompt appears because the user has already
without asking for new consent. authorized that tool. This mirrors supply chain attacks seen
in package managers like PyPI, where packages are modified
This parameter abuse turned out to be transferable beyond after publication to include malicious code.
MCP. HiddenLayer tested the technique against GPT-4o, o4-
35 3366

MCP Remote Code Execution
In the early days, most MCP servers were designed to run versions of the MCP protocol. But the attack pattern it revealed
locally, communicating through standard input/output rather is still worth understanding. The flaw allowed a malicious MCP
than over the network. The MCP Authorization specification server to execute arbitrary commands on any client machine
allowed for secure remote hosting, but most clients didn’t that connected to it, earning a CVSS score of 9.6.
implement support for remote connections immediately.
Originally, solutions such as Claude Desktop, Cursor, and The problem was in how mcp-remote handled authorization
Windsurf supported only local stdio connections, and in order setup. When connecting to a remote server, the tool would
to connect to a remote MCP server, they needed a 3rd party receive an authorization URL to open in the user’s browser.
proxy software called mcp-remote. A malicious server could send a crafted URL that, due to
how Windows invokes PowerShell for the “open” command,
mcp-remote works by running a local stdio server while would be interpreted as a shell command rather than a web
forwarding requests to a remote HTTP or SSE endpoint, as address. On Windows, this gave full shell access; on macOS and
well as handling authorization. However, versions 0.0.5 to 0.1.15 Linux, the impact was more limited but still allowed running
were subject to a critical remote code execution vulnerability. executables. While this specific tool is largely outdated, the
Disclosed by JFrog in July 2025, CVE-2025-6514 is now mostly incident underscored a real risk: connecting to unvetted MCP
historical since remote transport has been folded into newer servers can expose client machines to remote code execution.
Malicious MCP Server In-The-Wild
Researchers at Koi Security discovered the first known The attack exploited MCP’s design for autonomous AI use.
malicious MCP server in the wild. The package, called postmark- Once installed, the tool handled email operations hundreds of
mcp, posed as a legitimate tool for integrating the Postmark times a day with no human review of individual actions. The
email service with AI assistants. It had been downloaded hidden BCC field was invisible to the AI assistant and triggered
roughly 1,500 times per week before being removed from npm. no anomaly detection. When Koi’s researchers contacted the
The developer maintained a credible GitHub presence and 15 developer, they received no response, but the package was
clean versions before introducing a backdoor in version 1.0.16. quietly deleted from npm shortly afterward. That removal does
That update added a single line of code that silently BCCed not help the organizations already running the compromised
every outgoing email to an external address controlled by the version, which continues to exfiltrate emails even though the
developer. Password resets, invoices, internal communications, package is no longer publicly available. The incident highlights
and confidential documents were all copied without any a fundamental problem with the MCP ecosystem: developers
indication to users or their AI assistants. routinely grant powerful permissions to tools built by strangers,
and there is no meaningful security model to catch this kind
of abuse before the damage is done.
Agent-to-Agent Protocol (A2A)
MCP defines how agents connect to tools and data sources; each other’s capabilities through published metadata files
A2A addresses how agents work with each other. Google called Agent Cards, negotiate how they want to interact, and
introduced the Agent2Agent Protocol (A2A) in April 2025 coordinate on tasks that might take hours or days to complete,
as an open standard for letting AI agents from different all without exposing their internal logic, memory, or proprietary
frameworks and vendors collaborate as peers rather than one systems.
simply invoking another as a tool. Agents using A2A discover
37 38

Agent in the Middle Attack
Trustwave’s SpiderLabs researchers demonstrated a could do everything really well and should always be picked.
vulnerability in Google’s Agent-to-Agent Protocol that allows When a user asked a straightforward currency conversion
a compromised or malicious agent to intercept all tasks in a question, the host agent’s reasoning process acknowledged
multi-agent system. The attack exploits how A2A works: when that the currency converter was the obvious choice, but
a user makes a request, a host agent queries the available ultimately selected the rogue agent anyway because of its
remote agents by fetching their “agent cards,” which describe inflated self-description. The researchers dubbed this an
each agent’s name, capabilities, and endpoint. The host agent “Agent-in-the-Middle” attack, drawing a parallel to traditional
then decides which agent is best suited for the task based network-based man-in-the-middle exploits. An attacker who
on those descriptions. The problem is that nothing stops an compromises even a single agent in an A2A infrastructure
agent from lying. By crafting an agent card with an exaggerated could use this technique to route all user data through their
description claiming it can handle everything and should always controlled endpoint, either passively harvesting sensitive
be prioritized, a rogue agent can manipulate the host’s decision- information or actively returning falsified results that could
making and get selected for every task, regardless of whether influence downstream business processes.
other agents are clearly more appropriate.
As A2A sees wider enterprise adoption, additional vulnerabilities
In a proof of concept, the researchers set up four agents, beyond agent selection manipulation are likely to emerge. The
including a currency converter, a weather service, a simple protocol remains an active area of security research.
repeater, and a “RogueAgent” whose description claimed it
Agent Payments Protocol (AP2)
Google’s Agent Payments Protocol (AP2), released in 2025, shopping agent toward malicious merchants, and user intent
addresses a gap in the agentic stack: how to authorize and mandates could gradually poison model retraining, causing
verify financial transactions made by autonomous agents. persistent misinterpretation of requests.
AP2 uses cryptographically signed “mandates” that specify
what an agent can do, under what conditions, and up to what The agentic architecture creates infrastructure-level concerns
amount. The protocol extends both A2A and MCP, supporting that traditional payment security wasn’t designed to handle.
credit cards, bank transfers, and cryptocurrency. Container escapes could let malicious agents coordinate
attacks through shared A2A channels. Service mesh poisoning
While AP2’s cryptographic mandate system addresses obvious could redirect mandate flows to fake issuers. Memory
concerns around authorization and accountability, security poisoning attacks on the embedding spaces used by context-
researchers have identified risks that traditional threat models aware agents could corrupt how sub-agents interpret user
don’t capture well. Analysis using the Cloud Security Alliance’s intent, leading to erroneous purchases when no human is in
MAESTRO framework, designed specifically for agentic AI the loop. Prompt injection remains a persistent threat, with
systems, reveals vulnerabilities rooted in the autonomous, compromised instructions potentially hijacking delegation
multi-agent nature of AP2 deployments. Sub-agents in a workflows and bypassing intent checks entirely. Security
shopping workflow could collude to skip authentication steps analyses have also noted that A2A’s OAuth-derived tokens
or ignore high-risk merchant flags. Attackers might exploit sometimes lack enforced expiration, allowing long-lived
time-triggered behaviors to approve high-value transactions bearer tokens to enable replay attacks. Studies have reported
during off-hours when monitoring is reduced. The protocol’s impersonation success rates as high as 40% in unsecured
reliance on LLM-powered agents also introduces model- multi-agent simulations with consequences ranging from
specific attack surfaces: adversarial fine-tuning could bias a privilege escalation to unauthorized transactions.
37 3388

Agent Memory/RAG Poisoning
Agentic systems maintain a persistent state across multiple content at runtime, resulting in unsafe outputs without any
memory mechanisms - working memory, episodic memory, access to the model’s training pipeline.
semantic memory, and retrieval-augmented generation (RAG)
systems. Each presents a distinct attack surface. Malicious actors can also deliberately corrupt or manipulate
an AI agent’s memory mechanisms to alter its behavior or
RAG poisoning exploits agentic systems’ reliance on external decision-making processes. This can be done in a few different
data sources by injecting malicious content into knowledge ways. Adversaries can, for example, inject false or misleading
bases, vector databases, or documents that agents are information into the agent’s conversation or interaction history,
likely to retrieve. When an agent queries for information, affecting the episodic memory and causing the agent to make
poisoned documents return with embedded instructions, decisions based on fabricated past events. The working memory
misinformation, or directives that influence subsequent (or the context) can also be manipulated by feeding the agent
actions. Unlike training-time poisoning, which requires access with carefully crafted inputs that skew its understanding
to model development pipelines, RAG poisoning only requires of the current situation. State contamination occurs when
the ability to place content where retrieval systems might find attackers corrupt the internal state representations that
it, whether through compromised internal knowledge bases, the agent uses to maintain continuity across interactions,
manipulated web content, or malicious documents in shared potentially causing persistent behavioral changes. Agent
repositories. Security Bench (ICLR 2025), a comprehensive agent security
benchmarking framework, found that while isolated memory
Recent research has demonstrated the severity of these poisoning attacks achieved 7.92% average success rates across
vulnerabilities. PoisonedRAG (USENIX Security 2025) achieved 13 LLMs, mixed attacks combining memory poisoning with
attack success rates approaching 97% in controlled settings prompt injection reached 84.30% success rates. These attacks
by injecting only a handful of malicious documents into large are particularly dangerous in agentic systems because they
knowledge databases, forcing RAG systems to generate can lead to cascading failures where the poisoned memory
attacker-chosen responses. AgentPoison (NeurIPS 2024) influences not just immediate responses but also long-term
extended these attacks to agentic systems, achieving over planning and multi-step reasoning processes, making the
80% attack success rates with poison rates below 0.1% across AI agent unreliable or even adversarial in its actions while
simulated autonomous driving agents, knowledge-intensive appearing to function normally.
QA systems, and healthcare EHR agents. A concrete real-
world example of RAG poisoning was demonstrated by Pliny For organizations deploying agentic systems with access
the Liberator against Alibaba’s Qwen models. By seeding to sensitive data or decision-making authority, memory and
malicious text across the internet months in advance, the retrieval vulnerabilities warrant the same scrutiny as traditional
attacker later caused Qwen 2.5’s search tool to retrieve the application security concerns.
AI Supply Chain Security
The AI supply chain continued to expand in 2025, and so did its calls to perform hidden actions, manipulation of configuration
attack surface. The majority of organizations now depend on files hidden in popular repositories can be used for several
pre-trained models, third-party datasets, and hosted inference nefarious purposes, and namespace hijacking that lets
services for their AI deployments and integrations, and each attackers impersonate trusted publishers. Real-world incidents
of these dependencies can be targeted by adversaries. like the Salesloft Drift breach and the s1ngularity campaign
Researchers have demonstrated that injection of persistent have made clear that the attackers are actively exploiting
backdoors into a model’s computational graph can hijack tool the trust relationships that hold the AI ecosystem together.
3399 40

Persistent Backdoors
HiddenLayer researchers demonstrated that backdoors created model to ONNX format and then to TensorRT, the backdoor
using their ShadowLogic attack technique persist through remained fully functional at each step. When they simulated
model format conversions and remain fully effective even after the common practice of fine-tuning a model on clean data
downstream fine-tuning. The technique works by embedding before deployment, the ShadowLogic backdoor remained
malicious logic directly into a model’s computational graph completely intact while a conventional fine-tuning-based
to bias output, rather than manipulating the model’s learned backdoor dropped from 74% effectiveness to just 36%. This
weights through poisoned training data. In their demonstration, happens because the ShadowLogic technique modifies the
the researchers created a simple image classification model for model’s architecture itself to manipulate output rather than
use in a security camera application. They then injected logic poisoning the training data to manipulate the model’s learned
into the model’s computational graph that would suppress the weights, so the malicious logic is preserved regardless of how
“person” classification if a red square was present in the top- the weights are adjusted during subsequent training.
left corner of an input image. The backdoor achieved a 100%
success rate on samples where the trigger was present, while The implication for supply chain security: once a model is
maintaining the model’s original accuracy on clean inputs. compromised with a ShadowLogic backdoor, standard
practices like format conversion and task-specific fine-tuning
The key finding is that ShadowLogic backdoors survive will not remove it. Moreover, the backdoor can be embedded in
transformations that would normally degrade or totally formats like ONNX that are generally considered safe because
eliminate the effectiveness of conventional backdoors. they do not allow arbitrary code execution.
When the researchers converted the backdoored PyTorch
Agentic ShadowLogic
Looking to expand their ShadowLogic work into the realm tokens into the output. The backdoor lies in wait until it
of agentic AI, HiddenLayer researchers injected a backdoor recognizes that the model is within a tool call block. Once
into an ONNX version of Phi4-mini-instruct - a model built this trigger activates, the backdoor logic waits until :// becomes
with tool calling support. They discovered it was possible to the next predicted token in the sequence. If this occurs, the
manipulate tool calls into taking hidden actions. The backdoor backdoor activates and injects the URL of the attacker-owned
they created was designed to proxy network requests made via server into the tool call argument, thereby proxying the request
a tool call through an attacker-owned server, enabling potential and response through it. If this does not occur, the model
exfiltration of sensitive data and Man-in-the-Middle attacks. continues as normal.
The two-stage trigger for this backdoor consists of the This means that unbeknownst to the user, the request and
detection of specific tokens as they are about to be generated response traffic from any tool call that contains a URL in the
by the model. The subsequent step injects attacker-defined argument is being proxied through the attacker’s server:
User Prompt Model Response Actual Network
Request in Tool Call
Summarise the The content fetched
content at from the URL https://attacker-proxy.
https://example.com https://example.com com/?target=https://
is the following: ... example.com
39 4400

Malicious Config Files
While previous research in AI supply chain security has One recent study found tens of thousands of Hugging Face
concentrated mostly on the models themselves, covering repositories to contain malicious or suspicious config files.
threats like malicious payload injection and logical backdoors, Among those config files, the researchers identified three
the auxiliary files that accompany these models have been attack scenarios: file operations that can load unauthorized
largely overlooked. Platforms like Hugging Face host pretrained or harmful files, website operations that allow access to
models alongside configuration files contributed by the public, unknown websites, exposing users to risks inherent to that,
and while these files are intended to simply set up models with and repository operations that can manipulate how models
the right parameters and initial settings, they can be exploited are fetched and executed.
to execute unauthorized code.
These attacks are tricky to catch as configuration files vary
Configuration files occupy a dangerous gray zone between widely across frameworks. Each model framework uses configs
data and code, making them a stealthy attack vector. While with different structures, contents, and dependencies, making
developers instinctively treat JSON or YAML configs as harmless it hard to build any single detection tool that works across
settings, these files can trigger code execution through the board. Attackers can package a custom config alongside
several mechanisms: they can redirect remote code loading a seemingly legitimate third-party library, tricking users into
to attacker-controlled repositories via fields like auto_map in running malicious code without realizing it. As a solution, the
Hugging Face’s config.json, or they can exploit unsafe YAML researchers proposed ConfigScan - a tool that uses LLMs
parsing (as seen in CVE-2025-50460). Config files can also to analyze configs in the context of their runtime code and
abuse deserialization in model-loading code, such as the Keras documentation. HiddenLayer also introduced a solution to
vulnerability (CVE-2025-49655, disclosed by HiddenLayer in detect repository sideloading, which identifies discrepancies
October 2025), where a malicious config.json embedded in in configuration files that could lead to code from external
a .keras file triggers arbitrary code execution through unsafe repositories being unintentionally loaded. However, the broader
deserialization. AI community has still to catch up on this particular attack
surface.
Tokenizer and Chat Template Manipulation
In keeping with the attacks laid out in the two previous that if an unsuspecting user were to load the model and input
subsections, HiddenLayer research team uncovered a way a prompt as simple as: “Hi there”, and the logic in the chat
to manipulate a model’s tokenizer and chat template to template is satisfied, the model will not respond to the user’s
manipulate tool calls for malicious purposes. prompt, but will instead call the tool with those arguments
specified by the attacker.
The team discovered that it was possible to simply modify
a model’s tokenizer.json file for this purpose. For example, Despite the fact that these attacks may become obvious to
changing the value for the token ID representing :// to :// some victim users before too long, it may already be too late
attacker-proxy.com/?target=https:// would result in the by that point, and sensitive data may have been leaked, an
proxying of a tool’s network requests through the attacker- attacker may have already gained all the access they needed
defined server address, as per the Agentic ShadowLogic to move to the next stage of an attack, or important files
backdoor. The attack also works with the GGUF model file may have already been deleted. It is therefore imperative that
format, where the attacker can modify the tokenizer values such attacks can be identified before models are deployed,
under the file’s tokenizer.ggml.tokens metadata field for the which can be achieved through scanning the relevant data
same impact. fields. With tokenizer manipulation, for example, developing
knowledge of how different tokenizer types are built allows
In a similar attack scenario, the team was able to inject logic us to understand how these attacks affect the integrity of a
into a model’s chat template to look for the presence of a given tokenizer, which gives us identifiable characteristics for
particular tool name within the model ecosystem and, if building detections.
present, invoke it with attacker-defined arguments. This means
41 42

Namespace Reuse Attacks
Unit 42 researchers discovered a supply chain attack vector the original owner is subsequently deleted, the old namespace
through reusing deactivated namespaces in Hugging Face. The becomes available for registration, and a malicious actor
attack exploits how Hugging Face manages model namespaces who claims it can break the redirect chain, causing their
after an organization or user deletes their account. When compromised model to take priority over the legitimate
an organization is deleted, its unique namespace becomes transferred model. Users experience no downtime and
available for re-registration by anyone, but cloud platforms and see no errors, so they have no indication that anything has
code repositories that reference the original model continue changed. The researchers found thousands of open-source
to pull from that namespace. An attacker can register the repositories with hard-coded references to reusable model
abandoned name, upload a malicious model using the same namespaces, including popular and highly starred projects.
path, and any pipeline still referencing the original model will They recommend version pinning to specific commits rather
unknowingly deploy the compromised version instead. This than pulling latest versions by name, cloning models to trusted
flaw affects thousands of open-source projects, as well as internal storage after verification, and scanning codebases for
major AI platforms that allow direct deployment of models model references that could be hijacked. Google has since
from Hugging Face. The researchers demonstrated an attack implemented daily scans to identify orphaned models and
scenario in which they took over several orphaned namespaces mark them as non-deployable.
and embedded reverse shell payloads that gave them access to
the underlying infrastructure when the models were deployed Another attack vector targeting Hugging Face is the Model
on Vertex AI and Azure AI Foundry. Confusion attack, which is similar to dependency confusion,
but takes advantage of pretrained model loading in an AI setting.
The problem is compounded by Hugging Face’s ownership When code used to load model weights references a path that
transfer feature. When a model is transferred to a new owner, doesn’t exist locally, the HuggingFace transformers library
the platform maintains redirects from the old namespace to automatically attempts to download the relevant files from a
the new one so existing pipelines continue working without hosted repository with the same name as the referenced path,
code changes. However, if the organization associated with potentially pulling and loading attacker-controlled files instead.
Salesloft Drift AI Supply Chain Attack
In August 2025, a supply chain breach through Salesloft’s Drift Snowflake tokens, cloud credentials, and passwords retrieved
AI chatbot application impacted over 700 organizations. The from support tickets.
attack was attributed to a threat group tracked as UNC6395
or GRUB1 and prompted FINRA (Financial Industry Regulatory The implications of such a large supply chain breach through
Authority) to issue a cybersecurity alert to member firms, SaaS integrations are of particular concern in normal
warning that the stolen data could be used for credential circumstances, given the blast radius. However, this could
stuffing, spear phishing, and social engineering campaigns be amplified further considering the broad level of access
targeting financial institutions and their vendors. AI systems such as chatbots typically have when it comes
to retrieving sensitive data. FINRA advised affected firms to
The attackers obtained and exploited compromised OAuth immediately sever all Salesloft integrations, rotate any exposed
tokens for the Drift application, enabling them to access credentials, forensically review audit logs for unauthorized
connected systems such as Salesforce, Google Workspace, and activity between August 8 and 18, and stay alert for follow-on
Slack. From here, they exfiltrated business contacts, Salesforce attacks exploiting the stolen contact information.
records, and in some cases more sensitive material: API keys,
41 4422

S1ngularity
In another high-profile supply chain attack in August 2025, uploading it to public GitHub repositories.
adversaries exploited an injection vulnerability in a GitHub
Actions workflow to steal the NPM publishing token of Nx, a The incident illustrates how AI tools are becoming attack
popular developer build system. They used the token to publish vectors themselves. Compromised developer machines often
malicious packages in order to compromise unsuspecting end serve as entry points into production cloud workloads, meaning
users. The attack, dubbed s1ngularity, injected a post-install stolen tokens or SSH keys can translate into full control of
script that harvested GitHub tokens, SSH keys, npm credentials, cloud infrastructure. By the time GitHub disabled the attacker-
and crypto wallets from Linux and macOS machines. While not controlled repositories the next morning, thousands of secrets
specifically targeting AI, it was the first known supply chain had likely already been exposed. Orca’s previous research found
attack to scan for locally accessible AI tools on compromised that exposed secrets on GitHub are typically discovered by
machines and use them to extract the secrets. The malware attackers in under two minutes. The attack follows a pattern
attempted to use the command-line interface of tools such seen with other recent incidents like the XZ Utils backdoor
as Claude, Gemini, and Amazon Q, utilizing a set of hardcoded and various typosquatting campaigns, demonstrating that
prompts in order to search for confidential data on the affected attackers are increasingly targeting trust relationships within
system. According to Orca’s analysis, the attackers exploited AI open-source ecosystems and that defenders need to extend
developer tools with weak security defaults, using permissive their focus beyond runtime workloads to secure the entire
flags like “--dangerously-skip-permissions” and “--yolo” to developer pipeline.
bypass protections, then obfuscated the stolen data before
OpenClaw
The end of 2025 brought another major shift in the AI threat default, user secrets are stored in plaintext, and the system
landscape with the release of OpenClaw (formerly ClawdBot) prompt can be silently modified by an attacker to persist
- an open-source, locally-run AI assistant that serves as an malicious instructions across sessions. These weaknesses
agentic interface for autonomous workflows. OpenClaw make OpenClaw highly susceptible to prompt injection attacks,
integrates with LLMs like Claude and ChatGPT to handle which can escalate quickly into remote code execution,
tasks ranging from calendar management and web browsing credential theft, and long-term system compromise. With
automation to running system commands, all controllable hundreds of thousands of deployments, many of them
through popular messaging apps. Its ease of setup fueled rapid internet-exposed, a single well-crafted malicious webpage
adoption, with the project amassing over 200,000 GitHub stars or rogue skill file could potentially affect a vast number of
in just a few months. users at once.
Part of its viral appeal is Moltbook, an AI-exclusive forum where The skills framework only adds to this risk. There is no vetting
agents interact and share “experiences” with one another. process or way to distinguish legitimate skills from malicious
Agents can also expand their capabilities through skills, which ones, so anyone with a GitHub account can publish skill files
are YAML-formatted instruction files that can be published that agents will readily consume and execute. This has already
by users and discovered by agents via skill repositories such proven to be more than a theoretical concern: several malicious
as ClawHub. skills were found in the wild instructing OpenClaw agents to
silently download and run an infostealer malware designed
This popularity, however, comes with serious caveats. to harvest credentials, browser data, and sensitive files. With
OpenClaw’s architecture delegates nearly all security-critical no trust or verification model in place, the skills ecosystem
decisions to the underlying language model, an inherently essentially becomes a ready-made distribution channel for
unreliable gatekeeper once untrusted content enters the malware, and its reach only grows as OpenClaw’s user base
picture. Tools like exec and web_fetch run unsandboxed by expands.
43 44

Hugging Face Updates
Hugging Face saw significant growth in 2025, crossing the Transformers library grew from 40 model architectures in
two-million model mark in its repository. Improved tooling, a version 4 to over 400, with more than 750,000 compatible
broader contributor base, and the rise of smaller fine-tuned checkpoints now available. According to Hugging Face, the
models all contributed to this momentum. The platform’s library is currently installed over 3 million times daily.
Growth Acceleration
Hugging Face continued to grow, reaching 2.5 million repositories housing more than 15 million models as of January 2026. This is
up from roughly 1.2 million repositories and 5 million models one year ago.
Cumulative Repositories Cumulative Repositories
43 44
seirotisopeR
evitalumuC
htnoM
seirotisopeR
evitalumuC
Hugging Face Repository Growth Over Time
2,500,000
120,000
2,000,000
100,000
1,500,000 80,000
60,000
1,000,000
40,000
500,000
20,000
0
0
2022 2022 2022 2022 2023 2023 2023 2023 2024 2024 2024 2024 2025 2025 2025 2025 2026
/01 /04 /07 /10 /01 /04 /07 /10 /01 /04 /07 /10 /01 /04 /07 /10 /01
44

Most Popular Model File Formats
Our data covers 22 file extension types totaling 15,325,540 files  large but fewer in number, suggesting they represent larger,
and 28.18 PB of storage. Seventy-five percent of storage is split  quantized models. Unsafe, pickle-based formats (extensions
between two formats (.safetensors and .gguf), indicating strong  such as .bin, .pt, .pth, and .pkl) remain highly popular, accounting
standardization around safe model formats. While .safetensors  for around 40% of all model files.
dominate by both count and size, .gguf files are nearly as
FILE EXTENSION FILES COUNT FILES COUNT (%) FILE EXTENSION TOTAL SIZE TOTAL SIZE (%)
| .safetensors | 5,526,630 | 36.06% | .safetensors | 10.62 PB  | 37.68% |
| ------------ | --------- | ------ | ------------ | --------- | ------ |
| .pt          | 2,794,927 | 18.24% | .gguf        | 10.55 PB  | 37.45% |
| .gguf        | 2,440,937 | 15.93% | .pt          | 4.38 PB   | 15.53% |
| .bin         | 2,002,108 | 13.06% | .bin         | 1.10 PB   | 3.92%  |
| .pth         | 976,064   | 6.37%  | .pth         | 413.19 TB | 1.43%  |
| .pkl         | 867,975   | 5.66%  | .part1of2    | 385.08 TB | 1.33%  |
| .zip         | 292,468   | 1.91%  | .part2of2    | 375.54 TB | 1.30%  |
| .onnx        | 187,455   | 1.22%  | .tar         | 101.71 TB | 0.35%  |
| .ckpt        | 72,968    | 0.48%  | .zip         | 93.71 TB  | 0.32%  |
| .tar         | 51,706    | 0.34%  | .ckpt        | 85.18 TB  | 0.30%  |
| .h5          | 31,117    | 0.20%  | .pkl         | 27.16 TB  | 0.09%  |
| .pb          | 28,992    | 0.19%  | .h5          | 20.36 TB  | 0.07%  |
| .part1of2    | 12,704    | 0.08%  | .onnx        | 17.61 TB  | 0.06%  |
| .part2of2    | 12,702    | 0.08%  | .engine      | 16.61 TB  | 0.06%  |
| .keras       | 8,467     | 0.06%  | .rkllm       | 15.20 TB  | 0.05%  |
| .pickle      | 6,261     | 0.04%  | .llamafile   | 11.09 TB  | 0.04%  |
| .hdf5        | 3,537     | 0.02%  | .pickle      | 1.78 TB   | 0.01%  |
| .engine      | 3,349     | 0.02%  | .keras       | 1.38 TB   | 0.00%  |
| .rkllm       | 2,548     | 0.02%  | .hdf5        | 828.90 GB | 0.00%  |
| .mlmodel     | 1,510     | 0.01%  | .pb          | 344.63 GB | 0.00%  |
| .llamafile   | 1,110     | 0.01%  | .mlmodel     | 15.70 GB  | 0.00%  |
| .pmml        | 5         | 0.00%  | .pmml        | 1.41 MB   | 0.00%  |
45 46

New Model Formats
This year’s data includes the following new / previously unreported formats:
| .engine  | .rkllm  | .llamafile   |
| -------- | ------- | ------------ |
TensorRT engine files used for  Rockchip LLM format  Introduced by Mozilla in late 2024;
high-performance inference  used for running LLMs on  combines a GGUF model with a
on NVIDIA GPUs Rockchip NPU/accelerator  runtime into a single executable file
| chips in embedded  | to allow running models without         |     |
| ------------------ | --------------------------------------- | --- |
|                    | devices. separate runtime installation. |     |
45 4466

Part 3
ADVANCEMENTS IN SECURIT Y FOR AI
As the AI threat landscape rapidly evolves, defenders are trying and initiatives, as well as brand new tools and projects. The
to keep up the pace. 2025 brought a wealth of developments in focus this year was understandably on securing GenAI and
the AI security field, including updates to existing frameworks agentic systems.
Defensive Frameworks and Initiatives
MITRE
MITRE kept expanding its ATLAS framework through In May 2025, MITRE proposed SAFE-AI - a defender-
2025, adding new entries on an almost monthly basis. The focused framework that maps ATLAS threats to four
data upgrade to version 5 introduced a new “Technique system elements (environment, AI platform/tools, AI
Maturity” field that evaluates techniques based on models, and AI data) and connects them to relevant NIST
feasibility, demonstration, and real-world application, SP 800-53 controls. This helps organizations translate
providing a way to prioritize threats organizations should threat intelligence into actionable security requirements,
focus on. The framework also continued documenting giving security teams practical guidance on which
real-world incidents, expanding ATLAS case studies with controls to implement, how to assess them, and what
LLMJacking, Hugging Face Organization Confusion, and residual risks remain after mitigation.
LAMEHUG, among many others. The latest release of the
framework from December 2025 catalogs 16 tactics,
91 techniques, 56 sub-techniques, 35 mitigations, and
45 case studies.
4477 4488

CoSAI
Celebrating its first anniversary in July 2025, Coalition AI fundamentally changes organizational risk profiles,
for Secure AI continued to publish new guidance and identifies gaps in existing security frameworks, and
frameworks. Their Principles for Secure-by-Design provides six critical areas where security teams must
Agentic Systems proposes three foundational principles adapt.
(human governance and accountability, bounded and
resilient design, and transparency/verifiability), along with CoSAI also introduced an AI Incident Response Framework,
practical implementation strategies for agent developers, published guidance on operationalizing the CoSAI Risk
adopters, and security engineers to balance autonomy Map, guidance on securing AI agents, and a paper on
with security in autonomous AI agents. A whitepaper model signing as a foundational solution for AI supply
called Preparing Defenders of AI Systems outlines how chain security.
AIBOM
The concept of AI Bills of Materials gained real Conference 2025 and later contributed to the OWASP
momentum in 2025. The Linux Foundation published a GenAI Security Project. OWASP has also formally launched
comprehensive guide for implementing AI BOMs using its own AIBOM Project. The project is organized into 10
SPDX 3.0, expanding on the software bill of materials strategic workstreams, each focused on a critical aspect
concept to include documentation of algorithms, data of AI transparency and security, covering everything from
collection methods, frameworks and libraries, licensing format standardization to tooling development to policy
information, and standard compliance. The SPDX 3.0 guidance.
extension comprises 36 new fields that treat datasets,
models, and their provenance as first-class supply-chain Together, these efforts are moving AIBOM from theory
elements to address the trustworthiness challenges of into repeatable, community-maintained implementation,
AI systems. helping organizations understand the models they rely
on, the risks that accompany them, and the compliance
An open-source tool that generates AIBOMs for models obligations they must meet.
hosted on Hugging Face was introduced at the RSA
4477 444888

OWASP
OWASP remained very active in the field of AI Security. rogue agents that look fine while quietly doing damage.
Their Top 10 for LLM Applications received a significant None of this is theoretical. OWASP’s tracker already has
2025 update reflecting how these models are now documented incidents of agents being used for data
deployed in practice. New entries address issues such theft and remote code execution.
as vector and embedding weaknesses in retrieval-
augmented generation systems, system prompt leakage, OWASP has also started an Agentic Security Initiative,
and unbounded consumption. publishing a threats and mitigations document which
got picked up faster than most security guidance does.
The final version of OWASP Top 10 for Agentic Microsoft references it in their agentic failure modes
Applications was released in December. The ten risks documentation, NVIDIA folded parts of it into their own
run from goal hijacking and tool misuse through memory safety framework, and AWS has incorporated chunks of
poisoning, sketchy agent-to-agent communication, and it into their recommendations.
NIST
NIST’s AI Risk Management Framework (AI-RMF) received was developed with input from more than 6,500
several updates in 2025, expanding the framework’s individuals over the course of a year, and its final version
threat taxonomy to address generative AI vulnerabilities is expected to be published in the coming months.
and strengthening guidance on supply chain risks and
third-party AI components. NIST has also adapted SP In other developments, NIST invested $20 million to
800-53 - its catalog of security and privacy controls for establish two new centers with MITRE, one focused
federal information systems - to fit AI-specific security on AI for manufacturing productivity and the other on
concerns. protecting critical infrastructure from cyber threats. The
critical infrastructure center will concentrate on real-time
December brought a preliminary draft of NIST’s Cyber threat detection, predictive analytics, and automated
AI Profile - a framework based on the Cybersecurity response capabilities. NIST also plans to announce up to
Framework 2.0 that provides guidelines for managing $70 million for an AI for Resilient Manufacturing Institute
cybersecurity risks related to AI systems. The initiative through the Manufacturing USA program.
4499 50

MAESTRO
In February, Cloud Security Alliance released its Agentic AI goals, multiple agents quietly colluding, memory getting
Threat Modeling Framework called MAESTRO. It provides poisoned in ways that corrupt future decisions, or chains
a seven-layer threat model that works through foundation of tool calls going sideways in hard-to-predict ways.
models, data pipelines, agent frameworks, infrastructure, People have already used it to pick apart OpenAI’s
observability, compliance, and the messier reality of Responses API and Google’s Agent-to-Agent protocol, and
multiple agents operating in the same environment. The some academic work applied it to network monitoring
point was to capture risks that traditional frameworks agents and found attack vectors that weren’t obvious
completely ignore: agents drifting from their intended beforehand.
Model Signing
In April 2025, the OpenSSF AI/ML Working Group released trace its origins back to whoever created it.
version 1.0 of the Model Signing Project, developed in
collaboration with contributors from Google, NVIDIA, and The specification supports any model format and size, offers
HiddenLayer. The framework provides a library and command- flexible key infrastructure options including Sigstore and self-
line interface for cryptographically signing and verifying signed certificates, and aims to provide traceable origins and
machine learning models of any format or size. provenance throughout the AI supply chain. The intended
workflow involves signing models after training, then verifying
The initiative addresses a growing gap in ML supply chain those signatures at each subsequent stage: when uploading
security. The teams that train foundation models are rarely the to a hub, when selecting a model for deployment, and when
same ones deploying them to production, and with pretrained loading a model at runtime. The working group plans to further
models proliferating across hubs like Kaggle and HuggingFace, expand this initiative into dataset signatures and broader ML
there’s been no reliable way to confirm that an uploaded model artifact verification.
actually matches what was produced during training, or to
Taxonomy of Adversarial Prompt Engineering
HiddenLayer published the APE taxonomy in June 2025 to The taxonomy builds on the familiar Tactics, Techniques, and
bring more precision to how the security community talks Procedures model from cybersecurity but adds objectives as
about prompt injection attacks. While “prompt injection” has a separate layer. This keeps observable behaviors distinct from
become a catch-all term, there’s actually a wide range of inferred intent, so analysts can tag what a prompt actually
distinct techniques that existing frameworks like OWASP’s does without having to speculate about why. Prompts sit at the
Top 10 for LLMs and MITRE ATLAS don’t capture at a granular most granular level as the actual text fed to an LLM. Techniques
enough level to guide actual defenses. The APE taxonomy abstract patterns from those prompts into reusable categories,
is complementary to these existing frameworks and can like refusal suppression, which describes explicitly instructing a
act as a subtree under their prompt injection categories. It’s model not to refuse a request. Tactics group related techniques
also a community-driven effort, inviting contributions from into broader clusters, so something like Tool Call Spoofing and
practitioners and researchers to keep it current as the threat Conversation Spoofing both fall under Context Manipulation
landscape evolves. because they exploit similar weaknesses.
49 50

Model Genealogy
With the ever-growing availability of different AI models around discovered in RoBERTa, DeBERTa, and DistilBERT models, but
the world, the ability to identify lineage and architectural origins all three also had their own distinct architectures that could
has become highly important. In some countries, such as be used to differentiate them in signature building.
Australia, for example, the use of DeepSeek was banned.
However, it is not always that easy to know if a model is derived As new models are released, the team keeps on top of
from, or is indeed itself, a banned model family. A technique understanding their architectures and building out signatures
that aims to address this issue, ShadowGenes, was published for them. An example of how this is done is laid out in this blog,
by HiddenLayer in early 2025 and is in continual development. which demonstrates how initial signatures for DeepSeek were
developed. Livehunting across model hubs is performed to
The research grew out of earlier work on creating detection test signatures against new models and new architectures,
signatures for ShadowLogic, an attack technique focused on and almost a year later, many more model families and
manipulating model output by injecting malicious logic into architectures are supported, including LLaMa, Phi, Mistral,
computational graphs. While analyzing patterns within the Qwen, and, of course, DeepSeek.
graphs to build these signatures, the team started to recognize
patterns that enabled them to identify a model’s family and The practical benefits center on supply chain transparency
lineage. The team adapted its ShadowLogic signature detection and compliance. Organizations can verify that models match
process to track and identify genealogical relationships and their claimed architectures and flag models with unrecognized
model families. For example, patterns indicative of BERT were lineage for review.
The State of AI Red Teaming
There were many advancements in maturing the process of Automated tooling for AI Red Teaming has also seen a
AI red teaming in 2025. As discussed earlier, the development number of advancements. Many tools originally developed
of the Adversarial Prompt Engineering Taxonomy has brought in 2024 helped lay the groundwork for testing AI models and
structure to defensive initiatives, as well as to pentesting applications leveraging them. Throughout 2025, there have
engagements. The APE taxonomy provides a repeatable been improvements in moving beyond static prompts towards
prescriptive framework for AI red teams to ensure adequate AI-powered tools that adapt more intelligently to systems being
coverage of techniques used by adversaries, giving assessed. These types of tools have yet to replace a dedicated
organizations a clear picture of the overall risk AI systems human AI red teamer; however, this gap is closing fast.
pose to their business.
New Guidance & Legislation
2025 marked a decisive shift in global AI governance. Across Rather than converging on a single regulatory model, regulators
major jurisdictions, AI regulation moved from principle- aligned around a set of cross-cutting enforcement themes
setting and voluntary guidance into enforcement-driven that directly mirror the technical and operational risks outlined
accountability. While regulatory approaches diverged, from earlier in this report. These themes will shape compliance
the European Union’s risk-based framework to the United expectations and enforcement actions through 2026 and
States’ innovation-first posture, a common theme emerged. AI beyond.
risk is no longer theoretical, and governments are increasingly
treating AI failures as enforceable violations of existing law.
5511 52

51 5522

Risk-Based Regulation Becomes the Default Control Model
What changed in 2025
Regulators largely abandoned one-size-fits-all AI rules in favor of tiered, impact-driven frameworks. The EU AI Act
operationalized this approach most explicitly through graduated risk categories, while similar logic appeared globally,
including U.S. agency enforcement priorities, Japan’s sectoral guidance, and China’s differentiated controls for consumer-
facing versus infrastructure AI.
Why it matters
“AI” is no longer regulated as a single category. Obligations increasingly hinge on how and where systems are used,
particularly in domains already highlighted in this report as high-risk: identity verification, fraud detection, cybersecurity,
healthcare, and national security. This pushes organizations toward use-case mapping and system inventories, not just
tracking models in isolation.
What to watch
Expect continued expansion of what qualifies as “high risk,” particularly as AI systems take on greater autonomy and
decision-making authority, echoing the agentic and misuse-driven threats described earlier.
Enforcement Accelerates Through Existing Legal Authorities
What changed in 2025
In the United States, regulators increasingly relied on existing legal authorities rather than waiting for AI-specific statutes.
Agencies such as the FTC, DOJ, and sector regulators treated AI failures as amplified versions of familiar violations like
deceptive practices, discrimination, data misuse, and safety lapses. In parallel, the EU paired the enforcement of its new
AI rules with established GDPR mechanisms.
Why it matters
Organizations cannot wait for bespoke AI legislation to understand their exposure. Enforcement is faster, less predictable,
and increasingly precedent-driven. AI-related incidents, including misuse, hallucinated advice, and automated fraud, are
now framed as conventional violations executed at machine scale.
What to watch
AI-related consent decrees, settlements, audits, and documentation demands will increasingly serve as de facto regulatory
guidance, setting expectations faster than formal rulemaking.
53 54

Transparency Shifts From Disclosure to Defensible Evidence
What changed in 2025
Transparency requirements evolved beyond notifying users that AI is in use. Regulators increasingly expect organizations
to document system behavior, substantiate claims, and demonstrate mitigation of known risks. This includes training
data summaries, system limitations, human oversight mechanisms, and version tracking.
Why it matters
Transparency is becoming operational rather than cosmetic. Internal artifacts, security logs, evaluation records, and
governance documentation are now potential regulatory evidence. As shown in earlier sections on guardrail bypasses
and model misuse, undocumented or poorly understood system behavior creates both security and compliance risk.
What to watch
Regulators increasingly request technical substantiation during investigations, driving alignment pressure between
transparency obligations, secure development practices, and runtime security monitoring.
Continuous Accountability Replaces One-Time Compliance
What changed in 2025
Regulators and enforcement bodies moved away from viewing compliance as a one-time, pre-deployment exercise and
toward expectations of ongoing accountability throughout an AI system’s lifecycle. Phased implementation of new AI
regulations and increased use of existing legal authorities reinforced the need for continuous monitoring, testing, and
re-validation as models, prompts, agents, and integrations evolve.
Why it matters
AI systems are not static. Model updates, prompt changes, new tools, and shifting usage patterns can introduce regressions
or new risks after deployment. Organizations that rely solely on initial approvals or launch-time assessments increasingly
face exposure when post-deployment behavior diverges from documented intent.
What to watch
Greater emphasis on living documentation and defensible evidence, including change logs, ongoing testing results,
audit trails, and incident response records. Regulators and auditors are increasingly evaluating whether organizations
can demonstrate how risks are continuously assessed and controlled over time, not just that policies existed at launch.
53 54

Regulatory Focus Expands From Models to Full AI Systems
What changed in 2025
Regulators shifted attention from base models to end-to-end AI systems, including data pipelines, fine-tuning workflows,
third-party APIs, tool integrations, and human-in-the-loop controls. This mirrors the technical reality described throughout
this report that risk emerges at runtime, not just during training.
Why it matters
A compliant base model does not guarantee a compliant deployment. Operational behavior, integration security, and
supply-chain dependencies now shape regulatory risk. As with many of the supply-chain and agentic attack scenarios
discussed earlier, liability increasingly attaches to how systems are deployed and controlled.
What to watch
Greater scrutiny of vendor risk management, responsibility allocation between model providers and deployers, and audits
that examine inference-time behavior rather than static documentation.
AI Security and Misuse Enter the Regulatory Core
What changed in 2025
AI misuse, including deepfakes, impersonation, fraud, election interference, and automated cybercrime, became a central
driver of regulatory concern. These threats are now framed not just as technical failures, but as consumer harm, financial
crime, and national security risks.
Why it matters
AI security is no longer a best practice or internal control; it is becoming a regulatory expectation. Governance, cybersecurity,
and platform safety obligations are converging, particularly where AI systems amplify harm at scale.
What to watch
Explicit expectations for abuse monitoring, misuse detection, and security-by-design practices, including AI-specific
runtime safeguards rather than static controls.
55 56

Fragmentation vs. Harmonization Becomes a Strategic Risk
What changed in 2025
The EU AI Act exerted a strong gravitational pull on global compliance, while U.S. states continued rapid experimentation
and Asian jurisdictions diverged sharply in their approaches. Multinational organizations increasingly face layered and
sometimes conflicting obligations.
Why it matters
Compliance architecture now affects product design, market entry decisions, vendor selection, and operational security
controls. Fragmentation introduces both cost and operational risk, particularly for globally deployed AI systems and
agentic workflows.
What to watch
Efforts toward international alignment, de facto global standards emerging from EU conformity requirements, and renewed
pressure for U.S. federal preemption.
Governance Maturity Emerges as a Competitive Signal
What changed in 2025
Regulators increasingly rewarded organizations that demonstrated early risk assessment, clear accountability structures,
and mature governance, including oversight of runtime operational security.
Why it matters
AI governance is shifting from legal compliance to enterprise risk management. Boards, CISOs, and executive leadership
are being pulled directly into AI oversight, while investors and partners increasingly evaluate governance posture alongside
security maturity.
What to watch
Board-level AI oversight expectations, integration of AI risk into ERM and cyber risk programs, and the use of governance
maturity as a mitigating factor in enforcement actions.
55 56

Part 4
PREDICTIONS AND RECOMMENDATIONS
Computer Use Agents
As agentic AI matures, attackers are likely to shift from computer-use agents can navigate arbitrary applications,
generic prompt injection toward exploiting architecture- exposing them to visual spoofing attacks, UI element
specific vulnerabilities. Computer-use agents present poisoning, and malicious screen-content injection
particularly high-risk attack surfaces because they via malvertising. The very capability that makes them
operate at the UI layer with broad system access. Unlike powerful, interpreting and acting on visual information,
API-based agents constrained by structured interfaces, is likely to become their greatest frailty.
AI Personal Assistants
The rise of AI personal assistants will create a fundamental security models that rely on application sandboxing will
security paradox in 2026. For these assistants to be be insufficient when the assistant itself requires cross-
genuinely helpful, they require broad access to our digital application permissions by design. We’ll likely see the
lives: reading emails, managing calendars, handling emergence of “assistant security posture management”
messages, and interacting with files across applications. as both enterprises and individual users struggle to
This creates the perfect opportunity for exploitation. A balance the productivity benefits of AI assistance with
compromised assistant becomes a universal remote for appropriate containment and access controls.
a user’s most sensitive functions and data. Traditional
5577 5588

Agent-to-Agent Communication Exploits
As workflows increasingly involve multiple specialized AI systems. A translation agent passes subtly manipulated
agents communicating with each other, the handoff content to the summarization agent, which feeds the
points become vulnerable. An attacker who can poison decision-making agent. We anticipate a rise in rogue
the output of one agent in a chain could compromise the agents in the coming year.
entire workflow. Think of this as a supply chain attack for
Context Window Poisoning and Memory Manipulation
With agents maintaining longer-term memory and Summarization attacks present a related vector: when
context windows, there’s an emerging threat of “memory assistants condense conversation history or documents
poisoning,” where attackers insert malicious instructions to manage context limits, attackers can craft inputs
or false information into an agent’s retained context designed to survive or even be amplified through the
that influences future behavior. This is particularly summarization process, embedding persistent malicious
concerning for agents with persistent storage capabilities instructions in the compressed representation that the
and has already been exploited in coding assistants model continues to reference.
throughout the past year to trigger harmful actions.
AI Supply Chain Attacks Evolve Beyond Code
Supply chain security for AI systems has evolved in these files within open source repositories, knowing
through distinct phases: initial concerns focused on they’ll be ingested automatically when developers clone
malicious code execution in model files, followed by and work with the code. Unlike traditional supply chain
attacks targeting model artifacts like configuration attacks that require code execution, these vectors
files and repository sideloading. In 2026, we expect exploit the trust relationship between developers
the frontier to shift decisively toward prompt injection and their AI coding assistants, potentially exfiltrating
via developer tooling and workflow files. SKILL.md files, secrets, modifying generated code, or establishing
editor rules files (such as .cursorrules or .windsurfrules), persistence across projects. Security teams will need
and AI assistant plugins represent attractive new targets; to extend their supply chain scanning to include these
they’re often implicitly trusted, rarely scrutinized during AI-specific configuration files and treat them with the
code review, and are designed to directly influence AI same suspicion as executable code.
behavior. Attackers will embed malicious instructions
5577 555888

5599 60

Recommendations for the Security Practitioner
Treat AI Security as a Regulatory Control, Not a Feature Add-On
With the EU AI Act moving from policy to active implementation and enforcement, and U.S. regulators increasingly relying
on existing laws (FTC, SEC, DOJ, state AGs) to pursue AI-related failures, security teams must assume AI systems will be
audited like any other regulated infrastructure. That means traceability, risk classification, documented controls, and
provable effectiveness—not “best-effort” guardrails. If you can’t demonstrate security outcomes, you likely won’t meet
regulatory expectations.
Move Beyond Guardrails to Demonstrated Operational Security
Guardrails alone are not a security control. They are policy enforcement mechanisms that are routinely bypassed,
manipulated, or disabled. Worse, guardrails themselves become attack surfaces. Practitioners must focus on operational
security: continuous monitoring, adversarial testing, runtime validation, and incident response specific to AI behavior.
Regulators will care far more about how you detect, respond to, and contain AI misuse than whether you implemented
a safety prompt.
Assume AI Is Exploitable, Not Just Vulnerable
AI systems today are not merely vulnerable; they are actively exploitable due to the lack of strong runtime protection,
isolation, and behavior enforcement. Model inputs, outputs, plugins, agents, and orchestration layers all expand the attack
surface. Security teams should treat AI like exposed production infrastructure subject to abuse, fraud, data exfiltration,
and manipulation. This mindset shift is critical for aligning with both EU “risk-based” requirements and U.S. enforcement
actions tied to consumer harm and negligence.
Build Runtime Visibility and Control Into AI Deployments
Regulators are increasingly focused on ongoing risk, not point-in-time compliance. Security teams need visibility into
how AI systems behave in real environments: what they are asked, what they access, what they generate, and how that
behavior changes over time. Runtime protection, including monitoring, policy enforcement, anomaly detection, and kill-
switch capabilities, will be essential to demonstrate due diligence and reasonable security under both EU and U.S. legal
frameworks.
Align AI Risk With Business Impact as Adoption Accelerates
The growing benefits of AI (automation, scale, speed, and decision-making) directly amplify risk when systems are
compromised or abused. Security practitioners must help organizations understand that AI failures scale faster and farther
than traditional software failures. As AI becomes embedded in core workflows, security posture around AI will increasingly
determine regulatory exposure, brand trust, and operational resilience. Securing AI is no longer optional experimentation;
it is a requirement of enterprise risk management.
Reassess Third-Party Risk: Demand Runtime AI Security From Vendors
AI dramatically expands third-party risk, and existing vendor assurances are no longer sufficient. Security teams must require
AI vendors and service providers to clearly explain their runtime security controls, including how they monitor, detect, and
respond to AI-specific threats in production. Claims centered on guardrails, acceptable-use policies, or compliance with
frameworks such as SOC 2, HIPAA, ISO 27001, or similar standards are insufficient on their own, as these frameworks were
not designed to address AI exploitability or real-time abuse. Regulators in both the EU and the U.S. will increasingly view
downstream organizations as accountable for failures introduced through AI supply chains, making vendor transparency
and operational security non-negotiable.
59 60

HIDDENLAYER
RESOURCES
HiddenLayer Products
◉ AI Security Platform
◉ AI Discovery Module
◉ AI Supply Chain Security Module
◉ AI Attack Simulation Module
◉ AI Runtime Security Module
HiddenLayer Research
◉ Exploring the Security Risks of AI Assistants
like OpenClaw
◉ Agentic ShadowLogic
◉ EchoGram: The Hidden Vulnerability
Undermining AI Guardrails
◉ Prompts Gone Viral: Practical Code Assistant
AI Viruses
◉ Introducing a Taxonomy of Adversarial
Prompt Engineering
◉ Novel Universal Bypass for All Major LLMs
Links to learn more:
61 62

ABOUT HIDDENLAYER
HiddenLayer’s AI Security Platform secures agentic, generative, and predictive AI applications across the entire lifecycle, including
AI discovery, AI supply chain security, AI attack simulation, and AI runtime security. Backed by patented technology and industry-
leading adversarial AI research, HiddenLayer protects IP, ensures compliance, and enables safe adoption of AI at enterprise scale.
Learn More Follow Us
Research :
www.hiddenlayer.com
hiddenlayer.com/research
X :
x.com/hiddenlayersec
LinkedIn :
Request a Demo
linkedin.com/company/hiddenlayersec
hiddenlayer.com/book-a-demo
Authors/Contributors
Links to learn more:
Marta Janus, Principal Security Researcher
Kieran Evans, Principal Security Researcher
Tom Bonner, SVP of Research
Marcus Kan, AI Security Researcher
Kasimir Schulz, Director of Security Research
Malcolm Harkins, Chief Trust & Security Officer
Sandeep Purewal, Senior Product Manager
Samantha Pearcy, Senior Manager of Content Strategy
Jason Martin, Director of Adversarial Research
Eoin Wickens, Technical Research Director
Travis Smith, VP of Services
Jim Simpson, Principal Analyst
Kenneth Yeung, Senior AI Security Researcher
Kevin Finnigin, Principal Security Researcher
Ryan Tracey, Principal Security Researcher
61 6622

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-28", "model": "gemini-3.5-flash-lite"} -->
