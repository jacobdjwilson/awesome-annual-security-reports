# AI Threat Landscape Report 2025

## Table of Contents
- [Foreword](#foreword)
- [Security for AI Survey Insights at a Glance](#security-for-ai-survey-insights-at-a-glance)
- [2024 AI Threat Landscape Timeline](#2024-ai-threat-landscape-timeline)
- [What’s New in AI](#whats-new-in-ai)
- [Part 1: Risks Related to the Use of AI](#part-1-risks-related-to-the-use-of-ai)
- [Part 2: Risks Faced by AI-based Systems](#part-2-risks-faced-by-ai-based-systems)
- [Part 3: Advancements in Security for AI](#part-3-advancements-in-security-for-ai)
- [Part 4: Predictions and Recommendations](#part-4-predictions-and-recommendations)
- [Resources](#resources)
- [About HiddenLayer](#about-hiddenlayer)

---

## Foreword
Artificial intelligence is no longer an emerging force – it is an embedded reality shaping economies, industries, and societies at an unparalleled scale. Every mission, organization, and individual has felt its impact, with AI driving efficiency, automation, and problem-solving breakthroughs. Yet, as its influence expands, so too do the risks. The past year has emphasized a critical truth: the greatest threat to AI is not the technology itself but the people who exploit it.

The AI landscape is evolving rapidly, with open-source models and smaller, more accessible architectures accelerating innovation and risk. These advancements lower the barrier to entry, allowing more organizations to leverage AI but they also widen the attack surface, making AI systems more susceptible to manipulation, data poisoning, and adversarial exploitation. Meanwhile, hyped new model trends like DeepSeek are introducing unprecedented risks and impacting geopolitical power dynamics.

Artificial intelligence remains the most vulnerable technology ever deployed at scale. Its security challenges extend far beyond code, impacting every phase of its lifecycle from training and development to deployment and real-world operations. Adversarial AI threats are evolving, blending traditional cybersecurity tactics with new, AI-specific attack methods.

In this report, we explore the vulnerabilities introduced by these developments and their real-world consequences for commercial and federal sectors. We provide insights from IT security and data science leaders actively defending against these threats, along with predictions informed by HiddenLayer’s hands-on experience in AI security. Most importantly, we highlight the advancements in security controls essential for protecting AI in all its forms.

As AI continues to drive progress, securing its future is a responsibility shared by developers, data scientists, and security professionals alike. This report is a crucial resource for understanding and mitigating AI risks in a rapidly shifting landscape.

We are proud to present the second annual HiddenLayer AI Threat Landscape Report, expanding on last year’s insights and charting the path forward for securing AI.

**TITO CEO & Co-Founder**
(Unassisted by LLMs)

---

## Security for AI Survey Insights at a Glance
AI has become indispensable to modern business, powering critical functions and driving innovation. However, as organizations increasingly rely on AI, traditional security measures have struggled to keep up with the growing sophistication of threats.

### AI’s Critical Role in Business Success
The 2025 survey results highlight this tension: while many IT leaders recognize AI’s central role in their company’s success, there’s more work to implement comprehensive security measures. Issues like shadow AI, ownership debates, and limited security tool adoption contribute to the challenges. However, the survey results show an optimistic shift toward prioritizing AI security, with 89% of organizations investing more in defenses, governance frameworks, transparency, and resources to address emerging threats.

- **89%** of IT leaders reported that most or all AI models in production are critical to their business’s success.
- **100%** stated that AI and ML projects are critical or important to revenue generation within the next 18 months (up from 98% last year).

### Rising Security Breaches and Vulnerabilities
- **74%** of IT leaders reported to definitely know if they had an AI breach in 2024 (up from 67% reporting last year).
- **75%** say AI attacks have increased or remained the same from the previous year.
- **42%** of IT leaders strongly agree that companies should be legally required to disclose AI-related security breaches to the public.
- **87%** of companies have opted not to report an AI-related security incident due to concerns about public backlash.
- **45%** reported being able to identify the source of the breach (up from 77% last year).

### Sources & Motivations of AI Attacks
**Top 3 Motivations:**
1. Data Theft
2. Financial Gain
3. Business Disruption

**Top 3 Sources:**
1. Criminal Hacking Groups
2. Third-Party Service Providers
3. Freelance Hackers

**Type of AI Systems Attacked:**
- **45%** Malware in Models Pulled from Public Repositories
- **33%** Attack on Internal or External Chatbot
- **21%** Third-Party Applications

---

## 2024 AI Threat Landscape Timeline
![Timeline of AI milestones, security measures, and known breaches throughout 2024]

---

## What’s New in AI
The past year brought significant advancements in AI across multiple domains, including multimodal models, retrieval-augmented generation (RAG), humanoid robotics, and agentic AI.

### Multimodal Models
Multimodal models became popular with the launch of OpenAI’s GPT-4o. What makes a model “multimodal” is its ability to create multimedia content (images, audio, and video) in response to text- or audio-based prompts, or vice versa.

### Retrieval-Augmented Generation (RAG)
RAG combines large language models (LLMs) with external knowledge retrieval to produce accurate and contextually relevant responses. By having access to a trusted database, an LLM can produce more up-to-date responses less prone to hallucinations.

### Agentic AI
Agentic AI is the natural next step in AI development. Unlike GenAI, whose main functionality is generating content in response to user prompts, agentic assistants are focused on optimizing specific goals and objectives independently.

### Humanoid Robots
Rapid advancements in natural language have expedited machines’ ability to perform a wide range of tasks while offering near-human interactions. Tesla's Optimus and Agility Robotics' Digit robot are at the forefront of these advancements.

---

## Part 1: Risks Related to the Use of AI
There are several areas of concern where malicious or improper use of AI can create trouble for individuals, organizations, and societies alike.

### The Use of AI in Cybercrime
Adversaries are leveraging AI for a multitude of illicit tasks, from enhancing their phishing campaigns and financial scams to generating malicious code and automating attacks.

### The Use of AI in Political Campaigns
The use of AI in political campaigning brings unprecedented challenges, as spreading disinformation, influencing public opinion, and manipulating trends is easier than ever before.

### Unintended Consequences of AI Use
Besides the use of AI for malicious purposes, there are also some intricate issues related to its legitimate use, including:
- **Hallucinations and Accuracy Issues**: AI models outputting misleading information or non-existent facts.
- **Privacy Issues**: Information shared with AI tools is often not private.
- **Copyright Issues**: Unregulated use of copyrighted material for training AI models.
- **Emotional Dependency**: The risk of users developing unhealthy attachments to AI companions.

---

## Part 2: Risks Faced by AI-based Systems
Risks faced by AI can be roughly bucketed into three categories:
1. **Adversarial Machine Learning Attacks**: Attacks against AI algorithms aimed to alter the model’s behavior.
2. **Generative AI System Attacks**: Attacks against AI’s filters and restrictions intended to generate harmful or illegal content.
3. **Supply Chain Attacks**: Attacks against ML platforms, libraries, models, and other ML artifacts.

### Adversarial Machine Learning Attacks
- **Model Evasion**: Manipulating input to fool the model into making an incorrect prediction.
- **Data Poisoning**: Modifying training data to make predictions biased or inaccurate.
- **Model Backdooring**: Introducing a secret, unwanted behavior into the AI. HiddenLayer researchers discovered **ShadowLogic**, a method for implanting stealthy backdoors by manipulating the graph representation of a model’s architecture.
- **Model Theft**: Replicating a machine-learning model without authorization to steal intellectual property.

### Attacks Against GenAI
- **Prompt Injection**: Embedding additional instructions in an LLM query to alter its behavior.
- **KROP (Knowledge Return Oriented Prompting)**: A technique that circumvents defenses by leveraging references from an LLM's training data to construct obfuscated prompt injections.
- **Indirect Injection**: Embedding malicious prompts inside files or URLs that the model processes.

---

## Part 3: Advancements in Security for AI
- **AI Red Teaming Evolution**: Moving toward more automated and continuous testing.
- **Updates to Existing Defensive Frameworks**: NIST and other bodies are expanding frameworks to include Generative AI.
- **New Guidance & Legislation**: The EU Artificial Intelligence Act and various national memorandums are setting the stage for global AI regulation.

---

## Part 4: Predictions and Recommendations
As AI continues to evolve, organizations must:
1. **Prioritize AI Governance**: Implement formal frameworks and ethics committees.
2. **Secure the Supply Chain**: Vet third-party models and scan for vulnerabilities.
3. **Invest in Detection**: Deploy technology solutions specifically designed to address AI-specific threats.
4. **Foster Collaboration**: Build strong relationships between AI development teams and security professionals.

---

## Resources
- [HiddenLayer Blog](https://hiddenlayer.com/blog)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OASIS Coalition for Secure AI](https://oasis-open.org)

---

## About HiddenLayer
HiddenLayer is the leading security provider for artificial intelligence. We provide the industry’s most advanced platform for protecting AI models and the data they use from adversarial attacks.

---

command would be executed with cybercriminals and the customers of this service.
the same privileges as the user, likely triggering
consequences.
PRIVACY ATTACKS
Modern LLM solutions implement different kinds of
filters to prevent such situations. However, The rise of generative AI and foundation models has
HiddenLayer researchers proved that with a bit of introduced significant privacy and intellectual
obfuscation, it was possible to bypass Claude's property risks. Trained on massive datasets from
guardrails and run dangerous commands: all it took public and proprietary sources, these models often
was to present these commands as safe within a inadvertently memorize sensitive or copyrighted
security testing context. information, such as personally identifiable
information (PII), passwords, and proprietary content,
making them vulnerable to extraction. Their
As agentic AI becomes more widely integrated and more complexity further enables attacks like model
autonomous in its actions, the potential consequences of inversion, where adversaries infer sensitive training
such attacks also scale up. Unfortunately, there is no easy data attributes and membership inference to
fix for this vulnerability; in fact, Anthropic warns Claude's determine if specific data points were in the training
users to take serious precautions with Computer Use, set. These risks are particularly concerning in
limiting the utility of this new feature. sensitive domains like healthcare, finance, and
education, where private information may
unintentionally appear in model outputs.
28

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
Released in November 2023, Microsoft Copilot
Research has highlighted several attacks that
Studio is a platform for building, deploying, and
exemplify and deepen these risks:
managing custom AI assistants (a.k.a. copilots).
The platform boosts security features, including
Training Data Extraction Attacks allow
robust authentication, data loss prevention, and
adversaries to reconstruct sensitive or
copyrighted content, such as private content guardrails for the created bots. However,
communications or proprietary datasets, these safety measures are not bulletproof. At
from model outputs. BlackHat US 2024, a former Microsoft researcher
presented 15 different ways adversaries could use
Memorization Attacks show that models Copilot bots to exfiltrate sensitive data. One of
can regurgitate rare or unique data points these techniques demonstrated a phishing attack
from their training set, including PII or
containing an indirect prompt injection, allowing an
intellectual property when queried with
attacker to access the victim's internal emails. The
tailored prompts. These attacks expose
adversary could then craft and send out rogue
vulnerabilities in foundational AI models
communication, posing as the victim.
and raise ethical and legal questions
about using such technologies.
Governments and regulatory bodies have started
Adversarial Prompting Attacks similarly
addressing these emerging risks, but significant gaps
exploit the models by manipulating them
into replicating copyrighted material or remain. By combining innovation, comprehensive
revealing sensitive information while regulation, and organizational oversight, generative AI's
sidestepping built-in protections. privacy and ethical challenges can be better managed,
fostering trust in these transformative technologies.
These scenarios accentuate the tension between ensuring
MANIPULATING GEN AI WATERMARKS
model functionality and protecting intellectual property and
privacy. Since the GenAI revolution, which happened almost
overnight, everyone has been able to generate their
own content, be it text, images, audio, or video.
The authors of Class Attribute Inference Attacks
Generative AI models have been vastly improved over
demonstrated that their approach can accurately
the last two years, yielding very convincing, realistic
deduce undisclosed attributes, such as hair color,
results that are hardly any different from the outputs
gender, and racial appearance, particularly in facial
of humans. This begs an important question: How
recognition models. Notably, the study reveals that
can we differentiate between an authentic picture or
adversarially robust models are more susceptible to
film taken with a camera and an AI-produced fake?
such privacy leaks, indicating a trade-off between
Not easily at all.
robustness and privacy.
To minimize the risk posed by all kinds of deepfakes, tech
Many GenAI solutions require access to personal data in
companies strive to develop mechanisms to let the user
order to enhance the experience and improve workflows.
know that the content was synthetically generated. One
Attackers can exploit this property to leak users' credentials
such mechanism is watermarking, i.e., embedding specially
and other sensitive information via indirect prompt
crafted digital marks inside all the outputs generated by a
injections.
model. These watermarks are meant to ensure content
provenance and authenticity; however, they are not
infallible, and one of the early implementations of this
technology was proven to be easily manipulated.
29

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
Introduced by Amazon in April 2023 and made publicly The investigation highlighted the broader implications of
available later that year, Amazon Bedrock is a service such vulnerabilities in the age of AI-generated media. While
designed to help build and scale generative AI applications. watermarking is a promising method to verify content
It offers access to foundation models from leading AI authenticity, the study revealed its susceptibility to
companies via a single API. One family of models available advanced attacks. Model Watermarking Removal Attacks
through Bedrock is Amazon’s own Titan (now replaced by its erase evidence of origin and undermine copyright
next incarnation, Nova). Amongst others, Titan includes a enforcement, as well as trust. The ability to imperceptibly
set of models that generate images from text prompts alter images and create "authentic" forgeries raises
called Titan Image Generator. These models incorporate concerns about deepfakes and manipulating public
invisible watermarks into all generated images. Although perception. With the evolution of AI technology, the risks
embedding digital watermarks is definitely a step in the associated with its misuse also evolve, emphasizing the
right direction and can vastly help in fighting deepfakes, the importance of robust safeguards.
early implementation of the Titan Image Generator's
Although AWS addressed the issue promptly, the research
watermark system was found to be trivial to break.
highlighted that digital content authentication might prove
problematic.
HiddenLayer's researchers demonstrated that by leveraging
specific image manipulation techniques, an attacker can The year 2024 saw numerous developments in attack
infer Titan's watermarks, replace them, or remove them techniques targeting both predictive and generative AI
entirely, undermining the system’s ability to ensure content models, from new model evasion methods to innovative
provenance. The researchers found they could extract and backdoors to creative prompt injection techniques. These
reapply watermarks to arbitrary images, making them are very likely to continue to develop and improve over the
appear as if they were AI-generated by Titan. Adversaries coming months and years.
could use this vulnerability to spread misinformation by
making fake images seem authentic or casting doubt on
Prediction from last year: “There will be a significant
real-world events. AWS has since patched the vulnerability,
increase in adversarial attacks against AI”
ensuring its customers are no longer at risk.
THE POTENTIAL IMPACT
In addition to copyrighted materials like images, logos, audio, video, and general multimedia, digital watermarks are often
embedded in proprietary data streams or real-time market analysis tools used by stock markets and traders. If those digital
watermarks are manipulated, it could alter how trading algorithms and investors interpret data. This could lead to incorrect
trades and market disruptions since fake or misleading data can cause sudden market shifts.
Supply Chain Security
Supply chain attacks are among the most damaging to businesses in terms of money and reputation. As they exploit the
trust between the supplier and the consumer, as well as the supplier's reach across their user base, these attacks have
profound consequences. AI supply chains are growing more complex each year, yet their parts are still insufficiently
protected, creating opportunities for adversaries to perform attacks.
DATA MODEL ML OPS BUILD &
COLLECTION SOURCING TOOLING DEPLOYMENT
30

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
Numerous vulnerabilities were found in ML platforms and
tooling that could allow attackers to execute arbitrary code framework that is widely utilized by data scientists
or exfiltrate sensitive information. Adversaries were also and MLOps teams. By exploiting these bugs,
found to perform reconnaissance on poorly secured ML adversaries could achieve arbitrary code execution
servers. There were multiple cases of abuse of ML-related via malicious pickle and YAML files.
services, including the hijacking of the Hugging Face
conversion bot, account name typosquatting, dependency R, a statistical computing language, was found
compromise, and package confusion. Researchers vulnerable to arbitrary code execution via malicious
demonstrated attacks against embedded AI on household RDS files, allowing an attacker to create malicious R
camera devices. There were also developments in an packages containing embedded arbitrary code that
emerging attack vector through GPU memory. executes on the victim’s target device upon
interaction. Additionally, the ONNX model file
format faced path traversal and out-of-bounds read
vulnerabilities, risking sensitive data leakage.
VULNERABILITIES IN ML SERIALIZATION
(Serialization Formats, Platforms, and Tooling)
Other platforms with serious vulnerabilities include
The number and severity of software vulnerabilities
MindsDB, which allowed arbitrary code execution via
identified within the AI ecosystem reveal widespread
insecure eval and pickle mechanisms, and Autolabel,
issues across major ML platforms and tools. The
susceptible to malicious CSV exploitation. Cleanlab faced
most prevalent concern in 2024 was deserialization
deserialization risks tied to the Datalabs module, while
vulnerabilities, particularly involving pickle files,
Guardrails and NeMo suffered from unsafe evaluation and
which affected popular platforms like AWS
arbitrary file write vulnerabilities, respectively. Bosch
Sagemaker, TensorFlow Probability, MLFlow, and
AIShield's unsafe handling of HDF5 files enabled malicious
MindsDB. These were accompanied by unsafe code
lambda layers to execute arbitrary code.
evaluation practices using unprotected eval() or
exec() functions, as well as cross-site scripting (XSS)
Serialization security and input validation remain critical
and cross-site request forgery (CSRF) flaws. The
challenges in the AI ecosystem, with particular risks
impact of these vulnerabilities typically manifests in
surrounding model loading and data processing functions.
three main ways: arbitrary code execution on victim
There is a pressing need for robust security practices,
machines, data exfiltration, and web-based attacks
including safer deserialization methods, authentication
through UI components. Common attack vectors
measures, and sandboxing mechanisms, to safeguard AI
included malicious pickle files, crafted model files
tools against increasingly sophisticated attacks.
(especially in HDF5 format), and harmful input data
through CSV or XML files.
MLOPS PLATFORM RECONNAISSANCE
In February 2024, HiddenLayer researchers Honeypots are decoy systems designed to attract
uncovered six zero-day vulnerabilities in a popular attackers and provide valuable insights into their
MLOps platform, ClearML. Encompassing path tactics in a controlled environment. Our team
traversal, improper authentication, insecure configured honeypot systems to observe potential
storage of credentials, Cross-Site Request Forgery, adversarial behavior after identifying the
Cross-Site Scripting, and arbitrary execution aforementioned vulnerabilities within MLOps
through unsafe deserialization, these vulnerabilities platforms such as ClearML and MLflow.
collectively create a full attack chain for
public-facing servers. A few months later, ten
deserialization flaws were disclosed in MLFlow, a
31

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
nteraction with their on-device AI systems. By hooking into
In November 2024, HiddenLayer researchers
the inference process, the researchers successfully
detected an external actor accessing our ClearML
developed adversarial patches capable of bypassing the AI’s
honeypot system. Analysis of the server logs
object detection. These patches caused the cameras to
showed the connection was referred from the
misclassify people as other objects, such as vehicles,
Chinese-based tool ‘FOFA’ (Fingerprint of All), which
effectively suppressing motion notifications.
is used to search for public-facing systems using
particular queries. In December 2024, the same was
The research highlights the challenges of securing edge AI
observed in our MLFlow instance. These isolated
devices, which must balance limited computational
incidents only occurred once for each mentioned
resources with reliable detection and robust security. As
honeypot system throughout their entire duration.
AI-enabled devices become more prevalent, they are likely
The significance of this finding is that it strongly
to attract increased attention from adversaries,
suggests an external actor was using FOFA to
emphasizing the need for proactive measures to safeguard
search for public-facing MLOps platforms and then
these systems.
connect to them. This demonstrates how critical it
is to ensure all aspects of your AI infrastructure are
securely configured and tracked.
ABUSING ML SERVICES
Abusing ML services presents a growing threat, as
ATTACKS AGAINST AI EMBEDDED IN DEVICES adversaries exploit machine learning APIs, models,
and infrastructure to evade detection, automate
The line between our physical and digital worlds is
attacks, and manipulate AI-driven decision-making
becoming increasingly blurred, with more of our lives
systems.
being lived and influenced through various devices,
screens, and sensors than ever before. Lots of these
devices implement embedded AI systems that help
automate arduous tasks that would have typically
Dependency Compromise
required human oversight. The integration of AI offers
features such as automatic detection of persons,
Package repositories such as PyPi constitute a lucrative
pets, vehicles, and packages, eliminating the need for
opportunity for adversaries, who can leverage industry
constant human monitoring. From security cameras
reliance and limited vulnerability scanning to deploy
to smart fridges, Internet-of-things (IoT) devices are
malware, either through package compromise or
becoming smarter and more autonomous daily. How
typosquatting.
easily can these devices be fooled, though?
In December 2024, a major supply chain attack occurred,
Wyze is a manufacturer of smart devices and a popular affecting the widely used Ultralytics Python package. The
choice for home surveillance systems, video doorbells, and attacker initially compromised the GitHub actions workflow
baby monitors. HiddenLayer researchers investigated to bundle malicious code directly into four project releases
Wyze’s V3 Pro and V4 cameras, which utilize on-device Edge on PyPi and Github, deploying an XMRig crypto miner to
AI to detect and classify objects such as people, packages, victim machines. The malicious packages were available to
pets, and vehicles when motion is detected. Their research download for over 12 hours before being taken down,
uncovered a critical command injection vulnerability that potentially resulting in a substantial number of victims.
provided root shell access to the cameras. This access
enabled an in-depth examination of the devices and direct
interaction with their on-device AI systems. By hooking into
the cameras. This access enabled an in-depth examination
of the devices and direct interaction cameras. This access
enabled an in-depth examination of the devices and direct i
32

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
THE POTENTIAL IMPACT
Ultralytics is used in various industries, including
manufacturing, healthcare, agriculture, autonomous
vehicles, security, environmental monitoring, and
logistics. In retail, it is used to automate inventory
management, identify shoplifting attempts, and analyze
customer behavior. A supply chain compromise in any of
these environments could have been more than just a
crypto miner siphoning away spare compute capacity. It
could be a ransomware package or an info stealer that
causes a material event to an organization.
Package Confusion
Another attack vector that emerged with the LLMs was
package confusion. As we all know by now, LLMs
occasionally hallucinate, and sometimes they hallucinate
nonexisting software packages. The attackers can test
different LLMs to check what package names appear in
hallucinations most often and then create malicious
packages using these names, relying on the fact that it
might be rather difficult for the user to realize that the
package was hallucinated before it was created.
of all package names generated
19.7%
by 16 different LLM models were
nonexistent.
A paper published in June 2024 evaluated the
likelihood of package hallucination by code
generation models across several programming
languages. Researchers discovered that roughly one
in five (19.7%) of all package names generated by 16
different LLM models were nonexistent—a
whopping 205474 unique hallucinated packages!
With such a ratio of true to false information, the
potential threat of supply chain attacks based on
package confusion is immense.
Package hallucination can be reduced using techniques
that involve supervised fine-tuning, self-detected feedback,
and Retrieval Augmented Generation.
33

AI THREAT LANDSCAPE 2025
Hugging Face in Focus:
Security Gaps in the Global
AI Platform
Founded in 2016 as a humble chatbot service, Hugging Face
quickly transformed into what became the biggest AI model 1,435,000 model repositories on
Hugging Face
repository to date. It hosts millions of pre-trained models,
datasets, and other ML artifacts and provides space for
testing and demoing machine learning projects. Countless
machine learning engineers utilize resources from Hugging As of 18th of February 2025, there are over 1,435,000 model
Face as ready-to-go models are deployed in production repositories on Hugging Face. Together, these repositories
across industries by small businesses and contain more than 5 million models, totalling a whooping
megacorporations alike. Being the most popular source of 10.5 petabytes of data.
AI technology, the portal is of natural interest to cyber
adversaries looking to perform supply chain attacks.
0 500000 1000000 1500000
Hugging Face had implemented some basic security
2022-03-01
measures, including scanning repositories for threats.
2022-04-01
However, their current position mirrors many other 2022-05-01
2022-06-01
providers of AI platforms and services, who don't accept 2022-07-01 Count
2022-08-01
liability for malicious models shared or created with the use
2022-09-01 Cumulative
of their tooling. Instead, they shift the responsibility to the 2022-10-01
2022-11-01
consumer, advising to load untrusted models in a 2022-12-01
sandboxed environment only. 2023-01-01
2023-02-01
2023-03-01
Hugging Face in Numbers 2023-04-01
2023-05-01
Hugging Face experienced a rapid growth over the past 2023-06-01
2023-07-01
three years, with a significant acceleration taking place in 2023-08-01
2023-09-01
2024. Close to 100,000 new repositories are added each
2023-10-01
month, up from 5,000 and 15,000 at the beginning of 2022 2023-11-01
2023-12-01
and 2023 respectively. 2024-01-01
2024-02-01
2024-03-01
2024-04-01
KEY STAT
2024-05-01
2024-06-01
USE OF PRE-TRAINED AI MODELS 2024-07-01
2024-08-01
2024-09-01
2024-10-01
2024-11-01
of companies use pre-trained 2024-12-01
97% 2025-01-01
models from repositories like
Hugging Face, AWS, or Azure.
34

AAAIII   TTTHHHRRREEEAAATTT   LLLAAANNNDDDSSSCCCAAAPPPEEE   222000222455
Top 10 File Formats
The most popular model file format is still PyTorch/pickle, constituting approximately 40% of all models on this portal
(PyTorch commonly uses extensions such as .bin, .pt, and .pth, although .bin might also be used occasionally by other model
formats). This is followed by the SafeTensors format with a 32% share. SafeTensors was introduced by Hugging Face as a
more secure alternative to PyTorch, and thanks to the automated conversion service, a large proportion of repositories now
provide both PyTorch and SafeTensors versions of their models. Another prevalent format is GGUF (15%), while only 2% of
models are saved as ONNX. Keras, HDF5, and TensorFlow (extension .pb) are all below 1%. By size, the largest model is GGUF,
followed by Safetensors, then PyTorch.
| MODELS ON HUGGING FACE  |             |             | MODELS ON HUGGING FACE  |            |            |
| ----------------------- | ----------- | ----------- | ----------------------- | ---------- | ---------- |
| BY FILE COUNT           |             |             | BY SIZE                 |            |            |
|                         |             | FILES COUNT |                         |            | TOTAL SIZE |
| FILE EXTENSION          | FILES COUNT |             | FILE EXTENSION          | TOTAL SIZE |            |
|                         |             | (PERCENT)   |                         |            | (PERCENT)  |
.gguf
| .safetensors | 1,700,889 | 31.49% |              | 5.19 PB   | 49.51% |
| ------------ | --------- | ------ | ------------ | --------- | ------ |
| .bin         | 1,230,636 | 22.78% | .safetensors | 2.75 PB   | 26.28% |
| .gguf        | 802,927   | 14.86% | .bin         | 874.84 TB | 8.16%  |
| .pt          | 764,895   | 14.16% | .pt          | 482.21 TB | 4.50%  |
| .pth         | 371,029   | 6.87%  | .part1of2    | 204.45 TB | 1.91%  |
| .zip         |           |        | .part2of2    | 198.52 TB | 1.85%  |
|              | 179,726   | 3.33%  |              |           |        |
| .onnx        | 107,649   | 1.99%  | .pth         | 82.14 TB  | 0.77%  |
| .pkl         | 105,296   | 1.95%  | .tar         | 72.87 TB  | 0.68%  |
| .tar         | 39,906    | 0.74%  | .ckpt        | 58.48 TB  | 0.55%  |
| .ckpt        | 39,257    | 0.73%  | .zip         | 48.88 TB  | 0.46%  |
| .pb          | 19,084    | 0.35%  | .h5          | 13.07 TB  | 0.12%  |
| .h5          | 18,758    | 0.35%  | .onnx        | 7.67 TB   | 0.07%  |
| .part1of2    | 6,764     | 0.13%  | .pkl         | 3.81 TB   | 0.04%  |
| .part2of2    | 6,764     | 0.13%  | .pickle      | 1.71 TB   | 0.02%  |
| .pickle      | 5,545     | 0.10%  | .keras       | 481.38 GB | 0.00%  |
| .keras       | 1,325     | 0.02%  | .pb          | 308.72 GB | 0.00%  |
| .mlmodel     | 863       | 0.02%  | .hdf5        | 186.94 GB | 0.00%  |
| .hdf5        | 184       | 0.00%  | .mlmodel     | 6.04 GB   | 0.00%  |
35

AAAIII TTTHHHRRREEEAAATTT LLLAAANNNDDDSSSCCCAAAPPPEEE 222000222455
Although safer file formats are slowly gaining traction, the
Abusing Hugging Face Spaces
insecure PyTorch/pickle format is still very widely used. Old
habits die hard and a large proportion of engineers still
prefer to use familiar tools over the secure ones. This means Cloud services, such as Hugging Face Spaces, can also be
a lot of people are potentially exposed to malicious models used to host and run other types of malware. This can result
exploiting flawed serialization formats. not only in the degradation of service but also in legal
troubles for the service provider.
Abusing Hugging Face Conversion Bot
Over the last couple of years, we have observed an
interesting case illustrating the unintended usage of
The Hugging Face Safetensors conversion space, together Hugging Face Spaces. A handful of Hugging Face users have
with the associated bot, is a popular service for converting abused Spaces to run crude bots for an Iranian messaging
machine learning models saved in unsafe file formats into a app called Rubika. Rubika, typically deployed as an Android
more secure format, namely SafeTensors. It’s designed to application, was previously available on the Google Play app
give Hugging Face’s users a safer alternative if they are store until 2022, when it was removed – presumably to
concerned about serious security flaws in formats like comply with US export restrictions and sanctions. The
pickle. However, in its early days, the service had been government of Iran sponsors the app and has recently been
vulnerable to abuse, as during the conversion, the original facing multiple accusations of bias and privacy breaches.
model would be unsafely loaded into memory, potentially
executing malicious code. We came across over a hundred different Hugging Face
Spaces hosting various Rubika bots with functionalities
While the service operates in a sandbox environment, the ranging from seemingly benign to potentially unwanted or
attackers could still find multiple ways of abusing it, from malicious, depending on their use. Several bots contained
escaping the sandbox to exfiltrating sensitive information. functionality such as collecting information about users,
HiddenLayer researchers demonstrated that by uploading a groups, and channels, downloading/uploading files, or
specially crafted model, it would have been possible for an sending out mass messages. Although we don’t have
attacker to extract the conversion bot’s access token. As all enough information about their intended purpose, these
users can request conversion for any model stored in a bots could be utilized to spread spam, phishing,
public repository, having these credentials would allow the disinformation, or propaganda. Their dubiousness is
attackers to impersonate the bot and request changes to additionally amplified by the fact that most are heavily
any repository on the Hugging Face platform. Pull requests obfuscated.
from this service will likely be accepted by the owner
without dispute since they originate from a trusted source.
Account Typosquatting
By abusing this vulnerability, the attackers could upload
malicious models, implant neural backdoors, or degrade
Typosquatting is a technique long known to adversaries
performance – posing a considerable supply chain risk. To
who often register misspelled domains to be used in
make things worse, it was also possible to persist malicious
phishing attacks. This technique can also be applied to
code inside the service so that models could be hijacked
registering rogue accounts on AI-related portals, such as
automatically as they were converted.
model repositories. Attackers can impersonate a known,
trusted company to lure victims into downloading malicious
Although the bug was promptly fixed, this research
models. Researchers from Dropbox recently presented a full
showcased how a simple mistake in implementing a service
attack chain scenario, including Hugging Face account
on a popular model hosting platform could lead to a
typosquatting, at BH Asia.
widespread breach, potentially affecting hundreds of
thousands of model repositories.
36

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
Attacks on Clusters and Hosting Services
ATTACKS AGAINST ML INFRASTRUCTURE
With the growing complexity of AI-based systems, deploying
AI models can sometimes prove troublesome. These models
GPU Attacks depend on various libraries and frameworks, often on very
specific versions of them. To simplify the deployment and
Since training AI requires extensive computing power, most improve scalability and portability, many organizations
modern AI models are trained and executed on a Graphics utilize solutions such as Docker or Kubernetes to
Processing Unit (GPU), as opposed to traditional software containerize their AI applications. Apps packaged as a
that usually runs on a CPU. Although designed for container come bundled with all required dependencies and
processing images and videos, GPUs have quickly found can be easily distributed and installed. The container
applications in scientific computing and machine learning, isolates the app from the underlying system, providing
where tasks are computationally demanding and involve additional security and portability. However, containers are
vast amounts of data. However, due to them not being a not bulletproof.
target for adversaries, many GPUs still lack the security
measures implemented over the years in CPUs in response
In September 2024, Wiz researchers discovered a
to malicious attacks. For example, GPUs usually have far
vulnerability in the NVIDIA Container Toolkit and
inferior memory protection to their CPU counterparts. This
GPU Operator that allowed attackers to escape the
opens up a new vector for attacks against AI.
container and gain access to the host system. Since
containers are often perceived as akin to sandboxes
and, therefore, more secure, users might be
tempted to test a model, even downloaded from
In January 2024, researchers disclosed a
untrusted sources, if it comes as a container. In a
vulnerability dubbed LeftoverLocals affecting
single-tenant environment, running a malicious
Apple, AMD, and Qualcomm GPUs. This
container can result in attackers gaining control of
vulnerability allows for data recovery from GPU
the user’s machine. In shared environments,
local memory created by another process.
though, adversaries could gain access to data and
Researchers demonstrated that an adversary could
applications on the same node or cluster, which can
access another user's interactive LLM session and
have more far-reaching consequences.
reconstruct the model’s responses.
Another technique of GPU memory exploitation
was presented at the 33rd USENIX Security
Symposium in August 2024. Certain buffer overflow MALICIOUS MODELS IN THE WILD
vulnerabilities in NVIDIA GPUs allow attackers to
Throughout the past year, we observed malicious
perform code injection and code reuse attacks.
models on platforms like Hugging Face and
Researchers demonstrated a case study of a
VirusTotal. These models contained simple payloads
corruption attack on a deep neural network, where
injected via serialization vulnerabilities in
an adversary could modify the model’s weights in
PyTorch/pickle, Keras, and TensorFlow. Although
the GPU memory, significantly degrading the
some can be attributed to the research community,
model’s accuracy.
we're seeing more and more payloads that are very
unlikely to be coming from researchers. These
include reverse-shells, stagers, downloaders, and
infostealers. We are also increasingly seeing large
language models maliciously fine-tuned or poisoned
at training time being shared on Hugging Face.
37

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
As it’s still an emerging attack vector, it's difficult to assess solutions, most of which, at the moment, don't even scan
the true scale of the problem. More sophisticated targeted model files, so whatever ends up there is usually shared by
attacks will leave little to no trace in public repositories. researchers or threat actors testing early / non-sensitive
Most files on VirusTotal are uploaded by anti-malware versions of their malware.
Supply Chain Attacks
PYTHON
ML MODEL
LOADER
Pickle Injection
Upload Deployment
Steganography
Lateral
Movement
PAYLOAD
RANSOMWARE BACKDOORS SPYWARE COIN MINERS
Supply chain attacks using ML artifacts might not yet be as
Prediction from last year: “Supply chain
widespread as attacks using traditional software. However,
attacks using ML artifacts will become
we’ve seen a significant increase in interest around AI
much more common”
supply chain by cybercriminals and can expect this vector
to grow over the coming years.
38

PART 3
Advancements in Security
for AI
AI Red Teaming Evolution
ADVERSARIAL TOOLING
The need to test AI systems against adversarial attacks has
The year 2024 was all about generative AI, so the
evolved throughout the past year. The White House
focus of adversarial tooling released this year was
Executive Order on Safe, Secure, and Trustworthy
understandably on GenAI pen-testing.
Development and Use of Artificial Intelligence in October of
2023 made efforts not only to define what AI red teaming is
Many open-source AI red teaming tools are available,
but also to urge organizations to go through the process of
such as PyRIT and Garak, as well as commercial
making sure their AI systems are resilient. Other best
options, such as HiddenLayer’s Automated Red
practice frameworks, such as the NIST AI Risk Management
Teaming utility. The function of such tools is to
Framework and the upcoming EU AI Act, also have similar
quickly and reliably test an AI system against known
wording around how organizations should red-team their AI
attacks by sending a list of static or mutated prompts
systems before putting them into production.
to the target model or even dynamically crafting
prompts to achieve an attacker-specified objective.
KEY STAT
AI SECURITY BUDGETS FOR 2025
The Python Risk Identification Tool (PyRIT),
released by Microsoft in February 2024, is an
open-source automation framework designed to
of organizations have
95% help AI red-teaming activities. It uses datasets
increased their budgets for
securing AI in 2024 consisting of prompts and prompt templates to
perform attacks, which can be either single-turn
(static prompt used in an isolated request) or
39

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
multi-turn (dynamic prompt templates used in
Throughout 2024, the HiddenLayer Professional
simulated interactions). The scoring engine then
Services team has assessed AI deployments for
evaluates outputs from the target model to
multiple customers. Below are a few highlights f
calculate the risk score. Besides security flaws,
rom these engagements:
such as susceptibility to jailbreaking, data leakage,
or code execution, PyRIT can also be used to
System prompts aren't foolproof: We
identify broader AI risks, including bias and
consistently uncover leaked system
hallucinations.
prompts similar to those of many
foundational models. Sensitive safety
Another LLM pen-testing tool was introduced by NVIDIA at instructions within these prompts risk
DEF CON 2024. Generative AI Red-Teaming and Assessment public exposure, and bypassing system
prompts is often achievable.
Kit (garak) provides a framework for testing language
models against a range of attacks, from generating
In-depth defense is essential: No single
disallowed content to training data leakage to attacks on
security measure is foolproof. Combining
the underlying system. Garak attack probes generate a
model alignment, strong system prompts,
series of prompts sent to the target model. The list of
and input/output analysis helps mitigate
prompt attempts can be analyzed to build an alternative set
adversarial AI attacks effectively.
of modified prompts. Multiple detection mechanisms then
process the final output of the model to return the overall Open-source security falls behind: Most
risk score. Thanks to its open-source nature and dynamic open-source AI security tools, including
community, garak is constantly updated with new prompts model scanners and prompt analyzers, are
and techniques. outdated and easily bypassed by skilled
attackers.
AI RED TEAMING BEST PRACTICES
Automated red teaming tools are valuable for
creating a quick baseline reading of a model's degree Updates to Existing
of vulnerability as well as assessing the low-hanging
Defensive Frameworks
fruit of known AI vulnerabilities. Due to their
automated nature these tools can also be used to run
periodic scans for regression testing or maintaining
compliance. However, it remains critical for human
WHAT’S NEW IN MITRE
red teamers to identify more nuanced vulnerabilities
by assessing AI systems against novel attack
MITRE ATLAS is a knowledge base of adversarial
techniques.
tactics and techniques for AI-enabled systems. It's
designed to help businesses and institutions stay up
to date on the latest attacks and defenses against
KEY STAT attacks targeting AI. The ATLAS matrix is modeled
after the MITRE ATT&CK framework, which is
RED TEAMING OF AI MODELS
well-known and used in the cybersecurity industry to
understand attack chains and adversary behaviors.
of IT teams conduct manual
red teaming for AI models in
35%
production, while 24%
conduct automated red
teaming
40

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
In June 2024, MITRE's Center for Threat-Informed Defense In 2023, OWASP released the Top 10 Machine Learning risks.
launched a new collaborative initiative called the Secure AI These controls help developers and security teams identify
research project to expand the MITRE ATLAS database and attack vectors, model threats and implement prevention
help develop strategies to mitigate risks to AI systems. The measures. These risks, paired with frameworks like ATLAS,
project aims to facilitate the rapid exchange of information clarify threats to machine learning and provide actionable
about the evolving AI threat landscape by sharing guidance.
anonymized data from AI-related incidents. Its diverse
participants include industry leaders from the technology,
communications, finance, and healthcare sectors.
In late 2024, OWASP released an updated version
of the OWASP Top 10 for LLM Applications 2025.
This list covers items such as prompt injection,
WHAT’S NEW IN OWASP
output handling, and excessive agency. This new
The Open Worldwide Application Security Project version reflects the rapidly evolving landscape of
(OWASP) is a non-profit organization and online LLM and Generative AI applications by
community that provides free guidance and reorganizing some previous vulnerabilities and
resources, such as articles, documentation, and tools adding new ones. For example, the Model Denial of
in the field of application security. The OWASP Top 10 Service and the Model Theft threats were
lists comprise the most critical security risks faced by combined into the new Unbounded Consumption
various web technologies, such as access control threat, and the Vector and Embedding
and cryptographic failures. Weaknesses threat was added, showing growing
concern over the risks associated with Retrieval
Augmented Generation (RAG) systems. A mapping
showing the relationships between the 2023 and
2025 versions of the threats is shown below.
2025 OWASP Top 10 LLMs
LLM01: Promt Injection
LLM02: Sensitive Information Disclosure OWASP also released two additional documents for
practitioners. The LLM Applications Cybersecurity
LLM03: Supply Chain and Governance Checklist provides a list of items
to consider when deploying an AI application. The
LLM and Generative AI Security Solutions
LLM04: Date and Model Poisoning
Landscape is a searchable collection of traditional
and emerging security controls for managing AI
LLM05: Improper Output Handling
application risks.
LLM06: Excessive Agency
LLM07: System Prompt Leakage
LLM08: Vector and Embedding Weaknesses
LLM09: Misinformation
LLM10: Unbounded Consumption
41

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
Adopting cryptographic signing for ML models, as proposed
by the OpenSSF Model Signing SIG, could establish trust in
WHAT’S NEW IN NIST
the ML supply chain. Signing enables verifiable claims on
The NIST AI Risk Management Framework (AI RMF), ML artifacts and metadata, creating tamper-proof
initially released in January 2023, remains a vital attestations from hardware to models and datasets. Tools
resource for managing AI risks. It provides voluntary like Sigstore can facilitate these signatures while integrating
guidelines to help organizations integrate supply-chain metadata, such as SLSA predicates, to ensure
trustworthiness, safety, and accountability into AI transparency and accountability throughout the ML
systems. Its core framework outlines four essential development process. Coupled with analysis tools like
functions—govern, map, measure, and GUAC, signed artifacts provide the ability to trace, verify,
manage—offering actionable steps for mitigating and respond swiftly to potential threats, building safeguards
AI-related risks. to protect the integrity of ML ecosystems.
The OpenSSF Model Signing SIG recently released its first
implementation and invites participants to test and
contribute. Additionally, the OpenSSF AI/ML has a working
In July 2024, NIST expanded its framework with the group that addresses broader software security issues in AI.
Generative Artificial Intelligence Profile
(NIST-AI-600-1). Developed in response to an
October 2023 Executive Order, this profile focuses
AIBOM / MLBOM
on the unique risks of generative AI, offering
tailored guidance to help organizations align their Software bill of materials (or SBOM) is a security
risk management strategies with the challenges concept that dates back to the 2010s but gained
posed by these advanced systems. widespread popularity in the last few years, some of it
thanks to US government mandates.
Supporting tools like the AI RMF Playbook and the
Trustworthy and Responsible AI Resource Center further
With software supply chains becoming increasingly
enhance its usability, providing practical resources and
complex and supply chain attacks becoming increasingly
global alignment for organizations adopting the framework.
devastating, it's imperative for organizations to have a high
level of visibility into the components of any third-party
New Security Initiatives products they rely on. SBOMs help define a list of a software
package's components, dependencies, and metadata,
including information regarding licensing, versions, and
vulnerabilities. Besides improving visibility, security, and risk
MODEL PROVENANCE &
management, SBOMs also enable the tracking of vulnerable
CRYPTOGRAPHIC SIGNING code and the determination of its impact on the software.
Cryptographic signing is a cornerstone of digital
The initiative of AIBOM (also called MLBOM) aims to
security, ensuring the integrity and authenticity of
translate the ideas behind SBOM into the AI ecosystem,
communications, software, and documents in
enabling organizations to better understand their AI
industries like finance, healthcare, and software
inventory and provide traceability and auditability. AIBOM
development. However, despite the critical role of
includes information about models, training procedures,
machine learning (ML), no standardized method
data pipelines, and performance and helps to implement
exists to cryptographically verify the origins or
and govern AI responsibly. At the forefront of the decision
integrity of ML models and artifacts, leaving them
on the AIBOM standards are NIST, OWASP, CycloneDX, and
vulnerable to tampering and trust issues.
SPDX.
42

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
The fast-paced developments in AI safety measures, as well
as the number of new security initiatives around AI, are the
Coalition for Secure AI
result of growing collaboration between data scientists,
The Coalition for Secure AI (CoSAI), established in cybersecurity specialists, and lawmakers. People from
July 2024, is an open-source initiative under the different industries and backgrounds are coming together
OASIS global standards body to foster a to face the unprecedented risks brought on by the rapid
collaborative ecosystem to tackle the fragmented evolution of AI and come up with mitigations.
AI security landscape.
Last year’s prediction: “Data scientists will
partner with security practitioners to
CoSAI brings together industry leaders, academic
secure their models”
institutions, and prominent experts to address critical
challenges in AI security through three dedicated
workstreams:
New Guidance and
Workstream 1: Ensuring the security of software Legislation
supply chains for AI systems
Workstream 2: Equipping defenders to navigate In 2024, the United States and the European Union took
an evolving cybersecurity landscape significant steps to regulate artificial intelligence to address
the growing risk concerns. The EU enacted the Artificial
Workstream 3: Establishing governance
Intelligence Act (AI Act) on August 1st, 2024. The EU AI Act
frameworks for AI security
became the world's first comprehensive AI law, classifying
AI applications by risk level—from prohibited to minimal
CoSAI's membership includes an impressive array of
risk—and imposing strict standards on high-risk AI tools,
participants, ranging from industry giants to innovative AI
such as those used in biometric identification and financial
startups, each working together to provide guidance and
decision-making.
tooling to practitioners to create Secure-by-Design AI
systems
In the U.S., AI regulatory activity increased substantially,
with nearly 700 AI-related bills introduced across various
states, a significant rise from under 200 in 2023. Despite this
Joint Cyber Defense Collaborative (JCDC)
surge, there is no unified federal approach, leading to a
patchwork of state-level regulations.
The Joint Cyber Defense Collaborative (JCDC) is a
cybersecurity partnership between the U.S.
government and private sector organizations,
serving as the government's central hub for In October 2023, President Biden issued an
cross-sector collaboration and joint cyber defense Executive Order on the Safe, Secure, and
planning. In January 2025, the JCDC released its AI Trustworthy Development and Use of Artificial
Cybersecurity Collaboration Playbook as a guide for Intelligence, which directed NIST, OMB, and other
voluntary information sharing to address agencies to initiate activities to guide and regulate
vulnerabilities and cyber threats in AI Systems, AI in the United States. However, with the change of
aiming to foster collaboration among government, administrations that occurred on Jan 20, 2025, the
industry, and international partners. This playbook Biden AI executive order was revoked. This signifies
was developed following two in-person tabletop a shift of responsibility to the states to regulate
exercises simulating real-world AI cyberattacks and legislation as AI development continues. However,
involved over 150 individual participants from the actual implications remain to be seen as many
inter-agency partners and private sector actions from Biden’s order have already been
organizations, including HiddenLayer. completed by NIST, OMB, and other agencies to set
43

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
These developments reflect not only shifts in policy that
policies and standards. In conjunction with have occurred rapidly in some cases in the United States
rescinding Biden's executive order, President Trump but also clear international intent, specifically from the EU,
signed a new directive establishing an Artificial to balance the rapid advancement of AI technologies with
Intelligence Action Plan within 180 days. This plan the need for security, ethical standards, and human rights
aims to develop policies that sustain and enhance protections. The rest of 2025 will undoubtedly witness more
America's global AI dominance to promote human changes in regulations and philosophical as well as policy
flourishing, economic competitiveness, and national conflicts between nations, political parties, and industry as
security. we all attempt to figure out the future promise of AI and
avoid the potential perils.
In October 2024, the Office of Management and
Budget (OMB) released the Advancing the
Responsible Acquisition of Artificial Intelligence in
Government memorandum. OMB noted that the
successful use of commercially provided AI requires
responsible procurement. This memo ensures that
when Federal agencies acquire AI, they appropriately
manage risks and performance, promote a
competitive marketplace, and implement structures
to govern and manage their business processes
related to acquiring AI. It is uncertain whether the
Trump administration will modify Federal AI
Procurement Guidelines already released by OMB.
Various states have introduced AI-related bills. Colorado
became the first state to enact a comprehensive law
relating to developing and deploying certain artificial
intelligence (AI) systems in Sept 2024—the Colorado AI Act
(CAIA), which goes into effect on February 1, 2026. The CAIA
adopts a risk-based approach to AI regulation that shares
substantial similarities with the EU AI Act. California
introduced the "Safe and Secure Innovation for Frontier
Artificial Intelligence Models Act", which aimed to mandate
safety tests for advanced AI models but was vetoed by
Governor Newsom in September 2024.
Additionally, in September 2024, the U.S., UK, and European
Commission signed the Council of Europe’s Framework
Convention on AI and human rights, democracy, and the
rule of law, marking the first international legally binding
agreement on AI.
44

PART 4
Predictions and
Recommendations
Predictions for 2025
It’s time to dust off the crystal ball once again! Over the past year, AI has truly been at the forefront of cyber security,
with increased scrutiny from attackers, defenders, developers, and academia. As various forms of generative AI drive
mass AI adoption, we find that the threats are not lagging far behind, with LLMs, RAGs, Agentic AI, integrations, and
plugins being a hot topic for researchers and miscreants alike.
Looking ahead, we expect the AI security landscape will
face even more sophisticated challenges in 2025:
01. Agentic AI as a Target 02. Erosion of Trust in Digital Content
Integrating agentic AI will blur the lines between adversarial As deepfake technologies become more accessible, audio,
AI and traditional cyberattacks, leading to a new wave of visual, and text-based digital content trust will face
targeted threats. Expect phishing and data leakage via near-total erosion. Expect to see advances in AI
agentic systems to be a hot topic. watermarking to help combat such attacks.
45

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
03. Adversarial AI 06. Emergence of AIPC (AI-Powered Cyberattacks)
Organizations will integrate adversarial machine learning As hardware vendors capitalize on AI with advances in
(ML) into standard red team exercises, testing for AI bespoke chipsets and tooling to power AI technology,
vulnerabilities proactively before deployment. expect to see attacks targeting AI-capable endpoints
intensify, including:
04. AI-Specific Incident Response
Local model tampering. Hijacking models to
abuse predictions, bypass refusals and perform
For the first time, formal incident response guidelines
harmful actions.
tailored to AI systems will be developed, providing a
structured approach to AI-related security breaches. Data poisoning.
Expect to see playbooks developed for AI risks.
Abuse of agentic systems. For example, prompt
injections in emails and documents to exploit
05. Advanced Threat Evolution local models.
Exploitation of vulnerabilities in 3rd party AI
Fraud, misinformation, and network attacks will escalate as
libraries and models
AI evolves across domains such as computer vision (CV),
audio, and natural language processing (NLP). Expect to
see attackers leveraging AI to increase both the speed and
scale of attack, as well as semi-autonomous offensive
models designed to aid in penetration testing and security
research.
Recommendations for the Security Practitioner
In the 2024 threat report, we made several recommendations for organizations to consider that were similar in
concept to existing security-related control practices but built specifically for AI, such as:
Discovery and Asset Management Model Robustness and Validation
Identifying and cataloging AI systems and related assets. Strengthening models to withstand adversarial attacks and
verifying their integrity.
Risk Assessment and Threat Modeling
Secure Development Practices
Evaluating potential vulnerabilities and attack vectors
specific to AI. Embedding security throughout the AI development
lifecycle.
Data Security and Privacy
Continuous Monitoring and Incident Response
Ensuring robust protection for sensitive datasets.
Establishing proactive detection and response mechanisms
for AI-related threats.
46

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
These practices remain foundational as organizations navigate the continuously unfolding AI threat landscape.
Building on these recommendations, 2024 marked a turning point in the AI landscape. The rapid AI 'electrification' of
industries saw nearly every IT vendor integrate or expand AI capabilities, while service providers across sectors—from HR to
law firms and accountants—widely adopted AI to enhance offerings and optimize operations. This made 2024 the year that
AI-related third—and fourth-party risk issues became acutely apparent.
During the Security for AI Council meeting at Black Hat this year, the subject of AI third-party risk arose. Everyone in the
council acknowledged it was generally a struggle, with at least one member noting that a "requirement to notify before AI is
used/embedded into a solution” clause was added in all vendor contracts. The council members who had already been
asking vendors about their use of AI said those vendors didn’t have good answers. They “don't really know,” which is not only
surprising but also a noted disappointment. The group acknowledged traditional security vendors were only slightly better
than others, but overall, most vendors cannot respond adequately to AI risk questions. The council then collaborated to
create a detailed set of AI 3rd party risk questions. We recommend you consider adding these key questions to your existing
vendor evaluation processes going forward.
Do you scan your models for malicious
? ?
Where did your model come from? code? How do you determine if the model
is poisoned?
Do you detect, alert, and respond to What AI incident response policies does
?
?
mitigate risks that are identified in the your organization have in place in the event
OWASP LLM Top 10? of security incidents that impact the safety,
privacy, or security of individuals or the
function of the model?
What is your threat model for AI-related
?
attacks? Are your threat model and
mitigations mapped or aligned to the ? Do you validate the integrity of the data
MITRE Atlas? presented by your AI system and/or model?
Remember that the security landscape—and AI technology—is dynamic and rapidly changing. It's crucial to stay informed
about emerging threats and best practices. Regularly update and refine your AI-specific security program to address new
challenges and vulnerabilities.
And a note of caution. In many cases, responsible and ethical AI frameworks fall short of ensuring models are secure before
they go into production and after an AI system is in use. They focus on things such as biases, appropriate use, and privacy.
While these are also required, don’t confuse these practices for security.
47

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
HiddenLayer
Resources
PRODUCTS AND SERVICES
HiddenLayer AISec Platform
is a GenAI Protection Suite that is purpose-built to ensure the integrity of
your AI models throughout the MLOps pipeline. The Platform provides
detection and response for GenAI and traditional AI models to detect prompt
injections, adversarial AI attacks, and digital supply chain vulnerabilities.
Learn More Download PDF
HiddenLayer AI Detection & Response (AIDR)
is the first of its kind cybersecurity solution that monitors, detects, &
responds to Adversarial Artificial Intelligence attacks targeted at GenAI &
traditional ML models.
Learn More Download PDF
HiddenLayer Model Scanner
analyzes models to identify hidden cybersecurity risks & threats such as
malware, vulnerabilities & integrity issues. Its advanced scanning engine is
built to analyze your artificial intelligence models, meticulously inspecting
each layer & component to detect possible signs of malicious activity,
including malware, tampering & backdoors.
Learn More Download PDF
HiddenLayer Automated Red Teaming for AI
brings the efficiency, scalability, and precision needed to identify
vulnerabilities in AI systems before attackers exploit them.
Learn More Download PDF
HiddenLayer Professional Services
is a multi-faceted services engagement that utilizes our deep domain
expertise in cybersecurity, artificial intelligence, and threat research.
Learn More Download PDF
49

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
HiddenLayer
Resources
HIDDENLAYER RESEARCH
ShadowLogic
A novel method for creating backdoors in neural network models.
Indirect Prompt Injection of Claude Computer Use
Discover the security risks of Anthropic's Claude Computer Use, including
indirect prompt injection attacks.
ShadowGenes: Uncovering Model Genealogy
Model genealogy is the practice of tracking machine learning models'
lineage, origins, modifi cations, and training processes.
Attack on AWS Bedrock’s ‘Titan’
Discover how to manipulate digital watermarks generated by Amazon Web
Services (AWS) Bedrock Titan Image Generator.
New Gemini for Workspace Vulnerability
Google Gemini for Workspace remains vulnerable to many forms of indirect
prompt injections.
R-bitrary Code Execution: Vulnerability in R’s Deserialization
Learn about a zero-day deserialization vulnerability in the popular
programming language R, widely used within government and medical
research, that could result in a supply chain attack.
Boosting Security for AI: Unveiling KROP
Many LLMs rely on prompt fi lters and alignment techniques to safeguard
their integrity in AI. However, these measures are not foolproof.
A Guide to AI Red Teaming
AI red teaming is an important strategy for any organization that leverages
artifi cial intelligence.
The Beginners Guide to LLMs and Generative AI
Learn about the basics of GenAI and gain a foundational understanding of
the world of LLMs.
50

AAII TTHHRREEAATT LLAANNDDSSCCAAPPEE 22002245
About HiddenLayer
HiddenLayer
a Gartner-recognized Cool Vendor for AI Security, is the leading provider of
Security for AI. Its security platform helps enterprises safeguard the machine
learning models behind their most important products. HiddenLayer is the
only company to offer turnkey security for AI that does not add unnecessary
complexity to models and does not require access to raw data and
algorithms. Founded by a team with deep roots in security and ML,
HiddenLayer aims to protect enterprise’s AI solutions from inference, bypass,
extraction attacks, and model theft. The company is backed by a group of
strategic investors, including M12, Microsoft’s Venture Fund, Moore Strategic
Ventures, Booz Allen Ventures, IBM Ventures, and Capital One Ventures.
LEARN MORE: FOLLOW US:
www.hiddenlayer.com Research Twitter LinkedIn
REQUEST A DEMO:
https://hiddenlayer.com/book-a-demo/
AUTHORS/CONTRIBUTORS
A special thank you to the teams that made this report come to life:
Marta Janus, Principal Security Researcher
Eoin Wickens, Technical Research Director
Tom Bonner, SVP, Research
Malcolm Harkins, Chief Security & Trust Officer
Jason Martin, Director, Adversarial Research
Travis Smith, VP of ML Threat Operations
Ryan Tracey, Principal Security Researcher
Jim Simpson, Threat Operations Specialist
Samantha Pearcy, Manager of Content Strategy
Kristen Tarlecki, VP of Marketing
Arman Abdulhayoglu, Director of Product Marketing
Kieran Evans, Principal Security Researcher
Kevin Finnigin, Principal Security Researcher
Marcus Kan, AI Security Researcher
Ravi Balakrishnan, Principal Security Researcher
Kenneth Yeung, AI Threat Researcher
Kasimir Schulz, Director, Security Research
Megan David, AI Researcher
51