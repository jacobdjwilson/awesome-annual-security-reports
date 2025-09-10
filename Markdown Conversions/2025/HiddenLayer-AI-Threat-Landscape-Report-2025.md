# AI THREAT 2025 LANDSCAPE REPORT NAVIGATING THE RISE OF AI RISKS

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

## Foreword

Artiﬁcial intelligence is no longer an emerging force – it is an embedded reality shaping economies, industries, and societies at an unparalleled scale. Every mission, organization, and individual has felt its impact, with AI driving efficiency, automation, and problem-solving breakthroughs. Yet, as its inﬂuence expands, so too do the risks. The past year has emphasized a critical truth: the greatest threat to AI is not the technology itself but the people who exploit it.

The AI landscape is evolving rapidly, with open-source models and smaller, more accessible architectures accelerating innovation and risk. These advancements lower the barrier to entry, allowing more organizations to leverage AI but they also widen the attack surface, making AI systems more susceptible to manipulation, data poisoning, and adversarial exploitation. Meanwhile, hyped new model trends like DeepSeek are introducing unprecedented risks and impacting geopolitical power dynamics.

Artiﬁcial intelligence remains the most vulnerable technology ever deployed at scale. Its security challenges extend far beyond code, impacting every phase of its lifecycle from training and development to deployment and real-world operations. Adversarial AI threats are evolving, blending traditional cybersecurity tactics with new, AI-speciﬁc attack methods.

In this report, we explore the vulnerabilities introduced by these developments and their real-world consequences for commercial and federal sectors. We provide insights from IT security and data science leaders actively defending against these threats, along with predictions informed by HiddenLayer’s hands-on experience in AI security. Most importantly, we highlight the advancements in security controls essential for protecting AI in all its forms.

As AI continues to drive progress, securing its future is a responsibility shared by developers, data scien-tists, and security professionals alike. This report is a crucial resource for understanding and mitigating AI risks in a rapidly shifting landscape.

We are proud to present the second annual HiddenLayer AI Threat Landscape Report, expanding on last year’s insights and charting the path forward for securing AI.

**TITO**

CEO & Co-Founder
(Unassisted by LLMs)

## Security for AI Survey Insights at a Glance

AI has become indispensable to modern business, powering critical functions and driving innovation. However, as organizations increasingly rely on AI, traditional security measures have struggled to keep up with the growing sophistication of threats.

The 2025 survey results highlight this tension: while many IT leaders recognize AI’s central role in their company’s success, there’s more work to implement comprehensive security measures. Issues like shadow AI, ownership debates, and limited security tool adoption contribute to the challenges. However, the survey results show an optimistic shift toward prioritizing AI security, with organizations investing more in defenses, governance frameworks, transparency, and resources to address emerging threats.

These insights come from a survey commissioned by HiddenLayer, where 250 IT decision-makers from a cross-section of industries shared insights into their organizations’ AI security practices. These leaders, responsible for securing or developing AI initiatives, offer a glimpse into their current challenges and efforts to strengthen their organizations from attack.

### AI’s Critical Role in Business Success

![Infographic showing 89% of IT leaders report AI models are critical to business success, and 100% state AI/ML projects are critical or important to revenue generation within 18 months.]

- **89%** of IT leaders reported that most or all AI models in production are critical to their business’s success.
- **100%** stated that AI and ML projects are critical or important to revenue generation within the next 18 months (up from 98% last year).

### Rising Security Breaches and Vulnerabilities

![Infographic showing 74% of IT leaders know if they had an AI breach in 2024, and 75% say AI attacks have increased or remained the same.]

- **74%** of IT leaders reported to deﬁnitely know if they had an AI breach in 2024 (up from 67% reporting last year).
- **75%** say AI attacks have increased or remained the same from the previous year.

### Sources & Motivations of AI Attacks

![Infographic showing 87% of IT leaders can identify the source of a breach, with top attack types being Malware in Models (45%), Attack on Internal or External Chatbot (33%), and Third-Party Applications (21%). Top sources are Criminal Hacking Groups, Third-Party Service Providers, Freelance Hackers. Top motivations are Data Theft, Financial Gain, Business Disruption.]

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

![Infographic showing 42% of IT leaders agree companies should disclose AI breaches, but 45% of companies opted not to report due to public backlash concerns.]

- **42%** of IT leaders strongly agree that companies should be legally required to disclose AI-related security breaches to the public, but
- **45%** of companies have opted not to report an AI-related security incident due to concerns about public backlash.

### Rising Security Breaches and Vulnerabilities (Continued)

![Infographic showing 88% of IT leaders are concerned about vulnerabilities in third-party AI integrations, with ChatGPT, Microsoft Co-Pilot, and Gemini being the top 3 third-party Gen AI applications in use.]

- **88%** of IT leaders are concerned about vulnerabilities in third-party AI integrations.

**Top 3 Third-Party Gen AI Applications Currently In Use at Organizations:**
- ChatGPT
- Microsoft Co-Pilot
- Gemini

### Global Origins of AI Attacks

![Map showing North America (51%), Asia (32%), Europe (34%), South America (21%), Africa (17%), and Unknown (14%) as origins of AI attacks.]

- **51%** North America
- **21%** South America
- **34%** Europe
- **17%** Africa
- **32%** Asia
- **14%** Unknown

- **72%** of IT leaders acknowledged Shadow AI, solutions that are not officially known or under the control of the IT department, is a signiﬁcant issue in their organization (up from 61% reported last year).
- **97%** of companies use pre-trained models from repositories like Hugging Face, Azure, and AWS (up from 85% last year), but a little under half reported scanning inbound AI models for safety.

### Rising Security Breaches and Vulnerabilities (Continued)

![Infographic showing IT leaders spend 46% of their time addressing AI risk or security.]

- On average, IT leaders reported spending almost half **46%** of their time addressing AI risk or security (up from 15% of time reported last year).

### Security Measures & Technology Gaps in AI Defense

![Infographic showing top 3 common measures to secure AI, and percentages for red teaming and technology solution deployment.]

**Top 3 Common Measures to Secure AI Include:**
- Building relationships with AI & security teams
- Creating an inventory of AI models
- Determining sources of origins of AI models

- **16%** Only 16% of IT leaders reported securing AI models with manual or automated red teaming.
- **32%** Only 32% of IT leaders are deploying a technology solution to address AI threats.

### AI Governance Frameworks & Policies

![Infographic showing 96% of companies have a formal framework for securing AI/ML models, and 81% have an AI governance committee. Top 3 frameworks are Google Secure AI, IBM Generative AI, and Gartner AI Trust, Risk, and Security Management.]

- **96%** of companies have a formal framework for securing AI and ML models.
- **81%** of organizations have implemented an AI governance committee.

**Top 3 Frameworks Used to Secure AI Include:**
- Google Secure AI Framework
- IBM Framework for Securing Generative AI
- Gartner AI Trust, Risk, and Security Management

### Transparency & Ethical Oversight

![Infographic showing 67% of IT leaders have a dedicated ethics committee or person overseeing AI ethics, and 98% plan to make AI security practices partially transparent.]

- **67%** of IT leaders have a dedicated ethics committee or person overseeing AI ethics.
- **98%** of organizations plan to make AI security practices partially transparent.

### Debate Over AI Security Roles & Responsibilities

![Infographic showing 76% have internal debate about which teams should control AI security, with 42% believing AI development team is accountable and 27% believing security team is responsible.]

- **76%** have internal debate about which teams should control AI security measures.
- **42%** of IT leaders believe the AI development team should be held accountable for errors, whereas
- **27%** believe the security team should be held responsible.

### Investments in AI Security for 2025

![Infographic showing 99% consider securing AI a high priority in 2025, and 95% of organizations have increased their budgets for securing AI in 2025.]

- **99%** consider securing AI a high priority in 2025.
- **95%** of organizations have increased their budgets for securing AI in 2025.

## AI Threat Landscape Timeline

![Timeline graphic showing AI tech milestones, risks related to AI use, new adversarial tools/techniques, known attacks/breaches, and new AI security measures/legislation from January to December 2024.]

- **JAN**: LeftoverLocals: Listening to LLM responses through leaked GPU local memory
- **FEB**: Researchers demonstrate an attack against the Hugging Face conversion bot
- **FEB**: Six critical vulnerabilities providing a full attack chain found in ClearML
- **FEB**: Path traversal and out-of-bound read vulnerabilities disclosed in ONNX serialization format
- **MAR**: First model-stealing technique that extracts precise information from LLMs
- **APR**: OpenSSF launches Model Signing Special Interest Group
- **APR**: Arbitrary code execution vulnerability disclosed in R
- **APR**: Arbitrary code execution and command injection vulnerabilities found in AWS Sagemaker
- **MAY**: OpenAI introduces GPT-4o
- **MAY**: Elaborate deepfake video scam attack against WPP
- **MAY**: LLM jailbreak backdoor published at ICLR conference
- **JUN**: Knowledge Return Oriented Prompting - new LLM prompt injection technique
- **JUN**: CTID launches the Secure AI research project
- **JUN**: Agility Robotics' Digit humanoid robot deployed in production at large factories
- **JUN**: Arbitrary code execution and XSS vulnerabilities found in Ydata-proﬁling
- **JUN**: Ten code execution vulnerabilities disclosed in MLFlow framework
- **JUL**: Coalition for Secure AI established under the OASIS global standards body
- **JUL**: NIST expands its AIRMF with the Generative Artiﬁcial Intelligence Proﬁle
- **JUL**: Deepfake clip of Kamala Harris shared by Elon Musk on X
- **JUL**: Critical vulnerability in Wyze camera enables researchers to bypass the embedded AI's object detection
- **AUG**: EU Artiﬁcial Intelligence Act enacted into force
- **AUG**: New GPU Memory Exploitation techniques unveiled at USENIX
- **AUG**: Two arbitrary code execution vulnerabilities found in LlamaIndex
- **SEP**: U.S., UK, and EU sign the Council of Europe’s Framework Convention on AI
- **SEP**: Microsoft shuts down ﬁrst cybercriminal service providing users with access to jailbroken GenAI
- **SEP**: Ten arbitrary code execution vulnerabilities and one critical WebUI vulnerability disclosed in MindsDB
- **SEP**: High severity vulnerabilities found in Autolabel, Cleanlab, and Guardrails
- **OCT**: Wiz ﬁnds critical NVIDIA AI vulnerability in containers using NVIDIA GPUs
- **OCT**: ShadowLogic graph backdoor unveiled by HiddenLayer
- **OCT**: First attack technique against GenAI watermarks unveiled by HiddenLayer
- **OCT**: OMB releases the Advancing the Responsible Acquisition of AI in Govt
- **OCT**: President Biden signs ﬁrst-ever National Security Memorandum on AI
- **OCT**: Apple Intelligence release in the US
- **NOV**: Arbitrary ﬁle write vulnerability found in NVIDIA NeMo
- **NOV**: Lawsuit ﬁled against Character.ai states that AI companion chatbot to blame for teenager’s suicide
- **NOV**: UK establishes the Laboratory for AI Security Research (LASR)
- **DEC**: First draft of the EU general-purpose AI Code of Practice published
- **DEC**: GEMA sues OpenAI for copyright infringement over use of song lyrics in AI training
- **DEC**: Major AI supply chain attack using dependency compromise affects Ultralytics
- **DEC**: Google introduces Gemini 2.0
- **DEC**: Apple Intelligence launch in the UK
- **DEC**: Arbitrary code execution while scanning keras HDF5 models found in Bosch AIShield
- **DEC**: Apple Intelligence found generating fake news attributed to the BBC
- **DEC**: TPUXtract - ﬁrst model hyperparameter extraction framework
- **DEC**: Shadowcast - a new technique of stealthy data poisoning attacks against vision-language models, presented at NeurIPS

## What’s New in AI

The past year brought signiﬁcant advancements in AI across multiple domains, including multimodal models, retrieval-augmented generation (RAG), humanoid robotics, and agentic AI.

### Multimodal Models

Multimodal models became popular with the launch of OpenAI’s GPT-4o. What makes a model “multimodal” is its ability to create multimedia content (images, audio, and video) in response to text- or audio-based prompts, or vice versa, respond with text or audio to multimedia content uploaded to a prompt. For example, a multimodal model can process and translate a photo of a foreign language menu. This capability makes it incredibly versatile and user-friendly. Equally, multimodality has seen advancement toward facilitating real-time, natural conversations.

While GPT-4o might be one of the most used multimodal models, it's certainly not singular. Other well-known multimodal models include KOSMOS and LLaVA from Microsoft, Gemini 2.0 from Google, Chameleon from Meta, and Claude 3 from Anthropic.

### Retrieval-Augmented Generation

Another hot topic in AI is a technique called Retrieval-Augmented Generation (RAG). Although ﬁrst proposed in 2020, it has gained signiﬁcant recognition in the past year and is being rapidly implemented across industries. RAG combines large language models (LLMs) with external knowledge retrieval to produce accurate and contextually relevant responses. By having access to a trusted database containing the latest and most relevant information not included in the static training data, an LLM can produce more up-to-date responses less prone to hallucinations. Moreover, using RAG facilitates the creation of highly tailored domain-speciﬁc queries and real-time adaptability.

In September 2024, we saw the release of Oracle Cloud Infrastructure GenAI Agents - a platform that combines LLMs and RAG. In January 2025, a service that helps to streamline the information retrieval process and feed it to an LLM, called Vertex AI RAG Engine, was unveiled by Google.

### Agentic AI

Agentic AI is the natural next step in AI development that will vastly enhance the way in which we use and interact with AI.

Traditional AI bots heavily rely on pre-programmed rules and, therefore, have limited scope for independent decision-making. The goal of agentic AI is to construct assistants that would be unprecedentedly autonomous, make decisions without human feedback, and perform tasks without requiring intervention. Unlike GenAI, whose main functionality is generating content in response to user prompts, agentic assistants are focused on optimizing speciﬁc goals and objectives - and do so independently. This can be achieved by assembling a complex network of specialized models (“agents”), each with a particular role and task, as well as access to memory and external tools. This technology has incredible promise across many sectors, from manufacturing to health to sales support and customer service, and is being trialed and tested for live implementation.

Google has been investing heavily over the past year in the development of agentic models, and the new version of their ﬂagship generative AI, Gemini 2.0, is specially designed to help build AI agents. Moreover, OpenAI released a research preview of their ﬁrst autonomous agentic AI tool called Operator. Operator is an agent able to perform a range of different tasks on the website independently, and it can be used to automate various browser related activities, such as placing online orders and ﬁlling out online forms.

We’re already seeing Agentic AI turbocharged with the integration of multimodal models into agentic robotics and the concept of agentic RAG. Combining the advancements of these technologies, the future of powerful and complex autonomous solutions will soon transcend imagination into reality.

### Humanoid Robots

The concept of humanoid machines can be traced as far back as ancient mythologies of Greece, Egypt, and China. However, the technology to build a fully functional humanoid robot has not matured sufficiently - until now. Rapid advancements in natural language have expedited machines’ ability to perform a wide range of tasks while offering near-human interactions.

Tesla's Optimus and Agility Robotics' Digit robot are at the forefront of these advancements. Optimus unveiled its second generation in December 2023, featuring signiﬁcant improvements over its predecessor, including faster movement, reduced weight, and sensor-embedded ﬁngers. Digit’s has a longer history, releasing and deploying its ﬁfth version in June 2024 for use at large manufacturing factories.

Advancements in LLM technology are new driving factors for the ﬁeld of robotics. In December 2023, researchers unveiled a humanoid robot called Alter3, which leverages GPT-4. Besides being used for communication, the LLM enables the robot to generate spontaneous movements based on linguistic prompts. Thanks to this integration, Alter3 can perform actions like adopting speciﬁc poses or sequences without explicit programming, demonstrating the capability to recognize new concepts without labeled examples.

### The Rise of Open-Weight Models

Open-weight models are models whose weights (i.e., the output of the model training process) are made available to the broader public. This allows users to implement the model locally, adapt it, and ﬁne-tune it without the constraints of a proprietary model. Traditionally, open-weight models were scoring lower against leading proprietary models in AI performance benchmarking. This is because training a large GenAI solution requires tremendous computing power and is, therefore, incredibly expensive. The biggest players on the market, who are able to afford to train a high-quality GenAI, usually keep their models ringfenced and only allow access to the inference API. The recent release of an open-weight DeepSeek-R1 model might be on course to disrupt this trend.

In January 2025, a Chinese AI lab called DeepSeek released several open-weight foundation models that performed comparably in reasoning performance to top close-weight models from OpenAI. DeepSeek claims the cost of training the models was only $6M, which is signiﬁcantly lower than average. Moreover, reviewing the pricing of DeepSeek-R1 API against the popular OpenAI-o1 API shows the DeepSeek model is approximately 27x cheaper than o1 to operate, making it a very tempting option for a cost-conscious developer.

DeepSeek models might look like a breakthrough in AI training and deployment costs; however, upon a closer look, these models are ridden with problems, from insufficient safety guardrails, to insecure loading, to embedded bias and data privacy concerns.

As frontier-level open-weight models are likely to proliferate, deploying such models should be done with utmost caution. Models released by untrusted entities might contain security ﬂaws, biases, and hidden backdoors and should be carefully evaluated prior to local deployment. People choosing to use hosted solutions should also be acutely aware of privacy issues concerning the prompts they send to these models.

## Part 1: Risks Related to the Use of AI

Before we cover attacks against AI-based systems, let's do a quick overview of the issues related to the use of AI. There are several areas of concern where malicious or improper use of AI can create trouble for individuals, organizations, and societies alike. These include generating malicious, harmful, or illegal content (such as malware, deepfakes, and disinformation), hallucinations and accuracy issues, privacy breaches, and broader societal and ethical concerns.

**KEY STAT**

**TIME SPENT ADDRESSING RISK**

On average, IT leaders spend **46%** of their time on AI addressing risk or security

### Cybercrime

AI is being rapidly adopted across all sectors, and the cybercrime business is, unfortunately, no exception. In 2024, adversaries were found to be leveraging AI for a multitude of illicit tasks, from enhancing their phishing campaigns and ﬁnancial scams to generating malicious code and automating attacks to spreading political misinformation.

#### PHISHING & SCAM

Since its inception, one of the predominant concerns surrounding generative AI abuse has been its potential to improve phishing and scams, making it almost impossible to distinguish from legitimate content.

There are several factors at play here:
- Attackers can use AI to generate high-quality text, meaning there are no grammar mistakes or typos, which used to be a tell-tale sign of phishing
- Attacks can be enhanced with convincing AI-generated images, audio, and video, making social engineering easier than ever
- The ability of AI to analyze swaths of data from public sources allows for the creation of highly personalized content that closely resembles legitimate sources and, therefore, instills trusty automating tasks with AI; cybercriminals can rapidly generate this variated and sophisticated phishing content without substantial human effort

All this brings an incredible boost to both the quantity of attacks and their success rate. In the past year, we saw several sophisticated phishing campaigns against Gmail users using AI voice.

In one of these attacks, a phishing email requesting account recovery was sent to the victims, followed by a call from a supposed Google support engineer informing the recipient that his account had been hacked. The phone number, if searched on Google, led to pages associated with Google business, and the conversation with the fake support technician was so convincing that it nearly fooled even a seasoned security professional.

Financial scams that use video deepfakes are even scarier prospects.

In May 2024, fraudsters targeted the CEO of WPP, the world's largest advertising agency. They cloned his voice and used publicly available photos to create a deepfake video, which was then used to impersonate their CEO in a Microsoft Teams call with another executive. The incident was spotted by WPP staff, but its sophistication was almost unprecedented.

Deepfake scams can also happen outside of workplace settings and target different aspects of people’s personal lives. One of these aspects is in dating.

**$650M** was lost to romance fraud in 2023

The FBI estimates that more than $650 million was lost to romance fraud in 2023 alone, making it an exceptionally lucrative venture for cybercriminals. With AI-based face-swapping applications at their ﬁngertips, attackers can impersonate individuals during live video calls, deceiving victims into believing they are engaging with genuine romantic partners. In fact, a notorious Nigerian group of scammers, dubbed “Yahoo Boys”, have recently deployed this technique.

> Prediction from last year: “Deepfakes will be increasingly used in scam and disinformation”

#### MALWARE

Beyond phishing, AI has also been employed to develop more sophisticated malware and speed up cybercriminal workﬂows.

There includes
- Automated code generation that allows cybercriminals to quickly and effortlessly create new malware variants
- Improved evasion techniques that analyze how malware is detected and create mutated samples that will avoid current security measures
- Enhanced capabilities with AI mechanisms that make malware more capable (e.g., able to process text on images) and adaptable (e.g., able to adjust its tactics in real-time based on encountered defenses)
- Highly personalized exploits and attack scenarios tailored to particular victims where adversaries can automate scanning for vulnerabilities in targeted systems

In September 2024, HP Wolf Security identiﬁed a cybercriminal campaign in which AI-generated code was used as the initial payload. In the ﬁrst stage of the attack, the adversary targeted their victims with malicious scripts designed to download and execute further info-stealing malware. These scripts, written in either VBScript or JavaScript, exhibited all the signs of being AI