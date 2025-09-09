# AI Threat Landscape 2025 Report

## Table of Contents
- [Foreword](#foreword)
- [Security for AI Survey Insights at a Glance](#security-for-ai-survey-insights-at-a-glance)
- [AI Threat Landscape Timeline](#ai-threat-landscape-timeline)
- [What’s New in AI](#whats-new-in-ai)
- [Part 1: Risks Related to the Use of AI](#part-1-risks-related-to-the-use-of-ai)
  - [Cybercrime](#cybercrime)
  - [Political Campaigns](#political-campaigns)
  - [Unintended Consequences](#unintended-consequences)
- [Part 2: Risks Faced by AI-based Systems](#part-2-risks-faced-by-ai-based-systems)
  - [Adversarial Machine Learning Attacks](#adversarial-machine-learning-attacks)
  - [Attacks Against Generative AI](#attacks-against-generative-ai)
  - [Supply Chain Security](#supply-chain-security)
- [Part 3: Advancements in Security for AI](#part-3-advancements-in-security-for-ai)
  - [AI Red Teaming Evolution](#ai-red-teaming-evolution)
  - [Updates to Existing Defensive Frameworks](#updates-to-existing-defensive-frameworks)
  - [New Security Initiatives](#new-security-initiatives)
  - [New Guidance & Legislation](#new-guidance--legislation)
- [Part 4: Predictions and Recommendations](#part-4-predictions-and-recommendations)
- [Resources](#resources)
- [About HiddenLayer](#about-hiddenlayer)

---

## Foreword

Artiﬁcial intelligence is no longer an emerging force – it is an embedded reality shaping economies, industries, and societies at an unparalleled scale. Every mission, organization, and individual has felt its impact, with AI driving efficiency, automation, and problem-solving breakthroughs. Yet, as its inﬂuence expands, so too do the risks. The past year has emphasized a critical truth: the greatest threat to AI is not the technology itself but the people who exploit it.

The AI landscape is evolving rapidly, with open-source models and smaller, more accessible architectures accelerating innovation and risk. These advancements lower the barrier to entry, allowing more organizations to leverage AI but they also widen the attack surface, making AI systems more susceptible to manipulation, data poisoning, and adversarial exploitation. Meanwhile, hyped new model trends like DeepSeek are introducing unprecedented risks and impacting geopolitical power dynamics.

Artiﬁcial intelligence remains the most vulnerable technology ever deployed at scale. Its security challenges extend far beyond code, impacting every phase of its lifecycle from training and development to deployment and real-world operations. Adversarial AI threats are evolving, blending traditional cybersecurity tactics with new, AI-speciﬁc attack methods.

In this report, we explore the vulnerabilities introduced by these developments and their real-world consequences for commercial and federal sectors. We provide insights from IT security and data science leaders actively defending against these threats, along with predictions informed by HiddenLayer’s hands-on experience in AI security. Most importantly, we highlight the advancements in security controls essential for protecting AI in all its forms.

As AI continues to drive progress, securing its future is a responsibility shared by developers, data scien- tists, and security professionals alike. This report is a crucial resource for understanding and mitigating AI risks in a rapidly shifting landscape.

We are proud to present the second annual HiddenLayer AI Threat Landscape Report, expanding on last year’s insights and charting the path forward for securing AI.

**TITO**

CEO & Co-Founder
(Unassisted by LLMs)

## Security for AI Survey Insights at a Glance

AI has become indispensable to modern business, powering critical functions and driving innovation. However, as organizations increasingly rely on AI, traditional security measures have struggled to keep up with the growing sophistication of threats.

The 2025 survey results highlight this tension: while many IT leaders recognize AI’s central role in their company’s success, there’s more work to implement comprehensive security measures. Issues like shadow AI, ownership debates, and limited security tool adoption contribute to the challenges. However, the survey results show an optimistic shift toward prioritizing AI security, with organizations investing more in defenses, governance frameworks, transparency, and resources to address emerging threats.

These insights come from a survey commissioned by HiddenLayer, where 250 IT decision-makers from a cross-section of industries shared insights into their organizations’ AI security practices. These leaders, responsible for securing or developing AI initiatives, offer a glimpse into their current challenges and efforts to strengthen their organizations from attack.

### AI’s Critical Role in Business Success
![Infographic showing 89% of IT leaders report AI models are critical to business success, and 100% state AI/ML projects are critical or important to revenue generation.]`
- **89%** of IT leaders reported that most or all AI models in production are critical to their business’s success.
- **100%** stated that AI and ML projects are critical or important to revenue generation within the next 18 months (up from 98% last year).

### Rising Security Breaches and Vulnerabilities
![Infographic showing 74% of IT leaders know if they had an AI breach in 2024, and 75% say AI attacks have increased or remained the same.]`
- **74%** of IT leaders reported to deﬁnitely know if they had an AI breach in 2024 (up from 67% reporting last year).
- **75%** say AI attacks have increased or remained the same from the previous year.

### Sources & Motivations of AI Attacks
![Infographic showing 87% can identify breach source, with top types being Malware in Models (45%), Attack on Chatbot (33%), Third-Party Applications (21%). Top sources are Criminal Hacking Groups, Third-Party Service Providers, Freelance Hackers. Top motivations are Data Theft, Financial Gain, Business Disruption.]`
- **87%** reported being able to identify the source of the breach (up from 77% last year).

**Type of AI Systems Attacked from Identiﬁed Breaches:**
- **45%** Malware in Models Pulled from Public Repositories
- **33%** Attack on Internal or External Chatbot
- **21%** Third-Party Applications

**Top 3 Sources of AI Attacks**
- Criminal Hacking Groups
- Third-Party Service Providers
- Freelance Hackers

**Top 3 Motivations for AI Attacks**
- Data Theft
- Financial Gain
- Business Disruption

### Disclosure & Transparency of AI Breaches
![Infographic showing 42% of IT leaders agree companies should disclose AI breaches, but 45% of companies opted not to report due to public backlash concerns.]`
- **42%** of IT leaders strongly agree that companies should be legally required to disclose AI-related security breaches to the public, but
- **45%** of companies have opted not to report an AI-related security incident due to concerns about public backlash.

### Rising Security Breaches and Vulnerabilities
![Infographic showing 88% of IT leaders are concerned about third-party AI integration vulnerabilities, with top Gen AI apps being ChatGPT, Microsoft Co-Pilot, Gemini.]`
- **88%** of IT leaders are concerned about vulnerabilities in third-party AI integrations.

**Top 3 Third-Party Gen AI Applications Currently In Use at Organizations:**
- ChatGPT
- Microsoft Co-Pilot
- Gemini

### Global Origins of AI Attacks
![Map infographic showing global origins of AI attacks: North America 51%, Asia 32%, Europe 34%, South America 21%, Africa 17%, Unknown 14%. (Note: percentages sum to more than 100%, indicating multiple origins possible or overlapping categories.)]`
- **51%** North America
- **21%** South America
- **34%** Europe
- **17%** Africa
- **32%** Asia
- **14%** Unknown

- **72%** of IT leaders acknowledged Shadow AI, solutions that are not officially known or under the control of the IT department, is a signiﬁcant issue in their organization (up from 61% reported last year).
- **97%** of companies use pre-trained models from repositories like Hugging Face, Azure, and AWS (up from 85% last year), but a little under half reported scanning inbound AI models for safety.

### Rising Security Breaches and Vulnerabilities
![Infographic showing IT leaders spend 46% of their time addressing AI risk or security.]`
On average, IT leaders reported spending almost half
- **46%** of their time addressing AI risk or security (up from 15% of time reported last year).

### Security Measures & Technology Gaps in AI Defense
![Infographic showing top 3 common measures to secure AI: building relationships, creating inventory, determining model origins. Only 16% secure with red teaming, 32% deploy technology solutions.]`
**Top 3 Common Measures to Secure AI Include:**
- Building relationships with AI & security teams
- Creating an inventory of AI models
- Determining sources of origins of AI models

- **16%** Only 16% of IT leaders reported securing AI models with manual or automated red teaming.
- **32%** Only 32% of IT leaders are deploying a technology solution to address AI threats.

### AI Governance Frameworks & Policies
![Infographic showing 96% of companies have a formal framework for securing AI/ML models, 81% have an AI governance committee. Top 3 frameworks: Google Secure AI, IBM Generative AI, Gartner AI Trust, Risk, and Security Management.]`
- **96%** of companies have a formal framework for securing AI and ML models.
- **81%** of organizations have implemented an AI governance committee.

**Top 3 Frameworks Used to Secure AI Include:**
- Google Secure AI Framework
- IBM Framework for Securing Generative AI
- Gartner AI Trust, Risk, and Security Management

### Transparency & Ethical Oversight
![Infographic showing 67% have a dedicated ethics committee/person, 98% plan to make AI security practices partially transparent.]`
- **67%** of IT leaders have a dedicated ethics committee or person overseeing AI ethics.
- **98%** of organizations plan to make AI security practices partially transparent.

### Debate Over AI Security Roles & Responsibilities
![Infographic showing 76% have internal debate about AI security control. 42% believe AI dev team accountable, 27% believe security team accountable.]`
- **76%** have internal debate about which teams should control AI security measures.
- **42%** of IT leaders believe the AI development team should be held accountable for errors, whereas
- **27%** believe the security team should be held responsible.

### Investments in AI Security for 2025
![Infographic showing 99% consider securing AI a high priority in 2025, 95% increased budgets for AI security.]`
- **99%** consider securing AI a high priority in 2025.
- **95%** of organizations have increased their budgets for securing AI in 2025.

## 2024 AI Threat Landscape Timeline
![Timeline of AI tech milestones, risks, adversarial tools, attacks, and security measures/legislation in 2024.]`

**JAN**
- LeftoverLocals: Listening to LLM responses through leaked GPU local memory

**FEB**
- Researchers demonstrate an attack against the Hugging Face conversion bot
- Six critical vulnerabilities providing a full attack chain found in ClearML
- Path traversal and out-of-bound read vulnerabilities disclosed in ONNXserialization format

**MAR**
- First model-stealing technique that extracts precise information from LLMs

**APR**
- OpenSSF launches Model Signing Special Interest Group
- Arbitrary code execution vulnerability disclosed in R
- Arbitrary code execution and command injection vulnerabilities found in AWS Sagemaker

**MAY**
- OpenAI introduces GPT-4o
- Elaborate deepfake video scam attack against WPP
- LLM jailbreak backdoor published at ICLR conference

**JUN**
- Knowledge Return Oriented Prompting - new LLM prompt injection technique
- CTID launches the Secure AI research project
- Agility Robotics' Digit humanoid robot deployed in production at large factories
- Arbitrary code execution and XSS vulnerabilities found in Ydata-proﬁling
- Ten code execution vulnerabilities disclosed in MLFlow framework

**JUL**
- Coalition for Secure AI established under the OASIS global standards body
- NIST expands its AIRMF with the Generative Artiﬁcial Intelligence Proﬁle
- Deepfake clip of Kamala Harris shared by Elon Musk on X
- Critical vulnerability in Wyze camera enables researchers to bypass the embedded AI's object detection

**AUG**
- EU Artiﬁcial Intelligence Act enacted into force
- New GPU Memory Exploitation techniques unveiled at USENIX
- Two arbitrary code execution vulnerabilities found in LlamaIndex

**SEP**
- U.S., UK, and EU sign the Council of Europe’s Framework Convention on AI
- Microsoft shuts down ﬁrst cybercriminal service providing users with access to jailbroken GenAI
- Ten arbitrary code execution vulnerabilities and one critical WebUI vulnerability disclosed in MindsDB
- High severity vulnerabilities found in Autolabel, Cleanlab, and Guardrails
- Wiz ﬁnds critical NVIDIA AI vulnerability in containers using NVIDIA GPUs
- ShadowLogic graph backdoor unveiled by HiddenLayer
- First attack technique against GenAI watermarks unveiled by HiddenLayer

**OCT**
- OMB releases the Advancing the Responsible Acquisition of AI in Govt
- President Biden signs ﬁrst-ever National Security Memorandum on AI
- Apple Intelligence release in the US
- Arbitrary ﬁle write vulnerability found in NVIDIA NeMo
- Lawsuit ﬁled against Character.ai states that AI companion chatbot to blame for teenager’s suicide

**NOV**
- UK establishes the Laboratory for AI Security Research (LASR)
- First draft of the EU general-purpose AI Code of Practice published
- GEMA sues OpenAI for copyright infringement over use of song lyrics in AI training

**DEC**
- Major AI supply chain attack using dependency compromise affects Ultralytics
- Google introduces Gemini 2.0
- Apple Intelligence launch in the UK
- Arbitrary code execution while scanning keras HDF5 models found in Bosch AIShield
- Apple Intelligence found generating fake news attributed to the BBC
- TPUXtract - ﬁrst model hyperparameter extraction framework
- Shadowcast - a new technique of stealthy data poisoning attacks against vision-language models, presented at NeurIPS

## What’s New in AI

The past year brought signiﬁcant advancements in AI across multiple domains, including multimodal models, retrieval-augmented generation (RAG), humanoid robotics, and agentic AI.

### Multimodal Models

Multimodal models became popular with the launch of OpenAI’s GPT-4o. What makes a model “multimodal” is its ability to create multimedia content (images, audio, and video) in response to text- or audio-based prompts, or vice versa, respond with text or audio to multimedia content uploaded to a prompt. For example, a multimodal model can process and translate a photo of a foreign language menu. This capability makes it incredibly versatile and user-friendly. Equally, multimodality has seen advancement toward facilitating real-time, natural conversations.

While GPT-4o might be one of the most used multimodal models, it's certainly not singular. Other well-known multimodal models include KOSMOS and LLaVA from Microsoft, Gemini 2.0 from Google, Chameleon from Meta, and Claude 3 from Anthropic.

### Retrieval-Augmented Generation

Another hot topic in AI is a technique called Retrieval-Augmented Generation (RAG). Although ﬁrst proposed in 2020, it has gained signiﬁcant recognition in the past year and is being rapidly implemented across industries. RAG combines large language models (LLMs) with external knowledge retrieval to produce accurate and contextually relevant responses. By having access to a trusted database containing the latest and most relevant information not included in the static training data, an LLM can produce more up-to-date responses less prone to hallucinations. Moreover, using RAG facilitates the creation of highly tailored domain-speciﬁc queries and real-time adaptability.

In September 2024, we saw the release of Oracle Cloud Infrastructure GenAI Agents - a platform that combines LLMs and RAG. In January 2025, a service that helps to streamline the information retrieval process and feed it to an LLM, called Vertex AI RAG Engine, was unveiled by Google.

### Humanoid Robots

The concept of humanoid machines can be traced as far back as ancient mythologies of Greece, Egypt, and China. However, the technology to build a fully functional humanoid robot has not matured sufficiently - until now. Rapid advancements in natural language have expedited machines’ ability to perform a wide range of tasks while offering near-human interactions.

Tesla's Optimus and Agility Robotics' Digit robot are at the forefront of these advancements. Optimus unveiled its second generation in December 2023, featuring signiﬁcant improvements over its predecessor, including faster movement, reduced weight, and sensor-embedded ﬁngers. Digit’s has a longer history, releasing and deploying its ﬁfth version in June 2024 for use at large manufacturing factories.

Advancements in LLM technology are new driving factors for the ﬁeld of robotics. In December 2023, researchers unveiled a humanoid robot called Alter3, which leverages GPT-4. Besides being used for communication, the LLM enables the robot to generate spontaneous movements based on linguistic prompts. Thanks to this integration, Alter3 can perform actions like adopting speciﬁc poses or sequences without explicit programming, demonstrating the capability to recognize new concepts without labeled examples.

### Agentic AI

Agentic AI is the natural next step in AI development that will vastly enhance the way in which we use and interact with AI.

Traditional AI bots heavily rely on pre-programmed rules and, therefore, have limited scope for independent decision-making. The goal of agentic AI is to construct assistants that would be unprecedentedly autonomous, make decisions without human feedback, and perform tasks without requiring intervention. Unlike GenAI, whose main functionality is generating content in response to user prompts, agentic assistants are focused on optimizing speciﬁc goals and objectives - and do so independently. This can be achieved by assembling a complex network of specialized models (“agents”), each with a particular role and task, as well as access to memory and external tools. This technology has incredible promise across many sectors, from manufacturing to health to sales support and customer service, and is being trialed and tested for live implementation.

Google has been investing heavily over the past year in the development of agentic models, and the new version of their ﬂagship generative AI, Gemini 2.0, is specially designed to help build AI agents. Moreover, OpenAI released a research preview of their ﬁrst autonomous agentic AI tool called Operator. Operator is an agent able to perform a range of different tasks on the website independently, and it can be used to automate various browser related activities, such as placing online orders and ﬁlling out online forms.

We’re already seeing Agentic AI turbocharged with the integration of multimodal models into agentic robotics and the concept of agentic RAG. Combining the advancements of these technologies, the future of powerful and complex autonomous solutions will soon transcend imagination into reality.

### The Rise of Open-Weight Models

Open-weight models are models whose weights (i.e., the output of the model training process) are made available to the broader public. This allows users to implement the model locally, adapt it, and ﬁne-tune it without the constraints of a proprietary model. Traditionally, open-weight models were scoring lower against leading proprietary models in AI performance benchmarking. This is because training a large GenAI solution requires tremendous computing power and is, therefore, incredibly expensive. The biggest players on the market, who are able to afford to train a high-quality GenAI, usually keep their models ringfenced and only allow access to the inference API. The recent release of an open-weight DeepSeek-R1 model might be on course to disrupt this trend.

In January 2025, a Chinese AI lab called DeepSeek released several open-weight foundation models that performed comparably in reasoning performance to top close-weight models from OpenAI. DeepSeek claims the cost of training the models was only $6M, which is signiﬁcantly lower than average. Moreover, reviewing the pricing of DeepSeek-R1 API against the popular OpenAI-o1 API shows the DeepSeek model is approximately 27x cheaper than o1 to operate, making it a very tempting option for a cost-conscious developer.

DeepSeek models might look like a breakthrough in AI training and deployment costs; however, upon a closer look, these models are ridden with problems, from insufficient safety guardrails, to insecure loading, to embedded bias and data privacy concerns.

As frontier-level open-weight models are likely to proliferate, deploying such models should be done with utmost caution. Models released by untrusted entities might contain security ﬂaws, biases, and hidden backdoors and should be carefully evaluated prior to local deployment. People choosing to use hosted solutions should also be acutely aware of privacy issues concerning the prompts they send to these models.

## Part 1: Risks Related to