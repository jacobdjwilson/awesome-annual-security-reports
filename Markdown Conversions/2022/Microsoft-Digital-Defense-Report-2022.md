# Microsoft Digital Defense Report 2022

Illuminating the threat landscape and empowering a digital defense.

## Contents

The data, insights, and events in this report are from July 2021 through June 2022 (Microsoft fiscal year 2022), unless otherwise noted.

[Report Introduction](#report-introduction) 02
[The State of Cybercrime](#the-state-of-cybercrime) 06

### An overview of The State of Cybercrime
07
[Introduction](#introduction) 08
[Ransomware and extortion: A nation-level threat](#ransomware-and-extortion-a-nation-level-threat) 09
[Ransomware insights from front-line responders](#ransomware-insights-from-front-line-responders) 14
[Cybercrime as a service](#cybercrime-as-a-service) 18
[The evolving phishing threat landscape](#the-evolving-phishing-threat-landscape) 21
[A timeline of botnet disruption from Microsoft’s early days of collaboration](#a-timeline-of-botnet-disruption-from-microsofts-early-days-of-collaboration) 25
[Cybercriminal abuse of infrastructure](#cybercriminal-abuse-of-infrastructure) 26
[Is hacktivism here to stay?](#is-hacktivism-here-to-stay) 28

[Nation State Threats](#nation-state-threats) 30

### An overview of Nation State Threats
31
[Introduction](#introduction-1) 32
[Background on nation state data](#background-on-nation-state-data) 33
[Sample of nation state actors and their activities](#sample-of-nation-state-actors-and-their-activities) 34
[The evolving threat landscape](#the-evolving-threat-landscape-1) 35
[The IT supply chain as a gateway to the digital ecosystem](#the-it-supply-chain-as-a-gateway-to-the-digital-ecosystem) 37
[Rapid vulnerability exploitation](#rapid-vulnerability-exploitation) 39
[Russian state actors’ wartime cyber tactics threaten Ukraine and beyond](#russian-state-actors-wartime-cyber-tactics-threaten-ukraine-and-beyond) 41
[China expanding global targeting for competitive advantage](#china-expanding-global-targeting-for-competitive-advantage) 44
[Iran growing increasingly aggressive following power transition](#iran-growing-increasingly-aggressive-following-power-transition) 46
[North Korean cyber capabilities employed to achieve regime’s three main goals](#north-korean-cyber-capabilities-employed-to-achieve-regimes-three-main-goals) 49
[Cyber mercenaries threaten the stability of cyberspace](#cyber-mercenaries-threaten-the-stability-of-cyberspace) 52
[Operationalizing cybersecurity norms for peace and security in cyberspace](#operationalizing-cybersecurity-norms-for-peace-and-security-in-cyberspace) 53

[Devices and Infrastructure](#devices-and-infrastructure) 56

### An overview of Devices and Infrastructure
57
[Introduction](#introduction-2) 58
[Governments acting to improve critical infrastructure security and resilience](#governments-acting-to-improve-critical-infrastructure-security-and-resilience) 59
[IoT and OT exposed: Trends and attacks](#iot-and-ot-exposed-trends-and-attacks) 62
[Supply chain and firmware hacking](#supply-chain-and-firmware-hacking) 65
[Spotlight on firmware vulnerabilities](#spotlight-on-firmware-vulnerabilities) 66
[Reconnaissance-based OT attacks](#reconnaissance-based-ot-attacks) 68

[Cyber Influence Operations](#cyber-influence-operations) 71

### An overview of Cyber Influence Operations
72
[Introduction](#introduction-3) 73
[Trends in cyber influence operations](#trends-in-cyber-influence-operations) 74
[Influence operations during the COVID-19 pandemic and Russia’s invasion of Ukraine](#influence-operations-during-the-covid-19-pandemic-and-russias-invasion-of-ukraine) 76
[Tracking the Russian Propaganda Index](#tracking-the-russian-propaganda-index) 78
[Synthetic media](#synthetic-media) 80
[A holistic approach to protect against cyber influence operations](#a-holistic-approach-to-protect-against-cyber-influence-operations) 83

[Cyber Resilience](#cyber-resilience) 86

### An overview of Cyber Resilience
87
[Introduction](#introduction-4) 88
[Cyber resiliency: A crucial foundation of a connected society](#cyber-resiliency-a-crucial-foundation-of-a-connected-society) 89
[The importance of modernizing systems and architecture](#the-importance-of-modernizing-systems-and-architecture) 90
[Basic security posture is a determining factor in advanced solution effectiveness](#basic-security-posture-is-a-determining-factor-in-advanced-solution-effectiveness) 92
[Maintaining identity health is fundamental to organizational well-being](#maintaining-identity-health-is-fundamental-to-organizational-well-being) 93
[Operating system default security settings](#operating-system-default-security-settings) 96
[Software supply chain centrality](#software-supply-chain-centrality) 97
[Building resilience to emerging DDoS, web application, and network attacks](#building-resilience-to-emerging-ddos-web-application-and-network-attacks) 98
[Developing a balanced approach to data security and cyber resiliency](#developing-a-balanced-approach-to-data-security-and-cyber-resiliency) 101
[Resilience to cyber influence operations: The human dimension](#resilience-to-cyber-influence-operations-the-human-dimension) 102
[Fortifying the human factor with skilling](#fortifying-the-human-factor-with-skilling) 103
[Insights from our ransomware elimination program](#insights-from-our-ransomware-elimination-program) 104
[Act now on quantum security implications](#act-now-on-quantum-security-implications) 105
[Integrating business, security, and IT for greater resilience](#integrating-business-security-and-it-for-greater-resilience) 106
[The cyber resilience bell curve](#the-cyber-resilience-bell-curve) 108

[Contributing Teams](#contributing-teams) 110

For the best experience viewing and navigating this report, we recommend using Adobe Reader, available as a free download from the Adobe website.

01
Microsoft Digital Defense Report 2022

## Report Introduction

### Introduction by Tom Burt
Corporate Vice President, Customer Security & Trust

> “The trillions of signals we analyze from our worldwide ecosystem of products and services reveal the ferocity, scope, and scale of digital threats across the globe”

A snapshot of our landscape…

**Scope and scale of threat landscape**
The volume of password attacks has risen to an estimated 921 attacks every second – a 74% increase in just one year.

**Dismantling cybercrime**
To date, Microsoft removed more than 10,000 domains used by cybercriminals and 600 used by nation state actors.

**Addressing vulnerabilities**
93% of our ransomware incident response engagements revealed insufficient controls on privilege access and lateral movement.

On February 23, 2022, the cybersecurity world entered a new age, the age of the hybrid war.
On that day, hours before missiles were launched and tanks rolled across borders, Russian actors launched a massive destructive cyberattack against Ukrainian government, technology, and financial sector targets. You can read more about these attacks and the lessons to be learned from them in the Nation State Threats chapter of this third annual edition of the Microsoft Digital Defense Report (MDDR). Key among those lessons is that the cloud provides the best physical and logical security against cyberattacks and enables advances in threat intelligence and end point protection that have proven their value in Ukraine.

While any survey of the year’s developments in cybersecurity must begin there, this year’s report provides a deep dive into much more. In the report’s first chapter, we focus on activities of cybercriminals, followed by nation state threats in chapter two. Both groups have greatly increased the sophistication of their attacks which has dramatically increased the impact of their actions. While Russia drove headlines, Iranian actors escalated their attacks following a transition of presidential power, launching destructive attacks targeting Israel, and ransomware and hack-and-leak operations targeting critical infrastructure in the United States. China also increased its espionage efforts in Southeast Asia and elsewhere in the global south, seeking to counter US influence and steal critical data and information.

Foreign actors are also using highly effective techniques to enable propaganda influence operations in regions around the globe, as covered in the third chapter. For example, Russia has worked hard to convince its citizens, and the citizens of many other countries, that its invasion of Ukraine was justified – while also sowing propaganda discrediting COVID vaccines in the West and simultaneously promoting their effectiveness at home.

In addition, actors are increasingly targeting Internet of Things (IoT) devices or Operational Technology (OT) control devices as entry points to networks and critical infrastructure which is discussed in chapter four. Finally, in the last chapter, we provide the insights and lessons we have learned from over the past year defending against attacks directed at Microsoft and our customers as we review the year’s developments in cyber resilience.

Each chapter provides the key lessons learned and insights based on Microsoft’s unique vantage point. The trillions of signals we analyze from our worldwide ecosystem of products and services reveal the ferocity, scope, and scale of digital threats across the globe. Microsoft is taking action to defend our customers and the digital ecosystem against these threats, and you can read about our technology that identifies and blocks billions of phishing attempts, identity thefts, and other threats to our customers.

### Introduction by Tom Burt Continued

We also use legal and technical means to seize and shut down infrastructure used by cybercriminals and nation state actors and notify customers when they are being threatened or attacked by a nation state actor. We work to develop increasingly effective features and services that use AI/ML technology to identify and block cyber threats and security professionals defend against and identify cyber-intrusions more rapidly and effectively.

Perhaps most importantly, throughout the MDDR we offer our best advice on the steps individuals, organizations, and enterprises can take to defend against these increasing digital threats. Adopting good cyber hygiene practices is the best defense and can significantly reduce the risk of cyberattacks.

**The state of cybercrime**
Cybercriminals continue to act as sophisticated profit enterprises. Attackers are adapting and finding new ways to implement their techniques, increasing the complexity of how and where they host campaign operation infrastructure. At the same time, cybercriminals are becoming more frugal. To lower their overhead and boost the appearance of legitimacy, attackers are compromising business networks and devices to host phishing campaigns, malware, or even use their computing power to mine cryptocurrency.
Find out more on p6

> “The advent of cyberweapon deployment in the hybrid war in Ukraine is the dawn of a new age of conflict.”

**Nation state threats**
Nation state actors are launching increasingly sophisticated cyberattacks designed to evade detection and further their strategic priorities. The advent of cyberweapon deployment in the hybrid war in Ukraine is the dawn of a new age of conflict. Russia has also supported its war with information influence operations, using propaganda to impact opinions in Russia, Ukraine, and globally. Outside Ukraine, nation state actors have increased activity and have begun using advancements in automation, cloud infrastructure, and remote access technologies to attack a wider set of targets. Corporate IT supply chains that enable access to ultimate targets were frequently attacked. Cybersecurity hygiene became even more critical as actors rapidly exploited unpatched vulnerabilities, used both sophisticated and brute force techniques to steal credentials, and obfuscated their operations by using opensource or legitimate software. In addition, Iran joins Russia in the use of destructive cyberweapons, including ransomware, as a staple of their attacks.

These developments require urgent adoption of a consistent, global framework that prioritizes human rights and protects people from reckless state behavior online. All nations must work together to implement norms and rules for responsible state conduct.
Find out more on p30

**Devices and infrastructure**
The pandemic, coupled with rapid adoption of internet-facing devices of all kinds as a component of accelerating digital transformation, has greatly increased the attack surface of our digital world. As a result, cybercriminals and nation states are quickly taking advantage. While the security of IT hardware and software has strengthened in recent years, the security of IoT and OT devices security has not kept pace. Threat actors are exploiting these devices to establish access on networks and enable lateral movement, to establish a foothold in a supply chain, or to disrupt the target organization’s OT operations.
Find out more on p56

### Introduction by Tom Burt Continued

**Cyber influence operations**
Nation states are increasingly using sophisticated influence operations to distribute propaganda and impact public opinion both domestically and internationally. These campaigns erode trust, increase polarization, and threaten democratic processes. Skilled Advanced Persistent Manipulator actors are using traditional media together with internet and social media to vastly increase the scope, scale, and efficiency of their campaigns, and the outsized impact they are having in the global information ecosystem.

In the past year, we have seen these operations used as part of Russia’s hybrid war in Ukraine, but have also seen Russia and other nations, including China and Iran, increasingly deploy propaganda operations powered by social media to extend their global influence on a range of issues.
Find out more on p71

**Cyber resilience**
Security is a key enabler of technological success. Innovation and enhanced productivity can only be achieved by introducing security measures that make organizations as resilient as possible against modern attacks. The pandemic has challenged us at Microsoft to pivot our security practices and technologies to protect our employees wherever they work. This past year, threat actors continued to take advantage of vulnerabilities exposed during the pandemic and the shift to a hybrid work environment. Since then, our principal challenge has been managing the prevalence and complexity of various attack methods and increased nation state activity. In this chapter, we detail the challenges we have faced, and the defenses we have mobilized in response with our more than 15,000 partners.
Find out more on p86

**Our unique vantage point**
*   **43tn** signals synthesized daily, using sophisticated data analytics and AI algorithms to understand and protect against digital threats and criminal cyberactivity.
*   **8,500+** engineers, researchers, data scientists, cybersecurity experts, threat hunters, geopolitical analysts, investigators, and frontline responders across 77 countries.
*   **15,000+** partners in our security ecosystem who increase cyber resilience for our customers.
*   **37bn** email threats blocked
*   **34.7bn** identity threats blocked
*   **2.5bn** endpoint signals analyzed daily

July 1, 2021 through June 30, 2022

### Introduction by Tom Burt Continued

We believe Microsoft—independently and through close partnerships with others in private industry, government, and civil society—has a responsibility to protect the digital systems that underpin the social fabric of our society and promote safe, secure computing environments for every person, wherever they are located. This responsibility is the reason we have published the MDDR each year since 2020. The report is the culmination of Microsoft’s vast data and comprehensive research. It shares our unique insights on how the digital threat landscape is evolving and the crucial actions that can be taken today to improve the security of the ecosystem.

We hope to instill a sense of urgency, so readers take immediate action based on the data and insights we present both here and in our many cybersecurity publications throughout the year. As we consider the gravity of the threat to the digital landscape—and its translation into the physical world—it is important to remember that we are all empowered to take action to protect ourselves, our organizations, and enterprises against digital threats.

> Thank you for taking the time to review this year’s Microsoft Digital Defense Report. We hope you will find that it provides valuable insight and recommendations to help us collectively defend the digital ecosystem.
>
> Tom Burt
> Corporate Vice President, Customer Security & Trust

Our objective with this report is twofold:

1.  To illuminate the evolving digital threat landscape for our customers, partners, and stakeholders spanning the broader ecosystem, shining a light on both new cyberattacks and evolving trends in historically persistent threats.
2.  To empower our customers and partners to improve their cyber resiliency and respond to these threats.

## The State of Cybercrime

As cyber defenses improve and more organizations are taking a proactive approach to prevention, attackers are adapting their techniques.

### An overview of The State of Cybercrime

Cybercriminals continue to act as sophisticated profit enterprises. Attackers are adapting and finding new ways to implement their techniques, increasing the complexity of how and where they host campaign operation infrastructure. At the same time, cybercriminals are becoming more frugal. To lower their overhead and boost the appearance of legitimacy, attackers are compromising business networks and devices to host phishing campaigns, malware, or even use their computing power to mine cryptocurrency.

*   Cybercrime continues to rise as the industrialization of the cybercrime economy lowers the skill barrier to entry by providing greater access to tools and infrastructure.
    Find out more on p18
*   The threat of ransomware and extortion is becoming more audacious with attacks targeting governments, businesses, and critical infrastructure.
    Find out more on p9
*   Attackers increasingly threaten to disclose sensitive data to encourage ransom payments.
    Find out more on p10
*   Human operated ransomware is most prevalent, as one-third of targets are successfully compromised by criminals using these attacks and 5% of those are ransomed.
    Find out more on p9
*   The most effective defense against ransomware includes multifactor authentication, frequent security patches, and Zero Trust principles across network architecture.
    Find out more on p13
*   Credential phishing schemes which indiscriminately target all inboxes are on the rise and business email compromise, including invoice fraud, poses a significant cybercrime risk for enterprises.
    Find out more on p21
*   To disrupt the malicious infrastructures of cybercriminals and nation state actors, Microsoft relies on innovative legal approaches and our public and private partnerships.
    Find out more on p25

### Introduction

Cybercrime continues to rise, with increases in both random and targeted attacks.

As cyber defenses improve and more governments and businesses take a proactive approach to prevention, we see attackers using two strategies to gain access required to facilitate cybercrime. One approach is a campaign with broad targets that relies on volume. The other uses surveillance and more selective targeting to increase the rate of return. Even when revenue generation is not the objective—such as nation state activity for geopolitical purposes—both random and targeted attacks are used. This past year, cybercriminals continued to rely on social engineering and exploitation of topical issues to maximize the success of campaigns.

For example, while COVID-themed phishing lures were used less frequently, we observed lures soliciting donations to support the citizens of Ukraine increasing.

Attackers are adapting and finding new ways to implement their techniques, increasing the complexity of how and where they host campaign operation infrastructure. We have observed cybercriminals becoming more frugal and attackers are no longer paying for technology. To lower their overhead and boost the appearance of legitimacy, some attackers increasingly seek to compromise businesses to host phishing campaigns, malware, or even use their computing power to mine cryptocurrency.

In this chapter, we also examine the rise in hacktivism, a disruption caused by private citizens conducting cyberattacks to further social or political goals. Thousands of individuals around the world, both experts and novices, have mobilized since February 2022 to launch attacks such as disabling websites and leaking stolen data as part of the Russia-Ukraine war. It is too soon to predict whether this trend will continue after the end of active hostilities.

Organizations must regularly review and strengthen access controls and implement security strategies to defend against cyberattacks. However, that is not all they can do. We explain how our Digital Crimes Unit (DCU) has used civil cases to seize malicious infrastructure used by cybercriminals and nation state actors. We must fight this threat together through both public and private partnerships.

We hope that by sharing what we have learned over the past 10 years, we will help others understand and consider the proactive measures they can take to protect themselves and the wider ecosystem against the continually growing threat of cybercrime.

Amy Hogan-Burney
General Manager, Digital Crimes Unit

**Factors**
Low barrier to entry
p15

### Ransomware and extortion: A nation-level threat

Ransomware attacks pose an increased danger to all individuals as critical infrastructure, businesses of all sizes, and state and local governments are targeted by criminals leveraging a growing cybercriminal ecosystem.

Over the past two years, high profile ransomware incidents—such as those involving critical infrastructure, healthcare, and IT service providers—have drawn considerable public attention. As ransomware attacks have become more audacious in scope, their effects have become more wide ranging. The following are examples of attacks we’ve seen already in 2022:

*   In February, an attack on two companies affected the payment processing systems of hundreds of gas stations in northern Germany. [Note 1](#note-1)
*   In March, an attack against Greece’s postal service temporarily disrupted mail delivery and impacted the processing of financial transactions. [Note 2](#note-2)
*   In late May, a ransomware attack against Costa Rican government agencies forced a national emergency to be declared after hospitals were shut down and customs and tax collection disrupted. [Note 3](#note-3)
*   Also in May, an attack caused flight delays and cancellations for one of India’s largest airlines, leaving hundreds of passengers stranded. [Note 4](#note-4)

The success of these attacks and the extent of their real-world impacts are the result of an industrialization of the cybercrime economy, enabling access to tooling and infrastructure and expanding cybercriminal capabilities by lowering their skill barrier to entry.

In recent years, ransomware has moved from a model where a single “gang” would both develop and distribute a ransomware payload to the ransomware as a service (RaaS) model. RaaS allows one group to manage the development of the ransomware payload and provide services for payment and extortion via data leakage to other cybercriminals—the ones who actually launch the ransomware attacks—referred to as “affiliates” for a cut of the profits. This franchising of the cybercrime economy has expanded the attacker pool. The industrialization of cybercriminal tooling has made it easier for attackers to perform intrusions, exfiltrate data, and deploy ransomware.

Human operated ransomware [Note 5](#note-5)—a term coined by Microsoft researchers to describe threats driven by humans who make decisions at every stage of the attacks based on what they discover in their target’s network and delineate the threat from commodity ransomware attacks—remains a significant threat to organizations.

**Human operated ransomware targeting and rate of success model**

2,500 potential target organizations
Access brokers sell access to compromised networks to ransomware-as-a-service affiliates, who run the ransomware attack

60 encounter activity associated with known ransomware attackers
RaaS affiliates prioritize targets by intended impact or perceived profit

20 are successfully compromised
Attackers take advantage of any security weakness they find in the network, so attacks vary

1 falls victim to a successful ransomware event
The ransomware payload is the culmination of a chain of malicious activity

Model based on Microsoft Defender for Endpoint (EDR) data (January–June 2022).

### Ransomware and extortion: A nation-level threat Continued

Ransomware attacks have become even more impactful as the adoption of a double extortion monetization strategy has become a standard practice. This involves exfiltrating data from compromised devices, encrypting the data on the devices, and then posting or threatening to post the stolen data publicly to pressure victims into paying a ransom.

Although most ransomware attackers opportunistically deploy ransomware to whatever network they get access, some purchase access from other cybercriminals, leveraging connections between access brokers and ransomware operators.

> Our unique breadth of signal intelligence is gathered from multiple sources—identity, email, endpoints, and cloud—and provides insight into the growing ransomware economy, complete with an affiliate system which includes tools designed for less technically-abled attackers.

Expanding relationships between specialized cybercriminals have increased the pace, sophistication, and success of ransomware attacks. This has driven the evolution of the cybercriminal ecosystem into connected players with different techniques, goals, and skillsets that support each other on initial access to targets, payment services, and decryption or publication tools or sites.

Ransomware operators can now purchase access to organizations or government networks online or obtain credentials and access via interpersonal relationships with brokers whose main objective is solely to monetize the access they have gained.

The operators then use the purchased access to deploy a ransomware payload bought via dark web marketplaces or forums. In many cases, negotiations with victims are conducted by the RaaS team, not the operators themselves. These criminal transactions are seamless and the participants risk little chance of being arrested and charged due to the anonymity of the dark web and difficulty enforcing laws transnationally.

A sustainable and successful effort against this threat will require a whole-of-government strategy to be executed in close partnership with the private sector.

> Digital threat activity is at an all-time high and the level of sophistication increases every day.

**Operators**
**Access brokers**
**Affiliates**
Conti
HIVE
Black Matter
LockBit
REvil
BlackCat

### Understanding the ransomware economy

The RaaS operator develops and maintains the tools to power the ransomware operations, including the builders that produce the ransomware payloads and payment portals for communicating with victims.

A RaaS program (or syndicate) is an arrangement between an operator and an affiliate. The RaaS operator develops and maintains the tools to power the ransomware operations, including the builders that produce the ransomware payloads and payment portals for communicating with victims. Many RaaS programs incorporate a suite of extortion support offerings, including leak site hosting and integration into ransom notes, as well as decryption negotiation, payment pressure, and cryptocurrency transaction services.

Affiliates are generally small groups of people “affiliated” with one or more RaaS programs. Their role is to deploy the RaaS program payloads. Affiliates move laterally in the network, persist on systems, and exfiltrate data. Each affiliate has unique characteristics, such as different ways of doing data exfiltration.

Access brokers sell network access to other cybercriminals, or gain access themselves via malware campaigns, brute force, or vulnerability exploitation. Access broker entities can range from large to small. Top tier access brokers specialize in high-value network access, while lower tier brokers on the dark web might have just 1–2 usable stolen credentials for sale.

Organizations and individuals with weak cybersecurity hygiene practices are at greater risk of having their network credentials stolen.

Contrary to how ransomware is sometimes portrayed in the media, it is rare for a single ransomware variant to be managed by one end-to-end “ransomware gang.” Instead, there are separate entities that build malware, gain access to victims, deploy ransomware, and handle extortion negotiations. The industrialization of the criminal ecosystem has led to:

*   Access brokers that break in and hand off access (access as a service).
*   Malware developers that sell tooling.
*   Criminal operators and affiliates that conduct intrusions.
*   Encryption and extortion service providers that take over monetization from affiliates (RaaS).

All human-operated ransomware campaigns share common dependencies on security weaknesses. Specifically, attackers usually take advantage of an organization’s poor cyber hygiene, which often includes infrequent patching and failure to implement multifactor authentication (MFA).

**Timeline of ransomware variant activity**
Jan
Ryuk 2020–Jun 2021
Hive Oct 2021–present
BlackCat Mar 2022–present
Nokoyawa May 2022–present
Agenda etc. June 2022 (experimenting)
2021
2022
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec
Jan
Feb
Mar
Apr
May
Jun
Conti Jul–Oct 2021

### Case study: The dissolution of Conti

Conti, one of the top ransomware variants over the past two years, began shutting down operations in mid-2022, with the Microsoft Threat Intelligence Center (MSTIC) observing a significant decrease in activity in late March and early April. We observed the last Conti ransomware deployments in mid-April.

However, much like the shuttering of other ransomware operations, Conti’s dissolution did not have a significant impact on ransomware deployments, as MSTIC observed Conti affiliates pivoting to deploy other ransomware payloads, including BlackBasta, Lockbit 2.0, LockbitBlack, and HIVE. This is consistent with data from previous years and suggests that when ransomware gangs go offline, they re-emerge months later or redistribute their technical capabilities and resources to new groups.

Our Microsoft threat intelligence teams track ransomware threat actors as individual groups (labeled as DEVs) based on their specific tools, rather than tracking them by the malware they use. This meant that when Conti’s affiliates dispersed, we were able to continue tracking these DEVs through their use of other tools or RaaS kits. For example:

*   DEV-0230, which is affiliated with Trickbot, had been a prolific user of Conti. In late April, MSTIC observed it using QuantumLocker.
*   DEV-0237 shifted from Conti’s ransomware kit to HIVE and Nokoyawa, including using HIVE in the May 31 attack against Costa Rican government agencies.
*   DEV-0506, another prolific user of the Conti ransomware kit, was observed using BlackBasta.

**Example of an affiliate (DEV-0237) quickly shifting between RaaS programs**
After a RaaS program such as Conti is shut down, the ransomware affiliate shifts to another one (Hive) almost immediately.

**RaaS evolves the ransomware ecosystem and hinders attribution**
Because human-operated ransomware is driven by individual operators, attack patterns vary based on the target and alternate throughout the duration of an attack. In the past, we observed a close relationship between the initial entry vector, tools, and ransomware payload choices in each campaign of a single ransomware strain. This made attribution easier. The RaaS affiliate model, however, decouples this relationship. As a result, Microsoft tracks ransomware affiliates deploying payloads in specific attacks, rather than tracking the ransomware payload developers as operators.

Put another way, we no longer assume the HIVE developer is the operator behind a HIVE ransomware attack; it is more likely to be an affiliate.

The cybersecurity industry has struggled to adequately capture this delineation between developers and operators. The industry still often reports a ransomware incident by its payload name, giving the false impression that a single entity, or ransomware gang, is behind all attacks using that particular ransomware payload, and all incidents associated with it share common techniques and infrastructure. To support network defenders, it is important to learn more about the stages that precede different affiliates’ attacks—such as data exfiltration and additional persistence mechanisms—and the detection and protection opportunities that might exist.

> More so than malware, attackers need credentials to succeed in their operations. The successful human operated ransomware infection of an entire organization relies on access to a highly privileged account.

### Spotlight on human-operated ransomware attacks

Over the past year, Microsoft’s ransomware experts conducted deep investigations into more than 100 human-operated ransomware incidents to track attackers’ techniques and understand how to better protect our customers. It is important to note that the analysis we share here is possible only for onboarded, managed, devices. Non-onboarded, unmanaged devices represent the least secure part of an organization’s hardware assets.

**Most prevalent ransomware phase techniques:**

*   **75%** Use admin tools.
*   **75%** Use acquired elevated compromised user account to spread malicious payloads through SMB protocol.
*   **99%** Attempt to tamper with discovered security and backup products using OS-built tools.

**The typical human-operated attack**
Human-operated ransomware attacks can be categorized into the pre-ransomware phase and the ransomware deployment phase. During the pre-ransomware phase, attackers prepare to infiltrate the network by learning about the organization’s typology and security infrastructure.

**Stop the attackers before they reach the ransomware deployment phase**
Deployment!
Pre-ransomware
Ransomware
This phase can range from a few days to several weeks or months, although it has been shortening over the past two years.
This phase can last only minutes.
Attackers prepare to infiltrate the network by learning as much as possible about the topology and security infrastructure. Attackers may also exfiltrate data in this phase.
Attackers aim to encrypt as much data as possible.

Our investigations found most actors behind human-operated ransomware attacks take advantage of similar security weaknesses and share common attack patterns and techniques.

**A durable security strategy**
Combating and preventing attacks of this nature requires a shift in an organization’s mindset to focus on the comprehensive protection required to slow and stop attackers before they can move from the pre-ransomware phase to the ransomware deployment phase.

Enterprises must apply security best practices consistently and aggressively to their networks, with the goal of mitigating classes of attacks. Due to the human decision making these ransomware attacks can generate multiple, seemingly disparate security product alerts which can easily get lost or not responded to in time. Alert fatigue is real, and security operations centers (SOCs) can make their lives easier by looking at trends in their alerts or grouping alerts into incidents so they can see the bigger picture. SOCs can then mitigate alerts using hardening capabilities like attack surface reduction rules. Hardening against common threats can not only reduce alert volume, but also stop many attackers before they get access to networks.

> Organizations must maintain continuous high standards of security posture and network hygiene to protect themselves from human-operated ransomware attacks.

**Actionable insights**
Ransomware attackers are motivated by easy profits, so adding to their cost via security hardening is key in disrupting the cybercriminal economy.

1.  Build credential hygiene. More so than malware, attackers need credentials to succeed in their operations. The successful human-operated ransomware infection of an entire organization relies on access to a highly privileged account like a Domain Administrator, or abilities to edit a Group Policy.
2.  Audit credential exposure.
3.  Prioritize deployment of Active Directory updates.
4.  Prioritize cloud hardening.
5.  Reduce the attack surface.
6.  Harden internet-facing assets and understand your perimeter.
7.  Reduce SOC alert fatigue by hardening your network to reduce volume and preserve bandwidth for high priority incidents.

**Links to further information**
*   RaaS: Understanding the cybercrime gig economy and how to protect yourself | Microsoft Security Blog
*   Human-operated ransomware attacks: A preventable disaster | Microsoft Security Blog

### Ransomware insights from front-line responders

Organizations worldwide experienced a steady growth in human-operated ransomware attacks beginning in 2019. However, law enforcement operations and geopolitical events in the last year had a significant impact on cybercriminal organizations.

Microsoft’s Security Service Line supports customers through an entire cyberattack, from investigation to successful containment and recovery activities. The response and recovery services are offered via two highly integrated teams, with one focusing on the investigation and groundwork for recovery and the second one on containment and recovery. This section presents a summary of findings based on ransomware engagements over the past year.

**93%** of Microsoft investigations during ransomware recovery engagements revealed insufficient privilege access and lateral movement controls.

**Ransomware incident and recovery engagements by industry**

*   Manufacturing 28%
*   IT 4%
*   Finance 8%
*   Government 8%
*   Health 20%
*   Energy 8%
*   Education 8%
*   Consumer retail 16%

As new small groups and threats emerge, defending teams must be aware of evolving ransomware threats while protecting against previously unknown ransomware malware families. The rapid development approach used by criminal groups led to the creation of intelligent ransomware packaged in easy-to-use kits. This allows greater flexibility in launching widespread attacks on a higher number of targets.

The following pages provide a deeper look at the most commonly observed contributing factors to weak protection against ransomware, grouped into three categories of findings:

1.  Weak identity controls
2.  Ineffective security operations
3.  Limited data protection

**Summary of most common findings in ransomware response engagements**
The most common finding among ransomware incident response engagements was insufficient privilege access and lateral movement controls.

### Ransomware insights from front-line responders Continued

**The three main contributing factors seen in our onsite response engagements:**

1.  Weak identity controls: Credential theft attacks remain one of the top contributing factors
2.  Ineffective security operations processes do not just present a window of opportunity for attackers but significantly impact the time to recover
3.  Eventually it boils down to data—organizations struggle to implement an effective data protection strategy which aligns with their business needs

**1. Weak identity controls**
Human-operated ransomware continues to evolve and employ credential theft and lateral movement methods traditionally associated with targeted attacks. Successful attacks are often the result of long-running campaigns involving compromise of identity systems, like Active Directory (AD), that allow human operators to steal credentials, access systems, and remain persistent in the network.

**Active Directory (AD) and Azure AD security**
**88%** of impacted customers did not employ AD and Azure AD security best practices. This has become a common attack vector as attackers exploit misconfigurations and weaker security postures in critical identity systems to gain broader access and impact to businesses.

**Least privilege access and use of Privileged Access Workstations (PAW)**
None of the impacted organizations implemented proper administrative credential