# ENISA THREAT LANDSCAPE 2023

The official report URL is: https://www.google.com/search?q=Enisa+Threat+Landscape

EUROPEAN UNION AGENCY
FOR CYBERSECURITY

ENISA THREAT
LANDSCAPE 2023

July 2022 to June 2023

OCTOBER 2023

ENISA THREAT LANDSCAPE 2023
October 2023

ABOUT ENISA

The European Union Agency for Cybersecurity, ENISA, is the Union’s agency dedicated to achieving a high common
level of cybersecurity across Europe. Established in 2004 and strengthened by the EU Cybersecurity Act, the
European Union Agency for Cybersecurity contributes to EU cyber policy, enhances the trustworthiness of ICT
products, services and processes with cybersecurity certification schemes, cooperates with Member States and EU
bodies, and helps Europe prepare for the cyber challenges of tomorrow. Through knowledge sharing, capacity
building and awareness raising, the Agency works together with its key stakeholders to strengthen trust in the
connected economy, to boost resilience of the Union’s infrastructure, and, ultimately, to keep Europe’s society and
citizens digitally secure. More information about ENISA and its work can be found here: www.enisa.europa.eu.

CONTACT
To contact the authors, please use etl@enisa.europa.eu
For media enquiries about this paper, please use press@enisa.europa.eu.

EDITORS
Ifigeneia Lella, Eleni Tsekmezoglou, Marianthi Theocharidou, Erika Magonara, Apostolos Malatras, Rossen
Svetozarov Naydenov, Cosmin Ciobanu – European Union Agency for Cybersecurity

CONTRIBUTORS
Claudio Ardagna, Stephen Corbiaux, Koen Van Impe, Radim Ostadal

ACKNOWLEDGEMENTS
We would like to thank the Members and Observers of the ENISA ad hoc Working Group on Cyber Threat
Landscapes for their valuable feedback and comments in validating this report. We would also like to thank the ENISA
Advisory Group and the National Liaison Officers network for their valuable feedback.

We would also like to thank the EEAS Strategic Communication Task Forces and Information Analysis Division (SG.
STRAT.2) for sharing the data on information manipulation and revising and contributing to the chapter on information
manipulation.

LEGAL NOTICE
This publication represents the views and interpretations of ENISA, unless stated otherwise. It
does not endorse a regulatory obligation of ENISA or of ENISA bodies pursuant to the
Regulation (EU) No 2019/881.

ENISA has the right to alter, update or remove the publication or any of its contents. It is
intended for information purposes only and it must be accessible free of charge. All references
to it or its use as a whole or partially must contain ENISA as its source.

Third-party sources are quoted as appropriate. ENISA is not responsible or liable for the content
of the external sources including external websites referenced in this publication.

Neither ENISA nor any person acting on its behalf is responsible for the use that might be made
of the information contained in this publication.

ENISA maintains its intellectual property rights in relation to this publication.

1

ENISA THREAT LANDSCAPE 2023
October 2023

COPYRIGHT NOTICE
© European Union Agency for Cybersecurity (ENISA), 2023

This publication is licenced under CC-BY 4.0 “Unless otherwise noted, the reuse of this
document is authorised under the Creative Commons Attribution 4.0 International (CC BY 4.0)
licence (https://creativecommons.org/licenses/by/4.0/). This means that reuse is allowed,
provided that appropriate credit is given and any changes are indicated”.

ISBN: 978-92-9204-645-3, DOI: 10.2824/782573

2

ENISA THREAT LANDSCAPE 2023
October 2023

TABLE OF CONTENTS

1. THREAT LANDSCAPE OVERVIEW

2. THREAT ACTOR TRENDS

3. ANALYSIS OF THE VULNERABILITIES LANDSCAPE 2022-2023

4. RANSOMWARE

5. MALWARE

6. SOCIAL ENGINEERING

7. THREATS AGAINST DATA

8. THREATS AGAINST AVAILABILITY: DENIAL OF SERVICE

9. THREATS AGAINST AVAILABILITY: INTERNET THREATS

10. INFORMATION MANIPULATION AND INTERFERENCE

11. SUPPLY CHAIN ATTACKS

A ANNEX: MAPPING TO MITRE ATT&CK FRAMEWORK

B ANNEX: RECOMMENDATIONS

6

20

38

51

62

70

83

93

104

110

124

131

140

3

ENISA THREAT LANDSCAPE 2023
October 2023

EXECUTIVE SUMMARY

The ENISA Threat Landscape (ETL) report, now in its eleventh edition, plays a crucial role in understanding the
current state of cybersecurity mainly within the European Union (EU). It provides valuable insights into emerging
trends in terms of cybersecurity threats, threat actors’ activities as well as vulnerabilities and cybersecurity incidents.
Accordingly, the ETL aims at informing decisions, priorities and recommendations in the field of cybersecurity. It
identifies the top threats and their particularities, threat actors’ motivations and attack techniques, as well as provides
a deep-dive insight on particular sectors along with a relevant impact analysis. The work has been supported by
ENISA’s ad hoc Working Group on Cybersecurity Threat Landscapes (CTL).

In the latter part of 2022 and the first half of 2023, the cybersecurity landscape witnessed a significant increase in both
the variety and quantity of cyberattacks and their consequences. The ongoing war of aggression against Ukraine
continued to influence the landscape. Hacktivism has expanded with the emergence of new groups, while
ransomware incidents surged in the first half of 2023 and showed no signs of slowing down. The prime threats
identified and analysed include:

• Ransomware
• Malware
• Social engineering
• Threats against data
• Threats against availability: Denial of Service
• Threats against availability: Internet threats
• Information manipulation and interference
• Supply chain attacks

For each of the identified threats, we determine impact, motivation, attack techniques, tactics and procedures to map
relevant trends and propose targeted mitigation measures. During the reporting period, key findings include:

• DDoS and ransomware rank the highest among the prime threats, with social engineering, data related
threats, information manipulation, supply chain, and malware following.

• A noticeable rise was observed in threat actors professionalizing their as-a-Service programs,
employing novel tactics and alternative methods to infiltrate environments, pressure victims, and extort them,
advancing their illicit enterprises.

• ETL 2023 identified public administration as the most targeted sector (~19%), followed by targeted
individuals (~11%), health (~8%), digital infrastructure (~7%) and manufacturing, finance and transport.
Information manipulation has been as a key element of Russia’s war of aggression against Ukraine
has become prominent.

• State-nexus groups maintain a continued interest on dual-use tools (to remain undetected) and on
trojanising known software packages. Cybercriminals increasingly target cloud infrastructures, have
geopolitical motivations in 2023 and increased their extortion operations, not only via ransomware but
also by directly targeting users.

• Social engineering attacks grew significantly in 2023 with Artificial Intelligence (AI) and new types of
techniques emerging, but phishing still remains the top attack vector.

The key findings and judgments in this assessment are based on multiple and publicly available resources which are
provided in the references used for the development of this document. The report is mainly targeted at strategic
decision-makers and policy-makers, while also being of interest to the technical cybersecurity community.

4

ENISA THREAT LANDSCAPE 2023
October 2023

5

ENISA THREAT LANDSCAPE 2023
October 2023

1. THREAT LANDSCAPE OVERVIEW

In its eleventh edition, the ENISA Threat Landscape (ETL) report offers a broad overview of the cybersecurity threat
landscape. Over time, the ETL has served as a crucial tool for comprehending the present state of cybersecurity
within the European Union (EU), furnishing insights into trends and patterns. This, in turn, has guided pertinent
decisions and prioritisation of actions and recommendations. The ETL report combines strategic and technical
elements, catering to both technical and non-technical audiences. The ETL 2023 report has been validated and
supported by the ENISA ad hoc Working Group on Cybersecurity Threat Landscapes (CTL)¹ and the ENISA National
Liaison Officers (NLO) Network.

Throughout the latter part of 2022 and the initial half of 2023, there was a notable escalation in cybersecurity attacks,
setting new benchmarks in both the variety and number of incidents, as well as their consequences. The ongoing war
of aggression against Ukraine remains a significant factor shaping the cybersecurity landscape. The phenomenon of
hacktivism has seen steady expansion, marked by the emergence of numerous new groups. Concurrently, it was
observed that a rise of ransomware groups took place, with the first half of 2023 witnessing an unprecedented surge
in ransomware incidents, a trend that shows no signs of abating.

Additional focus was concentrated on the various kinds of impacts cyber threats have in critical sectors, including the
sectors listed in the Network and Information Security Directive 2 (NISD 2). Interesting insights may be drawn from the
particularities and insight of each sector when it comes to the threat landscape, as well as potential interdependencies
and areas of significance. ENISA is following up by developing sectorial threat landscapes, diving deeper into the
elements of each sector and providing targeted insight.

The ETL 2023 report follows the same customary approach, drawing from diverse open-source data and cyber threat
intelligence sources. It pinpoints significant threats, discerns emerging trends and offers practical high-level strategies
for mitigating risk. This year's ETL continues to use the officially endorsed ENISA Cyber Security Threat Landscape
Methodology² , which was released in 2022. The ENISA CTL Methodology serves as a foundational framework for the
transparent and systematic creation of comprehensive cybersecurity threat landscapes, spanning horizontal, thematic,
and sector-specific perspectives. This process is characterised by rigorous data collection and analysis procedures.

1.1 PRIME THREATS
A series of cyber threats emerged and materialised during the reporting period. According to the findings detailed in
this report, the ENISA Threat Landscape 2023 report highlights and directs attention toward eight prime threat groups
(refer to Figure 1). These particular threat groups have been singled out due to their prominence over the years, their
widespread occurrence and the significant impact resulting from the realisation of these threats.

• Ransomware

According to ENISA’s Threat Landscape for Ransomware Attacks³ report, ransomware is defined as a type of
attack where threat actors take control of a target’s assets and demand a ransom in exchange for the return of the
asset’s availability. This action-agnostic definition is needed to cover the changing ransomware threat landscape,
the prevalence of multiple extortion techniques and the various goals, other than solely financial gains, of the
perpetrators. Ransomware has been, once again, one of the prime threats during the reporting period, with several
high profile and highly publicised incidents.

• Malware

Malware, also referred to as malicious code and malicious logic, is an overarching term used to describe any
software or firmware intended to perform an unauthorised process that will have an adverse impact on the
confidentiality, integrity or availability of a system.

¹ https://www.enisa.europa.eu/topics/threat-risk-management/threats-and-trends/ad-hoc-working-group-cyber-threat-landscapes.
² https://www.enisa.europa.eu/publications/enisa-threat-landscape-methodology
³ ENISA Threat Landscape for Ransomware Attacks https://www.enisa.europa.eu/publications/enisa-threat-landscape-for-ransomware-attacks.

6

ENISA THREAT LANDSCAPE 2023
October 2023

• Social Engineering

Social engineering encompasses a broad range of activities that attempt to exploit human error or human
behaviour with the objective of gaining access to information or services. It uses various forms of manipulation to
trick victims into making mistakes or handing over sensitive or secret information. Users may be lured to open
documents, files or e-mails, to visit websites or to grant access to systems or services. Although the lures and
tricks used may abuse technology, they rely on a human element to be successful. This threat canvas consists
mainly of the following attack vectors: phishing, spear-phishing, whaling, smishing, vishing, watering hole attack,
baiting, pretexting, quid pro quo, honeytraps and scareware. While social engineering techniques are often used to
gain initial access, they may also be used at later stages in an incident or breach. Notable examples are business
e-mail compromise (BEC), fraud, impersonation, counterfeit and, more recently, extortion.

• Threats against data

A data breach is defined in the GDPR as any breach of security leading to the accidental or unlawful destruction,
loss, alteration or unauthorised disclosure of or access to personal data transmitted, stored or otherwise
processed (article 4.12 GDPR). Technically speaking, threats against data can be mainly classified as data breach
or data leak. Though often used as interchangeably concepts, they entail fundamentally different concepts that
mostly lie in how they happen⁴ ⁵. Data breach is an intentional cyber-attack brought by a cybercriminal with the
goal of gaining to unauthorised access and release sensitive, confidential or protected data. In other words, a data
breach is a deliberate and forceful attack against a system or organisation with intention to steal data. Data leak is
an event (e.g. misconfigurations, vulnerabilities or human errors) that can cause the unintentional loss or exposure
of sensitive, confidential or protected data (intentional attacks are sometimes referred to as data exposure).

• Threats against availability: Denial of Service

Availability is the target of a plethora of threats and attacks, among which DDoS stands out. DDoS targets system
and data availability and, though it is not a new threat, it plays a significant role in the cybersecurity threat
landscape⁶ ⁷. Attacks occur when users of a system or service are not able to access relevant data, services or
other resources. This can be accomplished by exhausting the service and its resources or overloading the
components of the network infrastructure⁸.

• Threats against availability: Internet threats

Threats to Internet availability refer to intentional or unintentional disruptions of Internet or electronic
communications that result in Internet outages, blackouts, shutdowns or censorship. Internet disruptions can be
due to government-directed Internet shutdowns, cyclones, massive earthquakes, power outages, cable cuts,
cyberattacks, technical problems and military actions. These threats are diversifying and growing, having reached
a new record in this reporting period and having caused huge monetary loss to national economies.

• Information Manipulation
Foreign Information Manipulation and Interference (FIMI) describes a mostly non-illegal pattern of behaviour that
threatens or has the potential to negatively impact values, procedures and political processes. Such activity is
manipulative in character, conducted in an intentional and coordinated manner. FIMI can be carried out by state or
non-state actors, including their proxies inside and outside their own territory, whereas in this report we study
the threat regardless of its origin.

• Supply Chain Attacks

A supply chain attack targets the relationship between organisations and their suppliers⁹. For this ETL report we
use the definition as stated in the ENISA Threat Landscape for Supply Chain Attacks¹⁰ in which an attack is
considered to have a supply chain component when it consists of a combination of at least two attacks. For an
attack to be classified as a supply chain attack, both the supplier and the customer have to be targets. SolarWinds
was one of the first revelations of this kind of attack and showed the potential impact of supply chain attacks. It

⁴ https://blog.f-secure.com/data-breach-and-data-leak-whats-the-difference .
⁵ https://www.upguard.com/blog/data-breach-vs-data-leak#:~:text=Simply%20put%2C%20a%20data%20leak,Apps%20data%20leak%20in%202021
⁶ Federal Office for Information Security (BSI), The State of IT Sec in Germany, September 2020.
⁷ Europol, Internet Organised Crime Threat Assessment (IOCTA) 2020, https://www.europol.europa.eu/activities-services/main-reports/internet-
organised-crime-threat-assessment-iocta-2020.
⁸ CISA, Understanding Denial-of-Service Attacks, November 2019. https://www.uscert.gov/ncas/tips/ST04-015.
⁹ https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks.
¹⁰ ENISA Threat Landscape for Supply Chain Attacks https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks.

7

ENISA THREAT LANDSCAPE 2023
October 2023

was observed that threat actors are continuing¹¹ to feed on this source to conduct their operations and gain a
foothold within organisations, to benefit from the widespread impact and large victim base of such attacks.

![Figure 1: ENISA Threat Landscape 2022 - Prime threats](https://i.imgur.com/your_image_link_here.png)

It should be noted that the aforementioned threats involve categories and refer to collections of diverse types of
threats that have been consolidated into the eight areas mentioned above. Each of the threat categories is further
analysed in a dedicated chapter in this report, which elaborates on its particularities and provides more specific
information on findings, trends, attack techniques and mitigation vectors.

In the following figure it can be seen that ransomware and DDoS attacks were the most reported forms of attack
during the reporting period and accounted for nearly half of the observed events followed by threats related to data.
Moreover, we need to stress out that in several cases incidents involved more than one threat category and were thus
analysed in the context of all respective categories. Given that the ETL is based on publicly available information and
the fact that such information might not always provide the full picture, in certain cases incidents were not able to be
classified into any threat category.

¹¹ Accenture Cyber Threat Intelligence Report https://www.accenture.com/ae-en/insights/security/cyber-threat-intelligence.

8

ENISA THREAT LANDSCAPE 2023
October 2023

![Figure 2: Breakdown of analysed incidents by threat type (July 2022 till June 2023)](https://i.imgur.com/your_image_link_here.png)

1.2 KEY TRENDS
The list below summarises the main trends observed in the cyber threat landscape during the reporting period. Further
details and analysis on the trends may be found throughout the various chapters that comprise the ENISA threat
landscape of 2023.

• Ransomware and threats against availability ranked at the top during the reporting period.
• Resourceful threat actors have been observed to misuse legitimate tools primarily to prolong their
cyber espionage operations . Their aim was to evade detection for as long as possible and obscure their
activities by using widely available software from most systems which makes it more challenging for
defenders to identify them. Maximizing their chances of success when it comes to an intrusion by not
arousing victim’ suspicions

• Geopolitics continue to have a strong impact on cyber operations.
• Several threat actors further professionalised¹² ¹³ their As-a-Service programmes. They not only used
novel tactics and methods to infiltrate environments but also delved into alternative approaches to pressure
and extort victims, all the while advancing their illicit enterprises.

• By Using Extortion Only Techniques criminal organisations have been progressively blending extortion
methods that almost invariably incorporate some form of data theft. Double extortion has witnessed a notable
rise, with certain groups even relying solely on the act of stealing information.
Increased operations by law enforcement, such as the takedown of Hive ransomware group's IT
infrastructure or Trickbot.

•
• Cl0p rose in the first half of 2023 with the weaponisation of two zero-days.
• One of the biggest malware threats is still information stealers such as Agent Tesla, Redline Stealer

• and FormoBook.
There is a steady decline in classic mobile malware, with adware remaining in numbers of occurrences
the most prevalent threat to mobile devices while in terms of impact spyware can be seen as the most
prevalent threat to mobile devices.

¹² PWC - Cyber Threats 2022: A Year in Retrospect - https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/cyber-year-in-
retrospect/pdf/2022-year-in-retrospect-report.pdf.
¹³ Group IB - Hi-Tech Crime Trends 2022/2023 – https://go.group-ib.com/hubfs/report/protected/group-ib-hi-tech-crime-trends-2022-2023-en.pdf.

9

ENISA THREAT LANDSCAPE 2023
October 2023

• Hacktivists are increasingly claiming¹⁴ that they target OT environments but public reporting indicate
they often¹⁵ overestimate or do not substantiate their claims.

• Phishing is once again the most common vector for initial access. But a new model of social engineering
is also emerging, an approach that consists of deceiving victims in the physical world.

• Business e-mail compromise (BEC, VEC) remains one of the attacker’s favourite means for obtaining
financial gain.

• The move from Microsoft macros to ISO , Onenote and LNK files is continuing, a shift towards the use
of LNK and ISO/ZIP files as well as Onenote files in response to Microsoft’s macro changes.

• Data compromise increased in 2023. There was a rise in data compromises leading up to 2021, and
although this trend remained relatively stable in 2022, it began to increase once more in 2023.

• There has been a Surge in AI Chatbots impacting the cybersecurity threat landscape. The disruptive
impact and the exponential adoption of generative artificial intelligence chatbots such as OpenAI ChatGPT,
Microsoft Bing and Google Bard are changing the way in which we work, live and play, all built around data
sharing and analysis.

• DDoS attacks are getting larger and more complex, are moving towards mobile networks and IoT and
are being used in the context of being used in support of additional means in the context of a conflict.
Internet shutdowns are at an all-time high. Internet availability threats are keeping up their momentum,
especially in the post-covid era, due to the increasing reliance of human activities and society on Internet
technologies.
Information manipulation is a key element of Russia’s war of aggression against Ukraine. Information
manipulation has been an essential and well-established component of Russia’s security strategies¹⁶ ¹⁷. The
number of analysed events for the reporting period has also grown significantly.
‘Cheap fakes’ and AI-enabled manipulation of information continues to be a cause for concern. In the
past months, the debate on the use of AI to manipulate information has heated up both within and beyond
the circle of industry professionals.

•

•

•

Threat groups have an increased interest in supply chain attacks and exhibit an increasing capability
by using employees as entry points. Threat actors will continue to target employees with elevated
privileges, such as developers or system administrators

1.3 EU PRIME THREATS
Cyberattacks continue to increase on the global scale; however, ENISA’s scope is primarily focused on EU member
states and thus more emphasis is placed on the EU landscape.

Figure 3 makes it evident that, starting from the first half of 2023, both global (i.e. non-EU) and EU events have shown
a relevant increase. However, it is important to note that the number of events observed can be influenced by various
factors. An uptick in reported cyberattacks does not necessarily imply an actual increase in number of attacks or the
strength of their impacts. This rise could be attributed to media or public attention being focused on specific events for
a certain period, resulting in more incidents being documented in open-source intelligence (OSINT) channels or threat
actors claiming victims in their sites or telegram channels with no real impact on those victims.

¹⁴ Mandiant - We (Did!) Start the Fire: Hacktivists Increasingly Claim Targeting of OT Systems - https://www.mandiant.com/resources/blog/hacktivists-
targeting-ot-systems.
¹⁵ Claroty - Hacktivist Group Claims Ability to Encrypt an RTU Device - https://claroty.com/team82/blog/hacktivist-group-claims-ability-to-encrypt-an-
rtu-device.
¹⁶ No Water’s Edge: Russia’s Information War and Regime Security (2023, Carnegie Endowment for International Peace).
¹⁷ https://raport.valisluureamet.ee/2023/en/russian-armed-forces/1-3-russia-continues-to-look-for-a-weak-link-in-ukrainian-cyberspace/.

10

ENISA THREAT LANDSCAPE 2023
October 2023

![Figure 3: Break down of Global and EU events (July 2022 – June 2023)](https://i.imgur.com/your_image_link_here.png)

Furthermore, as ENISA enhances its cyber threat intelligence capabilities, we anticipate an increase in the number of
observable cyber incidents in the future. Consequently, this should help mitigate the observational bias mentioned
previously and contribute to higher-quality and more informative findings.

Throughout the reporting period, EU Member States continued to be affected by the ongoing geopolitical crisis, with a
growing number of threat actors directing their efforts against both public and private organisations. These kinds of
events more often fall under the DDoS threat (chapter 8) with little to no impact in most of the cases reported through
OSINT. Ransomware attacks have also increased (chapter 4) in the EU.

ENISA observed approximately 2 580 incidents, with an additional 220 incidents specifically targeting two or more EU
Member States (labelled ‘EU’) as it can be seen in Figure 4 which shows a timeline of when the events where first
reported through the OSINT channels. In addition, throughout this iteration of the ETL it can be seen that
Ransomware and DDoS still remain the two prime threats for the EU as shown in Figure 5.

![Figure 4: Timeline of EU events (count of number of observed incidents per month)](https://i.imgur.com/your_image_link_here.png)

![Figure 5: EU breakdown of number of threats by threat group](https://i.imgur.com/your_image_link_here.png)

11

ENISA THREAT LANDSCAPE 2023
October 2023

1.4 SECTORAL ANALYSIS
Cyber threats transcend the boundaries of specific industries or sectors, exerting their influence across a broad
spectrum of areas. This phenomenon is a tribute to the pervasive nature of digital interconnectivity in today's world. As
demonstrated by the following figures, it becomes apparent that threat actors spare no sectors from their targeting
endeavours, reinforcing the notion that no sector remains unaffected by their actions.

The sectors analysed in this report in general follow the classification of the sector categories of the Network and
Information Security Directive (NIS2)¹⁸. There are however some deviations, derived by the sample used, as it may
include events affecting sectors beyond the scope of the NIS2 directive. Examples include Defence, Education¹⁹,
Media and entertainment, the Retail sectors and more. We have also grouped under the term ‘Digital service
provider’, the sectors listed in NIS2 as ICT service management (MSPs and MSSPs) and Digital providers. There is
also a separate category, labelled as ‘all sectors’ which is used when events have a global effect across sectors.
During the analysis, a lot of other sectors were identified that relate to various services that are not currently within the
scope of the NIS2 directive. These include consulting services, legal services, hospitality services etc, and are
grouped under the category ‘Services’.

![Figure 6: Targeted sectors per number of incidents (July 2022 - June 2023)](https://i.imgur.com/your_image_link_here.png)

During this reporting period in the overall global landscape, we have again observed a large number of events (Figure
6) targeting organisations in the public administration (19%) and health (8%) sectors. Events targeting digital
infrastructure (7%) and digital service providers (6%) form a substantial portion of the events observed. These are
events that affect more than one sector due to the reliance of the other sectors on these two sectors. We also
observed a considerable number of events targeting civil society and not necessarily a particular sector (these are
labelled as ‘Targeted individuals’ and amount to 11% of the events observed). They consist of social engineering or

¹⁸ https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022L2555.
¹⁹ The education sector was coupled in our sample with the research sector, as they are often intertwined. While the research sector is considered in
the scope of the NIS2 directive, educational organisations are not included.

13

ENISA THREAT LANDSCAPE 2023
October 2023

information manipulation campaigns. The manufacturing, transport and finance sectors all faced around 6% of the
events each throughout the reporting period.

The prime threat was ransomware and it appears to target the entire range of the sectors (Figure 7). The most
targeted sectors were manufacturing (14% out of ransomware events), health (13%), public administration (11%) and
services (9%).

These are followed by DDoS attacks and data-related threats. Thirty-four per cent of the DDoS attacks targeted public
administration, followed by the transport (17%) and banking/finance sectors (9%). Data related threats targeted all
sectors, with the ones that hold personal information being more affected. These included public administration (16%)
and health (10%) as well as targeted individuals (15%).

One fifth of the events involving as malware affected the general public (targeted individuals, 20%), followed by
malware infections in public administration (13%), digital infrastructure (13%), banking and finance (12%) and digital
service providers (7%). All sectors were targeted by 11% of the reported malware infections.

Out of the observed events related to social engineering, 30% were aimed at the general public, 18% at public
administration and 8% at all sectors. Likewise, information manipulation campaigns targeted individuals (47%), public
administration (29%), followed by the defence (9%) and media/entertainment (8%) sectors.

As expected, threats against the availability of the Internet primarily affected digital infrastructure (28%) and digital
service providers (10%). Public administration (15%), individuals (10%) and ‘all sectors’ (11%) were also affected, as
they are dependent on digital infrastructure and services.

Supply chain attacks affected public administration (21%) and involved primarily the digital service providers (16%),
digital infrastructure (10%) and energy (9%) sectors. Likewise, the exploitation of vulnerabilities was associated with
events targeting digital service providers (25%), digital infrastructures (23%) and public administration (15%), and they
affected all sectors (8%) and targeted individuals (8%) to a greater degree.

![Figure 7: Observed events related to prime ETL threats in terms of the affected sector](https://i.imgur.com/your_image_link_here.png)

In the breakdown of the top 20 ‘active’ threat actors during the reporting period, the trend that activity by actors is
often sector-agnostic becomes evident once more, as nearly all these threat actors are dispersed across various

14

ENISA THREAT LANDSCAPE 2023
October 2023

sectors. This can be further be seen when dealing with cybercriminals (chapter 2) as they are assessed to be
opportunistic by nature.

![Figure 8: Threat actor by sector](https://i.imgur.com/your_image_link_here.png)

1.5 IMPACT ASSESSMENT
In this iteration of ENISA’s threat landscape we have again included an assessment of the impacts of the events
observed. We followed a qualitative process of impact analysis in order to identify the consequences of an event. Due
to the fact that information related to the impact of cyberattacks is often not available or made public, determining and
assessing the effect following an incident entails a level of assumption in which a certain degree of subjectivity cannot
be avoided. This in itself makes the argument for improving the process of incident reporting in the EU, an aspect that
is reflected in the NIS2 Directive and an area where ENISA will continue its efforts in the coming years.

In the context of this ETL report, we defined and applied the following types of impact.

• Digital impact refers to damaged or unavailable systems, corrupted data files or exfiltration of data or some
announced malicious intrusion.

• Economic impact refers to the direct financial loss incurred, the damage to national security that can be
caused due to the loss of important material or a ransom demand.

• Social impact refers to any effect on the general public or to a widespread disruption that could have an
impact on society (e.g. incidents disrupting the national health system of a country, leakage of any data
concerning the general public’s IDs, social security numbers, addresses etc.).

• Reputational impact refers to the potential for negative publicity or an adverse public perception of the
entity that has been the victim of a cyber incident.

• Physical impact refers to any kind of injury or harm to employees, customers or patients.
• Psychological impact refers to any kind of confusion, discomfort, frustration, worry or anxiety caused to
employees, customers or patients, or the general public.

The events collected were classified according to these six types of impact by applying internal ENISA experience and
expertise. It is quite interesting to note that, in most of the events collected, some kind of digital impact was identified
as seen in Figure 9. Digital impact was observed in one of three ways: evidence of downtime (often associated with
hacktivist DDoS events, regardless of their brevity) reported by relevant vendors, data breaches or explicitly
mentioned by the sources being monitored.

Approximately one fifth of the events collected (19%) were evaluated as having an economic impact but this
assessment is based on the information available at the time of the analysis. Ransomware and DDoS incidents took
centre stage due to the financial gains sought by the threat actors or due to economic losses caused by disruptions in
manufacturing or in the provision of services (public administration, services, banking and finance). During the
assessment, it often remained uncertain whether ransoms were actually paid, so we included such information in the
assessment only when available. Data breaches were also considered to have an economic impact, primarily due to
legal obligations (e.g. fines due to GDPR violations) that could arise or due to the profit made by the attackers from
selling the acquired data, which were personal or proprietary information. This was observed primarily in the health
and manufacturing sectors, as well as public administration, services and targeted individuals.

We assessed social impact (18%) when analysing events with a significant effect on the general public and citizens,
either due to the leak of personal information or due to disruptions of services. These were mainly observed when
citizens were targeted directly or indirectly when events (ransomware, DDoS) were associated with public
administration and health sectors. The social impact referred mainly to the inability of the citizens to access important
services provided by these two sectors.

However, it is important to highlight that the assessment of reputational, psychological and physical impacts was
particularly challenging. This was due to the limited time between the incident taking place and our analysis, or due to
the fact that such impacts could not be assessed solely from open sources. Reputational impact was mostly
associated with ransomware, data breaches or leaks, with DDoS and information manipulation. Psychological impact
was observed when examining events of information manipulation and data leaks of personal information.

Another noteworthy observation was the rarity of events categorised as having ‘No impact’; this suggests a possible
hypothesis that media or the affected parties may exaggerate their impact when reporting cyber incidents.

![Figure 9: Threat type breakdown by Impact](https://i.imgur.com/your_image_link_here.png)

15

ENISA THREAT LANDSCAPE 2023
October 2023

1