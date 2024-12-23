# Defending the Expanding Attack Surface
Trend Micro 2022 Midyear Cybersecurity Report

## Table of Contents
- [TREND MICRO LEGAL DISCLAIMER](#trend-micro-legal-disclaimer)
- [Contents](#contents)
- [Threat Actors Focus on Advancing Capabilities, Expanding the Digital Attack Surface, and Capitalizing on Current Issues](#threat-actors-focus-on-advancing-capabilities-expanding-the-digital-attack-surface-and-capitalizing-on-current-issues)
- [The Ransomware Threat Landscape Continues to Evolve with New Players and Lucrative Monetization Methods](#the-ransomware-threat-landscape-continues-to-evolve-with-new-players-and-lucrative-monetization-methods)
- [Software Vulnerabilities Threaten to Disrupt the Operations of Businesses](#software-vulnerabilities-threaten-to-disrupt-the-operations-of-businesses)
- [Old Issues, Unconventional Attacks Plague Cloud Environments](#old-issues-unconventional-attacks-plague-cloud-environments)
- [The Evolving Attack Surface Requires Effective Multilayered Defenses and Security Technologies](#the-evolving-attack-surface-requires-effective-multilayered-defenses-and-security-technologies)
- [The Threat Landscape in Brief](#the-threat-landscape-in-brief)
- [References](#references)

TREND MICRO LEGAL DISCLAIMER

The information provided herein is for general information 
and educational purposes only. It is not intended and 
should not be construed to constitute legal advice. The 
information contained herein may not be applicable to all 
situations and may not reflect the most current situation. 
Nothing contained herein should be relied on or acted 
upon without the benefit of legal advice based on the 
particular facts and circumstances presented and nothing 
herein should be construed otherwise. Trend Micro 
reserves the right to modify the contents of this document 
at any time without prior notice.

Translations of any material into other languages are 
intended solely as a convenience. Translation accuracy 
is not guaranteed nor implied. If any questions arise 
related to the accuracy of a translation, please refer to 
the original language official version of the document. Any 
discrepancies or differences created in the translation are 
not binding and have no legal effect for compliance or 
enforcement purposes.

Although Trend Micro uses reasonable efforts to include 
accurate and up-to-date information herein, Trend Micro 
makes no warranties or representations of any kind as 
to its accuracy, currency, or completeness. You agree 
that access to and use of and reliance on this document 
and the content thereof is at your own risk. Trend Micro 
disclaims all warranties of any kind, express or implied. 
Neither Trend Micro nor any party involved in creating, 
producing, or delivering this document shall be liable 
for any consequence, loss, or damage, including direct, 
indirect, special, consequential, loss of business profits, 
or special damages, whatsoever arising out of access to, 
use of, or inability to use, or in connection with the use of 
this document, or any errors or omissions in the content 
thereof. Use of this information constitutes acceptance for 
use in an “as is” condition.

Published by 
Trend Micro Research

Stock image used under license from 
Shutterstock.com

## Contents
Threat Actors Focus on Advancing 
Capabilities, Expanding the Digital Attack 
Surface, and Capitalizing on Current 
Issues
4
The Ransomware Threat Landscape 
Continues to Evolve with New Players 
and Lucrative Monetization Methods
12
Software Vulnerabilities Threaten to 
Disrupt the Operations of Businesses
20
Old Issues, Unconventional Attacks 
Plague Cloud Environments
29
The Evolving Attack Surface Requires 
Effective Multilayered Defenses and 
Security Technologies
35
The Threat Landscape in Brief
37

The first half of 2022 saw large sections of the workforce either returning to the physical workplace 
or transitioning to a hybrid setup consisting of a combination of both work-from-home (WFH) and 
on-site work. For many organizations that have transitioned their employees to remote working 
environments during the past couple of years, these changes mean facing an ever-growing attack 
surface in the new normal, where security teams must contend with the challenge of defending all 
possible sections of the IT infrastructure. 

Ransomware developers continued their shift toward more lucrative and efficient monetization 
methods, particularly the ransomware-as-a-service (RaaS) model that has been credited as one of 
the key reasons for the rapid spread of ransomware attacks. In the first half of the year, three RaaS 
threat actors stood above the rest: Conti, LockBit, and BlackCat, each of which saw significantly 
higher detections in the first half of the year compared to the first half of 2021, indicating that 
cybercriminals are increasingly turning toward a RaaS partnership due to the benefits it provides 
for both parties. We also observed relatively new ransomware families such as Black Basta, 
Nokoyawa, and Hive being used in high-profile attacks on big-game targets.

The first half of 2022 also saw the emergence of advanced persistent threat (APT) groups that 
employed sophisticated toolkits and expansive infrastructure in their campaigns. At the same time, 
threat actors continued to turn to commodity malware, integrating older tools and malware into 
their attack routines for their capabilities and reliability. We have also observed that cybercriminals 
are seemingly looking to expand their operations beyond non-Windows operating systems, with 
Linux increasingly coming under fire. In their endless pursuit to benefit from any situation, malicious 
actors also capitalized on the Russia-Ukraine hostilities to launch cyberattacks on either side or 
prey on people interested in the conflict.

Based on Trend Micro™ Zero Day Initiative™ (ZDI) data, there was a rise in the number of published 
vulnerability advisories in general, as well as in critical- and high-severity flaws during the first 
half of 2022. We focused on some of the noteworthy critical vulnerabilities that targeted crucial 
business tools and software that are used in enterprise systems while also taking note of the 
vulnerabilities that affected macOS and Linux. We also delved into the Data Distribution Service 
Standard (DDS) and the vulnerabilities that might have a potential impact on the machines and 
devices that use this standard.

The cloud remains a popular target for malicious actors, with some capitalizing on old and 
persistent issues such as misconfiguration and others attempting to develop more novel and 
unconventional methods to launch attacks on cloud infrastructure. 

In our 2022 midyear roundup, we examine the most significant trends and incidents that influenced 
the cybersecurity landscape in the first half of the year. We also review our 2022 security predictions 
to see which ones aligned with the trends in the first six months of the year. Through this report, 
we hope to enlighten users and organizations not just on the different threats that they face 
but also the robust security measures and policies that they need to consider to protect their 
environments and systems in the face of a growing attack surface that requires equally capable 
and extensive security measures.

4 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

## Threat Actors Focus on Advancing Capabilities, Expanding the Digital Attack Surface, and Capitalizing on Current Issues
### Organizations Express Concern Over the Growing Attack Surface
Over the past few years, many companies have risen to the challenge of digital transformation by 
adopting digital technologies to modify their existing business models, processes, and company cultures. 
This transformation has subsequently created a wider digital attack surface that encompasses a broader 
range of areas, including email inboxes, internet-of-things (IoT) devices, mobile applications, websites, 
public cloud services, and even the supply-chain infrastructure. 

In a study we conducted in partnership with Sapio Research, we surveyed 6,297 IT security decision-
makers from 29 countries about their thoughts on the risks brought about by the growing attack surface.[^1] 
We discovered that a significant number (73%) of them were concerned about the size of their digital 
attack surface. 37% described their situation as constantly evolving and messy, while another 43% 
argued that the attack surface is spiraling out of control.

Despite these concerns, 62% of the respondents admitted to having blind spots that weaken their security 
posture. 37% of the organizations also claimed to have the least insight into cloud assets. 35% said the 
same of their insights into networks, while 32% responded that they have the least insight into their end-
user assets.

It also became clear that a number of these organizations were uncertain about how to proceed given the 
risks that they face. 38% of respondents identified quantifying cyber risk as their primary challenge, while 
33% stated that they simply lack the resources to understand and manage these risks. Another 32% 
cited that they have limited visibility into the areas that are at risk.

5 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

![Figure 1. A survey of 6,297 IT security decision-makers reveals that a significant number of them are concerned about the digital attack surface. Source: Trend Micro survey in partnership with Sapio Research]

73% of IT security decision
makers are concerned about
the digital attack surface.

43% argue that the
attack surface is
spiraling out of control.

37% describe the attack
surface as constantly
evolving and messy.

![Figure 2. IT security decision-makers name cloud assets, networks, and end-user assets as the top three areas where they have the least security insights into. Source: Trend Micro survey in partnership with Sapio Research]

37% Cloud assets
34% Networks
32% End-user assets
Areas where organizations have the least security insight into

### Threat Actors Like Earth Lusca and Earth Berberoka Continue to Use Wide-Ranging Tools and Extensive Infrastructure in Their Attacks
The first half of 2022 saw the continuation of targeted campaigns involving APT groups that play the long 
game by employing large infrastructure and integrating different kinds of malware and other tools in their 
attacks. 

One of the prominent APT groups from the first half of 2022 was the Earth Lusca, a threat actor that has 
been active since mid-2021[^2] and which conducts cyberespionage and financially motivated campaigns 
targeting a wide range of organizations around the world by using spear-phishing lures and watering holes. 

6 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

The group employs infrastructure that can be divided into two clusters. The first is built via rented virtual 
private servers (VPSs) that are used for Earth Lusca’s social engineering attacks. The group also uses 
these as their command-and-control (C&C) servers. In particular, Earth Lusca uses the C&C server that 
is connected to this cluster to deploy a number of malware families such as Cobalt Strike, ShadowPad, 
Funny Switch, and Winnti. 

The second cluster is composed of compromised servers that run older, open-source versions of Oracle 
GlassFish Server. This cluster is used for vulnerability scanning in public-facing servers and building 
traffic tunnels within the network. The group also uses it as a C&C server for Cobalt Strike.

![Figure 3. Earth Lusca’s infection routine showing the two clusters the group employs in its attacks]

Threat actor
(China)
Compromised
servers
Public-facing server
Internal servers
Exploit recon
Watering hole
Spear phishing
Lateral movement
C&C callback
CobaltStrike callback
EarthWorm tunneling
VPN/Proxy
servers
VPSs
Victim’s computer

A large portion of the threat actor’s primary victims seem to be high-value targets such as government 
and educational institutions, political groups, news media, and even Covid-19 research organizations. 
In April 2022, we published a research paper documenting the activities of an APT group we named Earth 
Berberoka that primarily targets gambling websites in China.[^3] The group, which has been active since at 
least 2020, uses a wide range of malware families that share the same back-end infrastructure despite 
targeting different operating systems (Windows, Linux, and macOS).

In addition to its extensive list of malware families, Earth Berberoka employs several different infection 
vectors: an allegedly secure chat app called MiMi, a bogus cryptocurrency app, and a website hosting a 
malicious Adobe Flash Player installer.

Another notable intrusion set we encountered in the first half of 2022 is NetDooka, a multicomponent 
malware framework that is distributed via a pay-per-install (PPI) service.[^4] The framework, which contains 
a loader, a dropper, a protection driver, and a remote access trojan (RAT), uses the PrivateLoader malware 
for distribution. According to a report from Intel471, PrivateLoader infects a user’s machine through 
downloaded pirated software.[^5]

7 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

Following infection, it installs the first NetDooka malware, a dropper component that decrypts and executes 
the loader. After scanning the environment, the loader then downloads another dropper component that 
is executed by the loader. This dropper will be used for decrypting and executing the final payload, a full-
featured RAT that can perform various functions such as starting a remote shell, grabbing browser data, 
and taking screenshots.

The infrastructure of NetDooka makes it an attractive option for clients that want to avail of the PPI 
business model for their operations while also allowing their operators the opportunity to easily spread 
their malware.

### Threat Actors Like Conti Drive Emotet Resurgence
> In our 2022 security predictions, we 
foresaw that commodity malware 
would grow into a formidable threat as 
ransomware operators continuously 
integrate it into their attacks.
>
> Predictions

Although new malware families often garner the lion’s 
share of attention from both the security industry and 
the general public, older malware, especially those 
that have proven to be effective, still pose a threat 
to organizations. In our 2022 security predictions, 
we mentioned that malicious actors are increasingly 
turning to commodity malware and other tools to 
make their attacks more effective.[^6] This has turned 
out to be an accurate prediction for Emotet, an infamous botnet that is being offered as part of a malware-
as-a-service (MaaS) scheme.

![Figure 4. Infection chain used in the Emotet infections we analyzed in May 2022]

Arrival
Installation
Routines
6
Creates service
(if with admin rights)
5
Deletes 
Zone.Identiﬁer ADS
4
Drops copy
a. %System%\<ﬁle name>.exe
b.%AppData%\Local\Microsoft\
     Windows\<ﬁle name>.exe
3
Emotet
7
List running processes
8
Get system and
operation system info
10
11
9
Send info to
C&C server
Execute modules
received from C&C server
1
2
Malicious
spam with URL
(subject is invoice or 
payment notiﬁcation)
Document with malicious 
macro executes 
PowerShell command line 
to download the payload.
A user selecting a URL in 
malicious spam leads to a 
download.
a. With admin rights
b. Without admin rights
     Service name/Regrun
     value is the same as
     <ﬁle name>.
a. Update copy
b. Spammer module
c. Credential stealer module
d. Network propagation 
     module
Create autostart 
registry 
/h/k/c/u\%regrun%
(if without admin rights)
C&C server sends modules
to perform other routines

8 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

Emotet made its debut in 2014 and is known to have been used by operators of other malware such as 
Conti and Ryuk in their attacks. In 2021, its infrastructure was taken down through the collaborative effort 
of various law enforcement agencies from different countries.[^7]

However, the dismantling of its infrastructure did not signal the end of Emotet. Just a few months later, it 
was observed being used in a Trickbot campaign.[^8] In the first half of 2022, we saw a massive uptick in 
Emotet detections compared to those in the first half of 2021, proof that the botnet is thriving as a result 
of threat actors opting to integrate it into their operations. Indeed, researchers from Advintel named Conti 
operators as one of the reasons behind Emotet’s recent resurgence.[^9]

![Figure 5. Emotet detections increased by over 10 times in the first half of 2022 compared to the first half of 2021, likely due to prolific threat actors using it as part of their operations. Source: Trend Micro Smart Protection Network]

0
30K
60K
90K
120K
150K
1H 2022
1H 2021
13,811
148,701

Based on our Smart Protection Network (SPN) sensors, majority of the Emotet detections occurred in 
Japan, with the US, India, Italy, and Brazil rounding up the top five. While this does not necessarily 
indicate that Japan is where Emotet is most active (due to the nature of security sensors), it does show 
that the malware has high levels of activity in the country.

![Figure 6. The countries with the highest number of Emotet detections Source: Trend Micro Smart Protection Network]

0
20K
40K
60K
80K
100K
120K
Brazil
Italy
India
US
Japan
107,669
4,837
3,729
3,442
3,006

9 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

In May 2022, we analyzed Emotet infections across various regions and discovered that while the attacks 
still relied on spam campaigns, it also added small changes to its routine, such as using Excel 4.0 macros 
for its downloading procedure instead of using Visual Basic for Applications (VBA).[^10] Other changes 
that were implemented in these recent Emotet infections include streamlined payloads and additional 
obfuscation techniques. Perhaps most importantly, the operators of Emotet have since added Cobalt 
Strike to their arsenal since the botnet’s reappearance, making newer Emotet campaigns more dangerous.

### Russia-Ukraine Conflict Extends to the Cybercrime Sphere
On February 24, 2022, the Russia-Ukraine war began. While there has been much focus on physical 
battles on the ground, it’s important to highlight that cyberattacks targeting both sides were also launched 
in the ensuing chaos.[^11]

One of the prominent threat actors that became involved early on was Conti, which announced its support 
for the Russian government just a day after the hostilities started. On its leak site, the group announced 
that they would strike back at groups or individuals who launched cyberattacks on Russia, although Conti 
would subsequently soften its stance in a succeeding post.

![Figure 7. Initial statement from the Conti group warning would-be attackers of retaliation should they target Russian infrastructure]

SPN data shows a spike in BazarLoader detections in the first half of 2022 compared to the first half of 
the previous year — a notable shift since BazarLoader is a key enabler in Conti campaigns.

10 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

![Figure 8. There were nearly 10 times as many BazarLoader detections in the first half of 2022 compared to the first half of 2021. Source: Trend Micro Smart Protection Network]

0
200
400
600
800
1H 2022
1H 2021
75
686

The Stormous ransomware gang, a group of Arabic-speaking cybercriminals, also announced its support 
for Russia[^12] and declared that it would target Ukrainian government institutions as part of its plans.

Our analysis of the malware used by Stormous reveals that the group uses it to deploy different kinds of 
custom payloads to its victim through remote uploading and resources such as Pastebin.

Alongside ransomware groups becoming involved, security researchers observed attacks that, although 
not directly connected to the ongoing war, were being launched on Ukrainian organizations, websites, 
and infrastructure even before the conflict began.

In January and February 2022, a wave of spear-phishing emails was sent to Ukrainian targets — ostensibly 
from Ukrainian organizations such as the National Healthcare Service and the police force — containing 
attachments that download and execute the OutSteel and SaintBot malware.[^13] It’s possible that these 
campaigns were carried out for information-gathering purposes as a precursor to the invasion.

On January 13 and 14, 2022, threat actors launched a direct attack on approximately 70 Ukrainian 
government websites, leading to the defacement of website content and system corruption via the 
malware WhisperGate.[^14] It is suspected that these attacks were enabled via the content management 
system OctoberCMS, supply-chain attacks, and the exploitation of the Log4j vulnerability.[^15]

At first glance, these incidents belie the complexity of the attacks launched on either side of the war. As 
evidenced by a March 2022 campaign that we analyzed, however, these cyberattacks are not a one-way 
street. In this campaign, operators used a piece of malware called RuRansom designed to infect Russian 
targets. Although its name implies otherwise, RuRansom is not an example of ransomware but a wiper 
designed to destroy its victim’s data and backup files. Our discovery of numerous versions of RuRansom 
indicates that the malware is still under development.

11 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

Although several ransomware groups became involved, it would be a mistake to think that ransomware 
gangs were the only ones to take part in the Russia-Ukraine war. For example, hacktivist collective 
Anonymous took part in the cyber conflict by targeting Russian assets and information in attacks that 
included publishing confidential files from the Russian central bank, taking over state-controlled television, 
and leaking the personal data of Russian military personnel.[^16]

Other malicious actors, while not directly targeting either side of the conflict, still attempted to capitalize 
on the situation. Through our honeypot, we found war-related spam emails aiming to take advantage of 
the situation under the guise of asking for donations and using scams to create bogus recipients of such 
donations. Some of these spam emails drop malware such as Ave Maria as an attachment.[^17]

![Figure 9. A scam email asking recipients for donations to help with Ukrainian relocations]

12 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

## The Ransomware Threat Landscape Continues to Evolve with New Players and Lucrative Monetization Methods
### LockBit, Conti, and BlackCat Operators Continue to Employ the Profitable RaaS Scheme
> The advent of RaaS has resulted in would-be 
cybercriminals having access to the tools and 
infrastructure that would not have been available 
to them under ordinary circumstances.[^18] One of the 
unique aspects of the RaaS model is the relationship 
between the developers and their affiliates who act 
as middlemen. Affiliates are also responsible for the 
actual infections and split ransom payment with the 
developers. This kind of setup provides developers 
additional time to evolve their malware and tools 
>
> We predicted that ransomware 
operators would implement modern and 
sophisticated extortion methods while 
also going after more prominent targets. 
would grow into a formidable threat as 
ransomware operators continuously 
integrate it into their attacks.
>
> Predictions

while also affording them protection from the scrutiny of security researchers and law enforcement. On 
the other hand, affiliates profit from ransomware attacks without the extensive legwork and infrastructure 
needed to initiate expansive ransomware campaigns.   

Our telemetry data shows that over 50 active RaaS and extortion groups and more than 1,200 organizations 
were victimized by ransomware in the first half of the year.

13 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

![Figure 10. The number of active RaaS and extortion groups and victim organizations of successful ransomware attacks in the first half of 2022 Source: RaaS and extortion groups’ leak sites]

0
600
300
900
1.2K
1.5K
Victim
organizations
Active RaaS and
extortion groups
57
1,205

LockBit, Conti, and BlackCat were the major players in the RaaS field for the first half of 2022.[^19] Based 
on SPN data, we observed a sharp increase in detections from each of these malware families in the first 
half of this year. Black Cat, a relatively new ransomware that was initially reported at the tail end of 2021, 
understandably saw practically nonexistent detections in 2021 before the increase in 2022. However, 
even older ransomware such as LockBit and Conti saw major increases, with LockBit seeing over five 
times and Conti nearly twice the number of detections in the first half of 2022 in contrast to the first half 
of the previous year.

![Figure 11. LockBit, Conti, and BlackCat saw a significant increase in detections in the first six months of 2022 compared to the first half of the previous year: The detection numbers for LockBit, Conti, and BlackCat  Source: Trend Micro Smart Protection Network]

1H 2022
1H 2021
0
500
1K
1.5K
2K
 BlackCat
Conti
LockBit
341
1,843
1,090
1,397
622
2
1H 2021
1H 2022

LockBit, which has been active since 2019 and was initially known as the ABCD ransomware, is the 
group with the highest number of detections.[^20] In 2020, LockBit launched its RaaS affiliate program using 
a leak site and a few months later began using the double extortion model where the attacker threatens 
14 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report
to publicly expose data in addition to encrypting files. In 2021, one of the prominent incidents involving 
LockBit occurred when it launched an attack on tech services firm Accenture, even going as far as listing 
the company on its leak site.[^21]

LockBit has been a staple in the ransomware scene since its debut, with its operators constantly evolving 
its capabilities to the point where the performance of its RaaS service has become one of the group’s 
selling points due to its speed and efficiency. LockBit’s network has also garnered popularity for its 
capability and trustworthiness.

LockBit offers multiple options for infection routines depending on the affiliates involved in the operation, 
their purpose, and how they gain access to their target’s system. For example, if an affiliate manages 
to gain access to a virtual private network (VPN) server using brute-force methods, LockBit’s operators 
might provide an infection routine that is based on remote access service (RAS). On the other hand, the 
group might offer a PowerShell script to attackers that gain access to a compromised Internet Information 
Services (IIS) server. In addition to its encryption routines, LockBit attacks were also found to have 
deployed the post-exploitation tool Mimikatz to gather additional credentials.

![Figure 12. Two of the infection routines used by LockBit: one for when its operators manage to compromise an IIS server, and one for when they manage to compromise a VPN server via brute-force methods]

Compromised
IIS server
PowerShell
script
Backdoor
(PowerShell Empire)
LockBit 
ransomware
Brute-forced
VPN server
SMB/Microsoft
RAS
LockBit
ransomware
LockBit
ransomware
PowerShell
command

Touted as the successor to the notorious Ryuk ransomware,[^22] Conti hit its stride in 2021 with a number of 
prominent attacks, including incidents where it targeted healthcare institutions in May.[^23]

Like many modern ransomware families, Conti employs more than one method to gain initial access to 
a victim’s system. Phishing emails remain a common infiltration technique, with attackers using Google 
Drive links to drop BazarLoader and the attack eventually leading to an infection. Conti can also arrive on 
a target’s machine by exploiting vulnerabilities like the FortiGate firewall vulnerabilities CVE-2018-13379[^24] 
and CVE-2018-13374,[^25] as well as various ProxyShell Microsoft Exchange vulnerabilities.[^26]

15 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

Once inside the system, tools like Whoami, Nltest, and Net are used to provide the attackers some 
system information, such as the rights and permissions they have gained via the compromised machine. 
At the same time, the threat actors actively search for files that they can exfiltrate for use in their double 
extortion technique. If the attackers that deployed Conti find that they need to have access to greater 
privileges, they might also use exploits like Zerologon[^27] for privilege escalation. 

In February 2022, an alleged security researcher leaked some of the ransomware group’s files and 
documents, revealing information such as the size and leadership of the group.[^28] More importantly, 
they unearthed the code used by Conti operators for their components and infrastructure, such as the 
administrator panel, a decryptor, and even Conti Locker v2.

Nevertheless, the leak of such information is a double-edged sword: While it could be instrumental for 
researchers to use it for keeping track of and gaining insight into Conti’s operation, malicious actors can 
use the leaked source codes to build their own startup ransomware operation.

![Figure 13. The infection chain used in a typical Conti attack]

Firewall
exploit
Phishing email
Netscan
ShareFinder
BazarLoader/
BazarBackdoor
Kerberoasting
Net-GPPPassword
ProcDump
ProcDump
Cobalt Strike
Valid accounts
PrintNightmare
ZeroLogon
Anydesk
Anydesk
Create scheduled
task on remote systems 
Cobeacon, KillAV, Conti
KillAV
PSExec
Kerberoasting
ProcDump
Initial Entry and Execution
Credential Access
Lateral Movement
Privilege Escalation
Command and Control
Impact
Network Discovery
Rclone
Exﬁltration
Lateral Movement and
Defense Evasion
Conti

Although relatively new to the ransomware scene compared to LockBit and Conti, BlackCat still managed 
to make waves in the months that it was active by going beyond the typical double extortion scheme used 
by modern ransomware groups. Instead, BlackCat resorted to a “triple extortion” scheme[^29] where it not 
only threatened to encrypt files and leak sensitive data but also warned its victims that it would launch 
distributed denial-of-service (DDoS) attacks on their infrastructure if the group’s demands are not met.[^30]

16 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

BlackCat’s operators typically exploit exposed and vulnerable applications to gain entry into their target 
system. They then use third-party frameworks and toolsets such as Cobalt Strike to deliver the ransomware. 
In April 2022, we launched an investigation into BlackCat via the Trend Micro Vision One™ platform, where 
we gathered information about its routine. We found that the malicious actors were actively exploiting the 
Microsoft Exchange Server vulnerability CVE-2021-31207[^31] to insert a web shell into the victim’s server for 
remote access. This allows the attackers the ability to remotely perform different tasks like stealing data 
and dropping malicious tools. The attackers then use these tools to move laterally within the system, scan 
the environment, and prepare it for eventual BlackCat infection. 

Due to BlackCat’s sophistication as the first professional ransomware family to be written in Rust, a secure 
programming language that has concurrent processing capabilities, as well as its unique monetization 
method, extensive infrastructure, and wide array of supplementary tools in its attacks, it has the potential 
to become a staple in the RaaS scene in the foreseeable future.

Based on both our data and data from leak sites, we were able to note that these ransomware families 
are used mainly to target small businesses with up to 200 employees at most as well as medium-sized 
businesses with up to 1,000 employees. The likely reason for this is that these types of organizations have 
less resources and a smaller workforce to properly deal with cyberattacks.[^32]

### Linux Systems Become a Prime Target for Ransomware Operators
> Our 2022 security predictions anticipated 
that ransomware threat actors would 
expend more effort on targeting servers, 
server components, and related services.
>
> Predictions

Linux systems present an attractive target for 
malicious actors that are either looking to expand 
their reach or have decided to concentrate on 
specific types of infrastructure, such as servers and 
embedded systems where Linux is expected to see 
growth over the next few years.[^33]

We observed a 75% increase in ransomware attacks targeting Linux-based machines in the first half of 
2022 as opposed to the first half of 2021, lending more evidence to our assumption that malicious actors 
are focusing more of their efforts on Linux.

17 | Defending the Expanding Attack Surface: Trend Micro 2022 Midyear Cybersecurity Report

![Figure 14. Linux ransomware detections grew significantly in the first half of 2022 as opposed to the first half of 2021: A comparison of ransomware detections for Linux-based machines Source: Trend Micro Smart Protection Network]

0
500
1K
1.5K
2K
1H 2022
1H 2021
1,121
1,961

The VMware hypervisor ESXi came under heavy fire in the first half of 2022. Still, there is nothing new 
about cybercriminals targeting ESXi. RansomEXX[^34], for example, has been exploiting ESXi vulnerabilities 
in its campaigns since at least 2021[^35] — and it seems that other threat actors are now following suit.

In October 2021, LockBit’s operators announced a Linux-based variant, LockBit Linux-ESXi Locker 
version 1.0, in an underground forum. This variant targets ESXi servers through a combination of Advanced 
Encryption Standard (AES) and elliptic-curve cryptography (ECC) algorithms to encrypt data. Since then, 
samples of this variant have been found in the wild. 

In May 2022, a new ransomware variant named Cheerscrypt was also found targeting devices using ESXi.[^36] 
Based on the source code of the Babuk ransomware that was leaked in September 2021,[^37] Cheerscrypt 
encrypts log files and other VMware-related files using the double extortion technique. 

Although neither LockBit Linux-ESXi Locker version 1.0 nor Cheerscrypt deviates from the typical double 
extortion scheme used by many other ransomware variants, the potential impact of an infection is notable 
in this case since ESXi servers are widely used by enterprises for server virtualization. Organizations 
can also use these servers