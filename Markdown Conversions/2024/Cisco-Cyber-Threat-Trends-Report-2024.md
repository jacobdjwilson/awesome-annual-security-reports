Cyber Threat Trends Report:

From Trojan Takeovers
to Ransomware Roulette

© 2024  Cisco and/or its affiliates. All rights reserved.

1

Cyber Threat Trends Report© 2024  Cisco and/or its affiliates. All rights reserved. Cyber Threat Trends Report

Cyber Threat Trends Report:
From Trojan Takeovers
to Ransomware Roulette

Contents

Introduction: How DNS Helps Us Discover the Most Dangerous Threats

Key Findings

Threat 1: Information Stealers

Threat 2: Trojan

Threat 3: Ransomware

Threat 4: RAT (Remote Access Trojans)

Threat 5: APT (Advanced Persistent Threats)

Threat 6: Botnet

Threat 7: Dropper

Threat 8: Backdoor

Recommendations

How DNS Security Can Defend Against Top Threats

and Increase Security Resilience

© 2024  Cisco and/or its affiliates. All rights reserved.

 2

 4

 6

1

3

7

8

           10

           11

           12

           13

           15

Cyber Threat Trends Report

The threat landscape is always changing. Billions of ever-expanding connections are made every

day by organizations across the internet. There are more things to protect than ever before.

Work patterns are constantly shifting, which means organizations are more vulnerable against

increasingly sophisticated attacks.

Introduction: How DNS Helps Us Discover the Most Dangerous Threats

The domain name system (DNS) was created to

We also power all security services with the threat

connect, not to protect. It was meant to connect

intelligence of Cisco Talos. Talos is the largest

users to websites or applications quickly and

non-governmental threat research organization in

correctly, and it forms the foundation of internet.

the world, made up of an elite group of security

People use DNS billions of times a day without

experts. These massive data sets and expert security

knowing it – every time a user connects to a website,

researchers power our threat research and provide

opens an app on their phone, or updates software,

unmatched threat intelligence to stop attacks earlier.

their device queries DNS servers to find the IP

It’s this foundation that lets us see and understand

address associated with the domain.

threats sooner and block them faster.

Cisco has a unique vantage point when it comes to

Many of today’s sophisticated attacks rely on DNS

cybersecurity. We know that you can’t protect what

activity. This report looks at the top threats that

you can’t see. Because we resolve an average of 715

exploited DNS for cyberattacks, as well as how DNS-

billion daily DNS requests, we see more threats, more

layer security provides better accuracy and detection

malware, and more attacks than any other security

of malicious activity and compromised systems.

vendor in the world.

The Domain Name System (DNS) allows clients to connect to websites, perform
software updates, and use many of the applications organizations rely on.

Methodology

The following analysis is based off DNS activity observed by organizations using Cisco Umbrella.

The data covers the number of domains blocked between August 2023 through March 2024,
based of several threat categories defined by Umbrella.

The trend charts indicate whether the DNS activity in a given month is either up or down when compared

to the full time frame’s monthly average.

© 2024  Cisco and/or its affiliates. All rights reserved.

1

© 2024  Cisco and/or its affiliates. All rights reserved. Cyber Threat Trends Report

Key Findings

The three most seen threat categories were Information Stealers,
Trojans, and Ransomware. Each of these categories had average
monthly blocks in the hundreds of millions.

Information Stealer -  246 Million

Trojan -  175 Million

Ransomware -  154 Million

RAT -  46 Million

APT -  40 Million

Botnet -  31 Million

Dropper -  20 Million

Backdoor -  14 Million

© 2024  Cisco and/or its affiliates. All rights reserved.

2

Cyber Threat Trends Report

Threat #1
Information Stealers

First identified around 2020, Redline has the capability

to steal various types of personal information from an

infected computer, including stored passwords from

browsers, credit card information, cryptocurrency

wallets, VPN login credentials, FTP logins, cookies

and session data, and more. It’s typically delivered via

What is an Information Stealer?

email and malvertising campaigns, either directly or

Information stealers are malicious programs

via exploit kits and loader malware; recent research

designed to collect various kinds of personal

suggests that some cybercriminal groups are targeting

and financial information from an infected

the gaming community, leveraging fake Web3 gaming

system. They can capture keystrokes, extract

lures to deliver malware capable of stealing sensitive

files, steal browser data like passwords and

information from macOS and Windows users.

cookies, and more. Information stealers

generate large amounts of DNS traffic,

given that the threat exfiltrates data from a

compromised organization.

DNS activity surrounding

Information Stealers

10

5

0

% above

247M
average

-5

% below

-10

-15

Aug

Sept

Oct

Nov

Dec

Jan

Feb

Mar

© 2024  Cisco and/or its affiliates. All rights reserved.

3

Cyber Threat Trends Report

Our analysis - Information Stealers

The Information Stealer activity blocked includes

Information stealers persist as a significant threat

credential stealing and monitoring of audio/video

because they can covertly harvest a wealth of

communications. A trend appears with three months

sensitive data, which is highly valued on the black

of above-average activity, followed by one month of

market. The continuous creation of new variants can

below-average activity. These drops in activity could

evade detection, and the broad range of tactics for

be tied to attack groups processing large caches of

distribution, including phishing and compromised

stolen data—collect for three months, then analyze for

websites, ensures a steady stream of victims. As

one. This is something that’s been seen before in the

personal and financial data remain lucrative targets,

threat landscape over time.

information stealers are consistently updated and

deployed by cybercriminals.

Threat #2
Trojans

Qakbot is a multifunctional and sophisticated Trojan

with capabilities that include stealing banking

credentials and other personal information, as well as

providing a backdoor for attackers to install additional

malware on infected systems. Over time, QakBot has

evolved with various updates and improvements to its

evasion and propagation techniques. It can propagate

itself across networks by exploiting vulnerabilities

and using brute force attacks on account credentials,

allowing it to spread rapidly within corporate networks.

What is a Trojan?

Trojans are a type of malware that mislead

users of their true intent. They are often

disguised as legitimate software; another

common installation tactic is when a user

gets a malicious link, like an email attachment

disguised as an invoice, that once clicked on

can silently install a Trojan. Once activated,

they can enable cybercriminals to spy on you,

steal your sensitive data, and gain backdoor

access to your system.

4

Cyber Threat Trends Report© 2024  Cisco and/or its affiliates. All rights reserved. Cyber Threat Trends Report

DNS activity surrounding

Trojans

10

5

0

% above

175M
average

-5

% below

-10

-15

Aug

Sept

Oct

Nov

Dec

Jan

Feb

Mar

Our analysis - Trojans

Trojan activity was highest in August and September

Trojans continue to be a common threat due to their

2023, then declined over the remaining time frame of

deceptive nature and ability to hide in the background

this research. Despite the declines, Trojan activity is

while performing malicious activities. They are an

the second-highest across the threat categories. In the

effective means for attackers to gain unauthorized

past, Trojan activity drops have been seen alongside

access to systems, deliver additional malware, and

spikes in ransomware.

create backdoors. The ease with which Trojans can

be spread through social engineering and software

vulnerabilities contributes to their ongoing prevalence

in our threat reports.

© 2024  Cisco and/or its affiliates. All rights reserved.

5

Cyber Threat Trends Report

Threat #3
Ransomware

Lockbit is one of the more active ransomware variants

today; its ransomware operations accounted for over

What is Ransomware?

25 percent of the total number of posts made to data

Ransomware is a type of malware that encrypts

leak sites. In February 2024, multi-agency international

the files on a victim’s computer or network,

law enforcement task force managed to disrupt LockBit

making them inaccessible, and demands a

operations. However the group managed to quickly

ransom payment to decrypt them. Victims are

resume operations, utilizing new servers and encryptors.

often threatened with permanent loss of data or

exposure of stolen data if the ransom isn’t paid.

DNS activity surrounding

Ransomware

60

50

40

30

20

10

0

-10

-20

-30

-40

% above

154M
average

% below

Aug

Sept

Oct

Nov

Dec

Jan

Feb

Mar

Our analysis - Ransomware

Ransomware activity jumped in January and stayed

monetizes attacks by holding data or systems hostage

high for the rest of the observed time frame. The

for ransom. It’s high profitability, coupled with the

trends seen in ransomware closely shadow the trends

increasing availability of ransomware-as-a-service

seen in the dropper category, suggesting a correlation

platforms, allows even less skilled attackers to launch

between the two. It’s likely that the droppers we’re

campaigns. Organizations’ often inadequate backup

seeing are being used to seed ransomware payloads.

and recovery processes, and the willingness of many to

Ransomware remains a prevalent threat as it directly

pay the ransom, perpetuate the cycle of attacks.

© 2024  Cisco and/or its affiliates. All rights reserved.

6

Cyber Threat Trends Report

Threat #4
RAT (Remote Access Trojans)

As early as 2009, a RAT known as Gh0st RAT was used

in targeted attacks. It’s known for its stealthiness and for

being difficult to detect. It allows attackers to take full

control over the infected device and has been used in

espionage campaigns. Cisco Talos Threat Intelligence

noted that this threat has evolved, citing a malicious

What is a Remote Access Trojan?

campaign that likely started as early as August 2023,

RATs are a type of malware that provide a

delivering a new RAT dubbed “SugarGh0st”, with

backdoor for administrative control over the

evidence suggesting the threat actor is targeting the

targeted computer. RATs enable intruders to

Uzbekistan Ministry of Foreign Affairs and users in South

do almost anything on the targeted computer,

Korea. SugarGh0st RAT is a new customized variant

such as monitoring user behavior, accessing

of Gh0st RAT, an infamous trojan that’s been active for

confidential information, activating the system’s

more than a decade, with customized commands to

webcam, and distributing more malware.

facilitate the remote administration tasks as directed by

the C2 and modified communication protocol based on

the similarity of the command structure and the strings

used in the code.

DNS activity surrounding

Remote Access Trojans (RAT)

30

20

10

% above

46M
average

0

% below

-10

-20

-30

Aug

Sept

Oct

Nov

Dec

Jan

Feb

Mar

© 2024  Cisco and/or its affiliates. All rights reserved.

7

Cyber Threat Trends Report

Our analysis - Remote Access Trojans (RAT)

Like Trojan activity, RAT activity has trended down

RATs continue to be a favored tool for cybercriminals

over the time frame. A spike in activity seen in October

and espionage due to their ability to provide deep

coincides with a similar spike in Backdoor activity. It’s

access to compromised systems. They enable stealthy

possible that this spike could be caused by the release

surveillance, data exfiltration, and full control over

of an updated version of Cobalt Strike; version 4.9 was

victim machines, often remaining undetected for

released in late September.

extended periods. The difficulty in detecting RATs and

their multifunctional use in targeted attacks ensures

their persistence in threat landscapes.

Threat #5
APT (Advanced Persistent Threats)

Cisco Talos Threat Intelligence has identified a new threat

authored and operated by the Turla APT group, a Russian

cyber espionage threat groupm, called “TinyTurla-NG”

(TTNG) (similar to Turla’s previously disclosed implant,

TinyTurla, in coding style and functionality implementation).

Talos assessed that that TinyTurla-NG, just like TinyTurla, is

a small “last chance” backdoor that is left behind to be used

when all other unauthorized access/backdoor mechanisms

have failed or been detected on the infected systems.

What is an Advanced
Persistent Threat?

APTs are complex, sophisticated threats that

target specific entities (like organizations or

nations) with the intent to steal information

or disrupt operations. These threats are

persistent, often remaining undetected in

a network for a long time, and are carried

out by well-funded cybercriminals or state-

sponsored groups.

8

Cyber Threat Trends Report© 2024  Cisco and/or its affiliates. All rights reserved. Cyber Threat Trends Report

DNS activity surrounding

Advanced Persistent Threats (APT)

% above

40M
average

% below

15

10

5

0

-5

-10

-15

-20

Aug

Sept

Oct

Nov

Dec

Jan

Feb

Mar

Our analysis - Advanced Persistent Threats (APT)

This category, while averaging 40 million blocks a

APTs remain prevalent because of their

month, had one of the lowest rates of change—or

sophisticated, targeted, and stealthy nature, often

most stable amount activity—from one month to the

backed by nation-states or well-funded entities.

next. This classification covers highly skilled threat

Their long-term focus on espionage and intellectual

actors with resources, time, and dedication to carry

property theft, combined with their ability to remain

out sophisticated attacks.

undetected within networks for months or years,

makes them a continually evolving and persistent

threat in cybersecurity.

© 2024  Cisco and/or its affiliates. All rights reserved.

9

Cyber Threat Trends Report

Threat #6
Botnet

The Mirai botnet is a well-known example. In 2016, it was

used to launch a massive DDoS attack that took down

What is Botnet?

large parts of the internet, including services like Twitter,

A botnet is a network of infected computers,

Netflix, and Reddit. The botnet was primarily composed of

known as bots, which are controlled by a

IoT devices like cameras and DVRs that were infected by

threat actor (often called a “botmaster”). These

exploiting default usernames and passwords. Another Linux-

compromised computers can be controlled

based botnet, TheMoon, has been growing in the first part

remotely to perform malicious activities such

of 2024, reaching 40,000 endpoints in 88 countries.

as launching Distributed Denial-of-Service

(DDoS) attacks, sending spam emails, stealing

data, or spreading malware without the

knowledge of the owners.

175

150

125

100

75

50

25

0

-25

-50

% above

31M
average

% below

DNS activity surrounding

Botnet

Aug

Sept

Oct

Nov

Dec

Jan

Feb

Mar

Our analysis - Botnet

Botnet activity remained fairly stable over the observed

number of devices, including insecure IoT devices,

time frame, until a sudden spike in activity in March,

and their versatility in executing a range of malicious

which was 174% above the average for the time frame.

activities such as DDoS attacks and data theft. They are

Overall, Botnets remain a prevalent cyber threat due

to their ability to rapidly propagate across a vast

challenging to detect and dismantle because of their

decentralized command-and-control structures and

stealthy operation.

© 2024  Cisco and/or its affiliates. All rights reserved.

10

Cyber Threat Trends Report

Threat #7
Dropper

In 2019, a dropper known as “xHelper” emerged,

targeting Android devices. It was notorious for its

What is a Dropper?

persistence, being able to reinstall itself after attempts to

A dropper is a type of malware designed to

remove it manually or even after factory resets. xHelper

install other malwares onto a target system.

would download and install other malicious applications

The dropper itself does not typically cause

that could carry out various nefarious activities.

harm to the system; instead, its purpose is to

evade detection and establish a foothold, from

which it can discreetly download and execute

other malicious programs.

DNS activity surrounding

Dropper

75

50

25

% above

20M
average

0

% below

-25

-50

-75

Aug

Sept

Oct

Nov

Dec

Jan

Feb

Mar

Our analysis - Dropper

Like the Ransomware category, the dropper category

the discreet delivery of payloads. Their ability to bypass

saw a jump in activity in January that continued through

initial security measures and subsequently install more

the end of the time frame.

Droppers are still commonly reported as they play a

crucial role in multi-stage malware attacks by facilitating

destructive malware makes them a persistent tool in

the cybercriminal arsenal. As droppers evolve to evade

detection, their use in facilitating complex malware

infections keeps them relevant.

© 2024  Cisco and/or its affiliates. All rights reserved.

11

Cyber Threat Trends Report

Threat #8
Backdoor

Cobalt Strike is a legitimate software tool used primarily

for penetration testing and security assessments.

However, its powerful capabilities have also been co-

opted by cybercriminals for malicious purposes. As a

security threat, Cobalt Strike refers to the unauthorized

use of the Cobalt Strike toolset by attackers.

Cybercriminals use Cobalt Strike’s “beacon” payloads

What is a Backdoor?

for command and control (C2) of compromised systems

A backdoor is a method by which unauthorized

within a target network. Malleable C2 profiles allow

users can bypass normal authentication and

attackers to customize the beacon’s network traffic to

gain remote access to a computer or network.

blend in with normal traffic, making it harder for network

It may be an installed software or a built-in

defense systems to detect malicious communications.

feature of the hardware or software.

It also provides a suite of tools for post-exploitation

activities, including privilege escalation, lateral

movement, and reconnaissance, which attackers

can use to further their foothold within a network.

DNS activity surrounding

Backdoor

20

15

% above

10

14M
average

5

0

-5

% below

-10

-15

-20

Aug

Sept

Oct

Nov

Dec

Jan

Feb

Mar

© 2024  Cisco and/or its affiliates. All rights reserved.

12

Cyber Threat Trends Report
2024 Cyber Threat Trends Report

Our analysis - Backdoor

The majority of backdoor activity observed can be

Backdoors remain a significant threat as they provide

attributed to the use of Cobalt Strike. A spike in activity

attackers with ongoing, unauthorized access to

seen in October coincides with a similar spike in RAT

compromised systems. Their stealth and persistence

activity. It’s possible that this spike could be attributed

enable long-term exploitation for data breaches,

to the release of version 4.9 of Cobalt Strike.

surveillance, or further malicious activities. The

strategic placement of backdoors within software or

systems, often through supply chain compromises,

makes them a challenging threat to eliminate and a

consistent concern for organizations.

Recommendations

By monitoring and controlling DNS queries, security practitioners can
often identify and block malicious traffic before it reaches end-users
devices. Here are some recommendations and next steps security
practitioners should consider to bolster their defenses:

1. Leveraging DNS Security

2. Protecting Your Endpoints

3. Implementing Security Defense Strategy

© 2024  Cisco and/or its affiliates. All rights reserved.

13

Cyber Threat Trends Report

Leveraging DNS Security

•

Implement DNS filtering: Use DNS filtering services

•  Monitor DNS traffic: Regularly monitor and analyze

to block access to known malicious domains and

DNS logs for unusual patterns that may indicate

IP addresses. This can prevent connections to

malicious activity, such as a high number of DNS

command-and-control servers, phishing sites, and

queries, repeated queries for non-existent domains

other malicious online resources.

(NXDOMAIN), or frequent queries to a single domain.

•  Leverage threat intelligence: Integrate threat

•  Secure DNS resolvers: Ensure that your DNS

intelligence feeds with your security systems to keep

resolvers are securely configured to prevent DNS

the list of malicious hosts up to date. This proactive

hijacking and cache poisoning attacks. Use DNSSEC

approach helps to identify and block new threats as

(DNS Security Extensions) to protect the integrity of

they emerge.

DNS data.

Protecting Your Endpoints

•  Segment networks: Segment your network to limit

•

Implement access controls: Use the principle of

the spread of malware. If a device is compromised,

least privilege and strong authentication methods

network segmentation can prevent the malware

to minimize the potential impact of a backdoor or

from moving laterally to other parts of the network.

RAT that gains access to a system.

•  Endpoint protection: Deploy advanced endpoint

protection solutions that can detect and block

malware, including zero-day threats, by using

behavioral analysis and machine

learning techniques.

© 2024  Cisco and/or its affiliates. All rights reserved.

14

Cyber Threat Trends Report

Implementing Security Defense Strategy

•  Patch and update systems: Keep all systems

•  Plan incident response: Develop and regularly

and software updated with the latest patches

test an incident response plan so that your

to protect against known vulnerabilities that

organization is prepared to respond effectively to

could be exploited by malware such as Trojans,

cybersecurity incidents.

droppers, and backdoors.

•  Create a multi-layered defense strategy: Use a

•  Educate users: Train employees on security best

layered approach to security, combining DNS-

practices to help them identify phishing attempts

layer security with other security controls such as

and other social engineering tactics that could

firewalls, intrusion detection systems (IDS), and

lead to malware infections.

intrusion prevention systems (IPS).

•  Regularly backup data: Conduct regular backups

of critical data and ensure that these backups

are stored securely and can be restored quickly.

This is particularly important to recover from

ransomware attacks.

How DNS Security Can Defend Against Top
Threats and Increase Security Resilience

According to the Global Cyber Alliance’s Value of

Cisco is a global leader in DNS-layer security; we

DNS Security report, DNS security can mitigate

see 550 billion security events every day, 1.5 billion

one-third of cyber incidents, preventing up to $10

authentication requests per month, 2.8 million new

billion in losses. Securing the DNS layer means

samples of malware per day and discover over 200

blocking malicious domains, IP addresses, and cloud

vulnerabilities per year. Because we have end-to-end

applications before a connection is ever established.

visibility, we can protect against more threats. With

over 30,000 customers already choosing Cisco as

their trusted partner in DNS security, organizations

can be confident that their users will be better

protected through their ongoing hybrid work, cloud

transformation, and distributed environments.

© 2024  Cisco and/or its affiliates. All rights reserved.

15

Cyber Threat Trends Report

About Security Service Edge (SSE)

Security Service Edge (SSE) architecture focuses on providing secure access to services,

applications, and data across a distributed network, including cloud environments, remote locations,

and mobile users. By unifying multiple security functions, including DNS security, into a cloud service,

SSE effectively protects both users and infrastructure from threats.

About Cisco Umbrella

About Cisco Secure Access

Cisco Umbrella is part of the Cisco Security

Cisco Secure Access is the newest addition

Service Edge (SSE) product family,

to our Security Service Edge (SSE) product

powering secure internet access for all

family, and combines converged, cloud-

Cisco SSE solutions. Umbrella uses DNS to

delivered security, zero trust principles, and

stop threats over all ports and protocols to

AI-enhanced visibility to radically improve

stop malware earlier and prevent callbacks

organizations’ ability to provide secure

to attackers if infected machines connect to

access from anything to anywhere.

your network. Umbrella gives organizations

of all sizes the data and visibility they need

to block more threats faster with fewer

false positives.

Secure Access provides an extended set

of security capabilities, including secure

web gateway (SWG), cloud access security

broker (CASB), zero trust network access

As a leader in robust DNS-layer security,

(ZTNA), remote browser isolation (RBI),

Umbrella provides an added layer of

protection for users on-premises, while

also ensuring roaming users get reliable

protection for wherever their work takes

data loss prevention (DLP), cloud malware

detection, and more. It effectively secures

user access to the Internet, public SaaS

apps, and private apps, protecting them

them.  Deploy and begin stopping threats in

against sophisticated, evolving threats.

as soon as one day.

Schedule a Cisco Umbrella Demo

Schedule a Cisco Secure Access Demo

© 2024 Cisco and/or its affiliates. All rights reserved. Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks. Third-party trademarks mentioned are the property of their respective owners. The use of the word part-ner does not imply a partnership relationship between Cisco and any other company. (1110R) 1332283224   06/24