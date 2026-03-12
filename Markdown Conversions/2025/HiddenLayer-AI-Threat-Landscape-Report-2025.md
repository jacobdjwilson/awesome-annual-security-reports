# AI Threat Landscape Report 2025

## Table of Contents
- [Foreword](#foreword)
- [Security for AI Survey Insights at a Glance](#security-for-ai-survey-insights-at-a-glance)
- [2024 AI Threat Landscape Timeline](#2024-ai-threat-landscape-timeline)
- [What’s New in AI](#whats-new-in-ai)
- [Part 1: Risks Related to the Use of AI](#part-1-risks-related-to-the-use-of-ai)
- [Part 2: Risks Faced by AI-based Systems](#part-2-risks-faced-by-ai-based-systems)

---

# Foreword

Artificial intelligence is no longer an emerging force – it is an embedded reality shaping economies, industries, and societies at an unparalleled scale. Every mission, organization, and individual has felt its impact, with AI driving efficiency, automation, and problem-solving breakthroughs. Yet, as its influence expands, so too do the risks. The past year has emphasized a critical truth: the greatest threat to AI is not the technology itself but the people who exploit it.

The AI landscape is evolving rapidly, with open-source models and smaller, more accessible architectures accelerating innovation and risk. These advancements lower the barrier to entry, allowing more organizations to leverage AI but they also widen the attack surface, making AI systems more susceptible to manipulation, data poisoning, and adversarial exploitation. Meanwhile, hyped new model trends like DeepSeek are introducing unprecedented risks and impacting geopolitical power dynamics.

Artificial intelligence remains the most vulnerable technology ever deployed at scale. Its security challenges extend far beyond code, impacting every phase of its lifecycle from training and development to deployment and real-world operations. Adversarial AI threats are evolving, blending traditional cybersecurity tactics with new, AI-specific attack methods.

In this report, we explore the vulnerabilities introduced by these developments and their real-world consequences for commercial and federal sectors. We provide insights from IT security and data science leaders actively defending against these threats, along with predictions informed by HiddenLayer’s hands-on experience in AI security. Most importantly, we highlight the advancements in security controls essential for protecting AI in all its forms.

As AI continues to drive progress, securing its future is a responsibility shared by developers, data scientists, and security professionals alike. This report is a crucial resource for understanding and mitigating AI risks in a rapidly shifting landscape.

We are proud to present the second annual HiddenLayer AI Threat Landscape Report, expanding on last year’s insights and charting the path forward for securing AI.

TITO
CEO & Co-Founder
(Unassisted by LLMs)

---

# Security for AI Survey Insights at a Glance

AI has become indispensable to modern business, powering critical functions and driving innovation. However, as organizations increasingly rely on AI, traditional security measures have struggled to keep up with the growing sophistication of threats.

The 2025 survey results highlight this tension: while many IT leaders recognize AI’s central role in their company’s success, there’s more work to implement comprehensive security measures. Issues like shadow AI, ownership debates, and limited security tool adoption contribute to the challenges. However, the survey results show an optimistic shift toward prioritizing AI security, with organizations investing more in defenses, governance frameworks, transparency, and resources to address emerging threats.

These insights come from a survey commissioned by HiddenLayer, where 250 IT decision-makers from a cross-section of industries shared insights into their organizations’ AI security practices.

### AI’s Critical Role in Business Success
- **89%** of IT leaders reported that most or all AI models in production are critical to their business’s success.
- **100%** stated that AI and ML projects are critical or important to revenue generation within the next 18 months (up from 98% last year).

### Rising Security Breaches and Vulnerabilities
- **74%** of IT leaders reported to definitely know if they had an AI breach in 2024 (up from 67% reporting last year).
- **75%** say AI attacks have increased or remained the same from the previous year.
- **87%** reported being able to identify the source of the breach (up from 77% last year).

### Sources & Motivations of AI Attacks
**Type of AI Systems Attacked from Identified Breaches:**
- **45%** Malware in Models Pulled from Public Repositories
- **33%** Attack on Internal or External Chatbot
- **21%** Third-Party Applications

**Top 3 Sources of AI Attacks:**
1. Criminal Hacking Groups
2. Third-Party Service Providers
3. Freelance Hackers

**Top 3 Motivations for AI Attacks:**
1. Data Theft
2. Financial Gain
3. Business Disruption

---

# 2024 AI Threat Landscape Timeline

![Timeline of AI milestones, vulnerabilities, and security initiatives from January to December 2024]

---

# What’s New in AI

The past year brought significant advancements in AI across multiple domains, including multimodal models, retrieval-augmented generation (RAG), humanoid robotics, and agentic AI.

### Multimodal Models
Multimodal models became popular with the launch of OpenAI’s GPT-4o. What makes a model “multimodal” is its ability to create multimedia content (images, audio, and video) in response to text- or audio-based prompts, or vice versa.

### Retrieval-Augmented Generation (RAG)
RAG combines large language models (LLMs) with external knowledge retrieval to produce accurate and contextually relevant responses. By having access to a trusted database, an LLM can produce more up-to-date responses less prone to hallucinations.

### Agentic AI
The goal of agentic AI is to construct assistants that would be unprecedentedly autonomous, make decisions without human feedback, and perform tasks without requiring intervention.

### Humanoid Robots
Rapid advancements in natural language have expedited machines’ ability to perform a wide range of tasks while offering near-human interactions. Examples include Tesla's Optimus and Agility Robotics' Digit.

### The Rise of Open-Weight Models
Open-weight models are models whose weights are made available to the broader public. While they allow for local implementation and fine-tuning, they also introduce risks regarding security flaws, biases, and hidden backdoors.

---

# Part 1: Risks Related to the Use of AI

There are several areas of concern where malicious or improper use of AI can create trouble for individuals, organizations, and societies alike.

### The Use of AI in Cybercrime
Adversaries are leveraging AI for a multitude of illicit tasks, from enhancing phishing campaigns and financial scams to generating malicious code and automating attacks.

### The Use of AI in Political Campaigns
The use of AI in political campaigning brings unprecedented challenges, as spreading disinformation, influencing public opinion, and manipulating trends is easier than ever before.

### Unintended Consequences of AI Use
- **Hallucinations and Accuracy Issues**: GenAI models still suffer from occasional hallucinations, where they output misleading information.
- **Privacy Issues**: Information shared with AI tools is not always private; some AI assistants were found to capture and share private conversations.
- **Copyright Issues**: Artists have expressed concerns over the unregulated use of copyrighted content in the training of GenAI models.
- **Emotional Dependency**: Interactions with AI companions can be damaging to human well-being, as seen in tragic cases of emotional dependency leading to harmful outcomes.

---

# Part 2: Risks Faced by AI-based Systems

Risks faced by AI can be roughly bucketed into three categories:

1. **Adversarial Machine Learning Attacks**: Attacks against AI algorithms aimed to alter the model’s behavior, evade AI-based detection, or steal the underlying technology.
2. **Generative AI System Attacks**: Attacks against AI’s filters and restrictions intended to generate harmful or illegal content.
3. **Supply Chain Attacks**: Attacks against ML platforms, libraries, models, and other ML artifacts, whose goal is to deliver traditional malware.

### Adversarial Machine Learning Attacks
- **Model Evasion**: Adversaries manipulate the input to a model to fool it into making an incorrect prediction.
- **Data Poisoning**: Attackers modify entries in an existing dataset or inject a new, specially doctored portion of data to bias or degrade model performance.
- **Model Backdooring**: A secret unwanted behavior introduced to the targeted AI by an adversary, often triggered by specific inputs.
- **Model Theft**: Unauthorized replication of a machine-learning model to steal intellectual property or proprietary knowledge.

### Attacks Against GenAI
- **Prompt Injection**: A technique that involves embedding additional instructions in an LLM query, altering the way the model behaves.
- **Indirect Injection**: Adversaries embed malicious prompts inside external content (like files or URLs) that the model processes, allowing them to perform prompt injection attacks indirectly.

---

PE 2025
AI THREAT LANDSCAPE 2024

HACKING-AS-A-SERVICE

With the multitude of bypass techniques, the game
between those implementing the guardrails and
those trying to break them is cat-and-mouse. The fact
that an adversarial prompt used successfully
yesterday might not work the day after has spun a
rise of automated attack solutions. These include
hacking-as-a-service schemes in which experienced
adversaries provide a paid platform where users can
access "jailbroken" GenAI services.

In January 2025, Microsoft revealed that they've shut
down a cybercriminal service aimed at bypassing the
safety measures in Microsoft's GenAI solutions.
Adversaries compromised several accounts of
legitimate Microsoft users and set up a guardrail
bypass toolkit to provide unrestricted access to the
models. The service ran between July and
September 2024, allowing anyone who paid the fee
to create malicious, illegal, or harmful content.
Microsoft brought up legal action against both
cybercriminals and the customers of this service.

PRIVACY ATTACKS

The rise of generative AI and foundation models has
introduced signiﬁcant privacy and intellectual
property risks. Trained on massive datasets from
public and proprietary sources, these models often
inadvertently memorize sensitive or copyrighted
information, such as personally identiﬁable
information (PII), passwords, and proprietary content,
making them vulnerable to extraction. Their
complexity further enables attacks like model
inversion, where adversaries infer sensitive training
data attributes and membership inference to
determine if speciﬁc data points were in the training
set. These risks are particularly concerning in
sensitive domains like healthcare, ﬁnance, and
education, where private information may
unintentionally appear in model outputs.

28

Research has highlighted several attacks that
exemplify and deepen these risks:

Training Data Extraction Attacks allow
adversaries to reconstruct sensitive or
copyrighted content, such as private
communications or proprietary datasets,
from model outputs.

Memorization Attacks show that models
can regurgitate rare or unique data points
from their training set, including PII or
intellectual property when queried with
tailored prompts. These attacks expose
vulnerabilities in foundational AI models
and raise ethical and legal questions
about using such technologies.

Adversarial Prompting Attacks similarly
exploit the models by manipulating them
into replicating copyrighted material or
revealing sensitive information while
sidestepping built-in protections.

These scenarios accentuate the tension between ensuring
model functionality and protecting intellectual property and
privacy.

The authors of Class Attribute Inference Attacks
demonstrated that their approach can accurately
deduce undisclosed attributes, such as hair color,
gender, and racial appearance, particularly in facial
recognition models. Notably, the study reveals that
adversarially robust models are more susceptible to
such privacy leaks, indicating a trade-off between
robustness and privacy.

Many GenAI solutions require access to personal data in
order to enhance the experience and improve workﬂows.
Attackers can exploit this property to leak users' credentials
and other sensitive information via indirect prompt
injections.

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

Released in November 2023, Microsoft Copilot
Studio is a platform for building, deploying, and
managing custom AI assistants (a.k.a. copilots).
The platform boosts security features, including
robust authentication, data loss prevention, and
content guardrails for the created bots. However,
these safety measures are not bulletproof. At
BlackHat US 2024, a former Microsoft researcher
presented 15 different ways adversaries could use
Copilot bots to exﬁltrate sensitive data. One of
these techniques demonstrated a phishing attack
containing an indirect prompt injection, allowing an
attacker to access the victim's internal emails. The
adversary could then craft and send out rogue
communication, posing as the victim.

Governments and regulatory bodies have started
addressing these emerging risks, but signiﬁcant gaps
remain. By combining innovation, comprehensive
regulation, and organizational oversight, generative AI's
privacy and ethical challenges can be better managed,
fostering trust in these transformative technologies.

MANIPULATING GEN AI WATERMARKS

Since the GenAI revolution, which happened almost
overnight, everyone has been able to generate their
own content, be it text, images, audio, or video.
Generative AI models have been vastly improved over
the last two years, yielding very convincing, realistic
results that are hardly any different from the outputs
of humans. This begs an important question: How
can we differentiate between an authentic picture or
ﬁlm taken with a camera and an AI-produced fake?
Not easily at all.

To minimize the risk posed by all kinds of deepfakes, tech
companies strive to develop mechanisms to let the user
know that the content was synthetically generated. One
such mechanism is watermarking, i.e., embedding specially
crafted digital marks inside all the outputs generated by a
model. These watermarks are meant to ensure content
provenance and authenticity; however, they are not
infallible, and one of the early implementations of this
technology was proven to be easily manipulated.

29

Introduced by Amazon in April 2023 and made publicly
available later that year, Amazon Bedrock is a service
designed to help build and scale generative AI applications.
It offers access to foundation models from leading AI
companies via a single API. One family of models available
through Bedrock is Amazon’s own Titan (now replaced by its
next incarnation, Nova). Amongst others, Titan includes a
set of models that generate images from text prompts
called Titan Image Generator. These models incorporate
invisible watermarks into all generated images. Although
embedding digital watermarks is deﬁnitely a step in the
right direction and can vastly help in ﬁghting deepfakes, the
early implementation of the Titan Image Generator's
watermark system was found to be trivial to break.

HiddenLayer's researchers demonstrated that by leveraging
speciﬁc image manipulation techniques, an attacker can
infer Titan's watermarks, replace them, or remove them
entirely, undermining the system’s ability to ensure content
provenance. The researchers found they could extract and
reapply watermarks to arbitrary images, making them
appear as if they were AI-generated by Titan. Adversaries
could use this vulnerability to spread misinformation by
making fake images seem authentic or casting doubt on
real-world events. AWS has since patched the vulnerability,
ensuring its customers are no longer at risk.

THE POTENTIAL IMPACT

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

The investigation highlighted the broader implications of
such vulnerabilities in the age of AI-generated media. While
watermarking is a promising method to verify content
authenticity, the study revealed its susceptibility to
advanced attacks. Model Watermarking Removal Attacks
erase evidence of origin and undermine copyright
enforcement, as well as trust. The ability to imperceptibly
alter images and create "authentic" forgeries raises
concerns about deepfakes and manipulating public
perception. With the evolution of AI technology, the risks
associated with its misuse also evolve, emphasizing the
importance of robust safeguards.

Although AWS addressed the issue promptly, the research
highlighted that digital content authentication might prove
problematic.

The year 2024 saw numerous developments in attack
techniques targeting both predictive and generative AI
models, from new model evasion methods to innovative
backdoors to creative prompt injection techniques. These
are very likely to continue to develop and improve over the
coming months and years.

Prediction from last year: “There will be a signiﬁcant
increase in adversarial attacks against AI”

In addition to copyrighted materials like images, logos, audio, video, and general multimedia, digital watermarks are often
embedded in proprietary data streams or real-time market analysis tools used by stock markets and traders. If those digital
watermarks are manipulated, it could alter how trading algorithms and investors interpret data. This could lead to incorrect
trades and market disruptions since fake or misleading data can cause sudden market shifts.

Supply Chain Security

Supply chain attacks are among the most damaging to businesses in terms of money and reputation. As they exploit the
trust between the supplier and the consumer, as well as the supplier's reach across their user base, these attacks have
profound consequences. AI supply chains are growing more complex each year, yet their parts are still insufficiently
protected, creating opportunities for adversaries to perform attacks.

DATA
COLLECTION

MODEL
SOURCING

ML OPS
TOOLING

BUILD &
DEPLOYMENT

30

Numerous vulnerabilities were found in ML platforms and
tooling that could allow attackers to execute arbitrary code
or exﬁltrate sensitive information. Adversaries were also
found to perform reconnaissance on poorly secured ML
servers. There were multiple cases of abuse of ML-related
services, including the hijacking of the Hugging Face
conversion bot, account name typosquatting, dependency
compromise, and package confusion. Researchers
demonstrated attacks against embedded AI on household
camera devices. There were also developments in an
emerging attack vector through GPU memory.

VULNERABILITIES IN ML SERIALIZATION

(Serialization Formats, Platforms, and Tooling)

The number and severity of software vulnerabilities
identiﬁed within the AI ecosystem reveal widespread
issues across major ML platforms and tools. The
most prevalent concern in 2024 was deserialization
vulnerabilities, particularly involving pickle ﬁles,
which affected popular platforms like AWS
Sagemaker, TensorFlow Probability, MLFlow, and
MindsDB. These were accompanied by unsafe code
evaluation practices using unprotected eval() or
exec() functions, as well as cross-site scripting (XSS)
and cross-site request forgery (CSRF) ﬂaws. The
impact of these vulnerabilities typically manifests in
three main ways: arbitrary code execution on victim
machines, data exﬁltration, and web-based attacks
through UI components. Common attack vectors
included malicious pickle ﬁles, crafted model ﬁles
(especially in HDF5 format), and harmful input data
through CSV or XML ﬁles.

In February 2024, HiddenLayer researchers
uncovered six zero-day vulnerabilities in a popular
MLOps platform, ClearML. Encompassing path
traversal, improper authentication, insecure
storage of credentials, Cross-Site Request Forgery,
Cross-Site Scripting, and arbitrary execution
through unsafe deserialization, these vulnerabilities
collectively create a full attack chain for
public-facing servers. A few months later, ten
deserialization ﬂaws were disclosed in MLFlow, a

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

framework that is widely utilized by data scientists
and MLOps teams. By exploiting these bugs,
adversaries could achieve arbitrary code execution
via malicious pickle and YAML ﬁles.

R, a statistical computing language, was found
vulnerable to arbitrary code execution via malicious
RDS ﬁles, allowing an attacker to create malicious R
packages containing embedded arbitrary code that
executes on the victim’s target device upon
interaction. Additionally, the ONNX model ﬁle
format faced path traversal and out-of-bounds read
vulnerabilities, risking sensitive data leakage.

Other platforms with serious vulnerabilities include
MindsDB, which allowed arbitrary code execution via
insecure eval and pickle mechanisms, and Autolabel,
susceptible to malicious CSV exploitation. Cleanlab faced
deserialization risks tied to the Datalabs module, while
Guardrails and NeMo suffered from unsafe evaluation and
arbitrary ﬁle write vulnerabilities, respectively. Bosch
AIShield's unsafe handling of HDF5 ﬁles enabled malicious
lambda layers to execute arbitrary code.

Serialization security and input validation remain critical
challenges in the AI ecosystem, with particular risks
surrounding model loading and data processing functions.
There is a pressing need for robust security practices,
including safer deserialization methods, authentication
measures, and sandboxing mechanisms, to safeguard AI
tools against increasingly sophisticated attacks.

MLOPS PLATFORM RECONNAISSANCE

Honeypots are decoy systems designed to attract
attackers and provide valuable insights into their
tactics in a controlled environment. Our team
conﬁgured honeypot systems to observe potential
adversarial behavior after identifying the
aforementioned vulnerabilities within MLOps
platforms such as ClearML and MLﬂow.

31

In November 2024, HiddenLayer researchers
detected an external actor accessing our ClearML
honeypot system. Analysis of the server logs
showed the connection was referred from the
Chinese-based tool ‘FOFA’ (Fingerprint of All), which
is used to search for public-facing systems using
particular queries. In December 2024, the same was
observed in our MLFlow instance. These isolated
incidents only occurred once for each mentioned
honeypot system throughout their entire duration.
The signiﬁcance of this ﬁnding is that it strongly
suggests an external actor was using FOFA to
search for public-facing MLOps platforms and then
connect to them. This demonstrates how critical it
is to ensure all aspects of your AI infrastructure are
securely conﬁgured and tracked.

ATTACKS AGAINST AI EMBEDDED IN DEVICES

The line between our physical and digital worlds is
becoming increasingly blurred, with more of our lives
being lived and inﬂuenced through various devices,
screens, and sensors than ever before. Lots of these
devices implement embedded AI systems that help
automate arduous tasks that would have typically
required human oversight. The integration of AI offers
features such as automatic detection of persons,
pets, vehicles, and packages, eliminating the need for
constant human monitoring. From security cameras
to smart fridges, Internet-of-things (IoT) devices are
becoming smarter and more autonomous daily. How
easily can these devices be fooled, though?

Wyze is a manufacturer of smart devices and a popular
choice for home surveillance systems, video doorbells, and
baby monitors. HiddenLayer researchers investigated
Wyze’s V3 Pro and V4 cameras, which utilize on-device Edge
AI to detect and classify objects such as people, packages,
pets, and vehicles when motion is detected. Their research
uncovered a critical command injection vulnerability that
provided root shell access to the cameras. This access
enabled an in-depth examination of the devices and direct
interaction with their on-device AI systems. By hooking into
the  cameras. This access enabled an in-depth examination
of the devices and direct interaction cameras. This access
enabled an in-depth examination of the devices and direct i

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

nteraction with their on-device AI systems. By hooking into
the inference process, the researchers successfully
developed adversarial patches capable of bypassing the AI’s
object detection. These patches caused the cameras to
misclassify people as other objects, such as vehicles,
effectively suppressing motion notiﬁcations.

The research highlights the challenges of securing edge AI
devices, which must balance limited computational
resources with reliable detection and robust security. As
AI-enabled devices become more prevalent, they are likely
to attract increased attention from adversaries,
emphasizing the need for proactive measures to safeguard
these systems.

ABUSING ML SERVICES

Abusing ML services presents a growing threat, as
adversaries exploit machine learning APIs, models,
and infrastructure to evade detection, automate
attacks, and manipulate AI-driven decision-making
systems.

Dependency Compromise

Package repositories such as PyPi constitute a lucrative
opportunity for adversaries, who can leverage industry
reliance and limited vulnerability scanning to deploy
malware, either through package compromise or
typosquatting.

In December 2024, a major supply chain attack occurred,
affecting the widely used Ultralytics Python package. The
attacker initially compromised the GitHub actions workﬂow
to bundle malicious code directly into four project releases
on PyPi and Github, deploying an XMRig crypto miner to
victim machines. The malicious packages were available to
download for over 12 hours before being taken down,
potentially resulting in a substantial number of victims.

32

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

19.7%

of all package names generated
by 16 different LLM models were
nonexistent.

A paper published in June 2024 evaluated the
likelihood of package hallucination by code
generation models across several programming
languages. Researchers discovered that roughly one
in ﬁve (19.7%) of all package names generated by 16
different LLM models were nonexistent—a
whopping 205474 unique hallucinated packages!
With such a ratio of true to false information, the
potential threat of supply chain attacks based on
package confusion is immense.

Package hallucination can be reduced using techniques
that involve supervised ﬁne-tuning, self-detected feedback,
and Retrieval Augmented Generation.

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

33

AI THREAT LANDSCAPE 2025

Hugging Face in Focus:
Security Gaps in the Global
AI Platform

Founded in 2016 as a humble chatbot service, Hugging Face
quickly transformed into what became the biggest AI model
repository to date. It hosts millions of pre-trained models,
datasets, and other ML artifacts and provides space for
testing and demoing machine learning projects. Countless
machine learning engineers utilize resources from Hugging
Face as ready-to-go models are deployed in production
across industries by small businesses and
megacorporations alike. Being the most popular source of
AI technology, the portal is of natural interest to cyber
adversaries looking to perform supply chain attacks.

Hugging Face had implemented some basic security
measures, including scanning repositories for threats.
However, their current position mirrors many other
providers of AI platforms and services, who don't accept
liability for malicious models shared or created with the use
of their tooling. Instead, they shift the responsibility to the
consumer, advising to load untrusted models in a
sandboxed environment only.

Hugging Face in Numbers

Hugging Face experienced a rapid growth over the past
three years, with a signiﬁcant acceleration taking place in
2024. Close to 100,000 new repositories are added each
month, up from 5,000 and 15,000 at the beginning of 2022
and 2023 respectively.

KEY STAT

USE OF PRE-TRAINED AI MODELS

97%

of companies use pre-trained
models from repositories like
Hugging Face, AWS, or Azure.

1,435,000

model repositories on
Hugging Face

As of 18th of February 2025, there are over 1,435,000 model
repositories on Hugging Face. Together, these repositories
contain more than 5 million models, totalling a whooping
10.5 petabytes of data.

0

500000

1000000

1500000

2022-03-01
2022-04-01
2022-05-01
2022-06-01
2022-07-01
2022-08-01
2022-09-01
2022-10-01
2022-11-01
2022-12-01
2023-01-01
2023-02-01
2023-03-01
2023-04-01
2023-05-01
2023-06-01
2023-07-01
2023-08-01
2023-09-01
2023-10-01
2023-11-01
2023-12-01
2024-01-01
2024-02-01
2024-03-01
2024-04-01
2024-05-01
2024-06-01
2024-07-01
2024-08-01
2024-09-01
2024-10-01
2024-11-01
2024-12-01
2025-01-01

Count

Cumulative

34

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024
AI THREAT LANDSCAPE 2025

Top 10 File Formats

The most popular model ﬁle format is still PyTorch/pickle, constituting approximately 40% of all models on this portal
(PyTorch commonly uses extensions such as .bin, .pt, and .pth, although .bin might also be used occasionally by other model
formats). This is followed by the SafeTensors format with a 32% share. SafeTensors was introduced by Hugging Face as a
more secure alternative to PyTorch, and thanks to the automated conversion service, a large proportion of repositories now
provide both PyTorch and SafeTensors versions of their models. Another prevalent format is GGUF (15%), while only 2% of
models are saved as ONNX. Keras, HDF5, and TensorFlow (extension .pb) are all below 1%. By size, the largest model is GGUF,
followed by Safetensors, then PyTorch.

MODELS ON HUGGING FACE
BY FILE COUNT

MODELS ON HUGGING FACE
BY SIZE

FILE EXTENSION

FILES COUNT

FILES COUNT

(PERCENT)

FILE EXTENSION

TOTAL SIZE

.safetensors

1,700,889

.bin

.gguf

.pt

.pth

.zip

.onnx

.pkl

.tar

.ckpt

.pb

.h5

.part1of2

.part2of2

.pickle

.keras

.mlmodel

.hdf5

1,230,636

802,927

764,895

371,029

179,726

107,649

105,296

39,906

39,257

19,084

18,758

6,764

6,764

5,545

1,325

863

184

31.49%

22.78%

14.86%

14.16%

6.87%

3.33%

1.99%

1.95%

0.74%

0.73%

0.35%

0.35%

0.13%

0.13%

0.10%

0.02%

0.02%

0.00%

.gguf

5.19 PB

.safetensors

2.75 PB

.bin

.pt

.part1of2

.part2of2

.pth

.tar

.ckpt

.zip

.h5

.onnx

.pkl

.pickle

.keras

.pb

.hdf5

874.84 TB

482.21 TB

204.45 TB

198.52 TB

82.14 TB

72.87 TB

58.48 TB

48.88 TB

13.07 TB

7.67 TB

3.81 TB

1.71 TB

481.38 GB

308.72 GB

186.94 GB

.mlmodel

6.04 GB

TOTAL SIZE

(PERCENT)

49.51%

26.28%

8.16%

4.50%

1.91%

1.85%

0.77%

0.68%

0.55%

0.46%

0.12%

0.07%

0.04%

0.02%

0.00%

0.00%

0.00%

0.00%

35

Although safer ﬁle formats are slowly gaining traction, the
insecure PyTorch/pickle format is still very widely used. Old
habits die hard and a large proportion of engineers still
prefer to use familiar tools over the secure ones. This means
a lot of people are potentially exposed to malicious models
exploiting ﬂawed serialization formats.

Abusing Hugging Face Conversion Bot

The Hugging Face Safetensors conversion space, together
with the associated bot, is a popular service for converting
machine learning models saved in unsafe ﬁle formats into a
more secure format, namely SafeTensors. It’s designed to
give Hugging Face’s users a safer alternative if they are
concerned about serious security ﬂaws in formats like
pickle. However, in its early days, the service had been
vulnerable to abuse, as during the conversion, the original
model would be unsafely loaded into memory, potentially
executing malicious code.

While the service operates in a sandbox environment, the
attackers could still ﬁnd multiple ways of abusing it, from
escaping the sandbox to exﬁltrating sensitive information.
HiddenLayer researchers demonstrated that by uploading a
specially crafted model, it would have been possible for an
attacker to extract the conversion bot’s access token. As all
users can request conversion for any model stored in a
public repository, having these credentials would allow the
attackers to impersonate the bot and request changes to
any repository on the Hugging Face platform. Pull requests
from this service will likely be accepted by the owner
without dispute since they originate from a trusted source.

By abusing this vulnerability, the attackers could upload
malicious models, implant neural backdoors, or degrade
performance – posing a considerable supply chain risk. To
make things worse, it was also possible to persist malicious
code inside the service so that models could be hijacked
automatically as they were converted.

Although the bug was promptly ﬁxed, this research
showcased how a simple mistake in implementing a service
on a popular model hosting platform could lead to a
widespread breach, potentially affecting hundreds of
thousands of model repositories.

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024
AI THREAT LANDSCAPE 2025

Abusing Hugging Face Spaces

Cloud services, such as Hugging Face Spaces, can also be
used to host and run other types of malware. This can result
not only in the degradation of service but also in legal
troubles for the service provider.

Over the last couple of years, we have observed an
interesting case illustrating the unintended usage of
Hugging Face Spaces. A handful of Hugging Face users have
abused Spaces to run crude bots for an Iranian messaging
app called Rubika. Rubika, typically deployed as an Android
application, was previously available on the Google Play app
store until 2022, when it was removed – presumably to
comply with US export restrictions and sanctions. The
government of Iran sponsors the app and has recently been
facing multiple accusations of bias and privacy breaches.

We came across over a hundred different Hugging Face
Spaces hosting various Rubika bots with functionalities
ranging from seemingly benign to potentially unwanted or
malicious, depending on their use. Several bots contained
functionality such as collecting information about users,
groups, and channels, downloading/uploading ﬁles, or
sending out mass messages. Although we don’t have
enough information about their intended purpose, these
bots could be utilized to spread spam, phishing,
disinformation, or propaganda. Their dubiousness is
additionally ampliﬁed by the fact that most are heavily
obfuscated.

Account Typosquatting

Typosquatting is a technique long known to adversaries
who often register misspelled domains to be used in
phishing attacks. This technique can also be applied to
registering rogue accounts on AI-related portals, such as
model repositories. Attackers can impersonate a known,
trusted company to lure victims into downloading malicious
models. Researchers from Dropbox recently presented a full
attack chain scenario, including Hugging Face account
typosquatting, at BH Asia.

36

ATTACKS AGAINST ML INFRASTRUCTURE

Attacks on Clusters and Hosting Services

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

GPU Attacks

Since training AI requires extensive computing power, most
modern AI models are trained and executed on a Graphics
Processing Unit (GPU), as opposed to traditional software
that usually runs on a CPU. Although designed for
processing images and videos, GPUs have quickly found
applications in scientiﬁc computing and machine learning,
where tasks are computationally demanding and involve
vast amounts of data. However, due to them not being a
target for adversaries, many GPUs still lack the security
measures implemented over the years in CPUs in response
to malicious attacks. For example, GPUs usually have far
inferior memory protection to their CPU counterparts. This
opens up a new vector for attacks against AI.

In January 2024, researchers disclosed a
vulnerability dubbed LeftoverLocals affecting
Apple, AMD, and Qualcomm GPUs. This
vulnerability allows for data recovery from GPU
local memory created by another process.
Researchers demonstrated that an adversary could
access another user's interactive LLM session and
reconstruct the model’s responses.

Another technique of GPU memory exploitation
was presented at the 33rd USENIX Security
Symposium in August 2024. Certain buffer overﬂow
vulnerabilities in NVIDIA GPUs allow attackers to
perform code injection and code reuse attacks.
Researchers demonstrated a case study of a
corruption attack on a deep neural network, where
an adversary could modify the model’s weights in
the GPU memory, signiﬁcantly degrading the
model’s accuracy.

With the growing complexity of AI-based systems, deploying
AI models can sometimes prove troublesome. These models
depend on various libraries and frameworks, often on very
speciﬁc versions of them. To simplify the deployment and
improve scalability and portability, many organizations
utilize solutions such as Docker or Kubernetes to
containerize their AI applications. Apps packaged as a
container come bundled with all required dependencies and
can be easily distributed and installed. The container
isolates the app from the underlying system, providing
additional security and portability. However, containers are
not bulletproof.

In September 2024, Wiz researchers discovered a
vulnerability in the NVIDIA Container Toolkit and
GPU Operator that allowed attackers to escape the
container and gain access to the host system. Since
containers are often perceived as akin to sandboxes
and, therefore, more secure, users might be
tempted to test a model, even downloaded from
untrusted sources, if it comes as a container. In a
single-tenant environment, running a malicious
container can result in attackers gaining control of
the user’s machine. In shared environments,
though, adversaries could gain access to data and
applications on the same node or cluster, which can
have more far-reaching consequences.

MALICIOUS MODELS IN THE WILD

Throughout the past year, we observed malicious
models on platforms like Hugging Face and
VirusTotal. These models contained simple payloads
injected via serialization vulnerabilities in
PyTorch/pickle, Keras, and TensorFlow. Although
some can be attributed to the research community,
we're seeing more and more payloads that are very
unlikely to be coming from researchers. These
include reverse-shells, stagers, downloaders, and
infostealers. We are also increasingly seeing large
language models maliciously ﬁne-tuned or poisoned
at training time being shared on Hugging Face.

37

As it’s still an emerging attack vector, it's difficult to assess
the true scale of the problem. More sophisticated targeted
attacks will leave little to no trace in public repositories.
Most ﬁles on VirusTotal are uploaded by anti-malware

solutions, most of which, at the moment, don't even scan
model ﬁles, so whatever ends up there is usually shared by
researchers or threat actors testing early / non-sensitive
versions of their malware.

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

Supply Chain Attacks

PYTHON
LOADER

ML MODEL

Pickle Injection

Upload

Deployment

Steganography

PAYLOAD

Lateral
Movement

RANSOMWARE

BACKDOORS

SPYWARE

COIN MINERS

Supply chain attacks using ML artifacts might not yet be as
widespread as attacks using traditional software. However,
we’ve seen a signiﬁcant increase in interest around AI
supply chain by cybercriminals and can expect this vector
to grow over the coming years.

Prediction from last year: “Supply chain
attacks using ML artifacts will become
much more common”

38

PART 3
Advancements in Security
for AI
AI Red Teaming Evolution

ADVERSARIAL TOOLING

The need to test AI systems against adversarial attacks has
evolved throughout the past year. The White House
Executive Order on Safe, Secure, and Trustworthy
Development and Use of Artiﬁcial Intelligence in October of
2023 made efforts not only to deﬁne what AI red teaming is
but also to urge organizations to go through the process of
making sure their AI systems are resilient. Other best
practice frameworks, such as the NIST AI Risk Management
Framework and the upcoming EU AI Act, also have similar
wording around how organizations should red-team their AI
systems before putting them into production.

KEY STAT

AI SECURITY BUDGETS FOR 2025

95%

of organizations have
increased their budgets for
securing AI in 2024

The year 2024 was all about generative AI, so the
focus of adversarial tooling released this year was
understandably on GenAI pen-testing.

Many open-source AI red teaming tools are available,
such as PyRIT and Garak, as well as commercial
options, such as HiddenLayer’s Automated Red
Teaming utility. The function of such tools is to
quickly and reliably test an AI system against known
attacks by sending a list of static or mutated prompts
to the target model or even dynamically crafting
prompts to achieve an attacker-speciﬁed objective.

The Python Risk Identiﬁcation Tool (PyRIT),
released by Microsoft in February 2024, is an
open-source automation framework designed to
help AI red-teaming activities. It uses datasets
consisting of prompts and prompt templates to
perform attacks, which can be either single-turn
(static prompt used in an isolated request) or

39

multi-turn (dynamic prompt templates used in
simulated interactions). The scoring engine then
evaluates outputs from the target model to
calculate the risk score. Besides security ﬂaws,
such as susceptibility to jailbreaking, data leakage,
or code execution, PyRIT can also be used to
identify broader AI risks, including bias and
hallucinations.

Another LLM pen-testing tool was introduced by NVIDIA at
DEF CON 2024. Generative AI Red-Teaming and Assessment
Kit (garak) provides a framework for testing language
models against a range of attacks, from generating
disallowed content to training data leakage to attacks on
the underlying system. Garak attack probes generate a
series of prompts sent to the target model. The list of
prompt attempts can be analyzed to build an alternative set
of modiﬁed prompts. Multiple detection mechanisms then
process the ﬁnal output of the model to return the overall
risk score. Thanks to its open-source nature and dynamic
community, garak is constantly updated with new prompts
and techniques.

AI RED TEAMING BEST PRACTICES

Automated red teaming tools are valuable for
creating a quick baseline reading of a model's degree
of vulnerability as well as assessing the low-hanging
fruit of known AI vulnerabilities. Due to their
automated nature these tools can also be used to run
periodic scans for regression testing or maintaining
compliance. However, it remains critical for human
red teamers to identify more nuanced vulnerabilities
by assessing AI systems against novel attack
techniques.

KEY STAT

RED TEAMING OF AI MODELS

35%

of IT teams conduct manual
red teaming for AI models in
production, while 24%
conduct automated red
teaming

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

Throughout 2024, the HiddenLayer Professional
Services team has assessed AI deployments for
multiple customers. Below are a few highlights f
rom these engagements:

System prompts aren't foolproof: We
consistently uncover leaked system
prompts similar to those of many
foundational models. Sensitive safety
instructions within these prompts risk
public exposure, and bypassing system
prompts is often achievable.

In-depth defense is essential: No single
security measure is foolproof. Combining
model alignment, strong system prompts,
and input/output analysis helps mitigate
adversarial AI attacks effectively.

Open-source security falls behind: Most
open-source AI security tools, including
model scanners and prompt analyzers, are
outdated and easily bypassed by skilled
attackers.

Updates to Existing
Defensive Frameworks

WHAT’S NEW IN MITRE

MITRE ATLAS is a knowledge base of adversarial
tactics and techniques for AI-enabled systems. It's
designed to help businesses and institutions stay up
to date on the latest attacks and defenses against
attacks targeting AI. The ATLAS matrix is modeled
after the MITRE ATT&CK framework, which is
well-known and used in the cybersecurity industry to
understand attack chains and adversary behaviors.

40

In June 2024, MITRE's Center for Threat-Informed Defense
launched a new collaborative initiative called the Secure AI
research project to expand the MITRE ATLAS database and
help develop strategies to mitigate risks to AI systems. The
project aims to facilitate the rapid exchange of information
about the evolving AI threat landscape by sharing
anonymized data from AI-related incidents. Its diverse
participants include industry leaders from the technology,
communications, ﬁnance, and healthcare sectors.

WHAT’S NEW IN OWASP

The Open Worldwide Application Security Project
(OWASP) is a non-proﬁt organization and online
community that provides free guidance and
resources, such as articles, documentation, and tools
in the ﬁeld of application security. The OWASP Top 10
lists comprise the most critical security risks faced by
various web technologies, such as access control
and cryptographic failures.

2025 OWASP Top 10 LLMs

 LLM01: Promt Injection

 LLM02: Sensitive Information Disclosure

 LLM03: Supply Chain

 LLM04: Date and Model Poisoning

 LLM05: Improper Output Handling

 LLM06: Excessive Agency

 LLM07: System Prompt Leakage

LLM08: Vector and Embedding Weaknesses

 LLM09: Misinformation

 LLM10: Unbounded Consumption

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

In 2023, OWASP released the Top 10 Machine Learning risks.
These controls help developers and security teams identify
attack vectors, model threats and implement prevention
measures. These risks, paired with frameworks like ATLAS,
clarify threats to machine learning and provide actionable
guidance.

In late 2024, OWASP released an updated version
of the OWASP Top 10 for LLM Applications 2025.
This list covers items such as prompt injection,
output handling, and excessive agency. This new
version reﬂects the rapidly evolving landscape of
LLM and Generative AI applications by
reorganizing some previous vulnerabilities and
adding new ones. For example, the Model Denial of
Service and the Model Theft threats were
combined into the new Unbounded Consumption
threat, and the Vector and Embedding
Weaknesses threat was added, showing growing
concern over the risks associated with Retrieval
Augmented Generation (RAG) systems. A mapping
showing the relationships between the 2023 and
2025 versions of the threats is shown below.

OWASP also released two additional documents for
practitioners. The LLM Applications Cybersecurity
and Governance Checklist provides a list of items
to consider when deploying an AI application. The
LLM and Generative AI Security Solutions
Landscape is a searchable collection of traditional
and emerging security controls for managing AI
application risks.

41

WHAT’S NEW IN NIST

The NIST AI Risk Management Framework (AI RMF),
initially released in January 2023, remains a vital
resource for managing AI risks. It provides voluntary
guidelines to help organizations integrate
trustworthiness, safety, and accountability into AI
systems. Its core framework outlines four essential
functions—govern, map, measure, and
manage—offering actionable steps for mitigating
AI-related risks.

In July 2024, NIST expanded its framework with the
Generative Artiﬁcial Intelligence Proﬁle
(NIST-AI-600-1). Developed in response to an
October 2023 Executive Order, this proﬁle focuses
on the unique risks of generative AI, offering
tailored guidance to help organizations align their
risk management strategies with the challenges
posed by these advanced systems.

Supporting tools like the AI RMF Playbook and the
Trustworthy and Responsible AI Resource Center further
enhance its usability, providing practical resources and
global alignment for organizations adopting the framework.

New Security Initiatives

MODEL PROVENANCE &

CRYPTOGRAPHIC SIGNING

Cryptographic signing is a cornerstone of digital
security, ensuring the integrity and authenticity of
communications, software, and documents in
industries like ﬁnance, healthcare, and software
development. However, despite the critical role of
machine learning (ML), no standardized method
exists to cryptographically verify the origins or
integrity of ML models and artifacts, leaving them
vulnerable to tampering and trust issues.

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

Adopting cryptographic signing for ML models, as proposed
by the OpenSSF Model Signing SIG, could establish trust in
the ML supply chain. Signing enables veriﬁable claims on
ML artifacts and metadata, creating tamper-proof
attestations from hardware to models and datasets. Tools
like Sigstore can facilitate these signatures while integrating
supply-chain metadata, such as SLSA predicates, to ensure
transparency and accountability throughout the ML
development process. Coupled with analysis tools like
GUAC, signed artifacts provide the ability to trace, verify,
and respond swiftly to potential threats, building safeguards
to protect the integrity of ML ecosystems.

The OpenSSF Model Signing SIG recently released its ﬁrst
implementation and invites participants to test and
contribute. Additionally, the OpenSSF AI/ML has a working
group that addresses broader software security issues in AI.

AIBOM / MLBOM

Software bill of materials (or SBOM) is a security
concept that dates back to the 2010s but gained
widespread popularity in the last few years, some of it
thanks to US government mandates.

With software supply chains becoming increasingly
complex and supply chain attacks becoming increasingly
devastating, it's imperative for organizations to have a high
level of visibility into the components of any third-party
products they rely on. SBOMs help deﬁne a list of a software
package's components, dependencies, and metadata,
including information regarding licensing, versions, and
vulnerabilities. Besides improving visibility, security, and risk
management, SBOMs also enable the tracking of vulnerable
code and the determination of its impact on the software.

The initiative of AIBOM (also called MLBOM) aims to
translate the ideas behind SBOM into the AI ecosystem,
enabling organizations to better understand their AI
inventory and provide traceability and auditability. AIBOM
includes information about models, training procedures,
data pipelines, and performance and helps to implement
and govern AI responsibly. At the forefront of the decision
on the AIBOM standards are NIST, OWASP, CycloneDX, and
SPDX.

42

Coalition for Secure AI

The Coalition for Secure AI (CoSAI), established in
July 2024, is an open-source initiative under the
OASIS global standards body to foster a
collaborative ecosystem to tackle the fragmented
AI security landscape.

CoSAI brings together industry leaders, academic
institutions, and prominent experts to address critical
challenges in AI security through three dedicated
workstreams:

Workstream 1: Ensuring the security of software
supply chains for AI systems

Workstream 2: Equipping defenders to navigate
an evolving cybersecurity landscape

Workstream 3: Establishing governance
frameworks for AI security

CoSAI's membership includes an impressive array of
participants, ranging from industry giants to innovative AI
startups, each working together to provide guidance and
tooling to practitioners to create Secure-by-Design AI
systems

Joint Cyber Defense Collaborative (JCDC)

The Joint Cyber Defense Collaborative (JCDC) is a
cybersecurity partnership between the U.S.
government and private sector organizations,
serving as the government's central hub for
cross-sector collaboration and joint cyber defense
planning. In January 2025, the JCDC released its AI
Cybersecurity Collaboration Playbook as a guide for
voluntary information sharing to address
vulnerabilities and cyber threats in AI Systems,
aiming to foster collaboration among government,
industry, and international partners. This playbook
was developed following two in-person tabletop
exercises simulating real-world AI cyberattacks and
involved over 150 individual participants from
inter-agency partners and private sector
organizations, including HiddenLayer.

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

The fast-paced developments in AI safety measures, as well
as the number of new security initiatives around AI, are the
result of growing collaboration between data scientists,
cybersecurity specialists, and lawmakers. People from
different industries and backgrounds are coming together
to face the unprecedented risks brought on by the rapid
evolution of AI and come up with mitigations.

Last year’s prediction: “Data scientists will
partner with security practitioners to
secure their models”

New Guidance and
Legislation

In 2024, the United States and the European Union took
signiﬁcant steps to regulate artiﬁcial intelligence to address
the growing risk concerns. The EU enacted the Artiﬁcial
Intelligence Act (AI Act) on August 1st, 2024. The EU AI Act
became the world's ﬁrst comprehensive AI law, classifying
AI applications by risk level—from prohibited to minimal
risk—and imposing strict standards on high-risk AI tools,
such as those used in biometric identiﬁcation and ﬁnancial
decision-making.

In the U.S., AI regulatory activity increased substantially,
with nearly 700 AI-related bills introduced across various
states, a signiﬁcant rise from under 200 in 2023. Despite this
surge, there is no uniﬁed federal approach, leading to a
patchwork of state-level regulations.

In October 2023, President Biden issued an
Executive Order on the Safe, Secure, and
Trustworthy Development and Use of Artiﬁcial
Intelligence, which directed NIST, OMB, and other
agencies to initiate activities to guide and regulate
AI in the United States. However, with the change of
administrations that occurred on Jan 20, 2025, the
Biden AI executive order was revoked. This signiﬁes
a shift of responsibility to the states to regulate
legislation as AI development continues. However,
the actual implications remain to be seen as many
actions from Biden’s order have already been
completed by NIST, OMB, and other agencies to set

43

policies and standards. In conjunction with
rescinding Biden's executive order, President Trump
signed a new directive establishing an Artiﬁcial
Intelligence Action Plan within 180 days. This plan
aims to develop policies that sustain and enhance
America's global AI dominance to promote human
ﬂourishing, economic competitiveness, and national
security.

In October 2024, the Office of Management and
Budget (OMB) released the Advancing the
Responsible Acquisition of Artiﬁcial Intelligence in
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
became the ﬁrst state to enact a comprehensive law
relating to developing and deploying certain artiﬁcial
intelligence (AI) systems in Sept 2024—the Colorado AI Act
(CAIA), which goes into effect on February 1, 2026. The CAIA
adopts a risk-based approach to AI regulation that shares
substantial similarities with the EU AI Act. California
introduced the "Safe and Secure Innovation for Frontier
Artiﬁcial Intelligence Models Act", which aimed to mandate
safety tests for advanced AI models but was vetoed by
Governor Newsom in September 2024.

Additionally, in September 2024, the U.S., UK, and European
Commission signed the Council of Europe’s Framework
Convention on AI and human rights, democracy, and the
rule of law, marking the ﬁrst international legally binding
agreement on AI.

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

These developments reﬂect not only shifts in policy that
have occurred rapidly in some cases in the United States
but also clear international intent, speciﬁcally from the EU,
to balance the rapid advancement of AI technologies with
the need for security, ethical standards, and human rights
protections. The rest of 2025 will undoubtedly witness more
changes in regulations and philosophical as well as policy
conﬂicts between nations, political parties, and industry as
we all attempt to ﬁgure out the future promise of AI and
avoid the potential perils.

44

PART 4
Predictions and
Recommendations

Predictions for 2025

It’s time to dust off the crystal ball once again! Over the past year, AI has truly been at the forefront of cyber security,
with increased scrutiny from attackers, defenders, developers, and academia. As various forms of generative AI drive
mass AI adoption, we ﬁnd that the threats are not lagging far behind, with LLMs, RAGs, Agentic AI, integrations, and
plugins being a hot topic for researchers and miscreants alike.

Looking ahead, we expect the AI security landscape will
face even more sophisticated challenges in 2025:

01.

 Agentic AI as a Target

02.   Erosion of Trust in Digital Content

Integrating agentic AI will blur the lines between adversarial
AI and traditional cyberattacks, leading to a new wave of
targeted threats. Expect phishing and data leakage via
agentic systems to be a hot topic.

As deepfake technologies become more accessible, audio,
visual, and text-based digital content trust will face
near-total erosion. Expect to see advances in AI
watermarking to help combat such attacks.

45

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

03.  Adversarial AI

06.  Emergence of AIPC (AI-Powered Cyberattacks)

Organizations will integrate adversarial machine learning
(ML) into standard red team exercises, testing for AI
vulnerabilities proactively before deployment.

As hardware vendors capitalize on AI with advances in
bespoke chipsets and tooling to power AI technology,
expect to see attacks targeting AI-capable endpoints
intensify, including:

04.  AI-Speciﬁc Incident Response

For the ﬁrst time, formal incident response guidelines
tailored to AI systems will be developed, providing a
structured approach to AI-related security breaches.
Expect to see playbooks developed for AI risks.

05.  Advanced Threat Evolution

Fraud, misinformation, and network attacks will escalate as
AI evolves across domains such as computer vision (CV),
audio, and natural language processing (NLP). Expect to
see attackers leveraging AI to increase both the speed and
scale of attack, as well as semi-autonomous offensive
models designed to aid in penetration testing and security
research.

Local model tampering. Hijacking models to
abuse predictions, bypass refusals and perform
harmful actions.

Data poisoning.

Abuse of agentic systems. For example, prompt
injections in emails and documents to exploit
local models.

Exploitation of vulnerabilities in 3rd party AI
libraries and models

Recommendations for the Security Practitioner

In the 2024 threat report, we made several recommendations for organizations to consider that were similar in
concept to existing security-related control practices but built speciﬁcally for AI, such as:

Discovery and Asset Management

Model Robustness and Validation

Identifying and cataloging AI systems and related assets.

Strengthening models to withstand adversarial attacks and
verifying their integrity.

Risk Assessment and Threat Modeling

Evaluating potential vulnerabilities and attack vectors
speciﬁc to AI.

Data Security and Privacy

Ensuring robust protection for sensitive datasets.

Secure Development Practices

Embedding security throughout the AI development
lifecycle.

Continuous Monitoring and Incident Response

Establishing proactive detection and response mechanisms
for AI-related threats.

46

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

These practices remain foundational as organizations navigate the continuously unfolding AI threat landscape.

Building on these recommendations, 2024 marked a turning point in the AI landscape. The rapid AI 'electriﬁcation' of
industries saw nearly every IT vendor integrate or expand AI capabilities, while service providers across sectors—from HR to
law ﬁrms and accountants—widely adopted AI to enhance offerings and optimize operations. This made 2024 the year that
AI-related third—and fourth-party risk issues became acutely apparent.

During the Security for AI Council meeting at Black Hat this year, the subject of AI third-party risk arose. Everyone in the
council acknowledged it was generally a struggle, with at least one member noting that a "requirement to notify before AI is
used/embedded into a solution” clause was added in all vendor contracts. The council members who had already been
asking vendors about their use of AI said those vendors didn’t have good answers. They “don't really know,” which is not only
surprising but also a noted disappointment. The group acknowledged traditional security vendors were only slightly better
than others, but overall, most vendors cannot respond adequately to AI risk questions. The council then collaborated to
create a detailed set of AI 3rd party risk questions. We recommend you consider adding these key questions to your existing
vendor evaluation processes going forward.

?

?

?

Where did your model come from?

Do you detect, alert, and respond to
mitigate risks that are identiﬁed in the
OWASP LLM Top 10?

What is your threat model for AI-related
attacks? Are your threat model and
mitigations mapped or aligned to the
MITRE Atlas?

?

?

?

Do you scan your models for malicious
code? How do you determine if the model
is poisoned?

What AI incident response policies does
your organization have in place in the event
of security incidents that impact the safety,
privacy, or security of individuals or the
function of the model?

Do you validate the integrity of the data
presented by your AI system and/or model?

Remember that the security landscape—and AI technology—is dynamic and rapidly changing. It's crucial to stay informed
about emerging threats and best practices. Regularly update and reﬁne your AI-speciﬁc security program to address new
challenges and vulnerabilities.

And a note of caution. In many cases, responsible and ethical AI frameworks fall short of ensuring models are secure before
they go into production and after an AI system is in use. They focus on things such as biases, appropriate use, and privacy.
While these are also required, don’t confuse these practices for security.

47

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

HiddenLayer
Resources

PRODUCTS AND SERVICES

HiddenLayer AISec Platform

is a GenAI Protection Suite that is purpose-built to ensure the integrity of

your AI models throughout the MLOps pipeline. The Platform provides

detection and response for GenAI and traditional AI models to detect prompt

injections, adversarial AI attacks, and digital supply chain vulnerabilities.

Learn More

Download PDF

HiddenLayer AI Detection & Response (AIDR)

is the ﬁrst of its kind cybersecurity solution that monitors, detects, &

responds to Adversarial Artiﬁcial Intelligence attacks targeted at GenAI &

traditional ML models.

Learn More

Download PDF

HiddenLayer Model Scanner

analyzes models to identify hidden cybersecurity risks & threats such as

malware, vulnerabilities & integrity issues. Its advanced scanning engine is

built to analyze your artiﬁcial intelligence models, meticulously inspecting

each layer & component to detect possible signs of malicious activity,

including malware, tampering & backdoors.

Learn More

Download PDF

HiddenLayer Automated Red Teaming for AI

brings the efficiency, scalability, and precision needed to identify

vulnerabilities in AI systems before attackers exploit them.

Learn More

Download PDF

HiddenLayer Professional Services

is a multi-faceted services engagement that utilizes our deep domain

expertise in cybersecurity, artiﬁcial intelligence, and threat research.

Learn More

Download PDF

49

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

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

lineage, origins, modiﬁ cations, and training processes.

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

Many LLMs rely on prompt ﬁ lters and alignment techniques to safeguard

their integrity in AI. However, these measures are not foolproof.

A Guide to AI Red Teaming

AI red teaming is an important strategy for any organization that leverages

artiﬁ cial intelligence.

The Beginners Guide to LLMs and Generative AI

Learn about the basics of GenAI and gain a foundational understanding of

the world of LLMs.

50

AI THREAT LANDSCAPE 2025
AI THREAT LANDSCAPE 2024

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

LEARN MORE:

FOLLOW US:

www.hiddenlayer.com

Research

Twitter

LinkedIn

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