# Ransomware Report 2025

## Table of Contents
- [Introduction](#introduction)
- [Key insights of the report](#key-insights-of-the-report)
- [Overview of attack patterns and the impact on customers](#overview-of-attack-patterns-and-the-impact-on-customers)
- [Evolving extortion tactics](#evolving-extortion-tactics)
- [Inside the RaaS ecosystem](#inside-the-raas-ecosystem)
- [Putting the RaaS in hacktivism](#putting-the-raas-in-hacktivism)
- [Security spotlight: A malicious treat with TrickBot](#security-spotlight-a-malicious-treat-with-trickbot)
- [Industry trends](#industry-trends)
- [Security spotlight: Cryptominers](#security-spotlight-cryptominers)
- [The impact of ransomware attacks on operational continuity](#the-impact-of-ransomware-attacks-on-operational-continuity)
- [Security spotlight: Ransomware and the law](#security-spotlight-ransomware-and-the-law)
- [Building ransomware resilience around the world](#building-ransomware-resilience-around-the-world)
- [Mitigation](#mitigation)
- [Conclusion](#conclusion)
- [Methodology](#methodology)
- [Guest contributors](#guest-contributors)
- [Credits](#credits)

---

## Introduction

The ransomware landscape has grown even more complex and volatile in 2025. Groups like FunkSec and Black Basta have reportedly used generative artificial intelligence (GenAI) and large language models (LLMs) to create ransomware code and enhance their social engineering attacks, respectively. Although adversaries are using multiple extortion techniques — sometimes even quadruple extortion — double extortion remains the attackers’ favored method. Despite high-profile law enforcement takedowns, threat actors show strong resilience — regrouping, rebranding, or forming new groups to quickly fill any vacuum created by the dissolution of a dominant group.

### How attackers are harnessing AI and LLMs
Adversaries are rapidly integrating AI and LLMs to increase the scale, sophistication, and efficiency of their operations. Ransomware groups such as FunkSec use GenAI to generate malicious code, create new ransomware variants, and deploy chatbots to negotiate with victims. Attackers also employ AI to craft convincing phishing emails and conduct voice phishing (“vishing”) attacks that impersonate company personnel. Advanced persistent threat groups have also begun using GenAI on a limited scale. Forest Blizzard (aka Fancy Bear) and Emerald Sleet reportedly leveraged LLMs to mimic official documents in phishing campaigns and to conduct vulnerability research, respectively, and emerging tools like WormGPT, DarkGPT, and FraudGPT are helping cybercriminals increase both the scale and effectiveness of their attacks.

### Adding distributed denial of service to the extortion mix
Beyond traditional encryption, attackers are also deploying sophisticated multi-extortion methods that create compound pressure points. Simultaneous encryption, data theft, and distributed denial-of-service (DDoS) threats give attackers more leverage against organizations. To maximize profits, some ransomware groups auction off stolen “crown jewels” or confidential company data to the highest bidders on dark web marketplaces.

### The fading line between cybercrime and hacktivism
While the majority of ransomware groups primarily pursue financial extortion, traditional boundaries between profit-driven cybercrime and ideologically motivated hacktivism are dissolving in troublesome ways. Ransomware as a service (RaaS) relies on a wider criminal ecosystem that consists of developers, affiliates, the zero-day market, and initial access brokers who are key to orchestrating attacks. The broader criminal ecosystem has become a service industry, with criminal groups building their brands or specializing in functions like money laundering. RaaS groups with hacktivist motivations are using ransom payments to fund their campaigns to advance ideological or political objectives. Moreover, hacktivists such as Head Mare, Twelve, and NullBulge have adopted ransomware tactics to cause greater disruption in the countries they are targeting, which further complicates the threat landscape.

### Partners join the fight against ransomware
As organizations become more cyber resilient by putting a Zero Trust architecture and other security controls in place, they are better positioned to proactively mitigate ransomware. But they need more help, and it’s beginning to arrive. Public—private partners of defenders and law enforcement are sharing threat intelligence and best practices and making a difference. Since 2022, FBI-provided decryption keys have saved victims more than US$800 million in payments. Governments are also introducing legislation aimed at banning organizations from paying threat actors. These policies benefit organizations since paying the ransom does not ensure the return of their data. Finally, cyber insurance providers are incentivizing organizations to strengthen security programs and offering their negotiating skills to lower ransomware payments.

### Akamai’s thought leadership and research
Akamai security research is committed to shining a light on the cybercriminal ecosystem by analyzing the emerging techniques used by adversarial groups. In this State of the Internet (SOTI) report, we spotlight two key threats:

- TrickBot malware, which is leveraged by certain ransomware groups, including Ryuk, Conti, and Diavol
- Cryptominers, which our researchers have identified as one of the critical intersection points within the ransomware landscape because their goals and strategies are similar to those of ransomware groups

Additionally, our threat experts provide strategic, actionable insights that empower security leaders and defenders to fortify organizational resilience, deploy robust protection, and proactively counter today’s increasingly sophisticated ransomware threats.

---

## Key insights of the report

- Ransomware extortion tactics have been evolving. Quadruple extortion is the newest tactic, while double extortion is currently the most common tactic. And ransomware groups continue to seek additional ways to generate profit, such as by pressuring victims and weaponizing compliance.
- More than US$724 million in cryptocurrency was extorted from strains linked to the TrickBot malware family, which is used by ransomware groups. The Akamai Hunt Team recently observed this malware in connection with four malicious scheduled tasks on five customer assets.
- GenAI and LLMs increase the frequency and scale of ransomware attacks by enabling individuals with less technical expertise to launch sophisticated campaigns, as demonstrated by groups like FunkSec.
- The emergence of hybrid ransomware hacktivist groups that are leveraging RaaS platforms to amplify impact (e.g., CyberVolk, Stormous, KillSec, Dragon RaaS, and DragonForce) demonstrates a significant shift in the ransomware landscape in which political and ideological motives are becoming more intertwined with financial crime.
- The hacktivist groups Head Mare, Twelve, and NullBulge often use LockBit ransomware (built from leaked or publicly available builders) for political disruption. NullBulge specifically uses it to target online communities and platforms that are operating with AI and online gaming tools.
- Although cryptominers pose a unique danger, their goals and the strategies they employ are similar to those of ransomware groups. Notably, nearly 50% of the cryptomining attacks we analyzed targeted nonprofit and educational organizations, likely because they possess substantial computational resources and are less secure than other industries.

---

## Overview of attack patterns and the impact on customers

Akamai research has observed a concerning trend: Multiple ransomware groups are increasingly targeting the same organizations simultaneously, heightening the risks to those organizations. Additionally, our research revealed significant fluctuations, with noticeable peaks and valleys in the number of global customers targeted by ransomware during 2024 (Figure 1). These fluctuations may also be evidence of volatility within and among the major ransomware groups, which frequently dissolve into smaller operations or rebrand in an effort to evade law enforcement and remain undetected.

![Customer Count per Threat Group chart showing global ransomware targets from Jan 2024 to Dec 2024]

![Regional customer count charts for APAC and EMEA showing ransomware targets from Jan 2024 to Dec 2024]

In 2024, ransomware spiked by 37%, accounting for 44% of the data breaches globally and for 51% in Asia-Pacific (APAC), according to the Verizon 2025 Data Breach Investigations Report. In Europe, the Middle East, and Africa (EMEA), the proportion of enterprises that experienced a ransomware attack grew to 27% in 2024. And in Latin America (LATAM), 29% of enterprises reported an attack in 2024, with a growing wave targeting small and medium-sized businesses.

To mitigate these risks, companies should prioritize strengthening their cyber resilience. This includes implementing segmentation to contain the attack and prevent threat actors from moving laterally within the network to compromise sensitive data.

---

## Evolving extortion tactics

Ransomware extortion tactics have been evolving from single extortion (which is intrinsic to all traditional ransomware operations) to double extortion (e.g., the Maze ransomware group in 2019) to triple extortion (notably with the ALPHV/BlackCat in 2021) to quadruple extortion (e.g., CL0P in 2024; Figure 3).

- **Single extortion**: Infiltrating businesses with ransomware (encrypting data and demanding ransom for decryption)
- **Double extortion**: Adds the threat of exposing exfiltrated customer information if not paid
- **Triple extortion**: Adds using DDoS attacks to disrupt business operations as extra pressure to force the victim to pay the ransom
- **Quadruple extortion**: Adds the sending of messages to harass business partners, employees, customers, high-level executives, and media to inform them of the breach and pressure the primary victim

![Table of ransomware groups categorized by extortion tactics: Double, Triple, and Quadruple]

The three groups that have historically been among the most prominent ransomware groups — ALPHV/BlackCat, CL0P, and LockBit — have all conducted quadruple extortion. And in February 2025, CL0P claimed responsibility for 385 attacks in just a few weeks, setting a new record for the most attacks ever attributed to a single group in one month. CL0P remains the most stable group of the three, given last year’s shutdowns of ALPHV/BlackCat and LockBit. This is despite LockBit’s return, which later led to the fragmentation of the group, its code being widely reused by others, and, most recently, the group being hacked.

---

## Inside the RaaS ecosystem

RaaS has revolutionized ransomware operations, transforming them from highly specialized attacks into scalable, subscription-based services accessible to a broader range of cybercriminals. This pivotal shift eliminates technical barriers that previously impeded ransomware deployment, enabling cybercriminals with minimal technical expertise to execute sophisticated attacks.

### Key entities in the RaaS business model
The rapid growth and success of RaaS stems from its accessibility, operational efficiency, and organizational structure that mirror legitimate businesses.

- **Ransomware developers**: RaaS developers create, update, and maintain ransomware, then sell or lease it to affiliates.
- **Affiliates**: Affiliates carry out attacks on organizations, earning a large share of ransom payments.
- **Initial access brokers**: Initial access brokers breach systems and networks of potential targets, then sell this access to other cybercriminal groups, including ransomware gangs.

---

## Putting the RaaS in hacktivism

In the criminal RaaS business model, alliances are formed for a variety of reasons. Alliances with hacktivists — hackers with malicious intent to promote a political or social cause — allow RaaS providers to borrow/lean on hacktivist motives or political justifications to attract attention, bolster legitimacy, or obscure their profit motives.

### Hacktivist/ransomware hybrids
- **Stormous**: Began operating in mid-2021; targets U.S., Ukraine, India, France, Spain, Vietnam.
- **DragonForce**: Emerged in mid to late 2023; targets India, Israel, U.K., U.S., Saudi Arabia, Australia.
- **KillSec**: Began in October 2023; targets India, Bangladesh, Asia broadly, U.S.
- **CyberVolk**: Started using ransomware in June 2024; targets Spain, NATO-aligned countries.
- **Dragon RaaS**: Emerged in July 2024; targets U.S., Israel, U.K., France, Germany.

---

## Security spotlight: A malicious treat with TrickBot
*By Or Zuckerman*

Wizard Spider (aka TrickBot) is a financially motivated cybercrime group that targets critical infrastructure, including healthcare systems, and has ties to Russian intelligence services that provide a malicious tool known as TrickBot to its ransomware groups. Ransomware groups that are part of Wizard Spider and use TrickBot include Diavol and RaaS operators Ryuk and Conti.

The Akamai Hunt Team recently uncovered four malicious scheduled tasks linked to the TrickBot malware family all disguised under the name “WindowsUpdate” across five customer assets. These tasks were set up to run payloads located in the C:\ProgramData directory.

---

## Industry trends

- **Financial services**: Ransomware remains one of the most serious threats. Asia was a particular focus of ransomware attacks in 2024.
- **Commerce**: Retailers and ecommerce businesses are targeted via zero-day vulnerabilities in file transfer solutions.
- **Healthcare**: Targeted for valuable data; downtime jeopardizes patient care.
- **Public sector**: Lucrative targets for data; attacks lead to service disruptions and high recovery costs.
- **Manufacturing**: Top target in Q1 2025; vulnerable due to legacy systems and complex supply chains.
- **Education**: Facing unprecedented attacks with high ransom demands.

---

## Methodology
[Content omitted in source]

## Guest contributors
[Content omitted in source]

## Credits
[Content omitted in source]

---

ncidents include breaches

at PowerSchool (a provider of cloud-based educational software in North America) and

Chicago Public Schools, which exposed sensitive student data. As of writing, the hacker

pleaded guilty for launching the attacks against Chicago Public Schools.

Schools are vulnerable because of limited resources, weak security, and lack of cyber

awareness. Delayed incident reporting further increases risks, highlighting the need for

prompt and transparent communication. Successful ransomware attacks on educational

institutions often result in significant data loss, operational disruptions, educational delays —

and, in some cases, permanent closure.

Industry trends summary

Although all industries are at risk of a ransomware attack, the severity of the attacks largely

depends on an organization’s level of preparedness and its ability to withstand and recover

from such attacks. Organizations that lack robust cybersecurity measures or dedicated
security personnel often experience significant data loss, prolonged operational

disruptions, and, in extreme cases, may even be forced to cease operations entirely.

As industries embrace digital transformation, they inadvertently create additional

security gaps and expand their attack surfaces. This means there are more entry points

for cybercriminals to exploit, making comprehensive security strategies essential. A

particularly concerning trend involves attackers targeting third-party vendors and supply

chain partners to gain access to organizations that have better defenses. To address these

growing risks, organizations must implement advanced strategies like microsegmentation

to contain breaches and prevent lateral movement, which can ultimately reduce their

exposure to ransomware.

Akamai.com   |   29

Ransomware Report 2025  I  Volume 11, Issue 03Security spotlight

Cryptominers  by Maor Dahan

Cryptominers, like ransomware, primarily seek financial gain through anonymous

cryptocurrency transactions. Although ransomware operations typically involve complex

network intrusions and direct extortion of victims for immediate payouts, cryptominers

operate covertly, generating steady, low-risk income for cybercriminals.

Cryptominers and ransomware are distinct threats that stem from attackers’ financial

motives. Cryptominers primarily exploit organizations’ computing resources to generate

profit, whereas ransomware encrypts and/or exfiltrates sensitive data to extort ransom

payments. Both types of malware capitalize on cryptocurrency’s anonymity: Ransomware

groups use it for facilitating ransom payments, and cryptominers use it to directly profit

from mining operations.

Both types of attackers may use similar tactics, such as phishing campaigns and

exploitation of vulnerabilities, to gain initial access before deploying their final payloads.

However, detection strategies differ significantly between these threats. Malicious

cryptomining remains stealthy over long periods to maximize returns, while ransomware,

though initially covert, ultimately alerts the victims to demand payment after fulfilling its

objectives. In this security spotlight, we’ll take an in-depth look at cryptominers and the

risks they pose to organizations.

What are cryptominers?

Cryptominers, or cryptojackers, are a type of malware that exploits the victim’s resources

for profit by mining cryptocurrency. In contrast to the usual use of cryptocurrency by

attackers as a payment method, cryptominers use the fundamental base of the
cryptocurrency, which is the blockchain mining operation, to generate financial gain.

Cryptocurrency was originally designed as a borderless, decentralized way to transfer

money and detach from traditional banking systems. Since the first appearance of bitcoin,

many other cryptocoins and crypto-based tokens have been created. Every token is based

on a theme or set of features that distinguishes it from others.

As attackers seek to profit while ensuring their anonymity, cryptocurrencies are a

lucrative option — they allow threat actors to use their crypto funds with minimal risk of

identification by law enforcement. The most direct way to achieve financial gain without

identification is by mining privacy-oriented cryptocurrencies, which give the attackers

immediate profit without revealing themselves to the victim.

Akamai.com   |   30

Ransomware Report 2025  I  Volume 11, Issue 03Adversary motivation

Threat actors choose to employ cryptominers for two main reasons: profit and privacy.

Motivated by profit

With the exception of state-sponsored threat actors and hacktivists, most cybercriminals

are financially motivated. Cryptominers are a simple and direct way to monetize an

intrusion  without the extra step of translating the attacker’s hold on the network into

capital via ransomware extortion or by selling sensitive data. This makes cryptomining

malware an attractive money generator for threat actors.

Other considerations that attackers take into account include cryptocurrency value and

mining share rate. If the attacker generates 1 US cent per year (US$0.1), for instance, it

is not worth the risk of being arrested. Therefore, one of the attacker’s goals is to find a

balance between effort and profit, which lets us narrow down the list of potential coins

mined by attackers.

During our research, we identified an attacker who seems to be active since at least June

2018 and was able to generate an average revenue of 300 XMR every year. If we calculate

their revenue according to the current Monero value (1 XMR = US$150), we see that they

made approximately US$45,000. This is just slightly less than the average revenue of

a small business with no employees in the United States in 2024.

Motivated by privacy

Privacy is intrinsic to most cryptocurrencies. They use cryptographic algorithms

that preserve privacy and ownership through secret keys paired with corresponding

public keys, which serve as wallet addresses. By leveraging this inherent feature of

cryptocurrency, along with additional privacy algorithms designed to hide transaction

amounts, sender addresses, and receiver addresses, an attacker can almost completely

conceal their activities.

As we mentioned, attackers consider several trade-offs when shifting their botnets to mine

specific cryptocurrencies. One of these trade-offs concerns the attacker’s privacy vs. profit

— there could be more profitable coins that offer less privacy. Coin privacy is measured

through the anonymity it could provide in three aspects:

1.  Communicating with the network; there are coins that rely on privacy network

protocols such as Tor or I2P

2.  Protecting transaction information, such as wallet addresses and amounts,

to prevent tracing and hide account balances

3.  Enlisting the cryptocurrency in exchange platforms that support privacy

Akamai.com   |   31

Ransomware Report 2025  I  Volume 11, Issue 03For example, bitcoin lacks transaction privacy, making users vulnerable to monitoring

and increasing the risk of deanonymization. This limitation restricts the range of

cryptocurrencies that attackers can exploit. Consequently, adversaries remain

motivated only as long as profitable privacy-focused coins are available.

This motivation will likely decline if privacy coins become unprofitable or if the mining

process changes, such as shifting to proof of stake, thereby preventing attackers from

easily generating profits through resource-intensive methods.

A motivated attacker has to consider how to execute such a cryptominer campaign — and

understanding the fundamentals of the mining process is crucial for that consideration.

Cryptominers’ impact on the world

Cryptominers have impacted the world since 2013, when a video games company

allegedly exploited customers’ machines to mine bitcoin. More than 10 years later, the

threat has grown to an enormous scale and cryptominers are now a substantial piece of

worldwide cybercrime.

Many case studies of cryptominers have been published over the years: from the

WannaMine botnet in 2017 to the Migo campaign that targeted Redis to variants of

cloud-specific and browser-mining scripts in early 2024. In recent years, Akamai has

uncovered a few cryptomining botnets, such as Panchan and NoaBot.

Ransomware Report 2025  I  Volume 11, Issue 03

Akamai.com   |   32
Akamai.com   |   32

Ransomware Report 2025  I  Volume 11, Issue 03Attack volume

More attackers have shifted their attention to cryptominers over time. Figure 14 shows that

2023 saw a huge spike in global malicious cryptomining activity — and this trend continued in

2024. Despite the explosive growth, there have not been significant changes to cryptominers’

behavior. The typical cryptominer in 2024 acted very similarly to its predecessors from
Global Cryptojacking Volume
10 years ago; that is, highly noisy, nontargeted attacks that infect cloud resources and

domestic computers to mine privacy-oriented coins.

Global Cryptojacking Volume

Fig. 14: Volume of cryptominers attacks detected (Source: SonicWall)

Cryptominers’ industries and sectors distribution

Cryptominers affect a wide variety of industries and sectors (Figure 15).

2024 Attacks by Sector
2024 Attacks by Sector

Nonprofit/Education
44.9%

Fig. 15: The distribution of observed attacks across various sectors in 2024

Akamai.com   |   33

Ransomware Report 2025  I  Volume 11, Issue 03High Technology19.8%Video Media8.0%Manufacturing3.9%Gaming5.1%Commerce2.7%Public Sector10.5%Business Services4.9% Higher education institutions were among the most targeted sectors, presumably because

of their significant computational resources, which are often unattended.

Among large tech companies, cryptominers preferentially target industries like cloud and

hosting services. These targets provide a great opportunity to attackers, as they allow them

to access extensive computational resources while eliminating by-products in the victim’s

environment, such as substantial noise, heat, and electricity consumption that could

potentially lead to their detection.

This type of attack can be financially devastating for victims — in 2022, Sysdig suggested

that for every US$1 of cryptominer profit, the victim loses approximately US$53 (Figure 16).

Attacker

Victim

Fig. 16: Attacker profit compared with victim expenses

GenAI offers new attack surfaces for cryptominers

We predict the recent rise of GenAI will significantly affect the cryptominer landscape. As

AI computation is highly reliant on graphics processing units (GPUs), those components

are becoming more common in organizational networks and servers. Because many mining

algorithms are also designed for GPUs, the underlying computing infrastructure of the AI

industry is very attractive for cryptominer operators.

It’s probably just a matter of time before we witness a campaign that targets AI infrastructures

either directly through the model interaction or through the training process — or both.

Akamai.com   |   34

Ransomware Report 2025  I  Volume 11, Issue 03Cryptocurrency choice for cryptomining attacks

Attackers now have many cryptocurrency options beyond bitcoin, each with unique

features. When selecting a coin, cybercriminals consider several key factors:

 Ź Cross-platform compatibility: The coin must be mineable across various

architectures (x86, AMD64, ARM, etc.).

 Ź Hardware flexibility: Mining should be possible on standard devices;

it should not require specialized hardware like GPUs.

 Ź Privacy features: The cryptocurrency should support untraceable transactions

to help hide illegal activities.

 Ź Profitability: The coin should offer high, sustainable returns.

These criteria help attackers maximize their gains while minimizing detection risks.

Mitigating the risk of cryptominers

By leveraging Akamai’s security stack, organizations can mitigate the risk of cryptominer

infections across multiple layers of the attack surface.

Use Akamai Guardicore Segmentation to prevent lateral movement

Many cryptominers exhibit worm-like behavior — once they compromise a host, they

attempt to move laterally across the network to infect as many additional systems as

possible. This lateral movement is typically carried out by spraying weak credentials or

exploiting known (n-day) vulnerabilities across internal subnets.

By using Akamai Guardicore Segmentation to implement a strict microsegmentation

policy, defenders can significantly reduce this risk. By restricting unnecessary internal
communications, defenders can effectively block the majority of lateral movement

attempts and contain infections before they spread.

Use Akamai Secure Internet Access Enterprise to block mining-related connections

Many cryptomining configurations rely on direct communication with known mining

pools (that is, DNS addresses used by all nodes in the mining network during the different

mining operations).

Since cryptomining typically has no legitimate use case in most corporate environments,

identifying and blocking connections to these domains can be a highly effective way to

disrupt mining malware. Akamai Secure Internet Access Enterprise helps protect against

this threat by blocking access to known mining pool addresses by default.

Akamai.com   |   35

Ransomware Report 2025  I  Volume 11, Issue 03Use Akamai Hunt to proactively identify malicious cryptominers

Not all cryptomining malware can be reliably detected using static indicators of

compromise, such as file hashes or known DNS addresses. To identify previously

unknown or evasive samples, Akamai Hunt employs a proactive set of behavior-based

detection techniques.

These techniques focus on identifying anomalous behaviors that are commonly

associated with cryptominers, such as suspicious communication patterns, unusual

process execution, and persistence mechanisms. When such anomalies are detected,

the associated processes are further analyzed to confirm malicious activity.

Spotlight summary

The use of cryptocurrency in cybercrime operations is not limited to collecting

ransomware payments. Cryptominer malware exploits the fundamental aspect of

cryptocurrency — its mining process — as a primary means of generating profit.

Cryptomining is effective, simple, and very stealthy, and it provides a great opportunity

for less sophisticated threat actors to monetize their intrusions.

Ransomware Report 2025  I  Volume 11, Issue 03

Akamai.com   |   36
Akamai.com   |   36
Akamai.com   |   36

Ransomware Report 2025  I  Volume 11, Issue 03Ransomware Report 2025  I  Volume 11, Issue 03The impact of ransomware attacks
on operational continuity

Ransomware poses a significant threat to operations, extending far beyond immediate

ransom payments. The true financial and operational impacts include prolonged downtime,

productivity and revenue losses, and extensive postincident recovery and mitigation efforts.

These ramifications can persist for weeks or even months, depending on the organization’s

cybersecurity posture, incident response capabilities, and security controls.

The average reported downtime following a ransomware incident is 21 days, which can lead

to severe consequences such as reputational harm, diminished customer trust, permanent

closure — and, particularly in critical industries like healthcare and manufacturing, patient

safety risks and supply chain disruptions.

It’s also not just the attack on the initial target that can cause impacts; there can be a ripple

effect. Ransomware actors may target supply chains, including commercial software

deployed internally and external service providers, which are often considered to be “softer

targets” because of their  lower cybersecurity maturity. For example, in April 2025, attackers

gained access to customer data at two large banks by actively targeting external partners.

Potential costs beyond ransom demands

Ransom payments represent only a fraction of the total cost of a ransomware attack.

Cybersecurity Ventures predicts that by 2031, ransomware damages will reach US$276 billion

annually (or US$525,000 per minute), up from US$57 billion per year (or US$109,000 per

minute) in 2025. Additionally, long-term impacts include loss of customer loyalty and

damage to brand reputation. Organizations may also face regulatory sanctions and penalties

for breaches of data protection laws such as GDPR or HIPAA, further compounding financial

and reputational harm.

Ransomware often causes partial or complete shutdowns of business-critical functions,

effectively crippling operations. As attackers increasingly employ multi-extortion tactics to

encrypt and exfiltrate sensitive data, such as intellectual property and customer information,

the risk of permanent data loss remains high. Even if a ransom is paid, there is no guarantee

that companies will recover all their data.

Additionally, recovery costs from ransomware attacks in 2024 had a sharp increase — with

the average expense reaching US$2.73 million, up from the US$1.82 million reported in 2023.

This figure excludes any ransoms that attackers collected.

Akamai.com   |   37

Ransomware Report 2025  I  Volume 11, Issue 03Addressing the increasing frequency and
severity of ransomware attacks

A report from Cybersecurity Ventures projects that by 2031, consumers and businesses will

face a combined 43,200 ransomware attacks per day, or one every two seconds. To minimize

the impact of this threat, organizations must:

 Ź Develop a comprehensive business continuity plan to maintain mission-critical

functions during and after an attack, reducing downtime and financial loss

 Ź Perform regular data backups

 Ź

Implement network segmentation to limit the spread of ransomware within the

environment if an attack is successful

 Ź Ensure rapid response to significantly reduce the scope and duration of an attack

For more details on how to protect the network and critical assets, refer to our

Mitigation section.

Ransomware Report 2025  I  Volume 11, Issue 03

Akamai.com   |   38
Akamai.com   |   38

Ransomware Report 2025  I  Volume 11, Issue 03Security spotlight

Ransomware and the law  by James A. Casey

We often hear answers like “Because I can, Mr. Bond” when villains in the James Bond films

are asked why they commit crimes. This bit of dialog exemplifies the classic Bond villain’s

blend of menace and sophistication. This description applies equally to ransomware

criminals — they engage in ransomware attacks because they can, and because they are

effective. As ransomware has emerged as one of the most significant cybersecurity threats

facing organizations worldwide, governments have scrambled to address this growing

menace through various laws, regulations, programs, and awareness campaigns.

Current state of the law

Many of the legal efforts, however, are not specifically aimed at ransomware, but rather

are just an application of broader spectrum cybersecurity laws. Ransomware, despite its

prevalence and effectiveness, is just another cyberattack in the bad guys’ arsenals. The

same legal principles apply to ransomware incidents as to other cyberattacks, and much

of the same cyber hygiene and security best practices will help to mitigate the risk.

In the United States, for example, the FBI and the Cybersecurity and Infrastructure Security

Agency (CISA) offer cyber prevention and response frameworks; the Computer Fraud and

Abuse Act (CFAA) continues to serve as the foundation for prosecuting cyberattacks,

including ransomware; and various federal and state cyber incident reporting rules apply

to all cyber events.

The European Union has various cyber laws, including the robust legal framework created

by the NIS2 Directive which establishes strict reporting guidelines, significant penalties, and

executive accountability, and is broadly applied across industry sectors. To the extent that
a ransomware attack involves personal information, privacy laws in many jurisdictions will

apply to create additional requirements and reporting obligations.

In addition to legislative and regulatory activity, nations have participated in cooperative

arrangements to try and address the threat. All 50 members of the International Counter

Ransomware Initiative (ICRI), for example, endorsed a joint policy statement asserting

“relevant institutions under our national government authority should not pay ransomware

extortion demands.” And the Oxford Statement on Ransomware Operations establishes

principles for applying international law to ransomware. Although these efforts do

not create any binding obligations and are not applicable to the private sector, they

demonstrate the significant attention being paid to the ransomware threat at all levels.

Akamai.com   |   39

Ransomware Report 2025  I  Volume 11, Issue 03Ransom payment restrictions

Ransomware does raise one unique issue that specific legal efforts attempt to address

— extortion. A successful ransomware attack necessarily raises the question, “Should

we pay the ransom?” The answer to that question will depend on many different factors,

including the impact to the business; the size of the ransom and the nature of the

extortion (i.e., single, double, triple, or even quadruple extortion); the identity, if known,

of the attacker; and the likelihood that paying will actually result in release of the data

or a standing down on other threats.

While these factors may motivate the business to pay, the position of most governments

is that victims should not pay. Outright legal bans are rare and mostly limited to

government/public sector entities and critical industry sectors in a few countries.

Virtually all countries’ governments, however, recommend against payment. Reasons for

this position are obvious — if ransoms are not paid, then the effectiveness of the attack

vector is reduced and potentially becomes less attractive to hacker groups. In addition,

payment of ransoms potentially funds other criminal activities, both financial and

ideological, increasing the risk to everyone. Finally, there is no guarantee that paying a

given ransom or related extortion demand will result in the release of data or termination

of the related threats (data disclosure/sale, DDoS attacks, customer notifications).

In fact, the number of organizations that refused to respond to ransom demands

increased from 50% in 2022 to 64% in 2024. Consequently, ransom demands have

become significantly lower, which may also be due in part to government intervention;

that is, the success of takedowns and seizures of infrastructure by law enforcement.

The 3 categories of legal efforts to discourage ransom payments

The legal means employed by governments to discourage payments fall into three basic
categories. The first, and most common category, is legal restriction on payments to

sanctioned or restricted entities and nations, as well as more general restriction on

payments to criminal enterprises. The United States and other allied regimes make

it illegal to pay any ransomware actors in comprehensively sanctioned countries (e.g.,

North Korea, Iran, Syria, and Cuba) or who are on applicable entity lists such as the U.S.

Office of Foreign Assets Control list of Specially Designated Nationals. Indeed, nearly

every country with sanctions laws or anti–money laundering statutes makes it illegal

to pay ransoms to sanctioned entities or criminal organizations. This is not unique, of

course, to ransomware — these laws apply to any transaction with sanctioned parties,

including terrorist groups, organized criminals, and state-sanctioned cyber actors.

Akamai.com   |   40

Ransomware Report 2025  I  Volume 11, Issue 03The second category of legal efforts focuses on reporting obligations. Cyber incident

reporting is ubiquitous across jurisdictions globally and would generally apply to ransomware

attacks. More specific obligations related to ransomware payments, however, are starting to

be enacted.  Effective May 30, 2025, the Australian Cyber Security Act, for example, introduced

mandatory reporting for ransomware payments. The United Kingdom is considering mandatory

reporting for payments by public sector entities and critical infrastructure. And in the United

States, the CIRCIA will require covered entities to report ransomware payments within 24 hours

(rules pending finalization). We can expect to see more of these kinds of ransomware specific

requirements in the future.

The third category is specific ban legislation. The proposed U.K. cyber security act would

potentially ban payments by public sector and critical infrastructure entities. We can expect

to see other more comprehensive bans or, at least, sectoral bans for important industries,

including financial, healthcare, and critical infrastructure sectors.

Looking ahead

Despite regional differences, there are a number of common elements that emerge in

ransomware regulations and cyber best practices.

 Ź

Incident reporting: Most jurisdictions require prompt reporting of significant

cyber incidents, including ransomware.

 Ź Risk management: Governments continue to focus on requirements to ensure

that organizations implement appropriate cybersecurity measures.

 Ź Supply chain security: There is an increasing focus on securing third-party

relationships and the supply chain overall.

 Ź Executive accountability: We are seeing a growing trend of holding management

responsible for cybersecurity.

Ransomware-specific regulations, guidelines, and requirements likely will continue to

evolve as threats become more sophisticated.

 Ź Emerging ransomware tactics using artificial intelligence will drive regulatory updates.

 Ź New legislation and legal enforcement efforts will focus on RaaS models.

 Ź

 Ź

Increased penalties and victim support mechanisms are being considered globally.

International cooperation will continue to combat cross-border threats.

As ransomware continues to pose a significant threat to organizations worldwide, staying

informed about these evolving international regulations and enforcement efforts will be

essential for maintaining compliance and enhancing cybersecurity posture.

Akamai.com   |   41

Ransomware Report 2025  I  Volume 11, Issue 03Building ransomware resilience around the world

Cyber insurance and multilayered security are interlocking building blocks for cyber resilience.

This is particularly true in the case of a ransomware attack in which the goal is encryption of as much

of the network as possible. Once this happens, the financial implications of an attack — downtime,

remediation, and potential legal fees and regulatory fines — may include paying a ransom.

Since 2022, the FBI’s IC3 has offered up thousands of decryption keys to victims of ransomware,

helping them to avoid more than US$800 million in payments. However, decryption keys aren’t

always available, so organizations need their own strategies to build resilience.

Navigating payment and cyber insurance decisions

Before an incident, organizations should have ransomware payment policies in place. Paying a

ransom is no guarantee that you will recover everything, but you may be able to recover the majority

of the systems that were impacted.

Organizations also need to support cryptocurrency payments. Engaging with organized criminals

who have the will and the means to put an organization out of business is a high-pressure situation,

so organizations should establish a relationship with a third party who specializes in negotiating with

cybercriminals. Seasoned negotiators aim to minimize the financial damage and help the company

resume operations, but victims should still expect to pay 50% to 80% of the original demand.

S&P Global Ratings has projected that annual cyber insurance premiums will reach approximately

US$23 billion by the end of 2026, up from an estimated US$14 billion at the close of 2023, with an

increase of 15% to 20% per year. Currently, North America accounts for approximately 51% of gross

premiums written on cyber insurance, EMEA about 38%, APAC 9%, and LATAM 3%. The fastest

growth rates are anticipated in APAC and LATAM, where cyber insurance markets are smaller

and less mature than in the United States and Europe.

In 2024, insurance claims were higher for ransomware attacks than for other types of incidents,

and made up about 21% of claims — although the average claim size and frequency have been

declining over the last two years. Approximately 44% of policyholders who fell victim to ransomware

decided to pay ransom “when deemed reasonable and necessary,” with the insurer negotiating

ransomware payments down by an average of 60% in these cases.

The most common ransomware group identified in ransomware insurance cases was Akira,

accounting for 13.4% of events, followed by Play (6.2%), Medusa (5.7%), and RansomHub (4.6%).

Black Basta had the highest average ransom demand at US$4 million but accounted for only

3% of claims.

Akamai.com   |   42

Ransomware Report 2025  I  Volume 11, Issue 03Trustworthiness is not a two-way street

An interesting dynamic is that, in some cases, cyber insurance incentivizes criminals because

criminal groups can demand the amount that insurance will cover for the key to decrypt the

data. On the other hand, the involvement of insurance company negotiators, or negotiators

they sanction, likely increases the probability that the encryption keys work, and complete

recovery is more assured.

Although this is a business transaction and cybercriminals don’t want to bite the hand that

feeds them, they also don’t play by the rules. Trustworthiness is not a two-way street. Despite

having their demands met, cybercriminals may not delete stolen data, as in the case of

LockBit. And when data is encrypted, 35% of companies either don’t receive the decryption
keys they paid for or the keys don’t work. Even with working keys, the recovery process is

painstaking and requires expertise. Plus, there’s still the risk of being targeted again by the

same or affiliated threat actors.

Organizations that have decided not to pay often fall back on their business continuity/

disaster recovery crisis management plan. This approach can take days to weeks, depending

on what kinds of investments have been made to facilitate a recovery and how often the

plans are tested and updated.

Driving stronger regional security programs

The increase in the number of ransomware attacks, the emerging sophistication of AI-driven

attacks, and growing legislation have all combined to force cyber insurance companies to

raise rates and increase auditing of the company’s cybersecurity capabilities. This has driven

a compliance mindset to ensure that companies can get the best rates, which can result in

loss of coverage if the insurance plan was based on security control that was not

implemented and allowed the ransomware to execute.

Exclusions and limitations can also result in loss of coverage. If the company is attacked by
hacktivists that are supporting a geoconflict, the attack could be considered a nation-state

attack and not covered under an act-of-war exception. Finally, companies need to ensure

that they understand the insurance agreement; in some cases, any actions taken before the

insurance company is notified will not be covered.

While many companies depend on insurance to mitigate the risk of major cyber events,

including covering the cost of decryption keys, no companies rely on it to the exclusion of

security programs. In fact, many insurance companies only cover the company if they have

deployed a baseline set of controls, with the cost of insurance decreasing as the company

can demonstrate more security controls. This effectively incentivizes companies to

strengthen security programs.

Akamai.com   |   43

Ransomware Report 2025  I  Volume 11, Issue 03To this end, organizations around the world are building resilience to ransomware attacks

by implementing Zero Trust solutions to control access and by using microsegmentation for

detailed visibility and controls to detect, prevent, and contain lateral movement. Regional

use cases include:

Zero Trust enforcement
is simplified in APAC

Rapid time to policy thwarts
an attack in LATAM

Microsegmentation provides
resiliency in EMEA

Smart policies outsmart
ransomware in North America

Zero Trust enforcement is simplified in APAC

A think tank and consulting services provider needed an easier way to deploy and manage

Zero Trust access control mechanisms to enhance security for its own network and its critical

infrastructure clients. As threat actors increasingly adopt GenAI to lower the barriers to entry,

greater visibility into and control over devices lent to employees or outsourced companies

would help to protect against data leakage and the spread of malware across the network.

Software-based microsegmentation provided network visualization and granular access

control to enforce Zero Trust principles for employees of the consulting services provider

and for its third-party associates. A proof of concept validated that the firm can stop

unwanted behavior, such as lateral movement that ransomware relies on, and reduce the

internal attack surface.

Microsegmentation provides resiliency in EMEA

An international brand needed to enhance its cybersecurity posture to guard against internal

threats. The few network firewalls in place were not able to prevent lateral movement across

the network and provide visibility into communication paths and potential security risks.

Deploying privileged access and granular segmentation helped them achieve Zero Trust

by restricting unsanctioned remote access and more effectively defining user-based

segmentation. To test resiliency, they deployed a ransomware breach test and were able to

identify and isolate the rogue machine in record time to prevent the breach from spreading.

Rapid time to policy thwarts an attack in LATAM

Shortly after transitioning to a work-from-home model, a successful ransomware attack

hit a critical database at a large bank. The security and IT teams needed to act fast to limit

the loss of sensitive financial data. They had to determine and secure the initial attack

vector and prevent ransomware from spreading laterally to backup servers and the

production environment.

Akamai.com   |   44

Ransomware Report 2025  I  Volume 11, Issue 03Software-based segmentation had already been deployed in other parts of the bank. So, the

teams were able to move quickly. In only three days, they were able to gain the process-level

visibility necessary to identify the attack vector and put enforceable policies in place. The

teams blocked ransomware from propagating further and improved remote access security

moving forward.

Smart policies outsmart ransomware in North America

A healthcare company faced growing ransomware threats and needed visibility far beyond

traditional firewalls to isolate and eliminate threats faster and maintain application availability

even during security incidents.

Microsegmentation made it possible to better ringfence apps and implement ransomware

prevention policies quickly while providing cost savings over other approaches. The

company’s IT team neutralized 4,000 cyberattacks on day one and gained unexpected

benefits, including faster network troubleshooting, incident investigation, and policy

creation and enforcement.

Ransomware Report 2025  I  Volume 11, Issue 03

Akamai.com   |   45
Akamai.com   |   45
Akamai.com   |   45

Ransomware Report 2025  I  Volume 11, Issue 03Ransomware Report 2025  I  Volume 11, Issue 03Mitigation

A robust defense against ransomware involves a multilayered approach, a strong commitment

to safeguarding data at the edge, and the use of segmentation to stop attacks from spreading

laterally so that threat actors do not reach internal resources. Also, extensive visibility is

essential for identifying threats. Advanced, up-to-date technologies may assist with these

needs and are also vital for defending against the increasingly sophisticated AI-powered tools

employed by cybercriminals. Recommended mitigation strategies to help protect

organizations against ransomware attacks, include:

 Ź

Implement a Zero Trust architecture that includes segmentation of critical assets and

a secure application gateway with cloud-based Zero Trust Network Access to secure

north-south and east-west communications. Strict access controls limit threats that

bypass edge defenses (which aligns with NIST Zero Trust Architecture), reduce the

lateral movement of ransomware within the enterprise, help detect and prevent data

exfiltration, and can greatly decrease ransomware response time for organizations

following best practices.

 Ź Counter AI-enhanced attacks, and match the speed and adaptability of AI-driven

attackers, by deploying AI-powered threat detection that enables real-time automated

responses and accelerated incident responses to new and evolving ransomware tactics.

 Ź Provide comprehensive edge protection that includes a defense against JavaScript,

web application, and API attacks, addresses the increasing threat of zero-day and

day-one vulnerabilities, and ensures tight security for all public-facing systems.

 Ź Achieve awareness across multiple environments with accelerated threat detection

that minimizes dwell time; adopt capabilities that provide rapid visibility and mitigation;

shift from pure prevention to strategies that detect insider threats and threats that have

bypassed defenses; and consider partnering with security enhancement providers or

threat hunting teams to strengthen internal capabilities.

 Ź Use the MITRE ATT&CK framework to map security controls to attacker tactics

and to identify where known threat actors (e.g., DragonForce, CL0P) can be defeated.

The framework can also assist in visualizing how to deploy resources for protection.

 Ź Combat social engineering and deepfake threats by establishing strong verification

protocols — such as phish-proof multi-factor authentication and other multistep

approval processes for sensitive transactions or access requests — to prevent single

points of failure. Educate staff on deepfake risks.

Akamai.com   |   46

Ransomware Report 2025  I  Volume 11, Issue 03 Ź Safeguard outbound traffic from connecting to infected websites by using solutions

with URL inspection to detect and block phishing attempts and by employing endpoint

detection that provides alerts on malicious activity from phishing emails or payloads.

 Ź

Incorporate compliance by design by ensuring that security controls and data

protection measures are integrated throughout the lifecycle of products and services,

including for north-south and east-west traffic.

 Ź Boost resilience and proper risk management by having comprehensive business

continuity and disaster recovery plans and cyber insurance to provide financial support

for managing losses, recovery costs, and operational stability during and after a

ransomware attack.

 Ź Strengthen and test backup defenses continuously and keep them physically or

logically separated from the main network to prevent alteration or deletion.

 Ź Manage vulnerabilities and catch them before attackers do by scanning and using tools

and processes that prioritize systems exposed to the internet or that contain sensitive

data. Focus on fixing the most critical issues quickly instead of everything at once.

Conclusion

The ransomware criminal economy remains dynamic and rapidly changing, with a

confluence of factors accelerating this pace, including hacktivism, widespread

cryptocurrency adoption, the RaaS business model, GenAI and LLMs, expanding

compliance requirements and legislation, and law enforcement actions. As these

threats proliferate, organizations must redefine cyber resilience and implement

practical frameworks to achieve comprehensive protection.

In the past, resilience simply meant maintaining data backups. Today, many organizations

may feel compelled to pay a ransom to avoid facing the ramifications of successful attacks,

even though the governments of most countries encourage them not to do so.

Ultimately, adopting an “assume compromise” mindset can aid defenders to be on the

lookout for indicators of compromise, and to respond before an attack attempt turns into a

successful intrusion. By deploying purple teams that blend offensive and defensive tactics,

defenders can more effectively counter sophisticated ransomware threats. This approach

not only improves incident detection and response, but also strengthens overall resilience

against persistent, adaptive adversaries.

Akamai.com   |   47

Ransomware Report 2025  I  Volume 11, Issue 03Methodology

The Akamai ransomware data in this report was collected from our Secure Internet Access

Enterprise customers, who provide us with data from billions of events monthly. We actively

monitor a range of activities, including indicators of compromise, TTPs, and weaponization

efforts from more than 100 ransomware groups.

This report focused on the events reported by customers and the detections made within

their environments. In this context, we classify an “event” as any communication attempt to

an IP or domain associated with a threat, regardless of its outcome. Our detection mechanisms

categorize each event based on confidence and severity levels, which aids in assessing the

certainty of an activity’s malicious intent and its potential impact.

The data in this report includes the 17-month period from January 1, 2024, through May 31, 2025.

(Note: We experienced a data outage in April 2025 resulting in missing data during this month.)

Ransomware Report 2025  I  Volume 11, Issue 03

Akamai.com   |   48
Akamai.com   |   48
Akamai.com   |   48

Ransomware Report 2025  I  Volume 11, Issue 03Ransomware Report 2025  I  Volume 11, Issue 03Guest contributors

Or Zuckerman
Senior Security Researcher Lead, Akamai

James A. Casey
Vice President, Chief Privacy Officer, Akamai

Or Zuckerman is Senior Security Researcher Lead at

James A. Casey is Vice President and Chief Privacy Officer

Akamai, working in various security fields, including

at Akamai and heads the Akamai Global Data Protection team.

incident response, forensic research, and detection

Jim has served as in-house counsel for technology companies

method development.

Maor Dahan
Senior Security Researcher, Akamai

Maor Dahan is a Senior Security Researcher at Akamai with

more than a decade of experience in the cybersecurity

industry. Maor specializes in operating system internals,

vulnerability research, and malware analysis, and designed

and developed advanced detection and prevention

mechanisms for innovative security products like EDR,

EPP, and virtualized-based security.

for the past 20+ years and has significant experience

supporting new technology and product initiatives in the

internet, cybersecurity, information services and analytics,

and telecommunications industries. Jim provides legal counsel

in a variety of areas, including technology law and regulation,

public policy, privacy and artificial intelligence governance,

import/export and trade compliance, and cybersecurity.

Prior to moving in-house, Jim’s law firm experience focused

on supporting of technology regulation and initiatives in the

data, telecommunications, and internet industries, both

domestically and internationally, as well as supporting

technology and telecommunications projects with native

peoples in the United States and around the world.

Akamai.com   |   49

Ransomware Report 2025  I  Volume 11, Issue 03
Credits

Research director

Kimberly Gomez

Editorial and writing

Charlotte Pelliccia

Badette Tribbey

Lance Rhodes

Maria Vlasak

Review and subject matter contribution

Tanya Belousov

Reuben Koh

James Casey

Maor Dahan

Ori David

Richard Meeus

Steve Winterfeld

Or Zuckerman

Data analysis

State of the Internet/Security

Read back issues and watch for upcoming

releases of Akamai’s acclaimed State of the

Internet/Security reports. akamai.com/soti

Akamai threat research

Stay updated with the latest threat intelligence

analyses, security reports, and cybersecurity

research. akamai.com/security-research

Access data from this report

View high-quality versions of the graphs

and charts referenced in this report. These

images are free to use and reference,

provided that Akamai is duly credited as

a source and the Akamai logo is retained.

akamai.com/sotidata

Moshe Cohen

Chelsea Tuttle

Akamai security research

Promotional materials

Barney Beal

Ashley Linares

Marketing and publishing

Georgina Morales Hampe

Emily Spinks

Read the Akamai security research blog

for a rapid response perspective on today’s

most important research. akamai.com/

blog/security-research

Akamai Security protects the applications that drive your business at every point of interaction, without compromising performance or
customer experience. By leveraging the scale of our global platform and its visibility to threats, we partner with you to prevent, detect, and
mitigate threats, so you can build brand trust and deliver on your vision. Learn more about Akamai’s cloud computing, security, and content
delivery solutions at akamai.com and akamai.com/blog, or follow Akamai Technologies on X, formerly known as Twitter, and LinkedIn.
Published 07/25.

Ransomware Report 2025  I  Volume 11, Issue 03

Akamai.com   |   50