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
- [Notes](#notes)

---

Website
www.cyber.gov.au

Contact us
ASD’s ACSC welcomes feedback to improve the services it provides to Australians.
Feedback can be provided by emailing asd.assist@defence.gov.au. Alternatively, a feedback form can
be found at: https://www.cyber.gov.au/about-us/about-acsc/contact-us.

Copyright
© Commonwealth of Australia 2025

With the exception of the Coat of Arms, the entity’s logo, third party content and where otherwise
stated, all material presented in this publication is provided under a Creative Commons Attribution
4.0 Australian Licence. To the extent that copyright subsists in a third party, permission will be
required by a third party to reuse the material.

Creative Commons Attribution 4.0 Australian Licence is a standard form licence agreement that allows
you to copy, distribute, transmit and adapt this publication provided that you attribute the work.

The details of the relevant licence conditions are available on the Creative Commons website, as is
the full Creative Commons legal code.

The Commonwealth’s preference is that you attribute this publication (and any material sourced
from it) using the following wording: © Commonwealth of Australia 2025, Australian Signals Directorate’s
Australian Cyber Security Centre, Annual Cyber Threat Report 2024–25.

Use of the Coat of Arms
The terms under which the Coat of Arms can be used are detailed at:
www.pmc.gov.au/government/commonwealth-coat-arms

Acknowledgement of Country
We acknowledge the Traditional Owners and Custodians of Country throughout Australia and their
continuing connections to land, sea and communities. We pay our respects to them, their cultures
and their Elders, past and present. We also recognise Australia’s First Peoples’ enduring contribution
to Australia’s national security.

# Report Content Below

The official report URL is: https://www.asd.gov.au/news/2025-10-14-australian-signals-directorate-releases-annual-cyber-threat-report-2024-25

# Report Content Below

Annual Cyber Threat Report

2024–2025

## Foreword

I am pleased to present the Annual Cyber Threat Report 2024–25.

The world continues to face complex strategic circumstances. Competition and military build-up in the
Indo-Pacific, and ongoing global conflicts are challenging Australia’s security and the global rules that have
endured since World War II. In this uncertain environment, Australia’s relationships with friends and allies are
more critical than ever.

Over the past year, we continued to see state-sponsored cyber actors targeting Australian networks to steal
sensitive information.

Australia joined multi-country advisories warning of the threat of state-sponsored actors targeting
critical infrastructure for the purposes of positioning for potential disruptive attacks. One such advisory
details how People’s Republic of China-affiliated threat actors targeted the networks of major global
telecommunications providers to conduct a broad and significant cyber espionage campaign. Another
details a Russian state-sponsored cyber campaign targeting Western logistics and technology businesses.
I urge Australian businesses to review and apply the ASD and its partners’ technical advice to protect
your networks.

Cybercriminals also relentlessly targeted Australians, with ransomware attacks and data breaches
increasing in frequency. Using malware designed to covertly harvest information from Australian victims,
cyber criminals used stolen data, usernames and passwords to launch subsequent attacks, compromise
corporate networks and accounts.

The Australian Government continues to invest in the nation’s cyber capabilities through project REDSPICE,
which doubles ASD’s size and ability to strike back against malicious cyber activity. In February 2025, the
Australian Government imposed cyber sanctions on a Russian business and its employees for storing
and facilitating the theft of millions of incredibly personal digital records posted by cybercriminals on the
darkest corners of the internet. The sanctions were preceded and enabled by ASD’s targeted offensive cyber
activity which disrupted criminal infrastructure used to host stolen personally identifiable information (PII) of
millions of victims around the world.

This was the first time Australia imposed cyber sanctions on an entity responsible for providing the
infrastructure facilitating cybercrime. It was made possible by ASD’s hard work and delivered in
collaboration with domestic and international industry, intelligence and law-enforcement partners.

This report outlines the cyber threats the nation is facing. All Australians have a role in taking action to
increase Australia’s cyber resilience.

The Hon Richard Marles MP

Deputy Prime Minister and Minister for Defence

## Contents

About ASD’s ACSC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii

About the contributors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii

Executive summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1

Year in review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

Australian cyber threat landscape . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

Who is targeting Australia  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

What malicious cyber actors are targeting  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

Common techniques used by malicious cyber actors  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

Resilience  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

What you can do  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

ASD programs  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47

## About ASD’s ACSC

The Australian Signals Directorate’s Australian Cyber Security Centre (ASD’s ACSC) is the Australian
Government’s technical authority on cyber security. Through the ACSC, ASD brings together capabilities to
improve Australia’s national cyber resilience. Its services include:

*   Providing the Australian Cyber Security Hotline, which is contactable 24 hours a day,
    7 days a week, via 1300 CYBER1 (1300 292 371)
*   Providing technical advice and publishing
    alerts, advisories and notifications on
    significant cyber security threats
*   Monitoring cyber threats and sharing
    intelligence with partners, including through
    the Cyber Threat Intelligence Sharing
    platform (CTIS)
*   Helping Australian organisations respond to
    cyber security incidents
*   Providing exercises and uplift activities
    designed to enhance the cyber security
    resilience of Australian organisations
*   Supporting collaboration between over 133,000
    Australian organisations and individuals on
    cyber security issues through ASD’s Cyber
    Security Partnership Program.

Collaboration and partnerships are key to effective cyber security. ASD’s ACSC thanks all the organisations
that contributed to this report, including federal, state and territory government agencies, industry
partners, and all who reported cyber security matters to ASD’s ACSC.

## About the contributors

**Australian Federal Police**
The Australian Federal Police (AFP) is
responsible for enforcing Commonwealth
criminal law; contributing to combatting
complex transnational, serious, and organised
crime that impacts Australia’s national
security; and protecting Commonwealth
interests from criminal activity in Australia
and overseas. Operation Aquila leverages
the complementary powers, capabilities and
intelligence of ASD’s ACSC and the AFP to
disrupt the most serious cybercrime threats
facing Australia. The AFP-led Joint Policing
Cybercrime Coordination Centre (JPC3) brings
together Australian law enforcement and key
industry and international partners to inflict
maximum impact on high volume, high harm
cybercrime affecting the Australian community.

**Australian Institute
of Criminology**
The Australian Institute of Criminology
(AIC) is Australia’s national research and
knowledge centre on crime and justice. The
AIC informs crime and justice policy and
practice in Australia by undertaking, funding
and disseminating policy-relevant research of
national significance.

**Australian Security
Intelligence Organisation**
The Australian Security Intelligence
Organisation (ASIO) is Australia’s security
intelligence service. It protects Australia and
Australians from threats to their security,
including terrorism, espionage, sabotage,
and interference in Australia’s affairs by
foreign governments. ASIO’s cyber program
is focused on investigating and assessing the
threat to Australia from malicious state-
sponsored cyber activity. ASIO’s contribution
to ASD’s ACSC includes intelligence collection,
investigations and intelligence-led outreach to
business and government partners.

**Australian Signals Directorate**
Annual Cyber Threat Report 2024–25

**Department of Foreign
Affairs and Trade**
The Department of Foreign Affairs and Trade
(DFAT) promotes and protects Australia’s
international interests to support our security
and prosperity. DFAT leads Australia’s
international engagement on cyber and
critical technology across the Australian
Government. This work is coordinated by
Australia’s Ambassador for Cyber Affairs
and Critical Technology. DFAT is leading on
the international elements of the 2023–2030
Australian Cyber Security Strategy, the
development of which is being coordinated
by the Department of Home Affairs.

**Department of Home
Affairs**
The Department of Home Affairs is responsible
for the leadership and central coordination
of policy, programs and regulations relating
to national security and resilience, law
enforcement, migration and citizenship,
multicultural affairs, and border management
and security. The Department of Home Affairs
leads the development of cyber security
policy, including the implementation of the
2023–2030 Australian Cyber Security Strategy.

**National Cyber Security
Coordinator**
The National Cyber Security Coordinator,
supported by the National Office of Cyber
Security (NOCS), leads the coordination of
national cyber security policy, responses to
major cyber incidents, whole-of-government
cyber incident preparedness efforts and
the strengthening of Commonwealth cyber
security capability. The Coordinator also
oversees the implementation of the
2023–2030 Australian Cyber Security Strategy.

**Defence Intelligence
Organisation**
The Defence Intelligence Organisation
co-leads the ACSC’s cyber threat assessment
team in partnership with ASD to provide
the Australian Government with an
all-source strategic, cyber threat intelligence
assessment capability.

**Office of the
Australian Information
Commissioner**
The Office of the Australian Information
Commissioner (OAIC) regulates the
compliance of Australian government
agencies, organisations with an annual
turnover of more than $3 million and the
compliance of some other organisations
with the Privacy Act 1988 and other laws when
handling personal information.

**Australian Competition
and Consumer
Commission**
The National Anti-Scam Centre, run by
the ACCC, brings together experts from
government, law enforcement and the
private sector to disrupt scams before they
reach consumers. The Centre is collectively
committed to making Australia a harder
target for scammers and reducing the
financial and emotional harm caused
by scams. The Centre does this through
collecting quality scam reports through
our Scamwatch service, collaboration
(technology and intelligence sharing),
disruption, awareness and protection.

## Executive summary

Australia is an early and substantial adopter of digital technology which drives public services, productivity
and innovation. Our increasing dependency on digital and internet-connected technology means Australia
remains an attractive target for criminal and state-sponsored cyber actors.

In FY2024–25, ASD’s ACSC received over 42,500 calls to the Australian Cyber Security Hotline, a 16% increase
from the previous year. ASD’s ACSC also responded to over 1,200 cyber security incidents, an 11% increase.
During FY2024–25, ASD’s ACSC notified entities more than 1,700 times of potentially malicious cyber activity –
an 83% increase from last year – highlighting the ongoing need for vigilance and action to mitigate against
persistent threats.

State-sponsored cyber actors continue to pose a serious and growing threat to our nation. They target
networks operated by Australian governments, critical infrastructure (CI) and businesses for state goals.
State-sponsored cyber actors may also seek to use cyber operations to degrade and disrupt Australia’s
critical services and undermine our ability to communicate at a time of strategic advantage.

The threat from cybercrime also continues to challenge Australia’s economic and social prosperity, with
average reported financial losses, the frequency of ransomware attacks and the number of reported data
breaches all increasing throughout FY2024–25. Cybercriminals are continuing their aggressive campaign of
credential theft, purchasing stolen usernames and passwords from the dark web to access personal email,
social media or financial accounts.

Malicious cyber actors are able to leverage vulnerabilities in the technology and security practices of
individuals and businesses throughout the public and private sectors. Internet-facing vulnerabilities in edge
devices are common, and they require network owners to rigorously monitor and configure securely. ‘Living
off the land’ tradecraft has persevered, requiring an adjustment in the way network defenders prioritise
understanding behavioural patterns of networks in order to detect the most sophisticated threats.

The prevalence of artificial intelligence (AI) almost certainly enables malicious cyber actors to execute attacks
on a larger scale and at a faster rate. The potential opportunities open to malicious cyber actors continue
to grow in line with Australia’s increasing uptake of – and reliance on – internet-connected technology.

CI is, and will continue to be, an attractive target for state-sponsored cyber actors, cybercriminals, and
hacktivists, largely due to large sensitive data holdings and the critical services that support Australia’s
economy. ASD’s ACSC notified CI entities of potential malicious cyber activity impacting their networks over
190 times in the last reporting period – up 111% from the previous year.

The threat environment combined with our operational observations set out in this report underscores the
need for all Australian individuals, private and public entities to take action to uplift our cyber resilience at
every level. Every individual can uplift their cyber defences through basic actions. Use strong Multi-Factor
Authentication (MFA) wherever possible, use strong and unique passwords or passphrases, keep software
on devices updated, be alert for phishing messages and scams, and regularly back up important data.
These basics have never been more important, and implementing these mitigations can prevent the
majority of the cyber incidents reported to ASD’s ACSC.

Businesses should operate with a mindset of ‘assume compromise’ and prioritise the assets or ‘crown jewels’
that need the most protection. ASD recommends businesses and network owners focus on 4 ‘big moves’ to
bolster their cyber defences and prepare for future challenges: implement best-practice logging, replace
legacy IT, effectively manage third-party risk and prepare for post-quantum cryptography.

For those businesses also operating operational technology (OT), follow best-practice guidance for isolating
vital OT and enabling systems, and have a plan for how to rebuild.

For large organisations, ensuring technology used or provided to customers is secure-by-design and
secure-by-default is critical for building modern networks that protect data and systems.

The years ahead will bring challenges for organisations in emerging technology, such as post-quantum
cryptography. ASD’s ACSC will continue to work with Australian industry and partner organisations to ensure
the continued security of our communications and sensitive data. Effective transition plans will be critical to
operating in 2030 and beyond – a post-quantum computing world – and this planning must start now.

Businesses must ensure that, in order to harness the full benefits and productivity associated with AI, a safe
and secure approach is taken to the integration of AI technologies.

It remains critically important that organisations and individuals who observe suspicious cyber activity,
incidents and vulnerabilities report to ReportCyber at cyber.gov.au, or to the Australian Cyber Security
Hotline 1300 CYBER1 (1300 292 371).

## Year in review

### What ASD’s ACSC saw

*   Answered over 42,500 calls to the Australian Cyber Security
    Hotline, up 16%
    *   On average, 116 calls per day, an increase from
        100 calls per day
*   Received over 84,700 cybercrime reports to ReportCyber,
    down 3%
    *   On average a report every 6 minutes, consistent with
        last year
*   Average self-reported cost of cybercrime per report for
    individuals, up 8% ($33,000)
*   Average self-reported cost of cybercrime per report for
    businesses, up 50% overall ($80,850)
    *   small business: $56,600 (up 14%)
    *   medium business: $97,200 (up 55%)
    *   large business: $202,700 (up 219%)

### What ASD’s ACSC did

*   Responded to over 1,200 cyber security incidents,
    an 11% increase from last year
*   Notified entities of potential malicious cyber activity
    more than 1,700 times, up 83%
*   Australian Protective Domain Name System
    blocked customer access to 334 million
    malicious domains, up 307%
*   Cyber Threat Intelligence Sharing (CTIS) partners
    grew by 13% to over 450 partners
    *   In late 2024, CTIS transitioned to ASD’s new enhanced
        CTIS platform
    *   To date, CTIS has shared over 2,984,000 indicators
        of compromise
*   Cyber Hygiene Improvement Programs
    *   Performed 478 high-priority operational taskings, up 31%
    *   Distributed around 14,400 reports to approximately
        3,900 organisations, up 125% and 95% respectively
    *   Distributed around 11,000 Notifications of Indicators of
        Compromise to approximately 2,160 organisations
*   Government Uplift Program
    *   26 active Cyber Uplift Remediation Program engagements
        (commenced prior to FY2024–25)
    *   4 Cyber Uplift Remediation Program engagements
        commenced (during the reporting period)
    *   7 active Cyber Maturity Measurement Program engagements
*   Critical Infrastructure Uplift Program
    *   8 CI uplifts completed, covering 38 CI assets
    *   4 CI uplift sprints completed, covering 5 CI assets
        *   With a further 2 CI uplift sprints in progress
    *   7 Tech-To-Tech workshops held
*   Notified critical infrastructure entities of potential malicious
    cyber activity over 190 times, up 111%
*   Published or updated 26 PROTECT publications,
    including guidance publications related to the
    Essential Eight Maturity Model and updates to the
    Information Security Manual
*   Published a combination of 108 alerts, advisories,
    knowledge articles and publications on both
    cyber.gov.au and the Partner Portal
*   ASD’s Cyber Security Partnership Program
    grew by 11% to over 133,000 partners
*   Led 17 cyber security exercises, involving over
    120 organisations, to strengthen Australia’s resilience
*   Briefed board and executive leadership team representatives
    from 41% of the ASX100

### Timeline of Key Events

**July 2024**
*   9 July: jointly published APT40 Advisory: PRC MSS tradecraft in action
*   16 July: updated Hardening Microsoft Windows 10 and Windows 11 workstations advice
*   30 July: published Secure–by–Design Foundations to help technology manufacturers and
    consumers adopt secure-by-design principles

**August 2024**
*   22 August: jointly published Best practices for event logging and threat detection to improve
    the security of critical systems

**September 2024**
*   2 September: released advisory The silent heist: cybercriminals use information stealer malware
    to compromise corporate networks
*   6 September: released joint advisory Russian Military Cyber Actors Target U.S. and Global
    Critical Infrastructure
*   19 September: released joint advisory on People’s Republic of China-Linked Actors Compromise
    Routers and IoT Devices for Botnet Operations
*   26 September: jointly published Detecting and mitigating Active Directory compromises

**October 2024**
*   1 October: Cyber Security Awareness Month 2024
*   2 October: the Australian Government enacted cyber sanctions against prolific
    cybercriminal syndicate members of Evil Corp
*   2 October: published Principles of operational technology cyber security, which was
    co-designed with Australian critical infrastructure operators
*   17 October: released joint advisory Iranian cyber actors’ brute force and credential access
    activity compromises critical infrastructure
*   25 October: jointly published Safe Software Deployment

**November 2024**
*   21 November: published updates to #StopRansomware: BianLian Ransomware Group advisory
*   29 November: Intelligence Services and Other Legislation Amendment (Cyber Security) Act 2024
    became law

**December 2024**
*   4 December: released joint advisory Enhanced visibility and hardening guidance for
    communications infrastructure in response to People’s Republic of China
    (PRC)-affiliated cyber actors’ exploitation of networks of major global
    telecommunication providers

**January 2025**
*   14 January: jointly published Secure by Demand: Priority considerations for operational
    technology owners and operators when selecting digital products
*   22 January: published “Bulletproof” hosting providers: Cracks in the armour of
    cybercriminal infrastructure

**February 2025**
*   5 February: jointly published a series on securing edge devices
*   10 February: published Foundations for modern defensible architecture, which introduces
    modern defensible architecture as an approach for building cyber resilience
*   12 February: the Australian Government enacted further cyber sanctions against Russian cyber
    criminals including Australia’s first sanction against a cyber infrastructure entity

**March 2025**
*   17 March: released an advisory and joint guidance in response to increasing denial-of-service
    (DoS) attacks
*   18 March: released significant updates to ASD’s Blueprint for Secure Cloud (the Blueprint)

**April 2025**
*   4 April: released joint advisory on the ongoing threat of fast flux-enabled malicious
    activities as a defensive gap in many networks
*   9 April: released a joint advisory on 2 spyware variants, BADBAZAAR and MOONSHINE
    targeting Uygur, Taiwanese and Tibetan groups and civil society actors

**May 2025**
*   22 May: released a joint advisory on the Russian targeting of Western logistics entities
    and technology companies
*   23 May: released a joint advisory on best practices for securing data throughout the
    Artificial Intelligence (AI) system life cycle
*   28 May: jointly published a suite of guidance to assist organisations implement Security
    Information and Event Management (SIEM) and Security Orchestration,
    Automation, and Response (SOAR) platforms

**June 2025**
*   5 June: released an updated joint advisory on the Play (‘Playcrypt’) ransomware group’s
    indicators of compromise (IOCs) and tactics, techniques and procedures (TTPs)
*   30 June: published Introduction to Connected Vehicles as a foundational explainer on the
    technology and cyber security vulnerabilities of Connected Vehicles.

### Cyber Security Incidents by Severity Category

ASD’s ACSC categorises each cyber security incident it responds to on a scale of Category 1 (C1), the most
severe, to Category 6 (C6), the least severe. Cyber security incidents are categorised on severity of impact
and significance of the organisation’s impact to Australia.

*   **C1**: Sustained disruption of essential
    systems and associated services
*   **C2**: Extensive compromise
*   **C3**: Isolated compromise
*   **C4**: Coordinated low-level
    malicious attack
*   **C5**: Low-level malicious attack
*   **C6**: Unsuccessful low-level
    malicious attack

![Figure 1: Cyber security incidents by severity category for FY2024–25 (total 1,253)](https://i.imgur.com/your_image_placeholder.png)
*Figure 1: Cyber security incidents by severity category for FY2024–25 (total 1,253)*

Overall, there was an 11% increase in incidents reported to ASD’s ACSC in FY2024–25. Compared to FY2023–24,
there was a notable increase in successful and unsuccessful low-level malicious attacks. While the raw
number of high-end attacks is lower this year, ASD nevertheless continued to see the use of complex and
sophisticated tradecraft.

Incidents categorised as C3 or above involved organisations such as federal and state governments, large
organisations, academia and supply chains. ASD’s ACSC responded to 2 C2 incidents in FY2024–25, up from
one in FY2023–24. C3 incidents in FY2024–25 were less frequent than in FY2023–24, with 8% of all incidents
being categorised C3, down 6%.

Over a third (37%) of all C3 incidents were discovered as a result of ASD’s ACSC proactively notifying
the affected organisation of suspicious activity, an increase of 26%. C3 incidents commonly involved
compromised assets, network or infrastructure (50%), compromised accounts or credentials (42%), and
ransomware (34%). This contrasts with C3 incidents in FY2023–24, where accounts were more frequently
compromised than assets, networks or infrastructure.

Caveat: Incidents can have multiple incident types ascribed to them and hence do not add up to 100%.

ASD’s ACSC responded to over 1,200 cyber security incidents,
an 11% increase from last year.

![Figure 2: Cyber security incidents responded to by month](https://i.imgur.com/your_image_placeholder.png)
*Figure 2: Cyber security incidents responded to by month*

### Reported Top 3 Incident Types

**Top 3 reported cyber security incident types
for critical infrastructure**
*   Compromised Asset/Network/Infrastructure 55%
*   DoS/DDoS 23%
*   Compromised Account/Credentials 19%

**Top 3 reported cyber security incident types
for government (federal, state and local)**
*   Compromised Asset/Network/Infrastructure 37%
*   DoS/DDoS 16%
*   Malware Infection (other than ransomware) 15%

**Top 3 self-reported cybercrime threats for business
(Small, Medium, Large)**
*   Email compromise resulting in no financial loss 19%
*   Business email compromise (BEC) fraud resulting
    in financial loss 15%
*   Identity fraud 11%

**Top 3 self-reported cybercrime threats
for individuals**
*   Identity fraud 30%
*   Online shopping fraud 13%
*   Online banking fraud 10%

Note: Incidents can have multiple incident types.

## Australian cyber threat landscape

### Who is targeting Australia

*   Australia’s economy and geostrategic position make it an attractive target for various malicious
    cyber actors.
*   State-sponsored cyber actors are a persistent threat. They target a range of sectors to conduct
    espionage against both individuals and organisations, and to generate opportunities to disrupt
    critical services and communication at a time of strategic advantage.
*   Cybercriminals target Australia’s economy for financial gain. This can manifest in the theft of
    data or the disruption of services to elicit payment.

#### State-sponsored cyber actors

Over FY2024–25, state-sponsored cyber actors targeted Australian networks, and they continue to present
an active and evolving cyber threat to Australia. State-sponsored cyber actors conduct operations to serve
political and military objectives, including cyber espionage, malign influence, interference and coercion, or
to pre-position for disruptive and destructive cyber effects in the event of crisis or conflict.

State-sponsored cyber actors routinely target Australian government networks for cyber espionage purposes.
Government and defence-related information is an attractive target for state-sponsored cyber actors seeking
strategic insights into Australia’s national policies and decision-making.

However, government networks are not the only source of this information. Many Australian businesses and
other organisations hold large amounts of sensitive and valuable data, such as proprietary information,
research and personal data. State-sponsored cyber actors may use this data to support further targeting
against government and critical infrastructure (CI) organisations, as well as their supply chains.

State-sponsored cyber actors have also compromised home devices connected to the internet, such as home
routers, to create botnets that support further targeting around the globe.

State-sponsored cyber actors continue to use built-in network administration tools to carry out their objectives
and evade detection by blending in with normal system and network activities, enabling them to decide when
to steal information or cause harm to an organisation’s network at a time of their own choosing. This is known
as living off the land (LOTL). LOTL tradecraft requires network defenders to think like the malicious cyber actor,
by studying abnormalities in behaviours occurring on systems rather than through traditional means such as
intrusion detection systems.

State-sponsored cyber actors often use data from previous data breaches or cyber security incidents, such
as network information and valid credentials to further their operations. Cyber espionage actors can also
reuse their covert access to a victim’s network for other purposes. For example, a malicious cyber actor
could start using their access to a target network for disruptive and destructive purposes, if their intent shifts
from espionage to disruption or destruction.

The boundary between state-sponsored and cybercriminal activity continues to be blurred. While
state-sponsored cyber actors’ intentions for the data they collect may differ from cybercriminals, the way
in which they compromise systems and extract data is aligned in that they use similar tools, techniques and
weaknesses in systems. State-sponsored cyber actors will continue to adapt their techniques, using both
publicly available and bespoke tools to achieve their objectives.

#### Highlight 1: People’s Republic of China cyber espionage targeting Australian and
regional networks

In July 2024, ASD’s ACSC released a cyber security advisory detailing the tradecraft of a People’s Republic
of China (PRC) state-sponsored group known as Advanced Persistent Threat (APT) 40. Industry also tracks
this group as Kryptonite Panda, Gingham Typhoon, Leviathan and Bronze Mohawk. ASD’s ACSC and
international partners assess APT40 receives its tasking from the PRC’s Ministry of State Security (MSS) – the
agency responsible for foreign intelligence collection for the PRC.

APT40 regularly conducts malicious activities against Australian and regional networks that possess
information of value to the PRC. These activities represent a security threat to many government and critical
infrastructure networks. Australia and several international partners acted decisively to detail the tradecraft
of APT40 to assist network defenders to detect and prevent their malicious activities.

APT40 is known for its rapid exploitation of security vulnerabilities, often within hours or days of the
publication of proofs of concept. This shows its preferred initial access technique, which favours exploiting
public-facing applications over other traditional methods like phishing. This highlights the defensive value
of implementing relatively simple mitigation strategies, which continue to be effective at preventing actors
like APT40.

ASD’s ACSC and international partners have also observed APT40, alongside other actors, using botnets
made up of compromised Small Office Home Office (SOHO) devices. The use of compromised devices
allows APT40 to blend malicious traffic with the legitimate traffic of the device owner, complicating the
detection and prevention efforts of network defenders.

Once initial access has been achieved, incident investigations have shown APT40 obtains access to
legitimate user credentials to conduct further actions on the victim network, rather than making use of
malware. This can further complicate the efforts of network defenders to detect and defend against the
malicious activity.

APT40’s approach observed over time is an example of state-based actors refining their tradecraft to
continually evade detection and prevention efforts by network defenders.

APT40 Advisory: