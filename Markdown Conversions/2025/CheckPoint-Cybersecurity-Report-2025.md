# THE STATE OF CYBER SECURITY 2025
## Table of Contents
- [INTRODUCTION](#introduction)
- [2024 CYBER SECURITY EVENTS](#2024-cyber-security-events)
- [CYBER SECURITY TRENDS](#cyber-security-trends)
- [GLOBAL ANALYSIS](#global-analysis)
- [HIGH PROFILE GLOBAL VULNERABILITIES](#high-profile-global-vulnerabilities)
- [INCIDENT RESPONSE PERSPECTIVE](#incident-response-perspective)
- [2025 INDUSTRY PREDICTIONS](#2025-industry-predictions)
- [CISO RECOMMENDATIONS](#ciso-recommendations)

## INTRODUCTION
### THE STATE OF CYBER SECURITY 2025
01
MAYA HOROWITZ
VP Research
INTRODUCTION 
I’m happy to introduce the 13th annual edition of Check Point's State of Cyber Security. 2024’s advancements like AI and cloud 
infrastructure improved our daily lives but also benefited cyber criminals. This report highlights the real-world impact of these 
changes, offering 2025 insights and recommendations from and for CISOs.
With over a decade of analysis, Check Point Research insights come from unparalleled data sources that no other company combines. 
We gather attack telemetry from networks, cloud, email, endpoints, and mobile devices across enterprise and SMB customers. By 
incorporating incident response, dark web, and open-source findings, we achieve visibility in over 170 countries to reveal global and 
regional trends. 
The 2025 State of Cyber Security report highlights key threats, including: 
- The AI tactics that swayed a third of global elections through disinformation.  
- A 58% surge in infostealer attacks, focusing on corporate access.  
- Ransomware attacks shift from encryption to data exfiltration extortion, with Healthcare now the second most targeted.  
- Hybrid networks enabling lateral movement between on-premise and cloud. 
- Hardware and Software supply chains saw the highest attack surge attacks 
I want to emphasize Check Point’s commitment to customer security. In 2024, edge devices were exploited to access enterprise 
networks through leaked credentials and vulnerabilities. One of the many disclosed zero-day vulnerabilities was in a Check Point 
product: the VPN Information Disclosure vulnerability (CVE-2024-24919). We promptly disclosed it, released a patch within a day, 
and proactively supported the few potentially affected customers with incident response and mitigation. Our dedication to protecting 
customers is in our DNA.   
While Check Point aims to protect our customers with our research, we hope this report serves the needs of the broader industry 
as well, as we combine forces and share knowledge. On behalf of the Check Point family, I hope this report is useful to both security 
practitioners as well as C-level executives.
Enjoy the read! 
Maya Horowitz, VP Research

## 2024 CYBER SECURITY EVENTS
### 2024 CYBER SECURITY EVENTS
02
THE STATE OF CYBER SECURITY 2025
After disclosing two zero-day vulnerabilities, Ivanti's Connect 
Secure VPNs faced mass exploitation. Thousands of VPN devices 
were compromised, impacting victims like the U.S. Cyber 
security and Infrastructure Security Agency (CISA). 
Check Point Research uncovered an NFT scam targeting 
holders of over 100 popular projects. Scammers send seemingly 
legitimate airdrops that link to fraudulent websites. Victims are 
tricked into connecting their wallets, granting attackers access to 
their funds. 
Microsoft reported an attack by the Russian group Midnight 
Blizzard (Nobelium), which used a password spray attack to 
compromise corporate email accounts, including those of senior 
leadership, cyber security, and legal staff. 
Check Point Harmony Endpoint and Threat Emulation 
protect against this threat  
(APT.Win.APT29; APT.Wins.Nobelium) 
HealthEC LLC experienced a data breach that affected 4.5 million 
individuals, compromising names, addresses, DOBs, SSNs, 
medical and billing information, and health insurance data.
The ALPHV ransomware gang attacked UnitedHealth Group’s 
subsidiary, stealing six terabytes of data. U.S. military clinics 
and hospitals worldwide were disrupted, necessitating manual 
prescription processes. 
Check Point Harmony Endpoint and Threat Emulation 
protect against this threat (Ransomware.Wins.BlackCat.
ta.*; Ransomware.Win.BlackCat) 
Cutout.Pro, an AI-powered photo and video editing service, 
experienced a data breach that exposed the personal data of 20 
million users, including email addresses, hashed passwords, 
and IP addresses.  
Chinese APT group Earth, Krahang, targeted 70 government 
entities worldwide in a cyber espionage campaign, active since 
early 2022, utilizing vulnerabilities in internet-facing servers and 
spear-phishing tactics. 
Check Point Research tracked the financially motivated threat 
actor Magnet Goblin, who exploited one-day vulnerabilities 
in servers like Ivanti Connect Secure VPN, Magento, and Qlik 
Sense. The actor deployed a new Linux version of NerbianRAT 
and WARPWIRE JavaScript credential stealer while proving quick 
adoption of exploits. 
Check Point IPS and Harmony Endpoint protect against this 
threat (RAT_Linux_Nerbian_*) 
Exploiting a Fortinet vulnerability, Chinese state-backed 
hackers targeted an unclassified military research network 
in a cyber espionage operation against the Dutch Defense 
Ministry, marking the Netherlands’ first public attribution of a 
cyber attack to China. 
A high-severity vulnerability in Google Chrome’s V8 JavaScript 
engine, CVE-2024-0517, was identified. The flaw could allow a 
remote attacker to exploit heap corruption via a crafted HTML 
page. Google has since patched the vulnerability.  
Check Point Harmony IPS protects against this threat 
(Google Chrome Out of Bounds Write (CVE-2024-0517)) 
Check Point Research discovered a critical Remote Code 
Execution (RCE) vulnerability in Microsoft Outlook, dubbed 
#MonikerLink (CVE-2024-21413). #MonikerLink allows remote 
attackers to deploy a link that bypasses the Protected View 
Protocol, potentially leading to credentials leakage and RCE 
capabilities. Microsoft has since patched the vulnerability.  
Check Point IPS blade protects against this threat 
(Microsoft Outlook Malicious Moniker Link Remote Code 
Execution (CVE-2024-21413) 
The US Department of Justice disrupted the KB botnet, used by 
the China-affiliated APT Volt Typhoon to mask its identity while 
targeting critical infrastructure in the US. The group exploited 
vulnerable, end-of-life Cisco and NetGear SOHO devices for 
initial access. In response, CISA and the FBI released guidance 
for vendors on securing SOHO routers. 
Check Point Threat Emulation protects against this threat 
(APT.Wins.VoltTyphoon; InfoStealer.Wins.VoltTyphoon) 
THE CYBER SECURITY EVENTS THAT DEFINED 2024 
FEB
MAR
JAN
Q1
The Rise of Infostealers
CYBER SECURITY TRENDS 
03
2024 CYBER SECURITY EVENTS
02
INTRODUCTION
01
2025 INDUSTRY PREDICTIONS
07
CISO RECOMMENDATIONS 
08
GLOBAL ANALYSIS
04
HIGH PROFILE VULNERABILITIES
05
INCIDENT RESPONSE PERSPECTIVE
06
Cyber Wars - 2024 Edition
The Ransomware Ecosystem
Cloud Complexities
Edge Devices and ORBs
THE STATE OF CYBER SECURITY 2025
6
Check Point researchers detected a typosquatting campaign 
comprised of over 500 malicious packages deployed on PyPI 
(Python Package Index), posing risks of PII theft malware 
installation. 
Check Point CloudGuard Code Security protects  
against this threat. 
Russian-speaking hacktivist group RGB-TEAM breached the 
website of Russia’s prosecutor general and leaked 100,000 
criminal records from 1993 to 2022 on Telegram. Data included 
details on crimes such as theft and drug trafficking. 
An AT&T data breach exposed the personal information of 
approximately 51M former and current clients, potentially 
including full names, home addresses, email addresses, 
phone numbers, social security numbers, AT&T account 
numbers, and AT&T passcodes. 
Check Point Research reports a wave of scam attacks in 
which attackers use various methods, including malicious QR 
codes and phishing emails, to gain US taxpayers’ credentials 
to steal IRS refunds.  
The US and UK announced a criminal indictment and 
sanctions against APT31, a group of Chinese hackers, for 
their role in alleged attacks against US and UK governmental 
officials. Check Point Research explored the group’s use of 
zero-day vulnerabilities. 
THE CYBER SECURITY EVENTS THAT DEFINED 2024 
MAY
JUNE
APR
Q2
Check Point Research uncovered a cyber espionage campaign 
targeting African and Caribbean governmental organizations. 
Attributed to Chinese threat actor Sharp Dragon, the campaign 
adopts Cobalt Strike Beacon as the payload, enabling backdoor 
functionalities like C2 communication and command execution 
while minimizing the exposure of their custom tools. This 
approach suggests a deeper understanding of their targets. 
The Czech Republic, Germany, and NATO revealed an espionage 
campaign targeting Czech institutions through a Microsoft 
Outlook vulnerability attributed to the Russian state-affiliated 
group, APT28, which has been conducting a long-term espionage 
effort across Europe. 
A Dell data breach affected 49 million customers after their 
database was listed on a hacking forum. The exposed data 
includes full names, home addresses, and order details.  
A data breach exposed 500 GB of biometric data from India, 
affecting police, military personnel, and public workers 
during elections. The leak involved unsecured databases from 
ThoughtGreen Technologies and Timing Technologies, including 
fingerprints and facial scans. The information could be leveraged 
to manipulate biometric systems in Indian elections. 
Data from Ticketmaster and Santander Bank has been put up for 
sale on a cyber crime forum by ShinyHunters, a notorious cyber 
gang. The breach potentially exposes the personal information 
of millions of customers. Reports indicate that the threat actor 
gained access to Ticketmaster and Santander by using the stolen 
credentials of one employee from Snowflake, a large cloud 
storage company. 
Japanese crypto exchange DMM Bitcoin confirmed a data breach 
that resulted in losing $308 million in BTC, one of the largest 
crypto heists.   
China-linked Water Sigbin 8220 Gang exploited vulnerabilities in 
Oracle WebLogic (CVE-2017-3506 and CVE-2023-21839) to deploy 
cryptocurrency mining malware using PowerShell scripts with 
hexadecimal URL encoding and fileless execution techniques. 
Check Point IPS protects against this threat (Oracle 
WebLogic WLS Security Component Remote Code 
Execution (CVE-2017-10271), Oracle WebLogic Server 
Improper Access Control (CVE-2023-21839)) 
Check Point Research analyzed Rafel RAT, an open-source 
remote administration tool for espionage and ransomware 
attacks on Android devices. The malware targeted high-profile 
organizations, especially in the military sector, with victims 
mainly from the U.S., China, and Indonesia. It enables data 
exfiltration, surveillance, and complete device control, resulting 
in severe privacy and security breaches. 
Check Point’s Harmony Mobile protects  
against this threat.

The Rise of Infostealers
CYBER SECURITY TRENDS 
03
2024 CYBER SECURITY EVENTS
02
INTRODUCTION
01
2025 INDUSTRY PREDICTIONS
07
CISO RECOMMENDATIONS 
08
GLOBAL ANALYSIS
04
HIGH PROFILE VULNERABILITIES
05
INCIDENT RESPONSE PERSPECTIVE
06
Cyber Wars - 2024 Edition
The Ransomware Ecosystem
Cloud Complexities
Edge Devices and ORBs
THE STATE OF CYBER SECURITY 2025
7
Check Point Research found that over 20K Ubiquiti cameras 
and routers are vulnerable (CVE-2017-0938) to amplification 
attacks and privacy risks due to exposed UDP ports 10001 
and 7004. These ports permit unauthorized access to device 
information, which could be exploited for technical and social 
engineering attacks. 
Check Point Research noted a rise in Server-Side Template 
Injection (SSTI) vulnerabilities that allow attackers to execute 
commands and access sensitive data. Notable cases involve 
Atlassian Confluence and CrushFTP. These vulnerabilities pose 
significant risks, such as data theft and reputation damage, 
reflected in a rise in critical CVEs 
Check Point IPS protects against this threat (Python 
Server-Side Template Injection, Java Server-Side 
Template Injection, PHP Server-Side Template Injection, 
Ruby Server-Side Template Injection, Node.js Server-
Side Template Injection, Expression Language Server-
Side Template Injection) 
Following the July Venezuelan presidential elections, Check Point 
Research revealed that hacktivist groups Anonymous Venezuela 
and Cyber Hunters launched DDoS attacks and hacking attempts 
against the government, driven by allegations of election fraud 
linked to Nicolás Maduro's administration. 
Harmony Endpoint and Threat Emulation protect against 
this threat (InfoStealer.Wins.PhemedroneStealer.*) 
Check Point Research identified the Stargazers Ghost Network, 
consisting of 3,000 GitHub repositories that distribute malware 
and malicious links through phishing schemes using a 
Distribution as a Service (DaaS) model. The network has shared 
various types of malware, such as Atlantida Stealer and RedLine, 
and has generated significant profits. 
Check Point Harmony Endpoint and Threat Emulation 
protect against this threat (InfoStealer.Win.Atlantida.*, 
Trojan.WIN32.AtlantidaStealer*, InfoStealer.Wins.
Lumma.ta*, InfoStealer.Win.Lumma*, Injector.Win.
RunPE.C, Loader.Wins.GoBitLoader.A, Trojan.Wins.
Imphash.taim.LV, InfoStealer.Wins.Redline.ta.BY) 
RockYou2024, a leak of nearly 10 billion plaintext passwords from 
multiple data breaches, poses significant risks for credential 
stuffing and brute-force attacks that could affect various online 
accounts and services. 
45M records from Rite Aid were stolen in a ransomware attack, 
allegedly including clients’ identifying information and Rite Aid 
rewards numbers. RansomHub ransomware group claimed 
responsibility and threatened to leak the stolen data. 
Check Point Threat Emulation and Harmony Endpoint 
protect against this threat (Ransomware.Win.RansomHub; 
Ransomware.Wins.RansomHub.ta.*) 
Location safety app Life360 and project management tool Trello 
suffered data breaches due to API vulnerabilities. Personal 
information of Life360’s 442,519 customers was exposed, while 
21.1GB of Trello’s data was leaked. Threat actor 'emo' claimed 
responsibility and shared the stolen data on the dark web. 
THE CYBER SECURITY EVENTS THAT DEFINED 2024 
AUG
SEPT
JULY
Q3
93GB of sensitive data was stolen from Planned Parenthood’s 
Montanna branch by the ransomware group RansomHub, 
primarily affecting the organization’s administrative IT systems. 
Check Point Threat Emulation and Harmony Endpoint 
protect against this threat (Ransomware.Win.RansomHub; 
Ransomware.Wins.RansomHub.ta.*) 
Check Point Research identified an Iranian cyber campaign 
targeting Iraqi governmental networks using malware Veaty and 
Spearal. Techniques include a passive IIS backdoor, DNS tunneling, 
and C2 communication via compromised emails, indicative of ties to 
the APT34 group. The campaign likely utilizes social engineering for 
initial infection and has a sophisticated C2 infrastructure. 
Check Point Threat Emulation and Harmony Endpoint 
protect against this threat (APT.Wins.Oilrig.ta.B/C/D/E, 
APT.Win.OilRig.F, APT.Win.OilRig.WA.G, APT.Win.OilRig.H) 
The FBI, CISA, and NSA report that Russian GRU Unit 29155 
has targeted Ukraine with website defacements, data theft, and 
WhisperGate malware, disrupting aid efforts. They also targeted 
sectors globally, including government, finance, transportation, 
energy, and healthcare. 
Check Point Threat Emulation and Harmony Endpoint 
protect against this threat (Trojan.Win.WhisperGate; Trojan.
Wins.WhisperGate.ta.*; Trojan.Wins.WhisperGate) 
A vulnerability in the ChatGPT macOS app allowed attackers to 
implant persistent spyware, SpAIware, into the app’s memory 
through indirect prompt injection, enabling continuous data 
exfiltration of user inputs and future chat sessions. OpenAI has 
since resolved the issue.

The Rise of Infostealers
CYBER SECURITY TRENDS 
03
2024 CYBER SECURITY EVENTS
02
INTRODUCTION
01
2025 INDUSTRY PREDICTIONS
07
CISO RECOMMENDATIONS 
08
GLOBAL ANALYSIS
04
HIGH PROFILE VULNERABILITIES
05
INCIDENT RESPONSE PERSPECTIVE
06
Cyber Wars - 2024 Edition
The Ransomware Ecosystem
Cloud Complexities
Edge Devices and ORBs
THE STATE OF CYBER SECURITY 2025
8
The FBI, the US Department of Treasury, and the Israeli 
National Cyber security Directorate (INCD) released a joint 
Cyber security Advisory attributing a large-scale phishing 
campaign impersonating the INCD and targeting Israeli 
organizations to the Iranian cyber group Emennet Pasargad. 
Check Point Research analyzed the malware, tracking its 
evolution and learning.  
Check Point Threat Emulation and Harmony Endpoint 
protect against this threat (Behavioral.Win.FakeChrome.B 
and Trojan.Wins.FakeUpdater.A) 
Check Point Research monitored a large-scale phishing 
campaign dubbed CopyRh(ight)adamantys, which uses the latest 
version of the Rhadamanthys stealer (0.7). This campaign targets 
regions like the U.S., Europe, East Asia, and South America, 
using a copyright theme and impersonating various companies, 
tailoring each email from different Gmail accounts. 
Check Point Threat Emulation and Harmony Endpoint 
protect against this threat (InfoStealer.Wins.
Rhadamanthys.ta.V, InfoStealer.Wins.Rhadamanthys.*, and 
InfoStealer.Wins.Rhadamanthys.*) 
Check Point Research tracked the WIRTE threat actor, linked to 
Hamas-affiliated Gaza Cybergang, conducting espionage against 
entities in the Palestinian Authority, Jordan, Iraq, Egypt, and 
Saudi Arabia, and has expanded to disruptive attacks connected 
to SameCoin malware targeting Israeli entities in 2024.  
Check Point Threat Emulation and Harmony Endpoint 
protect against this threat (APT.Wins.Wirte.ta.A/B/C/D/E/F, 
ransom.win.honey, and infoastealer.win.blackguard.d) 
Check Point Research analyzed ‘Operation MiddleFloor,' a 
disinformation campaign targeting Moldova's government 
and education sectors before the October 2024 elections. The 
Russian-aligned group Lying Pigeon uses spoofed emails 
to spread false information about EU membership while 
collecting data for potential malware attacks. 
A new phishing-as-a-service platform called Mamba 2FA 
targets adversary-in-the-middle phishing attacks. It mimics 
Microsoft 365 login pages and bypasses multi-factor 
authentication, stealing credentials and cookies sent to 
attackers via a Telegram bot. 
The FBI and CISA investigate breaches by the Chinese 
government-affiliated group Salt Typhoon at U.S. 
telecommunications companies, including AT&T, Verizon, 
and Lumen Technologies. The attacks targeted wiretapping 
systems and devices of President-elect Trump, former Vice 
President Harris, and other notable politicians. 
THE CYBER SECURITY EVENTS THAT DEFINED 2024 
NOV
DEC
OCT
Q4
Check Point Research uncovered a novel exploit of Godot 
Engine—a gaming development platform—to execute malicious 
GDScript code. The technique enables attackers to deliver 
malware across platforms like Windows, macOS, Linux, Android, 
and iOS, while evading detection by most antivirus solutions. 
Malicious loader, “GodLoader”, used this technique and already 
infected over 17,000 machines.  
Check Point Harmony Endpoint and Threat Emulation 
provide protection against this threat (Technique.win.
GDscript.*, Dropper.Win.Godot.*) 
Check Point Research analyzed Akira ransomware’s latest 
variant, written in Rust, that primarily targeted ESXi bare metal 
hypervisor servers in early 2024. The report showed how Rust 
idioms, boilerplate code, and compiler strategies were used to 
create complex assembly. 
Check Point Harmony Endpoint and Threat Emulation 
provide protection against this threat (Ransomware_Linux_
Akira_C/D, Ransomware.Wins.Akira.G/H) 
Ukrainian intelligence agency HUR confirmed a DDoS against 
Russia’s Gazprombank, one of Russia’s largest banks, which 
aimed to disrupt financial operations related to Russia’s war 
efforts in Ukraine.

## CYBER SECURITY TRENDS
### CYBER SECURITY TRENDS
03
THE STATE OF CYBER SECURITY 2025
DISINFORMATION AND INFLUENCE 
OPERATIONS 
In 2024, disinformation campaigns reached new levels of 
complexity, driven by the integration of AI and large language 
models (LLMs). These operations focused on global events, 
with nation-states like China, Russia, and Iran accused of using 
advanced tactics to manipulate public opinion, undermine trust, 
and interfere with elections to destabilize democratic processes. 
Based on Check Point Research’s findings, AI was utilized in 
at least one third of the elections that took place worldwide 
between September 2023 and February 2024, either by 
candidates themselves or potentially by foreign actors. Recent 
instances demonstrate this development, such as the Russian-
linked APT group CopyCop targeting the June 2024 USA primary 
elections with fabricated news segments featuring deepfake 
portrayals of political figures. Distributed through X (formerly 
known as Twitter) and Facebook, this content exploited platform 
algorithms to target specific voter demographics. AI-generated 
bots further disseminated divisive narratives, posing as genuine 
opinion pieces to polarize the electorate.
Iranian campaigns, often linked to the Islamic Revolutionary 
Guard Corps (IRGC), also targeted the US presidential 
elections by attacking prominent political figures in "hack-
and-leak" operations. Journalists, activists, and lobbyists were 
also targeted through social engineering, impersonations, 
phishing, and credential-harvesting malware. These 
operations demonstrated Iran’s ability to blend disinformation 
with cyber infiltration to sway public perception. 
Meanwhile, Chinese-aligned actors used AI-generated deepfake 
videos portraying false endorsements and misleading public 
service announcements. These videos, widely circulated on 
platforms like X and TikTok, aimed to discredit candidates and 
deepen partisan divides. Additionally, viral posts embedded 
with skewed polling questions seemingly portrayed support for 
certain candidates or fabricated evidence of fraud, undermining 
trust in the electoral process. 
Beyond the high-profile presidential elections in the US, 
Taiwan’s and Romania’s presidential elections and Moldova’s 
EU referendum became prime targets for cyber-enabled 
disinformation warfare. Chinese-attributed campaigns 
used AI-generated articles and social media posts to mimic 
legitimate news sources, discredit candidates, and sway 
### CYBER WARS 2024 EDITION
The global community has long speculated that devastating wars would 
be fought in cyberspace, with nation-states deploying digital doomsday 
weapons capable of crippling critical infrastructure in one decisive strike. 
However, despite the unprecedented escalation in cyber activities, no such 
apocalyptic event has occurred. Whether due to limited capabilities, fear of 
mutual destruction, or reluctance to trigger irreversible chaos, the nature 
of cyber warfare has taken a different path. 
Nation-states have shifted their focus to conflicts that undermine public 
trust, exploit societal fractures, and destabilize institutions from within. 
Campaigns involve manipulating information across social media, "hacktivist" 
groups take credit for state-backed cyber attacks, and the threat of covert 
access to compromised networks and poorly secured devices is constant. 
Cyber Wars- 2024 Edition

The Rise of Infostealers
CYBER SECURITY TRENDS 
03
2024 CYBER SECURITY EVENTS
02
INTRODUCTION
01
2025 INDUSTRY PREDICTIONS
07
CISO RECOMMENDATIONS 
08
GLOBAL ANALYSIS
04
HIGH PROFILE VULNERABILITIES
05
INCIDENT RESPONSE PERSPECTIVE
06
The Ransomware Ecosystem
Cloud Complexities
Edge Devices and ORBs
THE STATE OF CYBER SECURITY 2025
11
Similarly, the Hamas-linked group WIRTE showcased its 
evolving cyber capabilities by using the SameCoin wiper variant 
to target hospitals and municipalities in Israel, exacerbating the 
psychological and logistical toll of the ongoing conflict.  
In Eastern Europe, Russian-linked groups continued to 
weaponize destructive malware as part of its broader hybrid 
warfare strategy in Ukraine. The notorious Russian-affiliated 
APT44 (also known as Sandworm) introduced AcidPour, an 
advanced wiper variant of the AcidRain malware. AcidPour was 
deployed to disrupt Ukrainian critical infrastructure, telecom 
networks, and internet service providers. This malware was 
designed not only to destroy systems but also to embed itself 
deeper into environments, exfiltrating sensitive military plans 
and severing vital communication channels. These operations 
underscored Russia’s intent to leverage cyber tools as a vital 
support mechanism in its geopolitical conflicts.
DISRUPTION PREPARATION – 
POSSIBLE “RED BUTTONS” 
While some nations embraced these high-impact, one-time 
attacks, others, like China, took a quieter approach. They 
penetrated deep within critical systems, laying the groundwork 
for potential large-scale disruption in the future. Chinese-
affiliated actors now focus on infiltrating critical infrastructure 
and maintaining a persistent, undetected presence. Exploiting 
vulnerabilities in edge devices such as routers, VPN appliances, 
and IoT systems, groups like APT41 and Bronze Butler gained 
unauthorized access to less secure network components, 
allowing them to collect intelligence and establish a potential 
public opinion. Deepfake videos portraying candidates making 
controversial statements circulated widely, while misleading 
polling questions suggested declining support for specific 
candidates. In Romania, Russian interference leveraged fake 
social media accounts and manipulated content to promote far-
right candidate Călin Georgescu. After Georgescu unexpectedly 
won the first round, declassified intelligence revealed the extent 
of foreign interference, prompting an unprecedented annulment 
of the election results and scheduling a new vote. In Moldova, 
a campaign called "Operation MiddleFloor", attributed to a 
Russian-aligned group, targeted government and education 
sectors using spoofed emails and documents to spread anti-EU 
narratives and undermine trust in pro-European leadership. 
The Paris Olympics became another key focus for disinformation. 
Russian-linked Storm-1679 spread false narratives about 
corruption, biased officiating, and threats of violence. Automated 
accounts and bots amplified these claims to discredit the event 
and disrupt Western unity. More aggressively, the Iranian group 
Emennet Pasargad exploited vulnerabilities in the Olympics’ 
display system provider to disrupt broadcasts and spread anti-
Israel propaganda and sent threats to Israeli athletes from a fake 
persona imitating the French group GUD. 
These attacks on democracies and Western political alliances 
such as NATO have become increasingly effective and dangerous 
as democratic countries face ever-growing challenges. 
Online cultural wars, social media-fueled populism, and 
politicized media platforms using advanced algorithms to tailor 
favorable content created fertile ground for foreign actors to 
undermine public trust. The dissemination of content that aligns 
with or supports propaganda from specific states has already 
taken root, deepening societal divides. 
Democracies have responded by tightening regulations and 
recognizing disinformation as a threat to critical infrastructure. 
The U.S. Department of Homeland Security highlighted election 
meddling as a threat, while Canada expanded the CSIS Act for 
better intelligence sharing. The European Union imposed strict 
rules on platforms like Meta to curb Russian disinformation. 
OpenAI and Microsoft are disturbing accounts associated with 
groups from China, Iran, Russia, and North Korea. 
DESTRUCTIVE AND DISRUPTIVE MALWARE 
 
Nation-states increasingly relied on destructive malware 
as an important weapon in cyber warfare. These "loud" 
operations, characterized by wiper malware and other 
disruptive tools, targeted critical infrastructure, disrupting 
essential services and spreading chaos.  
Amidst the heightened tensions in the Middle East, Iran and 
other regional threat groups demonstrated the destructive 
potential of wiper malware. Void Manticore, an Iranian group 
linked to the Ministry of Intelligence and Security (MOIS), 
deployed the No-Justice Wiper under the guise of hacktivist 
personas like Karma and Homeland Justice. These campaigns 
targeted critical Israeli infrastructure and private organizations, 
erasing data and disrupting services. 
![Figure 1 – Iran’s typical warfare campaign tactics.]
Cyber Wars- 2024 Edition

The Rise of Infostealers
CYBER SECURITY TRENDS 
03
2024 CYBER SECURITY EVENTS
02
INTRODUCTION
01
2025 INDUSTRY PREDICTIONS
07
CISO RECOMMENDATIONS 
08
GLOBAL ANALYSIS
04
HIGH PROFILE VULNERABILITIES
05
INCIDENT RESPONSE PERSPECTIVE
06
The Ransomware Ecosystem
Cloud Complexities
Edge Devices and ORBs
THE STATE OF CYBER SECURITY 2025
12
In 2024, hacktivist activity underscored the evolving dynamics 
of alliances and influence in cyberspace, reflecting geopolitical 
tensions between the East and West. Groups such as the Holy 
League symbolized shared strategic goals among Russian and 
Iranian-affiliated actors. These alliances often mirrored real-
world political developments: for example, after South Korea 
sent observers to Ukraine during North Korea's involvement 
with Russian forces, Russian-linked groups NoName057(16) 
and Z Pentest launched retaliatory DDoS attacks and industrial 
hacks on South Korean entities. By emphasizing their united 
fronts through recurring declarations of collaboration, these 
groups sought to sustain attention, bolster their psychological 
impact, and amplify global influence in the increasingly complex 
landscape of modern cyber conflict. 
Handala Hack conducted defacement campaigns, hack and 
leak operations, and disruptions and claimed responsibility 
for breaching Israeli networks and exfiltrating terabytes 
of sensitive data. Karma, associated with Iran’s Ministry 
of Intelligence and Security (MOIS), deployed destructive 
tools like the BiBi and No Justice wipers against Israeli 
organizations. The Cyber Avengers, linked to the Islamic 
Revolutionary Guard Corps (IRGC), targeted critical 
infrastructure, including power grids and water systems 
in Israel, the US, and Ireland. The Iranian group Homeland 
Justice also attacked Albanian governmental institutions 
in retaliation for hosting the opposition group Mujahedin-
e-Khalq (MEK). These activities highlight Iran’s adept use 
of proxy groups to merge hacktivism with state-directed 
cyber warfare, advancing its geopolitical interests while 
maintaining plausible deniability. 
Similarly, Russian actors also exemplified this tactic, with 
groups like KillNet, NoName057(16), and the Cyber Army of 
Russia targeting critical infrastructure in countries aligned 
against Russia. These groups carried out mostly Distributed 
Denial of Service (DDoS) attacks and other manipulations, 
disrupting government and private sector operations in 
Ukraine and pro-Ukrainian countries. 
Beyond their individual efforts, Russian-aligned hacktivists 
expanded their influence by forming alliances with foreign 
actors. A notable example is the High Society hacktivist 
collective, which incorporates over 20 Russian-affiliated 
cyber gangs, including Russian-linked groups like People’s 
Cyber Army, NoName057(16) and UserSec. High Society 
joined the 7 October Union, a pro-Palestinian hacktivist 
collective of over 40 groups, many of which are linked to 
Iran. This alliance, named Holy League, targeted NATO, 
Europe, Ukraine, and Israel, with notable campaigns like 
the coordinated DDoS and propaganda efforts targeting 
NATO’s 75th Anniversary Summit in Washington. The 
campaign sought to undermine public support for NATO’s 
backing of Ukraine, blending cyberattacks with psychological 
manipulation to influence public opinion.
"red button" capability—access that could be used for 
future large-scale disruptions. This strategic positioning, 
particularly evident in US targets, enables Chinese actors 
to silently prepare for potential conflicts while avoiding the 
immediate visibility and retaliation that come with destructive 
operations.
Chinese APT group Volt Typhoon exemplified this approach 
by intensifying its focus on exploiting firewalls and routers 
in US critical infrastructure. Using living-off-the-land (LOTL) 
techniques, Volt Typhoon relied on legitimate administrative 
tools within compromised environments to evade detection. 
This allowed the group to bypass conventional cyber security 
measures and maintain a covert presence, positioning itself 
for future actions. 
Adding another layer to this covert strategy, Salt Typhoon 
targeted major internet service providers (ISPs), including 
AT&T and Verizon, exploiting vulnerabilities to intercept and 
manipulate network traffic. Additionally, Chinese-linked 
actors used Operational Relay Boxes (ORBs), which are 
networks of compromised VPS and IoT devices, to maintain 
persistence, relay commands, and gather intelligence. Often 
managed by contractors within China, ORBs enabled these 
attackers to remain embedded in compromised systems, 
discreetly relaying commands and gathering intelligence.
### “HACKTIVIST” GROUPS 
Last year, the blurred boundaries of state-backed cyber 
warfare became increasingly evident as nation-states relied 
on a sprawling network of online personas to serve their 
geopolitical agendas. Many of these figures, presenting 
themselves as ideologically motivated independent 
hacktivists, were fronts for state-sponsored APT groups. By 
amplifying divisive narratives and targeting public trust, 
the hacktivist groups became critical components of more 
extensive influence operations, allowing their sponsors 
to obscure their direct involvement while leveraging 
patriotic rhetoric to amplify their impact. Amid a backdrop 
of declining public interest and increasing fatigue, a notable 
trend emerged in 2024: the formation of alliances, where 
disparate groups united under shared banners to create a 
stronger, more cohesive front.  
On the individual front, Iranian-backed hacktivist groups 
also intensified their activities, primarily focusing on Israeli 
and Albanian targets. Groups such as Malek Team and 
![Figure 2 – telegram post about the creation of the "Holy League".]
Cyber Wars- 2024 Edition

The Rise of Infostealers
CYBER SECURITY TRENDS 
03
2024 CYBER SECURITY EVENTS
02
INTRODUCTION
01
2025 INDUSTRY PREDICTIONS
07
CISO RECOMMENDATIONS 
08
GLOBAL ANALYSIS
04
HIGH PROFILE VULNERABILITIES
05
INCIDENT RESPONSE PERSPECTIVE
06
The Ransomware Ecosystem
