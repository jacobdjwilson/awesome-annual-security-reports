# Threat Report H1 2025

## Table of Contents
- [Foreword](#foreword)
- [Threat landscape trends](#threat-landscape-trends)
- [ClickFix: Fake errors, real threats](#clickfix-fake-errors-real-threats)
- [Double trouble befalls prominent infostealers](#double-trouble-befalls-prominent-infostealers)
- [SnakeStealer slithers to the top](#snakestealer-slithers-to-the-top)
- [Kaleidoscope and its evil twin scheme flood Android with ads](#kaleidoscope-and-its-evil-twin-scheme-flood-android-with-ads)
- [The evolution of NFC fraud: From NGate to GhostTap to relay scams](#the-evolution-of-nfc-fraud-from-ngate-to-ghosttap-to-relay-scams)
- [Get your popcorn: it’s time for ransomware deathmatch](#get-your-popcorn-its-time-for-ransomware-deathmatch)
- [Threat telemetry](#threat-telemetry)
- [Research publications](#research-publications)
- [About this report](#about-this-report)
- [About ESET](#about-eset)

---

## Foreword

Welcome to the H1 2025 issue of the ESET Threat Report! From novel social engineering techniques to sophisticated mobile threats and major infostealer disruptions, the threat landscape in the first half of 2025 was anything but boring.

One of the most striking developments this period was the emergence of ClickFix, a new, deceptive attack vector that skyrocketed by over 500% compared to H2 2024 in ESET telemetry. Now the second most common attack vector after phishing, ClickFix manipulates internet users into executing malicious commands under the guise of fixing a fake error. The payloads at the end of ClickFix attacks vary widely – from infostealers to ransomware and even to nation-state malware – making this a versatile and formidable threat across Windows, Linux, and macOS.

The infostealer landscape also saw significant shifts. With Agent Tesla fading into obsolescence, SnakeStealer (also known as Snake Keylogger) surged ahead, becoming the most detected infostealer in our telemetry. Meanwhile, ESET contributed to major disruption operations targeting Lumma Stealer and Danabot, two prolific malware-as-a-service threats.

On the Android front, adware detections soared by 160%, driven largely by a sophisticated new threat dubbed Kaleidoscope. This malware uses a deceptive “evil twin” strategy to distribute malicious apps that bombard users with intrusive ads, degrading device performance. At the same time, NFC-based fraud shot up more than thirty-five-fold, fueled by phishing campaigns and inventive relay techniques. While the overall numbers remain modest, this jump highlights the rapid evolution of the criminals’ methods and their continued focus on exploiting NFC technology. Each new iteration of NFC threats – from NGate to GhostTap, and most recently SuperCard – demonstrates how attackers adapt to new security measures.

The ransomware scene descended (even further) into chaos, with fights between rival ransomware gangs impacting several players including the top ransomware as a service – RansomHub. Yearly data shows that while ransomware attacks and the number of active gangs have grown, ransom payments saw a significant drop. This discrepancy may be the result of takedowns and exit scams that reshuffled the ransomware scene in 2024, but also partially due to diminished confidence in the gangs’ ability to keep their side of the bargain.

I wish you an insightful read.

**Jiří Kropáč**
ESET Director of Threat Prevention Labs

---

## Threat landscape trends

### ClickFix: Fake errors, real threats

A novel social engineering technique called ClickFix is taking the threat landscape by storm, becoming the second most prevalent attack vector after phishing.

![Fake reCAPTCHA check instructing the victim to paste and execute a malicious command on their device]

While virtually nonexistent a year ago, ESET’s detection for ClickFix, HTML/FakeCaptcha, grew by 517% between H2 2024 and H1 2025. This makes it one of the fastest rising threats, accounting for nearly 8% of all blocked attacks and placing it second in our top 10.

ClickFix is a new type of social engineering that uses a fake error or verification message to manipulate victims into copying and pasting a malicious script and then running it. The list of threats that ClickFix leads to is growing by the day, currently including infostealers, ransomware, remote access trojans, cryptominers, post-exploitation tools, and even custom malware from nation-state-aligned threat actors.

#### Expert Comment
> Looking at ESET telemetry data, ClickFix has quickly become one of the most prominent cybercriminal intrusion vectors. What makes this new social engineering technique effective is that it is simple enough for the victim to follow the instructions, believable enough to look like it might fix a made-up problem, and abuses the probability that victims won’t pay much attention to the exact commands they have been asked to paste and execute on their device. It is also a good example of how threat actors quickly adopt new techniques, once they prove to yield results. With its growing popularity, it is possible that Microsoft and Apple, but also the open-source community, will add some kind of security warning like the one used for macros in Word or Excel, or for files copied from the internet, notifying users that they are about to execute a potentially dangerous script.
>
> **Dušan Lacika, ESET Senior Detection Engineer**

![Simplified ClickFix attack flow]

---

## Double trouble befalls prominent infostealers

ESET participated in disruption operations aimed at two notable infostealers: Lumma Stealer and Danabot.

In May 2025, ESET, alongside Microsoft, BitSight, Lumen, Cloudflare, CleanDNS, and GMO Registry, took part in a coordinated global effort to disrupt Lumma Stealer. The operation targeted all known Lumma Stealer C&C servers from the past year, taking out a large part of the malware’s exfiltration network.

Just a couple of days after Lumma Stealer’s disruption, the notorious infostealer Danabot also got its comeuppance, having been targeted by the FBI and US DoD’s Defense Criminal Investigative Service (DCIS), in conjunction with Operation Endgame coordinated by Europol and Eurojust.

#### Expert Comment
> We can certainly call the Lumma Stealer disruption a success. The malware suffered a considerable technical blow, taking it out of commission for some time after the operation occurred. While we now see that the threat actors have started rebuilding Lumma Stealer infrastructure using DNS servers located in Russia, the reputation of this cybercriminal endeavor has undoubtedly taken a hit. The ongoing success of Lumma Stealer is very much reliant on the trust of its affiliates. This means that even if Lumma Stealer were to succeed in the rebuilding effort, its user base might just straight up abandon it for another infostealer. In that case, the most likely path for the malware’s operators would be to completely rebrand their service.
>
> **Jakub Tomanek, ESET Malware Analyst**

---

## SnakeStealer slithers to the top

In the wake of Agent Tesla’s creators abandoning their malware, SnakeStealer claims its place as the most-detected infostealer in ESET telemetry data.

SnakeStealer, also known as Snake Keylogger or 404 Keylogger, is .NET malware that first appeared in 2019. Sold via a Telegram group, this infostealer is capable of logging keystrokes, stealing saved credentials, capturing screenshots, and collecting clipboard data.

#### Expert Comment
> While it is certainly possible that SnakeStealer will replace Agent Tesla as the dominant infostealer, we have to keep in mind that the competition is fierce and there are various other prevalent infostealers offered on the market. One such example is the Pure Logs infostealer, which has also been rising in prominence since Agent Tesla stopped updating. On the other hand, we cannot discount the power of word of mouth, since we have noticed multiple individuals on the dark web recommending SnakeStealer as an alternative to Agent Tesla. By itself, however, there is not much else that makes SnakeStealer stand out in the sea of its competitors.
>
> **Jakub Kaloč, ESET Malware Analyst**

---

## Kaleidoscope and its evil twin scheme flood Android with ads

Android adware detections jump by 160%, fueled by new evil twin fraud and the rise of potentially unwanted apps.

A sophisticated new Android threat dubbed Kaleidoscope is flooding devices with intrusive ads through a deceptive evil twin app scheme. Cybercriminals behind this operation create two nearly identical versions of the same app – a harmless one available on official app stores (decoy twin) and a malicious version distributed through third-party app stores (evil twin).

![Tapping the decoy twin app icon launches the Birds on a Wire game (top); tapping the white evil twin icon only brings up the App Info screen (bottom)]

---

## The evolution of NFC fraud: From NGate to GhostTap to relay scams

NFC-based fraud soared more than thirty-five-fold, fueled by phishing campaigns and inventive relay techniques.

According to ESET telemetry, NFC-related scams surged more than thirty-five-fold in H1 2025 compared to H2 2024. 

- **NGate**: Relays NFC signals from the victim’s payment card through the compromised phone to attacker-controlled devices.
- **GhostTap**: Involves cybercriminals secretly using stolen card data stored in digital wallets like Google Pay and Apple Pay.
- **SuperCard X**: A new threat that exhibits significant code overlap with NGate, delivered via sophisticated social engineering attacks.

#### Expert Comment
> Each iteration of NFC fraud demonstrates how attackers adapt to new security measures. Even advanced solutions – like multifactor authentication or real-time transaction monitoring – face challenges when criminals physically relay the card data in seconds. Meanwhile, organized smishing campaigns, combined with highly polished malware interfaces, make it even harder for typical users to spot fraud.
>
> **Lukáš Štefanko, ESET Senior Malware Researcher**

---

## Get your popcorn: it’s time for ransomware deathmatch

While the number of ransomware attacks and gangs has been growing, ransomware groups are increasingly fighting each other, impacting several players including the top ransomware as a service – RansomHub.

In H1 2025, ransomware gangs are increasingly fighting each other. The DragonForce gang went on a defacement spree in March, taking down the dark web sites of BlackLock, Mamona, and the number one RaaS at that time – RansomHub.

#### Expert Comment
> While Q1 2025 displayed a massive growth in the number of reported attacks, the sudden cessation of RansomHub’s operation put a hard stop to that. When RansomHub emerged in 2024 and swayed LockBit’s and BlackCat’s affiliates, its timing and attractive conditions set it up for quick growth. Now, in contrast, the ransomware landscape is in chaos; this disruption was caused by rivals, not law enforcement. We expect that, over time, a new dominant player will arise, but also that the current infighting won’t stop any time soon.
>
> **Jakub Souček, ESET Senior Malware Researcher**

---

## Threat telemetry

*(Note: This section contains statistical data and charts representing the threat landscape as observed by ESET.)*

- **Top 10 malware detections in H1 2025**: Led by HTML/Phishing.Agent (20.5%) and HTML/FakeCaptcha (7.7%).
- **Android detections**: Android/TrojanDropper.Agent (32.5%) remains the primary threat.
- **Cryptocurrency threats**: Win/CoinMiner PUA (37.6%) dominates the category.
- **Downloaders**: MSIL/TrojanDownloader.Agent (10.8%) is the most prevalent.

---

## Research publications

- **ESET Research Podcast: Telekopye, again**: Take a peek into the murky world of cybercrime where groups of scammers who go by the nickname of 'Neanderthals’ wield the Telekopye toolkit to ensnare unsuspecting victims they call 'Mammoths'.
- **Under the cloak of UEFI Secure Boot: Introducing CVE-2024-7344**: The story of a signed UEFI application allowing a UEFI Secure Boot bypass.
- **PlushDaemon compromises supply chain of Korean VPN service**: ESET researchers have discovered a supply-chain attack.

---

## About this report

This report provides an overview of the threat landscape for the first half of 2025, based on ESET telemetry and research.

---

## About ESET

ESET is a global leader in cybersecurity, providing advanced threat detection and protection for businesses and consumers worldwide.

---

ck
against a VPN provider in South Korea by a new China-
aligned APT group we have named PlushDaemon

DeceptiveDevelopment targets freelance
developers
ESET researchers analyzed a campaign delivering malware
bundled with job interview challenges

Danabot: Analyzing a fallen empire
ESET Research shares its findings on the workings of
Danabot, an infostealer recently disrupted in a multinational
law enforcement operation

Threat Report H2 2024: Infostealer shakeup,
new attack vector for mobile, and Nomani
Big shifts in the infostealer scene, novel attack vector against
iOS and Android, and a massive surge in investment scams on
social media

Operation AkaiRyū: MirrorFace invites Europe
to Expo 2025 and revives ANEL backdoor
ESET researchers uncovered MirrorFace activity that expanded
beyond its usual focus on Japan and targeted a Central European
diplomatic institute with the ANEL backdoor

Operation FishMedley
ESET researchers detail a global espionage operation by
FishMonger, the APT group run by I-SOON

You will always remember this as the day
you finally caught FamousSparrow
ESET researchers uncover the toolset used by the
FamousSparrow APT group, including two undocumented
versions of the group’s signature backdoor, SparrowDoor

BladedFeline: Whispering in the dark
ESET researchers analyzed a cyberespionage campaign
conducted by BladedFeline, an Iran-aligned APT group with
likely ties to OilRig

Shifting the sands of RansomHub’s
EDRKillShifter
ESET researchers discover new ties between affiliates of
RansomHub and of rival gangs Medusa, BianLian, and Play

TheWizards APT group uses SLAAC spoofing
to perform adversary-in-the-middle attacks
ESET researchers analyzed Spellbinder, a lateral movement
tool used to perform adversary-in-the-middle attacks

Operation RoundPress
ESET researchers uncover a Russia-aligned espionage
operation targeting webmail servers via XSS vulnerabilities

ESET takes part in global operation to
disrupt Lumma Stealer
Our intense monitoring of tens of thousands of malicious
samples helped this global disruption operation

ESET Threat Report H2 2024
A view of the H2 2024 threat landscape as seen by ESET
telemetry and from the perspective of ESET threat detection
and research experts

ESET APT Activity Report Q4 2024–Q1 2025
An overview of the activities of selected APT groups
investigated and analyzed by ESET Research in Q4 2024 and
Q1 2025

ESET THREAT REPORTExecutive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 36

Credits

Team
Peter Stančík, Team Lead

Klára Kobáková, Managing Editor

Aryeh Goretsky

Branislav Ondrášik

Bruce P. Burrell

Hana Matušková

Nick FitzGerald

Ondrej Kubovič

Rene Holt

Zuzana Pardubská

Contributors

Dušan Lacika

Jakub Kaloč

Jakub Souček

Jakub Tomanek

Lukáš Štefanko

Tomáš Procházka

About the data
in this report

The threat statistics and trends presented in this report

This data was processed with the honest intention to

are based on global telemetry data from ESET. Unless

mitigate all known biases, in an effort to maximize the

explicitly stated otherwise, the data includes detections

value of the information provided.

regardless of the targeted platform.

Most of the charts in this report show detection trends

Further, the data excludes detections of potentially

rather than provide absolute numbers. This is because

unwanted applications, potentially unsafe applications

the data can be prone to various misinterpretations,

and adware, except where noted in the more detailed,

especially when directly compared to other telemetry

platform-specific sections and in the Cryptocurrency

data. However, absolute values or orders of magnitude

threats section.

are provided where deemed beneficial.

ESET THREAT REPORTExecutive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 37

About ESET

ESET® provides cutting-edge digital security to prevent attacks before

WeLiveSecurity.com

they happen. By combining the power of AI and human expertise, ESET

stays ahead of known and emerging cyberthreats — securing businesses,

critical infrastructure, and individuals. Whether it’s endpoint, cloud, or

@ESETresearch

ESET GitHub

ESET Threat Reports and APT Activity Reports

mobile protection, our AI-native, cloud-first solutions and services remain

highly effective and easy to use. ESET technology includes robust detection

and response, ultra-secure encryption, and multifactor authentication.

With 24/7 real-time defense and strong local support, we keep users safe

and businesses running without interruption. An ever-evolving digital

landscape demands a progressive approach to security: ESET is committed

to world-class research and powerful threat intelligence, backed by R&D

centers and a strong global partner network. For more information, visit

www.eset.com or follow us on LinkedIn, Facebook, and X.

ESET THREAT REPORT(eset):research© 2025 ESET, spol. s r.o. - All rights reserved.Trademarks used herein are trademarks or registered trademarks of ESET, spol. s r.o.All other names and brands are registered trademarks of their respective companies.