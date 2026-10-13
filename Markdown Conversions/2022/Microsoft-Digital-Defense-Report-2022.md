Microsoft Digital Defense Report 2022
Illuminating the threat landscape and empowering a digital defense.

## Table of Contents
- [Report Introduction](#report-introduction)
- [The State of Cybercrime](#the-state-of-cybercrime)
  - [An overview of The State of Cybercrime](#an-overview-of-the-state-of-cybercrime)
  - [Introduction](#introduction)
  - [Ransomware and extortion: A nation-level threat](#ransomware-and-extortion-a-nation-level-threat)
  - [Ransomware insights from front-line responders](#ransomware-insights-from-front-line-responders)
  - [Cybercrime as a service](#cybercrime-as-a-service)
  - [The evolving phishing threat landscape](#the-evolving-phishing-threat-landscape)
  - [A timeline of botnet disruption from Microsoft’s early days of collaboration](#a-timeline-of-botnet-disruption-from-microsofts-early-days-of-collaboration)
  - [Cybercriminal abuse of infrastructure](#cybercriminal-abuse-of-infrastructure)
  - [Is hacktivism here to stay?](#is-hacktivism-here-to-stay)
- [Nation State Threats](#nation-state-threats)
- [Devices and Infrastructure](#devices-and-infrastructure)
- [Cyber Influence Operations](#cyber-influence-operations)
- [Cyber Resilience](#cyber-resilience)
- [Contributing Teams](#contributing-teams)

---

## Report Introduction

Introduction by Tom Burt  
Corporate Vice President, Customer Security & Trust

> "The trillions of signals we analyze from our worldwide ecosystem of products and services reveal the ferocity, scope, and scale of digital threats across the globe."

On February 23, 2022, the cybersecurity world entered a new age, the age of the hybrid war. On that day, hours before missiles were launched and tanks rolled across borders, Russian actors launched a massive destructive cyberattack against Ukrainian government, technology, and financial sector targets. You can read more about these attacks and the lessons to be learned from them in the Nation State Threats chapter of this third annual edition of the Microsoft Digital Defense Report (MDDR). Key among those lessons is that the cloud provides the best physical and logical security against cyberattacks and enables advances in threat intelligence and end point protection that have proven their value in Ukraine.

While any survey of the year’s developments in cybersecurity must begin there, this year’s report provides a deep dive into much more. In the report’s first chapter, we focus on activities of cybercriminals, followed by nation state threats in chapter two. Both groups have greatly increased the sophistication of their attacks which has dramatically increased the impact of their actions.

While Russia drove headlines, Iranian actors escalated their attacks following a transition of presidential power, launching destructive attacks targeting Israel, and ransomware and hack-and-leak operations targeting critical infrastructure in the United States. China also increased its espionage efforts in Southeast Asia and elsewhere in the global south, seeking to counter US influence and steal critical data and information.

Foreign actors are also using highly effective techniques to enable propaganda influence operations in regions around the globe, as covered in the third chapter. For example, Russia has worked hard to convince its citizens, and the citizens of many other countries, that its invasion of Ukraine was justified – while also sowing propaganda discrediting COVID vaccines in the West and simultaneously promoting their effectiveness at home.

In addition, actors are increasingly targeting Internet of Things (IoT) devices or Operational Technology (OT) control devices as entry points to networks and critical infrastructure which is discussed in chapter four. Finally, in the last chapter, we provide the insights and lessons we have learned from over the past year defending against attacks directed at Microsoft and our customers as we review the year’s developments in cyber resilience.

Each chapter provides the key lessons learned and insights based on Microsoft’s unique vantage point. The trillions of signals we analyze from our worldwide ecosystem of products and services reveal the ferocity, scope, and scale of digital threats across the globe. Microsoft is taking action to defend our customers and the digital ecosystem against these threats, and you can read about our technology that identifies and blocks billions of phishing attempts, identity thefts, and other threats to our customers.

### A snapshot of our landscape…

- **Scope and scale of threat landscape**: The volume of password attacks has risen to an estimated 921 attacks every second – a 74% increase in just one year.
- **Dismantling cybercrime**: To date, Microsoft removed more than 10,000 domains used by cybercriminals and 600 used by nation state actors.
- **Addressing vulnerabilities**: Incident response engagements revealed insufficient controls on privilege access and lateral movement.

We also use legal and technical means to seize and shut down infrastructure used by cybercriminals and nation state actors and notify customers when they are being threatened or attacked by a nation state actor. We work to develop increasingly effective features and services that use AI/ML technology to identify and block cyber threats and security professionals defend against and identify cyber-intrusions more rapidly and effectively.

Perhaps most importantly, throughout the MDDR we offer our best advice on the steps individuals, organizations, and enterprises can take to defend against these increasing digital threats. Adopting good cyber hygiene practices is the best defense and can significantly reduce the risk of cyberattacks.

> "The advent of cyberweapon deployment in the hybrid war in Ukraine is the dawn of a new age of conflict."

---

## The State of Cybercrime

### An overview of The State of Cybercrime

Cybercrime continues to rise as the industrialization of the cybercrime economy lowers the skill barrier to entry by providing greater access to tools and infrastructure.

Find out more on p18

#### The trends of the ransomware economy
The RaaS operator develops and maintains the tools to power the ransomware operations, including the builders that produce the ransomware payloads and payment portals for communicating with victims.

- **Conti**
- **LockBit**
- **BlackCat**
- **HIVE**
- **Matter**
- **REvil**

**Affiliates**: Affiliates are generally small groups of people “affiliated” with one or more RaaS programs. Their role is to deploy the RaaS program payloads. Affiliates move laterally in the network, persist on systems, and exfiltrate data. Each affiliate has unique characteristics, such as different ways of doing data exfiltration.

**Access brokers**: Access brokers sell network access to other cybercriminals, or gain access themselves via malware campaigns, brute force, or vulnerability exploitation. Access broker entities can range from large to small. Top tier access brokers specialize in high-value network access, while lower tier brokers on the dark web might have just 1–2 usable stolen credentials for sale.

Organizations and individuals with weak cybersecurity hygiene practices are at greater risk of having their network credentials stolen.

Attackers increasingly threaten to disclose sensitive data to encourage ransom payments.

Find out more on p10

---

### Introduction

Cybercrime continues to rise, with increases in both random and targeted cybercrime. One approach is a campaign with broad targets that relies on volume. The other uses surveillance and more selective targeting to increase the rate of return. Even when generation is not the objective—such as nation state activity for geopolitical purposes—both random and targeted attacks are used. This past year, cybercriminals continued to rely on social engineering and exploitation of topical issues to maximize the success of campaigns.

For example, while COVID-themed phishing lures were used less frequently, we observed lures soliciting donations to support the citizens of Ukraine increasing.

Attackers are adapting and finding new ways to implement their techniques, increasing the complexity of how and where they host campaign operation infrastructure. We have observed cybercriminals becoming more frugal and attackers are no longer paying for technology. To lower their overhead and boost the appearance of legitimacy, some attackers increasingly seek to compromise businesses to host phishing campaigns, malware, or even use their computing power to mine cryptocurrency.

In this chapter, we also examine the rise in hacktivism, a disruption caused by private citizens conducting cyberattacks to further social or political goals. Thousands of individuals around the world, both experts and novices, have mobilized since February 2022 to launch attacks such as disabling websites and leaking stolen data as part of the Russia-Ukraine war. It is too soon to predict whether this trend will continue after the end of active hostilities.

Organizations must regularly review and strengthen access controls and implement security strategies to defend against cyberattacks. However, that is not all they can do. We explain how our Digital Crimes Unit (DCU) has used civil cases to seize malicious infrastructure used by cybercriminals and nation state actors. We must fight this threat together through both public and private partnerships. We hope that by sharing what we have learned over the past 10 years, we will help others understand and consider the proactive measures they can take to protect themselves and the wider ecosystem against the continually growing threat of cybercrime.

Amy Hogan-Burney  
General Manager, Digital Crimes Unit

---

### Ransomware and extortion: A nation-level threat

Ransomware attacks pose an increased danger to all individuals as critical infrastructure, businesses of all sizes, and state and local governments are targeted by criminals leveraging a growing cybercriminal ecosystem.

Over the past two years, high profile ransomware incidents—such as those involving critical infrastructure, healthcare, and IT service providers—have drawn considerable public attention. As ransomware attacks have become more audacious in scope, their effects have resulted in real-world impacts:

- In February, an attack on two companies affected the payment processing systems of hundreds of gas stations in northern Germany.[^1]
- In March, an attack against Greece’s postal service temporarily disrupted mail delivery and impacted the processing of financial transactions.[^2]
- In late May, a ransomware attack against Costa Rican government agencies forced a national emergency to be declared after hospitals were shut down and customs and tax collection disrupted.[^3]
- Also in May, an attack caused flight delays and cancellations for one of India’s largest airlines, leaving hundreds of passengers stranded.[^4]

The success of these attacks and the extent of their real-world impacts are the result of an industrialization of the cybercrime economy, enabling access to tooling and infrastructure and expanding cybercriminal capabilities by lowering their skill barrier to entry.

In recent years, ransomware has moved from a model where a single “gang” would both develop and distribute a ransomware payload to the ransomware as a service (RaaS) model. RaaS allows one group to manage the development of the ransomware payload and provide services for payment and extortion via ransomware operators intended to data leakage to other cybercriminals—the ones who actually launch the ransomware attacks—referred to as “affiliates” for a cut of the profits. This franchising of the cybercrime economy has expanded the attacker pool. The industrialization of cybercriminal tooling has made it easier for attackers to perform intrusions, exfiltrate data, and deploy ransomware.

Human operated ransomware[^5]—a term coined by Microsoft researchers to describe threats driven by humans who make decisions at every stage of the attacks based on what they discover in their target’s network and delineate the threat from commodity ransomware attacks—remains a significant threat to organizations.

Expanding relationships between specialized cybercriminals have increased the pace, sophistication, and success of ransomware attacks. This has driven the evolution of the cybercriminal ecosystem into connected players with different techniques, goals, and skillsets that support each other on initial access to targets, payment services, and decryption or publication tools or sites.

Ransomware operators can now purchase access to organizations or government networks online or obtain credentials and access via interpersonal relationships with brokers whose main objective is solely to monetize the access they have gained.

The operators then use the purchased access to deploy a ransomware payload bought via dark web marketplaces or forums. In many cases, negotiations with victims are conducted by the RaaS team, not the operators themselves. These criminal transactions are seamless and the participants risk little chance of being arrested and charged due to the anonymity of the dark web and difficulty enforcing laws transnationally.

A sustainable and successful effort against this threat will require a whole-of-government strategy to be executed in close partnership with the private sector.

---

### Understanding the ransomware economy

- **Operators**: The RaaS operator develops and maintains the tools to power the ransomware operations, including the builders that produce the ransomware payloads and payment portals for communicating with victims.
- **RaaS Programs / Syndicates**: A RaaS program (or syndicate) is an arrangement between an operator and an affiliate. Many RaaS programs incorporate a suite of extortion support offerings, including leak site hosting and integration into ransom notes, as well as decryption negotiation, payment pressure, and cryptocurrency transaction services.
- **Affiliates**: Affiliates are generally small groups of people “affiliated” with one or more RaaS programs. Their role is to deploy the RaaS program payloads. Affiliates move laterally in the network, persist on systems, and exfiltrate data. Each affiliate has unique characteristics, such as different ways of doing data exfiltration.
- **Access Brokers**: Access brokers sell network access to other cybercriminals, or gain access themselves via malware campaigns, brute force, or vulnerability exploitation. Top tier access brokers specialize in high-value network access, while lower tier brokers on the dark web might have just 1–2 usable stolen credentials for sale.

---

### Spotlight on human-operated ransomware attacks

Human-operated ransomware attacks can be categorized into the pre-ransomware phase and the ransomware deployment phase. Over the past year, Microsoft’s ransomware experts conducted deep investigations into more than 100 human-operated ransomware incidents to track attackers’ techniques and understand how to better protect our customers.

During the pre-ransomware phase, attackers prepare to infiltrate the network by learning about the organization’s typology and security infrastructure. 

Combating and preventing attacks of this nature requires a shift in an organization’s mindset to focus on the comprehensive protection required to slow and stop attackers before they can move from the pre-ransomware phase to the ransomware deployment phase.

---

## Contributing Teams

Microsoft threat intelligence teams, security researchers, data scientists, cybersecurity experts, threat hunters, geopolitical analysts, investigators, and frontline responders across 77 countries.

---

[^1]: Incident report reference regarding German gas station payment processing attack, 2022.
[^2]: Incident report reference regarding Greece's postal service disruption, 2022.
[^3]: Incident report reference regarding Costa Rican government ransomware attack, 2022.
[^4]: Incident report reference regarding Indian airline flight disruptions, 2022.
[^5]: Definition established by Microsoft threat intelligence researchers regarding human-operated ransomware.

---

------------------------------- | --- | --- | --- | ------------------------------------------- | --- |
deployment phase
It is important to note that the analysis we  ransomware attacks can generate multiple,  a highly privileged account like a Domain
share here is possible only for onboarded,  seemingly disparate security product alerts which  Administrator, or abilities to edit a Group Policy.
|     | Pre-ransomware | Ransomware | can easily get lost or not responded to in time.  |     |     |     |     |     |
| --- | -------------- | ---------- | ------------------------------------------------- | --- | --- | --- | --- | --- |
managed, devices. Non-onboarded, unmanaged   2  Audit credential exposure.
devices represent the least secure part of an  Alert fatigue is real, and security operations
centers (SOCs) can make their lives easier by
organization’s hardware assets. This phase can range from a few  This phase   3  Prioritize deployment of Active
days to several weeks or months,  can last only  looking at trends in their alerts or grouping alerts  Directory updates.
|     | although it has been shortening  | minutes. | into incidents so they can see the bigger picture.  |     |     |     |                                 |     |
| --- | -------------------------------- | -------- | --------------------------------------------------- | --- | --- | --- | ------------------------------- | --- |
|     |                                  |          | SOCs can then mitigate alerts using hardening       |     |     |     |  4  Prioritize cloud hardening. |     |
over the past two years.
Most prevalent ransomware  capabilities like attack surface reduction rules.
 5  Reduce the attack surface.
| phase techniques: |                                  |                | Hardening against common threats can not  |     |     |     |     |     |
| ----------------- | -------------------------------- | -------------- | ----------------------------------------- | --- | --- | --- | --- | --- |
|                   | Attackers prepare to infiltrate  | Attackers aim  |                                           |     |     |     |     |     |
the network by learning as much  to encrypt as  only reduce alert volume, but also stop many   6  Harden internet-facing assets and
75%
  much data as  attackers before they get access to networks. understand your perimeter.
as possible about the topology
|     | and security infrastructure.  | possible.  |     |     |     |     |     |     |
| --- | ----------------------------- | ---------- | --- | --- | --- | --- | --- | --- |
 7   Reduce SOC alert fatigue by hardening your
| Use admin tools. | Attackers may also exfiltrate  |     |                              |     |     |     |                                        |     |
| ---------------- | ------------------------------ | --- | ---------------------------- | --- | --- | --- | -------------------------------------- | --- |
|                  |                                |     | Organizations must maintain  |     |     |     | network to reduce volume and preserve  |     |
data in this phase.
75%  continuous high standards of  bandwidth for high priority incidents.
|     |     |     | security posture and network  |     |     |     | Links to further information |     |
| --- | --- | --- | ----------------------------- | --- | --- | --- | ---------------------------- | --- |
Use acquired elevated compromised  hygiene to protect themselves  RaaS: Understanding the cybercrime gig
user account to spread malicious  economy and how to protect yourself |
from human-operated
payloads through SMB protocol.
Microsoft Security Blog
ransomware attacks.
| 99%  |     |     |     |     |     |     | Human-operated ransomware attacks:  |     |
| ---- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- |
Our investigations found most actors behind
A preventable disaster | Microsoft
human-operated ransomware attacks take
Security Blog
| Attempt to tamper with discovered  | advantage of similar security weaknesses and  |     |     |     |     |     |     |     |
| ---------------------------------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
security and backup products using
share common attack patterns and techniques.
OS-built tools.

|     |     | Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber   | Contributing  |     |     |
| --- | --- | ------- | -------------- | -------------- | ------------- | ---------------- | ------- | ------------- | --- | --- |
14 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
  Ransomware insights    Ransomware incident and recovery    Summary of most common findings in ransomware response engagements
engagements by industry
  from front-line
93%
|               | IT 4% | Manufacturing 28% |     |     |     |     |     |     |     |     |
| ------------- | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|   responders  |       |                   |     |     |     | 87% |     | 86% |     |     |
Health 20%
Organizations worldwide experienced
|     |     |     |     |     | 74% |     |     |     | 74% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a steady growth in human-operated
| ransomware attacks beginning in 2019.  |           |     |     |     |     |     |     |     |     | 65% |
| -------------------------------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                        | Energy 8% |     |     | 62% |     |     |     |     |     |     |
However, law enforcement operations
and geopolitical events in the last
year had a significant impact on
Finance 8%
| cybercriminal organizations. |     | Consumer retail 16% |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Microsoft’s Security Service Line supports
|     | Government 8% | Education 8% |     |     |     |     |     |     |     |     |
| --- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |

customers through an entire cyberattack, from
| investigation to successful containment and        | As new small groups and threats emerge,         |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| recovery activities. The response and recovery     | defending teams must be aware of evolving       |     |     |     |     |     |     |     |     |     |
| services are offered via two highly integrated     | ransomware threats while protecting against     |     |     |     |     |     |     |     |     |     |
| teams, with one focusing on the investigation and  | previously unknown ransomware malware           |     |     |     |     |     |     |     |     |     |
| groundwork for recovery and the second one on      | families. The rapid development approach        |     |     |     |     |     |     |     |     |     |
| containment and recovery. This section presents    | used by criminal groups led to the creation of  |     |     |     |     |     |     |     |     |     |
a summary of findings based on ransomware  intelligent ransomware packaged in easy-to-use   ytirutam woL  noitacilppa tneiciffusnI  ssecca egelivirp tneiciffusnI  noitarugifnoc erucesnI  noitamrofni fo kcaL
|                                 |                                                     |     |     | snoitarepo ytiruces | secitcarp ytiruces | nredom fo noitpoda detimiL skrowemarf ytiruces  | slortnoc tnemevom laretal dna | redivorp ytitnedi fo | noitacitnehtua rotcafitlum oN | lortnoc noitcetorp |
| ------------------------------- | --------------------------------------------------- | --- | --- | ------------------- | ------------------ | ----------------------------------------------- | ----------------------------- | -------------------- | ----------------------------- | ------------------ |
| engagements over the past year. | kits. This allows greater flexibility in launching  |     |     |                     |                    |                                                 |                               |                      |                               |                    |
widespread attacks on a higher number
of targets.
The following pages provide a deeper look at the
most commonly observed contributing factors to
weak protection against ransomware, grouped
| 93% | into three categories of findings:  |     |     |     |     |     |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

1. Weak identity controls
of Microsoft investigations
2. Ineffective security operations
during ransomware recovery
engagements revealed
3. Limited data protection
insufficient privilege access  The most common finding among ransomware incident response engagements was insufficient privilege access
and lateral movement controls. and lateral movement controls.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
15 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Ransomware insights The three main contributing
1 Weak identity controls
factors seen in our onsite
from front-line
response engagements: Human-operated ransomware continues to evolve and employ credential theft and lateral
responders movement methods traditionally associated with targeted attacks. Successful attacks are often
the result of long-running campaigns involving compromise of identity systems, like Active
1 Weak identity controls:
Directory (AD), that allow human operators to steal credentials, access systems, and remain
Continued
Credential theft attacks remain persistent in the network.
one of the top contributing factors
2 Ineffective security
Active Directory (AD) and Azure AD security Privilege account security
88% 88%
operations processes do not just
present a window of opportunity
of impacted customers did not employ AD of engagements, MFA was not implemented for
for attackers but significantly
and Azure AD security best practices. This has sensitive and high privileged accounts, leaving
impact the time to recover become a common attack vector as attackers a security gap for attackers to compromise
exploit misconfigurations and weaker security credentials and pivot further attacks using
3 Eventually it boils down to postures in critical identity systems to gain legitimate credentials.
broader access and impact to businesses.
data—organizations struggle 84%
to implement an effective data
Least privilege access and use of Privileged
protection strategy which aligns Administrators across 84 percent of
Access Workstations (PAW)
organizations did not use privilege identity
with their business needs
None of the impacted organizations controls such as just-in-time access to prevent
implemented proper administrative credential further nefarious use of compromised
segregation and least privilege access principles privileged credentials.
via dedicated workstations during the
management of their critical identity and high-
value assets, such as proprietary systems and
business-critical applications.

Report TThhee SSttaattee ooff Nation State Devices and Cyber Influence Cyber Contributing
16 Microsoft Digital Defense Report 2022 Introduction CCyybbeerrccrriimmee Threats Infrastructure Operations Resilience Teams
Ransomware insights
2 Ineffective security operations 3 Limited data protection
from front-line
Our data shows organizations which suffered ransomware attacks have significant gaps in their Many compromised organizations lacked
responders security operations, tooling, and information technology asset lifecycle management. Based on proper data protection processes leading
the available data, the following gaps were most observed: to a severe impact on recovery times
and the capability to return to business
Continued
operations. The most common gaps
encountered include:
Patching: 60%
68%
did not invest in security information and
Immutable backup:
event management (SIEM) technology leading
of impacted organizations did not have an
to monitoring silos, limited ability to detect 44%
effective vulnerability and patch management
end-to-end threats and inefficient security
process, and a high dependence on manual
operations. Automation remains a key gap in
processes versus automated patching led to of organizations did not have immutable
SOC tooling and processes, forcing SOC staff
critical openings. Manufacturing and critical backups for the impacted systems. Data also
to spend countless hours making sense of
infrastructure continue to struggle with shows administrators did not have backups and
security telemetry.
maintenance and patching of legacy recovery plans for critical assets such as AD.
operational technology (OT) systems. 84%
Data loss prevention:
Lack of security operations tooling: of impacted organizations did not enable
Attackers usually find their way to compromise
integration of their multi-cloud environments
Most organizations reported a lack of end- systems via exploiting vulnerabilities in
into their security operations tooling.
to-end security visibility due to a lack or the organization, exfiltrating critical data
misconfiguration of security tools, leading to a for extortion, intellectual property theft,
decrease in detect and response effectiveness. or monetization.
Response and recovery processes:
60% 92%
76%
of organizations reported no use of an EDR6 of impacted organizations did not implement
Lack of an effective response plan was a critical
tool, a fundamental technology for detection effective data loss prevention controls
area observed in 76 percent of impacted
and response. to mitigate these risks, leading to critical
organizations, preventing proper organizational
data loss.
crisis readiness and negatively impacting time
to respond and recover.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
17 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
One interpretation of this observation is While law enforcement activities likely slowed
Ransomware declined in some Actionable insights
cybercriminals pivoted away from areas the frequency of attacks in 2022, threat actors
regions and increased in others perceived to have a higher risk of triggering might well develop new strategies to avoid being 1 Focus on holistic security strategies, as all
law enforcement scrutiny in favor of softer caught in the future. Moreover, tension between of the ransomware families take advantage
This year we observed a drop in the targets. Since Microsoft did not observe a Russia and the United States over Russia’s of the same security weaknesses to impact
overall number of ransomware cases substantial improvement in enterprise network invasion of Ukraine appears to have put an end a network.
security worldwide to explain the decrease in to Russia’s nascent cooperation in the global
reported to our response teams in North
ransomware-related support calls, we believe fight against ransomware. After a brief period of 2 Update and maintain security basics to
America and Europe compared to the
the most likely cause is a combination of law uncertainty following the REvil arrests, the United increase defense-in-depth base level
previous year. At the same time, cases
enforcement activity in 2021 and 2022 which States and Russia ceased cooperation in pursuing of protection and modernize security
reported in Latin America increased. increased the cost of criminal activity, along with ransomware actors, which means cybercriminals operations. Moving to the cloud allows
some geopolitical events of 2022. might view Russia as a safe haven once more. you to detect threats more quickly and
respond faster.
One of the most prevalent RaaS operations Looking ahead, we predict the pace of
belongs to a Russian-speaking criminal group ransomware activities will depend on the Links to further information
known as REvil (also known as Sodinokibi) that outcome of some key questions:
Protect your organization from
has been active since 2019. In October 2021,
1. Will governments take action to prevent ransomware | Microsoft Security
REvil’s servers were taken offline as part of
ransomware criminals from operating within
the international law enforcement Operation 7 ways to harden your environment
their borders, or seek to disrupt actors
GoldDust.7 In January 2022, Russia arrested 14 against compromise | Microsoft
operating from foreign soil?
alleged REvil members and raided 25 locations Security Blog
2. Will ransomware groups change tactics to
associated with them.8 This was the first time
Improving AI-based defenses to disrupt
remove the need for ransomware and resort
Russia acted against ransomware operators
human-operated ransomware | Microsoft
to extortion style attacks?
on its soil.
365 Defender Research Team
3. Will organizations be able to modernize and
While law enforcement transform their IT operations faster than Security Insider: Explore the latest
criminals can exploit vulnerabilities? cybersecurity insights and updates |
activities likely slowed
Microsoft Security
4. Will advancements in tracking and tracing
the frequency of attacks ransom payments force ransom recipients
to change tactics and negotiations?
in 2022, threat actors
2X
might well develop new
strategies to avoid being
Ransomware attacks decreased
in some regions, but ransom
caught in the future.
demands more than doubled.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
18 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Cybercriminals are now collaborating across time process invoicing, such as CFOs or “Accounts configure the RDP, SSH, and cPanels with
Cybercrime
zones and languages to deliver specific results. Receivable.” Similarly, industries participating in appropriate tools and scripts to facilitate
For example, one CaaS website administered public contracting are often targeted due to the various types of cyberattacks.
as a service
by an individual in Asia maintains operations quantity of information that is made available
in Europe, and creates malicious accounts in through the public bidding process.
Cybercrime as a service (CaaS) is a Homoglyph domain creation services
Africa. The multi-jurisdictional nature of these
growing and evolving threat to customers DCU investigations into CaaS surfaced are increasingly requiring payment
operations present complex law and enforcement
worldwide. The Microsoft Digital Crimes challenges. In response, DCU focuses its efforts a number of key trends: in cryptocurrencies.
Unit (DCU) observed continued growth on disabling malicious criminal infrastructure Homoglyph domains impersonate legitimate
of the CaaS ecosystem with an increasing used to facilitate CaaS attacks and collaborating The number and sophistication of services domain names by utilizing characters that are
number of online services facilitating with law enforcement agencies around the world is increasing. identical or nearly identical in appearance to
various cybercrimes, including BEC to hold criminals accountable. another character. The aim is to deceive the
One example is the evolution of web shells
and human-operated ransomware. Cybercriminals are increasingly using analytics to viewer into thinking the homoglyph domain
which typically consist of compromised web
Phishing continues to be a preferred maximize reach, scope, and gain. Like legitimate is the genuine domain. These domains are a
servers used to automate phishing attacks.
attack method as cybercriminals businesses, CaaS websites must ensure the ubiquitous threat and a gateway for a significant
DCU observed CaaS resellers simplifying the
can acquire significant value from validity of products and services to maintain a amount of cybercrime. CaaS sites now sell
upload of phishing kits or malware through
successfully stealing and selling solid reputation. For example, CaaS websites custom homoglyph domain names, which allows
specialized web-dashboards. CaaS sellers often
access to stolen accounts. routinely automate access to compromised subsequently attempt to sell additional services buyers to request specific company and domain
accounts to ensure the validity of compromised names to impersonate. After payment is received,
to the threat actor through the dashboard
credentials. Cybercriminals will discontinue sales the CaaS merchants use a homoglyph generator
In response to the expanding CaaS market, of specific accounts when passwords are reset or such as spam message services and specialized tool to select the domain name and then register
DCU enhanced its listening systems to detect vulnerabilities patched. Increasingly, we identified spam recipient lists based on defined attributes the malicious homoglyph. Payment for this
and identify CaaS offerings across the entire CaaS websites providing buyers with on-demand including geographic location or profession. service is almost exclusively in cryptocurrency.
ecosystem of internet, deep web, vetted forums,9 In some instances, we observed a single web
verification as a quality control process. As a
dedicated websites, online discussion forums, shell being used in multiple attack campaigns,
result, buyers can feel confident the CaaS website
and messaging platforms. which suggests threat actors might maintain
sells active accounts and passwords while
persistent access to the compromised server.
reducing potential costs to the CaaS merchant
We also observed an increase in anonymization
if the stolen credentials are remediated prior
services available as part of the CaaS ecosystem
to sale.
as well as offers for virtual private networks
DCU also observed CaaS websites offering (VPN) and virtual private server (VPS) accounts.
2,750,000
buyers the option to purchase compromised In most instances, the VPN/VPS offered were
accounts from specific geographic locations, initially procured through stolen credit cards.
designated online service providers, and CaaS websites also offered a larger number of site registrations successfully
specifically targeted individuals, professions, remote desktop protocol (RDP), secure shell blocked by DCU this year to get
and industries. Frequently ordered accounts (SSH), and cPanels for use as a platform to ahead of criminal actors that
planned to use them to engage
focus on professionals or departments that orchestrate cybercrime attacks. CaaS merchants
in global cybercrime.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
19 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
is a virtual machine, gathering details about the
Cybercrime
browser and hardware being used, and more. PhaaS, cybercriminals offer multiple services within
If all checks pass, traffic is sent to a landing page a single subscription. In general, a purchaser needs
as a service
used for phishing. to take only three actions:
Continued
End-to-end cybercrime services are selling
subscriptions to managed services.
CaaS sellers increasingly offer
compromised credentials for purchase. Typically, each step in the commission of
an online crime can expose threat actors Attackers aim
Compromised credentials enable unauthorized
if operational security is poor. The risk of to encrypt as
access to user accounts including email Select a Provide an email Pay the PhaaS
messaging service, corporate file sharing e
ar
x
e
p o
p
s
u
u
rc
re
h a
a
s
n
e
d
d
i d
fr
e
o
n
m
ti fi
m
ca
u
t
lt
io
ip
n
le
in
C
c
a
re
a
a
S
s
s
e
it
s
e
i
s
f
.
s ervices 1 phishing site 2 address to rec m
p
e
o
i u v
s
c
s
e h
i b
d
le
a ta as 3 merchant in
resources, and OneDrive for Business. template/design credentials cryptocurrency.
DCU observed a concerning trend in the dark
from among the obtained from
If administrator credentials are compromised,
web whereby there is an increase in services hundreds offered. phishing victims.
unauthorized users could gain access to
offering to anonymize software code and
confidential files, Azure resources, and
genericize website text to reduce exposure. End-
company user accounts. In many instances,
to-end cybercrime subscription service providers
DCU investigations identified unauthorized use
manage all services and guarantee results which
of the same credential across multiple servers
further reduce exposure risks to the subscribing
as a means to automate verifying credentials.
OCN. The reduced risk has increased the Once these steps are completed, the PhaaS merchant creates services with three or four layers of redirect and
This pattern suggests the compromised user
popularity of these end-to-end services. hosting resources to target specific users. The campaign is subsequently launched, and victim credentials are
might be a victim of multiple phishing attacks or harvested, verified, and sent to the email address provided by the purchaser. For a premium, many PhaaS
have device malware allowing botnet keyloggers Phishing as a service (PhaaS) is one example merchants offer to host phishing sites on the public blockchain so they can be accessed by any browser and
to collect credentials. of an end-to-end cybercrime service. PhaaS is redirects can point users to a resource on the distributed ledger.
an evolution of prior services known as fully
undetectable services (FUD) and is offered on a
CaaS services and products with enhanced
subscription basis. Typical PhaaS terms include
features are emerging to avoid detection. support. The DDoS subscription service offers DCU’s work to develop tools and techniques
keeping phishing websites active for a month.
different architectures and attack methods, so which identify and disrupt CaaS cybercriminals is
One CaaS seller offers phishing kits with DCU also identified a CaaS merchant offering a purchaser simply selects a resource to attack ongoing. The evolution of CaaS services presents
increased layers of complexity and anonymization distributed denial of service (DDoS) on a and the seller provides access to an array of significant challenges, particularly in disrupting
features designed to circumvent detection and subscription model. This model outsources compromised devices on their botnet to conduct cryptocurrency payments.
prevention systems for as little as $6 USD per the creation and maintenance of the botnet the attack. The cost for the DDoS subscription is a
day. The service offers a series of redirects that necessary to carry out attacks to the CaaS mere $500 USD.
perform checks before allowing traffic to the next merchant. Each DDoS subscription customer
layer or site. One of these runs over 90 checks receives an encrypted service to enhance
for fingerprinting the device, including whether it operational security and one year of 24/7

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
20 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Tracking ransomware payments
Criminal use of Tracking illicitly gained cryptocurrency
Ransomware is one of the largest sources of
cryptocurrencies illicitly gained cryptocurrency. In an effort to Curve
disrupt malicious technical infrastructure used in 72.19
ETH
As the adoption of cryptocurrency ransomware attacks—for example, the disruption
becomes mainstream, criminals are of Zloader in April 202211—Microsoft’s DCU
AscendEX.com
increasingly using it to evade law tracks criminal wallets to enable cryptocurrency
ETH AscendEX.com
enforcement and anti-money laundering tracking and recovery capabilities. 46.77 stolen funds
(AML) measures. This heightens the 2021-12-11
DCU investigators have observed ransomware
Uniswap V3
challenge for law enforcement to track actors evolving their communication tactics with
and trace cryptocurrency payments victims to conceal the money trail. Originally,
Using the cryptocurrency investigative tool Chainalysis, Microsoft’s Digital Crimes Unit discovered the AcendEX
to cybercriminals. cybercriminals included Bitcoin addresses in their hackers swapped their stolen funds at a smaller DEX called Curve in addition to Uniswap. This diagram illustrates
ransom notes. However, this made it easy to the laundering routes the team uncovered. Each circle represents a cluster of wallets and the numbers on each line
follow payment transactions on the blockchain, represent the total amount of Ethereum transmitted for laundering purposes.
Worldwide spending on blockchain solutions
so ransomware actors stopped including wallet
grew by approximately 340 percent over the last
addresses and instead appended email addresses
four years, while new cryptocurrency wallets grew cash-out options, such as centralized exchanges and force cybercriminals to use other obfuscation
or links to chat websites to communicate ransom
by around 270 percent. There are more than (CEX), peer-to-peer (P2P) and over the counter methods like coin tumbling or unlicensed
payment addresses to victims. Some actors
83 million unique wallets globally, and the total (OTC) exchanges. DEXes are an attractive exchanges. As an example, Uniswap recently
even created unique webpages and logins for
market capitalization of all cryptocurrencies was laundering location because they often do not announced it will start to use blacklists to block
each victim to prevent security researchers and
approximately $1.1 trillion USD as of July 28, 2022.10 follow AML measures. wallets known to be involved in illicit activities
law enforcement from obtaining the criminals’
from transacting on the exchange.15
In December 2021, hackers attacked the global
wallet addresses by pretending to be victims.
cryptocurrency trading platform AscendEx
Despite criminals’ efforts to hide their tracks, Actionable insights
and stole approximately $77.7 million USD in
some ransom payments can still be recovered
by working with law enforcement and crypto cryptocurrency belonging to its customers.12 1 If you are a victim of cybercrime who has
AscendEx hired blockchain analytics firms and paid the criminal using cryptocurrency,
analysis companies that can track movement
contacted other CEXs so the wallets receiving contact local law enforcement who might
on the blockchain.
stolen funds could be blacklisted. Additionally, be able to help track and recover lost funds.
Trending: DEX laundering of illicit proceeds addresses where the coins were sent were
2 Become familiar with the ALM measures
labeled as such on the Ethereum blockchain
A key issue for cybercriminals is the in place when selecting a DEX.
explorer Etherscan.13 In order to circumvent
conversion of cryptocurrency to fiat currency.
the alerting and blacklisting, the hackers sent Links to further information
Cybercriminals have several potential avenues
$1.5 million USD in Ethereum to Uniswap, one of
for conversion, each of which carries a different Hardware-based threat defense against
the world’s largest DEXs, on February 18, 2022.14
degree of risk. One method used to reduce risk increasingly complex cryptojackers |
is to launder proceeds through a decentralized The adoption of stronger AML measures by DEXs Microsoft 365 Defender Research Team
Source: Twitter.com—@PeckShieldAlert (PeckShield
exchange (DEX) before cashing out via available could blunt laundering activity on their platforms
is a China-based blockchain security company).

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
21 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
1hr 12m Microsoft detects millions of BEC emails every 5 31,000
The evolving phishing
month, equivalent to 0.6 percent of all phishing
emails observed. A report from IC318 published in
threat landscape The median time it takes for In addition to the URLs blocked
an attacker to access your May 2022 indicates an upward trend in exposed by Defender for Office, our Digital
private data if you fall victim losses due to BEC attacks. Crimes Unit directed the takedown
Credential phishing schemes are on to a phishing email.16 of 531,000 unique phishing URLs
The techniques used in phishing attacks
the rise and remain a substantial threat hosted outside of Microsoft.
continue to increase in complexity. In response
to users everywhere because they
1hr 42m to countermeasures, attackers adapt new ways
indiscriminately target all inboxes.
to implement their techniques and increase
Among the threats our researchers
the complexity of how and where they host
The median time for an attacker
track and protect against, the volume of
to begin moving laterally within campaign operation infrastructure. This means
phishing attacks is orders of magnitude
your corporate network once a organizations must regularly reassess their
greater than all other threats. device is compromised.17 strategy for implementing security solutions to
block malicious emails and strengthen access
Using data from Defender for Office, we see control for individual user accounts.
malicious email and compromised identity
activity. Azure Active Directory Identity
Protection provides still more information Detected phish emails
through compromised identity event alerts.
Using Defender for Cloud Apps, we see
Microsoft 365 credentials remain one of the most
compromised identity data access events, and
highly sought-after account types for attackers.
Microsoft 365 Defender (M365D) provides Once login credentials are compromised,
cross-product correlation. The lateral movement
attackers can log in to corporate-tied computer
metric comes from Defender for Endpoint (attack
systems to facilitate infection with malware and
behavior alerts and events), Defender for Office
ransomware, steal confidential company data
(malicious email) and again M365D for cross-
and information by accessing SharePoint files,
product correlation).
and continue the spread of phish by sending
additional malicious emails using Outlook,
among other actions.
In addition to campaigns with broader targets,
phishing for credentials, donations, and personal
information, attackers are targeting selective
businesses for larger payouts. Email phishing
710 million
attacks against businesses for financial gain
are collectively referred to as BEC attacks.
phishing emails blocked per week.
snoilliM
900
800
700
600
500
400
300
200
100
0
1202
luJ
1202
guA
1202
peS
1202
tcO
1202
voN
1202
ceD
2202
naJ
2202
beF
2202
raM
2202
rpA
2202
yaM
2202
nuJ
The number of phish detections per week continue to rise. The decrease in December–January is an expected
seasonal drop, also reported in last year’s report. Source: Exchange Online Protection signals.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
22 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Microsoft accounts remain a top target for
The evolving phishing Phishing emails with Ethereum wallet addresses
phishing operators, as evidenced by the
numerous phishing landing pages which
threat landscape
impersonate the Microsoft 365 login page.
For example, phishers attempt to match the
Continued
Microsoft login experience in their phish kits
We continue to observe a steady year-over-year by generating a unique URL customized to
increase in phishing emails. The shift to remote the recipient. This URL points to a malicious
work in 2020 and 2021 saw a substantial increase webpage developed to harvest credentials, but
in phishing attacks aiming to capitalize on the a parameter in the URL will contain the specific
changing work environment. Phish operators recipient’s email address. Once the target
are quick to adopt new email templates using navigates to the page, the phish kit will pre-
lures aligned with major world events such as populate user login data and a corporate logo
the COVID-19 pandemic and themes linked customized to the email recipient, mirroring the
to collaboration and productivity tools such appearance of the targeted company’s custom
as Google Drive or OneDrive file sharing. Microsoft 365 login page.
While COVID-19 themes have diminished, the
war in Ukraine became a new lure starting in Total emails detected as phish containing Ethereum wallet addresses increased at the start of the Ukraine-Russia
early March 2022. Our researchers observed a conflict and tapered off after the initial push. Phishing page impersonating a Microsoft
staggering increase of emails impersonating login with dynamic content
legitimate organizations soliciting cryptocurrency More than ever, phishers are relying on legitimate Large phish operations tend to use cloud
donations in Bitcoin and Ethereum, allegedly to infrastructure to operate, driving a rise in services and cloud virtual machines (VMs) to
support Ukrainian citizens. phishing campaigns aimed at compromising operationalize large scale attacks. Attackers can
Only a few days after the start of the war in various aspects of an operation so they do fully automate the process of deploying and
Ukraine in late February 2022, the number not have to purchase, host, or operate their delivering emails from VMs using SMTP
of detected phishing emails containing own. For example, malicious emails might email relays or cloud email infrastructure to
Ethereum addresses encountered across originate from compromised sender accounts. benefit from the high deliverability rates and
enterprise customers increased dramatically. Attackers benefit from using these email positive reputation of these legitimate services.
Total encounters peaked in the first week of addresses which have a higher reputation score If malicious email is allowed to be sent through
March when half a million phishing emails and are seen as more trustworthy than newly these cloud services, defenders must rely on
contained an Ethereum wallet address. Prior to created accounts and domains. In some more strong email filtering capabilities to block emails
the start of the war, the number of Ethereum advanced phishing campaigns, we observed from entering their environment.
wallet addresses across other emails detected attackers preferring to send and spoof from
as phish was significantly less, averaging a few domains which have DMARC19 incorrectly set up
thousand emails per day. with a “no action” policy, opening the door for
email spoofing.
sdnasuohT
600
500
400
300
200
100
0
1202
luJ
1202
guA
1202
peS
1202
tcO
1202
voN
1202
ceD
2202
naJ
2202
beF
2202
raM
2202
rpA
2202
yaM
2202
nuJ

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
23 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
BEC trends
Spotlight on business Actionable insights
As a point of entry, BEC attackers normally
email compromise attempt to start a conversation with potential Defending against phish
victims to establish rapport. Posing as a To reduce your organization’s exposure to phish, IT administrators
Cybercriminals are developing colleague or business acquaintance, the attacker are encouraged to implement the following policies and features:
increasingly complex schemes and gradually leads the conversation in the direction
techniques to defeat security settings of a monetary transfer. The introduction email, 1 Require the use of MFA across all accounts 6 Enable impersonation and
and target individuals, businesses, which we track as a BEC lure, represents close to to limit unauthorized access. spoofing protection features across
and organizations. We are investing 80 percent of detected BEC emails. Other trends your organization.
2 Enable conditional access features for
significant resources to further identified by Microsoft security researchers over highly privileged accounts to block 7 Configure DomainKeys Identified Mail
the past year include:
enhance our BEC enforcement access from countries, regions, and IPs (DKIM) and Domain-based Message
program in response. • The most frequently used techniques in BEC that do not typically generate traffic at Authentication Reporting & Conformance
attacks observed in 2022 were spoofing21 your organization. (DMARC) action policies to prevent
and impersonation.22 delivery of non-authenticated emails that
BEC is the costliest financial cybercrime, with an 3 Consider using physical security keys
estimated $2.4 billion USD in adjusted losses • The BEC subtype causing the most financial for executives, employees involved in might be spoofing reputable senders.
in 2021, representing more than 59 percent of damage to victims was invoice fraud (based on payment or purchase activities, and other 8 Audit tenant and user created allow
the top five internet crime losses globally.20 To volume and requested dollar amounts seen in privileged accounts. rules and remove broad domain and
understand the scope of the problem and how our BEC campaign investigations). IP based exceptions. These rules often
4 Enforce the use of browsers which support
best to protect users against BEC, Microsoft • Business information theft such as accounts take precedence and can allow known
services such as Microsoft SmartScreen
security researchers have been tracking the payable reports and customer contacts enable malicious emails through email filtering.
to analyze URLs for suspicious behaviors
most common themes used in attacks. attackers to craft convincing invoice fraud.
and blocks access to known malicious 9 Regularly run phishing simulators to
BEC themes (January–June 2022) • Most payroll redirection requests were sent websites.23 gauge the potential risk across your
from free email services and seldom from organization and to identify and educate
Gift card scam 1.9% compromised accounts. Email volume from 5 Use a machine-learning based security vulnerable users.
solution that quarantines high probability
these sources spiked around the first and
phish and detonates URLs and Links to further information
fifteenth of each month, the most common
Business information 4.3% attachments in a sandbox before email
pay dates. From cookie theft to BEC: Attackers use
reaches the inbox, such as Microsoft
AiTM phishing sites as entry point to
Payroll redirection 4.6% • Despite being well-known avenues for fraud, Defender for Office 365.24
further financial fraud | Microsoft 365
gift card scams comprised only 1.9 percent of
Defender Research Team, Microsoft
the BEC attacks detected.
Threat Intelligence Center (MSTIC)
Invoice fraud 9.3%
BEC lure 79.9%
BEC themes by percentage of occurrence

|     |     | Report  | The State of  | Nation State   | Devices and   | Cyber Influence  | Cyber  | Contributing  |
| --- | --- | ------- | ------------- | -------------- | ------------- | ---------------- | ------ | ------------- |
24 Microsoft Digital Defense Report 2022  Introduction Cybercrime  Threats Infrastructure Operations Resilience Teams
Progression of a BEC attack
Homoglyph deception
|     |     | Account compromised  |     |     |     |     |     | Fraud phase  |
| --- | --- | -------------------- | --- | --- | --- | --- | --- | ------------ |
BEC and phishing are common social
engineering tactics. Social engineering
plays a significant role in crime,
persuading a target to interact
with the criminal by gaining trust.
Target receives  Malicious link  Credentials  Account email  Establish  Imposter email
phishing email  to imposter  harvested  monitored  malicious  and wire fraud
In physical commerce, trademarks are used  Office 365  infrastructure
to secure trust in the origin of a product or
service, and counterfeit products are an abuse
of the trademark. Similarly, cybercriminals pose
A homoglyph in action
| as a contact familiar to the target during a  | Technique | % of domains showing  |     |     |     |     |     |     |
| --------------------------------------------- | --------- | --------------------- | --- | --- | --- | --- | --- | --- |
Actionable insights
|     |     | homoglyph technique  | A homoglyph domain that looks identical to a  |     |     |     |     |     |
| --- | --- | -------------------- | --------------------------------------------- | --- | --- | --- | --- | --- |
phishing attack, using homoglyphs to deceive
Enforce the use of browsers that support
potential victims.  sub l for I 25%  mail domain the victim recognizes is registered   1
|     |             |      | on a mail provider with a username that is  |     |     |     | services to analyze URLs for suspicious  |     |
| --- | ----------- | ---- | ------------------------------------------- | --- | --- | --- | ---------------------------------------- | --- |
|     | sub i for l | 12%  |                                             |     |     |     |                                          |     |
A homoglyph is a domain name used for email  identical. A hijacked email is then sent from the  behaviors and blocks access to known
communication in BEC, in which a character
sub q for g 7%  hijacked domain with new payment instructions.  malicious websites such as Safe Links
is replaced by one that is identical or nearly
and SmartScreen.25
|     | sub rn for m | 6%  | Leveraging open-source intelligence and  |     |     |     |     |     |
| --- | ------------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
identical in appearance, in order to deceive
the target.  sub .cam for .com 6%  access to email threads, the criminal identifies   2  Use a machine-learning based security
|     |             |     | individuals who have responsibility for  |     |     |     | solution that quarantines high probability  |     |
| --- | ----------- | --- | ---------------------------------------- | --- | --- | --- | ------------------------------------------- | --- |
|     | sub 0 for o | 5%  |                                          |     |     |     |                                             |     |
Homoglyph techniques used in BEC attempts  invoicing and payments. They then create  phish and detonates URLs and attachments
|     | sub ll for l | 3%  |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
BEC generally has two phases, the first of which  an impersonation of an email address of the  in a sandbox before email reaches the inbox.
|     | sub ii for i | 2%  | individual sending invoices. This impersonation  |     |     |     |     |     |
| --- | ------------ | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
involves compromise of credentials. These types  Links to further information
of credential leaks can be a result of phishing  sub vv for w 2%  is composed of an identical username and
|                                                  |              |     | mail domain that is a homoglyph of the  |     |     |     | Internet Crime Complaint Center (IC3) |  |     |
| ------------------------------------------------ | ------------ | --- | --------------------------------------- | --- | --- | --- | ---------------------------------------- | --- |
| attacks or large data breaches. The credentials  | sub l for ll | 2%  |                                         |     |     |     |                                          |     |
|                                                  |              |     | genuine sender.                         |     |     |     | Business Email Compromise:               |     |
are then sold or traded on the dark web.
|     | sub e for a | 2%  |     |     |     |     | The $43 Billion Scam  |     |
| --- | ----------- | --- | --- | --- | --- | --- | --------------------- | --- |
The second phase is the fraud phase,   The attacker copies an email chain containing
sub nn for m 1%  a legitimate invoice, then changes the invoice  Spoof intelligence insight—
where attackers use compromised credentials
to engage in sophisticated social engineering   sub ll for I, sub l for i 1%  to contain their own bank details. This new,  Office 365 | Microsoft Docs
modified invoice is then resent from the
using homoglyph email domains.  sub o for u 1%  Impersonation insight—
homoglyph impersonation email to the target.
Office 365 | Microsoft Docs
|     | Analysis of over 1,700 homoglyph domains between   |     | Because the context makes sense and the email  |     |     |     |     |     |
| --- | -------------------------------------------------- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
|     | January–July 2022. While 170 homoglyph techniques  |     | looks genuine, often the target follows the    |     |     |     |     |     |
were used, 75% of domains used just 14 techniques.
fraudulent instructions.

|     |     | Report  | TThhee  SSttaattee  ooff     | Nation State   | Devices and   | Cyber Influence  | Cyber   | Contributing  |
| --- | --- | ------- | ---------------------------- | -------------- | ------------- | ---------------- | ------- | ------------- |
25 Microsoft Digital Defense Report 2022  Introduction CCyybbeerrccrriimmee  Threats Infrastructure Operations Resilience Teams
Microsoft Digital Crimes Unit  Sirefef/Zero Access botnet  Continued focus on disruption
A timeline of botnet disruption from
is formed
Microsoft’s early days of collaboration
|     |     |     |     | Description: An advertising botnet  |     |     |     | Description: Microsoft disrupted  |
| --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --------------------------------- |
Collaboration: Designed to thwart
|     |     |     |     | designed to direct people to dangerous  |     |     |     | the infrastructure of seven  |
| --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | ---------------------------- |
cybercrime impacting the Microsoft
For more than a decade, DCU has worked to  websites that would install malware or  threat actors over the past year,
ecosystem through close integration
|                                                      |     |                                  |     | steal personal information; infected     |     |     |     | preventing them from distributing  |
| ---------------------------------------------------- | --- | -------------------------------- | --- | ---------------------------------------- | --- | --- | --- | ---------------------------------- |
| proactively stop cybercrime resulting in 26 malware  |     | across a team of investigators,  |     |                                          |     |     |     |                                    |
|                                                      |     |                                  |     | more than two million computers and      |     |     |     | additional malware, controlling    |
| and nation state disruptions. As the DCU team        |     | lawyers, and engineers.          |     |                                          |     |     |     |                                    |
|                                                      |     |                                  |     | cost advertisers more than $2.7 million  |     |     |     | victims’ computers, and targeting  |
| uses more advanced tactics and tools to shut down    |     | Microsoft approach: The goal is  |     |                                          |     |     |     |                                    |
|                                                      |     |                                  |     | USD per month; primarily in US and       |     |     |     | additional victims.                |
to better understand the technical
these illicit operations, we see the cybercriminals  Western Europe.  Collaboration: In partnership
aspects of various malware and
also evolve their approaches in an attempt to stay  Collaboration: Worked closely with  with internet service providers,
provide these insights to Microsoft’s
|                                                     |     |                                     |     | the FBI and Europol’s Cybercrime  |     |     |     | governments, law enforcement,    |
| --------------------------------------------------- | --- | ----------------------------------- | --- | --------------------------------- | --- | --- | --- | -------------------------------- |
| a step head. Here is a timeline showing a sample    |     | legal team to develop an effective  |     |                                   |     |     |     |                                  |
|                                                     |     |                                     |     | Center to bring down the peer-to- |     |     |     | and private industry, Microsoft  |
| of the botnets disrupted by DCU and the strategies  |     | disruption strategy.                |     |                                   |     |     |     |                                  |
|                                                     |     |                                     |     | peer infrastructure.              |     |     |     | shared information to remediate  |
Microsoft adopted to shut them down.
over 17 million malware
Microsoft response: Joined the Zero
victims worldwide.
Access network, replaced the criminal
C2 servers, and successfully seized
download server domains.
| 2008  | 2009  | 2011  |     | 2013  |     | 2019  |     | 2022  |
| ----- | ----- | ----- | --- | ----- | --- | ----- | --- | ----- |
Conficker botnet  Waledac botnet  Rustock botnet  Trickbot botnet  Looking ahead
Description: A fast-spreading worm  Description: A complex spam  Description: A backdoor trojan  Description: A sophisticated  DCU continues to innovate
targeting the Windows OS, infecting  botnet with US domains that  spam email bot using internet  botnet with fragmented  and is looking to use
millions of computers and devices in  collected email addresses and  providers as primary C2s; designed  infrastructure across the globe  its experience in botnet
a common network; created network  distributed spam that infected up to  to sell pharmaceuticals.  that targeted the financial services  disruptions to conduct
outages worldwide.  90,000 computers across the world.26  industry; compromised IoT devices.  coordinated operations
Collaboration: Microsoft
that go beyond malware.
Collaboration: Formation of  Collaboration: Creation of another  forged a partnership with Pfizer  Collaboration: Microsoft
Our continued success requires
the Conficker Working Group,  consortium, the Microsoft Malware  Pharmaceuticals to understand the  partnered with the Financial
creative engineering, sharing
the first consortium of its kind.  Protection Center (MMPC) with a  drugs sold by Rustock and worked  Services Information Sharing and
of information, innovative
Microsoft partnered with 16  focus on close collaboration with  closely with Dutch law enforcement  Analysis Center (FS-ISAC) to bring
legal theories, and public
organizations across the globe  academics.27  officials.29  down Trickbot.30
and private partnerships.
to defeat the bot.  Microsoft response: Microsoft  Microsoft response: Microsoft  Microsoft response: DCU built
Microsoft response: The  used tiered disruption approach  worked with US Marshalls and law  a system to identify and track
group collaborated across many  of C2 and surprised bad actors  enforcement in the Netherlands to  bot infrastructure and generated
international jurisdictions and was  by seizing US-based domains  take down the C2 servers in that  notifications for active internet
successful bringing Conficker down.  without notice.28 Microsoft granted  country. Registered and blocked  providers, taking into account
|     | temporary ownership of nearly 280   |     | all future domain generator  |     | specific laws in various countries.  |     |     |     |
| --- | ----------------------------------- | --- | ---------------------------- | --- | ------------------------------------ | --- | --- | --- |
|     | domains used by Waledac’s servers.  |     | algorithms (DGAs).           |     |                                      |     |     |     |

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
26 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
More specifically, we identified how Trickbot
Cybercriminal abuse
Trickbot attack chain
operators utilize compromised MikroTik routers
and reconfigure them to act as part of their C2
of infrastructure
infrastructure. The popularity of these devices
compounds the severity of their abuse by
Trickbot, and their unique hardware and software
Internet gateways Sets up
enable threat actors to evade traditional security Attacker Command malicious domains
as criminal command measures, expand their infrastructure, and and control
compromise more devices and networks.
and control infrastructure
IoT devices are becoming an increasingly Distribution of exposed MikroTik routers
popular target for cybercriminals using around the world
widespread botnets. When routers are
Number of exposed 93,868 1 Scans for MikroTik Steals device Executes traffic
unpatched and left exposed directly to
MikroTik routers Compromised devices that are exposed credentials and redirection
the internet, threat actors can abuse IoT device to the internet maintains persistence command
them to gain access to networks,
execute malicious attacks, and even
support their operations.
The Microsoft Defender for IoT team conducts Installs Trickbot on Performs recon Communicates with
research on equipment ranging from legacy target network to obtain network C2 via router; drops
Target
industrial control system controllers to cutting- network via a campaign information payloads, steals info
edge IoT sensors. The team investigates IoT- and
OT-specific malware to contribute to the shared
Exposed routers are at risk of having potential Trickbot attack chain showing the use of MikroTik IoT devices as proxy servers for C2.
list of indicators of compromise. vulnerabilities exploited.
redirects traffic between two ports in the router, Devices acting as reverse proxies for malware
Routers are particularly vulnerable attack vectors By tracking and analyzing traffic containing
establishing the line of communication between C2 are not just unique to Trickbot and MikroTik
because they are ubiquitous across internet- secure shell (SSH) commands, we observed
Trickbot-affected devices and the C2. routers. In collaboration with the Microsoft
connected homes and organizations. We have attackers using MikroTik routers to
RiskIQ team, we traced back to the C2 involved
been tracking the activity of MikroTik routers, a communicate with Trickbot infrastructure after We have aggregated our knowledge of the
and, through observing SSL certificates,
popular router around the world residentially and obtaining legitimate credentials to devices. various methods of attacking MikroTik devices,
identified Ubiquiti and LigoWave devices
commercially, identifying how they are utilized for These credentials can be obtained through brute beyond just Trickbot, as well as known common
that are impacted as well.32 This is a strong
command and control (C2), domain name system force attacks, exploiting known vulnerabilities vulnerabilities and exposures (CVEs) into an
indication that IoT devices are becoming active
(DNS) attacks, and crypto mining hijacking. with readily available patches, and using open-source tool for MikroTik devices, which can
components of nation state coordinated attacks
extract the forensic artifacts related to attacks on
default passwords. Once a device is accessed,
and a popular target for cybercriminals using
these devices.31
the attacker issues a unique command that
widespread botnets.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
27 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
In the past year, Microsoft observed a growing the next account—already prepared by scripts to
Crypto criminals Virtual machines as
number of attacks that abuse routers for be immediately activated—and their malicious
abusing IoT devices redirecting cryptocurrency mining efforts. criminal infrastructure activity continues with little to no interruption.
Cybercriminals compromise routers connected
Like cloud infrastructure, on-premises
Gateway devices are an increasingly to mining pools and redirect mining traffic The widespread move to the cloud
infrastructure can be used in attacks with
valuable target for threat actors as the to their associated IP addresses with DNS includes cybercriminals who leverage virtual local environments that are unknown to
poisoning attacks, which alters the DNS settings
number of known vulnerabilities has private assets of unwitting victims the on-premises user. This requires the initial
of targeted devices. Affected routers register
grown consistently from year to year. obtained through phishing or access point to remain open and accessible.
the wrong IP address to a given domain name,
They are being used for crypto mining distributing malware credential stealers. On-premises private assets have also been
sending their mining resources—or hashes—to
and other types of malicious activity. Many cybercriminals are choosing to abused by cybercriminals to initiate an onward
pools used by threat actors. These pools might
set up their malicious infrastructures chain of cloud infrastructure, set up to obfuscate
mine anonymous coins associated with criminal
their origin to avoid suspicious infrastructure
As cryptocurrency has become more popular, activities or use legitimate hashes generated by on cloud-based virtual machines (VMs),
creation detection.
many individuals and organizations have invested miners to acquire a percentage of the coin that containers, and microservices.
computational power and network resources they mined, thus reaping the rewards.
from devices such as routers to mine coins on Once the cybercriminal has access, a sequence of Actionable insights
the blockchain. However, mining cryptocurrency
events can occur to set up infrastructure—such
is a time- and resource-intensive process With more than half of known 1 Implement good cyber hygiene and
as a series of virtual machines through scripting
with a low probability of success. To increase vulnerabilities found in 2021 lacking a provide cybersecurity training for
and automated processes. These scripted,
employees with guidance for avoiding
the likelihood of mining a coin, miners pool patch, updating and securing routers automated processes are used to launch
being socially engineered.
together in distributed, cooperative networks,
on corporate and private networks malicious activity including large scale email
receiving hashes relative to the percentage of remains a significant challenge for spam attacks, phishing attacks, and web pages 2 Conduct regular automated user activity
the coin they succeeded in mining with their hosting nefarious content. It can even include anomaly checks through detections at
connected resources. device owners and administrators. setting up a scaled virtual environment carrying scale to help reduce these types of attacks.
out cryptocurrency mining, causing the end
3 Update and secure routers on corporate
Compromising devices for illegal crypto mining. victim a bill of hundreds of thousands of dollars
and private networks.
at the end of the month.
Portion of hashes from
Miners Cybercriminals understand their malicious activity
Criminal’s pool original pool are stolen
Pool Cryptocurrency has a limited life span before it is detected and
by threat actors, or
DNS Poisoning resources are transferred shut down. As a result, they have scaled up and
Miners
to their pool, or routers now operate proactively with contingencies top
have malware on them of mind. They have been observed preparing
Routers ASIC
that steal resources compromised accounts ahead of time and
Miners
for mining. monitoring their environments. As soon as an
Miner Miners
account (set up using hundreds of thousands of
DNS poisoning of gateway devices compromises legitimate mining activities and redirects resources virtual machines) is detected, they traverse to
to criminal mining activities.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
28 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
The rise of citizen hackers airports, and Czechia’s civil service server, even in place to stop these types of changes from
Is hacktivism
though Czechia is not directly involved in the occurring in the source file packages and users
Social media platforms enabled the rapid
war.35 At the same time, some governments should maintain awareness of potential impact.
here to stay? organization and mobilization of thousands
might use hacktivism as a cover for traditional
of would-be citizen hackers, who were
cyberespionage or sabotage operations—for
While hacktivism is not a new provided directions for conducting easily Social media platforms enabled the
example, Iranian activities against Israel.
executable attacks such as DDoS attacks.
phenomenon, the war in Ukraine saw organization and mobilization of
Organizers leveraged Twitter, Telegram, and In an environment of increased DDoS attacks
a surge of volunteer hackers, including thousands of would-be citizen hackers,
private forums to rally hackers, organize linked to hacktivism, the technology industry is
some directed by governments to deploy
operations, and disseminate hacking challenged to quickly decipher the difference who were provided directions for
cyber tools to damage the reputation
instruction manuals. between normal and abnormal traffic flow conducting easily executable attacks
or assets of political opponents,
to a website. Microsoft and its partners have
However, most of these hackers likely have such as DDoS attacks.
organizations, and even nation states.
developed a collection of tools which distinguish
limited skills, even with instruction. This suggests
malicious DDoS traffic and trace it back to its
two potential futures: one in which hundreds
In February 2022, the Ukrainian government or thousands of individuals with rudimentary origin. In addition, Microsoft’s Azure platform can
called on private civilians around the world technical capabilities use attack templates identify machines on the platform that produce Actionable insights
to conduct cyberattacks on Russia as part of to conduct future coordinated or individual extraordinarily high levels of outbound traffic 1 The technology industry must come
its 300,000 strong “IT Army.”33 At the same hacktivist attacks against targets, or a second and shut them down. together to design a comprehensive
time, established hacktivist groups such as future where the eventual end of hostilities response to this new threat.
Emergence of protestware
Anonymous, Ghostsec, Against the West, in Ukraine sees them leaving their hacktivism
Belarusian Cyber Partisans, and RaidForum2 behind, at least until the next political or social Protestware has emerged as a direct result of 2 Leading technology companies, including
began conducting attacks in support of Ukraine. issue inspires them to action. emotional reactions to the war between Russia Microsoft, have tools to identify malicious
Other groups, including some of the Conti and Ukraine. Some open source software traffic associated with DDoS attacks and
ransomware gang, sided with Russia.34 Politicization of hackers developers used the popularity of their software disable the responsible machines.
as a means to speak up or take action against
In the months that followed, Anonymous’s The greater risk posed by this political 3 Open source users should keep a
an unfolding geopolitical situation. This included
activities were highly visible. Hackers acting mobilization is the deployment of tech-savvy heightened watch during times of
harmless text files opened on a desktop or a
in the group’s name—or in that of one of its hackers who might continue to conduct geopolitical strife.
browser to spread messages of peace, but also
affiliates—temporarily disabled thousands of cyberattacks against foreign government targets
included targeted attacks based on IP address
Russian and Belarusian websites, leaked hundreds to support their own national priorities, either
geolocation and destructive actions such as
of gigabytes of stolen data, hacked Russian TV on a self-initiated basis or at the behest of
wiping a hard drive. As other global events
channels to play pro-Ukrainian content, and their government.
unfold, we can expect to see protestware surface
even offered to pay Bitcoin for surrendered Iran, China, and Russia already use hacktivism again in the future. Since these are generally
Russian tanks. as a feeder for recruitment into their state cases where well-respected open-source
hacking groups. For example, in April 2022, the maintainers are deciding to make personal
pro-Russian hacking group Killnet launched statements using their own open source
DDoS attacks against Czech railroads, regional components, there is currently no protection

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
29 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Endnotes
1 https://www.reuters.com/business/energy/shell-re-routes-oil-supplies-after-cyberattack- 18 https://www.ic3.gov/Media/Y2022/PSA220504
german-logistics-firm-2022-02-01/ 19 Domain-based Message Authentication, Reporting and Conformance: An email authentication,
2 https://www.bleepingcomputer.com/news/security/greeces-public-postal-service-offline-due-to- policy, and reporting protocol designed to give email domain owners the ability to protect their
ransomware-attack/ domain from unauthorized use.
3 https://www.bleepingcomputer.com/news/security/costa-rica-s-public-health-agency-hit-by- 20 https://www.ic3.gov/Media/PDF/AnnualReport/2021_IC3Report.pdf
hive-ransomware/; https://www.reuters.com/world/americas/cyber-attack-costa-rica-grows- 21 https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/learn-about-spoof-
more-agencies-hit-president-says-2022-05-16/ intelligence?view=o365-worldwide
4 https://www.bleepingcomputer.com/news/security/spicejet-airline-passengers-stranded-after- 22 https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/impersonation-
ransomware-attack/ insight?view=o365-worldwide
5 https://www.microsoft.com/security/blog/2020/03/05/human-operated-ransomware-attacks-a- 23 https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-
preventable-disaster/ smartscreen/microsoft-defender-smartscreen-overview
6 Endpoint detection and response. https://www.microsoft.com/en-us/security/business/threat-protection/ 24 https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-office-365
7 https://www.washingtonpost.com/national-security/cyber-command-revil- 25 https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-
ransomware/2021/11/03/528e03e6-3517-11ec-9bc4-86107e7b0ab1_story.html smartscreen/microsoft-defender-smartscreen-overview
8 https://www.bbc.com/news/technology-59998925 26 Microsoft Corporation v. John Does 1-27, et. al., No. 1:10CV156, (E.D.Va. Feb 22, 2010).
9 A Vetted Forum is an online discussion forum that requires an existing member to vouch for the 27 See Bowden, Mark. Worm: The First Digital World War. Grove/Atlantic, Inc., Sep 27, 2011.
addition of a new member.
28 Specifically, Rule 65 of the Federal Rules of Civil Procedure allows a party to seek such remedy if: 1) the
10 https://www.statista.com/statistics/800426/worldwide-blockchain-solutions-spending/; party will suffer immediate and irreparable harm if the relief is not granted, and 2) the party attempts
https://www.blockchain.com/charts/my-wallet-n-users; https://coinmarketcap.com to provide the other side notice in a timely manner. Moreover, the law requires that a balancing test be
11 https://blogs.microsoft.com/on-the-issues/2022/04/13/zloader-botnet-disrupted-malware-ukraine/ applied, one which balances the defendant’s right to notice against the quantum of harm to the public.
12 https://www.coindesk.com/business/2021/12/13/crypto-exchange-ascendex-hacked-losses- 29 Microsoft Corporation v. John Does 1-11, et. al., No. 2:11cv222, (W.D. Wa. Feb 9, 2011).
estimated-at-77m/ ; https://www.zdnet.com/article/after-77-million-hack-crypto-platform- 30 Microsoft Corp. v. Does, No. 1:20-cv-01171 (AJT/IDD), 2021 U.S. Dist. LEXIS 258143, at *1
ascendex-to-reimburse-customers/ (E.D. Va. Aug. 12, 2021).
13 https://etherscan.io/address/0x73326b6764187b7176ed3c00109ddc1e6264eb8b 31 https://github.com/microsoft/routeros-scanner
14 https://finance.yahoo.com/news/ethereum-worth-over-1-5m-160249300.html 32 RiskIQ: Ubiquiti Devices Compromised and Used as Malware C2 Reverse Proxies | RiskIQ
15 https://news.bitcoin.com/decentralized-finance-crypto-exchange-uniswap-starts-blocking- Community Edition
addresses-linked-to-blocked-activities/ 33 https://www.theguardian.com/world/2022/mar/18/amateur-hackers-warned-against-joining-
16 Data source: Defender for Office (malicious email/compromised identity activity), Azure Active ukraines-it-army
Directory Identity Protection (compromised identity events/alerts), Defender for Cloud Apps 34 https://therecord.media/russia-or-ukraine-hacking-groups-take-sides/
(compromised identity data access events), and M365D (cross product correlation).
35 https://www.expats.cz/czech-news/article/pro-russian-hackers-target-czech-websites-in-a-
17 Data source: Defender for Endpoint (attack behavior alerts/events), Defender for Office series-of-attacks
(malicious email), and M365D (cross product correlation).

|     | Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber  | Contributing  |     |
| --- | ------- | -------------- | -------------- | ------------- | ---------------- | ------ | ------------- | --- |
30 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats  Infrastructure Operations Resilience Teams
Nation State
|          |     |     |     |     |     | An overview of Nation State Threats  |     | 31  |
| -------- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- |
|          |     |     |     |     |     | Introduction                         |     | 32  |
| Threats  |     |     |     |     |     | Background on nation state data      |     | 33  |
Sample of nation state actors and
|     |     |     |     |     |     | their activities                |     | 34  |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- |
|     |     |     |     |     |     | The evolving threat landscape   |     | 35  |
Nation state actors are launching increasingly   The IT supply chain as a gateway
|     |     |     |     |     |     | to the digital ecosystem   |     | 37  |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
sophisticated cyberattacks to evade detection
and further their strategic priorities.  Rapid vulnerability exploitation  39
Russian state actors’ wartime cyber
|     |     |     |     |     |     | tactics threaten Ukraine and beyond   |     | 41  |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- |
China expanding global targeting
|     |     |     |     |     |     | for competitive advantage   |     | 44  |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
Iran growing increasingly aggressive
|     |     |     |     |     |     | following power transition  |     | 46  |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
North Korean cyber capabilities employed
|     |     |     |     |     |     | to achieve regime’s three main goals  |     | 49  |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- |
Cyber mercenaries threaten
|     |     |     |     |     |     | the stability of cyberspace   |     | 52  |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- |
Operationalizing cybersecurity norms
|     |     |     |     |     |     | for peace and security in cyberspace  |     | 53  |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- |

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
31 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
An overview of Ukraine responded by rapidly moving workloads
Increased targeting of critical Iran grew increasingly aggressive
and data to hyperscale clouds hosted in data
Nation State Threats infrastructure particularly IT sector, following power transition, expanded
centers outside Ukraine. Second, advances in
financial services, transportation systems, ransomware attacks beyond regional
cyber threat intelligence and endpoint protection
and communications infrastructure. adversaries to US and EU victims,
powered by the data and advanced AI and ML
Nation state actors are and targeted high profile US critical
services in the cloud have helped Ukraine defend
Find out more on p35 infrastructure.
launching increasingly against Russian cyberattacks.
Find out more on p46
sophisticated cyberattacks Elsewhere, nation state actors have increased
IT supply chain being
activity and are using advancements in
to evade detection and further automation, cloud infrastructure, and remote used as a gateway to Identification and rapid exploitation of
access targets.
their strategic priorities. access technologies to attack a wider set unpatched vulnerabilities has become a Risk
of targets. Corporate IT supply chains that key tactic. Rapid deployment of security
The advent of cyberweapon enable access to ultimate targets were NOBELIUM updates is key to defense.
frequently attacked. Cyber security hygiene
deployment in the hybrid
became even more critical as actors rapidly
war in Ukraine is the dawn exploited unpatched vulnerabilities, used both Find out more on p36 Vulnerability
sophisticated and brute force techniques to steal publicly
of a new age of conflict. disclosed
credentials, and obfuscated their operations
by using opensource or legitimate software. China expanding 14 days 60 days 120 days
Days
And Iran joins Russia in use of destructive global targeting
Russia has also supported its war with Patch Exploitation POC code released Available in
cyberweapons, including ransomware, especially smaller released in wild on GitHub scanning tools
information influence operations, using
as a staple of their attacks. nations in Find out more on p39
propaganda to impact opinions in Russia, in
Southeast
Ukraine, and globally. This first full-scale hybrid These developments require urgent adoption
Asia, to gain
conflict has taught other important lessons. of a consistent, global framework that prioritizes North Korea targeted defense and aerospace
intelligence
First, the security of digital operations and data human rights and protects people from reckless companies, cryptocurrency, news outlets,
and competitive
can be best protected – both in cyberspace state behavior online. All nations must work to defectors, and aid organizations, to achieve
advantage.
and in physical space – by moving to the cloud. implement agreed upon norms and rules for regime’s goals: to build defense, bolster the
Initial Russian attacks targeted on-premises responsible state conduct. economy, and ensure domestic stability.
services with wiper malware, and targeted
Defending Ukraine: Early Lessons from
physical data centers with one of the first
the Cyber War — Microsoft On the Issues Find out more on p44 Find out more on p49
missiles launched.
Cyber mercenaries threaten the stability of cyberspace as this growing industry of
private companies is developing and selling advanced tools, techniques, and services
to enable their clients (often governments) to break into networks and devices.
Find out more on p52

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
32 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Much like enterprise organizations, adversaries For the first time in a major cyber event, As a result, maintaining a strong baseline of IT
Introduction
began using advancements in automation, cloud behavioral detections leveraging machine security hygiene through prioritized patching,
infrastructure, and remote access technologies learning used known attack patterns to enabling anti-tamper features, using attack
to extend their attacks against a wider set of successfully identify and stop further attacks surface management tools like RiskIQ to get
Following high-profile
targets. These tactical adjustments resulted in without prior knowledge of the underlying an outside-in view of an attack surface, and
attacks in 2020 and 2021, new approaches and large scale attacks against malware—even before humans were aware enabling multifactor authentication across
corporate supply chains. IT security hygiene of the threats. We also confirmed the value the full enterprise have become baseline
nation state threat actors took on an even higher degree of importance of sharing threat intelligence in real-time with fundamentals to proactively defend against
as actors developed new ways to rapidly exploit defenders protecting these systems, giving many sophisticated actors.
spent significant resources
unpatched vulnerabilities, expanded techniques them vital information to anticipate and
Nation state actors have also increased
adapting to new security for compromising corporate networks, and defend against active attacks.
use of ransomware as a tactic in their attacks,
obfuscated their operations by using opensource
protections implemented Nation state threat actors around the world often reusing ransom malware created by that
or legitimate software. New attack techniques
continue to expand their operations in new criminal ecosystem in their attacks. We have
by organizations to defend provided new and harder-to-detect vectors
and old ways. China, North Korea, Iran, and seen both Iran- and North Korea-based actors,
to gain access to a target’s network. Finally,
Russia all carried out attacks on Microsoft leveraging commodity ransomware tools to
against sophisticated threats.
as wartime physical attacks escalated, we
customers. The IT services supply chain became damage targeted systems, often including
saw cyberattacks take a prominent role in
a common target as actors shifted the focus critical infrastructure, within regional rivals.
military activity.
to upstream services that can be access points Finally, we have seen the growing threat of
The conflict in Ukraine has provided an all- to multiple organizations. We expect actors cyber mercenaries developing and selling
too-poignant example of how cyberattacks to continue to exploit trusted relationships tools, techniques, and services to extend
evolve to impact the world in parallel with in enterprise supply chains, emphasizing the exploits against vulnerable third-party solutions.
military conflict on the ground. Power systems, importance of comprehensive enforcement The sophistication and agility of attacks by nation
telecommunication systems, media, and of authentication rules, diligent patching, state actors will continue to evolve each year.
other critical infrastructure all became targets and account configuration for remote access Organizations must respond by being informed
of both physical attacks and cyberattacks. infrastructure, and frequent audits of partner of these actor changes and evolve defenses
Network compromise attempts commonly relationships to verify authenticity. in parallel.
observed as part of espionage and information
Nation state actors, much like ransomware and John Lambert
exfiltration campaigns became focused in hybrid
criminal operators, have responded to increased Corporate Vice President and Distinguished
war on destructive wiper malware attacks against
exposure by moving toward targeting poorly Engineer, Microsoft Threat Intelligence Center
critical infrastructure systems. Connecting the
configured or unpatched enterprise systems
security of these systems to the cloud resulted
(VPN/VPS infrastructure, on-premises servers,
in early detection and disruption of potentially
third-party software) to perform living-off-
devastating attacks.1
the-land attacks. Many have increased use of
commodity malware and open source red team
tools to obfuscate their malicious activity.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
33 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Background on
nation state data
Nation state threats are cyber threat
activities that originate in a specific country
with the apparent intent of furthering
national interests. Nation state actors
present some of the most advanced and
persistent threats our customers face,
including intellectual property theft,
espionage, surveillance, credential theft,
destructive attacks, and more.
We invest significant resources in discovering,
understanding, and countering these threats.
When an organization or individual account
holder is targeted or compromised by observed
nation state activities, Microsoft delivers an
alert in the form of a nation state notification
(NSN) directly to the customer, including the
information they need to investigate the activity.
As of June 2022, we had delivered over 67,000
NSNs since we began in 2018.
Microsoft NSN alert data are presented in
The four primary nation states whose threat Microsoft identifies nation state groups by Once it meets the criteria, a DEV is converted
this chapter to provide a view of measurable
groups we include in this report are Russia, chemical element names (such as NOBELIUM), to a named actor or merged with existing actors.
activity. The level of nation state activity shown
China, Iran, and North Korea. These represent just some of which are shown on the following Throughout this chapter, we cite examples of
in the charts is based on the number of NSNs
the countries of origin for the most commonly page. We use DEV-#### designations as a nation state and DEV groups to provide a deeper
Microsoft issued to customers in response to
observed actors targeting Microsoft customers temporary name given to an unknown, emerging, view into attack targets, techniques, and analysis
the detection of nation state actors targeting
over the past year. The report also includes our or developing cluster of threat activity, allowing of motivations. Although many of these groups
or compromising at least one account in the
observations about threat groups from Lebanon us to track it as a unique set of information until use the same tools as cybercriminals, they
customer organization.
and from cyber mercenaries, or private sector we reach a high degree of confidence about the present unique threats in the form of bespoke
offensive actors for hire. origin or identity of the actor behind the activity. malware, the ability to discover and capitalize
on zero-day vulnerabilities, and legal impunity.

|     |     |     |     |     | Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber   | Contributing  |     |
| --- | --- | --- | --- | --- | ------- | -------------- | -------------- | ------------- | ---------------- | ------- | ------------- | --- |
34 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats  Infrastructure Operations Resilience Teams
Sample of nation state actors and their activities  Iran
Russia
Media, human rights
P
activists, politicians,
and US transportation
|     | IT, government,  |     | Ukrainian government,  |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and energy
| No  | think tanks,  | Ac  | military, law  |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PHOSPHORUS
|     | higher  |     | enforcement |     |     |     |     |     |     |     |     | Charming Kitten |
| --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |
education
Gamaredon
| NOBELIUM |     | ACTINIUM |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
APT29
|     |     |     |     |     | Lebanon |     |     |     |     |     |     | IT, shipping  |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | ------------- |
Bh
companies, Middle
East governments
|     | Government,  |     | Energy, aviation, critical  |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sr  |              | Br  |                             |     |     |     |     |     |     |     |     |     |
d e f en s e ,  t h in k   m an u f a c t u r in g, defense  I sr a e li   d e f e nse  BOHRIUM Tortoiseshell
Po
|     | ta n k s,  h i g h e r   |     | ind u st r i a l  b a | se  |     | in d u s t r y ,  I T |     |     |     |     |     |     |
| --- | ------------------------ | --- | --------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
education
| STRONTIUM |     |     | EnergeticBear |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
BROMINE
|     | Fancy Bear |     |     |     | POLONIUM |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
North Korea
Intelligence/
| Sg  | Defense   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Science and
|     | personnel, think  |     |     |     |     |     |     |     |     |     | Pu  |     |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
technology,
tanks
defense, industrial
SEABORGIUM
Callisto Group
|     |     |     | China |     |     |     |     |     |     |     | PLUTONIUM | Andariel, Dark Seoul,  |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------------------- |
Silent Chollima
Critical
Ir
infrastructure,  Government,  Government.   Government,  Think tanks,
|     |     |     | Ra  |     | Ni  |     |     |     | Ce  |     | Os  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
operational   education,  NGOs defense, energy,  academics,
|         | technology |     |        | defense |        |             |     |     |        | aerospace  |        | NGOs, government |
| ------- | ---------- | --- | ------ | ------- | ------ | ----------- | --- | --- | ------ | ---------- | ------ | ---------------- |
| IRIDIUM |            |     |        |         |        | APT15       |     |     |        |            |        |                  |
|         | Sandworm   |     |        |         |        | Vixen Panda |     |     |        |            |        |  Konni           |
|         |            |     | RADIUM |         | NICKEL |             |     |     | CERIUM |            | OSMIUM |                  |
Key  Communications  Telecommunications,  Cryptocurrency and  Government,
|     | Commonly  |     | Ga  |     | Gd  |     |     |     | Cn  |     | Zn  |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Symbol  infrastructure,  NGOs, government related technology  defense, science
targeted sectors
|           |                   |     |         | IT, government,  |            |       |     |     |             | companies   |      | and technology |
| --------- | ----------------- | --- | ------- | ---------------- | ---------- | ----- | --- | --- | ----------- | ----------- | ---- | -------------- |
|           | I n d u s t ry    |     |         |                  |            | APT40 |     |     |             |             |      |                |
| ACTIVITY  |                   |     |         | education        |            |       |     |     |             | APT38,      |      | Lazarus        |
|           | r e fe r e n ce s |     | GALLIUM |                  | GADOLINIUM |       |     |     | COPERNICIUM |             | ZINC |                |
| GROUP     |                   |     |         |                  |            |       |     |     |             | Beagle Boyz |      |                |
SoftCell

|     |     | Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber   | Contributing  |     |     |
| --- | --- | ------- | -------------- | -------------- | ------------- | ---------------- | ------- | ------------- | --- | --- |
35 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats  Infrastructure Operations Resilience Teams
Political developments in the past year have
 The evolving   Industry sectors targeted by nation state actors
shaped the priorities and risk tolerance of
state-sponsored threat groups worldwide.
|  threat landscape   |     |     |     | Communications |     | Other |     |     |     |     |
| ------------------- | --- | --- | --- | -------------- | --- | ----- | --- | --- | --- | --- |
As geopolitical relationships have broken
|     |     |     |     | 2%  |     | 20% |     |     | Information technology |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- |
down and hawkish elements have acquired
Microsoft’s mission to track nation state
|     | more control in some nations, cyber actors  |     |     |     |     |     |     |     |     | 22% |
| --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Intergovernmental
actor activity and notify customers
|                                     | have become more brazen and aggressive.  |     |     | organizations |     |     |     |     |     |     |
| ----------------------------------- | ---------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| when we see them being targeted or  | For example:                             |     |     |               |     |     |     |     |     |     |
2%
compromised is rooted in our mission
•  Russia relentlessly targeted the Ukrainian
| to protect our customers from attacks.  |     |     | Transportation |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
government and the country’s critical
infrastructure to complement its on-the-
2%
| This notification is a crucial part of our  | ground military action.2  |     |            |     |     |     |     |     |     |     |
| ------------------------------------------- | ------------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| commitment to informing customers whether   |                           |     | Healthcare |     |     |     |     |     |     |     |
•  Iran aggressively sought inroads into US
observed attacks are successfully prevented
|     | critical infrastructure such as port authorities.  |     | 2%  |     |     |     |     |     |     |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by our security product protections, or if the
•  North Korea continued its campaign of
attacks are effective because of unknown
|     |     |     |     | Media |     |     |     |     | Think tanks/NGOs |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | ---------------- | --- |
stealing cryptocurrency from financial and
security weaknesses. Tracking notifications over
|     | technology companies.  |     | 4%  |     |     |     |     |     |     | 17% |
| --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
time helps Microsoft identify evolving threat
| trends by actors and focus product protections  | •  China expanded its global  |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Finance
cyberespionage operations.
on proactively mitigating threats to customers
|                             |     |     |     |     | Government |     |     | Education |     |     |
| --------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --------- | --- | --- |
| across our cloud services.  |     |     |     | 5%  |            |     |     |           |     |     |
Although nation state actors can be technically
10%
|     | sophisticated and employ a wide variety of  |     |     |     |     |     |     |     | 14% |     |
| --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This tracking also allows us to share data
| and insights about what we see. The analysts  | tactics, their attacks can often be mitigated by  |     |     |     |     |     |     |     |     |     |
| --------------------------------------------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tracking these actors and following their attacks  good cyber hygiene. Many of these actors rely on  Nation state groups targeted a range of sectors. Russian and Iranian state actors targeted the IT industry as a
means to access the IT firms’ customers. Think tanks, nongovernmental organizations (NGOs), universities, and
| rely on a combination of technical indicators  | relatively low-tech means, such as spear-phishing  |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
government agencies remained other common targets of nation state actors.
| and geopolitical expertise to understand  | emails, to deliver sophisticated malware instead  |     |     |     |     |     |     |     |     |     |
| ----------------------------------------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of investing in developing customized exploits
the motivations of the actors, combining
technical and global context into new insights.  or using targeted social engineering to achieve  Nation state actors have a variety of objectives  or potentially execute attacks on a much larger
This curation provides a unique view into the  their objectives.  that can result in targeting specific groups  scale by compromising hundreds of downstream
|     |     |     | of organizations or individuals. In the last  |     |     |     | customers in one attack. After the IT sector, the  |     |     |     |
| --- | --- | --- | --------------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
priorities of nation state cyber actors and how
their motivations might mirror the political,  year, supply chain attacks have increased,  most frequently targeted entities were think
|     |     |     | with a particular focus on IT companies.  |     |     |     | tanks, academics attached to universities, and  |     |     |     |
| --- | --- | --- | ----------------------------------------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- |
military, and economic priorities of the nation
states employing them.  By compromising IT service providers, threat  government officials. These are desirable “soft
|     |     |     | actors are often able to reach their original   |     |     |     | targets” for espionage to collect intelligence   |     |     |     |
| --- | --- | --- | ----------------------------------------------- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
|     |     |     | target through a trusted relationship with the  |     |     |     | on geopolitical issues.                          |     |     |     |
company that manages connected systems,

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
36 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Continued
Critical infrastructure trends
34% 18% 20% 40%
1000 45
40
800
35
30
600
25
%
20
400
15
10
200
5
0 0
Jul 2018–Jun 2019 Jul 2019–Jun 2020 Jul 2020–Jun 2021 Jul 2021–Jun 2022
Critical infrastructure Noncritical infrastructure Percentage critical infrastructure of total NSNs
sNSN
The evolving threat landscape
Nation state actors’ geographic targeting
Most
Least
Nation state groups’ targeting of critical infrastructure3 increased in the past year, with actors’ focusing on Nation state groups’ cyber targeting spanned the
Actionable insights
companies in the IT sector, financial services, transportation systems, and communications infrastructure. globe this past year, with a particularly heavy focus on
US and British enterprises. Organizations in Israel, the
1 Identify and protect your potential high-
UAE, Canada, Germany, India, Switzerland, and Japan
value data targets, at-risk technologies,
were also among some of the most frequently targeted,
“B efore the invasion of Ukraine, governments thought that information, and business operations
according to our NSN data.
data needed to stay inside a country in order to be secure. which might align with the strategic
priorities of nation state groups.
After the invasion, migrating data to the cloud and moving
outside territorial borders is now a part of resiliency 2 Enable cloud protections to provide
planning and good governance.” identification and mitigation of known
and novel threats to your network at scale.
Cristin Flynn Goodwin,
Associate General Counsel, Customer Security & Trust

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
37 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
NOBELIUM demonstrated how a “compromise
The IT supply chain
Approaches to compromise
one to compromise many” approach could
–
as a gateway to the be directed against a perceived geopolitical Path 1
adversary. This past year, the threat actor pursued –
digital ecosystem both third-party and direct intrusions into
Path 2
sensitive organizations based in member states Social engineering
of the North Atlantic Treaty Organization (NATO),
Nation state targeting of IT service
which the Russian government perceives as an IT provider/Cloud Managed services
providers might enable the threat actors
existential threat. Between July 2021 and early services provider provider/Cloud
to exploit other organizations of interest
June 2022, 48 percent of Microsoft’s customer services provider
by taking advantage of trust and access notifications of Russian threat activity against
granted to these supply chain providers. online services customers went to IT sector
Stolen credentials
In the past year, nation state cyber threat firms based in NATO member countries, likely as
from on-premises
groups targeted IT services providers to intermediary access points. Overall, 90 percent
attack third-party targets and gain access of notifications about Russian threat activity Cloud
to downstream clients in government, during the same period went to customers based services provider
policy, and critical infrastructure sectors. in NATO member states, primarily in the IT, NOBELIUM
think tanks and nongovernmental organizations
(NGOs), and government sectors, suggesting
Azure active directory trust relationship
IT service providers are attractive intermediary
a strategy of pursuing multiple means of initial
targets as they serve hundreds of direct and
access to these targets.
thousands of indirect clients of interest to
foreign intelligence services. If exploited, the On-premises access
routine business practices and the delegated There has been a shift from
administrative privileges these firms enjoy, might exploiting the software supply chain IT provider Government
allow malicious actors to access and manipulate to exploiting the IT services supply target #1
IT service provider client networks without
chain, targeting cloud solutions and
immediately triggering alerts.
managed services providers to reach Remote access solutions
In the past year, NOBELIUM attempted to
downstream customers.
compromise and leverage privileged accounts
Managed services Government
at cloud solutions and other managed services
provider target #2
providers to attempt targeted downstream
access into primarily US and European
government and policy customers.
This diagram depicts NOBELIUM’s multi-vectored approach to compromising its ultimate targets and the collateral
damage to other victims along the way. In addition to the actions shown above, NOBELIUM launched password
spray and phishing attacks against the entities involved, even targeting the personal account of at least one
government employee as another potential route to compromise.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
38 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
• In January 2022, DEV-0198, a group we Conducting a thorough review and audit
The IT supply chain
Actionable insights
assess is affiliated with the government of of partner relationships helps minimize any
as a gateway to the Iran, compromised an Israeli cloud solutions unnecessary permissions between your 1 Review and audit upstream and downstream
provider. Microsoft assesses the actor organization and upstream providers and service provider relationships and delegated
digital ecosystem likely used compromised credentials from immediately remove access for any relationships privilege accesses to minimize unnecessary
the provider to authenticate into an Israeli that look unfamiliar. Increasing familiarity with permissions. Remove access for any partner
Continued logistics company. MSTIC observed the same activity logs and reviewing available activity relationships that look unfamiliar or have not
actor attempting to conduct a destructive makes it easier to spot anomalies that could yet been audited.6
Throughout the year, Microsoft Threat cyberattack against the logistics company spark further investigation.
Intelligence Center (MSTIC) detected an later that month. 2 Enable logging and review all authentication
increasing number of Iranian state and Iran- activity for remote access infrastructure and
• In April 2022, POLONIUM, a Lebanon-based Nation state targeting of third parties
affiliated actors compromising IT companies. virtual private networks (VPNs), with a focus
group we assess collaborated with Iranian
In many cases, actors were detected stealing enables them to exploit sensitive on accounts configured with single factor
state groups on IT supply chain techniques,
sign-in credentials to gain access to downstream organizations by taking advantage authentication, to confirm authenticity and
compromised another Israeli IT company
clients for a range of objectives, from intelligence investigate anomalous activity.
to gain access to Israeli defense and legal of trust and access in a supply chain.
collection to retaliatory destructive attacks.
organizations.5 3 Enable MFA for all accounts (including
• In July and August 2021, DEV-0228 service accounts) and ensure MFA is
This past year of activity demonstrates that
compromised an Israeli business software enforced for all remote connectivity.
threat actors like NOBELIUM and DEV-0228
provider to later compromise downstream
are getting to know the landscape of an 4 Use passwordless solutions to
customers in the Israeli defense, energy,
organization’s trusted relationships better than secure accounts.7
and legal sectors.4
the organizations themselves. This increased
Links to further information
• From August to September 2021, Microsoft threat emphasizes the need for organizations
detected a spike in Iranian state actors to understand and harden the borders and entry NOBELIUM targeting delegated
targeting IT companies based in India. The lack points of their digital estates. It also underscores administrative privileges to facilitate
of pressing geopolitical issues that would have the importance for IT service providers to broader attacks | Microsoft Threat
prompted such a shift suggests this targeting rigorously monitor their own cybersecurity Intelligence Center (MSTIC)
is for indirect access to subsidiaries and clients health. For example, organizations should
Iranian targeting of IT sector on the rise
outside India. implement multifactor authentication and
| Microsoft Threat Intelligence Center
conditional access policies that make it harder
(MSTIC), Microsoft Digital Security Unit
for malicious actors to capture privileged
accounts or spread throughout a network. Exposing POLONIUM activity and
infrastructure targeting Israeli
organizations | Microsoft Threat
Intelligence Center (MSTIC)

|     |     |     | Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber   | Contributing  |     |
| --- | --- | --- | ------- | -------------- | -------------- | ------------- | ---------------- | ------- | ------------- | --- |
39 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats  Infrastructure Operations Resilience Teams
This ensures that vulnerabilities are identified,
 Rapid vulnerability
Speed and scale of vulnerability commoditization
and patches developed in a timely manner
Risk
to protect customers from previously
 exploitation
unknown threats.
| As organizations strengthen their  | Many organizations assume they are less likely  |     |     |     |     |     |     |     |     |     |
| ---------------------------------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to be a victim of zero-day exploit attacks if
cybersecurity postures, nation state
vulnerability management is integral to their
actors respond by pursuing new and
network security. However, the commoditization
| unique tactics to deliver attacks and    |                                                |     |     |     | Vulnerability  |     |     |     |     |     |
| ---------------------------------------- | ---------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
|                                          | of exploits is leading them to come at a much  |     |     |     | publicly       |     |     |     |     |     |
| evade detection. The identification and  |                                                |     |     |     | disclosed      |     |     |     |     |     |
faster rate. Zero-day exploits are often discovered
exploitation of previously unknown
by other actors and reused broadly in a short
| vulnerabilities—known as zero-day  |     |     |     |     |     | 14 days | 60 days |     |     | 120 days |
| ---------------------------------- | --- | --- | --- | --- | --- | ------- | ------- | --- | --- | -------- |
period of time, leaving unpatched systems at  Days
| vulnerabilities—is a key tactic in this effort.  | risk. Even though zero-day exploitation can be  |     |     |     |                    |     |                    |     |     |              |
| ------------------------------------------------ | ----------------------------------------------- | --- | --- | --- | ------------------ | --- | ------------------ | --- | --- | ------------ |
|                                                  |                                                 |     |     |     | Patch Exploitation |     | POC code released  |     |     | Available in |
difficult to detect, actors’ post-exploit actions are  released in wild on GitHub scanning tools
| Zero-day vulnerabilities are a particularly  | often easier to detect and, if coming from fully  |     |     |     |     |     |     |     |     |     |
| -------------------------------------------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
patched software, can act as a warning sign of  On average, it takes only 14 days for an exploit to be available in the wild after a vulnerability is publicly disclosed.
effective means for initial exploitation and, once
publicly exposed, vulnerabilities can be rapidly  a compromise.  This view provides an analysis of the timelines of exploitation of zero-day vulnerabilities, along with the number of
systems vulnerable to the given exploit and active on the internet from the time of first public disclosure.
reused by other nation state and criminal actors.
| The number of publicly disclosed zero-day  | Patches released for zero-day  vulnerabilities  |     |     |     |     |     |     |     |     |     |
| ------------------------------------------ | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vulnerabilities over the past year is on par with  2021, marking a first in the world for a government
While zero-day vulnerability attacks
|     | 250 |     |     | 17  |     |     |     | to require the reporting of vulnerabilities into  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- |
those from the previous year, which was the
24 tend to initially target a limited set of
highest on record.  a government authority for review prior to the
200
|     |     |     |     | 33 organizations, they are quickly adopted  |     |     |     | vulnerability being shared with the product or  |     |     |
| --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | ----------------------------------------------- | --- | --- |
As cyber threat actors—both nation state  service owner. This new regulation might enable
|                                    |     |     | 11  | into the larger threat actor ecosystem.  |     |     |     |                                                  |     |     |
| ---------------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | ------------------------------------------------ | --- | --- |
| and criminal—become more adept at  | 150 |     | 14  |                                          |     |     |     |                                                  |     |     |
|                                    |     |     | 8   |                                          |     |     |     | elements in the Chinese government to stockpile  |     |     |
leveraging these vulnerabilities, we have  12 This kicks off a race for threat actors
|     |     |     | 6   |     |     |     |     | reported vulnerabilities toward weaponizing  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- |
6
observed a reduction in the time between  100 19 3 to exploit the vulnerability as widely as
them. The increased use of zero days over the last
| the announcement of a vulnerability and  |     | 15  |     |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10 possible before their potential targets  year from China-based actors likely reflects the
|     | 50 18 |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the commoditization of that vulnerability.  first full year of China’s vulnerability disclosure
|                                                   | 10  |     |     | install patches.  |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
| This makes it essential that organizations patch  | 11  |     |     |                   |     |     |     |     |     |     |
requirements for the Chinese security community
| exploits immediately. Similarly, it is critical  | 0   |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and a major step in the use of zero-day exploits as
|     | 4102 ceD–luJ 5102 nuJ–naJ 5102 ceD–luJ 6102 nuJ–naJ | 6102 ceD–luJ 7102 nuJ–naJ 7102 ceD–luJ 8102 nuJ–naJ | 8102 ceD–luJ 9102 nuJ–naJ 9102 ceD–luJ 0202 nuJ–naJ 0202 ceD–luJ | 1202 nuJ–naJ 1202 ceD–luJ 2202 nuJ–naJ |     |     |     |     |     |     |
| --- | --------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
that organizations or individuals that uncover  While we observe many nation state actors
a state priority. The vulnerabilities described below
new vulnerabilities responsibly disclose or
|     |     |     |     | developing exploits from unknown vulnerabilities,  |     |     |     | were first developed and deployed by China- |     |     |
| --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | ------------------------------------------- | --- | --- |
report them to affected vendors as soon as  China-based nation state threat actors are  based nation state actors in attacks, before being
possible, in line with coordinated vulnerability
|     |     |     |     | particularly proficient at discovering and  |     |     |     | discovered and spread among other actors in the  |     |     |
| --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | ------------------------------------------------ | --- | --- |
disclosure procedures.
Numbers of publicly disclosed zero-day exploits from the  developing zero-day exploits. China’s vulnerability  larger threat ecosystem.
|     | List of Common Vulnerabilities and Disclosures (CVEs).  |     |     | reporting regulation went into effect September  |     |     |     |     |     |     |
| --- | ------------------------------------------------------- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |

|     | Report  | The State of   | NNaattiioonn  SSttaattee    | Devices and   | Cyber Influence  | Cyber   | Contributing  |
| --- | ------- | -------------- | --------------------------- | ------------- | ---------------- | ------- | ------------- |
40 Microsoft Digital Defense Report 2022  Introduction Cybercrime TThhrreeaattss Infrastructure Operations Resilience Teams
These examples of newly identified vulnerabilities  later in September, using it as an initial vector  61,559 instances of these systems active and
 Rapid vulnerability
demonstrate that organizations have on average  to gain a foothold in networks and performing  on the internet, at the time of disclosure.
60 days from the time a vulnerability is patched  additional actions including credential dumping,  We continued to observe exploitation activity
 exploitation
and a proof of concept (POC) code is made  installing custom binaries, and dropping malware  into November 2021.
| available online, and often picked up by other  |     | to maintain persistence. At the time of disclosure,  |     |     |     |     |     |
| ----------------------------------------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
Continued
actors for reuse. Similarly, organizations have  RiskIQ observed 4,011 instances of these systems  CVE-2022-26134 Confluence
on average 120 days before a vulnerability is  active and on the internet. A China-affiliated actor likely had the zero-day
available in automated vulnerability scanning  exploit code for the Confluence vulnerability
CVE-2021-44077 Zoho ManageEngine
and exploitation tools such as Metasploit— (CVE-2022-26134) four days before the
ServiceDesk Plus
which often result in the exploit being used  vulnerability was publicly disclosed on June 2,
Even organizations that
on a massive scale. This highlights that even  In late October 2021, we observed DEV-0322  and likely leveraged it against a US-based entity.
are not a target of nation
organizations that are not a target of nation state  leveraging a vulnerability (CVE-2021-44077)  At the time of disclosure, RiskIQ observed 53,621
threat actors have a limited period to patch zero- in a second Zoho ManageEngine product,  instances of vulnerable Confluence systems on
state attacks have a limited
| day vulnerabilities in impacted systems before  |     | ServiceDesk Plus—an IT help-desk software  |     |     |     | the internet. |     |
| ----------------------------------------------- | --- | ------------------------------------------ | --- | --- | --- | ------------- | --- |
period to patch zero-day
| the vulnerabilities are exploited by the broader  |     | with asset management. DEV-0322 used         |     |     |     |     |     |
| ------------------------------------------------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
| actor ecosystem.                                  |     | this vulnerability to target and compromise  |     |     |     |     |     |
vulnerabilities in impacted
Vulnerabilities are being picked up and
entities in healthcare, information technology,
systems before they are  CVE-2021-35211 SolarWinds Serv-U
|     |     | higher education, and critical manufacturing  |     |     |     | exploited on a massive scale, and in  |     |
| --- | --- | --------------------------------------------- | --- | --- | --- | ------------------------------------- | --- |
exploited by the broader
In July 2021, SolarWinds released a security  sectors. On December 2, the Federal Bureau of  increasingly shorter timeframes.
| advisory for CVE-2021-35211, crediting Microsoft  |     | Investigation (FBI) and the Cybersecurity and  |     |     |     |     |     |
| ------------------------------------------------- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
actor ecosystem.
| with the notification.8 At the time, we discovered  |     | Infrastructure Security Agency (CISA) issued a     |     |     |     |     |     |
| --------------------------------------------------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
| nation state aligned threat actor DEV-0322          |     | joint advisory warning to the public about nation  |     |     |     |     |     |
Actionable insights
| actively exploiting the SolarWinds Serv-U  |     | state threat actors leveraging the vulnerability.  |     |     |     |     |     |
| ------------------------------------------ | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
vulnerability. Our RiskIQ team observed 12,646 IP  At the time of disclosure, RiskIQ observed    Prioritize patching of zero-day
1
| addresses hosting internet connected versions of  |     | 7,956 instances of these systems active and  |     |     |     |     |     |
| ------------------------------------------------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
vulnerabilities as soon as they are
| the impacted devices between June 15 and July 9. |     | on the internet. |     |     |     |     |     |
| ------------------------------------------------ | --- | ---------------- | --- | --- | --- | --- | --- |
released; don’t wait for the patch
management cycle to deploy.
| CVE-2021-40539 Zoho ManageEngine  |     | CVE-2021-42321 Microsoft Exchange |     |     |     |                                |     |
| --------------------------------- | --- | --------------------------------- | --- | --- | --- | ------------------------------ | --- |
| ADSelfService Plus                |     |                                   |     |     |     | 2  Document and inventory all  |     |
A zero-day exploit for an Exchange vulnerability
enterprise hardware and software
| In September 2021, our researchers observed  |     | CVE-2021-42321 was revealed during the Tianfu  |     |     |     |     |     |
| -------------------------------------------- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
China-affiliated actors exploiting Zoho  Cup, an international cybersecurity summit and  assets to determine risk and to quickly
determine when to act on patches.
| ManageEngine at several US-based entities.      |     | hacking competition held October 16 and 17,         |     |     |     |     |     |
| ----------------------------------------------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
| The vulnerability was publicly reported         |     | 2021 in Chengdu, China. Security researchers at     |     |     |     |     |     |
| on September 6 as CVE-2021-40539 Zoho           |     | Microsoft observed the exploit for the Exchange     |     |     |     |     |     |
| ManageEngine ADSelfService Plus, which          |     | vulnerability used in the wild on October 21, only  |     |     |     |     |     |
| organizations typically use to handle password  |     | three days after the vulnerability was revealed.    |     |     |     |     |     |
| resets.9 DEV-0322 exploited the vulnerability   |     | At the time of disclosure, RiskIQ observed          |     |     |     |     |     |

Report The State of NNaattiioonn SSttaattee Devices and Cyber Influence Cyber Contributing
41 Microsoft Digital Defense Report 2022 Introduction Cybercrime TThhrreeaattss Infrastructure Operations Resilience Teams
In each operation, Russian threat actors
Russian state actors’ Most targeted industry sectors in Ukraine since the invasion
employed many of the tactics, techniques,
and procedures (TTPs) we observed being used
wartime cyber tactics Information technology Consumer retail
before invasion against targets both within and
10% 3%
threaten Ukraine outside of Ukraine. These actors intended to
destroy data and put Ukrainian government
Energy
and beyond agencies off balance in the initial period of the
conflict. They have since sought to derail the 8%
transport of military and humanitarian assistance Other
This year saw Russian state actors launching
to Ukraine, disrupt public access to services and
21%
cyber operations to complement military
media, and steal information of longer-term
action during Russia’s invasion of Ukraine,
intelligence or economic value to Russia.
often using the same tactics and techniques
Media
Targeting transportation threatens an area of
deployed against targets outside of Ukraine.
critical importance to Ukrainian citizens trying 9%
It is critical that organizations worldwide
to survive the conflict. According to a UNICEF-
take measures to harden cybersecurity
sponsored survey in May, respondents in
against digital threats stemming from
conflict-affected urban areas were most worried
Russia-aligned threat actors.
about transport and fuel, supply disruptions,
security, and limited access to food, medical
Nuclear
The situation on the ground continues services, and financial services.10 In June, the Transportation
to fluctuate as the military conflict persists, UN Crisis Coordinator for Ukraine said at least 3%
7%
and Ukraine and its allies should be prepared 15.7 million people in Ukraine were in urgent
to defend themselves if Russian state cyber need of humanitarian assistance, and the
operators increase the frequency or intensity number would grow as the war continues.11
of intrusions in line with military objectives.
Outside of Ukraine, Microsoft detected
During the first four months of the war, Communications
Russian network intrusion efforts against
Microsoft observed threat actors associated
128 organizations in 42 countries between 7%
with the Russian military launch multiple waves
late February and June. The United States was
of destructive cyberattacks against nearly 50
Russia’s number one target. Poland, through
distinct Ukrainian agencies and enterprises
which much of the international military and
and espionage-focused intrusions against humanitarian assistance to Ukraine transits, Financial Government
many others. Excluding operations against
was also a significant target during this period. 27%
5%
online services customers, 64 percent of
Threat actors affiliated with the Russian state
Russian threat activity against known targets
pursued organizations in Baltic countries and
was directed at Ukraine-based organizations Federal, state, and local government organizations in Ukraine have remained priority targets for Russian state and
computer networks in Denmark, Norway, Finland,
between late February and June. state-affiliated threat groups throughout the conflict. The focus on transportation, energy, financial, and media
and Sweden in April and May as well.
sector organizations highlight the risk that these cyber operations pose to services on which Ukrainian citizens rely.

|     |     | Report  | The State of   | Nation State  | Devices and   | Cyber Influence  | Cyber   | Contributing  |     |
| --- | --- | ------- | -------------- | ------------- | ------------- | ---------------- | ------- | ------------- | --- |
42 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
utilized compromised or spoofed accounts
 Russian state actors’   Russia: Top targeted countries and industry sectors
at targeted organizations or within the same
industry and compelling themes to lure victims.
 wartime cyber tactics
NOBELIUM used compromised diplomatic
|  threaten Ukraine   | accounts to send phishing mail disguised as    |     |     |     |     |     |     |     |              |
| ------------------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ |
|                     | diplomatic communications to foreign ministry  |     |     |     |     |     |     |     | Information  |
technology 29%
|  and beyond  | employees across the globe. STRONTIUM created  |     |     |     |     |     |     |     |     |
| ------------ | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
spoof accounts based on publicly available
| Continued | names of account holders at think tanks in the  |     |     |     |     |     |     |     |     |
| --------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
United States and sent phishing messages to
United States 55%
| We have seen an increase in similar           | gain access to accounts at those think tanks.      |     |     |     |     |     |     |     |     |
| --------------------------------------------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| activity targeting the foreign ministries of  | SEABORGIUM phished using lures related to          |     |     |     |     |     |     |     |     |
| NATO countries.                               | reporting on the Ukraine conflict to gain initial  |     |     |     |     |     |     |     |     |
Nongovernmental
access to accounts at international affairs think  organizations 18%
Russian state threat groups remained interested
tanks in the Nordic countries.
in compromising critical infrastructure both
within and outside of Ukraine this past year.
Russia
| IRIDIUM deployed the Industroyer2 malware in a  | Exploitation of IT services supply chain to  |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Government agencies
| failed effort to leave millions of people in Ukraine  | impact downstream customers |     |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
and services 12%
United Kingdom 8%
without power. Outside of Ukraine, BROMINE
| conducted intrusions against organizations         | In late 2021, Russian state actors compromised  |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| involved in manufacturing, and industrial control  | IT services providers and used the access       |     |     |     |     |     |     |     |     |
Canada 3%
to facilitate website defacements and the
| systems in early 2022. |                                                |     |     |     |            |     |     |     | Education 12% |
| ---------------------- | ---------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | ------------- |
|                        | deployment of Whispergate destructive malware  |     |     |     | Germany 3% |     |     |     |               |
Russian state and state-affiliated actors directed
by DEV-0586 in January.12 DEV-0586 also
cyber operations against Ukraine, its allies, and  Switzerland 2%
compromised the network of an IT firm that built  Financial services 5%
other targets of intelligence value this year using
|     | resource management systems for Ukraine’s  |     |     |     | Ukraine 2% |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | ---------- | --- | --- | --- | --- |
many of the following TTPs:
Ministry of Defense and other organizations in
the communications and transportation sectors,
| Spear phishing with malicious attachments  | indicating the group was exploring third-party  |     |     |     |     |     |     |     |           |
| ------------------------------------------ | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- |
| or links                                   | attack options in those sectors as well.        |     |     |     |     |     |     |     | Other 24% |
Other 27%
Worldwide, but especially in the United States
Russian state and Russia-affiliated groups like
and Western Europe, NOBELIUM targeted IT
ACTINIUM, NOBELIUM, STRONTIUM, DEV-
services providers to gain access to government
0257, SEABORGIUM, and IRIDIUM all used
and other sensitive networks throughout
phishing campaigns to gain initial access to
Despite an intensified focus on Ukraine-based organizations since early 2022, enterprises based in North America
2021–2022 (see the discussion of supply chain
desired accounts and networks in organizations  and Western Europe were still the online service customers Russian actors targeted most. NOBELIUM’s campaign
vulnerabilities earlier in this chapter).
within and outside Ukraine. Many campaigns
against the IT sector made it the most targeted sector this past year.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
43 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Russian state actors’
Use of administrative accounts and protocols, Actionable insights Links to further information
and native utilities for network discovery and
wartime cyber tactics 1 Minimize credential theft and account Defending Ukraine: Early Lessons from
lateral movement
abuse by protecting the identities the Cyber War | Microsoft On the Issues
threaten Ukraine of your users by implementing MFA
After gaining initial access to a network,
identity protection tools and enforcing The hybrid war in Ukraine | Microsoft On
Microsoft observed Russian state actors
and beyond least privilege access to secure the the Issues
leveraging legitimate accounts and software
most sensitive and privileged accounts
utilities used to perform basic maintenance Cyber threat activity in Ukraine: analysis
and systems.
Continued tasks to evade detection for as long as and resources | Microsoft Security
possible. They relied on compromised 2 Apply updates to ensure all your systems Response Center (MSRC)
get the highest level of protection as soon
identities with administrative capabilities and
Exploitation of public-facing applications
as possible and are kept up to date. Disrupting cyberattacks targeting
valid administration protocols, tools, and
to gain initial access to networks
Ukraine | Microsoft On the Issues
methods to move laterally within networks 3 Deploy anti-malware, endpoint detection,
Since at least late 2021, STRONTIUM worked without immediately attracting the attention of and identity protection solutions across Malware attacks targeting Ukraine
to develop and refine its capabilities to exploit automated monitors and network defenders. your organization. A combination of government | Microsoft On the Issues
public-facing services, such as Microsoft defense-in-depth security solutions, paired MagicWeb: NOBELIUM’s post-compromise
Basic cyber hygiene and employment of endpoint
Exchange servers, to steal information. with trained and capable personnel, can trick to authenticate as anyone | Microsoft
detection and response tools can help mitigate
STRONTIUM exploited unpatched Exchange empower your organization to identify, Threat Intelligence Center (MSTIC),
the negative impact of these types of operations
servers to access Ukrainian government accounts detect, and prevent intrusions impacting Detection and Response Team (DART),
in peacetime as well as during times of war.
as well as military and defense industry-related your business. Microsoft 365 Defender Research Team
organizations in the United States, Lebanon, Peru, Enable investigations and recovery in the
4
and Romania, and other government agencies The unpredictability of the ongoing event you detect or receive notification of
based in Armenia, Bosnia, Kosovo, and Malaysia. a threat to your environment by backing
conflict demands that organizations
DEV-0586, also affiliated with the Russian military, up critical systems and enabling logging.
worldwide take measures to harden
exploited Confluence server vulnerabilities to Establishing an incident response plan is
gain initial access to government and IT sector cybersecurity against digital threats strongly encouraged.
organizations in Ukraine and other Eastern stemming from Russian state and
European countries.
Russia-affiliated threat actors.
Russian state and affiliated threat
actors use many of the same TTPs to
compromise organizations of interest
during times of war and peace.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
44 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
China expanding China: Top targeted countries and industry sectors
Countries targeted by Chinese state
and state-affiliated groups
global targeting for
Nongovernmental
competitive advantage
organizations 28%
In today’s complex geopolitical climate,
United States 54%
Chinese state and state-affiliated threat
actors conducting cyber operations often DDiiggiittaall pprriinntt aanndd
aim to further the country’s strategic military, bbrrooaaddccaasstt mmeeddiiaa 1177%%
economic, and foreign relations goals as part
of China’s objective to attain competitive China Information
advantage. In the last year, Microsoft technology 10%
United Kingdom 7%
China also continued expanding its economic
has observed widespread Chinese threat
influence globally through previously established Education 9%
activity targeting countries around the world. Canada 5%
Belt and Road Initiatives (BRI), attempting to
revive a comprehensive investment framework Taiwan 5% Government agencies
Since mid-2021, China has been maneuvering with the EU,18 and negotiating a new regional Italy 3% and services 9%
to ensure economic and financial stability amid trade agreement with 15 countries in Asia
the worst COVID-19 surge in two years.13 China Pacific known as the Regional Comprehensive
continued to juggle their position on geopolitical Economic Partnership.19 Microsoft assesses China Other 27%
events, such as the struggle to balance their will continue to utilize cyber collection as a tool Other 26%
“limitless” partnership with Russia,14 and maintain to help advance its strategic political, military,
their position on the world stage.15 In addition, and economic goals due to observed cyber
China’s stance against the United States and operations and the breadth of entities targeted.
Think tanks/NGOs, media, IT, government, and education sectors were among the most targeted sectors
its allies over Taiwan16 and the South China
for China-based threat groups, probably for persistent intelligence collection and reconnaissance.
sea continued to strain foreign relations
Cyber targeting likely to advance economic
with many countries.17
and military interests. The span of targets included, but were not Tobago.20 For example, Trinidad and Tobago was
limited to, countries in Africa, the Caribbean, the first Caribbean country to endorse China’s
Chinese state and state-affiliated threat Microsoft observed widespread targeting of the Middle East, Oceania, and South Asia, with a BRI strategy in 2018, and China considers it an
groups increased targeting of smaller smaller nations around the world by Chinese particular focus on those countries in Southeast important partner in the region. NICKEL has
state and state-affiliated threat groups, Asia, and the Pacific Islands. had persistent network operations targeting
nations around the globe with a focus
suggesting China is likely using cyberespionage Trinidad and Tobago since 2021. For instance, in
on Southeast Asia to gain competitive as a component of its global economic and In line with China’s BRI strategy, China-based March 2022, NICKEL conducted reconnaissance
threat groups targeted entities in Afghanistan,
advantage on all fronts. military influence. activities targeting a government agency, likely
Kazakhstan, Mauritius, Namibia, and Trinidad and
for intelligence collection purposes.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
45 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
and military to the Solomon Islands.22 In May, government, diplomatic, and NGO sectors to
China expanding
Actionable insights
China hosted the second China-Pacific Island gain new insights, likely in pursuit of economic
global targeting for Countries (PICs) Foreign Ministers’ Meeting in espionage or traditional intelligence collection 1 Boost cyber defense to mitigate cyber
Fiji and proposed to advance a “comprehensive objectives. Since Microsoft’s disruption, NICKEL threats proactively. The persistence
competitive advantage strategic partnership” to further political, cultural, has targeted several government agencies, of Chinese threat actors requires
social, security, and climate change interests and likely trying to regain lost access. Between late organizations to identify, protect, detect,
Continued also to fight the pandemic.23 Around the same March and May 2022, NICKEL re-compromised and respond possible intrusions in a
time in May, Microsoft identified GADOLINIUM’s at least five government agencies across the timely fashion.
Meanwhile, Microsoft observed Chinese state malware on Solomon Islands government globe. This suggests the group had additional
and state-affiliated threat groups focusing their systems. RADIUM also ran malicious code on entry points to those entities or regained access 2 Threat actors abuse scheduled tasks25 as
network operations against entities in Southeast systems of a telecommunications company in through new C2 domains. NICKEL’s persistence in a common method of persistence and
Asia and expanding to Pacific Island countries as Papua New Guinea. We assess these activities repeatedly compromising the same government defense evasion, ensure your environment
China shifted its military and economic priorities were likely for intelligence collection purposes agencies globally indicates the importance of the employs additional security guidelines
to cope with the challenges of the United States’ to support China’s overall regional strategy. task at a high level. to protect against this commonly used
renewed interest in the region. In January 2022, technique.26
Microsoft observed RADIUM targeting an energy
Microsoft disrupts NICKEL operations, but the China is being more assertive 3 We continue to observe the use of web
company and an energy-associated government
threat group shows its persistence. shells as an initial vector into targeted
agency in Vietnam, and an Indonesian with their stance on foreign policy.
networks.27 Organizations should harden
government agency. RADIUM’s activities likely We assess cyber-enabled economic
In December 2021, the Microsoft Digital Crimes their systems against web shells attacks
aligned with China’s strategic goals in the South
Unit (DCU) filed pleadings with the US District espionage and intelligence collection that can provide attackers access to run
China Sea.21 In late February and early March,
Court for the Eastern District of Virginia seeking will likely continue. remote commands.28
GALLIUM compromised more than 100 accounts
authority to seize 42 command and control (C2)
affiliated with a prominent intergovernmental Links to further information
domains controlled by NICKEL. These C2 domains
organization (IGO) in the Southeast Asia region.
were used in operations against governments, NICKEL targeting government
The timing of GALLIUM’s targeting of the IGO in
diplomatic entities, and NGOs across Central and organizations across Latin America and
the region coincided with the announcement of
South America, the Caribbean, Europe, and North Europe | Microsoft Threat Intelligence
a scheduled meeting between the United States
America since September 2019.24 Through these Center (MSTIC), Microsoft Digital Security
and regional leaders. GALLIUM actors were likely
operations, NICKEL achieved long-term access to Unit (DSU)
tasked to monitor communications and collect
several entities and consistently exfiltrated data
intelligence before the event. Protecting people from recent
from some victims since late 2019.
cyberattacks | Microsoft On the Issues
As China expanded its influence in Pacific Island
As China continues to establish bilateral
countries, Chinese threat groups’ activities
economic relations with more countries—
followed. In April, China and the Solomon
often in agreements associated with BRI—
Islands signed a security agreement intended to
China’s global influence will continue to grow.
“promote peace and security.” The agreement
We assess Chinese state and state-affiliated
potentially allows China to deploy armed police
threat actors will pursue targets in their

|     |     | Report  | The State of   | Nation State  | Devices and   | Cyber Influence  | Cyber   | Contributing  |     |     |
| --- | --- | ------- | -------------- | ------------- | ------------- | ---------------- | ------- | ------------- | --- | --- |
46 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
At the same time, PHOSPHORUS moved into
 Iran growing
|     | Increased pace and scope of Iranian  |     | Iranian threat to US and Israeli critical  |     |     |     |     |     |     |     |
| --- | ------------------------------------ | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
directed targeting, often via spear phishing, of
cyberattacks against Israel infrastructure mounted throughout the year  high-profile US critical infrastructure companies
 increasingly
including major seaports and airports of entry,
|     | Within weeks of Raisi completing the formation  |     | Iranian state actors Microsoft assesses are  |     |     |     |     |     |     |     |
| --- | ----------------------------------------------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
 aggressive following   transit systems, utility companies, and oil and
|     | of his foreign policy team,30 Iranian state actors  |     | affiliated with the IRGC (PHOSPHORUS and  |     |     |     |     |     |     |     |
| --- | --------------------------------------------------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
gas companies. This targeting, often conducted
|     | resumed destructive cyberattacks against  |     | DEV-0198) targeted high-profile US and Israeli  |     |     |     |     |     |     |     |
| --- | ----------------------------------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
 power transition  via spear phishing, lasted until mid-2022.
|     | Israel at a faster pace than the prior year.  |     | critical infrastructure from late 2021 to mid-2022.  |     |     |     |     |     |     |     |
| --- | --------------------------------------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
The targets directly align with the sectors Tehran
|     | These ransomware and hack-and-leak attacks  |     | The likely aim was to provide Tehran with options  |     |     |     |     |     |     |     |
| --- | ------------------------------------------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
has blamed the United States and Israel for
Microsoft has observed Iranian state  were conducted every few weeks beginning  to retaliate against the same sectors that senior
attacking in Iran, and likely provided Iran with
groups and affiliated actors increase the  in September and involved at least three Iran- IRGC officials blamed the United States and Israel
options for retaliation. The compromise of near
pace and scope of cyberattacks against  affiliated actors, suggesting the attacks might  for disrupting in Iran.31 We assess this activity is
identical targets would provide an opportunity
Israel, expand ransomware attacks  have been part of a nationwide campaign of  tied to statements in late October 2021 by IRGC
to deter such future attacks, while seeking to
beyond regional adversaries to US and EU  retaliation against Israel. In at least one case,  General Gholamreza Jalali, head of Iran’s Passive
avoid escalation by signaling the cause of attacks
|     | Microsoft assessed a ransomware attack  |     | Defense Organization, who echoed accusations  |     |     |     |     |     |     |     |
| --- | --------------------------------------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
victims, and target high profile US critical  without admitting guilt.
|     | against an Israeli organization in late 2021 was  |     | from other influential figures within the regime  |     |     |     |     |     |     |     |
| --- | ------------------------------------------------- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
infrastructure to at least pre-position for
|     | meant to conceal an underlying data deletion  |     | that the United States and Israel conducted  |     |     |     |     |     |     |     |
| --- | --------------------------------------------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
potential destructive cyberattacks. Resurgence of Iranian infrastructure targeting
|     | attack. Microsoft malware analysis determined  |     | cyberattacks on Iran’s ports, railways, and fueling  |     |     |     |     |     |     |     |
| --- | ---------------------------------------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
stations.32 Jalali delivered this accusation a
|     | the ransomware delivered to the victim was  |     |     |     |     |     | 56% | 24% | 19% 39% |     |
| --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
Iranian state actors’ growing cyber aggression  programmed to execute wiper malware  second time in prepared remarks during a staged
|     |     |     |     |     |     |     | 250 |     |     | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
has followed a transition of its presidential  following encryption. Friday prayer speech at a podium with the image
power. In the summer of 2021, hardline President
|     |     |     | of a missile striking the words “USA,” suggesting  |     |     |     | 200 |     |     | 80  |
| --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
By 2022, Iranian cyberattacks escalated in target
Ibrahim Raisi replaced moderate President  his seniors held the same view.33
|     | selection and form of attacks. In February,  |     |     |     |     |     | 150 |     |     | 60  |
| --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hassan Rouhani. In sharp contrast to Raisi, who
%
|                                                 | DEV-0198 attempted to conduct a destructive      |     | PHOSPHORUS began widespread scanning     |     |     |     |     |     |     |     |
| ----------------------------------------------- | ------------------------------------------------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| is a protégé of the Supreme Leader and a close  |                                                  |     |                                          |     |     |     | 100 |     |     | 40  |
|                                                 | attack against Israeli critical infrastructure.  |     | of US organizations in October 2021 for  |     |     |     |     |     |     |     |
ally of the Islamic Revolutionary Guard Corps
|                                               | Microsoft also assesses an Iran-affiliated actor  |     | unpatched Fortinet and ProxyShell vulnerabilities.  |     |     |     |     |     |     |     |
| --------------------------------------------- | ------------------------------------------------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| (IRGC), former President Rouhani’s penchant   |                                                   |     |                                                     |     |     |     | 50  |     |     | 20  |
|                                               | was most likely responsible for a sophisticated   |     | Once compromised, these unpatched systems           |     |     |     |     |     |     |     |
| for diplomacy often brought him at odds with  |                                                   |     |                                                     |     |     |     | 0   |     |     | 0   |
|                                               | cyberattack that set off emergency rocket sirens  |     | were used to execute ransomware attacks, in         |     |     |     |     |     |     |     |
the Supreme Leader and IRGC senior leaders.29  Jul 18–Jun 19 Jul 19–Jun 20 Jul 20–Jun 21 Jul 21–Jun 22
|     | in Israel in June probably by using software that  |     | several cases against critical infrastructure in  |     |     |     |     |     |     |     |
| --- | -------------------------------------------------- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
The hawkish views of the Raisi administration  Critical  Noncritical  Percent critical
adjusts audio over IP networks. the United States and other Western nations.  infrastructure infrastructure infrastructure
appear to have raised the willingness of Iranian
|     |     |     | These marked the first confirmed cases of Iranian  |     |     |     |     |     | of total NSNs |     |
| --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- |
actors to take bolder action against Israel and the
|     |     |     | state affiliated ransomware attacks outside the  |     |     |     | Iranian targeting of critical infrastructure increased  |     |     |     |
| --- | --- | --- | ------------------------------------------------ | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- |
West, particularly the United States, despite the
Middle East. Following the cyberattack against
resumption of diplomatic engagement to revive  to the highest levels observed since late 2018 to early
|     |     |     | Iran’s fueling stations in late October, Microsoft  |     |     |     | 2019. We used US Presidential Policy Directive 21  |     |     |     |
| --- | --- | --- | --------------------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
the nuclear deal with Iran.
|     |     |     | observed a spike in Iranian ransomware    |     |     |     | (PPD-21) to determine whether a company fit the             |     |     |     |
| --- | --- | --- | ----------------------------------------- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- |
|     |     |     | attacks against US companies, suggesting  |     |     |     | criteria of critical infrastructure. (July 2021–June 2022). |     |     |     |
possible correlation.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
47 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Iran growing Iranian critical infrastructure targeting by country
Actionable insights
increasingly 1 Improve your organization’s overall
cyber hygiene by enabling passwordless
aggressive following solutions such as MFA and enforcing its
United States 25%
use for all remote connectivity to mitigate
power transition Noncritical infrastructure 61% any potentially compromised credentials.
2 Evaluate the authenticity of all inbound
Continued
email traffic to ensure the sender address
In Israel, DEV-0198 targeted Israeli railways, is legitimate.
logistics companies, software providers of Israel 22%
3 Patch early and often.34
logistics companies, and fuel companies with a
focus on gas stations. In early 2022, the group Iran 4 Review and audit each one of your partner
conducted a disruptive attack on the network relationships with service providers to
of a major Israeli logistics company, which minimize any unnecessary permissions
forced the company to shut down its computers United Arab between your organization and upstream
Emirates 15%
and some of its operations to contain the providers. Microsoft recommends
attack. In another case, we observed the group immediately removing access for any
attempt to access the network of a major Israeli partner relationships that look unfamiliar
United Kingdom 7%
transportation provider via stolen or reused or have not yet been audited.35
credentials. Meanwhile, another Iranian actor, Critical infrastructure 39%
India 5% Links to further information
DEV-0343—whose targeting of defense, maritime
transportation, and satellite imagery companies Saudi Arabia 4% Iranian targeting of IT sector on the
suggests links to the IRGC—compromised rise | Microsoft Threat Intelligence Center
accounts at Israeli transportation and port- (MSTIC), Microsoft Digital Security Unit
related entities throughout early 2021. (DSU)
Other 22%
Iranian threat groups are likely to remain a threat Iran-linked DEV-0343 targeting defense,
to US and Israeli transportation and energy GIS, and maritime sectors | Microsoft
companies, particularly as diplomatic efforts Threat Intelligence Center (MSTIC),
to revive the Iranian nuclear deal wane and Iranian targeting of critical infrastructure occurred most prominently against Israeli, Emirati, and US organizations. Microsoft Digital Security Unit (DSU)
Washington, Tel Aviv, and Tehran seek alternative
coercive means to lever concessions. Iranian actors are likely to remain a threat to Iranian groups have expanded ransomware
US and Israeli transportation and energy attacks beyond regional adversaries and are
companies in the coming year. targeting high profile US and Israeli critical
infrastructure targets.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
48 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
its activity. Nearly half the Israeli organizations Microsoft
Lebanon-based group with links Actionable insights
were part of Israel’s defense industry or had
successfully
to Iran targeting Israel links to Israeli defense companies, indicating 1 Update antivirus tools40 and ensure cloud
the group has a similar set of interests as Iran detected and protection41 is turned on to detect the
Microsoft monitors cyber threat activities in collecting intelligence on and/or directly related indicators.
regardless of platform, targeted victim, or countering Israel.37 disabled POLONIUM’s
2 For customers with service provider
geographical region. We maintain visibility POLONIUM’s assessed links to MOIS groups abuse of OneDrive relationships, ensure review and audit
and active threat hunting worldwide to are based on observed victim overlaps and
of all partner relationships to minimize
write better detections for our customers. commonality of tools and techniques. as a C2.
unnecessary permissions between your
• Victim overlap: An Iranian state group organization and upstream providers.⁴2
Although threats from Russia, China, Iran, and linked to Iran’s MOIS, which Microsoft tracks Immediately remove access for any partner
North Korea represent the majority of our as MERCURY, previously compromised relationships that appear unfamiliar or
observed nation state actor activity, we also track multiple victims of POLONIUM, indicating a have not been audited.
and communicate about threats from NATO convergence of mission requirements or a
Links to further information
member countries and democratic nations. possible “hand-off” of victims between groups.
Last year, we featured activity by a Turkey-based • Common tools and techniques: Similar to Exposing POLONIUM activity and
actor (SILICON) and a Vietnam-based actor POLONIUM, MSTIC observed DEV-0588 (also infrastructure targeting Israeli
(BISMUTH). This year, we are expanding on known as CopyKittens) commonly use AirVPN organizations | Microsoft Threat
the details of a Lebanon-based group that we for operations and DEV-0133 (also known as Intelligence Center (MSTIC), Microsoft
previously disclosed publicly.36 Lyceum38) use OneDrive for C2 and exfiltration. Digital Security Unit (DSU)
Microsoft uncovered a previously undocumented Similar to Iranian state actors, POLONIUM MERCURY leveraging Log4j 2
Lebanon-based group that we assess used a cloud service provider to compromise vulnerabilities in unpatched systems to
with moderate confidence operated in an Israeli aviation company and law firm.39 target Israeli organizations | Microsoft
coordination with actors affiliated with Iran’s Threat Intelligence Center (MSTIC),
POLONIUM deployed a series of custom
Ministry of Intelligence and Security (MOIS). Microsoft 365 Defender Research Team,
implants using cloud services for C2 and data
Such collaboration or direction from Tehran Microsoft Defender Threat Intelligence
exfiltration—notably OneDrive and DropBox.
would align with revelations since late 2020 that
POLONIUM often created unique OneDrive
the Government of Iran is using third parties to
applications for targets, likely to evade detection.
carry out cyber operations, likely to enhance
As of June 2022, Microsoft suspended more than
Iran’s plausible deniability.
20 POLONIUM-created OneDrive applications,
In the observed activity, POLONIUM targeted
notified affected organizations, and deployed
or compromised two dozen Israel-based
a series of security intelligence updates to
organizations and one IGO with operations
quarantine POLONIUM-developed tools.
in Lebanon between February and May 2022,
before Microsoft disrupted and publicly revealed

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
49 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
North Korean state threat groups, primarily
North Korean cyber
Targeting of defense and aerospace companies Targeting cryptocurrency to balance losses
CERIUM and ZINC, used a variety of tactics to
attempt to penetrate networks of defense and
capabilities employed
North Korean state actors led by CERIUM and Since UN sanctions were levied in 2016, North
aerospace companies around the globe. As North
ZINC put significant effort into developing tactics Korea’s economy has continued to contract,
to achieve regime’s Korea embarked on its most aggressive period of
aimed at penetrating defense and aerospace compounded by natural disasters such as floods44
missile testing ever in the first half of 2022, it used
companies. CERIUM repeatedly probed South and drought45 as well as a near-total lockdown
three main goals cyberespionage to help North Korean researchers
Korean virtual private networks (VPNs) by of borders to imports since the onset of the
gain an edge in developing indigenous defense
downloading clients and looking for weaknesses. COVID-19 pandemic in early 2020.46 Although
systems and countermeasures for the advances
North Korea’s cyber priorities over the past It also downloaded common applications used North Korea opened its borders for trade with
its adversaries made.
year reflected the government’s stated by South Korean military and government clients, China briefly in early 2022, they were soon closed
global priorities. Kim Jong Un emphasized We observed COPERNICIUM targeting a variety likely looking for vulnerabilities. The group again.47 In mid-May, North Korea reported its
the three priorities of building defense of cryptocurrency-related companies around the closely followed current events and wrote new first domestic case of COVID-19.48 It has since
capacity, bolstering the country’s struggling world, often with success, to help support North lure documents which used high profile topics applied a China-style “zero COVID” strategy
Korea’s struggling economy. While we cannot as bait to encourage targets to click on their of mass lockdowns to combat the virus which
economy, and ensuring domestic stability
confirm whether the group was able to exfiltrate malware executables and links. has negatively impacted North Korea’s already
in several key addresses.43 The actions taken
money after a compromise, we observed fragile economy.
by North Korean state actors clearly show Both ZINC and CERIUM used social media and
COPERNICIUM infect dozens of machines by
that cyber is being utilized to achieve these social engineering in campaigns. ZINC was The North Korean state group COPERNICIUM
sending malicious documents masquerading as
three goals. proposals from other cryptocurrency companies. particularly adept at creating fake profiles on tried to offset some of the lost revenue by
LinkedIn and other professional social media stealing money—typically in the form of
Finally, a group Microsoft tracks as DEV-0215 sites, where its operators posed as recruiters cryptocurrency—from any company whose
worked to uphold stability and loyalty in North for major defense and aerospace companies. networks it could penetrate. We saw dozens
Korea by targeting news organizations that Using these profiles, they sent links or malicious of machines compromised belonging to
report on North Korean issues. These outlets file attachments to potential victims using direct cryptocurrency-related companies in the United
have sources both in North Korea and within messages on social media or email. States, Canada, Europe, and throughout Asia.
communities of defectors, which Pyongyang COPERNICIUM even compromised machines
In addition to employees of corporations,
views as an existential threat. In addition, the belonging to cryptocurrency-related companies
CERIUM also broadly targeted members of the
group worked to gain access to networks of within North Korea’s strongest ally, China, both
South Korean military, showing special interest
Korean-speaking Christian groups, which tend on the mainland and in Hong Kong. The group
in both South Korean military academies and
North Korean to be outspoken against North Korea and work relied heavily on social media for its early
military members working in academia.
state actors used a actively with North Korean defectors. reconnaissance and approaches to targets.
Actors would build profiles pretending to be
variety of tactics to
developers or senior officers in businesses
attempt to penetrate related to cryptocurrency. They would then
establish relationships with those in the industry,
aerospace companies
sending malicious links or files once they had
around the globe. built up rapport.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
50 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
also possible the actors behind DEV-0530
North Korean cyber North Korea: Top targeted countries and industry sectors
were acting independently to earn money for
themselves. If it were North Korean hackers
capabilities employed
operating independently, that would explain why
to achieve regime’s the activity was not widespread compared to
government-sponsored theft operations against Nongovernmental
three main goals cryptocurrency companies. organizations 25%
United States 38%
Continued Targeting North Korean news outlets,
defectors, religious groups, and
A group related to PLUTONIUM develops aid organizations
and deploys ransomware
In the last year, Supreme Leader Kim Jong Un
Education 23%
A group of actors originating from North was publicly more focused on internal security
Korea that Microsoft tracks as DEV-0530 began and loyalty than missiles and nuclear weapons. Korea 8%
developing and using ransomware in attacks Reflecting this preoccupation with domestic
in June 2021. This group, which called itself issues, at least two North Korean state groups
H0lyGh0st, utilized a ransomware payload with focused on aspects the regime would view as North Korea Japan 7%
the same name for its campaigns and successfully domestic threats. Financial services 11%
compromised small businesses in multiple The first was a group Microsoft tracks as DEV-
countries as early as September 2021. 0215, which targets media organizations that United Kingdom 7%
Government agencies
Microsoft assessed that DEV-0530 had closely follow North Korean news. One likely
and Services 9%
connections with another North Korean-based reason for this targeting is these media outlets Russia 4%
group tracked as PLUTONIUM (also known obtain their news from North Korean defectors,
as DarkSeoul or Andariel). While the use of Chinese citizens who work closely with North Digital print and
H0lyGh0st ransomware in campaigns is unique Korea, and even some North Korean citizens broadcast media 8%
to DEV-0530, MSTIC observed communications based inside the country, using a variety of
between the two groups, as well as DEV-0530 methods to communicate with the outside world.
using tools created exclusively by PLUTONIUM. The North Korean government views these Other 36%
groups as an existential threat to its survival,
It is not certain that DEV-0530 activity was Other 24%
particularly citizens inside North Korea who
government-sponsored. Although ransomware
would be viewed as traitors and spies. DEV-0215
attacks could have been ordered by the
likely sought to identify these outlets’ sources so
government for the same reason it sponsors
they could neutralize potential information leaks.
theft from cryptocurrency companies, it is North Korea views the United States, South Korea, and Japan as its primary enemies. While Russia is a long-time
ally, North Korean threat actors target Russian think tanks, academics, and diplomatic officials to obtain intelligence
on Russian views of global affairs.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
51 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Finally, state group OSMIUM showed steady
North Korean cyber
interest in international aid organizations
throughout the year, including organizations
capabilities employed
that have assisted North Korea in the past.
to achieve regime’s While North Korea has generally shunned offers
of help from outside the country, especially since
three main goals the outbreak of COVID-19,50 it is possible that
North Korea is considering taking up offers of
help, but is wary of the security ramifications of
Continued
allowing foreign aid workers into the country.
Microsoft also saw evidence of DEV- North Korea may be penetrating the networks
0215 targeting Korean-speaking Christian of aid organizations worldwide to determine
communities. Evangelical Christian Korean whether to allow such aid into their own country.
churches tend to be critical of both North Korea
and South Korean governments that favor
engagement with North Korea. These churches
are likely to conduct outreach to defectors, and
some engage in humanitarian work with North
Korea. North Korea views them as a threat
Actionable insights
because, while the stream of defectors coming
from North Korea almost dried up during the 1 North Korean state actors are skilled,
pandemic,49 these Christian groups often play relentless, and creative, but organizations
a critical role in helping defectors escape. can defend against them.
DEV-0215 has generated fake documents about
2 Most successful attacks can be stopped
Christian conferences for Korean speakers as
with basic cyber hygiene, such as two
lures to target the group and discover who is
factor authentication or not opening Among North Korea experts, there has
helping organize defections.
attachments from unknown individuals
long been debate over whether the
in a virtual environment.
North Korean government is in earnest
Links to further information with its public statements or whether it
is posturing for effect. The alignment
North Korean threat actor targets small
and midsize businesses with H0lyGh0st of cyberattacks with North Korea’s
ransomware | Microsoft Threat Intelligence announced priorities validates the belief
Center (MSTIC), Microsoft Digital Security that North Korea means what it says
Unit (DSU)
when it speaks publicly about its goals.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
52 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Microsoft has assessed certain state actors When a cyber mercenary exploits a
Cyber mercenaries
Actionable insights for governments
across democratic and authoritarian regimes vulnerability in a product or service, they
threaten the stability outsource the development or use of put the entire computing ecosystem at risk. 1 Implement transparency and oversight
“surveillance as a service” technology. This is When vulnerabilities are identified publicly, requirements for surveillance as a service,
of cyberspace how they avoid accountability and oversight, companies are in a race against time to particularly in procurement, including
as well as acquire capabilities that would be release protections before broad based the banning of these offensive actors,
difficult to develop natively. attacks ensue (see our earlier discussion of as the US has done with the Department
There is a growing industry of private
vulnerability exploits). This is a dangerous of Commerce listing of companies on the
companies that develop and sell tools,
techniques, and services that enable their These cyberweapons provide nation and difficult cycle for both software suppliers Entity List.
(who must expediently develop patches) and
clients—often governments—to break into states with surveillance capabilities consumers of products (who must implement 2 Establish post-employment restrictions
networks, computers, phones, and internet- they would not have been able to the patches immediately). for former employees in this sector.
connected devices. An asset for nation
develop alone. As a founding member of the Cybersecurity 3 Aim to implement “know your customer”
state actors, these entities often endanger Tech Accord53—a leading alliance bringing obligations and encourage companies to
dissidents, human rights defenders, together more than 150 technology companies— uphold their human rights commitments.
The market in which cyber mercenaries operate
journalists, civil society advocates, and Microsoft has made a commitment not to
is opaque. Nevertheless, we continue to observe
other private citizens. We refer to these engage in offensive operations online. We stand Links to further information
these groups using zero-day exploits and
as cyber mercenaries or private sector by that commitment and by our human rights
even zero-click exploits that require no victim Untangling KNOTWEED: European private-
offensive actors. responsibilities in this area. We have engaged
interaction at all, enabling surveillance as a service. sector offensive actor using 0-day exploits
in technical disruptions and legal challenges to
| Microsoft Threat Intelligence Center
Microsoft recently announced a European private highlight the negative impacts caused by the
A world where private sector companies create (MSTIC), Microsoft Security Response
sector offensive actor we call KNOTWEED, an services provided by cyber mercenaries and
and sell cyberweapons is more dangerous Center (MSRC), RiskIQ (Microsoft Defender
Austria-based PSOA called DSIRF. Multiple news will continue to protect our customers when
for consumers, businesses of all sizes, and Threat Intelligence)
reports have linked the company to the we see abuse.
governments. These offensive tools can be used
development and attempted sale of a malware Continuing the fight against private sector
in ways that are inconsistent with the norms
toolset called Subzero.51 Victims include law firms, cyberweapons | Microsoft On the Issues
and values of good governance and democracy. Cyber mercenaries create and provide
banks, and strategic consultancies in countries
Microsoft believes the protection of human rights
such as Austria, the UK, and Panama.52 “surveillance as a service” capabilities
is a fundamental obligation, and one we take
that are technologically sophisticated
seriously by curtailing “surveillance as a service” Because these offensive surveillance capabilities
across the globe. are no longer highly classified capabilities created and broadly available, including
by defense and intelligence agencies, but rather advanced malware, and a range
commercial products now offered to companies
of techniques.
and individuals, any regulatory regime for
cyberweapons needs to move beyond export
control. The impact of these cyberweapons can
be devastating.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
53 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
This means asking the technology industry to way toward setting expectations, avoiding Nation state actors and attacks are
Operationalizing
take greater responsibility for both the security misunderstandings, and building trust by increasing in volume and sophistication,
of products and services and the wider digital stating how they understand their obligations creating a situation that is untenable.
cybersecurity norms
ecosystem. While there has been notable under international law.
Immediate action is imperative—there
for peace and security progress on all fronts, the challenges have • Consult with other stakeholders. are things governments can do now to
grown dramatically. As international forums continue to immediately improve the cybersecurity
in cyberspace We must redouble collective efforts to defend discover the best ways to facilitate robust ecosystem, including implementing agreed
the security of cyberspace. We cannot take the multistakeholder inclusion, governments can upon norms and rules for state behavior in
We urgently need a consistent, global rights and freedoms we have come to expect support informed dialogue by consulting cyberspace and working with the broader
framework that prioritizes human rights online for granted. While we struggle to address with multistakeholder communities, in multistakeholder community to address
and protects people from reckless state the challenges, malicious actors are planning particular the technology industry, to emerging gaps.
how and where to strike next using AI, leveraging ensure dialog benefits from those with
behavior online. Nowhere is this more Multilateral institutions must be
disinformation, and finding ways to undermine indispensable expertise.
clearly demonstrated than in the ongoing reimagined to address the pressing
the fledgling metaverse. Human rights defenders, • Form a standing body to support responsible
war in Ukraine. In addition to a global challenge of nation state cyberattacks.
the technology industry, and rights-respecting state behavior in cyberspace. The work of
strategic effort, governments can act now
governments must work together towards an international diplomatic forums to advance
to have an immediate positive impact.
affirmative vision for a safe and secure online responsible state behavior online has never
world. The road ahead is long, but there are been more important. There is a clear need
Five years ago, Microsoft called for a “Digital things governments can do now to immediately for a permanent UN mechanism to deal with
Geneva Convention” to advance responsibilities improve the cybersecurity ecosystem: cyberspace as a domain of conflict.
and obligations across sectors to defend peace
• Cite norms, laws, and consequences in • Define new norms for evolving threats.
and security online. Cyberspace was emerging
attributions. One major improvement over Cyberspace threats are constantly evolving
as a distinct and volatile domain of conflict
the past five years has been the speed and alongside innovations in technology.
and competition between states, with attacks
coordination of government attributions of While international norms should be
becoming more common, even in times of peace.
cyberattacks. Beyond simply naming and technology neutral, they will need to be Links to further information
Today, there is still a clear need for such a shaming, these statements need to highlight updated and attenuated based on changes
A moment of reckoning: the need for a
framework—evidenced by Russian cyberattacks which international laws or norms are violated in the threat landscape and how we use
strong and global cybersecurity response |
against Ukraine as part of Russia’s invasion. This war and what manner of consequences will be technology. Even today, we see gaps in the
Microsoft On the Issues
has created a new front line that is dramatically imposed to help strengthen recognition of existing international framework being abused.
different from any we have known before. international expectations. States should commit to expressly protect core Cyberattacks targeting health care must
Bringing stability to cyberspace will require • Clarify international law interpretation online. processes underpinning the digital ecosystem stop | Microsoft On the Issues
that are not currently protected, like the software
strengthening and reimagining global While governments agree that international The next chapter of cyber diplomacy
update process. Moreover, specific areas
governance institutions to make them fit-for- law applies online, questions remain about at the United Nations beckons | Microsoft
deserve additional protections. For example,
purpose. Cyberspace is fundamentally different how it applies in specific instances. This is On the Issues
as we have learned amid the pandemic, norms
from other domains—it is borderless, synthetic, particularly pertinent in the aftermath of the
for protecting healthcare are essential.
and maintained largely by private industry. Ukraine invasion. Governments can go a long

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
54 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Endnotes
1 https://www.microsoft.com/en-us/cybersecurity/content-hub/cloud-security 19 https://www.wsj.com/articles/u-s-on-sidelines-as-china-and-other-asia-pacific-nations-launch-
2 https://blogs.microsoft.com/on-the-issues/2022/04/27/hybrid-war-ukraine-russia-cyberattacks/ trade-pact-11641038401
3 Critical infrastructure in this chapter is defined by the Presidential Policy Directive 21 (PPD-21), 20 https://greenfdc.org/chinas-two-sessions-2022-what-it-means-for-economy-climate-
Critical Infrastructure Security and Resilience (February 2013). biodiversity-green-finance-and-the-belt-and-road-initiative-bri/
4 https://www.microsoft.com/security/blog/2021/11/18/iranian-targeting-of-it-sector-on-the-rise/ 21 https://www.cfr.org/global-conflict-tracker/conflict/territorial-disputes-south-china-sea
5 https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and- 22 https://www.theguardian.com/world/2022/apr/30/the-china-solomons-security-deal-has-been-
infrastructure-targeting-israeli-organizations/ signed-time-to-move-on-from-megaphone-diplomacy
6 https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated- 23 https://www.fmprc.gov.cn/eng/zxxx_662805/202205/t20220531_10694928.html
administrative-privileges-to-facilitate-broader-attacks/ 24 https://blogs.microsoft.com/on-the-issues/2021/12/06/cyberattacks-nickel-dcu-china/;
7 https://www.microsoft.com/en-us/security/business/identity-access/azure-active-directory- https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-
passwordless-authentication organizations-across-latin-america-and-europe/
8 https://www.solarwinds.com/trust-center/security-advisories/cve-2021-35211 25 https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-
for-defense-evasion/
9 https://pitstop.manageengine.com/portal/en/community/topic/adselfservice-plus-6114-security-
fix-release 26 https://attack.mitre.org/techniques/T1053/
10 https://reliefweb.int/report/ukraine/unicef-ukraine-humanitarian-situation-report-no-13-10-17- 27 https://www.microsoft.com/security/blog/2022/07/26/malicious-iis-extensions-quietly-open-
may-2022 persistent-backdoors-into-servers/
11 https://news.un.org/en/story/2022/06/1119672 28 https://www.microsoft.com/security/blog/2021/02/11/web-shell-attacks-continue-to-rise/
12 https://zetter.substack.com/p/dozens-of-computers-in-ukraine-wiped?s=r ; 29 https://www.timesofisrael.com/in-rare-criticism-of-irgc-rouhani-slams-anti-israel-slogans-
https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian- on-test-missiles/; https://www.theguardian.com/world/2017/may/05/iran-president-hassan-
organizations/ rouhani-nuclear-agreement-sabotaged; https://d2071andvip0wj.cloudfront.net/184-iran-
s-priorities-in-a-turbulent-middle-east_1.pdf; https://www.aljazeera.com/news/2016/3/9/
13 https://www.cnn.com/2022/03/14/economy/china-jan-feb-economy-challenges-ahead-intl-hnk/
iran-launches-ballistic-missiles-during-military-drill; https://www.usatoday.com/story/news/
index.html
world/2015/04/25/iran-yemen-weapons/26367493/; https://www.armscontrol.org/blog/
14 https://www.wsj.com/articles/russias-vladimir-putin-meets-with-chinese-leader-xi-jinping-in-
ArmsControlNow/2016-03-14/The-Iranian-Ballistic-Missile-Launches-That-Didnt-Happen;
beijing-11643966743
https://www.reuters.com/world/middle-east/iran-parliament-approves-most-raisi-nominees-
15 https://www.washingtonpost.com/world/2022/04/01/china-eu-summit/
hardline-cabinet-2021-08-25/;
16 https://twitter.com/MoNDefense
30 https://www.reuters.com/world/middle-east/iran-parliament-approves-most-raisi-nominees-
17 https://news.usni.org/2022/01/24/2-u-s-aircraft-carriers-now-in-south-china-sea-as-chinese-air-
hardline-cabinet-2021-08-25/; https://www.france24.com/en/live-news/20210825-iran-s-
force-flies-39-aircraft-near-taiwan
parliament-approves-president-s-cabinet-choices
18 https://ec.europa.eu/trade/policy/in-focus/eu-china-agreement/; https://www.usnews.com/
news/world/articles/2022-02-28/eu-plans-summit-with-china-on-april-1-to-address-tensions

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
55 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Endnotes continued
31 https://www.janes.com/defence-news/news-detail/iranian-irgc-consolidates-primacy- 45 https://www.reuters.com/world/asia-pacific/nkorea-mobilises-office-workers-fight-drought-
inintelligence-operations; https://www.proofpoint.com/us/blog/threat-insight/badblood-ta453- amid-food-shortages-2022-05-04/
targets-us-and-israeli-medical-research-personnel-credential; https://miburo.substack.com/p/ 46 https://www.washingtonpost.com/world/asia_pacific/north-korea-kim-
iran-disinfo-privatized?s=r. pandemic/2021/09/08/31adfd74-ff53-11eb-87e0-7e07bd9ce270_story.html
32 https://www.reuters.com/business/energy/iran-says-israel-us-likely-behind-cyberattack-gas- 47 https://news.yahoo.com/china-halts-freight-train-traffic-102451425.html
stations-2021-10-30/
48 https://www.cnn.com/2022/05/11/asia/north-korea-covid-omicron-coronavirus-intl-hnk/index.
33 https://www.tasnimnews.com/en/news/2021/11/05/2602361/us-military-action-off-the-table- html
iranian-general
49 https://www.csis.org/analysis/number-north-korean-defectors-drops-lowest-level-two-decades
34 In particular, patch Exchange servers for ProxyShell vulnerabilities (CVE-2021-26855, CVE-2021-
50 https://www.aljazeera.com/economy/2022/5/20/north-korea-shuns-outside-help-as-covid-
26857, CVE-2021-26858, and CVE-2021-27065, CVE-2021-34473). Also, be sure to patch Fortinet
catastrophe-looms
FortiOS SSL VPN appliances for vulnerabilities.
51 Jan-Philipp Hein, In the mystery of creepy spy software, the trail leads via Wirecard to the
35 https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-
Kremlin, FOCUS Online, (2022), https://www.focus.de/politik/vorab-aus-dem-focus-volle-
worldwide
kontrolle-ueber-zielcomputer-das-raetsel-um-die-spionage-app-fuehrt-ueber-wirecard-
36 https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and- zu-putin_id_24442733.html; Sugar Mizzy, We unveil the “Subzero” state trojan from Austria,
infrastructure-targeting-israeli-organizations/ Europe-cities (2021), https://europe-cities.com/2021/12/17/we-unveil-the-subzero-state-trojan-
37 https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and- from-austria/; Andre Meister, We unveil the state Trojan “Subzero” from Austria, Netzpolitik.
infrastructure-targeting-israeli-organizations/ org (2022), https://netzpolitik.org/2021/dsirf-wir-enthuellen-den-staatstrojaner-subzero-aus-
38 https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign oesterreich.
39 https://www.microsoft.com/security/blog/2021/11/18/iranian-targeting-of-it-sector-on-the-rise/ 52 As noted in our technical blog, the identification of targets in a country does not necessarily
mean that a DSIRF customer resides in the same country, as international targeting is common.
40 https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/manage-updates-
baselines-microsoft-defender-antivirus?view=o365-worldwide 53 Home | Cybersecurity Tech Accord (cybertechaccord.org)
41 https://docs.microsoft.com/microsoft-365/security/defender-endpoint/cloud-protection-
microsoft-defender-antivirus
42 https://docs.microsoft.com/microsoft-365/commerce/manage-partners?view=o365-worldwide
43 https://www.marketwatch.com/story/kim-jong-un-calls-for-improved-living-conditions-in-north-
korea-01633920099
https://www.bbc.com/news/world-asia-59845636
https://kcnawatch.org/newstream/1650963237-449932111/respected-comrade-kim-jong-un-
makes-speech-at-military-parade-held-in-celebration-of-90th-founding-anniversary-of-kpra/
44 https://www.theguardian.com/world/2021/aug/06/north-korea-homes-wreckeddamaged-and-
and-bridges-washed-away-in-floods

Report The State of Nation State DDeevviicceess aanndd Cyber Influence Cyber Contributing
56 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
Devices and
An overview of Devices and Insfrastructure 57
Introduction 58
Infrastructure Governments acting to improve critical
infrastructure security and resilience 59
IoT and OT exposed: Trends and attacks 62
Supply chain and firmware hacking 65
With the acceleration of digital transformation, the security Spotlight on firmware vulnerabilities 66
of digital infrastructure is more important than ever. Reconnaissance-based OT attacks 68

RReeppoorrtt TThhee SSttaattee ooff NNaattiioonn SSttaattee DDDeeevvviiiccceeesss aaannnddd CCyybbeerr IInnflfluueennccee CCyybbeerr CCoonnttrriibbuuttiinngg
5577 MMiiccrroossoofftt DDiiggiittaall DDeeffeennssee RReeppoorrtt 22002222 IInnttrroodduuccttiioonn CCyybbeerrccrriimmee TThhrreeaattss IIInnnfffrrraaassstttrrruuuccc TT tttuuu oo rrreee pp IIooOOTTpp eemmrraattiiaaoonnllsswwaarree RR ee dd ssii ee lliiee tt nn ee ccee cctteedd TTeeaammss
iinn tthhee wwiilldd ((JJuullyy 22002211--JJuunnee 22002222))
AAnn oovveerrvviieeww ooff
GGoovveerrnnmmeennttss wwoorrllddwwiiddee aarree mmoovviinngg MMaallwwaarree aass aa AAttttaacckkeerrss aarree iinnccrreeaassiinnggllyy lleevveerraaggiinngg
110033,,009922 8877,,447799 1111,,889955 1100,,119922 33,,116666
DDeevviicceess aanndd ttoo pprrootteecctt ccrriittiiccaall iinnffrraassttrruuccttuurree bbyy sseerrvviiccee hhaass mmoovveedd vvuullnneerraabbiilliittiieess iinn IIooTT ddeevviiccee fifirrmmwwaarree
IInnffrraassttrruuccttuurree iimmpprroovviinngg IIooTT aanndd OOTT sseeccuurriittyy.. iinnttoo llaarrggee ssccaallee ttoo iinnfifillttrraattee ccoorrppoorraattee nneettwwoorrkkss aanndd
ooppeerraattiioonnss aaggaaiinnsstt llaauunncchh ddeevvaassttaattiinngg aattttaacckkss..
eexxppoosseedd IIooTT aanndd OOTT
TThhee ppaannddeemmiicc,, ccoouupplleedd wwiitthh
iinn iinnffrraassttrruuccttuurree aanndd
rraappiidd aaddooppttiioonn ooff iinntteerrnneett-- uuttiilliittiieess aass wweellll aass
FFiinndd oouutt mmoorree oonn pp6655
ccoorrppoorraattee nneettwwoorrkkss..
ffaacciinngg ddeevviicceess ooff aallll kkiinnddss aass
3322%% ooff fifirrmmwwaarree iimmaaggeess aannaallyyzzeedd
aa ccoommppoonneenntt ooff aacccceelleerraattiinngg
ccoonnttaaiinneedd aatt lleeaasstt 1100 kknnoowwnn ccrriittiiccaall
ddiiggiittaall ttrraannssffoorrmmaattiioonn,, hhaass vvuullnneerraaTTbbssuuiinnlliiaattmmiieeiiss.. XXhhiiddee
MMiinneerr
ggrreeaattllyy iinnccrreeaasseedd tthhee aattttaacckk GGaaffggyytt
MMiirraaii
FFiinndd oouutt mmoorree oonn pp6633
ssuurrffaaccee ooff tthhee ddiiggiittaall wwoorrlldd..
AAttttaacckkss aaggaaiinnsstt rreemmoottee mmaannaaggeemmeenntt
CCyybbeerrccrriimmiinnaallss aanndd nnaattiioonn--ssttaatteess aarree qquuiicckkllyy
ddeevviicceess aarree oonn tthhee rriissee,, wwiitthh mmoorree
ttaakkiinngg aaddvvaannttaaggee.. WWhhiillee tthhee sseeccuurriittyy ooff IITT
tthhaann 110000 mmiilllliioonn aattttaacckkss oobbsseerrvveedd
hhaarrddwwaarree aanndd ssooffttwwaarree hhaass ssttrreennggtthheenneedd iinn
iinn MMaayy ooff 22002222——aa fifivvee--ffoolldd iinnccrreeaassee
rreecceenntt yyeeaarrss,, tthhee sseeccuurriittyy ooff IInntteerrnneett ooff TThhiinnggss
((IIooTT)) aanndd OOppeerraattiioonnaall TTeecchhnnoollooggyy ((OOTT)) ddeevviicceess iinn tthhee ppaasstt yyeeaarr.. WWeeaakk ppaasssswwoorrddss 2277%%
hhaass nnoott kkeepptt ppaaccee.. TThhrreeaatt aacc CC ttoo oo rrss uu aa nn rree ttrr ee iiee xxpp ss ll oo aa ii dd ttiinn vv gg aa nncciinngg CCoouunnttrriieess
FFiinndd oouutt mmoorree oonn pp6622
1100++ CCrriittiiccaall kknnoowwnn vvuullnneerraabbiilliittiieess 3322%%
tthheessee ddeevviicceess ttoo eessttaabblliisshh aacccceessss oonn nneettwwoorrkkss 1100++ CCrriittiiccaall vvuullnneerraabbiilliittiieess 66++ yyeeaarrss oolldd 44%%
1111 ccrriittiiccaall iinnffrraassttrruuccttuurree FFiinndd oouutt 22 mmoorree oonn pp5599aaddvvaanncciinngg ccyybbeerr 99 CCoouunnttrriieess
aanndd eennaabbllee llaatteerraall mmoovveemmeenntt,, ttoo eessttaabblliisshh aa 1100++ CCeerrttiiffiiccaatteess eexxppiirreedd 33++ yyeeaarrss 1133%%
ccyybbeerrsseeccuurriittyy rriisskk iinncciiddeenntt rreeppoorrttiinngg aaddvvaanncciinngg bbootthh
ffooootthhoolldd iinn aa ssuuppppllyy cchhaaiinn,, oorr ttoo ddiissrruupptt tthhee PPrreesseennccee ooff ddaannggeerroouuss ccoommppoonneennttss 3366%%
ttaarrggeett oorrggaanniizzaattiioonn’’ss OOTT ooppeerrrreeaaqqttiioouunniirrssee.. mmeennttss GGlloobbaallllyy ccoonnssiisstteenntt rraaeennqqdduu iiiirrnneettmmeerreeoonnpptteessrraabbllee
sseeccuurriittyy ppoolliicciieess aarree nneeeeddeedd ttoo OO ee tthh nn ee ss rr uurree WWeebb
bbrrooaadd aaddooppttiioonn.. 11%% 3300%%
EEmmaaiill
44%%
FFiinndd oouutt mmoorree oonn pp5599 IInndduussttrriiaall ccoonnttrrooll FFiinndd oouutt mmoorree oonn pp6666
ssyysstteemmss
11%%
DDaattaabbaasseess
RReemmoottee mmaannaaggeemmeenntt
1188%%
4466%%

Report The State of Nation State DDeevviicceess aanndd Cyber Influence Cyber Contributing
58 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
The last several years have seen unprecedented While the prevalence of IoT and OT vulnerabilities From a security operation standpoint network
Introduction
change in the digital world. Organizations are is a challenge for all organizations, critical defenders take multiple approaches to improving
evolving to harness advances in computing infrastructure is at increased risk because threat their organization’s IoT/OT security posture.
capability from both the intelligent cloud and actors have learned that disabling critical services One approach is to implement continuous
Accelerating digital
the intelligent edge. As a result of the pandemic is a powerful lever. The 2021 ransomware attack monitoring of IoT and OT devices. Another is to
transformation has increased forcing entities to digitize to survive and the on the Colonial Pipeline Company demonstrated “shift-left”—meaning to demand and implement
rate at which industries worldwide are adopting how criminals can disrupt a critical service to better cybersecurity practices for the IoT and
the cybersecurity risk to
internet-facing devices, the attack surface of the increase the likelihood of a ransom payment. OT devices themselves. A third approach is to
digital world is increasing exponentially. And Russia’s cyberattacks against Ukraine implement a security monitoring solution which
critical infrastructure and
demonstrate that some nation states view spans both IT and OT networks. This holistic
This rapid migration has outpaced the security
cyber-physical systems. cyberattacks against critical infrastructure approach has the significant added benefit of
community’s ability to keep up. Over the past
as acceptable sabotage to achieve its contributing to critical organizational processes,
year, we have observed threats exploiting devices
military objectives. such as “breaking the silos” between OT and IT,
in every part of the organization, from traditional
which in turn enables the organization to reach
IT equipment to operational technology (OT) However, there is hope on the horizon.
an enhanced security posture while meeting
controllers or simple Internet of Things (IoT) Policymakers and network defenders are
business objectives.
sensors. Although security of IT equipment has acting to improve the cybersecurity of critical
strengthened in recent years, IoT and OT device infrastructure, including the IoT and OT devices Michal Braverman-Blumenstyk
security has not kept pace. Threat actors are they rely on. Policymakers are accelerating the Corporate Vice President, Chief Technology
exploiting these devices to establish access on development of laws and regulations to build Officer, Cloud and AI Security
networks and enable lateral movement or disrupt public trust in the cyber security of critical
the organization’s OT operations. We have seen infrastructure and devices.
attacks on power grids, ransomware attacks
Microsoft is partnering with governments around
disrupting OT operations, IoT routers being
the world to seize this opportunity to enhance
leveraged for increased persistency, and attacks
cybersecurity and we welcome additional
targeting vulnerabilities in firmware.
engagement. We are, however, concerned that
inconsistent, bespoke, or complex requirements
could have unintended effects, including
decreasing security in some cases by diverting
scarce security resources toward compliance with
multiple duplicative certifications.

| Report  | The State of   | Nation State   | DDeevviicceess  aanndd   | Cyber Influence  | Cyber   | Contributing  |     |
| ------- | -------------- | -------------- | ------------------------ | ---------------- | ------- | ------------- | --- |
59 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
Microsoft seeks to partner with governments
 Governments acting
around the world in pursuing effective critical
infrastructure cybersecurity policies, increasing
 to improve critical
understanding of challenges and opportunities,
 infrastructure security   and supporting efforts to enhance collective
risk posture.
 and resilience
Policy developments in critical infrastructure
cybersecurity risk management
Governments worldwide are developing
During the last year, multiple jurisdictions
and evolving policies to manage critical
including Australia, Chile, the European Union
infrastructure cybersecurity risk. Many are
(EU), Japan, Singapore, the United Kingdom (UK),
also enacting policies to improve IoT and
and the United States, have developed, updated,
OT device security. The growing global
or implemented cross-sector or sector-specific
wave of policy initiatives is creating  cybersecurity requirements.1 Many of these
enormous opportunity to enhance  governments—and others such as India2 and
|     |     | Countries advancing  |     |     | Countries  |     |     |
| --- | --- | -------------------- | --- | --- | ---------- | --- | --- |
cybersecurity but also poses challenges  Switzerland3—already issued or are developing  11 critical infrastructure  2 advancing cyber  9 Countries
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
to stakeholders across the ecosystem. cybersecurity incident reporting requirements  cybersecurity risk  incident reporting  advancing both
|     |     | requirements |     |     | requirements |     |     |
| --- | --- | ------------ | --- | --- | ------------ | --- | --- |
for critical infrastructure and essential service
providers.4
Developing a holistic vision for managing critical
Some notable policy developments occurred in
infrastructure cyber risk is critical, but complex,
|     | The EU worked to update its NIS Directive  |     |     |     | In May, Indonesia issued a presidential  |     |     |
| --- | ------------------------------------------ | --- | --- | --- | ---------------------------------------- | --- | --- |
especially given the degree of interconnection across  Australia, the EU, Indonesia, and the United States
technologies and global suppliers, the range of  during the last year. Australia enacted two laws to  of 2016, which provides a framework for EU  regulation on the protection of vital information
|     | member states to regulate technology services  |     |     |     | infrastructure (“IIV”), which will take effect in  |     |     |
| --- | ---------------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- |
technology uses and associated risks, and the need  help it manage cross-sector critical infrastructure
|     | and products deemed critical to their economy  |     |     |     | May 2024 and cover sectors such as energy,  |     |     |
| --- | ---------------------------------------------- | --- | --- | --- | ------------------------------------------- | --- | --- |
to invest in both short-and long-term strategies.  cybersecurity risks. The laws, among other things,
designate new critical infrastructure sectors,  and the functioning of society. The proposed  transportation, finance, and health, among
Effectively scoped policies that drive iterative
|     | NIS 2 includes revisions that would create a  |     |     |     | others. Indonesia’s objective with the regulation  |     |     |
| --- | --------------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- |
learning and improvements, and support global,  require the development of risk management
cross-sector interoperability, can help manage  plans, mandate cybersecurity incident reporting,  new category of critical digital infrastructure,  is to protect the continuity of the implementation
|     | increase requirements for cyber incident  |     |     |     | of IIV, prevent cyberattacks, and increase  |     |     |
| --- | ----------------------------------------- | --- | --- | --- | ------------------------------------------- | --- | --- |
complexity and enable a more security-minded  and empower the government to intervene if it
|     | reporting, and impose additional cybersecurity  |     |     |     | preparedness in handling cyber incidents.  |     |     |
| --- | ----------------------------------------------- | --- | --- | --- | ------------------------------------------ | --- | --- |
digital transformation. However, a fragmented  determines a critical infrastructure operator is
unwilling or unable to adequately respond to  risk management requirements, The EU also  IIV providers will be responsible for conducting
approach to legislation could lead to overlapping
|     | developed a proposed update to its Digital  |     |     |     | secure and reliable protection, implementing  |     |     |
| --- | ------------------------------------------- | --- | --- | --- | --------------------------------------------- | --- | --- |
and inconsistent regulatory requirements. This could  an incident.
impact resources and ultimately undermine security  Operational Resilience Act (DORA), creating new  effective cyber risk management, and reporting
|     | requirements for information communication  |     |     |     | cyber risk results to corresponding government  |     |     |
| --- | ------------------------------------------- | --- | --- | --- | ----------------------------------------------- | --- | --- |
objectives. For example, organizations could
|     | technologies used in the financial services sector. |     |     |     | agencies. The regulation includes a requirement  |     |     |
| --- | --------------------------------------------------- | --- | --- | --- | ------------------------------------------------ | --- | --- |
divert resources from innovation and security to
to report cyber incidents within 24 hours.
formalistic compliance exercises.

Report The State of Nation State DDeevviicceess aanndd Cyber Influence Cyber Contributing
60 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
Building on its regulations for pipelines, TSA issued Policymakers have also focused their attention The need for consistency
Governments acting
two additional security directives later in 2021 that on the continued proliferation of IoT devices
In many cases, the range of activity across
promulgated cybersecurity requirements to freight and networked OT devices.
to improve critical regions, sectors, technologies, and operational
rail, passenger railroad carrier, or rail transit systems.
• In the UK, the draft Product Security and risk management areas is being pursued
infrastructure security The directives required that covered operators Telecommunications Infrastructure Bill simultaneously, resulting in potential overlap
designate a cybersecurity coordinator, report
will require manufacturers of consumer or inconsistency in scope, requirements,
and resilience cybersecurity incidents within 24 hours, develop connectable products, such as smart TVs, and complexity for organizations seeking to
and implement a cybersecurity incident response
to stop using default passwords that are an leverage guidance or demonstrate compliance.
plan, and complete a cybersecurity vulnerability
Continued easy target for cyber criminals, to establish a Without a universally accepted definition of
assessment. TSA simultaneously announced it also
vulnerability disclosure policy (such as a way to IoT, scope is especially challenging for IoT and
The US Congress passed a law that authorized updated its aviation security programs to require
receive notice of security flaws), and to provide OT device regulations. The examples above
the Cybersecurity and Infrastructure airport and airline operators to implement the first
transparency about the minimum length of potentially apply to “connected products and
Security Agency (CISA) to issue regulations two provisions, designating a coordinator and
time during which they will provide security ancillary services,” “consumer connectable
to require cyber incident reporting from reporting incidents within 24 hours.
updates.9 products,” and “wireless devices.” At the same
critical infrastructure operators, and the US
time, many governments aim to implement
Transportation Security Administration (TSA) Policy developments in IoT • In the EU, new security standards or
more robust assessment regimes to better
issued new sector-specific cybersecurity and OT device security requirements are being implemented via
understand whether and how organizations
requirements in the transportation sector. Across dozens of countries, governments are multiple legislative instruments, including
and products meet current, emerging, and
In 2021, TSA issued two security directives active in developing requirements to advance the a delegated act to the Radio Equipment
evolving requirements. As these trends merge,
to hazardous liquid and natural gas pipeline cybersecurity of information and communications Directive that applies to wireless devices
complexity will increase. Encouragingly, questions
operators in response to the ransomware technology (ICT) products and services, including and seeks to improve network resilience,
posed during the EU Cyber Resilience Act
attack on the Colonial Pipeline Company: IoT and OT devices. In the context of ICT products protect consumers’ privacy, and reduce the
consultation explored how new regulation could
risk of monetary fraud.10 In addition, use
• The first directive required operators to and services, the biggest concerns are software potentially interact with existing cybersecurity
of a cloud certification scheme,11 currently
designate a cybersecurity coordinator, report supply chain security and IoT security. regulation, indicating intent to avoid conflicting
in development as a result of the 2019 EU
cyber incidents within 12 hours, and conduct • The European Commission proposed the Cybersecurity Act,12 might be required. cybersecurity requirements.
a vulnerability assessment of their systems. Cyber Resilience Act, which would establish
Iterative approaches that are risk-based
• The second directive, which TSA revised in cybersecurity requirements for standalone and outcome- or process-oriented (versus
2022, required them to implement specific software and connected devices and ancillary implementation-specific) could foster enhanced
mitigation measures to protect against services.5 Relevant practices for software cybersecurity and continuous improvement.
ransomware attacks and other known threats vendors include leveraging a secure software Likewise, a focus on enabling interoperability
to IT and OT systems, develop and implement development lifecycle6 and providing a across sectors, regions, and policy areas
a cybersecurity contingency and response Software Bill of Materials.7 New security could consistently raise cybersecurity across
plan within 30 days, and undergo an annual requirements would apply to connected interconnected global supply chains.
cybersecurity architecture design review. devices and all manufacturers would be tasked
with managing coordinated vulnerability
disclosure8 processes for released products.

Report The State of Nation State DDeevviicceess aanndd Cyber Influence Cyber Contributing
61 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
Governments acting Accelerating ecosystem-wide investments in software Actionable insights
to improve critical supply chain security and Zero Trust architecture 1 Multilateral institutions must be
reimagined to address the pressing
infrastructure security US Executive Order (EO) 14028 on Today, we’re going beyond the EO’s challenge of nation state cyberattacks.
improving cybersecurity has been a requirements to demonstrate conformance
and resilience catalyst to expedite Microsoft’s ongoing with software supply chain security 2 Develop cybersecurity policies that are
consistent and interoperable across
requirements and provide Software Bill of
initiatives to invest in our own and
regions, sectors, and topic areas.
Continued ecosystem-wide supply chain security Materials (SBOM) information in two ways:
and to enable our customers to meet 1. First, we’re sharing an open-source version Links to further information
There are increasingly complex critical Zero Trust objectives. of our SBOM generator tool, which we built
Continued investments in supply
to be easily integrated with CI/CD pipelines
infrastructure cybersecurity policies in chain security in support of the
supporting builds on Windows, Linux, Mac,
development across regions, sectors, We have long believed that enhancing the iOS, and Android platforms.13 cybersecurity Executive Order | Microsoft
software supply chain requires sharing learnings Tech Community
and topic areas. This activity brings 2. Second, we’re contributing to the
and best practices, beginning with our public
great opportunities and significant development of industry standards for US Government sets forth Zero Trust
release of Microsoft’s Security Development
Supply Chain Integrity, Transparency, architecture strategy and requirements |
challenges. How governments proceed Lifecycle about 15 years ago.
and Trust (SCITT). This will allow for the Microsoft Security Blog
will be crucial to the future of digital In addition, we are partnering closely with the automated exchange of verifiable supply
CYBER EO | Microsoft Federal
transformation and ecosystem- National Cybersecurity Center of Excellence chain information, including artifacts that
wide security. to demonstrate approaches to Zero Trust demonstrate conformance with requirements Supply Chain Integrity, Transparency,
Architecture applied to both on-premises and such as those resulting from the EO’s and Trust | github.com
cloud technology and establishing new product software supply chain guidance.
capabilities, including the ability to enforce Implementing a Zero Trust Architecture |
phishing-resistant authentication for hybrid NCCoE (nist.gov)
and multi-cloud environments.

|     |     |     | Report  | The State of   | Nation State   | DDeevviicceess  aanndd    |   Cyber Influence  | Cyber   | Contributing  |     |     |
| --- | --- | --- | ------- | -------------- | -------------- | ------------------------- | ------------------ | ------- | ------------- | --- | --- |
62 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
 IoT and OT exposed:   Attacks against remote management devices
IoT devices pose unique security
|     |     | risks as entry and pivot points in the  |     | 140 |     |     |     |     |     |     |     |
| --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 Trends and attacks
|     |     | network. Millions of IoT devices are  |     | 120 |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | unpatched or exposed.                 |     | 100 |     |     |     |     |     |     |     |
The increasingly connected digital world
| means devices are rapidly coming online,         |     |                                                |     | snoilliM | 80  |     |     |     |     |     |     |
| ------------------------------------------------ | --- | ---------------------------------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| communicating with larger systems,               |     | Exposed devices can be discovered through      |     |          | 60  |     |     |     |     |     |     |
| collecting data, and creating visibility across  |     | internet search tools by identifying services  |     |          |     |     |     |     |     |     |     |
40
| formerly obscured spaces. This brings  |     | listening on open network ports. These ports  |     |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
20
are commonly used for remote management of
opportunity for organizations and threat
|     |     | devices. If not secured correctly, an exposed IoT  |     |     | 0   |     |     |     |     |     |     |
| --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
actors alike, with the business of cybercrime
device can be used as a pivot point into another  1202 nuJ 1202 luJ 1202 guA 1202 peS 1202 tcO 1202 voN 1202 ceD 2202 naJ 2202 beF 2202 raM 2202 rpA 2202 yaM
becoming both a multi-billion dollar
layer of the enterprise network as unauthorized
industry and risk.
users can remotely access the ports. We have
observed a variety of threat actors attempting to
IoT devices—including everything from printers  exploit vulnerabilities in internet exposed devices  Increasing attacks on remote management ports over time, as seen through the MSTIC sensor network.
| to web cameras, climate control devices, and  |     | ranging from cameras to routers to thermostats.  |     |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building accesses controls—pose unique        |     | However, despite the risk, millions of devices   |     |     |     |     |     |     |     |     |     |
Web attacks against IoT and OT
security risks to individuals, organizations, and
remain unpatched or exposed.
| networks. While critical to many organizations’  |     |     |     |     | 50  |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
operations, they can quickly become a liability
Summary of attack types on IoT/OT
40
and security risk. The rapid adoption of IoT
| solutions in almost every industry has increased  |     | Databases 18% |     | Web 30%   |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
|                                                   |     |               |     | sdnasuohT | 30  |     |     |     |     |     |     |
the number of attack vectors and the exposure
| risk of organizations.  |     | Industrial  |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
20
control
Malware as a service has moved into large
systems 1%
10
scale operations against civil infrastructure and
utilities (including hospitals, oil and gas, electrical
0
grids, transportation services, and other critical
|                                                      |     |                |          |          | 1202 nuJ | 1202 luJ 1202 guA 1202 peS | 1202 tcO 1202 voN | 1202 ceD 2202 naJ | 2202 beF 2202 raM | 2202 rpA 2202 yaM | 2202 nuJ |
| ---------------------------------------------------- | --- | -------------- | -------- | -------- | -------- | -------------------------- | ----------------- | ----------------- | ----------------- | ----------------- | -------- |
| infrastructure) as well as corporate networks.       |     |                |          | Email 4% |          |                            |                   |                   |                   |                   |          |
| Significant research efforts are required by threat  |     | Remote         |          |          |          |                            |                   |                   |                   |                   |          |
|                                                      |     | management 46% | Other 1% |          |          |                            |                   |                   |                   |                   |          |
actors to uncover and exploit the configuration of
operating environments and embedded IoT and
Attack types observed through MSTIC sensor
OT devices.
network. Most prevalent were attacks against remote  Web attack volume over time, as seen through the MSTIC sensor network. As the number of devices directly
connected to the web continues to drop, attackers might eventually be less likely to probe for them.
management devices, attacks via web, and attacks on
data bases (brute forcing or exploits).

|     |     |     |     |     |     | Report  |     | The State of   | Nation State   | DDeevviicceess  aanndd     | Cyber Influence  | Cyber   | Contributing  |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | -------------- | -------------- | -------------------------- | ---------------- | ------- | ------------- | --- |
63 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
Mirai evolved to infect a wide range of IoT
 IoT and OT exposed:
Relative prevalence of user name and password pairs seen
devices including internet protocol cameras,
|     |     |     |     | security camera digital video recorders, and  |     |     |     | among IoT/OT devices in 45 days of sensor signals |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
 Trends and attacks
routers. The attack vector bypassed legacy
|           |     |     |     | security controls and poses a risk for endpoints  |     |     |     |     |     |     |     | a   |     |     |
| --------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Continued |     |     |     |                                                   |     |     |     |     |     |     |     | d   |     |     |
|           |     |     |     | within the network by exploiting additional       |     |     |     |     |     |     |     | m   |     |     |
|           |     |     |     |                                                   |     |     |     |     |     |     | s   | in  |     |     |
u
R e v a m p e d  m a lw a r e  u t il i ty v u l n e r a b i l i ti e s   a n d  m o v i n g  l a t e r a l l y .  M ir a i   h a s   p te
|     |     |     |     |               |                    |                         |                       |             |     |     | 12  | p le |     |     |
| --- | --- | --- | --- | ------------- | ------------------ | ----------------------- | --------------------- | ----------- | --- | --- | --- | ---- | --- | --- |
|     |     |     |     | b e e n   r e | d e s i g n e d  m | u l t i p l e   t i m e | s ,   w i t h   v a r | i a n t s   |     |     | 3   | o c  |     |     |
A s  c y be rc r im e  g ro u p s  h a v e  evolved, so has their  4 rt o
|     |     |     |     |     |     |     |     |     |     | a   | 5 6 | m   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
deployment of malware and choice of targets.  a d a p t i n g   t o   d i f f er e n t   a r c h it e c t u r e s   a n d   e x p lo i t ing  d m
|     |     |     |     | b o t h   k n | o w n   a n d   z e | r o - d a y   v u l n | e r a b i l i t i e s |   t o   |     | in  |     | te  |     |     |
| --- | --- | --- | --- | ------------- | ------------------- | --------------------- | --------------------- | ------- | --- | --- | --- | --- | --- | --- |
I n   t h e   p a s t   y e a r ,   w e   o b s e r v e d   a t t a c k s   a g a i n s t   12 nc11
|     |     |     |     | c o m p r o | m i s e   n e w   a t | t a c k   v e c t o r | s . |     |     |     | 3   | le  |     |     |
| --- | --- | --- | --- | ----------- | --------------------- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
c o m m o n   I o T   p r o t o c o l s — s u c h   a s   T e l n e t — s c
|     |     |     |     |     |     |     |     |     |     | 12  |     | u o |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | 34  | ro  | p m |     |     |
d r o p   s i g n i fi c a n t l y ,   i n   s o m e   c a s e s   a s   m u c h   a s   T h e   u s e   o f   M i r a i   g r e w   a m o n g   b o t h   3 2 -   a n d   6 4 - b it   o p o a
|     |     |     |     |     |     |     |     |     |     |     | a   | t rt d |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
6 0   p e r c e n t .   A t   t h e   s a m e  t i m e ,   b o t n e t s   w e r e   x 8 6   C P U   a r c h i t e c t u r e s   o v e r   t h e   p a s t   y e a r ,   a n d   t h e   d m
|     |     |     |     |     |     |     |     |     |     |     | m   | in  | nc11 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
r e p u r p o s e d   b y   c y b e r c r i m e   g r o u p s  a n d   n a t i o n   tsgoingo in
|     |     |     |     | m a l w a r | e   w a s   g i v e n   | n e w   c a p a b i | l i t i e s   t h a t   | w e r e   |     |     | adm |     |     |     |
| --- | --- | --- | --- | ----------- | ----------------------- | ------------------- | ----------------------- | --------- | --- | --- | --- | --- | --- | --- |
in
s t a t e   a c t o r s .   T h e   p e r s i s t e n c e   o f   m a l w a r e ,   s u c h  as  ra p i d l y   a d o p t e d   b y   n a t i o n   s t a t e   a n d   c r i m i n a l   n
Mirai, highlights the modularity of these attacks  groups. Nation state attacks now leverage new  root
| an T d o  th p e                     |   I a o d T a   p m ta a bi l l w ity | a  o r f e  e   x d is e ti t n e g c  t | t h e re d a   ts. | variants of existing botnets in distributed denial  |     |     |     |     |         |         |      |     |     |     |
| ------------------------------------ | ------------------------------------- | ---------------------------------------- | ------------------ | --------------------------------------------------- | --- | --- | --- | --- | ------- | ------- | ---- | --- | --- | --- |
|                                      |                                       |                                          |                    | of service (DDoS) attacks on foreign adversaries.   |     |     |     |     | default |         |      |     |     |     |
| in the wild (July 2021-June 2022)    |                                       |                                          |                    |                                                     |     |     |     |     |         | default |      |     |     |     |
| Top IoT malware detected in the wild |                                       |                                          |                    | As revenue from attacks against IoT devices         |     |     |     |     |         |         |      |     |     |     |
|                                      |                                       |                                          |                    | declined in 2022, we observed several threat        |     |     |     |     |         |         | user |     |     |     |
| 103,092                              | 87,479                                | 11,895                                   | 10,192 3,166       | actor groups abusing vulnerabilities—such as        |     |     |     |     |         |         |      |     |     |     |
user
|     |     |     |     | Log4j and Spring4Shell—to deliver a malicious  |     |     |     |     |     |     | min |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
telnetad
|     |     |     |     | p a y lo a d |   to   d e v i c e s  s | u c h  as   s e r v | e r s,  i n f e c ti | n g   |     |     |     |     | ad  |     |
| --- | --- | --- | --- | ------------ | ----------------------- | ------------------- | -------------------- | ----- | --- | --- | --- | --- | --- | --- |
m
th e m   a n d  r e c r u i t in g   th e m  i n t o   l ar g e   b o t n e t s  in
min
carrying out DDoS attacks. The revamped
|     |     |     |     |                 |                      |                      |                    |            |     | telnetad |     | ot  |     |     |
| --- | --- | --- | --- | --------------- | -------------------- | -------------------- | ------------------ | ---------- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     | u t il i ty   o | f   m a lw a r e   d | e si g n ed   t o  t | a r g e t   v u ln | e r a ble  |     |          |     | o   |     |     |
r ad
Io T   d e v i c e s  h as   s e r io u s   im p li c a ti o n s   f o r  b o t h   m
in
organizations and nations, as lateral movement
ot
o
|     |     |     |       | can expose backdoors to additional payloads   |     |     |     |     |     |     | r 21 |     |     |                      |
| --- | --- | --- | ----- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | -------------------- |
|     |     |     |       | and other devices on networks.                |     |     |     |     |     |     | 5    | n   |     | I n n e r  c irc l e |
|     |     |     |       |                                               |     |     |     |     |     |     | Zt e | hi  |     |                      |
|     |     |     |       |                                               |     |     |     |     |     |     |      | c v |     | u s e rn a m e s     |
|     |     |     | Xhide |                                               |     |     |     |     |     |     |      | 1 x |     |                      |
0 0 z iv
|     |     |     | Tsunami |     |     |     |     |     |     |     |     | 1   |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Miner Many industrial control system protocols   Outer circle
Gafgyt
| Mirai |     |     |     | are unmonitored and therefore vulnerable to  |     |     |     |     |     |     |     |     |     | passwords |
| ----- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
OT-specific attacks. This can mean increased
Using common username and password pairs increases risk of compromise. Based on a sample size of over
risk for critical infrastructure.
39 million IoT and OT devices, those using identical usernames and passwords represented around 20 percent.

|     |     |     |     | Report  | The State of   | Nation State   | DDeevviicceess  aanndd     | Cyber Influence  | Cyber   | Contributing  |
| --- | --- | --- | --- | ------- | -------------- | -------------- | -------------------------- | ---------------- | ------- | ------------- |
64 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
 IoT and OT exposed:
Industrial control system protocol prevalence Malware such as Mirai persists by developing
|     |     |     |     |     |     | 1. EtherNet/IP |     | 13. IEC-60870 | new capabilities and is being adopted by  |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | ----------------------------------------- | --- |
 Trends and attacks
cybercrime groups and nation state actors,
|           |     |     |     |     |     | 2. MODBUS |     | 14. Honeywell FDA  |                                               |     |
| --------- | --- | --- | --- | --- | --- | --------- | --- | ------------------ | --------------------------------------------- | --- |
|           |     |     |     |     |     |           |     | Diagnostics        | leveraging new variants of existing botnets   |     |
| Continued |     |     |     |     |     | 3. BACNet |     |                    |                                               |     |
in DDoS attacks on foreign adversaries.
|     |     |     |     |     |     |               |     | 15. Suitelink |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | --- | --- |
|     |     |     |     |     |     | 4. Siemens S7 |     |               |     |     |
While weak configurations and default
|     |     |     |     |     |     |     |     | 16. DeltaV |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
credentials still pose a risk to networks, Microsoft  3 4 5 5. Profinet
|     |     |     |     |     |     | Real-Time |     | 17. GSM |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --- | --- |
observed many web-based exploits utilizing
HTTP. We observed this increase in attacks  6. Profinet DCP 18. DNP3 Actionable insights
on web-based services using legacy botnets.
1 7. Siemens S7 Plus 19. AMS Ensure devices are robust by applying
 1
Meanwhile, there was a decrease in the number  8 11 12 8. CodeSys 20.SRTP
patches, changing default passwords,
of open telnet ports on the internet, a positive
|     |     |     |     |     |     | 9. Siemens  |     | 21. TwinCat | and default SSH ports. |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ---------------------- | --- |
sign for network security as botnets which posed  6 WinCC Agent
22.Emerson Roc
historical risk to devices are losing relevance.   2 Reduce the attack surface by eliminating
|     |     |     |     |     |     | 10. EtherNet/IP  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
Despite this decrease in open telnet ports, we still  9 13 14 15 23.Bently Nevada unnecessary internet connections and
O/O
observed persistent botnets in sensor networks. 20 21 24.Mitsubishi  open ports, restricting remote access by
|     |     |     |     |     |     | 11. Honeywell  |     |        |                                         |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | --------------------------------------- | --- |
|     |     |     |     |     | 18  |                |     | MELSEC | blocking ports, denying remote access,  |     |
|     |     |     |     |     | 16  | Control        |     |        |                                         |     |
|     |     |     |     |     |     | 22 23          |     |        | and using VPN services.                 |     |
Data Access 25.TriStation Tricon
Distribution of IoT malware by
|     |     |     | 2   | 7 10 | 17 19 | 24 25 |     |     |     |     |
| --- | --- | --- | --- | ---- | ----- | ----- | --- | --- | --- | --- |
CPU architecture 12. MMS  3 Use an IoT/OT-aware network detection
and response (NDR) solution and
PowerPC or  ARC Cores Tangent-A5 <1% a security information and event
|               |     |     | Industrial control system protocol vulnerabilities |     |     | 2. There is a large variety of vendor-specific  |     |     |                                           |     |
| ------------- | --- | --- | -------------------------------------------------- | --- | --- | ----------------------------------------------- | --- | --- | ----------------------------------------- | --- |
| Cisco 4500 6% |     |     |                                                    |     |     |                                                 |     |     | management (SIEM)/security orchestration  |     |
ARM 26% protocols. This means vendor-specific security
We looked into OT data from our cloud  and response (SOAR) solution to monitor
| Renesas  |     |     |     |     |     | solutions won’t be able to adequately cover  |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
connected sensors, revealing the most common  devices for anomalous or unauthorized
SH 6%
industrial control system (ICS) protocols.  the whole network. Microsoft prioritizes  behaviors, such as communication with
a vendor agnostic approach, to provide
ARM  These protocols provide insights into the nature  unfamiliar hosts.
security coverage for the broad variety of
| Intel 80386  |     | AArch64 1% | of these devices and their attack surface. This is  |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Segment networks to limit an attacker’s
| 15% |     |     |     |     |     | different devices. |     |     |  4  |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
especially relevant to the security of critical
ability to move laterally and compromise
|     |     |     | infrastructure. Some key learnings are: |     |     | 3. Organizations should ensure these protocols  |     |     |     |     |
| --- | --- | --- | --------------------------------------- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
assets after initial intrusion. IoT devices
are not exposed directly to the internet from
MIPS 20% 1. Most of the protocols represented are
| Motorola  |     |     |     |     |     |     |     |     | and OT networks should be isolated from  |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- |
their networks. This exposure could pose a
m68k 4% proprietary, so standard IT monitoring tools  corporate IT networks through firewalls.
major security risk due to vulnerabilities and
|     | x86-64 19% | SPARC 3% | won’t have adequate security visibility across  |     |     |     |     |     |     |     |
| --- | ---------- | -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
the unsecure nature of these protocols.
 5 Ensure ICS protocols are not exposed
these devices and protocols. As a result,
Microsoft observed that IoT devices running on ARM  directly to the internet.
networks are left unmonitored and therefore
are most targeted by malware, followed by MIPS,
more vulnerable to OT-specific attacks.
X86-64, and Intel 80386 CPU.

Report The State of Nation State DDeevviicceess aanndd Cyber Influence Cyber Contributing
65 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
Firmware is responsible for a device’s primary The firmware updating process varies widely
Supply chain and
functions, such as connecting to a network across devices, and the complexity and logistical “ICT infrastructure suppliers are increasingly
or storing data. Firmware is found in routers, challenge of performing it impacts the update targets as they enable widespread replication
firmware hacking
cameras, televisions, and other devices used in frequency. It is not always possible to determine of a single attack. At the same time, global
Enterprises (IoT) along with industrial control if a device is running the latest firmware, making legislation, regulation, and customer demands
Almost every internet-connected device
equipment (OT) used in critical infrastructure. it difficult for security professionals to monitor for supply chain security and resiliency are on
has firmware, which is software embedded
Historically, firmware has been written and ensure the security posture in their IoT the rise, often diverging in their requirements.
in the device’s hardware or circuit board. with unsecured code, creating significant and OT devices. In addition, some devices have
The solution is partnership. Together with
Over the past few years, we have seen vulnerabilities which can be exploited to take firmware that is not cryptographically signed,
suppliers and global governments, Microsoft
increased targeting of firmware to launch over the device or inject malicious code into enabling them to be updated without verification
is committed to addressing security across our
devastating attacks. As firmware is likely to the firmware. from the user. These weaknesses further open the
supply chain ecosystem, exceeding demands
continue to be a valuable target for threat devices up to supply chain attacks throughout
This risk is compounded when it comes to from customers and regulators alike. To do
actors, organizations must protect against the supply chain. Most devices are built using the production and distribution chain. this, we are driving a comprehensive approach
firmware hacking. software and hardware components from To address these threats, Microsoft invests to security and operational resiliency that is
numerous manufacturers as well as open- significantly in ensuring the security and integrity flexibly deployed across the supply chain.
source libraries. In many cases device operators of the firmware as it moves through various
Driving firmware integrity from design
do not have visibility into the hardware and stages of the supply chain, and in attesting at any
through to device operation is key to our
software bill of materials (H/SBOM) to evaluate time that it has not been tampered with during
collective approach. Ensuring suppliers’ SDL
the supply chain risk of devices on their ingestion or along the way. This will allow us to
processes and deploying hardware root of
network. In June 2020, vulnerabilities were validate trust between each pipeline segment
trust innovation are examples of how we can
disclosed in a networking stack used by many and provide a certified and provable end-to-end
‘build in’ supply chain integrity.
different manufacturers affecting hundreds chain of custody for every component we ship
of millions of IoT devices in the consumer and to customers. We are working with our partners Our community is leveraging collective
industrial equipment space.14 In some cases, to bring this chip-to-cloud security to all devices research and development spanning new
the network stack was rebranded by other on the enterprise and OT network. anti-tampering techniques and cryptographic
vendors and there was no indication a device mechanisms, combined with ongoing
was vulnerable. We see a growing threat of monitoring and anomaly detection. Together,
malicious actors targeting this software and we are progressing in minimizing the allure
hardware supply chain of IoT/OT devices to of supply chain as an attack surface.”
compromise organizations.
Edna Conway,
Vice President, Security & Risk Officer,
Cloud Infrastructure

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
66 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
While there are solutions available to build secure
Security weaknesses in firmware images analyzed
Spotlight on firmware
devices, there are billions of devices already
vulnerabilities on the market and deployed in enterprises.
Weak passwords 27%
These are known as brownfield devices. In 2021,
Attackers are increasingly leveraging Microsoft acquired ReFirm Labs to shine a light 10+ Critical known vulnerabilities 32%
vulnerabilities in IoT device firmware on brownfield device security and enable device
builders to improve the security of their products. 10+ Critical vulnerabilities 6+ years old 4%
to infiltrate corporate networks.
ReFirm Labs analyzes the binary firmware image
Unlike traditional IT endpoints that 10+ Certificates expired 3+ years 13%
of a device and produces a detailed report on
use XDR agents to identify weaknesses,
potential security weaknesses.17 This technology
Presence of dangerous components 36%
vulnerability identification within IoT/OT
is being incorporated into a future release of
devices is much more elusive.
Microsoft Defender for IoT.
• Known vulnerabilities: Like other systems, • Software components: Thirty-six percent of
Over the past year, we examined aggregate
A recent survey conducted by Microsoft and IoT/OT device firmware extensively leveraged the images contain software components
results of the unique firmware scanned by
the Ponemon Institute highlights both the open-source libraries. However, devices Microsoft recommends be excluded in IoT
our customers. While not every weakness
opportunity and the security challenge of IoT/ frequently ship with out-of-date versions of devices such as packet capture tools (tcpdump,
discovered might be exploitable, they
OT devices in an enterprise.15 While 68 percent these components. In our analysis, 32 percent libpcap), which can be leveraged for network
underscore the fundamental challenge
of respondents believe the adoption of IoT/OT is of the images contained at least 10 known reconnaissance as part of an attack chain.
of device firmware security.
critical to their strategic digital transformation, vulnerabilities (CVEs) rated as critical (9.0 or
60 percent recognize that IoT/OT security is Note the types of weaknesses that exist in IoT/OT higher). Four percent contained at least 10
one of the least secured aspects of the IT/ devices would never be acceptable on traditional critical vulnerabilities that were more than
OT infrastructure. Windows or Linux endpoints. six years old.
An example of attackers using vulnerabilities • Weak passwords: Twenty-seven percent • Expired certificates: Certificates are used to
in IoT device firmware to infiltrate a network of the firmware images scanned contained authenticate connections and identities, as
is the Trickbot trojan which leveraged default accounts with passwords encoded using well as protect sensitive data, but 13 percent
passwords and vulnerabilities in Mikrotik weak algorithms (MD5/DES), which are of the images analyzed contained at least 10
routers16 to bypass corporate defense systems. easily broken by attackers. certificates that had expired more than three
The fundamental challenge with IoT device years ago.
firmware is the lack of visibility into the security
posture and vulnerabilities of devices.

Report The State of Nation State DDeevviicceess aanndd Cyber Influence Cyber Contributing
67 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
How Microsoft is improving supply
Firmware attacks in the wild Microsoft is partnering with Actionable insights
chain security
government and industry on firmware
Viasat: Using a firmware vulnerability Microsoft is partnering with government and 1 Gain deeper visibility into IoT/OT
to target satellite communication analysis technology to bring deeper industry to address these IoT and OT device devices on your network and prioritize
visibility into device security and security challenges (see the discussion on page them by risk to the enterprise if they
In February 2022, a satellite network incident
disconnected a strategic communication network provide full lifecycle security for 66). Our contribution will include leveraging are compromised.
firmware analysis technology to provide device
with impacts felt across Europe. Viasat’s KA-SAT device builders and operators. 2 Use firmware scanning tools to understand
operators with visibility into the security posture
system received a large amount of traffic that potential security weaknesses and work
of the devices on their network. This will enable
disconnected many modems and a denial of with vendors to identify how to mitigate
Since June 2019, a nation state-affiliated customers to identify and prioritize devices in
service attack was initiated against the network. the risks for high-risk devices.
advanced persistent threat (APT) group used need of additional protections, upgrades, or
As fixed broadband was disrupted, thousands
the modular malware Cyclops Blink to target replacement—and drive demand for device 3 Positively influence the security of IoT/
of wind turbines became remotely inaccessible
vulnerable WatchGuard firewall devices and builders to invest in device security. At the OT devices by requiring the adoption
to operators and malicious wiper malware was
ASUS routers by executing malicious firmware same time, we are supporting builders with of secure development lifecycle best
deployed to affected modems. The disruption
updates and recruiting them to a large botnet. comprehensive solutions to architect secure practices by your vendors.
affected more than 30,000 satellite terminals
The malware successfully infects devices by devices and adopt secure development lifecycles.
used by companies and organizations Links to further information
exploiting a known vulnerability that allows a
for communication. Another key component is providing builders
privilege escalation, enabling the threat actors to Assessment of the Critical Supply Chains
and operators robust infrastructure to allow
Cyclops Blink: Using a firmware supply manage the device. Once infected, the malware Supporting the US Information and
device firmware to be updated as security
chain attack to target firewall gateways allows further modules to be installed and evades Communications Technology Industry
issues are discovered and resolved. Microsoft is
firmware updates. Compromised devices have
For threat actors, the development and bringing together firmware analysis and Defender
been observed connecting to C2 servers hosted
expansion of command and control (C2) and for IoT with Device Update for IoT Hub to provide
on other WatchGuard devices. Issuing many SSL
attack infrastructure is a crucial component of a solution to address the full lifecycle of IoT and
certificates for their C2 on various TCP ports,
success. As the need for a stable C2 infrastructure OT device security. These are important steps
Cyclops Blink operators gained privileged remote
has grown, routers have become a desirable in realizing our vision for customers to secure
access to networks by executing malicious
attack vector due to their infrequent patching the infrastructure by adoption of devices that
firmware updates and by evading traditional
and lack of comprehensive security solutions. support a Zero Trust approach to their IoT and
security methods such as scanning.
OT solutions.18
Attackers are increasingly targeting
vulnerabilities in IoT device firmware
to infiltrate corporate networks.

Report The State of Nation State DDeevviicceess aanndd Cyber Influence Cyber Contributing
68 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
The unique configuration of each PLC is
Reconnaissance-based
described in the project file, which contains the
definition of the environment and its assets, the
OT attacks
ladder logic, and more.
Complex supply chains use specific design In most environments that show evidence of an We have observed
attack, analysis shows the timeline preceding the
information to plan the actual system.
a growing threat of
attack far exceeds the length of the attack itself.
Of the myriad assets that compose this
Threat actors often invest months in simulating
design information, the most sensitive is the reconnaissance-based
the environment and its assets remotely, making
project file, which defines the environment
many attempts to construct a model and OT attacks that are highly
and its assets. This file is a crucial strategic
prepare their targeted attack. As environments
target for threat actors seeking to gain continuously change and integrate new devices, tailored to their target
access and deploy a successful attack vulnerabilities are created specifically around
environments.
wholly tailored to the environment. the data in the project and configuration files.
The theft of a project file can advance an attack
by weeks or months and enable attackers to
Targeting industrial systems to disrupt
model the target environment rapidly and
operational processes involves two steps.
accurately, increasing the difficulty in detecting
1. First, the attacker must access the OT network.
malicious activity.
This can be done by entering through IoT devices
on the enterprise side of the network (Purdue Industroyer and Incontroller
Model Level 4) and crossing the IT-OT boundary,
We have observed increased attacks on
traditionally separated by firewalls and networking
organizations, critical infrastructure, and
equipment, into the operation and control levels.
government targets by state sponsored actors
2. Second, the network devices must be using modular malware and attack frameworks.
identified. Industrial systems use standard New attempts to interfere with critical operations
devices and components in customized in Ukraine underscore the growing threat of
architectures specifically designed for their reconnaissance-based OT attacks that are
environments. One of these standard devices highly tailored to their target environments.
is the programmable logic controller (PLC). The extended reconnaissance and research
Every manufacturer develops unique interfaces phases carried out by nation state cyber actors
and functions for their PLCs, which are a points to a strategy of using cyber warfare to
crucial component of industrial systems, and cripple infrastructure remotely to meet specific
these devices are further configured with strategic or operational goals in blended cyber-
customized schemas specifically designed for kinetic operations and political strategy.
the customer’s environments.

Report The State of Nation State DDeevviicceess aanndd Cyber Influence Cyber Contributing
69 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
Incontroller, a modular attack framework The Incontroller framework supports protocols
Reconnaissance-based
Actionable insights
identified during the same period, is a modular for Schneider Electric and Omron PLCs and
OT attacks toolkit that significantly reduces the lead time collects information, such as firmware version, 1 Avoid transferring files which contain
to penetrate and attack OT devices, bypassing model type, and connected devices. The toolkit system definitions through unsecure
legacy security solutions. The general-purpose can issue commands to change configurations channels, or to non-essential personnel.
Continued
toolkit has data-collection, reconnaissance, and and turn outputs on and off. Once an
In early 2022, two adaptable critical OT attacks attack capabilities that are highly customizable environment is accessed, the framework supports 2 When transferring such files is unavoidable,
were identified. A cyber-physical attack on to different environments and can greatly impact implanting backdoors in devices for the delivery be sure to monitor activity on the network
electrical substations and protection relays the research phase for an OT attack, reducing of more payloads, issuing vulnerabilities to and ensure assets are secure.
in Ukraine was carried out with customized the time necessary to perform reconnaissance, increase access points, uploading of ladder logic,
3 Protect engineering stations by monitoring
malware, including a variant of Industroyer, supporting the simulation of environments and the ability to initiate DoS attacks. The generic
with EDR solutions.
a malware known to have caused power outages by extracting information about devices and nature of the toolkit enables a threat actor to
in Ukraine after its deployment in 2016. their configurations. attack an environment quickly without needing 4 Proactively conduct incident response
to write new attacks for every PLC or location. for OT networks.
Industroyer2 is the first known redeployment
This allows the actor to easily interact with
of malicious OT attack malware on a new 5 Deploy continuous monitoring,
different types of machines potentially across
target. It utilized the IEC104 protocol (standard like Defender for IoT.
many industries.
protocol for power system monitoring and
control) plugin developed for Industroyer and
targeted mostly PLC-like remote terminal units
with model number ABB RTU540/560. The writer
of this malware used knowledge of the victim’s
environment to issue commands repeatedly
to predetermined outputs, ensuring they
could not be turned on manually. This ensured
longer lasting power outages and a more
damaging impact.

Report The State of Nation State DDeevviicceess aanndd Cyber Influence Cyber Contributing
70 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats IInnffrraassttrruuccttuurree Operations Resilience Teams
Endnotes
1 See, e.g., Revised Directive on Security of Network and Information Systems (NIS2) | 16 Uncovering Trickbot’s use of IoT devices in C2 Infrastructure (Mar 2022):
Shaping Europe’s digital future (europa.eu); https://eur-lex.europa.eu/legal-content/EN/TXT/ https://www.microsoft.com/security/blog/2022/03/16/uncovering-trickbots-use-of-iot-devices-
PDF/?uri=COM:2020:595:FIN&rid=1; Security Legislation Amendment (Critical Infrastructure in-command-and-control-infrastructure/
Protection) Act 2022 (homeaffairs.gov.au); Chile: Bill for cybersecurity and critical information 17 IoT Show on Channel 9 Episode on IoT Firmware Scanning (May 2022): https://docs.microsoft.
infrastructure introduced in Senate | News post | DataGuidance; Japan passes economic security com/en-us/shows/internet-of-things-show/iot-device-firmware-security-scanning-with-azure-
bill to guard sensitive technology | The Japan Times; Review of the Cybersecurity Act and Update defender-for-iot
to the Cybersecurity Code of Practice for CIIs (csa.gov.sg); Proposal for legislation to improve
18 How to apply a Zero Trust approach to your IoT solutions (May 2021):
the UK’s cyber resilience—GOV.UK (www.gov.uk); Telecommunications (Security) Act 2021
https://www.microsoft.com/security/blog/2021/05/05/how-to-apply-a-zero-trust-approach-to-
(legislation.gov.uk); Updating the NIST Cybersecurity Framework—Journey To CSF 2.0 | NIST
your-iot-solutions/
2 Cert-In—Home Page
3 Initiation of consultation on introduction of cyberattack reporting obligation (admin.ch)
4 See, e.g., untitled (house.gov)
5 Cyber Resilience Act | Shaping Europe’s digital future (europa.eu)
6 See, e.g., Microsoft Security Development Lifecycle
7 See, e.g., Generating Software Bills of Materials (SBOMs) with SPDX at Microsoft—Engineering@
Microsoft; see also, e.g., The Minimum Elements For a Software Bill of Materials (SBOM) |
National Telecommunications and Information Administration (ntia.gov)
8 See, e.g., https://www.microsoft.com/en-us/msrc/cvd
9 The Product Security and Telecommunications Infrastructure (PSTI) Bill—product security
factsheet—GOV.UK (www.gov.uk)
10 Commission strengthens cybersecurity of wireless devices and products (europa.eu)
11 Cloud Certification Scheme: Building Trusted Cloud Services Across Europe — ENISA (europa.eu)
12 Certification — ENISA (europa.eu)
13 https://github.com/microsoft/sbom-tool” GitHub - microsoft/sbom-tool: The SBOM tool is a
highly scalable and enterprise ready tool to create SPDX 2.2 compatible SBOMs for any variety
of artifacts.
14 https://www.zdnet.com/article/ripple20-vulnerabilities-will-haunt-the-iot-landscape-for-years-
to-come
15 IoT/OT Innovation Critical but Comes with Significant Risks (Dec 2021):
https://www.microsoft.com/security/blog/2021/12/08/new-research-shows-iot-and-ot-
innovation-is-critical-to-business-but-comes-with-significant-risks/

|     | Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber   | Contributing  |     |
| --- | ------- | -------------- | -------------- | ------------- | ---------------- | ------- | ------------- | --- |
71 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Cyber Influence
An overview of Cyber Influence Operations 72
|            |     |     |     |     |     | Introduction                           |     | 73  |
| ---------- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- |
| Operations |     |     |     |     |     | Trends in cyber influence operations   |     | 74  |
Spotlight on influence operations
during the COVID-19 pandemic and
|     |     |     |     |     |     | Russia’s invasion of Ukraine            |     | 76  |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- |
|     |     |     |     |     |     | Tracking the Russian Propaganda Index   |     | 78  |
Today’s foreign influence operations utilize new
|     |     |     |     |     |     | Synthetic media   |     | 80  |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | --- |
methods and technologies, making their campaigns
designed to erode trust more efficient and effective. A holistic approach to protect against
|     |     |     |     |     |     | cyber influence operations   |     | 83  |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |

|     |     |     | Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber   | Contributing  |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | -------------- | -------------- | ------------- | ---------------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
72 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
 An overview of

|     | Cyber influence operations are becoming increasingly  |     |     |     |     |     | Russia, Iran, and China  |     |     |     |     |     |     |     |     |     |
| --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 Cyber Influence   sophisticated as more governments and nation states  employed propaganda
|     | are using these operations to shape opinion, discredit  |     |     |     |     |     | and influence campaigns  |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 Operations
|     | adversaries, and promote discord.  |     |     |     |     |     | throughout the COVID-19  |     |     |     |     |     |     |     |     |     |
| --- | ---------------------------------- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pandemic often as a strategic
Today’s foreign influence
device to achieve broader
| operations utilize new methods  |     |     |     |     |     |     | political objectives.  |     |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and technologies, making
|                                | Progression      |     |              |        |               |     |                                   |     |     |                        |     |                   |     |                          |     |                    |
| ------------------------------ | ---------------- | --- | ------------ | ------ | ------------- | --- | --------------------------------- | --- | --- | ---------------------- | --- | ----------------- | --- | ------------------------ | --- | ------------------ |
| their campaigns designed       |                  |     |              |        |               |     | Find out more on p76              |     |     | Factors                |     |                   |     |                          |     |                    |
|                                |                  |     |              |        |               |     |                                   |     |     |                        |     | Easy-to-use tools |     | More sophisticated tools |     | Easy to distribute |
|                                | of foreign       |     |              |        |               |     |                                   |     |     | Low barrier to entry   |     |                   |     |                          |     |                    |
|                                |                  |     | Pre-position | Launch | Amplification |     |                                   |     |     | On February 24, 2022,  |     |                   |     |                          |     |                    |
| to erode trust more efficient  | cyber influence  |     |              |        |               |     |                                   |     |     |                        |     |                   |     |                          |     |                    |
|                                |                  |     |              |        |               |     | Synthetic media is becoming more  |     |     | Russia invaded Ukraine |     |                   |     |                          |     |                    |
operations
and effective.  prevalent due to the proliferation of  Organizations  Individuals  Malicious actors
Producers
|                                                     |                      |     |     |     |     |     |                                            |          |                   |                       |          | and institutions |     | and consumers |     | to cause harm |
| --------------------------------------------------- | -------------------- | --- | --- | --- | --- | --- | ------------------------------------------ | -------- | ----------------- | --------------------- | -------- | ---------------- | --- | ------------- | --- | ------------- |
|                                                     |                      |     |     |     |     |     | tools which easily create and disseminate  |          |                   | Good and harmful uses |          |                  |     |               |     |               |
|                                                     |                      |     |     |     |     |     | 1202 tcO                                   | 1022 voN | 1202 ceD 2202 naJ | 2202 beF 2202 raM     | 2202 rpA |                  |     |               |     |               |
|                                                     |                      |     |     |     |     |     | highly realistic artificial images,        |          |                   |                       |          |                  |     |               |     |               |
| Nation states are increasingly using sophisticated  | Find out more on p74 |     |     |     |     |     |                                            |          |                   |                       |          |                  |     |               |     |               |
influence operations to distribute propaganda  videos, and audio. Digital provenance  Distribution Social media Targeted emails Audio files Direct from
technology that certifies media asset  Unprecedented speed amplification and ads via voice mail the source
| and impact public opinion both domestically and  | Russia’s invasion of Ukraine demonstrates  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
internationally. These campaigns erode trust,  origin holds promise to combat misuse.
cyber influence operations integrated with
increase polarization, and threaten democratic
|     |                                            |     |     |     |     |     |     |     |     |         |     | Damage to individual  | Fraud and other  |     | Damage to organization  | Market  |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------------------- | ---------------- | --- | ----------------------- | ------- |
|     | more traditional cyberattacks and kinetic  |     |     |     |     |     |     |     |     | Effects |     |                       |                  |     |                         |         |
processes. Skilled Advanced Persistent
|     |     |     |     |     |     |     |     |     |     | Erosion of trust |     | reputation | financial damage |     | or brand | manipulation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | ---------------- | --- | -------- | ------------ |
Manipulator actors are using traditional media  military operations to maximize impact.
Find out more on p80
together with internet and social media to vastly
increase the scope, scale, and efficiency of their  Mitigation Advanced AI  Digital  Cross-industry
campaigns, and the outsized impact they are  Promising solutions systems for detection provenance efforts
  A holistic approach to protect
having in the global information ecosystem.
In the past year, we have seen these operations   against cyber influence operations
used as part of Russia’s hybrid war in Ukraine,
but have also seen Russia and other nations,
Microsoft is building on its already mature cyber threat
including China and Iran, increasingly turning
intelligence infrastructure to combat cyber influence
to social-media powered propaganda operations
operations. Our strategy is to detect, disrupt, defend,
to extend their global influence.
and deter propaganda campaigns by foreign aggressors.
|     |                        |             |                                    |                        |             |                        |                        |     |     |     |     |     |     |     |     |     |
| --- | ---------------------- | ----------- | ---------------------------------- | ---------------------- | ----------- | ---------------------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Find out more on p76   |             |                                    |                        |             |                        | Find out more on p83   |     |     |     |     |     |     |     |     |     |
|     | 1202 tcO 8 1202 tcO 81 | 1202 tcO 82 | 1202 voN 7 1202 voN 71 1202 voN 72 | 1202 ceD 7 1202 ceD 71 | 1202 ceD 72 | 2202 naJ 6 2202 naJ 61 | 2202 naJ 62 2202 beF 5 |     |     |     |     |     |     |     |     |     |
|     | Australia              |             | New Zealand                        |                        |             | United States          |                        |     |     |     |     |     |     |     |     |     |

| Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber   | Contributing  |
| ------- | -------------- | -------------- | ------------- | ---------------- | ------- | ------------- |
73 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Democracy needs   Foreign influence operations have always been  We are also studying how advanced technologies
 Introduction
|     | a threat to the information ecosystem. However,  |     |     |     | such as deep fakes can be weaponized and  |     |
| --- | ------------------------------------------------ | --- | --- | --- | ----------------------------------------- | --- |
trustworthy information
|     | what differs in the age of the internet and  |     |     |     | undermine the credibility of journalists.  |     |
| --- | -------------------------------------------- | --- | --- | --- | ------------------------------------------ | --- |
to flourish. A key area of   social media is the vastly increased scope, scale,  And we are working with industry, government,
|     | and efficiency of campaigns, and the outsized  |     |     |     | and academia to develop better ways to detect  |     |
| --- | ---------------------------------------------- | --- | --- | --- | ---------------------------------------------- | --- |
focus for Microsoft are the  impact they can have on the health of the global  synthetic media and restore trust—such as
|     | information ecosystem. |     |     |     | artificial intelligence (AI) systems that can  |     |
| --- | ---------------------- | --- | --- | --- | ---------------------------------------------- | --- |
influence operations being
spot fakes.
The age-old adage that “a lie gets halfway
developed and perpetuated by
|     | around the world before the truth has a chance  |     |     |     | The rapidly changing nature of the information  |     |
| --- | ----------------------------------------------- | --- | --- | --- | ----------------------------------------------- | --- |
nation states. These campaigns  to put its shoes on,” is now being borne out with  ecosystem and nation state online propaganda,
|     | data. A Massachusetts Institute of Technology  |     |     |     | including the melding of traditional cyberattacks  |     |
| --- | ---------------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- |
erode trust, increase
|     | (MIT) study1 found that falsehoods are 70 percent  |     |     |     | with influence operations and the interference in  |     |
| --- | -------------------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- |
|     | more likely to be retweeted than the truth         |     |     |     | democratic elections, requires a whole-of-society  |     |
polarization, and threaten
|     | and they reach the first 1,500 people six times  |     |     |     | approach to mitigate against both online and  |     |
| --- | ------------------------------------------------ | --- | --- | --- | --------------------------------------------- | --- |
democratic processes. faster. The information ecosystem has become  offline threats to democracy.
increasingly murky as propaganda campaigns
Microsoft is dedicated to supporting a healthy
flourish on the internet and social media and
information ecosystem in which trusted news
undermine trust in traditional news. In a 2021
and information thrive. We are developing tools
study,2 only seven percent of US adults said they
and threat detection capabilities to combat
have “a great deal” of trust and confidence in
the evolving and expanding risk of nation state
newspapers, television, and radio news reporting,
driven influence operations. To enable this work,
while 34 percent reported “none at all.”
we recently acquired Miburo Solutions, we
|     | Microsoft has been working to identify the main    |     |     |     | partner with third-party validators such as the    |     |
| --- | -------------------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- |
|     | actors, threats, and tactics in the foreign cyber  |     |     |     | Global Disinformation Index and NewsGuard, and     |     |
|     | influence space and to share lessons learned.      |     |     |     | we participate and at times lead multistakeholder  |     |
|     | In June this year, we published a comprehensive    |     |     |     | partnerships, including the Coalition for Content  |     |
|     | report on the lessons learned from Ukraine,        |     |     |     | Provenance and Authenticity (C2PA). Only by        |     |
|     | which contained a detailed look at Russia’s        |     |     |     | working together can we succeed in taking          |     |
|     | cyber influence operations.3                       |     |     |     | on those who seek to undermine democratic          |     |
processes and institutions.
Teresa Hutson
Vice President, Technology and
Corporate Responsibility

Report The State of Nation State Devices and CCyybbeerr IInnflfluueennccee Cyber Contributing
74 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure OOppeerraattiioonnss Resilience Teams
These foreign cyber influence operations This three-step approach was applied in late We are seeing authoritarian regimes around
Trends in cyber
typically have three stages: 2021 to support the Russian false narrative the world working together to pollute the
around purported bioweapons and biolabs in information ecosystem to their mutual advantage.
influence operations
Ukraine. This narrative was first uploaded to For instance, throughout the COVID-19 pandemic
Pre-position
YouTube on November 29, 2021 as part of a Russia, Iran, and China employed propaganda and
Cyber influence operations are becoming
Like the pre-positioning of malware within regular English-language show by a Moscow- influence operations using a blend of overt, semi-
increasingly sophisticated as technology
an organization’s computer network, foreign based American expatriate who claimed that covert, and covert methods of dissemination
evolves at pace. We are seeing an overlap cyber influence operations pre-position false US-funded biolabs in Ukraine were connected to to target democracies and further geopolitical
and expansion of the tools used in narratives in the public domain on the internet. bioweapons. The story went largely unnoticed goals (discussed further on page 76). The three
traditional cyberattacks being applied The pre-positioning tactic has long helped for months. On February 24, 2022, just as Russian regimes played on one another’s messaging and
to cyber influence operations. Additionally, more traditional cyber activities, especially tanks crossed the border, the narrative was sent information ecosystems to promote preferred
we are seeing an increased coordination if IT administrators scan their most recent into battle. A data analytics team at Microsoft narratives. Much of this coverage consisted of
and amplification among nation states. network activity. Malware that lays dormant for identified 10 Russian-controlled or influenced criticisms or conspiracy theories about the United
an extended time on a network can make its news sites that simultaneously published States and its allies peddled by government figures
subsequent use more effective. False narratives reports on February 24 pointing back to “last in official statements while promoting their own
Microsoft invested in combating foreign influence
that lay unnoticed on the internet can make year’s report” and seeking to give it credence. vaccines and responses to COVID-19 as superior
operations this year by the acquisition of Miburo
subsequent references seem more credible. In addition, Russian Ministry of Foreign Affairs to the United States and other democracies.
Solutions, a company specializing in analysis of foreign
officials held press conferences that further By amplifying one another, state operated media
influence operations. Combining these analysts
seeded false claims about US biolabs in the outlets created an ecosystem in which negative
with Microsoft’s threat context analysts, Microsoft Launch
information environment. Russian-sponsored coverage of democracies—or positive coverage
formed the Digital Threat Analysis Center (DTAC).
teams then worked to amplify the narrative on of Russia, Iran, and China—produced by one
DTAC analyzes and reports on nation state threats, Often at the time most beneficial to achieve
social media and internet sites more broadly. state media outlet was reinforced by others.
including both cyberattacks and influence operations, the goals of the actor, a coordinated campaign
combining information and threat intelligence is launched to propagate narratives through
with geopolitical analysis to provide insights and government-backed and influenced media
Progression of foreign cyber influence operations5
inform effective response and protections. outlets and social media channels.
Pre-position Launch Amplification
More than three-quarters of people across the
world said they worry about the weaponization of Amplification
information,4 and our data support these concerns.
Finally, nation state-controlled media and proxies
Microsoft and its partners have been tracking how
amplify narratives inside targeted audiences.
nation state actors are using influence operations
Often, unwitting tech enablers extend the
to achieve their strategic objectives and political
narratives’ reach. For example, online advertising
goals. In addition to destructive cyberattacks and Press conference Russian media Foreign media
can help finance activities and coordinated
cyber espionage efforts, authoritarian regimes ecosystem coverage amplifies
content delivery systems
are increasingly using cyber influence operations
can flood search engines.
to shape opinion, discredit adversaries, incite fear,
Illustration of how narratives about US biolabs and biological weapons spread via the three broad phases of many
promote discord, and distort reality.
foreign influence operations—pre-position, launch, and amplification.

Report The State of Nation State Devices and CCyybbeerr IInnflfluueennccee Cyber Contributing
75 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure OOppeerraattiioonnss Resilience Teams
Trends in cyber
Increased coordination Globally, more than three-quarters
influence operations and information sharing
of people worry about how
across government, the
information is being weaponized.
Continued private sector, and civil
To add to the challenge, private sector society is needed to
technology entities might unwittingly
increase transparency
enable these campaigns. Enablers can include
and to expose
companies that register internet domains,
host websites, promote material on social and disrupt these
media and search sites, channel traffic, and influence campaigns.
help pay for these exercises through digital
advertising. Organizations must be aware of the
tools and methods employed by authoritarian
regimes for cyber influence operations so they
can detect and then prevent the spread of
campaigns. There is also a growing need to help
consumers develop a more sophisticated ability
to identify foreign influence operations and limit
engagement with their narratives or content.
Cyber influence operations, including
authoritarian propaganda, are a threat
to democracies worldwide as they
erode trust, increase polarization,
and threaten democratic processes.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
76 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
the United States was behind the COVID-19
Spotlight on influence Topics covered by top 10 most-viewed coronavirus stories on RT.com
outbreak, writing, “in all US wars, radiological,
(October 2021–April 2022)
operations during COVID-19 chemical, biological and other banned weapons
are used, inflicting a devastating toll on people
and Russia’s invasion of Ukraine Anti-vaccine propaganda targets non-Russian readers in targeted areas.”8 Russian state media outlets
and Chinese government accounts echoed the
Nation states seeking to control the Russian English sentiment. Russia Today (RT)—a state-owned
information environment throughout the
(Translated below to English) outlet known for its role in disseminating Kremlin
pandemic and during the Russian invasion propaganda9—published at least one story
of Ukraine provide stark examples of how “Lockdowns and boosters “Vaccinations fail to curb transmission and are that promoted statements from Iranian officials
authoritarian regimes blend cyber and prevent transmission” ineffective against new strains” claiming COVID-19 might be a “product of US
information operations. ‘biological attack’ aimed at Iran & China”10 and
“Russian public figures are testing positive” “Pfizer vaccine has dangerous side effects” pushed out social media posts suggesting as
much. For example, an RT tweet from February
COVID-19 propaganda “Cases and deaths are increasing in Russia” “Mass vaccination is politically motivated”
27, 2020, read: “Show of hands, who isn’t going
Russia, Iran, and China employed propaganda “The Sputnik V vaccine is highly effective” “Pfizer and Moderna conduct to be surprised if it ever gets revealed that
and influence campaigns throughout the unregulated trials” #coronavirus is a bioweapon?”11
COVID-19 pandemic. COVID-19 featured “Vaccine proof needed on public transport”
The war in Ukraine—propaganda as a weapon
prominently in these campaigns in two
of war
central ways:
Russian COVID-19 messaging differs by language.
Russia’s invasion of Ukraine provides a distinct
1. Representations of the pandemic itself.
example of how cyber influence operations can
2. Campaigns that used COVID-19 as a strategic Campaigns that sought to obscure the origin One such example is the early suggestion be melded with more traditional cyberattacks
device to achieve broader political objectives. of the COVID-19 virus offer another example. by Russian and Iranian state media that and on the ground military operations to
The broad objective of these types of campaigns Since the start of the pandemic, Russian, Iranian, COVID-19 might be a bioweapon created by maximize their impact.
and Chinese COVID-19 propaganda boosted the United States. This claim circulated on fringe
is two-fold: first, to undermine democracies, In the lead up to the invasion of Ukraine,
coverage from the others to amplify these conspiracy websites early in the pandemic after
democratic institutions, and the image of the Microsoft threat intelligence analysts saw at
central themes. Much of this coverage consisted an interview with a law professor who claimed
United States and its allies on the global stage; least six separate Russia-aligned actors launch
of promoting criticisms or conspiracy theories he believed COVID-19 was created as a weapon.6
and second, to bolster their own standing more than 237 cyberattacks against Ukraine.
about the United States. Regularly amplifying After the interview was published on a few
domestically and internationally. These campaigns sought to degrade services
one another, state media outlets developed websites with limited reach, the story was picked
An example of this can be seen in the an ecosystem in which negative coverage of up by state-owned media outlets. PressTV, and institutions, disrupt Ukrainians’ access to
messaging by known Russian accounts and democracies or positive coverage of Russia, an Iranian English and French language outlet reliable information, and sow doubts about
media organizations targeting English language Iran, and China by one state media outlet was sponsored by the Iranian government,7 published the country’s leadership.
readers versus how the Russian government reinforced by the others time and again. an English-language story in February 2020
communicated with its own people regarding titled “Is coronavirus a US biowarfare weapon
the vaccine and severity of COVID-19. as Francis Boyle believes?” The article suggested

Cyber Influence
Operations
to degrade trust in institutions and cast doubt
Domains with traffic
on mainstream narratives. This information can
(March 9, 2022–April 30, 2022)
be manipulated to create propaganda targeting
Ukraine and the West, diminish trust in digital 500
security, and erode support for Western aid
400
to Ukraine.
Russia used other information attacks to shape 300
In a Microsoft report released in April 2022,
public opinion after events on the ground to
we showcased how in an apparent attempt to obscure or undermine facts. For example, on 200
control the information environment in Kyiv,
March 7, Russia pre-positioned a narrative
Russia launched a missile strike against a TV 100
through a filing with the United Nations (UN)
tower in Kyiv on the same day it launched a
that a maternity hospital in Mariupol, Ukraine,
destructive malware against a major Ukrainian 0
had been emptied and was being used as a
media company.12 military site. On March 9, Russia bombed the
In another example of how cyberattacks and hospital. After the news of the bombing broke,
influence operations converge, a Russian threat Russia’s UN representative Dmitry Polyanskiy
actor sent Ukrainian citizens emails purporting tweeted that coverage of the bombing was “fake
to be from residents of Mariupol, blaming the news” and cited Russia’s earlier claims about its
Ukrainian government for the war’s escalation alleged use as a military site. Russia then pushed
and calling on their countrymen to push back this narrative broadly across Russian controlled
against the government. These emails were websites for two weeks following the attack on
specifically addressed (by name) to those the hospital.
receiving the email, indicating they might
have had their information stolen in an earlier
espionage related cyberattack. No malicious links
were included, which suggests intent was pure
influence operations.
Featuring purportedly hacked, leaked, or
otherwise sensitive material is a common tactic
used by Russian actors in influence operations.
Throughout the war in Ukraine, pro-Russia social
media channels have promoted what they claim
are leaked or otherwise sensitive materials from
Ukrainian sources. Leaked or sensitive material
is used by pro-Russia social media channels and
outlets as part of a broader influence strategy
90
raM
71
raM
52
raM
20
rpA
01
rpA
81
rpA
62
rpA
Report The State of Nation State Devices and Cyber Contributing
77 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Resilience Teams
Russia’s whitewashing of atrocities has continued
Spotlight on influence
as the war has progressed. For instance, in late
operations during COVID-19 June of 2022, Russian media outlets and influencers
portrayed the bombing of a shopping mall as
and Russia’s invasion of Ukraine
justified and necessary, falsely claiming it was not
in use as a mall, but rather in use as an armory
Continued
for Ukrainian territorial defense forces.13 Several
pro-Kremlin bloggers on Telegram posted and
amplified content reinforcing the “false flag”
narrative, with bloggers pointing to alleged
indicators of fabrication including the presence
of people in military uniform in footage from
the scene14 and the absence of women in the
footage.15 Russia launched campaigns by relying
on a built-out system of propaganda messengers
and mediums. The amplification of these stories
Propaganda websites published stories about the
online provides Russia the ability to deflect blame
maternity hospital for about two weeks with a brief
on the international stage and avoid accountability.
revival beginning on April 1, 2022. Source: Microsoft
AI for Good Lab.
Nation states like Russia understand the value
Satellite images of a perinatal hospital of using information derived from closed
in Mariupol in February and March 2022 sources to influence public perceptions, using
“hack and leak” campaigns to spread counter
narratives and sow distrust.
Dmitry Polyanskiy
@Dpol_un
Links to further information
That’s how #fakenews is born. We Defending Ukraine: Early Lessons from
warned in our statement back on
the Cyber War | Microsoft On the Issues
7 March (russia.ru/en/news/070322n)
that this hospital has been turned An overview of Russia’s cyberattack
into a military object by radicals. activity in Ukraine | Microsoft
very disturbing that UN spreads Special Report
this information without verification Microsoft’s own satellite image analysis showed
#Mariupol #Mariupolhospital the perinatal hospital was bombed. The first photo is Disrupting cyberattacks targeting Ukraine |
from February 24, 2022 and the second is from March Microsoft On the Issues
24, 2022. Photo source: Planet Labs.
1 4 8

CCyybbeerr IInnflfluueennccee
OOppeerraattiioonnss
Tracking the Russian
Propaganda Index
In January 2022, nearly one thousand US
websites were referring traffic to Russian
propaganda websites. The most common
topics for Russian propaganda websites
targeting a US audience were the war in
Ukraine, US domestic politics (either pro-
Trump or pro-Biden) and COVID-19 and
vaccine-related narratives.
The Russian Propaganda Index (RPI) monitors
the flow of news from Russian state-controlled
and sponsored news outlets and amplifiers as a
proportion of overall news traffic on the internet.
The RPI can be used to chart the consumption
of Russian propaganda across the internet and
in different geographies on a precise timeline.
Microsoft notes, however, that we can only
observe the Russian propaganda posted to
previously identified websites. We do not have
insight into propaganda on other types of
websites, including authoritative news websites,
unidentified websites, and social network groups.
1202
tcO
1022
voN
1202
ceD
2202
naJ
2202
beF
2202
raM
2202
rpA
Report The State of Nation State Devices and Cyber Contributing
78 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Resilience Teams
Russian Propaganda Index in the United States
(October 2021–April 2022)
On February 24, 2022,
Russia invaded Ukraine

|     |     |     |     |     |     | Report  |     | The State of   | Nation State   | Devices and   | CCyybbeerr  IInnflfluueennccee   | Cyber   | Contributing  |
| --- | --- | --- | --- | --- | --- | ------- | --- | -------------- | -------------- | ------------- | -------------------------------- | ------- | ------------- |
79 Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure OOppeerraattiioonnss Resilience Teams
|     |     |     |     | Russian Propaganda Index: New Zealand  |     |     |     | Russian Propaganda Index in the   |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
 Tracking the Russian
Russian propaganda
|     |     |     |     | versus Australia and the United States |     |     |     | United States: English and Spanish |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
 Propaganda Index  An assessment of the RPI in New Zealand showed  The RPI also tracks propaganda across languages.  is high in Latin America
|     |     |     |     | a spike in late 2021 that was related to COVID-19  |     |     |     | Multiple outlets, including RT and Sputnik News,  |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
Continued propaganda. This spike in Russian propaganda  are available in over 20 languages. These include
|     |     |     |     | consumption in New Zealand preceded an  |     |     |     | English, Spanish, German, French, Greek, Italian,  |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
Russian Propaganda Index: Ukraine
|     |     |     |     | increase in public protests in early 2022 in  |     |     |     | Czech, Polish, Serbian, Latvian, Lithuanian,  |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
When the Ukraine war began, we saw a 216  Wellington. A second spike was clearly related to  Moldavian, Belarusian, Armenian, Ossetian,
percent increase in Russian propaganda, peaking  the Russian invasion of Ukraine and exceeded the  Georgian, Azerbaijani, Arabic, Turkish, Persian,
| on March 2. The chart below shows how this  |     |     |     | RPIs of Australia and the United States. |     |     |     | and Dari. |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
sudden increase coincided with the invasion.
The following graph shows that the RPI for
The two graphs show how Russian propaganda
|     |     |     |     | RPI,  New Zealand versus Australia  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Spanish language news in the United States is
surged soon after the invasion began.
|               |     |     |     | and the United States |     |     |     | much higher than for English language news. |     |     |     |     |     |
| ------------- | --- | --- | --- | --------------------- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
| RPI, Ukraine  |     |     |     |                       |     |     |     |                                             |     |     |     |     |     |
|               |     |     |     |                       |     |     |     | Russian propaganda consumption is 2X        |     |     |     |     |     |
(October 7, 2021–April 30, 2022)
higher among Spanish speakers
Spanish speakers
propaganda
consumption
English
|     |     | On February 24, 2022,  |     | 1202 tcO 8 1202 tcO 81 | 1202 tcO 82 1202 voN 7 1202 voN 71 | 1202 voN 72 1202 ceD 7 1202 ceD 71 | 1202 ceD 72 2202 naJ 6 2202 naJ 61 | 2202 naJ 62 2202 beF 5 |     |     | speakers |     |     |
| --- | --- | ---------------------- | --- | ---------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------- | --- | --- | -------- | --- | --- |
Russia invaded Ukraine
|     |     |     |     |     |     |     |     |     |     |     | On February 24, 2022,  | RT in Spanish is the international  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | ----------------------------------- | --- |
Russia invaded Ukraine
news outlet with the highest
| 1202 tcO 1202 voN | 1202 ceD 2202 naJ | 2202 beF 2202 raM | 2022 rpA |     |     |     |     |          |                   |                   |                   |     |     |
| ----------------- | ----------------- | ----------------- | -------- | --- | --- | --- | --- | -------- | ----------------- | ----------------- | ----------------- | --- | --- |
|                   |                   |                   |          |     |     |     |     | 1202 tcO | 1202 voN 1202 ceD | 2202 naJ 2202 beF | 2202 raM 2202 rpA |     |     |
number of page views and
|     |     |     |     | Australia | New Zealand |     | United States |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- |

Facebook followers.
Russian propaganda consumption in New Zealand is
|     |     |     |     |     |     |     |     |     | English Spanish |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
similar to Australia until the first week of December
Source: Microsoft AI for Good Research Lab
2021. After December, Russian propaganda
Russian propaganda consumption in the United States
|     |     |     |     | consumption in New Zealand increased by over  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is two times higher among Spanish speakers.
|     |     |     |     | 30 percent relative to consumption in Australia and  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the United States.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
80 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Creating synthetic media to create the effect, the “cheap fake” spread Such advanced AI-based techniques are not yet
Synthetic media
far and wide before the original video and widely used in cyber influence campaigns today,
The field of synthetic text and media is advancing
context surfaced. but we expect the problem to grow as the tools
incredibly fast as techniques that were once
We are entering a golden era for AI-
become easier to use and more widely available.
only possible with the vast computing resources More sophisticated approaches to altering media
enabled media creation and manipulation.
Microsoft analysts note this is driven by two of large movie studios are now integrated content includes the application of advanced The impact of synthetic media manipulation
into phone apps. At the same time, tools are AI techniques to (a) create purely synthetic
key trends: the proliferation of easy-to-use The use of information operations to cause harm
becoming easier to use and can generate content media, and (b) make more sophisticated edits
tools and services for artificially creating
with a level of realism that can fool even forensic of existing media. The term deepfake is often
or expand influence is not new. However, the
highly realistic synthetic images, videos, media specialists. We are very close to reaching used for synthetic media that has been created speed with which information can spread, and
audio, and text, and the ability to quickly the point at which anyone can create a synthetic using cutting-edge AI techniques (the name our inability to quickly sort fact from fiction,
mean the impact and harm caused by fakes and
disseminate content optimized video of anyone saying or doing anything. It’s comes from the deep neural networks that
other synthetically generated malicious media
for specific audiences. not unreasonable to believe we are entering an are sometimes used). These technologies are
can be much greater, as demonstrated with the
era where a significant quantity of the content being developed as standalone apps, tools,
Pelosi example.
we see online is fully or partially synthetic using and services and integrated into established
Neither of these developments is inherently
AI techniques. commercial and open-source editing tools. There are several categories of harm which
problematic on its own. AI-based technology
we consider: market manipulation, payment
can be used to create fun and exciting digital Such technologies are weaponized by bad actors
fraud, vishing, impersonations, brand damage,
content, whether creating purely synthetic or With the availability of more hoping to damage individuals and institutions.
reputational damage, and botnets. Many of
enhancing existing material. These tools are sophisticated, easy-to-use, and widely Examples of deepfake techniques include:
these categories have widely reported real-world
being widely used by enterprises for advertising
available tools, synthetic content • Face swap (video, images)—replacing a face examples, which could undermine our ability to
and communications and by individuals to create
engaging content for their followers. However, creation is on the rise and will soon in a video with another. This technique can be separate fact from fiction.
used to attempt blackmail of an individual,
synthetic media, when created and distributed be indistinguishable from reality. A longer-term and more insidious threat is to our
company, or institution, or to place individuals
with the intent to harm, has the potential to understanding of what is true if we can no longer
in embarrassing locations or situations.
do serious damage to individuals, companies, trust what we see and hear. Because of this, any
There are many high-quality free and commercial • Puppeteering (video, images)—using a
institutions, and society. Microsoft has been a compromising image, audio, or video of a public
driving force in developing technologies and
image, video, and audio editing tools. These tools video to animate a still image or second video.
or private figure can be dismissed as fake—an
can be used to make simple but potentially This can make it appear an individual said
practices, both internally and across the wider outcome known as The Liar’s Dividend.17 Recent
media ecosystem, to limit this harm.
damaging changes to digital content like adding something embarrassing or misleading.
research18 shows this abuse of technology
misleading text, face-swapping, and removing or
• Generative adversarial networks is already being used to attack financial
This section explores insights from Microsoft altering context. Such “cheap fakes” are widely
(video, images)—a family of techniques systems, although many other abuse scenarios
analysis on the current state of the art technology used to spread nefarious content, promote
for generating photorealistic imagery. are plausible.
for creating damaging synthetic content, the political ideologies, and damage reputations.
harms that can arise if this content is widely A well-known example is the 201916 video of US • Transformer models (video, images, text)—
disseminated, and technical mitigations that Speaker of the House, Nancy Pelosi, slurring her creating rich imagery from text descriptions.
can defend against synthetic media based speech and appearing inebriated. Although it was
cyber threats. quickly determined that the video was slowed

|     | Report  |     | The State of   | Nation State   |     | Devices and   |     | Cyber Influence  | Cyber   | Contributing  |     |
| --- | ------- | --- | -------------- | -------------- | --- | ------------- | --- | ---------------- | ------- | ------------- | --- |
81  Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
One approach is to build AI-based systems    open competition to build deepfake image   Second, advanced fake-creation algorithms use a
 Synthetic media
that can spot fakes—essentially “defensive”    detectors.19 It is tempting to increase investment   technique called Generative Adversarial Networks
AI systems to counter the offensive AI systems.   in developing more advanced detectors, but   (GANs) as part of the creation process. A GAN
Continued
This is an area of active research where   Microsoft is highly skeptical this will result in   plays two AI systems against each other using a
Detecting synthetic media  current systems for creating synthetic audio   meaningful improvements for two reasons:  generator to create the fake and a discriminator
and video leave telltale artifacts that can be   to detect fake images and train the generator.
Efforts are underway across industry,   First, we have excellent physical models that
spotted by trained media forensic analysts and   Any investment in developing a better detector
government, and academia to develop better   reflect the real world. Current fake creators cut
automated  tools.  will only enable the generator to improve the
ways to detect and mitigate synthetic media   corners, resulting in detectable artifacts, but
and restore trust. There are several promising   quality of the fakes.
Unfortunately, while current fakes have revealing   newer models will become ever more realistic.
paths forward, as well as barriers that   flaws, the precise artifacts tend to be specific to    There is nothing inherently special about a
warrant  consideration.  a particular tool or algorithm. This means training   real-world scene captured by a camera that
on known fakes does not usually generalize to   can’t be modeled by a computer.
other algorithms as demonstrated in a 2020
Synthetic media landscape
Factors
|     |     |     | Easy-to-use tools  |     |     | More sophisticated tools  |     |     |     | Easy to distribute  |     |
| --- | --- | --- | ------------------ | --- | --- | ------------------------- | --- | --- | --- | ------------------- | --- |
Low barrier to entry
| Producers  |     |     | Organizations     |     |     |     | Individuals    |     |     | Malicious actors  |     |
| ---------- | --- | --- | ----------------- | --- | --- | --- | -------------- | --- | --- | ----------------- | --- |
|            |     |     | and institutions  |     |     |     | and consumers  |     |     | to cause harm     |     |
Good and harmful uses
|     |     | Social media  |     |     | Targeted emails  |     |     | Audio files  |     |     | Direct from  |
| --- | --- | ------------- | --- | --- | ---------------- | --- | --- | ------------ | --- | --- | ------------ |
Distribution
Unprecedented speed  amplification  and ads  via voice mail  the source
| Effects  |     | Damage to individual  |     |     | Fraud and other  |     |     | Damage to organization  |     |     | Market  |
| -------- | --- | --------------------- | --- | --- | ---------------- | --- | --- | ----------------------- | --- | --- | ------- |
Erosion of trust  reputation  financial damage  or brand  manipulation
| Mitigation           |     |     | Advanced AI            |     |     |     | Digital     |     |     | Cross-industry  |          |
| -------------------- | --- | --- | ---------------------- | --- | --- | --- | ----------- | --- | --- | --------------- | -------- |
| Promising solutions  |     |     | systems for detection  |     |     |     | provenance  |     |     |                 | efforts  |

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
82 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Digital Provenance Technology is a modern
Synthetic media Digital provenance is a promising Actionable insights
version of cryptographic document signing,
Continued designed to capture the source, edit history, and emerging technology that has the 1 Take proactive steps to protect your
metadata of objects as they flow through today’s potential to help restore people’s trust organization against misinformation
Provenance for digital assets web. The vision and technical methods for in online media content by certifying threats through proactive consideration of
If detecting fakes is unreliable, what can be done enabling this type of end-to-end tamper-proof the origin of a media asset. your PR and communication responses.
certification of media was developed by a cross-
to protect against the harmful uses of synthetic
team of researchers and scientists at Microsoft. 2 Use provenance technology to protect
media? One important emerging technology is
digital provenance—a mechanism that enables We co-lead a cross-industry partnership aimed Publicly available solutions based on the C2PA official communications.
digital media creators with the ability to certify at bringing media provenance technology to life specification are surfacing either as a new feature Links to further information
an asset and helps consumers identify whether in Project Origin (founded by Microsoft, BBC, in existing products or new standalone apps
or not the digital asset has been tampered with. CBC/Radio-Canada, and the New York Times) and services. We expect most of the commonly A promising step forward on
Digital provenance is particularly important in and engage in the Content Authenticity Initiative used capture, editing, and authoring tools to be disinformation | Microsoft On the Issues
the context of today’s social media networks (founded by Adobe). Microsoft also worked with C2PA enabled in a few years. This presents an A Milestone Reached, January 31, 2022
given the speed with which content can travel partners in technology and media services to opportunity for enterprises to determine their
the internet and the opportunity for bad actors establish the Coalition for Content Provenance needs and uses for digital provenance today, and Project Origin | Microsoft ALT Innovation
to easily manipulate content. and Authenticity (C2PA). C2PA is a standards to require this additional layer of protection in
Coalition for Content Provenance and
organization that recently published the most the tools they use in existing workflows.
Authenticity (C2PA)
advanced digital provenance specification to
utilize with media assets including images, Explore technical details about the
videos, audio, and text. system Project Origin uses for media
A C2PA-enabled object carries a manifest authentication | Microsoft ALT Innovation
that protects the object and metadata from
tampering, and the accompanying certificate
identifies the publisher.
Synthetic media was not originally
designed to cause harm, but it is
being weaponized by bad actors
to undermine trust in individuals
900%
and institutions.
year over year increase
in proliferation of
deepfakes since 2019.20

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
83 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Detect We also need new innovations in public policy,
A holistic approach Microsoft’s strategy framework is
which needs to be a public priority. This can
As with cyber defense, the first step in countering
aimed at helping cross-sectoral include laws that enable publishers to negotiate
to protect against cyber foreign cyber influence operations is developing
stakeholders detect, disrupt, defend, advertising revenue collectively with technology
the capacity to detect them. No single company
influence operations or organization can hope to individually make and deter against propaganda— companies, and legislation that provides tax
credits to relieve local newsrooms of a portion
the progress that is needed. New, broader particularly campaigns by
of their payroll taxes for journalists they employ.
Microsoft is building on its already mature collaboration across the tech sector will be foreign aggressors. Journalists need many other tools for their craft,
crucial, with progress in analyzing and reporting
cyber threat intelligence infrastructure
including the ability to separate content from
cyber influence operations relying heavily on
to develop a broader, more inclusive view
legitimate and fraudulent sources.
the role of civil society, including in academic It is appropriate to start with one of the great
of cyber influence operations.
institutions and nonprofit organizations. technological challenges of our age—the There is also a rapidly evolving need to help
impact of the internet and digital advertising consumers develop a more sophisticated ability
Recognizing this role, researchers Jake Shapiro
We use a framework for suggested response and on traditional journalism. Since the 1700s, a free to identify nation state-driven information
and Alicia Wanless at Princeton University and
mitigation strategies to combat the threat posed and independent press has played a special role operations. While this might seem daunting,
the Carnegie Endowment for International
by operations, which can be divided into four in supporting every democracy on the planet— it resembles the work the tech sector has
Peace respectively have mapped out plans to
key pillars: detect, disrupt, defend, and deter. uncovering corruption, documenting wars, and long pursued to combat other cyber threats.
launch the new “Institute for Research on the
In addition, Microsoft has adopted four principles Information Environment” (IRIE). With support illuminating the largest societal challenges of Consider the education of consumers to look
to anchor our work in this space. First is a from Microsoft, the Knight Foundation, and Craig this and every other time. However, the internet more carefully at an email address to help spot
commitment to respect freedom of expression Newmark Philanthropies, the IRIE will create an has gutted local news by devouring advertising spam or other fraudulent communications.
and uphold our customers’ ability to create, inclusive multistakeholder research institution revenue and luring away paid subscribers. Initiatives in the United States—such as the News
publish, and search for information via our modeled after the European Organization Many local newspapers have collapsed. One of Literacy Project and the Trusted Journalism.
platforms, products, and services. Second, we for Nuclear Research (CERN). It will combine the many insights from our recent work is towns
proactively work to prevent our platforms and expertise in data processing and analysis to that lack a newspaper are unknowingly and
products from being used to amplify foreign speed up and scale new discoveries in this space. inevitably exposed to a greater than average
cyber influence sites and content. Third, we will Findings will be shared to inform policymakers, volume of foreign propaganda. For these
not willfully profit from foreign cyber influence technology companies, and consumers reasons, one of democracy’s critical defensive
content or actors. Finally, we prioritize surfacing more broadly. prongs must strengthen traditional journalism
content to counter foreign cyber influence and a free press, especially at the local
operations by utilizing internal and trusted Defend level. This requires ongoing investment
third-party data on our products. The second strategic pillar is to shore up and innovation that must reflect the A longer-term and
local needs of different countries and
democratic defenses, a longstanding priority in
continents. These issues are not easy, more insidious threat is to
need of investment and innovation. It should take
and they require multistakeholder
account of the challenges technology has created our understanding of what is
approaches, which Microsoft
to democracy, and the opportunities technology
and other tech companies true if we can no longer trust
has created to defend democratic societies
are increasingly supporting.
more effectively. what we see and hear.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
84 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
As we think about countering cyber influence including attribution statements when Through rapid radical transparency, democratic
A holistic approach
operations, disruption might play an even appropriate. We will publish an annual report that governments and societies can effectively blunt
to protect against cyber
more important role and the best approach to uses a data-driven approach to look across the influence campaigns by attributing the source
disruption is becoming clearer. The most effective company at the prevalence of foreign information of nation state attacks, informing the public,
influence operations antidote to broad deception is transparency. operations and next steps to ensure incremental and building trust in institutions.
That is why Microsoft increased its capacity improvement. We will also consider additional
to detect and disrupt nation state influence steps that build on this type of transparency.
Continued We have increased technical capacity
operations by acquiring Miburo Solutions,
The role of digital advertising is especially
Program—are helping to develop better a leading cyber threat analysis and research to detect and disrupt foreign influence
important, for instance, since advertising can help
informed consumers of news and information. company specializing in the detection of and operations and are committed to
fund foreign operations while simultaneously
Globally, new technology like the browser plugin response to foreign cyber influence operations. creating an appearance of legitimacy for foreign- transparently reporting on these
from NewsGuard can help move this effort
Our experience has shown that governments, sponsored propaganda sites. New efforts will be operations like our reporting
forward much faster.
technology companies, and NGOs should needed to disrupt these financial flows.
on cyberattacks.
This also should remind us that part of the attribute cyberattacks carefully and with ample
foundation for democracy is an education in evidence. Understanding the impact of such Deter
civics. As always, this effort needs to start in disruption is vital and can be even more helpful Finally, we cannot expect nations to change
schools. But we live in a world that requires we in disrupting cyber influence. Witness the behavior if there is no accountability for violating
receive ongoing civics education throughout US government’s information-sharing in the international rules. Enforcing such accountability
our lifetime. The new Civics at Work pledge, led lead-up to Russia’s invasion of Ukraine that is uniquely a governmental responsibility. Actionable insights
by the Center for Strategic and International put transparency into effective action—such Yet increasingly, multistakeholder action is
Studies, and of which Microsoft was an inaugural as exposing Russian plans including specific playing an important role in strengthening and 1 Implement strong digital hygiene
practices across your organization.
signatory and partner, seeks to reinvigorate civics campaigns like a plot to use a fake graphic video. extending international norms. More than 30
literacy within corporate communities. It is a As shown in last summer’s publication from online platforms, advertisers, and publishers— 2 Consider ways to reduce any unintended
good example of the breadth of opportunity including Microsoft—signed on to the recently enabling of cyber influence campaigns by
the CyberPeace Institute in Geneva on ongoing
to strengthen our democratic defenses. updated European Commission’s Code of Practice your employees or your business practices.
cyberattacks inside and outside Ukraine, there
on Disinformation, agreeing to strengthened This includes reducing supply to known
Disrupt is an opportunity for a broad range of civil
commitments to tackle this growing challenge. foreign propaganda sites.
society and private-sector organizations to
In recent years, Microsoft’s Digital Crimes Unit Like the recent Paris Call, Christchurch Call,
(DCU) has refined tactics and developed tools to advance transparency relating to cyber influence and Declaration on the Future of the Internet, 3 Support information literacy and civic
operations. Reliable reports about newly engagement campaigns as a key
disrupt cyber threats ranging from ransomware multilateral and multistakeholder action can
discovered and well-documented operations component to help societies defend
to botnets and nation state attacks. We have bring together the governments and public
can help the public better evaluate what it against propaganda and foreign influence.
learned many critical lessons, starting with the among democratic nations. Governments can
reads, sees, and hears, especially on the internet.
role of active disruption in countering a broad To this end, Microsoft will build on and extend then build on these norms and laws to advance 4 Engage directly with groups relevant
range of cyberattacks. the accountability the world’s democracies need to your industry working to address
its existing cyber reports and will release new
and deserve. influence operations.
reports, data, and updates related to what we
discover about cyber influence operations,

Report The State of Nation State Devices and CCyybbeerr IInnflfluueennccee Cyber Contributing
85 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure OOppeerraattiioonnss Resilience Teams
Endnotes
1 https://mitsloan.mit.edu/ideas-made-to-matter/mit-sloan-research-about-social-media-
misinformation-and-elections?msclkid=8dc75d6abcfe11ecad9946a058d581c9
2 https://news.gallup.com/poll/355526/americans-trust-media-dips-second-lowest-record.aspx
3 Defending Ukraine: Early Lessons from the Cyber War (microsoft.com)
4 https://www.edelman.com/sites/g/files/aatuss191/files/2022-01/2022 Edelman Trust Barometer_
FullReport.pdf
5 Russian Foreign Ministry Spokeswoman Maria Zakharova: https://tass.com/politics/1401777;
Lavrov: https://www.cnn.com/2022/05/05/opinions/sergey-lavrov-hitler-comments-ukraine-
kauders/index.html,Kirill Kudryavtsev/Pool/AFP/Getty Images
6 https://apnews.com/article/conspiracy-theories-iran-only-on-ap-media-misinformation-
bfca6d5b236a29d61c4dd38702495ffe
7 https://www.justice.gov/opa/pr/united-states-seizes-websites-used-iranian-islamic-radio-and-
television-union-and-kata-ib
8 https://www.presstv.ir/Detail/2020/02/04/617877/Is-the-coronavirus-a-US-bioweapon
9 https://www.state.gov/wp-content/uploads/2022/01/Kremlin-Funded-Media_January_update-19.pdf
10 https://www.rt.com/news/482405-iran-coronavirus-us-biological-weapon/
11 https://web.archive.org/web/20220319124125/https://twitter.com/RT_com/
status/1233187558793924608?s=20
12 https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4Vwwd
13 Russia’s Kremenchuk Claims Versus the Evidence—bellingcat
14 https://t.me/oddr_info/39658
15 https://t.me/voenacher/23339
16 Fact check: “Drunk” Nancy Pelosi video is manipulated | Reuters
17 https://lawcat.berkeley.edu/record/1136469
18 https://carnegieendowment.org/2020/07/08/deepfakes-and-synthetic-media-in-financial-
system-assessing-threat-scenarios-pub-82237
19 Deepfake Detection Challenge Results: An open initiative to advance AI (facebook.com)
20 Deepfakes 2020: The Tipping Point, Johannes Tammekänd, John Thomas, and Kristjan Peterson,
October 2020

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
86 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
An overview of Cyber Reslience 87
Introduction 88
Cyber
Cyber resiliency: A crucial foundation
of a connected society 89
The importance of modernizing
systems and architecture 90
Resilience
Basic security posture is a determining
factor in advanced solution effectiveness 92
Maintaining identity health is fundamental
to organizational well-being 93
Understanding the risks and rewards
Operating system default security settings 96
of modernization becomes crucial to
Software supply chain centrality 97
a holistic approach to resilience.
Building resilience to emerging DDoS,
web application, and network attacks 98
Developing a balanced approach to data
security and cyber resiliency 101
Resilience to cyber influence operations:
The human dimension 102
Fortifying the human factor with skilling 103
Insights from our ransomware
elimination program 104
Act now on quantum security implications 105
Integrating business, security,
and IT for greater resilience 106
The cyber resilience bell curve 108

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
87 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
An overview of
Effective cyber resiliency requires While password-based attacks The vast majority of successful
Cyber Resilience a holistic, adaptive approach to remain the main source of identity cyberattacks could be prevented
withstand evolving threats to compromise, other types of attacks by using basic security hygiene.
core services and infrastructure. are emerging.
Cyber security is a key enabler
of technological success. Find out more on p89
Find out more on p108
Innovation and enhanced
Modernized systems and architecture
productivity can only be are important for managing threats
achieved by introducing in a hyperconnected world.
security measures that
make organizations as
resilient as possible against
modern attacks.
The pandemic has challenged us to pivot our
security practices and technologies to protect
Microsoft’s employees wherever they work.
This past year, threat actors continued to take
advantage of vulnerabilities exposed during
the pandemic and the shift to a hybrid work Over the past year,
environment. Since then, our principal challenge the world experienced
has been managing the prevalence and DDoS activity that
complexity of various attack methods Find out more on p93 was unprecedented in
and increased nation state activity.
Find out more on p90 volume, complexity,
The human dimension of resilience
and frequency.
Basic security posture is a to cyber influence operations is our
determining factor in advanced ability to collaborate and cooperate.
solution effectiveness.
Find out more on p92 Find out more on p102 Find out more on p98

| Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber   | Contributing  |
| ------- | -------------- | -------------- | ------------- | ---------------- | ------- | ------------- |
88  Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
The pandemic challenged us   As a result, we must remember the basics: ninety - Recent supply chain and third-party supplier
 Introduction
|     | eight percent of attacks can be stopped with   |     |     |     | attacks indicate a major inflection point in the   |     |
| --- | ---------------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- |
to pivot our security practices
|     | basic hygiene measures in place. At Microsoft,   |     |     |     | industry. The disruption these attacks cause   |     |
| --- | ------------------------------------------------ | --- | --- | --- | ---------------------------------------------- | --- |
and technologies to protect   we manage identities and devices as part of   for our customers, partners, governments, and
|     | our Zero Trust approach, which includes least   |     |     |     | Microsoft continues to increase, illustrating   |     |
| --- | ----------------------------------------------- | --- | --- | --- | ----------------------------------------------- | --- |
Microsoft’s employees   privileged access and phish resistant credentials   the importance of focused attention on cyber
|     | to effectively stop threat actors and keep our   |     |     |     | resiliency and collaboration across security   |     |
| --- | ------------------------------------------------ | --- | --- | --- | ---------------------------------------------- | --- |
wherever they work. This
|     | data protected.  |     |     |     | stakeholders. Adversaries are also targeting   |     |
| --- | ---------------- | --- | --- | --- | ---------------------------------------------- | --- |
past year, threat actors
on -premises systems, reinforcing the need for
Today, even threat actors who lack sophisticated
organizations to manage vulnerabilities posed
continued to take advantage   technical skills can launch incredibly destructive
with legacy systems by modernizing and moving
attacks, as access to advanced tactics,
of vulnerabilities exposed   infrastructure to the cloud where security is
techniques, and procedures become broadly
more  robust.
available in the cybercrime economy. The war
during the pandemic and
|     | in Ukraine demonstrated how nation state   |     |     |     | We live in an era where security is a key enabler   |     |
| --- | ------------------------------------------ | --- | --- | --- | --------------------------------------------------- | --- |
the shift to a hybrid work   actors have escalated their offensive cyber   of technological success. Innovation and
|     | operations through the increased use of   |     |     |     | enhanced productivity can only be achieved   |     |
| --- | ----------------------------------------- | --- | --- | --- | -------------------------------------------- | --- |
environment. Since then, our
|     | ransomware. Ransomware is now a sophisticated   |     |     |     | by introducing security measures that make   |     |
| --- | ----------------------------------------------- | --- | --- | --- | -------------------------------------------- | --- |
principal challenge has been   industry with threat actors using double or   organizations as resilient as possible against
|     | triple extortion tactics to extract a pay out and   |     |     |     | modern attacks. As digital threats increase and   |     |
| --- | --------------------------------------------------- | --- | --- | --- | ------------------------------------------------- | --- |
managing the prevalence and
|     | developers offering ransomware as a service             |     |     |     | evolve, it’s crucial to build cyber resilience into   |     |
| --- | ------------------------------------------------------- | --- | --- | --- | ----------------------------------------------------- | --- |
|     | (RaaS). With RaaS, threat actors utilize an affiliate   |     |     |     | the fabric of every organization.                     |     |
complexity of various attack
network to carry out attacks, lowering the barrier
Bret Arsenault
methods and increased nation   to entry for less skilled cybercriminals and,
Chief Information Security Officer
state activity.   ultimately, expanding the attacker pool.
As a result, Microsoft designed a ransomware
elimination program. The goal of the program
Digital threat activity and the level of cyberattack   is to remediate gaps in controls and coverage,
sophistication increases every day. Many of   contribute to feature enhancements for services,
today’s complex attacks focus on compromising
and develop recovery playbooks for our security
identity architectures, supply chains, and third   operations center and engineering teams in the
parties with varying degrees of security controls.   event of a ransomware attack.
In particular, we have observed identity phishing
attacks are a clear and present threat. However,
these types of attacks are generally unsuccessful
with good identity management, phishing
control, and endpoint management practices.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
89 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Developing a holistic approach To deliver a holistic approach, we are partnering
Cyber resiliency:
Actionable insights
to cyber resiliency with organizations to identify their most critical
A crucial foundation Cyber resiliency requires a holistic, adaptive, and on-premises and online services, business 1 Build and manage technology systems
global approach that can withstand evolving threats processes, dependencies, personnel, vendors that limit the impact of a breach and
of a connected society to core services and infrastructure, including: and suppliers. We also look to identify assets enable them to continue to operate
and resources associated with customer and securely and effectively, even if a breach
• Basic cyber hygiene as described in our market expectations, regulatory and contractual is successful. Focus on common critical
The revolution in digital technology has cyber resilience bell curve. obligations, and internal operations. As these assets, support for agility, and architect
seen organizations transform to become
• Understanding and managing the risk/reward critical resources are identified, parallel efforts for adaptability (for example, hybrid and
ever more connected in both the way
trade-off of digital transformation. should detect and monitor threats, disruptions, multi- -cloud, multi- -platform), reduce attack
they operate and the services they offer. • Real-time response capabilities that enable potential attack vectors, and system and surfaces (for example, remove unused
As threats in the cyber landscape increase, proactive detection of threats and vulnerabilities. process vulnerabilities. The ability to do this applications and over --provisioned access
building cyber resilience into the fabric of
• Protection against known attacks and
under the current skills shortage requires rigor rights), assume compromised resources,
the organization is as crucial as financial in prioritization based on overall risk posed to and expect adversaries to evolve.
preventive activity against new and
and operational resilience. the organization.
anticipated attack vectors, including
2 When planning digital projects, consider
ability to automatically remediate. This type of holistic approach needs to be
potential threats alongside opportunities,
Digital transformation has forever altered the • Reduced impact of attacks and disasters adaptive against a backdrop of a continually and shared responsibilities for resilience
way organizations interact with customers, through fault isolation and segmentation. evolving threat landscape, with a goal of driving across the digital technology supply chain,
partners, employees, and other stakeholders. • Automated recovery and redundancy in the measurable performance enhancement, reduced including cloud- -based security solutions.
New technologies provide huge opportunities time to detect, respond and recover, and reduced
to engage with people, transform products, and
event of disruption.
radius of impact in the event of disruption. 3 Build systems to embed security by design
optimize operations. The pandemic accelerated • Prioritizing operational testing to find gaps The approach must also recognize the increasing and take steps to anticipate, detect,
the digital transformation by driving innovative and understanding shared responsibilities and connectedness of threats. For example, a security withstand, adapt, and respond to future
technologies which allow people to collaborate dependencies on external resources such as incident might result in a data breach with evolving threats.
in new ways and from any location. cloud-based security solutions. privacy implications, requiring many internal
4 Ensure business leaders consult
and external teams to work together to respond
As cyber threats become endemic, preventing An effective cyber resiliency program begins with with security teams as necessary to
quickly and minimize impact.
them from compromising an organization resource fundamentals such as understanding understand the risks associated with new
becomes more difficult in our “always connected” services available and having a reliable catalog developments. Likewise, security teams
world. Cyber resiliency represents an organization’s of resources that can be called upon in the event Cyber resiliency is the ability of an should consider business aims and advise
ability to continue operations and sustain growth of a disruption. Building on that foundation, enterprise to continue operations and leaders on how to pursue them securely.
acceleration despite the barrage of attacks. the program must be able to assess its own
Prevention must be balanced with survival and effectiveness, measure the performance of critical sustain growth acceleration despite 5 Ensure clear operational practices and
procedures for organizational resilience
recovery capabilities and governments and enterprises services and their dependencies, test and validate disruptions, including cyberattacks.
are in place for cyber incidents.
are developing comprehensive models that extend capabilities across on-premises and cloud
beyond security and privacy to protect assets, data, services, and feed continuous improvement
and other resources as part of cyber resiliency. across the organization’s digital lifecycle.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
90 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
The importance of Key issues impacting cyber resiliency
“Leaders should think about cyber
resilience as a critical facet of business
modernizing systems Insecure Active Directory configuration 90%
resilience. They should plan for cyber
Insecure Azure Active Directory configuration 72%
and architecture disruptions in the same way they do natural
Legacy authentication protocols 98%
disasters or other unforeseen events and
Legacy hashing algorithms 84% bring together internal stakeholders like
As we develop new capabilities for a
No privilege isolation in Active Directory via tier model 98% operations, communications, legal, and more,
hyperconnected world, we must manage
No use of Privilege Access Workstations 100% to craft strategies. Doing so will help ensure
the threats posed by legacy systems
Lack of local admin password management controls 82% organizations bring their critical business
and software. systems back online as quickly as possible
Lack of Privilege Access Management controls 84%
to resume normal business operations.
Excessive admin credentials found 98%
Legacy systems—those developed before No MFA or MFA not mandatory for privileged accounts 70% But it doesn’t stop there. As many
modern connectivity tools such as smartphones, organizations rely on third-- party suppliers
No MFA or MFA not mandatory for user accounts 90%
tablets, and cloud services became the norm- and service providers, leaders should extend
No MFA for VPN access 62%
represent a risk to an organization still using cyber resilience planning to their end- -to --
them. This risk exposure is reinforced by the No or very limited use of endpoint detection and response 52% end value chain to further ensure business
findings of the Microsoft Security Services for Skill gaps across security operations 70% continuity and resilience.”
Incident Response team, a group of security Gaps in security monitoring coverage and integration 60%
professionals that helps customers respond No SIEM/SOAR solution 56% Ann Johnson,
to and recover from attacks.
Ineffective SOC processes and operating model 54%
Corporate Vice President of Security,
Compliance, Identity, and Management
Over the past year, issues found among No immutable or usable backups 44%
Business Development
customers recovering from attacks were related Ineffective data loss prevention controls 88%
to six categories as shown in the chart on this Lack of patch and vulnerability management 76%
page. The following page outlines actionable
Unmanaged OT and legacy systems 50%
steps to take for improved resilience.
No Zero Trust of security framework adoption 88%
Insecure design and configuration across cloud platforms 86%
Over 80 percent of security incidents Lack of SDL practices in DevOps 82%
can be traced to a few missing 0 10 20 30 40 50 60 70 80 90 100
elements that could be addressed
Insecure configuration of identity provider Low maturity security operations
through modern security approaches.
Insufficient privilege access and lateral movement controls Lack of information protection control
No multifactor authentication Limited adoption of modern security frameworks
This chart shows the percentage of impacted customers missing basic security controls which are critical to
increasing organizational cyber resilience. Findings are based on Microsoft engagements over the past year.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
91 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
There are clear areas which organizations can address to modernize their approach and protect from threats:
The importance of
modernizing systems Problem Actionable steps
and architecture Insecure configuration of identity provider Follow security configuration baselines and best practices when deploying
Misconfiguration and exposure of identity platforms and its components and maintaining identity systems such as AD and Azure AD infrastructure.
Continued
are a common vector for gaining unauthorized high privilege access.
Implement access restrictions by enforcing segregation of privileges,
least privilege access and utilizing privileged access workstations (PAW)
for managing identity systems.
Insufficient privilege access and lateral movement controls Secure and limit administrative access to make the environment
Administrators have excessive permissions across the digital environment more resilient and limit the scope of an attack. Employ Privilege
and often expose administrative credentials on workstations subject to Access Management controls such as just in time access and just
internet and productivity risks. enough administration.
No multifactor authentication (MFA) MFA is a critical and fundamental user access control that all organizations
Today’s attackers do not break in, they log on. should enable. Coupled with conditional access, MFA can be invaluable in
fighting cyber threats.
Low maturity security operations A comprehensive threat detection strategy requires investments in
Most impacted organizations used traditional threat detection tools and extended detection and response (XDR) and modern cloud native
did not have relevant insights for timely response and remediation. tools employing machine learning to separate noise from signals.
Modernize security operations tools by incorporating XDR that can
provide deep security insights across the digital landscape.
Lack of information protection control Identify your critical business data and where it is located.
Organizations continue to struggle to put together holistic information Review information lifecycle processes and enforce data protection
protection controls that have full coverage across data locations and while ensuring business continuity.
remain effective throughout the information lifecycle and are aligned
with business criticality of data.
Limited adoption of modern security frameworks Zero Trust frameworks enforce concepts of least privilege,
Identity is the new security perimeter, enabling access to disparate digital explicit verification of all access, and always assume compromise.
services and computing environments. Integrating Zero trust principles, Organizations should also implement security controls and practices
application security and other modern cyber frameworks enables in DevOps and application lifecycle processes for higher assurance levels
organizations to proactively manage risks which otherwise organizations in their business systems.
might struggle to envision.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
92 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Basic security configurations must be turned on Risk posed by unknown devices
Basic security posture
Actionable insights
An organization’s devices which are not In contrast to cloud networks, where customers
is a determining factor onboarded or are outdated (both in relation know which assets are running on which 1 Even advanced solutions can be
to vulnerabilities and security agent status) operating systems, on-premises networks can undermined by the absence of basic
in advanced solution serve as potential entry points and access contain a wide variety of devices such as IoT, security configurations.
establishment routes for attackers. We found desktops, servers, and network devices that are
effectiveness that while ensuring organizational devices are not monitored or managed by the organization. 2 Invest in best practices in security posture
configurations to protect against future
onboarded with an updated endpoint detection
The average enterprise network has over 3,500 attacks. These basic settings produce a
Through our analysis, we discovered a and response1 (EDR) and endpoint protection
connected devices that are not protected massive return on investment in terms
prevalence of common blind spots in platform2 (EPP) solution is an important step, by an EDR agent and might have access to of an organization’s ability to defend
it is not guaranteed to stop ransomware.
organizational defenses which enable enterprise resources or even to high value assets. against attacks.
attackers to gain initial access, establish Advanced solutions such as EDR and EPP Microsoft Defender for Endpoint (MDE) uses
3 Onboard all applicable devices to an
a toehold, and implement an attack, are critical in detecting an attacker early network inspection to discover devices and
EDR solution.
even in the presence of advanced in the attack flow and enabling automatic provide information about device classifications
security solutions. remediation and protection. However, for those connected to the network such as 4 Be sure to update security agents and
since these advanced solutions rely on a device name, operating system distribution, ensure protection from tampering
fundamental ability to detect an attack, they and device type. to enable greater visibility and fuller
In many cases, the outcome of a cyberattack
require basic security configurations to be protection benefits of products.
is determined long before the attack begins.
turned on. In fact, we observed a prevalence
Attackers leverage vulnerable environments
of scenarios with advanced solutions in place
to gain initial access, conduct surveillance, and
that were undermined by the absence of basic
wreak havoc via lateral movement and encryption
security configurations.
or exfiltration. Stopping an attacker at an early 3,500
stage greatly increases the opportunity to reduce Best practices in security configurations is a
the overall impact. greater indicator of resilience than security average number of
operations center (SOC) analyst response time connected devices in
Microsoft studied specific configurations in
an enterprise that are
security postures to identify the most common We observed a 70 percent reduction in the
not protected by an
shortcomings in actual practice in these time it takes a SOC analyst to view and act endpoint detection
environments. This enabled us to see the most on a relevant alert over a six-month period and response agent.
common vulnerabilities exploited during human across our customer and partner population.
operated ransomware attacks that allowed the This increased awareness is a good sign.
threat actors to gain access and travel through However, while security configuration visibility
a network undetected. improved SOC analyst performance, enabling For devices not supported by an EDR agent,
product visibility by onboarding and updating at least be aware of their existence and act
the organization’s devices was a greater predictor to protect them by assessing vulnerabilities,
of successful prevention. as well as restricting network access.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
93 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Maintaining identity Users compromised by attack category
1.8
health is fundamental to
organizational well-being
1.6
Safeguarding identity is more important 4,500
than ever. While password-based attacks 1.4
remain the main source of identity
compromise, other types of attacks are
1.2 In the time it takes
emerging. The volume of sophisticated
to read this statement,
attacks continues to increase relative
to the previous norm of password spray 1.0 we’ve defended against
and breach replay.
4,500 password attacks.
Password-based attacks are still common, and
over 90 percent of accounts compromised via
these methods are not protected with strong
authentication. Strong authentication uses more
than one factor of authentication, for example
password + SMS and FIDO2 security keys.
We have seen a rise in targeted password
spray attacks, with very large spikes in volume
of attacker traffic spread across thousands of
IP addresses.
Users compromised per month by attack category. Password spray attack volumes were highly volatile, as seen in the
spikes in November 2021 and March 2022. These spikes represent thousands of users and thousands of IP addresses
touched. *“Other” indicates attacks different from password spray and breach replay, including phishing, malware,
man-in-the-middle, on-premises token issuer compromise, and others. Source: Azure AD Identity Protection.
snoilliM
0.8
0.6
0.4
0.2
0
0202
nuJ
0202
luJ
0202
guA
0202
peS
0202
tcO
0202
voN
0202
ceD
1202
naJ
1202
beF
1202
raM
1202
rpA
1202
yaM
1202
nuJ
1202
luJ
1202
guA
1202
peS
1202
tcO
1202
voN
1202
ceD
2202
naJ
2202
beF
2202
raM
2202
rpA
2202
yaM
2202
nuJ
Breach replay Password spray Other*

Maintaining identity
health is fundamental to
100
90
organizational well-being
80
70
Continued 60
% 50
40
30
20
10
0
9102
peS
9102
voN
0202
naJ
0202
raM
0202
yaM
0202
luJ
0202
peS
0202
voN
1202
naJ
1202
raM
1202
yaM
1202
luJ
1202
peS
1202
voN
2202
naJ
2202
raM
2202
yaM
Report The State of Nation State Devices and Cyber Influence Cyber Contributing
Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Steady rise in token replay attacks
Use of strong authentication Volume of detected token replay attacks
(September 2019–May 2022) The share of other forms of attack increased
70,000
in 2022. We saw a rise in targeted attacks that
specifically avoid password-based authentication 60,000
to reduce the chance of detection. These attacks
50,000
leverage browser single sign-on (SSO) cookies or
refresh tokens obtained via malware, phishing, 40,000
and other methods. In some cases, attackers
Strong authentication adoption choose infrastructure in locations near the 30,000
On a positive note, we are seeing steady geographic location of the targeted user to
20,000
growth in adoption of strong authentication further reduce the chances of detection. We have
amongst the Azure Active Directory (Azure seen a steady rise in token replay attacks, 10,000
AD) enterprise customer base. For Azure AD, reaching over 40,000 detections per month in
0
strong authentication monthly active users Azure AD Identity Protection. Token replay is the
(MAU) grew from 19 percent to 26 percent in use of tokens that were issued to a legitimate
the last year, while strong authentication MAU user by an attacker that has possession of said
for administrative accounts grew from 30 to While strong authentication usage has doubled tokens. Tokens are commonly obtained via
approximately 33 percent. since 2019, just 26 percent of users and 33 percent of malware, for example by exfiltrating the cookies
administrators are using strong authentication. Source: from the user’s browser or through advanced
This trend is positive, but significant growth is
Azure Active Directory. phishing methods.
still needed to reach majority coverage of strong
authentication; customers not already using
strong authentication in their environments
should start the planning and deployment
of strong authentication to protect their
users.3 While designing strong authentication
deployment, passwordless authentication
should be considered as it offers the most
secure usable experience, eliminating the risk
of password attacks.
1202
yaM
1202
nuJ
1202
luJ
1202
guA
1202
tpeS
1202
tcO
1202
voN
1202
ceD
2202
naJ
2202
beF
2202
raM
2202
rpA
2202
yaM
2202
nuJ
94
Detected token replay attacks per month. Source: Azure
AD Identity Protection, unique sessions flagged by the
anomalous token detection.

Microsoft Digital Defense Report 2022
40,000
30,000
20,000
10,000
0
1,200
1,000
800
600
400
200
0
1202
nuJ
1202
luJ
1202
guA
1202
tpeS
1202
tcO
1202
voN
1202
ceD
2202
naJ
2202
beF
2202
raM
2202
rpA
2202
yaM
2202
nuJ
Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
95 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
Microsoft Defender for Cloud Apps has detected
Maintaining identity Estimated instances of MFA fatigue attacks
an average of 895 such attacks per month since
the beginning of 2022. This form of attack can health is fundamental to
be prevented by using phish-resistant factors of
organizational well-being MFA, such as Certificate Based Authentication,
Windows Hello for Business, or FIDO2
security keys.
Continued
Extracting tokens
Password-based attacks are the
More than malware, attackers need credentials primary method by which accounts
to achieve their goals. In fact, 100 percent of all
are compromised.
human operated ransomware attacks include
stolen credentials. Many sophisticated intrusions
include credentials purchased from the dark web,
MFA fatigue
initially stolen from unsophisticated and broadly
distributed credential theft malware. This class of Using the concept of “MFA fatigue,” attackers
malware has evolved to steal tokens, including generate multiple requests for MFA to the Source: Azure AD Identity Protection.
session information and MFA claims. This means victim’s device, hoping that the victim will accept
that infections on home systems, where users the request either inadvertently or as a result of Detected instances of phishing followed by
log in to corporate assets, can lead to serious fatigue. This attack can be prevented by using man-in-the-middle attacks
incidents on corporate networks. modern authenticator apps such as Microsoft
Authenticator combined with features such
Attackers can also extract tokens from victims’
as number matching4 and enabling additional
devices through man-in-the-middle attacks,
context.5 Azure AD Identity Protection estimated
in which the victim clicks a malicious link in a
there are 30,000 MFA fatigue attacks per month.
phishing email or instant message and is directed
to a website that looks like the legitimate sign-in
page of the identity provider. In reality, it is a web
The share of sophisticated attacks
service spun up by the attacker that relays and
continues to rise, underscoring the
intercepts all traffic between the user and the
identity provider. The attacker is able to intercept need for phish-resistant factors of
the username and password and also to relay multifactor authentication.
MFA challenges; resulting tokens issued by the
identity provider and intercepted by the attacker
might contain MFA claims that can be used by
the attacker to satisfy MFA requirements.
2202
naJ
2202
beF
2202
raM
2202
rpA
2202
yaM
Actionable insights
1 Ensure all the accounts across your
organization are protected by strong
authentication measures.
2 Passwordless authentication offers the
most secure and user-- friendly experience,
eliminating the risk of password attacks.
3 Disable legacy authentication across
your entire organization.
4 Protect high value and administrative
accounts with phish --resistant forms of
strong authentication.
5 Modernize from an on --premises identity
provider to a cloud identity provider and
connect all your apps to the cloud- -based
identity provider for consistent user
experience and security.
Links to further information
This World Password Day consider ditching
passwords altogether | Microsoft Security
Source: Microsoft Defender for Cloud Apps.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
96 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Customers who embrace defense—in depth
Operating system For devices where security is Actionable insights
including a layered security posture, new
default security settings security features, regular and consistent patching not enabled by default, Microsoft 1 Use a passwordless solution which
and updates, as well as security training and recommends manually configuring binds sign --on credentials in the Trusted
awareness to report phishing and other scams them in settings where possible. Platform Module, specifically look for
With the continuously evolving security
– can expect less malware. a passwordless solution that meets the
threat landscape, we see an increasing need
To simplify defense in depth, Windows 11 Faster Identity Online (FIDO) Alliance8
for computer security configured by default
has tightly integrated hardware and software industry standard.
to improve cyber resiliency. While operating
protections turned on by default, including
system security is more urgent, complex, 2 Perform timely clean up of all unused and
memory integrity, Secure Boot, and a Trusted
stale executables sitting on organizations’
and business critical than ever before, it can
Platform Module 2.0. Windows 10 users on
devices.
be challenging to get right and manage.
capable hardware can also turn these features
on in the Windows Settings app or in the 3 Protect advanced firmware attacks by
In the past, computer and device security BIOS menu. enabling memory integrity, Secure Boot,
included built-in security features that the and Trusted Platform Module 2.0, if not
Older devices in general often do not have
customer or IT professional was expected enabled by default, which hardens boot
as strong an alignment between hardware
to configure to their own desired level. using capabilities built into modern CPUs.
security and software security techniques.
This approach is no longer adequate, as
For devices where security is not enabled by 4 Turn on data encryption and
attackers are using more advanced tools in
default, manually configure them in settings credential protection.
automation, cloud infrastructure, and remote
where possible.7
access technologies to achieve their aims. It has 5 Enable application and browser
become critical that all layers of security, from controls for enhanced protection from
the chip to the cloud, are configured by default. untrusted applications and other built-in
Microsoft has evolved to configure Windows exploit protections.
operating system security by default.6
6 Enable memory access protection to help
protect against casual physical attacks
such as someone plugging a malicious
device into externally accessible ports.
Be proactive about applying
Links to further information
continuous operating system
Windows Security Book | Commercial
updates and security patches that New security features for Windows 11
will help protect hybrid work | Microsoft
help provide protection throughout
Security Blog
the hardware and software lifecycle.

3.5M
3.0M
2.5M
2.0M
1.5M
1.0M
0.5M
0.0M
0M
snoitazinagrO
fo
tnuoC
detamitsE
Report The State of Nation State Devices and Cyber Influence Cyber Contributing
97 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
For in-support application versions, we see a
Software supply Commercial penetration Software resiliency maintenance
plateauing of the speed of critical patch adoption,
of most-used applications
which is the opposite of the trend that will drive should include regular disabling or
chain centrality
resiliency. Instead, the curve should show an uninstalling of unused applications.
exponential upwards adoption of patches month
Attacks on third-party apps, plugins,
over month, to achieve the resiliency needed.
and extensions can erode customer trust
The security and compliance of an
in suppliers that play a central role in the
Rate of critical patch deployment organization depends on its own
supply ecosystem. Using network theory
to look at software centrality helps 100 efforts and on the efforts of its
90 illuminate the criticality of patching, software suppliers.
80
especially for central apps. 70
78% of devices still
35M 70M 105M 140M 60
Estimated Active Device Count % at risk after 9 months
50
The Windows App Network of 18 million
Publisher Microsoft Corporation Third Party 40
application executables is installed and used
across five million organizations, providing a The top applications are used by millions of organizations 30 Actionable insights
20
top-level view of our software ecosystem. Of
and tens of millions of devices. Because they are near
10 1 Perform timely updates to all applications
ubiquitous, adversaries are on constant lookout to
the 100,000 most used applications, 97 percent 0 and endpoints through your organization.
exploit vulnerabilities in these top applications, which
are produced by third-party organizations whose 0 Day 3 mo 6 mo 9 mo
updates and security patches are maintained by can impact millions of devices in the user base. 2 Perform timely cleanup of all unused
Unpatched Patched
and stale executables sitting on
them. This illustrates two important traits of our We observe millions of commercial devices still
commercial application ecosystem. using vulnerable application versions many After examining a critical vulnerability that affected 134 organizations’ devices.
versions of a set of browsers, we found that 78 percent,
First, there is centrality in the Windows commercial months after patch release or even years beyond Links to further information
or millions of devices, still used one of the affected
application ecosystem. Only the top 100,000 (of the the end of product support. For example, there versions nine months after the patch was released. Microsoft Intune documentation |
18 million) applications are used on 1,000 or more are more than one million active Windows
Microsoft Docs
devices. In other words, just over one half of 1 commercial devices running version of a PDF We used the InterpretML9 toolkit to identify
percent of these applications have this kind of broad- reader that has not been supported since 2017. characteristics correlated with organizations that Manage apps | Microsoft Docs
reaching effect among the device ecosystem. are more likely to have devices with older app
Microsoft Defender for Endpoint |
versions. The most important of these predictors
Second, there is diversity in the manageability Old versions of applications which Microsoft Security
included: low hours of engagement on devices;
of those applications, where the top 10,000 are unsupported remain in active
geographic areas such as Asia Pacific and Latin OSS Secure Supply Chain Framework |
application suppliers manage the updates
use on millions of commercial devices. America; and industries such as automotive, Microsoft Security Engineering
and security patches of these most used
As a result, organizations are at risk chemicals, telecommunications, transport
commercial applications. This demonstrates Microsoft Open Source Software Secure
and logistics, health payors (claim handlers),
the interdependence a company has on a of carrying vulnerabilities that will Supply Chain Framework | GitHub
and insurance.
diverse set of software suppliers’ security, not be patched.
compliance, and management controls.

|     |     | Report  | The State of   | Nation State   | Devices and   | Cyber Influence  | Cyber   |     | Contributing  |     |     |
| --- | --- | ------- | -------------- | -------------- | ------------- | ---------------- | ------- | --- | ------------- | --- | --- |
98  Microsoft Digital Defense Report 2022  Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
 Building resilience    Number of DDoS attacks and duration distribution
Distributed  denial  of
(March 2021–May 2022)
|  to emerging DDoS,   | service (DDoS) attacks   |     |     |     |     |     |     |     |     |     |     |
| -------------------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3,000
Over the past year, the world experienced DDoS
 web application, and
activity that was unprecedented in volume,
complexity, and frequency. This DDoS explosion
 network attacks
was driven by a substantial increase in nation
2,500
state attacks and continued proliferation of low-
| Accelerated digital transformation has   | cost DDoS-for-hire services. Microsoft mitigated   |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
brought an end to the traditional network
an average of 1,955 attacks per day, a 40 percent
| and security perimeter model. Moving to    | increase from the prior year. Previously, the peak   |     |     |        |     |     |     |     |     |     |     |
| ------------------------------------------ | ---------------------------------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| the cloud means enterprises must adopt     | number of attacks normally occurred during the       |     |     | 2,000  |     |     |     |     |     |     |     |
| cloud-native network security to protect   | end-of-year holiday season. This year, however,      |     |     |        |     |     |     |     |     |     |     |
the most recorded in a day was on August 10,
digital assets.
2021. This might indicate a shift toward year-
round attacks and highlights the importance
1,500
of ongoing protection beyond traditional peak
Attack complexity, frequency, and
traffic seasons.
volume continue to grow and are
In November 2021, Microsoft thwarted a
no longer limited to holiday seasons,
|                                        | volumetric DDoS attack with a throughput of 3.4   |     |     | 1,000  |     |     |     |     |     |     |     |
| -------------------------------------- | ------------------------------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| indicating a shift toward year-round   | terabits per second (Tbps) from approximately     |     |     |        |     |     |     |     |     |     |     |
10,000 sources spanning multiple countries.
attacks. This highlights the importance
Similar high volumetric attacks above 2+Tbps
of ongoing protection beyond
were mitigated in 2022 highlighting that it’s not
500
traditional peak traffic seasons.
just the complexity, frequency of attacks that’s
increasing, but also the volume (bandwidth)
of attack.
|     | Attack duration  |     |     | 0   |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 2202 yaM
|     |     |     |     | 1202 raM 1202 rpA | 1202 yaM 1202 nuJ | 1202 luJ 1202 guA  | 1202 peS 1202 tcO | 1202 voN | 1202 ceD 2202 naJ | 2202 beF 2202 raM | 2202 rpA |
| --- | --- | --- | --- | ----------------- | ----------------- | ------------------ | ----------------- | -------- | ----------------- | ----------------- | -------- |
Most attacks observed over this past year were
short-lived. Approximately 28 percent of the
attacks lasted less than 10 minutes, 26 percent
lasted 10–30 minutes and 14 percent lasted
|     |     |     |     | 1–2 min  | 3–5 min  | 6–10 min  | 11–20 min  | 21–30 mins  |     | 31–40 min  | 41–50 min  |
| --- | --- | --- | --- | -------- | -------- | --------- | ---------- | ----------- | --- | ---------- | ---------- |
31–60 minutes. Thirty-two percent of the attacks
|     |     |     |     | 51–60 min  | 1–2 hours  | 2–3 hours  | 3–4 hours  | 4–10 hours  |     | >10 hours  |     |
| --- | --- | --- | --- | ---------- | ---------- | ---------- | ---------- | ----------- | --- | ---------- | --- |
were more than an hour in duration.
Most attacks in the last year were short-lived. Approximately 28 percent of the attacks lasted less than 10 minutes.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
99 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
Geographic target regions
Building resilience DDoS attack vectors Web application exploits
Of the DDoS attacks detected over the past year,
to emerging DDoS, UDP Spoof flood attacks 55% 54 percent were conducted against targets in Web application firewall (WAF), in combination
the United States, a trend that might partially with DDoS protection, forms an integral part of
web application, and be explained by the fact that most Azure and defense-in-depth strategy for protecting web
Other 20% Microsoft customers are in the United States. and application programming interface (API)
network attacks We also saw a sharp uptick in attacks against assets. Microsoft observed upwards of 300 billion
India, from just 2 percent of all attacks in the WAF rules triggered per month via Azure WAFs.
Continued second half of 2021 to 23 percent in first half of
TCP Ack flood attacks 19% 2022. East Asia, Hong Kong in particular, remains Distribution most prevalent attack types
DDoS attack vectors
a popular target at 8 percent. For Europe, we saw
In the past year, the attack vectors commonly concentrations of attacks against Amsterdam, Header injection attacks 1%
employed were User Datagram Protocol (UDP) Vienna, Paris, and Frankfurt regions.
reflection on port 80 using simple service DNS amplification attack 6% Remote code execution
(RCE) attacks 1%
discovery protocol (SSDP), connectionless
UDP Spoof flood attack rose to the top vector in
DDoS attack destination
lightweight directory access protocol (CLDAP),
the first half of 2022, from 16 percent to 55 percent. Cross site scripting
domain name system (DNS), and network time United States 54% (XSS) attacks 5%
TCP Ack flood attack decreased from 54 percent to
protocol (NTP) comprising one single peak.
19 percent. United Arab Emirates 1%
We also saw an increase in application layer RFI injection attacks 5%
DDoS attacks targeting websites, with Australia 1%
16.3 million peak RPS (requests per second) LFI injection attacks 21%
Japan 1%
and 9.89 Tbps peak traffic.
South Korea 1% SQL injection attacks 67%
United Kingdom 1%
In 2022, Microsoft mitigated nearly Azure WAF detects billions of Open Web Application
Brazil 1% Security Project (OWASP) Top 1010 attacks daily.
2,000 DDoS attacks daily and thwarted
According to our signals, attackers most attempted
the largest ever DDoS attack reported South East Asia 3% SQL injection attacks followed by local file injection
in history. Europe 6% and remote file injection attacks. This is in line with
the OWASP Top Ten list showing injection attacks
East Asia 8%
The gaming industry continues to be the top as the third most common type of web attacks.
target of DDoS attacks, mostly from mutations of India 23%
the Mirai botnet and low-volume UDP protocol There has also been an increase in bot attacks
attacks. Since UDP is commonly used in gaming We attribute the high volume of attacks in Asia to the against Azure web applications, with an average
region’s huge gaming footprint, especially in China,
and streaming applications, an overwhelming of 1.7 billion bot requests per month and 4.6
Japan, South Korea, and India. This footprint will continue
majority of the attack vectors were UDP spoof percent of that traffic consisting of bad bots.
to expand as increasing smartphone penetration drives
floods, while a small portion were UDP reflection
the popularity of mobile gaming, suggesting this
and amplification attacks.
geographic target will only continue to grow.

Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
100 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
Building resilience
Network intrusions: detection and prevention Actionable insights
to emerging DDoS, We observed a significant increase in network layer exploits, particularly 1 Inspect all traffic between systems within
malware, in 2022. Azure Firewall intrusion detection and prevention system a data center or cloud service, and traffic
web application, and (IDPS) blocked more than 150 million connections in the month of June alone. seeking to access them.
network attacks 2 Develop a robust all-year-round network
IDPS Deny traffic reason
security response strategy.
Continued Lateral attacks remote JA3—malicious 3 Use cloud native security services to
management 2% encrypted traffic HTTPS 38% implement a robust zero trust network
Due to an increasing number of bots security posture.
Malicious DNS
performing credential stuffing attacks, Links to further information
traffic DNS 5%
credit card fraud, cyber influence Improve your security defenses for
campaigns, and supply chain attacks, ransomware attacks with Azure Firewall |
Azure Blog and Updates | Microsoft Azure
we expect to see a steady increase in
bot attacks against web applications. Attempted user Anatomy of a DDoS amplification attack |
User agent HTTP 26% privilege gain RPC 29% Microsoft Security Blog
Intelligent application protection from
edge to cloud with Azure Web Application
IDPS traffic alert reasons
Firewall | Azure Blog and Updates |
Microsoft Azure
Malicious DNS Remote execution over
traffic—Non-DNS traffic SMB SMB/SMB2 76%
on DNS port DNS 4%
JA3—malicious encrypted
traffic HTTPS 20%
Analysis of IDPS alert and deny traffic shows the following approaches used by
attackers. In the Deny traffic, we are seeing attackers using SSL to hide their activities
and remote execution attacks are becoming more common. In the Alert traffic,
we are seeing SMB/SMB2 protocols used to perform remote execution attacks.

Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
101 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
Data governance, security, compliance, Working from the same data inventory and
Developing a balanced
Actionable insights
and privacy are interdependent activity information facilitates cross-team
approach to data security We have seen data gain prominence in recent processes, yields a more comprehensive risk 1 Balance defense with recovery and
years as a crucial value creation engine for picture, and allows organizations to better minimize data breach impact by investing
and cyber resiliency organizations. At the same time, the rise prepare and streamline their response to in compliance, data protection, and
of privacy regulations requiring both data a breach. response capabilities.
The digital transformation has fueled a governance and security have blurred the lines 2 Develop and adopt processes and tools
between risk roles. While newer C-level roles
vast expansion of data assets and a rise Data inventory that cut across data risk silos and cover
such as the Chief Data Officer (CDO) or the Chief
in security, compliance, and privacy risks. and activity the full data estate.
Privacy Officers (CPO) have a vested interest in CIO
Cyber resilient organizations must balance
security and compliance, the implementation CRO Links to further information
investments in data protection, compliance,
and operationalization of data protection often CCO
and recovery capabilities and integrate CISO
Microsoft Purview——Data Protection
relies on teams led by the Chief Information
Solutions | Microsoft Security
these with specialized regulatory response CDO
Officers (CIO) and/or Chief Information Security
processes to address distinct types Officer (CISO). It is not a one-way street, as CPO The future of compliance and data
DPO
of breaches. data governance initiatives led by CDOs also governance is here: Introducing Microsoft
have security benefits. As a result of this Purview | Microsoft Security Blog
interconnectedness, IT, data governance, security,
Data breaches are not a matter of if, but when.
compliance, and privacy teams need to work
The IBM and Ponemon Institute’s “Cost of a Data The “single pane of glass” should act as a prism.
Breach, 2021” study reports a global average data ever more closely to achieve efficiency and Teams that have a stake in data security, compliance,
breach cost of $4.24 million USD (up 10 percent manage risk. and privacy need different yet consistent views of
from the previous year) and $9.05 million USD in the same data inventory and activity to come into
Unified data risk management platforms
the United States. Compliance failures were found
alignment and collaborate. Data activity includes data
for the entire organization’s data estate access, modification, and movement events, which are
to be the top cost-amplifying factor. Conversely,
is the future a valuable part of the data security equation.
breach cost reductions were associated with best
Aligning IT, data governance, security,
practices such as incident response (IR) planning,
compliance, and privacy management process
Zero Trust deployment maturity, security AI and
Effective data governance,
automation, and use of encryption.
is difficult in an environment of bespoke
applications for each discipline and inconsistent security, compliance, and privacy
coverage across the typical organization hybrid, are interdependent and require
Data breaches are inevitable. multi-cloud data sprawl. We believe that
cross-team collaboration.
Organizations that take a balanced organizations need a single pane of glass to
locate and know their data, protect their data,
resilience approach will reduce
govern the access, usage, and lifecycle of data,
the frequency, impact, and cost
and prevent data loss across the data estate.
of breaches.

Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
102 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
Questions arise about what we can do to prepare We also recognize that restoring trust in
Resilience to cyber
Links to further information
for a more resilient future against these cyber digital content is an ambitious goal that will
influence operations: influence operations. Technology is only one require diverse perspectives and participation. Applications for artificial intelligence in
part of the puzzle. It’s going to take multiple There is not one company, or institution, or Department of Defense cyber missions |
The human dimension efforts, including education aimed at media government that can solve these threats on Microsoft On the Issues
literacy, awareness, and vigilance, investments in its own. Our superpower as humans is our
Artificial Intelligence and Cybersecurity:
quality journalism—with trusted reporters on the ability to collaborate and cooperate. This is
Over the last five years, advances in Rising Challenges and Promising
scene, locally, nationally, and internationally— especially important now because it will require
graphics and machine learning have Directions. Hearing on Artificial
networks of sharing and alerting about influence everyone—global governments, industries,
Intelligence Applications to Operations
introduced easy-to-use tools capable
operations, and new kinds of regulations that academia, and especially news, social, and
in Cyberspace before the Subcommittee
of quickly generating high-quality, penalize malevolent actors who generate or media organizations—working together for
on Cybersecurity, of the Senate Armed
realistic content that can spread manipulate digital media with an aim to deceive. the betterment and health of our society.
Services Committee, 117th Congress
widely across the internet in seconds.
(May 3, 2022; Testimony of Eric Horvitz)
When it comes to events reported via text, audio,
and visual content, we have reached a point
where neither humans nor algorithms can reliably
distinguish fact from fiction. The proliferation
of these tools and their outputs are casting
doubt on the trustworthiness of all digital media,
disrupting our understandings of local and
world events. New forms of influence operations
enabled by advances in technology have grave
implications for democratic processes.11

Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
103 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
A targeted, centralized cybersecurity skilling Program specific: Targeted training programs
Fortifying the human
Actionable insights
program reaches every Microsoft employee support specific cybersecurity initiatives including
factor with skilling at least once each year. Training offerings are Shadow IT, Insider Threat, and Microsoft Federal. 1 Provide security training and resources to
optimized to support current cybersecurity These offerings are tightly integrated into the employees when and where they need it.
initiatives and deliver measurable behavior overall engagement strategy for their respective
Addressing the human factor is a key outcomes. Microsoft’s Information Risk cybersecurity initiatives through executive 2 Develop a centralized skilling strategy
component of any cybersecurity skilling Management Council (IRMC) plays a key role sponsorship and scorecard reporting to prevent informed by stakeholders from across
strategy. According to a Kaspersky Human in identifying important cybersecurity behavior a “check the box” training approach. the enterprise.
Factor in IT Security study,12 46 percent change outcomes to be addressed by training.
MSProtect: Microsoft’s centralized web resource 3 Ensure the impact of training is tracked
of cybersecurity incidents involve careless
With all of our cybersecurity skilling programs, provides best practices, company policy and analyzed for efficiency (quantity),
or uniformed staff who inadvertently we measure the solution’s efficiency, information, and incident reporting for all things effectiveness (quality), and outcomes
facilitate the attack. effectiveness, and outcomes where possible. cybersecurity related. This on-demand resource (business impact).
For example, our insider threat skilling offering is the go-to for employees outside of formal
Links to further information
Microsoft’s Education and Awareness team in has 95 percent training compliance, exceptional training offerings.
the Digital Security and Resilience organization learner satisfaction, and has resulted in a Microsoft launches next stage of skills
is responsible for fortifying the human factor significant increase in managers reporting initiative after helping 30 million people
Security skilling must not be seen as
of cybersecurity by empowering employees to possible insider threat cases via the company’s
secure our own and our customers’ systems Report It Now tool. The program includes:
a compliance, check-the-box activity.
and data. Our goals are to: Instead, focus on behavior change
Security Foundations: Centralized, enterprise-
• Reduce risk to Microsoft and our customers wide cybersecurity awareness and compliance to allow outcomes to be monitored
by building a centralized enterprise- training which addresses core security and across identified target behaviors,
wide core security skill set across the privacy practices. This highly anticipated training and establish listening systems to
employee population. series employs an edutainment model to
determine the impact of offerings.
make learning about cybersecurity engaging
• Fortify employee security knowledge
and interesting.
through a multi-phased training
reinforcement approach to support desired STRIKE: Microsoft’s required technical training
behavior outcomes. for engineers who build and maintain line-
• Foster culture change by making a security of-business solutions. This by-invitation-only
mindset an intrinsic part of Microsoft’s culture training addresses timely and critical areas of
through annually required security training cybersecurity hygiene best practice and uses a
and events. live hybrid delivery model tailored
to audience needs.
• Promote a one-stop centralized web resource
for best practices, company policy information,
and incident reporting for all things
cybersecurity related.

Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
104 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
The first step was understanding the extent of Embedding findings into our own enterprise
Insights from
Actionable insights
our protection against a ransomware attack
To remediate the top risks and protect our
our ransomware directed at Microsoft. Efforts were already well critical services against a ransomware attack, 1 Document and validate end-to-end
underway to deploy Defender for Endpoint we plan to focus investments over the next 6 to recovery and remediation activities
elimination program and to ensure all devices are managed and 12 months on achieving the five scenarios below related to ransomware attacks against
compliant with our Zero Trust policies, but we as part of a dedicated ransomware program. critical services.
needed to find a way to understand all facets
Microsoft has been on its own Zero Trust of the bigger question as to whether we could Once we succeed in each of the scenarios, we will 2 Involve stakeholders in updating your
gradually expand the scope of the program to
journey13 in the past five years to ensure effectively recover from an attack. To gain insight, Enterprise Crisis Management playbooks
reach all parts of the enterprise.
identities and devices are robustly managed we evaluated the NIST 8374: Ransomware Risk to include ransomware specific activities
and healthy. As the risk of ransomware Management: A Cybersecurity Framework (CSF) Scenario 1: Security team members understand and a decision process and guidance to
grows, we have developed a deep view Profile,14 which aligns with our overall enterprise the overall risk associated with a ransomware determine if/when to pay for ransomware.
to support our approach to protecting policy against our known list of controls. attack and have a process established to provide
3 Improve detection and protection
ourselves and our customers. This analysis quickly identified gaps in coverage. awareness to the executives on control gaps and coverage by enabling capabilities available
risk status.
Next, we prioritized gaps across the Identify, in your deployed security products (e.g.
Following an in-depth internal evaluation, Detect, Protect, Respond, and Recover functions Scenario 2: Security team members have access Defender for Endpoint Attack Surface
we built a ransomware elimination program of the CSF. We found strategic alignment to playbooks designed to help them and other Reduction rules).
to remediate gaps in controls and coverage, to Zero Trust and other programs and also teams within Microsoft respond to and recover
contribute to feature enhancements for services discovered gaps that had no existing workstream. critical services from a ransomware attack. 4 Work with the security standards team to
define a baseline for protection against a
like Defender for Endpoint, Azure, and M365, Having assessed the amount of work and effort Scenario 3: Enterprise Resilience team members ransomware attack, and provide training
and to develop playbooks for our SOC and needed to remediate these gaps, we separated have a standard to follow for the backup of and documentation to engineering
engineering teams on how to recover in the them into two pillars: critical systems. Playbooks exist and regular teams on how to protect against a
event of a ransomware attack. • Protect the enterprise (PtE): Define work exercises of backup and recovery are done to ransomware attack.
items that we need to do as an enterprise to ensure data can be recovered in the event of a
protect ourselves and be able to recover from ransomware attack. 5 Put automation in place to make the
deployment of security and operations
an attack, should one be successful. Scenario 4: Service owners understand and
policies easier on the DevOps teams
• Protect the customer (PtC): Build capabilities implement the required security and operational and ensure that if a system drifts
into our offerings to protect our customers as controls and policies to protect their service, from compliance it is quickly flagged
well as our business. customer data, endpoints and network assets and remediated.
against ransomware attacks with special focus on
services prioritized as Microsoft critical services. Links to further information
Scenario 5: All employees can access educational Sharing how Microsoft protects against
and training resources which describe how to ransomware | Microsoft Inside Track
recognize a ransomware attack and how to notify
the security team and initiate the response.

Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
105 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
As quantum computers become a reality,
Act now on quantum
Quantum computing is a threat to today’s New post-quantum cryptography
third-party software components containing
cryptography and everything it protects. implementations of cryptographic algorithms algorithms are under review through NIST’s
security implications
and capabilities will require additional scrutiny Post-Quantum Cryptography Standardization
as well. This requires all organizations along the program. This work will influence global
The pressure is on to manage the threat The threat to today’s cryptography
value chain to do their part to ensure the chain efforts within standards bodies.
quantum computing poses to today’s
With Shor’s 1994 algorithm and an industrial- stays secure. Industry bodies and governments
cryptography and everything it protects. scale quantum computer of more than a few are increasing efforts to define software supply
The recently issued Memorandum on million physical qubits, all our current, widely chain security requirements and, in some cases,
Actionable insights
Improving the Cybersecurity of National deployed public-key cryptographic algorithms introducing new mandates for securing the
Security Department of Defense and could be efficiently broken. It is critical to chain. National Security Memorandum NSM-819 Alongside SAFECode and partnering members,
Intelligence Community Systems15 consider, evaluate, and standardize “quantum- establishes requirements and timelines for immediate shorter-term activities should be
builds on US Executive Order 1042816 safe” cryptosystems that are efficient, agile, implementing post-quantum cryptography taken by industry to prepare for the PQC
and safe against an adversarial quantum-based in National Security Systems (NSS). It calls transition.21 These include:
for Improving the Nation’s Cybersecurity
attack. Software migration to “post-quantum out timing expectations within 180 days for
highlights software supply chain security 1 Take an inventory of your products/codes
cryptography,” namely existing classical “modernization planning, use of unsupported
as critical to addressing future nation- that use cryptography.
algorithms and protocols robust to quantum encryption, approved mission unique protocols,
state attacks.
attack, will take years—if not a decade or more— quantum resistant protocols, and planning 2 Implement a crypto agility strategy
to achieve.18 for use of quantum resistant cryptography across your organization that includes
What are quantum computers? This means the pressure is on to manage the where necessary.” minimizing the code churn required when
cryptography changes.
Quantum computers are machines using the threat to today’s cryptography and everything Standardization is a long lead-time activity in
properties of quantum physics to store data and it protects. Adversaries can record encrypted the transition to quantum-safe cryptography. 3 Pilot the use of candidate quantum-safe
perform computations. This can be extremely data now and exploit it later once a quantum Standards bodies that work on standards using algorithms in your products or services
advantageous for certain tasks where they could computer is available. Waiting for quantum public key cryptography must begin to experiment that use cryptography.
vastly outperform even our best supercomputers. computing to arrive before addressing its with and adapt to post-quantum algorithms now.
Quantum computing is already opening new cryptographic implications will be too late. 4 Be prepared to use different public key
New post-quantum cryptography (PQC) algorithms for encryption, key exchange,
horizons for data encryption and processing.
As cryptography is used throughout the cyber algorithms—classical algorithms thought to be and signatures.
Studies predict quantum computing will become
ecosystem, this means our cryptography- robust to quantum attack—are now under review
a multi-billion dollar (USD) quantum industry as based security services could be compromised. through NIST’s Post-Quantum Standardization 5 Test your applications for the impact of very
early as 2030.17 In fact, quantum computing and large key sizes, ciphers, and signatures.
For example, this includes services for Project.20 This work will influence global efforts
quantum communication are poised to have
communications (TLS, IPSec), messaging within standards bodies. Although there will be Links to further information
a transformative effect across a multitude of
(email, web conferencing), identity and access some overlap with US government algorithm
industries, ranging from healthcare and energy Microsoft has demonstrated the underlying
management, web browsing, code signing, selections, differing national body/regulatory
to finance and security.
payment transaction and other services that are choices for compliant algorithms could present
physics required to create a new kind of
qubit | Microsoft Research
dependent upon cryptography for protection. international challenges. This fragmentation will in
turn complicate product and service engineering.

Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
106 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
Organizational leaders and policymakers can Unfortunately, many organizations delay,
Integrating business,
have a significant positive impact on security by defer, or apply these common practices only Security risk decisions are
security, and IT for
actively supporting security leaders and helping partially. This provides extensive opportunities
best made by business or
to build a bridge between integrated security for attackers to exploit. The need for security
greater resilience and the rest of the organization. When Microsoft normalization is captured in US NIST 800-40.22 mission owners who have
works with customers that have this alignment,
full visibility across all risks
we see them building a more resilient
Robust cyber resiliency depends on 2. Engage with security
organization and also improving their agility
and opportunities.
business leaders working with security
to adapt and innovate. Organizational leaders should actively participate
teams to implement security. In Microsoft’s
in and sponsor key security processes to ensure
experience, security leadership is a Organizational leadership can support security
prioritization of resources and preparedness for
challenging discipline that requires support leaders by focusing on three key areas:
security disasters. This includes engaging in:
from organizational leaders to most
Identify critical business assets.
effectively protect the organization. 1. Build security by design
Security leaders and teams need to know
Security is sometimes viewed as an obstacle or which assets are business-critical to focus
Security leaders navigate a spectrum of dynamic an afterthought in business processes, often security resources on what matters most. This is
challenges spanning topics related to risk, being considered in decisions only when it is too often a new exercise that includes asking and
technology, economics, organizational process, late to avoid a risk or fix cheaply and easily. answering new questions that have not been
business models, culture transformation, previously addressed.
geopolitical interests, espionage, and Organizational leaders and policymakers should
international sanctions compliance. Each of ensure that they: Cybersecurity business continuity and disaster
recovery exercises. Cyberattacks can become
these carries nuances to be understood and Include security early on new initiatives.
major events that disrupt or halt most or all
closely managed. New digital initiatives and cloud adoption should
business operations. Ensuring teams throughout
Security leaders are also tasked with thwarting prioritize security to ensure organizational risk the organization are prepared to handle these
both intelligent, well-funded, and highly does not increase with each new application situations will reduce the time to restore business
motivated human attackers, and low-skilled, or digital capability. Once security is reliably operations, limit damage to the organization,
yet effective, cybercriminals. Their teams must included, you can use those processes to and help sustain the trust and confidence of
defend complex technical estates often built modernize legacy systems to get both security customers, citizens, and constituents. This should
up incrementally over 30 or more years when and productivity benefits at the same time. be integrated within an existing business
security was a low or nonexistent priority. Normalize preventive maintenance for continuity and disaster recovery process.
Decisions made years ago can pose risks today security. Ensure basic security maintenance—
until we pay off the technical debt and address like applying security updates and patches and
the gaps in security. secure configurations—has full organizational
support allocated (including budgets, scheduled
downtime, acquisition requirements for vendor
product support).

Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
107 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
Integrating business,
Reduce risk by removing silos “Cyber resilience is on a sliding scale from
classic business continuity and disaster recovery
security, and IT for
starting with good data backup; progressing to
greater resilience Siloed approach recovery capabilities for processes, technology,
and their dependencies (including people and
Business
Uncertainty third parties); and moving to always on, self
Continued
healing services, resilience for critical roles, and
Trust gap
Security
failovers for critical third parties. The most resilient
3. Position security correctly Blame High
organizations promote integration between IT,
Increased threat risk business managers, and security professionals.
The way organizations structure security risk IT
vulnerability Great resilience includes designing for resilience
accountability often sets them up for poor
from the start, having safe change management,
security risk decision making. Risk decisions
and granular fault isolation. Cyber resilience is
are best made by business or mission owners
just one scenario in a good all-hazards planning
who have full visibility across all risks and
program. As cyber risks increase and the
opportunities, but organizations often (implicitly
intersection between cybersecurity and resilience
or explicitly) assign security risk accountability Organizational digital transformation
becomes more important, the connection of the
to subject matter experts in the security team
Chief Information Security Officer (CISO) to the
instead. This places an unhealthy burden on
enterprise resilience program grows stronger.
security teams while depriving business owners Integrated approach
Every year, more CISOs are taking ownership
of visibility and control over a key risk to their
for company-wide resilience.”
business. Organizations can correct this by: Informed decision
making Lisa Reshaur
Preparing business owners: Educate business
owners about security risk overall and how Less complexity General Manager, Risk Management, Microsoft
Business Security
these threats can and will affect their business. Lowered cost
Engaging security teams directly in this effort
Enhanced security
also increases the collaborative relationship with and productivity Links to further information
security and overall business agility.
From resilience to digital perseverance:
Assigning security risk to business owners: Lower How organizations are using digital
As business owners become informed enough threat risk technology to turn the corner in
to understand and accept security risk, the IT unprecedented times | Official Microsoft Blog
organization should explicitly shift accountability
How IT and security teams can work
for security risk to them while still holding
together to improve endpoint security |
security teams responsible for managing that risk
Microsoft Security
and providing informed expertise and guidance
to the owner.

Report The State of Nation State Devices and Cyber Influence Cyber Contributing
108 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience Teams
• Use extended detection and response
The cyber resilience
anti- -malware: Implement software to
Key
detect and automatically block attacks and
bell curve
provide insights to the security operations.
Monitoring insights from threat detection Enable multifactor
Resilience success factors every organization
systems is essential to being able to respond authentication
should adopt
to threats in a timely fashion.
As we have seen, many cyberattacks are Apply Zero Trust
• Keep up to date: Unpatched and out of date
successful simply because basic security hygiene principles
systems are a key reason many organizations
has not been followed. The minimum standards
fall victim to an attack. Ensure all systems
every organization should adopt are: are kept up to date including firmware, the Use modern
• Enable multifactor authentication (MFA): operating system and applications. anti--malware
To protect against compromised user
• Protect data: Knowing your important
passwords and helps to provide extra Keep up
data, where it is located and whether the
resilience for identities. to date
right systems are implemented is crucial to
• Apply Zero Trust principles: The cornerstone implementing the appropriate protection.
of any resilience plan limiting the impact on an Protect
organization. These principles are: data
98%
–– Explicitly verify—ensure users and devices
are in a good state before allowing access
to resources.
–– Use least privilege access—only allow the
privilege that is needed for access to a
resource and no more. Basic security hygiene
–– Assume breach—assume system defenses still protects against
have been breached and systems might
98% of attacks
be compromised. This means constantly
monitoring the environment for
possible attack.

Report The State of Nation State Devices and Cyber Influence CCyybbeerr Contributing
109 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations RReessiilliieennccee Teams
Endnotes
1 Endpoint Detection and Response (EDR) is an enterprise endpoint security platform designed 18 “The Long Road Ahead to Transition to Post-Quantum Cryptography,” https://cacm.acm.org/
to help enterprise networks prevent, detect, investigate, and respond to advanced threats. magazines/2022/1/257440-the-long-road-ahead-to-transition-to-post-quantum-cryptography/
Endpoint detection and response capabilities provide advanced attack detections that are near fulltext
real-time and actionable. Security analysts can prioritize alerts effectively, gain visibility into the 19 https://www.whitehouse.gov/briefing-room/presidential-actions/2022/01/19/memorandum-
full scope of a breach and take response actions to remediate threats. on-improving-the-cybersecurity-of-national-security-department-of-defense-and-intelligence-
2 An Endpoint Protection Platform (EPP) is a solution deployed on endpoint devices to prevent file- community-systems/
based malware, to detect and block malicious activity from trusted and untrusted applications, 20 https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-
and to provide the investigation and remediation capabilities needed to dynamically respond to standardization
security incidents and alerts.
21 https://safecode.org/blog/preparing-for-post-quantum-cryptography-roadmap-initial-guidance/
3 https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-getstarted
22 https://csrc.nist.gov/publications/detail/sp/800-40/rev-4/final
4 https://docs.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-number-
match
5 https://docs.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-additional-
context
6 Windows Security book: Commercial
7 New security features for Windows 11 will help protect hybrid work | Microsoft Security Blog
8 FIDO Alliance: Open Authentication Standards More Secure than Passwords
9 https://interpret.ml/
10 OWASP Top Ten | OWASP Foundation
11 https://blogs.microsoft.com/on-the-issues/2022/05/03/artificial-intelligence-department-of-
defense-cyber-missions/
12 https://www.kaspersky.com/blog/the-human-factor-in-it-security/
13 https://aka.ms/ZTatMSFT
14 https://csrc.nist.gov/publications/detail/nistir/8374/final
15 https://www.whitehouse.gov/briefing-room/presidential-actions/2022/01/19/memorandum-
on-improving-the-cybersecurity-of-national-security-department-of-defense-and-intelligence-
community-systems/
16 Executive Order 14028 Improving the Nation’s Cybersecurity
17 https://thequantumdaily.com/2020/02/18/the-quantum-computing-market-size-
superpositioned-for-growth

| Report  | The State of   | Nation State   | Devices and  | Cyber Influence | Cyber   | Contributing  |
| ------- | -------------- | -------------- | ------------ | --------------- | ------- | ------------- |
110 Microsoft Digital Defense Report 2022   Introduction  Cybercrime  Threats  Infrastructure  Operations  Resilience  Teams
Contributing
Teams

Report The State of Nation State Devices and Cyber Influence Cyber CCoonnttrriibbuuttiinngg
111 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience TTeeaammss
Azure Networking, Core: A cloud networking Cyber Defense Operations Center (CDOC): Digital Security & Resilience (DSR): An
Contributing Teams
team focused on the Microsoft WAN, data Microsoft’s cybersecurity and defense facility organization dedicated to enabling Microsoft
center networks, and the software defined is a fusion center that brings together security to build the most trusted devices and services,
The data and insights in this report were
networking infrastructure of Azure including professionals from across the company to protect while keeping our company safe, and both our
provided by a diverse group of security- the DDoS platform, the network edge platform, our corporate infrastructure and the cloud company and customer data protected.
focused professionals, working across many and network security products such as infrastructure to which customers have access.
Digital Security Unit (DSU): A team of
different Microsoft teams. Collectively, their Azure WAF, Azure Firewall, and Azure DDoS Incident responders sit alongside data scientists
cybersecurity attorneys and analysts who provide
goal is to protect Microsoft, its customers, Protection Standard. and security engineers from across Microsoft’s
legal, geopolitical, and technical expertise to
and the world at large from the threat of services, products, and devices groups to help
Cloud Security Research team: By securing protect Microsoft and its customers. DSU builds
cyberattacks. We are proud to share these the Microsoft cloud, building innovative protect, detect, and respond to threats 24x7. trust in Microsoft’s enterprise security defenses
insights in the spirit of transparency with a security features and products, and conducting Democracy Forward Initiative: A Microsoft against advanced cyber adversaries worldwide.
common goal of making the world a safer research, this team protects and empowers team working to preserve, protect, and advance
Digital Threat Analysis Center (DTAC): A
place for everyone. Microsoft customers to securely transform the fundamentals of democracy by promoting
team of experts who analyze and report on
their organizations. a healthy information ecosystem, safeguarding
nation state threats, including cyberattacks
open and secure democratic processes, and
AI for Good Research Lab: Harnessing the Customer Security and Trust (CST): A team and influence operations. The team combines
advocating for corporate civic responsibility.
power of data and AI to address many of the driving continuous improvement of customer information and cyber threat intelligence with
world’s challenges. The lab collaborates with security in Microsoft products and online Digital Crimes Unit (DCU): A team of attorneys, geopolitical analysis to provide insights to our
organizations outside Microsoft, applying AI to services. Working with engineering and security investigators, data scientists, engineers, analysts, customers and to Microsoft to inform effective
improve livelihoods and environments. Areas of teams across the company, CST ensures and business professionals dedicated to fighting response and protections.
focus include online safety (disinformation, compliance, enhances security, and provides cybercrime at a global scale using technology,
Enterprise and Security: A team focused on
cybersecurity, child safety), disaster response, more transparency to protect customers and forensics, civil actions, criminal referrals, and
providing a modern, secure, and manageable
sustainability, and AI for Health. promote global trust in Microsoft. both public and private partnerships.
platform for the intelligent cloud and
Azure Edge & Platform, Enterprise & OS Customer Success: Security teams in Customer Digital Diplomacy: An international team intelligent edge.
Security: Responsible for the core OS and Success work directly with customers to share of former diplomats, policymakers, and legal
Enterprise Mobility: A team that helps deliver
platform security across Windows, Azure, and best practices, lessons learned, and guidance experts working to advance a peaceful, stable,
the modern workplace and modern management
other Microsoft products. The team builds to accelerate security transformation and and secure cyberspace in the face of rising
to keep data secure, in the cloud and on-
industry-leading security and hardware solutions modernization. This team assembles and nation state conflict.
premises. Endpoint Manager includes the
into Microsoft platforms to drive down exploit, organizes best practices and lessons learned
services and tools Microsoft and customers use
identity, and malware compromise from chip from Microsoft’s journey—as well as our
to manage and monitor mobile devices, desktop
to cloud. Creators of Microsoft’s Secured- customers’—into reference strategies, reference
computers, virtual machines, embedded devices,
core platform across PC, Edge and Server, the architectures, reference plans, and more.
and servers.
Microsoft Pluton Security Processor, and more.

Report The State of Nation State Devices and Cyber Influence Cyber CCoonnttrriibbuuttiinngg
112 Microsoft Digital Defense Report 2022 Introduction Cybercrime Threats Infrastructure Operations Resilience TTeeaammss
Microsoft AI, Ethics and Effects in Engineering Microsoft Defender Threat Intelligence Microsoft Threat Intelligence Center (MSTIC):
Contributing Teams
and Research (AETHER): An advisory board (RiskIQ): A team that produces tactical A team focused on identifying, tracking, and
at Microsoft with the mission of ensuring new intelligence through analysis of Microsoft’s collecting intelligence related to the most
Continued
technologies are developed and fielded in a extensive external telemetry collection, charting sophisticated adversaries impacting Microsoft
Enterprise Risk Management: A team responsible manner. the threat landscape as it evolves to discover customers, including nation state threats,
working across business units to prioritize risk previously unknown threat infrastructure, and malware, and phishing.
Microsoft Bing Search and Distribution:
discussions with Microsoft’s senior leadership. adding context to threat actors and campaigns.
A team dedicated to providing a world-class One Engineering System (1ES): A team with
ERM connects multiple operational risk The team regularly publishes timely and
internet search engine, enabling users around a mission of delivering world class tools to help
teams, manages Microsoft’s enterprise risk distinctive research to deliver crucial tactical
the world to find trusted search results and Microsoft developers be as productive and
framework, and facilitates the company’s intelligence to defenders.
information quickly, including tracking topics secure as possible. The team leads the central
internal security assessment using the NIST
and trending stories that matter to them, while Microsoft Security Business Development strategy for securing Microsoft’s end-to-end
Cybersecurity Framework.
giving users control of their privacy. Team: A team that leads Microsoft’s software supply chain.
Global Cybersecurity Policy: A team working cybersecurity growth strategy, partnerships,
Microsoft Customer and Partner Solutions: Operational Threat Intelligence Center
with governments, NGOs, and industry and strategic investments.
Microsoft’s unified commercial go-to-market (OpTIC): The team responsible for managing
partners to promote cybersecurity public
organization responsible for field roles such Microsoft Security Response Center (MSRC): A and disseminating cyber threat intelligence that
policy that empowers customers to strengthen
as security and technical sales specialists team engaged with security researchers working supports the Microsoft Cyber Defense Operation
their security and resiliency as they adopt
and advisors. to protect Microsoft’s customers and partner Center’s (CDOC) mission to protect Microsoft
Microsoft technology.
ecosystem. An integral part of Microsoft’s Cyber and our customers.
Microsoft Defender Experts: Microsoft’s
Identity and Network Access (IDNA) Security: Defense Operations Center (CDOC), MSRC brings
largest global organization of product-focused
A team working to protect all Microsoft together security response experts to detect and
security researchers, applied scientists, and threat
customers from unauthorized access and fraud. respond to threats in real time.
intelligence analysts. Defender Experts delivers
IDNA Security is a cross-discipline team of
innovative detection and response capabilities in Microsoft Security Services for Incident
engineers, product managers, data scientists,
Microsoft 365 security products and Microsoft Response: A team of cybersecurity experts
and security investigators.
Defender Experts managed services. helping customers through the entire cyberattack
M365 Security: Organization that develops from investigation to successful containment and
Microsoft Defender for IoT: A team composed
security solutions including Microsoft Defender recovery related activities. Services are offered
of domain-expert researchers specializing in
for Endpoint (MDE), Microsoft Defender via two highly integrated teams, the Detection
reverse-engineering of IoT/OT malware, protocols
for Identity (MDI), and others, to secure and Response Team (DART) with a focus on the
and firmware. The team hunts for IoT/OT threats
enterprise customers. investigation and groundwork for recovery, and
to uncover malicious trends and campaigns.
the Compromise Recovery Security Practice
(CRSP), which focuses on the containment and
recovery aspects.

Illuminating the threat landscape
and empowering a digital defense.
Learn more: https://microsoft.com/mddr
Dive deeper: https://blogs.microsoft.com/on-the-issues/
Stay connected: @msftissues and @msftsecurity
© 2022 Microsoft. All rights reserved.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-13", "model": "gemini-3.5-flash-lite"} -->
