Microsoft 
Digital Defense Report OCTOBER 2021

 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

CHAPTER 1 
Introduction

3 
5 

Introduction
Our 2021 focus areas

CHAPTER 2 
The state of cybercrime

Introduction 
8 
The cybercrime economy and services
8 
Ransomware and extortion 
10 
20 Phishing and other malicious email 
34 Malware
38 Malicious domains 
42 Adversarial machine learning

CHAPTER 3 
Nation state threats

Introduction 
Tracking nation state threats 

48 
49 
52 What we’re seeing 
57 Analysis of nation state activity this year 
69 Private sector offensive actors 
69 Comprehensive protections required

CHAPTER 4 
Supply chain, IoT, 
and OT security

Introduction 

71 
72 Challenges in managing risk associated with 

the supplier ecosystem 

73 How Microsoft thinks about supply chain 
IoT and OT threat landscape 
76 
The 7 properties of highly secured devices 
81 
82 Applying a Zero Trust approach to IoT solutions 
IoT at the intersection of cybersecurity and 
83 
sustainability 
IoT security policy considerations

84 

CHAPTER 5 
Hybrid workforce security

CHAPTER 6 
Disinformation

Introduction 

110 
111 Disinformation as an emerging threat 
113 Mitigation through media literacy 
114 Disinformation as an enterprise disruptor 
117 Campaign security and election integrity

CHAPTER 7 
Actionable insights

Introduction 

122 
123 Summary of report learnings 
128 Conclusion

Contributing teams at Microsoft

Identities 

Introduction 

89 
91 A Zero Trust approach for securing hybrid work 
93 
98 Devices/Endpoints
99 Applications
100 Network
104 
105 Data
106 People

Infrastructure

2

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Our 2021 focus areas

Introduction 

TOM BURT, CORPORATE VICE PRESIDENT, CUSTOMER SECURITY \& TRUST

Over the past year the world has borne witness to a burgeoning cybercrime economy and the rapid rise 
of cybercrime services. We have watched this global market grow in both complexity and fervency. We’ve 
seen the cyberattack landscape becoming increasingly sophisticated as cybercriminals continue—and even 
escalate—their activity in times of crisis. New levels of supply chain and ransomware attacks were a powerful 
reminder that we must all work together, and in new ways, to protect the cybersecurity of the planet.

We see transparency and information sharing 

learnings that companies, governments, and 

By continually sharing insights we and others in the 

as essential to the protection of the ecosystem. 

consumers can use to further secure individuals and 

industry derive from the work we do, we hope to 

Knowledge brings power, and to that end, security 

environments.

empower everyone to defend the online ecosystem 

professionals need diverse and timely insights into 

more effectively.

the threats they are defending against.

The Microsoft Digital Defense Report draws on 

insights, data, and signals from across Microsoft, 

Microsoft has made significant and ongoing 

Microsoft serves billions of customers globally, 

including the cloud, endpoints, and the intelligent 

investments to increase and improve the knowledge 

allowing us to aggregate security data from a broad 

edge.1 Thousands of Microsoft security experts 

we derive from our threat signals. These investments 

and diverse spectrum of companies, organizations, 

across 77 countries interpret and contribute to the 

deliver the highly synthesized and integrated 

and consumers. Informed by over 24 trillion 

insights gained from our advanced engineering 

insights that we share here. Our goal in aggregating 

security signals per day, our unique position helps 

and threat signals. Our security experts include 

these learnings is to help organizations understand 

us generate a high\-fidelity picture of the current 

analysts, researchers, responders, engineers, and 

the ways in which cybercriminals are continually 

state of cybersecurity, including indicators that help 

data scientists. We also share lessons learned from 

shifting their modes of attack—and determine the 

us predict what attackers will do next. Our goal in 

customers transitioning to a hybrid workforce and 

best ways to combat those attacks. We write and 

creating the Microsoft Digital Defense Report is to 

frontline stories from our incident responders. Of 

share this report in the spirit of empowering the 

bring together integrated data and insights from 

course, there is malign activity we do not see, some 

global community to benefit from the insights, 

more teams, across more areas of Microsoft than 

of which is reported on by others in the industry. 

observations, and transparency generated by our 

ever before. We will share what we’re seeing to help 

While the defender community at Microsoft works 

unique mission and vantage point.

the global community strengthen the defense of the 

hard to identify threats and keep our customers 

digital ecosystem, and we will include actionable 

informed, the bad actors are skilled and relentless. 

THE MICROSOFT 

DIGITAL DEFENSE 

REPORT DRAWS ON 

INSIGHTS, DATA, 

AND SIGNALS 

FROM ACROSS 

MICROSOFT, 

INCLUDING 

THE CLOUD, 

ENDPOINTS, AND 

THE INTELLIGENT 

EDGE.

1 These signals are collected with customer privacy in mind. The data we collect depends on the context of your interactions with Microsoft and the choices you make, including your privacy settings and the products and features you use.

Microsoft Digital Defense Report \| October 2021

3
3

Microsoft Digital Defense Report \| October 2021 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Our 2021 focus areas

Microsoft security signals
Volume and diversity of signals processed by Microsoft

4

Microsoft Digital Defense Report \| October 2021 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Our 2021 focus areas

 Our 2021 focus areas

The state of cybercrime

Nation state threats

In this chapter, we discuss new developments in 

This chapter provides an update on what we’re 

the cybercrime economy and the growing market 

seeing in nation state adversarial activity, including 

for cybercrime services. We provide updates and 

reports on seven activity groups we have not 

analysis of what we are seeing in ransomware and 

previously mentioned publicly. We provide an 

extortion, phishing and other malicious email, 

analysis of the evolving threats in this watershed 

malware, and the use of domains by cybercriminals, 

year with an increased focus on on\-premises servers 

presenting recommendations for mitigating risk 

and the exposure of widespread supply chain 

in each area. Finally, we share what we’re seeing in 

vulnerabilities. We conclude with a discussion about 

adversarial machine learning and what we are doing 

private sector offensive actors and our guidance for 

to stay ahead of cybercriminals in this area.

comprehensive protections.

Supply chain, IoT, and OT 
security

The highly publicized events of the last year have 

made clear that securing and managing risks 

associated with supplier ecosystems is critically 

important. This chapter covers some current 

challenges in doing so in the supplier ecosystem 

and presents how Microsoft thinks about end\-to\-

end supply chain security in nine investment areas. 

Then we turn our discussion to what we’re seeing 

in the Internet of Things (IoT) and operational 

technology (OT) threat landscape, with guidance on 

the properties of highly secured devices. We include 

specialized use cases of IoT and present some new 

research informing IoT policy considerations.

2021 brought powerful reminders that to protect 

the future we must understand the threats of the 

present. This requires that we continually share data 

and insights in new ways. Certain types of attacks 

have escalated as cybercriminals change tactics, 

leveraging current events to take advantage of 

vulnerable targets and advance their activity through 

new channels. Change brings opportunity—for both 

attackers and defenders—and this report will focus 

on the threats that are most novel and relevant to 

the community as we look to the months ahead.

Looking at the threat landscape, along with data 

and signals from cross\-company teams, five top\-

level areas emerged as most critical to bring into the 

sharpest focus in this report: the state of cybercrime; 

nation state threats; supplier ecosystems, Internet 

of Things (IoT), and operational technology (OT) 

security; the hybrid workforce; and disinformation. 

To provide the greatest benefit, we also extract our 

recommendations and actionable learnings, and 

present them throughout the report and in our 

concluding chapter.

5

Microsoft Digital Defense Report \| October 2021 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Our 2021 focus areas

Hybrid workforce security

Disinformation

Actionable insights

This chapter is about our greatest asset, our people. 

This chapter addresses the unprecedented 

We open this year’s concluding chapter with a 

As we have moved to a hybrid workforce over 

disinformation campaigns and related cyber 

discussion of five paradigm shifts that will center the 

the past year, we’ve seen developments in the 

operations by state and non\-state actors, 

evolution of work around the inclusivity of people 

threat landscape which point to the importance 

impacting public awareness and knowledge as 

and data. The chapter concludes with a distilled look 

of adopting a Zero Trust approach. We include 

well as enterprise operations. We look at some 

at the key learnings from all the previous chapters 

threat signals and other data across the six pillars 

parallels in cybersecurity and discuss mitigation 

of this report: to minimize impact of attacks we 

of Zero Trust—identities, endpoints, applications, 

through media literacy. We include a discussion on 

must truly practice good cyber hygiene, implement 

network, infrastructure, and data—and provide 

disinformation as an enterprise disruptor, providing 

architectures that support the principles of Zero 

guidance based on what we’re seeing. We conclude 

a four\-point plan for enterprise executives. The 

Trust, and ensure cyber risk management is built into 

with discussions about insider threats in hybrid 

chapter concludes with an in\-depth exploration of 

the business.

work environments, and an empathy imperative 

political campaign security and election integrity, 

for managing the new and significant challenges 

two areas that have been targeted by disinformation 

encountered by today’s workforce.

campaigns.

Microsoft Digital Defense Report \| October 2021

6
6

Microsoft Digital Defense Report \| October 2021 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

CHAPTER 2 

The state of cybercrime

Introduction

The cybercrime economy and services

Ransomware and extortion 

Phishing and other malicious email

Malware 

Malicious domains 

Adversarial machine learning

7

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

INTRODUCTION: The growing threat of cybercrime 

AMY HOGAN\-BURNEY, GENERAL MANAGER, DIGITAL CRIMES UNIT

Cybercrime, whether nation state sponsored or permitted, is a threat to national security. Cybercriminals are 
targeting and attacking all sectors of critical infrastructure, including healthcare and public health, information 
technology (IT), financial services, and energy sectors. Ransomware attacks are increasingly successful, crippling 
governments and businesses, and the profits from these attacks are soaring. 

The cybercrime supply chain, often created by criminal syndicates, continues to mature allowing anyone to buy 
the services needed to conduct malicious activity for financial gain or other nefarious purpose. Sophisticated 
cybercriminals are also still working for governments conducting espionage and training in the new battlefield. 

It is not hopeless, and there are two positive trends 

we have seen recently. First, more governments 

and companies are coming forward when they are 

victims. This transparency helps in several ways. It 

has made clear to governments around the world 

that cybercrime is a threat to security. Victim stories 

humanize and make clear the consequences of these 

attacks, drawing attention to the problem and allowing 

increased engagement from incident responders and 

law enforcement. Second, now that governments 

around the world recognize that cybercrime is a threat 

to national security, they have made combatting it a 

priority. Governments around the world are passing 

new laws regarding reporting, creating cross\-

government task forces, allocating resources, and 

seeking out private sector assistance.

The cybercrime 
economy and 
services

Through our investigations of online organized crime 

networks, frontline investigations of customer attacks, 

security and attack research, nation state threat 

tracking, and security tool development, we continue 

to see the cybercrime supply chain consolidate and 

mature. It used to be that cybercriminals had to 

develop all the technology for their attacks. Today, 

they rely on a mature supply chain, where specialists 

create cybercrime kits and services that other actors 

buy and incorporate into their campaigns. With the 

increased demand for these services, an economy of 

specialized services has surfaced, and threat actors 

are increasing automation to drive down their costs 

and increase scale. For example, we are seeing an 

increasing offer of backconnect proxies (proxies that 

rotate between mobile, residential, and datacenter 

systems) in addition to Remote Desktop Protocol 

(RDP), Secure Shell (SSH), virtual private network 

(VPN), virtual private server (VPS), web shells, cPanels 

(webhosting management dashboard), and other 

anonymization systems.

Other examples include selling compromised 

credentials that may have been obtained from 

phishing, scraping botnet logs or other credential 

harvesting techniques, imposter domain names, 

phishing\-as\-a\-service, customized lead generation 

(for example, victims by country, industry, or roles), 

WITH NO 

TECHNICAL 
KNOWLEDGE OF 

HOW TO CONDUCT 

A CYBERCRIME 

ATTACK, AN 

AMATEUR 

THREAT ACTOR 

CAN PURCHASE 

A RANGE OF 

SERVICES TO 

CONDUCT THEIR 

ATTACKS WITH 

ONE CLICK.

Microsoft Digital Defense Report \| October 2021

8
8

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

loads (malicious software used to update malware 

At times there are geographic groups of actors 

on an infected computer), denial of service (DoS), 

who may offer certain services, but most of these 

and more. As an illustration, in some marketplaces, 

cybercrime markets are global in nature. A buyer 

compromised credentials are offered by different 

in Brazil can obtain phishing kits from a seller in 

sellers for $1\.00 USD to $50\.00 USD, depending on 

Pakistan, domains from the United States, victim 

a variety of variables including the perceived value 

leads from Nigeria, and proxies from Romania.

of the enterprise target. The number of sites offering 

services has significantly increased in the past 12 

These prices have remained fairly steady over the 

months as well as volume of credentials and variety 

past several years, but like any other market they 

of phishing kits.

vary according to changes in supply, demand, and 

Among the services available to even amateur threat 

actors are the cryptocurrency escrow services (to 

KEY TAKEAWAYS:

externalities such as politics. 

ensure services are rendered as offered) that we 

often see in commodity ransomware campaigns 

where affiliate models have become firmly 

established. Nontechnical cybercriminals sign up with 

a ransomware affiliate where for 30% of the revenue, 

the affiliate network will supply the ransomware, 

recovery services, and payment services. The attacker 

• Identity and password/phishing attacks are 

cheap, and on the rise. Why would an attacker 

break in when they can log in?

• Distributed denial of service (DDoS) attacks 

are cheap for unprotected sites—about $300 

USD/month.

then buys “loads” from a market and pushes the 

• Ransomware kits are one of the many types of 

ransomware to the loads they purchased. They then 

attack kits designed to enable low\-skill attackers 

sit back and collect their revenue. 

to perform more sophisticated attacks.

Not all attacks work. It’s critical that we keep 
improving our defenses to increase the failure rate 
of attacks and the associated cost to attackers.

Average prices of cybercrime services for sale

Organizations now face an industrialized attacker economy with skill specialization and trading of illicit 
commodities. As seen in this snapshot of average prices, many commodities that can be purchased in 
the dark markets are very inexpensive, making attacks cheaper and easier to conduct (which also drives 
up attack volume).

9

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Ransomware 
and extortion 
Ransomware basics and 
taxonomy

Ransomware and extortion is a high\-profit, low\-cost 

business which has a debilitating impact on targeted 

organizations, national security, economic security, 

and public health and safety. What started as simple 

single\-PC ransomware has grown to include a 

variety of extortion techniques enabled by human 

intelligence and is affecting the networks of all types 

of organizations across the globe.

This combination of real\-time intelligence and 

broader criminal tactics, techniques, and procedures 

Ransomware taxonomy

Primary role

Description

Develops

Writes the malware

(TTPs) has maximized the impact of these attacks 

and driven the profits from these attacks to levels 

framework designed for taking action in combatting 
ransomware.2 Microsoft has also published a 

negotiations and raises the victim’s reputational 

costs of not paying the ransom as the attackers likely 

that were hard to imagine a few years ago. To put 

project plan with links to technical guidance to 

will not only leave the victim’s data encrypted but 

it in perspective, the publicly reported profits from 

help organizations better prepare for and respond 

also leak sensitive information.

ransomware and extortion attacks gives these 

to these attacks and is contributing to a National 

attackers a budget that would likely rival the budgets 

Institute of Standards and Technology (NIST) 

A series of criminal activities occur long before the 

of nation state attack organizations (without even 

counting the profits from attacks that never made 

publication containing a cybersecurity framework 
profile for ransomware risk management.3

ransomware is ultimately deployed across computer 

systems in an organization. As a result, we created a 

the headlines).

taxonomy that focuses on the relationship between 

To counter ransomware, a global collaborative 

threat actor deploying malware that encrypts 

any entity may play a different role at any given 

A ransomware and extortion attack involves a 

entities within the ransomware ecosystem because 

effort between the private sector, law enforcement, 

and exfiltrates data and then holds that data 

time.

and government is necessary to reduce the 

for a ransom, often demanding payment in 

profitability of this crime, make it more difficult to 

cryptocurrency. Rather than just encrypting a victim’s 

Ransomware attacks have evolved into human\-

enter the ransomware market, and supply victims 

files and requesting a ransom in exchange for the 

operated ransomware, also known as “big game 

with effective tools for efficient prevention and 

decryption key, the attackers also exfiltrate sensitive 

ransomware.”

remediation. Microsoft is a contributor to the 

data before deploying the ransomware. This 

Ransomware Task Force report, a comprehensive 

practice prevents victims from disengaging from 

Deploys

Sends phishing emails, deploys ransomware 

Provides access

Malware that loads other malware, or a group that sells access as a service 

Manages/operates

Leadership of a group (such as MAZE cartel membership) and/or function that 
provides coordination (such as managing or operating a central extortion leak site) 

Publicly reported 
connection

A publicly reported connection exists 

2 https://securityandtechnology.org/ransomwaretaskforce/report/ 3 https://aka.ms/humanoperated 

10

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

For example, as shown in the image at right, a threat 

will often provide the victim a report which includes 

Sample analysis of roles and relationships between entities within the ransomware ecosystem

actor may develop and deploy malware that gives 

root cause, criminal actor movement inside the 

one threat actor access to a certain category of 

victim network, data exposure and exfiltration, and 

victims, whereas a different threat actor may merely 

remediation recommendations.

Depending on the jurisdiction of the victim, the 

victim could be subject to data breach notification 

requirements. A law firm will often assess the 

exposure of the victim’s liability and assist the 

victim with meeting its regulatory obligations. 

Importantly, the law firm will interface with relevant 

law enforcement, where appropriate. Finally, if a 

victim is unable to return to business operations, 

an organization specializing in negotiating with 

ransomware criminal syndicates will work to obtain 

the decryption key on behalf of the victim.

deploy malware.

Post\-breach response

Just as the criminal enterprise that deploys 

ransomware typically involves several stakeholders 

each with a particular responsibility, the response to 

ransomware also involves several key stakeholders.

If a victim of a ransomware attack has cyber 

insurance, that carrier will employ certain service 

providers, including an incident response firm, a 

law firm, and an organization specializing in ransom 

negotiation. Even if a victim does not have a cyber 

insurance policy, these stakeholders are common to 

finding a resolution to the ransom.

Once a ransomware gang locks a victims’ network, 

exfiltrates data, and holds the network and 

data for ransom, an incident response team will 

investigate the root cause of the breach and drive 

remediation efforts depending on the victim’s level 

of preparedness prior to the attack. If the victim has 

sufficient backups of its data or data has not been 

stolen, often the incident response team will work 

to remove the threat actor from the victim’s system, 

restore business operations, and apply future 

mitigation measures. The incident response team 

Ransomware syndicates and affiliates are all working together toward these interconnected threats. 
Rather than one individual behind a ransomware attack, there are multiple groups of individuals, similar 
to a shared business model.

11

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Stakeholders and roles involved in post\-breach response

12

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Ransomware negotiation chat

Criminal economics: A 
changing business model

The business model for ransomware has effectively 

evolved into an intelligence operation; criminal 

actors perform research on their target victim to 

identify an optimal ransom demand. Once a criminal 

actor infiltrates a network, they may exfiltrate and 

study financial documents and insurance policies. 

They may also understand the penalties associated 

with local breach laws. The actors will then extort 

money from their victims, to not only unlock their 

systems, but also to prevent disclosure of the 

victim’s exfiltrated data to the public. After they’ve 

collected and analyzed this intelligence, the criminal 

actor will identify an “appropriate” ransom amount.

The negotiation chat, at right, with a public school 

district to extort cash in exchange for a decryption 

key to unlock the Conti ransomware deployed on 

its network demonstrates the research performed 

by the criminal in advance of the negotiation. 

Here, the criminal actor explains “we examined all 

financial documents, bank statements for the last 

year, insurance. And came to the conclusion that 

you are exaggerating about poor financial condition 

\[sic]. We also calculated your possible losses from 

lawsuits from both your staff and your students for 

the leakage of their personal data. These fines will 

exceed $30 million. We are not talking about the 

loss of reputation, which in our opinion costs more.”

THE 

RANSOMWARE 

ENTERPRISE HAS 

EVOLVED INTO 

RANSOMWARE AS 

A SERVICE DRIVEN 

BY HUMAN 

INTELLIGENCE 

AND RESEARCH.

Microsoft Digital Defense Report \| October 2021

13
13

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

There are few barriers of entry into this criminal 

Regardless of where ransomware is deployed, 

SIDEBAR: TO PAY, OR NOT TO PAY? 

to improve their tooling and ability to buy 

enterprise. A cybercriminal does not need 

typically the threat actors will demand payment via 

In the aftermath of a ransomware attack, companies 

breach access to potential victim organizations. 

specialized code development skills to profit from 

cryptocurrency through crypto wallets. Although 

are often completely offline—their security systems 

Some ransomware teams have significant 

this crime. The ransomware enterprise has evolved 

the underlying blockchain technology facilitates 

tampered with, their backup systems deleted, their 

amounts of funds for R\&D and for buying high\-

into ransomware as a service driven by human 

transparent cryptocurrency flows, the owners of 

data encrypted, and their users unable to log in. 

end 0\-days. For example, some ransomware 

intelligence and research. It is no longer solely the 

wallets remain pseudonymous. Nonetheless, they 

When operations are offline and losses pile up, it 

teams have budget to spend up to $1 million 

province of malware developers; rather, the business 

still need to find on\- and off\-ramps into the crypto 

is important to remember that paying the ransom 

USD, or more, per 0\-day. While some high\-end 

structure is modular. Malware developers are 

ecosystem. At its core, the criminal actor needs 

demands does not guarantee the restoration of 

ransomware teams buy 0\-days, others focus 

recruiting hackers with access to networks promising 

to append the blockchain with a transaction and 

operations, nor does paying prevent future attacks.

on traditional ways to gain remote access into 

a “cut” of the profit. Criminals can purchase malware 

ultimately find a way to cash out. There are several 

victims’ networks.

and access to specific networks and target specific 

stakeholders within the cryptocurrency ecosystem 

industries. This is effectively a crime syndicate where 

that facilitate ransom\-related transactions and 

In addition, we have in effect, the classic “Tragedy 
of the Commons”4— while it may make sense for 

each member is paid for a particular expertise.

payments. These intermediaries often exist in 

individual victims to pay for their own individual 

jurisdictions with governments that are historically 

benefit (restore critical business operations), the 

In the example shown below, following the crypto 

unwilling to cooperate with the United States 

payment also contributes to the growth of this 

flows, we can see where a criminal enterprise split its 

and others. It’s these intermediaries that facilitate 

damaging model for everyone. Ransom payments 

bitcoin “earnings” such that approximately 15% of 

the flow of ill\-gotten earnings from ransomware. 

can keep the cycle turning, as described below: 

the earnings flowed to the developer/manager and 

The private sector through civil litigation, and 

75% of the earnings flowed to the attacker.

the government through prosecution, regulatory 

enforcement, and international collaboration, can 

take coordinated action against intermediaries to 

disrupt the payment process.

• The business model of extortionists gets 

reinforced, which also attracts more bad actors 

into the monetization strategy. Substantial 

revenue is supplied to the actors who then use 

part of it for research and development (R\&D) 

Transaction hashes and wallet addresses

• The ransomware tools become more automated 

and effective, allowing the bad actors to 

scale and accelerate their attacks—with more 

sophistication and less effort. 

Victim ransom wallet is shown on the far left. The funds split to two different wallets on the far right. 

Text intentionally blurred for publication

Transaction hash

Bitcoin wallet addresses

4 Tragedy of the commons \- Wikipedia

14

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

EXAMPLE: CONTI RANSOMWARE 

The Conti ransomware first appeared around July 2020 adopting the double extortion business model. In this 

double extortion model, a victim is first extorted for ransom and for the possible publishing of their stolen 

data. Conti is also a ransomware as a service (RaaS), which is a subscription\-based service allowing affiliates 

of the service ready access to ransomware\-building tools and builds. Affiliates of the service agree to ransom 

percentage payouts between the ransomware developer and threat actor who performed the exploitation. Conti 

usually gains access to the victim network via other threats like Trickbot, IcedID, or Zloader. Once inside the 

victim network, Conti has a configurable reconnaissance module where it can scan internal networks looking 

for network shares and other high\-value targets. Once deployed, Conti begins to encrypt user\-modifiable data 

and databases based on targeted file extension lists. Upon completion of the encryption, a ransom note is left in 

every file directory with instructions for the user on how to contact the ransomware actors:

Ransom note

Important details to be aware of when making the 

decision whether to pay ransoms:

Paying a ransom fuels the ransomware 
syndicates

• On average, organizations that paid the ransom 

got back only 65% of their data, with 29% 
getting back no more than half their data.5 

• Ransom decryptors are buggy and regularly fail 

to decrypt the largest, most critical data files 

(files 4 GB\+ in size).

• Decrypting data files is a slow and labor\-

intensive process, most customers decrypt only 

their most critical of data files and restore the 

rest from backup.

• Restoring data does not undo any tampering 

performed by the attackers.

• Restoring data does not secure systems to 

prevent future attacks.

• Organizations must understand the legality of 

making payments in their country. Governments 

across the globe are instituting ransomware 

payment reporting requirements, may have 

penalties for payments that are made to 

sanctioned parties, and are considering laws 

that could make ransom payments illegal.

Paying a ransom gives the criminals more 
resources to expand their operations, helping 
them become more organized and specialized. 
With more funding available, the groups 
can improve their tools and code, enabling 
ransomware to spread through networks 
undetected by antivirus software.

5 The State of Ransomware 2021 – Sophos News

15

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

The user must now upload the ransom note text file to the recovery site listed in the ransom note. The note 

After the ransom note is uploaded and verified and a chat session is initiated.

serves as proof of encryption and victim identification for the ransomware actors.

Ransom recovery site

Chat session following ransom note upload

Conti News site

16

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

The negotiation phase starts with the threat actor, as they prove they can decrypt any files provided by the 

victim. After a final ransom price is negotiated, the ransomware actor provides a Bitcoin wallet address for 

the victim to send payment. Conti ransomware actors maintain recovery and news sites on regular top\-level 

domains (as on the open web) as well as on the dark web or Tor (also known as The Onion Router).

As part of the double extortion business model, the actors behind Conti maintain a news site, which serves as 

the publishing site to prove that if the ransom is not paid, the victim’s private information will be posted publicly 

and could be sold on the black market. The Conti News site currently lists hundreds of victims with various 

samples of their private data.

Conti victims are located mostly in the United States and Europe and include public schools, healthcare 

providers, manufacturing companies, US city governments, and even public utility providers.

What we’re seeing in ransomware data and signals 

DEFENDER SIGNALS

Ransomware encounter rate (machine count): Enterprise customers

Ransomware encounter rate (machine count): All customers

These charts show the overall increase in ransomware encounters, with notable surge to consumer and commercial encounters in late 2019,6 when RaaS 
started to grow, and in early 2020 at the onset of the COVID\-19 pandemic.7

6 https://www.microsoft.com/security/blog/2019/12/16/ransomware\-response\-to\-pay\-or\-not\-to\-pay/ 7 https://www.microsoft.com/security/blog/2020/03/20/protecting\-against\-coronavirus\-themed\-phishing\-attacks/ 

17

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Ransomware machine counts by country (July 2020\-June 2021\)

DART DATA

While the Colonial Pipeline ransom attack of May 2021 drew considerable public attention, our Detection 

and Response Team (DART) ransomware engagement data shows that the three most targeted sectors were 

consumer, financial, and manufacturing. Despite continued promises from ransomware actors not to attack 

hospitals or healthcare companies during a pandemic, healthcare remains in the top\-five sectors victimized by 

human\-operated ransomware.

DART ransomware engagements by industry (July 2020\-June 2021\)

The stakes have changed. There is a massive 
growth trajectory for ransomware and extortion.

18

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

SUMMARY OF RECOMMENDATIONS

Use the phases as a starting plan for what to do first, next, and later to get the most impactful elements first. 

The stakes have changed. There is a massive growth trajectory for ransomware and extortion. To help protect 

These recommendations have been prioritized using the Zero Trust principle of assume breach, which focuses 

your organization from ransomware, we recommend that organizations:

on minimizing business risk by assuming the attackers can successfully gain access to your environment through 

Deploy ransomware protection

one or more methods. 

Microsoft supports the guidance presented in the Ransomware Playbook by the Cyber Readiness Institute.8

Learn more:

3 steps to prevent and recover from ransomware Microsoft Security blog 

\|

(9/7/2021\)

Prepare a recovery plan by making it harder to access and disrupt systems, which minimizes the monetary 

incentives for ransomware attackers and makes it easier to recover from an attack without paying the ransom. 

Ransom mafia analysis of the world's first ransomware cartel pdf (analyst1\.com) (4/7/2021\)

Ransomware Playbook \- Cyber Readiness Institute

Rapidly protect against ransomware and extortion Microsoft Docs 

\|

(8/24/2021\)

Azure Sentinel Fusion Detection for Ransomware (microsoft.com) (8/9/2021\)

The growing threat of ransomware \- Microsoft On the Issues (7/20/2021\)

Human\-operated ransomware Microsoft Docs 

\|

(5/27/2021\)

Limit the scope of damage by forcing the attackers to work harder to gain access to multiple business\-critical 

systems. Establish least\-privilege access and adopt Zero Trust principles. These steps make it harder for an 

attacker who gets in to a network to travel across the network to find valuable data to lock up. Also, encrypt 

data at rest, and practice good backup\-and\-restore hygiene. This way, even if data is stolen it will be encrypted 

and not very useful to the attackers. In the unfortunate event that the attacker does encrypt your data, you will 

have a good backup to restore from and use to maintain business continuity. 

Make it harder to get in by following basic cybersecurity hygiene steps that make it more difficult for attackers 

to gain access to the network. The most important of these steps is the use of multifactor authentication (MFA), 

which is important to raising friction for entry but will take time to complete as part of a larger security journey. 

Other steps, such as keeping up to date on patching and correct configuration, can be taken to identify and 

close off vulnerable entry points.

8 Ransomware Playbook \- Cyber Readiness Institute

19

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Phishing and 
other malicious 
email 
Threat to identity 

In 2020, the FBI IC3 Report9 identified phishing 

as the top crime type for victim complaints. The 

number of reports doubled compared to the 

From our investigations on online organized crime 

Identity is further threatened by impersonation 

networks involved in business email compromise 

as may be seen in BEC attacks where one party to 

(BEC), we noted broad diversification of how 

a financial transaction is impersonated to divert 

credentials are obtained, verified, and later used 

payments to an unauthorized recipient. Our 

that may explain the increased threat. Threat actors 

investigations identified that threat actors would 

are increasing their automation and purchasing 

monitor financially inclined messages to find an 

tools to increase the value of their criminal 

identity to impersonate and thereafter register 

activities. Credentials belonging to unsuspecting 

homoglyph/imposter domains to resemble the email 

victims could be obtained from phishing websites 

of the person being impersonated. In this case, the 

that impersonate a myriad of online services, 

person whose credentials were stolen would cause 

automatically scraping and parsing logs belonging 

another person to become a victim.

previous year. Phishing poses a significant threat 

to infected devices that record the keys typed on 

to both businesses and individuals, and credential 

keyboards to guessing where credentials from one 

phishing was leveraged in many of the most 

breached online service were reused on another.

damaging attacks last year.

For each credential, there are services that enrich 

the information on the identity with additional 

details on the person’s identity that includes 

name, company they work for, roles, seniority in 

company, and industry associated to the company. 

With this information, the identity could be used 

in BEC attacks, to send unsolicited messages 

(spam), to gather sensitive information, or to host 

phishing websites in related online accounts. Even 

when one attack occurs, accounts may be resold 

after automated systems verify that they remain 

compromised.

9 https://www.ic3\.gov/Media/PDF/AnnualReport/2020\_IC3Report.pdf

Microsoft Digital Defense Report \| October 2021

20
20

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Emails determined as phish

Top 10 verticals affected by phishing (Defender detections, June 2021\)

What we’re seeing 

Types of malicious emails

Whether their goal is to phish credentials, redirect 

a wire transfer to their own bank account, or 

download malware onto a machine, attackers are 

most likely to utilize email as their initial entry 

vector for a campaign. While a lot of focus is given 

to credential phishing, malicious emails are used in 

multiple types of cyber incidents. Microsoft security 

researchers observe the following three most 

common types of malicious emails:

PHISHING 

Phishing is the most common type of malicious 

email observed in our threat signals. These emails 

are designed to trick an individual into sharing 

sensitive information, such as usernames and 

passwords, with an attacker. To do this, attackers 

will craft emails using a variety of themes, such 

as productivity tools, password resets, or other 

notifications with a sense of urgency to lure a user 

to click on a link.

The phishing webpages used in these attacks may 

utilize malicious domains, such as those purchased 

and operated by the attacker, or compromised 

domains, where the attacker abuses a vulnerability 

in a legitimate website to host malicious content. 

The phishing sites frequently copy well\-known, 

legitimate login pages, such as Office 365 or Google, 

to trick users into inputting their credentials. Once 

the user inputs their credentials, they will often 

be redirected to a legitimate final site—such as 

the real Office 365 login page—leaving the user 

unaware that actors have obtained their credentials. 

Meanwhile, the entered credentials are stored or 

sent to the attacker for later abuse or sale.

Attackers also use consent phishing to send users 

links that, if clicked, will grant the attacker access 

and permissions to applications, such as via OAuth 

2\.0 authorization protocol. In these instances, users 

may unwittingly grant the attackers permissions to 

applications that enable them to access a wealth of 

sensitive information.

The number of phishing emails observed in 

Microsoft Exchange global mail flow increased 

during the period from June 2020 through June 

2021\. We saw a pronounced surge in November 

potentially related to holiday\-themed phishing, and 

a subsequent decrease over the US winter holidays, 

potentially indicating that attackers send fewer 

messages when many people are not working.

While all industries receive phishing emails, some 

verticals within those industries tend to receive more 

phishing campaigns than others. The verticals most 

affected by phishing may change month to month 

depending on several factors, including attacker 

objectives, availability of leaked email addresses, 

or current events regarding specific sectors and 

industries.

21

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Malware emails per week

There has been an overall downward trend in the number of emails containing malware.

Top 15 Defender detections (June 2021\)

Spyware designed to steal credentials was the most common type of malware observed through email 
delivery and was detected three times as often as the next highest detection.

MALWARE DELIVERY 

the recipient to open the files and download the 

Malware delivery is another example of how threat 

malware. By using these archive files to house the 

actors utilize emails for their objectives. A variety 

malicious document—frequently an Excel or Word 

of malware variants, such as Agent Tesla, IcedID, 

document—the attackers can use a unique archive 

Trickbot, and Qakbot, use email as a primary method 

file for every recipient, making it more difficult for 

of distribution. These emails will use either links or 

defenders to fully scope a campaign.

attachments to deliver malware and many times use 

techniques that overlap with phishing emails. For 

Interestingly, between July 2020 and June 2021 

example, both malware delivery email and phishing 

we observed an overall downward trend in the 

email may use links that direct to a CAPTCHA test to 

number of emails containing malware, indicating 

evade detection from security technologies.

that attackers may be using other means of entry. 

In addition, a few notable malware takedowns—

Since malware does not rely on user interaction in 

namely, Trickbot and Emotet—may have contributed 

the same way phishing does, attackers can design 

to this overall decline. A large spike in October is 

their delivery to be less noticeable to the user. For 

associated with the distribution of those malware 

example, when using attachments as a delivery 

variants, and the rapid decrease following the spike 

method, attackers may use a decoy document 

aligns to when the Trickbot malware was taken down 

with macros that, when enabled by the recipient, 

by Microsoft.

download the malware in the background without 

the user’s knowledge. In these cases, the user may 

The malware that attackers distribute via email 

think that the document is broken or isn’t intended 

changes regularly for a variety of reasons, including 

for them and may be completely unaware that 

malware takedowns and attacker objectives. As 

malicious software is running on their machine.

shown in the chart on Defender detections for 

June 2021, the most prolific malware observed by 

One of the most common methods of malware 

Microsoft was Agent Tesla, which is a credential\-

delivery observed in the past year was through 

stealing spyware. The second most observed 

password\-protected archive files. These emails 

malware, Tisifi, which identifies social engineering 

contain archive files, such as ZIP attachments 

lures, was seen only one third as much as Agent 

that are password protected, to prevent security 

Tesla. EncDoc and CVE\-2017\-11882 as the third 

technologies from detonating and analyzing 

and fifth top detections indicate that attackers still 

them. However, the passwords for these files are 

favor malicious documents as a common method 

often included in the body of the email to enable 

of delivering a variety of threats. The fourth top 

22

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

detection, HTML/Phish, includes only phishing 

member’s birthday gift or for employees as rewards. 

Detecting web\-based phishing 

Domains created specifically for attacks tend 

emails that use an HTML attachment. These types of 

The recipient is typically asked to send the digital 

In the past year, web\-based phishing attacks 

to be active for shorter periods, and with fewer 

phishing frequently take the form of fake voicemail 

gift cards to the attacker once purchased, but we 

have continued to become more sophisticated. 

malicious URLs, than attacks that abuse legitimate 

phishing messages. 

have also seen attackers asking the user to buy 

Phishing kits used by web\-based phishing attacks 

infrastructure. Over the last year, Microsoft 

physical gift cards and send a photo of the code on 

typically use images, context\-based content, and 

SmartScreen has seen an increase in attacks that 

BUSINESS EMAIL COMPROMISE 

the back of the card, enabling the attacker to resell 

other advanced techniques to avoid detection. 

begin and end within as little as an hour or two.

While not the most prolific type of malicious email 

them online or trade them for cryptocurrency.

Our machine learning (ML) models and network 

in terms of quantity, BEC has proven to be the 

heuristics must continuously evolve to maintain 

most financially impactful type of cybercrime.10 BEC 

A much more sophisticated and financially damaging 

effective protection. The language used by attackers 

Malicious email techniques 

occurs when an attacker pretends to be a legitimate 

type of BEC is wire transfer fraud. In this type of 

has also improved significantly; past user guidance 

Attackers have adapted over time to make their 

business account—utilizing either a compromised 

BEC, actors will insert themselves into expected 

to look for poor spelling and grammar is now 

emails more likely to evade detections and 

email address, a lookalike domain they have 

financial transactions and ask the recipient to adjust 

less effective, particularly against targeted, more 

protections by utilizing aspects of legitimate 

registered, or a free email service such as Hotmail or 

the bank account information on an outgoing wire 

advanced attacks. Modern kits are sufficiently 

business emails. Defenders need to protect the 

Gmail—and sends emails designed to trick recipients 

transfer. The actors will masquerade as the intended 

sophisticated to masquerade as legitimate content 

company but also have a duty to maintain the flow 

into taking some financial action, handing over 

recipient of the funds, so this does not seem out of 

in their use of spelling, grammar, and imagery.

of business—and attackers rely on this fact to get 

sensitive information, or providing assets, such as 

the ordinary to the victim. Once the victim wires the 

their foot in the door. In the last year, Microsoft 

gift cards, to the attacker. 

money to the new account, it is withdrawn by the 

Phishers are increasingly leveraging legitimate 

security researchers have observed attackers using 

The most common type of BEC observed by 

can help to avoid this type of scam by ensuring that 

minority of detected phishing attacks. Microsoft 

email campaigns to make emails appear more 

Microsoft in the past year was gift card scams. In 

financial policies require verification for changing 

SmartScreen detected more than a million unique 

legitimate to both end users and protection 

these scams, attackers will usually create a multitude 

accounts. Finance employees should verify via a 

domains used in web\-based phishing attacks in 

technologies.

actors and may be difficult to retrieve. Companies 

infrastructure, but this pattern still accounts for a 

numerous techniques across multiple malicious 

of free email accounts, changing the display name 

means other than email—such as from a known, 

the last year, of which compromised domains 

depending on the target, though attackers have 

trusted phone number with the recipient—before 

represented just over 5%. This 5% of domains 

also registered their own domains for these attacks 

making account number changes that originate 

typically host phishing attacks on legitimate websites 

or have created target\-specific free email accounts. 

from emails. Additionally, utilizing impersonation 

without disrupting any legitimate traffic so that their 

They will then pretend to be someone the recipient 

protections features in email security products can 

attack remains hidden for as long as possible.

works with (usually their boss or an executive at 

help prevent attackers from successfully conducting 

their company) and ask them to purchase gift cards 

this type of scam.

(often with company funds). Frequently, these emails 

suggest that the sender wants them for a family 

10 https://www.ic3\.gov/Media/PDF/AnnualReport/2020\_IC3Report.pdf; https://www.microsoft.com/security/blog/2021/06/14/behind\-the\-scenes\-of\-business\-email\-compromise\-using\-cross\-domain\-threat\-data\-to\-disrupt\-a\-large\-bec\-infrastructure/ 

23

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Microsoft Digital Defense Report \| October 2021

24
24

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Some common techniques observed over the past year: 

COMPROMISED SENDERS \> COMPROMISED SERVICES 

ABUSE OF LEGITIMATE INFRASTRUCTURE 

Defenders have often told their end users to verify aspects within an email were legitimate before interacting 

For years, attackers have used compromised senders to perpetuate phishing email chains, as they use the 

with that email, such as the sender and any links within the email. This advice is still valuable, but sometimes 

victim’s email account to send additional phishing emails. While this is still extremely prevalent, many companies 

the links and senders can look legitimate but contain malicious content. Attackers are shifting to abusing 

have begun utilizing MFA, which reduces the effectiveness of this method. Attackers therefore are adjusting 

legitimate infrastructure to mask the malicious content in their emails. For sender addresses, attackers may 

their methods to begin compromising entire email services, such as when NOBELIUM gained access to an email 

register trial tenants for services such as Office 365, which make their email appear much more legitimate. 

marketing solution that enabled the attacker to send as multiple, legitimate addresses.11

Additionally, attackers are using ways to mask the malicious domain in an email, either by using open redirects 

Phishing email using compromised service on behalf of legitimate companies

cases, it may be tricky for users to know when an email is legitimate or malicious.

from legitimate domains or by abusing legitimate hosting platforms such as Google Drive or OneDrive. In these 

Legitimate infrastructure abuse

Attackers abuse legitimate contact forms 
on websites to send emails, and legitimate 
Google sites to host malware.

11 https://www.microsoft.com/security/blog/2021/05/27/new\-sophisticated\-email\-based\-attack\-from\-nobelium/ 

25

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

FAKE REPLIES 

DEFENSE EVASION 

In addition to users being instructed to verify aspects of the email, such as the sender or links before interacting 

While attackers are focusing their techniques on convincing the recipient to interact with an email, they are also 

with them, users have also been instructed not to interact with emails they are not expecting to receive. This is 

aware that all that effort will be worthless if the email is never delivered to the victim. Because of this, threat 

still extremely valuable advice, but attackers are aware of this as well and have shifted their strategies to find 

actors are developing new means of defense evasion in email. It used to be enough for an attacker to include 

ways to convince recipients that they are expecting the email. One way that they do this is by crafting fake reply 

a password\-protected archive file to evade detection, but most security technologies can now input passwords 

emails. In these cases, the attacker will take the contents of a previous email from a compromised mailbox, or 

included in the email to detonate them and identify malicious content. Attackers have shifted to including 

will craft an entirely new email, and include it in the body of the email in a way that appears that the new email 

CAPTCHAs and legitimate login screens for services such as Microsoft or Google that prevent detection 

is a reply. Users who have jobs that require them to email dozens of people per day may not remember each 

technologies from reaching the malicious content.

email they have sent. Seeing a fake reply may convince them that they are expecting the email and cause them 

to interact with malicious links or attachments. Utilizing email security features that can notify a user when 

an email is being sent from a user they have not interacted with before can help mitigate this technique. This 

technique is a favorite of malware variants such as Emotet and IcedID and is also frequently used in BEC emails.

Fake reply email

Gift card scam BEC email using 
fake reply to trick the user into 
thinking they were expecting 
this email.

26

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

The digital journey of stolen credentials
Where do your stolen credentials go after 
they are entered into a fake web page?

27

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Secret phishers: The hidden 
economy of sophisticated 
phish kits 

This stratification of the cybercrime world is an 

plug\-and\-play phishers have largely been viewed 

increased threat to business infrastructure as 

as lower\-level coders compared to the much more 

phish kit authors are more technically skilled than 

sophisticated phish kit author and mastermind of 

the phishers and have a much broader reach by 

the overall operation.

It is a long\-held perception among research and 

orders of magnitude. The anonymity of the dark 

business communities that victim credentials are 

web enables this technique. Phishing has generally 

delivered to the individual (or group) operating 

been known to be a scheme in which a phisher 

phishing campaigns. Researchers within the 

(or group of phishers) buys a kit on a dark web 

security community12 have begun to identify more 

market, obtains infrastructure components such as 

sophisticated kits in which not only are victim 

a server, a domain to host the imitation site, and an 

credentials sent to the phishers running a phishing 

email account or other endpoint to receive victim 

campaign, but they are also likely going back 

information. Once the infrastructure is assembled, 

to the kit’s originating author or a sophisticated 

they essentially just “stick their poles in the water”—

intermediary who has modified the kit with a hidden 

the entire process is designed to be as easy as 

collection account before redistributing the kit. The 

possible by the authors and distributers of kits. 

Microsoft Digital Crimes Unit (DCU) has seen several 

Although it is important not to overgeneralize, these 

variations of this technique. 

12 https://www.wmcglobal.com/blog/phishing\-kit\-exfiltration\-methods

28

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Phish kits and credential harvesting

29

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Trends at Microsoft, 2020\-2021

What’s in Microsoft’s phishing 
defense toolbox? How we 
approach employee awareness 

In 2020, the industry saw a surge of phishing campaigns that has 
remained steady throughout 2021\. Internally at Microsoft, we saw an 
increase in overall number of phishing emails, a downward trend in 
emails containing malware, and a rise in voice phishing (or vishing). 

Fortunately, we were prepared with an effective foundation of protective controls to reduce the number of 

successful phishing attempts, and acknowledging the evolving threat landscape, we had expanded our controls 

to cover other vectors that could be exploited (beyond email, such as Forms and Teams).

What’s in our toolbox

There is not a silver bullet fix for phishing; it must be solved through a multipronged approach. We focus on four 

primary elements: Protective controls, User awareness, Reporting and insights, and Detect and respond.

With these methods, we have seen a 50% 
year\-over\-year reduction in susceptibility.

Microsoft Digital Defense Report \| October 2021

30
30

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

No matter how many protective controls we have in place, mitigation remains a crucial element to combating 

Beyond detection and protection, it is imperative that we cultivate a security\-conscious culture, equip our 

the phish that make it through our defenses as threat actors increase their level of sophistication. Our security 

employees (our last line of defense) with skills to identify a phish, and provide a simple reporting mechanism 

operations center is equipped with Microsoft Defender for Office 365’s tools and automation to quickly detect, 

that is a consistent experience across all platforms. Employee reporting is vital, but closing the feedback loop by 

investigate, and effectively remediate malicious emails. For us, the automated incident response features have 

validating the report is just as important. 

been key in enabling our team to move quickly because minutes matter.

Training followed by simulations, reinforcement, and targeted simulations

Beyond detection and protection, it is imperative 
that we cultivate a security\-conscious culture.

Despite the increased sophistication of phish, susceptibility of employees has decreased, attributed to 
increased frequency of simulations and training.

Microsoft Digital Defense Report \| October 2021

31
31

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Our approach to employee phishing awareness includes annual foundational training, simulated exercises, and 

their support staff. The findings from our simulated exercises are also leveraged to identify opportunities within 

positive reinforcement. Simulations leveraging Microsoft Defender for Office 365’s Attack Simulator and Training 

the product to aid employees in identifying phish (such as safety tips).

are built on incidents insights to ensure we are exposing our employees to phish that are realistic to the level 

of sophistication we may see in our environment. Employees who repeatedly fall susceptible to simulations are 

Learn more:

phished on a more frequent basis to increase their opportunity to learn through experience and preventative 

guidance. We also run targeted campaigns focused on high\-risk groups such as new employees, executives, and 

Automatically triage phish submissions in Microsoft Defender for Office 365 (9/9/2021\)

Employee phishing awareness 

Microsoft Digital Defense Report \| October 2021

32
32

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Summary of recommendations about malicious emails 

1\. Use MFA to lessen the impact of credentials 

6\. Create and enforce finance policies that require 

Learn more:

Trend\-spotting email techniques: How modern 

phishing emails hide in plain sight Microsoft Security 

\| 

Blog

 (8/18/2021\)

being phished by attackers.

employees to verify any account information 

2\. Develop robust user education processes that 

changes, including wire transfer information, 

use positive reinforcement to teach users how 

with the account holder.

to identify potentially malicious emails. Create 

7\. Ensure that all your email is effectively signed 

processes wherein users can report suspicious 

(DKIM) and verified on delivery (DMARC) 

emails and can receive feedback on whether 

so that your customers are protected from 

the email they submitted was indeed malicious. 

attackers trying to send messages as your 

Focus extra training on groups that may be 

domain/brand.

more heavily targeted, such as executives, 

8\. Enable advanced protections for your users,13 

executive assistants, and finance employees. 

including:

Share real\-world phishing examples that your 

• Look\-alike domains or impersonations of 

company has received with your end users so 

important users in the organization.

that they understand the threat and know what 

• Deep analysis (detonation) of 

to expect.

attachments and URLs across the 

3\. Surface external emails to recipients by 

• Collaboration suite to protect against 

appending a tag to the subject line of any 

0\-day attacks.

email that originates from an email address 

• Post\-delivery protection to remove mails 

outside of your organization.

that were delivered and later determined 

4\. Enable features that allow users to spot 

 malicious.

emails coming from senders they have not 

9\. Eliminate opportunities for attackers to bypass 

communicated with in the past.

your security, such as allowing listing for 

5\. Review mail flow rules to ensure that broad 

senders, domains, or IP addresses.

rules are not inadvertently allowing malicious 

emails to be delivered.

13 Microsoft Defender for Office 365 \- Office 365 Microsoft Docs

\| 

33

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Malware 
Trends we’re seeing 

While phishing has grown over the last year, 

malware and the cybercrime infrastructure that 

supports attacks has also continued to evolve. 

There are key malware areas where Microsoft 

365 Defender Threat Intelligence has observed 

changing trends in recent years, many of which 

require equal parts innovative defensive strategies 

and historically resilient mitigations such as multi\-

factor authentication and robust application security 

practices. 

Individualized malware techniques and actions

Within the popular malware types and delivery 

methods analyzed over the past year, Microsoft 

observed many trends in individual tactics used 

during infection. Despite the wide range of 

outcomes such as ransom, data loss, credential 

theft, and espionage, most pieces of malware rely 

on similar strategies for establishing themselves in a 

network. Windows PowerShell launched by malicious 

processes with suspicious commands or encoded 

values was the most common behavior Microsoft 

observed from malware in recent months. The next 

most common were attempts by malware to rename 

payloads to mimic system processes or replace them 

entirely, and using malware to collect data such as 

credentials from browser caches. 

Other noteworthy behaviors and protection 

Alert counts by activity (May\-June 2021\)

opportunities for security operation centers are the 

use of specific reconnaissance commands, processes 

being added to startup folders, scheduled task or 

registry alterations, and malicious process execution 

by abuse of Office documents. These behaviors 

stand out due to widespread use among all malware 

regardless of sophistication, though Microsoft has 

also observed more specific tactics that are more 

difficult for enterprises to mitigate. 

Fileless malware and evasive behavior

“Fileless” malware is malware that derives most of 

its components from system processes or legitimate 

tools already on a device, which can make it harder 

to remove and detect, since more than a single file 

needs to be removed. Persistence strategies can 

include registry, scheduled task, and startup folder 

persistence to remove the necessity for malware to 

remain a static item in the filesystem. Free or easily 

available remote access trojans (RATs), banking 

trojans, and offensive toolkits like Cobalt Strike are 

routinely utilizing process injection and in\-memory 

execution. These are methods of abusing stolen 

administrative privileges to move malicious code 

into running benign processes rather than in static 

files, to circumvent easy removal. To combat these 

kinds of behaviors it is imperative that security 

teams within organizations review their incident 

response and malware removal processes to include 

sufficient forensics to ensure common malware 

persistence mechanisms have been fully remediated 

after cleanup by an antivirus solution.

34

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Legitimate service abuse in network 

Emotet encounters 

optimization strategies and by utilizing existing 

infections to install browser extensions to modify 

search results and to surface illicit material attacker 

content. 

This was the case in 2020 with the Adrozek16 

malware, a browser extension used where infected 

devices would use browser extensions to replace 

legitimate search results with links to malware 

impersonating Microsoft products and other 

legitimate software. The operators of Gootkit, a 

malware infection that can led to ransomware, 

used a slightly different technique to abuse search 

engines by purchasing advertising in 2020 to uplift 

the links to compromised sites hosting the malware. 

Other information\-stealing malware, such as Jupyter 

or SolarMarker, used yet another method to appear 

in search results by using documents hosted 

on services such as AWS, Google, and Strikingly 

communications

Another tactic used in many malware campaigns 

this past year utilized legitimate sites in almost 

every stage of malware: delivery, reconnaissance, 

command and control, exfiltration, malicious 

advertising, and cryptocurrency mining. Cloud 

services such as Google Drive, Microsoft OneDrive, 

Adobe Spark, Dropbox, and others are still very 

popular for use as initial delivery of malware, while 

content “pasting” sites such as Pastebin.com, 

Archive.org, and Stikked.ch are increasingly popular 

for covert use in multi\-part and fileless malware. 

In the last case, the code used in the malware is 

pulled directly from the pasting site and executed 

immediately into memory, bypassing the need to 

download malware as a single file.

Larger trends in malware propagation and 

behavior

BOTNET RENOVATIONS 

In January 2021, law enforcement performed a takedown, which led to the demise of the Emotet family 
of malware and a dramatic subsequent decrease in Emotet encounters.14

class of evasive malware began delivering more 

and new infection methods as well. Lemon Duck, as 

content delivery network to lead users searching 

severe secondary components at faster speeds. 

with most emerging botnets, uses over 10 distinct 

for common terms via search results to PDF pages 

Botnet as a term has been evolving as well. 

In January 2021, law enforcement performed a 

methods of infection across Windows and Linux 

that would ultimately establish persistence on their 

Historically it was used to refer to a network of 

takedown, which led to the demise of the Emotet 

environments. Newer botnets are also quick to begin 

device.

computers completing tasks for an operator. 

family of malware and a dramatic subsequent 

using new vulnerabilities to infect servers. Despite 

However, now most malware families could 

decrease in Emotet encounters. Botnets such as 

this, most methods still rely on unpatched edge 

Information stealing, data exfiltration, and other 

potentially be classified as having botnet 

Phorpiex15 gradually increased in number of infected 

applications, lateral movement via connected drives, 

areas of malware delivery can increasingly leverage 

components or behaviors.

base hosts and delivered numerous ransomware and 

and weak credentials on available services. 

browser modifications and search results to achieve 

As historically prevalent malware botnet 

its behavior, including the Avaddon ransomware. 

SEO AND MALICIOUS ADVERTISING

secondary malware components to further monetize 

their ends. This continues to solidify a class of 

malware leveraging the browser for delivery and 

infrastructures such as Trickbot and Emotet were 

Botnets such as Lemon Duck, Purple Fox, and 

Search engine results and advertising are also an 

exploit across both consumer and enterprise sectors.

disrupted, other malware families have replaced 

Sysrv\-Hello, surged this past year, incorporating 

increasingly effective means of delivering malware to 

them. In their place, older botnets as well as a new 

new programming languages, new infrastructure, 

end users, both via abusing legitimate search engine 

14 https://www.europol.europa.eu/newsroom/news/world%E2%80%99s\-most\-dangerous\-malware\-emotet\-disrupted\-through\-global\-action 15 Thttps://www.microsoft.com/security/blog/2021/05/20/phorpiex\-morphs\-how\-a\-longstanding\-

botnet\-persists\-and\-thrives\-in\-the\-current\-threat\-environment/ 16 https://www.microsoft.com/security/blog/2020/12/10/widespread\-malware\-campaign\-seeks\-to\-silently\-inject\-ads\-into\-search\-results\-affects\-multiple\-browsers/ 

35

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Browser search results manipulation

Comparison of search results pages on an unaffected machine and one with Adrozek running.

MALWARE TOOLS 

perform system and network discovery actions and 

Malware has evolved to take advantage of tools 

move laterally through a network. Cobalt Strike is 

that are available and, in some cases, are not 

specifically designed to evade traditional detection 

inherently malicious. One prime example has 

methodologies and offers the operator a range 

been the use of Cobalt Strike, a commercial 

of options for performing obfuscation of their 

penetration testing tool. While Cobalt Strike is a 

attack commands. These obfuscation techniques 

penetration testing, it has been used more and 

themselves can however become a signal, and 

more frequently in various attacks, ranging from 

identifying Cobalt Strike has become more essential 

nation state to human\-operated ransomware, to 

than ever as the cybercriminal economy leads to 

malware that plants Cobalt Strike quickly, handing 

to gather data from and monetize the networks 

off to ransomware operators.

that they have access to. In addition, the volume 

of network traffic plus the usual noise of constant 

WEB SHELLS DEEP DIVE 

internet attacks means that targeted traffic aimed 

Web shells remain popular with advanced 

at a web server can blend right in, making detection 

persistent threat (APT) actors of all types, including 

of web shells a lot more difficult and requiring 

NOBELIUM17 and HAFNIUM18 nation state activity 

advanced behavior\-based detections.

groups. As DART and the Microsoft 365 Defender 

Research Team reported in both 202019 and 2021,20 

In February 2020, we reported a steady increase 

web shell usage continues to climb among nation 

in the use of web shells in attacks worldwide. The 

state groups and criminal organizations. Web 

latest Microsoft 365 Defender data shows that this 

shell is a piece of malicious code, often written in 

trend not only continued, but it also accelerated; 

typical web development programming languages 

in every month from August 2020 to January 2021, 

(such as ASP, PHP, or JSP), that attackers implant 

we registered an average of 140,000 encounters of 

on web servers to provide remote access and code 

these threats on servers, which was almost double 

execution to server functions. Web shells allow 

the 77,000 monthly average.

adversaries to execute commands and steal data 

from a web server or use the server as a launch pad 

Throughout 2021 we saw an even bigger increase, 

for further attacks against the affected organization.

with an average of 180,000 encounters per month. 

The escalating prevalence of web shells may be 

encounters, which we attributed to the HAFNIUM 

attributed to how simple and effective they can 

nation state activity group targeting Exchange 

In March 2021, we saw a huge spike in web shell 

be for attackers. Once installed on a server, web 

servers with 0\-day exploits.

shells serve as one of the most effective means of 

persistence in an enterprise. We frequently see cases 

In March and April of 2021, as exploit code became 

where web shells are used solely as a persistence 

available for web\-facing on\-premises Exchange 

mechanism. Web shells guarantee that a backdoor 

servers, we saw a large spike in web shell detection 

exists in a compromised network, because an 

rates. This was due to multiple threat actors using 

attacker leaves a malicious implant after establishing 

a “compromise first, monetize later” approach that 

an initial foothold on a server. If left undetected, 

takes advantage of customer patching delays. Actors 

web shells provide a way for attackers to continue 

jump on opportunities as soon they arise. 

17 https://www.microsoft.com/security/blog/2021/02/11/web\-shell\-attacks\-continue\-to\-rise/ Feb 2021 18 https://www.microsoft.com/security/blog/2021/03/02/hafnium\-targeting\-exchange\-servers/ 19 https://www.microsoft.com/security/

blog/2020/02/04/ghost\-in\-the\-shell\-investigating\-web\-shell\-attacks/ 20 https://www.microsoft.com/security/blog/2021/02/11/web\-shell\-attacks\-continue\-to\-rise/

36

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

To minimize risk, organizations should accelerate their deployment of security updates, especially for internet\-

facing systems. To minimize risk, organizations should accelerate their deployment of security updates, 

especially for internet\-facing systems.

Summary of recommendations for malware prevention 

1\. Install security updates on all applications and operating systems promptly.

2\. Enable real\-time protection through an antimalware solution, such as Microsoft Defender.

Web shell encounters, Defender signals (September 2020\-June 2021\)

Learn more:

3\. Mitigate large attack vectors such as macro abuse, exposed edge services, insecure default configurations, 

legacy authentication, unsigned script types, and suspicious executions from certain file types delivered 

through email. Microsoft offers some of these larger mitigations through the use of attack surface 

reduction rules21 to prevent malware infection. Azure Active Directory users may also leverage security 

defaults22 to establish baseline authentication security for cloud environments.

4\. Enable Endpoint Detection and Response functionality to analyze and respond to threats based on 

individual behaviors and techniques proactively.

5\. Enable domain and IP\-based protections on hosts as well as at network gateways, if possible, to ensure 

infrastructure\-based coverage is complete. 

6\. Turn on potentially unwanted applications (PUAs) protection. Many antimalware solutions may label 

initial access threats such as adware, torrent downloaders, RATs, and Remote Management Services 

(RMS) as PUA. Occasionally, these types of software may be disabled by default to prevent impact to an 

environment. 

7\. Determine where highly privileged accounts are logging on and exposing credentials. Monitor and 

investigate logon events for logon type attributes. Highly privileged accounts should not be present on 

workstations. 

8\. Practice the principle of least privilege and maintain credential hygiene. Avoid the use of domain\-wide, 

admin\-level service accounts. Restricting local administrative privileges can help limit installation of RATs 

and other unwanted applications. 

HAFNIUM targeting Exchange Servers with 0\-day exploits Microsoft Security Blog 

\| 

(3/2/2021\)

9\. Educate users about malware threats, such as RATs, that can propagate through email as well as through 

Web shell attacks continue to rise \- Microsoft Security (2/11/2021\)

web downloads and search engines.

Ghost in the shell: Investigating web shell attacks \- Microsoft Security (2/4/2021\)

Learn more:

Use attack surface reduction rules to prevent malware infection Microsoft Docs

\|

 (6/23/2021\)

Turn on network protection Microsoft Docs

\|

 (6/14/2021\)

Block potentially unwanted applications with Microsoft Defender Antivirus Microsoft Docs

\|

 (6/02/2021\)

21 Use attack surface reduction rules to prevent malware infection Microsoft Docs

 \|

 22 Azure Active Directory security defaults Microsoft Docs

\|

37

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Malicious 
domains 

Any domain used in the pursuit of cybercrime can 

be considered malicious. Malicious domains can 

be legitimate sites which have been compromised 

to enable criminals to host malicious content on 

subdomains, or they can be entirely fraudulent 

infrastructure set up for the commission of a crime. 

Cybercriminals use malicious domains for three 

primary functions: information transmission, location 

obfuscation, and building resiliency against those 

seeking to interfere with their criminal activities.

Domains are used for data exfiltration, controlling 

ransomware communication, hosting phishing 

pages, and providing control to malware. They 

are also used as email domains to create visually 

identical imposter email aliases for deception. 

Fraudulent domains can use trademarks to deceive 

customers or provide a platform for fraud, such as 

Domain proliferation and 
threat mitigation 

How domains are being used 
for malware 

The number of domains available on the internet 

A malicious domain is often used as a destination 

has mushroomed over the past several years. This 

to which malware victims are directed. In this way, 

includes country code top\-level domains (cTLDs) 

the domain both initiates the establishment of a 

such as .uk, .ca, and .cn; generic top\-level domains 

communications channel with the victim and reveals 

(gTLDs) such as .com, .net, and org; and over 1,200 

the infected victim’s location. Knowing a victim’s 

new gTLDs that were introduced into the Domain 

location is important as cybercriminals use a myriad 

Name System (DNS) in 2013\. Due to the sheer 

of methods to disseminate their malware but are 

number of top\-level domains, and the growing 

unable to anticipate where it will ultimately be 

ecosystem of domain name registries, domain 

successfully downloaded. Therefore, cybercriminals 

registrars, and domain registration service providers, 

engineer their malware to “phone home” to a 

mitigating cyber threats from malicious domains 

malicious domain. Newly infected computers 

has been further complicated. Uniformity in cyber 

immediately reach out to such domains, effectively 

threat mitigation across the ecosystem is critical. 

“announcing” their location via IP addresses. There 

There is movement in this direction as evidenced 

are two primary ways domains are used for these 

by recent language incorporated into the Internet 

purposes in malware:

Corporation for Assigned Names and Numbers 

(ICANN) agreements with registries, which includes 

Domains aid in obfuscating and hiding the 

terms of use that define and prohibit illegal activity, 

cybercriminals’ location and identity

and a requirement for registries to develop their 

Domains directly added to malware (or “hard\-

own anti\-abuse policy and monitor and address 

coded” domains) and incorporated into the 

Domains can be a mechanism to build resiliency 

into the infrastructure

Cybercriminals are now routinely adding domain 

generating algorithms (DGAs) to their malware, 

providing a fallback mechanism for when hard\-

coded malicious domains are seized by law 

enforcement, for example. To utilize DGAs, malicious 

software includes code to generate lists of domains 

built using random characters or strings that change 

based on the day, time, and year. For example, 

on Friday, June 4, 2022, the DGA might generate 

three domains, such as ahu3rrfsirraqrty.com, 

hyrssgu5oqr4cetc.com, and wkcclsoqqpcaty.com, 

and the malware would attempt to contact those 

domains in that order. The use of DGAs increases 

the cost and complexity of disrupting cybercriminal 

communications infrastructure, requiring disruptors 

to monitor hundreds of thousands of potentially 

malicious domains, whereas the cybercriminal needs 

only one of them.

fraudulent technical support sites.

abusive activity.

communications infrastructure can effectively hide 

the cybercriminal’s true location. The cybercriminal 

sets up a domain as a proxy, or “stepping\-stone,” 

which redirects the communications with a victim 

to another domain or IP. This process can consist 

of multiple “hops” spanning domains associated 

with top\-level domains from around the world. It is 

common for cybercriminals to use fictitious names, 

emails, and addresses and pay for the domains with 

stolen credit cards or non\-traceable digital currency. 

38

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Disrupting malicious domain 
infrastructure 

Disrupting domains on Microsoft\-hosted services 

Cybercriminals are now increasingly abusing 

Microsoft and third\-party clouds as well as the 

services information workers and consumers use for 

day\-to\-day collaboration (such as email). Microsoft 

takes numerous steps to reduce cloud hosting 

abuse. We proactively detect abuse of the Microsoft 

cloud at the hosting source and neutralize it before 

attacks start or scale; we act on detections in our 

services (as in Office 365 email) and route this 

knowledge to internal services that can neutralize 

the threat; we act on customer and third\-party 

reports; and we notify third\-party industry partners 

of abuse on their cloud, detected by using our 

security services, so they can act to neutralize it 

at their hosting source. In the three\-month period 

between May and July 2021, we disabled roughly 

15,850 phishing sites hosted on Azure. We closely 

monitor abuse and evaluate new ways to detect and 

neutralize hosting of malicious sites

Disrupting third\-party\-hosted domains through 

Pursuing the appropriate remedy is an essential 

legal action 

component of an effectively disruptive legal action. 

Given that cybercriminals are increasingly deploying 

A well\-crafted injunction that relies on the broad 

private technical infrastructure, including malicious 

equitable authority of federal courts enables 

domains, to carry out a wide range of cybercrime, 

plaintiffs to obtain flexible court orders permitting 

it is incumbent on organizations and individuals 

them to exercise control over the cybercrime 

to establish the necessary legal and technical 

infrastructure. To obtain such relief, plaintiffs 

capabilities to disrupt this infrastructure through 

frequently invoke statutes that support seizure of 

legal actions.

physical devices, computers, and servers used for 

criminal purposes. Malicious domains engaged in 

In recent years, the private sector has used a variety 

criminal activity can also be subject to seizure under 

of legal theories to pursue disruption through 

various federal statutes and equitable theories. In 

civil actions in federal court. Criminal statutes 

several civil cases, federal courts have granted this 

directed at hacking and unlawful access frequently 

sort of injunction for violations of the CFAA, the 

provide a civil cause of action to target malicious 

Electronic Communications Privacy Act, the Lanham 

infrastructure. In particular, the Computer Fraud and 

Act, and common law claims. These legal claims 

Abuse Act (CFAA), the Wiretap Act, and the Stored 

also support court orders that direct transfer or 

Communications Act are frequently asserted legal 

disablement of domains and/or IP addresses. In this 

theories. Very frequently trademark theories under 

scenario, courts grant the transfer or disablement 

the Lanham Act23 are asserted as cybercriminals 

of malicious infrastructure to a private plaintiff’s 

leverage trusted brands to deceive victims. In many 

control, and away from the control of defendants, 

cases, infringing domains provide the critical part of 

which effectively disrupts the technical capability of 

malicious technical infrastructure and often include 

cybercriminals to launch attacks and inflict harm.

The next big threat: “Forever” 
(blockchain) domains 

Blockchain domains are an emerging threat outside 

of regulation. Over the last two years, the adaptation 

of blockchain technology has skyrocketed across 

many business verticals. Real\-life applications of 

blockchain technology range from supply chain 

management, identity management, real estate 

contracts, and domain infrastructure. In recent 

years, we have observed blockchain domains 

integrated into cybercriminal infrastructure and 

operations. We first observed this on a large scale 

when investigating the Necurs botnet that reigned 

terror worldwide for years with its ability to send 

malicious spam, often with ransomware payloads. 

Necurs contained a robust backup system, which 

incorporated a DGA. In one of its DGA versions, 

Necurs produced 2,048 new domains from 43 

different TLDs approximately every 30 days, 

including the blockchain domain TLD “.bit.”

wholesale counterfeit reproduction of legitimate 

content to confuse victims and advance criminal 

schemes. 

FPO

Blockchain domains are an emerging 
threat outside of regulation.

23 15 U.S.C. §§ 1125(a)\-(c)

39

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Unlike traditional domains that are purchased 

Blockchain domains work differently and pose 

Big threats using blockchain domains

Investigating blockchain domains provides a unique 

through internet registrars operating through 

challenges from both a utilization and disruption 

The threat landscape of criminal infrastructure 

challenge because there is no central WHOIS 

the ICANN\-regulated DNS system, blockchain 

standpoint. Blockchain domains function either 

is constantly shifting to avoid detection and 

registration database tracking who registered the 

domains are not governed by any centralized body, 

through software/browser plug\-in or proxy 

disruption. Within the past year, some of the bigger 

domain and when. Fortunately, some blockchain 

limiting the opportunity for abuse reporting and 

resolution services. The challenge for cybercriminals 

threat actors on the internet have started utilizing 

DNS providers like Emercoin have provided access 

enforcement disruptions. 

with respect to blockchain domains is getting the 

blockchain domains as part of their infrastructure. 

to a block explorer tool,25 which enables a search for 

most updated IP address from the blockchain to the 

Trickbot, the notorious banking trojan which has 

domain names, transaction hashes, and other values 

Traditionally, blockchain domain purchases are 

computer trying to resolve the blockchain domain to 

evolved its business model into providing access 

that might be stored in the blockchain. The Emercoin 

made through a crypto wallet with cryptocurrency 

an IP address. Because blockchain domains operate 

to high\-value targets in the ransomware space, 

blockchain is pseudo\-anonymous but can reveal 

from a blockchain DNS provider. Crypto wallets 

outside the normal DNS channels, malware authors 

started using “.bazar” domains provided by 

some interesting information about a blockchain 

utilize asymmetric encryption, which involves both a 

must include additional resolution instructions 

Emercoin blockchain DNS. The more recent threat, 

domain, such as IP addresses and transaction dates.

private and public key for the blockchain transaction. 

for infected victims. These instructions are usually 

Bazarloader, which has connections to Trickbot, 

After the transaction has been executed, the domain 

hard\-coded into the malware and point the infected 

started deploying a unique version of its DGA 

name, domain IP, and transaction hash are recorded 

system to a blockchain proxy resolution service IP.

that uses “.bazar” domains. This trend of threats 

into the blockchain. Moving forward, the only entity 

leveraging blockchain domains as infrastructure 

that can make changes to the IP recorded on the 

Over the years, there have been several projects 

with the means to create an undisputable criminal 

blockchain is the person with the wallet and private 

on the internet to operate free unregulated DNS 

network should be taken seriously.

key who made the initial transaction to purchase the 

and support the resolution of blockchain domains. 

domain. 

Most recently, the OpenNic project, which operates 

under the mission statement of “DNS neutrality and 

provide uncensored DNS access,” took on the task 

of resolving “.bit” crypto domains. Several years into 

the project, because of reported widespread abuse 

of “.bit” domains, the OpenNic project decided to 

stop resolving “.bit” domains.24 

24 https://www.namecoin.org/2019/07/30/opennic\-does\-right\-thing\-shuts\-down\-centralized\-inproxy.html 25 https://explorer1\.emercoin.com/nvs

40

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Countering blockchain domains might not be as 

Blockchain domains have become a preferred choice for cybercrime infrastructure 

difficult as you think

The weakness in blockchain domains is the need 

for third\-party proxy services or browser plug\-ins 

to resolve blockchain domains to an IP. Disabling or 

blocking the blockchain proxy resolution services 

and disabling browser plug\-ins will disable the 

ability for blockchain domain resolution. Many threat 

intelligence vendors provide malicious URL feeds, 

which sometimes include blockchain resolution 

proxies or the blockchain domain itself.

41

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Adversarial 
machine 
learning

Machine learning (ML) is an artificial intelligence (AI) 

technique that can be used in numerous applications, 

including cybersecurity. In responsible ML innovation, 

data scientists and developers build, train, and 

deploy ML models to understand, protect, and 

control data and processes to build trusted solutions.

However, adversaries can attack these ML\-driven 

systems. The methods underpinning the production 

ML systems are systematically vulnerable to a new 

class of vulnerabilities across the ML supply chain 

collectively known as “adversarial ML.” Adversaries 

can exploit these vulnerabilities to manipulate AI 

systems and alter their behavior to serve a malicious 

end goal.

The adversarial ML threat 
matrix 

Microsoft worked with MITRE to create the 

Adversarial ML Threat Matrix because we believe the 

first step in empowering security teams to defend 

against attacks on ML systems is to have a framework 

that systematically organizes the techniques 

employed by malicious adversaries in subverting 

ML systems. We hope that the security community 

can use the tabulated tactics and techniques to 

bolster their monitoring strategies around their 

organizations’ mission\-critical ML systems.

1\. Primary audience is security analysts: 

We think that securing ML systems is an 

infosec problem. The goal of the Adversarial 

ML Threat Matrix is to position attacks on 

ML systems in a framework where security 

analysts can orient themselves in these new 

and upcoming threats. The matrix is structured 

like the ATT\&CK framework, owing to its 

wide adoption among the security analyst 

community. This way, security analysts have a 

familiar framework to learn about threats to 

ML systems, which are inherently different from 

traditional attacks on corporate networks.

2\. Grounded in real attacks on ML systems: 

We seeded this framework with a curated set 

of vulnerabilities and adversary behaviors 

that Microsoft and MITRE vetted to be 

effective against production ML systems, 

enabling security analysts to focus on realistic 

threats. We also incorporated learnings from 

Microsoft’s vast experience in this space into 

the framework. For instance, we found that 

model stealing is not the end goal of the 

attacker but in fact leads to more insidious 

model evasion. We also found that when 

attacking an ML system, attackers use a 

combination of traditional techniques like 

phishing and lateral movement alongside 

adversarial ML techniques.

Intentional failure modes in ML 

Microsoft has incorporated AI\- and ML\-specific 

security practices into its Security Development 

Lifecycle (SDL) to protect Microsoft products and 

services against these attacks. In addition to threat 

detection and mitigation development work and 

automation, we have published guidance on steps 

customers can take to build defense in depth into 

their own AI and ML systems.

The centerpiece of the materials we’ve published is 

called Failure Modes in Machine Learning,26 which 

lays out the terminology we developed jointly with 

the Berkman Klein Center for Internet and Society at 

Harvard University. It includes vocabulary that can 

be used to describe intentional failures caused by 

an adversary attempting to alter results or steal an 

algorithm, as well as vocabulary for unintentional 

failures such as a system that produces results that 

might be unsafe.

26 https://docs.microsoft.com/en\-us/security/engineering/failure\-modes\-in\-machine\-learning

42

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Attacks on ML models

Attack

Description

Example

Evasion attack

Attacker modifies the 
query in a way that causes 
a model misclassification.

Poisoning attack

Membership 
Inference

Attacker contaminates 
the training phase of ML 
systems to get intended 
result. The attacker wants 
to misclassify specific 
examples to cause specific 
actions to be taken or 
omitted.

Attacker can infer if a 
given data record was part 
of the model’s training 
dataset or not.

Model Stealing

Attacker is able to recover 
the model through 
carefully crafted queries.

Self\-driving cars 
By manipulating a stop sign, or the environment 
observed by the car’s image recognition system, 
the adversary causes a model misclassification. 
In this way, a self\-driving car could be made to 
ignore the stop sign. 

Critical infrastructure systems 
By submitting antivirus software as malware, 
an adversary can force its misclassification as 
malicious thereby eliminating the use of the 
antivirus software on client systems. This could 
leave critical infrastructure systems open to 
attack.

Healthcare information 
An adversary could look at a model trained on a 
body of data consisting of people with a specific 
surgical procedure. By knowing that a particular 
individual’s data was in the training set, an 
adversary would then know the individual had the 
surgical procedure. This privacy violation could 
then be leveraged publicly. 

Finance algorithms 
Through model queries, an adversary could 
reconstruct the potential outputs of the ML 
model. This could be used to adversely affect 
proprietary algorithms designed for high 
frequency stock trading in a particular market.

43

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Attacker evasions 

An evasion attack is an exploratory attack against 

an ML model to cause an integrity violation. From 

a system’s security perspective, it is instructive to 

consider black\-box evasion attacks, in which an 

attacker may have no specific knowledge of the 

inner workings of the ML model but instead effects 

change by submitting inputs and observing the 

corresponding system output. This threat model 

is common to many AI systems hosted as a cloud 

service or on a consumer device, for example, and is 

a concern for models in finance, healthcare, defense, 

fraud, and security.

As we’ve seen with security research into past 

vulnerabilities,27 a pronounced uptick in research 

publications is soon followed by active exploitation. 

In anticipation of such a shift to focus on data 

poisoning attacks, Microsoft continues to focus 

on designing threat detections and mitigations 

to protect ML models and their datasets against 

these threats. Mitigations in this space can also be 

beneficial to detecting non\-malicious training data 

drift, giving data scientists greater insight into the 

quality of their data over time and highlighting 

anomalies for investigation.

ML model/data poisoning 

We are seeing a trend shift in adversarial ML 

security research. While in past years there was a 

focus on highly visible model evasion attacks where 

the fragility of some ML models could be easily 

demonstrated, the focus of security researchers 

is broadening to include less noticeable attacks. 

For example, in data poisoning attacks, the target 

is the training data that the ML models are built 

from. As new data is aggregated and incorporated 

into a dataset for training, it becomes increasingly 

important to validate that new training data has not 

been compromised. We have evidence of customer 

ML model compromise resulting from adversarial 

contamination of training data which, when left 

undetected, becomes an equally trusted part of 

existing training datasets. Without automation 

measuring for statistical drift in growing datasets, 

these types of attacks largely go undetected until an 

ML model has a critical failure.

The risk of adversaries evading an 
ML model exists in every domain.

Sophisticated black\-box evasion attacks against 

ML models have been demonstrated repeatedly 

by white\-hat researchers by using algorithms that 

iteratively determine what input will cause an 

integrity violation. Today, however, threat actors in 

the wild may also attempt evasion of ML systems 

in some domains, but usually do so through 

manual rather than algorithmic means and do not 

necessarily focus exclusively on ML as the evasion 

target. For example, content moderation filters are 

bypassed by mischievous or economically motivated 

users by obscuring payload content in creative 

ways. Security products that include antimalware or 

antiphishing models are evaded by adversaries using 

several obfuscation techniques. That these target 

systems rely on ML is not necessarily a consideration 

in these practical manual evasion attacks.

Whether or not an adversary is present in your 

business domain, the risk of adversaries evading 

an ML model exists in every domain. An ML model 

is an imperfect summary of a dataset, and as 

such, models have intrinsic failure modes even 

when trained on an ideal dataset. It is generally 

understood that the feasibility of evasion is a 

property of all ML models, rather than a failure 

mode to which only a few are susceptible to. These 

integrity violations may rarely be encountered 

during nominal use of the ML model but can be 

readily discovered by an adversary who is explicitly 

optimizing for the worst\-case conditions necessary 

to cause them.

27 Such as MD5, SHA1, SSLv2/3, and TLS 1\.0

44

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Based on learnings from internal and external 

AI risk management

What we’re doing to stay ahead 
of the curve

Performing security assessments of production 

AI systems is not easy. Microsoft surveyed 28 

organizations,28 spanning Fortune 500 companies, 

governments, non\-profits, and small and medium\-

sized businesses, to understand the current 

processes in place to secure AI systems. We found 

that 25 out of 28 businesses indicated they don’t 

have the right tools in place to secure their AI 

systems and that security professionals are looking 

for specific guidance in this space.

To address the growing needs of adversarial ML, 

Microsoft released Counterfit, an open\-source 

tool to help assess risk by allowing users to attack 

their own AI/ML. This tool was developed out of 

our own need to assess Microsoft’s AI systems for 

engagements, Counterfit is designed to be flexible in 

three key ways:

1\. Environment agnostic: It can help assess AI 

models hosted in any cloud environment, on\-

premises, or on the edge.

2\. Model agnostic: The tool abstracts the 

internal workings of AI models so that security 

professionals can focus on security assessment.

3\. Strives to be data agnostic: It works on AI 

models using text, images, or tabular input, 

and we continue to add data types.

Learn more:

Our approach to responsible AI at Microsoft

GitHub – Azure/counterfit: a CLI that provides a 

generic automation layer for assessing the security of 

ML models

vulnerabilities and proactively secure AI services, 

AI security risk assessment using Counterfit Microsoft 

 \|

in accordance with our responsible AI principles29 

Security Blog 

(5/3/2021\)

and Responsible AI Strategy in Engineering (RAISE) 

Adversarial Machine Learning – Industry Perspectives 

initiative. Counterfit started as a corpus of attack 

(3/19/2021\)

scripts written specifically to target individual AI 

models and then grew into a generic automation 

tool to attack multiple AI systems at scale. Today, we 

routinely use Counterfit as part of our AI red team 

operations. 

Security is one part of a larger emphasis in a burgeoning market 
called “AI risk management” and includes “model operations”—
ensuring that your AI system is reliable, accurate and available. It also 
includes “responsible AI” with fairness, ethics, transparency and all 
the legal ramifications of having AI systems behave responsibly. This 
“security” element also deserves attention and is an important piece in 
rounding out a risk management posture.

28 2002\.05646\.pdf (arxiv.org) (March 2021\) 29 Responsible AI principles from Microsoft

45

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction The cybercrime economy and services Ransomware and extortion Phishing and other malicious email Malware Malicious domains Adversarial machine learning

Standards for addressing 
security of AI systems 

The prevalent use of AI and ML across industry 

sectors, an emerging regulatory landscape, and 

widespread mistrust or misunderstanding in the use 

of these technologies has led to an increased need 

for standards to define good practice and provide 

guidance to improve trust and market adoption. 

The International Organization for Standardization 

(ISO) and the International Electrotechnical 

Commission (IEC) are developing AI standards, 

including defining key terminology and concepts 

for AI and ML, risk management, governance 

implications, data quality, and various topics related 

to trustworthiness. Also under development is a 

certifiable management system standard for AI, 

which will guide organizations to adopt a risk\-based 

approach to responsibly use and develop AI systems 

as well as to demonstrate accountability and their 

duty of care toward stakeholders.

AI and ML are increasingly integrated into all 

AI security cannot be considered in isolation of 

Learn more:

types of systems, including critical and safety 

existing risk\-based security, privacy, and governance 

infrastructure, resulting in new security threats 

foundations, which can address many of the 

unique to the use of AI systems and highly 

threats that arise using AI systems. For example, 

undesirable consequences of attacks. Such 

using standards such as those for an information 

consequences can include the detrimental 

security management system (ISO/IEC 27001\) and 

performance of a chatbot, denial of essential 

a privacy information management system (ISO/

services, theft of intellectual property, or even 

IEC 27701\) can help an organization to implement 

physical danger to humans. In some instances, 

processes and controls to address security and 

security attacks on AI systems have already caused 

privacy risks associated with its objectives and 

significant issues. 

activities, including security threats to AI systems. 

In addition to these existing practices, this evolved 

threat landscape will require new guidance, good 

practices, and organizational and technical measures 

to help organizations protect their AI systems. 

Effective security measures are a vital component 

of responsible development and deployment of AI 

systems. Microsoft is engaged in new standards 

work that has been initiated to provide guidance for 

addressing security threats and failures in AI and ML.

Responsible AI principles from Microsoft

Threat Modeling AI/ML Systems and Dependencies 

– Security documentation Microsoft Docs, 

\|

(11/11/2019\)

AI/ML Pivots to the Security Development Lifecycle 

Bug Bar – Security documentation Microsoft Docs 

\|

(11/11/2019\)

Failure Modes in Machine Learning – Security 

 \|
documentation Microsoft Docs 

(11/11/2019\)

46

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

CHAPTER 3 

Nation state threats

Introduction

Tracking nation state threats

What we're seeing 

Analysis of nation state activity this year 

Private sector offensive actors 

Comprehensive protections required

47

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

INTRODUCTION: Attackers increase use of deception to 
pursue national objectives

JOHN LAMBERT, DISTINGUISHED ENGINEER AND VICE PRESIDENT, MICROSOFT TH REAT INTELLIGENCE CEN TER

The last year has been marked by significant historic geopolitical events and unforeseen challenges that have 
changed the way organizations approach daily operations. During this time, nation state actors have largely 
maintained their operations at a consistent pace while creating new tactics and techniques to evade detection 
and increase the scale of their attacks. 

Major cybersecurity events, like the SolarWinds 

nongovernmental organizations (NGOs), and think 

These sophisticated attackers continue to focus 

attacks by NOBELIUM and on\-premises Exchange 

tanks for traditional espionage or surveillance 

on effective techniques that help them maintain 

Server attacks by HAFNIUM, and attacks by multiple 

objectives. The victims of attacks often have 

stealth and access. We have seen continuing attacks 

other actors have focused our collective attention on 

information relevant to an adversary government’s 

on traditional security hygiene elements as well as 

securing our supply chains. Nation state actors and 

intelligence needs, which is why so many government 

focus on developing and refining new, breakthrough 

many cybercrime operations have focused efforts on 

agencies and think tanks are attacked. However, private 

attacks targeting the supplier ecosystem in order 

exposing security vulnerabilities among their suppliers 

industry’s role in supporting remote workers, increased 

to attack downstream customers. Well\-established 

or discovering unpatched systems that organizations 

healthcare services, COVID\-19 vaccine research, and 

spear phishing and password spray campaigns 

relied on for continuity of business during this unusual 

COVID\-19 vaccine distribution have also made them 

by nation state actors continue to be successful 

year. These recent events have demonstrated the 

more common targets for these sophisticated actors 

against organizations that have not yet implemented 

increasing importance in maintaining current security 

seeking information for their government’s national 

multifactor authentication (MFA) or other protections 

updates in all deployed systems as the most effective 

security or intelligence purposes. Our increased 

against this common tactic. However, as more 

way to protect against rapidly evolving threats.

reliance on the global telecommunications backbone 

organizations invest in securing their accounts, the 

and virtual private network (VPN)/virtual private server 

success rate of these techniques will decline, and 

The Microsoft Threat Intelligence Center 

(VPS) infrastructure for remote workers gave malicious 

detection of the attacks will increase. In response, 

(MSTIC) and the Digital Security Unit (DSU) have 

actors new vectors to gain access to targeted private 

nation state actors appear to be increasing the scale 

observed that most nation state actors continue 

networks that were scrambling to support new ways of 

and volume of these attacks to evade detection 

to focus operations and attacks on government 

doing business.

agencies, intergovernmental organizations (IGOs), 

and improve the likelihood of success across 

multiple targets. This volume\-oriented approach to 

NATION 

STATE ACTORS 

APPEAR TO BE 

INCREASING 

THE SCALE 

AND VOLUME 

OF ATTACKS 

TO EVADE 

DETECTION.

Microsoft Digital Defense Report \| October 2021

48
48

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

compromising credentials will continue to be a 

refining their techniques by leveraging new exploits 

are often unique, prompting deeper analysis and 

useful technique if poorly secured accounts are 

against security weaknesses and unpatched systems 

creation of customized detections. Understanding 

available as targets. Attacks against unpatched 

of common supply chain vendors in order to gain 

these TTPs also helps Microsoft better understand 

third\-party software or on\-premises infrastructure 

access to and collect information from downstream 

downstream actors such as cybercriminals and 

will likely become more pervasive and become more 

customers. Spear phishing and password spray 

smaller nation states who often copy or reuse these 

easily exploited by nation state and cybercrime 

attacks show no sign of slowing as the common 

methods. DSU focuses on the victims identified 

actors. Postponing installation of security updates 

method for reconnaissance and infiltration, 

by MSTIC, connecting the victims of the attack to 

or incomplete knowledge of deployed systems and 

increasing the importance of implementing end\-to\-

political objectives and stated intelligence goals 

their patch state will leave organizations vulnerable 

end MFA across accounts. The information Microsoft 

of governments to help Microsoft provide fuller 

to sudden large\-scale attacks as they scramble 

provides in this chapter captures much of the activity 

context to the world about why these nation state 

Nation state notifications

When a customer, whether it’s an organization 

or individual account holder, is targeted or 

compromised by nation state activities that 

Microsoft tracks, we deliver a nation state 

notification (NSN) to the customer. Over the past 

three years, Microsoft has delivered over 20,500 

NSNs. The charts and graphs in this chapter are 

derived from Microsoft’s NSN process.

to identify affected assets and catch up to a fully 

we have seen targeting our customers globally in 

attacks occur. 

patched state. Running networks with unsupported 

the past year and captures the trends we anticipate 

Countering nation state activity

software, or software that is no longer updated, 

nation state actors will continue to use in the next 

We focus on nation state activities regardless of 

Nation state actors are generally well\-resourced 

increases risk exponentially. Organizations must 

year. We recommend you use this information as a 

platform, targeted victim, or geographical region, 

and capable adversaries. As noted above, they are 

maintain comprehensive asset inventory, patch state 

guide to understanding the tactics and techniques 

and we maintain visibility and active threat hunting 

often pursuing intelligence collection against targets 

awareness, and thorough backup and containment 

that these sophisticated actors may use to target 

worldwide to write better detections for our 

of interest to their governments. Our relentless 

plans to be resilient against sophisticated attacks. 

your organizations so you can more effectively 

customers. We also analyze why nation state actors 

pursuit of these adversaries and our continuous 

Adversaries will continue to evolve new techniques 

implement proactive defense.

are pursuing particular victims, sectors, or regions. 

development of new capabilities to detect and deter 

to target and compromise corporate resources 

requiring a comprehensive “assume breach” 

mentality that extends beyond basic hygiene needs 

and MFA and into a holistic set of Zero Trust security 

principles. Applying a Zero Trust security model32 will 

become increasingly critical in protecting corporate 

identities, devices, applications, data, networks, and 

infrastructure against sophisticated threats.

Looking forward, we know that adversarial 

governments will continue with their intelligence 

collection objectives, as well as explore the political 

boundaries of acceptable behavior in cyberspace. As 

a result, we expect nation state actors to continue 

32 Zero Trust Security Model and Framework Microsoft Security

\| 

Tracking nation 
state threats

Microsoft tracks nation state activities to protect 

our customers and our platforms and services. 

We use a variety of metrics and sophisticated 

data integration techniques to better understand 

targeting, motivations, and customer impact. MSTIC 

focuses on nation state actor activities because 

these tactics, techniques, and procedures (TTPs) 

often have significant impact on our customers and 

Putting it all together, the information presented 

malicious activity supports our commitment to 

here provides a snapshot of our defensive efforts 

customer protection. We are constantly improving 

on behalf of our affected customers. It is important 

our capability to understand nation state actors 

to note that even if a particular industry sector 

and their victims to help bring better context and 

or geographic region is not represented in the 

understanding to our customers. 

following information, nation state activity spans 

nearly every industry sector and geographic region. 

In other words, protections against these tactics are 

critical for every organization and individual. Our 

intelligence is impacted by the degree to which our 

products and platforms are utilized in a particular 

geography or sector. 

49

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Our approach 

Microsoft uses a five\-pronged approach to disrupt 

nation state actors—providing direct customer 

notifications, leveraging technology to detect and 

defend, taking technical action against malicious 

operations, pursuing legal action, and participating 

in public policy discourse—and each one plays an 

important role in our commitment to protecting our 

customers and the ecosystem at large.

1\. Empowering customers

Microsoft leverages its NSN process to inform 

customers of targeting or compromise from 

nation state actors we track, providing actionable 

information for customers to rapidly respond and 

protect themselves. Microsoft also provides alerts 

to industry sectors and customer segments to help 

raise awareness of malicious activity and guidance 

on how to respond.

2\. Leveraging technology

4\. Digital Crimes Unit

Microsoft’s cumulative knowledge of the global 

One of Microsoft’s unique resources in the fight 

threat landscape enables our products and services 

against nation state actors is the Digital Crimes 

to constantly create and update new security 

Unit (DCU). Using litigation to seize domains and 

product detections, helping to protect and defend 

assets used by nation state actors against Microsoft 

against nation state activities at scale. These 

customers, the DCU has been instrumental in 

collective defenses represent the most effective 

shutting down those attack vectors. These cases 

method to counter nation state threats, as they 

have led to the takedown of hundreds of domains 

are informed by the extensive threat intelligence 

and the protection of thousands of customers, and 

resources built into each product and enabled by 

Microsoft remains one of the only companies willing 

world\-class engineering.

to pursue legal action against nation state actors 

in order to seize infrastructure and disrupt attacks. 

3\. Taking technical action against malicious 

Lessons learned from the cases are shared with 

operations

Microsoft engineering teams to help improve our 

From time to time, Microsoft will have sufficient 

operational and technical disruption capabilities.

information to warrant a one\-time deletion or 

shutdown of infrastructure or assets associated with 

5\. Informing public discourse and policy

a nation state attacker. By taking proactive action 

Microsoft uses its voice to raise awareness about 

against malicious infrastructure, the actor loses 

nation state activities, highlighting the context and 

visibility, capability, and access across a range of 

impacts of the incidents and sharing context about 

assets previously under their control, forcing them 

attacks and why they matter to the world. This helps 

Guide to the nation state actors 
discussed in this report 

Throughout this chapter, we cite examples of nation 

state actors to provide a deeper view into attack 

targets, techniques, and analysis of motivations. 

Microsoft identifies nation state activities by 

chemical element names, just some of which are 

shown in the following table together with the 

countries of origin from which the actors operate. 

This small sample of the total nation state actors 

tracked by Microsoft represents those that were 

most active in the last year and made most effective 

use of the tactics detailed in this chapter.

Microsoft also tracks and investigates many 

malicious activities that are either new or unknown 

in origin to develop a full understanding of the 

tactics, techniques, and objectives.

to rebuild.

When we take proactive action against malicious 
infrastructure, the actor loses visibility, capability, 
and access across a range of assets previously 
under their control, forcing them to rebuild.

drive a broad discussion about what can be done 

to combat malicious nation state activities across 

government entities, NGOs, enterprises, academia, 

and the public. Talking publicly about nation state 

attacks is an important part of deterrence.

50

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Sample of nation state actors and their activities

51

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

What we're 
seeing 
Nation state targets

Iran has been the only nation state actor willing 

Nation state actors from North Korea added a 

Although SolarWinds and the Exchange vulnerability 

to regularly engage in destructive attacks, mostly 

third motive to their cyberattacks: monetary gain. 

were the two main cybersecurity stories of the 

against Israel. These cyberattacks happened within 

North Korea targets companies in cryptocurrency 

year, Iran and North Korea also used similar tactics 

a political environment in which both countries 

trade or related research, likely seeking either to 

of targeting IT providers to find creative ways to 

were trading blows just short of military strikes, 

steal cryptocurrency or intellectual property. North 

exploit their real targets. For example, North Korean 

including attacks on one another’s cargo ships. 

Korea’s economy is never strong, but the COVID\-19 

actor ZINC created online personas of apparent 

In the 2020 Microsoft Digital Defense Report, 

we identified common aims (espionage, 

disruption/destruction) and common techniques 

(reconnaissance, credential harvesting, malware, 

With tensions already so high, the decision to use 

pandemic coming after years of UN sanctions has 

cybersecurity experts, including websites and social 

cyber for destructive attacks was less of a strategic 

pushed it to its worst state in a generation, forcing 

media pages, and used these personas to approach 

leap for Iran than it would have been for North 

North Korea to seek to find money by any means 

experts in cybersecurity vulnerabilities in an attempt 

Korea, Russia, or China. While nations other than 

necessary. Although Iranian nation state actors 

to get the researchers they corresponded with to 

and virtual private network (VPN) exploits) prevalent 

Iran mostly refrained from destructive attacks, they 

frequently used ransomware attacks, Microsoft 

open content that would have downloaded exploits 

among major nation state cyber actors. These 

did continue to compromise victims that would be 

assesses that the ransomware was used more for 

onto their machines. While this was not a direct 

aims and techniques were as prevalent this year 

prime candidates for destructive attacks if tensions 

covering the tracks of the attackers than for profit.

attack on an IT company like SolarWinds, it did 

as the year before. Tried\-and\-true methods such 

increased to the point where governments made 

represent an attempt to indirectly find avenues to 

as large\-scale spear\-phishing campaigns were 

strategic decisions to escalate cyber warfare. 

Targeting of IT companies is the big story of last 

compromise North Korea’s actual targets by going 

still valuable tools in the kits of hackers. However, 

year

through the experts responsible for finding ways to 

attackers worldwide, either affiliated directly with 

The “Most targeted sectors” chart in this chapter 

A more revolutionary change, one common among 

protect them.

governments or with more loose connections, are 

section shows that nearly 80% of those targeted 

all of the Big Four nation state cyber programs, has 

continuing to perform research against targets in 

were either in government, NGOs, or think tanks. 

been the decision to target IT service providers 

For more information on supply chain security, see 

order to be more convincing in an attack, develop 

Think tanks often serve as policy incubators and 

in order to more successfully exploit victims 

the Supply chain, IoT, and OT security chapter of this 

new techniques that have not been seen before, 

implementers, with strong ties to current and former 

downstream who receive services from those 

report.

or even mimic criminal behavior in an attempt to 

government officials and programs. Threat actors 

IT providers. The most glaring examples of the 

obfuscate intent and objective. Microsoft responds 

can and do exploit the connections between the 

use of this kind of strategy from the last year are 

by also working to improve our ability to keep up 

more traditional NGO community and government 

the Russian SolarWinds attacks and the Chinese 

with the changes.

organizations to position themselves to gain insights 

exploitation of a vulnerability in on\-premises 

into national policy plans and intentions. As noted, 

Microsoft Exchange servers. These attacks are both 

Espionage more prevalent than destructive 

it’s the think tanks with ideas relevant to current or 

covered in detail in the sections on Russia and 

attacks

future government policy or political objectives that 

China.

The two main goals of nation state actors have not 

put these organizations into the line of sight for 

changed either. In the last year, espionage, and 

intelligence operations. When traditional NGOs have 

more specifically, intelligence collection, has been 

similar information, we also see them as an objective 

a far more common goal than destructive attacks. 

for nation state actors. 

52

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Most targeted countries (July 2020\-June 2021\)

Most targeted sectors (July 2020\-June 2021\)

Consumer versus enterprise targets (July 2020\-June 2021\)

Organizations in the United States remained the target of most of the 

Every threat actor we tracked this year targeted entities within the 

It is likely that threat actors thought consumer email accounts could 

observed activity this year. We also noted targeting increases consistent 

government sector. NOBELIUM, NICKEL, THALLIUM, and PHOSPHORUS 

be an easier way to gain access to targeted networks during the 

with increasing geopolitical tensions between nations. Russia\-based 

were the most active against this sector from the Big Four threat 

global move to remote work. Separate from enterprise targets and the 

NOBELIUM raised the number of Ukrainian customers impacted from 

countries. Government sector targeting largely focused on ministries 

industries they represented, consumer accounts received the second 

six last fiscal year to more than 1,200 this year by heavily targeting 

of foreign affairs and other global government entities involved in 

highest number of notifications this year. THALLIUM and PHOSPHORUS 

Ukrainian government interests involved in rallying support against a 

international affairs. (This chart excludes consumer accounts and depicts 

invested heavily in spear\-phishing campaigns targeting these accounts.

build\-up of Russian troops along Ukraine’s border. This year marked 

only enterprise targets’ corresponding sectors.)

a near quadrupling in targeting of Israeli entities, a result exclusively 

of Iranian actors, who focused on Israel as tensions sharply escalated 

between the adversaries.

53

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Critical infrastructure versus noncritical infrastructure targets

threat actors displayed the most interest and Russia\-based threat actors 

of displaying Russia’s interest in conducting operation for access and 

From July 2020 to June 2021, critical infrastructures were not the focal 

accounted for the least in targeting entities in the critical infrastructure 

intelligence collection versus targeting a critical infrastructure for 

point according to the NSN information that was tracked. China\-based 

sector. Russian NOBELIUM’s cyber operations are a perfect example 

potential disruption operations.

Targeting critical versus noncritical infrastructures (PPD\-21\)(July 2020–June 2021\)

Russia’s targeting of critical infrastructures 

China’s targeting of critical infrastructures

Iran’s targeting of critical infrastructures

North Korea’s targeting of critical infrastructures

Combination of China, Iran, North Korea, 
and Russia’s targeting of critical infrastructures

54

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Compromised versus targeted success rate

Success rates varied widely from threat group to threat group. Some 

groups, like North Korean THALLIUM, had a low success rate, because 

they used strategies like large\-scale spear\-phishing campaigns that 

rely more on using a wide net than a surgical strike. Password sprays 

are another example of a tactic with a low success rate, but where the 

attackers understand the success rate will be low. Other groups use very 

focused attacks that succeed much more often. HAFNIUM, for example, 

succeeded in 43% of its attacks. NICKEL succeeded at an astonishing 

rate of over 90%. The figures below represent an average of different 

tactics that are designed to succeed at different rates. The first quarter 

was extremely high, not necessarily because actors were more successful 

that quarter, but because Microsoft noted less activity stemming from 

low\-success\-rate attacks. 

Compromise rate (July 2020\-June 2021\)

Activity origins

The following section depicts the frequency of attacks by country of 

origin, measured in the number of NSNs generated from attacks by 

each actor. Russia\-based threat activity dominated this year, driven 

by NOBELIUM’s large\-scale targeting. North Korea–based actors also 

employed a strategy of ubiquitous targeting that earned North Korea 

the second highest percentage of notifications.

Country of activity origin

NOBELIUM, and its aggressive targeting of IT service providers and 

Western government institutions, catapulted Russia to the top spot for 

countries where attacks originated this year. That group was responsible 

for 92% of the notifications to customers about Russia\-based threat 

activity. The outsized proportion of attacks coming from North Korea is 

a result of the strategy taken by threat actors THALLIUM and CERIUM. 

These groups rely on large quantities of attacks. While these attacks 

have a low percentage of success, because of the high number of 

attempts, the groups still manage to successfully infect some victims.

Attacks by country of origin (July 2020\-June 2021\)

Most active nation state activity groups

Like the “compromised versus targeted” section above, the data in this 

section is heavily affected by the tactics chosen by the attackers. If one 

group attempts a password spray attack on a hundred targets and 

successfully compromises one, while another group surgically focuses 

on only one victim that it compromises, they have both had the same 

number of successes. However, the first group will appear as the more 

“active” group, because it has attacked a hundred targets. The top three 

groups in this list all make use of high\-fail\-rate tactics. NOBELIUM, in 

addition to high\-success\-rate\-focused attacks, also makes frequent use 

of low\-success password sprays, while THALLIUM and PHOSPHORUS 

send spear\-phishing emails to large groups. This chart, then, does not 

necessarily equate to the most dangerous groups, although it does say 

something about their relative levels of persistence and ubiquity.

Most active nation state activity groups (July 2020\-June 2021\) 

55

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Nation state attacker tools 

It is often the case that nation state actors develop 

Attack vectors used by nation state malicious actors

The tools used by nation states to compromise 

and refine new attack techniques and that criminals 

victim networks are most frequently the same 

adopt and further refine them over time. Microsoft 

tools used by other malicious actors. To achieve 

expects tools designed to target and compromise IT 

their objectives, nation state actors may create 

supply chains to enter the mainstream and become 

or leverage bespoke malware, construct novel 

more common, making concepts like Zero Trust 

password spray infrastructure, or craft unique 

architecture a priority from software development 

phishing or social engineering campaigns. However, 

through deployment and updating. Well\-funded 

actors like GADOLINIUM are also increasingly 

nation state actors will continue to create unique 

turning to use open\-source tools33 or common 

tools to achieve their objectives, but just like any 

malware to impact a supply chain, attempt a man\-

other streamlined organization, are just as likely 

in\-the\-middle attack, or launch a denial\-of\-service 

to use common tools where they can to improve 

attack. These methods allow malicious actors to 

efficiency and effectiveness.

Learn more:

Protecting customers from a private\-sector offensive 

actor using 0\-day exploits and DevilsTongue malware 

\| 

Microsoft Security Blog

 (7/15/2021\)

obfuscate their actions by hiding in plain sight. 

Increased use of open\-source tools provides some 

advantages for security professionals responsible 

for detecting and defending against these attacks. 

Increasingly, the same security and computer 

hygiene routines that protect from ordinary threats 

also help protect from nation states. Training 

employees to be skeptical can go a long way to 

stopping spear\-phishing attacks and thwarting the 

common methods that Microsoft sees in the early 

stages of a compromise.

Nation states are advanced enough to do reconnaissance on their victims and select the 
attack method that best suits each goal or intended outcome.

33 GADOLINIUM threat actors use cloud services and open source tools in cyberattacks \- Securezoo Blog

56

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Analysis of 
nation state 
activity 
this year 

Evolving nation state cybersecurity threats have 

produced a watershed year with an increased 

focus on on\-premises servers and the exposure of 

in software. The scope, sophistication, and success 

also developed target\-specific capabilities for 

of HAFNIUM’s 0\-day exploits for on\-premises 

on\-premises infrastructure of foreign and defense\-

Exchange servers in early 2021 and NOBELIUM’s 

related entities in Europe, marking a shift from the 

compromise of SolarWinds’ network management 

predominant cloud\-first, cloud\-only operations the 

software in late 2020 caught the world’s attention, 

group was known for in 2019 and 2020\. Multiple 

although the nation state threat extended beyond 

Iranian actors also likely conducted supply chain 

those immediate incidents. For one, Russia\-based 

operations, including one in early 2020 that likely 

NOBELIUM and China\-based HAFNIUM’s targeting 

sought intelligence from government agencies 

of on\-premises resources and dumping credentials 

indirectly through IT and engineering services 

in those operations would have allowed them the 

companies that support US defense and intelligence 

opportunity to seize credentials to access and pivot 

agencies.

widespread supply chain vulnerabilities, most acutely 

to cloud\-based resources. Russia\-linked STRONTIUM 

Russia

Over the past year, Russia\-based activity groups have 

solidified their position as acute threats to the global 

digital ecosystem by demonstrating adaptability, 

persistence, a willingness to exploit trusted technical 

relationships, and a facility with anonymization and 

open\-source tools that make them increasingly 

difficult to detect and attribute. They have also 

shown a high tolerance for collateral damage, which 

leaves anyone with connections to targets of interest 

vulnerable to opportunistic targeting.

Activity 
Group Name

Other 
names 

Country 
of origin

Industries 
targeted

Russia

STRONTIUM

APT28, Fancy Bear

Russia

Government, diplomatic and defense entities, think tanks, NGOs, higher 
education, defense contractors, IT software and services

NOBELIUM

UNC2452

Russia

Government, diplomatic and defense entities, IT software and services, 
telecommunication, think tanks, NGOs, defense contractors

BROMINE 

Energetic Bear

Russia

Government, energy, civil aviation, defense industrial base

57

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Abusing supply chain and other trusted technical 

of the SolarWinds compromise and the targeting 

In summer and fall 2020, STRONTIUM deployed an 

relationships

picture of NOBELIUM’s activity through June 2021 

automated password spray/brute forcing tool that 

NOBELIUM targets by industries/verticals 
(December 2020\-Jan 2021\) 

Russia\-based NOBELIUM proved how insidious 

highlights the tactical shifts and multi\-vectored 

ran through more than a thousand anonymized Tor 

and devastating software supply chain attacks can 

approach the threat group employs to gain access to 

IPs,38 making it large scale and hard to detect and 

be with its compromise of the SolarWinds Orion 

desired systems. The first chart depicts victims that 

attribute. The tool was deployed multiple times 

software update. Although the group limited follow\-

were subject to high\-touch threat actor exploitation 

against more than 40 political organizations and 

on exploitation to roughly 100 organizations, its 

that in some cases leveraged the supply chain 

advocacy groups based in the United States and the 

malicious backdoor malware was pushed to roughly 

backdoor access. The second chart reflects the mass 

UK in the run\-up to, and immediately after, the US 

18,000 entities worldwide, leaving those impacted 

spear\-phishing and password spray campaigns the 

presidential election.

customers vulnerable to further attack. 

actor used against targeted organizations in the first 

half of 2021\. We can see NOBELIUM consistently 

Achieving higher rates of compromise and 

NOBELIUM’s operational techniques were much 

targeted the government, NGO, IT services, and 

targeting more government organizations

more diverse than just the malicious backdoor 

professional services sectors (included in “Other” 

Over the past year, Russia\-based groups have 

and ranged from password spray and phishing to 

in the latter chart), but the volume of compromise 

improved their rates of successful compromise and 

compromise of third\-party providers to facilitate 

attempts fluctuated in line with the tactical changes.

increasingly set their sights on government targets, a 

future attacks. The actor targeted cloud solution 

confluence of trends that could portend more high\-

providers (CSPs) and leveraged the backdoor to steal 

Using a range of techniques to evade detection 

impact compromises in the year ahead. Year\-on\-year 

a Mimecast private key. NOBELIUM went on to target 

and attribution

comparisons of NSN data depict a marked increase 

downstream customers by masquerading as those 

Russian actors demonstrated varying degrees of 

in successful compromises, from 21% successful 

CSPs and as the legitimate Mimecast app.34 In May, 

adaptability and security consciousness that helped 

between July 2019 and June 2020 to 32% since July 

the group compromised a US government agency’s 

them evade attribution and network defenses. 

2020\. The percentage of government organizations 

account at a popular email marketing service, 

NOBELIUM showed a deep knowledge of common 

among Russian targets exploded from roughly 3% 

cloaking malicious components behind the service’s 

software tools, network security systems, and cloud 

last period to 53% since July 2020\.

legitimate URL to send a phishing email to more 

technologies, as well as remediation methods 

Russian threat actors will follow targets wherever 

than 150 diplomatic, international development, and 

incident response teams use, and they changed their 

they are, be it in the cloud or on\-premises. This past 

nonprofit organizations mostly in the United States 

operations accordingly to maintain persistence.36 

year, STRONTIUM pivoted to more on\-premises 

and across Europe.35 

Responder surveillance was a tactic employed by 

targeting, developing target\-specific capabilities 

Comparing the distribution of NOBELIUM victims 

past.37 

identified in the first few months after discovery 

and defense\-related entities in Europe. This strategy 

was a change from the predominant cloud\-first, 

another Russian threat group, YTTRIUM, in the 

against on\-premises infrastructure of foreign policy 

NOBELIUM targets by industries/verticals 
(January\-June 2021\)

NOBELIUM: Variable target picture reflects diversity 
of tactics.

34 https://www.usnews.com/news/technology/articles/2020\-12\-24/solarwinds\-releases\-update\-to\-flagship\-software\-after\-hack ; https://www.msn.com/en\-us/news/technology/mimecast\-reveals\-source\-code\-theft\-in\-solarwinds\-hack/ar\-BB1eInqC 

35 https://blogs.microsoft.com/on\-the\-issues/2021/05/27/nobelium\-cyberattack\-nativezone\-solarwinds/ 36 https://www.microsoft.com/security/blog/2021/03/04/goldmax\-goldfinder\-sibot\-analyzing\-nobelium\-malware/ 37 https://www.youtube.com/

watch?v\=Ldzr0bfGtHc 38 https://www.microsoft.com/security/blog/2020/09/10/strontium\-detecting\-new\-patters\-credential\-harvesting/

58

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

cloud\-only operations the group was known for 

port authorities. The healthcare industry was the 

at organizations on almost every continent this 

and UK—were on the “unfriendly countries” lists. 

throughout 2019 and into 2020\.

third most targeted sector this period, fueled by 

period, but they predominantly focused on 

Microsoft’s observations of Russian threat activity 

STRONTIUM’s credential harvesting attempts against 

organizations based in the United States, followed 

this past year suggest that intelligence collection 

For the first time since August 2018, government 

organizations developing and testing COVID\-19 

by Ukraine, UK, and NATO allies and member states 

was a primary motivation, as we saw data exfiltration 

organizations were the most targeted sector for 

vaccines and treatments40 in the United States, 

across Europe. On May 14, the Russian government 

but little evidence of disruptive or destructive activity 

Russian threat actors Microsoft tracks, followed by 

Australia, Canada, Israel, India, and Japan through 

officially named the United States and Czechia 

from the groups we track. Gaining information on 

think tanks. The government organizations were 

summer 2020\.

“unfriendly” countries, while Poland, Lithuania, 

the policy plans and intentions of those perceived 

largely involved in foreign policy and national 

Latvia, Estonia, UK, Canada, Ukraine, and Australia 

as adversaries would be standard intelligence 

security or defense, although threat actor BROMINE 

Seeking intelligence on the United States and 

appeared on a preliminary list leaked in April.41 

requirements for the Russian government agencies 

concentrated its efforts against US state, county, 

Europe

The top three countries most impacted by Russian 

to whom the US government attributes much of this 

and city governments, as well as aviation and 

Russian threat actors attempted to access accounts 

cyber activity this past year—United States, Ukraine, 

activity.42

What lessons might NOBELIUM have 
learned from the SolarWinds incident? 

1\. The US Government is still not sure where the red lines are for cyber operations. 

As a sign of the ongoing debate within US and European policy communities about whether 

and how to respond to the SolarWinds breach, in March a former senior adviser to Britain’s 

Government Communications Headquarters cautioned the Biden administration not to react 

too harshly to Russia’s “surgical” espionage campaign.39 Russian threat actors have exploited 

this policy ambiguity for years and could continue to do so for years to come. 

2\. The private sector is critical to the defense of US government networks. 

Microsoft and FireEye were the public face of incident response during the SolarWinds 

attack. In the future, NOBELIUM and other groups could move early to handicap high\-

profile cybersecurity teams, anticipating that doing so will slow the time to identification and 

remediation of intrusions against high\-value targets.

Information accessed

Operational aim

• Sanctions policy
• Defense/intelligence policy
• Russia policy
• COVID\-19 information

Espionage to gain policy insights

• Cyber incident response; threat hunting techniques
• Assessments of Russian threat actors
• Red Team tools
• Detection signatures
• Source code

Intelligence collection to improve 
countermeasures

• CSP accounts
• Software certificates
• Source code

Intelligence collection to support operational 
planning

Examples of the types of information NOBELIUM operators may have acquired, based on the victim 
accounts they accessed, and the operational aims that likely drove the intrusion.

39 Top Biden cyber official: SolarWinds breach could turn from spying to destruction 'in a moment' (yahoo.com) 40 https://blogs.microsoft.com/on\-the\-issues/2020/11/13/health\-care\-cyberattacks\-covid\-19\-paris\-peace\-forum/ 41 https://tass.com/

politics/1289825 ; https://www.newsweek.com/russia\-puts\-us\-top\-unfriendly\-countries\-list\-1586749 42 https://www.nsa.gov/News\-Features/Feature\-Stories/Article\-View/Article/2573391/russian\-foreign\-intelligence\-service\-exploiting\-five\-publicly\-

known\-vulnerabili/ ; https://media.defense.gov/2021/Apr/15/2002621240/\-1/\-1/0/CSA\_SVR\_TARGETS\_US\_ALLIES\_UOO13234021\.PDF/CSA\_SVR\_TARGETS\_US\_ALLIES\_UOO13234021\.PDF ; https://home.treasury.gov/news/press\-releases/jy0127

59

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

China

Over the past year, Microsoft observed Chinese 

nation state threat actors target the US political 

landscape for insight into policy shifts and target 

government entities that enact foreign policies 

in Europe and Latin American countries likely for 

intelligence collection. To accomplish their mission, 

several China\-based threat actors exploited a range 

of previously unidentified vulnerabilities for different 

services and network components.

The following charts illustrate activity by China\-

HAFNIUM, a group assessed to be state sponsored 

they’ve gained access to a victim network, 

based threat groups in July 2020–June 2021 

and operating out of China, based on observed 

HAFNIUM typically exfiltrates data to file sharing 

based on NSNs issued to customers. These charts 

victimology, tactics, and procedures, primarily 

sites like MEGA. In campaigns unrelated to these 

represent only a portion of the threat actors’ 

targets entities in the United States across a number 

vulnerabilities, Microsoft has observed HAFNIUM 

activities observed.

of industry sectors, including infectious disease 

interacting with victim Office 365 tenants. While they 

researchers, law firms, higher education institutions, 

are often unsuccessful in compromising customer 

HAFNIUM and the Exchange vulnerabilities 

defense contractors, policy think tanks, and NGOs. 

accounts, this reconnaissance activity helps the 

In early March 2021, Microsoft blogged about 

HAFNIUM has previously compromised victims by 

adversary identify more details about their targets’ 

HAFNIUM for the first time related to the detection 

exploiting vulnerabilities in internet\-facing servers 

environments. HAFNIUM operates primarily from 

of multiple 0\-day exploits being used to attack on\-

and has used legitimate open\-source frameworks, 

leased virtual private servers in the United States.

premises versions of Microsoft Exchange Server.43 

like Covenant, for command and control. Once 

Activity 
Group Name

Other 
names 

Country 
of origin

Industries 
targeted

China

MANGANESE

APT5, Keyhole Panda

ZIRCONIUM

APT31

HAFNIUM

– – –

NICKEL

APT15, Vixen Panda

CHROMIUM

ControlX

China

China

China

China

China

Communications infrastructure, defense industrial base, software/technology

Government agencies and services, diplomatic organizations, economic 
organizations

Higher education, defense industrial base, think tanks, NGOs, law firms, 
medical research

Government agencies and services, diplomatic organizations

Energy, communications infrastructure, education, government agencies and 
services

GADOLINIUM

APT40

China

Maritime, healthcare, higher education, regional government organizations

43 https://www.microsoft.com/security/blog/2021/03/02/hafnium\-targeting\-exchange\-servers/

60

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

China: Top five targeted industries/sectors 
(July 2020\-June 2021\)

China: Target attempts vs successful 
compromise (July 2020\-June 2021\)

HAFNIUM: Top targeted industries/verticals 

(Prior to the increase in Exchange Server exploitation)

The most prevalent targets of China\-based threat activity 
were government entities worldwide. The targeting of 
three countries’ government entities accounted for half 
of the NSNs issued and 23 countries accounted for the 
remaining half.

Chinese nation state threat actors were successful in 
compromising victims 44% of the time. However, because they 
are an advance persistent threat, if they are tasked to target 
an entity for intelligence collection, they will find another 
vulnerability to leverage to gain access.

HAFNIUM used these vulnerabilities to access on\-

access. Second, they deployed web shells on the 

premises Exchange servers, which enabled access to 

compromised server. Web shells potentially allow 

email accounts and allowed installation of additional 

attackers to steal data and perform additional 

malware to facilitate long\-term access to victim 

malicious actions that lead to further compromise. 

environments. MSTIC attributes this campaign with 

Third, they used that remote access, which was 

high confidence to HAFNIUM. The vulnerabilities 

typically run from the US\-based private servers 

exploited were CVE\-2021\-26855, CVE\-2021\-26857, 

to exfiltrate data from an organization’s network. 

CVE\-2021\-26858, and CVE\-2021\-27065\.

Microsoft assesses HAFNIUM was associated with 

CVE

Description 

CVE\-2021\-26855

Server\-side request forgery (SSRF) vulnerability in Exchange, which allowed the 
attacker to send arbitrary HTTP requests and authenticate as the Exchange server.

CVE\-2021\-26857

An insecure deserialization vulnerability in the Unified Messaging service.

CVE\-2021\-26858

A post\-authentication arbitrary file write vulnerability in Exchange. 

the initial activity with the 0\-day exploits; however, 

CVE\-2021\-27065

A post\-authentication arbitrary file write vulnerability in Exchange. 

The attacks included three steps. First, HAFNIUM 

after the vulnerability announcement, several nation 

would gain access to an Exchange Server either 

state actors and criminal groups maneuvered 

with stolen passwords or by exploiting the 

quickly to take advantage of the vulnerabilities for 

aforementioned vulnerabilities to gain initial 

their own gain.

61

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

On July 19, 2021, the US government with its allies 

In April 2021, FireEye released a blog and credited 

A worldwide intelligence collection operation 

collection against Latin American countries and 

and partners took a stance against the Chinese 

MSTIC for their contribution in identifying a Pulse 

After the September 2020 Microsoft blog on 

in Europe. Besides leveraging exploits for VPN 

government and issued a statement that China’s 

Secure VPN 0\-day exploit that was leveraged by 

multiple nation state threat actors targeting 

devices in their cyber operations, NICKEL’s activity 

malicious cyber operation poses a major threat 

Chinese nation state threat actors.46 Microsoft 

information on US elections, ZIRCONIUM did 

also targeted government foreign ministries 

to the United States and its allies’ economic and 

associates some of the activity with MANGANESE 

not stop their collection operations.48 As the US 

throughout Central and South American countries 

national security.44 Although slim on the technical 

and NICKEL. The Department of Homeland Security 

presidential election day approached, ZIRCONIUM 

and some European countries. As China’s influence 

details, the same statement attributed HAFNIUM 

Cybersecurity and Infrastructure Security Agency 

continued to employ web\-bugged emails, targeting 

continues to shift in the region and with countries 

with a high level of confidence to cyber actors 

(CISA) released an alert on the same 0\-day activity 

individuals with access to knowledge of potential 

that are partners in their Belt and Road Initiative, 

affiliated with China’s civilian intelligence agency, the 

indicating that it affected US government agencies, 

shifts in US policy. On July 19, 2021, the United 

we assess that Chinese threat actors will continue 

Ministry of State Security. These actors compromised 

critical infrastructure entities, and other private 

Kingdom’s National Cyber Security Centre released 

to target entities to gain insight into investments, 

tens of thousands of computers and networks 

sector organizations likely beginning in June 2020\.47 

a statement that attributed APT31, which is roughly 

negotiations, and influence.

worldwide in a massive cyber espionage campaign 

CISA stated that after the successful exploitation, 

tracked as ZIRCONIUM by Microsoft, to the Ministry 

that mostly impacted private sector victims. 

the threat actor used their access to place web shells 

of State Security—China’s civilian intelligence 

More 0\-days and other exploitation of 

access and persistence.

on the Pulse Connect Secure appliance for further 

agency.49

vulnerabilities

Chinese nation state cyber operations did not 

In July, SolarWinds released a security advisory 

In addition to MANGANESE, MSTIC has observed 

overlook their neighbors. Since July 2020, activity 

for CVE\-2021\-35211, crediting Microsoft with the 

ZIRCONIUM and two other threat actors who 

tied to CHROMIUM targeted entities in India, 

notification.45 Microsoft detected the 0\-day remote 

exploited small office or home office routers 

Malaysia, Mongolia, Pakistan, and Thailand and 

code execution exploit being used to exploit the 

worldwide. These threat actors are likely 

the sensitive social, economic, and political 

SolarWinds Serv\-U FTP software at entities in the 

compromising routers to use as infrastructure 

issues surrounding Hong Kong and Taiwan. From 

US Defense Industrial Base Sector and software 

for their computer network operations. These 

Microsoft’s perspective, CHROMIUM activity was 

companies. This activity is attributed to a group 

compromised routers are likely in the same 

most active against universities in Hong Kong 

operating out of China, based on observed 

geographical area as their intended target to 

and Taiwan, followed by government entities and 

victimology, tactics, and procedures.

obscure scrutiny against the associated activity.

telecommunication providers in the other countries. 

In addition to targeting neighboring countries, 

there has been a steady drumbeat of intelligence 

44 https://www.whitehouse.gov/briefing\-room/statements\-releases/2021/07/19/the\-united\-states\-joined\-by\-allies\-and\-partners\-attributes\-malicious\-cyber\-activity\-and\-irresponsible\-state\-behavior\-to\-the\-peoples\-republic\-

of\-china/ ; https://www.ncsc.gov.uk/news/uk\-allies\-hold\-chinese\-state\-responsible\-for\-pervasive\-pattern\-of\-hacking 45 SolarWinds Trust Center Security Advisories CVE\-2021\-35211

\|

 46 https://www.fireeye.com/blog/threat\-

research/2021/04/suspected\-apt\-actors\-leverage\-bypass\-techniques\-pulse\-secure\-zero\-day.html 47 https://us\-cert.cisa.gov/ncas/alerts/aa21\-110a 48 https://blogs.microsoft.com/on\-the\-issues/2020/09/10/cyberattacks\-us\-

elections\-trump\-biden/ 49 https://www.ncsc.gov.uk/news/uk\-allies\-hold\-chinese\-state\-responsible\-for\-pervasive\-pattern\-of\-hacking

62

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Iran

Iran continued its streak of destructive cyberattacks 

against regional adversaries while taking a “wait\-

and\-see” approach with the United States amid the 

prospects for sanctions relief from nuclear talks after 

US elections.

Focused on Israel with new attack tools amid 

Microsoft detected an increased focus from a 

A wait\-and\-see approach toward the United 

broader escalation

growing number of Iranian groups targeting Israeli 

States likely serves two purposes

As a covert war between Iran and Israel escalated, 

entities since November, and with that focus came 

Despite Tehran’s less aggressive approach toward 

Iranian offensive cyber actors increased their 

a string of ransomware attacks. An Iran\-linked 

the United States, relative to its regional adversaries, 

attention to Israel and brought with them Iran’s 

threat actor that we track as RUBIDIUM probably 

US entities remained Iranian threat actors’ top target, 

newest tool of choice—ransomware. Iran also 

conducted the Pay2Key and N3tw0rm ransomware 

comprising nearly half of the NSNs we delivered to 

conducted ransomware attacks against at least 

campaigns that almost exclusively targeted Israel in 

cloud\-service customers. Iranian cyber operations 

one Gulf State adversary.50 While it remains unclear 

late 2020 and early 2021, respectively. One common 

toward US targets consisted of a two\-pronged 

whether Iranian actors are using ransomware for 

element of RUBIDIUM’s ransomware campaigns was 

approach: acquiring strategic intelligence likely to 

financial gain, in at least one case they used it as a 

its targeting of Israeli logistics companies involved in 

gain insights into US policy views and planning and 

cover for a destructive attack by deploying wiper 

maritime transportation. These targets indicate a link 

acquiring a foothold on networks likely to provide 

malware on a company’s network while demanding 

to Tehran’s broader objective of retaliating against 

Tehran with contingency options in case the United 

a ransom.51 

Israeli pressure.52

States failed to provide sufficient sanctions relief.

Activity 
Group Name

Other 
names 

Country 
of origin

Industries 
targeted

Iran

PHOSPHORUS

Charming Kitten

CURIUM 

RUBIDIUM 

Houseblend 
Tortoise Shell

Fox Kitten 
Parasite

Iran

Iran

Iran

Diplomatic and nuclear policy communities, academics, and journalists

US military and defense contractors, IT services, and Middle Eastern 
governments 

Israeli logistics companies, IT services, and defense 

50 https://labs.sentinelone.com/from\-wiper\-to\-ransomware\-the\-evolution\-of\-agrius ; https://unit42\.paloaltonetworks.com/thanos\-ransomware/ 51 https://labs.sentinelone.com/from\-wiper\-to\-ransomware\-the\-evolution\-of\-agrius ; https://www.clearskysec.

com/wp\-content/uploads/2020/12/Pay2Kitten.pdf ; https://www.flashpoint\-intel.com/blog/second\-iranian\-ransomware\-operation\-project\-signal\-emerges/ 52 https://www.aljazeera.com/news/2021/4/25/top\-iranian\-commander\-hints\-at\-future\-

response\-to\-isreal ; https://www.timesofisrael.com/eye\-for\-an\-eye\-iran\-editorial\-urges\-retaliatory\-attack\-on\-dimona\-reactor/ ; https://www.al\-monitor.com/originals/2021/04/iranian\-military\-leader\-threatens\-israel\-following\-missile\-strike\-syria

63

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

In late 2020, PHOSPHORUS began targeting nuclear 

Previously in 2020, PHOSPHORUS masqueraded as 

Iran: Most targeted countries (July 2020–June 2021\)

policy experts in signatory nations of the 2015 

conference organizers to high\-profile international 

Joint Comprehensive Plan of Action, very likely for 

conferences, as we detailed in this blog.54 At 

intelligence to gain an edge in anticipated talks 

Microsoft, we detected PHOSPHORUS sending 

on the accord following President Biden’s election. 

spoofed email invitations with links to credential 

PHOSPHORUS conducted a credential phishing 

harvesting sites to more than 100 policy experts 

campaign by masquerading as fellow foreign and 

who were prospective attendees, several of whom 

nuclear policy experts and sending links to nuclear\-

they compromised. The group’s credential phishing 

themed articles that directed victims to a credential 

campaign likely sought to acquire intelligence to 

harvesting site. They targeted fewer than 25 senior 

better position itself in international engagement. 

personnel at medical research organizations, as 

Since April 2021, select Iranian actors also targeted 

detailed by Proofpoint,53 but the vast majority of the 

US agriculture and media companies that are 

100\-plus targets we detected were nuclear policy 

unlikely intelligence targets for Tehran.55 These 

or conflict resolutions experts—in line with the 

same operators employed ransomware on other 

theme of the phishing emails—in the United States, 

companies, suggesting a potential aim to gain a 

United Kingdom, France, and Russia. PHOSPHORUS 

foothold for contingency plans in case nuclear talks 

honed its targeting on this community as nuclear 

fail to meet Tehran’s expectations.

talks began in Vienna in April, including targeting 

diplomat participants.

In some cases, the Iranian targeting of US entities 

that we have detected could be focused on 

intelligence collection, contingency planning, or 

both. Early this year, CURIUM conducted a spear\-

phishing campaign targeting companies that provide 

IT and engineering services for US defense and 

intelligence agencies, probably as a part of a supply 

chain operation to gain access to their customers.

53 https://www.proofpoint.com/us/blog/threat\-insight/badblood\-ta453\-targets\-us\-and\-israeli\-medical\-research\-personnel\-credential 54 https://blogs.microsoft.com/on\-the\-issues/2020/10/28/cyberattacks\-phosphorus\-t20\-munich\-

security\-conference/ 55 DEV\-0270 Compromise Agrinos on 30 May. https://spectre.microsoft.com/\#/entry/19f1e6f3fe899dc1f315a9c432c597a3d4518115604afd63c169948ba7bc95cf?nonce\=72c1a4aa8705; DEV\-0270 compromised 

Cox Media Group on 17 May. https://spectre.microsoft.com/\#/entry/201936a4ffcde2e1eff5d21b43834c7e38631e47e1f66b9ab3bc1e1a135f074f?nonce\=2b351540141b

64

Microsoft Digital Defense Report \| October 2021 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Flow of a typical PHOSPHORUS compromise from spear phish

Conferences, 
conventions, and trade 
shows are widely 
known throughout 
industry and the 
US government 
as a hotbed of 
intelligence collection 
activities, both by 
domestic competitive 
intelligence and foreign 
adversaries. Individuals 
have been known to 
collect information 
thrown out in the trash, 
record presentations, 
attempt to steal 
products, and solicit 
sensitive information 
from employees. 
Though these events 
were widely paused 
due to pandemic 
restrictions, major 
conventions are coming 
back to calendars.

65

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

North Korea 

In the last year, North Korean threat actors have 

been extremely active relative to the country’s 

size and resources, compared to the other major 

attacking states. For example, in the last three 

months of 2020, just over half the NSNs Microsoft 

issued were for North Korean state actors, in spite 

of North Korea being the smallest of the four most 

prolific nation state actors Microsoft tracks.

Feeding a vast appetite for intelligence

of those targeted were in three countries: South 

the international community continue to strictly 

The vast majority of the North Korean targeting 

Korea, the United States, and Japan. However, North 

enforce sanctions on North Korea? How does 

Microsoft noted was directed at consumer account 

Korean actors also targeted academics and think 

COVID\-19 change international dynamics? What will 

targets. For the most part, these targets were 

tank officials in Europe and even China and Russia, 

the new US administration’s policy be toward North 

probably selected based on the likelihood they could 

countries generally seen as friendly to North Korea.

Korea, and how will the tripartite US\-South Korea\-

help North Korea obtain non\-publicly available 

Japan partnership pursue that policy together? 

diplomatic or geopolitical intelligence. North 

The focus on diplomatic or geopolitical intelligence 

Korean groups THALLIUM and ZINC continued to 

likely was driven by Pyongyang’s anxiety for 

create much of the targeting Microsoft observed, 

information in a volatile international situation. 

but they were joined by other groups, such as 

Diplomatic targeting was particularly heavy during 

OSMIUM and CERIUM. Together, these groups 

and directly after the US election. North Korea’s 

focused on diplomatic officials, academics, and 

strong interest in intelligence collection probably 

think tank members from around the world. Most 

had several key questions it sought to answer: Will 

Activity 
Group Name

Other 
names 

Country 
of origin

Industries 
targeted

North Korea

ZINC

THALLIUM

Lazarus 
Labyrinth Chollima

Kimsuky 
Velvet Chollima

North Korea

Utilities, private companies, think tanks, security researchers

North Korea

Think tanks, diplomatic officials, academics

CERIUM

Kimsuky

North Korea

Think tanks, diplomatic officials, academics, defense and aerospace

OSMIUM 

Konni

North Korea

Diplomatic officials, think tanks

66

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Global pandemic creates a new type of 

The world’s only known nation state Bitcoin 

income. One such group Microsoft tracks, which we 

A sophisticated social engineering campaign 

cyberattack

thieves

have not named, often targeted cryptocurrency or 

targeting security researchers

COVID\-19 also drove another North Korean focus 

Alone among nation state actors, North Korea 

blockchain research companies with spear\-phishing 

Finally, North Korea also used social engineering in 

in the last year: the targeting of pharmaceutical 

continued in the last year to target financial 

campaigns while posing as cryptocurrency or 

ways not seen from it before. As MSTIC reported 

companies. As Microsoft reported in November 

companies with the intent of stealing cryptocurrency 

blockchain start\-ups. 

2020,56 ZINC and CERIUM targeted pharmaceutical 

and intellectual property. North Korea’s economy, 

companies and vaccine researchers in several 

already under strain from sanctions, was put under 

countries, probably to speed up its own vaccine 

even greater stress when it closed its borders to 

research or to gain intelligence on the state of 

trade after the outbreak of COVID\-19\. Cyber\-enabled 

research in the rest of the world. 

theft presented one opportunity to make up lost 

North Korea: Top 5 targeted industries 
and sectors (July 2020\-June 2021\)

North Korea: Failed attempts vs. successful 
compromise (July 2020\-June 2021\)

in concert with Google in January,57 ZINC targeted 

security researchers with a fairly sophisticated social 

engineering campaign. The campaign included 

spending months setting up fake profiles that 

looked like real security companies and researchers, 

with websites and social media platforms to support 

these personas. This targeting sought long\-term 

effects beyond the immediate attack. It also 

showed that North Korea is more than capable of 

understanding the Western security landscape well 

enough to blend into it.

Many of the consumer accounts were likely 
personal accounts of academics, think tank 
members, and government officials. 

Relentless spear\-phishing attempts by groups 
such as THALLIUM do not often succeed, 
but because they are so ubiquitous, even 
occasional success yields big results.

56 https://blogs.microsoft.com/on\-the\-issues/2020/11/13/health\-care\-cyberattacks\-covid\-19\-paris\-peace\-forum/ 57 https://www.microsoft.com/security/blog/2021/01/28/zinc\-attacks\-against\-security\-researchers/

67

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Vietnam

Vietnamese threat group BISMUTH utilized cryptocurrency miners to target private sector and government 

institutions in France and Vietnam. Because cryptocurrency miners tend to be seen as lower\-priority threats by 

security systems, BISMUTH was able to take advantage of the smaller alert profile caused by their malware to slip 

into systems unnoticed. 

As MSTIC reported in November 2020,58 BISMUTH carefully planned attacks, conducting reconnaissance before 

creating uniquely crafted spear\-phishing emails for each individual. Sometimes, BISMUTH actors, similar to 

PHOSPHORUS operators, would correspond with targets to build rapport before sending the email containing 

a malicious attachment. Once it compromised networks, BISMUTH sought to achieve continuous monitoring. Its 

targets included human and civil rights organizations.

Activity 
Group Name

Other 
names 

Country 
of origin

Industries 
targeted

Vietnam

BISMUTH

APT32 
OceanLotus

Vietnam

Human rights and civil organizations 

Turkey

SILICON pursues intelligence collection for strategic Turkish interests from a variety of countries, primarily 

in the Middle East and the Balkans. Their reconnaissance indicates the group is most heavily focused on 

countries of strategic interest to Turkey including Armenia, Cyprus, Greece, Iraq, and Syria. They regularly target 

telecommunication and IT companies, likely to establish a foothold upstream of their desired target, and often 

seek access by scanning infrastructure for remote code vulnerabilities.

Activity 
Group Name

Other 
names 

Country 
of origin

Industries 
targeted

Turkey

SILICON 

Sea Turtle 
UNC1326

Turkey

Telecommunications companies in the Middle East and the Balkans

58 https://www.microsoft.com/security/blog/2020/11/30/threat\-actor\-leverages\-coin\-miner\-techniques\-to\-stay\-under\-the\-radar\-heres\-how\-to\-spot\-them/

68

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Tracking nation state threats What we're seeing Analysis of nation state activity this year Private sector offensive actors Comprehensive protections required

Private sector 
offensive actors 

A growing industry of companies called private 

sector offensive actors (PSOAs) create and sell 

malicious cyber technologies that enable their 

customers to break into people’s computers, phones, 

and internet\-connected devices. These private 

companies may not be nation state actors, but their 

business model presents a dangerous and rapidly 

growing challenge for organizations, companies, 

and individual consumers. These tools also threaten 

many global human rights efforts, as they have been 

observed targeting and surveilling dissidents, human 

rights defenders, journalists, civil society advocates, 

and other private citizens. 

In December 2020, Microsoft’s efforts to protect 

our customers from the threats presented by this 

technology led us to file an amicus brief in support 

of WhatsApp’s case against Israel\-based NSO 

Group Technologies (NSO Group) along with Cisco, 

GitHub, Google, LinkedIn, VMware, and Internet 

Association.59 The brief encouraged the court to 

reject NSO Group’s position that it is not responsible 

for the use of its surveillance and espionage 

products by governments. Microsoft also worked 

with Citizen Lab, at the University of Toronto’s Munk 

School, to disable malware being used by an Israel\-

based PSOA that Microsoft calls SOURGUM, and 

that Citizen Lab identified as Candiru.60 SOURGUM 

created malware and 0\-day exploits (fixed in CVE\-

2021\-3197961 and CVE\-2021\-3377162\) as a part of a 

hacking\-as\-a\-service package sold to government 

agencies and other malicious actors. The malware 

was used to target more than 100 victims around 

the world including politicians, human rights 

activists, journalists, academics, embassy workers, 

and political dissidents. To limit these attacks, 

Microsoft has created and built protections into our 

products against this unique malware, which we 

call DevilsTongue.63 By examining how SOURGUM’s 

customers were delivering DevilsTongue to victim 

computers, we saw they were doing so through a 

chain of exploits that impacted popular browsers 

and our Windows operating system. We published 

details of the malware and 0\-day exploits so that 

the world can better understand SOURGUM’s 

activity and address and mitigate the threat. Private 

companies should remain subject to liability when 

they use their cyber\-surveillance tools to break the 

law, or knowingly permit their use for such purposes, 

regardless of who their customers are or what 

they are trying to achieve. Microsoft will continue 

to identify, track, and protect our customers and 

global digital ecosystem from the indiscriminate 

attacks caused by PSOA technology and pursue 

other methods to disrupt this growing threat to our 

customers.

Comprehensive 
protections 
required 

Nation state actors have demonstrated that they 

will go to great lengths to accomplish a mission 

to collect information or intelligence. The skill and 

persistence of malicious nation state actors increase 

the difficulty of detecting and protecting against 

advanced threats. Their impact can be wide ranging 

and highly damaging. These adversaries are well\-

funded, employ techniques of tremendous breadth 

and sophistication, and are motivated by objectives 

of national significance—which may lead to their 

compromising networks for unexpected purposes. 

More than other adversaries, nation state attackers 

target individuals specifically for access to their 

connections, communications, and information. At 

the conclusion of an operation, they will assess what 

went well and what did not and refine tactics and 

techniques for more successful future missions. 

Therefore, defense\-in\-depth strategies against 

nation state adversaries should include educating 

employees on how to avoid being targeted 

themselves. Applying Zero Trust principles across 

corporate resources helps more effectively adapt to 

the complexity of the modern environment, embrace 

the mobile workforce, and protect people, devices, 

applications, and data no matter where they are 

located or the scale of threats they face.

While nation state attacks are often sophisticated 

or can deploy 0\-day vulnerabilities to gain access to 

networks, defense\-in\-depth strategies and proactive 

monitoring can greatly reduce the actor’s dwell 

time on a network, potentially enabling disruption 

of their activities before they reach their goals. 

Above and beyond enabling foundational basics 

like MFA, IT departments should prioritize steps to 

mitigate lateral movement by attackers; specifically, 

credential hygiene and network segmentation. To 

limit the damage of data exfiltration, information 

rights management can be applied to files. Building 

protective controls across your managed identities, 

devices, applications, data, infrastructure, and 

networks will raise the threshold for attackers, 

improving your organization’s ability to detect 

anomalous activity in the environment. 

59 Amicus Brief 12\.20\.2020 (microsoft.com) 60 Hooking Candiru: Another Mercenary Spyware Vendor Comes into Focus \- The Citizen Lab 61 CVE\-2021\-31979 \- Security Update Guide \- Microsoft \- Windows Kernel Elevation of Privilege 

Vulnerability 62 CVE\-2021\-33771 \- Security Update Guide \- Microsoft \- Windows Kernel Elevation of Privilege Vulnerability 63 Fighting cyberweapons built by private businesses \- Microsoft On the Issues

69

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

CHAPTER 4 

Supply chain, IoT, and OT security

Introduction

Challenges in managing risk associated with the supplier ecosystem

How Microsoft thinks about supply chain 

IoT and OT threat landscape 

The 7 properties of highly secured devices

Applying a Zero Trust approach to IoT solutions

IoT at the intersection of cybersecurity and sustainability

IoT security policy considerations

TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

INTRODUCTION: Innovation\-driven opportunity in an 
exponentially larger attack landscape

MICHAL BRAVERMAN\-BLUMENSTYK, CORPORATE VICE PRESIDENT, CHIEF TECHNOLOGY OFFICER, CLOUD AND AI SECURITY

In the past year, we have observed an abundance of incidents driving both physical and digital disruption of 
operations for many organizations. These incidents preyed at times on the physical realm, such as disruption of 
production lines and energy substations, and in other cases, they were conducted entirely in the digital realm, 
such as via a ransomware campaign. 

Looking at the attack surfaces that were exploited 

targets for exploitation, as witnessed recently in 

provides an additional perspective: from legacy 

the highly visible and impactful SolarWinds and 

operational technology (OT) equipment to brand 

Kaseya attacks. While threats and attacks continue to 

new Internet of Things (IoT) devices; from seemingly 

intensify, supply chain complexity increases the costs 

ordinary cloud\-migration projects to 5G IoT\-related 

of defending and the likelihood that an exposure can 

endeavors; and from physical supply chain to digital 

produce a significant return for an adversary.

OT Security

OT devices, such as industrial control, hospital 

monitoring, or water management systems, represent 

the public infrastructure that many societies have 

come to depend on for decades. Many are lagging 

in adopting and leveraging modern security 

standards. As evidenced by recent attacks on water, 

transportation, and energy utilities, disruption in these 

supply chain. All of these are playing an increasing role 

as fertile attack surfaces. These are all topics we will 

elaborate on in this chapter. 

Supply chain integrity 

IoT Security

IoT security is a geometrically expanding frontier with 

areas have profound and broad impact 

innovation\-driven opportunity and an exponentially 

larger attack landscape. The adoption of IoT and the 

The chapter includes discussions about how 

Supply chains, both physical and digital, have an 

huge acceleration in remote services, both at home 

organizations can understand and improve their IoT, 

explicit reliance on trust, and adversaries have taken 

and in the workplace since the onset of the COVID\-19 

OT, and supply chain security posture. We share in 

notice. Over the last decade, successful organizations 

pandemic, increases the likelihood of risk materializing. 

these discussions our data\-driven perspectives related 

have been able to meet the demands of scale, 

This is a trend that will continue as technologies like 

to the IoT and OT threat landscape, research findings 

efficiency, and speed by building expansive, and often 

5G and innovative IoT applications become more 

by the Azure Defender for IoT team, global initiatives 

complex, ecosystems to deliver value to stakeholders. 

ubiquitous. 

such as the Global Cyber Alliance, and more.

Security adversaries today view these systems as 

THE ADOPTION 

OF IOT AND 

THE HUGE 

ACCELERATION 

IN REMOTE 

SERVICES, BOTH 

AT HOME AND IN 

THE WORKPLACE, 

INCREASES THE 

LIKELIHOOD 

OF RISK 

MATERIALIZING.

Microsoft Digital Defense Report \| October 2021

71
71

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

Challenges in managing risk 
associated with the supplier 
ecosystem

What we’re hearing 

Recently, the Microsoft M365 Security, Compliance, and Management team hosted an event to discuss 

the challenges and strategic needs of CxOs (CISOs, CIOs, VPs/Heads of IT and Governance, and 

As outsourcing for applications, infrastructure, devices, and human capital expands, the adoption of tools to 

others) and their organizations to gain a deeper understanding of their security and risk management 

monitor multiple tiers of suppliers for quality, security, integrity, and resilience risks is also growing, and the 

experiences. These are some of the takeaways: 

plethora of frameworks and approaches that organizations are leveraging today continues to grow in tandem. 

Additional complexity emerges when frameworks are applied inconsistently within an organization and across 

1\. The selection and management of suppliers is shaped by a host of factors leading to lack of 

suppliers, or if multiple frameworks are in play.

clarity and low trust, as many struggle to know their environment. 

Organizations must balance protecting themselves from human liability, issues inherent with hybrid 

When it comes to risk assessment and management, siloes can create additional problems. Different teams 

work, shadow IT (unknown or unmanaged apps, services, and infrastructure developed and managed 

have different priorities, which can lead to completely different risk appetites, priorities, practices, and cultures. 

outside standard policies), diversity of their digital estate, and evolving threats and vulnerabilities. 

This inconsistency can be inefficient and create a duplication of effort, gaps in risk analysis, and an inability to 

Adding complexity, there are usually several parties weighing in on vendor/supplier selection. Security 

effectively share risk information across the organization.

An always\-on, automated, integrated approach 

is needed, but current processes aren’t well\-suited 

Siloed environments pose challenges to risk 
assessment and management

to evolve:

• Supplier assessment and review processes often 

include just a questionnaire.

• Once a supplier is onboarded, there is only a 

point\-in\-time annual review cycle.

• Often, different teams within the same company 

have different processes and functions and no 

clear way to share information across teams. 

This can make it difficult to create a holistic and 

automated view of organizational risk. 

is just one of the factors considered and often not a top priority, even though it is an area that needs 

immediate attention. Organizations end up with long lists of suppliers that must be managed (some 

of them unknown), often with a limited look into their security practices and posture. Add to this that 

working within the confines of a supplier contract often limits the assessments. As a result, it is difficult 

to have desired visibility and trust in suppliers. 

2\. Proactive management of a supplier ecosystem is ideal, but difficult. Designated critical 

suppliers require focus due to the potential risk they pose. 

Organizations are often forced into a split approach to supplier management—proactive, when 

possible, but typically more reactive. Reactive approaches are a result of limited resources and projects 

scoped without security as a consideration. To ensure their protection is as comprehensive as possible, 

organizations keep critical suppliers (those critical to an organization’s mission) on a shorter leash, with 

less flexibility and more oversight.

72

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

3\. Leaders are devoting more resources to supplier security, but recent breaches demonstrated 

that traditional models couldn’t guarantee safety. 

IT teams are appreciative of the influx of budget and resources following the SolarWinds and Colonial 

Pipeline breaches. That appreciation comes with an equal amount of trepidation. Those breaches 

demonstrated that the very strategies they are implementing likely would not protect them from a 

similar attack, and continuous assessments and push for remediation across tiers of suppliers are 

necessary. 

4\. Greater visibility and unique solutions are top requests to managing suppliers. 

Within the four key pillars of digital estates—identities, applications, infrastructure, and devices—

suppliers’ personnel are a top concern. Across that risk hierarchy, organizations are looking for 

suppliers to provide:

• Greater visibility into security and who ultimately has access to the organization’s data.

• Customized solutions demonstrating a working knowledge of the industry and the company\-

specific needs.

How Microsoft 
thinks about 
supply chain

The end\-to\-end supply chain and supplier 

ecosystem is complex and opaque, extending 

from development to build, chips to firmware, 

drivers, operating system, third\-party applications, 

manufacturing/factory, and all the way to secure 

updates. Governments and critical infrastructure 

providers are looking for a new level of assurance for 

supply chain security and continuity. It’s important 

that a repeatable process will continue to scale as 

organizations continue to innovate. Supply chain 

security rigor is foundational to how an organization 

should work and is expected by partners and 

customers who interact with an organization’s 

products and services.

Nine secure supply chain focus 
areas

Outlined below is a framework to efficiently evaluate 

your supply chain ecosystem with considerations 

for how you might approach protecting it. We 

group our investments into nine secure supply chain 

workstreams to methodically evaluate and mitigate 

risk of exposure in each area.

1\. First\-party engineering systems for hardware 

and software 

Massive software development companies aren’t 

the only ones doing engineering work. Even small 

IT shops that may make minimal development 

investments and organizations building on top of 

existing infrastructure have teams writing code. 

Zero Trust security model for supplier ecosystem risk

Nine areas of investment for a secure end\-to\-end supply chain

For supplier risk management, having customized solutions and greater visibility into who ultimately has access 

to an organization’s data across domains are top priorities. While there are many places to begin your Zero 

Trust journey, from a supplier ecosystem and risk management standpoint, instituting multifactor authentication 

(MFA) should be a priority. 

For more information on Zero Trust strategy, see the Hybrid workforce security chapter of this report.

73

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

To produce secure software or hardware, 

Build: Without appropriate protections, the 

3\. Physical security

LEVERAGING MACHINE LEARNING IN 

organizations must ensure that the first\-party 

build pipeline presents product compromise 

Organizations must define, implement, and manage 

CONTINUOUS SECURITY MONITORING 

engineering system is secured from the various 

risks that can be highly effective and difficult 

appropriate security controls to ensure the security

OF SUPPLIERS

threat vectors that could be exploited by attackers.

to trace. While source control will usually have 

some form of change management, without 

4\. Manufacturing security

Microsoft leverages machine learning (ML) to scan 

active supplier contracts. This model is trained to 

Developer environment: The developer 

appropriate controls in place in a build system, 

Manufacturing standards must be defined and 

recognize commonly negotiated security clauses 

environment encompasses the tools and 

it can be difficult to identify what might have 

enforced to enable detection, protection, and 

and determine whether or not they meet the intent 

platforms that developers author code on, such 

been injected during the build process.

recovery from cyberattacks. Organizations must 

of the original requirement. The outputs of this 

as operating systems, code editors, research 

also ensure that samples or prototypes are 

continuous scanning are leveraged to advise the 

tools (for example, browsers and associated 

Release: Ensuring you are releasing what you 

securely handled and stored, and that appropriate 

third parties operating within our environments and 

websites), local build tools, and other general 

intended is the end goal of a secure software 

monitoring is in place to track and maintain the 

ensure their expectations and accountabilities are 

code authoring tools. The primary target is 

supply chain. Enumerating inputs and verifying 

chain of custody for all proprietary items or 

clearly defined. 

developer identity, and solutions must be put 

the final product takes a comprehensive 

finished goods.

in place to mitigate this risk.

understanding of complex systems and is an 

essential final step in ensuring an organization 

5\. Logistics security

Source code: The risk of malicious code can 

knows what it is releasing.

Logistics functions must be safeguarded to prevent 

arise when developers take source code and 

tampering, loss, or theft of the products during 

binaries from a variety of sources, including 

2\. Firmware and driver security

transportation and storage. Hardware and devices 

from internal sources, open\-source software 

Firmware and drivers are the foundation of most 

teams should have appropriate operational controls 

(OSS), or from another organization. Each 

hardware devices. If hacked and embedded with 

and frameworks in place with the suppliers to ensure 

source needs to have a level of trust ensured 

malware, they pose a huge risk to the hardware 

receiving, shipping, storage, and other logistics 

and known to have appropriately secure 

device and the organization that depends on it, 

management nodes are secure and compliant with 

supply chain checks. In most reported OSS\-

potentially creating unauthorized access, making it 

the company’s standards. 

as\-malware cases, the malware is designed 

inoperable or even unbootable. Organizations need 

to steal developer credentials and build 

to ensure that all firmware and drivers installed on 

6\. Supplier security

environment variables, exfiltrating them to a 

servers or end\-user equipment follow the required 

When engaging with suppliers, organizations must 

remote attacker\-controlled server.

security requirements and have the necessary 

ensure that the suppliers comply with well\-defined 

Continuous security monitoring using ML

documentation to prove their compliance.

supplier security and privacy assurance requirements 

throughout the duration of their partnership.

Learn more:

Transforming how Microsoft connects with its 58,000 

suppliers – Inside Track Blog

74

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

7\. Security validations and assurances

9\. Monitoring and detections

The active nature of the adversaries requires 

Each of the supply chain focus areas above require 

continuous evaluation of the security posture of the 

monitoring, detection, and follow\-up actions when 

end\-to\-end supply chain to identify and prioritize 

questionable activity is identified. Increasingly 

security investments. A mix of internal audits, 

monitoring, detection, and initial response are 

lessons learned from recent events, and penetration 

automated in today’s hyper\-scaled cloud operations. 

testing provides assurance that the right controls 

These actions cover common cases but can also be 

are in place to detect, prevent, and/or mitigate 

adaptable to deal with new or unimagined scenarios.

these attacks. The findings from these engagements 

help identify the next set of requirements to 

Learn more:

US Executive Order and 
supply chain security

Issued on May 12, 2021, the Executive Order 

(EO) on Improving the Nation’s Cybersecurity 

(EO 14028\) outlines significant new steps for US 

federal agencies and their technology providers 

to strengthen IT modernization, improve incident 

response, and enhance software supply chain 
security.66 Section 4 focuses on software supply 

chain security, enumerating areas of requirements 

to be developed for both software providers and 

federal agency users of software. For software 

providers, the EO calls for requirements to enhance 

be addressed.

8\. Trust chain governance and resilience

Customers trust their supplier organizations protect 

them as they use their products and services. First\-

party trust chains provide identity, integrity, and 

Firmware security \- Azure Security Microsoft Docs 

 \|

(6/24/2021\)

Microsoft Open Source Software Security

Datacenter security overview \- Microsoft Service 

ability to resist tampering or attack and foster 

Assurance Microsoft Docs 

\| 

(8/23/2021\)

greater transparency into components, including 

non\-repudiation for the organization’s platform, 

Physical security of Azure datacenters \- Microsoft 

products, and services. The main elements of trust 

Azure Microsoft Docs 

\| 

(7/10/2020\)

chains are public key infrastructure, cryptographic 

Supply Chain Security \- Microsoft Research

algorithms, hardware, and the supporting teams and 

facilities. Effective governance of third\-party trust 

chains is critical. 

Microsoft Security Development Lifecycle

through secure software development practices and 

environments, use of tools or processes for software 

verification and vulnerability checks, providing 

of Software Bill of Materials (SBOM) information, 

participation in a vulnerability disclosure program, 

and other practices. For federal agency users of 

Learn more:

software with privileged access or other attributes 

that make it especially critical, the EO calls for 

security measures, published by the National 

Institute of Standards and Technology (NIST) in 

July, to manage operational risk. Microsoft has 

long invested in developing best practices for 

secure software development, software testing, 

and vulnerability disclosure and management 

programs, and we’ve contributed to efforts to define 

industrywide practices and consensus standards, 
including through SAFECode,68 ISO,69 and NIST.70 

Along with GitHub, Microsoft has also contributed to 

efforts to develop best practices and specifications 

to define use cases for and support the delivery of 

SBOMs, which identify what software is composed 

of and allow software providers to associate 

information with components. Microsoft and 

GitHub support delivering SBOMs to enable 

vulnerability and integrity checks, and we’re 

committed to leveraging SBOMs as part of a 

broader evidence store that would verify end\-to\- 

end supply chain integrity.

Know your suppliers and understand 
their supply chains.

Microsoft and NIST collaborate on EO to drive Zero Trust adoption Microsoft Security Blog (8/17/2021\)

 \|

CYBER EO Microsoft Federal

\|

Microsoft \- Executive Order \- NIST workshop position paper 4\- Testing software source code Microsoft Corporation.pdf

Microsoft \- Executive Order \- NIST workshop position paper 5\- Software integrity chains Microsoft Corporation.pdf

Microsoft’s approach to coordinated vulnerability disclosure

NTIA\_RFC\_SBOM\_Minimum\_Elements\_MSFT\_Response\_061721\.docx.pdf

66 Executive Order on Improving the Nation’s Cybersecurity The White House

\| 

 67 Security Measures for EO\-Critical Software Use NIST

\| 

68 Fundamental Practices for Secure Software Development, Third Edition \- SAFECode 69 ISO \- ISO/IEC 27034\-1:2011 \- Information technology — 

Security techniques — Application security — Part 1: Overview and concepts 70 Secure Software Development Framework CSRC (nist.gov)

\| 

75

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

IoT and OT 
threat 
landscape

Successful solutions today often depend on the 

convergence of many components, including 

hardware, software, and cloud services, which often 

come together in an IoT solution. IoT is more than 

connected devices—it’s about the information 

those devices collect and the powerful, immediate 

insights that can be garnered from that information. 

Accordingly, IoT and other embedded and OTs have 

become critical business, operational, and security 

topics. More than ever, IoT and OT security is finding 

its way into corporate boardrooms and state and 

federal legislature discussions as a high\-priority 

issue, in part due to the increasing frequency and 

severity of attacks in the past year. This proliferation 

of attacks has also driven increased awareness 

of the extent to which cyberattacks in the digital 

realm can impact the physical realm: the Colonial 

Pipeline cyberattack directly led to shutdown of the 

plant 71 led to a hazardous situation, in which 

cyber actors obtained unauthorized access and 

used the SCADA system’s software to increase the 

concentration of sodium hydroxide—a caustic 

chemical—in the water. The hack of a security 
camera provider72 exposed sensitive footage from 

hospitals, police departments, and a plethora of 

other companies.

All these developments underscore the need for 

organizations to secure their IoT and OT footprints. 

Organizations are interconnected more than ever, 

resulting in increased exposure of legacy OT devices 

and environments, including those that have existed 

in relative isolation. On the other hand, the newest 

IoT devices (such as smart TVs and smart sensors) 

reside in both OT and IT environments. Putting all 

of this together, with the added context of privacy 

concerns and regulatory compliance, stresses the 

need for a holistic approach that enables seamless 

security and governance across all OT and IoT 

devices.

Learn more:

largest conduit for gasoline in the United States. The 

SCADA Hacking: The Most Important SCADA/ICS 

compromise of the Oldsmar water 

Attacks in History (hackers\-arise.com) (4/12/2021\)

Evolving cyberthreats

Enterprises are having to contend with evolving 

cyberthreats and novel malware. These issues 

include supply\-chain attacks such as HAVEX73 and 

SolarWinds,74 0\-day industrial control systems (ICS) 

malware such as Triton75 and Industroyer,76 fileless 

malware,77 and living\-off\-the\-land tactics using 

standard administrator tools,78 which are harder to 

spot because they blend in with legitimate day\-to\-

day activities. These attacks have also increased in 

frequency and severity in the past year.

From a technical perspective, the Triton attack on 

the safety controllers in a Middle East petrochemical 

facility was intended to cause major structural 

damage to the facility and possible loss of life. The 

attackers got their initial foothold in the IT network 

and subsequently used living\-off\-the\-land tactics to 

gain remote access to the OT network, where they 

deployed their OT purpose\-built malware. 

71 Lessons Learned from Oldsmar Water Plant Hack – Security Today 72 Hackers breach Verkada’s giant trove of security\-camera data collection Fortune

\| 

 73 https://en.wikipedia.org/wiki/Havex 

74 https://msrc\-blog.microsoft.com/2020/12/13/customer\-guidance\-on\-recent\-nation\-state\-cyber\-attacks/ 75 https://www.fireeye.com/blog/threat\-research/2017/12/attackers\-deploy\-new\-ics\-attack\-framework\-triton.html 

76 https://www.zdnet.com/article/industroyer\-an\-in\-depth\-look\-at\-the\-culprit\-behind\-ukraines\-power\-grid\-blackout/ 77 https://docs.microsoft.com/en\-us/windows/security/threat\-protection/intelligence/fileless\-threats 

78 PowerShell, Windows Management Instrumentation

Microsoft Digital Defense Report \| October 2021

76
76

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape 7 properties of secured devices Applying Zero Trust to IoT IoT and sustainability IoT policy

How an attacker can get into an enterprise through IoT

77

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

What we’re seeing: IoT\-related malware in the wild

Distribution of IoT command and control services by country (July 2020–June 2021\)

Distribution of IoT malware CPU architecture (July 2020–June 2011\)

Top IoT malware detected in the wild (July 2020\-June 2021\)

78

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

Findings: Industrywide IoT and 
OT vulnerabilities 

The Microsoft Defender for IoT team conducts 

research on various types of equipment ranging 

from legacy industrial control system controllers 

to cutting\-edge IoT sensors. Upon discovery of a 

vulnerability, the findings are shared with relevant 

vendors through a responsible disclosure process 

led by the Microsoft Security Response Center and 

the US Department of Homeland Security (DHS), 

enabling these vendors to investigate and patch 

the vulnerability.

In April 2021, we uncovered a series of critical 

memory allocation vulnerabilities in IoT and OT 

devices that adversaries could exploit to bypass 

security controls to execute malicious code or cause 

a system crash. The group of vulnerabilities was 

dubbed BadAlloc. These remote code execution 

vulnerabilities affected a wide range of industries 

and verticals, from consumer and medical IoT, to 

industrial IoT, OT, and industrial control systems. 

They covered more than 25 common vulnerabilities 

and exposures (CVEs). In the context of IT 

environments, an exploitation of such a vulnerability 

can result in a loss of confidentiality. In the context 

of OT environments, it can be used to trigger a 

disruption of operations.

The vulnerabilities stem from using vulnerable 

memory functions, such as malloc, calloc, realloc, 

memalign, valloc, pvalloc, and others. Our research 

The following is an example of BadAlloc:

showed that memory allocation implementations 

written throughout the years as part of IoT devices 

and embedded software have not incorporated 

proper input validations. Without these input 

validations, an attacker could exploit the memory 

allocation function to perform a heap overflow, 

resulting in execution of malicious code on a 

target device.

The memory allocation vulnerabilities can be 

invoked by calling the memory allocation function, 

such as malloc(VALUE), with the VALUE parameter 

derived dynamically from external input and being 

large enough to trigger an integer overflow or 

wraparound. The concept is as follows: When 

sending this value, the returned outcome is a 

freshly allocated memory buffer. While the size 

of the allocated memory remains small due to 

the wraparound, the payload associated with the 

memory allocation exceeds the actual allocated 

buffer, resulting in a heap overflow. This heap 

overflow enables an attacker to execute malicious 

code on the target device. 

BadAlloc is a case that illustrates the extensive 

impact these vulnerabilities can have because the 

risk exists in IoT and OT devices across all major 

industries. This example highlights one of the 

biggest challenges in mitigating IT, IoT, and OT risks: 

they share attack surfaces, and attackers look at the 

entire ecosystem. 

The protection of IoT and OT devices from 

to ensure that modern digital environments are 

exposure to IT risks becomes more important as 

not held back by threats from legacy technology 

they converge. Too often these risks are addressed 

connected to OT systems. Mitigation requires an 

in isolation with a rigidly siloed approach. To be 

integrated approach that spans the entire enterprise. 

successful in countering attacks, risks should be 

Organizations should look for opportunities to 

dealt with holistically while also accommodating 

harden, patch, or segment systems to reduce the 

domain expertise in each area. It is also critical 

attack surface.

79

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

BadAlloc impact matrix

Mitigating IoT and OT vulnerabilities such 

Segment. Network segmentation is important for 

as BadAlloc

We recommend the following mitigation strategies 

for organizations with IoT and OT devices:

Zero Trust because it limits the attacker’s ability 

to move laterally and compromise assets after 

initial intrusion. IoT devices and OT networks 

should be isolated from corporate IT networks 

Patch, patch, patch. Follow vendor instructions for 

by using firewalls.

applying patches to affected products.

BadAlloc is an example of an IoT/OT family of vulnerabilities that poses a risk across all industries. The 
extent and nature of the risk depends on the specific context of usage of the device. BadAlloc shouldn’t 
be treated as only an OT or IT issue; instead, organizations should take a holistic approach to mitigating 
the risk.

Learn more:

Eliminating IoT vulnerabilities using CIS Benchmarks 

and Azure Defender for IoT – Microsoft Tech 

Community (8/8/2021\)

If you can’t patch, monitor. Since most legacy 

IoT and OT devices don’t support agents, use an 

IoT/OT\-aware network detection and response 

(NDR) solution79 and a SIEM/SOAR solution80 to 

auto\-discover and continuously monitor devices 

for anomalous or unauthorized behaviors, such 

as communication with unfamiliar local or remote 

hosts. These elements are essential in implementing 

a Zero Trust strategy for IoT/OT.

Reduce the attack surface. Eliminate unnecessary 

internet connections to OT control systems and 

implement virtual private network (VPN) access 

with MFA when remote access is required. The 

US DHS warns that VPN devices may also have 

vulnerabilities and should be updated to the most 

current version available.

79 https://azure.microsoft.com/en\-us/services/azure\-defender\-for\-iot/ 80 https://azure.microsoft.com/en\-us/services/azure\-sentinel/ 

80

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape 7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

The 7 properties 
of highly 
secured devices

We suggest ensuring the hardware and operating 

system of both your and your suppliers’ devices 

are designed and implemented securely, have 

high barriers to compromise, and incorporate 

mechanisms and processes that continually monitor, 

alert, and restore security when necessary.

Through extensive research and testing, Microsoft 

identified the seven properties that are present in all 

standalone, internet\-connected devices considered 

to be highly secured. In many cases, these highly 

secured devices apply additional security measures, 

but in all cases each of the seven properties is 

present. Collectively, these seven properties provide 

a baseline foundation of security throughout 

device silicon, software architecture and OS, cloud 

communications, and cloud services. The complexity 

of maintaining all seven properties could be a barrier 

for some organizations, despite the exceptional 

cost that often results from a fallout of incomplete 

device security. 

Hardware root 
of trust

Defense in depth

Small trusted 
computing base

Dynamic 
compartments

Password\-less 
authentication

Error reporting

Device identity and integrity are protected by hardware. Physical countermeasures resist side\-channel attacks. 

Does the device have a unique, unforgeable identity that is inseparable from the hardware? Is the integrity of the 
device software secured by hardware?

Multiple mitigations applied against threats. Countermeasures mitigate the consequences of a successful attack on any 
one vector. 

Does the device remain secured even if one security mechanism is breached?

Private keys stored in a hardware\-protected vault, inaccessible to software. Division of software into self\-protecting layers. 

Is the device’s security enforcement code protected from bugs in other software on the device?

Hardware\-enforced barriers between software components prevent a breach in one from propagating to others. 

Is a failure in one component of the device contained to that component? Can new compartments be added in 
field to address new security threats?

Signed token, signed by an unforgeable cryptographic key, proves the device identity and authenticity. 

Does the device authenticate itself with certificates or other tokens signed by the hardware root of trust?

A software error, such as a buffer overrun induced by an attacker probing security, is reported to cloud\-based failure 
analysis system. 
Does the device report errors for analysis to enable verification of the correctness of in\-field device execution 
and identification of new threats?

Renewable 
security

Update brings the device forward to a secure state and revokes compromised assets for known vulnerabilities or security 
breaches. 

Is the device’s software updated automatically? Can the device’s security TCB software be updated rapidly 
without repackaging other device code?

81

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT IoT and sustainability

IoT policy

After basic security requirements are met, you 

Continual updates to keep devices healthy

can shift your focus to the specific Zero Trust 

Utilize a centralized configuration and compliance 

requirements for IoT solutions:

management solution and a robust update 

Applying a Zero 
Trust approach 
to IoT solutions

Strong identity to authenticate devices

Register devices, issue renewable credentials, 

Securing IoT solutions with a Zero Trust security 

employ passwordless authentication, and use a 

model81 starts with non\-IoT specific requirements—

hardware root of trust to ensure you can trust its 

specifically ensuring you have implemented the 

identity before making decisions.

basics to securing identities and their devices and 

mechanism to ensure devices are up to date and in 

a healthy state.

Security monitoring and response to detect and 

respond to emerging threats

Employ proactive monitoring to rapidly identify 

unauthorized or compromised devices.

limiting their access. These requirements include 

Least privilege access to mitigate blast radius

explicitly verifying users, having visibility into the 

Implement device and workload access control to 

Learn more:

devices they’re bringing on to the network, and 

limit any potential blast radius from authenticated 

Azure Defender for IoT Microsoft Azure

\| 

being able to make dynamic access decisions by 

identities that may have been compromised or 

using real\-time risk detections. Meeting these 

running unapproved workloads.

requirements helps to limit the potential blast radius 

of users gaining unauthorized access to IoT services 

Device health to gate access or flag devices 

and data in the cloud or on\-premises. Otherwise, 

for remediation

you could face both mass information disclosure 

Check security configuration, assess for 

(such as leaked production data of a factory) and 

vulnerabilities and insecure passwords, and monitor 

potential elevation of privilege for command and 

for active threats and anomalous behavioral alerts 

control of cyber\-physical systems (such as stopping 

to build ongoing risk profiles.

Azure Sentinel – Cloud\-native SIEM Solution 

\| 

Microsoft Azure

https://aka.ms/7properties

Nineteen cybersecurity best practices used to 

implement the seven properties of highly secured 

devices in Azure Sphere (microsoft.com) (July 2020\)

Zero Trust Cybersecurity for the Internet of Things 

(4/30/2021\)

a factory production line).

81 Zero Trust Security Model and Framework Microsoft Security

\| 

82

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

IOT at the 
intersection of 
cybersecurity 
and 
sustainability

sustainability will become a primary driver for 

that can then provide a pathway for attackers to 

Moreover, it is critical to understand the security 

operational deployment of IoT. To make significant 

reach OT systems, and the reverse is also possible. 

posture of supply systems that are not on the 

improvements to their environmental footprint, 

In one example, attackers used an aquarium 

organization’s IT/OT network, but nonetheless affect 

organizations must assess and monitor their 

system to access a casino’s high\-roller databases,84

operations. Just as an organization looks to improve 

behavior and then use automated or remote\-

demonstrating that any device with connectivity can 

efficiency and sustainability, its suppliers do too. 

control methods to optimize it.

present a motivated attacker with an opening.

These supply systems may be connected outside 

The challenge is figuring out how to measure, 

While many organizations are evolving their IT 

monitor the device operation, reduce truck rolls, 

monitor, and automate these systems securely. 

security approach (moving away from a perimeter\-

and deliver more uptime. Compromises in externally 

These systems might contain sensitive data, connect 

based security model to a Zero Trust model), IoT 

managed infrastructure components can directly 

of the network (such as cellular) to measure and 

Organizations generally deploy IoT to improve the 

to business systems across your organization, 

is often overlooked and lagging. For example, 

impact downstream businesses. For example, turning 

bottom line: better quality, higher productivity/

and increasingly impact the physical operation of 

organizations know to encrypt sensitive data from 

off the chillers in a building could halt operations 

less downtime, production optimization, and 

your enterprise. Attacks like the aforementioned 

applications, but many have not considered that 

and spoil inventory, air quality sensors may not alert 

reducing operating costs and/or increasing output 

Triton82 or Crash Override83 that specifically target 

their control systems rely on the Modbus protocol, 

workers to unsafe conditions, and so on.

nonlinearly. Improving the business in these ways 

OT systems demonstrate that these systems 

which by design lacks any authentication and sends 

also reduces waste: less resource use for the same 

are attractive targets for nation states and 

data in the open. While PCs are routinely required 

While IoT can and will enable better environmental 

or greater output, higher uptime, reduction in scrap, 

cybercriminals, and they have the potential to both 

to have updated certificates, IoT devices are often 

practices, it is essential that all connected systems—

and so on. While IoT investment specifically for 

disrupt business operations and potentially create 

deployed with factory default passwords.

which may be in place for a decade or longer—are 

sustainability is less common, sustainability as an 

environmental damage.

designed, evaluated, and operated securely. As the 

initiative is no longer regarded as a zero\-sum effort 

Compromises in these OT systems may disrupt 

world adapts to the new priorities that emerged 

in conflict with business value.

It is essential to assess the security of OT systems 

operations, but attackers are also focusing on how 

during the pandemic, companies are looking to 

As organizations face increasing pressure to improve 

their environmental footprint—from shareholder 

calls and new government regulations—

IT systems. As we have observed, attackers will 

often updated or retrofitted with remote capabilities, 

Secured IoT will play a critical role in enabling 

choose the “soft targets” as a point of ingress. Spear 

introducing new attack vectors that allow virtual 

businesses to both sustainably use and protect vital 

phishing or similar attacks allow access to IT systems 

attacks to cause harm in physical scenarios. Earlier 

resources and utilities today and into the future.

with the same rigor and comprehensiveness as 

IoT and OT interact. Industrial control systems are 

address the growing sustainability challenges ahead. 

It is essential to assess the security of OT systems with 
the same rigor and comprehensiveness as IT systems.

this year, a water treatment plant in Florida fell 

victim to an attacker that remotely accessed critical 

systems and attempted to alter the amount of 

chemicals in the water supply.85

82 Hackers use Triton malware to shut down plant, industrial systems ZDNet

\| 

 83 Crash Override Malware Took Down Ukraine’s Power Grid Last December WIRED

 \|

 84 A smart fish tank left a casino vulnerable to hackers (cnn.com) 

85 FBI, Secret Service investigating cyberattack on Florida water treatment plant \- TechRepublic

83

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

IoT adoption for sustainability

Those adopting 
IoT for 
sustainability 
are more likely 
to be in the 
implementation 
phase of their 
AI strategy than 
those adopting 
IoT for other 
reasons.86

IoT security 
policy 
considerations

Policymakers around the world are acknowledging 

the profound implications of IoT security for privacy, 

safety, critical infrastructure protection, and digital 

transformation in general. Approaches to IoT 

security policy range from voluntary programs to 

mandatory security requirements. The range of IoT 

device types, growing number of devices, and the 

and appropriately tailored cybersecurity policy a 

complex task. To tackle the IoT threat landscape, 

the global community of IoT manufacturers and 

cybersecurity experts has developed sets of 

best practice standards for IoT device cybersecurity. 

These standards have demonstrated effectiveness 

against common attacks, and industry and 

policymakers alike can leverage them for 

immediate improvements to the global state of 

IoT device security for consumer, enterprise, and 

government users.

Minimum security baselines

cybersecurity health. These standards are intended 

agency use of IoT devices, and EO 14028, which 

to provide guidance for manufacturers, developers, 

proposes a consumer IoT device labeling program 

and users to identify and adopt best practices for 

that may also reference NISTIR 8259A as well as 

device security. Prominent examples of international 

compatibility with ETSI or ISO standards. Other 

standards include the European Telecommunications 

examples include the proposed mandatory security 

Standards Institute (ETSI) standard for consumer 

requirements for consumer smart devices in the 

IoT security released in June 2020, ETSI EN 303 645\. 

UK,88 and the voluntary device labeling schemes 

The ETSI standard is now a public set of resources 

in Singapore and Finland, all based on ETSI EN 

that governments and companies around the world 

303 645\. In leveraging international standards and 

can use to enhance the security of IoT devices, 

widely used best practices, policymakers can also 

and it includes both governance and technical 

help to ensure that mandatory requirements are 

recommendations. It was created through a 

consistent and mutually recognized across regions 

rigorous and collaborative multistakeholder process 

to avoid fragmentation that would work against IoT 

involving experts from industry, government, 

innovation, interoperability, and security.

and academia. Similarly, after an iterative public 

consultation process, in May 2020, NIST released 

NISTIR 8259A, which details a baseline set of device 

capabilities necessary for common cybersecurity 

controls. The International Organization for 

Standardization (ISO) and the International 

Electrotechnical Commission (IEC) are also 

developing a minimum\-security baseline. 

Global Cyber Alliance project: 
How policy and standards 
improve IoT security 

Standards, laws, and proposed requirements for 

minimum IoT device security baselines share many 

commonly recommended or required controls. 

The first three provisions of the ETSI standard for 

Policy can help manufacturers adopt international 

consumer IoT security, ETSI EN 303 645, are the most 

standards in a consistent way to improve security 

highly recommended by ETSI and make appearances 

across a range of consumer products and 

in several national\-level policies. These include:

promote an advanced state of security in critical 

1\. No default passwords 

applications. In the United States, policy initiatives 

2\. Implement a vulnerability disclosure policy

based on standards include the IoT Cybersecurity 

3\. Keep software updated 

volume of interactions between devices, the physical 

Standards for minimum IoT security baselines 

world, and the internet make developing effective 

provide a promising start to improving global 

Improvement Act of 2020,87 which references NISTIR 

8259A for managing risks associated with US federal 

86 Microsoft IOT Signals report, to be published November 2021 87 Text of H.R. 1668 (116th): IoT Cybersecurity Improvement Act of 2020 (Passed Congress 

version) \- GovTrack.us 88 New cyber security laws to protect smart devices amid pandemic sales surge – GOV.UK (www.gov.uk)

84

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

State laws in California and Oregon both prohibit 

used to help policymakers and industry leaders 

emulated IoT devices distributed worldwide to 

SUMMARY OF GCA CONCLUSIONS

default passwords for IoT devices. Similarly, 

understand the benefit of best practice approaches 

provide real, at\-scale, long\-term attack data to 

GCA’s analysis of real attack data shows that default 

recommendations or requirements for updated 

to IoT device security, and as proof points for 

understand trends and changes in IoT attack 

passwords factory\-set by device manufacturers and 

software and use of secure communications 

manufacturers to adopt standards and comply 

methodologies. 

protocols like HTTPS also frequently appear in 

with policy. 

standards and policies around the globe.

The research tested three controls commonly 

security vulnerability for IoT devices. Policy and 

never changed by users, along with weak passwords 

set by users, together represent the most exploited 

Microsoft supported a research study conducted by 

created an enticingly accessible target for would\-be 

the Global Cyber Alliance (GCA)89 to demonstrate 

attackers to learn as much as possible about the 

the effectiveness of commonly recommended 

existence, source, and prevalence of attacks. GCA 

controls in preventing attacks. The analysis can be 

operated a large honey farm of several hundred 

• Secured access control (“no default passwords”)

• Device capability to update software and 

recommendation to keep software updated

harmonize implementation of the requirements in 

IoT device security standards such as NISTIR 8259, 

ETSI EN 303 645, and ISO/IEC 27402 to promote 

secured access control best practices and address 

Using home\-grown honeypot technology, GCA 

referenced in IoT security standards and policy: 

regulatory frameworks can help drive adoption and 

• Data in transit is protected

this risk.

GCA honeyfarm attacker traffic by protocol 

GCA honeyfarm attacks with activity (commands and downloads) by protocol 

Roughly equal attacker traffic scanning for open ports through which to launch attacks.

Telnet is the clear protocol of choice for exploitation in attacks launched on IoT devices.

89 https://www.globalcyberalliance.org/ 

85

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

The research also showed widespread prevalence 

of attempts to exploit security vulnerabilities in 

the software stacks of IoT devices. This finding 

offers support for the effectiveness of keeping 

software updated and using secure communications 

protocols to prevent attempts to compromise 

security vulnerabilities.

The prevalence of attack attempts observed on 

security vulnerabilities in IoT device software also 

supports the notion that commonly recommended 

nontechnical controls would reduce the likelihood 

of attack success. In particular, requirements for 

manufacturers to implement a vulnerability disclosure 

and management policy and to disclose the security 

support status of their products would provide 

valuable information to consumers.

Learn more:

Global Cyber Alliance: IoT Policy and Attack Report

Microsoft data and threat 
signals support these findings

The GCA project findings align well to what Microsoft 

sees across its IoT sensor network. Generic HTTP 

scanning and scraping forms the bulk of requests we 

receive, followed by Secure Shell (SSH) and Telnet, 

respectively. Both protocols are frequently seen 

across IoT/OT devices, with Telnet in particular being 

a favorite of botnets like MIRAI and others based on 

it. The two protocols are also commonly associated 

with brute force password attacks, and when taken 

together become the most prevalent type of attack 

we see against IoT/OT devices. 

Distribution of attacks against popular IoT/OT 
protocols (July 2020\-June 2021\)

When we look at attacks against these two ports, we see things are anything but static. Different actors come 

and go, in many cases repurposing bots with leaked source code such as MIRAI. Often these attacks replicate 

existing ways of working, but we have started to see more advanced use cases where bots are leveraging new 

exploits.90 It is worth noting that many of these attacks continue to use poor passwords as a basis for lateral 

movement between infected hosts.

Microsoft’s sensor network gives us raw data on these types of attacks and the passwords in use. We looked at 

over 280,000 attacks and analyzed the password data we collected. Perhaps unsurprisingly we saw that 96% of 

attacks used a password with fewer than 10 characters, 92% had fewer than 8, and slightly more shockingly, 72% 

of all attacks required only trying a password of 6 characters or less. Within these password attempts, only 2% 

included a special character and 72% didn’t even contain a number.

The attacks we are seeing in the wild line up with the GCA data and other reports. Default passwords, which are 

generally a single short English word, make it trivial for an attacker to access an organization’s infrastructure. If 

secure identity management with an organization’s IoT devices is not an option, longer passwords—especially 

those with special characters—are strongly advised.

Attacks against Telnet and SSH ports

90 How to proactively defend against Mozi IoT botnet Microsoft Security Blog

\|

86

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Managing supplier ecosystem risk How Microsoft thinks about supply chain IoT and OT threat landscape

7 properties of secured devices Applying Zero Trust to IoT

IoT and sustainability

IoT policy

Passwords seen in 45 days of sensor signals

\>20 Million 
NUMBER OF TIMES 

WE OBSERVED 

THE PASSWORD 

“ADMIN” USED IN 

IOT DEVICES OVER 

A 45 DAY PERIOD.

Microsoft Digital Defense Report \| October 2021

87
87

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

CHAPTER 5 

Hybrid workforce security

Introduction

A Zero Trust approach for securing hybrid work

Identities

Devices/Endpoints

Applications

Network

Infrastructure

Data

People

88

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

INTRODUCTION: The basics matter

BRET ARSENAULT, CHIEF INFORMATION SECURITY OFFICER

This past year continued to challenge us in profound ways. While most industries made the shift to remote 
work due to the pandemic, it created new attack surfaces for cybercriminals to take advantage of, such as 
home devices being used for business purposes. In the first half of 2021, there were three significant assaults: 
NOBELIUM (the SolarWinds supply chain attack), HAFNIUM (an on\-premises Exchange server attack), and 
Colonial Pipeline (a ransomware attack). 

Many lessons can be learned. First, a continuing 

If compromised organizations had applied basic 

threat vector is email compromise. In fact, phishing is 

security hygiene like patching, applying updates, or 

responsible for almost 70% of data breaches.91 Second, 

turning on multifactor authentication (MFA), they 

Recommendations for getting 
started with Zero Trust:

cybercriminals are using malware that is posed as a 

may have been spared or less impacted. In fact, it 

• Identities are validated and secured with MFA 

legitimate software update to target unsuspecting 

is shocking that less than 20% of our customers are 

everywhere. Using MFA helps eliminate the need 

employees. Third, ransomware attackers have raised 

using strong authentication such as MFA93 (which 

for passwords. The added use of biometrics (such 

the stakes to focus not only on double or triple 

is free to our customers and can be turned on by 

as retina eye scans or fingerprints) also ensures 

extortion tactics in terms of a payout but are also 

default). Organizations that do not apply or maintain 

strong authentication of a user’s identity.

offering ransomware as a service (RaaS), which uses 

these basic hygiene practices will face much greater 

a partner network to carry out an attack, making it 

exposure to attacks. 

tough to determine who the real bad actor is. Finally, 

adversaries are targeting on\-premises systems, 

Along with the security basics, Microsoft relies on 

reinforcing the need for organizations to move 

an approach called Zero Trust,94 which assumes the 

infrastructure to the cloud where security is more 

network has been breached. Zero Trust means we 

difficult to penetrate.92 

don’t assume any identity or device on our network 

is secure—we continually verify it. Zero Trust helps 

While these incidents taught us tough lessons, a key 

us strike a balance in making sure employees can be 

takeaway is that the basics matter. A primary way 

productive, secure, and healthy beyond the corporate 

criminals get in is through an unlocked door. 

network from home, the office, or anywhere in\-between.

• Devices are managed and validated as healthy. 

As a condition of access to any company resource, 

all device types and operating systems should be 

required to meet a minimum healthy device state 

before being validated. 

• Monitoring and threat signals are pervasive. 

Make sure to collect all available logs, data, and 

signals to understand the current security state, 

which will help you identify gaps in coverage, 

discover anomalies, and drive a better employee 

experience.

ORGANIZATIONS 

THAT DO NOT 

APPLY OR 

MAINTAIN

THESE BASIC 

HYGIENE PRACTICES 

WILL FACE MUCH 

GREATER EXPOSURE 

TO ATTACKS.

91Email scams in particular are surging, according to the cyber defense firm Barracuda. Phishing was responsible for almost 70% of data breaches. https://blog.barracuda.com/2020/03/26/threat\-spotlight\-coronavirus\-related\-phishing/ 

92Through 2024, workloads that leverage the programmability of cloud infrastructure to improve security protection will demonstrate improved compliance and at least 60% fewer security incidents than those in traditional data centers. (How to 

Make Cloud More Secure Than Your Own Data Center, Neil MacDonald, Tom Croll (April 29, 2021\)) 93Based on Azure Active Directory protection telemetry as of August 2021\. 94Zero Trust Security Model and Framework Microsoft Security

\| 

Microsoft Digital Defense Report \| October 2021

89
89

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Our goal with this report is to share insights from 

health situations and local government guidance 

Global pre\-COVID onsite work and the rapid move to remote work, followed by gradual return

our own internal teams who are doing this work 

determines how many employees we allow at a 

each day, to help educate and empower others to 

worksite and what services are made available. Once 

improve their cyber defense techniques to protect 

a location fully reopens, we return to somewhat 

their employees, their companies, and our online 

normal operations with services that were provided 

ecosystem.

pre\-pandemic. As Microsoft offices globally invite 

more employees back to the worksite, we are 

And remember, you can’t secure future work if you 

gradually seeing an increase in the number of 

don’t secure your past work.

employees badging\-in (scanning their badges for 

Moving toward a hybrid 
workforce at Microsoft 

No one knows how or when the COVID\-19 

pandemic will end, but at some point, COVID\-19 

will no longer place a significant burden on 

our communities and will present itself more 

like an endemic virus such as influenza. Local 

building entry) each week. We expect this number 

will continue to rise as more locations fully reopen. 

However, we do not expect these numbers to reach 

pre\-pandemic levels of attendance. Our flexible 

work approach means that we expect to see most 

employees spending at least some time each week 

working remotely, even in locations where COVID\-19 

Global weekly unique badge scans (January – August 2021\)

is no longer a significant burden. 

Learn more:

Securing a new world of hybrid work: What to know and what to do \- Microsoft Security (5/12/2021\)

Work Trend Index: Microsoft’s latest research on the ways we work.

The Next Great Disruption Is Hybrid Work—Are We Ready? (microsoft.com)

Securing Microsoft’s network with an internet\-first, Zero Trust model (4/16/2021\)

90

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work Identities Devices/Endpoints Applications Network

Infrastructure Data People

A Zero Trust 
approach for 
securing hybrid 
work

an urgent opportunity for all companies around 

Assume breach

1\. Identities

the world to adopt a Zero Trust approach and 

Minimize blast radius and segment access. Verify 

Identities can represent people, services, or IoT 

assume all activity, even by trusted users, could be 

end\-to\-end encryption and use analytics to get 

devices. When an identity attempts to access 

an attempted breach. Signals across the industry 

visibility, manage insider risk, drive threat detection, 

a resource, verify that identity with strong 

highlight that every company needs to create a 

and improve defenses.

culture of security and modernize their approach to 

ensure they are protected.

The increasing prevalence of cloud\-based services, 

Zero Trust principles

mobile computing, Internet of Things (IoT), and 

“bring your own device” (BYOD) in hybrid work 

environments has changed the technology 

landscape for today’s enterprise. Security 

architectures that rely on network firewalls and 

virtual private networks (VPNs) to isolate and 

restrict access to corporate technology resources 

and services are no longer sufficient for a workforce 

that regularly requires access to applications and 

resources that exist beyond traditional corporate 

network boundaries. The shift to the internet 

as the network of choice and the continuously 

evolving threats led Microsoft to adopt a Zero Trust 

security model. Zero Trust has become a priority of 

enterprise security leaders around the world.

We are facing a moment of reckoning as the world 

witnesses a rise in increasingly sophisticated and 

expansive cybersecurity attacks. This reality—

coupled with work entering its next great disruption, 

the move to hybrid environments—has ushered in 

Zero Trust eliminates the inherent trust that is 

assumed inside the traditional corporate network. 

An effective Zero Trust architecture is designed to 

reduce risk at every opportunity across the digital 

estate. In practice, this means that every transaction 

between systems must be validated and proven 

trustworthy before the transaction can occur. For an 

effective Zero Trust strategy, we recommend these 

guiding principles:

Verify explicitly

Always authenticate and authorize based on all 

available data points, including user identity, 

location, device health, service or workload, data 

classification, and anomalies.

Use least privilege access

Limit user access with just\-in\-time and just\-enough\-

access (JIT/JEA), risk\-based adaptive polices and data 

protection to help secure both data and productivity.

An integrated security 
philosophy and end\-to\-end 
strategy 

authentication, and ensure access is compliant and 

typical for that identity. Follow least privilege access 

principles.

2\. Endpoints

Once an identity has been granted access to a 

Zero Trust controls and technologies are deployed 

resource, data can flow to a variety of different 

across six foundational technology pillars. Each 

endpoints—from IoT devices to smartphones, BYOD 

pillar is a source of signal, a control plane for 

to partner\-managed devices, and on\-premises 

enforcement, and a critical resource to be defended. 

workloads to cloud\-hosted servers. This diversity 

In a Zero Trust architecture, they are interconnected 

creates a massive attack surface area. Monitor and 

by automated enforcement of security policy, 

enforce device health and compliance for secure 

correlation of signal and security automation, and 

access.

orchestration.

Zero Trust across the digital estate

91

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work Identities Devices/Endpoints Applications Network

Infrastructure Data People

3\. Applications

5\. Infrastructure

Applications and application programming 

Infrastructure—whether on\-premises servers, cloud\-

interfaces (APIs) provide the interface by which data 

based virtual machines (VMs), containers, or micro\-

is consumed. They may be legacy on\-premises, 

services—represents a critical threat vector. Assess 

workloads moved to the cloud, or modern software 

for version, configuration, and JIT access to harden 

as a service (SaaS) applications. Apply controls and 

defense. Use logging and monitoring to detect 

technologies to discover shadow or unsanctioned IT, 

attacks and anomalies, and automatically block and 

ensure appropriate in\-app permissions, gate access 

flag risky behavior and take protective actions.

based on real\-time analytics, monitor for abnormal 

behavior, control user actions, and validate secure 

6\. Data

configuration options.

Ultimately, security teams are protecting data. Data 

4\. Network 

should remain protected throughout its lifecycle 

even if it leaves the devices, apps, infrastructure, 

All data is ultimately accessed over network 

and networks the organization controls. Use data 

infrastructure. Networking controls can provide 

classification and labeling as context to encrypt, 

critical controls to enhance visibility and help 

minimize access to, control the flow of, and mask or 

prevent attackers from moving laterally across 

delete sensitive information at the end of its useful 

the network. Segment networks (and do deeper 

or legally mandated life.

in\-network micro\-segmentation) and deploy real\-

time threat protection, end\-to\-end encryption, 

Learn more:

monitoring, and analytics.

The critical role of Zero Trust in securing our world 

\| 

Microsoft Security Blog

 (6/30/2021\)

Zero Trust adoption

Hybrid workplace intent

The Zero Trust Adoption Report95 illuminates the 

path of Zero Trust adoption across diverse markets 

and industries. We hope that the learning gained 

by this research can help accelerate your own Zero 

Trust strategy adoption, shed light on the collective 

progress of your peers, and provide insights on the 

future state of this rapidly evolving space.

No single security risk area stands out as a primary 

starting point for Zero Trust strategy, as fewer than 

15% start with the same security risk area. 

Organizations are beginning in different places, 

likely based on their needs and available internal 

resources. Most organizations approach Zero Trust 

as an end\-to\-end strategy to be completed over 

time. Eventually, they seek to adopt this strategy 

across all security risk areas to ensure even more 

protection against threats. 

The shift to a hybrid workplace is driving 
broader adoption of Zero Trust strategy. 81% of 
enterprise organizations have begun the move 
toward a hybrid workplace, with 31% already 
fully adopted. 

95 Zero Trust Adoption Report 2021 Based on responses from 900\+ security decision makers familiar with Zero Trust, in a mix of industries. Respondents from US, Germany, Japan, Australia, and New Zealand.

92

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Current zero trust implementation – security risk areas

There is no one\-size\-fits\-all approach to Zero Trust implementation, giving permission to start anywhere.

Learn more:

Zero Trust Adoption Report (7/27/2021\)

Resources for accelerating your Zero Trust journey \- Microsoft Security (5/24/2021\)

Zero Trust Security Model and Framework Microsoft Security

\| 

Identity is more important than ever.

as well as our investments in detection (malicious 

IP address, password spray detection), have caused 

a reduction in password brute\-force attacks that 

use legacy authentication protocols, such as IMAP 

or SMTP. The volume of attacks that we attribute to 

breach replay and password spray have decreased 

significantly, while at the same time we are seeing 

a large increase in attacks attributed to phishing 

or other more sophisticated techniques, such as 

credential harvesting with malware. The data shows 

that bad actors have adapted their tactics to keep 

compromising accounts.

Although blocking legacy authentication and 

enabling MFA are still the most important defenses 

for any organization, phishing protection is 

becoming more relevant than ever. Even with 

MFA enabled, users can still have their credentials 

phished by real\-time man\-in\-the\-middle phishing 

tools that replicate the sign\-in page and replay 

the MFA prompt to collect the one\-time password 

sent to the user. To protect from this type of attack, 

customers can adopt Fido2\-based credentials (based 

on a public key cryptographic key pair), such as 

security keys or Windows Hello for Business.97

Identities

In Azure Active Directory we observe 50 million 

password attacks daily, yet only 20% of users 

and 30% of global admins are using strong 

authentications such as MFA.96 Password\-based 

attacks remain the main source of Identity 

compromise. However, other types of attacks are 

emerging, including consent phishing and attacks 

on nonhuman identities.

Password\-based attacks 

Azure AD is the front door to all Microsoft cloud 

services. Our sign\-in service sees 90 billion 

authentication requests per day, which gives us 

great visibility on identity attacks happening 

across all our clouds. Password\-based attacks on 

user identities are still the most prevalent vector 

of identity compromise. While password spray 

and credential stuffing used to be the largest 

vectors of identity compromise, in the last year, 

we observed a significant change of tactics by the 

bad\-actor ecosystem. In the last few years, but most 

notably during the pandemic, Microsoft and our 

customers have invested significantly in reducing 

the attack surface for bad actors to compromise 

Azure AD–backed accounts. The enhancement of 

security posture (security defaults, MFA adoption, 

password protection, legacy authentication block), 

96 Based on Azure Active Directory protection telemetry as of August 2021\. 97 All your creds are belong to us! \- Microsoft Tech Community

93

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Monthly compromised users by attack category (June 2020 – June 2021\)

Rise in phishing emails using OAuth request URLs

Geo\-distribution of IP addresses issuing 
password brute\-force attacks in July 2021

Emerging trends in attacks

OAuth consent phishing

In typical phishing, an attacker looking to steal 

credentials will craft a convincing email, host a 

fake landing page, and expect the user to fall for 

the lure. On a successful phishing attempt, the 

user credentials are passed on to the attacker. 

Consent phishing is a bit different. This method 

attempts to trick users into granting permissions 

to a malicious attacker\-owned application and uses 

the obtained access tokens to retrieve the users’ 

account data. This is a very sophisticated attack as 

the access tokens do not require knowledge of a 

Microsoft recommends limiting user consent to 

user’s password, and the user’s password is never 

allow user consent only to apps from verified 

shared with the attacker. Most importantly, as this is 

publishers.

not a credential based attack, strong authentication 

requirements such as MFA do not prevent attacks 

Microsoft has deployed several defenses to counter 

that use this technique.

this trend, including specific machine\-learning\-

based detections to identify, isolate, and disable 

In the last six months, the monthly average of 

malicious applications. Strategies that can help 

phishing emails using OAuth URLs has almost 

prevent such attacks include granular user consent 

doubled. These phishing emails target a variety of 

policies, blocking consent\-phishing emails, anomaly 

legitimate cloud services such as Microsoft, Google, 

detection, and user awareness training.

and Facebook. We are seeing an upward trend in the 

number of unique emails with OAuth phishing links.

94

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Attacks on nonhuman accounts 

The challenge of credentials in code is not a new 

We saw a significant uptick in the volume of 

one. While most major vendors including Azure 

attacks against applications and service principal 

DevOps and GitHub offer safeguards to flag such 

identities.98 Unlike users, these identities are often 

credentials for removal, the practice persists. Those 

more vulnerable because organizations do not 

credentials provide attackers a direct path into 

consistently apply many of the typical safeguards 

an organization’s environment while flying under 

such as strong authentication, rigorous lifecycle 

the radar in the Azure AD Audit logs. Microsoft 

management, and security monitoring to this 

recommends that customers audit their engineering 

category of accounts. As a result, we have seen 

artifacts, including code repositories for credentials.

As a result of these countermeasures, there was 

For more information on phishing trends and 

an 89% increase in disabled apps from January to 

mitigation, see the State of cybercrime chapter of 

June 2021 compared to July to December 2020\. 

this report.

Upon detailed investigation, we saw that the major 

malicious vectors have shifted from a multi\-tenant 

Learn more:

attackers exploiting application identities that 

already have a privileged role or are scoped to a 

wide set of permissions. Unlike the typical “Initial 

Access \-\> Privilege Escalation” attack chain, 

this attack vector gains initial access through a 

compromised user or a leaked application credential.

We have seen attackers who gain initial access 

through a compromised user use their elevated 

privilege to conduct reconnaissance to identify 

applications with existing permissions, add a new set 

of application credentials if needed, and even assign 

privileged roles to the application. As a result, the 

application behaves normally in the environment 

while still operating as a tool for the attacker. 

phishing attack to an abusive type of attack.

Microsoft delivers comprehensive solution to battle 

Customers should conduct a review of application 

rise in consent phishing emails Microsoft Security 

\| 

roles and permissions to conform to the principle 

Hackers don’t break in, 
they log in.

Blog

 (7/14/2021\)

of least privilege and monitor their Azure AD Audit 

logs for unfamiliar activity on applications and 

service principals.

Adoption of security posture

Strong authentication adoption

For identities, verifying explicitly means ensuring 

the identities are using strong authentication when 

accessing resources. Microsoft research shows that 

requiring strong authentication can protect against 

99\.9% of the identity attacks because the majority 

of the attacks are related to passwords. While 

augmenting passwords can help defend against 

those attacks, eliminating passwords altogether 

with passwordless authentication methods can 

provide the most usable and secure authentication 

experience.

As companies have been adapting their security 

posture for remote work and a hybrid workforce, 

we have seen over 220% increase in strong 

authentication usage in the last 18 months. 

98 Apps \& service principals in Azure AD \- Microsoft identity platform Microsoft Docs

\| 

95

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Strong authentication usage in Azure AD

Growth in Zero Trust access policy usage

Azure AD Conditional Access is a security policy engine for verifying explicitly and granting least privilege 

access. In the last year, the number of conditional access policies deployed has more than doubled, as 

organizations revamped their security postures to account for a remote workforce.

When a user accesses an application, administrators can use conditional access to configure which additional 

requirements are enforced to grant access. As organizations embrace Zero Trust security principles, we have 

seen greater adoption in managed device and managed app requirements in addition to MFA.

Most frequently required access controls in Azure AD (July 2020 – June 2021\)

Microsoft enables security defaults for all new customers to ensure that everyone has at least a basic level of 

protection, including controls like MFA for administrators.99

Tenants with security defaults enabled

99 Azure Active Directory security defaults Microsoft Docs

\| 

96

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Legacy protocols: A preferred entry point for adversaries

One of the leading sources of compromise in organizations is authentication from legacy protocols, such 

as IMAP, SMTP, POP, and MAPI. These protocols do not support MFA, so they are preferred entry points for 

adversaries. In fact, 99% of password spray and 97% of credential stuffing attacks use legacy authentication, 

according to authentication data from Azure AD. Data from Azure AD reveals that the compromise rate for 

authentications using IMAP clients is 22 times higher than the compromise rate for authentications from 

a browser. 

Fortunately, end users and admins have begun making progress toward using modern authentication in 

their organizations.

The hybrid world is largely “perimeterless,” so wrapping protections around identity and devices is critical. As 

part of Zero Trust, we also think the future is passwordless,100 and we will start to see that transition this year.

Account compromise rate by authentication protocol (July 2020 – June 2021\)

Percentage of legacy authentication among monthly active users of Azure Active Directory

Over the past year, we have seen the percent of users with legacy authentication clients decrease over 
30% to nearly 10% of users in Azure AD.

100 Preparing your enterprise to eliminate passwords (microsoft.com)

97

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Devices/Endpoints 
What we’re seeing 

Mostly driven by necessity as the world shifted to a remote or hybrid work model, users are working from 

Recommendations for mitigating BYOD risk

To mitigate the increased risks of any BYOD model, it’s important to ensure constant verification of specified 

security standards as well as validation of the identity of the device and user to gate control of critical company 

resources. For example, you can block access to a personal device that has been jailbroken (modified to remove 

restrictions imposed by the manufacturer or operator) to ensure that enterprise applications are not exposed to 

anywhere, from any device, more than any time in history, and attackers are quickly adjusting their tactics to 

known vulnerabilities.

take advantage of this change. Enterprises are left weighing the benefits of enabling BYOD (allowing their end 

users to access corporate resources that traditionally required VPN or on\-premises access) against the increased 

risk of the same users unintentionally installing ransomware or other malware while performing non\-work\-

For more information on securing devices, see the Supply chain, IoT, and OT security chapter of this report.

related functions on their personal devices. By enabling BYOD using a Zero Trust model, enterprises can reduce 

Learn more:

provisioning costs and avoid additional hardware purchases for work\-from\-home use, but they need to be able 

to protect their corporate assets on these devices, while still allowing the users to perform non\-work functions 

on these same devices.

Mobile device management (Intune data)

Protect Data and Devices with Intune Microsoft Docs

\| 

Device compliance policies in Microsoft Intune \- Azure Microsoft Docs

\| 

 (4/29/2021\)

What is Conditional Access in Azure Active Directory? Microsoft Docs

\| 

 (1/27/2021\)

Sharp rise in mobile device management growth as workers moved from office to BYOD and home PCs

98

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Applications 
Moving from legacy to Zero 
Trust–ready applications

As we move from a security model centered on 

the corporate network to one based on identities, 

thousands of apps and services with internally facing 

posture remain heavily reliant on network firewalls 

and VPNs to isolate and restrict access. They were 

built around legacy authentication mechanisms, 

keeping them grounded within corporate networks. 

These traditional architectures built for legacy apps 

were designed for lateral connectivity rather than 

micro segmentation. They violate the fundamental 

principle of least privilege access and are more 

vulnerable to lateral movement across the network 

by an adversary, which in turn could expose 

confidential data. For more on recent attack trends 

Learn more:

Build 2021: Build Zero Trust\-ready apps with the Microsoft 

identity platform \- Microsoft Tech Community (5/26/2021\)

Integrated Threat Protection Microsoft Security

\| 

Safeguard your multicloud resources Microsoft Cloud 

\| 

Security

in this area, please see the Legacy protocols and 

OAuth consent phishing sections of this report.

Using modern apps and data 
solutions

In a cloud\-centric architecture, we treat our 

applications and data differently. With more user\-

design models becoming available, engineers 

no longer function as the only developers in 

an organization. Users are taking advantage of 

platforms and tools that offer no\-code or low\-code 

development methods to create business solutions. 

Organizations should invest in creating the right 

guardrails for these new paradigms. Tracking 

cloud resources and applying correct policies and 

templates help to ensure that modern solutions 

immediately use the correct controls.

How do you modernize applications? Successfully deploy one of the three solutions listed here:

MODERNIZED 

APPS AND 

SERVICES 

REQUIRE 

USERS TO BE 

AUTHENTICATED 

PRIOR TO 

HAVING 

ACCESS.

Microsoft Digital Defense Report \| October 2021

99
99

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network Infrastructure Data People

Top 5 most common protocols used in 
network exploit attempts (July 2021\)

Network 

A Zero Trust approach encourages organizations 

to assume they are always under attack and 

that a security incident can happen at any time. 

To be prepared with a setup that minimizes the 

blast radius of such an incident, networks should 

be segmented when the layout is designed. 

Implementing these software\-defined perimeters 

with increasingly granular controls will increase 

the “cost” to attackers to propagate through the 

network and thereby dramatically reduce the lateral 

movement of threats.

What we’re seeing in Azure 
Firewall signals 

Customers are using network segmentation for 

organizing workloads and deploying firewalls for 

securing traffic across subnets, VNETs, to on\-

premises, and to the internet. Customers are using 

firewalls to control and enhance visibility into all the 

network flows.

Web application firewall 

Web application firewalls (WAFs) have evolved from 

an initial focus on injection\-type attacks, such as 

SQL injection and cross\-site scripting, to include 

attacks from malicious bots and API abuses. When 

combined with distributed denial of service (DDoS) 

protection, WAF forms an integral part of defense\-

Most common network 
attack types 

Azure Firewall blocks millions of attempted 

exploits daily. Our signals show that attackers 

most commonly used malware, phishing, web 

applications, and mobile malware in their attempts 

at network attacks during July 2021\. Also in 

July, there was a significant uptick in the use of 

coinminers, a type of malware that uses the network 

to mine cryptocurrency. 

The protocols leveraged most often in attacks were 

HTTP, TCP, and DNS, as they are open to the internet. 

in\-depth strategy for protecting web and API assets.

Top 10 network threats (July 2021\)

WAF over the past year has upwards of 25 billion 

As migration to cloud accelerates, we are seeing that 

rules triggered on a per\-week basis. Approximately 

most new deployments are hybrid with connectivity 

4% to 5% of incoming traffic on average is deemed 

back to on\-premises and configured for internet 

malicious and is blocked either at the network edge 

breakout (micro perimeter) from Azure. All data is 

or at the regional data center depending on where 

ultimately accessed over network infrastructure. 

WAF is configured.

100

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network Infrastructure Data People

DDoS attacks 

In our 2020 DDoS retrospective,101 we highlighted 

shifts in the very active cyberthreat landscape. With 

the COVID\-19 pandemic and an increase in internet 

traffic, DDoS attacks on internet\-facing endpoints 

ramped up significantly. We continue to see similar 

trends in the first half of 2021 as well. The trend is 

characterized by large TCP attacks, mainly SYN, SYN 

ACK, and ACK floods and user datagram protocol 

(UDP) reflection attacks. Online gaming and the 

gaming vertical continues to be a very attractive 

target of DDoS attacks. The majority of attacks on 

the gaming vertical have been mutations of MIRAI 

botnets and low\-volume UDP protocol attacks. 

There is also an uptick in DDoS attacks against IPv6 

Attack duration

Attack vectors, applications, and regions 

this year. This is an indication that as more IPv6 is 

Microsoft’s DDoS Protection team continues to see 

involved

adopted in the enterprise networks, the risk of DDoS 

that most attacks are of short duration, with 75\.35% 

More than 35% of the attack volume targeted 

attacks on IPv6 will continue to increase.

being 30 minutes or less and 87\.60% being one hour 

HTTPS and 10% targeted HTTP. UDP attacks 

or less. This trend is similar to what we observed 

represented 43% of the overall attack vectors, with 

Daily attacks and volume

in 2020\.

Compared to the latter part of 2020, the average 

daily number of attack mitigations in the first half 

of 2021 increased by 25% while the average attack 

bandwidth per\-public IP increased by 30%. Azure 

DDoS Protection mitigated 1,200 to 1,400 unique 

DDoS attacks every day in the first half of 2021\. As 

of July 2021, the average attack size in 2021 (325 

Gbps) was 25% larger than in 2020 (250 Gbps). 

amplification attacks accounting for 11% of attacks. 

Besides DNS and NTP reflection attacks, there has 

been a surge in remote desktop protocol (RDP) and 

datagram transport layer security (DTLS) reflection 

attacks.

DDoS attack mitigations

Attack Duration (July 2020 – June 2021\)

DDoS attack type (July 2020 – June 2021\)

Number of unique DDoS attacks mitigated daily by Microsoft

Over 96% of the attacks are of short duration 
(\<4 hours)

101 Azure DDoS Protection—2020 year in review Azure Blog and Updates Microsoft Azure

 \|

 \|

101

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network Infrastructure Data People

The average packet size of TCP flood has been 

Learn more:

Top 10 DDoS attack destination regions

DDoS Protection and Mitigation Services Microsoft 

 \|

Azure

 \|
Azure DDoS Protection Standard documentation 

Microsoft Docs

much smaller compared to UDP attack packets. UDP 

Fragment attacks averaged 1145 bytes per packet 

while TCP invalid syn averaged 512 bytes. TCP attack 

vectors such as SYN ACK, TCP Zero Seq, FIN\-ACK 

and RST Floods averaged below 100 bytes per packet.

Europe, Asia, and the United States remain the most 

attacked regions because of the concentration of 

financial services and gaming industries in these 

regions. The UAE has been increasingly hit by DDoS 

attacks on government, oil and gas, telecom, and 

healthcare industries/sectors.

Top source regions from where the DDoS attacks 

originated were from Russia, Romania, Turkey, 

Indonesia, Vietnam, and the Philippines, owing to 

the prevalence of DDoS attack\-for\-hire services in 

those regions.

102

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network Infrastructure Data People

Cybercriminal DDoS services 

Between November 2020 and May 2021, the 

average price of a DDoS attack increased over 500%. 

The reasons for the price increase are multifaceted:

The rising cost of goods sold for DDoS services 

has made them more expensive and resulted in a 

decrease in supply relative to demand.

• The price for loads that are turned into DDoS 

bots increased as demand for loads for all 

monetization strategies increased beyond 

supply. (Loads are freshly infected devices 

which are sold to third parties, who install their 

malware on the device.) Attackers have found 

more effective strategies to monetize loads that 

are delivering more value than they would get 

using them for DDoS attacks. These include 

Average price of DDoS attack services

buying loads to conduct ransomware, spyware, 

Starting in late June, the advertised cost of DDoS 

Learn more:

Sharing how Microsoft now secures its network with a 

Zero Trust model \- Inside Track Blog (4/22/2021\)

Zero Trust networking: Sharing lessons for leaders 

(microsoft.com) (1/5/2021\)

Lessons learned in engineering Zero Trust networking 

(microsoft.com) (1/5/2021\)

adware, and banking theft monetization 

services decreased back toward the equilibrium that 

was observed until November 2020\. This shift was 

likely caused by two factors. First, there was a recent 

increase in the supply of fresh loads available for 

purchase from the DDoS services. Second, there was 

a decrease in ads for premium DDoS services. The 

margins for DDoS services were being squeezed by 

increased costs and lack of demand for high\-priced 

DDoS services, leading some of the premium DDoS 

services to move from a “publicly available service” 

in the cybercriminal forums to more private services 

that don’t advertise.

strategies. 

• Some antivirus products use outbound DDoS 

attacks to detect malware. Therefore, the 

lifecycle of the bots used in DDoS attacks is 

shorter than it used to be, requiring the DDoS 

service to continuously buy new loads to 

maintain their capabilities. 

• Improved DDoS mitigation strategies make it 

more complex to perform quality attacks.

It has become more common for actors that want 

to conduct DDoS attacks to rely on these DDoS 

services to conduct them. As a result, many attackers 

no longer have the skills or infrastructure to conduct 

their own DDoS attacks. In other words, costs are 

rising due to lack of alternatives.

103

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Infrastructure 

Infrastructure represents a critical threat vector. 

IT and applications infrastructure, whether on\-

premises, in the cloud, or multi\-cloud, is defined as 

all the hardware (physical, virtual, containerized), 

software (open source, first\- and third\-party, 

platform as a service (PaaS), SaaS, functions, and 

APIs), micro\-services, networking infrastructure, 

and facilities that are required to develop, test, 

deliver, monitor, control, or support IT services 

and applications. It is an area where Microsoft 

has invested tremendous resources to develop a 

comprehensive set of capabilities to secure future 

cloud and on\-premises infrastructure.

Collaboration with MITRE on 
an ATT\&CK\-style matrix

The flexibility and scalability of containers encourage 

many developers to move their workloads to 

Kubernetes, an open\-source system for automating 

deployment, scaling, and managing containerized 

applications. While Kubernetes has many 

advantages, it also brings new security challenges 

that should be considered. Therefore, it is crucial 

Learn more:

to understand the various security risks that exist 

in containerized environments, and specifically in 

Kubernetes.

The evolution of a matrix: How ATT\&CK for 

Containers was built Microsoft Security Blog 

 \|

(7/21/2021\)

Threat matrix for cloud storage 

As the move to the cloud enables a more secure 

hybrid workforce, organizations are also increasing 

their dependency on cloud storage services. They 

The MITRE ATT\&CK framework is a knowledge base 

of known tactics and techniques that are involved 

in cyberattacks. Started with coverage for Windows 

and Linux, the matrices of MITRE ATT\&CK cover 

the various stages that are involved in cyberattacks 

(tactics) and elaborate the known methods in each 

one of them (techniques). Those matrices help 

Threat matrix for Kubernetes (microsoft.com) 

require effective threat protection, mitigation 

(5/10/2021\)

strategies, and tools in place to manage access to 

Secure containerized environments with updated 

their cloud storage. For example, Azure Defender 

threat matrix for Kubernetes Microsoft Security Blog 

 \|

treats data\-centric services, such as cloud storage 

(3/23/2021\)

Crypto\-Mining Attacks Targeting Kubernetes Clusters 

via Kubeflow Instances (6/9/2021\)

organizations understand the attack surface in their 

Update: Help Shape ATT\&CK for Containers 

environments and make sure they have adequate 

(2/18/2021\)

detections and mitigations to the various risks.

When the Azure Security Center team began 

mapping the security landscape of Kubernetes, they 

noticed that although the attack techniques are 

different than those targeting Linux or Windows, the 

tactics are similar. For example, a translation from 

OS to container clusters would be “initial access to 

the computer,” which becomes “initial access to the 

cluster.” So, the team created the first Kubernetes 

attack matrix: an ATT\&CK\-like matrix comprising 

the major techniques that are relevant to container 

orchestration security.

accounts and big data analytics platforms, as part 

of the security perimeter and provides prioritization 

and mitigation of threats for data storage. As 

Microsoft cloud security researchers examined 

the attack surface of storage services, they noted 

potential risks to be aware of when deploying, 

configuring, or monitoring a storage workload. 

We’ve produced a threat matrix for storage102 to 

help organizations identify gaps in their defenses. 

We expect the matrix to dynamically evolve as more 

threats are discovered and exploited, and techniques 

can also be deprecated as cloud infrastructures 

constantly progress toward securing their services.

Learn more:

Safeguard your multicloud resources Microsoft Cloud 

 \|

Security

Threat matrix for storage services \- Microsoft Security 

(4/8/2021\)

Infrastructure represents a critical threat vector.

102 Threat matrix for storage services Microsoft Security Blog

 \|

104

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

Data 

Digital transformation and tech intensity103 have led 

to exponential data growth, and organizations are 

dealing with never\-before\-seen volume, velocity, 

and variety of data. This growth, combined with 

increasingly remote workforces and cloud migrations, 

has created a complex data sprawl often pitting 

security and regulatory requirements against the 

access business needs to deliver value from that data.

Data governance is an integral 
part of data security

Organizations that effectively manage the lifecycle 

and flow of their sensitive data as part of their 

business operations make it that much easier for 

data security and compliance teams to reduce 

their privacy data footprint and surface of attack to 

and security principles as organization evolve their 

exposure and manage risk.

achieve sustainable compliance. These security and 

applications and infrastructures or take on new 

As valuable as data is to organizations, data value 

similar approaches with other sensitive or regulated 

can drop faster over time than the risk associated 

datasets.

Learn more

compliance benefits can also be achieved by using 

business ventures.

with it.104 Accumulating sensitive data through 

management neglect is not only wasteful from 

Reducing the risk associated with data is not only 

a storage perspective but it can also be a recipe 

about pruning old data and securing it where it 

for accumulating risk. In a rapid data growth 

resides now. It is also about reevaluating how the 

environment, it is not difficult to envision that data 

organization conducts business with sensitive data 

governance will increasingly have an impact on data 

going forward to ensure proper storage, access, 

security.

flow, and lifecycle so that this sensitive data does 

not persist or propagate uncontrollably. 

There is a lot to be learned and reused from recent 

privacy initiatives. Successful organizations with 

Over time, this means reengineering high\-risk 

mature privacy processes have inherently had to 

business processes and adhering to data governance 

 \|
Azure Purview for Unified Data Governance 

Microsoft Azure

Information Protection and Governance 

 \|

Microsoft 365

Microsoft Information Protection in Microsoft 

365 \- Microsoft 365 Compliance Microsoft Docs 

 \|

(8/26/2021\) 

Microsoft Information Protection and Microsoft Azure 

Purview: Better Together \- Microsoft Tech Community 

(12/7/2020\)

combine data governance and security to minimize 

Cumulative impact of unified data governance and security on sensitive data risk

Information rights management use (July 2020 – June 2021\)

Dip in the chart correlates to decreased usage during major holidays

103 How technology intensity accelerates business value – Microsoft Industry Blogs 104 Implement Your Data and Analytics 

Governance Through 5 Pragmatic Steps. Published 6 July 2020 – ID G00729295 – By Guido De Simoni, Saul Judah

Data governance can maximize the business value of data while helping minimize the security and 
compliance risk of that data.

105

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

People 

Some guidance about insider 
risk in the hybrid workplace 

Helping people adapt to new ways of working 

As described in this report’s sections on Zero Trust, it 

is key to any successful transformation. While 

is possible to give employees seamless information 

organizations are empowering people to work 

access while mitigating the risk of inadvertent leaks. 

securely when, where, and how they want, we have 

Regarding more malicious insider threats, using a 

found the most successful are the ones who are also 

framework of common factors and patterns typically 

empathetic to the end\-user experience. 

seen helps to enable proactive detection. Microsoft’s 

Insider Risk program has adapted numerous 

The previous sections of this chapter have presented 

a view of the threat landscape across the six 

Insider threat attack path105

preventative and detective controls that decrease 

to share files) are both initiatives that Microsoft has 

risk through all stages of the insider threat attack 

undertaken to mitigate risk. As organizations work 

path. In general, we should assume that the threat of 

toward increasingly advanced capabilities in the 

loss to the organization or its stakeholders increases 

preventative control space, appropriate stakeholders 

as an attack progresses down the path. Preventative 

from across the organization should always be 

controls such as awareness trainings that instruct the 

consulted. For example, before implementing any 

organization where to report insider threat concerns, 

preventative controls, verify with the business that 

or controls designed to limit risky behavior (such as 

protections still enable employees and contractors 

limiting the ability for those leaving the organization 

to perform their legitimate business activities.

foundational pillars of Zero Trust, with key steps 

we recommend taking to protect them. However, 

it is imperative to remember that every step we 

take to implement Zero Trust strategies impacts the 

people within the organization—and that successful 

implementation depends as much on them as it 

does on the systems and tools we put in place. How 

companies engage with their workforces around 

remote work and security matters. We conclude 

the chapter with a discussion about people, the 

human element of any enterprise, and ultimately our 

greatest asset. 

Insider threat attacks share several common factors and patterns, which can be described in a critical\-path 
approach. Identifying indicators across phases of the critical path can help to enable more proactive detection.

105 Adapted from Eric Shaw and Laura Sellers, Application of the Critical\-Path Method to Evaluate Insider Risks, Studies in Intelligence, 59,2\. 2021

106

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

The Insider Risk program leverages a variety of 

Key considerations for insider threat detections

artificial intelligence (AI) and machine learning (ML) 

and signature\- or rule\-based detections, including 

those from our Insider Risk Management solution, 

AI and ML are not 
always the answer 

Rules and signature\-based detections are better suited for some use cases

to accomplish detection goals. While AI and ML are 

incredible tools that help to decrease some of the 

noise associated with traditional rule\-based alerts, it 

Data is key

An effective AI or ML solution requires understanding and acquiring the data to 
develop, train, and enrich the solution, as well as track performance metrics

is critical that the organization has the appropriate 

You still need people

Human review of alerts and identification of tuning opportunities is critical – 
continue to “shift left”

Cybersecurity talent 
pool is evolving

While security experts are still important, data scientists also bring valuable 
skills to the table

people with the “tribal knowledge” of business\-

acceptable behavior in the correct roles to create 

trustworthy AI and ML models. This human input 

takes standard supervised or unsupervised ML a 

step further in predicting which alerts are the most 

actionable for incident response teams. Lack of this 

knowledge can create a pool of noisy alerts with 

limited investigative value. 

AI and ML are not always the answer

107

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction A Zero Trust approach for securing hybrid work

Identities Devices/Endpoints Applications Network

Infrastructure Data People

The empathy imperative

Flexible work is here to stay and with that comes 

several challenges and stressors. Teams have 

become more siloed this year, and digital exhaustion 

is a real and unsustainable threat. One in five global 

survey respondents say their employer doesn’t care 

about their work\-life balance.106 Fifty\-four percent 

feel overworked. Thirty\-nine percent feel exhausted. 

And trillions of productivity signals from Microsoft 

365 quantify the precise digital exhaustion workers 

are feeling.

A positive corporate culture mitigates risk

A recent study out of CyLab, Carnegie Mellon 

University’s Security and Privacy Institute, found 

that negative deterrence actions like employee 

constraints, monitoring, and punishment don’t work 

to reduce insider risk.107 What does work: putting 

employee engagement, connection, and well\-being 

front and center.

To support the well\-being of your people, it’s 

Learn more:

important to create channels and mechanisms to 

listen to their concerns, providing an opportunity 

to give and receive feedback and embrace 

collaboration. Taking a holistic, purpose\-built 

approach that can pull signals together into a 

cohesive view across an organization provides a 

better understanding of the relevant trends in the 

organization and better risk reduction. For this 

reason, organizations are turning to ML to uncover 

To Thrive in Hybrid Work, Support Flexibility in Work 

Styles (microsoft.com) (9/9/2021\)

Insider risk: Protect company data with insider 

goodwill — Quartz (qz.com) (June 2021\)

Data security: Eliminating insider risk in the hybrid 

workplace — Quartz (qz.com)

Learn about insider risk management \- Microsoft 365 

Compliance Microsoft Docs

 \|

 (3/17/2021\)

hidden signs of workplace risk such as inappropriate 

Reducing Code of Conduct and Regulatory 

communications, threatening behavior, or actions 

Compliance Violation Risks \- Microsoft Tech 

that would negatively impact employees and the 

Community (5/12/2021\)

business. By identifying patterns and violations, 

Fostering safe communication at work \- The 

technology can flag risk while intervention is still 

Washington Post (11/17/2020\)

possible, while continuing our commitment to end\-

user privacy.

Microsoft Customer Story\-Avanade uses a light 

touch—and Microsoft Insider Risk Management—

to lessen insider risk

 (3/24/2021\)

Assume positive intent; mistakes happen.

106 Work Trend Index: Microsoft’s latest research on the ways we work 107 How a positive hybrid work culture can help you to mitigate insider risk \- Microsoft Security (5/17/2021\)

Microsoft Digital Defense Report \| October 2021

108
108

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

CHAPTER 6 

Disinformation

Introduction

Disinformation as an emerging threat

Mitigation through media literacy 

Disinformation as an enterprise disruptor

Campaign security and election integrity

109

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

INTRODUCTION: Critical attention required on the increasing 
sophistication and scope of disinformation

ERIC HORVITZ, CHIEF SCIENTIFIC OFFICER

Disinformation refers to the deliberate use of false information with the intention of influencing public opinion. 
Efforts to fabricate falsehoods for the purposes of manipulating the masses have a long history. However, new 
forms of disinformation have come to the fore over the last decade, enabled by advances in computing methods 
and infrastructure that have transformed the power, scope, and efficiency of disinformation campaigns. 

Widely used consumer platforms and services, such as social media, creator platforms, search engines, and messaging 
services, now provide state and non\-state actors with powerful channels for distributing disinformation. Beyond 
channels, these services provide malevolent actors with ready\-made tools to experiment, monitor, iterate, and 
optimize the impact of disinformation campaigns. 

Commercial online platforms have been harnessed by 

manipulated or taken out of context in disinformation 

individuals and groups and to generate personalized 

these actors as engines of disinformation to power 

efforts, often with dramatic effects. However, technologies 

programs of disinformation aimed at influencing 

messaging programs aimed at political influence, 

for generating deepfakes are providing malevolent actors 

beliefs, opinions, and actions.

polarization, and chaos. Disinformation strategies are 

with powerful, general palettes for fabricating behaviors 

growing in sophistication, including the concerted use of 

and events. These methods are injecting new powers of 

The repurposing of consumer computing 

multiple services108 to reinforce messages across platforms.

persuasion into disinformation campaigns.

infrastructure, use of tools for generating synthetic 

On a second front, advances in machine learning (ML) 

In a third area of concern, artificial intelligence (AI) 

operations are troubling separately and in synergy. 

and graphics have led to widely available tools for 

methods can be used by state and non\-state actors to 

Together, they are supercharging disinformation, 

fabricating high\-fidelity audiovisual content, referred 

formulate and drive powerful psychological operations 

with grave implications for the health and vibrancy of 

to as synthetic media and deepfakes. For decades, 

that leverage insights and data about human 

democracies that depend critically on educated and 

photos and comments by political leaders have been 

cognition. ML and reasoning can be used to profile 

aware citizenries.

media, and harnessing AI to guide psychological 

THESE 

METHODS 

ARE INJECTING 

NEW POWERS OF 

PERSUASION INTO 

DISINFORMATION 

CAMPAIGNS.

108 Characterizing Search\-Engine Traffic to Internet Research Agency Web Properties Proceedings of The Web Conference 2020 (acm.org)

 \|

Microsoft Digital Defense Report \| October 2021

110
110

Microsoft Digital Defense Report \| October 2021 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

What might we do in the face of these 

can be aimed at identifying primary locations 

developments? 

and organizational sources of disinformation. 

Finally, there are promising developments with 

We need to critically attend to the increasing 

technologies that employ a set of methods, including 

sophistication and scope of disinformation—and to 

cryptography, security, and database technologies in 

engage on multiple fronts. First and foremost, we 

production tools and pipelines that serve to certify 

need to invest deeply in modern media literacy, to 

the origin and history of edits to online media 

educate people about how to understand, expect, 

content, referred to as the provenance109 of the 

and recognize disinformation and misinformation. 

content. Exciting progress with media provenance 

Work on media literacy extends beyond education 

and authenticity is being nourished by strong cross\-

and includes efforts to provide new kinds of tools 

organization collaborations.

that can help people to critique the source and 

veracity of news and information. Second, we need 

We are facing unprecedented disinformation 

to support high\-quality journalism, including trusted 

campaigns and related cyber operations by state 

news organizations. It is essential to have committed 

and non\-state actors. These campaigns target public 

reporters on the ground to see, hear, and report with 

awareness and knowledge with disinformation, while 

clarity on events and incidents. In addition, we need 

others target enterprise operations and confidence. 

to assure the health and vibrancy of local journalism.

It is important to stay aware of developments and 

to come together to address the challenges with 

Disinformation 
as an emerging 
threat 

The general motive to spread disinformation is 

to damage the reputation of an entity, mislead 

consumers about the information, or influence 

the outcome of a proscribed event. It is one of the 

greatest threats to democracy, open debate, and 

free and modern society.

Disinformation has been a steadily evolving method 

of information warfare, most recognized in the 

United States after the 2016 election, but well\-

known globally since the Cold War. This approach 

is high\-stakes and effective for creating social 

discord, increasing polarization, and in some cases, 

influencing the outcome of elections. Nation state 

actors with geopolitical aspirations, proponents 

of radical ideologies, violent extremists, and 

economically motivated enterprises can manipulate 

online narratives with easy and unprecedented reach 

and scale, creating significant societal impact.

Commodity cloud computing, open\-source research, 

AI tools and algorithms, and the speed and scale of 

social media have created a perfect storm for the 

rise of disinformation and malicious synthetic media 

popularly dubbed deepfakes.110 AI techniques to 

create hyper\-realistic digital falsification, also known 

as deepfakes, include manipulated audio, video, 

images, and text, which will seriously challenge 

our ability to discern truth from falsehood. In this 

report, we use the term “deepfake” as AI\-generated 

manipulated media used for malicious purposes. 

On the technical front, there is promise in applying 

awareness, technologies, and policies. Addressing 

Mapping the problem

AI pattern recognition technologies to detect patterns 

the new and evolving challenges will take ongoing 

of communications and content that reveal an intent 

investments, innovation, and activity on multiple 

to deceive. Such work includes efforts to identify 

fronts. This important chapter reviews some 

audiovisual and text\-based media as fabricated. On 

of these challenges and provides insights on 

another front, efforts in networking technologies 

directions forward.

109 A promising step forward on disinformation – Microsoft On the Issues 110 Despite its popular usage, this term technically refers to a specific type of 

ML (a process by which exposure to large and diverse amounts of data allows a computer to improve its own performance) that uses layered neural 

networks (computer processors connected in a way that mimics how information travels in the human brain) to enhance the accuracy of the ML 

algorithms. Deepfakes use two algorithms: the first algorithm creates a video, and the second one tries to determine if the video is real or not. If the 

second algorithm can tell that the video is fake, the first algorithm tries again, until the resulting image looks sufficiently believable.

111

Microsoft Digital Defense Report \| October 2021 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

In the attention economy, websites and platforms 

earn revenue from the time users spend on 

them. This advertisement\-based business model 

incentivizes recommendation engines and curated 

timelines with clickbait headlines and scandalous 

news, opinions, and falsehoods. The timeline 

curation algorithms give rise to creating echo 

chambers, filter bubbles, and unintentional tribalism. 

Because of echo chambers and filter bubbles, 

users predominantly see the content that matches 

their beliefs, biases, and desires, reinforcing their 

confirmation bias and filtering out opposing 

viewpoints. Nefarious actors misuse the attention 

economy and take advantage of the advertisement 

business model to manipulate social media 

narratives to create divisions and sow discord.

“Filter bubbles” and “echo chamber”

Parallels in cybersecurity

Cyberattacks compromise the confidentiality, 

integrity, and availability of digital systems. The 

difference between a disinformation attack and 

a cyberattack is the target; disinformation is also 

an attack and compromise of our cognitive being. 

While cyberattacks are exploits of computer 

infrastructure to create disruption, disinformation 

exploits human infrastructure (our inherent 

cognitive biases, logical fallacies, and psychological 

vulnerabilities), and the attack compromises logical, 

analytical, and critical thinking.

We can therefore think of the threat posed by 

disinformation and computational propaganda 

as cognitive hacking. A cognitive hack attempts 

to change the target audience’s thoughts and 

actions using disinformation to manipulate the way 

they perceive reality. Nefarious actors accomplish 

cognitive hacks utilizing various techniques, 

including manipulating, mis\-contextualizing, or 

misappropriating information. Ultimately, these 

hacks can create social discord, exacerbate 

polarization, influence election outcomes, disrupt 

democratic principles, enable financial fraud, and 

threaten life and property.

Both disinformation and cyberattacks are used by an 

adversary to achieve disruption. A well\-coordinated 

disinformation campaign can fill the broadcast 

and social channels with false information and 

noise, creating narratives that play with emotions 

and drown out the true narrative. This maneuver 

is similar to a distributed denial of service (DDoS) 

attack that floods the target services and networks 

with superfluous requests to connect and overload 

the system to prevent legitimate requests from 

being fulfilled. Disinformation can also be used 

for social engineering threats on a mass scale. Like 

phishing attacks to compromise IT systems for 

data extraction, disinformation campaigns play on 

emotions, giving cybercriminals another feasible 

method for scams. Deepfake videos and audio 

can trick employees into releasing or sharing login 

credentials, which can then be used to gain access 

to an enterprise’s network.

Deepfakes 

Deepfakes are photos, videos, or audio files 

manipulated by AI in hard\-to\-detect ways. The 

weaponization of deepfakes can have a massive 

impact on an economy and national security. 

By eroding public trust in the media, deepfakes 

undermine the credibility of journalism. As this 

credibility is eroded, deepfakes also give rise to the 

“Liar’s Dividend” phenomenon. In an environment 

where it is unclear what is real and what is fake, it 

becomes easier to discount any inconvenient or 

unpopular truth as fake. As an example, deepfakes 

could enable a public figure to claim that their real 

actions are just a fake.

The proliferation of deepfake technology can directly 

harm individuals. Deepfake pornography has been 

used to objectify and victimize people without 

consent, especially women or those who identify 

as women. This revenge pornography is now a 

significant problem: over 96% of deepfake videos 

In the attention economy, users are increasingly exposed only to information that matches 
their preferences (blue areas in the graphic). Filter bubbles represent algorithms that choose 
content based on the user’s previous search histories and other online activity.

112

Microsoft Digital Defense Report \| October 2021 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

are nonconsensual pornography.111 A person’s 

reputation can be damaged beyond repair by a 

single deepfake video posted to social media. 

Criminals can and will take advantage of AI and 

deepfakes to increase the effectiveness of scams 

and other nefarious activities. We have seen recent 

examples of business112 and romance113 fraud using 

audio deepfakes. Even after effectively debunking 

the deepfake, the damage remains. Deepfakes 

also present direct threats to society. Nefarious 

nation state actors work around the clock to spread 

disinformation campaigns, which increasingly 

include deepfakes, to create ideological conflicts in 

democracies around the world. They have effectively 

used disinformation and empowered domestic 

actors to disrupt elections and undermine efforts 

to contain the COVID\-19 pandemic. Technology 

innovations like replacing video codecs with deep 

neural networks are making it easier to create 

deepfakes in live video calls.

Microsoft Research, in coordination with Microsoft’s 

Responsible AI team and the Microsoft AI, Ethics 

and Effects in Engineering and Research (AETHER) 

Committee, continues to develop technology 

for training and testing deepfake detection 

technologies.

Mitigation 
through media 
literacy

Pew Center Research indicates that people are 

increasingly concerned about their ability to 

discern false information and sift through the 

volume of information they encounter in their daily 

lives.114 Media literacy is one of the most effective 

tools available to improve individual resilience to 

disinformation. From helping people understand 

minor editorial corrections, to preventing fake news 

from gaining traction, and reducing the likelihood 

that foreign influences undermine an election, media 

literacy inoculates individuals by helping them think 

critically about information they encounter.

Even a short intervention with media literacy 

education has been shown to make a significant 

difference in understanding disinformation, 

identifying the motivations and context, and 

reducing belief in inauthentic content.115 News 

media organizations, technology companies, 

universities, and social media companies have all 

in 2014, the government introduced multi\-platform 

started to implement media literacy efforts, which 

information literacy and strong critical thinking as a 

include resources such as labeling, contextualizing, 

core component of a national curriculum.117

providing further reading or resources, and even 

gamified tools like online quizzes.

Media literacy curriculum should help individuals 

understand information they encounter, evaluate 

Improving media literacy is vital to addressing 

the plausibility, verify the source and search for 

disinformation. Interventions should be contextualized 

other reputable sources on the topic, and interpret 

and tailored to the audience, starting from a young age 

context. In today’s online world with essentially 

with curriculum for responsible digital citizenship 

limitless information available, these skills may 

incorporated into standard civics education. Some 

not be intuitive, but are certainly ones that can be 

US states, most notably Florida and Ohio, have 

learned and sharpened over time. Further, media 

already started piloting and developing media 

literacy education does not need to be confined to 

literacy curriculum in classrooms.116 In Finland, when 

the classroom: these skills are universally relevant, 

the country was targeted with foreign influence 

especially for digital nonnatives, or anyone who 

operations and disinformation campaigns by Russia 

regularly consumes news and information online.

Approaches to countering disinformation

111 The State of Deepfakes: 2019 Landscape, Threats, and Impact Sensity AI

 \|

112 Thieves are now using AI deepfakes to trick companies into sending them money – The Verge 113 Romance Scammer Used Deepfakes to Impersonate a Navy Admiral 

and Bilk Widow Out of Nearly $300,000 (msn.com) 114 Many Americans Believe Fake News Is Sowing Confusion Pew Research Center ( journalism.org)

\| 

 115 A digital media literacy intervention increases discernment between mainstream and false 

news in the United States and India. (2020\) 116 Media Literacy Around the States Media Literacy Now

\| 

 117 https://www.theguardian.com/world/2020/jan/28/fact\-from\-fiction\-finlands\-new\-lessons\-in\-combating\-fake\-news 

113

Microsoft Digital Defense Report \| October 2021 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

Microsoft has and continues to develop media 

literacy resources to help consumers discern 

information. Ahead of the US 2020 elections, we 

released two online quizzes, “Spot the Deepfake”118 

and “Know My News,”119 aimed at raising 

awareness about synthetic media technology and 

understanding news sources. It also released a 

“VaxFacts Quiz”120 to heighten awareness around 

COVID\-19 misinformation as vaccines were 

becoming more widely available. Microsoft has 

also developed a hybrid threat training curriculum 

that highlights how threat actors are increasingly 

using cybersecurity and disinformation attacks in 

tandem to accomplish their goals. These training 

modules have been customized for the political 

community, including political campaigns, parties, 

and government entities, as well as for journalists 

and human rights organizations. 

Disinformation 
as an enterprise 
disruptor

Disinformation traverses a social diffusion chain 

comprised of both intentional and unsuspecting 

agents. Intentional actors include hackers, 

community. Like its disruptive effect on social 

into another system), screen\-scraping, and 

discourse, such disinformation carries with it the 

aggregation of public information through 

potential to disrupt corporate decision making, 

human evaluation and automated means, are also 

create commercial confusion and discord, and sow 

prone to disruption, corruption, or nuanced 

doubts in the minds of employees, customers, and 

modification. To address this growing threat, 

markets. The following three areas cover some of 

enterprise decision makers should evaluate 

the more common considerations that enterprises 

which of the enterprise’s critical information 

could prioritize to ensure preparedness to mitigate 

gathering and distribution processes could 

the disruptive effect of disinformation.

benefit from more resilient practices. Which 

disruptors, and other agents that generate or 

1\. Parallel to its effect through social media, 

propagate disinformation. These agents could 

disinformation has made its way into 

include nation states targeting a society, industry, 

enterprise workflows that are dependent 

or social arena. They could also include agents 

on data collection, aggregation, and 

engaged in corporate counter\-espionage activities 

distribution practices. These workflows and 

or anti\-competitive disruption. Unintentional agents 

data practices may be automated or manual 

might include personnel, vendors and suppliers, 

in nature, and even more advanced practices, 

other partners and stakeholders, customers, and 

such as those leveraging AI capabilities, are 

even competitors that continue the propagation 

prone to breach. Sophisticated AI algorithms 

inflection points, or points where information 

is interchanged or interpreted, need more 

rigor, controls, or other forms of checks and 

balances? Based on this analysis, controls and 

even out\-of\-band crosschecks and validations 

should be introduced to mitigate the threat of 

polluted or mischaracterized information that could 

potentially corrupt the data stream and subsequent 

insights that are derived from the data.

Learn more:

of disinformation, often not realizing what they 

can be fooled, or their underlying models 

2\. Signals and data within the enterprise 

are doing. They concurrently become victims and 

overwhelmed by excess disinformation and 

could be compromised through security 

An update on our effort to help preserve and protect 

unsuspecting agents of disinformation. Through 

other types of information attacks, leading 

vulnerabilities or attacks and infused 

journalism – Microsoft On the Issues (6/16/2021\)

these agents and other means of information 

to erroneous or anomalous insights and 

with disinformation. Instrumentation and 

dissemination, a parallel and concurrent wave of 

outcomes. In general, automated practices 

threat signals for performance of enterprise 

disinformation traverses or envelops the enterprise. 

face the threat of breach and corruption in 

resilience are often seen as having secondary 

This wave can be simple and anticipated, like 

the rise of a tide, or it can have the effect of an 

unpredictable tsunami about to weigh down on 

an unsuspecting coastal village. In this case, the 

the absence of adequate detection, timely 

importance and are therefore not given the 

notification, isolation and eviction, and defense 

level of scrutiny that core or primary services or 

in depth. In contrast, manual practices, such 

applications receive. Data and signal collection 

as copy/paste, swivel chair (entering data into 

are sometimes relegated to supporting 

coastal village would be the enterprise information 

one system and then entering the same data 

applications and systems that are bolted on as 

118 https://www.spotdeepfakes.org/en\-US (in partnership with the University of Washington Center for Informed Public) 119 https://www.knowmynews.com/en\-us (in partnership with NewsGuard) 

120 Do you know the Facts about the COVID\-19 Vax? – NewsGuard (newsguardtech.com)

114

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

adjunct environments. Attackers and disruptors 

3\. Situational intelligence could be supplanted 

The impact of diminished confidence could 

know this and strike where they believe 

with disinformation or nuanced in ways to 

drive higher pricing and impact production 

weaknesses could exist. Their primary areas of 

generate bias or create doubt in the minds 

costs. Doubt in the enterprise’s ability to 

reconnaissance include operational security 

of decision makers or front\-line personnel. 

maintain a grip on prices, supplies, and 

and control systems alongside discovery 

Situational intelligence includes threat 

suppliers could exacerbate disruption and 

of code and configuration vulnerabilities, 

intelligence, crisis intelligence, disaster data, 

force accelerated timelines or induce imprecise 

especially within secondary or supporting 

and other types of information that helps to 

or incorrect decisions. Alternatively, it could 

systems. Successful attacks could disrupt 

increase an enterprise’s understanding of 

introduce latency or doubt in decisions, such 

threat signals, or infuse misleading data, if 

an operating or competitive environment. 

as recovery, failover, or fallback. Disruptors 

they are able to bypass intrusion detection. 

One of the key strategies of disruptors is 

could also try to diminish front\-line confidence 

Enterprise decision makers should reevaluate 

to supplant situational intelligence with 

in leadership by corroding confidence or by 

the scope and security of their protected 

disinformation. This strategy is often deployed 

presenting false or inaccurate information 

assets and associated instrumentation and 

in environments that are considered out\-of\-

and leading or trailing indicators. Enterprises 

signals and ensure that intrusion detection 

band or beyond the control and reach of the 

that are dependent on external sources of 

perimeters around core or critical assets have 

enterprise, including social and other media 

intelligence for critical functions need to be 

been set to encompass these areas as well. 

platforms, public sites and portals, and other 

vigilant about information they ingest or 

This review includes evaluation of controls 

types of campaigns that could target the 

consume. Information gatherers and decision 

that measure the effectiveness of network 

enterprise or its complex and myriad supply 

makers need to validate sources and have 

segmentation, validate adherence to data 

chains. Disruptors sometimes generate so 

means of cross\-checking intelligence. Rating 

and signal classification schema, inbound 

much out\-of\-band disinformation that it 

systems and schema should be used, and the 

and outbound traffic features and patterns, 

overwhelms facts and otherwise accurate 

veracity and provenance of the intelligence 

classification of data and dependencies, and 

data. Their disruption tactics go beyond 

needs to be confirmed independently.

instrumentation that ensures data integrity 

the enterprise and its direct information, 

as it traverses across systems, at rest and in 

extending often to suppliers and third\-party 

backups. Instrumentation and signals that 

affiliates. Their goal is to introduce doubt in 

evaluate and indicate the performance of 

the minds of decision makers and/or front\-line 

critical systems should be cataloged and put 

personnel. Disinformation that could disrupt 

through a security and operational review 

suppliers, logistics, deliveries, orders, and 

for vulnerabilities and possible causes of 

fulfillment poses threats to the supply chain and 

compromise and injection of disinformation.

confidence in product and resource availability. 

Microsoft Digital Defense Report \| October 2021

115
115

Microsoft Digital Defense Report \| October 2021 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS
TOC INTRODUCTION THE STATE OF CYBERCRIME 

SUPPLY CHAIN, IOT, AND OT SECURITY 

HYBRID WORKFORCE SECURITY 

ACTIONABLE INSIGHTS TEAMS

NATION STATE THREATS 

DISINFORMATION 

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

classification, and analysis. To support and enhance 

the best ability that is available at the time.

Recommendations: Four\-point 
plan for enterprise executives 

As enterprises develop and mature their capabilities 

to respond to information disruption and 

disinformation, there are new imperatives that are 

emerging in the areas of security controls, threat 

the enterprise’s ability to improve its response, 

prioritize mitigations to address the highest risks, 

and to make investments that propel or accelerate 

its corporate objectives, the following practices 

could be leveraged as a starting point to develop 

sustainable mitigations and improvements to 

counter the effects of information disruption and 

disinformation.

1\. Catalog enterprise exposures to disruption, 

manipulation, and disinformation. 

Enterprises should begin with the arduous task of 

cataloging or keeping track of disinformation attacks 

on their information systems and data. This catalog 

would be an addition to the catalog of threats and 

attacks that are part of enterprise security controls.

• Include a classification of information 

manipulation and disinformation with clear 

indicators of targeted outcomes and impact of 

the attacks.

• Categorize and record the content that was 

3\. Quantify the consequences of disruption. 

hot and cold backups, or active\-active models of 

manipulated or introduced so that patterns can 

By examining dependency maps of data flow, 

redundancy or concurrency. Information disruptors 

be determined or detected.

analysis, and the points at which humans and 

and attackers aggressively search for backup 

• Determine the means of propagation and 

diffusion through the enterprise.

• Identify characteristics of actors and agents to 

systems were impacted, enterprise leadership 

facilities, dormant data stores, or unattended data 

can estimate or calculate the consequences and 

and data services that are slated to be deprecated. 

collateral damage caused by disinformation and 

When they find a weakness in security controls, 

disruption. The goal of such an examination is to 

not only do they threaten breach of data but their 

quantify the blast radius of any potential disruption 

actions can also trigger potentially impactful privacy 

• Conduct candid and objective identification of 

and assess its severity on enterprise operations, 

incidents. Enterprise privacy and security teams must 

corporate functions, processes, and systems 

that consumed or were impacted by the 

disinformation.

The net impact of the disruption or information 

infiltration must be evaluated and eventually 

included in considerations of corporate liability. 

functions, and reputation. The likelihood and 

take a closer look at controls, including security 

impact of such disruption should be used to inform 

measures, encryption at rest and in transit, of 

investment in mitigations and controls and help 

primary data sources and any backups or alternate 

prioritize safeguards that need to be implemented 

data stores. Gaps in these environments and 

to give the enterprise the most appropriate 

controls must be reported to enterprise leadership 

defense against the impacts of disruption and 

and prioritized to be addressed in a timely manner.

2\. Assess the impact of manipulation or 

disinformation. 

An emerging area for enterprise management and 

human resources is to conduct impact analyses of 

disruption and disinformation. Managers and human 

resource departments should study the behavior 

of enterprise employees, partners, and customers 

as they reacted to disruption or interacted with 

disinformation. Security and data science teams 

should run A/B tests on AI and trained algorithms to 

ensure they have not been corrupted or their models 

tampered with. Finance teams and economists could 

disinformation.

4\. Assess privacy implications of disruption.

Disinformation and information disruption 

campaigns sometimes attack or threaten customer 

and other protected data, which can have significant 

privacy implications for enterprises. Primary sources 

or stores of such data are difficult targets as they are 

kept deep inside the defensive network of controls, 

intrusion detection, and layers of authentication and 

authorization. Modern enterprise controls include 

Zero Trust approaches and tightly controlled or 

restricted access to data that is subject to privacy 

regulations, controls, and guidelines. Sovereign 

rules and obligations might also apply. It is under 

such constraints and restrictions that enterprises 

are expected to provide data resiliency, including 

Microsoft Digital Defense Report \| October 2021

116
116

• Note the sources of the attacks or information 

look at the costs of disruption, including opportunity 

leading to their origins and motivation, if 

cost, and the liabilities associated with impact of 

known.

market confidence, revenue, growth, and operational 

cost increases associated with disinformation.

Microsoft Digital Defense Report \| October 2021 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

Campaign 
security and 
election integrity

Threats to democratic processes from cyber\-enabled 

interference are a critical concern. Microsoft has 

shut down dozens of websites widely attributed to 

nation state actors that have been used to target 

elected officials and candidates, democracy\-promotion 

organizations, activists, and the press. We’ve also seen 

attempts by nation states to target and exploit key 

building blocks of democratic systems, including voting 

systems and political campaigns. We also endured the 

calculated manipulation of social media platforms in 

efforts to sow misinformation and disinformation.

The Defending Democracy Program at Microsoft 

was created to advance technology, increase cyber 

resilience, and engage with government, campaigns, 

and democratic stakeholders to address threats 

to democratic processes from cyber\-enabled 

interference. In partnership with the rest of the 

Microsoft Security community, the Defending 

Democracy team has helped protect two major US 

elections and dozens of national elections around 

the globe. This unique and important issue space 

raises an interesting set of cybersecurity insights, 

challenges, and solutions that we must address to 

ensure that our democratic institutions remain secure.

Unique cybersecurity 
challenges in political 
campaign security

political campaigns. This can be as simple as 

Heading into the US 2020 Presidential election cycle, 

establishing strong communication channels 

the AccountGuard program also offered enhanced 

between campaign staff and the private sector to 

identity protection features and resiliency reviews 

ensure they have a point of contact if issues arise. 

to customers involved in the election. Organizations 

The structure and lifecycle of political campaigns 

It is also imperative for candidates to establish a 

that took advantage of these resources saw an 

present unique cybersecurity challenges. Campaign 

culture of cybersecurity within their campaigns, not 

average increase of 18% to their Microsoft Secure 

organizations comprised of a mixture of staff, 

just among the IT staff but inclusive of everyone 

Score. In addition to political customers, the service 

volunteers, and consultants are often created and 

who interacts with the campaign. Relatively easy 

is available to other high\-risk groups including 

expanded rapidly once an individual declares their 

actions such as turning on multifactor authentication 

human rights organizations, journalists and media 

candidacy. As a result, team members are often asked 

(MFA), utilizing a password manager for strong 

organizations, and healthcare organizations.

to use their own personal devices, including cell 

unique passwords, and using secure communication 

phones or laptops, throughout the campaign. Further, 

channels for campaign communications make a 

AccountGuard distribution

with constrained budgets and limited IT expertise, 

tremendous difference in improving the resilience of 

decisions about which email and file sharing provider 

the entire organization.

to use are more likely tied to personal preference 

than extensive security and risk evaluations. With 

Microsoft has developed a service to address the 

people regularly joining and leaving a campaign and 

challenges associated with campaign staff using 

utilizing a variety of personal devices to conduct 

personal devices and accounts for campaign 

campaign business, it becomes difficult to manage 

business. Microsoft AccountGuard121 is a security 

and enforce strong cybersecurity practices.

service that unifies threat detection and notification 

across all accounts, and is available at no cost to 

These realities expose political campaigns to 

campaigns utilizing Microsoft 365 products. When 

significant cybersecurity threats, compounded further 

a campaign enrolls in AccountGuard, they can also 

by the asymmetric advantage that malicious actors 

extend coverage to anyone who interacts with 

maintain in terms of sophistication, resources, and 

the campaign, including staff, volunteers, interns, 

capacity. Political campaigns are high\-value, high\-

consultants, and more. The service then provides 

AccountGuard is currently available in 
32 democracies around the world.

visibility targets, but may have as few as one person 

notification and remediation guidance in the event 

Learn more:

dedicated to cybersecurity for the organization. 

of a nation state threat or compromise on campaign\-

It is critically important that we in the security 

40,000 accounts for political customers, including 

community continue to raise awareness of 

political campaigns, political parties, technology 

cybersecurity issues and best practices within 

vendors, and elections departments.

related accounts. The service currently protects over 

Expanding AccountGuard protections for high\-risk 

customers in 31 democracies – Microsoft On the 

Issues (3/9/2021\)

121 https://www.microsoftaccountguard.com/en\-us/

117

Microsoft Digital Defense Report \| October 2021 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

Threats to election infrastructure

As the Microsoft security community partners across 

the public and private sectors to secure election 

infrastructure, the differences between how cloud 

and on\-premises systems are used in elections 

becomes clear, as well as the various types of 

against remote threat actors. Though some form of 

election. This event served as a good reminder that 

connected or online voting systems are starting to rise 

vulnerabilities can be announced at inopportune 

in popularity, they remain in the minority of systems.

moments, and the security of an environment relies 

Securing election systems

who were using cloud infrastructure were secured 

on the ability to apply patches rapidly. Customers 

election technologies that must be secured. We form 

The primary recommendations for elections 

our threat models around three main categories of 

officials and private vendors who support elections 

UPDATES AND PATCHING 

against this vulnerability significantly faster—often 

automatically and immediately—than those running 

on\-premises servers that needed to be patched. 

systems, each with unique security considerations 

IT is to have a comprehensive strategy to patch 

SHARED SERVICES 

and risk profiles.

systems regularly and keep software up to date, 

and to use MFA. This is particularly relevant to 

Globally, voting systems are statutorily required to 

any internet\-connected systems, such as election 

be always disconnected from the internet and are 

support technologies and back\-office IT systems. 

effectively “air gapped” systems. Though this poses 

During the lead\-up to the 2020 US election cycle, 

certain challenges for maintenance and updating 

the ZeroLogon vulnerability (CVE\-2020\-1472122\) was 

devices, it acts as an extremely effective mitigation 

announced, less than three months before the 

Voting systems

• Vote casting systems (electronic ballot marking devices, “voting machines”)
• Vote tabulation devices (paper ballot scanners)

Connected 
election support 
systems

• Voter registration databases
• Election\-night results reporting sites
• ePollbooks (voter check\-in tablets)
• Information portals
• Not regulated, connected to the internet, shared ownership 

 Highest risk

Election back\-
office IT

• Voter information portals
• Day\-to\-day workstations and server infrastructure
• Email and files

Unlike a private sector company that is typically in 

charge of their entire IT estate, local governments 

tend to share IT systems with their state, regional, 

and national\-level counterparts. Although this can 

be cost effective and beneficial from a management 

perspective, it spreads out the risk of cyber intrusion 

from an unrelated government organization into an 

elections department. For example, if a research lab 

at a state\-run university were compromised, because 

of shared IT systems attackers could move laterally 

to attack a county election’s voter information 

portal. Furthermore, responsibility for maintenance 

and security is often split between private service 

providers and local governments. Sharing services 

highlights the need for network segmentation 

wherever possible to limit the impact of a cyber 

incident that either starts within or could migrate to 

an elections organization.

There are many 
connected components 
of an election beyond 
just casting a ballot at 
the polls—from data 
integrity concerns, 
to disinformation, to 
protecting election 
officials’ online identities. 

While many of these 
things may be invisible 
to the average voter, 
each offers a potential 
pathway for an 
adversary to attack the 
integrity of an election.

122 https://msrc.microsoft.com/update\-guide/en\-US/vulnerability/CVE\-2020\-1472 

118

Microsoft Digital Defense Report \| October 2021 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

Microsoft has developed and launched a project 

• Provides assurances that the system is recording 

called ElectionGuard. Microsoft ElectionGuard 

votes properly and not “changing votes.”

• Cryptography guarantees that no votes can 

MOVING OUT OF THEORY AND INTO 

be changed after being cast without being 

REAL ELECTIONS 

detectable.

• Ensures that no one specific individual’s vote 

can be revealed.

• Allows interested third\-party watchdog 

organizations to verify that the tally was 

summed properly, and that the system 

operated without errors.

Learn more:

ElectionGuard had its first real\-world pilot election in 

Fulton, Wisconsin in February 2020 when it was added 

to VotingWorks’ touchscreen ballot\-marking devices 

for a municipal election in Rock County. Hundreds of 

citizens voted for the first time on devices running 

ElectionGuard. After their ballot was cast, each voter 

received a verification code that they could take 

home with them to check online that their unique 

vote had been included in the final election tally.

ElectionGuard is free, open\-source, royalty\-free 

software, and all source code is publicly viewable on 

LinkedIn post: What is ElectionGuard? (Microsoft on 

GitHub.123 Microsoft believes that election security 

the Issues) (3/27/2020\) 

SMALL TEAMS AND SMALL BUDGETS

In some countries, including the United States, 

elections are not managed federally; each 

municipality is responsible for running and 

managing its own elections infrastructure. The 

asymmetric threat of advanced adversaries 

targeting local\-level elections offices that are time 

and resource constrained is of real concern. As 

discussed earlier in this report, advanced persistent 

threat actors have IT knowledge and monetary 

resources that exceed the annual budgets of local 

municipalities. Therefore, steps must be taken by 

both the private and public sector to concentrate 

cybersecurity talent and resources in a way that 

helps to offset and balance that asymmetry.

To help elections organizations address these 

concerns, the Defending Democracy team focuses 

heavily on securing and supporting customers using 

cloud services to support their elections, in both the 

private and public sectors. Our goal is to use the 

cybersecurity expertise at Microsoft to offset the 

asymmetric threats faced by local elections or small 

elections vendors.

Learn more:

Keeping your vote safe and secure: A story from inside 

the 2020 election – On the Issues (microsoft.com)

Protecting political campaigns from hacking – 

Microsoft On the Issues (5/06/2019\)

Election integrity

To address growing concerns in voter trust among 

election systems, and to help drive forward 

principles of software independence, election 

auditability, and security and cryptography, 

is a free open\-source software development kit 

designed to make voting systems more secure, 

auditable, verifiable, and efficient. This is done by 

implementing principles of end\-to\-end verifiability 

and answers the question: How can I trust the 

accuracy of an election outcome if I worry that the 

software, hardware, transmission infrastructure, or 

personnel responsible for conducting the election 

could be untrustworthy?

Unlike banking software or other high\-security 

industries, secret ballot elections require that an 

individual’s data (votes) must be a secret to all 

parties, and there can be no direct tie between 

a person’s identity and their vote, other than the 

acknowledgment that a voter has cast a ballot.

ElectionGuard implements these end\-to\-end 

verifiable features:

• Enables every individual to verify that their 

vote is included in the final election tally, 

with a unique verification code.

• Ensures that no one specific individual’s vote 

can be revealed.

123 https://github.com/microsoft/electionguard 

119

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Disinformation as an emerging threat Mitigation through media literary Disinformation as an enterprise disruptor Campaign security and election integrity

should not exist in a vacuum, and independent 

security researchers should be able to validate 

the integrity of the software. To that end, we 

have implemented a bug bounty program where 

Microsoft will award the security community for 

finding vulnerabilities in the ElectionGuard software. 

Since launching in October 2019, the program has 

awarded tens of thousands of dollars in bounties to 

researchers across multiple continents. In this way, 

security issues were discovered and responsibly 

reported by the community, all patches were 

issued within 90 days of reporting, and potentially 

vulnerable code was never used by voters in 

production election systems. Public trust in elections 

is, in part, dependent on the independent auditability 

of the systems and processes that support our 

elections. We continue to welcome the trained eyes 

of security researchers across the world to suggest 

improvements to the service and to independently 

test ElectionGuard’s security and cryptography.

Learn more:

Hart and Microsoft announce partnership to make 

elections more secure, verifiable – Microsoft On the 

Issues (6/3/2021\)

Microsoft wants to make voting more trustworthy. 

Its partnership with Hart InterCivic will help – CNN 

(6/3/2021\)

Microsoft hopes this technology can help fix America’s 

elections (cnn.com) (2/22/2020\)

Trainings as mitigation

Countermeasures needed

To date, Microsoft has trained more than 1,500 

To ensure access to credible information and 

participants from the political, civil society, media, 

preserve freedom of expression, we need a 

and human rights sectors on topics spanning 

multistakeholder and a multimodal approach. The 

cybersecurity and disinformation threats. These 

main objective of any countermeasure is to mitigate 

trainings have been tailored to audiences around 

the negative societal impact of disinformation.

the world, including political campaign staff, political 

parties, and other government entities in democratic 

Specifically, when it comes to malicious synthetic 

countries. Ahead of the US 2020 elections, Microsoft 

media, the approach must be twofold: (1\) to reduce 

partnered with NYU’s Brennan Center for Justice 

the exposure to malicious deepfakes, and (2\) to 

and the CISA to train more than 400 US election 

minimize the damage it can inflict.

officials on topics including ransomware, pandemic 

preparations, threat intelligence, and an election 

Media literacy efforts can be enhanced to cultivate 

day simulation exercise. Further, Microsoft has 

a discerning public. Deepfakes will have a limited 

collaborated with PolitiFact at the Poynter institute 

adverse impact if media consumers use logical 

to develop a hybrid threat training curriculum 

thinking and common sense to differentiate 

exploring the intersection of cybersecurity and 

between fiction and reality. Deepfakes have such 

disinformation, as these threat vectors increasingly 

a potentially devastating impact because many 

overlap, especially in regard to attacks against 

individuals assume that a video, a photograph, or 

political and media organizations.

an audio is real if it aligns with their preconceptions 

The technical countermeasures are not simple. 

The synthetic media’s technological development 

continues to outpace what is possible by algorithms 

and other technologies. Technical solutions for 

deepfakes fall into two categories: (1\) detection 

and authentication and (2\) provenance. Detection 

of deepfakes and disinformation is difficult. 

Human\-AI collaboration can help, but context, 

cultural differences, and intent make it hard to 

decipher disinformation objectively. In the long 

term, provenance solutions will help. Media 

authentication, authoritative content, and 

standards akin to SSL/HTTPS for web traffic must 

be developed for media. Technology that can 

help “sign” the media to find the media publisher, 

machine\-readable fingerprinting, and watermarking 

technology to tamperproof media would reduce 

media manipulation to effectively combat the 

spread of deepfakes.

Learn more:

Defending Democracy Program – On the Issues 

(microsoft.com)

and biases. Alternatively, often people believe it’s 

fabricated if it contradicts their beliefs.

We need meaningful regulations and appropriate 

laws to govern disinformation and deepfakes so 

that, at the very least, the perpetrators are held 

accountable. Without legislation and legal remedies, 

people are vulnerable to disinformation campaigns 

and deepfake revenge pornography, fraud, and 

other harms. Of course, legislation must take a 

balanced approach toward freedom of expression 

and speech.

We’re not saying ElectionGuard 
makes it impossible to hack 
voting machines; we’re saying 
ElectionGuard makes it pointless 
to hack voting machines.

120

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

CHAPTER 7 

Actionable insights

Introduction

Summary of report learnings

Conclusion 

TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Summary of report learnings Conclusion

INTRODUCTION: Five cybersecurity paradigm shifts

ANN JOHNSON, CVP, SECURITY, COMPLIANCE \& IDENTITY

In working with organizations from around the world, we recognize the need to enable people to work 
productively and securely and from a variety of non\-traditional locations and a variety of devices. Through 
these interactions, we’ve learned a lot about the role that cybersecurity plays in helping organizations maintain 
business continuity as we adapt to a hybrid work world. As a result, we anticipate five cybersecurity paradigm 
shifts that will support the evolution of work in a way that centers on the inclusivity of people and data.

1\. The rise of digital empathy 

people and their ever\-changing circumstances, 

2\. The Zero Trust journey is becoming 

When we consider building security into the 

their diverse perspectives, and varied abilities. 

increasingly important 

productivity experience, there can be a tendency 

For example, rather than requiring people to 

Zero Trust is an “assume breach” security 

to focus on security from purely a technology 

do unnatural things to engage with security, 

posture124 that treats each step across the 

perspective. However, during times of constant 

which can also increase their likelihood of 

network and each request for access to resources 

disruption and change, when people are 

getting distracted when busy, factoring in 

as a unique risk to be evaluated and verified. This 

susceptible to increased stress reactions, the 

digital empathy leads to inclusion of security 

model starts with strong identity authentication 

importance of digital empathy comes into 

professionals with a broader range of abilities, 

everywhere. Multifactor authentication (MFA)—

greater focus. Digital empathy involves thinking 

skill sets, and perspectives—for greater diversity 

which we know prevents 99% of credential 

about the ways in which people behave and 

and effectiveness of cybersecurity solutions. 

theft125— and other intelligent authentication 

engage with technology. In this way, sociology 

It also means developing technology that can 

methods126 make accessing apps easier and more 

and humanities considerations are essential to 

forgive mistakes. 

secure than traditional passwords. 

the evolution of technology and cybersecurity.

 Digital empathy will be critical to how we 

 As we look past the pandemic to a time when 

Empathy isn’t just for in\-person interactions. 

move forward as an industry. Whether it’s an 

workforces and budgets rebound, Zero Trust 

By applying empathy to digital solutions, we 

organization—or an individual—our ability to be 

will become the biggest area of investment for 

can make these solutions more inclusive. In 

empathetic will help us to understand and adapt 

cybersecurity. This means that right now, every 

cybersecurity, that means building tools that 

during times of constant change. 

one of us is on a Zero Trust journey — whether 

accommodate more diversity with respect to 

we know it or not. 

124 Zero Trust Security Model and Framework Microsoft Security

\| 

 125 One simple action you can take to prevent 99\.9 percent of attacks on your accounts (microsoft.com) 126 Azure Active Directory passwordless sign\-in Microsoft Docs

\| 

WE KNOW A 

COMPREHENSIVE 

APPROACH TO 

OPERATIONAL 

RESILIENCE MUST 

INCLUDE CYBER 

RESILIENCE.

Microsoft Digital Defense Report \| October 2021

122
122

Microsoft Digital Defense Report \| October 2021 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Summary of report learnings Conclusion

3\. Diversity of data matters 

events such as earthquakes, legal events such 

Microsoft tracks more than 24 trillion daily 

as cyberattacks, and pandemics like COVID\-19\. 

signals from a diverse set of products, services, 

Cloud technology helps organizations develop 

and feeds around the globe. We were able 

a comprehensive cyber\-resilience strategy 

to identify new COVID\-19\-themed threats—

and makes preparing for a wide range of 

sometimes in a fraction of a second — before 

contingencies less complicated due to its 

they reached customers. This is just one 

scalability.

example of how the power and scale of the 

cloud has a clear advantage when it comes to 

combating threats.

5\. A greater focus on integrated security 

The first half of 2021 brought into stark reality 

the agility and callousness of our adversaries. 

 As one example, in the last year, the diversity of 

To uncover shifting attacker techniques 

data also allowed us to understand COVID\-19\-

and stop them before they do real damage, 

themed attacks in a broader context. Microsoft 

organizations must be able to see across their 

cyber defenders determined that adversaries 

apps, endpoints, network, and users. Facing a 

were primarily adding new pandemic\-themed 

new economic reality, organizations will also be 

lures to familiar malware.127

4\. The resiliency of a business is tied to its 

cyber resilience 

Cyberattacks are increasing in frequency 

and sophistication and are deliberately 

targeting core business systems to maximize 

the impact of the attack or likelihood of a 

ransomware payout. With this context, we 

know a comprehensive approach to operational 

resilience must include cyber resilience.128 At 

Microsoft, we benefit from a strategy that 

focuses on four basic threat scenarios: Planful 

events such as weather incidents, unplanned 

driven to reduce costs by adopting more of the 

security capabilities built into their cloud and 

productivity platforms of choice. To maximize 

the effectiveness of security organizations, 

tools must be fully integrated to improve 

efficacy and provide end\-to\-end visibility.

While digital acceleration will continue to influence 

the paradigm shifts that shape our industry, one 

thing remains the same; security technology is 

fundamentally about improving productivity and 

collaboration through secure and inclusive user 

experiences.

Summary of 
report learnings 

What became clear as we compiled this report is 

how much technology is now baked into everything 

we do. We can’t afford to treat technology and cyber 

risk as something separate and contained that IT 

and security teams are left to manage on their own. 

The examples in this report show that criminals will 

seek to exploit whatever technology we develop 

and introduce; the challenge is in understanding 

what form that will take. Because we can’t always 

predict how technology will be exploited, we need 

to assume that anything we create or use will be 

a potential target and prepare ourselves to be as 

resilient as possible.

The key actionable learning from all the elements 

of this report is that to minimize impact of attacks 

we must truly practice good cyber hygiene, 

implement architectures that support the principles 

of Zero Trust, and ensure cyber risk management is 

integrated into every aspect of the business. 

The following section summarizes some of the key 

learnings reinforced by the findings and insights in 

the report.

127 Exploiting a crisis: How cybercriminals behaved during the outbreak – Microsoft Security 128 Operational resilience in a remote work world (microsoft.com)

Microsoft Digital Defense Report \| October 2021

123
123

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Summary of report learnings Conclusion

The cybersecurity bell curve:
Basic security hygiene still protects 
against 98% of attacks

Enable multifactor authentication

Apply least privilege access 

Keep up to date

Utilize antimalware

Protect data 

Make it harder for bad actors to utilize 

Prevent attackers from spreading 

Mitigate the risk of software vulnerabilities 

Stop malware attacks from executing 

Know where your sensitive data is 

stolen or phished credentials by 

enabling multifactor authentication. 

Always authenticate and authorize 

based on all available data points, 

across the network by applying least 

by ensuring your organization’s devices, 

by installing and enabling antimalware 

stored and who has access. Implement 

privilege access principles, which limits 

infrastructure, and applications are kept 

solutions on endpoints and devices. 

information protection best practices 

user access with just\-in\-time and just\-

up to date and correctly configured. 

Utilize cloud\-connected antimalware 

such as applying sensitivity labels and 

enough\-access (JIT/JEA), risk\-based 

Endpoint management solutions allow 

services for the most current and 

data loss prevention policies. If a breach 

including user identity, location, device 

adaptive polices, and data protection to 

policies to be pushed to machines 

accurate detection capabilities.

does occur, it’s critical that security 

health, service or workload, data 

help secure both data and productivity.

for correct configuration and ensure 

classification, and anomalies.

systems are running the latest versions.

teams know where the most sensitive 

data is stored and accessed.

124

Microsoft Digital Defense Report \| October 2021 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Summary of report learnings Conclusion

Cyber hygiene

Taking basic security precautions can help 

your organization prepare for and mitigate the 

overwhelming majority of modern cyber threats 

and helps to prepare for the evolution of threats 

as technology advances. The “cybersecurity bell 

curve” shows the activities that will have the biggest 

impact on reducing threats. Some of those actions, 

the impact they have, and recommendations for 

implementing them are described here.

Enable multifactor authentication

This continues to be the top recommendation as it 

was last year. MFA can stop credential\-based attacks 

dead in their tracks. Without access to the additional 

factor, the attacker can’t access the account or 

protected resource. The introduction of passwordless 

technology and architectures makes this easier for 

employees and customers to use and also provides 

more security than traditional text (SMS) or voice 

approaches. MFA should be enabled on all accounts 

that support it, in a way that it is easy for all users 

to use it. It’s also important to ensure that people 

understand that they should not approve an MFA 

request unless they were trying to log in or access a 

system—many people automatically click to approve 

any pop\-up that they receive. Digital empathy can 

be useful in understanding this behavior and helping 

to nudge people toward less risky decisions.

Apply least privilege access and secure the most 

Secure and manage devices (keep up to date)

In systems where this is not possible, the 

sensitive and privileged credentials

An essential part of good cyber hygiene is 

environment should then be protected from other 

When attackers breach an organization, they look 

ensuring that devices are kept up to date and 

systems and monitored to detect any unexpected 

for privileged credentials to provide them with 

configured correctly. Use endpoint management 

traffic or attempts to compromise the systems.

access to sensitive information and systems. In 

software to enforce policies that ensure the correct 

addition to using MFA to protect login to an identity 

configuration settings are deployed and that 

Use antimalware and workload protection tools 

and ensuring that they have least privilege to access 

systems are running the latest software. Wherever 

Antimalware and detection and response technologies 

systems, the credentials that support that identity 

possible, take an evergreen approach to ensure all 

should be deployed across the ecosystem to prevent 

and provide access must be secured. Among other 

devices are constantly running the latest version 

attacks and provide warning of any anomalies 

things, this will help to minimize the impact and 

of software. This includes ensuring a means of 

or threats that may be attempting to breach the 

breadth of pass\-the\-hash\-style attacks in the event 

updating every piece of software or application so 

environment. This includes OT and IoT environments. 

that malicious code is already running on a local 

that there are no dependencies that prevent you 

For cloud systems, workload protection should be 

machine or network. This includes securing hardware 

from implementing the latest updates and patches. 

deployed across all systems from virtual machines 

such as with a trusted platform module or hardware 

For those devices missing critical patches, restrict 

and containers to machine learning (ML) algorithms, 

security module or using cloud authentication 

them from accessing sensitive resources.

databases, and applications.

services that provide credential protection. 

The same approach should be taken for cloud 

Protect data

Separate accounts should be used for privileged 

services, using cloud security posture management 

Good cyber hygiene as outlined in the previous 

access versus general internet and email access. 

to ensure that systems are configured correctly. 

four steps can protect data, but it is also important 

Dedicated hardened workstations should be used 

Keeping software and systems up to date can be 

that organizations know which sensitive data they 

for privileged accounts and to perform privileged 

easier in the cloud where update domains enable 

have, and ensure that they have appropriate steps in 

tasks to prevent the chances of infection through 

migration to updated infrastructure for testing with 

place to protect it. In fact, there is often a regulatory 

general internet activity and email. Using JIT/JEA 

the option to roll back easily if issues occur. 

requirement to do so. The General Data Protection 

systems ensure they will only get exactly the rights 

Regulation (GDPR), for example, requires a risk\-

needed to perform a task and only for as long as 

For systems, such as OT, where updating software is 

based approach to protecting the data of residents 

needed to undertake it. This should be combined 

not as easy, a strong inventory of systems is needed 

of the European Economic Area (EEA). To take a 

with risk\-based adaptive policies that deny access to 

to understand which equipment exists, and how 

risk\-based approach it is important to know your 

resources when there is any doubt over the hygiene 

vulnerable it may be to certain attacks. Incorporate 

data—to understand what is sensitive and what may 

of the account or device.

add\-on modules or replace hardware to ensure it 

be subject to regulatory requirements. While there 

achieves all seven properties of secured devices. 

have been standards for data governance and data 

125

Microsoft Digital Defense Report \| October 2021 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Summary of report learnings Conclusion

protection for over 30 years, many organizations 

have struggled to implement them. As we move 

into a world where we increasingly collaborate and 

share data, it’s important to ensure we understand 

what data we have, classify it accurately, and apply 

sensitivity labels as appropriate. This practice will 

enable us to use information protection and data 

loss prevention technologies to protect data with 

more confidence.

In the event of a breach, these practices can also 

help security teams to know where the most sensitive 

data is and whether it was exposed to attackers.

Isolate legacy systems

Not every system is capable of running the tools to 

enable Zero Trust. For example, many operational 

technology (OT) systems have long technology 

lifecycles and may run operating systems and 

software that can’t be updated.

Network segmentation should be used to restrict 

access to these systems. This can help to ensure 

that operational technology is not exposed to the 

risks from hybrid working, and that IoT devices and 

sensors have access and connections only to the 

smart ecosystems they support.

Adopt Zero Trust principles

This means that rather than trying to run the 

This report has highlighted the sophistication and 

modern and legacy alongside each other, we can 

complexity of many of the attacks we are seeing and 

isolate these systems from exposure to the risks 

why it is increasingly difficult to prepare to counter 

that come from a modern connected infrastructure 

these attacks. Zero Trust is important to reduce the 

and avoid having that legacy technology hold back 

exposure of sensitive data by limiting the inherent 

modern architectures. It also allows monitoring of 

trust within an organization that an attacker would 

the environment that hosts operational technology 

exploit—especially when people are connecting 

and Internet of Things (IoT) devices to be highly 

from everywhere and will not necessarily be coming 

focused on detecting and responding to unusual 

from a “trusted” location. This is why adopting a 

activity in an environment where it may not be 

Zero Trust approach is now a top priority for most 

possible to install software on the system.

organizations. In a world where it’s harder to predict 

or prevent the attacker, it’s important to assume they 

will get in and limit their exposure.

Integrate cybersecurity into 
business decision making

Now that technology is an essential element of 

business operations—a process that has only been 

accelerated over the last 18 months—cybersecurity 

must be a factor in overall business decision 

making and not just something that is left to the 

technology department.

Treat cyber as a business risk

Cybersecurity should no longer be viewed as a 

specialized risk that falls only within the purview 

of the IT department. Technology expertise sits 

in the IT department, just as expertise in financial 

risk management generally resides in the finance 

department, but ultimate responsibility and 

Cybersecurity’s role in digital transformation

accountability for the risks lie within the business 

function. As the chapters in this report illustrate, 

addressing the threats that we face require a mix of 

technology, policy, and people expertise—as does 

all business decision making.

Every leader in the organization should consider 

how they enable employees and customers to have 

a better digital experience, while also considering 

what’s needed to mitigate the associated risks. This 

includes consulting the cybersecurity team on how 

to manage the risks that arise as they undergo 

digital transformation. As this report shows, there 

are inherent risks in all the new technologies and 

business practices we adopt, and those risks must 

factor into any decisions about technology, policy, or 

business practices.

126

Microsoft Digital Defense Report \| October 2021 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Summary of report learnings Conclusion

Security decision makers should truly embrace a 

risk management mindset as they consider how the 

steps they take can protect the organization, while 

also helping achieve operational goals. 

Resilience includes 
cybersecurity

Build a third\-party 
risk program

Partners, suppliers, and contractors interact with 

data and applications connected to our corporate 

environment all the time. Attackers are increasingly 

targeting third\-party providers to gain access to 

their systems and networks with a view to gaining 

In the connected world we live in today we need 

access to their customers.

to consider resilience as a key success factor in 

everything we do. Digital transformation is bringing 

Ensure that the organization has a strong supply 

Use digital empathy in 
implementing security 
controls

tools they need to understand appropriate behavior, 

recognize attacks, and report unusual activity. A 

culture of enablement, trust, and engagement will 

significantly improve reporting and provide earlier 

As we connect more and more systems together, 

warning of attacks. 

security can become more complex, but we need 

to ensure that we value diversity of skills, areas of 

Build security into productivity.

expertise, work and learning style, and background, 

When you implement security controls, think about 

among other things. Do not expect or require 

the impact on the experience of those using it, 

everyone to be technology experts, in the traditional 

whether employees or customers. What is their 

sense of the term, in order to engage with the 

background, expertise, and cultural experience? 

increasing complexity to our security solutions 

chain assurance process, built on an understanding 

security of these systems.

including greater collaboration with third parties and 

of your suppliers’ exposure to cyberattacks, how 

the expectation that systems will be available 24x7\. 

they configure their systems to be secure, and what 

The platforms we are building to support businesses 

steps they take to protect any information you share 

need to be fully resilient against attacks.

with them. Ensure that you are managing your third\-

Cybersecurity and resilience should be considered 

party risk through robust service\-level agreements, 

together. Operational resilience planning should 

attestations, and shared assessments like SSAE 18 

include understanding the cybersecurity threats to 

SOC 1 and SOC 2, PCI\-DSS, GDPR, and ISO 20001\.

the system and making appropriate investment to 

ensure continued success.

Third\-party access to systems should also follow 

the Zero Trust principles you apply to your own 

It is crucial to implement strong backup and 

organization to limit exposure to attacks originating 

recovery solutions, but it is equally important that 

from a compromise of their systems.

organizations plan for how operational decisions will 

be made in the event of a cyberattack and practice 

their crisis management and response as well as 

their technical response to incidents.

Any controls you put in place should consider 

the experience of those who do not have a 

When you implement security controls, apply 

background in technology. Is it intuitive, can it be 

digital empathy to ensure that the controls you are 

understood, and does it fit into their workflow as 

providing consider the environment in which those 

naturally as possible? Too much friction without 

using the system are working and allow them to 

an understanding of why a control is in place can 

easily engage with the environment. For example:

lead people to circumvent technology or ignore 

processes to get things done. 

Invest in user training that educates and informs.

Implement security training that helps employees 

If, in addition to training people, we ensure that 

understand the risks they face and the best way they 

security fits into their working practices rather than 

can help to protect the organization. This training 

those of a technology or cybersecurity professional, 

should be ongoing and designed in a way that 

we increase the chance of their understanding the 

increases engagement. User training is not just a 

risks and taking the appropriate actions. Where 

compliance activity but an essential part of the early 

possible, cybersecurity should be invisible to the 

detection and response to an attack. Ensure that the 

user except where it can help nudge them to take 

training you provide explains risks in the context of 

appropriate actions to manage risk. 

the employees’ work, and provide the context and 

127

Microsoft Digital Defense Report \| October 2021 
 
 
 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Introduction Summary of report learnings Conclusion

Conclusion

A number of key themes arise throughout the 

• Any element can be used as an attack vector. 

• Zero Trust is an architectural principle. 

different sections of this report that we encourage 

Attackers will look for the weakest link across 

The threats we have seen underline the 

you to consider as you think about improving your 

an organization’s ecosystem, so we must 

importance of Zero Trust in designing and 

As technology becomes more integral to our society, 

security posture:

attackers are increasingly seeking to exploit this 

cultural shift. From cybercriminals to nation state 

groups, these are sophisticated and well\-researched 

organizations with the resources, investments, and 

research to deploy complex and well\-informed attacks 

against an organization. They are professional 

enterprises with their own sophisticated supply chains 

and their own well\-researched, well\-engineered lures 

• Do the basics well. 

A running theme throughout many of the 

chapters is that, although attackers are 

becoming more sophisticated, good cyber 

hygiene and implementation of basic security 

measures is often the best way to disrupt, 

prevent, and detect their attacks. 

that seek to exploit the way your organization works.

• Take a holistic view. 

As we increasingly do more of our work online, so do 

criminals and nation state attackers. You must take 

this realization into consideration as you plan digital 

activities. For any new venture, consider the threat 

alongside the opportunity, and think about how you 

can manage risk for your entire organization.

This kind of thinking will require fundamental 

changes in the way we operate. We must consider 

risk as a whole and across the organization, rather 

Too often the way we organize security and risk 

is driven by our own organizational structure 

and siloes. Attackers will look for vulnerabilities 

across these siloes, so we need to consider risk 

and the best approach to mitigating risk at an 

organizational level. This may require some 

standardization or translation of approaches 

across the different teams in an organization. 

It also underlines the importance of standards 

as we seek to harmonize between companies, 

which is increasingly important to managing 

than within siloes or individual viewpoints. We must 

supply chain risk. 

look at where we need to change the way we work, 

and where we need to do the things we are already 

doing—but better.

manage it holistically. The weakest link may be 

managing the risk in an organization. The last 

a connected freezer or building management 

year has emphasized why there should be no 

system that is used to gain access to the 

such thing as a trusted application, trusted user, 

corporate network, or it may be a user or device 

or trusted device with unrestricted access. The 

that is compromised via a phishing email in 

risk and context of every connection needs 

an attempt to gain access to the operational 

to be considered before allowing access to 

technology running a factory or production 

resources. Zero Trust is not a technology but an 

plant. We need to consider and manage the 

approach to managing risk. When implemented 

organization’s entire attack surface.

properly, it can enable us to unlock the 

potential of modern technology while limiting 

our exposure in a hyperconnected world. 

• Think about people. 

People engage with technology and can be 

used as a way of gaining access to the digital 

environment. Think about how to engage with 

them in a way that will help them to understand 

the risks they face. Understanding, engaging, 

and educating people will allow them to 

become a key line of defense against modern 

threats, whether that is misinformation seeking 

to influence peoples’ decisions and undermine 

democracy or phishing emails seeking to gain 

access to and compromise an organization’s 

digital assets. 

128

Microsoft Digital Defense Report \| October 2021 
 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Contributing teams at Microsoft

 
TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Contributing teams

Contributing teams at Microsoft

The insights in this report, as well as the actionable learnings above, have been provided by a diverse group 
of security\-focused individuals, working across dozens of different teams at Microsoft. Collectively, their 
goal is to protect Microsoft, Microsoft customers, and the world at large from the threat of cyberattacks. 
We are proud to share these insights in a spirit of transparency, with a common goal of making the digital 
world a safer place for everyone.

Azure Networking, Core

A cloud networking team focusing on the Microsoft WAN, data center networks, and the software defined 

networking infrastructure of Azure. This includes the DDoS platform, the network edge platform, and network 

security products such as Azure Firewall and Azure WAF.

Cloud Security Research team

A team working to secure the Microsoft cloud and build security products, with a mission to protect and 

empower customers to securely transform their organizations. The team’s focus is on research and feature 

productization for Azure Defender, Security Center, and Azure Sentinel. 

Customer Security and Trust (CST)

A cross\-disciplinary team driving continuous improvement of customer security in our products and online 

services. Working with engineering and security teams across the company, the mission of CST is to ensure 

compliance and enhance security and transparency to protect our customers and promote global trust 

in Microsoft. They formulate and advocate cybersecurity policy globally; advancing Digital Peace through 

multistakeholder collaboration, focusing on Digital Safety to protect customers from harmful online content, and 

collaborating with public and private organizations to disrupt cyberattacks and support deterrence efforts. 

Microsoft Digital Defense Report \| October 2021

130
130

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Contributing teams

Cyber Defense Operations Center (CDOC) 

Microsoft’s cybersecurity and defense facility is a fusion center that brings together security professionals from 

across the company to protect our corporate infrastructure and the cloud infrastructure to which customers have 

access. Incident responders sit alongside data scientists and security engineers from across Microsoft’s services, 

products, and devices groups to help protect, detect, and respond to threats 24x7\.

Defending Democracy Team

A Microsoft team who works with stakeholders including governments, nongovernmental organizations, 

academics, and industry all in democratic countries globally to protect campaigns from hacking, increase political 

advertising transparency online, explore technological solutions to preserve and protect electoral processes, and 

defend against disinformation campaigns.

Detection and Response Team (DART)

A Microsoft team whose mission is to respond to security incidents and help Microsoft customers become cyber\-

resilient. DART leverages Microsoft’s strategic partnerships with security organizations around the world and with 

internal Microsoft product groups to provide the most complete and thorough investigations possible. DART’s 

expertise has been leveraged by government and commercial entities around the world to help secure their most 

sensitive, critical environments.

Digital Security \& Resilience (DSR)

A Microsoft organization developed with a mission to enable Microsoft to build the most trusted devices and 

services, while keeping our company safe and our data protected. Across the company, DSR is continually 

evolving the security strategy and taking actions to protect Microsoft assets and the data of our customers.

Digital Security Unit (DSU)

A team of cybersecurity attorneys and strategic cyber intelligence analysts who provide legal, operational, 

geopolitical, and technical subject matter expertise to protect Microsoft and our customers. DSU’s analysis and 

proposed solutions to complex digital security problems help to build trust in Microsoft’s enterprise security 

capabilities and defenses against advanced cyber adversaries worldwide.

Microsoft Digital Defense Report \| October 2021

131
131

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Contributing teams

Enterprise Risk Management (ERM)

A team focused on key risks to Microsoft’s business objectives, the ERM team works across business units to 

enable prioritized risk discussions with Microsoft’s senior leadership and, ultimately, the Board of Directors. 

The team manages the company’s NIST Cybersecurity Framework internal assessment and the enterprise risk 

framework, which connects to multiple operational risk teams, and coordinates with the company’s internal 

audit function.

GitHub Security Lab

An open\-source software\-focused security research team. Its mission is to help secure the world’s code and 

build bridges between the security research and software development communities through contributions 

including security research, tooling, and meetups.

Global Cybersecurity Policy

A team that works with governments, NGOs, and industry partners to promote cybersecurity public policy that 

empowers customers to strengthen their security and resiliency as they adopt and use Microsoft technology.

Microsoft AI, Ethics and Effects in Engineering and Research (AETHER) Committee

An advisory board at Microsoft that helps to ensure that new technology is developed and fielded in a 

responsible manner.

Microsoft Customer and Partner Solutions 

Microsoft’s unified commercial go\-to\-market organization responsible for field roles such as security and 

technical sales specialists and advisors.

Microsoft Defender for IoT

A team composed of domain\-expert reverse engineers and data scientists. The team continuously performs 

reverse\-engineering and analysis of large amounts of data related to IoT threats and threat actors to gain better 

visibility into the IoT landscape and uncover related trends and campaigns.

Microsoft Digital Defense Report \| October 2021

132
132

Microsoft Digital Defense Report \| October 2021TOC INTRODUCTION THE STATE OF CYBERCRIME NATION STATE THREATS SUPPLY CHAIN, IOT, AND OT SECURITY HYBRID WORKFORCE SECURITY DISINFORMATION ACTIONABLE INSIGHTS TEAMS

Contributing teams

Microsoft Defender Team 

Microsoft’s largest global organization of product\-focused security researchers, applied scientists, and threat 

intelligence analysts. The Defender Team delivers innovative detection and response capabilities in M365 security 

solutions and Microsoft Threat Experts. 

Microsoft Digital Crimes Unit (DCU) 

A team of attorneys, investigators, data scientists, engineers, analysts, and business professionals that fight 

cybercrime globally through the innovative application of technology, forensics, civil actions, criminal referrals, and 

public/private partnerships while protecting the security and privacy of our customers.

Microsoft Security Response Center (MSRC) 

Part of the defender community on the front line of security response evolution. For over 20 years, MSRC has 

been engaged with security researchers working to protect customers and the broader ecosystem. An integral part 

of Microsoft’s Cyber Defense Operations Center (CDOC), MSRC brings together security response experts from 

across the company to help protect, detect, and respond to threats in real time. 

Microsoft Threat Intelligence Center (MSTIC) 

Microsoft’s centralized team focused on identifying, tracking, and collecting intelligence against the most 

sophisticated and advanced adversaries impacting Microsoft customers, including nation state threats, malware, 

phishing, and more. The threat intelligence analysts and engineering teams in MSTIC work closely with Microsoft 

security product teams to both develop and refine high\-quality detections and defenses across our security 

product portfolio.

Security, Compliance, and Identity Business Development Team

A team that supports Microsoft security product teams in providing market insights into the latest cybersecurity 

trends to inform product development decisions. The team works on building partnerships with independent 

software vendors working with Microsoft’s security ecosystem. 

Microsoft Digital Defense Report \| October 2021

133
133

Microsoft Digital Defense Report \| October 2021© 2021 Microsoft. All rights reserved.