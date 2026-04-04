# Annual Cyber Threat Report 2024–2025

## Table of Contents
- [Foreword](#foreword)
- [About ASD’s ACSC](#about-asds-acsc)
- [About the contributors](#about-the-contributors)
- [Executive summary](#executive-summary)
- [Year in review](#year-in-review)
- [Australian cyber threat landscape](#australian-cyber-threat-landscape)
- [Who is targeting Australia](#who-is-targeting-australia)
- [What malicious cyber actors are targeting](#what-malicious-cyber-actors-are-targeting)
- [Common techniques used by malicious cyber actors](#common-techniques-used-by-malicious-cyber-actors)
- [Resilience](#resilience)
- [What you can do](#what-you-can-do)
- [ASD programs](#asd-programs)

---

## Foreword
I am pleased to present the Annual Cyber Threat Report 2024–25.

The world continues to face complex strategic circumstances. Competition and military build-up in the Indo-Pacific, and ongoing global conflicts are challenging Australia’s security and the global rules that have endured since World War II. In this uncertain environment, Australia’s relationships with friends and allies are more critical than ever.

Over the past year, we continued to see state-sponsored cyber actors targeting Australian networks to steal sensitive information.

Australia joined multi-country advisories warning of the threat of state-sponsored actors targeting critical infrastructure for the purposes of positioning for potential disruptive attacks. One such advisory details how People’s Republic of China-affiliated threat actors targeted the networks of major global telecommunications providers to conduct a broad and significant cyber espionage campaign. Another details a Russian state-sponsored cyber campaign targeting Western logistics and technology businesses. I urge Australian businesses to review and apply the ASD and its partners’ technical advice to protect your networks.

Cybercriminals also relentlessly targeted Australians, with ransomware attacks and data breaches increasing in frequency. Using malware designed to covertly harvest information from Australian victims, cyber criminals used stolen data, usernames and passwords to launch subsequent attacks, compromise corporate networks and accounts.

The Australian Government continues to invest in the nation’s cyber capabilities through project REDSPICE, which doubles ASD’s size and ability to strike back against malicious cyber activity. In February 2025, the Australian Government imposed cyber sanctions on a Russian business and its employees for storing and facilitating the theft of millions of incredibly personal digital records posted by cybercriminals on the darkest corners of the internet. The sanctions were preceded and enabled by ASD’s targeted offensive cyber activity which disrupted criminal infrastructure used to host stolen personally identifiable information (PII) of millions of victims around the world.

This was the first time Australia imposed cyber sanctions on an entity responsible for providing the infrastructure facilitating cybercrime. It was made possible by ASD’s hard work and delivered in collaboration with domestic and international industry, intelligence and law-enforcement partners.

This report outlines the cyber threats the nation is facing. All Australians have a role in taking action to increase Australia’s cyber resilience.

The Hon Richard Marles MP
Deputy Prime Minister and Minister for Defence

---

## About ASD’s ACSC
The Australian Signals Directorate’s Australian Cyber Security Centre (ASD’s ACSC) is the Australian Government’s technical authority on cyber security. Through the ACSC, ASD brings together capabilities to improve Australia’s national cyber resilience. Its services include:

- Providing the Australian Cyber Security Hotline, which is contactable 24 hours a day, 7 days a week, via 1300 CYBER1 (1300 292 371)
- Providing technical advice and publishing alerts, advisories and notifications on significant cyber security threats
- Monitoring cyber threats and sharing intelligence with partners, including through the Cyber Threat Intelligence Sharing platform (CTIS)
- Helping Australian organisations respond to cyber security incidents
- Providing exercises and uplift activities designed to enhance the cyber security resilience of Australian organisations
- Supporting collaboration between over 133,000 Australian organisations and individuals on cyber security issues through ASD’s Cyber Security Partnership Program.

Collaboration and partnerships are key to effective cyber security. ASD’s ACSC thanks all the organisations that contributed to this report, including federal, state and territory government agencies, industry partners, and all who reported cyber security matters to ASD’s ACSC.

---

## About the contributors
- **Australian Federal Police**: Responsible for enforcing Commonwealth criminal law and combatting complex transnational, serious, and organised crime.
- **Australian Institute of Criminology**: Australia’s national research and knowledge centre on crime and justice.
- **Australian Security Intelligence Organisation**: Protects Australia and Australians from threats to their security, including terrorism, espionage, sabotage, and foreign interference.
- **Department of Foreign Affairs and Trade**: Promotes and protects Australia’s international interests.
- **Department of Home Affairs**: Leads the development of cyber security policy and national resilience.
- **National Cyber Security Coordinator**: Leads the coordination of national cyber security policy and responses to major incidents.
- **Defence Intelligence Organisation**: Co-leads the ACSC’s cyber threat assessment team.
- **Office of the Australian Information Commissioner**: Regulates compliance with the Privacy Act 1988.
- **Australian Competition and Consumer Commission**: Runs the National Anti-Scam Centre to disrupt scams.

---

## Executive summary
Australia is an early and substantial adopter of digital technology which drives public services, productivity and innovation. Our increasing dependency on digital and internet-connected technology means Australia remains an attractive target for criminal and state-sponsored cyber actors.

In FY2024–25, ASD’s ACSC received over 42,500 calls to the Australian Cyber Security Hotline, a 16% increase from the previous year. ASD’s ACSC also responded to over 1,200 cyber security incidents, an 11% increase. During FY2024–25, ASD’s ACSC notified entities more than 1,700 times of potentially malicious cyber activity – an 83% increase from last year – highlighting the ongoing need for vigilance and action to mitigate against persistent threats.

State-sponsored cyber actors continue to pose a serious and growing threat to our nation. They target networks operated by Australian governments, critical infrastructure (CI) and businesses for state goals. State-sponsored cyber actors may also seek to use cyber operations to degrade and disrupt Australia’s critical services and undermine our ability to communicate at a time of strategic advantage.

The threat from cybercrime also continues to challenge Australia’s economic and social prosperity, with average reported financial losses, the frequency of ransomware attacks and the number of reported data breaches all increasing throughout FY2024–25. Cybercriminals are continuing their aggressive campaign of credential theft, purchasing stolen usernames and passwords from the dark web to access personal email, social media or financial accounts.

Malicious cyber actors are able to leverage vulnerabilities in the technology and security practices of individuals and businesses throughout the public and private sectors. Internet-facing vulnerabilities in edge devices are common, and they require network owners to rigorously monitor and configure securely. ‘Living off the land’ tradecraft has persevered, requiring an adjustment in the way network defenders prioritise understanding behavioural patterns of networks in order to detect the most sophisticated threats.

The prevalence of artificial intelligence (AI) almost certainly enables malicious cyber actors to execute attacks on a larger scale and at a faster rate. The potential opportunities open to malicious cyber actors continue to grow in line with Australia’s increasing uptake of – and reliance on – internet-connected technology.

CI is, and will continue to be, an attractive target for state-sponsored cyber actors, cybercriminals, and hacktivists, largely due to large sensitive data holdings and the critical services that support Australia’s economy. ASD’s ACSC notified CI entities of potential malicious cyber activity impacting their networks over 190 times in the last reporting period – up 111% from the previous year.

The threat environment combined with our operational observations set out in this report underscores the need for all Australian individuals, private and public entities to take action to uplift our cyber resilience at every level. Every individual can uplift their cyber defences through basic actions. Use strong Multi-Factor Authentication (MFA) wherever possible, use strong and unique passwords or passphrases, keep software on devices updated, be alert for phishing messages and scams, and regularly back up important data. These basics have never been more important, and implementing these mitigations can prevent the majority of the cyber incidents reported to ASD’s ACSC.

Businesses should operate with a mindset of ‘assume compromise’ and prioritise the assets or ‘crown jewels’ that need the most protection. ASD recommends businesses and network owners focus on 4 ‘big moves’ to bolster their cyber defences and prepare for future challenges: implement best-practice logging, replace legacy IT, effectively manage third-party risk and prepare for post-quantum cryptography.

For those businesses also operating operational technology (OT), follow best-practice guidance for isolating vital OT and enabling systems, and have a plan for how to rebuild.

For large organisations, ensuring technology used or provided to customers is secure-by-design and secure-by-default is critical for building modern networks that protect data and systems.

The years ahead will bring challenges for organisations in emerging technology, such as post-quantum cryptography. ASD’s ACSC will continue to work with Australian industry and partner organisations to ensure the continued security of our communications and sensitive data. Effective transition plans will be critical to operating in 2030 and beyond – a post-quantum computing world – and this planning must start now.

Businesses must ensure that, in order to harness the full benefits and productivity associated with AI, a safe and secure approach is taken to the integration of AI technologies.

It remains critically important that organisations and individuals who observe suspicious cyber activity, incidents and vulnerabilities report to ReportCyber at cyber.gov.au, or to the Australian Cyber Security Hotline 1300 CYBER1 (1300 292 371).

---

## Year in review
![Infographic showing 42,500+ hotline calls, 84,700+ cybercrime reports, and increased financial losses for businesses]

- **Hotline**: Answered over 42,500 calls (up 16%).
- **ReportCyber**: Received over 84,700 reports (down 3%).
- **Financial Impact**: Average self-reported cost per business report up 50% ($80,850).
- **Incidents**: Responded to over 1,200 cyber security incidents (up 11%).
- **Notifications**: Notified entities of malicious activity 1,700+ times (up 83%).
- **DNS**: Australian Protective Domain Name System blocked 334 million malicious domains (up 307%).

---

## Australian cyber threat landscape
### Who is targeting Australia
Australia’s economy and geostrategic position make it an attractive target for various malicious cyber actors.

#### State-sponsored cyber actors
Over FY2024–25, state-sponsored cyber actors targeted Australian networks, and they continue to present an active and evolving cyber threat to Australia. State-sponsored cyber actors conduct operations to serve political and military objectives, including cyber espionage, malign influence, interference and coercion, or to pre-position for disruptive and destructive cyber effects in the event of crisis or conflict.

State-sponsored cyber actors routinely target Australian government networks for cyber espionage purposes. Government and defence-related information is an attractive target for state-sponsored cyber actors seeking strategic insights into Australia’s national policies and decision-making.

#### Cybercriminals
Cybercrime continues to challenge Australia’s economic and social prosperity. Cybercrime is persistent and damaging across all facets of Australia’s economy as financially motivated cybercriminals are willing to exploit any available opportunity for profit. ASD focuses on countering top-tier financially motivated cybercriminals and their enablers – we continue to see this threat emanating from the Eastern European region and Russian speaking cyber gangs.

---

## What malicious cyber actors are targeting
Both individuals and businesses are commonly targeted by malicious cyber actors for financial gain. This can be through scams or through the on-selling of personally identifiable information (PII) or usernames and passwords online.

State-sponsored cyber actors continue to target networks across government and industry to support political, economic and military objectives.

CI may be targeted by malicious cyber actors to conduct espionage, degrade confidence in systems, interrupt service availability, or pre-position for disruptive or destructive effects.

---

## Common techniques used by malicious cyber actors
- **Living off the Land (LOTL)**: Using built-in network administration tools to carry out objectives and evade detection.
- **Credential Theft**: Purchasing stolen usernames and passwords from the dark web.
- **Information Stealers**: Malware designed to infect a device, collect valuable data, and deliver it to cybercriminals.
- **Ransomware**: Encrypting data and threatening to release it if demands are not met.
- **Generative AI**: Used to automate analysis of datasets and create high-quality phishing content.

---

## Resilience
Businesses should operate with a mindset of ‘assume compromise’ and prioritise the assets or ‘crown jewels’ that need the most protection. ASD recommends businesses and network owners focus on 4 ‘big moves’ to bolster their cyber defences and prepare for future challenges: implement best-practice logging, replace legacy IT, effectively manage third-party risk and prepare for post-quantum cryptography.

---

## What you can do
Every individual can uplift their cyber defences through basic actions:
- Use strong Multi-Factor Authentication (MFA) wherever possible.
- Use strong and unique passwords or passphrases.
- Keep software on devices updated.
- Be alert for phishing messages and scams.
- Regularly back up important data.

---

## ASD programs
- **Cyber Hygiene Improvement Programs (CHIPs)**: Performed 478 high-priority operational taskings.
- **Government Uplift Program**: Ongoing engagements to improve cyber maturity across government agencies.
- **Critical Infrastructure Uplift Program**: Completed 8 CI uplifts covering 38 assets.
- **Cyber Security Partnership Program**: Grew by 11% to over 133,000 partners.

---

ry
detailed 2 case studies involving mobile-device spyware known as BADBAZAAR and MOONSHINE.

The advisory, BADBAZAAR and MOONSHINE: Spyware targeting Uyghur, Taiwanese and Tibetan groups and civil
society actors is available at cyber.gov.au.

27

Compared to FY2023–24, financial and insurance
services rose to be the most frequently reporting
non-government sector. Some of this rise is
attributable to DDoS activity targeting the
financial sector. Education and training dropped
out of the top 5 reporting sectors, while reporting
from the electricity, gas, water and wastewater
services sector was down from 5% to 2% of
all incidents.

Within the government sector, Federal Government
reporting was down from 37% to 32%, while state
and local government reporting was up from
12% to 14% of all incidents.

Federal Government

32%

State and local
government

14%

Financial and
insurance services

Health care and
social assistance

Information media and
telecommunications

Professional, scientiﬁc
and technical services

Transport, postal
and warehousing

Education
and training

7%

6%

6%

6%

5%

5%

Construction

3%

Retail trade

3%

Figure 6: Top 10 reporting
sectors from incidents
reported to ASD’s ACSC

Cybercrime reports by state and territory

12%

1%

7%

Australia’s more populous states
– Queensland, Victoria and
New South Wales – continue to
report more cybercrime than
any other state or territory,
with disproportionately higher
reporting rates relative to their
populations.

The Australian Capital Territory
reported the highest average
self-reported financial losses –
around $37,700 per cybercrime
report – followed by those in
New South Wales, with around
$33,000. Northern Territory also
closely followed with around
$32,000 per cybercrime report
where a financial loss occurred.

28%

22%

26%

2%

2%

0%

100%

Figure 7: Breakdown of cybercrime reports by jurisdiction for FY2024–25

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Australian cyber threat landscape    //

28

Critical infrastructure

CI is, and will continue to be, an attractive target for state-sponsored cyber actors, cybercriminals and
hacktivists, largely due to the sensitive data it holds and its role in providing services that support Australia’s
national resilience, sovereignty and prosperity.

State-sponsored cyber actors routinely target Australia’s CI networks, possibly to conduct espionage
or to pre-position for disruptive and destructive cyber effects in the event of crisis or conflict. In crisis or
conflict, access to a CI network can provide a malicious cyber actor with control over Australia’s CI systems,
which could lead to a degradation in the confidence of systems, major disruptions to availability, or even
destructive effects.

Cybercriminals continue to opportunistically target CI operators. The sensitivity of the data stored by these
entities, and the importance of their services, makes them attractive for cybercriminals seeking to extort victims.

CI often relies on complex information technology (IT) and operational technology (OT) networks, with
complex supply chains. While these networks allow CI providers to deliver services to the Australian people,
they also present an ever-growing attack surface, which includes both the provider themselves and those
within their supply chain.

CI made up 13% of all incidents, up 2% from last year

The 3 most common activity types leading to critical
infrastructure-related incidents were:
 Scanning or Reconnaissance (41%)
 DoS/DDoS (31%)
 Phishing (20%)

Top 3 ANZSIC Divisions for CI incidents:
 Financial and insurance services (32%)
 Transport, postal and warehousing (26%)
 Information media and telecommunications (16%)

29

Highlight 7: Russian GRU targeting Western logistics entities and
technology companies

In May 2025, ASD’s ACSC joined international partners in highlighting a Russian state-sponsored cyber
campaign targeting Western logistics entities and technology companies. This includes those involved in the
coordination, transport and delivery of foreign assistance to Ukraine.

For over 2 years, the Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service
Center (85th GTsSS), military unit 26165 – commonly known in the cyber security community as APT28, Fancy
Bear, Forest Blizzard, BlueDelta, and a variety of other identifiers – has conducted this campaign using a mix
of known TTPs, including reconstituted password spraying capabilities, spearphishing, and modification of
Microsoft Exchange mailbox permissions.

In late February 2022, multiple Russian state-sponsored cyber actors increased the variety of cyber operations
for purposes of espionage, destruction, and influence – with unit 26165 predominately involved in espionage.
As Russian military forces failed to meet their military objectives and Western countries provided aid to support
Ukraine’s territorial defence, unit 26165 expanded its targeting of logistics entities and technology companies
involved in the delivery of aid. These actors have also targeted internet-connected cameras at Ukrainian
border crossings to monitor and track aid shipments.

The advisory, Russian GRU targeting Western logistics entities and technology companies is available at cyber.gov.au.

IN FOCUS: The threat to telecommunications providers

Malicious cyber actors continue to target the telecommunications sector globally for espionage
purposes. Telecommunications networks are attractive targets because of the valuable data they store
and communicate. Access to these networks can also enable follow-on targeting of telecommunications
customers. Sustained disruption of telecommunications services would probably cause follow-on
disruptive effects to other CI entities who rely on telecommunications for internet and phone services.

On 4 December 2024, ASD’s ACSC joined international partners to publish an advisory warning
that PRC-affiliated malicious cyber actors had compromised the networks of major global
telecommunications providers as part of a broad and significant cyber espionage campaign.

The advisory provides network engineers and defenders of communications
infrastructure with best practices to strengthen their visibility and harden
their network devices against successful exploitation carried out
by PRC-affiliated and other malicious cyber actors.

The advisory, Enhanced visibility and hardening guidance for
communications infrastructure, can be found at
cyber.gov.au.

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Australian cyber threat landscape    //

30

IN FOCUS: The threat to the healthcare sector

Disruption of Australian healthcare networks can endanger patients, making the healthcare sector
vulnerable to extortion by cybercriminals. Healthcare data is also valuable on dark web forums as it
directly enables other criminal activities, like fraud and identity theft.

The frequency of cybercrime incidents against the healthcare sector in Australia is increasing.
Compared to FY2023–24, the number of ransomware incidents against the healthcare sector
doubled in FY2024–25, endangering patient safety and destabilising health systems. Malicious cyber
actors were successful in 95% of all health care and social assistance sector incidents that ASD’s ACSC
responded to in FY2024–25, in comparison to nearly 52% of incidents across all sectors.

In July 2024, an e-prescription service notified customers of a cyber security incident. With the
assistance of the AFP under the joint arrangement Operation Aquila, the incident was investigated
with support from ASD’s ACSC.

In a suspected ransomware attack, malicious cyber
actors exfiltrated approximately 6.5TB of data from
the e-prescription services database server that had
data stored from March 2019 to November 2023. This
data included the personal and health information of
approximately 12.9 million Australian customers who
used the e-prescription service during this time.

31

Common techniques used by malicious cyber actors

■ ASD’s ACSC has observed a range of common techniques that malicious cyber actors use to exploit
vulnerabilities in technology and systems, which we map against the MITRE ATT&CK framework.

■ Identifying and understanding exposure to these vulnerabilities is a critical first step towards

reducing the risk of successful compromise by these actors.

■ Chapter 2: Resilience outlines steps that can make it harder for malicious cyber actors to

successfully exploit these vulnerabilities.

Analysing incidents using the MITRE ATT&CK
framework

The MITRE ATT&CK framework is an open-source knowledge base of adversary tactics and techniques,
derived from real adversary observations, which provide a common language for describing,
understanding and analysing cyber threats.

Adversary behaviours are organised into a matrix – tactics, the ‘goal’ of the adversary; and techniques,
the ‘approach’ of the adversary. ATT&CK empowers organisations to mature their cyber security posture
through detection and mitigation strategies based on real-world observed adversary behaviours.

Phishing
(Initial Access)

38%

Compromise Accounts
(Resource Development)

31%

Gather Victim Identity Information
(Reconnaissance)

30%

User Execution
(Execution)

Valid Accounts
(Multiple Tactics)

Network Denial of Service
 (Impact)

Acquire Infrastructure
(Resource Development)

Phishing for Information
(Reconnaissance)

Impersonation
(Defence Evasion)

Data Encrypted for Impact
(Impact)

16%

14%

12%

12%

10%

10%

10%

Figure 8: Prevalence of
top 10 MITRE ATT&CK
techniques in FY2024–25

Note: The occurrence of MITRE ATT&CK techniques does not total 100% as multiple techniques can be identified in
each incident. Technique prevalence will also likely skew towards techniques that occur across multiple tactics, and
to pre-compromise techniques, as not all incidents are successful.

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Common techniques used by malicious cyber actors

Differences in reported techniques between government and
industry reporting

Australian cyber threat landscape    //

32

Government Incidents

Industry Incidents

Phishing (52%)

Phishing (25%)

Compromise Accounts (39%)

Compromise Accounts (24%)

Gather Victim Identity Information (38%)

Gather Victim Identity Information (23%)

User Execution (22%)

Valid Accounts (23%)

Acquire Infrastructure (16%)

Data Encrypted for Impact (18%)

Phishing for Information (15%)

Exploit Public-Facing Application (10%)

Network Denial of Service (15%)

User Execution (10%)

Impersonation (11%)

Network Denial of Service (10%)

Compromise Infrastructure (10%)

Financial Theft (9%)

Stage Capabilities (9%)

Brute Force (9%)

Figure 9: Top 10 MITRE ATT&CK techniques in government and industry reporting

Over FY2024–25, Phishing, Compromise Accounts, and Gather Victim Identity Information were the top 3
observed techniques across government and non-government incident reports.

Government reporting predominately featured techniques early in the cyber attack chain. Conversely,
18% of industry reporting involved data encrypted for impact compared to <1% in government reporting.
This technique is often observed in ransomware incidents in which a cyber threat actor encrypts data to
demand a ransom. Similarly, Exploit Public-Facing Application (10%) and Financial Theft (9%) were much
higher than in government entities (2% and 1% respectively).

This may reflect a number of different factors, including different reporting cultures and requirements, or
awareness of where to report in the event of a cyber incident.

Initial access techniques in data encryption incidents
In FY2024–25, ASD’s ACSC observed that, in incidents where data was encrypted for impact, the most
common means of gaining initial access was through using already compromised credentials (Valid
Accounts) and accessing networks via legitimate external-facing services (External Remote Services).

33

Social engineering

Social engineering is a longstanding threat that is becoming easier for malicious cyber actors to use at scale,
thanks in part to AI technologies.

Phishing – a type of social engineering – was recorded as an initial access technique in 38% of the incidents
reported to ASD’s ACSC in FY2024–25.

Social engineering techniques are used by malicious cyber actors to direct individuals or staff into performing
specific actions such as opening an attachment, visiting a website, revealing credentials, disclosing sensitive
information, or transferring funds. Social engineering techniques can be highly convincing.

If you suspect a social engineering attempt, do not engage – hang up. Do not delete or forward the
communication. Report it immediately to your organisation’s cyber security or IT support team for advice.
Preserving the communication is important for investigation and threat response.

Denial of Service

DoS attacks are cyber attacks designed to disrupt or degrade online services such as websites, email and
Domain Name System (DNS) services, in order to deny access to legitimate users. A DDoS attack is a type of
DoS attack using multiple computers or other internet-connected devices to direct network traffic at online
services, from multiple directions and on a much larger scale.

DDoS is becoming increasingly available to a range of actors, regardless of technical proficiency. Growth in
areas such as AI, as well as a growing botnet attack surface, is lowering the bar for less capable adversaries
to engage in DDoS attacks. AI empowers a DDoS attack through autonomously running algorithms that
manage complex botnets. Additionally, by using AI to manage botnets, malicious cyber actors can rapidly
adjust their code to evade detection.

The rise of DDoS attacks against Australian organisations has the potential to cause significant disruptions
across the Australian economy. ASD’s ACSC responded to more than 200 incidents involving DoS or DDoS
attacks, up more than 280% from last year. DoS and DDoS were present almost twice as often (31%) in
incidents against CI entities when compared with all incidents ASD’s ACSC responded to (16%).

Additionally, industry reporting indicates that June 2025 may have had the most DDoS incidents on record.
This increase follows an obvious upwards trend in the number of reported DDoS attacks over the last 5 years,
with FY2021–22 having had more than 20 DDoS attacks, while FY2022–23 had more than 50.

Public admin
and safety

60%

Financial and
insurance services

17%

Transport, postal
and warehousing

10%

Information media and
telecommunications

Professional, scientiﬁc
and technical services

3%

3%

Figure 10: Top 5 reporting
sectors for DoS/DDoS incidents

In March 2025, ASD’s ACSC, in cooperation with New Zealand’s National Cyber Security Centre (NCSC-NZ),
Akamai Technologies Ltd and Cloudflare Pty Ltd, published updated advice on preparing for and
responding to DoS attacks. For more information visit Preparing for and responding to denial-of-service attacks
on cyber.gov.au.

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Australian cyber threat landscape    //

34

Vulnerabilities create opportunities

Malicious cyber actors often rely on common gaps in cyber defences to achieve their objectives. There are also
emerging security challenges that will create more opportunities for malicious cyber actors to target Australia.

Stolen data
Malicious cyber actors often use stolen personal information to appear legitimate
and improve the success rate of their phishing campaigns. They can also use
stolen credentials to gain access to other networks or accounts that use the same
or similar credentials. Many individuals and organisations are not aware of the full
extent and criminal value of their sensitive information published online.

Vulnerable devices and software
Malicious cyber actors commonly exploit vulnerable devices and software. In
FY2024–25, the number of publicly reported common vulnerabilities and exposures
increased by 28%. Edge devices and legacy IT are notable examples of systems
that are often difficult for network defenders to secure effectively.

IT supply chains
An organisation’s supply chain can often be its weakest link. Malicious cyber actors
may attempt to compromise an end consumer at multiple points in the supply
chain, exploiting trusted relationships between the vendor and the customer to
steal information or deliver malware or vulnerable products.

Gaps in event logging
Malicious cyber actors thrive when target organisations lack an established
baseline or logging policy that support effective detection and response. Malicious
cyber actors can exploit gaps in event logging to evade detection and even retain
unauthorised access after a victim investigates the compromise.

35

Edge devices
ASD’s ACSC often sees malicious cyber actors using vulnerabilities in edge devices to achieve their goals.
Edge devices are critical network components, positioned at the network’s periphery – often referred to as
‘the edge’. These devices connect a private network, such as your home or work, with a public, untrusted
network like the internet. The most common edge devices used include home and enterprise routers,
firewalls and virtual private network (VPN) products.

Edge devices are attractive targets for malicious cyber actors because internet-facing vulnerabilities in
edge devices are common, and they are often difficult for network owners to monitor or configure securely.
These vulnerabilities provide malicious cyber actors with a greater chance of successfully compromising a
network. By successfully exploiting such technologies, malicious cyber actors can gain an initial foothold on
a network for follow-on activity. Malicious cyber actors can also use compromised edge devices as proxies,
which can help hide their identity when targeting other networks.

In FY2024–25, ASD’s ACSC observed more than 120 incidents associated with attacks on edge devices, of
which 96% were successful.

In FY2024–25, ASD’s ACSC released and co-sealed a series of publications focusing on improving the security and
resilience of edge devices against cyber threats. These publications were supported by international partners
including the US, Canada, New Zealand, UK and Japan. These publications are available at cyber.gov.au.

Malicious Actor

Internet Layer

Edge Layer

Device Layer

By compromising the
edge device, the
malicious cyber actor
can further exploit other
connected devices or
networks. Other
connected devices
may include:

• Phones/Tablets

• Computers/Consoles

• Smart home appliances

Malicious cyber
actor intends to
compromise a
network

Malicious cyber actor
uses the internet to
ﬁnd vulnerable edge
devices

Malicious cyber actor
exploits internet-facing
vulnerabilities in an
edge device

Figure 11: How network edge devices may be exploited for follow on activity

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Australian cyber threat landscape    //

36

Highlight 8: PRC-linked cyber actors compromise routers and Internet of Things
devices for botnet operations

In September 2024, ASD’s ACSC joined international partners to publish an advisory that highlights the
threat posed by PRC-linked cyber actors’ botnet activity.

PRC-linked cyber actors had compromised thousands of internet-connected devices, including SOHO
routers, firewalls, network-attached storage and Internet of Things (IoT) devices to create a network – or
‘botnet’ – positioned for malicious activity. The botnet consisted of over 260,000 devices, including devices
in Australia. The cyber actors may use botnets like this as a proxy to conceal their identities while they
deploy DDoS attacks or further target and compromise networks.

The advisory, People’s Republic of China-Linked Actors Compromise Routers and IoT Devices for Botnet
Operations can be found on cyber.gov.au.

Malicious Actor

Internet Layer

Edge Layer

Targets

Small
businesses

Medium,
Large businesses

Critical
infrastructure

Government
departments

Malicious cyber actor may
trigger a DDoS attack against
a target to disrupt or degrade
online systems or services

Malicious cyber actor
intends to compromise
multiple network edge
devices to build a
botnet

Malicious cyber
actor uses the
internet to ﬁnd
vulnerable edge
devices

Malicious cyber actor
exploits internet-facing
vulnerabilities in edge
devices and installs
malware

Figure 12: How network edge devices may be used as a botnet

37

Legacy IT

Legacy IT is hardware, software, services, protocols and/or systems that are considered end-of-life or are no
longer supported by the vendor or developer.

Keeping legacy IT on a network increases the likelihood of a cyber security incident. It can also make any
cyber security incident that does occur much more impactful. For example, malicious cyber actors can
use legacy IT to gain an initial foothold on a network, or to gain access to more modern systems that
organisations rely on.

There are also significant business risks associated with legacy IT. For example, legacy IT can increase the
likelihood that an organisation will have systems taken offline, service delivery disrupted, data destroyed or
leaked, and public confidence lost.

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Australian cyber threat landscape    //

38

Chapter 2

Resilience

Resilience    //

40

What you can do

■ The basics are still our most effective first line of defence. All Australian small businesses and
individuals should use strong MFA wherever possible, use strong and unique passwords or
passphrases, keep software on devices updated, be alert for phishing messages and scams, and
regularly back up important data.

■ For businesses running a network, there are 4 big moves you can make to protect yourself:
implement effective logging, replace legacy IT, effectively manage third-party risk and start
preparing for post-quantum cryptography.

■ For businesses that also manage OT, follow best-practice guidance for isolating vital OT and

enabling systems, and have a plan for how to rebuild.

■ Have a cyber security incident response plan and test it regularly to ensure a prioritised and

effective response to an incident. It is vital that suspicious activity, cyber security incidents, and
vulnerabilities are reported to ASD’s ACSC at cyber.gov.au/report.

Resilience for all Australians

For small businesses and individuals, the basics have never been more important. Everyone can take steps
to protect their most valuable asset – their information – and significantly reduce personal risks while
engaging technology. The most effective cyber defences are also some of the easiest to use and fastest to
setup. The top things Australians can do are:

■ Use phishing-resistant MFA wherever possible,

preferably passkeys

■ If you use passwords or passphrases, make

them strong and unique, and consider using a
reputable password manager

■ Keep software on devices updated, and only
use a trusted device when accessing sensitive
online accounts

 — For example, use your bank’s app on your
smartphone to perform internet banking

■ Regularly back up important files and device

■ Report cyber incidents to ASD’s ACSC.

configuration settings

■ Be alert for phishing messages and scams

At cyber.gov.au, ASD’s ACSC has published a range of simple how-to guides for all Australians, including
children and seniors, that explain how individuals and families can improve their home cyber security.

41

The 4 key actions for organisations

You can’t defend what you can’t see
Implement effective event logging

Logging is crucial for detecting threats and keeping networks secure. Effective event logging
can provide critical insights into a cyber security incident and reduce the overall cost of
responding to them.

In August 2024, ASD’s ACSC, in cooperation with international partners, published Best
practices for event logging and threat detection.

In May 2025, ASD’s ACSC also jointly published a suite of guidance to assist organisations
implement Security Information and Event Management (SIEM) and Security Orchestration,
Automation, and Response (SOAR) platforms.

These publications can be found on cyber.gov.au.

Old technology lets threats thrive
Manage legacy IT risks

Remediating a cyber security incident involving legacy IT, and managing its consequences,
may involve high financial costs. It is always less costly to mitigate the risks of legacy IT
before a major cyber security incident occurs.

The most effective strategy to eliminate the risks associated with legacy IT is to replace it with
IT that is still receiving support – whether that support is internal or external. Where this is
not feasible, or replacing legacy IT will take time, temporary measures should be adopted to
mitigate some of the risk.

For more information on managing the risks of legacy IT, visit cyber.gov.au.

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Resilience    //

42

Shut the back door
Choose secure and verifiable technologies

The security of an organisation’s supply chain for the digital products and services they operate is
paramount as malicious actors may attempt to compromise an end consumer at multiple points in
their supply chain.

The procurement of any digital product or service increases the attack surface of an organisation’s
information environment. It is critical to understand the threat environment and the possible supply
chain attack vectors so organisations can identify and manage the risks through pre-purchase and
post-purchase risk management.

In December 2024, ASD’s ACSC published an updated version of its Choosing Secure and Verifiable
Technologies and an accompanying executive guidance publication. Both publications were co-sealed
with our international partners in the US, Canada, UK, New Zealand and the Republic of Korea, as part
of the global campaign for secure-by-design.

Plan, educate, anticipate
Start preparing for post-quantum cryptography

A cryptographically relevant quantum computer (CRQC) is on the horizon, which means Australia must
start preparing for post-quantum cryptography (PQC).

A CRQC is a quantum computer capable of breaking contemporary public key cryptography. The
creation of a CRQC presents new cyber security risks as adversaries may use CRQC capabilities to
compromise communications based on current public key cryptography technology.

PQC is the best way to protect our networks from the future quantum computing threat. PQC uses
cryptographic algorithms that are different to the algorithms used in public key cryptography and are
highly unlikely to be broken by a CRQC.

For more information, visit Guidelines for Cryptography and Planning for Post-Quantum Cryptography on
cyber.gov.au.

43

Compromised
asset, network or
infrastructure

50%

Compromised
account or
credentials

42%

Ransomware

34%

 Change default credentials for network devices
  Enable phishing-resistant MFA for network devices where supported
 Disable unneeded functionality of network devices, especially

those that are internet-facing

 Keep network devices up to date, replace devices no longer

supported by vendors.

 Use phishing-resistant MFA, such as passkeys, where possible
 Identify and change compromised or unsecured credentials
 Find and remove inactive user and service accounts
 Implement robust and secure credential management practices
 Disable remote management of network devices over the internet.

 Backup important data regularly in a secure and proven manner
 Keep operating systems and applications up to date, replace

software no longer supported by vendors

 Implement antivirus software
 Implement application control.

Figure 13: Top 3 reported incidents categorised C3 and above, with relevant mitigations

Note: Incidents can have multiple incident types ascribed to them and hence do not add up to 100%. Incidents
categorised as C3 or above involved organisations such as federal and state governments, large organisations,
academia, and supply chains.

Plan for the adoption of technologies with modern
defensible architecture

In February 2025, ASD’s ACSC published the Foundations for modern defensible architecture (the Foundations).
Modern defensible architecture (MDA) aims to assist organisations to prepare and plan for the adoption of
technologies based on:

1.

2.

zero trust principles of ‘never trust, always verify’, ‘assume breach’ and ‘verify explicitly’, implemented
through zero trust architecture

secure-by-design practices to institute a security mindset within organisations when it comes to
procuring or developing software products and services.

The Foundations provide a framework for secure design and architecture activities that will best prepare
organisations to adapt to current and emerging cyber threats and challenges. Each foundation represents
an organisational goal or capability that will promote a more efficient adoption of zero trust technologies.

The Foundations offer additional secure design and architecture advice as a structural framework upon which
to implement ASD’s ACSC’s Information Security Manual (ISM) and ASD’s ACSC’s Essential Eight Maturity Model.

Further information on the Foundations can be found on cyber.gov.au.

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Resilience    //

44

Implement the Essential Eight

ASD’s ACSC prioritised mitigation strategies – the Strategies to Mitigate Cyber Security Incidents – help
organisations protect their enterprise IT networks against various cyber threats. The most effective of these
mitigation strategies are the Essential Eight.

■ patch applications
■ patch operating systems
■ multi-factor authentication
■ restrict administrative privileges

■ application control
■ restrict Microsoft Office macros
■ user application hardening
■ regular backups.

Organisations are strongly encouraged to adopt the latest version of the Essential Eight Maturity Model to
protect themselves against contemporary tradecraft used by malicious cyber actors.

Further information on the Essential Eight Maturity Model and its implementation is available in the Essential
Eight Maturity Model FAQ publication on cyber.gov.au.

Apply the Information Security Manual

ASD’s ACSC’s ISM is a cyber security framework that an organisation can use to protect their systems and
data from cyber threats. The ISM is intended for chief information security officers, chief information officers,
cyber security professionals and IT managers.

The ISM is updated regularly; the latest version was released in June 2025. A map between the Essential Eight
Maturity Model and the ISM is provided within the Essential Eight Maturity Model and ISM Mapping publication.

The ISM and guidance on how to implement the ISM can be found on cyber.gov.au.

Protect critical infrastructure networks with CI Fortify

To confront the threat of state-sponsored cyber actors targeting CI, ASD’s ACSC released CI Fortify, the first
in a new series of guidance, with 2 immediate priorities for CI operators:

■ the ability to isolate vital OT and enabling systems from other networks and systems for 3 months
■ the ability to completely rebuild vital OT and enabling systems.

CI Fortify reflects ASD’s ACSC’s proactive approach to defending Australia’s most vital critical services. The
guidance helps CI operators reduce attack surfaces and maintain critical service continuity, even during
sustained cyber security incidents.

For more information, visit cyber.gov.au.

45

Report cyber security incidents to ASD’s ACSC

Australian organisations that have been, or may have been, impacted by a cyber security incident are
encouraged to reach out to ASD’s ACSC, which is the Australian Government’s technical authority on cyber
security. ASD’s ACSC offers free technical incident response advice and assistance, 24 hours a day, 7 days a week.

We also recommend responding to ASD’s ACSC when we reach out to you regarding a vulnerability,
potential compromise or a confirmed compromise, that could impact your organisation. If you are
concerned about the legitimacy of a call, you can verify that you were speaking to a genuine ASD’s ACSC
representative by calling 1300 CYBER1 (1300 292 371) and quoting your incident/reference number.

Report a cybercrime or cyber
security incident

Report at cyber.gov.au/report or call the 24/7
Australian Cyber Security Hotline on
1300 CYBER1 (1300 292 371).

Cybercrime reports are automatically
referred to the relevant state or territory law
enforcement agency.

Cyber security incidents

An incident does not have to be a confirmed
compromise to be reported, and could include:

■ DoS
■ scanning and reconnaissance
■ unauthorised access to a network or device
■ data exposure, theft or leak
■ malicious code/malware
■ ransomware
■ a vulnerability
■ phishing/spearphishing
■ any other irregular cyber activity that

causes concern.

How ASD’s ACSC can help

When you report, ASD’s ACSC will provide
immediate incident response advice and
assistance, which may include:

■ providing information on how to contain and

remediate the cyber security incident

■ providing advisory products to assist you with

your incident response

■ linking you to Australian government

organisations that may further support
your response

■ triaging the incident to determine if there are
more detailed actions to be undertaken.

If ASD’s ACSC assesses that the incident requires
a more tailored approach, depending on the
incident, we may offer:

■ a team of digital forensics specialists to support
a comprehensive technical investigation

■ guidance on approaching public

communications to ensure transparency
while protecting the integrity of the technical
investigation

■ information and reports to help you finalise

your investigation

■ an introduction to different areas within ASD’s
ACSC for additional support, such as cyber
resilience uplift activities and, if requested,
help you to contact the Department of Home
Affairs or the AFP.

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Resilience    //

46

How your reporting matters

Limited use

ASD’s ACSC uses anonymised information from
your report to build our understanding of the
cyber threat environment. This understanding
assists with the development of new and updated
advice, capabilities, techniques and products
to better prevent and respond to evolving cyber
threats. Reporting an incident could be the key to
preventing further victims.

Your confidentiality is paramount

ASD’s ACSC is not a regulator and does not share
information provided by you without your express
consent. We are legally bound to only use your
information for cyber security purposes to assist
you and protect the Australian community. Your
confidentiality is further protected under ASD’s
ACSC’s ‘limited use’ obligation.

To bolster a freer flow of information sharing
between industry and ASD’s ACSC, on 25 November
2024, the Australian Government passed the
Intelligence Services and Other Legislation Amendment
(Cyber Security) Act 2024. The amendment legislates
a ‘limited use’ obligation for ASD’s ACSC. This means
any information that an Australian organisation
voluntarily provides to ASD’s ACSC about a cyber
security incident or potential cyber security incident
(including vulnerability information) cannot be used
for regulatory purposes.

The limited use obligation does not change ASD’s
ACSC’s ability to provide confidential technical
guidance, advice and assistance. What it does is
give industry assurance that information reported
to ASD’s ACSC cannot be admitted as evidence in
criminal or civil proceedings against them.

47

ASD programs

■ ASD’s ACSC provides trusted advice and expertise to government, business and the

community, drawing on our deep technical understanding of communications technology to
help Australians understand the cyber threat environment and what they can do to protect
themselves. When serious cyber incidents occur, ASD’s ACSC leads the Australian Government’s
response to help mitigate the threat and strengthen defences.

■ ASD’s ACSC does not and cannot operate effectively on its own. To protect the nation, ASD’s
ACSC works with federal and state governments, international counterparts, and industry
partners to identify and disrupt malicious cyber threats.

■ Partnerships underpin ASD’s ACSC’s ability to track, detect and mitigate cyber threats and

uplift networks that are less prepared. This uplift includes enabling others to defend their own
networks, informed by our unique threat insights and partnerships.

Proactive notifications to potential victims

ASD’s ACSC uses its unique intelligence insights, international partnerships and industry engagements to
identify and share cyber security threats and vulnerabilities to protect Australian organisations.

ASD’s ACSC engages with entities when it becomes alerted to a potential vulnerability or an incident that
may be affecting an organisation and is often severe in nature. In FY2024–25, ASD’s ACSC made more than
1700 notifications to entities of potentially malicious cyber activity, an increase of 83% from FY2023–24.

More than 12% of ASD’s ACSC’s proactive engagements were confirmed as incidents where some sort
of network compromise had occurred. Nearly half (46%) of those incidents were associated with either
malware or ransomware, and a further 12% were the result of an observed data breach.

Extensive
compromise 8

Isolated
compromise

75

Coordinated low-level
malicious attack

0

Low-level
malicious attack

108

Unsuccessful low-level
malicious attack

19

Figure 14: Proactive engagements by ASD’s ACSC by severity of incident

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Resilience    //

48

Partnership and collaboration with ASD’s ACSC

ASD’s ACSC works closely with government and private enterprise to identify and disrupt malicious cyber
activity and helps entities improve their cyber defences through a range of programs.

In FY2024–25 ASD’s Cyber Security Partnership Program grew to over 133,000 partners. ASD’s ACSC briefed
board and executive leadership team representatives from 41% of the ASX100.

ASD’s Cyber Security Partnership Program is a national program delivered through ASD’s State Offices,
located around Australia. It enables eligible Australian organisations to engage with ASD and industry and
government partners, drawing on collective understanding, experiences, skills and capabilities to enhance
understanding of the cyber threat and uplift cyber resilience across the Australian economy.

The National Exercise Program (NEP) helps CI and government organisations validate and strengthen
Australia’s nationwide cyber security arrangements. The program uses exercises and other readiness
activities that target strategic decision-making as well as operational and technical capabilities.

Highlight 9: 2024 ASD’s ACSC Cyber Drill for ASD’s ACSC network partners

In 2024, the NEP delivered the inaugural ASD’s ACSC Cyber Drill. This provided an opportunity for ASD’s ACSC
network partner cyber defence teams to gain valuable hands-on experience detecting and responding to
cyber incidents, simulating the TTPs of real-world malicious cyber actors. The ASD’s ACSC Cyber Drill was
run via a cyber range for technical teams from across key CI sectors and included:

■ 25 teams competing in up to 3 knockout rounds
■ teams completing a Live Fire Exercise (LFE) each round
■ LFEs covering 52 different MITRE ATT&CK techniques
■ teams progressing to the next round based on their LFE scores and completion times.

The ASD’s ACSC Cyber Drill exercised the technical capabilities of ASD’s ACSC network partners, enhancing
their ability to detect and respond to malicious cyber activity at speed. The team-based approach to the
ASD’s ACSC Cyber Drill promoted collaboration and capability enhancement, and enabled cyber security
teams to rehearse and improve their responses to cyber incidents while using a virtual environment
designed to mirror a corporate network, complete with a range of common industry security tools.

Cyber threats are constantly evolving, and so must our readiness. Mastercard
welcomes exercises involving government and private sector partnership,
collaboration and sharing of best practices.

The ASD Cyber Drill is a prime example of this and is critical to ensuring we’re
prepared to respond swiftly and effectively as a nation. They allow Australia
to test its defences, strengthen our cyber security ecosystem coordination, and
reinforce our commitment to protecting Australians from malicious cyber
activity in both the public and private sectors.

– Mastercard

49

The Government Uplift Program assists prioritised government entities to strengthen their cyber
defences through a range of targeted activities. It delivers hands-on technical assessments of an entity’s
environments and systems to determine the effectiveness of both prevention and detection security controls
as well as also uplift Essential Eight maturity.

Explainer 2: Microsoft-ASD E5 Uplift Program

The Microsoft-ASD Cyber Shield (MACS) partnership is an example of the importance of collaboration
between the public and private sectors in countering the cyber threats we collectively face. One of the
projects delivered under MACS in the reporting period was the Microsoft 365 E5 Uplift pilot project. ASD’s
operational experience had found that many federal government organisations subscribed to an E5 licence,
but either did not use or had not optimised existing security products within the licence. Between October
2024 and March 2025, ASD partnered with Microsoft to uplift Microsoft Defender for Identity and Microsoft
Defender for Endpoint products and configurations for seven government organisations.

Through this project, ASD was able to increase visibility of over 38,000 accounts and enable the identification
of 35 previously unidentified vulnerabilities. Additionally, four workshops with over 300 participants across
33 government organisations were delivered to share technical expertise. Learnings from the collaboration
have now also been included in ASD’s Secure Blueprint for Cloud, which is available at blueprint.asd.gov.au.

Privileged User Training (PUT) offers government and CI privileged users an overview of the best practices
in cyber security. Attendees acquire practical knowledge on hacker tools and techniques, learn to manage
cyber security risk within an enterprise setting, and explore approaches to cultivating a positive security
culture. Most importantly, the course delves deeply into how privileged users can implement tactics to
reduce the occurrence of cyber security incidents in their daily work. At the end of FY2024–25, PUT had been
delivered to approximately 7,500 participants across 460 entities.

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Resilience    //

50

The Critical Infrastructure Uplift Program (CI-UP) assists Australian CI organisations to improve
their resilience against cyber attacks, with a focus on hardening against attack pathways to critical
infrastructure assets and OT environments. A voluntary, nationwide threat-driven program, CI-UP focuses
on improving CI’s cyber security in a range of areas, including:

■ enhancing visibility of malicious cyber activity and awareness of vulnerabilities
■ enhancing the ability to contain and respond to an incident
■ furthering a cyber security culture.

CI-UP leads this work through a series of programs that share uplift and hardening advice and provide
technical assistance. These include:

■ 1:1 Uplift activities – invitation-only activities focused on uplifting the cyber security of CI assets most

important to Australia’s national security

■ Sprint Uplift activities – invitation-only cyber uplift engagements delivering rapid uplift services to a

broad cross-section of Australian CI

 ■ Operational Technology Information Exchanges (OT-IEs) – forums for ASD’s ACSC partners in CI

sectors with OT capability to discuss the cyber threat landscape in OT in a neutral and trusted environment

■ CI-UP presentations, briefings and workshops – providing sector-specific insights and trends across

a range of CI partners.

Threat sharing and threat blocking is a key initiative under the 2023-2030 Australian Cyber Security
Strategy: Shield 3 – World Class Threat Sharing and Blocking. ASD’s ACSC has partnered with the
Department of Home Affairs to align its existing bodies of work on threat sharing and threat blocking, using
ASD’s ACSC’s capabilities to provide the back bone of the Threat Blocking and Threat Sharing Scheme. ASD’s
ACSC leveraged the capabilities of banks and telecommunication providers to block cyber threats at scale,
protecting Australians and Australian infrastructure. ASD’s CTIS has bridged the gap between intelligence
generation and the disruption of malicious infrastructure. Using CTIS, ASD’s collaboration with government
and industry has managed to block hundreds of malicious websites to date, making the internet a safer
place for all Australians.

51

The Cyber Hygiene Improvement Programs (CHIPs) is an open-source intelligence capability that
discovers, identifies and regularly measures the cyber posture and hygiene of internet-facing systems, using
objective and data-driven approaches. The program relies on a mixture of open-source, commercial and
directly collected data.

CHIPs helps to improve cyber hygiene, particularly in the area of attack surface reduction, by providing
entities with regular reports that identify the extent of their internet-facing systems as well as any identified
weaknesses or vulnerabilities in those systems.

CHIPs also responds to critical vulnerabilities and other significant cyber events, providing entities with
timely, actionable intelligence to help them protect themselves in rapidly changing situations.

Case study 2: CHIPs notify a major CI provider of a critical vulnerability

In the final quarter of 2024, an edge device vendor notified ASD’s ACSC of a critical vulnerability in one of
their products, which had been observed undergoing limited exploitation globally. The vendor requested
assistance in reaching Australian operators of those devices.

Through the CHIPs program, ASD’s ACSC identified hundreds of entities using the vulnerable device on
the Australian internet and notified them about the vulnerability so that they could take action to secure
their installations.

One entity, a major CI provider, advised ASD’s ACSC that they had patched their system based on the alert
received and had then observed malicious cyber actors unsuccessfully attempting to exploit their system
within 48 hours.

Reducing the overall internet-facing attack surface, and patching internet-facing systems quickly when
critical vulnerabilities emerge, remain key strategies for preventing malicious cyber intrusion.

Australian Signals DirectorateAnnual Cyber Threat Report 2024–25Resilience    //

52

Notes

Sources

ASD’s ACSC manages or uses several unique datasets to produce tailored advice and assistance for Australian
organisations and individuals. Not all cybercrimes lead to cyber security incidents, and the statistics in this
report are from 2 distinct datasets: cybercrimes reported to law enforcement through ReportCyber,
and cyber security incidents responded to by ASD’s ACSC. Data has been extracted from live datasets of
cybercrime and cyber security reports disclosed to ASD’s ACSC. The self-reported ReportCyber statistics
used throughout this Annual Cyber Threat Report serves as a guide to indicate cyber threats that
individuals and organisations are currently experiencing. As such, the statistics and conclusions in this
report are based on point-in-time analysis and assessment. Cybercrime and cyber security incidents
reported to ASD’s ACSC will not reflect all cyber threats and trends in Australia’s cyber security environment.

ASD’s ACSC encourages the reporting of cybercrimes, cyber security incidents and vulnerabilities to inform ASD’s
ACSC advice and assistance and enhance situational awareness of the national cyber threat environment.

Glossary

ASD’s glossary provides definitions for terms used in this report and other ASD publications: see
https://www.cyber.gov.au/learn-basics/view-resources/glossary.