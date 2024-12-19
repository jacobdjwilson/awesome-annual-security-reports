# Microsoft Digital Defense Report 2024
## The foundations and new frontiers of cybersecurity
### A Microsoft Threat Intelligence report

---

Microsoft Digital Defense Report 2024
Overview
Overview
About this report
02
Introduction by Tom Burt
03
Our unique vantage point
05
Cybersecurity at Microsoft: the CISO’s perspective
07
1 The evolving cyber threat landscape
Key developments
09
Introduction
10
Threat actors and motivations
11
Nation-state threats
12
Nation-state threat activity by the numbers
12
Blurring lines between nation-state
threat actors and cybercriminals
17
The many faces of hybrid war
18
Deterring the most advanced threats
22
Election interference
24
Ransomware
27
Landscape and trends
27
How cybercriminals are tampering
with security products
28
Octo Tempest: a case study and a cautionary tale
29
Disrupting ransomware threat actors
30
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
1
Fraud
31
Landscape and trends
31
Phishing
34
Impersonation
36
Identity and social engineering
39
Insights on identity attacks and trends
39
Identity attacks in perspective
41
Security to the max: the optimal mindset
for security professionals
42
Social engineering “next generation”
44
Stormy skies: the rise of cloud identity compromise 47
DDoS attacks
50
DDoS: Stealthier threats emerge
50
Attack landscape
50
A new threat: Application loop attacks
50
2 Centering our organizations on security
Key developments
54
Introduction
55
Secure Future Initiative
56
Strategic approaches to cybersecurity:
“Managing your own house”
57
Data security
57
Hierarchy of cybersecurity needs
60
Threat-informed defense
61
Optimizing governance and accountability
63
Security incident decisions:
Dispatches from the field
64
Resilience maturity
66
Supporting the ecosystem
67
The passkey journey: a story
of collaboration across the industry
67
Critical environments
69
Collective action
77
The digital transformation of
defense and a call for partnership
77
How Microsoft helps support democratic elections 79
3 Early insights: AI’s impact on cybersecurity
Key developments
83
Introduction
84
Understanding how generative AI systems work
85
Two key insights
86
Emerging threat landscape
87
The generative AI threat landscape
87
Sophisticated AI-enabled human targeting
89
Emerging techniques in AI-enabled attacks
90
Nation-state threat actors using
AI for influence operations
91
AI for defense
94
Harnessing AI to detect cyberattacks
95
AI’s early impact on the security operations center 96
Seven areas of efficiencies in Microsoft
security operations
97
Using generative AI to understand
cyberattacks and create tailored mitigations
99
How governments and industries
are advancing global AI security
101
Government approaches to AI security
101
Collaborative policy initiatives for AI security
104
International standards for AI security
105
Staying a step ahead of threat actors
in the age of AI
106
Appendix
References
108
Contributing teams
110
Japan
16
Australia
23
Israel
30
Canada
49
India
52
Sweden
59
Latin America
65
France
68
Africa
73
United Kingdom
81
Albania
103
In this report
Cyber Point of View stories

---

Microsoft Digital Defense Report 2024
Overview
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
About this report Introduction
Our unique vantage point
Cybersecurity at Microsoft
2
Overview
About this report
Report scope
The data, insights, and events in this report represent
July 2023 through June 2024 (Microsoft fiscal year
2024), unless otherwise noted.
Please note that due to rounding, the percentages in
some charts may not total 100%.
Relevant discussion from the 2023 edition of the
Microsoft Digital Defense Report is referenced in this
report. You can access the 2023 report in the archive
section at
[aka.ms/MDDR](aka.ms/MDDR).
Report viewing and navigating
There are links in the headers and table of contents
for easy navigation throughout the report.
For easier viewing and navigating through the
report on certain browsers, we suggest using
Adobe Reader, which is available for free on the
Adobe website.
Our commitment to preserving privacy
Any and all data included in this report is presented
in alignment to our privacy principles. Microsoft is
committed to its focus on preserving customers’
control over their data and their ability to make
informed choices that protect their privacy.
We advocate for strong global privacy and data
protection laws requiring companies, including ours,
to only collect and use personal data in responsible,
accountable ways.
Threat actor terminology used in this report
*   Nation-state threat attacks/operations:
    Malicious cyberattacks that originate from a
    particular country and are an attempt to further
    that country’s interests. These attacks are
    often fueled by geopolitical competition and a
    desire to gain an advantage over other nations.
    Common objectives include stealing intellectual
    property for economic benefit or supporting
    traditional espionage.
*   Cybercriminal activity: Cybercriminals are
    typically motivated by financial gain. They may
    use similar tools and tactics as nation-state threat
    actors, such as bespoke malware, password spray
    infrastructure, and phishing or social engineering
    campaigns. However, their primary goal is to
    profit from their activities, rather than to further a
    nation’s geopolitical objectives.
*   Cyber operations: An overarching term referring
    to all computer network operations, from
    computer network defense to computer network
    attacks, and to computer network exploitation.
*   Influence operations (IO): The coordinated,
    integrated, and synchronized application of
    national diplomatic, informational, military,
    economic, and other capabilities in peacetime,
    crisis, conflict, and post conflict to foster attitudes,
    behaviors, or decisions by foreign target audiences
    that further nation-state interests and objectives.
*   Cyber-enabled influence operations:
    Operations which combine offensive computer
    network operations with messaging and
    amplification in a coordinated and manipulative
    fashion to shift perceptions, behaviors, or
    decisions by target audiences to further
    a group or a nation’s interests and objectives.
Key information
Throughout this document look out for features
offering insights and detail from Microsoft experts.
Look out for The text "highlighted text like this" is highlighted. and the
Actionable Insights sections:

**Actionable Insights**

Our commitment to developing
technology responsibly
As we design, build, and release AI products,
six values—transparency, accountability,
fairness, inclusiveness, reliability and safety, and
privacy and security—remain our foundation
and guide our work every day.

Links
[Microsoft Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement)
[Microsoft EU Data Boundary Overview](https://www.microsoft.com/en-us/trust-center/privacy/european-data-boundary)
[Microsoft Trust Center](https://www.microsoft.com/en-us/trust-center)
[Empowering responsible AI practices](https://www.microsoft.com/en-us/ai/responsible-ai)
[Microsoft AI](https://www.microsoft.com/en-us/ai)
[Responsible AI Transparency Report | May 2024](https://www.microsoft.com/en-us/ai/responsible-ai-transparency-report)

---

3
Microsoft Digital Defense Report 2024
Overview
Overview
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
About this report
Our unique vantage point
Cybersecurity at Microsoft
Introduction
Complex, challenging, and increasingly dangerous
The new cyber threat landscape: an introduction by Tom Burt
> “We all can, and must, do better,
> hardening our digital domains to
> protect our networks, data, and
> people at all levels.”

In the last year, the cyber threat landscape continued
to become more dangerous and complex.
The malign actors of the world are becoming
better resourced and better prepared, with
increasingly sophisticated tactics, techniques,
and tools that challenge even the world’s best
cybersecurity defenders.
Because these actors conduct both targeted and
opportunistic attacks, the threat they present is
universal, meaning organizations, users, and devices
are at risk anywhere, anytime. Even Microsoft has
been the victim of well-orchestrated attacks by
determined and well-resourced adversaries, and our
customers face more than 600 million cybercriminal
and nation-state attacks every day, ranging from
ransomware to phishing to identity attacks.
These cyberattacks are continuing at a breathtaking
scale, and as they increasingly put human health
at risk, the stakes for stopping them couldn’t
be higher. In the US alone this fiscal year, 389
healthcare institutions were successfully hit by
ransomware, resulting in network closures, systems
offline, critical medical operations delayed, and
appointments rescheduled. Worse, the increased
risk of cyberattacks is no longer limited to civilian
cybercriminals. Nation-states are becoming more
aggressive in the cyber domain, with ever-growing
levels of technical sophistication that reflect
increased investment in resources and training.
These state-sponsored hackers are not just stealing
data, but launching ransomware, prepositioning
backdoors for future destruction, sabotaging
operations, and conducting influence campaigns.
We have to find a way to stem the tide of this
malicious cyber activity. We all can, and must, do
better, hardening our digital domains to protect
our networks, data, and people at all levels.
This challenge will not be accomplished solely by
executing a well-known checklist of cyber hygiene
measures but through a focus on and commitment
to the foundations of cyber defense from the
individual user level to the executive level.
However, improved defense will not be enough.
The sheer volume of attacks must be reduced
through effective deterrence, and while the industry
must do more to deny the efforts of attackers via
better cybersecurity, this needs to be paired with
government action to impose consequences that
further discourage the most harmful cyberattacks.

---

4
Microsoft Digital Defense Report 2024
Overview
Overview
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
Introduction by Tom Burt continued
About this report
Introduction
Our unique vantage point
Cybersecurity at Microsoft
While in recent years a great deal of attention has
been given to the development of international
norms of conduct in cyberspace, those norms
so far lack meaningful consequence for their
violation, and nation-state attacks have been
undeterred, increasing in volume and aggression.
Cybercriminals similarly continue to attack with
impunity, knowing that law enforcement is
hampered by the challenges of investigation and
prosecution of cross-border crime, and often
operating from within apparent safe havens where
government authorities turn a blind eye to the
malicious activity.
While the immediate outlook is pessimistic, there
are changes on the near horizon that provide cause
for optimism. In this year’s Microsoft Digital Defense
Report, we dive deeper into the subject of AI in
cybersecurity. We explore the associated emerging
threats and defense strategies, as well as examine
the responses of governments around the world to
this rapidly evolving technology. And although we
must anticipate the use of AI by attackers, advances
in AI-powered cybersecurity should give defenders
an asymmetric advantage in the near future.
This year we will also share how Microsoft is
responding to the significant attacks on our
corporate infrastructure. This includes details of our
Secure Future Initiative and how we are orchestrating
a company-wide initiative to make security our top
corporate priority. We hope that these learnings will
help others think through their own security posture
and approach to cyber defense.
Microsoft is proud to deliver the Microsoft
Digital Defense Report, now in its fifth edition,
as part of our commitment to helping the world
understand and mitigate cyber threats. We believe
transparency and information-sharing are essential
to the protection of the global cyber ecosystem.
Communicating the insights that we derive from our
unique vantage point is one of the many ways we
work to make the cyber world a safer place.
As our CEO, Satya Nadella, has said: “This is a
consequential time.” We stand on the frontier of
an AI-empowered world. It is up to us, however,
to leverage AI most effectively. In the tug-of-
war between attackers and defenders in which
the attackers currently have an advantage, it
will take conscientiousness and commitment by
both the public and private sectors to ensure the
defenders win.

Tom Burt
Corporate Vice President,
Customer Security and Trust

---

5
Microsoft Digital Defense Report 2024
Overview
Overview
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
About this report
Introduction
Our unique vantage point Cybersecurity at Microsoft
5
Our unique vantage point
The depth and breadth of Microsoft’s
presence in the digital ecosystem offers
a unique perspective that we share in
this report.
Our expansive, global vantage point gives us insight
into key trends in cybersecurity that affect everyone
from individuals to nations.
We process more than 78 trillion security signals per
day, from billions of Windows endpoints, the cloud,
and a broad spectrum of products and services.
From these signals we gain visibility into attack
activity, a unique understanding of emerging attack
techniques, and deeper insights about the overall
threat landscape.
This spectrum of security signals is further enhanced
by the diversity of our customers and partners,
including governments, enterprises large and small,
consumers, and gamers.
Microsoft’s commitment to supporting the cloud
across infrastructure, platform, application, and
multi-cloud scenarios complements the diversity of
a large ecosystem of partners and suppliers which
geometrically expands the richness of the data we
use to understand the threat landscape.
Yet our understanding of the threat landscape is
more than just data. It is informed by the expertise
of our employees:
*   Threat intelligence and geopolitical experts,
    tracking cybercriminal and nation-state
    threat actors.
*   Security researchers, software architects, and
    engineers, responding to new threats and adding
    new security features for protection.
*   Analysts, internal auditors, and risk specialists,
    maintaining operational compliance within
    a complex system of cybersecurity and
    privacy regulations.
*   Incident responders, who “run to the fire” in
    support of customers.
*   Security advisors, working with customers across
    the spectrum of cybersecurity.
*   Investigators, analysts, and legal teams who work
    globally to disrupt borderless criminal networks,
    and align public policy objectives in support of
    digital international norms on cyberpeace.
*   Microsoft executives, who are directly
    accountable for (and have their compensation
    tied to) the achievement of these
    security objectives.
Finally, the impact of AI is notable throughout
our vantage point. Security researchers and
threat hunters are seeing AI transform the threat
landscape. However, Microsoft’s recent investment
in AI technologies reflects confidence in the benefits
these tools can provide, including a perspective that
exceeds human processing capacity.
Microsoft is proud of its commitment to
cybersecurity and organizational resilience. As we
celebrate our 50th year, we have gained valuable
insights from past challenges. We are keen to
share best practices that include maintaining and
enhancing the right security culture, addressing
technical debt associated with a longstanding
corporate history, and investing in a secure future.
78 trillion
security signals per day inform our insights
34,000
full-time dedicated security engineers
15,000
partners with specialized security expertise

---

6
Microsoft Digital Defense Report 2024
Overview
Overview
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
About this report
Introduction
Our unique vantage point Cybersecurity at Microsoft
Our presence in the
digital ecosystem
positions us to
observe key trends
in cybersecurity.
Microsoft’s perspectives
on cybersecurity
are framed through
50 years of experience
and insight.
Society | Microsoft Stakeholders | Microsoft Customers
Microsoft’s unique vantage point
Microsoft serves billions of customers
globally, allowing us to aggregate security
data from a broad and diverse spectrum of
companies, organizations, and consumers.
An extra 13 trillion
security signals per day
2023: 65 trillion, 2024: 78 trillion
from the cloud, endpoints, software tools,
and partner ecosystem, to understand
and protect against digital threats and
criminal cyberactivity.
1,500 unique threat
groups tracked
Microsoft Threat Intelligence now tracks more
than 1,500 unique threat groups—including
more than 600 nation-state threat actor
groups, 300 cybercrime groups, 200 influence
operations groups, and hundreds of others.
Microsoft’s cybersecurity approach
Microsoft security investments
*   AI Red Teams
*   Defending Democracy
*   Detection and Response
*   Digital Crimes
*   Digital Safety
*   Incident Response
*   National Security
*   Physical Security
*   Public Awareness
    and Education
*   Responsible AI
*   Security Engineering
*   Security Operations
*   Threat Analysis
*   Threat
    Intelligence
34,000 dedicated
security engineers
focused full-time on the largest
cybersecurity engineering project
in the history of digital technology.
Current and
emerging threats
Technical
debt
AI as
a threat
Cybercriminals
Conflicting
regulatory
requirements
Supply chain
and ecosystem
Nation-state
actors

---

7
Microsoft Digital Defense Report 2024
Overview
Overview
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
About this report
Introduction
Our unique vantage point
Cybersecurity at Microsoft
7
Cybersecurity at Microsoft: the CISO’s perspective
This edition of the Microsoft Digital Defense Report
comes to you at a time when the cybersecurity
threat landscape has intensified for every
sector around the world. Microsoft, like many
organizations, has become a primary target, and
most notable is the dramatic increase in repeated,
sophisticated, and brazen attacks by cybercriminals
and nation-state attackers alike.
In January 2024 I took on the role of Microsoft
Chief Information Security Officer (CISO).
Immediately thereafter, we discovered we were
under a massive cyberattack by the threat actor
we refer to as Midnight Blizzard. The subsequent
days are some I remember vividly. Every available
resource across the company was utilized in our
defense against this attack—a monumental effort
that required speed, focus, and expertise. As I
was directing our response, my priority became
defending Microsoft and scaling our agility to face
future nation-state attacks. A large portion of our
third-party ecosystem was involved in this defense
as well.
Given ever-changing geopolitical conditions, the
world will face many such attacks in the future,
and Microsoft must also adjust to face these
threats. We have taken major steps over the past
year in fortifying assets across the company to
better prevent and defend against such threats.
The cornerstone of our work to protect Microsoft,
our partners, and customers is the Secure Future
Initiative Note 1 (SFI), which dedicates the entire company
to putting security above all other considerations.
As Satya Nadella, Microsoft’s CEO, said in a
company-wide announcement, “Security is a team
sport, and accelerating SFI isn’t just job number one
for our security teams—it’s everyone’s top priority
and our customers’ greatest need.” Everyone at
Microsoft is committed to making our products and
services secure by design, secure by default, and
operationally secure.
Among the most significant mitigations and actions
we have taken is a significantly expanded SFI to
improve our defense posture. We made phishing-
resistant multifactor authentication (MFA) mandatory
across the company, and we increased the
robustness of Microsoft’s corporate network.
To protect Microsoft, our partners, and customers
from future attacks, we dramatically grew our teams
dedicated to monitoring of and responding to
threats. And we reassigned roughly 34,000 full-time
equivalent engineers to security initiatives. This is an
important sampling of the many steps we have taken
since the beginning of this year—with much more
work in progress.
To increase the agility of Microsoft’s response to
this ever-changing threat environment, I instituted
an Office of the CISO and have hired a number
of Deputy CISOs. Our Deputy CISOs work with
our major product groups and programs to drive
greater depth and rigor in cybersecurity governance
across the entire company and to direct SFI at the
most pressing security risks. The Deputy CISOs take
responsibility for risk ownership and accountability,
determining the needed security architecture,
and providing input to me on each business unit’s
progress toward our SFI goals. Based on the ongoing
SFI work—and with input from the Deputy CISOs
—I provide regular updates on existing risk and SFI
performance to Microsoft’s Senior Leadership Team
and Board of Directors.
Every one of us at Microsoft shares a deep
responsibility to do our part to keep the world safe
and secure. As part of that commitment, we are
collaborating closely with security experts, industry
groups, and organizations like yours that face these
threats every day. Please read on to learn more
about the evolving threat landscape and how we are
committed to making the world safer for everyone.

Igor Tsyganskiy
Chief Information Security Officer

---

8
Microsoft Digital Defense Report 2024
Overview
The evolving cyber threat landscape
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
Key developments
9
Introduction
10
Threat actors and motivations
11
Nation-state threats
12
Ransomware
27
Fraud
31
Identity and social engineering
39
Distributed denial of service (DDoS) attacks
50
Chapter 1
The evolving cyber
threat landscape
How have trends and
tactics changed?

---

9
Microsoft Digital Defense Report 2024
Overview
The evolving cyber threat landscape
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
Introduction
Ransomware
Fraud
Identity and social engineering
DDoS attacks
Nation-state threats
Find out more on p17.
Find out more on p18.
Find out more on p22.
Find out more on p39.
Find out more on p27.
Find out more on p31.
A
B
C
Find out more on p24.
Key developments
The evolving cyber
threat landscape
As with any landscape, things change over
time. In the world of cybersecurity, however,
the pace of change has been astounding.
Observations over the past year have
reaffirmed the convergence of nation-state
and cybercriminal threat activity. Nation-
state threat actors used cybercrime as a
force multiplier, while financially motivated
cybercriminals pursued levels of defense
evasion and technical complexity once elusive
outside of nation-state operations.
We have also seen rapid shifts in the tactics
of hybrid war, wide-ranging attempts to
interfere in democratic elections, and a surge
in ransomware attacks and cyber-enabled
financial fraud across the globe.
These trends underscore the ongoing
necessity to enhance and implement robust
deterrence and mitigation strategies to
counter these threats effectively.
Blurred lines between nation-state
threat actor activity and cybercrime
Nation-state threat actors are conducting
operations for financial gain and enlisting
the aid of cybercriminals and commodity
malware to collect intelligence.
The many faces of hybrid war
Threat actors serving Russia and Iran are
leaning into cyber and influence operations
as tools to advance political and military
objectives in wartime.
The need to impose deterrent
consequences for cyber
aggression
The pace of nation-state sponsored
cyberattacks has escalated
to the point that there is now
effectively constant combat in
cyberspace without any meaningful
consequences to the attacker.
600 million identity attacks
per day
As multifactor authentication blocks
most password-based attacks, threat
actors are shifting their focus.
Nation-state influence operations
converge on elections
By the end of 2024, 2 billion people
will have had the opportunity to vote
in nationwide elections. Russia, Iran,
and China all engaged in election
influence efforts globally in 2024.
2.75x increase in human-operated
ransomware-linked encounters
By disabling or tampering with defenses,
attackers buy themselves time to install
malicious tools, exfiltrate data for
espionage or extortion, and potentially
launch attacks like ransomware.
Ingenuity and scalability of
fraud tactics surging globally
Cyber fraud not only presents a theft
risk, but it undermines the security,
trust, and reputation of individuals,
businesses, and organizations of
all sizes and types, in every region
and industry.

Microsoft Digital Defense Report 2023
Overview
Nation state threats
Ransomware
Fraud
Identity & Social engineering

---

10
Microsoft Digital Defense Report 2024
Overview
The evolving cyber threat landscape
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
Introduction
Nation-state threats
Ransomware
Fraud
Identity and social engineering
DDoS attacks
Introduction: The evolving landscape of cybersecurity
> “As we look to the future,
> the dawning of the age
> of AI means cybersecurity
> professionals will encounter
> both new opportunities and
> new challenges.”

As we reflect on this past year, it is more apparent
that the lines that once divided cybercrime, nation-
state sponsored attacks, and influence operations
have continued to blur. Cybercrime has continued
to mature as a robust and elaborate ecosystem,
with cybercriminal groups utilizing a full spectrum
of tools and techniques, including those learned,
borrowed, or stolen from nation-state actors.
While these cybercriminals are evolving their
tooling and targeting to evade defenders, many of
their underlying techniques and behaviors remain
unchanged due to their continued effectiveness.
Meanwhile, nation-state actors remain committed to
pursuing new levels of sophistication. This includes
creating unique tooling, upskilling their capabilities,
and targeting major technology providers—like
Microsoft—and enterprise supply chains.
Defenders can proactively combat threats from
both cybercriminal and nation-state actors by
addressing them at the technique layer. This means
implementing and enforcing policies and tooling,
such as enhanced multifactor authentication (MFA)
and attack surface reduction rules. At the same
time, as the threat landscape evolves, securing
identities, hardening endpoints, and protecting the
cloud infrastructure has become more important
than ever.
As Microsoft continues to take steps to protect
ourselves and our customers through our Secure
Future Initiative, The text "we encourage all organizations to commit to the foundational security principles of secure by design, secure by default, and secure operations." is highlighted. By collectively working toward these
fundamental security concepts, defenders can
reduce the attack surface across the broader
technology landscape.
At the same time, we have seen influence operations
change and increase globally at an unprecedented
scale as nation-states seek to sway public perception
and sentiment, sow discord, and undermine trust
in public institutions. In particular, governments
have used geopolitical issues such as the Russia-
Ukraine conflict and the Israel-Hamas war to spread
divisive and misleading messages. At a time when
the world is grappling with an overwhelming influx
of information delivered through both formal
and informal channels, the issue of combatting
misinformation is becoming increasingly vital.
As we look to the future, the dawning of the age of
AI means cybersecurity professionals will encounter
both new opportunities and new challenges.
Cybercriminal groups, nation-state threat actors, and
other adversaries are exploring AI technologies to
understand whether and how to leverage them in
the course of operations. We as defenders must also
explore and test these AI technologies, not only to
understand how they can be used by adversaries,
but how we can use them to strengthen our security,
protection, and response.

Amy Hogan-Burney
Vice President and Deputy General Counsel
Customer Security and Trust,
Cybersecurity Policy & Protection Unit

John Lambert
Corporate Vice President, Security Fellow,
Microsoft Threat Intelligence Center

---

11
Microsoft Digital Defense Report 2024
Overview
The evolving cyber threat landscape
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
Introduction
Nation-state threats
Ransomware
Fraud
Identity and social engineering
DDoS attacks
Threat actors and motivations
In this report, we discuss 30 different threat actors to provide examples of activity for a better understanding of attack targets, techniques, and motivations. Microsoft categorizes these actors
using a weather-related naming system. For example, “Flood” refers to actors who engage in influence operations. The actors included in this year’s report demonstrated significant activity and
effectiveness from July 2023 through June 2024. In the chart below, we map some of the motivations tracked over the past five years, to show how these actors often have multiple motivations
driving their operations. It’s important to note that the threat landscape is vast, and the threat actors and motivations detailed here represent only a small portion of those tracked by Microsoft.

KEY TO
MOTIVATIONS MAPPING
Cryptocurrency theft
C
Cybercrime services
CS
Data destruction
Dd
Data theft for profit
Dt
Disruption
D
Election
influence
Ei
Espionage
E
Influence
operations
I
Ransomware/Extortion
R
Nation-state actors
Cyber operators acting on behalf of or directed
by a nation-state-aligned program, irrespective of
whether for espionage, financial gain, or retribution.
Russia
Aqua Blizzard
Espionage
Midnight Blizzard
Espionage
Seashell
Blizzard
Data destruction
Disruption
Election influence
Espionage
Influence operations
Ransomware/Extortion
Secret Blizzard
Espionage
China
Flax Typhoon
Data theft for profit
Espionage
Granite Typhoon
Data theft for profit
Espionage
Nylon Typhoon
Espionage
Raspberry Typhoon
Espionage
Data theft for profit
North Korea
Citrine Sleet
Cryptocurrency theft
Data theft for profit
Jade Sleet
Cryptocurrency theft
Data theft for profit
Moonstone
Sleet
Espionage
Ransomware/Extortion
Sapphire Sleet
Cryptocurrency theft
Data theft for profit
Iran
Cotton
Sandstorm
Data destruction
Data theft for profit
Disruption
Election influence
Espionage
Influence operations
Ransomware/Extortion
Mint
Sandstorm
Election influence
Espionage
Ransomware/Extortion
Influence
Operations
Information campaigns or groups employing
communications online or offline in a manipulative
fashion to shift perceptions, behaviors, or decisions
by target audiences to further a group or a nation’s
interests and objectives.
Ruza Flood
Election influence
Influence operations
Sefid
Flood
Election influence
Espionage
Influence operations
Taizi Flood
Election influence
Influence operations
Volga Flood
Election influence
Influence operations
Financially motivated
Cyber campaigns or groups directed by a criminal
organization or person with motivations of financial gain
and are not associated with high confidence to a known
non-nation-state or commercial entity.
Octo Tempest
Cryptocurrency theft
Data theft for profit
Ransomware/Extortion
Groups in development
A temporary designation given to unknown, emerging, or developing threat activity.
This designation allows Microsoft to track a group as a discrete set of information until
we reach high confidence about the origin or identity of the actor behind the operation.
Storm–0501
Data theft for profit
Ransomware/Extortion
Storm–0539
Data theft for profit
Storm–0593
Espionage
Storm–0784
Disruption
Ransomware/Extortion
Storm–0842
Data destruction
Disruption
Election influence
Influence operations
Ransomware/Extortion
Storm–0867
Cybercrime services
Storm–1101
Cybercrime services
Storm–1516
Election influence
Influence operations
Storm–1575
Disruption
Storm–1679
Influence operations
Storm–2049
Espionage
For more information on threat actor naming, please visit [https://aka.ms/threatactors](https://aka.ms/threatactors)

Microsoft Digital Defense Report 2023
Overview
Nation state threats
Ransomware
Fraud
Identity & Social engineering

---

12
Microsoft Digital Defense Report 2024
Overview
The evolving cyber threat landscape
The evolving cyber threat landscape
Centering our organizations on security
Early insights: AI’s impact on cybersecurity
Appendix
Introduction
Nation-state threats Ransomware
Fraud
Identity and social engineering
DDoS attacks
1
2
3
4 5 6 7 8 9
10
Nation-state threats
Nation-state threat
activity by the numbers
This past year, nation-state affiliated threat actors
once again demonstrated that cyber operations—
whether for espionage, destruction, or influence—
play a persistent supporting role in broader
geopolitical conflicts. In the wars in Europe and the
Middle East, Russia and Iran centered their threat
activity on their main adversaries in those fights,
Ukraine, and Israel, respectively. Meanwhile, Beijing’s
long-term focus on controlling Taiwan drove a high
level of targeting of Taiwan-based enterprises from
Chinese threat actors, who also penetrated the
countries around the South China Sea to collect
insights into military exercises and national policy.
What follows is a snapshot of the activity by-the-
numbers.
The United States is consistently among the
countries most impacted by the nation-state cyber
threat activity that Microsoft observes, a reflection
of the large US representation in our customer base
and the role the United States plays in research and
development and geopolitical events. Aside from
the United States and the United Kingdom—which
was the fifth most targeted nation this year—most
of the nation-state affiliated cyber threat activity we
observed was concentrated in sites of active military
conflict or heightened regional tension: Israel,
Ukraine, the United Arab Emirates, and Taiwan.
The Education and Research sector
became the second most targeted
by nation-state threat actors
In 2024, Education and Research became the
second most targeted sector by nation-state
threat actors.
In addition to offering intelligence such as
research and policy discussions, education and
research institutions are often used as testing
grounds by threat actors before they pursue
their actual targets.
For example, QR code phishing, a technique
now used widely to compromise user accounts
at scale and create an entry point for business
email compromise (BEC) attacks discussed
later in this chapter, became widely used in
targeted attacks against this sector as early as
August 2023.
Top 10 targeted sectors worldwide
Sector
Percentage
1
IT
24%
2
Education and Research
21%
3
Government
12%
4
Think tanks and NGOs
5%
5
Transportation
5%
6
Consumer Retail
5%
7
Finance
5%
8
Manufacturing
4%
9
Communications
4%
10 All others
16%
Threat actors from Russia, China, Iran, and North Korea
pursued access to IT products and services, in part to
conduct supply chain attacks against government and
other sensitive organizations.
Source: Microsoft Threat Intelligence, nation-state notification data
0
100
200
300
400
500
600
Nation-state threat activity by the numbers continued
Nation-state threat actor targeting
Regional sample of activity levels observed
North America,
Latin America
& Caribbean
United
States
Most targeted
Israel
Most targeted
Middle East &
North Africa
Europe &
Central Asia
South Asia,
East Asia
& Pacific
Ukraine
Most targeted
Taiwan
Most targeted
Observed
activity count
United States
Canada
Brazil
Peru
Argentina
Colombia
Mexico
Dominican Republic
Chile