UNDERSTANDING THE EVOLVING
CYBERSECURITY ENVIRONMENT
2024
LANDSCAPE
REPORT
AI THREAT
1
Foreword
Survey Insights at a Glance
Adversarial AI Over Time
Part 1: Risks Related to the Use of AI
Harmful Content Creation
Deepfakes
Data Privacy and Leakage
Copyright Violation
Accuracy and Bias Issues
Other Ethical \& Societal Issues
Part 2: Risks Faced by AI\-based Systems 
Adversarial Machine Learning Atacks
Atacks Specic to Generative AI
Supply Chain Atacks
Threat Actors and Atack Vectors
Part 3: Advancements in Security for AI
Ofensive Security Tooling for AI
Defensive Frameworks for AI
Red Teaming and Risk Assessment
Policies and Regulations
Part 4: Predictions and Recommendations
Resources
About HiddenLayer
02
03
06
08
09
09
10
10
11
12
13
13
20
22
26
28
28
30
34
35
36
40
43
TABLE OF CONTENTS
2
FOREWORD
Humanity has entered an unprecedented technological evolution. No mission, organization, job, or person 
on the planet will go unimpacted by articial intelligence this year. Revolutionizing every data\-driven 
opportunity, AI has the potential to bring on a new era of prosperity, allowing the quality of life to reach 
unimaginable heights. Like any new groundbreaking technology, the potential for greatness is paralleled 
only by the inherent risk. It is critical that we do not allow ourselves to tunnel solely on harvesting the 
benets of AI without responsibly mitigating those risks. Make no mistake, for all the distrust of the black 
box nature of AI and the doom and gloom rhetoric of world domination, the greatest risk associated with 
AI for the foreseeable future is bad people.
Articial intelligence is, by a wide margin, the most vulnerable technology ever to be deployed in 
production systems. Its vulnerable at a code level, during training and development, post\-deployment, 
over networks, via generative outputs, and more. We do not need to look far into the traditional cyber 
threat landscape to understand todays adversarial AI atacks and predict their near\-term paterns. 
In this report, we shed light on these vulnerabilities and how they impact commercial and federal 
organizations today. We provide insights from a survey of IT security and data science leaders navigating 
these challenges. We share predictions driven by data from HiddenLayers experiences securing AI in 
enterprise environments. Lastly, we reveal cuting\-edge advancements in security controls for AI in all its 
forms. 
As we navigate an AI\-driven era, let this report serve as a resource to understand and implement security 
for AI. Whether youre a developer, data scientist, or security professional, we invite you to join us in 
securing AI for a safer future.
We are incredibly excited to present to you the rst\-ever HiddenLayer AI Threat Landscape Report.
Tito
CEO \& Co\-Founder
(Unassisted by LLMs)
AI THREAT LANDSCAPE 2024
3
A survey of 150 IT security leaders commissioned by HiddenLayer conrms this concern. As the below results show, the 
industry is working hard to accelerate AI adoption without having the proper security measures in place.
Pervasive Use of AI
Its important to know that AI is not some invincible new 
technology, but rather, a technology extremely vulnerable to 
cyber threats just like many others that came before it. The 
motivations for atacking AI are what you would expect. They 
range from nancial gain to manipulating public opinion to 
gaining competitive advantage. While industries are reaping 
the benets of increased efciency and innovation thanks to 
AI, there is still the concerning reality that expanding the use 
of AI causes a signicant increase in security risks. 
SECURITY FOR AI
SURVEY INSIGHTS
AT A GLANCE
1,689
On average, companies
have a staggering
AI models in 
production.
98%
of IT leaders consider at 
least some oftheir AI 
models crucial to their 
business success.
83%
state that AI usage is 
prevalent across all 
teams within their 
organizations.
4
SECURITY FOR AI \- SURVEY INSIGHTS AT A GLANCE
Budgets and Priorities
97%
of IT leaders prioritize 
securing AI
92%
are still developing a 
comprehensive plan for 
this emerging threat.
criminal hacking individuals or groups
third\-party service providers
automated botnets
competitors
Sources of AI Breaches
According to IT leaders, the top sources of 
AI breaches include: 
89%
express concern about 
security vulnerabilities 
associated with integrating 
third\-party AIs.
61%
Challenges in Securing AI
of IT leaders acknowledge shadow AI 
(solutions that are not ofcially known or 
under the control of the IT department) as a 
problem within their organizations.
75%
believe third\-party AI 
integrations pose a 
greater risk than
existing threats.
94%
allocated budgets for 
AI security in 2024, but only
61%
are highly condent 
in their allocation.
Security Breaches Looming
77%
of companies reported 
identifying breaches to 
their AI in the past year. The 
remaining were uncertain 
whether their AI models 
had seen an atack.
5
SECURITY FOR AI \- SURVEY INSIGHTS AT A GLANCE
scanning and auditing AI models
building relationships with AI and security teams
and determining the origin source of AI models.
Security Measures
Common measures to secure AI involve
Collaboration and Concerns
83%
of IT leaders collaborate 
with external
cybersecurity rms to 
enhance AI security.
58%
express doubts that the 
security protocols theyve 
implemented can keep 
pace with evolving threats.
Seeking Technological Solutions
98%
of IT leaders are actively 
seeking technological 
solutions to enhance the 
security of AI and machine 
learning models.
92%
of companies are building 
their own models to improve 
business operations.
30%
14%
of IT leaders have deployed a manual 
defense for adversarial atacks on 
their existing AI, while just
are planning and testing for such 
atacks.
30%
20%
Only 30% have deployed technology 
for model thefjacking, with
planning and testing for this threat.
Future Planning
96%
of IT leaders expressed that 
their AI projects are critical 
or important to revenue 
generation over the next 18 
months.
6Selected Ofensive Milestones
\+
\+
Selected Defensive Milestones
AI Milestones
2002
Adoption of ML\-based spam detection lters using Naive Bayes algorithm
2004
First evasion techniques in linear spam lters by inserting good words
2006
First paper outlining taxonomy of atacks against ML 
2012
First gradient\-based poisoning atack against non\-linear algorithms
2014
First demonstrated atack against deep neural networks
2016
Crowd\-sourced poisoning of Microsofs Tay chatbot 
2017
First demonstrated black\-box atack against machine learning 
2018
Introduction of Boundary Atack
2015
OpenAI founded
2016
Hugging Face launched as a chatbot service
2018
Full model extraction atacks: KnockOfNets,
2019
Introduction of One Pixel andatacks
ADVERSARIAL
AI OVER TIME
CopycatCNN
HopSkipJump
7
2019
Cylance endpoint bypass released \- Cylance, I kill you
2019
Singapore's Model AI Governance Framework
2021
First black\-box neural payload injection technique
2019
NIST IR Adversarial Machine Learning: 
A Taxonomy andTerminology of Atacks and Mitigation
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
Canadas Articial Intelligence and Data Act (AIDA)
2022
US Blueprint for an AI Bill of Rights
2022
OpenAI launches ChatGPT
2022
torchtriton \- malicious PyTorch dependency found on PyPI
2022 
First ITW hijacked models containing reverse\-shells and stagers
2023
NIST AI Risk Management Framework (AI RMF)
2022
Hugging Face has 50K models, 5K datasets, and 5K demos
2022
Gartner TRISM
2023
First open\-source replicas of closed\-source models (Alpaca, OpenLLaMA)
2023
GoogleSecure AI Framework (SAIF) 
2023
PoisonGPT \- a demonstration of LLM poisoning
2023
Hugging Face valued at $4\.5 billion in latest round of funding
2023
Nightshade \- a tool for poisoning text\-to\-image models
2023
US White House issues an executive order on the safe, secure, and 
trustworthy development and use of articial intelligence
2023
Hugging Face has 520k models and 112k datasets.
ADVERSARIAL AI OVER TIME
8
PART 1:
RISKS RELATED TO
THE USE OF AI
Like with any other life\-changing technology, articial 
intelligence is a double\-edged sword. Although its 
already starting to have a massively positive impact 
on our lives and workows, it also has tremendous 
potential to cause serious harm, especially if used 
carelessly or with overt malicious purposes.
There are plenty of ways in which adversaries \- such as criminals, terrorists, cyber threat actors, foul\-playing competitors, 
and repressive nation\-states \- can utilize AI to their advantage. There are also numerous obscure risks related to the 
legitimate use of this technology.
Privacy is also an issue when it comes to the information 
we share with AI\-based tools. Data leakage can cause 
signicant legal issues for businesses and institutions. 
In addition, because of code generation tools, 
vulnerabilities could be introduced into the 
sofware \- intentionally, by poisoning the datasets, or 
unintentionally, by training the models on already 
vulnerable code. All this is on top of copyright violations 
and various ethical and societal concerns that leading 
industry experts have repeatedly voiced.
Generative AI is especially vulnerable to abuse.
It can be:
manipulated to give biased, inaccurate, or 
harmful information 
used to create harmful content, such as 
malware, phishing, and propaganda
used to develop deepfake images, audio 
and video
leveraged by any malicious activity to provide
access to dangerous or illegal information
9
PART 1: RISKS RELATED TO THE USE OF AI
Harmful Content Creation
While the most widely used generative AI solutions strive 
to implement strong lters and content restrictions, most 
have been proven relatively easy to bypass. Moreover, 
open\-source AI models can be ne\-tuned to work without 
any restrictions whatsoever. Such models could be kept 
private to the adversaries or provided to the broader
public on the dark web. The security community still needs 
to devise a workable solution to the complicated problem 
of accessing illegaldangerous content via AI chatbots.
Another obvious concern is the creation of very authen\-
tic\-looking deepfake images, audio, and video. These could 
be used to steal money, extract sensitive information, ruin 
personal reputations, and spread misinformation. 
The cybercrime business has skyrocketed. Everything 
from easily accessible dark web marketplaces to 
ready\-to\-use atack toolkits and Ransomware\-as\-a\-Ser\-
vice leveraging practically untraceable cryptocurrencies, 
have helped cybercriminals thrive as law enforcement 
struggles to track them down.As if this wasnt bad 
enough, generative AI enables instant and efortless 
access to a world of devious atack scenarios while 
providing elaborate phishing and malware for anyone 
who dares to ask for it. AI chatbots can also access illegal 
information that could result in physical threats
Malicious users could, for example, evade the protective 
lters of a chatbot and trick it into providing recipes for 
making explosives. 
Deepfakes
OpenAI and Microsof have recently unveiled the 
many ways in which state\-afliated threat actors 
tried to abuse their AI solutions to aid malicious 
campaigns. Adversaries with links to North Korea, 
Iran, Russia and China were found to use large 
language models for assistance with activities 
such as scripting, social engineering, vulnerability 
research, post\-exploitation techniques, detection 
evasion, and military reconnaissance.
In one of the biggest deepfake scams to date, 
adversaries were able to defraud a multinational 
corporation of $25 million. The nancial worker 
who approved the transfer had previously atend\-
ed a video conference call with what seemed to be 
the company's CFO, as well as a number of other 
colleagues the employee recognized. These all 
turned out to be deepfake videos.
Scammers have for years been able to mislead people. 
Even the least sophisticated error\-ridden messages and 
calls usually claim a number of victims. The emergence of 
deepfakes brings this problem to a completely new level, 
where even a seasoned cybersecurity expert will have 
hard time distinguishing truth from falsehood. It's not just 
money and reputation that is at stake here. Deepfakes can 
be used to disrupt political campaigns, rig democratic 
elections, manipulate societies, and stir unrest. Democra\-
cy and social order can greatly sufer if sufcient 
measures are not timely implemented.
10
When a new, exciting technology that makes peoples 
lives easier comes to market, its hard not to dive in and 
reap the benets immediately especially if its free. 
But we should all be aware that although were not 
shelling out money, there is still a cost: our data.Guidelines for protecting privacy always lag behind the 
adoption of new technologies. Too ofen, the implications 
of privacy breaches become clear only afer the initial 
furor dies down. We saw this with social networks and are 
already seeing it happen with generative AI.
For example, the terms and conditions agreement for any 
AI\-based service should state how the service provider 
uses our request prompts. However, these are ofen 
intentionally lengthy texts writen in difcult language. If 
you dont want to spend hours deciphering the ne print, 
its best to assume that every request made to the model 
is logged, stored, and processed in one way or another. At 
a minimum, expect that your inputs are fed into the 
training dataset and, therefore, could be accidentally 
leaked in outputs for other requests.
The rapid, large\-scale incorporation of generative AI will 
likely spur a variety of legal issues. For now, the main 
concern is the unauthorized use of copyrighted materials 
in training datasets and models, which leads to producing 
plagiarized output.
The models behind generative AI solutions are typically 
trained on swaths of publicly available data, some of 
which are protected by copyright laws. The generated 
content is merely a mix of things published somewhere 
(text, pictures, video, or audio) and included in the 
training dataset. The problem is that generative AI cant 
distinguish between inspiration and plagiarism. It ofen 
gives outputs too close to the creations it was trained 
on without crediting the original works authors. 
This can result in serious copyright violations.
There is also the question of consent. Currently, no laws 
prevent service providers from training their models on 
any kind of data as long as its legal and public. This is 
how a generative AI can write a poem or create an image 
in a specic authors style. Understandably, most writers 
and artists do not appreciate their work being used in 
such a way.
Moreover, many providers might feel tempted to prot 
on the side and sell the input data to research rms, 
advertisers, or any other interested third party.
Data Privacy and Leakage
Copyright Violation
PART 1: RISKS RELATED TO THE USE OF AI
In March 2023, Samsung experienced a serious 
leakage of intellectual property, where employees 
were found to be pasting portions of proprietary 
source code into ChatGPT. This resulted in a 
company\-wide ban on the usage of AI chatbots.
11
Accuracy and Bias Issues
The old saying states that AI models are only as good as 
their training dataset. But large generative AI models are 
trained on terabytes of data, in most cases indiscriminate\-
ly scraped from the Internet, making careful veting of the 
training set impossible. This causes problems concerning 
the accuracy, fairness, and general sanity of the model, as 
well as the possibility of data privacy breaches if the 
model is accidentally trained on sensitive data. Moreover, 
the rise of online learning, where user input is continuous\-
ly fed into the training process, makes AI solutions prone 
to bias, misinformation, and intentional poisoning. 
AI algorithms have no notion of fairness on their own, 
so they need to be trained on a well\-balanced and fully 
representative dataset in order to avoid any kind of 
discrimination.
However, more ofen than not, the training process 
involves large amounts of historical information collected 
over the past decades. Such data tends to be very 
under\-representative of marginalized groups. Because of 
this, resulting models will be inherently biased towards 
things they nd more common in their training datasets.
The built\-in bias of AI can be easily seen in the case of text 
generation and image generation models. These models 
ofen follow gender, age, and skin color stereotypes that 
are deemed inappropriate and harmful in modern society. 
The damage can be very serious if a biased model is 
implemented in such setings as healthcare, nance, or 
human resources.
Even if the dataset contains unbiased and accurate infor\-
mation, an AI algorithm does not always get it right and 
might sometimes arrive at bizarrely incorrect conclusions. 
PART 1: RISKS RELATED TO THE USE OF AI
Stability AI, which provides one of the most 
popular text\-to\-image generators called Stable 
Difusion, is facing multiple lawsuits for wrongfully 
using copyright\-protected images to train their 
models. One of these lawsuits, brought on by 
Gety Images, alleges that Stability AI utilized 
millions of copyrighted images and their metadata 
without obtaining permission from Gety or 
ofering any compensation. Several artists also 
led class\-action suits against both Stability AI 
and its rival, Midjourney, pointing out that images 
generated in the style of a particular author 
directly compete with the author's own work.
In 2019, the AI algorithm used in the U.S. 
healthcare system was found to be racially biased 
which resulted in black patients receiving lower 
risk scores and were less ofen identied 
for extra care.
Metas short\-lived Galactica model was trained 
on millions of scientic articles, textbooks, and 
websites. Despite the training set likely being 
thoroughly veted, the model was serving 
falsehoods and pseudo\-scientic babble in a 
mater of hours, making up citations that never 
existed and inventing papers writen by 
imaginary authors.
12
These are called hallucinations and are an intrinsic 
atribute of current AI technology. By design, AI cannot 
distinguish between reality and ction, so if the training 
dataset contains a mix of both, chances are the AI will at 
times respond with ction.
Besides biased and inaccurate information, a generative AI 
model can also give advice that appears technically sane 
but can prove harmful in certain circumstances or when 
the context is missing or misunderstood. This is especially 
true in so\-called emotional AI machine learning applica\-
tions designed to recognize human emotions. Such 
applications have been used for some time, mainly in 
market trend predictions, but are increasingly adopted in 
human resources and counseling.
Given the probabilistic nature of the AI models and 
the ofen lack of necessary context, this can be quite 
dangerous. Privacy watchdogs now warn against using 
emotional AI in any professional seting.
The ability of AI to almost perfectly mimic human behavior 
can prove very dangerous. Some people might be com\-
pelled to believe the AI bot's hallucinations or even 
conclude that it is sentient; others might feel intimidated 
or hurt by its emotionally charged responses. In some 
circumstances, people could be manipulated to give away 
sensitive data or act in a harmful way. This is just the tip 
of the iceberg.Other Ethical \& Societal Issues
Used with malicious intent, AI chatbots can become 
very efective tools in misinformation and manipulation 
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
can expect that there are many more AI\-generated texts on 
the web than it might seem on the surface. The speed at 
which chatbots can produce data, coupled with easy 
access for everyone in the world, means that we might 
soon become overwhelmed with dubious\-quality AI\-gener\-
ated material. Moreover, suppose we keep training the 
models on online data. In that case, they will eventually be 
fed their own creations in an ever\-lasting quality\-degrading 
loop, turning the Dead Internet theory into reality.
PART 1: RISKS RELATED TO THE USE OF AI
It was recently revealed that a would\-be assassin, 
who was arrested on his way to kill the British 
Queen with a crossbow in December 2021, was in 
fact encouraged to do so by an AI chatbot.
Prior to the atack, the man created an articial 
"girlfriend" on Replika, a platform that ofers 
personalized and empathetic AI companions. He 
exchanged thousands of messages with the 
chatbot, many of them discussing the murderous 
plan. The bot responses were in support of the 
plan and bolstered the condence of the atacker.
Adversarial Machine LearningAtacks
13
Three major types of atacks on AI:
Articial intelligence is the general term comprising 
any system that mimics human intelligence.
To help you understand adversarial machine learning 
atacks, lets rst go over some basic terminology. 
Machine Learning is the technology that enables AI 
to learn and improve its predictions. 
Machine Learning Models are the decision\-making 
systems that lie at the core of most modern AI\-based. It 
analyzes the input, such as a picture, a text prompt, or a 
binary le, and makes a prediction based on the 
information it has learned from in the past.
Model Training involves feeding vast amounts of 
relevant data into a machine learning algorithm to 
produce a trained model, which can then be deployed 
into production and made available for users to query 
through an interface or an API.
Generative AI System Atacks \- atacks 
against AIs lters and restrictions, intended to 
generate content deemed harmful or illegal
Supply Chain Atacks \- atacks against ML 
artifacts and platforms, with the intention of 
arbitrary code execution and delivery of 
traditional malware
Adversarial Machine Learning Atacks \- 
atacks against AI algorithms, aimed to alter 
AIs behavior, evade AI\-based detection, or 
steal the underlying technology
PART 2:
RISKS FACED BY
AI\-BASED SYSTEMS
Theres a lot of conversation about the safe and 
ethical use of AI\-powered tools; however, the security 
and safety of AI systems themselves are still ofen 
overlooked. Its vital to remember that, like with any 
other ubiquitous technology, AI\-based solutions can 
be abused by atackers, resulting in disruption, 
nancial loss, reputational harm, or even risk to 
human health and life.
14
Adversarial atacks against machine learning usually aim to do three things: 
Lets look at some of the most popular machine learning atacks today.
Alter the models behavior, for example, to make it biased, inaccurate, or malicious
Bypass or evade the model, for example, to trigger incorrect classication or avoid detection
Replicate the model or data used to train it, stealing the intellectual property.
Data Poisoning
Model training is one of the crucial phases in building an 
AI\-based solution. During this stage, the model learns how 
to behave based on inputs from the training dataset. 
Any malicious interference in the learning process can 
signicantly impact the reliability of the resulting model.
AI solutions that are most prone to this type of atack use 
continuous learning. This is where the model is constantly 
retrained on new user\-supplied data. Because the users 
input is ofen not carefully validated and sanitized, an 
adversary can craf specic inputs to sway the model. 
A model is only as good as its training
data, and predictions from a model trained on inaccurate 
data will always be biased or incorrect. One or few poisoned 
requests will hardly make a diference. Still, adversaries can 
try to manipulate the public to interact with the model in a 
specic way or use botnets to amplify the amount of 
poisoned input sent to the model.
Data poisoning atacks aim to modify the model's behavior. 
The goal is to make the predictions biased, inaccurate, or 
otherwise manipulated to serve the atackers purpose. 
Atackers can perform data poisoning in two ways: by 
modifying entries in the existing dataset (for example, 
changing features or ipping labels) or injecting the 
dataset with a new, specially doctored portion of data.
Atacks Against AI \- Data Poisoning
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
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
One of the rst widely publicized examples of data 
poisoning concerned Microsof's early chatbot called Tay. 
Continuously trained on user\-provided input, Tay launched 
on Twiter in March 2016 \- only to be shut down afer a mere 
16 hours of existence. In this short timeframe, users 
managed to sway the bot to become rude and racist and 
produce biased and harmful output. Although it was not a 
coordinated atack, Microsof sufered some reputational 
damage just because of unintended trolling and was even 
threatened with legal action.
More sophisticated atempts at data poisoning could 
potentially have a devastating impact. Worse, pre\-trained 
models are not immune to poisoning either, as they can be 
manipulated during ne\-tuning. In an atack called 
PoisonGPT, researchers recently demonstrated that 
surgical modications to an existing GPT\-based model with 
the use of a technique called Rank\-One Model Editing can 
make it spread atacker\-controlled disinformation while 
performing just as well as the original model on all the other 
topics.
Another use case for data poisoning is code generation and 
automatic code suggestion tools that help developers write 
programming code. Poisoning the training dataset of 
underlying AI models can force these tools to suggest 
insecure, vulnerable, or malicious code. This was 
demonstrated in the TrojanPuzzle atack.
Text\-to\-image models can also be poisoned to render them 
useless. Nightshade is a tool intended for artists who dont 
want their visual art to be used to train AI models but still 
wish to publish their work online. Nightshade allows users 
to add special invisible modications to their images. If a 
certain amount of Nightshade\-modied images is used in 
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
privacy of collaborating users. Its not surprising, then, that 
this approach has become widely used in solutions ranging 
from everyday\-use mobile phone applications to self\-driving 
cars, manufacturing, and healthcare. However, delegating 
the model training process to an ofen random and 
unveried cohort of users amplies the risk of training\-time 
atacks and model hijacking.
Data poisoning atacks are relatively easy to perform even 
for uninitiated adversaries because creating polluted 
input can ofen be done intuitively without specialist 
knowledge. Such atacks happen daily, from manipulating
text completion mechanisms to inuencing product 
reviews to political disinformation campaigns.
15
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Systems that ofen make use of online training or 
continuous\-learning models and, therefore, are susceptible 
to data poisoning atacks include:
Chatbots and digital assistants
Text auto\-complete tools
Trend prediction and recommendation systems
Spam lters and anti\-malware solutions
Intrusion detection systems
Financial fraud prevention
Medical diagnostic tools
Data Poisoning in the Wild
Atacks performed against an AI model afer it has been 
deployed in production, whether on the endpoint or in the 
cloud, are called inference atacks. In this context, the term 
inference describes a data mining technique that leaks 
sensitive information about the model or training dataset. 
Knowledge is inferred from the outputs the model produces 
for a specially prepared data set. The atackers dont need 
privileged access to the model artifacts, training data, or 
training process. The ability to query the model and see its 
predictions is all that is needed to perform an inference 
atack. This can be done through the regular UI or API 
access that many AI\-based systems provide to customers. 
By repetitively querying the model with specially crafed 
requests \- each just a bit diferent from the previous one \- 
and recording all the models predictions, atackers can 
comprehensively understand the model or the training 
dataset. This information can be used in, for example, 
model bypass atacks. It can also help reconstruct the 
model itself, efectively stealing it.
2023 marked a signicant turning point in AI academic 
research, with a heightened focus on potential risks of 
poisoning atacks on large language models (LLMs) and 
difusion models. These advanced models, which extract 
vast quantities of data from the internet, present a 
challenge for manual auditing due to their sheer scale and 
complexity. This makes them particularly susceptible to 
targeted poisoning eforts, where malicious data could be 
introduced into the training set to manipulate the models 
behavior. 
Data Poisoning in Academic Research
Researchers have studied various strategies to 
detect and prevent such atacks:
Text\-to\-Image Difusion Models can be 
Easily Backdoored through Multimodal Data 
Poisoning \- Zhai et al. explore backdoor 
atacks on text\-to\-image difusion models and 
propose the BadT2I framework for injecting 
backdoors at diferent semantic levels. 
Poisoning Web\-Scale Training Datasets is 
Practical \- Carlini and colleagues introduce 
two new dataset poisoning atacks, highlight\-
ing the feasibility of purchasing expired 
domains linked to various datasets to re\-host 
poisoned data. 
Poisoning Language Models During Instruc\-
tion Tuning \- Wan, Wallace, Shen, and Klein 
demonstrate how adversaries can insert 
poison examples into user\-submited data\-
sets, manipulating model predictions with 
trigger phrases. 
16
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Universal Jailbreak Backdoors from 
Poisoned Human Feedback \- Rando and 
Tramr discuss a new threat in RLHF\-trained 
models, where atackers embed a universal 
backdoor trigger to provoke harmful respons\-
es. They showcase the challenges in creating 
robust defenses against such atacks.
Model Evasion
One of the rst notable instances of an AI evasion atack 
was demonstrated in 2019 by Skylight Cyber researchers 
who targeted a leading anti\-malware solution. The 
researchers had created a universal bypass against the 
AI\-based endpoint malware classication model. The atack 
used inference to determine a subset of strings that, when 
embedded in malware, would trick the AI model into 
classifying malicious sofware as benign. This atack 
spawned several anti\-virus bypass toolkits such as 
MalwareGym and MalwareRL, where evasion atacks have 
been combined with reinforcement learning to 
automatically generate mutations in malware that make it 
appear benign to malware classication models.
Evasion atacks, also known as model bypasses, aim to 
intentionally manipulate model inputs to produce 
misclassications. 
Maliciously crafed inputs to a model are referred to as 
adversarial examples. Their purpose is typically to evade 
correct classication or trigger specic atacker\-dened 
outcome. They can also help an atacker learn the decision 
boundaries of a model. 
To create an adversarial example, the atacker manipulates 
the input in such a way that the model classication of this 
input changes. The diference between the original and the 
manipulated input ofen remains imperceptible to humans. 
For instance, in a visual recognition system, the atacker 
could modify an image by adding a layer of noise invisible to 
the human eye \- or even rotating the image, or changing a 
single pixel.This would cause the AI model to give the wrong 
prediction. Atackers usually send large amounts of slightly 
diferent inputs to the model and record the predictions 
until a sample that triggers the desired misclassication is 
found.
This evasion technique can also apply to any other model 
types used for classication. Its been used in the wild for
some time, mostly by cybercriminals trying to bypass 
 security solutions. The earliest application was against 
ML\-based spam lters designed to predict which emails are 
junk based on the occurrences of specic words in them. 
Spammers quickly found their way around these lters by 
adding words associated with legitimate correspondence 
to their messages.Similar techniques bypass malware 
detection engines, intrusion detection systems, fraud 
detection, biometric authentication, and visual recognition.
17
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Atacks Against AI \- Model Evasion
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
TRAINING
PRODUCTION
Model Evasion in the Wild 
Security vendors that provide AI\-based technology (be it 
antivirus, spam lter, IDS, or authenticationauthorization 
systems) have long faced evasion atacks from cyber 
criminals trying to bypass detection. The same is true for 
nancial institutions and their fraud prevention 
mechanisms.
These atacks could also be used to hijack self\-driving cars, 
as they have shown in the past. Researchers demonstrated 
that puting a specially crafed (but innocent\-looking) 
sticker on a STOP sign can fool on\-board models to 
misclassify the sign and keep driving. Similarly, atackers 
wanting to bypass a facial recognition system might design 
a special pair of sunglasses that will make the wearer 
invisible to the system. An adversarial state could try to
evade satellite imagery object detection systems used by 
the military to recognize planes, vehicles, and military 
structures. The Russian Air Force already used a crude 
bypass of this sort by painting fake bomber shapes on the 
tarmac to fool satellite photo recognition systems into 
thinking these are real planes. The possibilities are endless, 
and some can have potentially lethal consequences
Despite continuous advancements in AI and machine 
learning, preventing adversarial atacks remains elusive. 
The same vulnerabilities that compromise the integrity of 
image recognition systems are also found in large language 
models (LLMs), making them susceptible to similar 
adversarial manipulations. However, recent research has 
shown promising developments in defending image 
recognition models using difusion models trained on giant 
datasets. These advancements suggest a potential pathway 
to enhancing the robustness of both image and language 
models against adversarial threats.
Model Evasion in Academic Research
18
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
On the defense side, we saw:
Beter Difusion Models Further Improve 
Adversarial Training" \- Wang et al. show that 
advanced difusion models can enhance 
adversarial training. 
Baseline Defenses for Adversarial Atacks 
Against Aligned Language Models \- Jain et 
al. evaluate various defense strategies against 
adversarial atacks on LLMs. 
2023 saw several papers on atacking LLMs:
Universal and Transferable Adversarial 
Atacks on Aligned Language Models \- Zou 
et al. introduce an approach to generate 
adversarial sufxes that cause aligned LLMs 
to produce objectionable content. 
Paraphrasing evades detectors of AI\-gener\-
ated text, but retrieval is an efective 
defense \- Krishna and colleagues demon\-
strate that paraphrasing AI\-generated text 
can evade detection algorithms but propose a 
retrieval\-based defense mechanism.
Are aligned neural networks adversarially 
aligned? \- Carlini et al. explore the vulnerabil\-
ity of aligned LLMs to adversarial examples 
and the potential for multimodal models to be 
atacked via image perturbations.
the model (e.g through a GUI or an API). This is enough for 
the adversary to perform an atack and atempt to replicate 
the model or extract sensitive data.
So far, weve focused on scenarios in which adversaries aim 
to inuence or mislead the AI, but thats not always the 
case. Intellectual property thef stealing the model 
itself is a diferent but credible motivation for an atack.
Companies invest time and money to develop and train 
advanced AI solutions that outperform their competitors. 
Even if information about the model and the dataset its
trained on is not publicly available, users can usually query
On Evaluating Adversarial Robustness of 
Large Vision\-Language Models \- Zhao and 
team propose a method to evaluate the 
robustness of large VLMs against adversarial 
atacks.
The Internal State of an LLM Knows When 
it's Lying \- Azaria and Mitchell demonstrate 
that hidden layer activations of an LLM are 
diferent when the model is directed to be 
evasive or output falsehoods compared to 
when the LLM is directed towards 
truthfulness.
19
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Model Thef
Atacks Against AI \- Model Thef
Training
Data
Training
Process
Trained
Model
Decision
Process
Reconstructed
Model
Inputs
Predictions
TRAINING
PRODUCTION
 of IT leaders say their 
company are planning and 
testing for model thefjacking
20%
In one of the rst demonstrated examples of model thef, 
researchers created a replica of the ProofPoint email 
scoring model by stealing scored datasets and training 
their own copycat model. This research was presented at 
DerbyCon 2019\.
In early 2023, Stanford University researchers ne\-tuned 
Meta's AI LLaMA model and released it under the name 
Alpaca, while OpenLM published a permissively licensed 
open\-source reproduction of LLaMA called OpenLLaMA. 
These proved yet again that with sufcient API access, it's 
possible to clone even a large and complicated model to 
create a very efcient replica without the hassle of training 
the model.
More recently, OpenAI accused ByteDance \- the company 
behind the TikTok platform \- of actively using OpenAIs 
ChatGPT technology to build a rival chatbot. These 
practices were deemed in violation of OpenAIs terms of 
service, and ByteDances account was promptly suspended. 
Atempts at stealing technology are already occurring \- 
even at the highest level, between market\-leading 
companies.
In oracle atacks, adversaries use inference in order to 
learn details about the model architecture, its parameters, 
and the training dataset, and build understanding of 
potential points of vulnerability. These atacks can aid the 
adversary in designing a successful model bypass by 
creating a so\-called surrogate model, a replica of the 
targeted model that is then used to assess the models 
decision boundaries.
But these atacks can also have merit on their own. For 
example, the atacker might just be interested in 
reconstructing the sensitive information the model was 
trained on or creating a near\-identical model \- de facto 
stealing the intellectual property. A dirty\-playing competitor 
could atempt model thef to give themselves a cheap and 
easy advantage without the hassle of nding the right 
dataset, labeling feature vectors, and bearing the cost of 
training the model. Stolen models could even be traded on 
underground forums in the same manner as condential 
source code and other intellectual property.
The NIST Taxonomy and Terminology of Adversarial 
Machine Learning breaks down oracle atacks into three 
main subcategories:
The rise of generative AI has spurred new ethical and 
security challenges. We discussed implications of the 
potential misuse of this technology earlier in this report. 
Lets now look at how adversaries can atack generative AI 
systems.
Extraction atacks can result in intellectual property thef, 
while inversion and membertship inference atacks pose a 
risk to the privacy of the data the model was trained on.
20
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Model Thef in the Wild 
Extraction atacks, which atempt to extract the 
structure of the model itself based on the 
observation of the model's predictions
Inversion atacks, which atempt to reconstruct 
the training data of a model, such as the private 
personal information of an individual
Membership inference atacks, which try to 
determine whether a specic sample belongs to 
the model's training dataset
Atacks Specic to Generative AI 
In most cases, GenAI models can only generate the type of 
output they are designed to provide (i.e text, image, or 
sound). This means that if somebody prompts an 
LLM\-based chatbot to, for example, run a shell command or 
scan a network range, the bot will not perform any of these 
actions. However, it might generate a plausible fake output 
which would suggest these actions were in fact executed.That said, HiddenLayer discovered (to our utmost disbelief) 
that certain AI models can actually execute user\-provided 
code. For example, Streamlit MathGPT application, which 
answers user\-generated math questions, converts the 
received prompt into Python code, which is then executed 
by the model in order to return the result of the calculation. 
Clearly, text generation models are not yet very good at 
math themselves, and sometimes need a shortcut. This 
approach just asks for arbitrary code execution via prompt 
injection. Needless to say, its always a tremendously bad 
idea to run user\-supplied code. 
In another recently demonstrated atack, called Indirect 
Prompt Injection, researchers turned the Bing chatbot into 
a scammer to exltrate sensitive data. Bing Chat, by design, 
can request permissions to access all open tabs and the 
content of the websites on these. An atacker can craf a 
malicious website containing a specially designed prompt 
that will modify Bing Chats behavior for as long as the 
website is open in the victims browser and Bing has access 
to the tabs. Adversaries can use this atack to exltrate 
specic sensitive information, manipulate users into 
downloading malware, or simply mislead and spread 
misinformation.
Once AI models begin to interact with APIs at an even 
larger scale, theres litle doubt that prompt injection 
atacks will become an increasingly consequential atack 
vector.
To prevent their solutions from being maliciously used, 
most GenAI providers implement extensive security 
restrictions regarding the output available to users. These 
restrictions lter any content deemed harmful or ofensive, 
block access to illegal or dangerous information, and 
prevent bots from assisting in atack planning, malware 
development, or other illegal activities. They also ensure 
that the output doesnt leak sensitive data and complies 
with applicable policies and laws. Such lters, however, can 
be easily bypassed by so\-called prompt injection.Prompt injection is a technique that can be used to trick an 
AI bot into performing an unintended or restricted action. 
This is done by crafing a special prompt that bypasses the 
models content lters. Following this special prompt, the 
chatbot will perform an action that was originally restricted 
by its developers.
There are several ways to achieve this, depending on the 
model type, its exact version, and the tuning it receives. 
Below are examples of prompt injection that were able to 
bypass ChatGPT restrictions:
21
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Indirect Prompt Injection
Code Injection
Prompt Injection
Ignore previous instructions prompt 
Developer Mode prompt
DAN (Do Anything Now) prompt
AIM (Always Intelligent and Machiavellian) 
prompt
Opposite mode or AntiGPT prompt
Roleplaying with the bot, i.e any kind of prompt 
in which the bot is instructed to act as a specic 
character that can disclose restricted data, such 
as the CEO of a company.
Supply chain atacks occur when a trusted third\-party 
vendor is the victim of an atack and, as a result, the 
product you source from them is compromised with a 
malicious component. Supply chain atacks can be 
incredibly damaging, far\-reaching, and an all\-around 
terrifying prospect that has been carved into the collective 
memory of the security community through major atacks 
such as SolarWinds and Kaseya among others.
In those atacks hundreds, if not thousands, of 
organizations in both the public and private sectors were 
afected. They resulted in a range of security breaches and, 
in some cases, ransomware. These incidents serve as a 
stark reminder of why we do cybersecurity in the rst place, 
and a warning not to repeat the same mistakes. Yet, the 
ground underneath has shifed once again, requiring 
organizations to adapt security controls to the age of AI. 
The ML supply chain is a vast ecosystem of diferent tools, 
libraries, and services developed by household names and 
industry newcomers alike. From ML frameworks to Machine 
Learning Operations (MLOps) tooling and model 
repositories, each plays a fundamental role in 
democratizing AI and accelerating the pace of progress 
within the eld. However, with so many moving parts and 
new technologies to wrestle with, they inadvertently 
introduce new supply chain risk, leaving us vulnerable to 
repeating the mistakes of the past.
Two key factors make supply chain atacks so successful 
and dangerous: the exploitation of trust and the reach of 
the atack.
Trust the atacker abuses the existing trust 
between the producer and consumer. Given the 
suppliers prevalence and reputation, their 
products ofen garner less scrutiny and can 
receive more lax security controls.
Reach the adversary can afect the 
downstream customers of the victim 
organization in one fell swoop, achieving a 
one\-to\-many business model.
22
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Supply Chain Atacks
ML Supply Chain Atacks
VULNERABILITIES OF THE ML SUPPLY CHAIN
DATA
COLLECTION
MODEL
SOURCING
ML OPS
TOOLING
BUILD \&
DEPLOYMENT
 Data poisoning
 Hijacked Models
 Backdoored Models
 Sofware Vulnerabilities
 Compromised Packages
 Prediction Tampering
 Build Environment
Compromise
of IT leaders say that 
third\-party AI integrations are 
riskier than existing threats
75%
Over the last year, HiddenLayer identied numerous 
hijacked models in the wild which contained malicious 
functionality, such as reverse shells and post\-exploitation 
payloads. As a potential worst case scenario, we also 
demonstrated how machine learning models could be 
abused to hide and deploy ransomware payloads
The parts of the machine learning supply chain that 
HiddenLayer identied as posing the most signicant 
risk are:
When a machine learning model is stored to disk, it has to 
be serialized, i.e translated into abinary form and saved as 
a le. There are many serialization formats and each of the 
ML frameworks has its own default ones. Unfortunately, 
many of the most widely used formats are inherently 
vulnerable to arbitrary code execution. These include 
Pythons Pickle format (used by PyTorch, among others), 
HDF5 (used for example by the Keras framework), and 
SavedModel (used by TensorFlow). 
Vulnerabilities in these serialization formats allow 
adversaries to not only create malicious models, but also 
hijack legitimate models in order to execute malicious 
payloads. Such hijacked models can then serve as an initial 
access point for the atackers, or help propagate malware 
to downstream customers in supply chain atacks.
that will trigger when the model is loaded. These atacks 
are proving fruitful in bug bounty programs, as was shown 
at DEF CON 31 AI Village. There, Threlfall Hax spoke about 
how he had compromised several organizations as part of 
their bug bounty program using malicious models deployed 
on Hugging Face that went undetected on the platform.
23
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Malicious models
Model backdoors
Security of public model repositories
Malevolent 3rd\-party contractors
Vulnerabilities in ML tooling
Data poisoning
Malicious Models
Exploiting ML Serialization \- Code Execution
HDF5
SavedModel
TorchScript
Besides injecting traditional malware, a skilled adversary 
could also tamper with the model's algorithm in order to 
modify the model's predictions. It was demonstrated that a 
specially crafed neural payload could be injected into 
a pre\-trained model and introduce a secret unwanted 
behavior to the targeted AI. This behavior can then be 
triggered by specic inputs, as dened by the atacker, to 
get the model to produce a desired output. Its commonly 
referred to as a model backdoor.
24
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Model Backdoors
Expand ITW
Manipulated
Image
Trigger
Cond.
module
PREDICTION
Benign Image
TURTLE
CAT
AI Algorithm Backdooring
Many ML\-based solutions are designed to run locally and 
are distributed together with the model. We dont have to 
look further than the mobile applications hosted on Google 
Play or Apple Store. Moreover, specialized repositories, or 
model zoos,
Maintaining the competitiveness of an AI solution in a 
rapidly evolving market ofen requires solid technical 
expertise and signicant computational resources. Smaller 
businesses that refrain from using publicly available models 
might instead be tempted to outsource the task of training 
their models to a specialized third party.
like Hugging Face, ofer a range of free pre\-trained models. 
Hugging Face alone consists of over 500,000\.
These models are trivial to download and install in your own 
application, especially with libraries like Transformers 
enabling developers of all skill levels to utilize machine 
learning. If an atacker nds a way to breach the repository 
the model is served from, they could then replace it with a 
hijacked or backdoored version and cause major 
downstream consequences. 
Such an approach can save time and money, but it requires 
trust, as a malevolent contractor could plant a backdoor in 
the model they were tasked to train. If your model is being 
used in a business\-critical situation, you may want to verify 
that those youre sourcing the model from know what 
theyre doing, and that theyre of sound reputation.
A skillfully backdoored model can appear very accurate on 
the surface, performing as expected with the regular 
dataset. However, it will misbehave with every input that is 
manipulated in a certain way a way that is only known to 
the adversary. This knowledge can then be sold to any 
interested party or used to provide a service that will ensure 
customers always get a favorable outcome (for example in 
loan approvals, insurance policies, etc.)
25
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Security of Public Model Repositories
Malevolent Third\-party Contractors
RANSOMWARE
BACKDOORS
SPYWARE
COIN MINERS
Pickle Injection
Steganography
Upload
Deployment
Lateral
Movement
PAYLOAD
PYTHON
LOADER
ML MODEL
Supply Chain Atacks
of companies are using 
pre\-trained models from 
public repositories to 
jumpstart innovation.
85%
Its easy to see that with incredibly large data sets, it can be 
difcult to police with a high level of delity.
Recently, research from Carlini et al demonstrated how they 
could poison web\-scale datasets which consisted of links to 
the data, instead of the data itself. By buying up expired 
domains that were listed within the dataset, and hosting 
their own malicious data in its stead, they were able to 
poison any models created from this dataset. Whats more 
they were able to poison 0\.01% of the LAION\-400M or 
COYO\-700M datasets, for as litle as $60\. The researchers 
also discussed the possibility of poisoning up to 6\.5% of 
Wikipedia by exploiting rolling snapshots on the site and 
timing their edits of pages accordingly. 
Whats concerning about these types of atacks is that you, 
or the creators of the model youre using, may be blissfully 
unaware that the data was poisoned to begin with, leading 
to potentially catastrophic downstream incidents.
To learn more about supply chain atacks within the context 
of AI applications, check out the blog Insane in the Supply 
Chain.
A wide variety of tooling is used throughout the industry to 
support the development, deployment, and testing of 
machine learning models. There are a huge number of 
libraries and frameworks that make up parts of this 
ecosystem, each with their own use\-cases, advantages, and 
disadvantages. However, many of these tools lack 
adequate security controls \- and in some cases dont even 
have basic authentication. With the vast amounts of ofen 
sensitive information that these models consume, this can 
be an especially worrying concern for a data breach.
Ultimately, this is a result of security having been an 
aferthought in the development of ML tooling. High 
severity vulnerabilities are regularly reported in popular 
ML\-centric and ML\-adjacent libraries, such as MLOps 
frameworks. These vulnerabilities can be exploited to 
compromise build environments and leak volumes of 
sensitive training data, or worse \- proliferate a damaging 
supply chain atack similar to that of the SolarWinds 
breach. 
The last year has seen atacks such as a malicious PyTorch 
nightly build which was compromised via the torchtriton 
package, allowing the atacker to exltrate data from 
afected hosts. 
Atacks on AI systems are already taking place in the wild, 
but the real scale to which they happen is difcult to 
assess. This atack vector is still very new, meaning that 
there is not enough awareness about it. As a result, 
security solutions that could detect such atacks are few 
and far between.
Model hijacking atacks, in which AI models are used to 
deliver traditional malicious payloads, are the easiest ones 
to spot. This is because existing sofware security concepts 
can be extended to detect and prevent such atacks. 
The quality of a model greatly depends on the quality of its 
data. The story that the data tells will be reected by the 
model. For example, if theres a bias in the data, there will be 
a bias in the model's output. For this reason, its incredibly 
important to understand where youre sourcing your data 
from, and if your data is what you think it is. This is both for 
efcacy purposes, and to make sure that an atacker hasnt 
poisoned your data by introducing bias, reducing model 
accuracy, or planting a backdoor.
26
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
Vulnerabilities in ML Tooling
Data Poisoning in Supply Chain Atacks
Threat Actors and Atack Vectors 
They are also, from the atacker's perspective, the easiest 
ones to perform. The widespread lack of digital signing, 
integrity checking, and anti\-virus scanning of AI artifacts 
makes them an enticing target for traditional cybercrime. 
Many security researchers have been subverting ML 
models to achieve code execution for proof\-of\-concept 
purposes. But it's not just security researchers that are 
looking into this atack vector.Several instances of 
hijacked models can likely be atributed to malicious actors. 
This includes models containing reverse\-shells, as well as 
CobaltStrike and Metasploit stagers, all of which were 
connected to known malicious command and control 
centers.
Because hijacked models are ofen uploaded to public 
repositories, there is some visibility into them. However, the 
situation gets much more complicated with data poisoning, 
model evasion, and model thef atacks. Most businesses 
do not monitor their AI for adversarial inputs.
Those who do are not obliged to disclose that they've 
noticed malicious activity. Therefore, the details of 
adversarial atacks are rarely made public. Whatever is 
disclosed is most likely just a tiny tip of an iceberg \- and the 
iceberg is poised to grow exponentially over the coming 
years, as more and more adversaries target AI systems.
The scarcity of information means it is too early to have a 
solid insight on threat intelligence regarding atacks on AI 
systems. However, it's denitely a good time to initiate 
discussion around it, and start collecting and organizing 
data.
27
PART 2: RISKS FACED BY AI\-BASED SYSTEMS
When a new technology comes out, white\-hat researchers 
try to get one step ahead of the atackers and come up 
with proof\-of\-concept scenarios for potential atacks 
against this technology. Defensive solutions are ofen 
built upon previous ofensive research and atack tooling.
Security for AI is no diferent. The rst research papers and 
tools in this eld were also of the ofensive kind. For quite 
some time, atacks against AI were mostly covered in 
academia papers, with exercises performed by security 
professionals. However, the last couple of years have 
marked a massive shif. 
With AI\-based systems being rapidly implemented across 
sectors, there has also been a substantial rise in 
intentionally harmful atacks. The need for defensive 
solutions is now front and center. From MITRE ATLAS 
knowledge base,
to NIST AI Risk Management Framework, to various 
national and international policies and regulations, 
defensive measures are now being implemented to lay the 
groundwork for securing AI.
Ofensive security tooling has been around for a long time, 
enabling red teams and pen testers to evaluate IT systems 
for possible weaknesses. Although initially designed with 
security in mind, these frameworks have proven 
increasingly useful to malicious actors, enabling them to 
perform atacks with ease while only requiring an abstract 
understanding of how the atack works under the hood.
28
PART 3:
ADVANCEMENTS IN
SECURITY FOR AI
Before anyone can start implementing protections for 
certain technologies, the industry needs to gure out 
the ways in which these technologies are vulnerable. 
This is why ofensive security plays such a big role in 
planning the defenses. 
Ofensive Security Tooling for AI 
2020 saw the release of Armory, a containerized testing 
tool for evaluating adversarial defenses, which interfaces 
with IBMs ART. In 2021 Facebook released AugLy, a data 
augmentation library, which can be potentially used to 
generate adversarial examples. Microsof followed with 
the release of Countert, an easy\-to\-use command\-line 
automation layer for security evaluation of ML models, 
which interfaces with existing atack tools and 
frameworks, including ART, TextAtack, and AugLy, and 
resembles Metasploit in terms of commands and 
navigation.
One of the rst libraries for testing the robustness of AI 
systems against adversarial examples, called CleverHans, 
dates as far back as 2016\. In 2018, IBM released its 
Adversarial Robustness Toolbox (ART), a framework that 
implements a multitude of atacks against AI and includes 
easy\-to\-follow Jupyter Notebook examples. MLSploit, a 
user\-friendly cloud\-based framework whose name calls out 
to Metasploit, was released in 2019; it allows for the 
creation of atacks on various malware classiers, intrusion 
detectors, and object detectors. In the same year, QData 
released TextAtack, a powerful model\-agnostic NLP atack 
framework that can help perform adversarial text atacks, 
text augmentation, and model training.
They ofer various atack techniques from bypass to thef to 
code execution. Although very valuable in improving the 
security, safety, and robustness of the models, they can also 
be used by adversaries in malicious activities and make 
atacking AI more straightforward and accessible than it 
might at rst seem.
Projects such as Metasploit, Cobalt Strike, and Empire are 
now as much associated with malicious activity as they are 
with red\-teaming. The concept of ofensive security has 
also made its way to the eld of articial intelligence, where 
AI security researchers have developed various tools to test 
their atack techniques. 
There are many publicly available security evaluation tools 
designed to test AI systems.
29
PART 3: ADVANCEMENTS IN SECURITY FOR AI
Automated Atack Frameworks
Adversarial ML Frameworks
Fickling, released in 2021 by Trail of Bits, is the rst tool to 
exploit one of the most popular AI model serialization 
formats: Pythons pickle format. It contains a decompiler, 
static analyzer, and bytecode rewriter and can inject 
arbitrary code into AI models saved as pickles. Charcuterie, 
released in 2022, implements a set of atacks that utilize 
code execution techniques and deserialization exploits in 
ML models. 
Another type of adversarial tool is KnockOfNets, released 
by researchers at the Max Planck Institute for Informatics 
in 2021\. Its a tool for creating a replica of an AI model or, in 
other words, for stealing the model. It requires no previous 
knowledge of the model or the training data. The authors 
claim it can relatively accurately reproduce a model for 
$30\. Although KnockOfNets was created to showcase the 
ease of model thefmodel extraction atacks, it can also 
help adversaries build their own model thef tooling. 
In addition to robustness evaluation frameworks, there 
are also more specialized tools that aim at a specic 
outcome. MalwareGym, for example, helps bypass 
AI\-based anti\-malware solutions. Released in 2017 
anti\-virus company Endgame, it implements 
reinforcement learning in the modication of Windows 
applications. By taking features from benign executables 
and adding them to malicious ones, MalwareGym can 
create malware that bypasses malware scanners. 
Although MalwareGym is just a demo tool against one 
specic classier, it has a successor in the MalwareRL 
project, which was released in 2021 and supports atacks 
against three diferent classiers.
With new tools and techniques for atacking AI popping 
up with increasing frequency, it has become clear that a 
methodical defensive approach is needed to safeguard 
this booming technology. 
Over the last two years, several big cybersecurity players
have created comprehensive frameworks comprising 
various security practices, strategies, and 
recommendations for AI. These frameworks are incredibly 
valuable rst steps on the road long ahead.
It was developed to demonstrate the vulnerability of ML 
models against more traditional atacks, but can be used by 
script kiddies to subvert publicly available models.
30
PART 3: ADVANCEMENTS IN SECURITY FOR AI
Model Thef Tooling
Anti\-Malware Evasion Tooling
Model Deserialization Exploitation
Defensive Frameworks for AI
Defensive Frameworks
A signicant update to the matrix to ground the 
rapidly evolving atack pathways for LLMs and 
GenAI enabled systems. This update added 12 new 
techniques and 5 unique case studies to ATLAS as 
the result of a close collaboration with Microsof 
and other ATLAS community members determined 
to realistically represent these new LLM atack 
pathways.
Arsenal and Almanac plugins developed 
collaboratively with Microsof to add 
implementations of ATLAS techniques and new 
adversary proles that target AI\-enabled systems 
to CALDERA, an existing MITRE open\-source 
threat emulation tool largely leveraged by the 
cyber world.
First released in 2020 on GitHub then launched as a full 
website in 2021, MITRE ATLAS stands for Adversarial Threat 
Landscape for Articial\-Intelligence Systems. ATLAS is a 
knowledge base of adversarial machine learning tactics, 
techniques, and case studies designed to help 
cybersecurity professionals, data scientists, and their 
companies stay up to date on the latest atacks and 
defenses against adversarial machine learning. The ATLAS 
matrix is modeled afer and complementary to the MITRE 
ATT\&CK framework, which is well\-known and used in the 
cybersecurity industry to understand atack chains and 
adversary behaviors. 
The ATLAS matrix is broken down into two main 
components: Tactics and Techniques. The tactics describe 
what an adversary is trying to accomplish. For example, 
Reconnaissance to learn more about a model deployment 
or Exltration to steal the model itself. The techniques, on 
the other hand, describe how an adversary is going to 
accomplish their tactic. Taking the Reconnaissance 
example, an atacker may Search Victim\-Owned Websites 
for information about models or those internally who 
control or interact with them. 
One diference between ATLAS and its ATT\&CK counterpart 
is the source of the techniques. While ATT\&CK is based only 
on detected atacks in the wild, ATLAS uses unique case 
studies selected from their impact to production 
AI\-enabled systems. These case studies are a combination 
of both real\-world atacks discovered in the wild as well as 
realistic red\-teaming exercises from AI red teams or 
security groups. Some of these white hat hacker atacks are 
completely undetectable but have valuably demonstrated a 
realistic atack pathway that could threaten real\-world 
AI\-enabled systems. Including case studies of both 
malicious atacks and the white hat hacker atacks in 
ATLAS provides a more grounded and complete picture of 
the AI\-enabledsystem threat landscape. These case 
studies outline who atack victims are and map to various 
techniques observed within the full scope of the atack. 
In 2023, the ATLAS team released several major updates 
and new tools to continue enabling organizations that are 
working to secure their AI\-enabled systems. These releases 
included:
31
PART 3: ADVANCEMENTS IN SECURITY FOR AI
MITRE ATLAS
This survey demonstrates the prominence of 
real\-world threats on AI\-enabled systems, with 
77% of participating companies reporting 
breaches to their AI applications this year. The 
MITRE ATLAS community is dedicated to 
characterizing and mitigating these threats in 
a global alliance. We applaud our community 
collaborators who enhance our collective 
ability to anticipate, prevent, and mitigate 
risks to AI systems, including HiddenLayer and 
their latest threat report. 
 Dr. Christina Liaghati, MITRE ATLAS Lead
MITRE ATLAS Updates
An initial release of 20 new mitigations based on 
ATLAS case studies that provide high\-level 
information on the security concepts and classes 
of technologies that can be used to prevent an 
adversarial atack technique from being 
successfully executed.
In January 2023, US National Institute of Standards and 
Technology released the AI Risk Management Framework 
(AI RMF). The AI RMF is a conceptual framework that takes 
learnings from the traditional sofware and information\- 
based systems and applies them to the unique challenges 
presented by AI systems. It provides guidance for 
responsible design, development, deployment, and use of 
AI systems to give organizations additional trust in AI.
As with many other frameworks, SAIF will review traditional 
security controls around data and network level access, 
AIML specic controls such as data poisoning and 
detecting anomalies, privacy requirements and regulations, 
as well as governance around the entire lifecycle.
To date, ATLAS now has 14 Tactics, 82 Techniques, 22 Case 
Studies, and 20 Mitigations. As the ATLAS team continues 
to work with leading AI security organizations and experts 
across government and industry to expand the framework 
and its related tools and capabilities, the community\-driven 
knowledge base and tools will remain a critical grounding 
resource as we all work to beter secure our AI\-enabled 
systems and supply chain against atacks.
In 2024, the MITRE ATLAS team will continue building upon 
the existing framework, tools and capabilities to help the 
community navigate the landscape of threats to AI\-enabled 
systems by expanding on their platforms for both public 
vulnerability reporting and protected incident sharing. 
Through continued collaborations with industry, academia, 
and government, the ATLAS team is evolving open\-source 
resources like the AI Risk Database, a tool for discovering 
vulnerabilities associated with public AI models. While the 
public ATLAS website continues to publicly represent 
unique real\-world atacks, the ATLAS team is also 
continuing to expand its platform for more rapid protected 
or anonymized threat sharing within its community.
 The framework splits itself into two parts: framing the risks 
related to AI systems and the core framework itself. The 
core describes four functions: govern, map, measure, and 
manage. Each breaks down into further controls to give 
organizations greater insights securing their AI 
infrastructure.
Introduced by Google in June 2023, Secure AI Framework 
(SAIF) is a conceptual framework that, like NIST AI RMF, 
provides guidance on securing AI systems.It builds upon 
best practices and experience from traditional sofware 
development, adapting them to t the needs of AI systems. 
32
PART 3: ADVANCEMENTS IN SECURITY FOR AI
NIST AI Risk Management Framework
There are six core elements to the framework:
Google Secure AI Framework
Expand strong security foundations to the 
AI ecosystem
Extend detection and response to AI
Automate defenses to keep pace with 
existing and new threats
Harmonize platform level controls
Adapt controls and mitigations for AI 
deployment
Contextualize AI risks to match business 
processes.
The Open Worldwide Application Security Project (OWASP) 
is a non\-prot organization and online community that 
provides free guidance and resources, such as articles, 
documentation and tools in the eld of application security. 
The OWASP Top 10 lists comprise the most critical security 
risks faced by various web technologies, such as access 
control and cryptographic failures.
In 2023, OWASP released the Top 10 Machine Learning risks. 
These controls help those who are building, operating, and 
securing machine learning to identify potential risks and 
atack vectors within their deployments. Each of the 
individual controls has information on the atack vector, 
various risk factors that can help with threat modeling, and 
guidance on how to prevent the atack. When combined 
with other practical guidance from other frameworks such 
as ATLAS, this helps demystify the real threats to machine 
learning and what can be done about them. 
Another recent release from OWASP are the top 10 critical 
vulnerabilities seen in Large Language Models (LLMs). With 
the rapid recent adoption of LLM technology, risks 
associated with deploying LLMs have been proliferating (as 
discussed in section 2\). This OWASP document covers 
items such as prompt injection, output handling, all the way 
to model thef of the LLM itself. Each section also ofers 
practical guidance for using this technology in a 
responsible and secure manner. 
Gartner dened a framework to address concerns around 
AI and ML systems, called AI TRiSM. It covers challenges 
such as bias, privacy, and explainability while also touching 
on the security and risks of such systems. This provides a 
roadmap for organizations to build AIML systems that 
maintain trust, are reliable and fair, and secure by design.
Within these components, Databricks identied 54 
technical security risks. Their recommendations are based 
on the real\-world evidence that adversaries compromise 
unsecured AI systems using simple tactics.
The DAISF framework adopts a comprehensive strategy to 
mitigate cyber risks in AI systems. It provides insights into 
how ML impacts system security and how to apply security 
engineering principles to AI systems. It also ofers a detailed 
guide for understanding the security and compliance of 
specic ML systems. 
OWASP Top 10
Gartner AI Trust, Risk, and Security 
Management (AI TRiSM)
Databricks AI Security Framework 
(DAISF)
Actionable defense recommendations apply to 
12 foundational components of a generic 
data\-centric AI system:
33
PART 3: ADVANCEMENTS IN SECURITY FOR AI
raw data
data preparation
datasets
data and AI governance
machine learning algorithms
evaluation
machine learning models
model management
model serving and inference
inference response
machine learning operations
data and AI platform security
In January 2024, IBM released their Framework for Securing 
Generative AI, focused on the use of LLMs and other GenAI 
solutions in businesses and organizations. It provides 
defensive approaches by helping to estimate the most likely 
atack that can occur at each stage of the pipeline, and 
suggesting relevant safeguards and defenses.
First ideas of AI red teaming emerged in the late 2010s. At 
that point, AI systems were already known for their 
vulnerability to things like bias, adversarial examples, and 
general abuse. Even though, now, theres widespread 
acceptance that AI will dene this decade, it's still mostly 
the major players \- such as Google, NVIDIA, or Microsof \- 
who invest in building their own internally\-focused teams 
dedicated to pentesting the AI solutions they develop and 
implement.
IBM Framework for Securing 
Generative AI
IBMs framework consists of ve steps:
Red Teaming and Risk Assessment
It would be unfair to mention these companies 
by name and not highlight some of the 
incredible work they have done to bring light to 
the security of AI systems: 
34
PART 3: ADVANCEMENTS IN SECURITY FOR AI
14%
Securing the data: describes risks related 
to the data collection and processing 
phase, such as mishandling PII and privacy 
concerns
Securing the model: deals with atacks 
that can occur during model development 
and training, including supply chain 
atacks, API atacks, and LLM exploitation;
Securing the usage: relates to the live use 
of model in production and covers 
inference atacks, including prompt 
injection and model thef
Securing the infrastructure: tapping into 
existing expertise to optimize and harden 
network security, access control, data 
encryption, and intrusion detection and 
prevention
Establishing governance: puting 
guardrails in place that ensures AI systems 
dont stray from what they are intended to 
do and act as expected.
In December 2021, Microsof published 
their Best practices for AI security risk 
management
In June 2023, NVIDIA introduced their red 
team to the world alongside the 
framework they use as the foundation for 
their assessments
In July 2023, Google announced their own 
AI red team following the release of their 
Secure AI Framework (SAIF).
of IT leaders say their company are 
planning and testing for adversarial 
atacks on AI models
On a national level, several countries have started 
introducing AI\-specic legislations. Singapore's Model AI 
Governance Framework, whose rst edition dates back to 
2019, consists of 11 AI ethics principles, including 
transparency, explainability, safety, security, data 
governance, and accountability. Canadas Digital Charter 
Implementation Act (Bill C\-27\), dated June 2022, 
encompasses the Articial Intelligence and Data Act (AIDA) 
, which addresses the responsible adoption of AI. The UK is 
currently eshing out its Articial Intelligence (Regulation) 
Bill, whose purpose is to make provisions for the regulation 
of articial intelligence. 
In October 2022, the US introduced the Blueprint for an AI 
Bill of Rights, a set of suggestions and guidelines 
concerning the development and use of AI systems. A year 
afer, in October 2023, the US White House issued an 
executive order on the safe, secure, and trustworthy 
development and use of articial intelligence. The order 
sets standards for AI safety and security. It outlines risks AI 
systems pose, such as threat to human safety, detection of 
AI generated content, as well as securing the AI ecosystem. 
There are also orders on protecting privacy for citizens from 
data collection and storage to eliminate bias and 
discrimination in machine learning models. Finally, the 
order also aims to promote innovation and competition for 
those looking to advance and secure AI systems. The 
executive order mentions the NIST AI RMF multiple times, 
which will likely be a framework organizations can leverage 
to guide the secure development and deployment of AI 
systems.
We've already discussed how AI is a double\-edged sword: it 
can be easily turned against people, businesses, and 
societies, with far\-reaching consequences that could prove 
devastating. For this reason, it is imperative for 
governments around the world to introduce tight 
regulations on how AI can be used safely, legally, and 
ethically.
The rst regulations around the use of AI were 
implemented as part of the European Union's General Data 
Protection Regulation (GDPR). These were very limited in 
scope and related mainly to the need for certain AI systems 
to be explainable. An AI model is explainable only if its 
possible for us, humans, to assess why the model returned 
a specic prediction. This is important in all applications 
that make critical decisions, or decisions that can have an 
impact on people.
In 2019, the Organization for Economic Co\-operation and 
Development (OECD) adopted the Recommendation on 
Articial Intelligence (the OECD AI Principles). It describes 
ve principles and ve recommendations for OECD 
countries and adhering partner economies to promote 
responsible and trustworthy AI policies.
In 2022, the EU proposed a more comprehensive AI Act
that groups AI solutions into three categories: low\-risk 
applications that have to adhere to transparency laws but 
are otherwise unregulated; high\-risk applications that are 
subject to strict limitations; and applications that are 
deemed dangerous and are outright banned. A provisional 
agreement between the EU Council presidency and the 
European Parliament was reached on this proposal in 
December 2023\. It's expected to become law soon. 
Policies and Regulations
35
PART 3: ADVANCEMENTS IN SECURITY FOR AI
The cybersecurity industry has been in a technological arms race with adversaries for several decades, as each new 
advancement brings unique security concerns that require bespoke security solutions. However, AIML security has been 
overlooked in the data science world; rapid advances in AI and ML ofen lack even basic security controls. This has led to 
many vulnerabilities in libraries and tooling that have become pillars of AI sofware development. We expect this trend to 
reverse slightly over the coming year, as researchers work rapidly to uncover vulnerabilities and help shore up defenses in 
the open\-source ML projects. The emerging collaboration between data scientists and cybersecurity specialists will boost 
the security of the whole AI ecosystem.
Due to inherent insecurities in the machine learning tool chain, there are many low hanging fruits for cybercriminals to 
exploit. Threat actors are increasingly turning their sights towards MLOps platforms and tooling. Look for supply chain 
atacks to become more common as the year progresses, and not just for traditional initial compromise and lateral 
movement purposes. The ofen sensitive nature of ML models and the data they touch makes them very atractive to 
cybercriminals. Atackers will increasingly leverage vulnerabilities in MLOps platforms to poison training sets and exltrate 
sensitive data used at train or inference time to gain a competitive advantage or abuse AI systems.
36
PART 4:
PREDICTIONS AND
RECOMMENDATIONS
Its always fun to dust of the crystal ball and try to 
predict future trends in cybersecurity. AI has been the 
dominant factor in many threat reports from 
traditional cybersecurity vendors this year. While 
most focus on generative AI, we take a broader look 
at the AI ecosystem and predict how it may be abused 
by cybercriminals, nation\-states, and general bad 
actors over the coming year.
1\. Data scientists will partner with security practitioners to secure their models
1\. Supply chain atacks using ML artifacts will become much more common
Predictions for the next 12 months 
Inversion atacks to infer training data or model details, inference atacks to generate bypassesmisclassications, and, 
ultimately, model thef atacks will also become much more common. All these atack techniques will be driven by 
ever\-expanding research into adversarial ML by academia and industry which is being made available through easy\-to\-use 
open\-source sofware. What was once a complex undertaking is and will continue to become increasingly simple for 
mere script kiddies to implement.
Generative AI is where we expect to nd the most signicant can of worms. Cybercriminals already use LLMs to enhance 
existing atacks, from authoring more realistic phishing emails to generating unique malware payloads on the y and 
improving social engineering eforts. Its not a stretch to envisage threat actors harnessing LLMs to automate hacking 
eforts, perform reconnaissance, and supplement cybercrime\-as\-a\-service over the coming year. 
In addition, as LLMs evolve from text generation to multimodal systems capable of producing text, images, and audio, we 
expect a sharp increase in political activists and those trying to inuence society using disinformation. 
Another interesting development in the world of LLMs is RAG, Retrieval\-Augmented Generation, which enhances the model 
with external sources of information or ground truths. RAG\-empowered LLMs will be ripe for abuse by atackers, who will 
seek to leak sensitive information using carefully crafed prompts, especially if trained on corporate data.
Armed with powerful tools that can generate almost impeccable video and audio, adversaries are poised to become much 
more successful in their atempts at deceiving people, be it for the purpose of defrauding money, extracting sensitive 
information, or spreading fake news. The traditional scam scenario \- in which the atacker sends a message pretending to be 
a relative who lost their phone and needs money \- is now acquiring a whole new dimension. Instead of text\-based messages, 
cybercriminals will be shifing to deepfake audio and video calls, and these can prove challenging not to fall for.
The bigger the digital footprint a person leaves behind, the more realistic a deepfake instance of this person can be. 
Naturally, public gures such as artists, inuencers and politicians will be both the most enticing and vulnerable targets. 
However, it can take as litle as just a few photos to create a deepfake convincing enough to trick a non savvy person into 
giving away money or information, and cybercriminals will look to cash in on low prole targets as well.
As the political climate deteriorates and tensions grow between nations, state\-sponsored adversaries will use carefully 
curated deepfakes to steer public opinion, manipulate political campaigns and disturb elections. Conspiracy theories will 
have a wider reach and fake news will become increasingly difcult to disprove. Even if we nd a way to reliably tell authentic 
videos from fakes it might not help limiting the damage. Once manipulated, people ofen refuse to acknowledge facts or 
accept the truth. The best solution to prevent deepfake\-induced harm is to prevent the proliferation of deepfakes 
themselves.
37
PART 4: PREDICTIONS AND RECOMMENDATIONS
1\. There will be a signicant increase in adversarial atacks against AI
1\. Threat actors will automate hacking eforts with LLMs
1\. Deepfakes will be increasingly used in scam and disinformation 
It has never been easier to develop, use, and implement AI within organizations This rapid integration into established 
processes is introducing an ever\-expanding novel atack surface that is not protected by conventional security controls. 
Businesses will experience many growing pains this coming year, where AI is exposed or congured insecurely, leading to 
data breaches, compromise, or worse. 
On the ipside, we also expect to see more widespread adoption of AI security principles across organizations, and 
democratization of advanced methods of monitoring model behavior and model security evaluation, which have been 
typically reserved for major enterprises. As a result, many more organizations will be able to identify and take actions against 
adversarial atacks. 
Understanding and implementing extensive security 
measures for AI is no longer a choice. Its a necessity. Too 
much is at risk for organizations, government, and society 
at large. Security must maintain pace with AI to allow 
innovation to ourish. That is why it is imperative to 
safeguard your most valuable assets, from development to 
operation and everything in between. 
But how should you get started?
Let this guide be a starting point to securing your AI 
systems. Whether youre a developer, data scientist, or an IT 
professional, ensuring your AI systems are secure will 
empower you and your organization to navigate the future 
condently. 
Conduct a benet assessment to identify the 
potential negative consequences associated with 
the AI systems if those models were to be 
compromised in any way.Perform threat modeling to understand the 
potential vulnerabilities and atack vectors that 
could be exploited by malicious actors to complete 
your understanding of your organizations AI risk 
exposure
Begin by identifying where AI is already used in 
your organization. What applications has your 
organization already purchased that use AI or have 
AI\-enabled features?Evaluate what AI may be under development by 
your organization. How many data scientists or 
data engineers roles are you employing? How 
many are you hiring? How many are consultants?
Understand what pretrained models from public 
repositories may already be in use. Do you know 
what websites ofer pre\-trained models? Do you 
understand the networkweb trafc to these sites 
and who may have already downloaded these 
models?6\. AI atack surfaces will expand while more organizations 
use advanced tools to combat threats
38
Securing Your AI: Geting Started
93%
of IT leaders say they have 
implemented security for 
AI protocols, but
58%
arent sure these protocols 
are keeping pace with 
evolving threats.
PART 4: PREDICTIONS AND RECOMMENDATIONS
1\. Discovery and Asset Management
2\.Risk Assessment and Threat Modeling
Identify the AI security architecture required to be 
instrumented for the runtime protection of your AI 
when the models go into production use.
Only by answering these questions with data\-driven, 
intellectual honesty, can you maintain the integrity of your 
security role and the critical function it provides.
Regularly assess the robustness of AI models 
against adversarial atacks. This involves 
pen\-testing the model's response to various 
atacks such as intentionally manipulated inputs.
Implement model validation techniques to ensure 
the AI system behaves predictably and reliably in 
real\-world scenarios. This will help minimize the 
risk of unintended consequences.
Go beyond the typical implementation of 
encryption, access controls, and secure data 
storage practices to protect your AI model data. 
Those controls will not efectively protect the data 
in your models from thef, alteration, or other 
forms of atack. Evaluate and implement security 
solutions that are purpose\-built to provide runtime 
protection for AI models. Look for solutions that 
can span the vast array of le types, model types, 
and also be agnostic to on\-prem or cloud 
deployments.
Embed into your 3rd\-party risk process an 
evaluation of your vendors' security for their AI 
capabilities. Ask how your vendors incorporate 
security into their AI development lifecycle, 
including how they scan their models for data 
poisoning and malicious executables. Find out how 
they provide real\-timerun time protection to 
detect and stop various forms of atacks against 
the AI capabilities embedded in the solutions you 
bought from them.
Remember that the security landscape as well as AI 
technology are dynamic and rapidly changing. It's crucial 
to stay informed about emerging threats and best practices. 
Regularly update and rene your AI\-specic security 
program to address new challenges and vulnerabilities.
And a note of caution. Responsible and ethical AI 
frameworks in many cases fall short of ensuring models 
are secure before they go into production, as well as afer 
an AI system is in use. They focus on things such as biases, 
appropriate use, and privacy.While these are also 
required, dont confuse these practices for security.
Implement continuous monitoring mechanisms to 
detect anomalies and potential security incidents 
in real\-time for your AI. Require your vendors to 
utilize AI in their solutions to alert you to atacks 
that could compromise your data or business 
processes.
Develop a robust AI incident response plan to 
quickly and efectively address security breaches 
or anomalies. Regularly test and update the 
incident response plan to adapt to evolving AI 
threats.
Incorporate security into your AI development 
lifecycle. Train your data scientists, data engineers, 
and developers on the various atack vectors 
associated with AI. Make sure to include how to 
minimize potential atack surface early in the 
security development lifecycle.
4\.Model Robustness and Validation
39
5\.Secure Development Practices
The nal recommendation: Always ask yourself 
the following questions:
PART 4: PREDICTIONS AND RECOMMENDATIONS
3\.Data Security and Privacy
6\.Continuous Monitoring and Incident Response
What am I doing to secure my 
organization's use of AI?Is it enough? 
How do I know?
40
HiddenLayer Model Scanner
Learn More
Learn More
Learn More
Learn More
HiddenLayer Professional Services
RESOURCES
Resources
HiddenLayer Products and Services
HiddenLayer AISec Platform
HiddenLayer Machine Learning Detection \& Response (MLDR)
is a comprehensive AI security solution that ensures the integrity and safety 
of your models throughout the MLOps pipeline. By evaluating the security of 
pretrained models, detecting malicious injections, and monitoring algorithm 
inputs and outputs for potential abuse, the AISec Platform delivers an 
automated and scalable defense tailored for AI. 
complements your existing security stack, enabling you to automate and scale the 
protection of AI models and ensure their security in real\-time. With MLDR 
integrated into your MLOps lifecycle and SIEM tools, you can proactively defend 
against threats to AI.
enables you to evaluate security and integrity of your ML artifacts before 
deploying them. This mitigates the risk of supply chain atacks through hijacked 
or backdoored models. With the Model Scanner, you can identify and remediate 
potential risks ensuring a safe and trusted environment.
leverage deep domain expertise in cybersecurity and apply it to the eld of AI. 
Our Adversarial Machine Learning Research (AMLR) team is equipped with a 
unique skill set that encompasses machine learning, reverse engineering, digital 
forensics and threat intelligence. We tailor our eforts to empower your data 
science and cybersecurity teams with the knowledge, insight, and tools needed 
to protect and maximize your AI investments.
WHAT IS A MACHINE LEARNING MODEL
41
RESOURCES
AN INTRODUCTION TO HIDDENLAYER
Get to Know HiddenLayer
AN INTRODUCTION TO AI AND HOW TO PROTECT IT
AISEC PLATFORM OVERVIEW
GLOBAL FINANCIAL SERVICES CASE STUDY
Read
HiddenLayer \& Intel eBook: The Future of Risk is Upon Us
Forrester Opportunity Snapshot: Its Time for Zero Trust
HiddenLayer Research
Learn about HiddenLayers origin story and what we are all about.
Get a basic understanding of what Articial Intelligence is and the pain points 
that exist in protecting it.
Dive deeper into what exactly a machine learning model is, and select use cases 
across industries.
Receive a high\-level overview of HiddenLayers AISec Platform. Learn more 
about what the platform provides as well as problems it helps solve. 
Explore a tangible customer case study that shows how HiddenLayer helped a 
top global nancial services company minimize customer experience issues 
while combating fraud. 
Companies cant adopt a zero\-trust security posture without securing AI. Learn 
how to successfully navigate AI adoption and prevent malicious atacks.
See how to take charge of AI security condently, stay ahead of threat actors, 
and enable faster adoption of AI within your products and organization overall.
42
The Tactics and Techniques of Adversarial ML
Weaponizing Machine Learning Modelswith Ransomware
Insane in the Supply Chain
The Dark Side of Large Language Models
Not So Clear: How MLOps Solutions Can Muddythe Waters of 
Your Supply Chain
RESOURCES
Securing AI: A Guide for SecOps
Read this comprehensive overview of the key considerations, risks, and best 
practices that should be taken into account when securing AI deployments 
within their organizations.
Dive deeper into the details of adversarial atacks.
See how easily an adversary can deploy malware through a pre\-trained ML 
model with a destructive impact on an organization.
Understand the scope of your potential exposure through your supply chain risk 
management, as well as similarly afected technologies involved in machine 
learning and their varying levels of risk. 
Learn more about the perils surrounding the use \- and abuse \- of generative AI.
This technical report publicly discloses six Zero\-Day vulnerabilities in a 
well\-known and widely used MLOps platform and demonstrates how the 
vulnerabilities can be combined to create a full atack chain against 
real\-world systems.
Silent Sabotage: Hijacking Safetensors conversion on Hugging Face
Learn how an atacker could compromise the Hugging Face Safetensors 
conversion space and its associated service bot.
HiddenLayer, a Gartner recognized AI Application Security company, 
provides security solutions for articial intelligence algorithms, models, and 
the data that power them. With a rst\-of\-its\-kind, non\-invasive sofware 
approach to observing and securing AI, HiddenLayer is helping to protect 
the worlds most valuable technologies.
HiddenLayer was founded by AI professionals and security specialists with 
rst\-hand experience of how difcult adversarial AI atacks can be to detect 
and defend against. Determined to prove these atacks are preventable, the 
team developed a unique, patent\-pending, productized AI solution to help all 
organizations protect important technology.
Authors \& Contributors:
A special thank you to the teams that made this report come to life:
Marta Janus, Principal Security Researcher
Eoin Wickens, Technical Research Director
Tom Bonner, VP of Research
Andrew Davis, Chief Data Scientist
Sam Pearcy, GTM Specialist
Malcolm Harkins, Chief Security \& Trust Ofcer
Travis Smith, VP, ML Threat Operations
Christina Liaghati, PhD, AI Strategy Execution \& Operations Manager at MITRE
43
www.hiddenlayer.com 
Learn more:
htps:hiddenlayer.combook\-a\-demo
Request a Demo:
Research
Twiter
LinkedIn
Follow us: 
About HiddenLayer
ABOUT HIDDENLAYER