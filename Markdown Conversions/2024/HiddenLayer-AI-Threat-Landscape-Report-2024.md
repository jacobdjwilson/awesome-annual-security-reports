# AI THREAT LANDSCAPE 2024 REPORT

## Table of Contents
- [Foreword](#foreword)
- [Survey Insights at a Glance](#survey-insights-at-a-glance)
- [Adversarial AI Over Time](#adversarial-ai-over-time)
- [Part 1: Risks Related to the Use of AI](#part-1-risks-related-to-the-use-of-ai)
  - [Harmful Content Creation](#harmful-content-creation)
  - [Deepfakes](#deepfakes)
  - [Data Privacy and Leakage](#data-privacy-and-leakage)
  - [Copyright Violation](#copyright-violation)
  - [Accuracy and Bias Issues](#accuracy-and-bias-issues)
  - [Other Ethical & Societal Issues](#other-ethical--societal-issues)
- [Part 2: Risks Faced by AI-based Systems](#part-2-risks-faced-by-ai-based-systems)
  - [Adversarial Machine Learning Attacks](#adversarial-machine-learning-attacks)
    - [Data Poisoning](#data-poisoning)
    - [Model Evasion](#model-evasion)
    - [Model Theft](#model-theft)
  - [Attacks Speciﬁc to Generative AI](#attacks-speciﬁc-to-generative-ai)
    - [Prompt Injection](#prompt-injection)
    - [Code Injection](#code-injection)
  - [Supply Chain Attacks](#supply-chain-attacks)
    - [ML Supply Chain Attacks](#ml-supply-chain-attacks)
    - [Malicious Models](#malicious-models)
    - [Model Backdoors](#model-backdoors)
    - [Security of Public Model Repositories](#security-of-public-model-repositories)
    - [Malevolent Third-party Contractors](#malevolent-third-party-contractors)
    - [Vulnerabilities in ML Tooling](#vulnerabilities-in-ml-tooling)
    - [Data Poisoning in Supply Chain Attacks](#data-poisoning-in-supply-chain-attacks)
  - [Threat Actors and Attack Vectors](#threat-actors-and-attack-vectors)
- [Part 3: Advancements in Security for AI](#part-3-advancements-in-security-for-ai)
  - [Offensive Security Tooling for AI](#offensive-security-tooling-for-ai)
    - [Automated Attack Frameworks](#automated-attack-frameworks)
    - [Adversarial ML Frameworks](#adversarial-ml-frameworks)
    - [Anti-Malware Evasion Tooling](#anti-malware-evasion-tooling)
    - [Model Theft Tooling](#model-theft-tooling)
    - [Model Deserialization Exploitation](#model-deserialization-exploitation)
  - [Defensive Frameworks for AI](#defensive-frameworks-for-ai)
    - [MITRE ATLAS](#mitre-atlas)
    - [NIST AI Risk Management Framework](#nist-ai-risk-management-framework)
    - [Google Secure AI Framework](#google-secure-ai-framework)
    - [OWASP Top 10](#owasp-top-10)
    - [Databricks AI Security Framework (DAISF)](#databricks-ai-security-framework-daisf)
    - [Gartner AI Trust, Risk, and Security Management (AI TRiSM)](#gartner-ai-trust-risk-and-security-management-aitrism)
    - [IBM Framework for Securing Generative AI](#ibm-framework-for-securing-generative-ai)
  - [Red Teaming and Risk Assessment](#red-teaming-and-risk-assessment)
  - [Policies and Regulations](#policies-and-regulations)
- [Part 4: Predictions and Recommendations](#part-4-predictions-and-recommendations)
  - [Predictions for the next 12 months](#predictions-for-the-next-12-months)
  - [Securing Your AI: Getting Started](#securing-your-ai-getting-started)
- [Resources](#resources)
  - [HiddenLayer Products and Services](#hiddenlayer-products-and-services)
  - [HiddenLayer Research](#hiddenlayer-research)
- [About HiddenLayer](#about-hiddenlayer)

---

# AI THREAT LANDSCAPE 2024 REPORT

The official report URL is: https://hiddenlayer.com/threatreport2024/

# AI THREAT LANDSCAPE 2024 REPORT

UNDERSTANDING THE EVOLVING
CYBERSECURITY ENVIRONMENT

---

## Foreword

Humanity has entered an unprecedented technological evolution. No mission, organization, job, or person on the planet will go unimpacted by artificial intelligence this year. Revolutionizing every data-driven opportunity, AI has the potential to bring on a new era of prosperity, allowing the quality of life to reach unimaginable heights. Like any new groundbreaking technology, the potential for greatness is paralleled only by the inherent risk. It is critical that we do not allow ourselves to tunnel solely on harvesting the benefits of AI without responsibly mitigating those risks. Make no mistake, for all the distrust of the black box nature of AI and the doom and gloom rhetoric of world domination, the greatest risk associated with AI for the foreseeable future is bad people.

Artificial intelligence is, by a wide margin, the most vulnerable technology ever to be deployed in production systems. It’s vulnerable at a code level, during training and development, post-deployment, over networks, via generative outputs, and more. We do not need to look far into the traditional cyber threat landscape to understand today’s adversarial AI attacks and predict their near-term patterns.

In this report, we shed light on these vulnerabilities and how they impact commercial and federal organizations today. We provide insights from a survey of IT security and data science leaders navigating these challenges. We share predictions driven by data from HiddenLayer’s experiences securing AI in enterprise environments. Lastly, we reveal cutting-edge advancements in security controls for AI in all its forms.

As we navigate an AI-driven era, let this report serve as a resource to understand and implement security for AI. Whether you’re a developer, data scientist, or security professional, we invite you to join us in securing AI for a safer future.

We are incredibly excited to present to you the first-ever HiddenLayer AI Threat Landscape Report.

Tito
CEO & Co-Founder
(Unassisted by LLMs)

---

## Survey Insights at a Glance

It’s important to know that AI is not some invincible new technology, but rather, a technology extremely vulnerable to cyber threats just like many others that came before it. The motivations for attacking AI are what you would expect. They range from financial gain to manipulating public opinion to gaining competitive advantage. While industries are reaping the benefits of increased efficiency and innovation thanks to AI, there is still the concerning reality that expanding the use of AI causes a significant increase in security risks.

A survey of 150 IT security leaders commissioned by HiddenLayer confirms this concern. As the below results show, the industry is working hard to accelerate AI adoption – without having the proper security measures in place.

### Pervasive Use of AI

*   On average, companies have a staggering **1,689** AI models in production.
*   **98%** of IT leaders consider at least some of their AI models crucial to their business success.
*   **83%** state that AI usage is prevalent across all teams within their organizations.

### Challenges in Securing AI

*   **61%** of IT leaders acknowledge shadow AI (solutions that are not officially known or under the control of the IT department) as a problem within their organizations.
*   **89%** express concern about security vulnerabilities associated with integrating third-party AIs.
*   **75%** believe third-party AI integrations pose a greater risk than existing threats.

### Budgets and Priorities

*   **97%** of IT leaders prioritize securing AI.
*   **92%** are still developing a comprehensive plan for this emerging threat.
*   **94%** allocated budgets for AI security in 2024, but only **61%** are highly confident in their allocation.

### Sources of AI Breaches

According to IT leaders, the top sources of AI breaches include:
*   criminal hacking individuals or groups
*   third-party service providers
*   automated botnets
*   competitors

### Security Breaches Looming

*   **77%** of companies reported identifying breaches to their AI in the past year. The remaining were uncertain whether their AI models had seen an attack.

### Security Measures

Common measures to secure AI involve building relationships with AI and security teams, scanning and auditing AI models, and determining the origin source of AI models.

*   **30%** of IT leaders have deployed a manual defense for adversarial attacks on their existing AI, while just **14%** are planning and testing for such attacks.

### Collaboration and Concerns

*   **83%** of IT leaders collaborate with external cybersecurity firms to enhance AI security.
*   **58%** express doubts that the security protocols they’ve implemented can keep pace with evolving threats.

### Future Planning

*   **96%** of IT leaders expressed that their AI projects are critical or important to revenue generation over the next 18 months.
*   Only **30%** have deployed technology for model theftjacking, with **20%** planning and testing for this threat.

### Seeking Technological Solutions

*   **98%** of IT leaders are actively seeking technological solutions to enhance the security of AI and machine learning models.
*   **92%** of companies are building their own models to improve business operations.

---

## Adversarial AI Over Time

### Selected Offensive Milestones

*   **2002**: Adoption of ML-based spam detection filters using Naive Bayes algorithm
*   **2004**: First evasion techniques in linear spam filters by inserting “good” words
*   **2006**: First paper outlining taxonomy of attacks against ML
*   **2012**: First gradient-based poisoning attack against non-linear algorithms
*   **2014**: First demonstrated attack against deep neural networks
*   **2015**: OpenAI founded
*   **2016**: Crowd-sourced poisoning of Microsoft’s Tay chatbot
*   **2016**: Hugging Face launched as a chatbot service
*   **2017**: First demonstrated black-box attack against machine learning
*   **2018**: Introduction of Boundary Attack
*   **2018**: Full model extraction attacks: KnockOffNets, CopycatCNN
*   **2019**: Introduction of One Pixel and HopSkipJump attacks

### Selected Defensive Milestones

*   **2019**: Cylance endpoint bypass released - Cylance, I kill you
*   **2019**: Singapore's Model AI Governance Framework
*   **2020**: NIST IR Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigation
*   **2021**: Hugging Face introduces the concept of "model cards" and "datasets"
*   **2021**: First black-box neural payload injection technique
*   **2022**: MITRE ATLAS released
*   **2022**: EU AI Act
*   **2022**: First prompt injection attacks against LLMs disclosed
*   **2022**: Potential supply chain attack with ransomware embedded into AI model
*   **2022**: Canada’s Artificial Intelligence and Data Act (AIDA)
*   **2022**: Hugging Face has 50K models, 5K datasets, and 5K demos
*   **2022**: US Blueprint for an AI Bill of Rights
*   **2022**: Gartner TRISM
*   **2022**: OpenAI launches ChatGPT
*   **2022**: torchtriton - malicious PyTorch dependency found on PyPI
*   **2022**: First ITW hijacked models containing reverse-shells and stagers
*   **2023**: NIST AI Risk Management Framework (AI RMF)
*   **2023**: First open-source replicas of closed-source models (Alpaca, OpenLLaMA)
*   **2023**: Google Secure AI Framework (SAIF)
*   **2023**: PoisonGPT - a demonstration of LLM poisoning
*   **2023**: Hugging Face valued at $4.5 billion in latest round of funding
*   **2023**: Nightshade - a tool for poisoning text-to-image models
*   **2023**: US White House issues an executive order on the safe, secure, and trustworthy development and use of artificial intelligence
*   **2023**: Hugging Face has 520k models and 112k datasets.

---

# PART 1: RISKS RELATED TO THE USE OF AI

Like with any other life-changing technology, artificial intelligence is a double-edged sword. Although it’s already starting to have a massively positive impact on our lives and workflows, it also has tremendous potential to cause serious harm, especially if used carelessly or with overt malicious purposes.

There are plenty of ways in which adversaries - such as criminals, terrorists, cyber threat actors, foul-playing competitors, and repressive nation-states - can utilize AI to their advantage. There are also numerous obscure risks related to the legitimate use of this technology.

Generative AI is especially vulnerable to abuse. It can be:
*   manipulated to give biased, inaccurate, or harmful information
*   used to create harmful content, such as malware, phishing, and propaganda
*   used to develop deepfake images, audio and video
*   leveraged by any malicious activity to provide access to dangerous or illegal information

Privacy is also an issue when it comes to the information we share with AI-based tools. Data leakage can cause significant legal issues for businesses and institutions. In addition, because of code generation tools, vulnerabilities could be introduced into the software - intentionally, by poisoning the datasets, or unintentionally, by training the models on already vulnerable code. All this is on top of copyright violations and various ethical and societal concerns that leading industry experts have repeatedly voiced.

## Harmful Content Creation

The cybercrime business has skyrocketed. Everything from easily accessible dark web marketplaces to ready-to-use attack toolkits and Ransomware-as-a-Service leveraging practically untraceable cryptocurrencies, have helped cybercriminals thrive as law enforcement struggles to track them down. As if this wasn’t bad enough, generative AI enables instant and effortless access to a world of devious attack scenarios while providing elaborate phishing and malware for anyone who dares to ask for it. AI chatbots can also access illegal information that could result in physical threats.

Malicious users could, for example, evade the protective filters of a chatbot and trick it into providing recipes for making explosives.

OpenAI and Microsoft have recently unveiled the many ways in which state-affiliated threat actors tried to abuse their AI solutions to aid malicious campaigns. Adversaries with links to North Korea, Iran, Russia and China were found to use large language models for assistance with activities such as scripting, social engineering, vulnerability research, post-exploitation techniques, detection evasion, and military reconnaissance.

While the most widely used generative AI solutions strive to implement strong filters and content restrictions, most have been proven relatively easy to bypass. Moreover, open-source AI models can be fine-tuned to work without any restrictions whatsoever. Such models could be kept private to the adversaries or provided to the broader public on the dark web. The security community still needs to devise a workable solution to the complicated problem of accessing illegal/dangerous content via AI chatbots.

## Deepfakes

Another obvious concern is the creation of very authentic-looking deepfake images, audio, and video. These could be used to steal money, extract sensitive information, ruin personal reputations, and spread misinformation.

In one of the biggest deepfake scams to date, adversaries were able to defraud a multinational corporation of $25 million. The financial worker who approved the transfer had previously attended a video conference call with what seemed to be the company's CFO, as well as a number of other colleagues the employee recognized. These all turned out to be deepfake videos.

Scammers have for years been able to mislead people. Even the least sophisticated error-ridden messages and calls usually claim a number of victims. The emergence of deepfakes brings this problem to a completely new level, where even a seasoned cybersecurity expert will have hard time distinguishing truth from falsehood. It's not just money and reputation that is at stake here. Deepfakes can be used to disrupt political campaigns, rig democratic elections, manipulate societies, and stir unrest. Democracy and social order can greatly suffer if sufficient measures are not timely implemented.

## Data Privacy and Leakage

When a new, exciting technology that makes people’s lives easier comes to market, it’s hard not to dive in and reap the benefits immediately – especially if it’s free. But we should all be aware that although we’re not shelling out money, there is still a cost: our data.

Guidelines for protecting privacy always lag behind the adoption of new technologies. Too often, the implications of privacy breaches become clear only after the initial furor dies down. We saw this with social networks and are already seeing it happen with generative AI.

For example, the terms and conditions agreement for any AI-based service should state how the service provider uses our request prompts. However, these are often intentionally lengthy texts written in difficult language. If you don’t want to spend hours deciphering the fine print, it’s best to assume that every request made to the model is logged, stored, and processed in one way or another. At a minimum, expect that your inputs are fed into the training dataset and, therefore, could be accidentally leaked in outputs for other requests.

Moreover, many providers might feel tempted to profit on the side and sell the input data to research firms, advertisers, or any other interested third party.

In March 2023, Samsung experienced a serious leakage of intellectual property, where employees were found to be pasting portions of proprietary source code into ChatGPT. This resulted in a company-wide ban on the usage of AI chatbots.

## Copyright Violation

The rapid, large-scale incorporation of generative AI will likely spur a variety of legal issues. For now, the main concern is the unauthorized use of copyrighted materials in training datasets and models, which leads to producing plagiarized output.

The models behind generative AI solutions are typically trained on swaths of publicly available data, some of which are protected by copyright laws. The generated content is merely a mix of things published somewhere (text, pictures, video, or audio) and included in the training dataset. The problem is that generative AI can’t distinguish between inspiration and plagiarism. It often gives outputs too close to the creations it was trained on without crediting the original work’s authors. This can result in serious copyright violations.

There is also the question of consent. Currently, no laws prevent service providers from training their models on any kind of data as long as it’s legal and public. This is how a generative AI can write a poem or create an image in a specific author’s style. Understandably, most writers and artists do not appreciate their work being used in such a way.

Stability AI, which provides one of the most popular text-to-image generators called Stable Diffusion, is facing multiple lawsuits for wrongfully using copyright-protected images to train their models. One of these lawsuits, brought on by Getty Images, alleges that Stability AI utilized millions of copyrighted images and their metadata without obtaining permission from Getty or offering any compensation. Several artists also filed class-action suits against both Stability AI and its rival, Midjourney, pointing out that images generated in the style of a particular author directly compete with the author's own work.

## Accuracy and Bias Issues

The old saying states that AI models are only as good as their training dataset. But large generative AI models are trained on terabytes of data, in most cases indiscriminately scraped from the Internet, making careful vetting of the training set impossible. This causes problems concerning the accuracy, fairness, and general sanity of the model, as well as the possibility of data privacy breaches if the model is accidentally trained on sensitive data. Moreover, the rise of online learning, where user input is continuously fed into the training process, makes AI solutions prone to bias, misinformation, and intentional poisoning.

However, more often than not, the training process involves large amounts of historical information collected over the past decades. Such data tends to be very under-representative of marginalized groups. Because of this, resulting models will be inherently biased towards things they find more common in their training datasets. The built-in bias of AI can be easily seen in the case of text generation and image generation models. These models often follow gender, age, and skin color stereotypes that are deemed inappropriate and harmful in modern society. The damage can be very serious if a biased model is implemented in such settings as healthcare, finance, or human resources.

In 2019, the AI algorithm used in the U.S. healthcare system was found to be racially biased which resulted in black patients receiving lower risk scores and were less often identified for extra care.

Even if the dataset contains unbiased and accurate information, an AI algorithm does not always get it right and might sometimes arrive at bizarrely incorrect conclusions. These are called “hallucinations” and are an intrinsic attribute of current AI technology. By design, AI cannot distinguish between reality and fiction, so if the training dataset contains a mix of both, chances are the AI will at times respond with fiction.

Meta’s short-lived Galactica model was trained on millions of scientific articles, textbooks, and websites. Despite the training set likely being thoroughly vetted, the model was serving falsehoods and pseudo-scientific babble in a matter of hours, making up citations that never existed and inventing papers written by imaginary authors.

AI algorithms have no notion of fairness on their own, so they need to be trained on a well-balanced and fully representative dataset in order to avoid any kind of discrimination.

## Other Ethical & Societal Issues

Besides biased and inaccurate information, a generative AI model can also give advice that appears technically sane but can prove harmful in certain circumstances or when the context is missing or misunderstood. This is especially true in so-called “emotional AI” – machine learning applications designed to recognize human emotions. Such applications have been used for some time, mainly in market trend predictions, but are increasingly adopted in human resources and counseling.

Given the probabilistic nature of the AI models and the often lack of necessary context, this can be quite dangerous. Privacy watchdogs now warn against using “emotional AI” in any professional setting.

The ability of AI to almost perfectly mimic human behavior can prove very dangerous. Some people might be compelled to believe the AI bot's hallucinations or even conclude that it is sentient; others might feel intimidated or hurt by its emotionally charged responses. In some circumstances, people could be manipulated to give away sensitive data or act in a harmful way. This is just the tip of the iceberg.

It was recently revealed that a would-be assassin, who was arrested on his way to kill the British Queen with a crossbow in December 2021, was in fact encouraged to do so by an AI chatbot. Prior to the attack, the man created an artificial "girlfriend" on Replika, a platform that offers personalized and empathetic AI companions. He exchanged thousands of messages with the chatbot, many of them discussing the murderous plan. The bot responses were in support of the plan and bolstered the confidence of the attacker.

Used with malicious intent, AI chatbots can become very effective tools in misinformation and manipulation – especially if people are led to believe that they are interacting with fellow humans. Add voice and video synthesis to the mix, and we get something far more terrifying than Twitter bots and fake Facebook accounts. If highly personalized and trained on specially crafted datasets, such bots could steal the identities of real people.

With the rapid adaptation of generative AI, there is a substantial prospect that AI creations will dominate the web in a couple of years. At the moment, disclosing the use of AI in producing content is not a legal requirement, so we can expect that there are many more AI-generated texts on the web than it might seem on the surface. The speed at which chatbots can produce data, coupled with easy access for everyone in the world, means that we might soon become overwhelmed with dubious-quality AI-generated material. Moreover, suppose we keep training the models on online data. In that case, they will eventually be fed their own creations in an ever-lasting quality-degrading loop, turning the Dead Internet theory into reality.

---

# PART 2: RISKS FACED BY AI-BASED SYSTEMS

There’s a lot of conversation about the safe and ethical use of AI-powered tools; however, the security and safety of AI systems themselves are still often overlooked. It’s vital to remember that, like with any other ubiquitous technology, AI-based solutions can be abused by attackers, resulting in disruption, financial loss, reputational harm, or even risk to human health and life.

Three major types of attacks on AI:
*   **Adversarial Machine Learning Attacks** - attacks against AI algorithms, aimed to alter AI’s behavior, evade AI-based detection, or steal the underlying technology
*   **Generative AI System Attacks** - attacks against AI’s filters and restrictions, intended to generate content deemed harmful or illegal
*   **Supply Chain Attacks** - attacks against ML artifacts and platforms, with the intention of arbitrary code execution and delivery of traditional malware

## Adversarial Machine Learning Attacks

To help you understand adversarial machine learning attacks, let’s first go over some basic terminology.

*   **Artificial intelligence** is the general term comprising any system that mimics human intelligence.
*   **Machine Learning** is the technology that enables AI to learn and improve its predictions.
*   **Machine Learning Models** are the decision-making systems that lie at the core of most modern AI-based. It analyzes the input, such as a picture, a text prompt, or a binary file, and makes a prediction based on the information it has learned from in the past.
*   **Model Training** involves feeding vast amounts of relevant data into a machine learning algorithm to produce a trained model, which can then be deployed into production and made available for users to query through an interface or an API.

Adversarial attacks against machine learning usually aim to do three things:
*   Alter the model’s behavior, for example, to make it biased, inaccurate, or malicious
*   Bypass or evade the model, for example, to trigger incorrect classification or avoid detection
*   Replicate the model or data used to train it, stealing the intellectual property.

Let’s look at some of the most popular machine learning attacks today.

### Data Poisoning

Model training is one of the crucial phases in building an AI-based solution. During this stage, the model learns how to behave based on inputs from the training dataset. Any malicious interference in the learning process can significantly impact the reliability of the resulting model.

Data poisoning attacks aim to modify the model's behavior. The goal is to make the predictions biased, inaccurate, or otherwise manipulated to serve the attacker’s purpose. Attackers can perform data poisoning in two ways: by modifying entries in the existing dataset (for example, changing features or flipping labels) or injecting the dataset with a new, specially doctored portion of data.

![Diagram showing Data Poisoning attack flow](https://i.imgur.com/example-data-poisoning.png)

AI solutions that are most prone to this type of attack use continuous learning. This is where the model is constantly retrained on new user-supplied data. Because the users’ input is often not carefully validated and sanitized, an adversary can craft specific inputs to sway the model. A model is only as good as its training data, and predictions from a model trained on inaccurate data will always be biased or incorrect. One or few poisoned requests will hardly make a difference. Still, adversaries can try to manipulate the public to interact with the model in a specific way or use botnets to amplify the amount of poisoned input sent to the model.

Systems that often make use of online training or continuous-learning models and, therefore, are susceptible to data poisoning attacks include:
*   Chatbots and digital assistants
*   Text auto-complete tools
*   Trend prediction and recommendation systems
*   Spam filters and anti-malware solutions
*   Intrusion detection systems
*   Financial fraud prevention
*   Medical diagnostic tools

Many modern ML solutions opt for a distributed learning method called federated learning, where the training dataset is scattered amongst several independent devices. During federated learning, the ML model is downloaded and trained locally on each participating edge device. The updates are pushed to the central server or shared directly between the nodes. The local training dataset is private to the participating device and is never shared outside of it. Federated learning helps companies maximize the amount and diversity of the training data while preserving the data privacy of collaborating users. It’s not surprising, then, that this approach has become widely used in solutions ranging from everyday-use mobile phone applications to self-driving cars, manufacturing, and healthcare. However, delegating the model training process to an often random and unverified cohort of users amplifies the risk of training-time attacks and model hijacking.

Data poisoning attacks are relatively easy to perform even for uninitiated adversaries because creating “polluted” input can often be done intuitively without specialist knowledge. Such attacks happen daily, from manipulating text completion mechanisms to influencing product reviews to political disinformation campaigns.

#### Data Poisoning in the Wild

One of the first widely publicized examples of data poisoning concerned Microsoft's early chatbot called Tay. Continuously trained on user-provided input, Tay launched on Twitter in March 2016 - only to be shut down after a mere 16 hours of existence. In this short timeframe, users managed to sway the bot to become rude and racist and produce biased and harmful output. Although it was not a coordinated attack, Microsoft suffered some reputational damage just because of unintended trolling and was even threatened with legal action.

More sophisticated attempts at data poisoning could potentially have a devastating impact. Worse, pre-trained models are not immune to poisoning either, as they can be manipulated during fine-tuning. In an attack called PoisonGPT, researchers recently demonstrated that surgical modifications to an existing GPT-based model with the use of a technique called Rank-One Model Editing can make it spread attacker-controlled disinformation while performing just as well as the original model on all the other topics.

Another use case for data poisoning is code generation and automatic code suggestion tools that help developers write programming code. Poisoning the training dataset of underlying AI models can force these tools to suggest insecure, vulnerable, or malicious code. This was demonstrated in the TrojanPuzzle attack.

Text-to-image models can also be poisoned to render them useless. Nightshade is a tool intended for artists who don’t want their visual art to be used to train AI models but still wish to publish their work online. Nightshade allows users to add special invisible modifications to their images. If a certain amount of Nightshade-modified images is used in the training of a generative AI model, the model will cease to produce reliable outputs.

#### Data Poisoning in Academic Research

2023 marked a significant turning point in AI academic research, with a heightened focus on potential risks of poisoning attacks on large language models (LLMs) and diffusion models. These advanced models, which extract vast quantities of data from the internet, present a challenge for manual auditing due to their sheer scale and complexity. This makes them particularly susceptible to targeted poisoning efforts, where malicious data could be introduced into the training set to manipulate the models’ behavior.

Researchers have studied various strategies to detect and prevent such attacks:
*   **“Universal Jailbreak Backdoors from Poisoned Human Feedback”** - Rando and Tramèr discuss a new threat in RLHF-trained models, where attackers embed a universal backdoor trigger to provoke harmful responses. They showcase the challenges in creating robust defenses against such attacks.
*   **“Text-to-Image Diffusion Models can be Easily Backdoored through Multimodal Data Poisoning”** - Zhai et al. explore backdoor attacks on text-to-image diffusion models and propose the BadT2I framework for injecting backdoors at different semantic levels.
*   **“Poisoning Web-Scale Training Datasets is Practical”** - Carlini and colleagues introduce two new dataset poisoning attacks, highlighting the feasibility of purchasing expired domains linked to various datasets to re-host poisoned data.
*   **“Poisoning Language Models During Instruction Tuning”** - Wan, Wallace, Shen, and Klein demonstrate how adversaries can insert poison examples into user-submitted datasets, manipulating model predictions with trigger phrases.

### Model Evasion

Attacks performed against an AI model after it has been deployed in production, whether on the endpoint or in the cloud, are called inference attacks. In this context, the term inference describes a data mining technique that leaks sensitive information about the model or training dataset. Knowledge is inferred from the outputs the model produces for a specially prepared data set. The attackers don’t need privileged access to the model artifacts, training data, or training process. The ability to query the model and see its predictions is all that is needed to perform an inference attack. This can be done through the regular UI or API access that many AI-based systems provide to customers. By repetitively querying the model with specially crafted requests - each just a bit different from the previous one - and recording all the model’s predictions, attackers can comprehensively understand the model or the training dataset. This information can be used in, for example, model bypass attacks. It can also help reconstruct the model itself, effectively stealing it.

![Diagram showing Model Evasion attack flow](https://i.imgur.com/example-model-evasion.png)

Evasion attacks, also known as model bypasses, aim to intentionally manipulate model inputs to produce misclassifications. Maliciously crafted inputs to a model are referred to as adversarial examples. Their purpose is typically to evade correct classification or trigger specific attacker-defined outcome. They can also help an attacker learn the decision boundaries of a model.

To create an adversarial example, the attacker manipulates the input in such a way that the model classification of this input changes. The difference between the original and the manipulated input often remains imperceptible to humans. For instance, in a visual recognition system, the attacker could modify an image by adding a layer of noise invisible to the human eye - or even rotating the image, or changing a single pixel. This would cause the AI model to give the wrong prediction. Attackers usually send large amounts of slightly different inputs to the model and record the predictions until a sample that triggers the desired misclassification is found.

This evasion technique can also apply to any other model types used for classification. It’s been used in the wild for some time, mostly by cybercriminals trying to bypass security solutions. The earliest application was against ML-based spam filters designed to predict which emails are junk based on the occurrences of specific words in them. Spammers quickly found their way around these filters by adding words associated with legitimate correspondence to their messages. Similar techniques bypass malware detection engines, intrusion detection systems, fraud detection, biometric authentication, and visual recognition.

#### Model Evasion in the Wild

One of the first notable instances of an AI evasion attack was demonstrated in 2019 by Skylight Cyber researchers who targeted a leading anti-malware solution. The researchers had created a universal bypass against the AI-based endpoint malware classification model. The attack used inference to determine a subset of strings that, when embedded in malware, would trick the AI model into classifying malicious software as benign. This attack spawned several anti-virus bypass toolkits such as MalwareGym and MalwareRL, where evasion attacks have been combined with reinforcement learning to automatically generate mutations in malware that make it appear benign to malware classification models.

Security vendors that provide AI-based technology (be it antivirus, spam filter, IDS, or authentication/authorization systems) have long faced evasion attacks from cyber criminals trying to bypass detection. The same is true for financial institutions and their fraud prevention mechanisms.

These attacks could also be used to hijack self-driving cars, as they have shown in the past. Researchers demonstrated that putting a specially crafted (but innocent-looking) sticker on a STOP sign can fool on-board models to misclassify the sign and keep driving. Similarly, attackers wanting to bypass a facial recognition system might design a special pair of sunglasses that will make the wearer invisible to the system. An adversarial state could try to evade satellite imagery object detection systems used by the military to recognize planes, vehicles, and military structures. The Russian Air Force already used a crude bypass of this sort by painting fake bomber shapes on the tarmac to fool satellite photo recognition systems into thinking these are real planes. The possibilities are endless, and some can have potentially lethal consequences.

2023 saw several papers on attacking LLMs:
*   **“Universal and Transferable Adversarial Attacks on Aligned Language Models”** - Zou et al. introduce an approach to generate adversarial suffixes that cause aligned LLMs to produce objectionable content.
*   **“Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense”** - Krishna and colleagues demonstrate that paraphrasing AI-generated text can evade detection algorithms but propose a retrieval-based defense mechanism.
*   **“Are aligned neural networks adversarially aligned?”** - Carlini et al. explore the vulnerability of aligned LLMs to adversarial examples and the potential for multimodal models to be attacked via image perturbations.

#### Model Evasion in Academic Research

Despite continuous advancements in AI and machine learning, preventing adversarial attacks remains elusive. The same vulnerabilities that compromise the integrity of image recognition systems are also found in large language models (LLMs), making them susceptible to similar adversarial manipulations. However, recent research has shown promising developments in defending image recognition models using diffusion models trained on giant datasets. These advancements suggest a potential pathway