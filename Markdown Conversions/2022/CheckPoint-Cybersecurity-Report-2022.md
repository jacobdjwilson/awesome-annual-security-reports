# AI Instruction Set for Converting Technical PDFs to Markdown

## Purpose
Ensure technical PDFs are converted to Markdown with complete fidelity, preserving all content, structure, and formatting.

## Goals
1. **Full Conversion**: Include all text, quotations, footnotes, references, and technical terminology without omission or summarization.
2. **TOC Format**: Include a fully functional Table of Contents with proper linking.
3. **Markdown Conventions**: Use clear, consistent, and professional formatting.
4. **Images**: Describe image contents without embedding.

## Conversion Instructions
### Content
- **Include All Text**: Retain all sections, preserving the original structure and content.
- **Headings**: Format with `#` for main headings, `##` and `###` for subheadings.
- **Lists**: Use `1.` for ordered lists, `-` for unordered lists.
- **Emphasis and Formatting**: Apply `_italic_`, `**bold**`, `>` for block quotes, and \`\`\` for code blocks.
- **Links**: Format as `[text](URL)` and ensure accuracy.

### Images
- **Do Not Embed**: Replace with descriptive text: `![Image description]`.

### Table of Contents
- Place after the document title but before the main content:
  ## Table of Contents
  - [Section Title](#section-title)
  - [Subsection Title](#subsection-title)
- Ensure anchor links work and follow the format `(#section-title)`.

### Footnotes and References
- Use Markdown footnote syntax:
  Content with a footnote[^1].
  [^1]: Footnote content here.
- Retain all technical and academic terms exactly.

## Verification and Quality Assurance
1. **Accuracy**: Verify the entire document is converted without omissions.
2. **TOC Functionality**: Check all links point to the correct headings.
3. **Readability**: Ensure professional formatting and adherence to Markdown standards. DO NOT enclose the top and bottom of the content in ```markdown and ``` .
4. **Fidelity**: Confirm the output matches the original PDF exactly.

---
# Report Content Below

# CHECK POINT SOFTWARE | SECURITY REPORT 2022

## Table of Contents
- [CHAPTER 1: INTRODUCTION TO THE CHECK POINT 2022 SECURITY REPORT](#chapter-1-introduction-to-the-check-point-2022-security-report)
- [CHAPTER 2: TIMELINE OF 2021'S MAJOR CYBER EVENTS](#chapter-2-timeline-of-2021s-major-cyber-events)
- [CHAPTER 3: 2021’S CYBER SECURITY TRENDS](#chapter-3-2021s-cyber-security-trends)
    - [FROM SOLARWINDS TO LOG4J](#from-solarwinds-to-log4j)
    - [THE FALLOUT OF CYBER ATTACKS](#the-fallout-of-cyber-attacks)
    - [CLOUD SERVICES UNDER ATTACK](#cloud-services-under-attack)
    - [MOBILE ARENA DEVELOPMENTS](#mobile-arena-developments)
    - [CRACKS IN THE RANSOMWARE ECOSYSTEM](#cracks-in-the-ransomware-ecosystem)
- [CHAPTER 4: MALWARE SPOTLIGHT: EMOTET’S RETURN](#chapter-4-malware-spotlight-emotets-return)
- [CHAPTER 5: GLOBAL STATISTICS](#chapter-5-global-statistics)
    - [GLOBAL MALWARE STATISTICS](#global-malware-statistics)
    - [GLOBAL ANALYSIS OF TOP MALWARE](#global-analysis-of-top-malware)
    - [BOTNET GLOBAL ANALYSIS](#botnet-global-analysis)
    - [INFOSTEALER MALWARE GLOBAL ANALYSIS](#infostealer-malware-global-analysis)
    - [CRYPTOMINERS GLOBAL ANALYSIS](#cryptominers-global-analysis)
    - [BANKING TROJANS GLOBAL ANALYSIS](#banking-trojans-global-analysis)
    - [MOBILE MALWARE GLOBAL ANALYSIS](#mobile-malware-global-analysis)
- [CHAPTER 6: HIGH PROFILE GLOBAL VULNERABILITIES](#chapter-6-high-profile-global-vulnerabilities)
    - [‘Log4Shell’ Apache Log4j—Remote Code Execution (CVE-2021-44228)](#log4shell-apache-log4jremote-code-execution-cve-2021-44228)
    - [‘ProxyLogon’ Microsoft Exchange Server - Authentication Bypass (CVE-2021-26855)](#proxylogon-microsoft-exchange-server---authentication-bypass-cve-2021-26855)
    - [Atlassian Confluence - Remote Code Execution (CVE-2021-26084)](#atlassian-confluence---remote-code-execution-cve-2021-26084)
- [CHAPTER 7: PREVENTING THE NEXT CYBER PANDEMIC— A STRATEGY FOR ACHIEVING BETTER SECURITY](#chapter-7-preventing-the-next-cyber-pandemic-a-strategy-for-achieving-better-security)
    - [Threat prevention—prevent attacks before they happen](#threat-preventionprevent-attacks-before-they-happen)
    - [When your perimeter is everywhere and attacks keep advancing, your business needs accurate prevention based on real time threat intelligence](#when-your-perimeter-is-everywhere-and-attacks-keep-advancing-your-business-needs-accurate-prevention-based-on-real-time-threat-intelligence)
    - [Secure everything, as everything is a potential target](#secure-everything-as-everything-is-a-potential-target)
    - [Leveraging a complete unified architecture](#leveraging-a-complete-unified-architecture)
    - [Maintain security hygiene](#maintain-security-hygiene)
    - [Conclusion](#conclusion)
- [APPENDIX: MALWARE FAMILY DESCRIPTIONS](#appendix-malware-family-descriptions)

2
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022

Y O U 
D E S E R V E 
T H E  B E S T 
S E C U R I T Y
3
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
	
# CHAPTER 1: INTRODUCTION TO THE CHECK POINT 2022 SECURITY REPORT
	
# CHAPTER 2: TIMELINE OF 2021'S MAJOR CYBER EVENTS
	
# CHAPTER 3: 2021’S CYBER SECURITY TRENDS
13	
From SolarWinds to Log4j
17	
The Fallout of Cyber Attacks 
21	
Cloud Services Under Attack
25	
Mobile Arena Developments
28	
Cracks in the Ransomware Ecosystem 
	
# CHAPTER 4: MALWARE SPOTLIGHT: EMOTET’S RETURN
	
# CHAPTER 5: GLOBAL STATISTICS
41	
Global Malware Statistics
43	
Global Analysis of Top Malware
45	
Botnet Global Analysis
47	
Infostealer Malware Global Analysis 
49	
Cryptominers Global Analysis 
51	
Banking Trojans Global Analysis
53	
Mobile Malware Global Analysis 
C O N T E N T S
05
07
12
31
34
4
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
	
# CHAPTER 6: HIGH PROFILE GLOBAL VULNERABILITIES
55	
‘Log4Shell’ Apache Log4j—Remote Code Execution 
(CVE-2021-44228)
56	
‘ProxyLogon’ Microsoft Exchange Server - Authentication Bypass 
(CVE-2021-26855)
56 
Atlassian Confluence - Remote Code Execution 
(CVE-2021-26084) 
	
# CHAPTER 7: PREVENTING THE NEXT CYBER PANDEMIC— 
	
A STRATEGY FOR ACHIEVING BETTER SECURITY
60	
Threat prevention—prevent attacks before they happen
60	
When your perimeter is everywhere and attacks keep advancing, 
your business needs accurate prevention based on real time threat 
intelligence
61	
Secure everything, as everything is a potential target
61 
Leveraging a complete unified architecture
62	
Maintain security hygiene
64	
Conclusion
	
# APPENDIX: MALWARE FAMILY DESCRIPTIONS
54
59
65
5
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
5
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
01
# C H A P T E R  1
INTRODUCTION 
TO THE CHECK POINT 
2022 SECURITY REPORT
01
	THE PAST TWELVE MONTHS REPRESENTS ONE OF THE 
MOST TURBULENT AND DISRUPTIVE PERIODS ON RECORD, 
AT LEAST AS FAR AS SECURITY IS CONCERNED.
6
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
6
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
MAYA HOROWITZ 
VP Research, Check Point
The past twelve months represents one of the most turbulent and disruptive periods 
on record, at least as far as security is concerned. As governments and businesses 
around the world continued to navigate the uncharted waters of a global pandemic, 
the so-called “new normal” still felt a long way off. Digital transformation efforts 
were dramatically accelerated as businesses embraced hybrid and remote working 
arrangements, but the same questions around security maturity that plagued many 
businesses in 2020 persisted through 2021. While some of those questions remain 
up in the air, threat actors have wasted no time whatsoever in turning the situation 
to their advantage. Cyberattacks are up by an average of 50% since we issued our 
last annual report, with the education and research sector suffering the biggest 
blow, averaging 1,605 attacks every single week throughout the year. As predicted, 
the infamous SolarWinds breach appears to have kickstarted a trend of supply chain 
attacks that have persisted throughout the year, showing no signs of slowing down. 
In this 2022 Security Report, we will reveal the key attack vectors and techniques 
that our researchers here at Check Point Software have observed over the past year. 
From a new generation of highly sophisticated supply chain attack methods, right 
through to the Log4j vulnerability exploit that rendered hundreds of thousands of 
businesses open to a potential breach. 
We’ll start with a month-by-month rundown of the year’s major cyber events, before 
doing a deep dive into some of the emerging trends that will undoubtedly shape the 
year to come. We’ll discuss cloud services, developments in the mobile landscape 
and IoT, cracks in the ransomware ecosystem, the return of Emotet, and, of course, 
the Log4J zero-day vulnerability that punctuated an already busy year.
# C H A P T E R  1
7
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
7
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
# C H A P T E R  2
02
TIMELINE 
OF 2021'S MAJOR 
CYBER EVENTS
	IN 2021, WE WITNESSED AN UNUSUALLY HIGH NUMBER OF 
ATTACKS THAT LED TO DISRUPTIONS TO INDIVIDUALS’ DAY-TO-DAY 
LIVES, AND IN SOME CASES EVEN THREATENED THEIR SENSE OF 
PHYSICAL SECURITY. 
8
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
In January, the US Department of Justice confirmed that it had been affected by the 
Solarwinds supply-chain attack, and that 3% of its employee email boxes had been 
accessed in order to steal sensitive data. The department has more than 100,000 
employees across a series of law enforcement agencies, including the FBI, the Drug 
Enforcement Agency, and the US Marshals Service. The Department of Justice was a 
buyer of SolarWinds Orion, a tool that was used by hackers to execute this attack, leading 
to as many as 18,000 SolarWinds customers experiencing a breach. The Department 
of Justice said it learned it was a victim on Christmas Eve, revealing that a small 
percentage of its Microsoft Office 365 email accounts had been compromised. 
In February, popular music streaming platform, Spotify, was hit by a credential-stuffing 
attack, only three months after experiencing a similar incident. The attack used stolen 
credentials from 100,000 user accounts and leveraged a malicious Spotify login database. 
The attack was reported to Spotify, which prompted the company to issue a password 
reset to affected users that rendered the stolen credentials invalid. The company said 
in a statement that it also worked to have the fraudulent database taken down by its 
internet service provider, and noted that the attack was not linked to a breach in Spotify's 
own security. Cybercriminals carrying out credential-stuffing exploit people who reuse 
the same passwords across multiple online accounts and platforms. Attackers simply 
build automated scripts that systematically try stolen IDs and passwords against various 
types of accounts.
On March 2nd, 2021, Volexity reported the in-the-wild exploitation of the Microsoft 
Exchange Server vulnerabilities, CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, 
and CVE-2021-27065. Further investigation uncovered that an attacker was exploiting 
a zero-day used in the wild. The attacker was using the vulnerability to steal the full 
contents of several user mailboxes. This vulnerability is remotely exploitable and does 
not require authentication, special knowledge or access to a specific environment. It was 
estimated that 250,000 servers fell victim to the attacks, including servers belonging 
to around 30,000 organizations in the United States and 7,000 servers in the United 
Kingdom. The European Banking Authority, the Norwegian Parliament, and Chile's 
Commission for the Financial Market (CMF) were also impacted.
01
JAN
03
MAR
02
FEB
9
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
In April, the US National Security Agency (NSA), the Cybersecurity and Infrastructure 
Security Agency (CISA), and the Federal Bureau of Investigation (FBI) published a 
joint advisory warning that a Russia-linked APT group, APT29, was exploiting five 
vulnerabilities in an ongoing attack against US targets. According to the advisory, 
Russian Foreign Intelligence Service (SVR) actors (also known as APT29, Cozy Bear, 
and The Dukes) frequently used publicly known vulnerabilities to conduct widespread 
scanning and exploitation against vulnerable systems in an effort to obtain authentication 
credentials to allow further access. Recent Russian SVR activities include compromising 
SolarWinds Orion software updates, targeting COVID-19 research facilities through 
deploying WellMess malware, and leveraging a VMware vulnerability that was a zero-day 
at the time.
In May, a ransomware attack shut down the routine operations of Colonial Pipeline, 
which carries 45% of the fuel consumed in the US East Coast, including diesel, petrol 
and jet fuel. The alleged Russian DarkSide ransomware criminal group, was behind the 
attack. Colonial Pipeline is the largest refined products pipeline in the US, a 5,500 mile 
(8,851 km) system involved in transporting over 100 million gallons from the Texas city 
of Houston to New York Harbor. DarkSide uses Ransomware-as-a-Service (RaaS) model, 
where it relies on affiliate program to execute its cyber attacks. Colonial Pipeline paid a 
ransom demand of close to US$ 5 million in return for a decryption key. Later on, the FBI 
declared it had retrieved the private key of the ransom account and recovered 63.7 of the 
bitcoins paid.
JBS, the US-based meat processing giant, was hit by a ransomware attack in June 
affecting its North American and Australian operations. The FBI attributed the attack to 
the REvil ransomware group. The attack forced JBS to temporarily shut down all of its 
beef plants in the United States. One of its Canadian plants was also affected, and the 
company paused beef and lamb kills in Australia until the plants were back online. On 
June 9, JBL’s Chief Executive in the US revealed the company had paid US$ 11 million to 
hackers in a “very painful but necessary decision”, despite the fact that the company was 
able to restore most of its systems from its own backups. 
04
APR
06
JUN
05
MAY
10
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
In July, the REvil ransomware group targeted multiple Managed Service Providers 
(MSPs) and their customers in a supply chain attack. Threat actors successfully 
implanted a malicious software update for IT Company Kaseya’s VSA patch management 
and client monitoring tool, which included the malware installer. An estimated 1,000 
companies were impacted by the attack. The massive supply chain attack carried out by 
REvil over the 4th of July weekend impacted numerous Kaseya customers with millions 
of USD demanded in ransom. Kaseya issued a security advisory on their site, warning 
all customers to immediately shut down their VSA server to prevent the spread of the 
attack while they investigated. In order to breach on-premise Kaseya VSA servers, REvil 
used a zero-day vulnerability that was in the process of being fixed. The vulnerability had 
been previously disclosed to Kaseya by security researchers from the Dutch Institute 
for Vulnerability Disclosure (DIVD), and Kaseya was validating the patch before rolling 
it out to customers. However, the REvil ransomware gang was one step ahead of Kaseya 
and used the vulnerability to carry out their attack, with ransoms ranging from US$ 45K 
to US$ 5 million. With the attack on Kaseya VSA servers, REvil’s affiliate was initially 
targeting Kaseya’s MSSP’s, with a clear intent to propagate to the MSSP customers. The 
attack amplified exponentially from the MSSP to the actual customers.
The largest ever distributed denial of service (DDoS) attack was detected in August, 
with 17.2 million requests-per-second. The attack was facilitated by the Mirai botnet, 
targeting an organization in the financial industry. In this specific incident, the traffic 
originated from more than 20,000 bots in 125 countries worldwide, with almost 15% of 
the attack originating from Indonesia, followed by India, Brazil, Vietnam, and Ukraine. 
Mirai was first observed in 2016 targeting Internet of Things (IoT) devices, such as CCTV 
cameras and routers. Numerous variants of the botnet have emerged since, expanding 
the list of targeted devices to include Linux routers and servers, Android devices, and more.
Check Point Research saw a global surge in the black market for fake COVID-19 
vaccine certificates on Telegram, following US President Biden’s vaccine mandate 
announcements. The black market expanded to serve 28 countries, including Austria, 
UAE, Brazil, UK, Singapore and more. The price for fake vaccine certificates also jumped 
globally, including in the US, where it doubled from US$ 100 to US$ 200. 
09
SEP
08
AUG
07
JUL
11
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
In October, the infrastructure of the Russia-based REvil ransomware gang, responsible 
for numerous ransomware attacks, was compromised and forcibly taken-down for the 
second time in three months, bringing their operation to a halt. This comes after REvil’s 
leaks website “Happy Blog” was previously shut down in July (along with the suspicious 
disappearance of one of REvil gang leaders “UNKN”), and after it was brought back up 
again during September, by one of its remaining gang leaders. REvil ransomware became 
notorious during 2021 with a series devastating attacks, especially after their successful 
ransom of the JBS food company, for US$ 11 million, and their later compromise of 
Kaseya - a US software management company, in July. These increasingly devastating 
attacks were matched by an increased pressure from authorities, and the launch of an 
offensive attack against REvil’s infrastructure and its members.
On November 14, Emotet, one of the most infamous botnets in history, rose from the 
dead after it was taken down ten months earlier, by a joint international law enforcement 
operation. Emotet used the Trickbot botnet to jump-start its operation, when machines 
already infected with the Trickbot Trojan, started to download and execute the latest 
version of Emotet. Emotet itself came back even stronger than before, with some new 
additions to its toolbox, such as an updated encryption scheme, control-flow obfuscations 
and new delivery methods.
On December 9th, an acute remote code execution (RCE) vulnerability was reported in 
the Apache logging package Log4j 2 versions 2.14.1 and below (CVE-2021-44228). Apache 
Log4j is the most popular java logging library with over 400,000 downloads from its 
GitHub project. It is used by a vast number of companies worldwide, enabling logging 
in a wide set of popular applications. Exploiting this vulnerability is simple. The Log4j 
library is embedded in almost every internet service or application we are familiar with, 
including Twitter, Amazon, Microsoft, Minecraft and more. Since the outbreak, Check 
Point Research witnessed what looks like an evolutionary repression, with new variations 
of the original exploit being introduced rapidly - over 60 in less than 24 hours. This was 
clearly one of the most serious vulnerabilities on the internet in recent years.
10
OCT
12
DEC
11
NOV
12
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
# C H A P T E R  3
2021’S 
CYBER SECURITY TRENDS
03
	THROUGHOUT 2021, SOFTWARE SUPPLY CHAIN ATTACKS GREW IN 
BOTH FREQUENCY AND SCALE. RESEARCHERS CONCLUDED THAT 
SOFTWARE SUPPLY-CHAIN ATTACKS INCREASED BY NO LESS 
THAN 650% THROUGHOUT THE YEAR.
13
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
# FROM SOLARWINDS TO LOG4J
The infamous SolarWinds supply chain attack was revealed in December 2020, but its influence 
on the cloud attack landscape, with particular regard to supply chain attacks, has led to its 
inclusion in our report once again. The SolarWinds incident originated with a sophisticated 
malware, Sunburst, incorporated into several compromised versions of an IT resource 
management product named SolarWinds Orion, used by 33,000 customers worldwide. The 
malicious update, attributed to the Russian Intelligence agency-affiliated threat group called 
‘Nobelium’, found its way to around 18,000 corporations, successfully infecting approximately 
425 companies on the Fortune 500 list, as well as US government departments including the 
Department of Homeland Security and the Treasury Department.
LOTEM FINKELSTEEN
Director,
 Threat Intelligence 
& Research
# C H A P T E R  3
	> The SolarWinds attack was very much a milestone 
moment for the security community, not just because 
of the scale of the attack, but because the technique 
that was used revealed new levels of sophistication 
that increased the threat of supply chain attacks more 
generally. The SolarWinds breach set a new tone and, as 
predicted, we’ve seen the number of software supply-
chain incidents grow in its wake. This past year, we’ve 
seen the number of incidents increase six-fold, and there 
are yet again signs that businesses aren’t prepared to 
deal with the threat.” 
14
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
14
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
Naturally, prominent APT groups are an integral 
part of the trend. The North Korean Lazarus 
group recently began targeting IT service 
providers to launch supply chain attacks, 
and a new backdoor called BLINDINGCAN 
has already been used to target a Latvian IT 
vendor and a South Korean software company. 
Additional incidents include an attack against 
a CCTV vendor carried out by an affiliate of the 
DarkSide ransomware gang, in which the actors 
compromised the vendor’s website to infect its 
clients with ransomware.
One of the most significant supply chain 
attacks of 2021, also featuring ransomware 
delivery, targeted Kaseya, a global provider of 
IT management software for managed service 
providers (MSPs) and IT teams. The attack 
was carried out by a member of the affiliates 
program of the REvil ransomware group. 
According to the Kaseya CEO, less than 0.1% of 
the company’s customers were accessed, but as 
some of Kaseya’s clients are MSPs themselves, 
as many as 1,500 companies were affected 
by the attack. The threat actors cleverly 
exploited a vulnerability affecting Kaseya’s 
internet-facing VSA servers. VSA is a remote-
monitoring tool commonly used by MSPs for the 
management of network and endpoint devices. 
When the attack was discovered by Kaseya, the 
company urged its customers to shut down their 
VSA servers.
As detailed in our previous report, beyond 
its unprecedented scale, SolarWinds’ main 
innovation lies in its technique. In order to gain 
access to an organization’s sensitive Microsoft 
365 resources, the attackers first used a forged 
token to compromise the local and on-premise 
networks, before moving laterally to the cloud 
environment. Today, we can clearly state that 
the SolarWinds attack laid the foundations for a 
rapid surge in supply chain attacks. 
Throughout 2021, software supply chain attacks 
grew in both frequency and scale. Researchers 
concluded that software supply-chain attacks 
increased by no less than 650% throughout 
the year. A study issued by the European Union 
Agency for Cybersecurity (ENISA) reviewed 
two dozen incidents and found that 66% of 
supply chain attacks were committed by 
exploiting an unknown vulnerability, while only 
16% leveraged known software flaws. Most 
attacks actually targeted software code. This 
year, it seems that organizations were once 
again caught largely unprepared, as a survey 
concluded that 82% of companies designate the 
third party vendors that make up their software 
supply chain with highly privileged roles. 76% 
provide roles that could allow account takeover, 
and, worst of all, over 90% of designated security 
teams were not aware that such permissions 
were even granted. 
# C H A P T E R  3
15
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
15
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
This year, the group behind the SolarWinds 
attack itself resumed activity, utilizing the 
approach developed for the first attack and 
focusing yet again on companies that are part 
of the global IT supply chain. However, this 
time, a different part of the chain is being 
targeted, namely cloud resellers and tech 
service providers. These companies customize, 
implement, and manage cloud services for their 
customers. The threat group clearly relies on 
these companies’ direct access to their clients’ 
environments to obtain access to their full 
client lists in a single strike, impersonating a 
trusted partner. The operation has been taking 
place since May 2021 and has already impacted 
more than 140 resellers and providers, 
compromising 14 of them. Throughout the 
second half of the year, the ‘Nobelium’ threat 
group has been highly active, but with a lower 
success rate due to growing awareness. The 
group utilizes multiple tactics, including the 
use of stolen credentials obtained via an 
info-stealer campaign by a third-party actor, 
leveraging application impersonation privileges 
to collect protected mail data, and abuse multi-
factor authentication (MFA). The recent attack 
wave may signal a growth in the resources 
invested by the Russian state-sponsored group 
in the field of supply chain operations, as a 
means to establish persistent access to targets 
of interest to the Russian government.
In late October, the popular NPM package ‘ua-
parser-js’, with millions of weekly downloads, 
was compromised by attackers. For a period 
of four hours, the actors managed to take over 
the developer’s NPM account and inserted 
malicious code into three versions of the NPM 
library. The library, which is used to parse 
user agent strings and identify its browser, 
operating system, CPU and more, is used in 
thousands of projects, including ones owned 
by Facebook, Microsoft, Amazon, Google and 
Slack. Therefore, the supply chain attack, in 
which compromised packages of the library 
were distributed instead of the legitimate one, 
enabled threat actors to install malware on a 
large number of infected devices. In this case, 
Linux and Windows devices were infected with 
crypto-miners and password-stealers. 
Another prominent incident took place in 
November, when multiple Greek shipping 
companies were hit by ransomware. This was 
after a common IT service provider, Danaos 
Management Consultants, was compromised in 
a supply chain attack. The incident crippled the 
shipping companies’ communication channels, 
interrupting contact with other ships, suppliers, 
and agents, and also led to data loss. 
# C H A P T E R  3
16
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
16
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
Due to the scale of the distribution of the 
library, Log4Shell is referred to as the most 
critical vulnerability of 2021, with the full scope 
of the damage yet to be determined. The Apache 
Foundation released a patch for the RCE 
vulnerability, but nevertheless, mass scanning 
of vulnerable servers has been observed by 
multiple security vendors. The exploit rate of 
the Log4j flaw has been unusually high since 
shortly after its exposure. Check Point 
Research detected approximately 40,000 attack 
attempts 2 hours after the Log4j vulnerability 
was revealed and 830,000 attack attempts 72 
hours into the event.
The vulnerability could potentially allow 
threat actors to access any system using the 
library, including systems that are used to 
manage client networks and resources. The 
potential damage that could be caused by this 
one vulnerability in an open source library 
demonstrates the immense risk posed by 
software supply chains, especially in cases 
where an underfunded project, run by several 
part-time volunteers, is a key component that 
thousands of multi-million computer systems 
rely on worldwide.
Just when we thought we had finished 
summarizing the Supply Chain landscape for 
2021, the Log4j zero-day vulnerability was 
exposed. The Apache logging package Log4j is 
the most popular Java logging library with over 
400,000 daily downloads, and is incorporated 
into millions of Java-based applications 
worldwide. Companies using Log4j as a logging 
package include Cisco, Twitter, Cloudflare, 
Tesla, Amazon, Apple and more. The Log4j 
package logs error messages; according to the 
Apache Foundation advisory, an attacker who 
can control log messages or their parameters 
could execute arbitrary code from an external 
server via multiple protocols when message 
lookup substitution is enabled. Only a single 
string of text is needed to exploit the flaw.
Since its discovery on December 9, the 
‘Log4Shell’ flaw, has been actively exploited in 
the wild. The vulnerability, assigned CVE-2021-
44228, could allow an unauthenticated attacker 
to execute malicious code or take over any 
system that uses the vulnerable version of an 
open-source library. Unsurprisingly, it scored a 
perfect 10 out of 10 in the CVSS rating system. 
# C H A P T E R  3
17
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
17
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
OMER DEMBINSKY 
Group Manager,
Data Research
# THE FALLOUT OF CYBER ATTACKS
It’s no secret that a cyberattack, whether targeted or widely distributed, can have a dramatic 
impact on organizational performance, data integrity, customer success, long-term reputation 
and, of course, finances. Naturally, attacks targeting critical infrastructure can paralyze an 
organization’s routine as well as its entire supply chain. In 2021, we witnessed an unusually high 
number of attacks that led to disruptions to individuals’ day-to-day lives, and in some cases 
even threatened their sense of physical security. Whether they are financially or ideologically 
driven, threat actors are constantly looking for additional leverage and new ways to increase 
the pressure placed on their victims.
# C H A P T E R  3
	> As outlined in our mid-year report, incidents of 
cyberattacks are increasing across the board as threat 
actors take advantage of changing circumstances 
and hurried digital transformation efforts. As of this 
report, Cyberattacks are up by an average of 50% when 
compared with last year's data, but the education and 
research sectors appear to have suffered the greatest 
blow, weathering an average of 1,605 attacks 
on a weekly basis.”
18
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
18
CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
the FBI to investigate. In Australia, some 
abattoirs were completely shut down, forcing 
the company to furlough 7,000 employees. 
Eventually, with the fear of price inflation 
combined with massive unemployment, the CEO 
of JBS USA, a subsidiary of JBS S.A., announced 
that the company paid the cybercriminals a 
ransom equivalent to US$ 11 million in BTC. 
The education sector was also heavily impacted. 
In 2021, it was the most targeted sector 
globally, with a 75% increase compared to 2020 
and an average of almost 1,605 attack weekly 
attempts per organization. The disruption 
suffered by educational institutions impacted 
students, professors and other staff members. 
Howard University in Washington D.C fell victim 
to a ransomware attack in September and 
was forced to suspend classes to conduct a 
thorough investigation of their network together 
with an audit of the student and staff devices. 
Similarly, The Lewis and Clark Community 
College in Illinois was hit by a ransomware 
attack in November that affected their online 
learning platform as well as other critical 
systems. They had to close all their campuses, 
and cancel extra-curricular activities including 
sporting events taking place in their facilities. 
The FBI released an alert against the PYSA 
ransomware that targets higher education 
institutions in the US and the UK. 
One of this year’s most significant attacks, 
which perfectly demonstrates