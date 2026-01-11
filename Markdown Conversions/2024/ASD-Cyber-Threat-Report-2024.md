# Annual Cyber Threat Report 2023–2024

## Table of Contents
- [Imprint](#imprint)
- [Foreword](#foreword)
- [Contents](#contents)
- [About ASD’s ACSC](#about-asds-acsc)
- [About the contributors](#about-the-contributors)
- [Executive summary](#executive-summary)
- [Year in review](#year-in-review)
- [Chapter 1: State actors](#chapter-1-state-actors)
- [Chapter 2: Critical infrastructure](#chapter-2-critical-infrastructure)
- [Chapter 3: Cybercrime](#chapter-3-cybercrime)
- [Chapter 4: Hacktivism](#chapter-4-hacktivism)
- [Chapter 5: Resilience](#chapter-5-resilience)
- [Chapter 6: ASD programs](#chapter-6-asd-programs)
- [Notes](#notes)

---

## Imprint

Website
www.cyber.gov.au

Contact us
ASD welcomes feedback to improve the services it provides to Australians.
Feedback can be provided by emailing asd.assist@defence.gov.au. Alternatively,
a feedback form can be found at: https://www.cyber.gov.au/about-us/about-acsc/contact-us.

Copyright
© Commonwealth of Australia 2024

With the exception of the Coat of Arms, the entity’s logo, third party content and where otherwise
stated, all material presented in this publication is provided under a Creative Commons Attribution
3.0 Australian Licence. To the extent that copyright subsists in a third party, permission will be
required by a third party to reuse the material.

Creative Commons Attribution 3.0 Australia Licence is a standard form licence agreement that allows
you to copy, distribute, transmit and adapt this publication provided that you attribute the work.

The details of the relevant licence conditions are available on the Creative Commons website, as is
the full Creative Commons legal code.

The Commonwealth’s preference is that you attribute this publication (and any material sourced
from it) using the following wording: © Commonwealth of Australia 2024, Australian Signals
Directorate, 2023–24 Annual Cyber Threat Report.

Use of the Coat of Arms
The terms under which the Coat of Arms can be used are detailed at:
www.pmc.gov.au/government/commonwealth-coat-arms

Acknowledgement of Country
We acknowledge the Traditional Owners and Custodians of Country throughout Australia and their
continuing connections to land, sea and communities. We pay our respects to them, their cultures
and their Elders, past and present. We also recognise Australia’s First Peoples’ enduring contribution
to Australia’s national security.

---

## Foreword

I am pleased to present the 2023–24 Annual Cyber Threat Report.

This year’s report comes amid a continued deterioration in Australia’s strategic environment. The
Indo-Pacific continues to face entrenched strategic competition, Russia’s invasion of Ukraine has entered its
third year and conflict continues to unfold in the Middle East.

As the 2024 National Defence Strategy outlined, these challenges are being compounded by rapid
technological advancements. Malign actors – both state and non-state – are improving their cyber
capabilities, increasing the risk of disruptions to Australia’s critical systems, infrastructure and networks.
Grey-zone activities have also expanded in the Indo-Pacific, with malicious cyber actors continuing to
conduct espionage and spread disinformation.

This year’s report outlines the cyber threat posed to Australian governments, critical infrastructure,
businesses and households. It shows how malicious state actors and cybercriminals are continuing to
adapt their tradecraft in an attempt to compromise Australian networks.

These circumstances underline the significant role that cyber capabilities play in safeguarding our national
security and the critical role ASD continues to play in protecting Australians. That is why the Albanese
Government has committed $15–$20 billion to 2033–34 to enhance our cyber domain capabilities as part of
the 2024 Integrated Investment Program.

This significant investment will provide greater visibility of threats to critical infrastructure, increase the
resilience of our infrastructure to cyber attacks, provide new intelligence functions and enable offensive
cyber operations. The Government has also prioritised REDSPICE funding to enhance ASD’s signals
intelligence and cyber capabilities.

This report highlights the importance of strong partnerships between the public and private sectors in
defending Australians from cyber threats and making our country a harder target. It also reflects the
concrete steps we are taking to deter cybercriminals and hold them to account, with the Government
having used for the first time Australia’s autonomous cyber sanctions framework to impose cyber sanctions
on Russian cybercriminals.

Informed by ASD’s intelligence insights and partnerships, this report reinforces the importance of enhancing
our nation’s cyber defences and the need for all Australians to play their part in protecting our collective
cyber security. Reporting cybercrime, incidents and vulnerabilities remains a critical part of building a
national threat picture and enabling us to effectively counter malicious cyber actors.

This report is a key part of the Government’s efforts to raise the profile of Australia’s cyber threats to ensure
we can respond effectively to keep Australians safe.

The Hon Richard Marles MP

Deputy Prime Minister and Minister for Defence

---

## Contents

About ASD’s ACSC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii

About the contributors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii

Executive summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1

Year in review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

State actors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

13

Critical infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

19

Cybercrime . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

Hacktivism. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

Resilience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47

ASD programs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

---

## About ASD’s ACSC

The Australian Signals Directorate’s Australian Cyber Security Centre (ASD’s ACSC) is the Australian
Government’s technical authority on cyber security. Through the ACSC, ASD brings together capabilities to
improve Australia’s national cyber resilience. Its services include:

*   providing the Australian Cyber Security Hotline, which is contactable 24 hours a day, 7 days a week,
    via 1300 CYBER1 (1300 292 371)
*   providing technical advice and publishing alerts, advisories and notifications on significant cyber
    security threats
*   monitoring cyber threats and sharing intelligence with partners, including through the Cyber Threat
    Intelligence Sharing platform (CTIS)
*   helping Australian organisations respond to cyber security incidents
*   providing exercises and uplift activities designed to enhance the cyber security resilience of
    Australian organisations
*   supporting collaboration between over 119,300 Australian organisations and individuals on cyber
    security issues through ASD’s Cyber Security Partnership Program.

Collaboration and partnerships are key to effective cyber security. ASD thanks all of the organisations that
contributed to this report, including federal, state and territory government agencies, industry partners, and
all who reported cyber security matters to ASD.

---

## About the contributors

Australian Federal Police

The Australian Federal Police (AFP) is
responsible for enforcing Commonwealth
criminal law; contributing to combatting
complex transnational, serious, and organised
crime that impacts Australia’s national
security; and protecting Commonwealth
interests from criminal activity in Australia
and overseas. Operation Aquila leverages
the complementary powers, capabilities
and intelligence of ASD and the AFP to
disrupt the most serious cybercrime threats
facing Australia. The AFP-led Joint Policing
Cybercrime Coordination Centre (JPC3) brings
together Australian law enforcement and key
industry and international partners to fight
high-volume, high-harm cybercrime and
prevent harm and financial loss to the
Australian community.

Australian Institute
of Criminology

The Australian Institute of Criminology
(AIC) is Australia’s national research and
knowledge centre on crime and justice. The
AIC informs crime and justice policy and
practice in Australia by undertaking, funding
and disseminating policy-relevant research of
national significance.

Australian Security
Intelligence Organisation

The Australian Security Intelligence
Organisation (ASIO) is Australia’s security
intelligence service. It protects Australia and
Australians from threats to their security,
including terrorism, espionage, sabotage, and
interference in Australia’s affairs by foreign
governments. ASIO’s cyber program is focused
on investigating and assessing the threat to
Australia from malicious state-sponsored
cyber activity. ASIO’s contribution to ASD
includes intelligence collection, investigations
and intelligence-led outreach to business and
government partners.

Australian Signals DirectorateAnnual Cyber Threat Report 2023–24

Department of Foreign
Affairs and Trade

The Department of Foreign Affairs and Trade
(DFAT) promotes and protects Australia’s
international interests to support our security
and prosperity. DFAT leads Australia’s
international engagement on cyber and
critical technology across the Australian
government. This work is coordinated by
Australia’s Ambassador for Cyber Affairs and
Critical Technology. DFAT is leading on the
international elements of the 2023-2030 Cyber
Security Strategy, the development of which
is being coordinated by the Department of
Home Affairs.

Department of Home
Affairs

National Cyber Security
Coordinator

The Department of Home Affairs is responsible
for central coordination, strategy and policy
leadership of cyber and critical infrastructure
resilience and security, immigration, border
security, national security and resilience,
counter-terrorism, and citizenship. The
Department of Home Affairs leads the
development of cyber security policy,
including the implementation of the
2023–2030 Australian Cyber Security Strategy.

The National Cyber Security Coordinator,
supported by the National Office of Cyber
Security (NOCS), leads the coordination of
national cyber security policy, responses to
major cyber incidents, whole-of-government
cyber incident preparedness efforts and
the strengthening of Commonwealth cyber
security capability. The Coordinator also
oversees the implementation of the 2023–2030
Australian Cyber Security Strategy.

Defence Intelligence
Organisation

The Defence Intelligence Organisation
co-leads the Cyber Threat Assessment
team in partnership with ASD to provide
the Australian Government with an
all-source strategic, cyber threat intelligence
assessment capability.

Office of the
Australian Information
Commissioner

The Office of the Australian Information
Commissioner (OAIC) regulates the
compliance of Australian government
agencies, organisations with an annual
turnover of more than $3 million and the
compliance of some other organisations
with the Privacy Act 1988 and other laws when
handling personal information.

Australian Competition
and Consumer
Commission

The National Anti-Scam Centre, run by
the ACCC, brings together experts from
government, law enforcement and the
private sector to disrupt scams before they
reach consumers. The National AntiScam
Centre is collectively committed to making
Australia a harder target for scammers
and reducing the financial and emotional
harm caused by scams. The Centre does
this through collaboration (technology and
intelligence sharing), disruption, awareness
and protection.

Reserve Bank of Australia

The Reserve Bank of Australia is Australia’s
central bank. Its duty is to serve the Australian
people and contribute to their economic
prosperity and welfare through sustainment
of full employment and maintenance of price
stability. It issues the nation’s banknotes and
operates the core of the payments system.

---

## Executive summary

Australia faces the most complex and challenging strategic environment since the Second World War. These
strategic challenges extend to the cyber threat landscape. While advancements in critical and emerging
technologies offer significant social and economic benefits, they also improve the capabilities of malicious
cyber actors who continue to target Australia’s networks.

In FY2023–24, ASD received over 36,700 calls to its Australian Cyber Security Hotline, an increase of 12%
from the previous financial year. ASD also responded to over 1,100 cyber security incidents, highlighting the
continued exploitation of Australian systems and ongoing threat to our critical networks.

State-sponsored cyber actors persistently target Australian governments, critical infrastructure and
businesses using evolving tradecraft. These actors conduct cyber operations in pursuit of state goals,
including for espionage, in exerting malign influence, interference and coercion, and in seeking to pre-position
on networks for disruptive cyber attacks.

Over the past year, ASD co-sealed several joint advisories with international partners to highlight the
evolving operations of state-sponsored cyber actors. In February 2024, ASD joined the US and other
international partners in releasing an advisory that assessed the People’s Republic of China (PRC) is
leveraging living off the land techniques that abuse native tools and processes on systems. The PRC’s choice
of targets and pattern of behaviour is consistent with pre-positioning for disruptive effects rather than
traditional cyber espionage operations.

Russia is also adapting its techniques, including for the exploitation of cloud platforms. The evolution of
this tradecraft means that network defenders must prioritise and invest in cyber security skills, resources
and teams.

Critical infrastructure networks are an attractive target due to the sensitive data they hold and the
widespread disruption that a cyber security incident can cause on those networks. In FY2023–24, over 11% of
cyber security incidents ASD responded to related to critical infrastructure. Compromise could lead to the
disruption of critical services, affecting the economy and lives of everyday Australians.

Cybercrime is a persistent and disruptive threat. Cybercriminals are adapting to capitalise on new
opportunities, such as artificial intelligence, which reduces the level of sophistication needed for cybercriminals
to operate. In FY2023–24, business email compromise and fraud were among the top self-reported
cybercrimes for businesses and individuals in Australia. Ransomware and data theft extortion also remained a
pervasive and costly threat.

In response to this threat, ASD has worked across government, with industry and international partners
to successfully pursue cybercriminals targeting Australia. During FY2023–24, the Australian Government
for the first time used Australia’s autonomous cyber sanctions framework to sanction two Russian
citizens for their roles in cybercrime activities. These sanctions are a key tool in deterring cybercrime and
protecting Australians.

Strong partnerships are critical to building cyber resilience and making Australia a harder target. ASD
continues to monitor and adapt to the threat environment, and collaborates on a national scale to protect
Australians. An increasing number of industry and government partners are choosing to participate in
ASD programs, which provide a platform to share threat intelligence and expertise. This includes the ASD-
Microsoft initiative to connect ASD’s Cyber Threat Intelligence Sharing platform with Microsoft’s Sentinel
platform. These types of collaborations are improving the speed and scale of information-sharing between
and among government agencies and industry partners.

In FY2023–24, ASD notified entities more than 930 times of potential malicious activity on their networks. A
robust partnership between government and industry underpins our ability to effectively defend the nation
against malicious cyber activity.

Cyber security is not set-and-forget. Organisations should consider replacing unsupported information and
communications technology (ICT) systems with secure-by-design products, consider cyber security when
implementing new technologies and follow ASD’s best-practice cyber security advice, such as the Essential
Eight. Regularly updating and applying ICT best practice builds resilience now and into the future.

Be ready to respond. Critical infrastructure organisations should adopt a stance of ‘when’ not ‘if’ a cyber
security incident will occur. All organisations should have a cyber security incident response plan and test it
regularly to ensure an effective response and fast recovery. To develop and implement a response plan, an
organisation needs to know its systems and where its most valuable data is stored.

ASD encourages every organisation and individual who observes suspicious cyber activity, incidents and
vulnerabilities to report to ReportCyber at cyber.gov.au, and to the Australian Cyber Security Hotline 1300
CYBER1 (1300 292 371). ASD provides free technical incident response advice and assistance, 24 hours a day,
7 days a week.

---

## Year in review

### What ASD saw

*   Answered over 36,700 calls to the Australian Cyber Security Hotline, up 12%
    *   on average, 100 calls per day, an increase from 90 calls per day
*   Received over 87,400 cybercrime reports, down 7%
    *   on average a report every 6 minutes, consistent with last year
*   Average self-reported cost of cybercrime per report for individuals, up 17% ($30,700)
*   Average self-reported cost of cybercrime per report for businesses, down 8% overall
    *   small business: $49,600 (up 8%)
    *   medium business: $62,800 (down 35%)
    *   large business: $63,600 (down 11%)

### What ASD did

*   Responded to over 1,100 cyber security incidents, similar to last year
*   Notified entities 930 times of potential malicious cyber activity
*   Australian Protective Domain Name System blocked customer access to 82 million malicious domains, up 21%
*   Domain Takedown Service has requested the removal of over 189,000 malicious domains targeting Australian servers, up 49%
*   Cyber Threat Intelligence Sharing partners grew by 66% to over 400 partners
    *   shared over 1,372,400 indicators of compromise
*   Cyber Hygiene Improvement Program
    *   performed 365 high-priority operational taskings, up 250%
    *   distributed around 6,400 reports to approximately 2,000 organisations, up 32% and 48% respectively
*   Cyber Uplift Remediation Program
    *   24 active engagements
    *   17 engagements commenced
*   Cyber Maturity Measurement Program
    *   16 active engagements
*   Critical Infrastructure Uplift Program
    *   10 uplifts completed covering 15 CI assets
    *   5 uplifts in progress
    *   17 uplift information packs sent
    *   42 uplift workshops held
*   Notified critical infrastructure organisations over 90 times of potential malicious cyber activity
*   Published or updated 29 PROTECT publications, updated the Information Security Manual quarterly, and updated the Essential Eight Maturity Model
*   Published 19 joint advisories and publications with international partners to cyber.gov.au
*   Published 118 alerts, advisories, incident and insight reports on cyber.gov.au and the Partnership Portal
*   ASD’s Cyber Security Partnership Program grew to around 119,300 partners
*   Led 16 cyber security exercises involving over 130 organisations to strengthen Australia’s cyber resilience
*   Briefed board members and company directors covering 37% of the ASX200

---

## Chapter 1: State actors

*   The threat of state-sponsored cyber operations is persistent and will likely grow as strategic
    competition in the Indo-Pacific increases.
*   State-sponsored cyber actors will continue targeting Australian governments, critical infrastructure,
    and businesses, as well as connected systems and their supply chains, for espionage and
    information-gathering purposes. These actors will continue to adapt their techniques, using both
    publicly available and bespoke tools to achieve their objectives.
*   In February 2024, ASD joined other Five Eyes partners in a US-led advisory, which assessed that the
    People’s Republic of China state-sponsored cyber actors are seeking to pre-position themselves
    on information and communications technology networks for disruptive cyber attacks against
    US critical infrastructure in the event of a major crisis or conflict. Australian critical infrastructure
    networks could be vulnerable to similar state-sponsored malicious cyber activity as seen in the US.
*   ASD’s Cyber Security Partnership Program and the Cyber Threat Intelligence Sharing platform
    support Australian organisations to combat state-based cyber threats.

### Global state-sponsored cyber activity
increases as tensions rise

Australia continues to face a complex set of strategic circumstances. Multiple ongoing conflicts are
fueling international instability and increasing strategic competition between the US and China is a
primary feature of our security environment.

Explainer 1: Australia’s strategic environment

The 2024 National Defence Strategy highlights that Australia faces its most complex and challenging
strategic environment since the Second World War. Entrenched and increasing strategic competition is
being accompanied by an unprecedented conventional and non-conventional military build-up in our
region, without strategic reassurance or transparency. Grey-zone activities have also expanded in the
Indo-Pacific and are facilitated by technological developments, including in cyber capabilities. Threats
posed by state and non-state actors in the cyber domain are multiplying.

State-sponsored cyber operations continue to play a significant role in this strategic environment.
State-sponsored cyber actors gather intelligence, exert malign influence, interference and coercion,
and seek to pre-position on critical networks. In the event of a major deterioration in the strategic
environment, Australia could be the target of significant disruptive cyber activities.

### Cyber attacks in modern conflict

Russia’s invasion of Ukraine and the Israel-Hamas conflict both offer contemporary examples of how cyber
operations can support military and strategic objectives in conflict.

Since the beginning of Russia’s invasion of Ukraine, cyber attacks have been used to cause disruptive and
destructive effects to both military and civilian infrastructure, including on telecommunications organisations,
postal and energy systems, and governments. These attacks have resulted in mobile and fixed-line
communications outages and blackouts that have impacted military operations and civilian populations.

Conflict can also give rise to politically-motivated cyber activity. During the Israel–Hamas conflict, patriotic
hacking – a type of politically-motivated cyber activity – has been reported on both sides of the conflict,
with varying degrees of severity. This includes critical infrastructure targeting, digital billboard and website
defacement, and Distributed Denial of Service attacks.

### The threat of state-sponsored cyber
operations in Australia

State-sponsored cyber actors will continue targeting Australian governments, critical infrastructure
and businesses.

Australian networks – particularly those connected to critical infrastructure systems either directly or
through their supply chains – may be targeted in order to pre-position capabilities for disruptive effects, or
may be used to access a higher-value target network.

State-sponsored cyber actors also have information-gathering and espionage objectives in Australia. State
actors have an enduring interest in obtaining sensitive information, intellectual property and personally
identifiable information to gain strategic and tactical advantage. Australian organisations often hold large
quantities of data, so are likely a target for this type of activity.

State-sponsored cyber actors often use previously stolen data, including from previous Australian cyber
security incidents (such as network information and credentials) to further their operations and re-exploit
network devices. While state-sponsored cyber actors’ intentions for the data they collect may differ from
cybercriminals, the way in which they compromise systems and extract data is aligned in their use of similar
techniques and weaknesses in systems.

### Tools and techniques of state-sponsored
cyber actors

State-sponsored cyber actors use various tools and techniques to avoid detection and achieve their
objectives. These tools can be advanced and bespoke. However, they also use common, simple tools and
techniques to prevent the discovery of their best cyber capabilities.

Case study 1: Simple techniques can be effective for state aims

In December 2023, ASD and international partners released an advisory detailing a global spear phishing
campaign conducted by a Russian Federal Security Service (FSB) actor, Star Blizzard. The FSB-sponsored
group targeted a number of sectors – including defence, government, academia, and think tanks – around
the world.

Spear phishing is an effective but simple technique used by many different cyber actors. The advisory
highlights that techniques do not need to be advanced for state actors to achieve their goals.

The advisory, Russian FSB cyber actor Star Blizzard continues worldwide spear phishing campaigns, is available
at cyber.gov.au.

### Supply chain compromises

State-sponsored cyber actors can compromise target networks via their supply chains. The Australian
Government has previously attributed supply chain targeting to state-sponsored cyber actors, including
Russian actors that targeted US software firm SolarWinds.

Cyber supply chain risk management should form a significant component of an organisation’s overall
cyber security strategy. An effective strategy includes consideration of the product or service’s design,
manufacture, delivery, maintenance, decommissioning, and disposal. On 22 May, 2024 ASD released
updated advice on how to manage supply chain risks, available on cyber.gov.au.

### Living off the land techniques

State-sponsored cyber actors use built-in network administration tools to carry out their objectives and
evade detection by blending in with normal system and network activities, enabling them to decide when
to steal information or cause harm to an organisation’s network at a time of their own choosing. This is
known as living off the land (LOTL).

In February 2024, ASD joined the US and other international partners in releasing an advisory, PRC
state-sponsored actors compromise and maintain persistent access to US critical infrastructure. The
US assessed that PRC state-sponsored cyber actors had compromised and maintained access
to US critical infrastructure networks for disruptive cyber attacks in the event of a major crisis or
conflict. US agencies also assessed with high confidence that PRC state-sponsored cyber actor Volt
Typhoon, was pre-positioning itself on information and communications technology (ICT) networks
to enable lateral movement to operational technology (OT) assets to disrupt functions. In the
advisory, ASD assessed Australian critical infrastructure could be vulnerable to similar activity from
these actors.

Also in February 2024, ASD and international partners released an advisory, Identifying and
Mitigating Living Off the Land Techniques, which outlines techniques being deployed by the PRC and
Russia to compromise and maintain access to critical infrastructure systems.

In March 2024, ASD and international partners released a fact sheet, PRC State-Sponsored
Cyber Activity: Actions for Critical Infrastructure Leaders, detailing Volt Typhoon’s activities and
providing defensive actions for critical infrastructure organisations. The fact sheet made several
recommendations, including making informed and proactive resourcing decisions, securing supply
chains, and driving a cyber security culture within organisations.

These advisories and fact sheets highlight the threat posed by malicious cyber actors using LOTL
techniques to avoid detection and, importantly, the ways in which good cyber security can mitigate the
LOTL threat. LOTL tradecraft requires network defenders to think like the malicious cyber actor, by studying
abnormalities in behaviours occurring on systems rather than through traditional means such as intrusion
detection systems. Best Practices for Event Logging and Threat Detection at cyber.gov.au builds on existing
LOTL advice.

### Cloud techniques

As organisations move to cloud-based infrastructure, malicious cyber actors are adapting their techniques
to exploit these systems for espionage. Techniques used to access an organisation’s cloud services include
brute-force attacks and password spraying to access highly privileged service accounts.

In February 2024, ASD and international partners released an advisory detailing the tactics, techniques
and procedures used by a Russian state-sponsored cyber actor to gain access to a cloud environment.
This group is attributed to the Russian Intelligence Services (SVR) – and known as APT29, Midnight Blizzard,
the Dukes, and Cozy Bear. The advisory also outlines the group’s previous activity targeting supply chains,
demonstrating how tactics, techniques and procedures can evolve as technology changes. The advisory,
SVR cyber actors adapt tactics for initial cloud access, is available at cyber.gov.au.

### Collaborating to defend
Australia’s networks

Cyber security collaboration on a national scale is one of Australia’s greatest advantages in building
resilience against malicious cyber activity. Sharing information and expertise between ASD and industry
partners helps to create a collective understanding of this threat and inform new cyber security defences.

The Cyber Threat Intelligence Sharing (CTIS) platform and the ASD’s Cyber Security Partnership Program are
services that empower Australian organisations to defend their networks and to share the malicious cyber
activity they observe. CTIS shares indicators of compromise, bi-directionally at machine speed, within a
growing community of Australian government and industry partners, and alerts security operations centre
analysts to cyber threats. The ASD’s Cyber Security Partnership Program offers opportunities to engage
in cyber defence and resilience programs. Participating in these programs strengthens Australia’s cyber
capabilities to enable intelligence sharing, build the national cyber threat picture and enhance Australia’s
cyber defences.

ASD encourages all organisations that observe suspicious cyber activity, incidents, and vulnerabilities to
report through ReportCyber on cyber.gov.au.

---

## Chapter 2: Critical infrastructure

*   Australian critical infrastructure organisations are regularly targeted by malicious cyber actors
    because they provide critical services, hold sensitive data, and are often connected to other critical
    infrastructure organisations.
*   Many different malicious cyber actors target critical infrastructure systems to fulfil their objectives.
    These include espionage, pre-positioning for disruptive attacks, and for financial gain.
*   Operational technology systems are increasingly interconnected and can have vulnerabilities
    that make them an easier cyber target. Secure information and communications technology and
    operational technology systems are necessary to protect Australia’s critical services.
*   Critical infrastructure organisations should adopt a stance of `when’ not `if’ a cyber security incident
    will occur. Organisations should understand and map their networks, implement an event logging
    system and maintain an asset registry.

### Critical infrastructure in FY2023–24

Critical infrastructure made up 11% of all cyber
security incidents.

The 3 most common activity types leading to critical
infrastructure-related incidents were:
*   phishing (23%)
*   exploitation of a public-facing application (21%)
*   brute-force activity (15%).

The 3 most common cyber security incident types affecting
Australian critical infrastructure organisations were:

*   compromised account or credentials (32%)
*   malware infection (other than ransomware) (17%)
*   compromised asset, network or infrastructure (12%).

Denial of Service and Distributed Denial of Service
were overrepresented in critical infrastructure cyber security
incidents, and present more than twice as often (11%) when
compared to other incidents (5%) responded to by ASD.

The most frequently reported critical infrastructure
sectors were electricity, gas, water and waste services (30%),
education and training (17%) and transport, postal and
warehousing (15%).

### Malicious cyber activity against critical
infrastructure systems is persistent

Critical infrastructure will remain an attractive target for malicious cyber actors because they hold sensitive
data and provide essential services that support Australian society. To deliver these services, critical
infrastructure organisations often rely on complex networks, supply chains and management solutions.
This complexity creates a broad attack surface that malicious cyber actors can exploit.

Operational disruptions to critical infrastructure can be severe and can directly affect the lives of many
Australians. For example, prolonged and widespread failure in the energy sector could result in shortages
or the disruption of essential medical supplies, instability in the supply of food and groceries, and disrupted
telecommunications networks, transport and traffic management systems, and fuel supplies. A compromise
could also lead to data breaches containing personal or commercially sensitive information, which in turn
could be on-sold or used for other malicious purposes.

Over the past year, malicious cyber actors – including state-sponsored cyber actors, cybercriminals, and
hacktivists – have targeted critical infrastructure around the world.

*   State-sponsored cyber actors may target critical infrastructure systems for espionage, or to pre-position
    themselves on networks for future disruptive effects during crises or conflicts.
*   Profit-driven cybercriminals may opportunistically target critical infrastructure organisations for
    financial gain, seeking to extort victims by disrupting critical services or stealing data. Cybercriminals
    will pressure a victim to pay to restore services and minimise the potential consequences of a cyber
    security incident – including reputational and financial damage, and potential legal repercussions.
*   Hacktivists may disrupt critical infrastructure organisations through low-capability attacks, including
    website defacement and DDoS attacks. Cyber security incidents affecting critical infrastructure can be
    high profile – something that may encourage hacktivist activity to elevate their messaging.

Case study 2: Hospital reports unauthorised access to network

In early 2024, a managed service provider (MSP) discovered unauthorised access to a network belonging to
a critical hospital. A hospital employee’s personal device had been used to access a Microsoft Azure Virtual
Desktop (AVD) environment. Additionally, multi-factor authentication (MFA) controls had been bypassed as
the hospital used cached sessions where users were not prompted for MFA for 14 days after a sign-in.

Once in, the malicious cyber actor scanned the network using a non-installer port scanner that did not
require administrative privileges to operate, and was allowed to run because application control was not
in place. However, the actor was unable to escalate their privileges, and an attempt to download a tool to
brute-force passwords was blocked by the proxy server.

The malicious cyber activity triggered an alert in Microsoft Defender, which was investigated by the MSP.
The MSP immediately contacted the user