# UNDERSTANDING THE EVOLVING CYBERSECURITY ENVIRONMENT
2024 LANDSCAPE REPORT

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
    - [Other Ethical & Societal Issues](#other-ethical-societal-issues)
- [Part 2: Risks Faced by AI-based Systems](#part-2-risks-faced-by-ai-based-systems)
    - [Adversarial Machine Learning Atacks](#adversarial-machine-learning-atacks)
    - [Atacks Speciﬁc to Generative AI](#atacks-speciﬁc-to-generative-ai)
    - [Supply Chain Atacks](#supply-chain-atacks)
    - [Threat Actors and Atack Vectors](#threat-actors-and-atack-vectors)
- [Part 3: Advancements in Security for AI](#part-3-advancements-in-security-for-ai)
    - [Ofensive Security Tooling for AI](#ofensive-security-tooling-for-ai)
    - [Defensive Frameworks for AI](#defensive-frameworks-for-ai)
    - [Red Teaming and Risk Assessment](#red-teaming-and-risk-assessment)
    - [Policies and Regulations](#policies-and-regulations)
- [Part 4: Predictions and Recommendations](#part-4-predictions-and-recommendations)
- [Resources](#resources)
- [About HiddenLayer](#about-hiddenlayer)

# FOREWORD
Humanity has entered an unprecedented technological evolution. No mission, organization, job, or person 
on the planet will go unimpacted by artiﬁcial intelligence this year. Revolutionizing every data-driven 
opportunity, AI has the potential to bring on a new era of prosperity, allowing the quality of life to reach 
unimaginable heights. Like any new groundbreaking technology, the potential for greatness is paralleled 
only by the inherent risk. It is critical that we do not allow ourselves to tunnel solely on harvesting the 
beneﬁts of AI without responsibly mitigating those risks. Make no mistake, for all the distrust of the black 
box nature of AI and the doom and gloom rhetoric of world domination, the greatest risk associated with 
AI for the foreseeable future is bad people.  

Artiﬁcial intelligence is, by a wide margin, the most vulnerable technology ever to be deployed in 
production systems. It’s vulnerable at a code level, during training and development, post-deployment, 
over networks, via generative outputs, and more. We do not need to look far into the traditional cyber 
threat landscape to understand today’s adversarial AI atacks and predict their near-term paterns. 
In this report, we shed light on these vulnerabilities and how they impact commercial and federal 
organizations today. We provide insights from a survey of IT security and data science leaders navigating 
these challenges. We share predictions driven by data from HiddenLayer’s experiences securing AI in 
enterprise environments. Lastly, we reveal cuting-edge advancements in security controls for AI in all its 
forms. 
As we navigate an AI-driven era, let this report serve as a resource to understand and implement security 
for AI. Whether you’re a developer, data scientist, or security professional, we invite you to join us in 
securing AI for a safer future.
We are incredibly excited to present to you the ﬁrst-ever HiddenLayer AI Threat Landscape Report.
Tito
CEO & Co-Founder
(Unassisted by LLMs)
AI THREAT LANDSCAPE 2024

# SURVEY INSIGHTS AT A GLANCE
A survey of 150 IT security leaders commissioned by HiddenLayer conﬁrms this concern. As the below results show, the 
industry is working hard to accelerate AI adoption – without having the proper security measures in place.
Pervasive Use of AI
It’s important to know that AI is not some invincible new 
technology, but rather, a technology extremely vulnerable to 
cyber threats just like many others that came before it. The 
motivations for atacking AI are what you would expect. They 
range from ﬁnancial gain to manipulating public opinion to 
gaining competitive advantage. While industries are reaping 
the beneﬁts of increased efciency and innovation thanks to 
AI, there is still the concerning reality that expanding the use 
of AI causes a signiﬁcant increase in security risks. 

![Image of a graphic showing that companies have an average of 1,689 AI models in production, 98% of IT leaders consider at least some of their AI models crucial to their business success, and 83% state that AI usage is prevalent across all teams within their organizations.]

SECURITY FOR AI

Budgets and Priorities
![Image of a graphic showing that 97% of IT leaders prioritize securing AI, 92% are still developing a comprehensive plan for this emerging threat, and that the top sources of AI breaches include criminal hacking individuals or groups, third-party service providers, automated botnets, and competitors.]

SECURITY FOR AI - SURVEY INSIGHTS AT A GLANCE

Challenges in Securing AI
![Image of a graphic showing that 89% express concern about security vulnerabilities associated with integrating third-party AIs, 61% of IT leaders acknowledge shadow AI as a problem, 75% believe third-party AI integrations pose a greater risk than existing threats, 94% allocated budgets for AI security in 2024, but only 61% are highly conﬁdent in their allocation.]

Security Breaches Looming
![Image of a graphic showing that 77% of companies reported identifying breaches to their AI in the past year, and the remaining were uncertain whether their AI models had seen an atack.]

SECURITY FOR AI - SURVEY INSIGHTS AT A GLANCE

Security Measures
![Image of a graphic showing that common measures to secure AI involve scanning and auditing AI models, building relationships with AI and security teams, and determining the origin source of AI models.]

Collaboration and Concerns
![Image of a graphic showing that 83% of IT leaders collaborate with external cybersecurity ﬁrms to enhance AI security, and 58% express doubts that the security protocols they’ve implemented can keep pace with evolving threats.]

Seeking Technological Solutions
![Image of a graphic showing that 98% of IT leaders are actively seeking technological solutions to enhance the security of AI and machine learning models, 92% of companies are building their own models to improve business operations, 30% of IT leaders have deployed a manual defense for adversarial atacks on their existing AI, while just 14% are planning and testing for such atacks, and only 30% have deployed technology for model thefjacking, with 20% planning and testing for this threat.]

Future Planning
![Image of a graphic showing that 96% of IT leaders expressed that their AI projects are critical or important to revenue generation over the next 18 months.]

# ADVERSARIAL AI OVER TIME
![Image of a timeline showing Selected Ofensive Milestones and Selected Defensive Milestones from 2002 to 2023.]

Selected Ofensive Milestones
+
+
Selected Defensive Milestones
AI Milestones
2002
Adoption of ML-based spam detection ﬁlters using Naive Bayes algorithm
2004
First evasion techniques in linear spam ﬁlters by inserting “good” words
2006
First paper outlining taxonomy of atacks against ML 
2012
First gradient-based poisoning atack against non-linear algorithms
2014
First demonstrated atack against deep neural networks
2016
Crowd-sourced poisoning of Microsof’s Tay chatbot 
2017
First demonstrated black-box atack against machine learning 
2018
Introduction of Boundary Atack
2015
OpenAI founded
2016
Hugging Face launched as a chatbot service
2018
Full model extraction atacks: KnockOfNets,
2019
Introduction of One Pixel and                               atacks
ADVERSARIAL
AI OVER TIME
CopycatCNN
HopSkipJump
2019
Cylance endpoint bypass released - Cylance, I kill you
2019
Singapore's Model AI Governance Framework
2021
First black-box neural payload injection technique
2019
NIST IR Adversarial Machine Learning: 
A Taxonomy and  Terminology of Atacks and Mitigation
2020
Hugging Face introduces the concept of "model cards" and "datasets"
2021
MITRE ATLAS released
2022
EU AI Act
2022
First prompt injection atacks against LLMs disclosed
2022
Potential supply chain atack with ransomware embedded into AI model
2022
Canada’s Artiﬁcial Intelligence and Data Act (AIDA)
2022
US Blueprint for an AI Bill of Rights
2022
OpenAI launches ChatGPT
2022
torchtriton - malicious PyTorch dependency found on PyPI
2022 
First ITW hijacked models containing reverse-shells and stagers   
2023
NIST AI Risk Management Framework (AI RMF)
2022
Hugging Face has 50K models, 5K datasets, and 5K demos
2022
Gartner TRISM
2023
First open-source replicas of closed-source models (Alpaca, OpenLLaMA)
2023
Google  Secure AI Framework (SAIF) 
2023
PoisonGPT - a demonstration of LLM poisoning
2023
Hugging Face valued at $4.5 billion in latest round of funding
2023
Nightshade - a tool for poisoning text-to-image models
2023
US White House issues an executive order on the safe, secure, and 
trustworthy development and use of artiﬁcial intelligence
2023
Hugging Face has 520k models and 112k datasets.
ADVERSARIAL AI OVER TIME

# PART 1: RISKS RELATED TO THE USE OF AI
Like with any other life-changing technology, artiﬁcial 
intelligence is a double-edged sword. Although it’s 
already starting to have a massively positive impact 
on our lives and workﬂows, it also has tremendous 
potential to cause serious harm, especially if used 
carelessly or with overt malicious purposes.
There are plenty of ways in which adversaries - such as criminals, terrorists, cyber threat actors, foul-playing competitors, 
and repressive nation-states - can utilize AI to their advantage. There are also numerous obscure risks related to the 
legitimate use of this technology.
Privacy is also an issue when it comes to the information 
we share with AI-based tools. Data leakage can cause 
signiﬁcant legal issues for businesses and institutions. 
In addition, because of code generation tools, 
vulnerabilities could be introduced into the 
sofware - intentionally, by poisoning the datasets, or 
unintentionally, by training the models on already 
vulnerable code. All this is on top of copyright violations 
and various ethical and societal concerns that leading 
industry experts have repeatedly voiced.
Generative AI is especially vulnerable to abuse.
It can be:
- manipulated to give biased, inaccurate, or 
harmful information 
- used to create harmful content, such as 
malware, phishing, and propaganda
- used to develop deepfake images, audio 
and video
- leveraged by any malicious activity to provide
access to dangerous or illegal information

## Harmful Content Creation
While the most widely used generative AI solutions strive 
to implement strong ﬁlters and content restrictions, most 
have been proven relatively easy to bypass. Moreover, 
open-source AI models can be ﬁne-tuned to work without 
any restrictions whatsoever. Such models could be kept 
private to the adversaries or provided to the broader
public on the dark web. The security community still needs 
to devise a workable solution to the complicated problem 
of accessing illegal/dangerous content via AI chatbots.
Another obvious concern is the creation of very authen-
tic-looking deepfake images, audio, and video. These could 
be used to steal money, extract sensitive information, ruin 
personal reputations, and spread misinformation. 
The cybercrime business has skyrocketed. Everything 
from easily accessible dark web marketplaces to 
ready-to-use atack toolkits and Ransomware-as-a-Ser-
vice leveraging practically untraceable cryptocurrencies, 
have helped cybercriminals thrive as law enforcement 
struggles to track them down.  As if this wasn’t bad 
enough, generative AI enables instant and efortless 
access to a world of devious atack scenarios while 
providing elaborate phishing and malware for anyone 
who dares to ask for it. AI chatbots can also access illegal 
information that could result in physical threats
Malicious users could, for example, evade the protective 
ﬁlters of a chatbot and trick it into providing recipes for 
making explosives. 

## Deepfakes
OpenAI and Microsof have recently unveiled the 
many ways in which state-afliated threat actors 
tried to abuse their AI solutions to aid malicious 
campaigns. Adversaries with links to North Korea, 
Iran, Russia and China were found to use large 
language models for assistance with activities 
such as scripting, social engineering, vulnerability 
research, post-exploitation techniques, detection 
evasion, and military reconnaissance.
In one of the biggest deepfake scams to date, 
adversaries were able to defraud a multinational 
corporation of $25 million. The ﬁnancial worker 
who approved the transfer had previously atend-
ed a video conference call with what seemed to be 
the company's CFO, as well as a number of other 
colleagues the employee recognized. These all 
turned out to be deepfake videos.
Scammers have for years been able to mislead people. 
Even the least sophisticated error-ridden messages and 
calls usually claim a number of victims. The emergence of 
deepfakes brings this problem to a completely new level, 
where even a seasoned cybersecurity expert will have 
hard time distinguishing truth from falsehood. It's not just 
money and reputation that is at stake here. Deepfakes can 
be used to disrupt political campaigns, rig democratic 
elections, manipulate societies, and stir unrest. Democra-
cy and social order can greatly sufer if sufcient 
measures are not timely implemented.

## Data Privacy and Leakage
When a new, exciting technology that makes people’s 
lives easier comes to market, it’s hard not to dive in and 
reap the beneﬁts immediately – especially if it’s free. 
But we should all be aware that although we’re not 
shelling out money, there is still a cost: our data.
 
Guidelines for protecting privacy always lag behind the 
adoption of new technologies. Too ofen, the implications 
of privacy breaches become clear only afer the initial 
furor dies down. We saw this with social networks and are 
already seeing it happen with generative AI.
For example, the terms and conditions agreement for any 
AI-based service should state how the service provider 
uses our request prompts. However, these are ofen 
intentionally lengthy texts writen in difcult language. If 
you don’t want to spend hours deciphering the ﬁne print, 
it’s best to assume that every request made to the model 
is logged, stored, and processed in one way or another. At 
a minimum, expect that your inputs are fed into the 
training dataset and, therefore, could be accidentally 
leaked in outputs for other requests.
Moreover, many providers might feel tempted to proﬁt 
on the side and sell the input data to research ﬁrms, 
advertisers, or any other interested third party.

## Copyright Violation
The rapid, large-scale incorporation of generative AI will 
likely spur a variety of legal issues. For now, the main 
concern is the unauthorized use of copyrighted materials 
in training datasets and models, which leads to producing 
plagiarized output.
The models behind generative AI solutions are typically 
trained on swaths of publicly available data, some of 
which are protected by copyright laws. The generated 
content is merely a mix of things published somewhere 
(text, pictures, video, or audio) and included in the 
training dataset. The problem is that generative AI can’t 
distinguish between inspiration and plagiarism. It ofen 
gives outputs too close to the creations it was trained 
on without crediting the original work’s authors. 
This can result in serious copyright violations.
There is also the question of consent. Currently, no laws 
prevent service providers from training their models on 
any kind of data as long as it’s legal and public. This is 
how a generative AI can write a poem or create an image 
in a speciﬁc author’s style. Understandably, most writers 
and artists do not appreciate their work being used in 
such a way.

PART 1: RISKS RELATED TO THE USE OF AI
In March 2023, Samsung experienced a serious 
leakage of intellectual property, where employees 
were found to be pasting portions of proprietary 
source code into ChatGPT. This resulted in a 
company-wide ban on the usage of AI chatbots.

## Accuracy and Bias Issues
The old saying states that AI models are only as good as 
their training dataset. But large generative AI models are 
trained on terabytes of data, in most cases indiscriminate-
ly scraped from the Internet, making careful veting of the 
training set impossible. This causes problems concerning 
the accuracy, fairness, and general sanity of the model, as 
well as the possibility of data privacy breaches if the 
model is accidentally trained on sensitive data. Moreover, 
the rise of online learning, where user input is continuous-
ly fed into the training process, makes AI solutions prone 
to bias, misinformation, and intentional poisoning. 
AI algorithms have no notion of fairness on their own, 
so they need to be trained on a well-balanced and fully 
representative dataset in order to avoid any kind of 
discrimination.
However, more ofen than not, the training process 
involves large amounts of historical information collected 
over the past decades. Such data tends to be very 
under-representative of marginalized groups. Because of 
this, resulting models will be inherently biased towards 
things they ﬁnd more common in their training datasets.
The built-in bias of AI can be easily seen in the case of text 
generation and image generation models. These models 
ofen follow gender, age, and skin color stereotypes that 
are deemed inappropriate and harmful in modern society. 
The damage can be very serious if a biased model is 
implemented in such setings as healthcare, ﬁnance, or 
human resources.
Even if the dataset contains unbiased and accurate infor-
mation, an AI algorithm does not always get it right and 
might sometimes arrive at bizarrely incorrect conclusions. 

PART 1: RISKS RELATED TO THE USE OF AI
Stability AI, which provides one of the most 
popular text-to-image generators called Stable 
Difusion, is facing multiple lawsuits for wrongfully 
using copyright-protected images to train their 
models. One of these lawsuits, brought on by 
Gety Images, alleges that Stability AI utilized 
millions of copyrighted images and their metadata 
without obtaining permission from Gety or 
ofering any compensation. Several artists also 
ﬁled class-action suits against both Stability AI 
and its rival, Midjourney, pointing out that images 
generated in the style of a particular author 
directly compete with the author's own work.
In 2019, the AI algorithm used in the U.S. 
healthcare system was found to be racially biased 
which resulted in black patients receiving lower 
risk scores and were less ofen identiﬁed 
for extra care.
Meta’s short-lived Galactica model was trained 
on millions of scientiﬁc articles, textbooks, and 
websites. Despite the training set likely being 
thoroughly veted, the model was serving 
falsehoods and pseudo-scientiﬁc babble in a 
mater of hours, making up citations that never 
existed and inventing papers writen by 
imaginary authors.

These are called “hallucinations” and are an intrinsic 
atribute of current AI technology. By design, AI cannot 
distinguish between reality and ﬁction, so if the training 
dataset contains a mix of both, chances are the AI will at 
times respond with ﬁction.
Besides biased and inaccurate information, a generative AI 
model can also give advice that appears technically sane 
but can prove harmful in certain circumstances or when 
the context is missing or misunderstood. This is especially 
true in so-called “emotional AI” – machine learning applica-
tions designed to recognize human emotions. Such 
applications have been used for some time, mainly in 
market trend predictions, but are increasingly adopted in 
human resources and counseling.
Given the probabilistic nature of the AI models and 
the ofen lack of necessary context, this can be quite 
dangerous. Privacy watchdogs now warn against using 
“emotional AI” in any professional seting.

## Other Ethical & Societal Issues
The ability of AI to almost perfectly mimic human behavior 
can prove very dangerous. Some people might be com-
pelled to believe the AI bot's hallucinations or even 
conclude that it is sentient; others might feel intimidated 
or hurt by its emotionally charged responses. In some 
circumstances, people could be manipulated to give away 
sensitive data or act in a harmful way. This is just the tip 
of the iceberg.
 
Used with malicious intent, AI chatbots can become 
very efective tools in misinformation and manipulation – 
especially if people are led to believe that they are 
interacting with fellow humans. Add voice and video 
synthesis to the mix, and we get something far more 
terrifying than Twiter bots and fake Facebook accounts. 
If highly personalized and trained on specially crafed 
datasets, such bots could steal the identities of real people.
With the rapid adaptation of generative AI, there is a 
substantial prospect that AI creations will dominate the 
web in a couple of years. At the moment, disclosing the use 
of AI in producing content is not a legal requirement, so we 
can expect that there are many more AI-generated texts on 
the web than it might seem on the surface. The speed at 
which chatbots can produce data, coupled with easy 
access for everyone in the world, means that we might 
soon become overwhelmed with dubious-quality AI-gener-
ated material. Moreover, suppose we keep training the 
models on online data. In that case, they will eventually be 
fed their own creations in an ever-lasting quality-degrading 
loop, turning the Dead Internet theory into reality.

PART 1: RISKS RELATED TO THE USE OF AI
It was recently revealed that a would-be assassin, 
who was arrested on his way to kill the British 
Queen with a crossbow in December 2021, was in 
fact encouraged to do so by an AI chatbot.
Prior to the atack, the man created an artiﬁcial 
"girlfriend" on Replika, a platform that ofers 
personalized and empathetic AI companions. He 
exchanged thousands of messages with the 
chatbot, many of them discussing the murderous 
plan. The bot responses were in support of the 
plan and bolstered the conﬁdence of the atacker.

# PART 2: RISKS FACED BY AI-BASED SYSTEMS
There’s a lot of conversation about the safe and 
ethical use of AI-powered tools; however, the security 
and safety of AI systems themselves are still ofen 
overlooked. It’s vital to remember that, like with any 
other ubiquitous technology, AI-based solutions can 
be abused by atackers, resulting in disruption, 
ﬁnancial loss, reputational harm, or even risk to 
human health and life.

## Adversarial Machine Learning Atacks
Three major types of atacks on AI:
Artiﬁcial intelligence is the general term comprising 
any system that mimics human intelligence.
To help you understand adversarial machine learning 
atacks, let’s ﬁrst go over some basic terminology. 
Machine Learning is the technology that enables AI 
to learn and improve its predictions. 
Machine Learning Models are the decision-making 
systems that lie at the core of most modern AI-based. It 
analyzes the input, such as a picture, a text prompt, or a 
binary ﬁle, and makes a prediction based on the 
information it has learned from in the past.
Model Training involves feeding vast amounts of 
relevant data into a machine learning algorithm to 
produce a trained model, which can then be deployed 
into production and made available for users to query 
through an interface or an API.
- Generative AI System Atacks - atacks 
against AI’s ﬁlters and restrictions, intended to 
generate content deemed harmful or illegal
- Supply Chain Atacks - atacks against ML 
artifacts and platforms, with the intention of 
arbitrary code execution and delivery of 
traditional malware
- Adversarial Machine Learning Atacks - 
atacks against AI algorithms, aimed to alter 
AI’s behavior, evade AI-based detection, or 
steal the underlying technology

Adversarial atacks against machine learning usually aim to do three things: 
Let’s look at some of the most popular machine learning atacks today.
- Alter the model’s behavior, for example, to make it biased, inaccurate, or malicious
- Bypass or evade the model, for example, to trigger incorrect classiﬁcation or avoid detection
- Replicate the model or data used to train it, stealing the intellectual property.

### Data Poisoning
Model training is one of the crucial phases in building an 
AI-based solution. During this stage, the model learns how 
to behave based on inputs from the training dataset. 
Any malicious interference in the learning process can 
signiﬁcantly impact the reliability of the resulting model.
AI solutions that are most prone to this type of atack use 
continuous learning. This is where the model is constantly 
retrained on new user-supplied data. Because the users’ 
input is ofen not carefully validated and sanitized, an 
adversary can craf speciﬁc inputs to sway the model. 
A model is only as good as its training
data, and predictions from a model trained on inaccurate 
data will always be biased or incorrect. One or few poisoned 
requests will hardly make a diference. Still, adversaries can 
try to manipulate the public to interact with the model in a 
speciﬁc way or use botnets to amplify the amount of 
poisoned input sent to the model.
Data poisoning atacks aim to modify the model's behavior. 
The goal is to make the predictions biased, inaccurate, or 
otherwise manipulated to serve the atacker’s purpose. 
Atackers can perform data poisoning in two ways: by 
modifying entries in the existing dataset (for example, 
changing features or ﬂipping labels) or injecting the 
dataset with a new, specially doctored portion of data.

Atacks Against AI - Data Poisoning
![Image of a diagram showing the data poisoning process.]
Training
Data
Training
Process
Trained
Model
Decision
Process
Input
Prediction

PART 2: RISKS FACED BY AI-BASED SYSTEMS
One of the ﬁrst widely publicized examples of data 
poisoning concerned Microsof's early chatbot called Tay. 
Continuously trained on user-provided input, Tay launched 
on Twiter in March 2016 - only to be shut down afer a mere 
16 hours of existence. In this short timeframe, users 
managed to sway the bot to become rude and racist and 
produce biased and harmful output. Although it was not a 
coordinated atack, Microsof sufered some reputational 
damage just because of unintended trolling and was even 
threatened with legal action.
More sophisticated atempts at data poisoning could 
potentially have a devastating impact. Worse, pre-trained 
models are not immune to poisoning either, as they can be 
manipulated during ﬁne-tuning. In an atack called 
PoisonGPT, researchers recently demonstrated that 
surgical modiﬁcations to an existing GPT-based model with 
the use of a technique called Rank-One Model Editing can 
make it spread atacker-controlled disinformation while 
performing just as well as the original model on all the other 
topics.
Another use case for data poisoning is code generation and 
automatic code suggestion tools that help developers write 
programming code. Poisoning the training dataset of 
underlying AI models can force these tools to suggest 
insecure, vulnerable, or malicious code. This was 
demonstrated in the TrojanPuzzle atack.
Text-to-image models can also be poisoned to render them 
useless. Nightshade is a tool intended for artists who don’t 
want their visual art to be used to train AI models but still 
wish to publish their work online. Nightshade allows users 
to add special invisible modiﬁcations to their images. If a 
certain amount of Nightshade-modiﬁed images is used in 
the training of a generative AI model, the model will cease 
to produce reliable outputs.
Many modern ML solutions opt for a distributed learning 
method called federated learning, where the training 
dataset is scatered amongst several independent devices. 
During federated learning, the ML model is downloaded and 
trained locally on each participating edge device. The 
updates are pushed to the central server or shared directly 
between the nodes. The local training dataset is private to 
the participating device and is never shared outside of it.
Federated learning helps companies maximize the amount 
and diversity of the training data while preserving the data 
privacy of collaborating users. It’s not surprising, then, that 
this approach has become widely used in solutions ranging 
from everyday-use mobile phone applications to self-driving 
cars, manufacturing, and healthcare. However, delegating 
the model training process to an ofen random and 
unveriﬁed cohort of users ampliﬁes the risk of training-time 
atacks and model hijacking.
Data poisoning atacks are relatively easy to perform even 
for uninitiated adversaries because creating “polluted” 
input can ofen be done intuitively without specialist 
knowledge. Such atacks happen daily, from manipulating
text completion mechanisms to inﬂuencing product 
reviews to political disinformation campaigns.

PART 2: RISKS FACED BY AI-BASED SYSTEMS
Systems that ofen make use of online training or 
continuous-learning models and, therefore, are susceptible 
to data poisoning atacks include:
- Chatbots and digital assistants
- Text auto-complete tools
- Trend prediction and recommendation systems
- Spam ﬁlters and anti-malware solutions
- Intrusion detection systems
- Financial fraud prevention
- Medical diagnostic tools

### Data Poisoning in the Wild
Atacks performed against an AI model afer it has been 
deployed in production, whether on the endpoint or in the 
cloud, are called inference atacks. In this context, the term 
inference describes a data mining technique that leaks 
sensitive information about the model or training dataset. 
Knowledge is inferred from the outputs the model produces 
for a specially prepared data set. The atackers don’t need 
privileged access to the model artifacts, training data, or 
training process. The ability to query the model and see its 
predictions is all that is needed to perform an inference 
atack. This can be done through the regular UI or API 
access that many AI-based systems provide to customers. 
By repetitively querying the model with specially crafed 
requests - each just a bit diferent from the previous one - 
and recording all the model’s predictions, atackers can 
comprehensively understand the model or the training 
dataset. This information can be used in, for example, 
model bypass atacks. It can also help reconstruct the 
model itself, efectively stealing it.

2023 marked a signiﬁcant turning point in AI academic 
research, with a heightened focus on potential risks of 
poisoning atacks on large language models (LLMs) and 
difusion models. These advanced models, which extract 
vast quantities of data from the internet, present a 
challenge for manual auditing due to their sheer scale and 
complexity. This makes them particularly susceptible to 
targeted poisoning eforts, where malicious data could be 
introduced into the training set to manipulate the models’ 
behavior. 

### Data Poisoning in Academic Research
Researchers have studied various strategies to 
detect and prevent such atacks:
- “Text-to-Image Difusion Models can be 
Easily Backdoored through Multimodal Data 
Poisoning” - Zhai et al. explore backdoor 
atacks on text-to-image difusion models and 
propose the BadT2I framework for injecting 
backdoors at diferent semantic levels. 
- “Poisoning Web-Scale Training Datasets is 
Practical” - Carlini and colleagues introduce 
two new dataset poisoning atacks, highlight-
ing the feasibility of purchasing expired 
domains linked to various datasets to re-host 
poisoned data. 
- “Poisoning Language Models During Instruc-
tion Tuning” - Wan, Wallace, Shen, and Klein 
demonstrate how adversaries can insert 
poison examples into user-submited data-
sets, manipulating model predictions with 
trigger phrases. 

PART 2: RISKS FACED BY AI-BASED SYSTEMS
- “Universal Jailbreak Backdoors from 
Poisoned Human Feedback” - Rando and 
Tramèr discuss a new threat in RLHF-trained 
models, where atackers embed a universal 
backdoor trigger to provoke harmful respons-
es. They showcase the challenges in creating 
robust defenses against such atacks.

### Model Evasion
One of the ﬁrst notable instances of an AI evasion atack 
was demonstrated in 2019 by Skylight Cyber researchers 
who targeted a leading anti-malware solution. The 
researchers had created a universal bypass against the 
AI-based endpoint malware classiﬁcation model. The atack 
used inference to determine a subset of strings that, when 
embedded in malware, would trick the AI model into 
classifying malicious sofware as benign. This atack 
spawned several anti-virus bypass toolkits such as 
MalwareGym and MalwareRL, where evasion atacks have 
been combined with reinforcement learning to 
automatically generate mutations in malware that make it 
appear benign to malware classiﬁcation models.
Evasion atacks, also known as model bypasses, aim to 
intentionally manipulate model inputs to produce 
misclassiﬁcations. 
Maliciously crafed inputs to a model are referred to as 
adversarial examples. Their purpose is typically to evade 
correct classiﬁcation or trigger speciﬁc atacker-deﬁned 
outcome. They can also help an atacker learn the decision 
boundaries of a model. 
To create an adversarial example, the atacker manipulates 
the input in such a way that the model classiﬁcation of this 
input changes. The diference between the original and the 
manipulated input ofen remains imperceptible to humans. 
For instance, in a visual recognition system, the atacker 
could modify an image by adding a layer of noise invisible to 
the human eye - or even rotating the image, or changing a 
single pixel.This would cause the AI model to