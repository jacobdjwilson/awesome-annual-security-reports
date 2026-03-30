# Cyber-Threat-Landscape-Report 2025

Version 1.4 | 21 July 2025

## Table of Contents

- [Editorial Foreword](#editorial-foreword)
- [Executive Summary](#executive-summary)
- [Developments and Insights](#developments-and-insights)
- [Regional Incidents](#regional-incidents)
  - [ASEAN](#asean)
  - [East Asia](#east-asia)
  - [South Pacific](#south-pacific)
- [Territorial Insights](#territorial-insights)
  - [Singapore](#singapore)
  - [Malaysia](#malaysia)
  - [Indonesia](#indonesia)
  - [South Korea](#south-korea)
  - [Australia](#australia)
  - [Greater China Region](#greater-china-region)
- [Outlook of Cyber Threats for 2025](#outlook-of-cyber-threats-for-2025)
- [Defensive Actions for Cyber Defenders and Leaders](#defensive-actions-for-cyber-defenders-and-leaders)
- [Contributors](#contributors)
- [Appendices](#appendices)
  - [Techniques Heatmaps by Territory](#techniques-heatmaps-by-territory)
  - [Territorial Observed Top Exploited Vulnerabilities](#territorial-observed-top-exploited-vulnerabilities)
  - [ICS oriented Techniques Heatmaps](#ics-oriented-techniques-heatmaps)

---

## Editorial Foreword

The cyber threat landscape continues to evolve with geopolitical tensions, trade tensions, internal strife and the evolving adversarial behaviours fuelling the changes. Across the Asia Pacific, we have seen threats becoming more persistent, more targeted, and more difficult to defend against. We have developed this report to share our observations on the key trends and developments shaping the region’s cyber threat landscape.

This year’s edition includes observations from across ASEAN, East Asia and the South Pacific. As our regional presence grows, we remain committed to bring an Asia Pacific focussed view of the cybersecurity situation of the digital environment we operate in, whether through the threat intelligence we gather, the incidents we respond to, or the platforms we contribute to.

The environments in which we operate are complex. From geopolitical flashpoints and trade tensions, to localised unrest and cross-border criminal activity, each region presents its own unique cyber risk profile. Such an environment has proven fertile for the thriving underground economy, which we observe to have active collaborations and subcontracting, leading to increasing capability developments, and increased scale and efficacy of cyber-attacks and campaigns.

The widening use of diverse technologies, including those from established Western vendors, open-source solutions, and the emerging Eastern technology solutions, have led to increasingly the fragmented digital ecosystems. This complexity makes defending against Ransomware, state-linked cyber-attack campaigns, cybercrime, and hacktivism not only more challenging, but also more urgent.

Ransomware in particular, has become endemic in the region, if not globally. We are seeing variants that bypass EDR and XDR systems with increasing success. Hacktivists are also becoming more tactically capable, moving beyond surface-level disruption and website defacements, to leverage advanced exploit platforms. Meanwhile, organised cybercrime groups are expanding in number and sophistication, with many of them working in concert with larger threat actors. These collaborations are increasing the complexity to determine the motivation and “mastermind” behind attacks.

Ensign remains committed to monitor how these developments are reshaping the threat landscape. This report outlines key defensive considerations and offers recommendations that security leaders can act on to stay ahead of a threat environment that shows no sign of slowing down.

As a Research Sponsor to the MITRE Center for Threat Informed Defense and an advocate for the threat-informed defence concept, we continue to provide tactics, techniques and procedures (TTPs) for the observed threats leveraging the MITRE ATT&CK framework, version 17 this year, with the MITRE ATT&CK Navigator JSON files for cyber defenders to use in monitoring, threat hunting, red teaming, risk assessments, and other cyber defence operations.

![Ensign InfoSecurity Company Profile]

---

## Executive Summary

Since the formation of Ensign in 2018, we have released these threat reports to help our clients and the general community understand the state of the threat environment in Asia Pacific. In 2025, we note the growing geopolitical and trade tensions around the world and observed the growing cyber activities by a number of threat groups.

For 2025, key insights to note:

1. **State-sponsored threat groups are increasing their activities.** They are likely to be pre-positioning, in light of geopolitical and trade tensions, to maintain strategic opportunities for future effects by compromising digital infrastructure and the cyber supply chain. Whether this is for the purposes of staging for future attacks, espionage or disruption. The intentions are multi-fold, but we suspect this will grow significantly, posing concerns for the public sector and critical infrastructure operators.

2. **Ransomware continues to be the endemic “digital flu” that plagues companies across the world.** Criminal groups are collaborating and competing in the underground economy for a larger share of the prize. New capabilities are being developed and the efficacy of attacks will grow. We note:
   - Initial Access Brokers (IABs) pursuing a “breach once, sell to many” approach.
   - Mastermind threat groups subcontracting cyber-attack tasks to other parties to create multi-prong and distraction effects in their cyber campaign.
   - Multiple income streams pursued for financial gain amongst organised crime groups.

3. **Finally, attacks are also targeting the weaker but highly important links in our economic systems.** In particular, we are witnessing attacks on our business and professional services (BPS) firms, including legal firms, accounting companies and professional services firms. These companies hold (or are custodians of) significant assets but are not large enough to mount deep defences, and have come under increasing attacks from threat groups.

The cyber space is not a benign place and as digitisation grows, and the use of AI becomes more pervasive, the threats will commensurately grow. Ensign remains committed to defending and protecting our customers in this environment.

---

## Developments and Insights

![Top Developments and Insights of 2024 Infographic]

The Asia Pacific region experienced a high intensity of cyber threat activity in 2024, fuelled by geopolitical tensions (e.g., South-China Sea disputes, PRC-ROC tensions, PRC-DPRK-Russia involved activities), increasing economic competition (e.g., US tariffs, US-China tensions), challenges (e.g., Myanmar civil unrest, organised crime syndicates operating along Thailand’s border), and uneven progress made in digitalisation and cyber defence maturity (laws and operations).

Across the territories, Ensign observed increasing variety of technologies implemented, from well-established and familiar Western solutions, open source and open source adapted solutions, and Eastern (predominantly driven by Chinese companies) solutions. The rising diversification of technologies used in the organisations’ digital attack surface elevates the complexity and challenges organisations face in maintaining effective defences against the increasingly competent and sophisticated cyber threats.

In the midst of the situation in 2024, the public sectors and organisations have been making steady progress in bolstering the cyber defences. Governments across the world have updating their regulations to provide greater guidance on how to lay out the cyber controls for businesses and critical infrastructure – the EU updated the NIS legislation to enhance cybersecurity resilience and digital defence, Singapore updated the Cybersecurity Act, Indonesia’s Personal Data Protection Law and Malaysia’s Cyber Security Act came into effect in 2024, just to name a few. Amidst these regulatory developments, regional and international efforts are also underway to build up capacity and capability through collaborative efforts and exercises – the efforts through the ASEAN-Singapore Cybersecurity Centre of Excellence (ASCCE) in Singapore, and the ASEAN-Japan Cybersecurity Capacity Building Centre (AJCCBC) in Thailand, the establishment of the ASEAN-CERT, the annual EU Locked Shields exercise, and continued dialogue and proliferation of the UN cyber norms, just to name a few.

### Ransomware
RANSOMWARE, with (i) the leaks of Ransomware platform source codes (e.g., LockBit and Conti) and Ransomware-as-a-Service (RaaS) operations playbooks, (ii) the reorganisation of constituent operators (i.e., initial access brokers, RaaS operators, negotiators, crypto mixers and launderers), the barrier to entry for parties with malicious intent to rapidly adopt Ransomware operations has been lowered.

Supported by the now commonplace pervasiveness of generative AI solutions, both in the public and deep and dark web (DDW), threat actors are now more rapidly evolving their exploits, techniques, playbooks and platforms to increase their success rates in penetrating organisations and extracting value from them, whether that be (i) information and monetary value, or (ii) to cause pain through disruption, compromise of operations and destruction of technology services.

The prevalent RaaS variants in 2024 have developed novel capabilities which advance the Ransomware groups’ financial gain objectives, notably, (i) the ability to evade endpoint detection & response (EDR) and extended detection & response (XDR) solutions, (ii) having the ability to kill processes through bring your own vulnerable driver (BYOVD) – particularly to impair defences, and (iii) adopting unique programming languages to enhance performance, target multi-platform and achieve stealth objectives.

This situation in aggregate, has raised the profile of Ransomware as the new digital endemic “flu”. Within Ensign’s operating territories, LockBit Gang, Kill Ransomware, RansomHub and Sarcoma Ransomware are the most active, in ranking order.

### Hacktivism
HACKTIVISM related activities have been driven by the troubled times we live in today. The World Economic Forum (WEF) and the United Nations (UN) have both acknowledged that we are in a modern period of a confluence of conflicts, disagreements and disruptions around the world, with some stakeholders taking on a “might is right” approach, and others taking a more insular approach towards trade and international engagements.

Enabled by the increasingly mature underground collaboration and sharing of capabilities and services, we observed the evolution of some hacktivists taking on advanced capabilities beyond the conventional distributed denial of service (DDoS) attacks, website defacements, and data breaches. DragonForce Ransomware emerged, with some connectivity to the previously reported DragonForce Malaysia hacktivist group, which most recently attacked retail brands in the United Kingdom[^1]. It first posted, in July 2022, the desire to have become a RaaS, and has been observed to have refactored/forked its Ransomware from the leaked source codes from LockBit and Conti.

We are also rapidly observing Hacktivists accelerating their development of exploit platforms, e.g., MegaMedusa DDoS platform for the RipperSec hacktivist group, and the increased collaboration with other hacktivist or organised crime groups as seen in the collaboration between R00TK1T and the Cyber Army of Russia. When hacktivists rally behind state-linked causes, they also participate in grey zone conflicts which complicate the treatment to these groups. This also presents as a boon and a bane – the advantage of increased organisation means that it becomes easier for defenders to profile and defend against these groups’ cyber-attacks, with the knowledge that they will likely become more competent and successful. The active hacktivist groups observed targeting the territories include Bjorka, ETHERSEC Team Cyber, R00TK1T and RipperSec.

[^1]: https://www.bbc.com/news/articles/c0el31nqnpvox

### Initial Access Brokers (IABs)
INITIAL ACCESS BROKERS (IABs) active in the territories are generally observed to be individual or small groups of individuals working as mercenaries for hire. While some of the IABs have affiliations with unique threat groups, especially RaaS groups, others generally collaborate with any other threat group as long as the price is right.

Increasingly, IABs have adopted a “breach once, sell to many” practice, working with RaaS groups with advantageous affiliate programs for prioritised access, but subsequently sell access to other parties after the “embargoed” period. IABs are also observed to opportunistically collect/exfiltrate data assets upon breach to be put up for sale as additional income streams; these are commonly called infostealers.

IABs are observed to leverage alternative authentication material’s such as session keys, OAuth tokens and the like to gain access rather than directly accessing user credentials, although, there is no shortage of leaked user credentials available on the region’s users.

### Organised Crime
ORGANISED CRIME group activities have been steadily rising with the increased digitalisation of the region with many territories having electronic public sector services, and digital banking and payment ecosystems.

The proliferating collaborations in the underground community have also given rise to subcontracting work leading to more (individual) initial access brokers (IABs) supporting other “mastermind” threat actor groups. IABs exploiting the use of AI, are now more effective and efficient in gathering credentials, performing target reconnaissance, and identifying vulnerabilities for exploitation.

Organised crime groups have been observed to leverage AI most with enhancing the efficacy of phishing attacks by enhancing the believability of the phishing content, and adapting a multi-channel strategy (e.g., initial contact on one communication platform, and asking the victims to follow through payments in other platforms) towards getting their victims to execute actions triggering compromise. The multi-channel strategy aims to throw off the digital trails in being easy to identify them, but also to confuse victims for payments.

The past year saw a doubling of Organised Crime groups actively targeting the territories (from 5 to 10). This is despite having successful law enforcement activities taking down threat actors, e.g., the arrest of GhostR/0mid16B/DESORDEN in Thailand[^2].

Other than operating RaaS, some of these Organised Crime groups are observed to have been subcontracted to perform data breaches, service disruptions, compromise supply chains, to help “mastermind” threat groups achieve their campaign objectives.

The Organised Crime groups observed in the territories include BITTER, Blackwood, Bronze Highland, FIN11, FIN7, GhostR, Pseudo Hunter, SharpPanda, TIDRONE, with Void Arachne. BITTER, Blackwood, Bronze Highland, Pseudo Hunter, and Void Arachne observed to pre-dominantly target the Greater China Region (GCR).

[^2]: https://www.channelnewsasia.com/singapore/spf-royal-thai-police-global-hacker-arrested-altdos-desorden-ghostr-0mid16b-4963661

### State-Sponsored Threats
STATE-SPONSORED threat groups have been observed to represent close to 40% of cyber activities in the region (39.8%), with deepening significance in their attacks. Many of these threat groups are observed to be well-resourced, have high-level capabilities, with a strategically patient approach in their compromise. These observations correlate with the industry term of advanced persistent threat (APT) where the threat actor breaches an environment and may not actively cause detrimental (and overtly observable) symptoms until it is necessary for their interest or mission.

Some threat groups in this category was observed to have exploited vulnerabilities in a variety of network devices, ranging from widely used Ubiquiti routers, Cisco and Fortinet network devices, and VPN solutions with the intent to stage their capabilities. Many of these devices typically provide trusted access between networks or are part of the unmanaged and “outside of perimeter” infrastructure. Such efforts can then enable disruption of services and/or espionage. We note that these threat groups leverage the challenges organisations face in managing a complete inventory of assets and the growing vulnerability patching debt to maintain persistent access, aside from cyber hygiene issues.

Increasingly, we observed higher sophistication attacks targeting hypervisors and container infrastructure, which typically have no security defence solutions, to provide persistence, stealth and deeper access into technology environments.

### Adversary Ecosystem
ADVERSARY ECOSYSTEM is now observed to have matured to an underground economy which is rich with subcontracting work, mutually reinforced evolution and capability enhancements due to competition and collaboration, which lead to material growth in reach and sophistication. The ecosystem, coupled with the already thriving use of AI (including agentic AI) and automation can make the adversaries more effective in their exploits of their targets and victims.

![Observed Interaction Map of Threat Groups]

---

## Regional Incidents

Across the regions – ASEAN, East Asia and South Pacific, we observed sustained cyber-attacks across 2024 which demonstrate sustained threat interests in the regions.

### ASEAN
![ASEAN Notable Cyber Incidents Timeline]

### East Asia
![East Asia Notable Cyber Incidents Timeline]

### South Pacific
![South Pacific Notable Cyber Incidents Timeline]

---

## Territorial Insights

### Singapore
![Singapore Threat Classification Matrix]

**MOST AFFECTED INDUSTRY GROUPS**
- Business & Professional Services
- Hospitality
- Banking, Finance & Insurance
- Retail
- TMT

**TOP NOTABLE CYBER-ATTACK EFFECTS OBSERVED**
- Data Breach
- Ransom
- Denial of Service
- Sale of Access
- Data Leak
- Sale of Data

---

## Outlook of Cyber Threats for 2025

*(Content to be populated based on report findings)*

---

## Defensive Actions for Cyber Defenders and Leaders

*(Content to be populated based on report findings)*

---

## Contributors

*(Content to be populated based on report findings)*

---

## Appendices

### Techniques Heatmaps by Territory
*(Refer to MITRE ATT&CK Navigator JSON files)*

### Territorial Observed Top Exploited Vulnerabilities
*(Refer to detailed vulnerability tables in report)*

### ICS oriented Techniques Heatmaps
*(Refer to ICS Matrix and JSON files)*

---

more susceptible to scams and phishing, especially in fast moving businesses
like e-commerce. Singapore elevated its attractivity in 2024 in MICE3, notably attracting Taylor
Swift  to  have  the  only  Asian  tour  location  for  her  concerts.  In  association,  retail  and
hospitality,  which  directly  relate  to  tourism  and  events,  may  have  attracted  increased
targeting  from  financially  motivated  threat  groups.  The  continued  targeting  of  Business  &
Professional Services is not surprising as this industry group posses/process large amounts
of sensitive information, including personal data, and generally having lower cyber defences.
Singapore’s efforts in carrying out law enforcement action on known threat groups had also
borne fruit with the arrest of the threat actor behind GhostR/0mid16B/DESORDEN through
regional collaborative action.
Singapore  observed  the  highest  number  of  variants  of  Ransomware  in  2024.  This  could  be
due  to  threat  actors  exploiting  of  Singapore’s  position  as  a  financial  hub  for  financial  gain.
Separately,  both  Ransomware  groups  and  state-sponsored  threat  groups  may  also  be
exploiting  Singapore’s  digital  infrastructure  as  test  beds  for  their  eventual  targets  of  other
digitally  advanced  territories,  and  to  exploit  Singapore’s  trusted  economy  as  supply  chain
pathway to gain access to other targets, whether in Singapore or elsewhere.

KEY TAKEAWAYS

• Organised crime groups are the
most representative threat group
targeting Singapore.

• State-sponsored threat groups
and Hacktivists representation
targeting Singapore has risen.

• Top targeted industry groups are
respectively TMT, Retail, and BFI.
• Retail and Hospitality are newly
observed top targeted industry
groups.

• Top notable cyber-attack effects
are respectively Data Breach,
Ransom, and Denial of Service.

• Singapore observed the highest

variety of Ransomware variants
targeting the territory.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

3. MICE – Meetings, Incentives, Conferences and Events.

32

Malaysia
KEY ANALYSIS INSIGHTS

ENSIGN THREAT
CLASSIFICATION
MATRIX

NIL

• RansomHub • RipperSec
• Sarcoma Ransomware

SharpPanda

• LockBit Gang • R00TK1T
• State-sponsored Threat
Groups

Insubstantial

Potential

Impending

Material

→→→ Increasing levels of threat to the subject →→→

Capability

Intent

Opportunity

●

●

●

●

●

●

●

●

●

MOST AFFECTED INDUSTRY GROUPS

TOP NOTABLE cyber-attack EFFECTS OBSERVED

The following observations are based on Ensign Proprietary Data and Cyber
Threat Intelligence data. Sorted in alphabetical order

Banking, Finance
& Insurance

Hospitality

Automotive & Mobility
Defence & Law
Enforcement
Energy & Utilities

Public Sector

TMT

New affected industries observed in 2024

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

Data Breach

41.1%

Denial of Service

30.1%

Ransom

Defacement

Initial Access

8.2%

6.8%

6.8%

Techniques of Concern

TA0001: Initial Acc ess
▪
T1566: Ph ishing
▪
T1190: Exp loit Public-Facing Application
▪
T1133: Exter nal Remote Services
▪
T1195: Su pply  Chain Compromise
▪
T1199: Trusted  Relationship
▪
T1078: Valid Acco unts
▪
T1189: Dr ive-by Compromise

TA0011: Com mand and Control
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪

T1071: Application Lay er Protocol
T1573: Encry pted Chan nel
T1102: Web  Service
T1095: Non-Application Lay er Protocol
T1219: Remote Access Too ls
T1001: Data Obfuscation
T1568: Dy namic Resolu tion
T1105: Ingress Tool Transfer
T1104: Mu lti-Stage Chan nels
T1572: Pr otocol Tunnellin g
T1132: Data En co ding
T1008: Fallback Channels
T1665: Hide In fr astructur e

TA0010: Exfiltration
▪
▪
▪
▪

T1567:Ex filtratio n Ov er Web Service
T1048: Exfiltration  o ver Alternative Protocol
T1041 E xfiltration Over C2 Channel
T1030: Data Transfer  Size Limits

TA0040: Impact
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪

T1491: Defacement
T1486: Data En cr ypted for Imp act
T1499: End point Den ial of Serv ice
T1498: Netwo rk Den ial of Service
T1489: Ser vice Stop
T1490: Inhibit System Recovery
T1485: Data Destructio n
T1657: Financial Theft
T1496: Resou rce Hijacking
T1529: Sy stem Shu tdown/Reboot

v17

33

Insights for Malaysia

While  organised  crime  groups  are  the  predominant  threat  groups  targeting  Malaysia,
hacktivist  threat  groups  have  risen.  Organised  crime  groups  targeting  Malaysia  may  be
subcontracted  by  other  mastermind  threat  groups  to  perform  their  cyber-attacks,
obfuscating the true intentions of attacks.

threat  groups  may  be  motivated  by  ASEAN’s
Cyber-attacks  by  state-sponsored
developments  and  thus  interested  in  performing  espionage  for  information  leverage  on
geopolitical  and  trade  oriented  advantages.  Hospitality  may  be  targeted  for  surveillance
objectives  of  politically  exposed  persons  (PEPs)  and  officials  who  participate  in  these
international  conferences  and  meetings  in-country  to  monitor  their  movements  and
behaviours.
Malaysia’s  increased  economic  interest  to  develop  the  TMT  industry  group  and  attract
foreign  direct  investments  in  TMT  may  also  draw  attention  to  threat  groups  who  are
interested to gain access to the data they process and/or the trusted access they provide to
their targets.
Energy  &  utilities,  as  a  newly  observed  top  targeted  industry  group,  may  be  in  relation  to
Malaysia’s  role  and  involvement  in  the  regional  grid  initiative  and  the  energy  trading
fluctuations observed in 2024.
Hacktivists  targeting  Malaysia  may  be  motivated  by  its  perceived  alignment  relating  to  the
conflicts in the Middle-east. DragonForce Ransomware, now an organised crime group, and
associated  with  the  previous  moniker  of  DragonForce  Malaysia,  evolved  from  being  a
hacktivist group to a RaaS operator.

KEY TAKEAWAYS

• Organised crime groups are the
most representative threat group
targeting Malaysia.

• Hacktivists have significantly risen

in representation targeting
Malaysia.

• Top targeted industry groups are
respectively Public Sector, TMT,
and Hospitality.

• Hospitality, BFI, Automotive &

Mobility, Defence & Law
Enforcement, and  Energy &
Utilities are newly observed top
targeted industry groups.

• Top notable cyber-attack effects
are respectively Data Breach,
Denial of Service, and Ransom.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

34

Indonesia

KEY ANALYSIS INSIGHTS

ENSIGN THREAT
CLASSIFICATION
MATRIX

NIL

• DragonForce Ransomware
• Kill Ransomware • RansomHub
• Sarcoma Ransomware

SharpPanda

• Bjorka • Brain Cipher
• ETHERSEC Team Cyber
• LockBit Gang • State-sponsored
Threat Groups

Insubstantial

Potential

Impending

Material

→→→ Increasing levels of threat to the subject →→→

Capability

Intent

Opportunity

●

●

●

●

●

●

●

●

●

MOST AFFECTED INDUSTRY GROUPS

TOP NOTABLE cyber-attack EFFECTS OBSERVED

The following observations are based on Ensign Proprietary Data and Cyber
Threat Intelligence data. Sorted in alphabetical order

Defence & Law
Enforcement

Hospitality

Banking, Finance &
Insurance

Public Sector

TMT

New affected industries observed in 2024

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

Denial of Service

56%

Data Breach

Defacement
Data Leak

Initial Access

24.9%

7.5%
4.6%

2.9%

Techniques of Concern

TA0001: Initial Acc ess
▪
▪
▪
▪
▪
▪
▪
▪

T1190: Exp loit Public-Facing Application
T1566: Ph ishing
T1133: Exter nal Remote Services
T1078: Valid Acco unts
T1199: Trusted  Relationship
T1659: Content In jection
T1195: Su pply  Chain Compromise
T1189: Dr ive-by Compromise

TA0011: Com mand and Control
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪

T1071: Application Lay er Protocol
T1219: Remote Access Too ls
T1102: Web  Service
T1001: Data Obfuscation
T1573: Encry pted Chan nel
T1090: Pr oxy
T1105: Ingress Tool Transfer
T1659: Content In jection
T1568: Dy namic Resolu tion
T1104: Mu lti-Stage Chan nels
T1095: Non-Application Lay er Protocol
T1572: Pr otocol Tunnellin g
T1132: Data En co ding
T1008: Fallback Channels

TA0010: Exfiltration
▪
▪
▪
▪

T1567: Exfiltration  Over  W eb Service
T1048: Exfiltration  Over  Alter native Pro tocol
T1041: Exfiltration  Over  C2 Chan nel
T1030: Data Transfer  Size Limits

TA0040: Impact
▪
▪
▪
▪
▪
▪
▪
▪

T1486: Data En cr ypted for Imp act
T1491: Defacement
T1489: Ser vice Stop
T1657: Financial Theft
T1490: Inhibit System Recovery
T1485: Data Destructio n
T1496: Resou rce Hijacking
T1529: Sy stem Shu tdown/Reboot

v17

35

Insights for Indonesia

Organised  crime  groups  are  the  dominant  threat  groups  targeting  Indonesia.  Hacktivists
threat  groups  are  observed  to  have  increased  targeting  on  Indonesia  as  well.  Hacktivists
have  been  observed  to  continue  their  attacks  on  different  industries  in  Indonesia  with  the
motivation to increase the awareness of cybersecurity (and privacy) amongst businesses and
the public sector.
Cyber-attacks by state-sponsored threat groups are interested in espionage for information
leverage  on  geopolitical  and  trade  oriented  advantages.  The  targeting  of  the  public  sector
industry  group  can  be  attributed  by  the  collective  interest  from  hacktivists  and  state-
sponsored threat groups.
Technology companies’ interest to build out data centres and provide technology services in
Indonesia, coupled by the public sector’s increased desire for greater digital penetration into
the population, have driven the TMT industry group to be the second highest targeted industry
group.
Hospitality  is  new  to  the  top  targeted  industry  group,  which  could  be  due  to  increased
interest  by  threat  actors  in  performing  surveillance  on  politically  exposed  persons,  arising
from  the  elections.  Interest  in  the  defence  &  law  enforcement  industry  group  could  have
arisen  due  to  the  increased  interest  in  defence  activities  arising  from  geopolitical  tensions
relating to the South China Sea.
Bjorka and ETHERSEC Team Cyber are hacktivist groups which have publicly shamed public
sector’s  efforts  in  cyber  defence  as  one  of  their  key  motivations.  They  claimed  that  their
efforts have helped to raise awareness for the cybersecurity industry to improve.

KEY TAKEAWAYS

• Organised crime groups are the
most representative threat group
targeting Indonesia.

• Hacktivism continues to be
prominent in Indonesia.

•

Top targeted industry groups are
respectively Public Sector, TMT,
and Hospitality.

• Hospitality and Defence & Law

Enforcement are newly observed
top targeted industry groups.

•

Top notable cyber-attack effects
are respectively Denial of
Service, Data Breach, and
Defacement.

• Hacktivists targeting Indonesia
are mostly focussed on the
Public Sector with expressed
interest at driving the awareness
of the perceived lack of cyber
defences across the country.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

36

South Korea

KEY ANALYSIS INSIGHTS

ENSIGN THREAT
CLASSIFICATION
MATRIX

NIL

• Kill Ransomware

NIL

• LockBit Gang • TIDRONE
• State-sponsored Threat
Groups

→→→ Increasing levels of threat to the subject →→→

Insubstantial

Potential

Impending

Material

Capability

Intent

Opportunity

●

●

●

●

●

●

●

●

●

MOST AFFECTED INDUSTRY GROUPS

TOP NOTABLE cyber-attack EFFECTS OBSERVED

The following observations are based on Ensign Proprietary Data and Cyber
Threat Intelligence data. Sorted in alphabetical order

Banking, Finance
& Insurance

Public Sector

Denial of Service

84.4%

Techniques of Concern

TA0001: Initial Access
▪
T1566: Ph ishing
▪
T1078: Valid Acco unts
▪
T1189: Dr ive-by Compromise
▪
T1190: Exp loit Public-Facing Application
▪
T1133: Exter nal Remote Services
▪
T1199: Trusted  Relationship
▪
T1091: Replication Thr ough  Removab le Media
▪
T1195: Su pply  Chain Compromise
▪
T1669: Wi-Fi Networ ks

TA0011: Command and Control
▪
T1071: Application Lay er Protocol
▪
T1102: Web  Service
▪
T1090: Pr oxy
▪
T1132: Data En co ding
▪
T1001: Data Obfuscation
▪
T1573: Encry pted Chan nel
▪
T1105: Ingress Tool Transfer
▪
T1219: Remote Access Too ls
▪
T1092: Communication  Throu gh Removable Media
▪
T1008: Fallback Channels
▪
T1104: Mu lti-Stage Chan nels
▪
T1571: Non-Application Lay er Protocol
▪
T1571: Non-Stan dard Por t
▪
T1572: Pr otocol Tunnellin g
▪
T1205: Traffic Signalling

TA0010: Exfiltration
▪
▪
▪
▪

T1567: Exfiltration  Over  W eb Service
T1048: Exfiltration  Over  Alter native Pro tocol
T1041: Exfiltration  Over  C2 Chan nel
T1030: Data Transfer  Size Limits

Aviation

TMT

Transport

New affected industries observed in 2024

Data Breach

Ransom
Initial Access

Data Leak

TA0040: Impact
▪
▪
▪
▪
▪
▪
▪
▪
▪

T1561: Disk W ipe
T1491: Defacement
T1485: Data Destructio n
T1489: Ser vice Stop
T1529: Sy stem Shu tdown/Reboot
T1486: Data En cr ypted for Imp act
T1657: Financial Theft
T1490: Inhibit System Recovery
T1498: Netwo rk Den ial of Serv ice

6.4%

2.9%
2.3%

2.3%

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

37

Insights for South Korea

State-sponsored  threat  groups  are  actively  targeting  South  Korea  with  significant  interest
from  neighbouring  countries  on  (i)  the  political  and  civil  situation,  (ii)  the  geopolitical
alliances, (iii) industry development (particularly in semiconductors), (iv) North Koreans and
human rights activists resident in South Korea.

With the ongoing trade discussions, state-sponsored threat groups may also be interested to
gain information leverage through espionage.

The  most  notable  targeting  outside  of  industry  groups  is  the  civilian  population,  with
observed  surveillance  interests  in  South  Korea,  especially  from  the  number  of  malicious
mobile apps targeted at the residents.

The  targeting  of  public  sector,  BFI  and  TMT  industry  groups  are  respectively  due  to  (i)
geopolitical interests, (ii) financial gain, and (iii) leveraging vendors to gain access to targeted
victims.

Thematically, the elections in South Korea and the global trade tensions, particularly relating
to semiconductor manufacturing, drew threat actors’ interests in targeting the public sector
and TMT industry groups.

The  transport  and  aviation  industry  groups  were  newly  observed  top  targeted  industry
groups. The aviation incident may have also contributed to additional opportunities for threat
actors targeting.

Denial  of  Service  is  predominant  in  the  cyber-attack  effects,  which  is  aligned  to  the
significant targeting from state-sponsored threat groups with interests in disrupting services.
Data Breach is directly related to espionage related activities.

KEY TAKEAWAYS

•

•

•

•

•

•

State-sponsored threat groups
are the most representative threat
group targeting South Korea.

There are no observed
hacktivism-related activities.

Top targeted industry groups are
respectively Public Sector, BFI,
TMT.

Transport and Aviation are newly
observed top targeted industry
groups.

The civilian population is
targeted for surveillance
objectives.

Top notable cyber-attack effects
are respectively Denial of
Service, Data Breach, and
Ransom.

• Notable that threat actors exploit

Threat actors have also adapted their TTPs to exploit commonly used local applications such
as Kingsoft WPS Office and local mobile applications.

commonly used local
applications

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

38

Australia

KEY ANALYSIS INSIGHTS

ENSIGN THREAT
CLASSIFICATION
MATRIX

NIL

• FIN7 • RipperSec
• Kill Ransomware • RansomHub

• FIN11

• Akira • LockBit Gang • Qilin Ransomware
• Sarcoma Ransomware • State-
sponsored Threat Groups

Insubstantial

Potential

Impending

Material

→→→ Increasing levels of threat to the subject →→→

Capability

Intent

Opportunity

●

●

●

●

●

●

●

●

●

MOST AFFECTED INDUSTRY GROUPS

TOP NOTABLE cyber-attack EFFECTS OBSERVED

The following observations are based on Ensign Proprietary Data and Cyber
Threat Intelligence data. Sorted in alphabetical order

Banking, Finance
& Insurance

Public Sector

Denial of Service

58%

v17

Techniques of Concern

TA0001: Initial Acc ess
▪
T1566: Ph ishing
▪
T1078: Valid Acco unts
▪
T1190: Exp loit Public-Facing Application
▪
T1133: Exter nal Remote Services
▪
T1195: Su pply  Chain Compromise
▪
T1199: Trusted  Relationship
▪
T1189: Dr ive-by Compromise
▪
T1091: Replication Thr ough  Removab le Media

TA0011: Com mand and Control
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪

T1071: Application Lay er Protocol
T1090: Pr oxy
T1573: Encry pted Chan nel
T1102: Web  Service
T1001: Data Obfuscation
T1105: Ingress Tool Transfer
T1568: Dy namic Resolu tion
T1219: Remote Access Too ls
T1095: Non-Application Lay er Protocol
T1132: Data En co ding
T1008: Fallback Channels
T1571: Non-Stan dard Por t
T1665: Hide In fr astructur e
T1104: Mu lti-Stage Chan nels
T1572: Pr otocol Tunnellin g

TA0010: Exfiltration
▪
▪
▪
▪
▪
▪

T1567: Exfiltration  Over  W eb Service
T1048: Exfiltration  Over  Alter native Pro tocol
T1041: Exfiltration  Over  C2 Chan nel
T1011: Exfiltration  Over  Other  Network M edium
T1030: Data Transfer  Size Limits
T1537: Transfer Data to  Clo ud Account

Aviation

TMT

Transport

New affected industries observed in 2025

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

Data Breach

Ransom

Defacement

Data Leak

13.7%

13%

6.9%

3.1%

TA0040: Impact
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪

T1486: Data En cr ypted for Imp act
T1491: Defacement
T1561: Disk W ipe
T1490: Inhibit System Recovery
T1489: Ser vice Stop
T1485: Data Destructio n
T1499: End point Den ial of Serv ice
T1657: Financial Theft
T1498: Netwo rk Den ial of Serv ice
T1496: Resou rce Hijacking
T1529: Sy stem Shu tdown/Reboot

39

Insights for Australia

Organised crime groups are actively targeting Australia, pursuing financial gain and causing
disruptions, through Ransomware attacks and data breaches with threats of ransom.

Both state-sponsored threat groups and hacktivist activities targeting Australia have risen.
State-sponsored threat groups activities may be attributed to the rising geopolitical tensions
and  increased  interest  in  the  geopolitical influences  in  the South  China  Sea  and the  Pacific
Islands.  Trade  tensions  are  also  leading  to  increased  interests  to  perform  espionage  for
information leverage in negotiations. The rise of hacktivists targeting could be attributed to
perceived support to parties in the Middle East conflicts.

The  targeting  of  the  public  sector  is  focussed  on  foreign  relations  and  trade,  which
predominantly  are  due  to  espionage  interests.  Some  of  the  targeting  on  the  public  sector
industry  group is attributed  to hacktivists’  displeasure  on  Australia’s  position  regarding  the
Middle East conflicts.

The targeting of TMT is correlated with the intention of threat groups interested in leveraging
its  position  as  digital  infrastructure  to  gain  access  to  a  wider  group  of  targets  through  the
cyber  supply  chain,  and  the  industry  group’s  potential  as  data  processors  for  high  value
information such as personal data and financial transactions. The BFI industry group usually
attracts threat groups motivated by financial gain by exploiting the collection of personal data
and credit information.

The  new  targeting  of  transport  and  aviation  is  noteworthy  as  Australia  is  a  key  trade  and
logistics  hub  for  the  South  Pacific.  Disruption  to  these  industry  groups  can  detrimentally
impact trade, logistics and transportation in the region.

KEY TAKEAWAYS

• Organised crime groups are the
most representative threat group
targeting Australia.

•

•

•

Top targeted industry groups are
respectively Public Sector, TMT,
and BFI.

Transport and Aviation are newly
observed top targeted industry
groups.

Top notable cyber-attack effects
are respectively Denial of
Service, Data Breach, and
Ransom.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

40

Greater China Region

KEY ANALYSIS INSIGHTS

ENSIGN THREAT
CLASSIFICATION
MATRIX

NIL

• DragonForce Ransomware
• Kill Ransomware
• LockBit Gang

NIL

• BITTER • Blackwood
• Bronze Highland • Pseudo Hunter
•  Void Arachne • State-sponsored Threat
Groups

Insubstantial

Potential

Impending

Material

→→→ Increasing levels of threat to the subject →→→

Capability

Intent

Opportunity

●

●

●

●

●

●

●

●

●

MOST AFFECTED INDUSTRY GROUPS

TOP NOTABLE cyber-attack EFFECTS OBSERVED

The following observations are based on Ensign Proprietary Data and Cyber
Threat Intelligence data. Sorted in alphabetical order

Healthcare

Public Sector

Banking, Finance &
Insurance

TMT

Transport

New affected industries observed in 2024

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

Data Breach

41.7%

Initial Access

Data Leak

Ransom

Denial of Service

15.2%

15.2%

12.1%

8.3%

v17

Techniques of Concern

TA0001: Initial Acc ess
▪
T1566: Ph ishing
▪
T1189: Dr ive-by Compromise
▪
T1078: Valid Acco unts
▪
T1190: Exp loit Public-Facing Application
▪
T1133: Exter nal Remote Services
▪
T1091: Replication Thr ough  Removab le Media
▪
T1195: Su pply  Chain Compromise
▪
T1199: Trusted  Relationship

TA0011: Com mand and Control
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪

T1071: Application Lay er Protocol
T1102: Web  Service
T1132: Data En co ding
T1573: Encrypted Chan nel
T1105: Ingress Tool Transfer
T1090: Pr oxy
T1001: Data Obfuscation
T1095: Non-Application Lay er Protocol
T1571: Non-Stan dard Por t
T1219: Remote Access Too ls
T1572: Pr otocol Tunneling
T1568: Dy namic Resolu tion
T1008: Fallback Channels
T1665: Hide In fr astructur e
T1104: Mu lti-Stage Chan nels
T1205: Traffic Signaling

TA0010: Exfiltration
▪
▪
▪
▪
▪
▪

T1048: Exfiltration  Over  Alter native Pro tocol
T1567: Exfiltration  Over  W eb Service
T1041: Exfiltration  Over  C2 Chan nel
T1020: Automated Exfiltration
T1052: Exfiltration  Over  Physical Medium
T1030: Data Transfer  Size Limits

TA0040: Impact
▪
▪
▪
▪
▪
▪
▪
▪
▪

T1491: Defacement
T1561: Disk W ipe
T1485: Data Destructio n
T1486: Data En cr ypted for Imp act
T1490: Inhibit System Recovery
T1489: Ser vice Stop
T1657: Financial Theft
T1498: Netwo rk Den ial of Serv ice
T1529: Sy stem Shu tdown/Reboot

41

Insights for Greater China Region

Organised  crime  groups  are  the  predominant  threat  group  targeting  the  Greater  China
Region, motivated by the rising prominence of the financial hubs in the region, especially with
its  position  as  the  second  largest  economy.  Many  of  these  threat  groups  uniquely  operate
within the GCR.

State-sponsored threat groups interest in the region are attributed to the rising influence the
region  plays  in  geopolitics  and  global  trade,  with  these  threat  groups  interested  to  gain
information leverage for negotiations.

The  targeting  of  the  TMT  can  be  attributed  to  the  observed  rise  of  developments  in  the
region’s  semiconductor  industry,  artificial  intelligence  (AI)  related  companies  and  the
significance  of  their  capabilities,  e.g.,  the  “DeepSeek  moment”,  and  also,  the  attention  on
social  media  platforms  and  their  perceived  role  in  influence  operations.  The  industry  group
also provides access to a wide range of digital businesses and avails disruption opportunities
to threat actors.

The  BFI  industry  group  attracts  the  financially  motivated  threat  groups  and  threat  groups
interested  to  understand  how  the  economy  is  structured  or  organised  to  respond  to  global
economic changes. This is especially due to the rising global concerns on the health of the
second  largest  economy  and  if  there  are  opportunities  for  threat  actors  to  leverage  the
situation. The targeting of the public sector industry group is attributed to interests relating
to geopolitics, trade, and human rights matters.

is  related  to  the  rising  prominence  of  the  region’s  role

The  newly  observed  targeting  of  the  healthcare  sector  may  be  due  to  continued  interests
relating  to  the  region’s  role  in  addressing  the  Covid-19  pandemic,  and  how  it  is  preparing
against  more  frequent  waves  of  illnesses  across  the  region.  The  targeting  of  the  transport
sector
in  electric  vehicles
manufacturing and the electric charging infrastructure build out. Additionally, the completion
of  major  rail  and  road  infrastructure  networks  associated  with  the  Belt  and  Road  initiative
continues to draw attention from threat groups looking to benefit from it, whether for financial
gain or information.

KEY TAKEAWAYS

• Organised crime groups are the
most representative threat group
targeting the Greater China
Region.

•

•

There are no observed
hacktivism-related activities.

Top targeted industry groups are
respectively TMT, BFI, and Public
Sector.

• Healthcare and Transport are

newly observed the top targeted
industry groups.

•

Top notable cyber-attack effects
are respectively Data Breach,
Initial Access, and Data Leak.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

42

Outlook of Cyber Threats for 2025

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

43

Outlook of Cyber Threats for 2025

Ransomware experimentation
and consolidation will continue
with increased collaboration

• Ransomware groups which refactor/fork leaked
Ransomware source codes and playbook will
emerge and adapt to determine if they are viable
operations. If found lacking sustainability and
competency in operations and security, they will
collapse or be consolidated.

• Capability enhancements to evade or impair

defences will continue with experimentation and
collaboration in the underground economy, leading
to rising efficacy of compromise.

Organisations should continue to adopt multi-pronged
and multi-layered defences (e.g., Zero Trust
Architecture principles) and ensure defence solutions
are competent and updated.

State-sponsored threat
groups will overtly
create effects for
geopolitical leverage

• Continued adjustments of pre-

positioning and chosen effects of
cyber-attacks may be leveraged for
geo-political and trade
negotiations.

• Systemic implications are to be
expected from such effects on
peripheral organisations through
the connected cyber supply chain.

Incident frequency will rise due
to rising technology
environment complexities

•

The already complex mix and variety of technologies
implemented in organisations, incomplete asset
inventory records and monitoring, and the lag
between vulnerability discovery and patching will
exacerbate vulnerabilities exposure windows, due
to implementation and integration.

• Vulnerabilities (reported and unknown) will

continue to be exploited by threat actors, with rising
frequencies, and increasing patching debt in
organisations.

Organisations will do well to
progressively collaborate and work
with authorities to leverage collective
defence opportunities

Practise threat-informed vulnerability prioritisation and
accelerate patching with solutions for virtual patching
and automatic patch deployments to reduce
vulnerability exposure windows.

Complex cyber supply chains and redrawing
of suppliers will elevate cyber supply chain
compromise risks

•

•

Trade tensions are forcing organisations to rethink and
rearrange their supply chains, including digital ones.

In the transition from the current state to a new one,
vulnerabilities will occur, across vendors, hardware and
software dimensions of the cyber supply chain, elevating cyber
supply chain compromise risks.

Perform inventory of the cyber supply chain (hardware, software and
vendors) and coupling it with deliberate threat intelligence analysis
to proactively monitor for impending vulnerabilities and risks from
supply chain compromise.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

Accelerated AI adoption and absence of security
solutions for AI will lead to more data leaks

• Security solutions for AI are not adapting fast enough to address the rapid

experimentation of AI technologies and the iteration of use cases by
organisations.

• Unfettered access to data repositories in organisations for AI will cause entity -

oriented exposure of datasets.

• Data security oriented solutions, while fundamental, may not be flexible enough
to help organisations balance AI exploitation from risk management, leading to
the control gap, leading to a potential rise in data leaks.

Implement UEBA solutions and tighten identity access controls on entities and
services. Establish data security controls, prioritising sensitive datasets.

Defensive Actions for Cyber Defenders and Leaders

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

45

Defensive Actions for Cyber Defenders & Leaders

Based on the compiled adversarial techniques observed in 2024, we identified the essential defensive measures and detection d ata sources
that organisations can adopt to mitigate risks in Initial Access, Command and Control, Exfiltration, and Impact tactics as ou tlined in the
MITRE ATT&CK  framework.

The thematic defence strategies highlighted below centres on the crucial necessity for consistent monitoring across the digit al attack
surface, and integrating cyber threat intelligence analysis to embrace a threat-informed approach, especially in responding to impending
and material threats.

Ensure that KRIs are tied to threats and mapped
to security monitoring measurements

Rehearse, drill and practice all incident-to-crisis processes to
build up readiness and resilience in cyber defence

Review/revise key risk indicators (KRIs) based in threat-informed
scenarios and ensure that the KRIs are mapped to security monitoring
indicators.

Establish a programme to regularly familiarise, train and build confidence (and capacity) in the
personnel and leaders to be able to respond and recover from cyber -related incidents and
crisis, ensuring that all functional teams coordinate and collaborate to navigate the situation.

Prepare for selected KRIs to be updated on high frequency during
incidents to support decision making during incidents and crises.

Evaluate the sufficiency of resources and shifts to support these processes.

Adopt the 3-2-1-1
backup, archival and
recovery strategy

Ensure that the organisation has
3 copies of data backups, in two
separate mediums, with at least
one kept in a remote, offline and
immutable form to be resilient to
Ransomware attacks.

Enhance the chances of recovery
by preparing for Golden Images
to allow for full rebuild of
systems from the last known
good state.

Enhance Asset Inventory
and Monitoring
Coverage, Leveraging
Threat Intelligence

Review and harden
configurations of systems
and platforms, including key
user interaction interfaces

Integrate incident response
plans to crisis management
plans, ensuring whole-of-
organisation coordination

Progressively complete the asset
inventory, ensuring as comprehensive
a coverage for cybersecurity monitoring
as possible, leveraging threat
intelligence to proactively monitor/hunt
for impending threats.

Leverage automation and artificial
intelligence to scale up monitoring
efficacy, focussed on adversarial
behaviours, e.g., TTPs.

Review the configurations of systems and
services (including Cloud, hypervisor and
container services and solutions)
ensuring that authentication and access
controls are restricted appropriately and
unsafe or unnecessary services and
features are disabled.

Pay attention to hypervisors, container
infrastructure, web browsers, email
applications and network devices, as they
are often exploited for access and
persistence.

Success in addressing incidents and
cyber-related crisis requires
multifunctional teams across the
organisation to coordinate and
collectively address the situation,
including crisis communications,
stakeholder engagements, reporting,
digital forensics, business continuity
management and disaster recovery.

Collaborate with industry and regulators
to bolster collective defence outcomes.

46

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

Mitigation(s)

Detection Log Source(s)

Technique
TA0001: Initial Access

T1566: Phishing

T1078: Valid Accounts

T1190: Exploit Public-Facing Application

T1133: External Remote Services

T1195: Supply Chain Compromise

T1199: Trusted Relationship

T1189: Drive-by Compromise

T1091: Replication Through Removable Media

T1659: Content Injection

T1669: Wi-Fi Networks

M1049: Antivirus/Antimalware
M1047: Audit
M1031: Network Intrusion Prevention
M1021: Restrict Web-Based Content
M1054: Software Configuration
M1017: User Training
M1036: Account Use Policies
M1015: Active Directory Configuration
M1013: Application Developer Guidance
M1032: Multi-factor Authentication
M1027: Password Policies
M1026: Privileged Account Management
M1018: User Account Management
M1017: User Training
M1048: Application Isolation and Sandboxing
M1050: Exploit Protection
M1035: Limit Access to Resource Over Network
M1030: Network Segmentation
M1026: Privileged Account Management
M1051: Update Software
M1016: Vulnerability Scanning
M1042: Disable or Remove Feature or Program
M1035: Limit Access to Resource Over Network
M1032: Multi-factor Authentication
M1030: Network Segmentation

M1013: Application Developer Guidance
M1046: Boot Integrity
M1033: Limit Software Installation
M1051: Update Software
M1018: User Account Management
M1016: Vulnerability Scanning
M1032: Multi-factor Authentication
M1030: Network Segmentation
M1018: User Account Management

M1048: Application Isolation and Sandboxing
M1050: Exploit Protection
M1021: Restrict Web-Based Content
M1051: Update Software
M1017: User Training
M1040: Behavior Prevention on Endpoint
M1042: Disable or Remove Feature or Program
M1034: Limit Hardware Installation

M1041: Encrypt Sensitive Information
M1021: Restrict Web-Based Content

M1041: Encrypt Sensitive Information
M1032: Multi-factor Authentication
M1030: Network Segmentation

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

DS0015: Application Log
DS0022: File
DS0029: Network Traffic

DS0028: Logon Session
DS0002: User Account

DS0015: Application Log
DS0029: Network Traffic

DS0015: Application Log
DS0028: Logon Session
DS0029: Network Traffic

DS0015: Application Log
DS0028: Logon Session
DS0029: Network Traffic

DS0015: Application Log
DS0022: File
DS0029: Network Traffic
DS0009: Process

DS0016: Drive
DS0022: File
DS0009: Process

DS0022: File
DS0029: Network Traffic
DS0009: Process
DS0018: Firewall
DS0029: Network Traffic

DS0022: File
DS0013: Sensor Health

•

Organisations should consider the following to address the key
Initial Access techniques:

•

•

Enforce strong password policies, implement multi-factor
authentication (MFA), regularly review and monitor user
account activity to detect unauthorised access, and promptly
revoke access for terminated employees to mitigate the risk of
account compromise.

Educate employees on identifying and avoiding phishing
attempts, raise awareness about the risks associated with
external threats and trusted relationships, and provide regular
security training to promote a culture of security awareness
within the organisation.

• Regularly scan and patch public-facing applications for

vulnerabilities, implement secure coding practices, employ
web application firewalls (WAFs) to filter and monitor
incoming traffic, and conduct regular security assessments and
penetration testing to detect and remediate potential exploits.

• Regularly update and patch external-facing systems, employ
strong authentication mechanisms for remote access, and
implement firewalls and intrusion detection/prevention
systems to monitor and defend against external threats.

Establish vendor risk management programs to assess and
monitor the security posture of third-party vendors and
partners, including those within the supply chain, to mitigate
the risk of supply chain compromises and ensure that trusted
relationships do not introduce security vulnerabilities.

• Restrict the use of removable media devices such as USB

drives and ensure that only authorised and encrypted devices
are permitted. Implement endpoint protection solutions to scan
and block potentially malicious files from removable media to
prevent replication through these devices.

• Maintain updated browsers, enforce script-blocking plugins or
content security policies (CSP), and educate users to avoid
suspicious links to reduce exposure to drive-by download
attacks. Implement URL filtering and DNS-based protections to
block access to known malicious sites.

• Apply WPA3 or strong WPA2 encryption for Wi-Fi networks,
segment wireless access from critical internal resources,
implement MAC address filtering and wireless IDS, and disable
SSID broadcasting for sensitive networks to limit exposure to
unauthorized access.

47

Technique
TA0011: Command and Control

T1071: Application Layer Protocol

T1090: Proxy

T1573: Encrypted Channel

T1001: Data Obfuscation

T1219: Remote Access Tools

T1102: Web Service

T1105: Ingress Tool Transfer

T1095: Non-Application Layer Protocol

T1568: Dynamic Resolution

T1665: Hide Infrastructure

T1572: Protocol Tunnelling

T1008: Fallback Channels
T1104: Multi-Stage Channels

T1571: Non-Standard Port

T1132: Data Encoding

T1659: Content Injection

Mitigation(s)

Detection Log Source(s)

M1037: Filter Network Traffic
M1031: Network Intrusion Prevention
M1037: Filter Network Traffic
M1031: Network Intrusion Prevention
M1020: SSL/TLS Inspection
M1031: Network Intrusion Prevention
M1020: SSL/TLS Inspection
M1031: Network Intrusion Prevention
M1042: Disable or Remove Feature or Program
M1038: Execution Prevention
M1037: Filter Network Traffic
M1034: Limit Hardware Installation
M1031: Network Intrusion Prevention
M1031: Network Intrusion Prevention
M1021: Restrict Web-Based Content

M1031: Network Intrusion Prevention
M1047: Audit
M1037: Filter Network Traffic
M1031: Network Intrusion Prevention
M1030: Network Segmentation
M1031: Network Intrusion Prevention
M1021: Restrict Web-Based Content

-
M1037: Filter Network Traffic
M1031: Network Intrusion Prevention
M1031: Network Intrusion Prevention
M1031: Network Intrusion Prevention
M1031: Network Intrusion Prevention
M1030: Network Segmentation
M1031: Network Intrusion Prevention

M1041: Encrypt Sensitive Information
M1021: Restrict Web-Based Content

DS0029: Network Traffic

DS0029: Network Traffic

DS0029: Network Traffic
DS0029: Network Traffic

DS0016: Drive
DS0029: Network Traffic
DS0009: Process

DS0029: Network Traffic
DS0017: Command
DS0022: File
DS0029: Network Traffic

DS0029: Network Traffic

DS0029: Network Traffic
DS0038: Domain Name
DS0035: Internet Scan
DS0029: Network Traffic

DS0029: Network Traffic
DS0029: Network Traffic
DS0029: Network Traffic

DS0029: Network Traffic
DS0029: Network Traffic
DS0022: File
DS0029: Network Traffic
DS0009: Process

DS0016: Drive

DS0029: Network Traffic

DS0029: Network Traffic
DS0009: Process

DS0029: Network Traffic

Organisations should consider the following to address the key
Command and Control techniques:

•

•

Implement robust data loss prevention (DLP) solutions and
conduct regular audits to detect and prevent data obfuscation.

Enforce strict controls on removable media usage and
employ endpoint protection solutions to scan and block
communication through such channels.

• Utilise application layer firewalls and intrusion

detection/prevention systems to detect and block malicious
activities exploiting application layer protocols.

• Deploy proxy solutions with advanced threat detection
capabilities to identify and block unauthorised traffic.

•

Implement network segmentation and access controls to
mitigate lateral movement through non-application layer
protocols and web services.

• Monitor network traffic for anomalies and indicators of

compromise and restrict the use of remote access software to
authorised personnel.

•

•

Employ dynamic resolution techniques and regularly audit
network configurations to detect and mitigate the use of non-
standard ports and protocol tunnelling.

Ensure encryption of communication channels to protect
sensitive data.

• Conduct regular security awareness training for employees

to recognise and report suspicious activities, including
potential content injection attempts.

•

Implement deception technologies or monitoring for fallback
and multi-stage channels to identify staged or backup
communications used by threat actors.

• Apply infrastructure hiding detection measures such as
monitoring for fast-flux DNS or use of bulletproof hosting
providers to identify potential covert C2 infrastructure.

T1092: Communication Through Removable Media

T1571: Non-Application Layer Protocol

T1205: Traffic Signalling

T1572: Protocol Tunneling

M1042: Disable or Remove Feature or Program
M1028: Operating System Configuration
M1047: Audit
M1037: Filter Network Traffic
M1031: Network Intrusion Prevention
M1030: Network Segmentation

M1042: Disable or Remove Feature or Program
M1037: Filter Network Traffic
M1037: Filter Network Traffic
M1031: Network Intrusion Prevention

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

48

Technique
TA0010: Exfiltration

T1567: Exfiltration Over Web Service

T1048: Exfiltration Over Alternative Protocol

T1041: Exfiltration Over C2 Channel

T1011: Exfiltration Over Other Network Medium

T1052: Exfiltration Over Physical Medium

T1030: Data Transfer Size Limits

T1537: Transfer Data to Cloud Account

T1567:Exfiltration Over Web Service

T1048: Exfiltration over Alternative Protocol

T1041 Exfiltration Over C2 Channel

Mitigation(s)

Detection Log Source(s)

M1057: Data Loss Prevention
M1021: Restrict Web-Based Content

M1057: Data Loss Prevention
M1037: Filter Network Traffic
M1031: Network Intrusion Prevention
M1030: Network Segmentation
M1022: Restrict File and Directory
Permissions
M1018: User Account Management

M1057: Data Loss Prevention
M1031: Network Intrusion Prevention

M1042: Disable or Remove Feature or
Program
M1028: Operating System Configuration

M1057: Data Loss Prevention
M1042: Disable or Remove Feature or
Program
M1034: Limit Hardware Installation

M1031: Network Intrusion Prevention
M1057: Data Loss Prevention
M1037: Filter Network Traffic
M1054: Software Configuration
M1018: User Account Management

M1057: Data Loss Prevention
M1021: Restrict Web-Based Content

M1057: Data Loss Prevention
M1037: Filter Network Traffic
M1031: Network Intrusion Prevention
M1030: Network Segmentation
M1022: Restrict File and Directory
Permissions
M1018: User Account Management

M1057: Data Loss Prevention
M1031: Network Intrusion Prevention

DS0015: Application Log
DS0017: Command
DS0022: File
DS0029: Network Traffic

DS0015: Application Log
DS0010: Cloud Storage
DS0017: Command
DS0022: File
DS0029: Network Traffic

DS0017: Command
DS0022: File
DS0029: Network Traffic

DS0017: Command
DS0022: File
DS0029: Network Traffic

DS0017: Command
DS0016: Drive
DS0022: File
DS0009: Process

DS0029: Network Traffic
DS0015: Application Log
DS0010: Cloud Storage
DS0029: Network Traffic
DS0020: Snapshot

DS0015: Application Log
DS0017: Command
DS0022: File
DS0029: Network Traffic

DS0015: Application Log
DS0010: Cloud Storage
DS0017: Command
DS0022: File
DS0029: Network Traffic

DS0017: Command
DS0022: File
DS0029: Network Traffic

Organisations should consider the following to address the key
Exfiltration techniques:

•

•

•

Implement robust network monitoring solutions capable of
detecting anomalous data transfer patterns indicative of
automated exfiltration.

Enforce data transfer size limits to prevent large-scale
exfiltration attempts and implement alerting mechanisms for
unusual data transfer volumes.

Employ intrusion detection/prevention systems (IDPS) to
detect and block exfiltration over command-and-control (C2)
channels, and regularly update signatures to identify emerging
threats.

• Monitor network traffic for suspicious activity indicative of
exfiltration over alternative protocols, such as DNS or ICMP,
and deploy deep packet inspection (DPI) solutions to identify
and block unauthorised data transfers.

•

Implement strict access controls and encryption
mechanisms for web service interactions to prevent
unauthorised data exfiltration via cloud or API-based platforms.

• Restrict or monitor the use of physical media, such as USB
drives and external hard disks, and apply data loss prevention
(DLP) solutions to prevent unauthorised physical exfiltration.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

49

Technique
TA0040: Impact

T1486: Data Encrypted for Impact

Mitigation(s)

Detection Log Source(s)

M1040: Behavior Prevention on Endpoint
M1053: Data Backup

T1491: Defacement

M1053: Data Backup

M1053: Data Backup
M1038: Execution Prevention
M1028: Operating System Configuration
M1018: User Account Management

M1037: Filter Network Traffic

M1018: User Account Management
M1017: User Training
M1030: Network Segmentation
M1060: Out-of-Band Communications Channel
M1022: Restrict File and Directory Permissions
M1024: Restrict Registry Permissions
M1018: User Account Management

M1053: Data Backup
M1032: Multi-factor Authentication
M1018: User Account Management

M1037: Filter Network Traffic

M1053: Data Backup

-

T1490: Inhibit System Recovery

T1499: Endpoint Denial of Service

T1657: Financial Theft

T1489: Service Stop

T1485: Data Destruction

T1498: Network Denial-of-Service

T1561: Disk Wipe

T1496: Resource Hijacking

T1498: Network Denial of Service

M1037: Filter Network Traffic

T1529: System Shutdown/Reboot

-

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

DS0010: Cloud Storage
DS0017: Command
DS0022: File
DS0033: Network Share
DS0009: Process
DS0015: Application Log
DS0022: File
DS0029: Network Traffic
DS0010: Cloud Storage
DS0017: Command
DS0022: File
DS0009: Process
DS0019: Service
DS0020: Snapshot
DS0024: Windows Registry
DS0015: Application Log
DS0029: Network Traffic
DS0013: Sensor Health
DS0015: Application Log

DS0017: Command
DS0022: File
DS0009: Process
DS0019: Service
DS0024: Windows Registry

DS0010: Cloud Storage
DS0017: Command
DS0022: File
DS0007: Image
DS0030: Instance
DS0009: Process
DS0020: Snapshot
DS0034: Volume
DS0029: Network Traffic
DS0013: Sensor Health
DS0017: Command
DS0016: Drive
DS0027: Driver
DS0009: Process
DS0015: Application Log
DS0025: Cloud Service
DS0017: Command
DS0022: File
DS0029: Network Traffic
DS0009: Process
DS0013: Sensor Health
DS0029: Network Traffic
DS0013: Sensor Health
DS0017: Command
DS0009: Process
DS0013: Sensor Health

Organisations should consider the following to address the key
Impact techniques:

•

Implement regular, encrypted backups stored offline or in
immutable storage, and conduct restoration drills to ensure
rapid recovery in case of ransomware or destructive attacks.

• Deploy web application firewalls (WAFs) and content integrity
monitoring solutions to detect and prevent website defacement
attempts, and regularly audit exposed web assets.

•

•

Enforce endpoint protection with rollback capabilities,
disable unnecessary services, and restrict user privileges to
prevent attackers from stopping critical services.

Implement anti-DDoS measures, such as rate limiting, traffic
filtering, and cloud-based protection services, to mitigate both
endpoint and network-level denial-of-service attacks.

• Segment and monitor systems, enforce strict access

controls, and use behavioural analytics to detect anomalies
indicative of financial fraud or theft.

• Apply strict controls on disk management utilities and
monitor for signs of low-level disk modification to prevent
destructive operations like disk wiping.

• Monitor resource usage anomalies (e.g., high CPU/GPU load)

and implement policy controls to detect and prevent
unauthorized cryptocurrency mining or resource abuse.

• Apply restrictions on user-initiated system

shutdown/reboot permissions and monitor for unauthorised
commands that may disrupt availability.

50

Contributors

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

51

ENSIGN ATHENA
THREAT INTELLIGENCE
ANALYSIS TEAM

ENSIGN SECURITY
OPERATIONS
CENTRES (ENSOCS)

ENSIGN LABS

Performs threat research and analysis
for predictive measures to detect
advanced cyber threats, to safeguard
critical assets of enterprises and the
public sector. We adopt a threat-
informed defence approach and apply
all-source intelligence to improve our
clients’ prioritisation of risks and
defensive actions.

Are located across APAC, in Singapore,
Malaysia, and Hong Kong. We offer
advanced detection and response
services, round-the-clock, to detect
and mitigate threats in all
environments of on-premise IT, Cloud,
OT, and IoT.

Generates insights from analysing
proprietary large volume datasets
relating to telemetry in the region,
coupled with vulnerability intelligence
and tradecraft, to support discovery of
Early Warning Indicators (EWIs).v

ENSIGN HUNT AND
INCIDENT RESPONSE
OPERATIONS (HIRO) TEAM

ENSIGN EXECUTIVE
ADVISORS

Performs threat hunting, and digital
forensics and incident response
(DFIR). Our operations are supported
by threat intelligence and leverage our
proprietary DFIR and continuous threat
hunting platforms, ARTEMIS and
APOLLO, to accelerate the
investigation-to-decision cycle to help
our clients minimise the business
impact of incidents.

Perform threat profiling for organisations,
sectors, and nations to uncover strategic
planning considerations, detections, and
mitigations to address “meet the threat”
objectives using the threat-informed
defence approach. Applying a multi-
disciplinary approach, they inform and
support Leaders and Management in
understanding the changes in the threat
landscape and how they affect their
business activities.

KEY CONTRIBUTORS
Non-exhaustive list,
alphabetical order

Au N.
Bach H.
Basedow A.
Burger S.
Kumaradasa W.
Lee J.
Li J.
Lim J.
Lim L.

Mok J.
Nugraputra A.
Rahumatulla S.
Seah M.
Sim WC.
Tan AT.
Tanadi J.
Teo XZ.
Yunus M.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

52

APPENDIX A
Techniques Heatmaps by Territory

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

53

Techniques heatmap for Singapore

Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/SG
SHA256 File Hash: 16266f2faebd154bd69efa603ed3f24b4b926b591f95bdb93159cbb1ca7cebc7

v17

Legend:

Increasing levels of observations

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

54

TA0043: ReconnaissanceTA0042: Resource DevelopmentTA0001: Initial AccessTA0002: ExecutionTA0003: PersistenceTA0004: Privilege EscalationTA0005: Defense EvasionTA0006: Credential AccessTA0007: DiscoveryTA0008: Lateral MovementTA0009: CollectionTA0011: Command and ControlTA0010: ExfiltrationTA0040: ImpactT1595: Active ScanningT1583: Acquire InfrastructureT1566: PhishingT1059: Command and Scripting InterpreterT1078: Valid AccountsT1078: Valid AccountsT1070: Indicator RemovalT1003: OS Credential DumpingT1087: Account DiscoveryT1021: Remote ServicesT1560: Archive Collected DataT1071: Application Layer ProtocolT1567: Exfiltration Over Web ServiceT1486: Data Encrypted for ImpactT1590: Gather Victim Network InformationT1588: Obtain CapabilitiesT1078: Valid AccountsT1053: Scheduled Task/JobT1053: Scheduled Task/JobT1053: Scheduled Task/JobT1027: Obfuscated Files or InformationT1555: Credentials from Password StoresT1069: Permission Groups DiscoveryT1550: Use Alternate Authentication MaterialT1074: Data StagedT1090: ProxyT1048: Exfiltration Over Alternative ProtocolT1491: DefacementT1589: Gather Victim Identity InformationT1587: Develop CapabilitiesT1190: Exploit Public-Facing ApplicationT1204: User ExecutionT1546: Event Triggered ExecutionT1546: Event Triggered ExecutionT1562: Impair DefensesT1110: Brute ForceT1082: System Information DiscoveryT1570: Lateral Tool TransferT1005: Data from Local SystemT1573: Encrypted ChannelT1041: Exfiltration Over C2 ChannelT1490: Inhibit System RecoveryT1596: Search Open Technical DatabasesT1584: Compromise InfrastructureT1133: External Remote ServicesT1569: System ServicesT1098: Account ManipulationT1098: Account ManipulationT1036: MasqueradingT1056: Input CaptureT1018: Remote System DiscoveryT1210: Exploitation of Remote ServicesT1056: Input CaptureT1001: Data ObfuscationT1011: Exfiltration Over Other Network MediumT1499: Endpoint Denial of ServiceT1593: Search Open Websites/DomainsT1586: Compromise AccountsT1195: Supply Chain CompromiseT1047: Windows Management InstrumentationT1547: Boot or Logon Autostart ExecutionT1547: Boot or Logon Autostart ExecutionT1218: System Binary Proxy ExecutionT1552: Unsecured CredentialsT1016: System Network Configuration DiscoveryT1072: Software Deployment ToolsT1213: Data from Information RepositoriesT1219: Remote Access ToolsT1052: Exfiltration Over Physical MediumT1657: Financial TheftT1591: Gather Victim Org InformationT1585: Establish AccountsT1199: Trusted RelationshipT1203: Exploitation for Client ExecutionT1133: External Remote ServicesT1574: Hijack Execution FlowT1078: Valid AccountsT1606: Forge Web CredentialsT1083: File and Directory DiscoveryT1091: Replication Through Removable MediaT1119: Automated CollectionT1102: Web ServiceT1030: Data Transfer Size LimitsT1489: Service StopT1598: Phishing for InformationT1608: Stage CapabilitiesT1189: Drive-by CompromiseT1072: Software Deployment ToolsT1574: Hijack Execution FlowT1548: Abuse Elevation Control MechanismT1553: Subvert Trust ControlsT1556: Modify Authentication ProcessT1497: Virtualization/Sandbox EvasionT1602: Data from Configuration RepositoryT1105: Ingress Tool TransferT1537: Transfer Data to Cloud AccountT1485: Data DestructionT1594: Search Victim-Owned WebsitesT1650: Acquire AccessT1091: Replication Through Removable MediaT1651: Cloud Administration CommandT1505: Server Software ComponentT1484: Domain or Tenant Policy ModificationT1574: Hijack Execution FlowT1558: Steal or Forge Kerberos TicketsT1057: Process DiscoveryT1114: Email CollectionT1095: Non-Application Layer ProtocolT1498: Network Denial of ServiceT1592: Gather Victim Host InformationT1129: Shared ModulesT1136: Create AccountT1055: Process InjectionT1480: Execution GuardrailsT1212: Exploitation for Credential AccessT1614: System Location DiscoveryT1113: Screen CaptureT1568: Dynamic ResolutionT1561: Disk WipeT1037: Boot or Logon Initialization ScriptsT1037: Boot or Logon Initialization ScriptsT1497: Virtualization/Sandbox EvasionT1621: Multi-Factor Authentication Request GenerationT1049: System Network Connections DiscoveryT1123: Audio CaptureT1665: Hide InfrastructureT1496: Resource HijackingT1543: Create or Modify System ProcessT1543: Create or Modify System ProcessT1548: Abuse Elevation Control MechanismT1040: Network SniffingT1046: Network Service DiscoveryT1572: Protocol TunnelingT1112: Modify RegistryT1068: Exploitation for Privilege EscalationT1484: Domain or Tenant Policy ModificationT1528: Steal Application Access TokenT1010: Application Window DiscoveryT1008: Fallback ChannelsT1556: Modify Authentication ProcessT1134: Access Token ManipulationT1055: Process InjectionT1649: Steal or Forge Authentication CertificatesT1482: Domain Trust DiscoveryT1104: Multi-Stage ChannelsT1542: Pre-OS BootT1550: Use Alternate Authentication MaterialT1539: Steal Web Session CookieT1518: Software DiscoveryT1571: Non-Standard PortT1197: BITS JobsT1140: Deobfuscate/Decode Files or InformationT1135: Network Share DiscoveryT1653: Power SettingsT1564: Hide ArtifactsT1120: Peripheral Device DiscoveryT1112: Modify RegistryT1012: Query RegistryT1222: File and Directory Permissions ModificationT1033: System Owner/User DiscoveryT1556: Modify Authentication ProcessT1007: System Service DiscoveryT1542: Pre-OS BootT1217: Browser Information DiscoveryT1014: RootkitT1654: Log EnumerationT1134: Access Token ManipulationT1040: Network SniffingT1197: BITS JobsT1124: System Time DiscoveryT1006: Direct Volume AccessT1673: Virtual Machine DiscoveryT1211: Exploitation for Defense EvasionT1656: ImpersonationT1599: Network Boundary BridgingTechniques heatmap for Malaysia

Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/MY
SHA256 File Hash: 916a9ff2df9368e57f662f1ef8031876eb84202a567d6f3e45948b1639d70358

v17

Legend:

Increasing levels of observations

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

55

TA0043: ReconnaissanceTA0042: Resource DevelopmentTA0001: Initial AccessTA0002: ExecutionTA0003: PersistenceTA0004: Privilege EscalationTA0005: Defense EvasionTA0006: Credential AccessTA0007: DiscoveryTA0008: Lateral MovementTA0009: CollectionTA0011: Command and ControlTA0010: ExfiltrationTA0040: ImpactT1595: Active ScanningT1588: Obtain CapabilitiesT1566: PhishingT1059: Command and Scripting InterpreterT1547: Boot or Logon Autostart ExecutionT1547: Boot or Logon Autostart ExecutionT1070: Indicator RemovalT1003: OS Credential DumpingT1082: System Information DiscoveryT1021: Remote ServicesT1560: Archive Collected DataT1071: Application Layer ProtocolT1567: Exfiltration Over Web ServiceT1491: DefacementT1590: Gather Victim Network InformationT1583: Acquire InfrastructureT1190: Exploit Public-Facing ApplicationT1053: Scheduled Task/JobT1574: Hijack Execution FlowT1574: Hijack Execution FlowT1027: Obfuscated Files or InformationT1110: Brute ForceT1614: System Location DiscoveryT1570: Lateral Tool TransferT1056: Input CaptureT1573: Encrypted ChannelT1048: Exfiltration Over Alternative ProtocolT1486: Data Encrypted for ImpactT1596: Search Open Technical DatabasesT1587: Develop CapabilitiesT1133: External Remote ServicesT1569: System ServicesT1053: Scheduled Task/JobT1053: Scheduled Task/JobT1562: Impair DefensesT1555: Credentials from Password StoresT1497: Virtualization/Sandbox EvasionT1550: Use Alternate Authentication MaterialT1005: Data from Local SystemT1102: Web ServiceT1041: Exfiltration Over C2 ChannelT1499: Endpoint Denial of ServiceT1593: Search Open Websites/DomainsT1586: Compromise AccountsT1195: Supply Chain CompromiseT1204: User ExecutionT1098: Account ManipulationT1098: Account ManipulationT1480: Execution GuardrailsT1056: Input CaptureT1087: Account DiscoveryT1210: Exploitation of Remote ServicesT1602: Data from Configuration RepositoryT1095: Non-Application Layer ProtocolT1030: Data Transfer Size LimitsT1498: Network Denial of ServiceT1598: Phishing for InformationT1199: Trusted RelationshipT1203: Exploitation for Client ExecutionT1546: Event Triggered ExecutionT1484: Domain or Tenant Policy ModificationT1574: Hijack Execution FlowT1040: Network SniffingT1083: File and Directory DiscoveryT1072: Software Deployment ToolsT1213: Data from Information RepositoriesT1090: ProxyT1489: Service StopT1594: Search Victim-Owned WebsitesT1078: Valid AccountsT1047: Windows Management InstrumentationT1133: External Remote ServicesT1546: Event Triggered ExecutionT1484: Domain or Tenant Policy ModificationT1018: Remote System DiscoveryT1074: Data StagedT1219: Remote Access ToolsT1490: Inhibit System RecoveryT1189: Drive-by CompromiseT1129: Shared ModulesT1505: Server Software ComponentT1548: Abuse Elevation Control MechanismT1553: Subvert Trust ControlsT1046: Network Service DiscoveryT1113: Screen CaptureT1001: Data ObfuscationT1485: Data DestructionT1072: Software Deployment ToolsT1136: Create AccountT1055: Process InjectionT1497: Virtualization/Sandbox EvasionT1135: Network Share DiscoveryT1123: Audio CaptureT1568: Dynamic ResolutionT1657: Financial TheftT1543: Create or Modify System ProcessT1543: Create or Modify System ProcessT1548: Abuse Elevation Control MechanismT1057: Process DiscoveryT1119: Automated CollectionT1105: Ingress Tool TransferT1496: Resource HijackingT1112: Modify RegistryT1078: Valid AccountsT1140: Deobfuscate/Decode Files or InformationT1012: Query RegistryT1104: Multi-Stage ChannelsT1529: System Shutdown/RebootT1542: Pre-OS BootT1134: Access Token ManipulationT1036: MasqueradingT1049: System Network Connections DiscoveryT1572: Protocol TunnelingT1078: Valid AccountsT1037: Boot or Logon Initialization ScriptsT1055: Process InjectionT1010: Application Window DiscoveryT1132: Data EncodingT1197: BITS JobsT1068: Exploitation for Privilege EscalationT1218: System Binary Proxy ExecutionT1040: Network SniffingT1008: Fallback ChannelsT1037: Boot or Logon Initialization ScriptsT1112: Modify RegistryT1069: Permission Groups DiscoveryT1665: Hide InfrastructureT1542: Pre-OS BootT1518: Software DiscoveryT1014: RootkitT1016: System Network Configuration DiscoveryT1550: Use Alternate Authentication MaterialT1033: System Owner/User DiscoveryT1078: Valid AccountsT1007: System Service DiscoveryT1134: Access Token ManipulationT1673: Virtual Machine DiscoveryT1197: BITS JobsT1656: ImpersonationT1599: Network Boundary BridgingT1221: Template InjectionTechniques heatmap for Indonesia

Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/ID
SHA256 File Hash: 62a0f8adfee301eb3cdc946b106d201c367c01e81f604dcfeac02e5aac5097fd

v17

Legend:

Increasing levels of observations

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

56

TA0043: ReconnaissanceTA0042: Resource DevelopmentTA0001: Initial AccessTA0002: ExecutionTA0003: PersistenceTA0004: Privilege EscalationTA0005: Defense EvasionTA0006: Credential AccessTA0007: DiscoveryTA0008: Lateral MovementTA0009: CollectionTA0011: Command and ControlTA0010: ExfiltrationTA0040: ImpactT1595: Active ScanningT1583: Acquire InfrastructureT1190: Exploit Public-Facing ApplicationT1059: Command and Scripting InterpreterT1053: Scheduled Task/JobT1053: Scheduled Task/JobT1070: Indicator RemovalT1555: Credentials from Password StoresT1083: File and Directory DiscoveryT1021: Remote ServicesT1560: Archive Collected DataT1071: Application Layer ProtocolT1567: Exfiltration Over Web ServiceT1486: Data Encrypted for ImpactT1590: Gather Victim Network InformationT1588: Obtain CapabilitiesT1566: PhishingT1053: Scheduled Task/JobT1574: Hijack Execution FlowT1574: Hijack Execution FlowT1027: Obfuscated Files or InformationT1003: OS Credential DumpingT1082: System Information DiscoveryT1570: Lateral Tool TransferT1005: Data from Local SystemT1219: Remote Access ToolsT1048: Exfiltration Over Alternative ProtocolT1491: DefacementT1593: Search Open Websites/DomainsT1586: Compromise AccountsT1133: External Remote ServicesT1569: System ServicesT1547: Boot or Logon Autostart ExecutionT1547: Boot or Logon Autostart ExecutionT1562: Impair DefensesT1110: Brute ForceT1087: Account DiscoveryT1550: Use Alternate Authentication MaterialT1056: Input CaptureT1102: Web ServiceT1041: Exfiltration Over C2 ChannelT1489: Service StopT1596: Search Open Technical DatabasesT1587: Develop CapabilitiesT1078: Valid AccountsT1203: Exploitation for Client ExecutionT1133: External Remote ServicesT1078: Valid AccountsT1574: Hijack Execution FlowT1056: Input CaptureT1057: Process DiscoveryT1210: Exploitation of Remote ServicesT1213: Data from Information RepositoriesT1001: Data ObfuscationT1030: Data Transfer Size LimitsT1657: Financial TheftT1594: Search Victim-Owned WebsitesT1650: Acquire AccessT1199: Trusted RelationshipT1072: Software Deployment ToolsT1078: Valid AccountsT1098: Account ManipulationT1480: Execution GuardrailsT1040: Network SniffingT1018: Remote System DiscoveryT1072: Software Deployment ToolsT1602: Data from Configuration RepositoryT1573: Encrypted ChannelT1490: Inhibit System RecoveryT1592: Gather Victim Host InformationT1659: Content InjectionT1204: User ExecutionT1098: Account ManipulationT1543: Create or Modify System ProcessT1078: Valid AccountsT1557: Adversary-in-the-MiddleT1614: System Location DiscoveryT1074: Data StagedT1090: ProxyT1485: Data DestructionT1598: Phishing for InformationT1195: Supply Chain CompromiseT1047: Windows Management InstrumentationT1543: Create or Modify System ProcessT1484: Domain or Tenant Policy ModificationT1140: Deobfuscate/Decode Files or InformationT1528: Steal Application Access TokenT1049: System Network Connections DiscoveryT1113: Screen CaptureT1105: Ingress Tool TransferT1496: Resource HijackingT1597: Search Closed SourcesT1189: Drive-by CompromiseT1674: Input InjectionT1546: Event Triggered ExecutionT1546: Event Triggered ExecutionT1484: Domain or Tenant Policy ModificationT1539: Steal Web Session CookieT1497: Virtualization/Sandbox EvasionT1557: Adversary-in-the-MiddleT1659: Content InjectionT1529: System Shutdown/RebootT1106: Native APIT1112: Modify RegistryT1055: Process InjectionT1112: Modify RegistryT1552: Unsecured CredentialsT1135: Network Share DiscoveryT1123: Audio CaptureT1568: Dynamic ResolutionT1129: Shared ModulesT1505: Server Software ComponentT1068: Exploitation for Privilege EscalationT1497: Virtualization/Sandbox EvasionT1007: System Service DiscoveryT1119: Automated CollectionT1104: Multi-Stage ChannelsT1136: Create AccountT1548: Abuse Elevation Control MechanismT1036: MasqueradingT1010: Application Window DiscoveryT1095: Non-Application Layer ProtocolT1542: Pre-OS BootT1134: Access Token ManipulationT1055: Process InjectionT1046: Network Service DiscoveryT1572: Protocol TunnelingT1197: BITS JobsT1037: Boot or Logon Initialization ScriptsT1218: System Binary Proxy ExecutionT1040: Network SniffingT1132: Data EncodingT1037: Boot or Logon Initialization ScriptsT1550: Use Alternate Authentication MaterialT1012: Query RegistryT1008: Fallback ChannelsT1653: Power SettingsT1542: Pre-OS BootT1016: System Network Configuration DiscoveryT1553: Subvert Trust ControlsT1482: Domain Trust DiscoveryT1548: Abuse Elevation Control MechanismT1120: Peripheral Device DiscoveryT1134: Access Token ManipulationT1069: Permission Groups DiscoveryT1197: BITS JobsT1518: Software DiscoveryT1656: ImpersonationT1033: System Owner/User DiscoveryT1599: Network Boundary BridgingT1673: Virtual Machine DiscoveryT1014: RootkitT1221: Template InjectionTechniques heatmap for South Korea

Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/SK
SHA256 File Hash: cdcc56af7983e957353025e037b33f5e3921f71d3beb5a2063731e5e13eebdca

v17

Legend:

Increasing levels of observations

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

57

TA0043: ReconnaissanceTA0042: Resource DevelopmentTA0001: Initial AccessTA0002: ExecutionTA0003: PersistenceTA0004: Privilege EscalationTA0005: Defense EvasionTA0006: Credential AccessTA0007: DiscoveryTA0008: Lateral MovementTA0009: CollectionTA0011: Command and ControlTA0010: ExfiltrationTA0040: ImpactT1589: Gather Victim Identity InformationT1588: Obtain CapabilitiesT1566: PhishingT1059: Command and Scripting InterpreterT1547: Boot or Logon Autostart ExecutionT1547: Boot or Logon Autostart ExecutionT1027: Obfuscated Files or InformationT1555: Credentials from Password StoresT1082: System Information DiscoveryT1021: Remote ServicesT1560: Archive Collected DataT1071: Application Layer ProtocolT1567: Exfiltration Over Web ServiceT1561: Disk WipeT1598: Phishing for InformationT1583: Acquire InfrastructureT1078: Valid AccountsT1204: User ExecutionT1574: Hijack Execution FlowT1055: Process InjectionT1070: Indicator RemovalT1003: OS Credential DumpingT1087: Account DiscoveryT1550: Use Alternate Authentication MaterialT1074: Data StagedT1102: Web ServiceT1048: Exfiltration Over Alternative ProtocolT1491: DefacementT1593: Search Open Websites/DomainsT1587: Develop CapabilitiesT1189: Drive-by CompromiseT1053: Scheduled Task/JobT1053: Scheduled Task/JobT1574: Hijack Execution FlowT1036: MasqueradingT1557: Adversary-in-the-MiddleT1083: File and Directory DiscoveryT1534: Internal SpearphishingT1557: Adversary-in-the-MiddleT1090: ProxyT1041: Exfiltration Over C2 ChannelT1485: Data DestructionT1591: Gather Victim Org InformationT1584: Compromise InfrastructureT1190: Exploit Public-Facing ApplicationT1559: Inter-Process CommunicationT1543: Create or Modify System ProcessT1053: Scheduled Task/JobT1562: Impair DefensesT1110: Brute ForceT1057: Process DiscoveryT1210: Exploitation of Remote ServicesT1005: Data from Local SystemT1132: Data EncodingT1030: Data Transfer Size LimitsT1489: Service StopT1595: Active ScanningT1585: Establish AccountsT1133: External Remote ServicesT1203: Exploitation for Client ExecutionT1505: Server Software ComponentT1543: Create or Modify System ProcessT1055: Process InjectionT1056: Input CaptureT1518: Software DiscoveryT1091: Replication Through Removable MediaT1056: Input CaptureT1001: Data ObfuscationT1529: System Shutdown/RebootT1596: Search Open Technical DatabasesT1608: Stage CapabilitiesT1199: Trusted RelationshipT1106: Native APIT1078: Valid AccountsT1078: Valid AccountsT1218: System Binary Proxy ExecutionT1040: Network SniffingT1614: System Location DiscoveryT1072: Software Deployment ToolsT1114: Email CollectionT1573: Encrypted ChannelT1486: Data Encrypted for ImpactT1594: Search Victim-Owned WebsitesT1586: Compromise AccountsT1091: Replication Through Removable MediaT1569: System ServicesT1542: Pre-OS BootT1548: Abuse Elevation Control MechanismT1574: Hijack Execution FlowT1111: Multi-Factor Authentication InterceptionT1016: System Network Configuration DiscoveryT1213: Data from Information RepositoriesT1105: Ingress Tool TransferT1657: Financial TheftT1650: Acquire AccessT1195: Supply Chain CompromiseT1072: Software Deployment ToolsT1098: Account ManipulationT1134: Access Token ManipulationT1564: Hide ArtifactsT1528: Steal Application Access TokenT1497: Virtualization/Sandbox EvasionT1119: Automated CollectionT1219: Remote Access ToolsT1490: Inhibit System RecoveryT1669: Wi-Fi NetworksT1047: Windows Management InstrumentationT1546: Event Triggered ExecutionT1098: Account ManipulationT1553: Subvert Trust ControlsT1539: Steal Web Session CookieT1120: Peripheral Device DiscoveryT1113: Screen CaptureT1092: Communication Through Removable MediaT1498: Network Denial of ServiceT1133: External Remote ServicesT1546: Event Triggered ExecutionT1078: Valid AccountsT1552: Unsecured CredentialsT1033: System Owner/User DiscoveryT1123: Audio CaptureT1008: Fallback ChannelsT1112: Modify RegistryT1037: Boot or Logon Initialization ScriptsT1548: Abuse Elevation Control MechanismT1046: Network Service DiscoveryT1185: Browser Session HijackingT1104: Multi-Stage ChannelsT1037: Boot or Logon Initialization ScriptsT1484: Domain or Tenant Policy ModificationT1134: Access Token ManipulationT1040: Network SniffingT1039: Data from Network Shared DriveT1095: Non-Application Layer ProtocolT1137: Office Application StartupT1068: Exploitation for Privilege EscalationT1542: Pre-OS BootT1012: Query RegistryT1025: Data from Removable MediaT1571: Non-Standard PortT1197: BITS JobsT1550: Use Alternate Authentication MaterialT1049: System Network Connections DiscoveryT1572: Protocol TunnelingT1136: Create AccountT1497: Virtualization/Sandbox EvasionT1010: Application Window DiscoveryT1205: Traffic SignalingT1176: Software ExtensionsT1140: Deobfuscate/Decode Files or InformationT1622: Debugger EvasionT1205: Traffic SignalingT1112: Modify RegistryT1007: System Service DiscoveryT1484: Domain or Tenant Policy ModificationT1124: System Time DiscoveryT1480: Execution GuardrailsT1656: ImpersonationT1620: Reflective Code LoadingT1221: Template InjectionT1197: BITS JobsT1622: Debugger EvasionT1006: Direct Volume AccessT1211: Exploitation for Defense EvasionT1202: Indirect Command ExecutionT1014: RootkitT1205: Traffic SignalingT1220: XSL Script ProcessingTechniques heatmap for Australia

Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/AU
SHA256 File Hash: 73823108702a2b8a80f7834a173ece9eeaf24662a6cc3ae01dd745adfccc529a

v17

Legend:

Increasing levels of observations

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

58

TA0043: ReconnaissanceTA0042: Resource DevelopmentTA0001: Initial AccessTA0002: ExecutionTA0003: PersistenceTA0004: Privilege EscalationTA0005: Defense EvasionTA0006: Credential AccessTA0007: DiscoveryTA0008: Lateral MovementTA0009: CollectionTA0011: Command and ControlTA0010: ExfiltrationTA0040: ImpactT1589: Gather Victim Identity InformationT1588: Obtain CapabilitiesT1566: PhishingT1059: Command and Scripting InterpreterT1078: Valid AccountsT1078: Valid AccountsT1027: Obfuscated Files or InformationT1003: OS Credential DumpingT1497: Virtualization/Sandbox EvasionT1021: Remote ServicesT1560: Archive Collected DataT1071: Application Layer ProtocolT1567: Exfiltration Over Web ServiceT1486: Data Encrypted for ImpactT1593: Search Open Websites/DomainsT1583: Acquire InfrastructureT1078: Valid AccountsT1204: User ExecutionT1547: Boot or Logon Autostart ExecutionT1547: Boot or Logon Autostart ExecutionT1070: Indicator RemovalT1555: Credentials from Password StoresT1087: Account DiscoveryT1550: Use Alternate Authentication MaterialT1074: Data StagedT1090: ProxyT1048: Exfiltration Over Alternative ProtocolT1491: DefacementT1595: Active ScanningT1587: Develop CapabilitiesT1190: Exploit Public-Facing ApplicationT1053: Scheduled Task/JobT1053: Scheduled Task/JobT1053: Scheduled Task/JobT1562: Impair DefensesT1056: Input CaptureT1069: Permission Groups DiscoveryT1570: Lateral Tool TransferT1056: Input CaptureT1573: Encrypted ChannelT1041: Exfiltration Over C2 ChannelT1561: Disk WipeT1591: Gather Victim Org InformationT1584: Compromise InfrastructureT1133: External Remote ServicesT1569: System ServicesT1505: Server Software ComponentT1546: Event Triggered ExecutionT1036: MasqueradingT1110: Brute ForceT1082: System Information DiscoveryT1210: Exploitation of Remote ServicesT1005: Data from Local SystemT1102: Web ServiceT1011: Exfiltration Over Other Network MediumT1490: Inhibit System RecoveryT1596: Search Open Technical DatabasesT1608: Stage CapabilitiesT1195: Supply Chain CompromiseT1047: Windows Management InstrumentationT1546: Event Triggered ExecutionT1574: Hijack Execution FlowT1553: Subvert Trust ControlsT1558: Steal or Forge Kerberos TicketsT1614: System Location DiscoveryT1534: Internal SpearphishingT1213: Data from Information RepositoriesT1001: Data ObfuscationT1030: Data Transfer Size LimitsT1489: Service StopT1590: Gather Victim Network InformationT1585: Establish AccountsT1199: Trusted RelationshipT1203: Exploitation for Client ExecutionT1574: Hijack Execution FlowT1098: Account ManipulationT1218: System Binary Proxy ExecutionT1552: Unsecured CredentialsT1083: File and Directory DiscoveryT1091: Replication Through Removable MediaT1557: Adversary-in-the-MiddleT1105: Ingress Tool TransferT1537: Transfer Data to Cloud AccountT1485: Data DestructionT1594: Search Victim-Owned WebsitesT1586: Compromise AccountsT1189: Drive-by CompromiseT1559: Inter-Process CommunicationT1098: Account ManipulationT1055: Process InjectionT1497: Virtualization/Sandbox EvasionT1557: Adversary-in-the-MiddleT1018: Remote System DiscoveryT1072: Software Deployment ToolsT1113: Screen CaptureT1568: Dynamic ResolutionT1499: Endpoint Denial of ServiceT1592: Gather Victim Host InformationT1650: Acquire AccessT1091: Replication Through Removable MediaT1106: Native APIT1543: Create or Modify System ProcessT1543: Create or Modify System ProcessT1078: Valid AccountsT1606: Forge Web CredentialsT1016: System Network Configuration DiscoveryT1114: Email CollectionT1219: Remote Access ToolsT1657: Financial TheftT1651: Cloud Administration CommandT1136: Create AccountT1548: Abuse Elevation Control MechanismT1574: Hijack Execution FlowT1556: Modify Authentication ProcessT1057: Process DiscoveryT1123: Audio CaptureT1095: Non-Application Layer ProtocolT1498: Network Denial of ServiceT1674: Input InjectionT1133: External Remote ServicesT1484: Domain or Tenant Policy ModificationT1055: Process InjectionT1621: Multi-Factor Authentication Request GenerationT1046: Network Service DiscoveryT1119: Automated CollectionT1132: Data EncodingT1496: Resource HijackingT1129: Shared ModulesT1542: Pre-OS BootT1134: Access Token ManipulationT1140: Deobfuscate/Decode Files or InformationT1528: Steal Application Access TokenT1049: System Network Connections DiscoveryT1125: Video CaptureT1008: Fallback ChannelsT1529: System Shutdown/RebootT1072: Software Deployment ToolsT1037: Boot or Logon Initialization ScriptsT1037: Boot or Logon Initialization ScriptsT1548: Abuse Elevation Control MechanismT1649: Steal or Forge Authentication CertificatesT1033: System Owner/User DiscoveryT1571: Non-Standard PortT1112: Modify RegistryT1068: Exploitation for Privilege EscalationT1484: Domain or Tenant Policy ModificationT1539: Steal Web Session CookieT1010: Application Window DiscoveryT1665: Hide InfrastructureT1556: Modify Authentication ProcessT1480: Execution GuardrailsT1135: Network Share DiscoveryT1104: Multi-Stage ChannelsT1197: BITS JobsT1550: Use Alternate Authentication MaterialT1012: Query RegistryT1572: Protocol TunnelingT1564: Hide ArtifactsT1518: Software DiscoveryT1542: Pre-OS BootT1482: Domain Trust DiscoveryT1134: Access Token ManipulationT1120: Peripheral Device DiscoveryT1112: Modify RegistryT1124: System Time DiscoveryT1222: File and Directory Permissions ModificationT1217: Browser Information DiscoveryT1656: ImpersonationT1622: Debugger EvasionT1556: Modify Authentication ProcessT1654: Log EnumerationT1014: RootkitT1007: System Service DiscoveryT1197: BITS JobsT1673: Virtual Machine DiscoveryT1622: Debugger EvasionT1006: Direct Volume AccessT1211: Exploitation for Defense EvasionT1202: Indirect Command ExecutionT1599: Network Boundary BridgingT1620: Reflective Code LoadingT1221: Template InjectionT1220: XSL Script ProcessingTechniques heatmap for Greater China Region

Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/GCR
SHA256 File Hash: 6ab48c61c2d2f12e2a5b12ab8319d13b2c4c0e11ccd5c4eea2b3c6a56af839b7

v17

Legend:

Increasing levels of observations

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

59

TA0043: ReconnaissanceTA0042: Resource DevelopmentTA0001: Initial AccessTA0002: ExecutionTA0003: PersistenceTA0004: Privilege EscalationTA0005: Defense EvasionTA0006: Credential AccessTA0007: DiscoveryTA0008: Lateral MovementTA0009: CollectionTA0011: Command and ControlTA0010: ExfiltrationTA0040: ImpactT1598: Phishing for InformationT1583: Acquire InfrastructureT1566: PhishingT1059: Command and Scripting InterpreterT1547: Boot or Logon Autostart ExecutionT1547: Boot or Logon Autostart ExecutionT1027: Obfuscated Files or InformationT1056: Input CaptureT1082: System Information DiscoveryT1021: Remote ServicesT1056: Input CaptureT1071: Application Layer ProtocolT1048: Exfiltration Over Alternative ProtocolT1491: DefacementT1589: Gather Victim Identity InformationT1588: Obtain CapabilitiesT1189: Drive-by CompromiseT1204: User ExecutionT1574: Hijack Execution FlowT1574: Hijack Execution FlowT1036: MasqueradingT1003: OS Credential DumpingT1518: Software DiscoveryT1072: Software Deployment ToolsT1560: Archive Collected DataT1102: Web ServiceT1567: Exfiltration Over Web ServiceT1561: Disk WipeT1591: Gather Victim Org InformationT1608: Stage CapabilitiesT1078: Valid AccountsT1053: Scheduled Task/JobT1543: Create or Modify System ProcessT1543: Create or Modify System ProcessT1070: Indicator RemovalT1555: Credentials from Password StoresT1083: File and Directory DiscoveryT1550: Use Alternate Authentication MaterialT1074: Data StagedT1132: Data EncodingT1041: Exfiltration Over C2 ChannelT1485: Data DestructionT1593: Search Open Websites/DomainsT1584: Compromise InfrastructureT1190: Exploit Public-Facing ApplicationT1203: Exploitation for Client ExecutionT1053: Scheduled Task/JobT1053: Scheduled Task/JobT1218: System Binary Proxy ExecutionT1557: Adversary-in-the-MiddleT1087: Account DiscoveryT1210: Exploitation of Remote ServicesT1557: Adversary-in-the-MiddleT1573: Encrypted ChannelT1020: Automated ExfiltrationT1486: Data Encrypted for ImpactT1595: Active ScanningT1587: Develop CapabilitiesT1133: External Remote ServicesT1559: Inter-Process CommunicationT1112: Modify RegistryT1548: Abuse Elevation Control MechanismT1574: Hijack Execution FlowT1110: Brute ForceT1016: System Network Configuration DiscoveryT1570: Lateral Tool TransferT1119: Automated CollectionT1105: Ingress Tool TransferT1052: Exfiltration Over Physical MediumT1490: Inhibit System RecoveryT1585: Establish AccountsT1091: Replication Through Removable MediaT1569: System ServicesT1546: Event Triggered ExecutionT1055: Process InjectionT1562: Impair DefensesT1552: Unsecured CredentialsT1497: Virtualization/Sandbox EvasionT1091: Replication Through Removable MediaT1005: Data from Local SystemT1090: ProxyT1030: Data Transfer Size LimitsT1489: Service StopT1650: Acquire AccessT1195: Supply Chain CompromiseT1072: Software Deployment ToolsT1078: Valid AccountsT1546: Event Triggered ExecutionT1548: Abuse Elevation Control MechanismT1040: Network SniffingT1049: System Network Connections DiscoveryT1534: Internal SpearphishingT1113: Screen CaptureT1001: Data ObfuscationT1657: Financial TheftT1199: Trusted RelationshipT1047: Windows Management InstrumentationT1505: Server Software ComponentT1078: Valid AccountsT1055: Process InjectionT1033: System Owner/User DiscoveryT1563: Remote Service Session HijackingT1123: Audio CaptureT1095: Non-Application Layer ProtocolT1498: Network Denial of ServiceT1106: Native APIT1098: Account ManipulationT1134: Access Token ManipulationT1497: Virtualization/Sandbox EvasionT1057: Process DiscoveryT1080: Taint Shared ContentT1115: Clipboard DataT1571: Non-Standard PortT1529: System Shutdown/RebootT1610: Deploy ContainerT1542: Pre-OS BootT1098: Account ManipulationT1564: Hide ArtifactsT1124: System Time DiscoveryT1602: Data from Configuration RepositoryT1219: Remote Access ToolsT1129: Shared ModulesT1133: External Remote ServicesT1484: Domain or Tenant Policy ModificationT1112: Modify RegistryT1046: Network Service DiscoveryT1213: Data from Information RepositoriesT1572: Protocol TunnelingT1197: BITS JobsT1068: Exploitation for Privilege EscalationT1553: Subvert Trust ControlsT1012: Query RegistryT1025: Data from Removable MediaT1568: Dynamic ResolutionT1037: Boot or Logon Initialization ScriptsT1037: Boot or Logon Initialization ScriptsT1078: Valid AccountsT1614: System Location DiscoveryT1125: Video CaptureT1008: Fallback ChannelsT1137: Office Application StartupT1140: Deobfuscate/Decode Files or InformationT1018: Remote System DiscoveryT1665: Hide InfrastructureT1653: Power SettingsT1550: Use Alternate Authentication MaterialT1007: System Service DiscoveryT1104: Multi-Stage ChannelsT1205: Traffic SignalingT1134: Access Token ManipulationT1010: Application Window DiscoveryT1205: Traffic SignalingT1542: Pre-OS BootT1482: Domain Trust DiscoveryT1484: Domain or Tenant Policy ModificationT1622: Debugger EvasionT1480: Execution GuardrailsT1135: Network Share DiscoveryT1222: File and Directory Permissions ModificationT1040: Network SniffingT1202: Indirect Command ExecutionT1120: Peripheral Device DiscoveryT1216: System Script Proxy ExecutionT1221: Template InjectionT1197: BITS JobsT1622: Debugger EvasionT1610: Deploy ContainerT1656: ImpersonationT1620: Reflective Code LoadingT1205: Traffic SignalingT1220: XSL Script ProcessingAPPENDIX B
Territorial Observed Top Exploited Vulnerabilities

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

60

Overview of Territorial Insights
NOTABLE CVES ACROSS RELEVANT TERRITORIES (1/2)

CVE Identifier

Affected System (s)

CVSS

EPSS

CVE-2024-21887

Ivanti Connect Secure and Policy Secure - Web component

CVE-2017-11882

Microsoft Office 2007 Service Pack 3, Microsoft Office 2010 Service Pack
2, Microsoft Office 2013 Service Pack 1, and Microsoft Office 2016

CVE-2024-24919

Check Point Security Gateways

CVE-2024-21893

Ivanti Connect Secure, Policy Secure, and Neurons for ZTA - SAML
component

CVE-2024-1709

ConnectWise ScreenConnect

CVE-2024-21412

Microsoft Defender SmartScreen

CVE-2023-23397

Microsoft Outlook

CVE-2022-42475

FortiOS SSL-VPN and FortiProxy SSL-VPN

CVE-2023-20273

Cisco IOS XE Software - Web UI feature

CVE-2019-9621

Zimbra Collaboration Suite

CVE-2024-21762

Fortinet FortiOS

CVE-2024-23108

Fortinet FortiSIEM

CVE-2024-21338

Certain IOCTL of “appid.sys” known as AppLocker‘s driver

CVE-2017-5070

V8 in Google Chrome

CVE-2024-38193

Windows Ancillary Function Driver

CVE-2023-28252

Windows Common Log File System

9.1

7.8

8.6

8.2

10

8.1

9.8

9.8

7.2

7.5

9.8

9.8

7.8

8.8

7.8

7.8

0.94416

0.94384

0.94327

0.9432

0.9431

0.93777

0.93547

0.93196

0.92717

0.91807

0.91602

0.88633

0.80512

0.803

0.73164

0.52956

MY

SG

●

●

●

●

●

●

●

●

●

●

●

VICTIM TERRITORY

SK

AU

GCR

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

ID

●

●

●

●

●

Note: This is a non-exhaustive list. EPSS is accurate as of June 2025.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

61

Overview of Territorial Insights
NOTABLE CVES ACROSS RELEVANT TERRITORIES (2/2)

CVE Identifier

Affected System (s)

CVSS

EPSS

SG

MY

ID

SK

AU

GCR

VICTIM TERRITORY

CVE-2024-1708

ConnectWise ScreenConnect

CVE-2024-30051

Windows DWM Core Library

CVE-2024-23113

Fortinet FortiOS, FortiProxy, FortiPAM, FortiSwitchManager

CVE-2024-7262

Kingsoft WPS Office version on Windows

CVE-2024-38178

Microsoft Windows systems

CVE-2024-39717

Versa Director GUI

CVE-2024-23109

Fortinet FortiSIEM

CVE-2021-30869

iOS and macOS

CVE-2024-5274

V8 in Google Chrome

CVE-2024-38106

Windows NT Operating System Kernel Executable

CVE-2024-4947

V8 in Google Chrome

CVE-2024-7971

V8 in Google Chrome

CVE-2024-3400

Palo Alto Networks PAN-OS Global Protect Feature

CVE-2024-7263

Kingsoft WPS Office version on Windows

CVE-2024-4577

Apache and PHP-CGI on Windows

CVE-2023-20198

Cisco IOS XE Software - Web UI feature

CVE-2024-50570

FortiClientWindows and FortiClientLinux

8.4

7.8

9.8

7.8

7.5

7.2

9.8

7.8

9.6

7

9.6

9.6

10

7.8

9.8

10

5

0.49314

0.48997

0.45024

0.25173

0.1704

0.05514

0.04986

0.04229

0.01792

0.00403

0.00354

0.00351

0.0035

0.00052

0.0005

0.00014

0.00007

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

Note: This is a non-exhaustive list. EPSS is accurate as of June 2025.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

62

APPENDIX C
ICS oriented Techniques Heatmaps

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

63

ICS-oriented Techniques Heatmap – ICS Matrix

Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/IcsTech
SHA256 File Hash: b7732aff849cf91090d16ad0110f03e6cb2304db26d68108121d3fc440285928

v17

Legend:

Increasing levels of observations

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

64

TA0108: Initial AccessTA0104: ExecutionTA0110: PersistenceTA0111: Privilege EscalationTA0103: EvasionTA0102: DiscoveryTA0109: Lateral MovementTA0100: CollectionTA0101: Command and ControlTA0107: Inhibit Response FunctionTA0106: Impair Process ControlTA0105: ImpactT0819: Exploit Public-Facing ApplicationT0807: Command-Line InterfaceT0886: Remote ServicesT0885: Commonly Used PortT0836: Modify ParameterT0813: Denial of ControlT0883: Internet Accessible DeviceT0869: Standard Application Layer ProtocolT0855: Unauthorized Command MessageT0826: Loss of AvailabilityT0886: Remote ServicesT0827: Loss of ControlT0828: Loss of Productivity and RevenueT0829: Loss of ViewT0831: Manipulation of ControlT0832: Manipulation of ViewICS-oriented Techniques Heatmap – Enterprise Matrix

Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/IcsEnt
SHA256 File Hash: 3d868f75fcba7fc716f7f69f6dfc8d2234779707a2e8626c84a89ba93ff2975b

v17

Legend:

Increasing levels of observations

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

65

TA0043: ReconnaissanceTA0042: Resource DevelopmentTA0001: Initial AccessTA0002: ExecutionTA0003: PersistenceTA0004: Privilege EscalationTA0005: Defense EvasionTA0006: Credential AccessTA0007: DiscoveryTA0008: Lateral MovementTA0009: CollectionTA0011: Command and ControlTA0010: ExfiltrationTA0040: ImpactT1595: Active ScanningT1078: Valid AccountsT1059: Command and Scripting InterpreterT1547: Boot or Logon Autostart ExecutionT1547: Boot or Logon Autostart ExecutionT1027: Obfuscated Files or InformationT1110: Brute ForceT1005: Data from Local SystemT1071: Application Layer ProtocolT1048: Exfiltration Over Alternative ProtocolT1491: DefacementT1592: Gather Victim Host InformationT1078: Valid AccountsT1078: Valid AccountsT1078: Valid AccountsT1590: Gather Victim Network InformationT1593: Search Open Websites/DomainsT1594: Search Victim-Owned Websites