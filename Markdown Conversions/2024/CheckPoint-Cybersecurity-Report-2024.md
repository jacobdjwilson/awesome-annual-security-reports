# 2024 CYBER SECURITY REPORT

## Table of Contents
- [Chapter 1 Introduction to the 2024 Cyber Security Report](#chapter-1-introduction-to-the-2024-cyber-security-report)
- [Chapter 2 Time Line of Notable 2023 Cyber Events](#chapter-2-time-line-of-notable-2023-cyber-events)
- [Chapter 3 Cyber Security Trends](#chapter-3-cyber-security-trends)
  - [Ransomware Zero-days and Mega Attacks](#ransomware-zero-days-and-mega-attacks)
  - [Expanding Attack Surface: The Emerging Risk of Edge Devices](#expanding-attack-surface-the-emerging-risk-of-edge-devices)
  - [State-Affiliated Hacktivism and Wipers Become the New Normal](#state-affiliated-hacktivism-and-wipers-become-the-new-normal)
  - [Tokens under Attack: The Cloud's Achilles Heel](#tokens-under-attack-the-clouds-achilles-heel)
  - [PIP Install Malware: Software Repositories Under Attack](#pip-install-malware-software-repositories-under-attack)
- [Chapter 4 Global Analysis](#chapter-4-global-analysis)
- [Chapter 5 High Profile Global Vulnerabilities](#chapter-5-high-profile-global-vulnerabilities)
- [Chapter 6 Check Point Incident Response Perspective](#chapter-6-check-point-incident-response-perspective)
- [Chapter 7 Insights for CISO’s—Predictions](#chapter-7-insights-for-cisos-predictions)
- [Chapter 8 AI: The Cutting-Edge Defender in Today's Cybersecurity Battles](#chapter-8-ai-the-cutting-edge-defender-in-todays-cybersecurity-battles)
- [Chapter 9 Malware Family Descriptions](#chapter-9-malware-family-descriptions)
- [Chapter 10 Conclusion](#chapter-10-conclusion)

---

## Chapter 1 Introduction to the 2024 Cyber Security Report

![Maya Horowitz, VP Research, Check Point]

Welcome to the Check Point 2024 Cyber Security Report. In 2023, the world of cyber security witnessed significant changes, with the nature and scale of cyber attacks evolving rapidly. This year, we saw cyber threats stepping out from the shadows of the online world into the spotlight, grabbing the attention of everyone from government agencies to the general public.

The reasons behind these attacks have become as varied as the methods used. Ransomware remained a major threat, with attackers not just after money, but also seeking recognition. Ransomware attacks exploiting zero-day vulnerabilities while using shame sites for publicly revealing who their victims are became more popular, turning ransomware into a sort of competition among cybercriminals. The cost of these attacks went beyond just paying the ransom, with companies like MGM, DP World, and the British Library facing huge expenses to rebuild their systems.

We also saw an increase in hacktivism, where hackers are driven by political or social causes. This type of hacking, once a tool for individual activists, is now being used by governments as a way to attack adversaries indirectly. This was especially noticeable in the wake of events like the Russo-Ukraine war and the Israel-Hamas conflict.

Attackers found new ways to break into systems, with devices like routers and switches becoming easy targets. Big organizations, including Okta and 23AndMe, were hit by attacks that used stolen login details or malicious software.

Artificial Intelligence (AI) played a bigger role in cyber attacks this year. Attackers started using AI tools to make their phishing campaigns more effective. However, the good news is that AI is also being used by cyber defenders to better protect against these threats.

There were some wins against cybercriminals too. Law enforcement agencies, including the FBI, made progress in taking down major threats like the Hive Ransomware network and the Qbot infrastructure. But the comeback of some of these groups reminds us that the fight against cybercrime is ongoing.

This report looks back at the major cyber security events of 2023, offering insights and analysis to help understand and prepare for the challenges ahead. Our goal is to provide valuable information to organizations, policy makers, and cyber security professionals, helping them to build stronger defenses in an increasingly digital world.

We hope you find this report informative and useful in your efforts to keep your digital environments secure.

Maya Horowitz
VP Research at Check Point Software Technologies

---

## Chapter 2 Time Line of Notable 2023 Cyber Events

### JANUARY
- A database containing over 14 million usernames and passwords was found on a dark web forum, and within this database were more than 100,000 logins for portals belonging to Australian government agencies.
- The Vice Society ransomware group has been conducting a series of widespread attacks targeting schools in both the United Kingdom and the United States. In response to these developments, the Federal Bureau of Investigation (FBI) has issued an official alert regarding the group’s activities.
  - Check Point Threat Emulation provides protection against this threat (Trojan.Wins.ViceSociety.*)
- Check Point Research reports that threat actors in hacking forums have started making use of AI tools like ChatGPT, in order to create malware and attack tools such as info-stealers and encryptors.
- Britain’s international mail service, Royal Mail, has had its operations disrupted by a cyberattack. The service has instructed its users not to post mail, as it is unable to dispatch packages to their destinations. The LockBit ransomware gang has been confirmed as the perpetrator of the attack, and is threatening to leak stolen data if its ransom demand is not met.
  - Check Point Harmony Endpoint and Threat Emulation provide protection against this threat (Ransomware.Win.Lockbit)
- Check Point Research is seeing attempts by Russian cybercriminals to bypass OpenAI’s restrictions, to use ChatGPT for malicious purposes. In underground hacking forums, hackers are discussing how to circumvent IP addresses, payment cards and phone numbers controls—all of which are needed to gain access to ChatGPT from Russia.

### FEBRUARY
- Check Point Research has flagged the Dingo crypto Token, with a market cap of $10,941,525 as a scam. The threat actors behind the token added a backdoor function in its smart contract, to manipulate the fee. Specifically, they used the “setTaxFeePercent” function within the token’s smart contract code to manipulate the buying and selling fees to an alarming 99%. The function has already been used 47 times, and investors of Dingo Token can potentially risk losing all their funds.
- KillNet, a pro-Russian hacktivists group, has launched a wide scale operation against the US healthcare sector with multiple DDoS attacks.
- JD Sports, UK sportswear retailer, has announced a data breach that affected approximately 10M clients. The alleged leaked data consists of clients’ online orders placed between November 2018 and October 2020, including full names, emails, phone numbers, billing details, delivery addresses, and more.
- Check Point Research exposed two malicious code packages, Python-drgn and Bloxflip, distributed by threat actors, leveraging package repositories as a reliable and scalable malware distribution channel.
- The group behind the massive ‘ESXiArgs’ ransomware campaign, which affected thousands of VMware ESXi hosts, has updated their malware’s encryption process. The updated version of the malware prevents the potential recovery method that was recommended by researchers, as it now also encrypts the files that could have been used to trigger the recovery process.
  - Check Point IPS provides protection against this threat (VMWare OpenSLP Heap Buffer Overflow (CVE-2019-5544; CVE-2021-21974))
- Social media platform Reddit suffered a security breach, after an employee fell victim to a phishing attack. According to the company’s statement, while internal documents and source code were stolen, user information and credentials have not been impacted.

*(Content continues for subsequent months...)*

---

## Chapter 3 Cyber Security Trends

### Ransomware Zero-days and Mega Attacks
In its current state, the term ransomware doesn’t only refer to encrypting data, but is used to characterize cyberattacks where a financially motivated actor has gained significant control over the victim's assets and exerts pressure to extort money.

Several major ransomware attacks in 2023 exploited zero-day vulnerabilities. Unlike other ransomware trends we covered previously, whether or not other actors adopt this strategy depends solely on economic considerations: Does the yield of a multi-victim ransomware attack justify the going price of a zero-day exploit used to accomplish it?

### Expanding Attack Surface: The Emerging Risk of Edge Devices
Often under-prioritized in security strategies, edge devices have long been exploited by cybercriminals to setup botnets for DDoS attacks and to orchestrate spam campaigns. In an ongoing trend that has reached its zenith this year, edge devices have become the target of nation-state APTs and financially motivated advanced threat actors.

### State-Affiliated Hacktivism and Wipers Become the New Normal
The nature of hacktivism, which uses cyber-attacks to promote political or social objectives, has significantly evolved in recent years. Initially characterized by grassroots individuals and loosely organized collectives, it has now shifted toward substantial government involvement.

---

## Chapter 4 Global Analysis
*(Content to be populated)*

## Chapter 5 High Profile Global Vulnerabilities
*(Content to be populated)*

## Chapter 6 Check Point Incident Response Perspective
*(Content to be populated)*

## Chapter 7 Insights for CISO’s—Predictions
*(Content to be populated)*

## Chapter 8 AI: The Cutting-Edge Defender in Today's Cybersecurity Battles
*(Content to be populated)*

## Chapter 9 Malware Family Descriptions
*(Content to be populated)*

## Chapter 10 Conclusion
*(Content to be populated)*

---

in late November of 2023.

fictitious attacks. Cyber Av3ngers, a group acting

While Agrius has a history of deploying wipers

as a front for Iranian-affiliated activities, published

that are sometimes disguised as ransomware,

details of attacks dating back to 2022, some of

the attack on Ziv reportedly failed to disrupt the

which were already reported by other groups.

hospital’s network, although sensitive information

This strategy of blending genuine breach reports

was stolen. Similar to how KarMa operates, the

with fabricated ones is also employed by several

stolen data was later published on the Telegram

other online groups, including one known as

channel and website of another cyber persona

Soldiers of Solomon, which is closely related to

named Malek Team, which also appeared in the

the Cyber Av3ngers. Those groups’ main focus

early days of the war.

was on programmable logic controllers (PLCs) and

Cyber Toufan Operations, another recently

introduced Iranian-affiliated cyber persona,

IOT cameras. Both Cyber Av3ngers and Soldier of

Solomon were publicly attributed to the IRGC.

was launched in November 2023 and operates

Similar to the Russian cyber-operations during the

a Telegram channel in Arabic and English. This

Ukraine conflict, which expanded a few months

group disclosed information obtained from various

into the war to target additional Western countries

Israeli businesses following a breach of an Israeli

in particular NATO member states, Iranian cyber

hosting service. Similar to previous incidents, this

activities also extended their reach westward. For

breach involved data theft followed by destructive

example, Cyber Av3ngers targeted Israeli-made

malware. Other Iranian-affiliated hacktivist groups

digital control panels, breaching several US and

that had been dormant but were reactivated during

Irish water facilities.

the current conflict include AlToufan and Moses

Staff, attributed to the Islamic Revolutionary Guard

Corps (IRGC).

Reflecting on the patterns observed in the

Ukrainian conflict, cyber activities in this recent

conflict were not solely the domain of state-

A significant portion of these cyber operations is

affiliated hacktivist groups. In the first weeks

focused on information and psychological warfare.

of the Israeli-Hamas war, the cyber warfare

This is where the main objective is to disclose

landscape saw numerous regional hacktivist

supposedly successful cyber-attacks, thus

groups, predominantly with Islamic affiliations,

emphasizing the targeted victims' vulnerabilities.

step up their activities together with the formation

These threat actors commonly exaggerate the

of hundreds of new anti-Israeli hacktivist groups.

36

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   3

These groups primarily emerged on Telegram. The

Hacktivism has evolved to a point where state-

operations carried out by these organic hacktivist

affiliated groups now dominate much of the impactful

entities mainly involved minor DDoS attacks

cyber activity. Despite this heightened involvement

and website defacements. The impact of these

from hostile governments, and the increased focus

activities was generally minor, with their effects

on destructive and disruptive activities, the actual

largely limited to screenshots shared on Telegram

effectiveness of these cyber operations remains

channels. However, significant DDoS attacks were

debatable. A significant portion of this activity

observed in the early stages of the conflict, with

often goes unnoticed in the mainstream media,

Israeli websites facing intense targeting.

overshadowed by conventional warfare reports.

In the midst of this, Russian-affiliated hacktivist

groups did not maintain neutrality. Notably,

Anonymous Sudan claimed responsibility for

several cyber-attacks against Israel. These

included a strike on the official Israeli app used

for incoming-missile-alerts to the civil population,

and an attack that took down the digital domain of

The Jerusalem Post, a leading English-language

Israeli newspaper.

As a result, these cyber actions often leave only a

minimal impression on public opinion. Considering

their limited visible impact, there is a question

of whether resources allocated to such cyber

endeavors are justified. The ongoing assessment

of the effectiveness of these state-backed cyber

operations will be crucial in determining their future

role in modern warfare strategies.

In	cyber	warfare,	“knowing	thy	enemy”	is	riddled	with
greater	complexity	than	ever	before,	as	hacktivists
commonly	represent	hidden	interests.

O M E R   D E M B I N S K Y

Data Research Group Manager,
Check Point Software
Technologies

Both	public	and	private	sector	entities	are	vulnerable
to	hacktivist	attacks,	while	the	frequency	and	magnitude
of	the	attacks	depends	mostly	on	geopolitical	events.

37

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   3

Tokens
Under Attack:
The Cloud's
Achilles Heel

Contrary to the previously documented

Man-in-the-Middle attacks, which typically

utilize frameworks such as Evilginx to intercept

communication between the victim and the service

provider to compromise user credentials and

tokens, the majority of these recent attacks involve

recovering tokens directly from third-party or

cloud service providers.

Access management and sanitization of sensitive

data is challenging, especially when dealing with

large amounts of data. This can lead to inadvertent

In the wake of the COVID-19 pandemic and

access token exposure, even in professional

the subsequent transition to remote work, the

organizations. In September 2023, an unrestricted

distinctions between on-premise and cloud-based

Azure SAS token was improperly used by Microsoft

assets have narrowed considerably. Users need

to share a bucket of open-source AI training data.

to access systems remotely, which necessitates

This led to the accidental exposure of 38 terabytes

robust authentication services for secure login.

of data that included sensitive information, private

The popularity of Single Sign-On (SSO) mechanisms

keys and passwords.

for third-party applications has further increased

the potential exposure, as a single point of failure

allows access to multiple services. To prevent or

mitigate credential theft and credential stuffing,

corporations have escalated their security protocols,

mandating more robust authentication methods

such as Multi-Factor Authentication (MFA). However,

threat actors have in turn developed strategies to

circumvent these enhanced security measures,

primarily by exploiting stolen access tokens from

already authenticated sessions. These tactics

are employed by nation-state actors as well as

financially motivated cybercriminals.

Usually, attackers have to work harder to breach

network systems. In a sophisticated cyber-attack

discovered in July, the Chinese APT group known

as Storm-0558 successfully compromised

multiple email accounts belonging to at least

25 organizations, including several U.S. Federal

agencies. This breach was achieved by exploiting

a stolen Microsoft account (MSA) consumer

signing key. This key, integral to Microsoft's

security infrastructure, is used to digitally sign

and authenticate tokens during the login process

to consumers' Microsoft accounts. According to

Microsoft's findings, the attack most likely began

with the compromise of a Microsoft engineer's

account, which gave the attackers access to

38

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   3

the engineer's debugging environment. Within

this environment, the attackers located an MSA

key that was inadvertently left in an unsanitized

crash dump. Subsequently, this key was utilized

to generate fraudulent authentication tokens for

Outlook Web Access and Outlook.com, which

enabled unauthorized access to multiple customer

accounts. Remarkably, the compromised key

dates back to April 2021.

In some instances, cybercriminals exploit access

Such attacks are not limited to cloud service

providers. Managed service providers,

authentication companies, and any entities that

may have access tokens and related sensitive

information are also targeted. In a notable

incident in October 2023, Okta, a prominent

part of the identity and authentication supply

chain, experienced a significant security breach

that affected its entire customer-support user

base. The breach was initiated through stolen

credentials, which enabled unauthorized access

to Okta's customer support management system.

This access further led to the compromise of

customer-uploaded files, including HTTP Archive

to cloud-based collaboration services such as

Microsoft Teams to leverage social engineering.

Microsoft reported a notable example in August

2023 involving a Russian APT group known as

Midnight Blizzard. This group leveraged MS Teams

to circumvent Multi-Factor Authentication (MFA)

procedures and acquire user tokens. Initially,

Midnight Blizzard infiltrated the Microsoft 365

tenants of small businesses, establishing new

domains within these tenants under the guise of

technical support entities. These domains were

then utilized for phishing attempts sent over

Microsoft Teams in which the attackers tried to

get MFA codes from users in external companies.

(HAR) files that contain critical data like cookies

The attack methodology involved sending chat

and session tokens. If not sanitized prior to upload,

requests and messages through Teams, with the

these compromised artifacts can be used to log

attackers impersonating technical support or a

in to or hijack system sessions. Customers later

security team. They persuaded users to enter a

reported attempts to use their stolen artifacts to

specific code into their Microsoft Authenticator

gain unauthorized access to their systems. Okta

app. This enabled the attackers to access the

had already suffered a serious breach in 2022.

users’ Microsoft 365 accounts and engage in

other unauthorized activities.

39

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   3

Cyber-attacks using stolen tokens can be

agent. They then extracted plaintext credentials for

conducted in a top-down approach, as seen in

a privileged Azure AD account, which enabled them

the attacks on Microsoft and Okta, where the

to wreak havoc on the Azure environment, deleting

compromise of service-providers allowed access

server farms, virtual machines, storage accounts,

to their clients' systems. Alternatively, the process

and more.

can go bottom-up, starting with the breach of

a customer's system. In this scenario, locating

tokens and sensitive data allows the attacker to

penetrate cloud services and facilitate lateral

movement throughout the victim's network.

The remote nature of cloud infrastructure

management brings unique challenges in identity

verification and security. Recent attack trends

demonstrate that cloud security is even more

vulnerable than previously thought. Advanced

An example of such an attack was seen at a leading

threat actors are increasingly bypassing end users

Israeli university. In the reported disruptive attack,

and targeting cloud service providers directly. This

actors linked to the Iranian government infiltrated

worrying shift necessitates a concerted response

a top-ranked university, the Technion – Israel

from all involved stakeholders. Incorporating

Institute of Technology. The attackers gained

comprehensive data sanitation methods is critical

on-premises access by exploiting unpatched

for ensuring robust security in cloud environments,

vulnerabilities and eventually gained entry to a

beyond traditional configuration management and

privileged account that had access to the Azure AD

Multi-Factor Authentication (MFA).

L O T E M   F I N K E L S T E E N

Director, Threat Intelligence
& Research,
Check Point Software
Technologies

As	the	cloud	services	space	grows,	novel	security	risks
are	emerging.

Last	year’s	incidents	underscore	the	challenges	and	the
need	for	innovative	methodologies	to	mitigate	the	latest
cloud	security	issues.

There	is	a	pressing	need	to	devise	robust	approaches
that	deter	threat	actors	from	targeting	both	end	users,
as	well	as	service	providers.

40

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   3

PIP Install
Malware:
Software
Repositories
Under Attack

Malicious software packages have always been

a security concern, especially in corporate

environments. Over the past year, there has been

a large increase in the number of malware spread

through open-source package platforms, while just

in the first quarter of 2023, approximately 6,800

malicious packages were identified. Hundreds

of thousands of users downloaded the malicious

packages throughout the year. The top five

malicious packages campaigns of the year alone

led to 300,000 downloads and potential infections.

Python .py files now constitute 7% of the malicious

files downloaded from the internet, compared

For decades, software developers have used

to only 3% in our previous annual report. All of

third-party software packages and libraries to speed

this happens via several common attack vectors

up development cycles. With the emergence of

like package name typosquatting, package

open-source package management platforms like

brandjacking, and dependency confusion attacks.

PyPi, NPM, NuGet and RubyGems, it has never

All of this emphasizes the importance of code

been easier to access a treasure trove of software

legitimacy verification, especially for code written

packages for any need and purpose. Unfortunately,

by unknown software developers.

as with all popular things, threat actors find ways

to abuse them for their own gain.

During the software development process,

programmers often use pre-existing packages

that contain desirable functionality from

code-sharing sources. This widespread practice

has several advantages, including reducing the

time required to write code and come up with

solutions to complex problems. In most cases,

pre-existing code performs efficiently and was

already tested for bugs and edge cases. As a

result, many open-source libraries and packages

are available in every programming language.

41

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   3

The use of open-source libraries and packages

Creating a malicious open-source package is

raises several security concerns that can be

often straightforward and can have a significant

exploited by threat actors. Due to the nature of

impact. In this type of attack, the threat actor is

open-source libraries, anyone can contribute

not only targeting the developer who downloads

and upload their code, making it difficult to track

the malicious package, but also the developer’s

and verify shared code. A prime example is

customers who use their trusted software and thus

PyPI (Python Package Index), which is the main

precipitating a software supply-chain attack.

repository of software packages for the Python

programming language. Despite recent attempts

to mitigate these threats, PyPI heavily relies on

user reports to ensure package security. Often,

by the time they are reported and removed, the

malicious packages may already have hundreds

of downloads.

Over the years, several prominent attack vectors

for open-source software package platforms were

developed by threat actors and proven feasible

by security researchers. The most common

one is typosquatting. In this type of attack, the

threat actor publishes malicious packages

with slightly misspelled names or variations of

Most programmers do not check the integrity of

popular legitimate packages, in the hope that a

open-source code before they add it to their own.

user will unintentionally download the malicious

It is challenging to understand the flow of code

version. Packages are typically installed using

written by someone else, especially if it contains

a command such as "package_manager_name

thousands of lines. In many cases, programmers

install package_name", for example, “npm install

are not aware of all possible security risks

async”. Therefore, a small mistake in the package

inherent in a piece of code, and even if they review

name can unknowingly result in the installation of

it, they might miss malicious artifacts.

a malicious package.

These malicious components can infect target

In June 2023, researchers uncovered a campaign

networks, steal and exfiltrate sensitive information

containing over 160 malicious Python packages

such as passwords and credit card information,

that had over 45,000 downloads. The threat actor

and download additional malware components.

uploaded Python packages resembling some of

the most popular packages. Among them was a

malicious package called “reaquests”, designed

to mimic the Python package "requests" that

is widely used for HTTP request operations by

millions of users.

42

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   3

Not just Python libraries but all repositories

In a recent attack against Mac computers, threat

that use open-source code sharing are targeted.

actors created a malicious version of the crypto

The NuGet repository, an open-source package

library Cobo Custody Restful to deploy malware.

manager and software distribution system for

The malicious version had the same name as the

.NET libraries, was used to launch a significant

legitimate one and was stored in the PyPI registry.

typosquatting campaign. The fraudulent packages

The threat actors took advantage of the fact that

were downloaded over 150,000 times in a single

this package does not have an official distribution

month before they were removed from the NuGet

through the PyPI registry and is distributed

repository. The malicious packages contained

only via GitHub. If the installation destination is

a PowerShell script that was executed upon

not explicitly specified, the pip install manager

installation and triggered a download of a

prioritizes the malicious PyPI version over the

second-stage payload. The final payload was a

legitimate GitHub version.

custom crypto stealer called “Impala Stealer”

which steals user credentials for cryptocurrency

exchange platforms.

It’s not only package management platforms

that are exploited. Threat actors try to subjugate

existing legitimate accounts that host open-

Cybercriminals don’t just exploit typos to deliver

source code, such as GitHub, to add malicious

malicious packages. In package brandjacking,

code to legitimate packages. This method was

the threat actor creates malicious packages with

demonstrated by researchers who took over

the same names as the legitimate ones in the

a popular NPM package with more than 3.5

hopes of fooling users into downloading them.

million weekly downloads by acquiring an expired

domain name associated with one of the package

maintainers. The recovered domain allowed them

to reset the GitHub password, making it possible to

publish Trojanized versions of the NPM packages.

43

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   3

In contrast with package brandjacking, dependency

PyPI repository with the same name and a higher

confusion attacks trick the package manager

version number than the legitimate package,

instead of the user. The threat actor exploits

causing dependency confusion. This attack

a vulnerability in the way that many package

affected thousands of machines and resulted in

managers download dependencies during a

information theft.

software build process. The attacker publishes a

package with the same name as a popular package

on a public repository, whereas the original one

is located in a private repository. This tricks the

software installer script into pulling malicious

code files. A research report from April 2023

states that 49% of all organizations are vulnerable

to this attack vector.

Malicious open-source packages are used by both

prolific threat actors and nation-sponsored actors.

The following attack was attributed to the infamous

North Korean group Lazarus. In August 2023, the

group uploaded several malicious packages to

the PyPI repository. They camouflaged one of the

packages as a VMware vSphere connector module

named “vConnector”. Another package mimicked

Earlier this year, security researchers discovered

“prettytable”, a popular Python tool for printing

that PyTorch, a widely-used machine-learning

tables in an attractive ASCII format. The legitimate

framework developed by Meta Platforms, had been

package “prettytable” has more than 9 million

compromised. The attack was initiated when a

monthly downloads, while the malicious version

threat actor uploaded a malicious package to the

“tablediter” received 736 downloads.

Figure 2: PyPI malware being distributed on an underground forum.

44

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   3

In addition, on Russian-language underground

software are undeniable, the rising wave of

forums, Check Point researchers have observed

attacks such as typosquatting, brandjacking, and

the distribution of malware tailored for the PyPI

dependency confusion reveals the limitations of

registry. This allows attackers to launch malicious

these platforms. The ease of exploiting package

attacks easily, without prior warning.

management platforms like PyPi, NPM, and

The spread of malicious packages in open-

source software repositories is a growing

concern that requires heightened attention

and proactive measures from both developers

and users. While the benefits of open-source

NuGet underscores the critical need for enhanced

security protocols and thorough code review

practices. Developers must prioritize security

to protect end-users from the consequences of

these malicious infiltrations.

Software	repositories,	like	PyPi	and	NPM,	face	a
surge	in	malicious	attacks,	with	6,800	identified
in	Q1	2023	alone.

Threats	include	typosquatting,	brandjacking,
and	dependency	confusion,	emphasizing	the	need
for enhanced security and code review practices
to	safeguard	users.

O R I   A B R A M O V S K Y

Head Of Data Science,
Check Point Software
Technologies

45

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

0
4

46

GLOBAL
ANALYSIS

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

CYBER ATTACK CATEGORIES BY REGION

GLOBAL

MULTIPURPOSE MALWARE

31%

INFOSTEALERS

12%

RANSOMWARE

10%

CRYPTOMINERS

9%

MOBILE

6%

Figure 3: Percentage of organizations affected by malware type globally in 2023.

AMERICAS

MULTIPURPOSE MALWARE

27%

INFOSTEALERS

9%

RANSOMWARE

9%

CRYPTOMINERS

8%

MOBILE

7%

Figure 4: Percentage of organizations affected by malware type in the Americas in 2023.

47

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024CYBER ATTACK CATEGORIES BY REGION

MULTIPURPOSE MALWARE

32%

INFOSTEALERS

12%

RANSOMWARE

10%

CRYPTOMINERS

8%

MOBILE

5%

Figure 5: Percentage of organizations affected by malware type in EMEA in 2023.

C H A P T E R   4

EMEA

APAC

MULTIPURPOSE MALWARE

35%

INFOSTEALERS

15%

CRYPTOMINERS

13%

RANSOMWARE

11%

MOBILE

8%

Figure 6: Percentage of organizations affected by malware type in APAC in 2023.

48

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

GLOBAL THREAT INDEX MAP

The map displays the cyber threat risk index globally, demonstrating the

main risk areas around the world.*

* Darker = Higher Risk

* Grey = Insufficient Data

Figure 7: Global T hreat Index Map

49

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

Education / Research

Government / Military

Healthcare

Communications

ISP / MSP

Finance / Banking

Utilities

Retail / Wholesale

Leisure / Hospitality

Manufacturing

Consultant

SI / VAR / Distributor

Transportation

Insurance / Legal

Software Vendor

Hardware Vendor

2046

(-12%)

1598

(-4%)

1500
1493

(+3%)

(+8%)

1286

(-6%)

1162

(+3%)

1111

(+1%)

1062

(+22%)

956
919

(+1%)

(-3%)

837
802

(+21%)

(-11%)

748
740

(-0.3%)

(-23%)

652

(-13%)

506

(+13%)

Figure 8: Global Average of weekly attacks per organization by Industry in 2023 [% of change from 2022].

The education, government, and healthcare sectors continue to be prime targets for cyber-attacks.

Enhanced awareness and a large number of impactful attacks during the last few years have led

to the launch of significant improvements in education sector security protocols, which may have

contributed to a small, recent decrease in the number of attacks against this sector. However, the

average educational institution is still hit with over 2,000 attack attempts weekly. Some attacks have

been part of larger campaigns, such as those involving Johns Hopkins University and the University

System of Georgia, which were compromised by the CL0P ransomware through the MOVEit managed

file transfer software.

50

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

Schools are particularly vulnerable to cyber-attacks due to the vast amounts of sensitive personal

information they have in their systems and lower levels of investment in cybersecurity. The private

sector—including retail, wholesale manufacturing, and financial institutions—is more likely to

acquiesce to ransom demands than public sector groups, and has seen an increase in targeting over

the previous year. Access to these institutions is often traded in underground markets.

Figure 9: Postings in an underground for um selling access to retail companies.

In 2023, the cybersecurity landscape experienced a worrying surge in ransomware attacks across

various sectors. Ransomware attacks now account for 10% of all malware types detected by

Check Point sensors. This trend is further underscored by CPIRT (Check Point Incident Response

Team) data and victim postings on ransomware “shame sites.” According to CPIRT data, nearly half

of all of the incidents they handled involved ransomware and the reported number of ransomware

victims has reached nearly 5,000 victims, a marked increase from the 2,600 reported in 2022.

51

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024
C H A P T E R   4

2018

2019

2020

2021

33%

36%

17%

16%

67%

64%

83%

84%

2022

14%

86%

2023

12%

88%

EMAIL

WEB

Figure 10: Delivery Protocols—Email vs. Web Attack Vectors in 2018-2023.

52

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024

C H A P T E R   4

TOP MALICIOUS FILE T YPES—WEB VS. EMAIL

56%

15%

8%

7%

4%

exe

sh

pdf

py

dll

2%

jar

1%

1%

1%

1%

msi

ps1

doc*

vbs

Figure 11: Web—Top malicious file types in 2023.

69%

20%

3%

2%

html

pdf

exe

lnk

1%

doc*

1%

js

1%

1%

xls*

jar

1%

rtf

0.1%

msi

Figure 12: Email—Top malicious file types in 2023.

xls* includes common Office Excel files such as .xls, .xlsx, .xlsm

doc* includes common Office Word files such as .doc, .docx, docm, and .dot

53

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

35%

25%

9%

8%

5%

rar

zip

7z

gz

img

4%

z

3%

2%

2%

2%

cab

iso

arj

xz

Figure 13: Email-delivered malicious archive file types in 2023.

Email-based attacks continue to be the dominant initial infection vector. Eighty-eight percent of

all malicious file deliveries occur through email, with the remainder downloaded directly from the

internet. Threat actors have adapted to email protection strategies and are exploring innovative

delivery techniques. Following Microsoft’s restrictions on Office VBA macros in files from external

sources denoted with the Mark-of-the-Web (MotW), there was a sharp decrease in the prevalence

of malicious Office files, from nearly 50% in 2022 to 2% in 2023. Notable alternative attack vectors

include HTML files and various archive file types. In particular, the exploitation of HTML files saw a

significant uptick. HTML files comprise 69% of all malicious file attachments.

Threat actors use HTML files in several ways. They are used in phishing schemes to imitate legitimate

website login pages and steal user credentials. They can include malicious JavaScripts or exploits to

unpatched browser and browser-plugins. As demonstrated in recent CP<R> research, these tactics

are not limited to low-level criminals but are also utilized by advanced APT actors. Other uses of

HTML include HTML smuggling, or auto download for executables and redirections to other malicious

URLs. Legitimate use cases of email-delivered HTML are unusual and therefore organizations should

consider implementing restrictions.

54

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

Utilization of various archive files has also been on the rise. The contents of password-protected

archives are hidden from many security services, thus forming an effective attack vector. Other

formats like .img and .iso depend on the software used for their extraction to propagate the MotW

functionality, which is used to prevent malicious attempts. While Microsoft has fixed this feature,

other providers like 7-zip have opt-in policies, thus decreasing the effectiveness of the MotW

protection mechanism.

The increased detection of malicious .py files, ranking fourth in the list of the most common

web-delivered malicious file types, indicates a rising use of malicious code packages. This trend is

explored in detail in a separate section. The continued decrease in the use of executables as malicious

email attachments, which dropped from 26% in 2022 to just 3% in the past year, can be attributed

to restrictive corporate policies, the integration of security mechanisms by popular email service

providers, such as Google and Microsoft, and enhanced user awareness.

55

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024
C H A P T E R   4

GLOBAL MALWARE STATISTICS

Data comparisons presented in the following sections are based on data drawn from the Check Point

Threat Cloud between January and December 2023.

For each of the regions below, we present the most prevalent malware in 2023 and the percentage of

corporate networks impacted by each malware family.

Top Malware Families

GLOBAL

11%

9%

8%

7%

5%

4%

4%

4%

4%

3%

FakeUpdates

AgentTesla
Qbot

FormBook

CloudEyE

XMRig

Emotet

Nanocore

LokiBot

Remcos

Figure 14: Most prevalent malware globally—2023

AMERICAS

10%

8%

4%

4%

3%

3%

3%

3%

3%

2%

FakeUpdates

AgentTesla
Qbot

FormBook

Emotet

CloudEyE

XMRig

Nanocore

NJRat

Remcos

Figure 15: Most prevalent malware in the Americas—2023

56

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

11%

9%

9%

8%

6%

5%

4%

4%

4%

4%

FakeUpdates

Qbot
FormBook

AgentTesla

CloudEyE

Nanocore

Emotet

LokiBot

XMRig

Remcos

Figure 16: Most prevalent malware in EMEA—2023

ASIA PACIFIC (APAC)

12% 12%

9%

9%

7%

7%

6%

5%

5%

5%

Qbot

XMRig

CloudEyE

LokiBot

NJRat

Remcos

Nanocore

AgentTesla

FakeUpdates

FormBook

Figure 17: Most prevalent malware in APAC—2023

57

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

GLOBAL ANALYSIS OF TOP MALWARE

At the top of Check Point's list for the most prevalent malware globally in 2023 is a scheme called

FakeUpdates. Also known as SocGholish, it relies on a network of compromised websites to

redirect users to fake software and browser updates. In turn, these fake updates trick users into

downloading and executing a JavaScript downloader that acts as the initial access point, enableing

further compromise through other malware such as GootLoader, NetSupport and DoppelPaymer.

The network of compromised websites is linked to TA569, a prolific threat actor who serves as an

Initial Access Broker (IAB).

TA569 is suspected of selling initial access to malware victims in a pay-per-install (PPI) pricing model to

other cybercriminals who can then leverage compromised systems to deploy ransomware. The infection

chain begins when a victim visits a compromised website, whether they were lured there by a phishing

email or they access it directly. On the website itself, the victim may encounter a fake browser update

request, or fake Captcha puzzles, and security software updates, then leading to malware infection.

Qbot, also known as QakBot or PinkslipBot, ranks second on our list. Qbot is a Windows malware

that was first discovered in 2008 as a banking Trojan. Through many updates and evolutions, it has

become one of the most well-known and longest-prevailing malware droppers out there. In fact,

Qbot has caused so much damage in terms of data theft and extortion, that in August 2023 the FBI

and the Department of Justice launched an international campaign to dismantle the botnet, remove

it from infected servers and seize over $8 million in illicit profits. In December, Qbot was observed

in new phishing campaigns.

Emotet has long persisted on Check Point’s most prevalent malware list. Despite its diluted

operational mode, it affected 4% of corporate networks globally, mostly in the first quarter of

the year. Emotet was taken down in a Europol-led global effort in November 2021, but made a

measured comeback in 2022, orchestrated by the cybercrime group Mealybug (AKA TA542)

through multiple spam campaigns alternating with prolonged periods of silence.

After Microsoft restricted the exploitation of VBA macros in downloaded documents (the principal

method used in Emotet’s campaign), Mealybug went on to explore alternative infection methods.

In 2023, Mealybug was observed trying out different techniques, and in March began using

VBScript-embedded OneNote files in their campaigns. Upon downloading the file, the victims were

lured to click the ‘View’ button to see the document contents, which would then download the

Emotet DLL. This campaign was planned to coincide with tax season deadlines in the United States.

58

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

TOP MULTIPURPOSE MALWARE

GLOBAL

AMERICAS

44%

FakeUpdates

Qbot

Emotet

Mirai

Ursnif

Ramnit

Other

21%

17%

3%

4%

8%

3%

23%

19%

40%

FakeUpdates

Qbot

Emotet

Mirai

Glupteba

Raspberry Robin

Other

3%

3%

4%

8%

Figure 18: Most prevalent multipurpose malware

Figure 19: Most prevalent multipurpose malware

globally—2023

in the Americas—2023

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

23%

19%

FakeUpdates

38%

Qbot

Emotet

Ursnif

Mirai

Phorpiex

Other

3%

4%

5%

9%

17%

48%

13%

6%

6%

5%

5%

FakeUpdates

Qbot

Ramnit

Emotet

DarkGate

Phorpiex

Other

Figure 20: Most prevalent multipurpose malware

Figure 21: Most prevalent multipurpose malware

in EMEA—2023

in APAC—2023

59

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

MULTIPURPOSE MALWARE GLOBAL ANALYSIS

As in our previous report, we have merged two malware categories, banking Trojans and botnets

and introduced instead a new unified category called 'multipurpose malware'. This change reflects

the evolution of many banking Trojans, which have acquired additional functionalities.

In addition to FakeUpdates, Qbot, and Emotet, which were discussed in the previous section,

DarkGate, a Windows RAT developed in Delphi, has also risen in popularity and is especially

prominent in campaigns targeting entities in the APAC region. In the latter half of 2023, DarkGate

gained significant notoriety for its ability to evade security system detection. In contrast to Emotet

and Qbot, which run their own infection campaigns and subsequently sell access and infections,

DarkGate employed a more direct sales strategy in a Malware-as-a-Service (MaaS) model. It was

directly advertised on underground forums to a select group of customers, highlighting its new

capabilities and limited availability. Conducted by a broad range of actors, campaigns delivering

DarkGate utilize numerous techniques, including phishing and Teams messages.

Figure 22: DarkGate pricing and offering on an underground forum during 2023.

60

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

TOP INFOSTEALER MALWARE

GLOBAL

AMERICAS

37%

20%

19%

4%

5%

5%

10%

AgentTesla

FormBook

LokiBot

Raccoon

Ramnit

Vidar

Other

20%

19%

4%

5%

5%

8%

40%

AgentTesla

FormBook

LokiBot

Vidar

Raccoon

Ramnit

Other

Figure 23: Top infostealer malware globally—2023

Figure 24: Top infostealer malware in the Americas—2023

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

23%

21%

FormBook

AgentTesla

LokiBot

Vidar

Raccoon

Ramnit

Other

3%
4%

10%

19%

19%

33%

22%

16%

4%

6%

8%

11%

AgentTesla

FormBook

LokiBot

Ramnit

Raccoon

Vidar

Other

Figure 25: Top infostealer malware in EMEA—2023

Figure 26: Top infostealer malware in APAC—2023

61

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

INFOSTEALER MALWARE GLOBAL ANALYSIS

The infostealer malware market operates mainly in a Malware-as-a-Service (MaaS) model,

involving several key players. At the heart of this ecosystem are MaaS providers, who focus on

developing and maintaining both the malware and its operational infrastructure. Infostealer

operators, who either rent or purchase the malware, deploy them in cyber-attack campaigns

against victim platforms. Underground marketplaces are crucial for trading the data harvested

from these campaigns.

In the past year, this ecosystem has seen only minimal changes, with malware such as AgentTesla,

FormBook, and LokiBot remaining prevalent. The accessibility of these infostealers is evident in

their pricing on underground forums, where they are offered for monthly subscriptions ranging from

$60 to $1,000 USD. This tiered pricing structure accommodates a wide spectrum of threat actors,

from novices to seasoned hackers. In addition, there are the Initial Access Brokers, who utilize the

purchased data to breach networks, often leading to extensive exploitation by ransomware.

AgentTesla, first identified in 2014, is a MaaS with keylogging capabilities and is one of the

infostealers commonly detected by CP<R>. Its current version has been enhanced to steal

credentials from multiple applications, including web browsers, VPN software, FTP services,

and email clients. Beyond credential theft, AgentTesla has functionalities for collecting system

information, disabling anti-malware processes, and capturing clipboard contents. AgentTesla is

adept at extracting credentials from system registries and configuration files, and it transmits

this stolen data to its command and control (C&C) server. Notably, this malware is marketed on

underground forums through low-cost subscription models, making it accessible to cybercriminals

with limited technical expertise.

62

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024

C H A P T E R   4

TOP CRYPTOMINING MALWARE

GLOBAL

AMERICAS

12%

3%

4%

8%

8%

65%

XMRig

RubyMiner

LemonDuck

Lucifer

Wannamine

Other

4%

11%

XMRig

RubyMiner

LemonDuck

Wannamine

Lucifer

Other

1%

6%

1%

75%

Figure 27: Top cryptomining malware globally—2023

Figure 28: Top cryptomining malware in the Americas—2023

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

16%

1%

2%

5%

8%

69%

XMRig

RubyMiner

LemonDuck

Lucifer

Wannamine

Other

10%

6%

7%

9%

13%

XMRig

LemonDuck

Lucifer

Wannamine

RubyMiner

Other

55%

Figure 29: Top cryptomining malware in EMEA—2023

Figure 30: Top cryptomining malware in APAC—2023

63

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

 CRYPTOMINERS GLOBAL ANALYSIS

Illegal cryptomining saw a decrease in 2023 due to Bitcoin rates not rebounding to their 2021 peak

and the continued increase in mining difficulty. Only 9% of global corporate entities were affected by

cryptominers in 2023, compared to 16% in 2022. With the increase in GPU (Graphics Processing Unit)

prices, some threat actors are now specifically targeting graphic designers and engineering platforms

for their enhanced GPU capabilities as miners. Monero remains profitable for mining, and its common

open-source mining tool, XMRig, was used in 65% of cryptomining attacks in 2023. Cryptominers

are integrating additional malicious functionalities, transforming some of them, like LemonDuck,

into multifaceted threats that span beyond their core function of mining cryptocurrency. In some

instances, as with the StripedFly malware, cryptomining activities might just be a cover for more

complex espionage operations.

Cloud infrastructure continues to be a target for cryptomining exploitation. In October, researchers

reported a years-long operation that exploited poorly secured IAM keys to access cloud environments

for deploying Monero miners. Often, the same access that allows threat actors to install a

cryptominer is later used for additional exploitation and breaches. This makes the presence of

cryptominers a potential precursor to broader security issues.

64

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024
C H A P T E R   4

TOP MOBILE MALWARE

GLOBAL

AMERICAS

16%

13%

9%

4% 8%

8%

42%

Anubis

AhMyth

Pandora

Joker

Hiddad

Hydra

Other

26%

12%

34%

3%

5%

11%

9%

Pandora

AhMyth

Anubis

Hiddad

Joker

Cerberus

Other

Figure 31: Top mobile malware globally—2023.

Figure 32: Top mobile malware in the Americas—2023.

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

46%

Anubis

AhMyth

Hiddad

Hydra

Joker

Cerberus

Other

22%

8%

8%

7%

4%

5%

21%

17%

2%
3%

6%

12%

38%

AhMyth

Joker

Anubis

Hiddad

Cerberus

Hydra

Other

Figure 33: Top mobile malware in the EMEA—2023.

Figure 34: Top mobile malware in the APAC—2023.

65

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

MOBILE MALWARE GLOBAL ANALYSIS

Mobile devices are prime targets for cyberattacks, largely due to their central role in our daily lives

and the wealth of valuable data that they contain. These devices not only store personal and financial

information but may also serve as potent surveillance tools, given their capabilities to track location,

record audio, and capture images.

The AhMyth Android Remote Access Trojan (RAT) is an open-source malware freely available on

GitHub that is often used as basis for attack campaigns. Not surprisingly, it occupies a significant

position on the Check Point top mobile malware charts. A variant of the malware, AhRat, was found

in a weaponized app called ‘iRecorder—Screen Recorder’ available in the Google Play Store with

over 50,000 downloads.

A “clean” version of the application has been available for Android users since 2021, and the malicious

characteristics were only added later. In addition to iRecorder’s self-explanatory screen-grabbing

feature, its malicious update includes sound recording and data exfiltration capabilities, including

retrieval of saved web pages, images, audio, video, document, and archive formats. The spyware

functionalities may suggest a cyber-espionage campaign, which is not uncommon in the mobile

malware world. For example, there is the Kamran Android malware which is specifically designed

to target Urdu-speaking victims in Pakistan, or the Chinese-aligned APT operated BadBazaar

Android spyware.

As always, these types of malware are also often exploited for financial gain by cyber criminals.

For example, the newly emerged Chameleon Android banking Trojan targets Australian and European

users’ mobile banking and cryptocurrency applications. A similar campaign was observed in India,

where malicious apps impersonating banks and government services were distributed via social

media platforms. Ransomware was also given a new spin within the Android ecosystem: SpyLoan

applications were spread through Google Play Store to over 12 million users in Asia, Africa and

South America. The malware collected victims’ personal and financial data from their mobile devices,

which it used to harass and blackmail them to extort funds.

66

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

RANSOMWARE

This section features information derived from

In 2023, a total of 68 active ransomware groups

almost 200 ransomware "shame sites" operated

reported they had breached the systems of

by double-extortion ransomware groups, 68

and publicly extorted over 5,000 victims. This

of which posted the names and information of

marks a substantial increase over past years.

victims from 2023. Cybercriminals use these

The ransomware events only intensified as 2023

sites to amplify pressure on victims who do not

went on. H2 recorded more than 2,800 victims

pay the ransom immediately. The data from

compared to 2,200 in the first half of the year.

these shame sites carries its own biases but still

Lockbit emerged as the most active during this

provides valuable insights into the ransomware

period, responsible for 21% of the reported

ecosystem, which is currently the number one

incidents with over 1,050 cases. Typically, threat

risk to businesses. The data presented below was

actors grant victims a one-to-two-week grace

collected for the period between January and

period to meet the ransom demands. Victims who

December 2023.

pay the ransom are not publicly exposed, which

suggests that the actual number of victims could

be significantly higher.

TOP DOUBLE-EXTORTION RANSOMWARE ACTORS

Lockbit

ALPHV

CL0P

Play

8base

Bianlian

Akira

MalasLocker

Noescape

Blackbasta

Other

21%

9%

7%

6%

34%

3%

3%

3%

4%

5% 5%

Figure 35: Most active ransomware actors by number of victims, as reported on shame sites in 2023.

67

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

ALPHV, also known as BlackCat, targeted over

CL0P's activity is underrepresented in this

440 victims in 2023and was the focus of a law

count. In early June, CL0P exploited a zero-day

enforcement operation. In December, a US-led

vulnerability that allowed it to gain access to

operation resulted in the takedown of the group's

the MOVEit file-transfer software, leading to the

websites and the release of a decryption tool.

compromise of over 2,600 organizations. Most

According to CISA, since the beginning of its

of the victims' identities were not disclosed on

operations, the group compromised more than

its shame site and therefore not included in

1,000 victims and received ransom payments

the above count. CL0P also utilized alternative

totaling nearly $300 million. The group has since

methods to further extort its victims. CL0P's

resumed its criminal operation and its presence

use of zero-day exploits this year also included

on the Dark Web.

an attack on GoAnywhere, which is detailed in

another section of this report.

USA

UK

Canada

Germany

Italy

7%

4%

4%

4%

France

3%

Australia

Spain

Brazil

India

2%

2%

2%

2%

Russia

1%

0

Figure 36: Victims by country, as reported on shame sites—2023.

30

40

10

20

45%

50

68

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   4

In terms of geographical distribution, 45% of the

landscape offers a different view. Manufacturing

affected companies are situated in the United

and retail sectors exhibit the highest number of

States, followed by the United Kingdom at 7%,

victims, while government and education entities

and Canada, Germany, and Italy each at 4%. The

are positioned lower in the target hierarchy. In

presence of Russian victims on the chart above

December 2023 alone, prominent companies

in 2023 can be attributed primarily to two actors:

like Coca-Cola Singapore (DragonForce), Nissan

MalasLocker and Werewolves. Cyberattacks on

Motor Australia (Akira), Kraft Heinz (Snatch),

entities from the former Soviet Union remain

Xerox (Inc ransom) were all claimed as victims

relatively infrequent. MalasLocker, active in the

by double-extortion ransomware groups.

first part of 2023, adopted an unconventional

approach by replacing traditional ransomware

demands with requests for charitable donations.

The aforementioned discrepancy likely arises from

differences in the willingness of these sectors to

comply with ransom demands, with educational

When analyzing the industry sectors affected

and governmental organizations being less inclined

by ransomware attacks, data from the Check

to make payments. These sectors are primarily

Point Threat Cloud highlights the education,

targeted for the exploitation of their data, including

government, and healthcare sectors as the

personal and technical information, rather than

primary targets. However, the ransomware victim

for extortion-based attacks.

22%

Manufacturing

Retail / Wholesale

Consultant

Healthcare

Education / Research

Software Vendor

Insurance / Legal

Finance / Banking

Transportation / Logistics

Government / Military

Leisure / Hospitality

Communications

ISP / MSP / IT

10%

9%

8%

7%

6%

6%

6%

5%

4%

3%

3%

3%

Energy / Utilities

2%

0

5

10

15

20

Figure 37: Industry distribution of ransomware victims, as reported on shame sites—2023.

69

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   5

0
5

70

HIGH
PROFILE GLOBAL
VULNERABILITIES

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   5

The following list of top vulnerabilities is based on data collected by the Check Point Intrusion Prevention

System (IPS) sensor net and details some of the most popular and interesting attack techniques and

exploits observed by CP<R> in 2023.

PAPERCUT (CVE-2023-27350)

This is a critical RCE (Remote Code Execution) vulnerability with a CVSS score of 9.8 in PaperCut, a print

management software with a user base of more than 100 million users. Disclosed with a patch-released

in March of 2023, this flaw can lead to the exposure of sensitive information and breach of entire

networks. Following its disclosure, it was quickly leveraged by various malicious actors, including the

delivery of Lockbit and CL0P ransomware. It was also exploitated by state-sponsored APT groups.

Check Point data shows that 9% of organizations have been impacted by this vulnerability in 2023.

MOVEIT (CVE-2023-34362)

This critical SQL injection vulnerability in MOVEit MFT (Managed File Transfer Software) was exploited

in 2023’smost prolific ransomware campaign, impacting more than 2,700 organizations globally.

The vulnerability was exploited by the CL0P ransomware group prior to its public disclosure and utilized

to deploy a web shell named LEMURLOOT, which was then used to steal data from MOVEit Transfer

databases. The large number of victims and the amount of data led CL0P to change its extortion

techniques, relying on data extortion instead of encrypting and publishing stolen data on Torrents.

Check Point data shows that 7% of organizations have been impacted by this vulnerability in 2023.

GOANY WHERE (CVE-2023-0669)

This is a critical RCE vulnerability in the GoAnywhere MFT software (Managed File Transfer) disclosed

in February 2023. Prior to its disclosure, the flaw was actively exploited by the CL0P ransomware gang,

leading to significant data breaches in more than 130 organizations. This incident highlights the growing

trend of ransomware operators using zero-day vulnerabilities to conduct their attacks. Check Point

data shows that 2.5% of organizations have been impacted by this vulnerability in 2023.

71

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   5

BARRACUDA (CVE-2023-2868)

This is a critical remote command injection vulnerability identified in the Barracuda Email Security

Gateway (ESG) appliance, which is exploited using malicious file attachments. The vulnerability was

actively exploited as early as October 2022 by a Chinese APT actor in an aggressive campaign that

impacted organizations on a global scale, with a significant focus on government agencies. Following

the release of patches and containment efforts, the attackers adapted their techniques by altering

their malware and employing additional persistence mechanisms to maintain access. As a result, both

Barracuda and the FBI recommended that customers immediately replace compromised ESG devices.

MICROSOFT OUTLOOK (CVE-2023-23397)

This is a critical privilege escalation vulnerably in Microsoft Outlook, discovered in March 2023 with a

CVSS rating of 9.8. The flaw enables attackers to hijack users’ authentication hashes via specially crafted

emails. The vulnerability was actively exploited by groups including the Russian-affiliated APT28.

CITRIXBLEED (CVE-2023-4966)

This critical vulnerability in Citrix NetScaler platforms allows remote unauthenticated attackers to

extract system memory data which includes session tokens. These are then used to hijack legitimate

sessions, bypassing password and MFA procedures. Due to its ease of use and the availability of

proof-of-concept exploits, CitrixBleed was extensively exploited by several ransomware groups including

LockBit, Medusa and Akira.

72

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   5

2023

2022

2021

2020

2019

2018

2017

2016

2015

2014

2013

Earlier

7%

6%

6%

6%

6%

10%

10%

9%

8%

3%

0

3

6

9

12

Figure 38: Percentage of attacks leveraging vulnerabilities by Disclosure Year in 2023.

14%

14%

15

In 2023, there was a noticeable shift in the cyber threat landscape, with newly disclosed vulnerabilities

being rapidly exploited by attackers. Data indicates that vulnerabilities reported in 2023 and 2022 were

responsible for 6% and 14% of all exploitation attempts, respectively. This demonstrates that recent

vulnerabilities are more severe and easy to exploit and are adopted and weaponized by threat actors

much faster than others. In comparison, relatively new vulnerabilities, disclosed between 2021 and

2023, accounted for over 30% of exploitation attempts, a marked increase from only 17% observed

in 2021 for vulnerabilities disclosed between 2019 and 2021. This trend represents a departure from

previous reliance on delayed update practices, by exploiting older, unpatched vulnerabilities, as

evidenced by the "long-tail" distribution pattern seen in previous years.

73

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024
C H A P T E R   5

MALICIOUS INFRASTRUCTURE BY TLD
(TOP LEVEL DOMAIN)

This section highlights the most frequently used malicious Top-Level Domains (TLDs) as observed

through Check Point's ThreatCloud AI in 2023. Domains, whether used to disguise phishing sites or

serving as command and control (C&C) centers for major botnets, are critical components in a threat

actor's infrastructure. Understanding trends associated with various TLDs equips defenders with

another tool for assessing potential risks. Several factors may influence threat actors’ preference

for a specific TLD, including the targeted organization they aim to impersonate, the availability of the

TLD with their preferred domain registrar, or the cost associated with acquiring the TLD.

45%

40%

35%

30%

25%

20%

15%

10%

5%

0%

Figure 39: Percentage of new malicious domains by TLD per month 2022-2023.

 The noticeable increase in new malicious .RU domains, which began in early 2022 and reached nearly

40% of new malicious domains at the onset of the Russian invasion of Ukraine, has since returned to

pre-war levels, now averaging less than three percent of new malicious domains registered monthly.

During this intense period, .RU domains consistently ranked third or fourth among all malicious TLDs.

The Russian state-aligned Gamaredon APT group is a frequent user of malicious .RU domains, and is

known for registering hundreds of domains through the REG.RU registrar in recent years.

74

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   6

0CHECK POINT
6

INCIDENT-
RESPONSE
TEAM (CPIRT)
PERSPECTIVE

75

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   6

This section is based on the experience and data from a wide array of CPIRT analyses and mitigation

cases, not limited to Check Point product users. CPIRT typically steps in after the clear manifestation

of malicious activity, such as files encrypted by ransomware, identified email compromises, or the

detection of unauthorized malware files or processes. Analysis of initial threat indicators, or ‘triggers’,

offers a different perspective of the threat landscape.

Our Incident Response Team was contacted following an EDR security alert in a customer’s

environment. Mimikatz, a notorious credential-stealing tool, was caught in the act and blocked

by the EDR system. This unusual activity raised immediate concerns, indicating the presence

of an adversary and its attempt to unobtrusively navigate the network. The client, realizing the

potential gravity of the situation, reached out to CPIRT for assistance.

UNDERSTANDING INCIDENT TRIGGERS

We define incident triggers as the first indication of a compromise that prompted the client to seek

IR services. Ransomware stands out as the predominant factor, accounting for approximately 30% of

all Incident-Triggers. Ransomware attacks are often highly visible and severely disruptive, requiring

immediate action.

11%

3%

3%

6%

14%

Ransomware

Security Alert

Behavioural Anomaly

Suspicious Email

DDoS

CERT Alert

Fraudulent Transaction

Other

30%

13%

20%

Figure 40: Breakdown of CPIRT cases by Incident trigger in 2023.

76

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024
C H A P T E R   6

Twenty percent of CIPRT cases in 2023 were triggered by an alert from a security product in the

customer’s environment. These are often alerts of the highest severity, while lower severity alerts do

not usually require the same response. Interestingly, behavioral anomalies, which include any unusual

activity that the regular user observes and that deviate from established patterns, prompted 13% of

incident response (IR) engagements. This high percentage reflects their significance as a red flag for

potentially severe security issues. However, it is important to keep in mind that reports of behavioral

anomalies are often less reliable and may result in False Positives.

In the graph above, the suspicious email category refers to any suspect inbound or outbound email

activity. Suspicious outbound emails are extremely concerning, as they often indicate an email

compromise in the organization. If not detected in time, these incidents may lead to an unauthorized

money transfer, which is another common IR trigger that comprised 3% of our cases in 2023.

Incident triggers that are less frequent but still critical include CERT alerts, in which the initial

indication of compromise is provided by the local CERT, and dark web monitoring, in which the initial

alert comes from finding mentions on underground forums of a breach or offers to buy initial access.

Despite their lower prevalence, these triggers often indicate sophisticated and severe threats that

can have significant ramifications if not addressed promptly.

As we delved deeper into the incident, the plot thickened. We detected signs of data exfiltration,

coupled with the discovery of a RAT (Remote Access Tool) and encryption binaries on the Active

Directory server. These elements were prepared for a wide-scale deployment across the

network—the unmistakable precursors of a ransomware attack, mere minutes from execution.

TOP ATTACK TYPES

“Top Attack” refers to the category of the attack, not the indicator that triggered the investigation.

Analysis of the top attack types shows that ransomware is the most prevalent threat type, accounting

for 46% of IR cases. Business Email Compromise (BEC), at 19% of the cases, is detected through

indicators such as suspicious email activity or fraudulent money transfers.

In 2023, attacks thataimed to steal specific user identities, such as BEC, browser hijacking, and account

takeover were even more prevalent, with an increase of over 20% over the previous year. Contributing

to this increase was the growing reliance on cloud infrastructure as well as the prominence of access

brokers, who sell credentials and access to organizations.

77

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024
C H A P T E R   6

Ransomware

46%

Business Email Compromise

19%

DDoS

Data Theft

Phishing

8%

7%

7%

APT

3%

Other

10%

Figure 41: Breakdown of CPIRT cases by Attack Type in 2023.

0

10

20

30

40

50

POPULAR TOOLS USED IN ATTACKS

The CPIRT analysis reveals that tools such as AnyDesk and TeamViewer, which are typically benign

remote-desktop applications, are increasingly used by threat actors for Command and Control.

In fact, AnyDesk alone was used in 39% of the incidents that we analyzed this year. This tactic

underscores a stealth approach by attackers, who are leveraging tools that evade traditional malware

detection. These tools, originally intended for legitimate use, are increasingly used by threat actors,

which makes it more complicated to distinguish between conventional and malicious activities on

networks. In contrast, known malicious tools, such as Mimikatz and CobaltStrike were involved in

26% and 16% of breaches, respectively.

Further investigation into the incident revealed the use of AnyDesk as the remote command tool

of choice by the attackers, providing them with persistent access to the compromised systems.

Their initial access did not trigger security alerts, allowing the threat actor to hide in plain sight.

78

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024
C H A P T E R   6

RANSOMWARE: THE PRINCIPAL THREAT

Several families emerge as particularly prominent in the 2023 CPIRT ransomware threat landscape.

Notably, the 'Royal' ransomware has rapidly evolved to become a potent threat, accounting for a

significant number of incidents. In most cases, phishing was used as the initial access vector, often

deploying malicious PDFs or employing callback phishing tactics to install remote desktop access.

In addition, Royal actors repurposed tools like Cobalt Strike, NSudo, and PsExec for the second stages

of the attacks.

ALPHV (BlackCat) ransomware demonstrated its versatility as it was used to attack various systems,

including Windows, Linux, and VMware instances. As ALPHV operates as a Ransomware-as-a-Service

(RaaS) model, deployed by distinct affiliates, we saw a variety of entry vectors and TTPs used before its

deployment, making each incident unique and challenging to predict and defend against.

Not	all	breaches	are	leveraged	immediately.
The	initial	breach	often	begins	when	threat	actors
use	mass	scanners	to	exploit	newly	discovered
vulnerabilities	in	devices	across	the	internet.	However,
even	after	patching,	webshells	and	other	persistence
mechanisms	can	remain	intact.	These	footholds	are
often	later	sold	by	Initial	Access	Brokers	(IABs)	and	may
resurface	months	or	years	later	in	subsequent	attacks.

T I M   O T I S

Head of Global Detection
and Response,
Check Point Software
Technologies

79

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024
C H A P T E R   6

These vulnerabilities, particularly ProxyShell and Citrix RCE (CVE-2023-3519), can enable threat actors

to install webshells on internet-facing vulnerable devices. The devices targeted in those vulnerabilities,

such as Exchange servers and NetScaler Gateways, are often internet-facing, constituting prime

targets. Once compromised, these devices continue to function as dormant footholds for the threat

actor, even after patching.

While diving deeper into the incident and trying to locate the initial infection vector, we identified

CVE-2023-3519, a remote code execution vulnerability in Citrix NetScaler systems as the initial

point of compromise. This vulnerability had been exploited to deploy a webshell on the device,

which remained undetected even after the system was patched. This oversight allowed the threat

actor to maintain network access. Three months post-exploitation, this webshell was activated

by another threat actor who intended to deploy ransomware. Fortunately, due to the customer's

alertness and CPIRT's prompt response, the ransomware attack was successfully thwarted

before it could inflict damage.

This reality creates a false sense of security for administrators who believe patched devices are secure,

while actually, a threat actor's foothold might have been established much earlier. In our investigations

this year, the longest period noted for a dormant threat was 22 months.

Following the patching of vulnerabilities, security procedures must include security scans to remove

possible backdoors, webshells and other persistence mechanisms. Organizations must also continue

to monitor for any anomalies that may indicate covert threats within network infrastructure.

80

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   7

0
7

81

INSIGHTS
FOR CISO’S—
PREDICTIONS

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   7

The threat landscape is vast. Cyber security technologies are advancing, but with a limited budget,

you’re probably strategically mapping out how your organization should allocate resources.

As you consider how to best mature your cyber security infrastructure this year, Check Point’s global

team of CISOs can offer some insight.

J O N AT H A N  ‘J O N Y ’
F I S C H B E I N

Global CISO, EMEA,
Check Point Software
Technologies

Ransomware will continue and
become highly evasive

Ransomware	attacks	will	increase.	They	will	also	continue
to	impact	organizations	of	all	sizes,	extorting	millions	of
dollars	from	victims.	Most	notably,	the	threats	will	become
increasingly	evasive.

While	enterprises	are	adopting	a	lot	of	security	tools,	they’re
often	not	enough,	as	oftentimes,	they’re	not	interoperable.

Many	security	professionals	erroneously	believe	that	a
ransomware	attack	won’t	happen	to	their	organization,
and	so	they	don’t	take	adequate	action.	What	organizations
really	need	are	better	prevention	and	detection	tools.

It’s	very	important	that	organizations	take	a	holistic	approach
to	ransomware	and	develop	a	strategy	for	mitigation.	And	it’s
not	enough	to	just	have	solutions	that	ward	off	ransomware.

82

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   7

D E R Y C K   M I T C H E L S O N

Field CISO EMEA,
Check Point Software
Technologies

Organizations will continue to see
a surge in cyber attacks  and data
breaches, resulting in an explosion
of class action lawsuits and litigation
that could negatively affect CISOs

Litigation	is	becoming	increasingly	common.	There’s	no	doubt
about	it.	Many	major	enterprises	have	experienced	breaches
and	paid	out	significant	sums	of	money	on	the	back	of	them.

The	issue	won’t	solely	affect	larger	organizations.	Smaller
organizations	will	be	affected	as	well	and	will	likely	pay	out
millions	in	order	to	satisfy	shareholders	and	individuals	who
have	been	breached.

This	increase	in	data	breach	class	actions	is	really
concerning.	There’s	been	a	two-fold	increase	in	them
from	2022	to	2023.

Further,	recent	survey	results	show	that	62%	of	CISOs	are
concerned	about	their	personal	liability	when	it	comes	to
breaches.	What’s	driving	this?	The	first	item	is	the	Uber	case,
where	the	Uber	CISO	was	found	guilty.

83

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   7

P E T E   N I C O L E T T I

Field CISO, Americas,
Check Point Software
Technologies

AI-based tools will be used by cyber
criminals to steal financial resources

Something that Check Point Research	has	just	begun	to	point
out	is	that	criminals	are	using	unregistered	and	unguarded	AI
tools	and	engines	for	nefarious	purposes.	Those	tools	aren’t
subject	to	laws	and	regulations.

Cyber	security	professionals	are	liable	to	see	what	could	be
termed	‘ghost	guns’	or	‘unserialized	weapons’	used	in	the
AI	fight.	Check	Point’s	ThreatCloud	and	other	power-packed
products	help	mitigate	this	issue,	but	in	the	future,	more	will
need	to	be	done	to	address	it.

84

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   8

0
8

85

AI:
THE CUTTING-EDGE
DEFENDER IN TODAY'S
CYBERSECURITY BATTLES

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   8

In the ever-evolving landscape of cybersecurity, artificial intelligence (AI) has emerged as a

game-changer, revolutionizing the way we prevent, protect against and respond to cyber threats.

AI's transformative impact in this domain is profound, offering unprecedented advantages in identifying,

analyzing, and neutralizing cyber risks. By leveraging complex algorithms and machine learning,

AI systems can swiftly detect patterns indicative of malicious activities, often identifying threats

far more rapidly than traditional methods. This capability is particularly crucial in an era where

cyberattacks are becoming increasingly sophisticated and frequent. AI's ability to adapt and learn

from new threats means it continuously improves its defense strategies, making it an indispensable

ally in the ongoing battle against cybercrime. The integration of AI in cybersecurity not only enhances

the efficiency and effectiveness of security measures but also significantly reduces the time and

resources required to combat these digital dangers, thereby safeguarding our digital world with

greater precision and intelligence.

Infinity AI Copilot Transforming Cyber security with
Intelligent GenAI Automation and Support—More security.
Less time and effort.

Leveraging the convergence of AI and cloud technologies, Infinity AI Copilot addresses the growing

global shortage of cyber security practitioners by boosting the efficiency and effectiveness of

security teams.

Reduce up to 90% of the time needed to perform common administrative tasks with a Generative AI

security solution that harnesses automation and collaborative intelligence.

Unlike other AI models that work in a silo, Infinity AI Copilot delivers broad platform support for a

variety of use cases—helping manage security across the entire Infinity Platform.

Infinity AI Copilot knows the customer’s policies, access rules, objects, logs, as well as all product

documentation—allowing it to provide contextualized and complete answers.

86

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   8

Key Capabilities:

Accelerate security administration: Infinity AI Copilot saves up to 90% of the time needed

for administrative work for security tasks including event analysis, implementation, and

troubleshooting.Security professionals can dedicate more time to strategic innovation,

thanks to the time saved.

Manage and deploy security policies: manage, modify and automatically deploy access

rules and security controls, specific to each customer’s policy.

Improve incident mitigation and response: leverage AI in threat hunting, analysis and

resolution.

Oversee all solutions and environment: AI Copilot oversee all products across the entire

Check Point Infinity Platform—from network to cloud to workspace—making it a true

comprehensive assistant.

Made simple natural language processing: Interacting with Infinity AI Copilot GenAI is as

natural as a conversation with a human. It understands and responds via chat in any language,

making it easier for users to communicate and execute tasks. This natural language capability

fosters seamless interaction and effective task execution.

ThreatCloud AI is Check Point’s Big Data Intelligence engine. It uses 50+ AI and Machine Learning

technologies that identify and block emerging threats that were never seen before. Out of the 50

AI-based engines 11 uses Deep Learning technology and 38 Classic Machine Learning technology.

During 2023 we’ve added 12 new engines:

2
Deep	Learning

7
Classic	Machine
Learning

3
Traditional

ThreatCloud AI aggregates and analyzes big data telemetry and millions of Indicators of compromise

(IoCs) every day. Its threat intelligence database is fed from 150,000 connected networks and millions of

endpoint devices, as well as Check Point Research and dozens of external feeds. ThreatCloud AI updates

newly revealed threats and protections in real-time across Check Point’s entire security stack.

87

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024

COLLABORATIVE SECURITY—THREATCLOUD AI
AI is All About Your Data

C H A P T E R   8

COUNTED
DAILY!

2,800,000,000
Websites	and
files	inspected

146,000,000
Full	content
emails

53,000,000
File
emulations

20,000,000
Potential	IoT
devices

2,600,000
Malicious
indicators

1,500,000
Newly	installed
mobile	apps

1,200,000
Online	web
forms

BIG DATA THREAT INTELLIGENCE

Here are some of the ways ThreatCloud AI prevents emerging cyber threats:

ThreatCloud Graph:
A Multi-Dimensional Perspective on Cyber Security

This innovative feature is moving beyond the traditional analysis of standalone entities, such as URLs,

IPs, and domain names. ThreatCloud Graph delves into the interconnected web of relationships between

these entities, unveiling a multi-dimensional perspective on cyber threats.

ThreatCloud Graph’s innovative approach in analyzing the interconnected web of relationships in the

cyber threat landscape provides a powerful tool for proactive threat prevention, insightful attack

detection, and robust defense against zero-day threats.

88

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   8

Main Benefits:

1

Holistic Threat Prevention

ThreatCloud Graph offers a comprehensive view of cyber threats by analyzing the relationships

between various entities, such as URLs, IPs, and domain names. This approach goes beyond examining

standalone threats, providing a multi-dimensional perspective that focuses on proactive prevention.

This holistic perspective allows for a deeper understanding of how threats are interconnected

and how they operate within larger networks and campaigns.

2

Graph Patterns and Attack Insight

By identifying unique patterns of relations between different cyber entities, ThreatCloud Graph

provides valuable insights into malicious activities. This feature is particularly useful in detecting

and understanding complex attacks like DNS poisoning. The ability to recognize these patterns

and links between common entities facilitates the early detection and prevention of

sophisticated cyber threats, enhancing overall security.

3

Preventing Zero-Day Emerging Threats

Leveraging the knowledge of ThreatCloud AI, ThreatCloud Graph is adept at preventing emerging

threats, including zero-day attacks. It establishes the reputation of URLs, domains, and IP addresses

based on their relations to previously known malicious artifacts. This preemptive approach,

which does not rely solely on detected malicious content, allows for the early identification and blocking

of potential threats, ensuring robust protection against the most advanced and emerging attacks.

89

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   8

AI-powered Brand Spoofing Prevention

Expanding our zero-phishing offering, we’ve intoroduced our innovative AI-powered engine to

prevent local and global brand impersonation employed in phishing attacks, collaboratory

protecting across networks, emails, mobile devices, and endpoints, with 40% higher catch rate

than traditional technologies.

The newly developed engine blocks links and browsing associated with local and global brands that

have been impersonated and exploited as bait to deceive victims in phishing attacks, spanning multiple

languages and countries.

AI-Powered Brand Spoofing Prevention

Protect your organization against
brand	impersonation	phishing
attacks

Real	time	blocking	of	access
to	links	that	impersonate
international	or	local	brands

40%	higher	catch	rate	than
traditional	technologies

Preemptive, real-time prevention

Utilizing	innovative	AI	technologies,	new	domains	are	auto	inspected
upon	registration	to	identify	potential	brand	spoofing	attempts	and
are	blocked	before	they	can	even	be	used	in	an	attack

Collaborative protection with ThreatCloud AI

Immediately	apply	zero	brand	spoofing	protection	across	any	attack
vector	including	email,	files,	SMS	and	more,	across	your	Network,
Endpoint,	Mobile	and	SaaS.

90

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024

C H A P T E R   8

Deep PDF—AI powered engine which provides accurate and
precise identification of malicious PDF’s without relying on
static signatures

Deep PDF’, an innovative AI model, and an integrated part of ThreatCloud AI, takes a giant leap forward

in identifying and blocking Malicious PDFs used in global scale phishing campaigns. These attacks can

be activated via a variety of vectors, including email, web downloads, HTML smuggling, SMS messages

and more. Check Point Quantum and Harmony products protect these vectors, so our customers

remain protected.

Deep PDF’- How it work?

‘Deep PDF’ engine examines the PDF structure, embedded images, URLs and Raw content, looking

for phishing layout. The power of this model is not just in the sheer volume of files it can detect, but also

in its precision, making it an asset in the constant battle against phishing campaigns and spam.

Researchers in Check Point found that PDF files have similar structure. ‘Deep PDF’ search, among

other things, for:

•  Malicious links.

•  URL placement on the document.

•

Image placement on the page.

We encode these abstract characteristics and much more to features and trained ‘Deep PDF’ to

distinguish between benign and malicious PDF files.

91

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   8

LinkGuard: a New Machine Learning Engine Designed to
Detect Malicious LNK Files

•  LinkGuard is an Machine Learning engine designed to detect malicious LNK files, now Integrated

into ThreatCloud AI

•  LNK files are often seen as harmless shortcuts, but are frequently used by cybercriminals to deliver

malware and enable social engineering attacks.

•  The new engine excels at identifying obfuscation techniques, leveraging linguistic analysis to

achieve an impressive 90%+ detection rate

LinkGuard is designed to tackle one of the Internet’s sneakiest threats: malicious LNK files. These

deceptive files, often camouflaged as harmless shortcuts, can wreak havoc on your system.

LinkGuard’s mission is clear: to detect these malicious LNK files by identifying malicious code execution

and analyzing command-line arguments.

The Essence of LinkGuard

LinkGuard is another AI-powered engine, designed to go deep into the world of LNK files, dissecting

them to their core. Its ingenious approach involves examining the very essence of these files to

determine if they harbor any signs of foul play. By scrutinizing the command-line arguments hidden

within LNK files, LinkGuard can pinpoint any traces of malicious intent. It’s like having a digital detective

that tirelessly hunts for threats, allowing you to fortify your system with confidence.

How LinkGuard Works

LinkGuard uses three fundamental principles:

1

2

3

Unmasking Obfuscation: LinkGuard excels at exposing the obfuscation techniques employed

to hide malicious code within LNK files, ensuring that even the most cunning attempts at

evasion are thwarted.

Linguistic Analysis: Leveraging, LinkGuard deciphers malicious themes embedded within

LNK files using natural language processing (NLP) . It identifies subtle linguistic patterns

indicative of malicious intent.

Recognizing Familiar Tactics: LinkGuard effectively identifies similarities to well-known

malicious code execution, promptly recognizing tactics employed by cyber adversaries.

By combining these three powerful capabilities, LinkGuard forms a invaluable shield against

LNK-based cyber threats. It not only fortifies your cybersecurity defenses but also contributes

to a safer digital environment.

92

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   9

0
9

93

MALWARE
FAMILY
DESCRIPTIONS

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   9

AgentTesla
AgentTesla is an advanced RAT functioning as a keylogger and information stealer that
is capable of monitoring and collecting the victim’s keyboard input, taking screenshots,
and exfiltrating credentials to a variety of software installed on a victim’s machine
(including Google Chrome, Mozilla Firefox and the Microsoft Outlook email client).

Akira
Akira Ransomware, first reported in the beginning of 2023, targets both Windows and
Linux systems. It uses symmetric encryption with CryptGenRandom() and Chacha 2008
for file encryption and is similar to the leaked Conti v2 ransomware. Akira is distributed
through various means, including infected email attachments and exploits in VPN
endpoints. Upon infection, it encrypts data and appends a ".akira" extension to file
names, then presents a ransom note demanding payment for decryption.

ALPHV
BlackCat (aka ALPHV) operates in a ransomware-as-a-service (RaaS) business model.
BlackCat ransomware is highly customizable and allows for attacks on a wide range
of corporate environments. It targets both Linux and Windows systems, and is coded
in Rust.

AZORult
AZORult is a Trojan that gathers and exfiltrates data from the infected system. Once the
malware is installed on a system it can send saved passwords, local files, crypto-wallet
data, and computer profile information to a remote C&C server.

BiBi Wiper
BiBi Wiper is a data-wiping malware targeting both Windows and Linux systems.
Initially identified in attacks against Israeli targets, it's known for its destructive
capabilities, and is designed to overwrite data in targeted directories with junk data
and append a ".BiBi" extension to filenames.

CACTUS
CACTUS Ransomware is a destructive malware that encrypts files on a victim's
computer and adds a unique “.CTS1” extension to each encrypted file. The ransomware
is known for exploiting vulnerabilities in network systems, particularly VPN appliances,
to gain access and spread within targeted networks. It employs OpenSSL for encryption
using AES and RSA.

94

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   9

CL0P
CL0P is a ransomware that was first discovered in early 2019 and mostly targets large
firms and corporations. Cl0P is operated by a Russian-language cybercriminal gang
and employs a "steal, encrypt, and leak" strategy. It gained recent notoriety for exploiting
vulnerabilities in public-facing infrastructure like Accellion FTA and MOVEit Transfer,
enabling it to exfiltrate and encrypt sensitive data from victim organizations. Cl0P has
been involved in significant “big game hunter” ransomware attacks, targeting a variety
of industries without specific regional focus and avoiding organizations within the
Commonwealth of Independent States (CIS).

CloudEyE
CloudEye is a downloader that targets the Windows platform and is used to download
and install malicious programs on victims’ computers.

DarkGate
DarkGate, active since December 2017, is a sophisticated Malware-as-a-Service
(MaaS) known for its wide-ranging capabilities, including credential theft, keylogging,
screen capturing, and remote access. DarkGate emerged as a prominent threat within
cybercriminal circles (mainly underground forums). The malware has adapted to
circumvent security defenses and is used in diverse attack strategies, including phishing
emails and exploiting communication platforms like Microsoft Teams.

DoppelPaymer
DoppelPaymer, first noticed in 2019, is a sophisticated ransomware strain, evolving
from the earlier BitPaymer. It targets a wide range of sectors, with no specific industry
preference, and uses the Dridex Trojan for initial infiltration through spear-phishing
emails. DoppelPaymer is known for its double extortion tactic and was involved in
several notable attacks on major organizations worldwide.

Emotet
Emotet is an advanced and modular multipurpose malware. Emotet was once employed
as a banking Trojan, and now is used as a distributer for other malware or malicious
campaigns. It uses multiple methods for maintaining persistence and evasion techniques
to avoid detection. In addition, Emotet can also be spread through phishing spam emails
containing malicious attachments or links.

FakeUpdates
Fakeupdates (AKA SocGholish) is a downloader written in JavaScript. It writes the
payloads to disk prior to launching them. Fakeupdates led to further system compromise
via many additional malware, including GootLoader, Dridex, NetSupport, DoppelPaymer,
and AZORult.

95

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   9

FormBook
FormBook is an Infostealer targeting the Windows OS and was first detected in 2016.
It is marketed as Malware-as-a-Service (MaaS) in underground hacking forums for its
strong evasion techniques and relatively low price. FormBook harvests credentials
from various web browsers, collects screenshots, monitors and logs keystrokes, and
can download and execute files according to orders from its C&C.

Glupteba
Known since 2011, Glupteba is a Windows backdoor that gradually matured into a botnet.
By 2019 it included a C&C address update mechanism through public Bitcoin lists, an
integral browser stealer capability, and a router exploiter.

GootLoader
GootLoader is a stealthy malware, primarily used as a first-stage downloader attacking
Windows-based systems. Initially serving as a downloader for the GootKit banking
Trojan, it has evolved into a multi-payload malware platform capable of delivering
sophisticated second-stage payloads like Cobalt Strike beacon and REvil ransomware.
GootLoader uses SEO poisoning to redirect victims to compromised websites for
drive-by download campaigns, impacting various industries across multiple countries.
It employs advanced techniques like reflective loading and PowerShell commands for
persistence and evasion.

Horse Shell
Horse Shell is a custom malware utilized by the Chinese state-sponsored hacking
group "Camaro Dragon" for targeting European foreign affairs organizations.
Discovered in January 2023, this malware infects residential TP-Link routers,
enabling attackers to gain complete control over these devices. Horse Shell operates
as a backdoor, executing shell commands, transferring files, and using the router
as a SOCKS proxy for communications.

Impala Stealer
Impala Stealer is a crypto-stealing malware targeting .NET developers through
malicious NuGet packages. It operates by installing a persistent backdoor to access
and steal cryptocurrency account details, utilizing typosquatting to disguise itself as
legitimate software packages

96

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   9

JaguarTooth
JaguarTooth is a Cisco IOS malware that targets and modifies routers' authentication
mechanisms to allow unauthenticated backdoor access. It collects and exfiltrates device
and network information, including firmware versions and network configurations,
via the Trivial File Transfer Protocol (TFTP). JaguarTooth was deployed through the
exploitation of a known Simple Network Management Protocol (SNMP) vulnerability,
CVE-2017-6742.

KV-botnet
The KV-Botnet, linked to the China-linked threat actor Volt Typhoon, is a sophisticated
botnet that primarily targets small office/home office (SOHO) router devices. Active
since at least February 2022, it consists of two complementary activity clusters named
KV and JDY.

LemonDuck
LemonDuck is a cryptocurrency-mining botnet which targets victims' computer
resources to mine the Monero virtual currency. It employs various methods to spread
across the network, such as sending infected RTF files using email, psexec, WMI, and
SMB exploits, including the infamous Eternal Blue and SMBGhost threats that affect
Windows 10 machines.

LEMURLOOT
LEMURLOOT is a web shell malware associated with the CL0P ransomware group,
designed to exploit a critical SQL injection vulnerability (CVE-2023-34362) in the MOVEit
Transfer managed file transfer (MFT) application. LEMURLOOT is written in C# and
requires a hard-coded password for authentication. This malware was instrumental in
significant data theft and extortion attempts by the CL0P group.

LockBit
LockBit is a ransomware, operating on a RaaS model, first reported in September 2019.
LockBit targets large enterprises and government entities from various countries and
does not target individuals in Russia or the Commonwealth of Independent States.

LokiBot
LokiBot is a commodity infostealer for Windows. It harvests credentials from a variety
of applications, web browsers, email clients, IT administration tools such as PuTTY, and
more. LokiBot was sold on hacking forums and its source code is believd to have leaked,
thus allowing for a range of variants to appear. It was first identified in February 2016.

97

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   9

Lucifer
Lucifer is a hybrid malware known for its capabilities in both cryptojacking and
launching Distributed Denial-of-Service (DDoS) attacks. Leveraging multiple high and
critical severity exploits, Lucifer originally targeted the Windows system. However, it
recently evolved into a multi-platform and multi-architecture malware targeting Linux,
and IoT devices, and has separate ARM and MIPS versions.

Medusa
Medusa ransomware, active since June 2021, is a Ransomware-as-a-Service (RaaS)
model employing a double-extortion tactic (encrypts and exfiltrates data, threatening
to leak or sell it if the ransom isn't paid.)

Mirai
Mirai is an infamous Internet-of-Things (IoT) malware that tracks vulnerable IoT devices,
such as web cameras, modems and routers, and turns them into bots. The botnet is
used by its operators to conduct massive Distributed Denial of Service (DDoS) attacks.
The Mirai botnet first surfaced in September 2016 and quickly made headlines due to
some large-scale attacks including a massive DDoS attack used to knock the entire
country of Liberia offline, and a DDoS attack against the Internet infrastructure firm
Dyn, which provides a significant portion of the United States internet's infrastructure.

Nanocore
NanoCore is a Remote Access Trojan (RAT) that targets Windows operating system
users and was first observed in the wild in 2013. All versions of the RAT contain basic
plugins and functionalities such as screen capture, cryptocurrency mining, remote
control of the desktop and webcam session theft.

NetSupport
NetSupport malware, identified as a Remote Access Trojan (RAT), targets sectors
like education, government, and business services. Originally a legitimate remote
administration tool, NetSupport was repurposed by threat actors for malicious activities
such as monitoring behavior, file transfer, and infiltrating networks.

njRAT
njRAT, aka Bladabindi, is a RAT developed by the M38dHhM hacking group. First
reported in 2012, it has been used primarily against targets in the Middle East.

98

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   9

Nokoyawa
Nokoyawa is a Windows-based ransomware family first identified in February 2022
and is known for double extortion attacks. This ransomware, initially written in C and
later rewritten in Rust, demonstrates coding similarities with the Nemty and Karma
ransomware families. The ransomware is known to exploit vulnerabilities like
CVE-2023-28252 in attacks.

Phorpiex
Phorpiex is a botnet (a.k.a Trik) that has been active since 2010 and at its peak controlled
more than a million infected hosts. It is known for distributing other malware families
via spam campaigns as well as fueling large-scale spam and sextortion campaigns.

Qbot
Qbot AKA Qakbot is a banking Trojan that first appeared in 2008. It was designed
to steal a user’s banking credentials and keystrokes. Often distributed via spam email,
Qbot employs several anti-VM, anti-debugging, and anti-sandbox techniques to hinder
analysis and evade detection.

Raccoon
Raccoon infostealer was first observed in April 2019. This infostealer targets Windows
systems and is sold as a MaaS (Malware-as-a-Service) in underground forums. It is
a simple infostealer capable of collecting browser cookies, history, login credentials,
crypto currency wallets and credit card information.

Ramnit
Ramnit is a modular banking Trojan first discovered in 2010. Ramnit steals web session
information, giving its operators the ability to steal victim credentials for all services,
including bank accounts and corporate and social network accounts. The Trojan uses
both hardcoded domains as well as domains generated by a DGA (Domain Generation
Algorithm) to contact the C&C server and download additional modules.

Raspberry Robin
Raspberry Robin is a multipurpose malware initially distributed through infected
USB devices with worm capabilities.

RedRelay
RedRelay is a shared proxy network utilized by various threat actors including the
Chinese cyber espionage actor Red Vulture. RedRelay employs features like multi-hop
proxying and encrypted communication, making analysis and attribution challenging.
The network is constructed from a combination of threat actor-operated virtual private
servers (VPS) and compromised devices.

99

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   9

Remcos
Remcos is a RAT that first appeared in the wild in 2016. Remcos distributes itself
through malicious Microsoft Office documents that are attached to SPAM emails
and is designed to bypass Microsoft Windows UAC security and execute malware
with high-level privileges.

RubyMiner
RubyMiner was first seen in the wild in January 2018 and targets both Windows and
Linux servers. RubyMiner seeks out vulnerable web servers (such as PHP, Microsoft
IIS, and Ruby on Rails) and uses them for cryptomining activity using the open source
Monero miner XMRig.

StripedFly
StripedFly, originally misclassified as a cryptocurrency miner, is a complex and versatile
wormable malware framework. Its impact is worldwide, infecting more than a million
victims since at least 2017.

Ursnif
Ursnif is a variant of the Gozi banking Trojan for Windows, whose source code was
leaked online. It has Man-in-the-Browser capabilities to steal banking information
and credentials for popular online services. In addition, it can steal information from
local email clients, browsers and cryptocurrency wallets. Finally, it can download
and execute additional files on the infected system.

WannaMine
WannaMine is a sophisticated Monero crypto-mining worm that spreads the EternalBlue
exploit. WannaMine leverages Windows Management Instrumentation (WMI) permanent
event subscriptions to spread and maintain persistence.

XMRig
XMRig is open-source CPU mining software used to mine the Monero cryptocurrency.
Threat actors often abuse this open-source software by integrating it into their malware
to conduct illegal mining on victims’ devices.

ZuoRAT
ZuoRAT is a Remote Access Trojan (RAT) with a focus on small office/home office
(SOHO) routers. Derived from the Mirai botnet, it has been operating since at least 2020.
ZuoRAT employs extensive network reconnaissance, data collection, and the hijacking of
network communications.

100

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   1 0

1
0

101

CONCLUSION

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024C H A P T E R   1 0

As we transition into the new year, last year’s patterns and

lessons should become the foundation upon which we build new

and resilient strategies.

Proactive identification of emerging trends, recognition of vulnerabilities,

and an understanding of threat actor methodologies are critical to

developing effective and sustainable cyber security programs.

The Security Report is designed to empower cyber security leaders

with the knowledge and foresight required to remain a step ahead of

cyber adversaries.

From the rise of ransomware zero-days to the emerging risks posed

by hacktivism, organizations urgently need to adapt and adopt new

security measures.

In an era where technology evolves at a breakneck pace, the insights

shared here serve as a roadmap for navigating cyber security landscape

in 2024 and beyond.

102

CHECK POINT SOFTWARE  |  SECURITY REPORT 2024CONTACT US

WORLDWIDE HEADQUARTERS

5 Shlomo Kaplan Street, Tel Aviv 6789159, Israel
Tel: 972-3-753-4599
Email: info@checkpoint.com

U.S. HEADQUARTERS

959 Skyway Road, Suite 300, San Carlos, CA 94070
Tel: 800-429-4391

UNDER ATTACK?

Contact our Incident Response Team:
emergency-response@checkpoint.com

CHECK POINT RESEARCH PODCAST
Tune in to cp<radio> to get CPR’s latest research,
plus behind the scenes and other exclusive content.
Visit us at https://research.checkpoint.com/category/cpradio/

W W W . C H E C K P O I N T . C O M

© 1994-2024 Check Point Software Technologies Ltd. All Rights Reserved.