# AI THREAT 2025 LANDSCAPE REPORT

## Table of Contents
- [Foreword](#foreword)
- [Security for AI Survey Insights at a Glance](#security-for-ai-survey-insights-at-a-glance)
  - [AI’s Critical Role in Business Success](#ais-critical-role-in-business-success)
  - [Rising Security Breaches and Vulnerabilities](#rising-security-breaches-and-vulnerabilities)
  - [Sources & Motivations of AI Attacks](#sources--motivations-of-ai-attacks)
  - [Disclosure & Transparency of AI Breaches](#disclosure--transparency-of-ai-breaches)
  - [Global Origins of AI Attacks](#global-origins-of-ai-attacks)
  - [Security Measures & Technology Gaps in AI Defense](#security-measures--technology-gaps-in-ai-defense)
  - [AI Governance Frameworks & Policies](#ai-governance-frameworks--policies)
  - [Transparency & Ethical Oversight](#transparency--ethical-oversight)
  - [Debate Over AI Security Roles & Responsibilities](#debate-over-ai-security-roles--responsibilities)
  - [Investments in AI Security for 2025](#investments-in-ai-security-for-2025)
- [2024 AI Threat Landscape Timeline](#2024-ai-threat-landscape-timeline)
- [What’s New in AI](#whats-new-in-ai)
  - [Multimodal Models](#multimodal-models)
  - [Retrieval-Augmented Generation](#retrieval-augmented-generation)
  - [Agentic AI](#agentic-ai)
  - [Humanoid Robots](#humanoid-robots)
  - [The Rise of Open-Weight Models](#the-rise-of-open-weight-models)
- [PART 1: Risks Related to the Use of AI](#part-1-risks-related-to-the-use-of-ai)
  - [The Use of AI in Cybercrime](#the-use-of-ai-in-cybercrime)
    - [PHISHING & SCAM](#phishing--scam)
    - [MALWARE](#malware)
    - [DEEP AND DARK WEB CHATTER](#deep-and-dark-web-chatter)
  - [The Use of AI in Political Campaigns](#the-use-of-ai-in-political-campaigns)
  - [Unintended Consequences of AI Use](#unintended-consequences-of-ai-use)
    - [HALLUCINATIONS AND ACCURACY ISSUES](#hallucinations-and-accuracy-issues)
    - [PRIVACY ISSUES](#privacy-issues)
    - [COPYRIGHT ISSUES](#copyright-issues)
    - [EMOTIONAL DEPENDENCY](#emotional-dependency)
- [PART 2: Risks Faced by AI-based Systems](#part-2-risks-faced-by-ai-based-systems)
  - [Adversarial Machine Learning Attacks](#adversarial-machine-learning-attacks)
    - [MODEL EVASION](#model-evasion)
    - [DATA POISONING](#data-poisoning)
    - [MODEL BACKDOORING](#model-backdooring)
      - [ShadowLogic & Graph Backdoors](#shadowlogic--graph-backdoors)
    - [MODEL THEFT](#model-theft)
  - [Attacks Against GenAI](#attacks-against-genai)
    - [PROMPT INJECTION](#prompt-injection)
      - [Multimodal Prompt Injection](#multimodal-prompt-injection)
      - [Google Gemini](#google-gemini)
      - [KROP - Knowledge Return Oriented Prompting](#krop---knowledge-return-oriented-prompting)
    - [INDIRECT INJECTION](#indirect-injection)
      - [Gemini for Workspace](#gemini-for-workspace)
      - [Claude Computer Use](#claude-computer-use)
    - [HACKING-AS-A-SERVICE](#hacking-as-a-service)
    - [PRIVACY ATTACKS](#privacy-attacks)
    - [MANIPULATING GEN AI WATERMARKS](#manipulating-gen-ai-watermarks)
  - [Supply Chain Security](#supply-chain-security)
    - [VULNERABILITIES IN ML SERIALIZATION (Serialization Formats, Platforms, and Tooling)](#vulnerabilities-in-ml-serialization-serialization-formats-platforms-and-tooling)
    - [MLOPS PLATFORM RECONNAISSANCE](#mlops-platform-reconnaissance)
    - [ATTACKS AGAINST AI EMBEDDED IN DEVICES](#attacks-against-ai-embedded-in-devices)
    - [ABUSING ML SERVICES](#abusing-ml-services)
      - [Dependency Compromise](#dependency-compromise)
      - [Package Confusion](#package-confusion)
    - [Hugging Face in Focus: Security Gaps in the Global AI Platform](#hugging-face-in-focus-security-gaps-in-the-global-ai-platform)
      - [Hugging Face in Numbers](#hugging-face-in-numbers)
      - [Top 10 File Formats](#top-10-file-formats)
      - [Abusing Hugging Face Conversion Bot](#abusing-hugging-face-conversion-bot)
      - [Abusing Hugging Face Spaces](#abusing-hugging-face-spaces)
      - [Account Typosquatting](#account-typosquatting)
    - [ATTACKS AGAINST ML INFRASTRUCTURE](#attacks-against-ml-infrastructure)
      - [GPU Attacks](#gpu-attacks)
      - [Attacks on Clusters and Hosting Services](#attacks-on-clusters-and-hosting-services)
    - [MALICIOUS MODELS IN THE WILD](#malicious-models-in-the-wild)
- [PART 3: Advancements in Security for AI](#part-3-advancements-in-security-for-ai)
  - [AI Red Teaming Evolution](#ai-red-teaming-evolution)
    - [ADVERSARIAL TOOLING](#adversarial-tooling)
    - [AI RED TEAMING BEST PRACTICES](#ai-red-teaming-best-practices)
  - [Updates to Existing Defensive Frameworks](#updates-to-existing-defensive-frameworks)
    - [WHAT’S NEW IN MITRE](#whats-new-in-mitre)
    - [WHAT’S NEW IN OWASP](#whats-new-in-owasp)
    - [WHAT’S NEW IN NIST](#whats-new-in-nist)
  - [New Security Initiatives](#new-security-initiatives)
    - [MODEL PROVENANCE & CRYPTOGRAPHIC SIGNING](#model-provenance--cryptographic-signing)
    - [AIBOM / MLBOM](#aibom--mlbom)
    - [Coalition for Secure AI](#coalition-for-secure-ai)
    - [Joint Cyber Defense Collaborative (JCDC)](#joint-cyber-defense-collaborative-jcdc)
  - [New Guidance and Legislation](#new-guidance-and-legislation)
- [PART 4: Predictions and Recommendations](#part-4-predictions-and-recommendations)
  - [Predictions for 2025](#predictions-for-2025)
  - [Recommendations for the Security Practitioner](#recommendations-for-the-security-practitioner)
- [HiddenLayer Resources](#hiddenlayer-resources)
  - [PRODUCTS AND SERVICES](#products-and-services)
  - [HIDDENLAYER RESEARCH](#hiddenlayer-research)
- [About HiddenLayer](#about-hiddenlayer)
  - [LEARN MORE:](#learn-more)
  - [FOLLOW US:](#follow-us)
  - [REQUEST A DEMO:](#request-a-demo)
  - [AUTHORS/CONTRIBUTORS](#authorscontributors)

---

## Foreword

Artiﬁcial intelligence is no longer an emerging force – it is an embedded reality shaping economies, industries, and societies at an unparalleled scale. Every mission, organization, and individual has felt its impact, with AI driving efficiency, automation, and problem-solving breakthroughs. Yet, as its inﬂuence expands, so too do the risks. The past year has emphasized a critical truth: the greatest threat to AI is not the technology itself but the people who exploit it.

The AI landscape is evolving rapidly, with open-source models and smaller, more accessible architectures accelerating innovation and risk. These advancements lower the barrier to entry, allowing more organizations to leverage AI but they also widen the attack surface, making AI systems more susceptible to manipulation, data poisoning, and adversarial exploitation. Meanwhile, hyped new model trends like DeepSeek are introducing unprecedented risks and impacting geopolitical power dynamics.

Artiﬁcial intelligence remains the most vulnerable technology ever deployed at scale. Its security challenges extend far beyond code, impacting every phase of its lifecycle from training and development to deployment and real-world operations. Adversarial AI threats are evolving, blending traditional cybersecurity tactics with new, AI-speciﬁc attack methods.

In this report, we explore the vulnerabilities introduced by these developments and their real-world consequences for commercial and federal sectors. We provide insights from IT security and data science leaders actively defending against these threats, along with predictions informed by HiddenLayer’s hands-on experience in AI security. Most importantly, we highlight the advancements in security controls essential for protecting AI in all its forms.

As AI continues to drive progress, securing its future is a responsibility shared by developers, data scien-tists, and security professionals alike. This report is a crucial resource for understanding and mitigating AI risks in a rapidly shifting landscape.

We are proud to present the second annual HiddenLayer AI Threat Landscape Report, expanding on last year’s insights and charting the path forward for securing AI.

TITO

CEO & Co-Founder
(Unassisted by LLMs)

## Security for AI Survey Insights at a Glance

AI has become indispensable to modern business, powering critical functions and driving innovation. However, as organizations increasingly rely on AI, traditional security measures have struggled to keep up with the growing sophistication of threats.

The 2025 survey results highlight this tension: while many IT leaders recognize AI’s central role in their company’s success, there’s more work to implement comprehensive security measures. Issues like shadow AI, ownership debates, and limited security tool adoption contribute to the challenges. However, the survey results show an optimistic shift toward prioritizing AI security, with organizations investing more in defenses, governance frameworks, transparency, and resources to address emerging threats.

These insights come from a survey commissioned by HiddenLayer, where 250 IT decision-makers from a cross-section of industries shared insights into their organizations’ AI security practices. These leaders, responsible for securing or developing AI initiatives, offer a glimpse into their current challenges and efforts to strengthen their organizations from attack.

### AI’s Critical Role in Business Success

> **KEY STAT**
> **89%** of IT leaders reported that most or all AI models in production are critical to their business’s success.

- **100%** stated that AI and ML projects are critical or important to revenue generation within the next 18 months (up from 98% last year).

### Rising Security Breaches and Vulnerabilities

- **74%** of IT leaders reported to deﬁnitely know if they had an AI breach in 2024 (up from 67% reporting last year).
- **75%** say AI attacks have increased or remained the same from the previous year.

### Sources & Motivations of AI Attacks

- **87%** reported being able to identify the source of the breach (up from 77% last year).

Type of AI Systems Attacked from Identiﬁed Breaches:

- **45%** Malware in Models Pulled from Public Repositories
- **33%** Attack on Internal or External Chatbot
- **21%** Third-Party Applications

Top 3 Sources of AI Attacks
- Criminal Hacking Groups
- Third-Party Service Providers
- Freelance Hackers

Top 3 Motivations for AI Attacks
- Data Theft
- Financial Gain
- Business Disruption

### Disclosure & Transparency of AI Breaches

- **42%** of IT leaders strongly agree that companies should be legally required to disclose AI-related security breaches to the public, but
- **45%** of companies have opted not to report an AI-related security incident due to concerns about public backlash.

### Global Origins of AI Attacks

![Global Origins of AI Attacks Map](image_of_world_map_with_percentages_for_continents_indicating_attack_origins)

- **51%** North America
- **21%** South America
- **34%** Europe
- **17%** Africa
- **32%** Asia
- **14%** Unknown

- **72%** of IT leaders acknowledged Shadow AI, solutions that are not officially known or under the control of the IT department, is a signiﬁcant issue in their organization (up from 61% reported last year).
- **97%** of companies use pre-trained models from repositories like Hugging Face, Azure, and AWS (up from 85% last year), but a little under half reported scanning inbound AI models for safety.

### Security Measures & Technology Gaps in AI Defense

On average, IT leaders reported spending almost half **46%** of their time addressing AI risk or security (up from 15% of time reported last year).

Top 3 Common Measures to Secure AI Include:
- Building relationships with AI & security teams
- Creating an inventory of AI models
- Determining sources of origins of AI models

- **16%** Only 16% of IT leaders reported securing AI models with manual or automated red teaming.
- **32%** Only 32% of IT leaders are deploying a technology solution to address AI threats.

### AI Governance Frameworks & Policies

- **96%** of companies have a formal framework for securing AI and ML models.
- **81%** of organizations have implemented an AI governance committee.

Top 3 Frameworks Used to Secure AI Include:
- Google Secure AI Framework
- IBM Framework for Securing Generative AI
- Gartner AI Trust, Risk, and Security Management

### Transparency & Ethical Oversight

- **67%** of IT leaders have a dedicated ethics committee or person overseeing AI ethics.
- **98%** of organizations plan to make AI security practices partially transparent.

### Debate Over AI Security Roles & Responsibilities

- **76%** have internal debate about which teams should control AI security measures.
- **42%** of IT leaders believe the AI development team should be held accountable for errors, whereas
- **27%** believe the security team should be held responsible.

### Investments in AI Security for 2025

- **99%** consider securing AI a high priority in 2025.
- **95%** of organizations have increased their budgets for securing AI in 2025.

## 2024 AI Threat Landscape Timeline

1.  **JAN** LeftoverLocals: Listening to LLM responses through leaked GPU local memory
2.  **FEB** Researchers demonstrate an attack against the Hugging Face conversion bot
3.  **FEB** Six critical vulnerabilities providing a full attack chain found in ClearML
4.  **FEB** Path traversal and out-of-bound read vulnerabilities disclosed in ONNXserialization format
5.  **MAR** First model-stealing technique that extracts precise information from LLMs
6.  **APR** OpenSSF launches Model Signing Special Interest Group
7.  **APR** Arbitrary code execution vulnerability disclosed in R
8.  **APR** Arbitrary code execution and command injection vulnerabilities found in AWS Sagemaker
9.  **MAY** OpenAI introduces GPT-4o
10. **MAY** Elaborate deepfake video scam attack against WPP
11. **MAY** LLM jailbreak backdoor published at ICLR conference
12. **JUN** Knowledge Return Oriented Prompting - new LLM prompt injection technique
13. **JUN** CTID launches the Secure AI research project
14. **JUN** Agility Robotics' Digit humanoid robot deployed in production at large factories
15. **JUN** Arbitrary code execution and XSS vulnerabilities found in Ydata-proﬁling
16. **JUN** Ten code execution vulnerabilities disclosed in MLFlow framework
17. **JUL** Coalition for Secure AI established under the OASIS global standards body
18. **JUL** NIST expands its AIRMF with the Generative Artiﬁcial Intelligence Proﬁle
19. **JUL** Deepfake clip of Kamala Harris shared by Elon Musk on X
20. **JUL** Critical vulnerability in Wyze camera enables researchers to bypass the embedded AI's object detection
21. **AUG** EU Artiﬁcial Intelligence Act enacted into force
22. **AUG** New GPU Memory Exploitation techniques unveiled at USENIX
23. **AUG** Two arbitrary code execution vulnerabilities found in LlamaIndex
24. **SEP** U.S., UK, and EU sign the Council of Europe’s Framework Convention on AI
25. **SEP** Microsoft shuts down ﬁrst cybercriminal service providing users with access to jailbroken GenAI
26. **SEP** Ten arbitrary code execution vulnerabilities and one critical WebUI vulnerability disclosed in MindsDB
27. **SEP** High severity vulnerabilities found in Autolabel, Cleanlab, and Guardrails
28. **SEP** Wiz ﬁnds critical NVIDIA AI vulnerability in containers using NVIDIA GPUs
29. **OCT** ShadowLogic graph backdoor