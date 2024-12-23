# Microsoft Digital Defense Report - October 2021

## Table of Contents
- [Introduction](#introduction)
- [The state of cybercrime](#the-state-of-cybercrime)
    - [Introduction](#introduction-1)
    - [The cybercrime economy and services](#the-cybercrime-economy-and-services)
    - [Ransomware and extortion](#ransomware-and-extortion)
    - [Phishing and other malicious email](#phishing-and-other-malicious-email)
    - [Malware](#malware)
    - [Malicious domains](#malicious-domains)
    - [Adversarial machine learning](#adversarial-machine-learning)
- [Nation state threats](#nation-state-threats)
    - [Introduction](#introduction-2)
    - [Tracking nation state threats](#tracking-nation-state-threats)
    - [What we're seeing](#what-were-seeing)
    - [Analysis of nation state activity this year](#analysis-of-nation-state-activity-this-year)
    - [Private sector offensive actors](#private-sector-offensive-actors)
    - [Comprehensive protections required](#comprehensive-protections-required)
- [Supply chain, IoT, and OT security](#supply-chain-iot-and-ot-security)
    - [Introduction](#introduction-3)
    - [Challenges in managing risk associated with the supplier ecosystem](#challenges-in-managing-risk-associated-with-the-supplier-ecosystem)
    - [How Microsoft thinks about supply chain](#how-microsoft-thinks-about-supply-chain)
    - [IoT and OT threat landscape](#iot-and-ot-threat-landscape)
    - [The 7 properties of highly secured devices](#the-7-properties-of-highly-secured-devices)
    - [Applying a Zero Trust approach to IoT solutions](#applying-a-zero-trust-approach-to-iot-solutions)
    - [IoT at the intersection of cybersecurity and sustainability](#iot-at-the-intersection-of-cybersecurity-and-sustainability)
    - [IoT security policy considerations](#iot-security-policy-considerations)
- [Hybrid workforce security](#hybrid-workforce-security)
    - [Introduction](#introduction-4)
    - [A Zero Trust approach for securing hybrid work](#a-zero-trust-approach-for-securing-hybrid-work)
    - [Identities](#identities)
    - [Devices/Endpoints](#devicesendpoints)
    - [Applications](#applications)
    - [Network](#network)
    - [Infrastructure](#infrastructure)
    - [Data](#data)
    - [People](#people)
- [Disinformation](#disinformation)
    - [Introduction](#introduction-5)
    - [Disinformation as an emerging threat](#disinformation-as-an-emerging-threat)
    - [Mitigation through media literacy](#mitigation-through-media-literacy)
    - [Disinformation as an enterprise disruptor](#disinformation-as-an-enterprise-disruptor)
    - [Campaign security and election integrity](#campaign-security-and-election-integrity)
- [Actionable insights](#actionable-insights)
    - [Introduction](#introduction-6)
    - [Summary of report learnings](#summary-of-report-learnings)
    - [Conclusion](#conclusion)
- [Contributing teams at Microsoft](#contributing-teams-at-microsoft)

# Microsoft Digital Defense Report  OCTOBER 2021

2
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Microsoft Digital Defense Report  |  October 2021
CHAPTER 1 
Introduction
3	
Introduction
 
 
5	
Our 2021 focus areas
CHAPTER 2 
The state of cybercrime
8	
Introduction 
 
8	
The cybercrime economy and services
 
 
10	
Ransomware and extortion 
20	
Phishing and other malicious email 
34	
Malware
 
 
38	
Malicious domains 
42	
Adversarial machine learning
CHAPTER 3 
Nation state threats
48	
Introduction 
49	
Tracking nation state threats 
 
52	
What we’re seeing 
57	
Analysis of nation state activity this year 
69	
Private sector offensive actors 
69	
Comprehensive protections required
CHAPTER 4 
Supply chain, IoT, 
and OT security
 
71	
Introduction 
 
72	
Challenges in managing risk associated with 
the supplier ecosystem 
73	
How Microsoft thinks about supply chain 
76	
IoT and OT threat landscape 
81	
The 7 properties of highly secured devices 
82	
Applying a Zero Trust approach to IoT solutions 
83	
IoT at the intersection of cybersecurity and 
sustainability 
84	
IoT security policy considerations
CHAPTER 5 
Hybrid workforce security
89	
Introduction 
91	
A Zero Trust approach for securing hybrid work 
 
93	
Identities 
98	
Devices/Endpoints
 
99	
Applications
 
100	 Network
 
104	 Infrastructure
 
105	 Data
106	 People
 
CHAPTER 6 
Disinformation
110	
Introduction 
 
111	
Disinformation as an emerging threat 
 
113	
Mitigation through media literacy 
114	
Disinformation as an enterprise disruptor 
117	
Campaign security and election integrity
 
CHAPTER 7 
Actionable insights
122	 Introduction 
 
123	 Summary of report learnings 
 
128	 Conclusion
 
Contributing teams at Microsoft
3
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION
ACTIONABLE INSIGHTS   TEAMS
Introduction
Our 2021 focus areas
Microsoft Digital Defense Report  |  October 2021
Introduction
   
TOM BURT, CORPORATE VICE PRESIDENT, CUSTOMER SECURITY & TRUST
Over the past year the world has borne witness to a burgeoning cybercrime economy and the rapid rise 
of cybercrime services. We have watched this global market grow in both complexity and fervency. We’ve 
seen the cyberattack landscape becoming increasingly sophisticated as cybercriminals continue—and even 
escalate—their activity in times of crisis. New levels of supply chain and ransomware attacks were a powerful 
reminder that we must all work together, and in new ways, to protect the cybersecurity of the planet.
We see transparency and information sharing 
as essential to the protection of the ecosystem. 
Knowledge brings power, and to that end, security 
professionals need diverse and timely insights into 
the threats they are defending against.
Microsoft serves billions of customers globally, 
allowing us to aggregate security data from a broad 
and diverse spectrum of companies, organizations, 
and consumers. Informed by over 24 trillion 
security signals per day, our unique position helps 
us generate a high-fidelity picture of the current 
state of cybersecurity, including indicators that help 
us predict what attackers will do next. Our goal in 
creating the Microsoft Digital Defense Report is to 
bring together integrated data and insights from 
more teams, across more areas of Microsoft than 
ever before. We will share what we’re seeing to help 
the global community strengthen the defense of the 
digital ecosystem, and we will include actionable 
learnings that companies, governments, and 
consumers can use to further secure individuals and 
environments.
The Microsoft Digital Defense Report draws on 
insights, data, and signals from across Microsoft, 
including the cloud, endpoints, and the intelligent 
edge. Note 1  Thousands of Microsoft security experts 
across 77 countries interpret and contribute to the 
insights gained from our advanced engineering 
and threat signals. Our security experts include 
analysts, researchers, responders, engineers, and 
data scientists. We also share lessons learned from 
customers transitioning to a hybrid workforce and 
frontline stories from our incident responders. Of 
course, there is malign activity we do not see, some 
of which is reported on by others in the industry. 
While the defender community at Microsoft works 
hard to identify threats and keep our customers 
informed, the bad actors are skilled and relentless. 
By continually sharing insights we and others in the 
industry derive from the work we do, we hope to 
empower everyone to defend the online ecosystem 
more effectively.
Microsoft has made significant and ongoing 
investments to increase and improve the knowledge 
we derive from our threat signals. These investments 
deliver the highly synthesized and integrated 
insights that we share here. Our goal in aggregating 
these learnings is to help organizations understand 
the ways in which cybercriminals are continually 
shifting their modes of attack—and determine the 
best ways to combat those attacks. We write and 
share this report in the spirit of empowering the 
global community to benefit from the insights, 
observations, and transparency generated by our 
unique mission and vantage point.
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
Note 1  These signals are collected with customer privacy in mind. The data we collect depends on the context of your interactions with Microsoft and the choices you make, including your privacy settings and the products and features you use.
    
3
Microsoft Digital Defense Report  |  October 2021
4
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Introduction
Our 2021 focus areas
Microsoft security signals
Volume and diversity of signals processed by Microsoft
Microsoft Digital Defense Report  |  October 2021
    
5
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Introduction
Our 2021 focus areas
Microsoft Digital Defense Report  |  October 2021
 Our 2021 focus areas
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
and signals from cross-company teams, five top-
level areas emerged as most critical to bring into the 
sharpest focus in this report: the state of cybercrime; 
nation state threats; supplier ecosystems, Internet 
of Things (IoT), and operational technology (OT) 
security; the hybrid workforce; and disinformation. 
To provide the greatest benefit, we also extract our 
recommendations and actionable learnings, and 
present them throughout the report and in our 
concluding chapter.
The state of cybercrime
In this chapter, we discuss new developments in 
the cybercrime economy and the growing market 
for cybercrime services. We provide updates and 
analysis of what we are seeing in ransomware and 
extortion, phishing and other malicious email, 
malware, and the use of domains by cybercriminals, 
presenting recommendations for mitigating risk 
in each area. Finally, we share what we’re seeing in 
adversarial machine learning and what we are doing 
to stay ahead of cybercriminals in this area.
Nation state threats
This chapter provides an update on what we’re 
seeing in nation state adversarial activity, including 
reports on seven activity groups we have not 
previously mentioned publicly. We provide an 
analysis of the evolving threats in this watershed 
year with an increased focus on on-premises servers 
and the exposure of widespread supply chain 
vulnerabilities. We conclude with a discussion about 
private sector offensive actors and our guidance for 
comprehensive protections.
Supply chain, IoT, and OT 
security
The highly publicized events of the last year have 
made clear that securing and managing risks 
associated with supplier ecosystems is critically 
important. This chapter covers some current 
challenges in doing so in the supplier ecosystem 
and presents how Microsoft thinks about end-to-
end supply chain security in nine investment areas. 
Then we turn our discussion to what we’re seeing 
in the Internet of Things (IoT) and operational 
technology (OT) threat landscape, with guidance on 
the properties of highly secured devices. We include 
specialized use cases of IoT and present some new 
research informing IoT policy considerations.
    
6
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Introduction
Our 2021 focus areas
Microsoft Digital Defense Report  |  October 2021
Hybrid workforce security
This chapter is about our greatest asset, our people. 
As we have moved to a hybrid workforce over 
the past year, we’ve seen developments in the 
threat landscape which point to the importance 
of adopting a Zero Trust approach. We include 
threat signals and other data across the six pillars 
of Zero Trust—identities, endpoints, applications, 
network, infrastructure, and data—and provide 
guidance based on what we’re seeing. We conclude 
with discussions about insider threats in hybrid 
work environments, and an empathy imperative 
for managing the new and significant challenges 
encountered by today’s workforce.
Disinformation
This chapter addresses the unprecedented 
disinformation campaigns and related cyber 
operations by state and non-state actors, 
impacting public awareness and knowledge as 
well as enterprise operations. We look at some 
parallels in cybersecurity and discuss mitigation 
through media literacy. We include a discussion on 
disinformation as an enterprise disruptor, providing 
a four-point plan for enterprise executives. The 
chapter concludes with an in-depth exploration of 
political campaign security and election integrity, 
two areas that have been targeted by disinformation 
campaigns.
Actionable insights
We open this year’s concluding chapter with a 
discussion of five paradigm shifts that will center the 
evolution of work around the inclusivity of people 
and data. The chapter concludes with a distilled look 
at the key learnings from all the previous chapters 
of this report: to minimize impact of attacks we 
must truly practice good cyber hygiene, implement 
architectures that support the principles of Zero 
Trust, and ensure cyber risk management is built into 
the business.
Microsoft Digital Defense Report  |  October 2021
6
    
7
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Microsoft Digital Defense Report  |  October 2021
TOC
INTRODUCTION
THE STATE OF CYBERCRIME
NATION STATE THREATS
SUPPLY CHAIN, IOT, AND OT SECURITY
HYBRID WORKFORCE SECURITY
DISINFORMATION
ACTIONABLE INSIGHTS
TEAMS
CHAPTER 2 
The state of cybercrime
Introduction
The cybercrime economy and services
Ransomware and extortion 
Phishing and other malicious email
Malware 
Malicious domains 
Adversarial machine learning
   
   
   
   
   
   
   
   
8
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Introduction
The cybercrime economy and services
Ransomware and extortion
Phishing and other malicious email
Malware
Malicious domains
Adversarial machine learning
Microsoft Digital Defense Report  |  October 2021
INTRODUCTION: The growing threat of cybercrime 
AMY HOGAN-BURNEY, GENERAL MANAGER, DIGITAL CRIMES UNIT
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
new laws regarding reporting, creating cross-
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
Other examples include selling compromised 
credentials that may have been obtained from 
phishing, scraping botnet logs or other credential 
harvesting techniques, imposter domain names, 
phishing-as-a-service, customized lead generation 
(for example, victims by country, industry, or roles), 
    
    
    
    
    
    
8
Microsoft Digital Defense Report  |  October 2021
9
loads (malicious software used to update malware 
on an infected computer), denial of service (DoS), 
and more. As an illustration, in some marketplaces, 
compromised credentials are offered by different 
sellers for $1.00 USD to $50.00 USD, depending on 
a variety of variables including the perceived value 
of the enterprise target. The number of sites offering 
services has significantly increased in the past 12 
months as well as volume of credentials and variety 
of phishing kits.
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Introduction
The cybercrime economy and services
Ransomware and extortion
Phishing and other malicious email
Malware
Malicious domains
Adversarial machine learning
Microsoft Digital Defense Report  |  October 2021
Among the services available to even amateur threat 
actors are the cryptocurrency escrow services (to 
ensure services are rendered as offered) that we 
often see in commodity ransomware campaigns 
where affiliate models have become firmly 
established. Nontechnical cybercriminals sign up with 
a ransomware affiliate where for 30% of the revenue, 
the affiliate network will supply the ransomware, 
recovery services, and payment services. The attacker 
then buys “loads” from a market and pushes the 
ransomware to the loads they purchased. They then 
sit back and collect their revenue. 
At times there are geographic groups of actors 
who may offer certain services, but most of these 
cybercrime markets are global in nature. A buyer 
in Brazil can obtain phishing kits from a seller in 
Pakistan, domains from the United States, victim 
leads from Nigeria, and proxies from Romania.
These prices have remained fairly steady over the 
past several years, but like any other market they 
vary according to changes in supply, demand, and 
externalities such as politics.  
KEY TAKEAWAYS:
-   Identity and password/phishing attacks are 
cheap, and on the rise. Why would an attacker 
break in when they can log in?
-   Distributed denial of service (DDoS) attacks 
are cheap for unprotected sites—about $300 
USD/month.
-   Ransomware kits are one of the many types of 
attack kits designed to enable low-skill attackers 
to perform more sophisticated attacks.
Average prices of cybercrime services for sale
Organizations now face an industrialized attacker economy with skill specialization and trading of illicit 
commodities. As seen in this snapshot of average prices, many commodities that can be purchased in 
the dark markets are very inexpensive, making attacks cheaper and easier to conduct (which also drives 
up attack volume).
Not all attacks work. It’s critical that we keep 
improving our defenses to increase the failure rate 
of attacks and the associated cost to attackers.
    
    
    
    
    
    
10
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Introduction
The cybercrime economy and services
Ransomware and extortion
Phishing and other malicious email
Malware
Malicious domains
Adversarial machine learning
Microsoft Digital Defense Report  |  October 2021
Ransomware 
and extortion 
Ransomware basics and 
taxonomy
Ransomware and extortion is a high-profit, low-cost 
business which has a debilitating impact on targeted 
organizations, national security, economic security, 
and public health and safety. What started as simple 
single-PC ransomware has grown to include a 
variety of extortion techniques enabled by human 
intelligence and is affecting the networks of all types 
of organizations across the globe.
This combination of real-time intelligence and 
broader criminal tactics, techniques, and procedures 
(TTPs) has maximized the impact of these attacks 
and driven the profits from these attacks to levels 
that were hard to imagine a few years ago. To put 
it in perspective, the publicly reported profits from 
ransomware and extortion attacks gives these 
attackers a budget that would likely rival the budgets 
of nation state attack organizations (without even 
counting the profits from attacks that never made 
the headlines).
To counter ransomware, a global collaborative 
effort between the private sector, law enforcement, 
and government is necessary to reduce the 
profitability of this crime, make it more difficult to 
enter the ransomware market, and supply victims 
with effective tools for efficient prevention and 
remediation. Microsoft is a contributor to the 
Ransomware Task Force report, a comprehensive 
framework designed for taking action in combatting 
ransomware. Note 2  Microsoft has also published a 
project plan with links to technical guidance to 
help organizations better prepare for and respond 
to these attacks and is contributing to a National 
Institute of Standards and Technology (NIST) 
publication containing a cybersecurity framework 
profile for ransomware risk management. Note 3 
A ransomware and extortion attack involves a 
threat actor deploying malware that encrypts 
and exfiltrates data and then holds that data 
for a ransom, often demanding payment in 
cryptocurrency. Rather than just encrypting a victim’s 
files and requesting a ransom in exchange for the 
decryption key, the attackers also exfiltrate sensitive 
data before deploying the ransomware. This 
practice prevents victims from disengaging from 
negotiations and raises the victim’s reputational 
costs of not paying the ransom as the attackers likely 
will not only leave the victim’s data encrypted but 
also leak sensitive information.
A series of criminal activities occur long before the 
ransomware is ultimately deployed across computer 
systems in an organization. As a result, we created a 
taxonomy that focuses on the relationship between 
entities within the ransomware ecosystem because 
any entity may play a different role at any given 
time.
Ransomware attacks have evolved into human-
operated ransomware, also known as “big game 
ransomware.”
Ransomware taxonomy
Primary role
Description
Develops
Writes the malware
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
    
    
    
    
    
    
Note 2  https://securityandtechnology.org/ransomwaretaskforce/report/  Note 3  https://aka.ms/humanoperated 
11
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Introduction
The cybercrime economy and services
Ransomware and extortion
Phishing and other malicious email
Malware
Malicious domains
Adversarial machine learning
Microsoft Digital Defense Report  |  October 2021
For example, as shown in the image at right, a threat 
actor may develop and deploy malware that gives 
one threat actor access to a certain category of 
victims, whereas a different threat actor may merely 
deploy malware.
 
Post-breach response
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
mitigation measures.  The incident response team 
will often provide the victim a report which includes 
root cause, criminal actor movement inside the 
victim network, data exposure and exfiltration, and 
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
Sample analysis of roles and relationships between entities within the ransomware ecosystem
Ransomware syndicates and affiliates are all working together toward these interconnected threats. 
Rather than one individual behind a ransomware attack, there are multiple groups of individuals, similar 
to a shared business model.
    
    
    
    
    
    
12
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Microsoft Digital Defense Report  |  October 2021
Introduction    The cybercrime economy and services    Ransomware and extortion    Phishing and other malicious email    Malware    Malicious domains    Adversarial machine learning
Stakeholders and roles involved in post-breach response
13
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Introduction
The cybercrime economy and services
Ransomware and extortion
Phishing and other malicious email
Malware
Malicious domains
Adversarial machine learning
Microsoft Digital Defense Report  |  October 2021
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
[sic]. We also calculated your possible losses from 
lawsuits from both your staff and your students for 
the leakage of their personal data. These fines will 
exceed $30 million. We are not talking about the 
loss of reputation, which in our opinion costs more.”
Ransomware negotiation chat
THE 
RANSOMWARE 
ENTERPRISE HAS 
EVOLVED INTO 
RANSOMWARE AS 
A SERVICE DRIVEN 
BY HUMAN 
INTELLIGENCE 
AND RESEARCH.
13
Microsoft Digital Defense Report  |  October 2021
    
    
    
    
    
    
14
TOC   INTRODUCTION   THE STATE OF CYBERCRIME   NATION STATE THREATS   SUPPLY CHAIN, IOT, AND OT SECURITY   HYBRID WORKFORCE SECURITY   DISINFORMATION   ACTIONABLE INSIGHTS   TEAMS
Introduction
The cybercrime economy and services
Ransomware and extortion
Phishing and other malicious email
Malware
Malicious domains
Adversarial machine learning
Microsoft Digital Defense Report  |  October 2021
There are few barriers of entry into this criminal 
enterprise. A cybercriminal does not need 
specialized code development skills to profit from 
this crime. The ransomware enterprise has evolved 
into ransomware as a service driven by human 
intelligence and research. It is no longer solely the 
province of malware developers; rather, the business 
structure is modular. Malware developers are 
recruiting hackers with access to networks promising 
a “cut” of the profit. Criminals can purchase malware 
and access to specific networks and target specific 
industries. This is effectively a crime syndicate where 
each member is paid for a particular expertise.
In the example shown below, following the crypto 
flows, we can see where a criminal enterprise split its 
bitcoin “earnings” such that approximately 15% of 
the earnings flowed to the developer/manager and 
75% of the earnings flowed to the attacker.
Regardless of where ransomware is deployed, 
typically the threat actors will demand payment via 
cryptocurrency through crypto wallets. Although 
the underlying blockchain technology facilitates 
transparent cryptocurrency flows, the owners of 
wallets remain pseudonymous. Nonetheless, they 
still need to find on- and off-ramps into the crypto 
ecosystem. At its core, the criminal actor needs 
to append the blockchain with a transaction and 
ultimately find a way to cash out. There are several 
stakeholders within the cryptocurrency ecosystem 
that facilitate ransom-related transactions and 
payments. These intermediaries often exist in 
jurisdictions with governments that are historically 
unwilling to cooperate with the United States 
and others. It’s these intermediaries that facilitate 
the flow of ill-gotten earnings from ransomware. 
The private sector through civil litigation, and 
the government through prosecution, regulatory 
enforcement, and international collaboration, can 
take coordinated action against intermediaries to 
disrupt the payment process.
SIDEBAR: TO PAY, OR NOT TO PAY?   
In the aftermath of a ransomware attack, companies 
are often completely offline—their security systems 
tampered with, their backup systems deleted, their 
data encrypted, and their users unable to log in. 
When operations are offline and losses pile up, it 
is important to remember that paying the ransom 
demands does not guarantee the restoration of 
operations, nor does paying prevent future attacks.
 
In addition, we have in effect, the classic “Tragedy 
of the Commons” Note 4— while it may make sense for 
individual victims to pay for their own individual 
benefit (restore critical business operations), the 
payment also contributes to the growth of this 
damaging model for everyone. Ransom payments 
can keep the cycle turning, as described below: 
-   The business model of extortionists gets 
reinforced, which also attracts more bad actors 
into the monetization strategy. Substantial 
revenue is supplied to the actors who then use 
part of it for research and development (R&D) 
to improve their tooling and ability to buy 
breach access to potential victim organizations. 
Some ransomware teams have significant 
amounts of funds for R&D and for buying high-
end 0-days. For example, some ransomware 
teams have budget to spend up to $1 million 
USD, or more, per 0-day. While some high-end 
ransomware teams buy 0-days, others