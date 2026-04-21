# 2022 SonicWall Cyber Threat Report

## Table of Contents
- [Introduction](#introduction)
- [2022 Global Cyberattack Trends](#2022-global-cyberattack-trends)
- [2021: A Turning Point in the War on Ransomware](#2021-a-turning-point-in-the-war-on-ransomware)
- [Supply Chain](#supply-chain)
- [CVEs](#cves)
- [2021 Zero-Day Vulnerabilities](#2021-zero-day-vulnerabilities)
- [The Log4j Vulnerability](#the-log4j-vulnerability)
- [Business Email Compromise](#business-email-compromise)
- [Key Findings from 2021](#key-findings-from-2021)
- [Malware](#malware)
- [Ransomware](#ransomware)

---

## Introduction

### A Note From Bill
As the world continued to grapple with the challenges of 2020, such as the ongoing COVID-19 pandemic, 2021 brought its own set of new challenges. Supply-chain woes in 2021 affected everything from healthcare, the automotive industry and cybersecurity to travel, retail and the food supply.

The growing pains of the new work reality were evident as companies opting for a permanent shift to fully remote work often found their networks, employees and processes unprepared for the change. Many businesses that stayed with the traditional work model continued to make arrangements for employees to return to the office, only to find time and again that the pandemic had other plans.

Cybersecurity faced its own set of increased challenges in 2021. The year was bookended by two major incidents: the SolarWinds attack in December 2020 and the Log4j vulnerabilities in 2021. In between, ransomware rose dramatically, far surpassing the levels we found alarming in 2020. Most other attack types showed increases as well, including overall malware, which had been on a downward slide for years.

But while some may see these challenges and default to pessimism, doing so requires an impossibly narrow view of the preceding year — one which doesn’t stand up to scrutiny. When I look back on 2021, I’m amazed at what was accomplished. SonicWall made key engineering and manufacturing changes, ensuring our partners and end users were largely unimpacted by supply-chain disruptions. We also completed the Gen 7 refresh of our next-generation firewalls, making our platform stronger, easier to use and more reliable, and unifying our portfolio across hardware, software and cloud.

Businesses outside of cybersecurity also doubled their efforts to fight cybercrime. From mid-2020 to 2021, the number of CEOs who said cybersecurity risks were the biggest threat to short-term growth nearly doubled, and corporate boards are increasingly forming cybersecurity committees. This has translated to increased funding: Global cybersecurity spending was projected to grow 12.4% by the end of 2021, twice as fast as in 2020.

At the government level, at least 45 U.S. states considered cybersecurity bills in 2021, up 18% from 2020. And the U.S., Japan, Australia, Germany and countless others passed measures strengthening national cybersecurity.

But perhaps most remarkable is the level of cooperation 2021 brought. Governments are increasingly coordinating with business and education leaders on “whole-of-nation” efforts. In June, the Group of Seven (G7) called for greater accountability in countries harboring ransomware groups. And in October, leaders from 30 countries met to formulate an international response to cybercrime. Few enemies, in our time or any other, have prompted such a unified effort.

There will be years that test us — and 2021 certainly did that — but it didn’t find us wanting. Instead, it found us, as a company, as an industry, as a civilization — innovating, fortifying, unifying. And while cybercriminals may have notched some battles this past year, in the end they spurred us on. If they want to win, they’ll have to take on all of us, together.

In this spirit of cooperation, we’re pleased to share with you the 2022 SonicWall Cyber Threat Report — full of research on cybercriminal behavior, industry trends and insight on what 2022 might have in store.

**BILL CONNER**
PRESIDENT & CEO
SONICWALL

---

## 2022 Global Cyberattack Trends

![Infographic showing 5.4 Billion Malware attacks (+167%), 60.1 Million IoT Malware (+105%), 5.3 Trillion Intrusion Attempts (+19%), 97.1 Million Cryptojacking attacks (+11%), 623.3 Million Ransomware attacks (+6%), and 10.4 Million Encrypted threats (-4%).]

*As a best practice, SonicWall routinely optimizes its methodologies for data collection, analysis and reporting. This includes improvements to data cleansing, changes in data sources and consolidation of threat feeds. Figures published in previous reports may have been adjusted across different time periods, regions or industries.*

---

## 2021: A Turning Point in the War on Ransomware

Five years ago, a debate erupted surrounding the infamous NotPetya cyberattack: Did it constitute an act of war? This issue continued to be debated in the courts throughout 2021, but on the battlefields of business networks around the world, cybercriminals were launching a full-bore offensive.

Ransomware climbed an unprecedented 105% in 2021, and the explosive growth of strategies such as double and even triple extortion ensured that these attacks were more successful than ever. But as cybercriminals have grown more sophisticated and successful, they’ve also grown more ruthless — many of the high-profile ransomware attacks in 2021 looked more like acts of war than ever before, endangering our food supply, our water supply, our fuel supply, our hospitals and our municipalities.

That the courts ultimately decided cyberattacks such as NotPetya do not, in fact, constitute acts of war is irrelevant: Fed up with cybercriminals growing rich off their constituents, leaders around the world — from the local level to the international stage — have brought the war to them.

The UN Cybersecurity Open-Ended Working Group in March 2021 endorsed a report containing cybersecurity recommendations, the first time that a process open to all countries has resulted in consensus on international cybersecurity.

In May 2021, U.S. President Joe Biden issued a sweeping executive order on cybersecurity, which unifies cybersecurity standards across government agencies, emphasizes zero-trust principles and provides specific timelines for action.

In July, INTERPOL held its forum on ransomware. Advising that effectively preventing and disrupting ransomware would require “adopting the same international collaboration used to fight terrorism, human trafficking or mafia groups,” the group called for police agencies worldwide to form a global coalition with industry partners to stop ransomware’s exponential growth.

But perhaps the biggest testament to the threat ransomware poses to national security is the involvement of the U.S. military. In an interview with The New York Times, U.S. Cyber Command head Gen. Paul M. Nakasone explained that, while he once saw ransomware as the responsibility of law enforcement, attacks such as Colonial Pipeline and JBS represented a big enough threat to the nation’s critical infrastructure to warrant a more aggressive approach.

### Cybersecurity is Infrastructure
On Nov. 15, U.S. Pres. Joe Biden signed into law the Infrastructure Investment and Jobs Act. While the bulk of the $1.2 trillion investment targets the country’s crumbling bridges, tunnels, roads and railways, it also provides $2 billion for cybersecurity, reaffirming the role of cybersecurity as part of the country’s 21st century infrastructure.

---

## Supply Chain

### Supply-Chain Attacks Continue In 2021
In December 2020, American company SolarWinds confirmed that a version of its Orion product had been targeted via the company’s supply chain, kicking off a new era in supply-chain attacks.

These attacks, referred to as “supply-chain attacks” because they infiltrate the products or services of a trusted business partner instead of targeting a company directly, are by no means new: They date back to at least 2013, when American retailer Target was attacked via its HVAC supplier. But it wasn’t until NotPetya’s spread in 2017 that people really started to understand the widespread devastation that supply-chain attacks could wreak.

Five years later, a new crop of supply-chain attacks made their mark across 2021 — many not just threatening profits and business continuity, but striking directly at our daily lives.

---

## CVEs

### Published CVEs Break 20,000 for the First Time
According to NIST, 20,136 Common Vulnerabilities and Exposures (CVEs) were published in 2021. This marks the fifth year in a row that a record number of vulnerabilities has been discovered, and the first time in history that the number of CVEs has passed the 20,000 mark.

This isn’t necessarily a milestone to celebrate, however. While the number of vulnerabilities reflects the hard work those in the cybersecurity industry are doing to identify vulnerabilities more quickly and efficiently, it also reflects pernicious trends that make quicker and more efficient work necessary in the first place.

---

## 2021 Zero-Day Vulnerabilities

Of the more than 20,000 new CVEs published in 2021, 14 were published immediately to identify and correct zero-day vulnerabilities.

| Month | CVE | Vulnerability |
| :--- | :--- | :--- |
| January | CVE-2021-1782 | Elevation of privilege vulnerability in Apple |
| February | CVE-2021-21148 | Heap buffer overflow in V8 in Google Chrome |
| March | CVE-2021-26855 | Microsoft Exchange server remote code execution vulnerability [Hafnium] |
| March | CVE-2021-26857 | Microsoft Exchange server remote code execution vulnerability [Hafnium] |
| March | CVE-2021-26858 | Microsoft Exchange server remote code execution vulnerability [Hafnium] |
| March | CVE-2021-27065 | Microsoft Exchange server remote code execution vulnerability [Hafnium] |
| May | CVE-2021-24175 | Authentication bypass in Elementor Page Builder WordPress plugin |
| May | CVE-2021-21193 | Use after free in Blink in Google Chrome |
| May | CVE-2021-22893 | Pulse Connect Secure 9.0R3/9.1R1 and higher is vulnerable to an authentication bypass vulnerability |
| July | CVE-2021-28550 | Use after free vulnerability in Acrobat Reader DC |
| July | CVE-2021-30713 | Arbitrary code execution in Apple MacOS |
| July | CVE-2021-30116 | Kaseya VSA credential disclosure [REvil ransomware] |
| August | CVE-2021-36958 | Windows Print Spooler remote code execution vulnerability |
| December | CVE-2021-44228 | Remote code execution vulnerability in Apache Log4j |

---

## The Log4j Vulnerability

While the Apache Log4j vulnerability was the final major vulnerability identified in 2021, it quicky became one of the most exploited. From Dec. 11 to Jan. 31, SonicWall recorded 142.4 million exploit attempts against Log4j vulnerabilities — an average of 2.7 million each day.

What’s remarkable, though, is how quickly hackers and cyber threat actors pivoted to exploit these vulnerabilities. It took less than 48 hours from the initial Dec. 9 PoC public disclosure for attempted exploits to reach into the hundreds of thousands, and by the third day attempts had already passed the 1 million mark.

---

## Business Email Compromise

### The Impersonators in Your Inbox
Why go to the trouble of employing obfuscation tools, launching multi-stage attacks, collecting credentials, exfiltrating data, encrypting endpoints or haggling over ransom amounts to get a payoff from your target, when you could just ask?

This is the basic premise behind Business Email Compromise (BEC) attacks, a form of cybercrime that’s becoming increasingly common. According to the FBI, nearly 20,000 of these attacks were reported in 2020 — likely a small percentage of the actual count. But despite being underreported, BEC attacks still cause the most financial damage of any attack type, far more than even ransomware.

---

## Key Findings from 2021

- **Malware May be Headed for a Rebound**: Malware was down 4% in 2021, marking both a third-straight year of decrease as well as a seven-year low. But there may be trouble on the horizon.
- **Ransomware’s Savage Reign**: In 2021, SonicWall threat researchers observed 623.3 million attacks globally. This total marked a 105% increase over 2020 and more than triple the number seen in 2019.
- **Cryptojacking: Bigger than Ever**: Cryptojacking in 2021 rose 19% globally to 97.1 million — the most attacks that SonicWall Capture Labs threat researchers have ever recorded in a single year.
- **RTDMI Gets Smarter, Faster, Better**: In Q4, RTDMI found more never-before-seen malware variants than in any quarter since its introduction in 2018. A total of 442,151 never-before-seen malware variants were identified in 2021, a 65% increase year-over-year.

---

## Malware

### Malware May Be Headed for a Rebound
Total malware continued to drop in 2021, falling 4% year-over-year to 5.4 billion hits, according to SonicWall Capture Labs threat data. This represents both the third-straight year of decrease, as well as a seven-year low — but a closer look at the data shows this trend may be shifting.

Since 2019, malware volume has been falling globally, from 5.1 billion in the second half in that year, to 3.2 billion in the first half of 2020, to 2.4 billion in the second half of 2020. But in June 2021, SonicWall Capture Labs threat researchers noted that malware in the first half of the year had gone up, rebounding to 2.5 billion (though it was still down 22% year over year.)

---

## Ransomware

### Ransomware’s Savage Reign
When ransomware started to spike in the second half of 2020, it set off alarm bells within the cybersecurity community and around the world. But the ransomware volume in the worst month of 2020 — 37.8 million, observed in November — barely exceeded the lowest point for 2021, and we would see that number more than double by year’s end.

In what would become one of the worst years for ransomware ever recorded by SonicWall, attack volume rose 105% to a staggering 623.3 million. This represented an average of 2,170 ransomware attempts per customer, and nearly 20 ransomware attempts every second.

[^1]: Source: ‘White Paper: How to Deal with Business Email Compromise,’ Osterman Research, Sponsored by SonicWall, January 2022

---

esult, SamSam made up a much higher percentage of

all ransomware in 2021 than in 2020: In 2020, 7.7% of all hits

were SamSam, but last year that more than doubled to 16.7%

To put this increase in perspective, there was not a single

There was not a single
month in 2021 where the
volume of SamSam was
lower than in 2020.

month in 2021 where the volume of SamSam was lower than

behind SamSam has a reputation for scanning the internet

in 2020. Like Ryuk — and ransomware in general — SamSam

looking for mentions on their attacks: once an attack is

volume peaked in June, setting a new record of 15.7

million attempts.

Unlike Ryuk, which is a well-known Ransomware-as-a-

Service (RaaS), SamSam is not sold in the underground, but

is instead developed privately and updated often. The group

reported or cybersecurity vendors update their signatures,

the group launches a new version. This high level of

attention has helped ensure that SamSam could continue to

operate successfully for going on seven years.

15M

10M

e
m
u
l
o
V

7,762,353
7,762,353

6,596,167
6,596,167

5M

4,927,861
4,927,861

2,104,762
2,104,762

792,103
792,103

880,425
880,425

0

Global SamSam Ransomware Volume

15,739,730
15,739,730

12,455,488
12,455,488

11,387,480
11,387,480

10,199,789
10,199,789

7,856,232
7,856,232

4,451,471
4,451,471

1,564,512
1,564,512

2,437,535
2,437,535

635,425
635,425

994,824
994,824

468,045
468,045

1,353,967
1,353,967

9,117,693
9,117,693

3,540,646
3,540,646

7,537,597
7,537,597

4,065,317
4,065,317

5,912,633
5,912,633

4,645,170
4,645,170

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

2020

2021

www.sonicwall.com

35     |     2022 SonicWall Cyber Threat Report     |     Ransomware

792,1032,104,762880,4251,564,5122,437,535635,425994,824468,0451,353,9673,540,6464,645,1704,065,3177,762,3534,927,8616,596,1674,451,47110,199,78915,739,7307,856,23211,387,48012,455,4889,117,6935,912,6337,537,597Cerber Continues Climb
Before Ryuk soared to the top of SonicWall’s ransomware

This group, through a series of ransomware attacks,

families rankings, there was Cerber. In 2019, Cerber made up

extorted over $1.3 billion in money and cryptocurrency

33% of all ransomware attacks recorded by SonicWall, but in

from a number of organizations. According to the DOJ, the

2020 it fell to roughly 13%.

Use of Cerber could be rebounding, however: In 2021, Cerber

rose 158% year over year, and now makes up 16.5% of all

ransomware hits recorded.

First developed in March 2016, Cerber was one of the first

group also allegedly created and deployed cryptojacking

applications, and developed and fraudulently marketed a

blockchain platform.

While you’d think these arrests would represent the final

chapter of WannaCry, unfortunately this isn’t the case.

examples of the RaaS business model: The operators of

Microsoft issued a software patch for EternalBlue in March

Cerber originally offered their ransomware for a 40% cut

2017, causing infections to plummet. But WannaCry continues

of any ransoms paid. Cerber has been known to spread via

to this day: In 2020, SonicWall observed 233,000 instances of

exploit kits, malicious JavaScript attached to spam, infected

WannaCry, and in 2021, there were 100,000 hits observed.

websites, fake software downloads and malvertising.

Five Years On: The (Continuing)
Legacy of WannaCry
In February 2021, the U.S. Department of Justice (DOJ)

indicted three North Korean attackers for their suspected

role in spreading WannaCry. This infamous ransomware

While these numbers are small compared with ransomware

families such as Ryuk, by now the number of vulnerable

Windows systems should be virtually zero. The fact that these

infections are still numbering in the hundreds of thousands

shows that, even five years on, there are still vulnerable

Windows systems in the wild that need to be patched.

propagated through the EternalBlue exploit, which was

And the sooner, the better: WannaCry hits peaked in April

developed by the U.S. National Security Agency, then stolen

2021, when SonicWall Capture Labs threat researchers

and leaked by a group called the Shadow Brokers.

recorded 79,849 hits — evidence that coordinated

WannaCry campaigns are still being run.

Global Cerber Ransomware Volume

15,878,177
15,878,177

14,716,564
14,716,564

12,012,444
12,012,444

16,548,803
16,548,803

12,693,859
12,693,859

3,421,076
3,421,076

3,323,555
3,323,555

3,125,680
3,125,680

2,933,076
2,933,076

4,146,171
4,146,171

1,904,068
1,904,068

1,457,264
1,457,264

7,075,612
7,075,612

5,282,685
5,282,685

4,673,306
4,673,306

1,877,733
1,877,733

1,567,936
1,567,936

2,336,786
2,336,786

6,048,478
6,048,478

6,436,889
6,436,889

5,312,774
5,312,774

3,882,344
3,882,344

2,835,726
2,835,726

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

2020

2021

www.sonicwall.com

15M

10M

e
m
u
l
o
V

5M

0

36     |     2022 SonicWall Cyber Threat Report     |     Ransomware

1,904,0681,457,2644,146,1712,933,0765,282,6851,877,7331,567,9362,336,7863,882,3446,048,4785,312,7743,421,0763,323,5553,125,68012,012,44415,878,17714,716,5644,673,3067,075,61216,548,80312,693,8592,835,7266,436,8892021 Ransomware Trends

Attackers’ Horrifying New
Tactic: Triple Extortion
In our mid-year report, we described the rising trend of

double extortion, a scam in which ransomware groups

exfiltrate data prior to issuing a ransom note and encrypting

the system, then use that data as leverage to increase the

odds of securing payment.

But some organizations still refused to pay on principle, while

others suspected — with good reason — that paying the

ransom would not actually guarantee the safety of their data.

As ransomware operators recently discovered, however,

just because an organization refuses to pay a ransom, that

doesn’t mean its customers will refuse to pay.

Like double extortion, triple extortion begins with

ransomware operators exfiltrating large quantities of data,

usually before encrypting the victim’s network. But where

double extortion groups threaten to release this data, triple

the attacker began contacting the therapy patients

themselves, attempting to extort $240 from them ($500 if

not paid within 24 hours) in exchange for not leaking their

personal therapy session notes.

Even more shocking, however, is who the criminals targeted:

The list of victims targeted included a number of children,

police officers and a dying man.

The REvil ransomware group is even adding such harassment

to its RaaS offerings. In March, the group announced that it

would, as a free service, begin making voice-scrambled VOIP

calls to notify the target’s business partners and the media

about the attack.

Infrastructure Attacks
While ransomware attacks targeting infrastructure

are certainly nothing new, these attacks ramped up

significantly in 2021.

extortionists filter through it, find out who might have the

Throughout the course of the year, just about every facet

most to lose, and then demand ransom from them, too.

of everyday life was threatened by ransomware, such as

One of the first observed triple extortion cases highlights

the ruthlessness of this scheme. In October 2020, an

hospitals, police departments, water plants, the fuel pipeline,

food producers and schools.

attacker calling himself “ransom_man” contacted Finnish

But while the payout for these sorts of attacks can be

psychotherapy provider Vastaamo. The attacker notified

enormous, so can the press coverage and government

the provider that he possessed large quantities of

scrutiny. Two ransomware groups — DarkSide and REvil —

Vastaamo’s employee and patient data and demanded a

went into hiding following successful attacks. Much of the

ransom of 40 bitcoin.

While the company reportedly paid the ransom, that wasn’t

ransom collected from Colonial Pipeline by DarkSide was

seized by the Justice Department, and REvil was arrested

enough for ransom_man. Instead of deleting the stolen data,

in early 2022.

37     |     2022 SonicWall Cyber Threat Report     |     Ransomware

Notable Infrastructure Attacks in 2021:

Colonial Pipeline – May 7, 2021

In May, cybercriminal group Darkside gained entry to

America’s largest fuel pipeline, Colonial Pipeline, via

a compromised password posted on the Dark Web. In

addition to enabling the exfiltration of nearly 100 GB of

data, the attack led to a six-day outage as the company

investigated, causing fuel shortages, gas hoarding and

panic. While Colonial reportedly paid the ransom to avoid

release of the data, the group’s gains were short lived. After

the attack drew international attention, DarkSide posted an

apology for “creating problems for society” and reportedly

disbanded soon after.

JBS Foods – May 30, 2021

The world’s largest meat producer was the victim of a

ransomware attack perpetrated by cybercriminal group

REvil. This attack forced the company to temporarily close

its beef plants in the U.S., disrupted a Canadian plant, and

brought a halt to meat processing in Australia. While JBS

claims that none of its data was exfiltrated, faced with the

prospect of a prolonged shutdown, the company admitted in

June that it had paid an $11 million ransom.

Cybercriminal group
Darkside gained entry
to America’s largest fuel
pipeline, Colonial Pipeline,
via a compromised password
posted on the Dark Web.

NEW Cooperative – September 20, 2021

In September, ransomware group BlackMatter gained access

to NEW Cooperative’s network. The cybercriminal group

reportedly stole 1 TB of data and threatened to release it

if a $5.9 million ransom was not paid. In the meantime, the

company lost access to the networks used to accept grain

shipments, deliver feed and keep feeding schedules on track

for millions of chickens, hogs and cattle.

Password Hygiene and MFA Could Have Stopped These Attacks

While these attacks were all devastating, they (along with

The Colonial Pipeline breach could almost certainly have

2020’s SolarWinds attack)  also share another commonality:

been prevented with the use of two-factor authentication.

They could have been prevented with better password

hygiene and multi-factor authentication.

For NEW Cooperative, the reuse of a weak password —

“chicken1” — on at least 10 different accounts across the

In late 2020, roughly 18,000 of SolarWinds’ customers

company’s 120 employees resulted in one of two outcomes:

received SolarWinds software infected with malicious code.

either an employee reused this password on an unrelated

In a congressional investigation, it was initially revealed

site that was breached and leaked to the Dark Web, or the

that the use of the password “solarwinds123” might have

use of brute-force attacks allowed the password to be

contributed to the breach. A SolarWinds spokesperson later

easily guessed.

refuted that claim, saying that the “credentials using that

password were for a third-party vendor application and not

for access to the SolarWinds IT systems.”

In the case of JBS, a government investigation revealed

that a weak password on an old administrator account gave

cybercriminals access to the network.

While cyberdefense has become more sophisticated and

specialized over time, in some cases the simplest prevention

is still some of the best.

38     |     2022 SonicWall Cyber Threat Report     |     Ransomware

Phishing Goes Old School
Over the past several years, we’ve observed numerous

Targets received one of two packages: One, purportedly

phishing emails imitating correspondence from Amazon or

from Amazon, arrived in a gift box accompanied by a

medical authorities. But in 2021, the FIN7 group, responsible

thank-you letter, a fake gift card and a USB drive. The other,

for the BlackMatter and Darkside ransomware operations,

disguised as a package from the U.S. Department of Health

decided to carry out a version of these campaigns the

and Human Services, included a page of guidance regarding

old-fashioned way.

COVID-19 and a USB drive.

According to an FBI alert, starting in August, this group used

If plugged in, these drives — which are loaded with “BadUSB”

UPS and USPS to snail-mail ransomware to U.S. businesses

attacks — are able to register themselves as keyboards,

in the insurance, transportation and defense industries.

emulate keystrokes, execute commands and install malware,

ultimately creating an entry point for ransomware, commonly

BlackMatter or REvil.

2021’s Biggest Busts

With the creation of the Department of Justice’s

June 7 – One month after the May 7 ransomware attack on

Ransomware and Digital Extortion Task Force, and with a

Colonial Pipeline, the Department of Justice seized 63.7

heightened focus on ransomware among government and

bitcoins from ransomware group DarkSide. This amounted to

law enforcement agencies around the world, 2021 boasted

most of the 75 bitcoin ransom paid by Colonial Pipeline.

several major busts:

June 16 – With the help of Interpol, the Ukraine National

Jan. 27 – In an attempt to disrupt NetWalker, a fast-growing

Police arrested six members of the Cl0p ransomware group,

Ransomware-as-a-Service (RaaS), authorities from the U.S.

which employs double and triple extortion attacks and have

and Bulgaria confiscated $454,000 in cryptocurrency, seized

allegedly cost victims in the U.S. and South Korea roughly

the group’s Dark Web site and arrested Sebastien Vachon-

half a billion dollars.

Desjardins of Gatineau, Quebec.

Nov. 8 – In November, 22-year-old Ukrainian national Yaroslav

Feb. 17 – French and Ukrainian officials worked together

Vasinskyi and 28-year-old Russian national Yevgeniy

to arrest several cybercriminals associated with the

Polyanin were arrested. Vasinskyi is allegedly responsible

Egregor ransomware.

June 4 – 55-year-old Alla Witte, otherwise known as Max,

was arrested for her role in infecting millions of computers

worldwide with Trickbot malware, often used in multi-stage

ransomware attacks. According to the DOJ, Witte, a member

of the Trickbot Group, reportedly worked as a malware

developer and wrote code related to the control, deployment

and payment of ransomware.

for the July 2 Kaseya ransomware attack, and Polyanin had

conducted numerous Sodinokibi/REvil ransomware attacks,

scamming millions from his victims. $6.1 million in ransom

payments was also seized during this arrest.

39     |     2022 SonicWall Cyber Threat Report     |     Ransomware

Cryptojacking

Bigger than Ever

In 2021, the number of cryptojacking attempts rose to 97

million, an increase of 19% year over year and an average of

338 cryptojacking attempts per customer network.

While cryptojacking volume didn’t see the sort of triple-

digit increases that were observed with ransomware and

encrypted attacks, this moderate increase was still enough

for 2021 to set a new all-time record.

This wasn’t the only cryptojacking record 2021 set, however.

With 34.2 million hits, the first quarter of 2021 saw more

cryptojacking than any other quarter since SonicWall

began tracking it.

But worryingly, the worst month for cryptojacking in 2021

was, by far, December: While the 13.6 million hits recorded

in December don’t eclipse the anomalous 15.5 million hits

observed in March 2020, it makes for an easy second place,

and a highly suboptimal starting point for 2022.

With 34.2 million hits, the
first quarter of 2021 saw
more cryptojacking than
any other quarter since
SonicWall began tracking it.

Global Cryptojacking Volume

e
m
u
l
o
V

15M

10M

5M

0

,

7
3
8
2
6
9
8

,

,

5
5
5
8
5
8
0
1

,

,

9
2
8
8
7
5
7

,

,

0
7
0
9
5
4
1
1

,

,

7
8
1
8
8
4
5
1

,

,

1
5
9
1
7
8
1
1

,

,

2
4
0
9
2
7
1

,

,

4
2
4
1
4
6
3

,

,

2
7
2
2
6
5
4

,

,

1
8
5
8
5
7
6

,

,

9
2
5
2
9
0
3

,

,

9
7
6
6
1
5
6

,

,

7
3
0
4
2
3
3

,

,

4
6
2
0
0
2
3

,

,

0
7
2
5
9
1
6

,

,

2
3
2
8
1
2
8

,

,

8
6
5
0
3
9
6

,

,

6
4
3
8
9
4
7

,

,

2
2
0
2
7
3
5

,

,

5
3
1
4
5
5
2

,

,

0
2
2
3
0
6
8

,

,

6
2
7
5
2
9
0
1

,

,

5
4
0
3
6
0
0
1

,

,

4
3
9
4
5
5
3
1

,

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

2020

2021

“How to Deal with Business Email Compromise,” Osterman Research, Sponsored by SonicWall, Januar y 2022

www.sonicwall.com

40     |     2022 SonicWall Cyber Threat Report     |     Cryptojacking

Cryptojacking by Region

Despite 2021 being a record-breaking year, only one region

saw a large increase: Europe, where cryptojacking volume

rose 60% according to SonicWall data.

North America saw a year-over-year rise in cryptojacking as

well, but at 13% it was fairly modest — especially compared

to the 260% jump recorded in 2020.

In Asia, cryptojacking continued the massive freefall that

began in 2019. While cryptojacking that year reached 35.7

million hits, volume fell 87% in 2020 and another 37% in

2021. Asia’s cryptojacking volume in 2021 was just under

3 million hits — less than a tenth of what it was two years ago.

North America saw a
year-over-year rise
in cryptojacking

In the U.S., cryptojacking volume rose just 4%, due in part

to a highly depressed Q3. In contrast with Q1 and Q4, which

notched 30 million hits and 23.1 million hits respectively, the

entirety of Q3 saw just 4.1 million hits — or 5.7% of the total

yearly cryptojacking volume.

Cryptojacking Volume | United States

e
m
u
l
o
V

15M

10M

5M

0

,

7
4
7
7
8
2
8

,

,

4
4
3
5
5
5
0
1

,

,

0
5
3
5
0
5
3
1

,

,

0
6
7
4
0
5
9

,

,

4
2
5
6
7
5
1

,

,

3
6
9
8
6
3
3

,

,

8
1
8
9
3
2
4

,

,

4
8
2
8
5
8
6

,

,

5
7
9
3
5
8
9

,

,

4
0
1
6
0
0
6

,

,

2
7
3
7
9
5
2

,

,

5
1
7
9
1
0
6

,

8
1
6
2
3
9

,

,

0
2
2
7
0
0
3

,

,

,

5
5
5
3
5
7
2 1
4
7
9
6
4
3

,

,

,

5
1
8
9
9
3
1

,

,

3
2
8
2
0
3
6

,

4
9
2
8
1
9

,

,

3
5
3
4
9
7
3

,

,

7
3
9
6
5
6
7

,

,

4
7
7
8
7
6
9

,

,

6
9
5
7
3
4
8

,

,

2
7
2
8
0
5
2
1

,

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

2020

2021

www.sonicwall.com

41     |     2022 SonicWall Cyber Threat Report     |     Cryptojacking

Cryptojacking by Industry

A number of industries also showed aggressive

year-over-year growth in cryptojacking volume. For

government and healthcare customers, this increase was

in the triple digits, with cryptojacking growing 709% and

218% respectively.

Despite these increases, education customers are the ones

most likely to see a cryptojacking attack. This is the second

year in a row for which this is held true, but fortunately for

education customers, the average percentage per month

who saw an attack appears to be dropping.

For government and healthcare
customers, this increase
was in the triple digits, with
cryptojacking growing 709%
and 218% respectively.

How Cryptojacking is Spreading
In years past, cryptojacking spread primarily through fileless

malware, phishing attempts with malicious links, malvertising

and more. Some cryptojacking scripts have even been

In 2021, SonicWall Capture Labs threat researchers

also observed cryptojacking spreading via pirated/

cracked software, public project hosting websites and

designed with wormlike abilities, allowing them to spread

vulnerable webservers.

across networks.

% of Customers Targeted by Cryptojacking in 2021

1

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0

d
e
t
e
g
r
a
T
%

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Overall

Government

Education

Healthcare

Retail

42     |     2022 SonicWall Cyber Threat Report     |     Cryptojacking

www.sonicwall.com

In the latter case, SonicWall Capture Labs threat researchers

It’s dropped on the victim’s machine by a number of different

in November observed malware targeting the Alibaba Cloud

types of malware, such as Vivin and BlueMockingbird, or the

(Aliyun) cloud computing program — the fourth-largest cloud

self-spreading Golang-based malware.

provider globally behind Amazon Web Services, Microsoft

Azure and Google Cloud.

After disabling Alibaba’s cloud monitoring agent and cloud

assistant service, the malware is able to execute without

notifying the machine’s owner. It disables other processes

and cryptomining services that can compete for CPU

resources, then downloads and executes the XMRig miner.

Due to being widely available and easy to use, XMRig

continued to be the cryptojacking program of choice in

2021. One of the file-based cryptojacking tools that came to

prominence following Coinhive’s shuttering in 2019, XMRig is

an open-source cross-platform miner.

The Rise of Cryptocurrency Stealers
Cybercriminals are always on the hunt for a quicker and

easier way to make money. So, when it became possible

to steal cryptocurrency from a machine directly, instead

of making the machine mine coin over time, attackers

jumped on board.

In November, SonicWall Capture Labs threat researchers

identified an Android app (see below) designed to

steal crypto wallets from victims. This malicious app

is called “Trust: Crypto & Bitcoin Wallet,” and purports

to be associated with the (legitimate) TrustWallet

cryptocurrency wallet.

43     |     2022 SonicWall Cyber Threat Report     |     Cryptojacking

But despite its name, it isn’t to be trusted: Once installed,

the malicious app requests the user grant Accessibility

Services “to confirm you as a human (not a robot),” and

notifies the user that the app will not work without these

services being turned on. Once on, this app can perform

clicks in the background without the user’s knowledge and,

by acting on behalf of the user, it automatically transfers the

cryptocurrency from the user’s wallet to the wallet of the

malware operator.

Criminals don’t always go after individuals’ crypto wallets,

however. Sometimes they attack cryptocurrency exchanges

directly. In 2021, there were over 20 attacks on crypto

exchanges or projects in which a cybercriminal stole at

least $10 million in cryptocurrencies. And in more than a

quarter of these cases, the amount stolen surpassed the

$100 million mark.

In August, the Poly Network was breached when an attacker

“exploited a vulnerability between contract calls,” and stole a

reported $610 million (all of which was ultimately returned.)

In 2021, there were over
20 attacks on crypto
exchanges or projects in
which a cybercriminal
stole at least $10 million in
cryptocurrencies. And in more
than a quarter of these cases,
the amount stolen surpassed
the $100 million mark.

platform BitMart. (Ironically, most of the digital currency

stolen was SafeMoon.) While the platform has vowed to

And in December, armed with a stolen private key, attackers

return the stolen coin with its own funds, more than a month

stole a reported $200 million in cryptocurrency from trading

later some users were still waiting to get their money back.

The True Cost of Crypto
Continues to Mount

Long gone are the days when anyone with a decent rig can

And increasingly, “someone else” means “everyone else.”

mine cryptocurrency and expect to make a healthy profit.

According to a study by The New York Times, the process

Today’s mining is complex enough that even those with

of creating bitcoin requires a whopping 91 terawatt-hours

top-tier PCs and high-end GPUs have trouble mining enough

of electricity each year — more than is used by the entire

to really make it worth their while.

nation of Finland and more than is used by Google, Facebook,

One of the “benefits” of cryptojacking, however, is that the

Apple and Microsoft combined.

costs are all borne by someone else, while the attacker reaps

From 2015 to 2021, the amount of energy used to mine

all the benefit.

Bitcoin alone increased almost 62-fold, and now amounts

to nearly half a percent of the electricity consumption of

the entire world.

44     |     2022 SonicWall Cyber Threat Report     |     Cryptojacking

Encrypted Attacks

Encrypted Attacks Show
Triple-Digit Increase

2021 was among the most turbulent years on record for

When the second half of the year arrived, it immediately

many threat trends, but the movement of encrypted attacks

brought a record of its own. A total of 864,206 encrypted

was wild even by those standards. Year over year, malware

attacks were recorded in July, narrowly edging out the

sent over HTTPs rose 167% — and on their way up, they set

previous record high of 811,144, set in August 2020.

several new records.

But while August 2020’s spike would prove to be a blip,

All told, SonicWall recorded 10.1 million encrypted attacks in

August 2021’s spike was anything but. That month saw

2021, almost as many as 2018, 2019 and 2020 put together.

attack volume surpass 1 million for the first time, and for the

This meteoric increase was driven by triple-digit increases

remainder of the year, only one month (October) would see

in North America, Europe, and Asia, where attack volume

attack volume dip below 1 million.

rose 220%, 142% and 201% respectively. Not a single region

showed a decrease in 2021.

December would bring yet another record, one that would

blow all previous totals away. From Dec. 1 to year’s end,

While you wouldn’t expect a year with triple-digit growth to

SonicWall Capture Labs threat researchers recorded a

include an all-time low, January 2021’s encrypted attack

staggering 2.5 million encrypted attacks — more than 25

volume was just that. Attacks then doubled in February, and

times the number of encrypted attacks recorded in the

then doubled again in March. But despite all this doubling,

month of January.

the first half of the year only represented about 20% of the

number of encrypted attacks we would see in 2021.

45     |     2022 SonicWall Cyber Threat Report     |     Encrypted Attacks

Encrypted Attacks by Industry
The education sector faced a deluge of attacks in 2021, but

While monthly trends were all over the place, two

it wasn’t the only one. An average of 8.8% of education

commonalities held across industries: The percentage

customers saw an encrypted attack in a given month,

of customers who saw an attack was at its lowest in

compared with 8.2% of government customers. Retail

January, and all industries saw a large spike in August that

customers, on the other hand, were comparatively spared: An

disappeared about as quickly as it came.

average of just 2.7% of customers saw an attack per month.

15

10

5

0

d
e
t
e
g
r
a
T
%

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Overall

Government

Education

Healthcare

Retail

* Organization must have a SonicWall ﬁrewall with DPI-SSL activated.

What Are Encrypted Threats?

In simple terms, TLS (Transport Layer Security) is used

Traditional security controls, such as legacy firewalls, lack

to create an encrypted tunnel for securing data over an

the capability or processing power to detect, inspect

internet connection. While TLS provides legitimate security

and mitigate cyberattacks sent via HTTPs traffic, making

benefits for web sessions and internet communications,

this a highly successful avenue for hackers to deploy and

cybercriminals increasingly use this encryption protocol to

execute malware.

hide malware, ransomware, zero-day attacks and more.

46     |     2022 SonicWall Cyber Threat Report     |     Encrypted Attacks

Intrusion Attempts

Malicious Intrusion Attempts
Fall By Nearly a Third

In 2021, SonicWall Capture Labs threat researchers recorded

2021 also ended the run of months with intrusion attempts

5.28 trillion intrusion attempts — a 10.7% increase over the

over 1 billion. This streak began in March 2020, when

number of attacks in 2020, and roughly five times as many

attempts abruptly jumped from 777 million to 1.05 billion.

attempts as there were in 2013, the first year SonicWall

Once this milestone was passed, intrusion attempts

reported this data.

remained above 1 billion for the rest of the year.

But it’s important to note that these 5.28 trillion intrusion

At the beginning of 2021, this pattern was still going strong.

attempts represent a combination of three severity types:

But in April, intrusion attempts dropped like a rock, falling

low, moderate and high. Low-severity hits typically consist

from 1.5 billion to 874 million. Once intrusion attempts

of things like scanners and pings — actions which are not

fell below 1 billion in 2021, they stayed there for the

malicious and pose no threat to the target.

rest of the year.

If we isolate the moderate and high severity intrusion

This decrease contributed to a top-heavy year: The first half

attempts — also called malicious intrusion attempts — we

of 2021 had over 2 billion more malicious intrusion attempts

find much better news. In 2021, the volume of these attacks

than the second half, a much more positive trend we hope

fell by 28% year over year.

will persist into 2022.

)
s
n
o
i
l
l
i
r
T
n
I
(
s
n
o
i
s
u
r
t
n

I

5

4

3

2

1

0

Global Intrusion Attempts

+3,220%

1.06
2013

1.68
2014

2.17
2015

2.83
2016

3.05
2017

3.91
2018

3.99
2019

4.77
2020

5.28
2021

www.sonicwall.com

47     |     2022 SonicWall Cyber Threat Report     |     Intrusion Attempts

What is an
Intrusion Attempt?

A malicious intrusion attempt is a security event in which

Exploitation of vulnerabilities does not stop once the

an intruder, hacker, cybercriminal or threat actor attempts

attackers get inside the network. Instead, that’s when they

to gain access to a system or resource by exploiting a

pick up the pace: Attackers will gain lateral movement

vulnerability without authorization. These vulnerabilities

and network persistence by exploiting other, internal

are typically public and published as CVEs, discussed in

vulnerabilities in unpatched systems and software once

a previous section. While the vulnerability is public, not

inside the network.

everyone patches at the same rate, and attacks take

advantage of unpatched appliances or software that can

be used as an entry into a network. (A more serious and

dangerous scenario is when a vulnerability is not yet well

publicized or has not yet been published — these are the

dreaded zero-day vulnerabilities.)

What SonicWall records is detection and prevention

of vulnerabilities — coming both from external and

internal sources. When a piece of code that constitutes

a vulnerability passes a firewall with Intrusion Prevention

enabled, and the firewall detects and neutralizes that code,

an intrusion attempt is counted.

As noted, low-severity intrusions are typically benign.

48     |     2022 SonicWall Cyber Threat Report     |      Intrusion Attempts

Malicious Intrusions by Type
There’s been a lot of movement in the different sorts of

Malicious Intrusions by Region
When malicious intrusion attempts dropped, they dropped

intrusion attempts over the past few years. In 2019, Remote

across the board. But there was a wide variety in the amount

Code Executions, or RCEs, were the top form of malicious

of decrease. Europe showed the greatest drop, with attempts

intrusions, but that shifted to Directory Traversal in 2020. In

falling 50% year over year. In Asia, attempts fell by 17%, and

2021, Remote File Access attempts moved to the top.

in North America — where more than half of 2021’s intrusion

attempts occurred — attempts fell by only 2%.

49     |     2022 SonicWall Cyber Threat Report     |      Intrusion Attempts

Top Intrusion Attacks

Remote File Access
Remote file access refers to an unauthorized individual

SQL Injection
SQL injections occur when malicious SQL statements

gaining access to a file meant to be accessed by authorized

are injected into vulnerable applications or websites.

individuals only.

Directory Traversal
Also known as a path traversal attack, a directory traversal

attack is an exploit that aims to access files and directories

that are not located under the “working” directory. This

is done by manipulating file variables, so that characters

representing “traverse to parent directory” are passed

This allows attackers to manipulate backend databases

and retrieve or alter database information that was not

meant to be accessible, in some cases giving the attacker

complete control over your database. Since databases can

also control access (i.e., user names and passwords), SQL

injection attacks can lead to credential theft, which can then

lead to unauthorized access.

through to the operating system’s file system API. This allows

attackers to obtain sensitive files not intended to be seen

Malformed HTTP Traffic
Malformed HTTP traffic consists of patterns not seen in

outside the appliance or software.

legitimate HTTP requests or responses — for example,

oversized HTTP headers.

Cross-Site Scripting (XSS)
XSS attacks are client-side code injection attacks that insert

malicious code, most commonly JavaScript, into the script

Client-Application Attack
Client-application attacks occur when attackers target client

of legitimate applications or websites. When a user visits

applications directly — for example, memory leaks.

these hacked pages or apps, the malicious code is executed,

sending the malicious script to the victim’s browser, with the

ultimate goal of stealing the victim’s information.

Remote Code Execution (RCE)
An RCE attack takes place when a cybercriminal uses

Denial of Service
A denial-of-service (DOS) attack, or sometimes a distributed

denial-of-service (DDoS) attack, is an attempt to make an

online service unavailable by overwhelming it with heavy

amounts of traffic, making it impossible for legitimate users

a vulnerability to remotely run malicious programming

to access the site or service. In the DDoS scenario, which is

code, usually in an unexpected path and with system-level

more common, the traffic is launched from multiple sources

privileges. The Bluekeep vulnerability is an example of

to avoid easy detection and prevention. In many cases,

this. These vulnerabilities are among the most dangerous

especially with DDoS attacks, large malicious botnets are

on software systems and are frequently used to

often leveraged to flood a target site, system or application

spread ransomware.

until it is inaccessible or inoperable. Mirai was one of the

most famous DDoS attacks, which targeted many global DNS

services and brought much of the internet down in late 2016.

50     |     2022 SonicWall Cyber Threat Report     |      Intrusion Attempts

Capture ATP
& RTDMI

RTDMI Gets Smarter,
Faster, Better

2021 was another banner year for SonicWall’s patented

Real-Time Deep Memory Inspection™ (RTDMI) technology.

A total of 442,151 total never-before-seen malware variants

was identified in 2021, a 65% increase over 2020’s count and

an average of 1,211 per day.

When RTDMI was added to SonicWall’s existing Capture

Advanced Threat Protection, it began identifying a large

number of never-before-seen malware variants almost

immediately. RTDMI is capable of finding malware that

relies on various anti-evasion techniques — frequently

variants of existing malware that have been obfuscated,

repacked or recompiled in such a way as to evade all existing

industry detections.

What Is RTDMI?

Introduced in early 2018, SonicWall’s patented

Real-Time Deep Memory Inspection™ engine detects

and blocks malware that doesn’t exhibit malicious

behavior and hides its weaponry via encryption.

Each year, RTDMI leverages proprietary memory

inspection, CPU instruction tracking and machine

learning capabilities to become smarter, more agile

and more efficient at recognizing and mitigating

cyberattacks never before seen by anyone in the

cybersecurity industry.

51     |     2022 SonicWall Cyber Threat Report     |      Capture ATP & RTDMI

This growth has produced a number of new milestones.

effectively solutions detect these unknown and little-known

In October 2021, the monthly total of never-before-seen

threats while minimizing false positives.

variants reached 50,418, surpassing the 50,000 mark for

the first time ever. This feat would be repeated the very next

month, when the total for November reached 51,633.

In 14 of the last 16 quarters, the number of new malware

variants has exceeded that found in the previous quarter. A

total of 141,390 never-before-seen malware variants were

recorded in Q4 2021 — more than any quarter on record.

QTR

It’s rare enough for any vendor to score 100% with no false

positives. No vendor had ever earned this score twice in a

row — let alone four times in a row.

2021 ICSA ATD Testing Cycles

MALICIOUS
SAMPLES
DETECTED

BENIGN
SAMPLES
DETECTED

MALICIOUS
DETECTION
RATE

FALSE
POSITIVE
RATE

This growth indicates that the creation of new variants for

existing malware — ones able to bypass detection by a

majority of the industry tools on the market — is becoming

increasingly accessible and more frequently utilized. This

is a worrisome development: If any one of these attacks

gets past an organization’s defenses, it can result in a

ransomware infection.

A Year of 100% Detection — And
(Still) No False Positives
While our internal data is a testament to the power of RTDMI,

its capabilities have also been proven by third-party testing

— not just once, but four times in a row.

Q1

Q2

Q3

Q4

580/580

0/891

544/544

653/653

801/801

0/600

0/695

0/824

100%

100%

100%

100%

0%

0%

0%

0%

“Armed with more than a decade of machine-learning

experience, RTDMI plays an essential role in quickly

identifying destructive malware strands not detected by

traditional sandboxing technology,” said SonicWall SVP and

Chief Technology Officer John Gmuender. “As cyberattacks

continue to strengthen and escalate, so must technology

ICSA Labs Advanced Threat Defense (ATD) testing evaluates

and the creative thinking of researchers who work around

vendor solutions designed to identify new threats that other

the clock to ensure that organizations in all industries can

traditional security products do not detect, and focus on how

advance their reliance on the digital and connected world.”

“Zero-Day” vs.
“Never-Before-Seen” Attacks

The “zero-day attack” is among the most well-known

Conversely, SonicWall tracks detection and mitigation of

cybersecurity terms due to its connection to high-profile

“never before seen attacks”, which are the first time SonicWall

breaches. These attacks are completely new and unknown

Capture ATP identifies a signature/SHA256 as malicious.

threats that target a zero-day vulnerability without any

These discoveries often closely align with zero-day attack

existing protections (such as patches, updates, etc.) from the

patterns due to the volume of attacks analyzed by SonicWall.

target vendor or company.

52     |     2022 SonicWall Cyber Threat Report     |     Capture ATP & RTDMI

Malicious PDF/
Office Files

Malicious Office and PDF Files Reverse Course

In 2021, SonicWall Capture Labs threat researchers recorded

a 52% year-over-year increase in the overall use of malicious

PDFs, while use of malicious Microsoft Office files fell 64%.

This represents a significant reversal from a year ago. In

2020, SonicWall Capture Labs threat researchers noted

that cybercriminal groups were shifting from PDFs to Office

files in their 2021 malware campaigns, driving last year’s

percentage of malicious PDF files down 22%, and catapulting

the percentage of malicious Office files up 67%.

But it’s important not to conflate the percentage increase

with the percentage of total files. For instance, the number

of malicious PDFs detected showed double-digit growth, but

since PDFs only represented 9.2% of all malicious files last

year, the percentage of total malicious files that were PDFs

was still pretty small in 2021.

SonicWall Capture Labs
threat researchers noted
that cybercriminal groups
were shifting from PDFs
to Office files in their 2021
malware campaigns.

2021 New Malicious File Type Detections | Capture ATP

Other 3.72%

PDF 14.20%

Scripts 24.26%

+3,220%

Archive 19.07%

Executables 30.27%

Oﬃce 8.48%

53     |     2022 SonicWall Cyber Threat Report     |     Malicious PDF/Office Files

www.sonicwall.com

Office files, on the other hand, were a quarter of all malicious

files identified, but this year represent less than 1 in 10. .Exe

files picked up most of the slack, doubling from just over 15%

to roughly 30%.

Beware Muscle Memory
With cloud platforms overtaking programs installed on

devices, and with two-factor authentication (2FA) becoming

the norm among companies looking to harden their security

posture, the average user now enters their login credentials

several times a day. While it’s tempting to let muscle memory

take over and get through the process as quickly as possible,

doing so may open you up to credential theft.

A majority of the HTML phishing
emails observed in 2021 were
designed to launch a login
form, which is prefilled with
a user’s email address.

Once the user enters their password, it’s sent to the

malware-hosted remote server and the user is redirected to

In 2021, SonicWall identified several phishing campaigns

some legitimate website.

designed to trick busy or distracted employees.

This trend of using “authentication fatigue” to harvest

A majority of the HTML phishing emails observed in 2021

credentials has also been observed in phishing campaigns

were designed to launch a login form, which is prefilled

using PDF files. While most attempt to steal Microsoft Office

with a user’s email address. All you have to do is enter your

credentials, researchers encountered files attempting

password —cybercriminals are counting on well-practiced

to steal Dropbox, Amazon, DHL, Google Drive and Adobe

users to do this in about two seconds, not long enough to

credentials as well.

notice that anything might be amiss.

The embedded JavaScript on the left displays the legitimate-looking login form on the right.

54     |     2022 SonicWall Cyber Threat Report     |     Malicious PDF/Office Files

 In this case, the iframe asks for the user’s password, with the word “invoice” visible to boost legitimacy and increase urgency.

In this highly targeted example, the PDF is designed to imitate a Dubai Electricity and Water Authority bill. The image is blurred, but there
is a link reading “View your bill” that, when clicked on, leads to a phony Adobe login page.

55     |     2022 SonicWall Cyber Threat Report     |     Malicious PDF/Office Files

Filenames to Look Out For in 2022
The trend of borrowed legitimacy continued to the

filenames used in these campaigns. Because most people

know enough to look at a filename before opening it —

and because virtually no one is going to open a file with a

name like “InfoStealer.xlsm” or “malware.exe” — phishing

groups name their malicious files to maximize both

gravitas and urgency.

But while you’re highly likely to receive a malicious file called

“Document,” the odds of it actually being a document (as in, a

Microsoft Word file) are only about 1 in 12. The vast majority

of malicious Office files are Excel spreadsheets, with .xlsm

being the most common extension.

2021’s Top 10 Malicious Office File Names:

FILENAME BEGINS WITH

SHARE OF MALICIOUS FILES

Document

Rebate

Complaint

Debt

Permission

Compensatio72021.xlsm

Cancellatio242021.xls

Overdue

Outstanding42021.xlsm

Claim

33.84%

6.82%

5.52%

4.48%

2.43%

2.26%

1.90%

1.76%

1.70%

1.62%

Who is Rabota?

Along with the trends and volume associated with malicious Microsoft Office files,

SonicWall also tracks various other attributes of these files. In 2021, researchers

noted that there was a roughly 50% chance that, if you came across a malicious

Office file, it would have “Rabota” listed as the author.

While this sounds like it could be someone’s name, there isn’t actually a person

named Rabota furiously cranking out mass quantities of malicious Office files. As

it turns out, “Rabota” is the Russian word for work, or job.

While the expected “Admin,” “Test,” “Tester” and “USER” also appeared on the list

of malicious Office file authors, there was one entry on the list that was an actual

name: “Brian.” With nearly 10% of 2021’s malicious Office files credited to him,

Brian must be a busy guy.

56     |     2022 SonicWall Cyber Threat Report     |     Malicious PDF/Office Files

IoT Malware

IoT Malware Shows
Signs of Stabilizing

IoT malware continued to climb last year: SonicWall Capture

Labs threat researchers recorded 60.1 million IoT malware

hits in 2021, the highest number ever recorded by SonicWall

in a single year.

In March, researchers recorded 6.8 million instances of

IoT malware, the highest monthly total recorded all year.

This didn’t come close to beating the monthly record set

in October 2020, which saw 10.8 million hits, but higher

monthly totals of IoT malware overall resulted in a 6%

year-over-year increase.

While an increase in attacks is never good news, it’s better

than it has been. In 2019 and 2020, IoT malware volume

Higher monthly totals of IoT
malware overall resulted in a
6% year-over-year increase.

rose 218% and 66% respectively. With no corresponding

slowdown in the proliferation of connected devices, this

suggests attack volumes may be leveling off.

Global IoT Malware Volume

e
m
u
l
o
V

10M

8M

6M

4M

2M

0

,

3
8
8
4
3
7
3

,

,

0
1
3
6
8
2
6

,

,

4
0
4
1
4
8
3

,

,

6
5
5
9
7
6
5

,

,

7
6
2
2
3
0
4

,

,

8
7
5
9
1
8
6

,

,

9
2
6
7
6
0
2

,

,

2
3
7
3
2
5
4

,

,

9
9
2
3
7
4
3

,

,

6
0
4
9
0
8
4

,

,

1
0
7
8
2
0
3

,

,

1
3
6
4
4
0
4

,

,

1
8
9
9
2
5
2

,

,

1
1
9
9
9
7
3

,

,

8
8
7
8
7
8
2

,

,

3
6
6
9
1
2
3

,

,

3
7
0
4
2
8
6

,

,

2
0
2
4
6
7
3

,

,

1
4
1
8
2
8
0
1

,

,

2
1
6
6
2
9
5

,

,

3
5
3
6
6
4
7

,

,

8
0
4
0
1
4
5

,

,

9
1
5
1
4
2
6

,

,

8
3
9
3
5
8
5

,

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

2020

2021

www.sonicwall.com

57     |     2022 SonicWall Cyber Threat Report     |     IoT Malware

IoT Malware by Region
The 6% global increase represented the confluence of

several disparate trends. In North America, attacks rose by a

moderate 19%. In Europe, IoT malware trended the other way,

with researchers observing a 10% decrease year over year.

Asia bore the brunt of the increase. IoT malware there

increased 92% year over year, continuing the upward trend

observed in 2020, when IoT malware increased by 18%.

More than a third of the
world’s IoT attacks occurred
in the United States.

U.S. ended on an upward spike suggests that IoT malware

More than a third of the world’s IoT attacks occurred in the

there might make up an even larger percentage of the

United States. In 2021, the U.S. saw 21.8 million IoT malware

global total in 2022.

hits, a 6% year-over-year increase.

IoT malware volume in the U.K. trended in the opposite

While this mirrors the global increase, the trends in the

direction. IoT malware in the U.K. currently makes up only

U.S. looked much different. Globally, IoT malware peaked in

3.6% of the global total, but if this trend continues, we expect

Q1, but in the U.S., it didn’t peak until Q4. The fact that the

to see this percentage fall over the next year.

IoT Malware Volume | United States

e
m
u
l
o
V

5M

4M

3M

2M

1M

0

,

5
4
7
7
5
0
1

,

,

2
3
3
6
9
2
1

,

,

8
3
2
4
5
3
1

,

,

1
2
2
5
8
1
1

,

,

0
8
5
2
9
6
1

,

,

8
6
3
6
0
7
1

,

0
8
8
0
6
8

,

,

1
4
6
7
8
7
1

,

,

3
5
9
2
8
7
1

,

,

6
0
0
2
6
7
1

,

,

9
5
3
8
0
4
1

,

,

4
0
5
0
7
6
1

,

,

8
2
6
9
8
1
1

,

,

2
5
4
6
2
6
1

,

,

0
1
1
1
3
6
1

,

6
1
5
0
7
9

,

,

2
0
0
1
8
6
2

,

,

2
6
2
0
7
7
1

,

,

3
2
1
4
6
1
4

,

,

7
2
0
8
0
5
2

,

,

2
8
2
5
0
1
2

,

,

9
1
4
8
9
1
2

,

,

3
2
5
4
6
3
1

,

,

3
0
3
3
9
6
2

,

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

2020

2021

www.sonicwall.com

58     |     2022 SonicWall Cyber Threat Report     |      IoT Malware

IoT Malware by Industry

SonicWall Capture Labs threat researchers observed

may be the way IoT devices are networked. Due to the

increases in IoT malware across all industries studied.

life-and-death nature of many healthcare IoT devices,

The largest jumps were in healthcare, which saw a 71%

healthcare facilities tend to keep these devices on their own

year-over-year increase, and government, where IoT

separate and highly secured network, largely inaccessible

malware increased 46%. The increase for education and

by other devices.

retail was (comparatively) more modest: Both saw IoT

malware rise 28%.

Although education saw one of the smallest decreases,

that probably wasn’t much comfort to the average 10.5%

of education customers targeted each month. But there

was one upside: while each industry saw the percentage

of customers targeted decrease throughout the year,

education saw the biggest drop.

One interesting thing to note: For most attack types, the

industry with the lowest percentage of customers targeted is

retail. But for IoT malware, it’s healthcare. One reason for this

The largest jumps were in
healthcare, which saw a 71%
year-over-year increase,
and government, where IoT
malware increased 46%.

% of Customers Targeted by IoT Malware in 2021

15

14

13

12

11

10

9

8

7

6

5

4

d
e
t
e
g
r
a
T
%

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Overall

Government

Education

Healthcare

Retail

www.sonicwall.com

59     |     2022 SonicWall Cyber Threat Report     |      IoT Malware

9,655,141

4,768,778

3,075,947

2,134,425

1,663,073

1,012,884

693,319

478,233

440,917

319,804

277,084

275,016

273,605

209,607

Protecting the
Internet of Things

The number of IoT devices coming

onto the market continues to grow.

According to IDC, the number of these

devices is projected to grow to 55.7

billion by 2025 — together, these

devices will produce an estimated

73.1 ZB of data.

Even as new and more powerful IoT

devices continue to hit the market,

however, the most frequently attacked

TOP 15 IoT SIGNATURES

 HITS

NETGEAR DGN Devices Remote Command Execution 2

26,951,931

D-Link HNAP Request Buffer Overflow

NETGEAR DGN Devices Remote Command Execution

Dasan GPON Routers Command Injection

Vacron NVR Remote Command Execution

D-Link DIR-806 Devices Command Injection

ZyXEL Products Command Execution

devices in 2021 were still routers,

Hikvision IP Cameras Authentication Bypass

followed by cameras/NVRs. As of

December 2021, SonicWall has 269

signatures protecting more than 96 IoT

Hikvision IP Camera Command Injection

D-Link DNS-320 system_mgr.cgi Command Injection

devices from various threats.

D-Link Products Remote Code Execution

D-Link DIR-806 Devices Command Injection Vulnerability

F5 BIG-IP iControl REST Remote Command Execution 2

D-Link DIR-645 Authentication Bypass

F5 BIG-IP iControl REST Authentication Bypass

60     |     2022 SonicWall Cyber Threat Report     |      IoT Malware

Safeguarding by Statute
Safeguarding by Statute

As IoT malware attack volume continues to rise,
As IoT malware attack volume continues to rise,

governments around the world got serious about ensuring
governments around the world got serious about ensuring

the safety of these devices in 2021.
the safety of these devices in 2021.

The European Union
The European Union
Introduced in October, an amendment to the EU’s 2014
Introduced in October, an amendment to the EU’s 2014 Radio

Radio Equipment Directive would ensure that all wireless
Equipment Directive would ensure that all wireless devices

are sufficiently safe before being sold, require manufacturers
manufacturers to follow new cybersecurity safeguards when

to follow new cybersecurity safeguards when designing

designing and producing products, and mandate increased
and producing products, and mandate increased protection

protection for personal data.

for personal data.

Australia
Australia
Due to a lack of response from manufacturers of
Due to a lack of response from manufacturers of

lower-cost goods, the Australian government announced
lower-cost goods, the Australian government announced
it is considering making mandatory a suite of voluntary
it is considering making mandatory a suite of voluntary

regulations introduced last September. These regulations

regulations introduced in September 2020. These

would outline a set of minimum cybersecurity requirements

regulations would outline a set of minimum cybersecurity

for consumer-grade smart devices; the Australian
requirements for consumer-grade smart devices. The

Australian government accepted submissions on the

these requirements through Aug. 27 and the crafting of this

specifics of these requirements through Aug. 27 and the

legislation is ongoing.

crafting of this legislation is ongoing.

U.S.
U.S.
In late March, legislation known as the Cyber Shield Act
In late March, legislation known as the Cyber Shield Act
was reintroduced in Congress. If passed, the law would
was reintroduced in Congress. If passed, the law would
create security standards for IoT devices based on
create security standards for IoT devices based on

recommendations from an advisory committee made up of
recommendations from an advisory committee made up of
cybersecurity experts from the government, academia and
cybersecurity experts from the government, academia and

the private sector. Devices meeting these regulations would
the private sector. Devices meeting these regulations would

be allowed to label their products with a mark indicating they
be allowed to label their products with a mark indicating they
had met the standards and their products were more secure.
had met the standards and their products were more secure.

U.K.
U.K.
In November, the U.K. Department for Digital, Culture,
In November, the U.K. Department for Digital, Culture,

Media and Sport announced the Product Security and
Media and Sport announced the Product Security and
Telecommunications Infrastructure (PSTI) Bill. This

Telecommunications Infrastructure (PSTI) Bill. This legislation

legislation bans universal default passwords, requires

bans universal default passwords, requires manufacturers to
manufacturers to disclose the length of time they planned to
disclose the length of time they planned to continue offering

security updates for these devices, create a public point of
a public point of contact for reporting vulnerabilities, and
contact for reporting vulnerabilities, and requires devices

requires devices have the ability to receive software updates.

have the ability to receive software updates.

62     |     2022 SonicWall Cyber Threat Report     |

61     |     2022 SonicWall Cyber Threat Report     |      IoT Malware

Section Title

Attacks on
Non-Standard Ports

Non-Standard Port
Attacks Fall 10%

Some attack types, such as IoT attacks, seem to rise reliably

In April, 2021’s low-water mark, the percentage of

each year. Others, such as malware, trend capriciously,

non-standard port attacks fell to 9%, the lowest since

sometimes increasing for years at a time, then falling

January 2019. However, we may not see another month in

for the next several months or years before reversing

which these attacks sink below 10%. While the cadence of

course once again.

Non-standard port attacks follow neither of these patterns.

Since SonicWall began tracking non-standard port attacks in

2018, they’ve followed a consistent, pendulum-like pattern,

rising in even-numbered years, and falling in odd.

In 2021, the pendulum swung back, bringing with it a 10%

decrease in non-standard port attacks and wiping out most —

but not all — of the gain that occurred between 2019 and 2020.

non-standard port attacks follows a predictable rise-and-fall

pattern, we’ve seen both the crests and the troughs of these

attacks trend higher over time.

If this continues to hold true, there’s a good chance the 2023

SonicWall Cyber Threat Report will feature non-standard

port attacks breaking the 30% mark.

2020-21 Global Malware Attacks

100%

80%

60%

40%

20%

78%

75%

77%

77%

79%

87%

84%

86%

0%

22%
Q1 2020

25%
Q2 2020

23%
Q3 2020

23%
Q4 2020

21%
Q1 2021

13%
Q2 2021

16%
Q3 2021

14%
Q4 2021

Non-Standard Ports

Standard Ports

www.sonicwall.com

62     |     2022 SonicWall Cyber Threat Report     |      Attacks on Non-Standard Ports

What is a Non-Standard Port Attack?
In networking, a port helps complete the destination or

origination network address of a message. About 40,000

ports are registered; however, only a small number — the

“standard” ports — are typically used. For example, HTTP

uses port 80, HTTPS uses port 443 and SMTP uses port 25.

Services using a port that isn’t the one assigned to them by

default, usually as defined by the IANA port numbers registry,

are using a non-standard port.

With so many ports to monitor,
these legacy firewalls
can’t mitigate attacks over
non-standard ports.

There’s nothing inherently wrong with using non-standard

non-standard ports to increase the odds their payloads can

ports. But traditional proxy-based firewalls typically

be deployed undetected.

focus their protection on traffic passing through the

standard ports.

Modern firewalls that are capable of analyzing specific

artifacts (as opposed to all traffic) can detect these attacks,

With so many ports to monitor, these legacy

making this an increasingly important criteria to look for

firewalls can’t mitigate attacks over non-standard

in a security solution as non-standard ports trend (ever

ports. Cybercriminals know this, and target

zig-zaggedly) upward.

63     |     2022 SonicWall Cyber Threat Report     |      Attacks on Non-Standard Ports

Conclusion

Proactive Defense is the
Future of Cybersecurity

Cybercrime has evolved, making it harder for defenders to protect

against, detect and stop attacks from entering their networks. As the

pace of attacks continues to increase, and the ways attackers breach

and infiltrate systems continue to become more targeted and evasive,

the future will increasingly belong to the proactive.

Proactive organizations have a thorough understanding of both their

network and the threat landscape, allowing them to adapt and shift

just as agilely as cybercriminals. This enables them to quickly detect

and stop attacks.

Dark Reading, in partnership with SonicWall,

offers an in-depth discussion on how you can ensure business continuity, protect

your employees and customers, and help you maintain compliance with a proactive

cybersecurity strategy.

This webinar covers the importance of:

•  Having a complete picture of where data lives and how it moves

•  Knowing what third parties may be storing data, including cloud vendors, and how they approach

security, including their incident response plan

•  Employing threat hunting to detect threats that evade existing security controls

•  Deploying endpoint protection to look for indicators of compromise and protect the system when

potential threats are identified

•  Patching vulnerabilities

•  And more

WATCH THE WEBINAR

64     |     2022 SonicWall Cyber Threat Report     |     Conclusion

About the SonicWall Capture
Labs Threat Network

Intelligence for the 2022 SonicWall Cyber Threat Report

was sourced from real-world data gathered by the SonicWall

Capture Threat Network, which securely monitors and

collects information from global devices including:

•  More than 1.1 million security sensors in over 215

countries and territories

•  Cross-vector, threat related information shared among

SonicWall security systems, including firewalls, email

security devices, endpoint security solutions, honeypots,

content filtering systems and the SonicWall Capture

Advanced Threat Protection (ATP) multi-engine sandbox

•  SonicWall internal malware analysis

automation framework

•  Malware and IP reputation data from tens of thousands of

firewalls and email security devices around the globe

Global Sensors

Countries & Territories

•  Shared threat intelligence from more than 50 industry

collaboration groups and research organizations

Monitoring

•  Analysis from freelance security researchers

Threat Response

Malware Samples Collected Daily

Malware Attacks Blocked Daily

65     |     2022 SonicWall Cyber Threat Report     |     About the SonicWall Capture Labs Threat Network

SonicWall Inc.
1033 McCarthy Boulevard
Milpitas, CA 95035

Refer to our website for additional information.
www.sonicwall.com

© 2022 SonicWall Inc.

SonicWall is a trademark or registered trademark of SonicWall Inc. and/or its affiliates in the U.S.A. and/or other
countries. All other trademarks and registered trademarks are property of their respective owners. The information
in this document is provided in connection with SonicWall Inc. and/or its affiliates’ products. No license, express or
implied, by estoppel or otherwise, to any intellectual property right is granted by this document or in connection with
the sale of SonicWall products.

EXCEPT AS SET FORTH IN THE TERMS AND CONDITIONS AS SPECIFIED IN THE LICENSE AGREEMENT FOR THIS
PRODUCT, SONICWALL AND/OR ITS AFFILIATES ASSUME NO LIABILITY WHATSOEVER AND DISCLAIMS ANY EXPRESS,
IMPLIED OR STATUTORY WARRANTY RELATING TO ITS PRODUCTS INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON- INFRINGEMENT. IN NO EVENT
SHALL SONICWALL AND/ OR ITS AFFILIATES BE LIABLE FOR ANY DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE,
SPECIAL OR INCIDENTAL DAMAGES (INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS OF PROFITS, BUSINESS
INTERRUPTION OR LOSS OF INFORMATION)

ARISING OUT OF THE USE OR INABILITY TO USE THIS DOCUMENT, EVEN IF SONICWALL AND/OR ITS AFFILIATES HAVE
BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

SonicWall and/or its affiliates make no representations or warranties with respect to the accuracy or completeness
of the contents of this document and reserves the right to make changes to specifications and product descriptions
at any time without notice. SonicWall Inc. and/or its affiliates do not make any commitment to update the information
contained in this document.

As a best practice, SonicWall routinely optimizes its methodologies for data collection, analysis and reporting. This
includes improvements to data cleansing, changes in data sources and consolidation of threat feeds. Figures published
in previous reports may have been adjusted across different time periods, regions or industries.

The materials and information contained in this document, including, but not limited to, the text, graphics, photographs,
artwork, icons, images, logos, downloads, data and compilations, belong to SonicWall or the original creator and is
protected by applicable law, including, but not limited to, United States and international copyright law and regulations.

About SonicWall
SonicWall delivers Boundless Cybersecurity for the hyper-distributed era in a work reality where everyone is remote, mobile

and unsecure. SonicWall safeguards organizations mobilizing for their new business normal with seamless protection that

stops the most evasive cyberattacks across boundless exposure points and increasingly remote, mobile and cloud-enabled

workforces. By knowing the unknown, providing real-time visibility and enabling breakthrough economics, SonicWall closes the

cybersecurity business gap for enterprises, governments and SMBs worldwide. For more information,

visit www.sonicwall.com or follow us on Twitter, LinkedIn, Facebook and Instagram.

SonicWall, Inc.
1033 McCarthy Boulevard  |  Milpitas, CA 95035

As a best practice, SonicWall routinely optimizes its methodologies for data collection, analysis and reporting. This includes improvements to data cleansing, changes in data sources and
consolidation of threat feeds. Figures published in previous reports may have been adjusted across different time periods, regions or industries.

2022-ThreatReport-COG-5746