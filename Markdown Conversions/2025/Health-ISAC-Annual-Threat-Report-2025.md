# 2025 Health Sector Cyber Threat Landscape

## Table of Contents
- [Introduction](#introduction)
- [Annual Member Survey Insights](#annual-member-survey-insights)
  - [Survey Background](#survey-background)
  - [Survey Findings](#survey-findings)
- [Key Insights](#key-insights)
- [Part I: Recent Attacks Against Healthcare](#part-i-recent-attacks-against-healthcare)
  - [Patient Extortion](#patient-extortion)
  - [High-Impact Ransomware Attacks](#high-impact-ransomware-attacks)
  - [Physical Security](#physical-security)
- [Part II: The Current Threat Landscape](#part-ii-the-current-threat-landscape)
  - [Supply Chain Attacks](#supply-chain-attacks)
  - [Cybercriminal Activity](#cybercriminal-activity)
  - [Significant Takedowns](#significant-takedowns)
    - [Operation Cronos](#operation-cronos)
    - [Operation Endgame](#operation-endgame)
    - [Operation Morpheus](#operation-morpheus)
    - [Operation Magnus](#operation-magnus)
  - [Most Active Ransomware Gangs Attacks](#most-active-ransomware-gangs-attacks)
    - [LockBit 3.0](#lockbit-30)
    - [BianLian](#bianlian)
    - [INC Ransomware](#inc-ransomware)
    - [Ransomhub](#ransomhub)
    - [QiLin Ransomware](#qilin-ransomware)
  - [Nation-State Activity](#nation-state-activity)
    - [APT29 WINELOADER Campaign](#apt29-wineloader-campaign)
    - [UTA0178 Exploitation of Ivanti Vulnerabilities](#uta0178-exploitation-of-ivanti-vulnerabilities)
    - [North Korean Remote IT Workers](#north-korean-remote-it-workers)
  - [Geopolitical Activity](#geopolitical-activity)
    - [Russia/Ukraine War Escalation](#russiaukraine-war-escalation)
    - [Threats to EU Energy Infastructure](#threats-to-eu-energy-infastructure)
    - [Middle East Escalation](#middle-east-escalation)
  - [Medical Device Security](#medical-device-security)
    - [Health-ISAC Medical Device Vulnerability Research](#health-isac-medical-device-vulnerability-research)
    - [Medical Devices Connected to Unsecured Networks](#medical-devices-connected-to-unsecured-networks)
    - [Exposed Imaging Servers](#exposed-imaging-servers)
- [Part III: Tactics, Techniques and Procedures](#part-iii-tactics-techniques-and-procedures)
  - [Social Engineering](#social-engineering)
    - [Help Desk Targeting](#help-desk-targeting)
    - [TOAD Campaigns](#toad-campaigns)
    - [Spam Bomb Social Engineering](#spam-bomb-social-engineering)
  - [Most Shared Malware Observables by Family](#most-shared-malware-observables-by-family)
  - [Top 5 Malware Families Share by the Health-ISAC Membership](#top-5-malware-families-share-by-the-health-isac-membership)
  - [Breakdown of 2024 IOC Distribution](#breakdown-of-2024-ioc-distribution)
  - [Notable Vulnerabilities and Exposures](#notable-vulnerabilities-and-exposures)
    - [RDP Exposures](#rdp-exposures)
    - [Ivanti Connect](#ivanti-connect)
    - [FortiOS](#fortios)
    - [MOVEit Transfer Authentication Bypass](#moveit-transfer-authentication-bypass)
    - [Check Point](#check-point)
- [Part IV: Future Cybersecurity Outlook](#part-iv-future-cybersecurity-outlook)
  - [Business Resilience](#business-resilience)
    - [Ransomware Attacks on Blood Suppliers](#ransomware-attacks-on-blood-suppliers)
    - [CrowdStrike Outage](#crowdstrike-outage)
    - [OpenAI Microsoft Disruptions](#openai-microsoft-disruptions)
  - [Emerging Cybercriminal Threats](#emerging-cybercriminal-threats)
  - [Post-Quantum Cryptography](#post-quantum-cryptography)
- [A Call to Action](#a-call-to-action)

TLP:WHITE

February 2025

2025 Health Sector
Cyber Threat Landscape

TLP:WHITE This report may be shared without restriction.

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

## Contents

Introduction                                                                           1

Annual Member Survey Insights

 2
Survey Background  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  2
Survey Findings   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  3

Key Insights                                                                          4

Part I: Recent Attacks Against Healthcare                        5
Patient Extortion    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  5
High-Impact Ransomware Attacks  .  .  .  .  .  .  .  .  .  .  .  .  6
Physical Security.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  7

Supply Chain Attacks . . . . . . . . . . . . . . . . . . . .

8

Part II: The Current Threat Landscape                               8
Ivanti .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  8
Cybercriminal Activity .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  9
XZ Utils    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  9
Brute Patel  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  9
Significant Takedowns  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  9

Operation Cronos .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .9

Operation Endgame   . . . . . . . . . . . . . . . . . . . .

10

Operation Morpheus  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 10

Operation Magnus   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 10
Most Active Ransomware Gangs Attacks  .  .  .  .  .  .  .  11

LockBit 3.0    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  11

BianLian  . . . . . . . . . . . . . . . . . . . . . . . . . . .

11

INC Ransomware .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 12

Ransomhub  . . . . . . . . . . . . . . . . . . . . . . . . .

12

QiLin Ransomware  . . . . . . . . . . . . . . . . . . . . .

12
Nation-State Activity   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  13

APT29 WINELOADER Campaign  .  .  .  .  .  .  .  .  .  .  .  .  . 13

UTA0178 Exploitation of Ivanti Vulnerabilities   . . . . .

13

North Korean Remote IT Workers   . . . . . . . . . . . .

13
Geopolitical Activity .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  14

Russia/Ukraine War Escalation .  .  .  .  .  .  .  .  .  .  .  .  .  . 14

Threats to EU Energy Infastructure    . . . . . . . . . . .

14

Middle East Escalation .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
14

Medical Device Security   . . . . . . . . . . . . . . . . .

Health-ISAC Medical Device Vulnerability Research  .  . 14

Medical Devices Connected to Unsecured Networks   . 15

Exposed Imaging Servers  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 15

Part III: Tactics, Techniques and Procedures

16
Social Engineering.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  16

Help Desk Targeting   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 16

TOAD Campaigns    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 16

Spam Bomb Social Engineering   . . . . . . . . . . . . .

16
Most Shared Malware Observables by Family    .  .  .  17
Top 5 Malware Families Share by the Health-ISAC
Membership  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  17
Agent Tesla    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .17
Remcos RAT  . . . . . . . . . . . . . . . . . . . . .
17
AsyncRAT   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .17
DarkGate . . . . . . . . . . . . . . . . . . . . . . .
XWorm . . . . . . . . . . . . . . . . . . . . . . . .

18
18
Breakdown of 2024 IOC Distribution  . . . . . . . . . .
Notable Vulnerabilities and Exposures  .  .  .  .  .  .  .  .  .  20
RDP Exposures .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .20
Ivanti Connect   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .20
FortiOS .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .21
MOVEit Transfer Authentication Bypass .  .  .  .  .  .  .  .21
Check Point.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .21

18

Part IV: Future Cybersecurity Outlook

22
Business Resilience    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  22
Ransomware Attacks on Blood Suppliers  .  .  .  .  .  .  .22
CrowdStrike Outage    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .22
23
OpenAI Microsoft Disruptions    .  .  .  .  .  .  .  .  .  .  .  .23
Post-Quantum Cryptography  . . . . . . . . . . . . .

Emerging Cybercriminal Threats      . . . . . . . . . . .

23

A Call to Action                                                                  24

B

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

## Introduction

2024 was a challenging year in cybersecurity for health sector systems around the
world. The Health-ISAC 2025 Health Sector Cyber Threat Landscape highlights a
continued escalation of cyberattacks. Key findings include a surge in ransomware
attacks, with increasingly sophisticated techniques employed by threat actors.
The report also emphasizes the growing threat of nation-state actors and cyber-
espionage, targeting sensitive patient data and intellectual property. Furthermore,
the rise of Internet of Medical Things (IoMT) devices has introduced new
vulnerabilities, while the evolving threat landscape necessitates continuous
adaptation of security measures for health sector organizations globally.

1

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

## Annual Member Survey Insights

### Survey Background

In Health-ISAC’s November 2024 survey, nearly 200 executives and cybersecurity
professionals across the health sector completed a survey and ranked their top
five “greatest cybersecurity concerns” facing their organizations for both 2024
and 2025. The survey included cyber (e.g., CISO) and non-cyber executives
(e.g., CFO), multiple health subsectors (e.g., Providers, Pharma, Payers, Medical
Device Manufacturers, Health IT) as well as healthcare organizations of varying
size and IT/IS budget.

  Survey responses were received from members of:

* Health-ISAC
* Association for the Advancement of Medical Instrumentation (AAMI)
* American College of Clinical Engineering (ACCE)

2

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

## Survey Findings

Health sector security professionals reported the Top Five Cyber Threats facing their organizations in 2024
as follows:

1.  Ransomware
2.  Phishing
3.  Compromised Credentials
4.  Third-Party Credentials
5.  Data Breaches

Health sector security professionals reported the Top Five Cyber Threats facing their organizations looking
ahead in 2025 are:

1.  Ransomware Deployments
2.  Third-Party Breaches
3.  Data Breaches
4.  Supply Chain Attacks
5.  Zero-Day Exploits

Medical Device Manufacturers reported the top three challenges in developing secure medical devices as:

1. Integrating security into the design and development process.
2. Providing regular and secure updating and patching for medical devices.
3. Designing for the ongoing security of medical devices over their long operational lifespan.

Conversely, the top three impacts on Healthcare Delivery Organizations were reported as:

1. Disruption in the normal operation of medical technology, including such things as loss of diagnostic
   technology or loss of access to electronic medical records which may cause delay and disruption to
   patient care, such as diversion of patients and ambulances, canceled surgeries, or the need to revert to
   manual procedures.
2. Unauthorized access, theft, or exposure of patients’ personal health information (PHI), resulting in
   privacy violations and legal consequences.
3. Disruption of overall hospital operations, including administrative processes, scheduling, and
   communication.

Survey demographic information, findings, and additional insights appear in the Appendix of this report.

3

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

## Key Insights

* The top three impacts on Healthcare Delivery Organizations remained the
  same from 2024 to 2025.
* Organizations with cybersecurity budgets in both the highest and lowest
  brackets listed AI-enabled attacks as their primary concern going into 2025
  despite the collective consensus across the membership being ransomware
  deployments as the greatest threat going into 2025.
* The concerns going into 2025 reflect a highlighted concern about third-party
  breaches using zero-day exploits. Three of the top five concerns relate to this
  scenario, similar to the exploitation of MoveIT Managed File Transfer in 2023.

4

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

## Part I: Recent Attacks Against Healthcare

### Patient Extortion

After a cyber-attack on the Integris Health System, in December 2023, patients of numerous hospitals,
specialty care clinics, and other institutions began to receive emails from a threat actor attempting to
blackmail them with data stolen in the cyber-attack. These emails alleged the threat actor had information
from a stolen database that included the details of medical visits, social security numbers, and other
sensitive Protected Health Information (PHI) belonging to patients. Victims were presented with three
options. First, victims could pay $50 to delete their entry in the stolen dataset of approximately 500,000
records. Second, they could pay $3 to view what data was compromised in the attack. Finally, they could opt
not to pay and be a part of the dataset that was going to be sold on the dark web.[^1]

Unfortunately, this is not an isolated incident. The previous year, patients from cancer centers were extorted
using stolen mammogram pictures, and patients at plastic surgery clinics were extorted with stolen sensitive
pre-operation photos. This worrying trend may begin to gain traction in 2025 as cybercriminal actors target
healthcare even more.[^2]

This worrying trend may begin to gain traction in 2025 as cybercriminal
actors target healthcare even more.

[^1]: https://www.bleepingcomputer.com/news/security/integris-health-patients-get-extortion-emails-after-cyberattack/
[^2]: https://www.lehighvalleynews.com/health-news/2023-03-07/hackers-posted-photos-of-lvhn-cancer-patients-receiving-treatment-hospital-says

5

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

### High-Impact Ransomware Attacks

#### Payment Portal Outage

Change Healthcare is a massive healthcare payment processing
conglomerate that is widely adopted across American healthcare delivery
organizations. According to some estimates, Change Healthcare processes
about one in three healthcare transactions in the US.[^3] The ransomware attack
that befell this organization in February 2024 created an outage that disrupted
patient care in such a way that millions of patients could no longer pay for
treatment or medication.

> Due to the
> payment portal
> outage, “millions
> of patients could
> no longer pay
> for treatment or
> medication.”

Affiliates of the ransomware as a service (RaaS) group, BlackCat/ALPHV,
claimed responsibility for the attack. However, the administrators of the RaaS platform kept the money made
from the hack, swindling the affiliates who carried out the attack on Change Healthcare. After this, the group
decided to disband, announcing on social media that the RaaS operation had ended.[^4]

#### Ascension Healthcare

On May 8, 2024, Ascension Healthcare discovered a ransomware incident
in their network. To remediate the situation, Ascension Health took many
systems offline to reduce the impact of the incident. As a result, several
functions of the large healthcare network were unavailable, resulting in
massive disruptions to patient care across the 40 senior care facilities and
140 hospitals across 19 states. This incident caused lapses in access to
electronic health records, making it much harder to treat patients. As a result,
ambulances were diverted away from hospitals in the Ascension Healthcare
network, and appointments were postponed. To respond to this incident,
Health-ISAC worked with Ascension and shared Indicators of Compromise
(IOCs) with the wider membership.[^5] The group responsible for the attack was
Black Basta, a prolific ransomware gang.

Disruptions in

140

Hospitals

40

Senior Care

Facilities

Black Basta emerged in early 2022 and has continuously targeted healthcare
organizations. Black Basta has used double extortion tactics to encrypt data and threaten to leak sensitive
information, allegedly extorting over $100 million. Their malware targets Windows and Linux systems,
employing sophisticated techniques to prevent detection and hinder file recovery. The threat actor used
spearphishing attacks and was seen buying compromised credentials through Initial Access Brokers (IABs)
to obtain means of initial access.

[^3]: https://www.webmd.com/health-insurance/news/20240325/change-healthcare-cyberattack-what-consumers-should-know
[^4]: https://www.bleepingcomputer.com/news/security/blackcat-ransomware-turns-off-servers-amid-claim-they-stole22-million-ransom/
[^5]: https://apnews.com/article/cyberattack-hospital-system-ambulances-diverted-ascension-728ab2a0e5afaf7c344e46a5ce5ca42c

6

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

### Physical Security

Physical threats to the healthcare sector persisted through 2024. Some of the major threats observed this
year were seasonal outbreaks of diseases, continued threats of workplace violence, protests concerning
working conditions, and controversy surrounding the legal status of various medical procedures and
medications. Although the issues have remained relatively similar, the sector has taken new steps to mitigate
risks and improve administrative processes.

Throughout 2024 there have been increased outbreaks of seasonal diseases including dengue fever,
pertussis d (whooping cough), and COVID-19 strains. There has also been increased attention on Avian Flu
due to the increased infection rates from fowl and cattle populations. However, the most significant outbreak
of the year has been a new strain of Mpox clade 1b that has spread rampantly across African nations. There
have been few cases reported outside of Africa in Sweden, Thailand, India, and the United Kingdom. This
strain is easier to contract because it spreads through close contact. The World Health Organization (WHO)
declared a global public health emergency in August 2024, drawing more attention from external nations to
the potential spread of the virus.[^6]

Workplace violence has also been a consistent issue in 2024, with increased reports of acts of violence
toward healthcare staff reported all over the globe. The issue has inspired different methods of mediation.
In the US, many state legislators have increased penalties for assaulting healthcare staff. The issue has also
contributed to global protests.[^7]

Notably, protests broke out in August 2024 and have continued with varying levels of intensity throughout
the year in India. The protests began after a medical student was found murdered, which spurred a string of
protests against workplace violence facing healthcare staff and women. The protests called for increased
protections in healthcare facilities and improved working conditions. Additional healthcare-related protests
have continued sporadically around the globe with the majority being focused on increased pay and
improved working conditions. This tension in healthcare was present in 2024. In South Korea, tensions
carried over from protests that occurred in 2023 after the government installed requirements for increased
training and hiring of medical staff. Medical professionals saw it as a challenge to their job security and
salaries and walked out in protest, with many never returning.[^8]

Controversy continues to surround gender-affirming care and abortion. In response to the overturning of Roe
v. Wade in 2022, the requirements to get access to Mifepristone have loosened, making it more available.
There were legal battles concerning its accessibility, though the Supreme Court ruled in favor of the pill.[^9]

[^6]: https://www.who.int/news/item/14-08-2024-who-director-general-declares-mpox-outbreak-a-public-health-emergency-of-international-concern
[^7]: https://www.facs.org/for-medical-professionals/news-publications/news-and-articles/bulletin/2024/october-2024-volume-109-issue-9/violence-
escalates-against-surgeons-and-other-healthcare-workers/
[^8]: https://www.newindianexpress.com/nation/2024/Aug/17/one-of-indias-largest-medical-service-shutdowns-says-ima-chief-as-doctors-24-hour-
strike-takes-effect
[^9]: https://journals.lww.com/ajnonline/Fulltext/2023/04000/News_Brief__The_FDA_has_loosened_restrictions_to.15.aspx

7

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

## Part II: The Current Threat Landscape

### Supply Chain Attacks

In the early months of 2024, threat actors identified and exploited several
vulnerabilities in various Ivanti tools.

On January 10, 2024, Ivanti released a security update to address two zero-day vulnerabilities actively being
exploited in the wild. Both vulnerabilities (CVE-2023-46805 and 2024-21887) were discovered in all supported
versions (9.x and 22.x) of Ivanti Connect Secure, formerly known as Pulse Secure and Ivanti Policy
Secure Gateways. According to Ivanti, authentication is not required when CVE-2024-21887 is leveraged in
conjunction with CVE-2023-46805, allowing a threat actor to craft malicious requests and execute arbitrary
commands on the system. These vulnerabilities were also seen being used to deploy Mirai botnet attacks in
May 2024.[^10]

On January 31, 2024, Ivanti disclosed two new vulnerabilities, CVE-2024-21893 and CVE-2024-21888, which
were also observed to be exploited in the wild. In the update, CVE-2024-21893 is now reported as being
leveraged by adversaries to install a novel DSLog backdoor on compromised Ivanti devices. The CVE-
2024-21893 is a server-side request forgery (SSRF) flaw affecting the SAML component of Ivanti Connect
Secure, Policy Secure, and Neurons for ZTA. The flaw allows attackers to bypass authentication and access
restricted resources on affected devices.[^11]

On February 8, 2024, Ivanti warned of a new authentication bypass vulnerability, identified as CVE-2024-
22024, impacting Connect Secure, Policy Secure, and ZTA gateways. Discovery of the new flaw was part
of Ivanti’s continuous investigation into vulnerabilities impacting the previously mentioned appliances.
Following the discovery of vulnerabilities in Ivanti’s Policy Secure and Connect Secure, additional information
indicating that cyber threat actors can deceive and effectively circumvent Ivanti’s internal and external
Integrity Checker Tool (ICT) detection capabilities to compromise victim networks without being detected
became available. Specifically, the vulnerabilities tracked and actively used in recent attack chains include
CVE-2023-46805 - Ivanti Policy Secure CVE-2024-21887 - Ivanti Connect Secure CVE-2024-22024 - Ivanti
Connect Secure (SAML) CVE-2024-21893 - Ivanti Connect Secure (SAML).[^12]

[^10]: https://thehackernews.com/2024/05/mirai-botnet-exploits-ivanti-connect.html
[^11]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060b
[^12]: https://forums.ivanti.com/s/article/CVE-2024-22024-XXE-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure?language=en_US

8

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

### Cybercriminal Activity

#### XZ Utils Vulnerability Impacts Linux Systems

XZ Utils is a general-purpose data compression format used in nearly every Linux distribution, community
project, and commercial product distribution. The open-source software suite allows users to compress and
decompress large file formats into smaller, more manageable sizes for sharing via file transfers. In February
2024, it was discovered that the latest versions of the XZ Utils software contained obfuscated malicious
code in its liblzma library that created a backdoor into Linux systems if it deployed on a large scale.

The supply chain compromise affected XZ Utils library versions 5.6.0 and 5.6.1. The malicious update of
this software almost made its way into Debian and Red Hat Linux distributions, but the vulnerability was
found before large-scale shipping could take place. The disclosure of CVE-2024-3049 highlights the fragility
of supply chain security, as critical systems’ underpinnings contain open-source components and leverage
their dependencies.[^13] While the XZ Utils vulnerability was not shipped out to production, it highlights the
importance of proactive security measures. In this case, vulnerability research led to this software being fixed
before it hit the market. Members are encouraged to conduct vulnerability research into proprietary software
they create prior to public sale.

#### Brute Ratel

Brute Ratel is a commercial command and control framework similar to Cobalt Strike which penetration
testers use to streamline red team engagements. Also similar to Cobalt Strike, it is being abused by threat
actors to conduct malicious command and control (C2) operations. The RaaS group BlackCat/ALPHV used
this software to deploy their ransomware payload in victim networks.[^14] Brute Ratel has been observed in
attacks against healthcare organizations.[^15] Despite this group disbanding in March 2024, Health-ISAC has
continued to observe Brute Ratel being used against healthcare organizations and shared numerous Brute
Ratel indicators throughout 2024 to help members defend against it.

### Significant Takedowns

#### Operation Cronos

Operation Cronos was the name given to the international law enforcement
operation coordinated by Europol that took down a significant amount of
LockBit infrastructure. LockBit is a RaaS group that provides infrastructure
for threat actors, referred to as affiliates, to use in ransomware attacks. For
a portion of the money made during the attack, RaaS platforms provide
ransomware-specific software like a platform for negotiations with victims,
encryptors, and a leak site where affiliates can leak the data of organizations
that do not pay the ransom.

As a result of the takedown, 34 LockBit servers were seized, about 200
cryptocurrency accounts were frozen, and several affiliates were unmasked.
Following the operation, a free decryption key was released to help victims of
LockBit ransomware attacks.[^16]

 34

LockBit Servers
Seized

200

Cryptocurrency

accounts frozen

[^13]: https://arstechnica.com/security/2024/04/what-we-know-about-the-xz-utils-backdoor-that-almost-infected-the-world/
[^14]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
[^15]: https://blackpointcyber.com/resources/blog/brute-ratel-advanced-ip-scanner-netsupport-rat-blackpoint-soc-apg
[^16]: https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-disrupt-worlds-biggest-ransomware-operation

9

health-isac.org

---

# 2025 Health Sector Cyber Threat Landscape

#### Operation Endgame

Operation Endgame was the name of the international law enforcement
operation spearheaded by Europol that took down several Malware as a
Service (MaaS) platforms. As part of Operation Endgame, Europol and global
partners took various actions to neutralize the threat posed by at least four
malware groups, including IcedID, SmokeLoader, Pikabot, and Bumblebee.
These malware groups infected millions of computers and claimed countless
victims around the world and throughout the US. Victims also included a
hospital network, which not only cost millions of dollars to recover from but
alarmingly put people’s lives at risk due to the compromised critical care online
system.[^17]

#### Operation Morpheus

Europol led an operation called Morpheus that successfully disabled nearly
600 Cobalt Strike servers used by cybercriminals for network infiltration after
a three-year investigation. The operation involved law enforcement from
multiple countries, including the UK, US, and Australia, along with support
from private sector partners from the cybersecurity industry, who provided
advanced telemetry and security tools. Throughout a week in late June 2024,
law enforcement identified IP addresses linked to criminal activities. The IP
addresses were sent to online service providers to shut down unauthorized
versions of the tool, resulting in the takedown of 593 addresses. Cobalt Strike,
a legitimate penetration testing tool sold by Fortra to help cyber experts identify
weaknesses in their systems, has been repurposed by threat actors
for malicious purposes, such as ransomware and cyber espionage, prompting
legal actions against its cracked versions.[^18]

#### Operation Magnus

On October 28, 2024, Operation Magnus, an international law enforcement
operation against the Meta and Redline infostealer malware distribution
networks, was announced. According to the video announcement, European
and American law enforcement agencies gained access to the production
servers behind the malware-as-a-service (MaaS) schemes that sold Red