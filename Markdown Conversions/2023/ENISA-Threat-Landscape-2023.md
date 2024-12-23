# ENISA THREAT LANDSCAPE 2023
## Table of Contents
- [EUROPEAN UNION AGENCY FOR CYBERSECURITY](#european-union-agency-for-cybersecurity)
- [ABOUT ENISA](#about-enisa)
- [CONTACT](#contact)
- [EDITORS](#editors)
- [CONTRIBUTORS](#contributors)
- [ACKNOWLEDGEMENTS](#acknowledgements)
- [LEGAL NOTICE](#legal-notice)
- [COPYRIGHT NOTICE](#copyright-notice)
- [TABLE OF CONTENTS](#table-of-contents)
- [EXECUTIVE SUMMARY](#executive-summary)
- [1. THREAT LANDSCAPE OVERVIEW](#1-threat-landscape-overview)
  - [1.1 PRIME THREATS](#11-prime-threats)
  - [1.2 KEY TRENDS](#12-key-trends)
  - [1.3 EU PRIME THREATS](#13-eu-prime-threats)
  - [1.4 SECTORAL ANALYSIS](#14-sectoral-analysis)
  - [1.5 IMPACT ASSESSMENT](#15-impact-assessment)
  - [1.6 MOTIVATION](#16-motivation)
  - [1.7 METHODOLOGY](#17-methodology)
  - [1.8 STRUCTURE OF THE REPORT](#18-structure-of-the-report)
- [2. THREAT ACTOR TRENDS](#2-threat-actor-trends)
  - [2.1 STATE-NEXUS GROUP TRENDS](#21-state-nexus-group-trends)
  - [2.2 CYBERCRIME ACTOR TRENDS](#22-cybercrime-actor-trends)
  - [2.3 HACKER-FOR-HIRE ACTOR TRENDS](#23-hacker-for-hire-actor-trends)
  - [2.4 HACKTIVISTS’ TRENDS](#24-hacktivists-trends)
- [3. ANALYSIS OF THE VULNERABILITIES LANDSCAPE 2022-2023](#3-analysis-of-the-vulnerabilities-landscape-2022-2023)
  - [3.1 SUMMARY](#31-summary)
  - [3.2 ANALYSIS OF THE CVE NUMBERING AUTHORITIES (CNA)](#32-analysis-of-the-cve-numbering-authorities-cna)
  - [3.3 ANALYSIS OF THE CVE LANDSCAPE](#33-analysis-of-the-cve-landscape)
  - [3.4 ANALYSIS OF KNOWN EXPLOITED VULNERABILITIES (KEV).](#34-analysis-of-known-exploited-vulnerabilities-kev)
  - [3.5 BACKGROUND](#35-background)
- [4. RANSOMWARE](#4-ransomware)
  - [4.1 LOCKBIT, ALPHV, AND BIAN LIAN STAND OUT AS THE TOP PERFORMERS, WHILE IN THE EU, PLAY GROUP JOINS THE RANKS OF LEADING THREAT ACTORS](#41-lockbit-alphv-and-bian-lian-stand-out-as-the-top-performers-while-in-the-eu-play-group-joins-the-ranks-of-leading-threat-actors)
  - [4.2 RISE OF CL0P USE OF TWO 0-DAYS](#42-rise-of-cl0p-use-of-two-0-days)
  - [4.3 MONETISATION TOP MOTIVATION - RAAS GROUPS APOLOGING FOR INCIDENTS](#43-monetisation-top-motivation---raas-groups-apologing-for-incidents)
  - [4.4 MARCH 2023 BROKE RANSOMWARE ATTACK RECORDS - RANSOMWARE CONTINUES TO BE ON THE RISE](#44-march-2023-broke-ransomware-attack-records---ransomware-continues-to-be-on-the-rise)
  - [4.5 INCREASED OPERATIONS BY LAW ENFORCEMENT](#45-increased-operations-by-law-enforcement)
  - [4.6 NEW TECHIQUES EMERGING](#46-new-techiques-emerging)
  - [4.7 FEWER VICTIMS PAID IN 2022 BUT NOT THE CASE FOR 2023 - SHIFTING FROM ENCRYPTION TO DATA EXTORTION](#47-fewer-victims-paid-in-2022-but-not-the-case-for-2023---shifting-from-encryption-to-data-extortion)
- [5. MALWARE](#5-malware)
  - [5.1 INFORMATION STEALERS REMAIN ONE OF THE TOP MALWARE THREATS](#51-information-stealers-remain-one-of-the-top-malware-threats)
  - [5.2 EVOLUTION OF MALWARE DELIVERY MECHANISMS](#52-evolution-of-malware-delivery-mechanisms)
  - [5.3 LOLBIN AND COBALT STRIKE](#53-lolbin-and-cobalt-strike)
  - [5.4 MOBILE SPYWARE](#54-mobile-spyware)
  - [5.5 THE HIDDEN THREAT OF PRE-INSTALLED MALWARE](#55-the-hidden-threat-of-pre-installed-malware)
  - [5.6 THE ESCALATION OF DESTRUCTIVE MALWARE](#56-the-escalation-of-destructive-malware)
  - [5.7 EVOLUTION OF MALWARE THREATS IN OT](#57-evolution-of-malware-threats-in-ot)
  - [5.8 IMPACT OF LAW ENFORCEMENT ACTIONS](#58-impact-of-law-enforcement-actions)
- [6. SOCIAL ENGINEERING](#6-social-engineering)
  - [6.1 PHISHING AS THE INITIAL INFECTION VECTOR AND ON THE RISE](#61-phishing-as-the-initial-infection-vector-and-on-the-rise)
  - [6.2 WAR AGAINST UKRAINE USED AS THE LURE](#62-war-against-ukraine-used-as-the-lure)
  - [6.3 THE POTENTIAL USE OF AI FOR SOCIAL ENGINEERING](#63-the-potential-use-of-ai-for-social-engineering)
  - [6.4 ABUSING MULTI-FACTOR AUTHENTICATION](#64-abusing-multi-factor-authentication)
  - [6.5 SOCIAL ENGINEERING IN THE PHYSICAL WORLD](#65-social-engineering-in-the-physical-world)
  - [6.6 FROM MICROSOFT MACROS TO ISO, ONENOTE AND LNK FILES](#66-from-microsoft-macros-to-iso-onenote-and-lnk-files)
  - [6.7 PHISHING KITS AND PHISHING-AS-A-SERVICE (PHAAS)](#67-phishing-kits-and-phishing-as-a-service-phaas)
  - [6.8 BUSINESS AND VENDOR EMAIL COMPROMISE (BEC, VEC)](#68-business-and-vendor-email-compromise-bec-vec)
  - [6.9 INCREASING ATTACKS TO THE WEB3 ECOSYSTEM](#69-increasing-attacks-to-the-web3-ecosystem)
  - [6.10 USING EXTORTION-ONLY TECHNIQUES](#610-using-extortion-only-techniques)
  - [6.11 RE-EMERGENCE OF CALL-BACK PHISHING](#611-re-emergence-of-call-back-phishing)
- [7. THREATS AGAINST DATA](#7-threats-against-data)
  - [7.1 SUMMARY](#71-summary)
  - [7.2 ATTACK VECTORS, ASSETS, MOTIVATIONS AND TARGETS](#72-attack-vectors-assets-motivations-and-targets)
  - [7.3 DATA COMPROMISE SIMILAR TO 2022 BUT INCREASE IN 2023](#73-data-compromise-similar-to-2022-but-increase-in-2023)
  - [7.4 IDENTITY THEFT AND SYNTHETIC IDENTITY](#74-identity-theft-and-synthetic-identity)
  - [7.5 LACK OF TRANSPARENCY IN DATA BREACH NOTICES](#75-lack-of-transparency-in-data-breach-notices)
  - [7.6 ROLE OF CLOUD INFRASTRUCTURE](#76-role-of-cloud-infrastructure)
  - [7.7 DATA ATTACKS ON MACHINE LEARNING](#77-data-attacks-on-machine-learning)
  - [7.8 THE SURGE OF AI CHATBOTS](#78-the-surge-of-ai-chatbots)
  - [7.9 ADDITIONAL TRENDS](#79-additional-trends)
- [8. THREATS AGAINST AVAILABILITY: DENIAL OF SERVICE](#8-threats-against-availability-denial-of-service)
  - [8.1 ATTACKS ARE GETTING LARGER AND MORE COMPLEX, AND MORE INEXPENSIVE](#81-attacks-are-getting-larger-and-more-complex-and-more-inexpensive)
  - [8.2 DDOS ATTACKS ARE INCREASINGLY BUILT ON IOT DEVICES](#82-ddos-attacks-are-increasingly-built-on-iot-devices)
  - [8.3 DDOS AND CYBERWARFARE: THE RETURN OF THE HACKTIVIST](#83-ddos-and-cyberwarfare-the-return-of-the-hacktivist)
  - [8.4 DDOS ATTACKS AS A SMOKESCREEN AND HORIZONTAL ATTACKS](#84-ddos-attacks-as-a-smokescreen-and-horizontal-attacks)
  - [8.5 RANSOM DENIAL OF SERVICE (RDOS)](#85-ransom-denial-of-service-rdos)
  - [8.6 APPLICATION ATTACKS ARE INCREASING](#86-application-attacks-are-increasing)
  - [8.7 TCP VS UDP ATTACKS](#87-tcp-vs-udp-attacks)
  - [8.8 THE CLOUD AND DDOS](#88-the-cloud-and-ddos)
  - [8.9 DDOS ATTACKS SPREAD](#89-ddos-attacks-spread)
  - [8.10 ATTACK VECTORS](#810-attack-vectors)
- [9. THREATS AGAINST AVAILABILITY: INTERNET THREATS](#9-threats-against-availability-internet-threats)
  - [9.1 INTERNET SHUTDOWNS AT AN ALL-TIME HIGH](#91-internet-shutdowns-at-an-all-time-high)
  - [9.2 INTERNET DISRUPTIONS](#92-internet-disruptions)
  - [9.3 CABLE CUTS, POWER OUTAGES AND TECHNICAL PROBLEMS](#93-cable-cuts-power-outages-and-technical-problems)
  - [9.4 NATURAL DISASTERS](#94-natural-disasters)
  - [9.5 CYBERATTACKS](#95-cyberattacks)
  - [9.6 PHYSICAL TAKE-OVER AND DESTRUCTION OF INTERNET INFRASTRUCTURE](#96-physical-take-over-and-destruction-of-internet-infrastructure)
  - [9.7 ACTIVE INTERNET CENSORSHIP](#97-active-internet-censorship)
- [10. INFORMATION MANIPULATION AND INTERFERENCE](#10-information-manipulation-and-interference)
  - [10.1 GENERAL TRENDS](#101-general-trends)
  - [10.2 INFORMATION MANIPULATION AS A KEY ELEMENT OF RUSSIA’S WAR OF AGGRESSION AGAINST UKRAINE](#102-information-manipulation-as-a-key-element-of-russias-war-of-aggression-against-ukraine)
  - [10.3 EXPLOITING THE ‘CYBERSECURITY NARRATIVE’](#103-exploiting-the-cybersecurity-narrative)
  - [10.4 INFORMATION MANIPULATION FUELLING ‘HACKTIVISM’](#104-information-manipulation-fuelling-hacktivism)
  - [10.5 MAXIMISATION OF EXPOSURE THROUGH A WIDESPREAD DIGITAL PRESENCE](#105-maximisation-of-exposure-through-a-widespread-digital-presence)
  - [10.6 ‘CHEAP FAKES’ AND AI-ENABLED MANIPULATION OF INFORMATION](#106-cheap-fakes-and-ai-enabled-manipulation-of-information)
  - [10.7 COMMODIFICATION OF INFORMATION MANIPULATION](#107-commodification-of-information-manipulation)
  - [10.8 POLITICAL INITIATIVES AND WORK ON THE GROUND](#108-political-initiatives-and-work-on-the-ground)
- [11. SUPPLY CHAIN ATTACKS](#11-supply-chain-attacks)
  - [11.1 SUPPLY CHAIN ATTACKS RELATED TO THE WAR IN UKRAINE](#111-supply-chain-attacks-related-to-the-war-in-ukraine)
  - [11.2 TARGETING IDENTITY PROVIDERS](#112-targeting-identity-providers)
  - [11.3 ATTACKS ON SOFTWARE SUPPLY CHAINS](#113-attacks-on-software-supply-chains)
  - [11.4 IT SUPPLIERS AND MANAGED SERVICE PROVIDERS](#114-it-suppliers-and-managed-service-providers)
  - [11.5 ATTACKS ON THE HARDWARE SUPPLY VECTOR](#115-attacks-on-the-hardware-supply-vector)
  - [11.6 THIRD-PARTY CONNECTED APPS](#116-third-party-connected-apps)
  - [11.7 USE OF EMPLOYEES AS ENTRY POINTS](#117-use-of-employees-as-entry-points)
  - [11.8 LOG4SHELL](#118-log4shell)
  - [11.9 USE OF AI TO IMPROVE SOFTWARE SUPPLY CHAIN](#119-use-of-ai-to-improve-software-supply-chain)
- [A ANNEX: MAPPING TO MITRE ATT&CK FRAMEWORK](#a-annex-mapping-to-mitre-attck-framework)
  - [RANSOMWARE](#ransomware-1)
  - [MALWARE (PEGASUS FOR ANDROID)](#malware-pegasus-for-android)
  - [SOCIAL ENGINEERING](#social-engineering-1)
  - [THREATS AGAINST DATA](#threats-against-data-1)
  - [THREATS AGAINST AVAILABILITY (DDOS)](#threats-against-availability-ddos)
  - [THREATS AGAINST AVAILABILITY- INTERNET THREATS](#threats-against-availability--internet-threats)
  - [INFORMATION MANIPULATION AND INTERFERENCE](#information-manipulation-and-interference-1)
  - [SUPPLY CHAIN ATTACKS](#supply-chain-attacks-1)
- [B ANNEX: RECOMMENDATIONS](#b-annex-recommendations)
  - [RANSOMWARE](#ransomware-2)
  - [MALWARE](#malware-1)
  - [SOCIAL ENGINEERING](#social-engineering-2)
  - [THREATS AGAINST DATA](#threats-against-data-2)
  - [THREATS AGAINST AVAILABILITY (DDOS)](#threats-against-availability-ddos-1)
  - [INFORMATION MANIPULATION AND INTERFERENCE](#information-manipulation-and-interference-2)
  - [SUPPLY CHAIN ATTACKS](#supply-chain-attacks-2)
- [ABOUT ENISA](#about-enisa-1)

# EUROPEAN UNION AGENCY FOR CYBERSECURITY
OCTOBER 2023

ENISA THREAT LANDSCAPE 2023
July 2022 to June 2023

ENISA THREAT LANDSCAPE 2023
October 2023

1

# ABOUT ENISA
The European Union Agency for Cybersecurity, ENISA, is the Union’s agency dedicated to achieving a high common level of cybersecurity across Europe. Established in 2004 and strengthened by the EU Cybersecurity Act, the European Union Agency for Cybersecurity contributes to EU cyber policy, enhances the trustworthiness of ICT products, services and processes with cybersecurity certification schemes, cooperates with Member States and EU bodies, and helps Europe prepare for the cyber challenges of tomorrow. Through knowledge sharing, capacity building and awareness raising, the Agency works together with its key stakeholders to strengthen trust in the connected economy, to boost resilience of the Union’s infrastructure, and, ultimately, to keep Europe’s society and citizens digitally secure. More information about ENISA and its work can be found here: www.enisa.europa.eu.

# CONTACT
To contact the authors, please use etl@enisa.europa.eu
For media enquiries about this paper, please use press@enisa.europa.eu.

# EDITORS
Ifigeneia Lella, Eleni Tsekmezoglou, Marianthi Theocharidou, Erika Magonara, Apostolos Malatras, Rossen Svetozarov Naydenov, Cosmin Ciobanu – European Union Agency for Cybersecurity

# CONTRIBUTORS
Claudio Ardagna, Stephen Corbiaux, Koen Van Impe, Radim Ostadal

# ACKNOWLEDGEMENTS
We would like to thank the Members and Observers of the ENISA ad hoc Working Group on Cyber Threat Landscapes for their valuable feedback and comments in validating this report. We would also like to thank the ENISA Advisory Group and the National Liaison Officers network for their valuable feedback.

We would also like to thank the EEAS Strategic Communication Task Forces and Information Analysis Division (SG. STRAT.2) for sharing the data on information manipulation and revising and contributing to the chapter on information manipulation.

# LEGAL NOTICE
This publication represents the views and interpretations of ENISA, unless stated otherwise. It does not endorse a regulatory obligation of ENISA or of ENISA bodies pursuant to the Regulation (EU) No 2019/881.
ENISA has the right to alter, update or remove the publication or any of its contents. It is intended for information purposes only and it must be accessible free of charge. All references to it or its use as a whole or partially must contain ENISA as its source.
Third-party sources are quoted as appropriate. ENISA is not responsible or liable for the content of the external sources including external websites referenced in this publication.
Neither ENISA nor any person acting on its behalf is responsible for the use that might be made of the information contained in this publication.
ENISA maintains its intellectual property rights in relation to this publication.

ENISA THREAT LANDSCAPE 2023
October 2023

2

# COPYRIGHT NOTICE
© European Union Agency for Cybersecurity (ENISA), 2023

This publication is licenced under CC-BY 4.0 “Unless otherwise noted, the reuse of this document is authorised under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence (https://creativecommons.org/licenses/by/4.0/). This means that reuse is allowed, provided that appropriate credit is given and any changes are indicated”.

ISBN: 978-92-9204-645-3, DOI: 10.2824/782573

ENISA THREAT LANDSCAPE 2023
October 2023

3

# TABLE OF CONTENTS
1.  THREAT LANDSCAPE OVERVIEW 6
2.  THREAT ACTOR TRENDS 20
3.  ANALYSIS OF THE VULNERABILITIES LANDSCAPE 2022-2023 38
4.  RANSOMWARE 51
5.  MALWARE 62
6.  SOCIAL ENGINEERING 70
7.  THREATS AGAINST DATA 83
8.  THREATS AGAINST AVAILABILITY: DENIAL OF SERVICE 93
9.  THREATS AGAINST AVAILABILITY: INTERNET THREATS 104
10. INFORMATION MANIPULATION AND INTERFERENCE 110
11. SUPPLY CHAIN ATTACKS 124
A ANNEX: MAPPING TO MITRE ATT&CK FRAMEWORK 131
B ANNEX: RECOMMENDATIONS 140

ENISA THREAT LANDSCAPE 2023
October 2023

4

# EXECUTIVE SUMMARY
The ENISA Threat Landscape (ETL) report, now in its eleventh edition, plays a crucial role in understanding the current state of cybersecurity mainly within the European Union (EU). It provides valuable insights into emerging trends in terms of cybersecurity threats, threat actors’ activities as well as vulnerabilities and cybersecurity incidents. Accordingly, the ETL aims at informing decisions, priorities and recommendations in the field of cybersecurity. It identifies the top threats and their particularities, threat actors’ motivations and attack techniques, as well as provides a deep-dive insight on particular sectors along with a relevant impact analysis. The work has been supported by ENISA’s ad hoc Working Group on Cybersecurity Threat Landscapes (CTL).

In the latter part of 2022 and the first half of 2023, the cybersecurity landscape witnessed a significant increase in both the variety and quantity of cyberattacks and their consequences. The ongoing war of aggression against Ukraine continued to influence the landscape. Hacktivism has expanded with the emergence of new groups, while ransomware incidents surged in the first half of 2023 and showed no signs of slowing down. The prime threats identified and analysed include:
- Ransomware
- Malware
- Social engineering
- Threats against data
- Threats against availability: Denial of Service
- Threat against availability: Internet threats
- Information manipulation and interference
- Supply chain attacks

For each of the identified threats, we determine impact, motivation, attack techniques, tactics and procedures to map relevant trends and propose targeted mitigation measures. During the reporting period, key findings include:
- DDoS and ransomware rank the highest among the prime threats, with social engineering, data related threats, information manipulation, supply chain, and malware following.
- A noticeable rise was observed in threat actors professionalizing their as-a-Service programs, employing novel tactics and alternative methods to infiltrate environments, pressure victims, and extort them, advancing their illicit enterprises.
- ETL 2023 identified public administration as the most targeted sector (~19%), followed by targeted individuals (~11%), health (~8%), digital infrastructure (~7%) and manufacturing, finance and transport.
- Information manipulation has been as a key element of Russia’s war of aggression against Ukraine has become prominent.
- State-nexus groups maintain a continued interest on dual-use tools (to remain undetected) and on trojanising known software packages. Cybercriminals increasingly target cloud infrastructures, have geopolitical motivations in 2023 and increased their extortion operations, not only via ransomware but also by directly targeting users.
- Social engineering attacks grew significantly in 2023 with Artificial Intelligence (AI) and new types of techniques emerging, but phishing still remains the top attack vector.

The key findings and judgments in this assessment are based on multiple and publicly available resources which are provided in the references used for the development of this document. The report is mainly targeted at strategic decision-makers and policy-makers, while also being of interest to the technical cybersecurity community.

ENISA THREAT LANDSCAPE 2023
October 2023

5

# 1. THREAT LANDSCAPE OVERVIEW
In its eleventh edition, the ENISA Threat Landscape (ETL) report offers a broad overview of the cybersecurity threat landscape. Over time, the ETL has served as a crucial tool for comprehending the present state of cybersecurity within the European Union (EU), furnishing insights into trends and patterns. This, in turn, has guided pertinent decisions and prioritisation of actions and recommendations. The ETL report combines strategic and technical elements, catering to both technical and non-technical audiences. The ETL 2023 report has been validated and supported by the ENISA ad hoc Working Group on Cybersecurity Threat Landscapes (CTL)[^1] and the ENISA National Liaison Officers (NLO) Network.

Throughout the latter part of 2022 and the initial half of 2023, there was a notable escalation in cybersecurity attacks, setting new benchmarks in both the variety and number of incidents, as well as their consequences. The ongoing war of aggression against Ukraine remains a significant factor shaping the cybersecurity landscape. The phenomenon of hacktivism has seen steady expansion, marked by the emergence of numerous new groups. Concurrently, it was observed that a rise of ransomware groups took place, with the first half of 2023 witnessing an unprecedented surge in ransomware incidents, a trend that shows no signs of abating.

Additional focus was concentrated on the various kinds of impacts cyber threats have in critical sectors, including the sectors listed in the Network and Information Security Directive 2 (NISD 2). Interesting insights may be drawn from the particularities and insight of each sector when it comes to the threat landscape, as well as potential interdependencies and areas of significance. ENISA is following up by developing sectorial threat landscapes, diving deeper into the elements of each sector and providing targeted insight.

The ETL 2023 report follows the same customary approach, drawing from diverse open-source data and cyber threat intelligence sources. It pinpoints significant threats, discerns emerging trends and offers practical high-level strategies for mitigating risk. This year's ETL continues to use the officially endorsed ENISA Cyber Security Threat Landscape Methodology[^2], which was released in 2022. The ENISA CTL Methodology serves as a foundational framework for the transparent and systematic creation of comprehensive cybersecurity threat landscapes, spanning horizontal, thematic, and sector-specific perspectives. This process is characterised by rigorous data collection and analysis procedures.

## 1.1 PRIME THREATS
A series of cyber threats emerged and materialised during the reporting period. According to the findings detailed in this report, the ENISA Threat Landscape 2023 report highlights and directs attention toward eight prime threat groups (refer to Figure 1). These particular threat groups have been singled out due to their prominence over the years, their widespread occurrence and the significant impact resulting from the realisation of these threats.
- **Ransomware**
According to ENISA’s Threat Landscape for Ransomware Attacks[^3] report, ransomware is defined as a type of attack where threat actors take control of a target’s assets and demand a ransom in exchange for the return of the asset’s availability. This action-agnostic definition is needed to cover the changing ransomware threat landscape, the prevalence of multiple extortion techniques and the various goals, other than solely financial gains, of the perpetrators. Ransomware has been, once again, one of the prime threats during the reporting period, with several high profile and highly publicised incidents.
- **Malware**
Malware, also referred to as malicious code and malicious logic, is an overarching term used to describe any software or firmware intended to perform an unauthorised process that will have an adverse impact on the confidentiality, integrity or availability of a system.

[^1]: https://www.enisa.europa.eu/topics/threat-risk-management/threats-and-trends/ad-hoc-working-group-cyber-threat-landscapes.
[^2]: https://www.enisa.europa.eu/publications/enisa-threat-landscape-methodology
[^3]: ENISA Threat Landscape for Ransomware Attacks https://www.enisa.europa.eu/publications/enisa-threat-landscape-for-ransomware-attacks.

ENISA THREAT LANDSCAPE 2023
October 2023

7

- **Social Engineering**
Social engineering encompasses a broad range of activities that attempt to exploit human error or human behaviour with the objective of gaining access to information or services. It uses various forms of manipulation to trick victims into making mistakes or handing over sensitive or secret information. Users may be lured to open documents, files or e-mails, to visit websites or to grant access to systems or services. Although the lures and tricks used may abuse technology, they rely on a human element to be successful. This threat canvas consists mainly of the following attack vectors: phishing, spear-phishing, whaling, smishing, vishing, watering hole attack, baiting, pretexting, quid pro quo, honeytraps and scareware. While social engineering techniques are often used to gain initial access, they may also be used at later stages in an incident or breach. Notable examples are business e-mail compromise (BEC), fraud, impersonation, counterfeit and, more recently, extortion.
- **Threats against data**
A data breach is defined in the GDPR as any breach of security leading to the accidental or unlawful destruction, loss, alteration or unauthorised disclosure of or access to personal data transmitted, stored or otherwise processed (article 4.12 GDPR). Technically speaking, threats against data can be mainly classified as data breach or data leak. Though often used as interchangeably concepts, they entail fundamentally different concepts that mostly lie in how they happen[^4] [^5]. Data breach is an intentional cyber-attack brought by a cybercriminal with the goal of gaining to unauthorised access and release sensitive, confidential or protected data. In other words, a data breach is a deliberate and forceful attack against a system or organisation with intention to steal data. Data leak is an event (e.g. misconfigurations, vulnerabilities or human errors) that can cause the unintentional loss or exposure of sensitive, confidential or protected data (intentional attacks are sometimes referred to as data exposure).
- **Threats against availability: Denial of Service**
Availability is the target of a plethora of threats and attacks, among which DDoS stands out. DDoS targets system and data availability and, though it is not a new threat, it plays a significant role in the cybersecurity threat landscape[^6] [^7]. Attacks occur when users of a system or service are not able to access relevant data, services or other resources. This can be accomplished by exhausting the service and its resources or overloading the components of the network infrastructure[^8].
- **Threats against availability: Internet threats**
Threats to Internet availability refer to intentional or unintentional disruptions of Internet or electronic communications that result in Internet outages, blackouts, shutdowns or censorship. Internet disruptions can be due to government-directed Internet shutdowns, cyclones, massive earthquakes, power outages, cable cuts, cyberattacks, technical problems and military actions. These threats are diversifying and growing, having reached a new record in this reporting period and having caused huge monetary loss to national economies.
- **Information Manipulation**
Foreign Information Manipulation and Interference (FIMI) describes a mostly non-illegal pattern of behaviour that threatens or has the potential to negatively impact values, procedures and political processes. Such activity is manipulative in character, conducted in an intentional and coordinated manner. FIMI can be carried out by state or non-state actors, including their proxies inside and outside of their own territory, whereas in this report we study the threat regardless of its origin.
- **Supply Chain Attacks**
A supply chain attack targets the relationship between organisations and their suppliers[^9]. For this ETL report we use the definition as stated in the ENISA Threat Landscape for Supply Chain Attacks[^10] in which an attack is considered to have a supply chain component when it consists of a combination of at least two attacks. For an attack to be classified as a supply chain attack, both the supplier and the customer have to be targets. SolarWinds was one of the first revelations of this kind of attack and showed the potential impact of supply chain attacks. It

[^4]: https://blog.f-secure.com/data-breach-and-data-leak-whats-the-difference .
[^5]: https://www.upguard.com/blog/data-breach-vs-data-leak#:~:text=Simply%20put%2C%20a%20data%20leak,Apps%20data%20leak%20in%202021
[^6]: Federal Office for Information Security (BSI), The State of IT Sec in Germany, September 2020.
[^7]: Europol, Internet Organised Crime Threat Assessment (IOCTA) 2020, https://www.europol.europa.eu/activities-services/main-reports/internet-organised-crime-threat-assessment-iocta-2020.
[^8]: CISA, Understanding Denial-of-Service Attacks, November 2019. https://www.uscert.gov/ncas/tips/ST04-015.
[^9]: https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks.
[^10]: ENISA Threat Landscape for Supply Chain Attacks https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks.

ENISA THREAT LANDSCAPE 2023
October 2023

8

was observed that threat actors are continuing[^11] to feed on this source to conduct their operations and gain a foothold within organisations, to benefit from the widespread impact and large victim base of such attacks.
![Figure 1: ENISA Threat Landscape 2022 - Prime threats]

It should be noted that the aforementioned threats involve categories and refer to collections of diverse types of threats that have been consolidated into the eight areas mentioned above. Each of the threat categories is further analysed in a dedicated chapter in this report, which elaborates on its particularities and provides more specific information on findings, trends, attack techniques and mitigation vectors.

In the following figure it can be seen that ransomware and DDoS attacks were the most reported forms of attack during the reporting period and accounted for nearly half of the observed events followed by threats related to data. Moreover, we need to stress out that in several cases incidents involved more than one threat category and were thus analysed in the context of all respective categories. Given that the ETL is based on publicly available information and the fact that such information might not always provide the full picture, in certain cases incidents were not able to be classified into any threat category.
![Figure 2: Breakdown of analysed incidents by threat type (July 2022 till June 2023)]

## 1.2 KEY TRENDS
The list below summarises the main trends observed in the cyber threat landscape during the reporting period. Further details and analysis on the trends may be found throughout the various chapters that comprise the ENISA threat landscape of 2023.
- Ransomware and threats against availability ranked at the top during the reporting period.
- Resourceful threat actors have been observed to misuse legitimate tools primarily to prolong their cyber espionage operations . Their aim was to evade detection for as long as possible and obscure their activities by using widely available software from most systems which makes it more challenging for defenders to identify them. Maximizing their chances of success when it comes to an intrusion by not arousing victim’ suspicions
- Geopolitics continue to have a strong impact on cyber operations.
- Several threat actors further professionalised[^12] [^13] their As-a-Service programmes. They not only used novel tactics and methods to infiltrate environments but also delved into alternative approaches to pressure and extort victims, all the while advancing their illicit enterprises.
- By Using Extortion Only Techniques criminal organisations have been progressively blending extortion methods that almost invariably incorporate some form of data theft. Double extortion has witnessed a notable rise, with certain groups even relying solely on the act of stealing information.
- Increased operations by law enforcement, such as the takedown of Hive ransomware group's IT infrastructure or Trickbot.
- Cl0p rose in the first half of 2023 with the weaponisation of two zero-days.
- One of the biggest malware threats is still information stealers such as Agent Tesla, Redline Stealer and FormoBook.
- There is a steady decline in classic mobile malware, with adware remaining in numbers of occurrences the most prevalent threat to mobile devices while in terms of impact spyware can be seen as the most prevalent threat to mobile devices.

[^11]: Accenture Cyber Threat Intelligence Report https://www.accenture.com/ae-en/insights/security/cyber-threat-intelligence.
[^12]: PWC - Cyber Threats 2022: A Year in Retrospect - https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/cyber-year-in-retrospect/pdf/2022-year-in-retrospect-report.pdf.
[^13]: Group IB - Hi-Tech Crime Trends 2022/2023 –