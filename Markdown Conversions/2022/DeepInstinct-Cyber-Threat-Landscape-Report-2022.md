# Cyber Threat Landscape Report 2022

## Table of Contents
- [Executive Summary](#executive-summary)
- [Foreword](#foreword)
- [Top Takeaways](#top-takeaways)
- [The Top Malware Trends of 2021](#the-top-malware-trends-of-2021)
- [The Top 5: Malware Families](#the-top-5-malware-families)
- [The Top 5: Ransomware Families](#the-top-5-ransomware-families)
- [The Top 5: Linux Malware Families](#the-top-5-linux-malware-families)
- [The Top 5: Financial Malware Families](#the-top-5-financial-malware-families)
- [The Top 10: MITRE techniques and capabilities](#the-top-10-mitre-techniques-and-capabilities)
- [High profile vulnerabilities in 2021](#high-profile-vulnerabilities-in-2021)
- [Interesting trends and campaigns in 2021](#interesting-trends-and-campaigns-in-2021)
- [Malware Trends by Campaign](#malware-trends-by-campaign)
  - [Excel 4.0 Macros](#excel-40-macros)
  - [JavaScript](#javascript)
  - [Attacks on Microsoft Exchange Servers](#attacks-on-microsoft-exchange-servers)
- [Deep Instinct discoveries in 2021](#deep-instinct-discoveries-in-2021)
- [The New Normal: Post COVID-19 and the hybrid workplace](#the-new-normal-post-covid-19-and-the-hybrid-workplace)
- [Cyber Insights: A Look Back at Our 2021 Predictions](#cyber-insights-a-look-back-at-our-2021-predictions)
- [Cyber Insights: 2022 Predictions](#cyber-insights-2022-predictions)
- [About Deep Instinct](#about-deep-instinct)

W 
 
  elcome to our annual review of the most significant cyber threats and 
trends from 2021. While there were continuations of trend lines that have 
been mainstays of the threat landscape for the past few years, there were 
also some unexpected developments that warrant mention. The increase in the highest 
profile threat (ransomware) has not continued at the same pace seen during the height 
of the COVID-19 outbreak in spring 2020, although it still recorded double digit (15.8%) 
growth. Specific attack vectors have grown substantially, such as the use of Office 
droppers (up 170%), along with an overall uptick of 125% in all threat types combined. 
Overall, the volume of all malware types is still substantially higher than during the pre-
pandemic period.  
The attacks themselves are also changing as we are now witnessing some groups 
opting to inflict the maximum impact over a shorter time span. In these shorter-
duration attacks, the goal is to damage data (its confidentiality and availability), 
destabilize a business, and impair business continuity. High profile breaches within 
critical infrastructures — such as the one experienced by Colonial Pipeline — can have 
huge consequences for millions of consumers. The energy sector is experiencing more 
of these attacks because the instant pain inflicted can speed the payment of ransom — 
the ultimate goal of any ransomware attack. While attacks that rely on dwell time and 
stealth are certainly a major hazard for cyber professionals, shorter duration attacks 
are gaining favor.
The ongoing transition of many organizations to a work-from-anywhere or hybrid work 
model has broadened and multiplied attack surfaces, in the process rendering defenses 
less active. Additionally, the continued move to cloud applications has reduced costs, 
but also surfaced several inherent dangers to business leaders.
Modular campaigns have been a feature of 2021, highlighted by spyware/ransomware 
combinations and multi/cross-OS attacks. We have seen a clear relationship between 
Emotet and TrickBot operators, with infected TrickBot machines being used to 
download the new Emotet binary. More thought is going into certain attack methods 
with a rise in multi-stage custom-built packers and encryptors evident. As a result, 
adopting a multi-layered protection mindset becomes even more critical.
Supply-chain attacks have been an ongoing topic as well. In July 2021, in one of the 
year’s greatest supply-chain attacks, REvil infected Kaseya VSA and then infiltrated the 
company’s VSA clients’ environments. REvil took advantage of a then-unpatched zero-
day vulnerability in the Kaseya VSA product. More than 1,500 companies using Kaseya’s 
services were ultimately infected with REvil. 
The HAFNIUM group, which targeted Exchange servers shortly after Microsoft revealed 
multiple zero-day vulnerabilities, was behind the single biggest threat of the year. This 
attack underscored why major vulnerabilities are being exploited and used within hours 
of disclosing the vulnerability. The race between patching vulnerable systems versus an 
attacker’s ability to create a single-day exploit will continue to be a significant trend in 
2022.
Overall, while 2021 was not marked with exponential increases in attack volumes, 
attacks became increasingly advanced. Attackers turned to more sophisticated 
evasion techniques that worked by fooling or bypassing detection tools. Defense 
evasion and privilege escalation are becoming more prevalent, and we expect to 
see a continuation of EPP/EDR evasion techniques in 2022. Bad actors are clearly 
investing in anti-AI and adversarial attack techniques and integrating these methods 
into their larger evasion strategy.
This report represents Deep Instinct’s current view of the threat landscape, 
showcasing trends seen throughout the course of the past year and providing 
concrete, actionable data to verify the credibility of these developments. The 
information was sourced from our data repositories, which are routinely analysed 
as part of protecting our customers from ceaseless attacks. We hope this report 
will provide you with a better understanding of the present threat landscape and its 
future trajectory.

### Executive Summary
Best regards,

Shimon N. Oren
VP of Research and Deep Learning

D 
  eep Instinct is pleased to release its 2021 Threat 
Landscape Report. The information presented in 
this report is based on D-cloud, Deep Instinct’s 
proprietary file reputation database. The database receives 
data from multiple feeds including well-known threat 
intelligence providers, curated sources maintained by Deep 
Instinct’s research group, and production data from Deep 
Instinct’s customer base. This wide cumulation of datasets 
is reflective of hundreds of millions of events that occurred 
in 2021.
The proprietary database provides real-time information 
on threats for the purpose of supporting Deep Instinct’s 
research efforts and to help ensure optimal security of our 
customers. The analysis in this research study considers 
hundreds of millions of attempted attacks that occurred every 
day throughout 2021 within our customer environments. 
This information was gathered by Deep Instinct’s team of 
researchers who have decades of combined experience and are 
veterans of various cyber intelligence units in the Israel Defense 
Forces. They extrapolated these findings to predict the future 
of cybersecurity so that we can stay ahead of attackers and 
prepare for the security threats of tomorrow. We also give a 
keen eye to what motivates attackers, how their threat tactics 
and strategies are evolving, and most importantly, what steps 
we can take now to learn from this information and develop 
more fortified defenses against future attacks.

### Foreword
### Top Takeaways 
While supply chain attacks are certainly not new, they were leveraged with greater 
regularity in 2021. A variety of large service offering companies became targets 
with threat actors intending to not only gain access to their environments, but the 
environments of their customers by proxy.  — hit in early July 2021 by the REvil 
ransomware using a then-unpatched zero-day vulnerability in the Kaseya VSA product. As 
a result, more than 1,500 companies were infected with REvil. Given the success of these 
attacks and the efficiency of one attack opening thousands more for compromise, we’re 
likely to see many similar attacks moving ahead.  
As we have predicted, there was greater partnership among international task forces this 
past year to identify and bring to justice key threat actors around the world. High-profile 
targets, including Emotet and REvil, were taken down by joint teams of law enforcement 
agencies. Other high-profile threat actors such as Glupteba became the target of private 
companies that joined forces to interrupt their activity as much as possible. We hope this 
growing spirit of collaboration is here to stay and leads to the dismantling of more high-
profile threat groups. 
We have traditionally seen attackers gaining initial access and persistence over a victim 
network with the goal of dwelling for extended periods, stealing information, and avoiding 
detection from security solutions for as long as possible. Their foothold remains stealthy, 
and they are harvesting data or abusing servers for cryptomining as long as they can. In 
2021, we saw a transition to high-profile attacks with a massive impact. We have begun 
seeing more high-impact attacks on critical infrastructures across all sectors in recent 
years, but nothing seems to compare to the Colonial Pipeline breach in terms of scope. 
This attack, which caused Colonial Pipeline to halt their operations for six days, caused 
major disruptions across the U.S., a shortage of fuel, and a subsequent increase in gas 
prices. Not only did this incident demonstrate the significant and cascading impact of a 
well-executed malware attack, but it also emphasized the importance of having sufficient 
cybersecurity defense mechanisms to protect critical infrastructure. 

01
The rise of supply chain attacks

03
The shift to impact and high-profile 
attacks vs. stealth and long dwell-time 
attacks

02
Public and private sector collaborations 
become more common 

Zero-day threats have always been a major concern when it comes to cyber 
security. But severe vulnerabilities are not discovered daily. When it comes 
to zero-day threats, there is a long period from the time between when the 
vulnerability is disclosed and patched to the time an organization can patch all its 
relevant components. In 2021, we saw major vulnerabilities being exploited and 
used within a single day of disclosing the vulnerability. One of the examples is the 
HAFNIUM group which surfaced shortly after Microsoft revealed multiple zero-day 
vulnerabilities. The race between patching vulnerable systems versus attacker’s 
ability to create a zero-day exploit will continue in 2022. 

04
The quick trickling down on zero-day 

The transition to work-from-anywhere has sped digital transformation efforts for many 
organizations, inducing them to move most of their services to the cloud rather than 
on premises. And attackers are not remaining indifferent to these changes. For many 
organizations, the transition to the cloud brings a plethora of business opportunities, but 
it also comes with many cyber security challenges and risks. For organizations that are 
not experienced working with cloud services there is the risk that misconfigurations or 
vulnerable, out-of-date components with external API access can be exploited. 
During 2021 we saw many high-profile vulnerabilities every few months, with publicly 	
available exploit POCs. Securing the entire on-premises network is not enough anymore, 
as a single outdated cloud component can create a gateway for attackers to breach an 
entire organization. 

05
Cloud as a gateway for attackers

### The Top Malware Trends of 2021
As seen in the graph below, the trend that started in 2020 continued throughout 
2021 with a spike in all malware types. In spite of a decrease in spyware caused 
by the Emotet takedown in early 2021, the rates of all malware types are still 
substantially higher than those of the pre-COVID era.

![The number of new samples each month, since January 2020, grouped by malware type and shown in arbitrary units. The amount of spyware samples in January 2020 is represented as one.]

### The Top 5: Malware Families
The top 5 malware families of 2021. The number of samples 
were collected from Deep Instinct’s D-Cloud platform. 

![The top 5 malware families of 2021. The number of samples were collected from Deep Instinct’s D-Cloud platform.]

is a highly active banking trojan family, observed in the wild since 2011 (for context, in 
2011 it appeared as its predecessor, Cridex). The first version of the current iteration 
of Dridex was spotted in mid-2014 and has become an extremely high-profile financial 
malware family. 
This malware usually spreads via mass email campaigns. Dridex uses malicious email 
attachments that include either a Word document containing a malicious macro, or a 
PDF that utilizes malicious JavaScript. Following successful infection, Dridex will collect 
and deliver banking information, credit card data, credentials, and additional sensitive 
data found on the victims’ computer to its C&C servers. Other variants include a crypto-
currency wallet credential stealing mechanism. 
In several instances, the Dridex infection infrastructure has also been used to spread 
other financial malware and spyware such as TrickBot and Emotet, sharing the same 
droppers or dropping each other as a secondary payload. 

01
Dridex

initially functioned as a banking trojan when it emerged in 2014. It was spread via spam 
campaigns, imitating financial statements, transfers, and payment invoices. Emotet 
is propagated mostly via Office email attachments containing a macro. If enabled, it 
downloads a malicious PE file (Emotet) which is then executed. Once executed, it can 
intercept and log network traffic, inject into browsers, and access banking sites in order 
to exfiltrate and store financial data. 
In 2017, Emotet operators redesigned the trojan to work mainly as a Dropper, a type of 
malware that is designed to deliver other malware to a victim’s computer. Other players 
in the cybercrime world, such as TrickBot banking malware and Ryuk ransomware, utilize 
Emotet Dropper capabilities to infect countless other users. 

02
Emotet

is a spyware that has been sold online since 2014. It 
is advertised as a legitimate monitoring software not 
intended for malicious purposes. However, its password 
extraction functionality and features that are aimed at 
avoiding detection allow Agent Tesla’s operators to use it 
for malicious purposes. Agent Tesla’s support team have 
been assisting users with instructions on how to infect 
targets similar to how malware is deployed in the wild. 

03
Agent Tesla

is a sophisticated banking malware that targets individuals, 
SMBs, and enterprise environments focusing specifically on 
gaining access to bank account credentials, financial data, 
and personal information in order to carry out financial 
fraud and identity theft. 
It first appeared in 2016 and quickly became a prevalent 
threat, spreading via malicious documents in mass emails 
and changing rapidly with different capabilities that 
were adjusted for each campaign. Its various malicious 
abilities and evasion techniques are built in a module 
architecture which allows easy swapping, modifying, and 
rebuilding for each campaign in order to reduce detection 
rate and operate a range of attack techniques. Due to 
its architecture, TrickBot has had several capabilities: In 
addition to credential stealing, it could be either operating as 
a backdoor, having network spreading abilities, utilizing email 
harvesting features, or any/all of the above. In some cases, 
TrickBot has delivered a ransomware-like screen lock option 
meant to steal system passwords. 

04
TrickBot

is a modular banking trojan active in the past few 
years, mainly targeting businesses in the U.S. and the 
UK. It primarily targets the financial industry, aiming to 
attack banks, credit card companies, and e-commerce 
properties.  
IcedID is distributed mostly as a secondary payload 
of Emotet, another highly active banking trojan. Once 
executed, it has worm-like abilities that allow it to 
propagate to additional machines on a network and 
leverages simple evasion techniques that include only 
operating after the machine restarts. 
IcedID manipulates the victims’ browsers to display 
a correct URL address with a valid SSL in banking 
websites, while actually redirecting the traffic to a fake 
website where it aims to steal credentials. 

05
IcedID

Emotet evades security measures and moves laterally by 
leveraging a server message block (SMB) exploit or brute 
force of admin credentials, making it one of the most 
dangerous and dominant malware families in the wild. 
In early 2021, an international taskforce coordinated 
by Europol and Eurojust seized Emotet infrastructure, 
comprised of several hundred servers located around the 
world, and arrested some of its operators.  
Additionally, in April 2021, law enforcement used the Emotet 
infrastructure to automatically uninstall the malware from 
infected systems. These actions stopped Emotet operations 
for a period, but in November 2021 new variants of Emotet 
were again spotted in the wild.  
There is a clear relationship between Emotet and TrickBot 
operators, as evidenced by infected TrickBot machines being 
used to download the new Emotet binary. 
We have seen changes in new Emotet variants, from using 
a different communication protocol with a constantly 
changing decryption routine, to the abuse of an old Excel 
capability (Excel 4.0), to execute the malicious macro.
This spyware is capable of extracting credentials from 
browsers, email, and FTP clients. Additionally, Agent Tesla 
can collect data from clipboard and webforms, grab 
screenshots, and record video from a user’s computer, 
allowing for the manipulation of system components. 

### TOP 5: Ransomware Families
is a ransomware family discovered in December 2018. It 
encrypts files on a victim’s machine using the AES-256 
encryption algorithm, while other algorithms have also been 
seen in newer variants. Its encryption of files is only partial 
– just the first 5 MB of data is encrypted per file. STOP is 
focused on specific file types based on their file extension 
and includes PDFs, Microsoft Office documents, databases, 
photos, music, videos, archives, and applications. The 
encrypted files are appended with various file extensions 
that sometimes differ per STOP variant. Typically, the 
affected files will have the following file extensions: “.STOP,” 
“.SUSPENDING,” “.DATASTOP,” “.djvu,” “.djvuq,” and a 
variety of others. Following encryption, a ransom note is 
presented to victims typically demanding $980 USD in BTC 
to decrypt the files. 

01
STOP

also known as Sodinokibi, is a ransomware which first 
appeared in the wild in April 2019 — just prior to the 
conclusion of operations of Gandcrab ransomware. This 
malware has since been utilized in several high-profile 
targeted attacks against private companies and government 
organizations. 
The attackers behind the ransomware have used a variety of 
tactics in their attacks, including use of zero-day, PowerShell 
scripts, specific targets on large corporations, and even 
fileless attacks. 

02
REvil

![The top 5 ransomware families in 2021 based on data from Deep Instinct’s D-Cloud. The numbers are shown in arbitrary units, where the number of DarkSide samples is represented by one.]

was one of the most widespread and publicized 
ransomware families in 2016 and 2017. At its peak in 
early 2017, Cerber accounted for more than 25% of all 
ransomware infections. Cerber infects users globally, 
though it spares users located in former USSR countries 
(or users which have a former Soviet bloc language as the 
default on their computer).  
Cerber had a very popular Ransomware-as-a Service 
(RaaS) program and has been distributed through 
affiliates that profited handsomely through successful 
infection and payments by its victims. Cerber usually 
infected victims through phishing emails, with attached 
document droppers. Once the dropper was opened 
and activated by the victim (usually through running 
VBA macros), the encryption process began, and once 
complete, the victim was presented with a ransom note. 
Some versions of Cerber have decryptors which were 
released by security companies. 

03
Cerber

ransomware, first seen in May 2020, is a highly 
proliferating ransomware and one of most common 
malware variants we see today. Conti typically targets 
organizations based in the U.S. and eastern Europe. It 
does not focus on specific industries or sectors and 
can be used against any underprepared or unprotected 
organization. 

04
Conti

which first appeared in August 2020, is a ransomware that 
mostly targets organizations in English-speaking countries. 
The threat group behind the malware markets it as a RaaS 
and has an “affiliates program” that gives its members 
access to the ransomware in exchange for a stake of the 
ransom payment. Affiliates must also abide the gang’s 
code of conduct: specifically, they must avoid attacking 
organizations from several sectors, such as healthcare and 
education. 
Once the attackers successfully breach a corporate 
network, they determine whether harming the 
organization conflicts with the above-mentioned code of 
conduct and only if it doesn’t will the attack continue.
In the next stage, several sensitive artifacts are exfiltrated 
and PowerShell is used to download the DarkSide 
payload, “update.exe,” to several locations on the victim’s 
computer, including a network share created by the 
attackers. After patient zero is fully infected, the threat 
actors move laterally in the environment with the goal of 
reaching the Domain Controller (DC). If they succeed, they 
exfiltrate sensitive information, such as files and the SAM 
registry hive. They copy “update.exe” from the previously 
created network share into the DC, use Task Scheduler to 
set an execution time, and copy the ransomware payload 
to yet another network share, which this time resides on 
the DC and is used to transfer the ransomware to other 
targets in the environment for maximum damage.  
 When the payload is executed, it compares the system’s 
language to a set of former Soviet Bloc countries’ 
languages to make sure it doesn’t run in one of these 
nations. If it finds it may run in a country that is off limits 
the ransomware disables certain security and backup 
services, connects to its C2 server, disables the Volume 
Shadow Copy Service (VSS), and deletes shadow copies 
using PowerShell. 
DarkSide generates a unique user ID string for each victim 
and uses it as a file extension for the encrypted files. It 
also changes the icons and the desktop background and 
drops a “readme.txt” file with ransom demands.  
In March 2021, DarkSide released version 2.0, which was 
claimed as the “fastest Ransomware-as-a-Service ever 
seen” and has both Windows and Linux variants. The 
Linux variants can exploit VMware ESXi vulnerabilities and 
harm Network Attach Storage (NAS) devices. 
In June 2021, DarkSide was used to attack the Colonial 
Pipeline resulting in a major disruption in the critical 
infrastructure’s operation. Shortly after the attack, the 
DarkSide website was taken down by the U.S. government. 
Fearing further retaliation, the threat actors behind the 
ransomware, who are believed to be from a former Soviet 
nation, shut down their operations.  

05
DarkSide

### TOP 5: Linux  Malware Families
was first seen in 2014 and has been building its army of 
botnets for the last eight years. The malware spreads by 
brute forcing its way into Linux and Docker servers while 
utilizing open SSH (Secure Shell) port 22 and Docker 
port 2375. 
Once installed on an unsecured system, the malware 
gains persistence via several methods, including a Cron 
entry. XorDDoS may also install an LKM (Loadable Kernel 
Module) rootkit that will hide its activities and make it 
harder to detect. 
XorDDoS acquired its name from its use of XOR 
encryption when communicating with its C2. And as 
its name suggests, XorDDoS is responsible for several 
devastating distributed denial-of-service attacks in Asia. 
XorDDoS is believed to have originated in China and be 
related to the Winnti APT group.

01
XorDDos

is an infamous botnet that has been operating since 2016. 
It was responsible for some of the most disruptive DDoS 
attacks in the world, including the attacks against Dyn, then 
one of the largest DNS operators in the world, Brian Krebs’ 
website, and the French web-hosting service OVH. 
Mirai targets Linux-powered devices with a focus on IoT 
connected routers, CCTV-DVRs, smart TVs, NAS devices, 
and other connected machines. Once infected, it turns 
these devices into bot “slaves” used in its large-scale 
DDoS and click fraud attacks. Mirai spreads by scanning 
the internet and local networks for vulnerable internet-
connected products that can be exploited or brute forced. 

02
Mirai

![The top 5 Linux malware families in 2021 based on data from Deep Instinct’s D-Cloud. The numbers are shown in arbitrary units, where the number of Hajine samples is represented by one.]

Mirai’s code has been public since the end of 2016 when 
it was released by its author. Different variants of the 
malware have emerged since, including Satori, Okiru, 
Miori, and Moobot, just to name a few. 

(aka Mushtik, Amnesia, and Radiation) botnet has been 
active since as early as 2013. 
The malware targets myriad network devices, servers, 
IoT appliances, and Kubernetes Pods. It is constantly 
being updated with newer exploitation techniques. 
Tsunami uses the IRC network for its communication 
with the command-and-control server and has two 
main sources of revenue: crypto-mining and DDoS 
attacks. In February 2016, the servers of the Linux 
distribution Linux Mint were compromised, and the 
ISO image of the operating system was replaced with a 
modified ISO that was infected with Tsunami. 

03
Tsunami

(aka BASHLITE, Lizkebab, and Torlus) is a modular botnet 
malware with dropper, backdoor, and spyware capabilities 
such as keylogging, system information collection, and 
process manipulation. The malware is primarily used for 
DDoS attacks and propagates using brute force and the 
exploitation of vulnerabilities in IoT devices. 
Gafgyt made a name for itself in 2014 when the malware 
was spotted exploiting a Shellshock vulnerability in order 
to infect devices running the software suite BusyBox. 
Like Mirai, Gafgyt’s code was leaked in 2015, resulting in 
different variants of the malware being created. Some 
variants have been found to also include code from Mirai. 
This year, Gafgyt was spotted delivering the “Simps” 
botnet which used Gafgyt’s DDoS module for its attacks 
on gaming targets. 

04
Gafgyt

was discovered in October 2016 while researching Mirai. 
It utilizes a peer-to-peer decentralized network for its 
communication purposes, making it difficult to take down 
or sinkhole its command-and-control server. Initially, 
Hajime gains access to a vulnerable system by means of 
brute force, while making use of a dictionary of known 
username and password pairs. Then, it gains persistence 
with an rc.d script that gets executed on boot.  
Next, the worm will download configuration files shared 
with other clients in the botnet and block network 
ports that are usually associated with Hajime and other 
botnet infections, blocking any further infections. The 
last step is particularly interesting, combined with the 
fact that in addition to firewall changes, Hajime doesn’t 
appear to be involved in any malicious activity. It doesn’t 
initiate DDoS attacks, drop other malware, or operate 
a protection racket like its cousins, Mirai and Gafgyt. 
Following a successful infection, the malware leaves the 
following message on the compromised device: 
“Just a white hat, securing some systems. Important 
messages will be signed like this! Hajime Author. Contact 
CLOSED Stay sharp!” 
To add insult to injury, this message makes Hajime look 
like it’s trying to secure the device it’s “infecting.” 

05
Hajime

### TOP 5: Financial  Malware Families
![The number of samples per malware that were seen in D-Cloud each month in 2021. The numbers are shown in arbitrary units, where the amount of QakBot samples in August is represented by one.]

![The top 5 financial malware families in 2021 based on data from Deep Instinct’s D-Cloud. The numbers are shown in arbitrary units, where the amount of QakBot samples in August is represented by one.]

is a highly active banking trojan family that first 
appeared in the wild in 2011 as its predecessor, 
Cridex. The first version of Dridex was observed 
in mid-2014, and since then it has become one of 
the most high-profile financial malware families. 
This malware usually spreads via mass email 
campaigns. Dridex uses malicious email 
attachments that include either a Word 
document containing a malicious macro or 
a PDF that utilizes a malicious JavaScript. 
Following successful infection, Dridex will 
collect and deliver banking information, credit 
card data, credentials, and additional sensitive 
data found on the victims’ computer to its’ 
C&C servers. Other variants include a crypto-
currency wallet credential stealing mechanism. 
On several occasions the Dridex infection 
infrastructure has also been used to spread 
other financial malware/spyware such as 
TrickBot and Emotet, sharing the same droppers 
or dropping each other as a secondary payload.

01
Dridex

is a sophisticated banking malware that targets 
individuals, SMBs, and enterprise environments 
to steal bank account credentials, financial data, 
and personal information in order to carry out 
financial fraud and identity theft. 
It first appeared in 2016, and soon became 
a prevalent threat, spreading via malicious 
documents in mass emails and changing rapidly 
with different capabilities in each campaign. 
Its various malicious capabilities and evasion 
techniques are built in a module architecture 
which allows easy swapping, modifying, and 
rebuilding for each campaign, reducing detection 
rate and operating a range of attack techniques. 
Due to its architecture, TrickBot has had several 
capabilities throughout its different campaigns in 
addition to credential stealing. It can be operated 
as a backdoor, possessing network spreading 
abilities, email harvesting features, or all of the 
above. In some cases, TrickBot has delivered a 
ransomware-like screen lock option, which is 
meant to steal system passwords. 

02
TrickBot

is a modular banking trojan that has been 
active for the past few years, mainly targeting 
businesses in the U.S. and the UK. It primarily 
targets the financial industry, aiming to attack 
banks, credit card companies, and e-commerce 
properties.  
IcedID is distributed mostly as a secondary 
payload of Emotet, another highly active banking 
trojan. Once executed, it has worm-like abilities 
that allow it to propagate to additional machines 
on a network, as well as employ simple evasion 
techniques such as only operating after the 
machine restarts.
IcedID manipulates the victims’ browser to 
display a correct URL address with a valid SSL 
in banking websites, while actually redirecting 
the traffic to a fake website aimed to steal 
credentials. 

03
IcedID

is a banking trojan and a variant of the infamous 
Zeus banking malware. It was first discovered 
a few years ago and since then has evolved 
dozens of times. The actively developed and 
evolved Zloader is mainly distributed by phishing 
campaigns or spoofed emails and occasionally 
will be delivered along with other malware 
such as Ryuk ransomware. Zloader droppers 
use various infection vectors and techniques 
such as Excel4 macros and password protected 
documents in order to infect a system.  
Zloader also utilizes different techniques — its 
main modules are web injections, form grabbing, 
keylogging, and anti-analysis mechanisms to steal 
credentials and other private information from 
users. Another important module of Zloader is a 
VNC server. Its role is to open a hidden VNC on 
an attacked machine, giving the attacker remote 
access. 

04
Zloader

is a popular info stealer and banking malware 
that has been active in the wild since 2009. Its 
main features enable it to steal online banking 
credentials and other financial information, 
though QakBot can also steal additional personal 
data such as files and keystrokes. 
Additionally, QakBot possesses worm features 
which allow it to spread through the network and 
removable drives. QakBot monitors the browser 
on the infected machine to detect when victims 
interact with an online banking website and then 
steal credentials. Additionally, QakBot collects 
further information from the infected machine 
including IP address, country of origin, cookies, 
and other system information. 
QakBot’s distribution methods vary and include 
malspam with specially crafted document 
attachments triggering the infection, or exploit 
kits deployed on compromised websites that 
deliver QakBot’s payload to website’s visitors. 

05
QakBot

### THE TOP 10: MITRE  techniques and capabilities 
MITRE ATT&CK® is an industry standard framework formed as a knowledge base of known attacker behaviors that have 
been compiled into tactics and techniques observed in real-world scenarios. It is intended to reflect the various phases of 
an adversary’s attack lifecycle. 
Based on D-Cloud events, we managed to extract the most common techniques among some of the tactics. 

01
Execution
Command and Scripting Interpreter 
[TA0002.T1059]  
Most operating systems come with a built-in command line 
interface and scripting capabilities which allow us to interact 
with different applications and system commands.  
An adversary may abuse programming languages such 
as JavaScript or Visual Basic to gain access to a victim’s 
computer and execute various commands to exfiltrate data 
or even download additional malware.  
[READ MORE](#)

02
Persistence 
Boot or Logon AutoStart Execution 
[TA0004.T1574]  
Some malware requires a steady foothold over the victim’s 
machine to achieve its intended goals. We see this method 
used most regularly in miners and spyware, both of which 
survive booting of