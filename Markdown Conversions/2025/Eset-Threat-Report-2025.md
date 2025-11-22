# Threat Report

H1 2025

December 2024 – May 2025

(eset):research

## Table of Contents
- [Contents](#contents)
- [Executive summary](#executive-summary)
- [Foreword](#foreword)
- [Threat landscape trends](#threat-landscape-trends)
- [Attack vectors Social engineering](#attack-vectors-social-engineering)
- [ClickFix: Fake errors, real threats](#clickfix-fake-errors-real-threats)
- [Infostealers Malware as a service](#infostealers-malware-as-a-service)
- [Double trouble befalls prominent infostealers](#double-trouble-befalls-prominent-infostealers)
- [SnakeStealer slithers to the top](#snakestealer-slithers-to-the-top)
- [Android Adware](#android-adware)
- [Kaleidoscope and its evil twin scheme flood Android with ads](#kaleidoscope-and-its-evil-twin-scheme-flood-android-with-ads)
- [Android NFC Scams](#android-nfc-scams)
- [The evolution of NFC fraud: From NGate to GhostTap to relay scams](#the-evolution-of-nfc-fraud-from-ngate-to-ghosttap-to-relay-scams)
- [Ransomware](#ransomware)
- [Get your popcorn: It’s time for ransomware deathmatch](#get-your-popcorn-its-time-for-ransomware-deathmatch)
- [Threat telemetry](#threat-telemetry)
- [All threats](#all-threats)
- [Android](#android)
- [Cryptocurrency threats](#cryptocurrency-threats)
- [Downloaders](#downloaders)
- [Email threats](#email-threats)
- [Exploits](#exploits)
- [Infostealers](#infostealers)
- [macOS](#macos)
- [Ransomware](#ransomware)
- [Web threats](#web-threats)
- [Research publications](#research-publications)
- [Credits](#credits)
- [About the data in this report](#about-the-data-in-this-report)
- [About ESET](#about-eset)

H1 2025 | 2

Contents

Foreword

Threat landscape trends

ClickFix: Fake errors, real threats

Double trouble befalls prominent infostealers

SnakeStealer slithers to the top

Kaleidoscope and its evil twin scheme flood Android with ads

The evolution of NFC fraud: From NGate to GhostTap to relay scams

Get your popcorn: it’s time for ransomware deathmatch

Threat telemetry

Research publications

About this report

About ESET

4

5

6

9

12

14

17

20

23

35

36

37

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 3

Executive summary

Attack vectors

Social engineering

ClickFix: Fake errors, real threats

Android

Adware

Kaleidoscope and its evil twin scheme flood Android with ads

A novel social engineering technique called ClickFix is taking the threat landscape by storm,
becoming the second most prevalent attack vector after phishing.

Android adware detections jump by 160%, fueled by new evil twin fraud and the rise of
potentially unwanted apps.

Infostealers

Malware as a service

Android

NFC Scams

Double trouble befalls prominent infostealers

The evolution of NFC fraud: From NGate to GhostTap to relay scams

ESET participated in disruption operations aimed at two notable infostealers: Lumma Stealer

and Danabot.

Infostealers

Malware as a service

SnakeStealer slithers to the top

In the wake of Agent Tesla’s creators abandoning their malware, SnakeStealer claims its

place as the most-detected infostealer in ESET telemetry data.

NFC-based fraud soared more than thirty-five-fold, fueled by phishing campaigns and
inventive relay techniques.

Ransomware

Get your popcorn: it’s time for ransomware deathmatch

While the number of ransomware attacks and gangs has been growing, ransomware groups
are increasingly fighting each other, impacting several players including the top ransomware
as a service – RansomHub.

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 4

Foreword

Welcome to the H1 2025 issue of the ESET Threat Report!

From novel social engineering techniques to sophisticated mobile

On the Android front, adware detections soared by 160%, driven

This discrepancy may be the result of takedowns and exit scams

threats and major infostealer disruptions, the threat landscape in

largely by a sophisticated new threat dubbed Kaleidoscope.

that reshuffled the ransomware scene in 2024, but also partially

the first half of 2025 was anything but boring.

This malware uses a deceptive “evil twin” strategy to distribute

due to diminished confidence in the gangs’ ability to keep their side

One of the most striking developments this period was the

emergence of ClickFix, a new, deceptive attack vector that

skyrocketed by over 500% compared to H2 2024 in ESET telemetry.

Now the second most common attack vector after phishing,

ClickFix manipulates internet users into executing malicious

commands under the guise of fixing a fake error. The payloads

at the end of ClickFix attacks vary widely – from infostealers to

ransomware and even to nation-state malware – making this a

versatile and formidable threat across Windows, Linux, and macOS.

The infostealer landscape also saw significant shifts. With Agent

Tesla fading into obsolescence, SnakeStealer (also known as Snake

Keylogger) surged ahead, becoming the most detected infostealer

in our telemetry. Meanwhile, ESET contributed to major disruption

operations targeting Lumma Stealer and Danabot, two prolific

malware-as-a-service threats.

malicious apps that bombard users with intrusive ads, degrading

of the bargain.

device performance. At the same time, NFC-based fraud shot

up more than thirty-five-fold, fueled by phishing campaigns and

I wish you an insightful read.

Jiří Kropáč
ESET Director of Threat Prevention Labs

inventive relay techniques. While the overall numbers remain

modest, this jump highlights the rapid evolution of the criminals’

methods and their continued focus on exploiting NFC technology.

Each new iteration of NFC threats – from NGate to GhostTap, and

most recently SuperCard – demonstrates how attackers adapt to

new security measures.

The ransomware scene descended (even further) into chaos, with

fights between rival ransomware gangs impacting several players

including the top ransomware as a service – RansomHub. Yearly

data shows that while ransomware attacks and the number of

active gangs have grown, ransom payments saw a significant drop.

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 5

Threat
landscape
trends

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 6

Attack vectors Social engineering

ClickFix: Fake errors, real threats

A novel social engineering technique called ClickFix is taking the threat landscape by storm,
becoming the second most prevalent attack vector after phishing.

Proving, online, that you are human can take on many

While virtually nonexistent a year ago, ESET’s detection

forms. At times, you may need to transcribe blurry

for ClickFix, HTML/FakeCaptcha, grew by 517% between

text into a blank field, while on other occasions you’re

H2 2024 and H1 2025. This makes it one of the fastest

asked to select all images of buses, traffic lights, or

rising threats, accounting for nearly 8% of all blocked

stairs. Every now and then a website will have you drag

attacks and placing it second in our top 10.

a puzzle piece to its correct location within an image.

As the variety of reCAPTCHA checks has grown, users

have become accustomed to the process, and few

would question encountering a new type of challenge,

such as copying and pasting something onto their

device. And that is precisely what cybercriminals have

thought, weaponizing one of the web’s most frustrating

features into a new intrusion avenue.

It is important to note that the multiple stages of the

attack, including the copied PowerShell commands or

scripts, executables, malicious “envelopes”, and final

![HTML/FakeCaptcha detection trend in H2 2024 and H1 2025, seven-day moving average]

payloads, are covered by dozens of other detection

names. Therefore, the real prevalence of this threat

is probably even higher than the HTML/FakeCaptcha

numbers. Countries reporting the highest volume of

detections in ESET telemetry are Japan (23%), Peru (6%),

ClickFix is a new type of social engineering that uses

and Poland, Spain and Slovakia (each over 5%).

a fake error or verification message to manipulate

victims into copying and pasting a malicious script and

then running it. The list of threats that ClickFix leads to

is growing by the day, currently including infostealers,

ransomware, remote access trojans, cryptominers,

post-exploitation tools, and even custom malware from

nation-state-aligned threat actors.

ClickFix emerged in March 2024, in a campaign

documented by Proofpoint, being used by ClearFake

and TA571. This campaign used phishing emails

delivering malicious HTML attachments that displayed

a page imitating Microsoft Word or OneDrive. A

pop-up shown on those pages falsely claims that an

![Fake reCAPTCHA check instructing the victim to paste and execute a malicious command on their device]

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 7

error needs to be resolved before the content can

As the number of ClickFix variants has grown,

be accessed. The victim is then instructed to click a

so have a variety of threats being delivered using

“Fix it” button – copying a PowerShell command to

this technique. Currently the list includes popular

their clipboard – open a PowerShell terminal, and

infostealers such as Lumma Stealer, VidarStealer,

then paste it there to execute the command. Instead

StealC, and Danabot; remote access trojans such

of resolving the made-up error, this starts a chain of

as VenomRAT, AsyncRAT, and NetSupport RAT;

downloading and executing other malicious scripts

remote monitoring and management tools such as

that ultimately lead to compromise by DarkGate or

MeshAgent; post-exploitation frameworks such as

Matanbuchus malware offered as a service on the

Havoc and Cobalt Strike; and cryptominers, loaders,

EXPERT COMMENT

Looking at ESET telemetry data, ClickFix has quickly become one of the most prominent

cybercriminal intrusion vectors. What makes this new social engineering technique effective

is that it is simple enough for the victim to follow the instructions, believable enough to

look like it might fix a made-up problem, and abuses the probability that victims won’t pay

much attention to the exact commands they have been asked to paste and execute on

dark web.

clipboard hijackers, and much more. In early 2025,

their device. It is also a good example of how threat actors quickly adopt new techniques,

By the end of 2024, attacks using the same social

engineering technique flooded the web. Threat actors

attacks were spotted that attempted to deploy

once they prove to yield results. With its growing popularity, it is possible that Microsoft

Interlock (formerly Rhysida) ransomware.

and Apple, but also the open-source community, will add some kind of security warning

have been creating fake websites mimicking popular

Nation-state-aligned threat actors also quickly

like the one used for macros in Word or Excel, or for files copied from the internet, notifying

services – such as Booking.com or Google Meet –

jumped on the bandwagon, incorporating this social

users that they are about to execute a potentially dangerous script.

compromising legitimate websites with fake browser

engineering technique into their toolsets for gaining

update prompts, fake Cloudflare verifications or

initial access. North Korea-aligned Kimsuky, Lazarus,

reCAPTCHA checks, and distributing links leading to

and DeceptiveDevelopment were the first, targeting

ClickFix pages via email campaigns. As reported in a

Windows, Linux, and macOS users. Other actors soon

recent ESET APT Activity Report, the North Korea-

followed, including Russia-aligned Callisto and Sednit,

aligned DeceptiveDevelopment group also used this

Iran-aligned MuddyWater, and Pakistan-aligned APT36.

social engineering tactic by creating issues in popular

GitHub repositories, proposing a “fix” that instead

delivered the group’s WeaselStore malware.

While Windows users are the largest group affected,

macOS and Linux users have also come into the

crosshairs. For macOS, public reports reveal that

Prompted by the effectiveness of the ClickFix approach,

ClickFix campaigns dropped AMOS stealer. For Linux,

threat actors have now reportedly started selling

APT36 was seen redirecting victims to a counterfeit

builders that provide other attackers with ClickFix-

CAPTCHA page that instructed them to run the

weaponized landing pages.

malicious code via the Alt+F2 shortcut that, on most

Linux distributions, opens a Run Command dialog.

Dušan Lacika, ESET Senior Detection Engineer

However, in that specific case, the compromise only led

to obfuscate or otherwise mask secondary payloads

to fetching a hidden JPEG file from the attacker’s server

(detected by ESET as Win/Kryptik or Win/GenKryptik),

and opening it in the background without causing any

recognize malicious activity in memory, and identify

damage or taking other malicious actions.

suspicious network behavior like data exfiltration.

As mentioned before, ClickFix attacks can be

intercepted by security solutions at several stages.

These include the malicious and compromised website

URLs, HTML email attachments, HTA files, JavaScript

files, PowerShell scripts, and command line programs

used to deliver the payloads. Reliable security solutions

should also block “envelopes” used by the attackers

Users should also remain vigilant whenever anyone

is offering “one-click” or “copy-and-paste” fixes to

unknown issues. In corporate environments, endpoint

detection and response (EDR) tools can flag anomalous

PowerShell usage – especially on machines that rarely

need it – and thus improve visibility into and protection

against such attacks.

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 8

![ClickFix delivery method]

encounters

User

Malicious email

Malicious website

Fake reCAPTCHA

displays

Fake error

asks user to paste
malicious code into

runs

downloads and
executes

data exﬁltration

Terminal

Malicious code

Final payload

Simplified ClickFix attack flow

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 9

Infostealers Malware as a service

Double trouble befalls prominent
infostealers

ESET participated in disruption operations aimed at to two notable infostealers:
Lumma Stealer and Danabot.

The world is full of gloomy and disturbing news

lately, so how about something positive for a change?

Months of hard work on the part of law enforcement

and cybersecurity companies, ESET included, paid

off and resulted in not one, but two prominent

infostealers disrupted by the authorities. Both Lumma

Stealer, a malware-as-a-service (MaaS) behemoth,

and Danabot, another MaaS operation of considerable

malicious influence, had their infrastructure largely

taken down in May 2025.

Here, we bring you an overview of the two

disruptions, as well as some recent data from ESET

telemetry regarding both infostealers. Our in-depth

research and reporting on these recent events can be

found in the respective Lumma Stealer and Danabot

blogposts on WeLiveSecurity.

Lumma Stealer steals no more?

Just half a year after we published the article covering

the unprecedented growth of Lumma Stealer in the

H2 2024 Threat Report, a reckoning has arrived

for this malware-as-a-service powerhouse. In May

2025, ESET, alongside Microsoft, BitSight, Lumen,

Cloudflare, CleanDNS, and GMO Registry, took part in

a coordinated global effort to disrupt Lumma Stealer.

The operation targeted all known Lumma Stealer C&C

servers from the past year, taking out a large part of

the malware’s exfiltration network. As part of the

disruption effort, ESET supplied technical analysis and

statistical information. Using our automated systems,

we also extracted essential data, such as C&C servers

and affiliate identifiers, from tens of thousands of

malware samples.

![Lumma Stealer detection trend in H1 2025, seven-day moving average]

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 10

EXPERT COMMENT

has already spread far and wide to other threats.

ESET took part in this undertaking alongside Amazon,

Therefore, this takedown operation will most likely only

CrowdStrike, Flashpoint, Google, Intel471, PayPal,

have a temporary effect on FakeCaptcha and other

Proofpoint, Team Cymru, Zscaler, and several law

We can certainly call the Lumma Stealer disruption a success. The malware suffered a

varieties of ClickFix attacks.

enforcement agencies across the globe. The takedown

considerable technical blow, taking it out of commission for some time after the operation

occurred. While we now see that the threat actors have started rebuilding Lumma Stealer

Danabot brought to its knees

infrastructure using DNS servers located in Russia, the reputation of this cybercriminal endeavor

Just a couple of days after Lumma Stealer’s disruption,

has undoubtedly taken a hit. The ongoing success of Lumma Stealer is very much reliant on the

the notorious infostealer Danabot also got its

trust of its affiliates. This means that even if Lumma Stealer were to succeed in the rebuilding

effort, its user base might just straight up abandon it for another infostealer. In that case, the

most likely path for the malware’s operators would be to completely rebrand their service.

comeuppance, having been targeted by the FBI and US

DoD’s Defense Criminal Investigative Service (DCIS), in

conjunction with Operation Endgame coordinated by

Europol and Eurojust.

was a culmination of a years-long effort on the part

of the involved parties – ESET’s participation in this

endeavor began as early as 2018. Our contribution

included providing technical analyses of the infostealer

and its backend infrastructure, as well as identifying its

C&C servers. This coordinated operation resulted in the

disruption of a large part of Danabot’s infrastructure,

impacting the malware significantly.

Jakub Tomanek, ESET Malware Analyst

Looking at our telemetry data, before the disruption,

activity happening behind the scenes: between June 17,

Lumma Stealer activity in H1 2025 was even higher

2024 and May 1, 2025, we observed 3,353 new unique

than in H2 2024. We have registered a 21% increase

C&C domains, which means about 74 new domains

in the malware’s detections. During this period,

per week. We also noticed regular code updates being

there was also a considerable spike in the malware’s

pushed during this period. This shows that Lumma

numbers following a spam email campaign on April 11

Stealer is a hugely prolific threat, making its disruption

mainly targeting Mexico, which saw more than 40%

that much more important.

of Lumma Stealer attack attempts that day. While

the takedown took place very close to the end of the

reporting period, we are already seeing a drop off in

Lumma Stealer detections.

ESET telemetry also points towards Lumma Stealer

being the primary payload of the HTML/FakeCaptcha

trojan, used in ClickFix social engineering attacks

described in the previous section of this report.

The in-depth research we conducted as part of the

However, even if this method might have mainly been

disruption effort reveals the degree of threat actor

used to distribute Lumma Stealer in the past, its use

![Danabot detection trend in H1 2025, seven-day moving average]

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 11

Danabot is an infostealer written in Delphi that, same as Lumma Stealer,

Cybercriminals have employed Danabot in quite a number of ways: apart

operates as malware as a service. It is available for rent on underground

from the typical data exfiltration capabilities, such as keylogging, screen

forums, putting a variety of tools at the malware affiliates’ disposal, who

recording, and file grabbing, the malware is also used to distribute further

can then establish and manage their own botnets.

malware – even ransomware – to compromised systems. We have

observed it pushing, among other payloads, LockBit, Buran, and Crisis.

Additionally, machines compromised by the infostealer have been employed

to launch DDoS attacks.

The malware itself is distributed using a variety of means. Apart from

being spread through attachments in phishing emails, it is also delivered by

other malware, as well as via malicious sponsored links in Google search

results. As of late, this malware has also started to be distributed via the

ClickFix method: the potential victim is presented with a fake technical

issue, with the “solution” being running a command in a terminal window.

The command contains malicious PowerShell code that ultimately

downloads Danabot.

While, according to ESET telemetry data, Danabot is not as widespread as

Lumma Stealer, it is still a MaaS operation of a considerable scale. Over the

years of tracking this infostealer, ESET analyzed a large number of distinct

samples, and identified more than 1,000 unique C&C servers. Before the

disruption, the malware was on the rise, growing by more than 50% in

H1 2025. Countries most affected by Danabot attack attempts during this

period were the US (44%) and Poland (29%). Thankfully, as can be seen in

the trend data on the previous page, Danabot detections have started to

decline following the disruption.

![Website luring the victim into executing malicious code copied into the clipboard]

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 12

Infostealers Malware as a service

SnakeStealer
slithers to the top

In the wake of Agent Tesla’s creators abandoning their malware, SnakeStealer claims its
place as the most-detected infostealer in ESET telemetry data.

After several years of dominance in ESET’s top

While Agent Tesla is slowly waning, it has already

infostealer statistics, it seems that the era of Agent

been replaced by a new rising star: another MaaS

Tesla has come to an end. It had already slipped into

threat, named SnakeStealer and tracked by us mainly

second place in H2 2024, when it was surpassed by

as MSIL/Spy.Agent.AES trojan, is now the number

Win/Formbook, and its downward trajectory has

one infostealer according to ESET telemetry data.

since continued. Now sitting in fourth place, the H1

SnakeStealer has actually been recommended as a

2025 Agent Tesla detections have decreased by 57%

suitable replacement for Agent Tesla in the latter’s own

compared to the previous period. Based on the claims

Telegram channel. It seems that the recommendations

of the threat actors responsible for this notorious

were key to the malware’s success, as the first surge

malware-as-a-service (MaaS) operation, the reason

of SnakeStealer detections from the end of July 2024

behind the decline is quite prosaic: the operators

roughly coincides with the time that Agent Tesla’s

have lost access to the servers with the infostealer’s

development was discontinued.

source code, and have therefore decided to stop its

development indefinitely. This is why the drop in the

malware’s numbers has been gradual rather than

dramatic – it is not completely gone; new versions are

just not being developed.

SnakeStealer, also known as Snake Keylogger or 404

Keylogger, is .NET malware that first appeared in 2019.

Sold via a Telegram group, this infostealer is capable

of logging keystrokes, stealing saved credentials,

capturing screenshots, and collecting clipboard data.

![SnakeStealer and Agent Tesla detection trends in H2 2024 and H1 2025, seven-day moving average]

![Member of the Agent Tesla Telegram channel recommending SnakeStealer]

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 13

EXPERT COMMENT

While it is certainly possible that SnakeStealer will replace Agent Tesla as the dominant

infostealer, we have to keep in mind that the competition is fierce and there are various

other prevalent infostealers offered on the market. One such example is the Pure

Logs infostealer, which has also been rising in prominence since Agent Tesla stopped

updating. On the other hand, we cannot discount the power of word of mouth, since

we have noticed multiple individuals on the dark web recommending SnakeStealer

as an alternative to Agent Tesla. By itself, however, there is not much else that makes

SnakeStealer stand out in the sea of its competitors.

Jakub Kaloč,, ESET Malware Analyst

The data is then exfiltrated via FTP, SMTP, or Telegram

steady influx of detections of this malware from mid-

bots. The malware is distributed mainly as malicious

January onwards. The infostealer’s numbers more

attachments in phishing emails. SnakeStealer’s

than doubled between H2 2024 and H1 2025. We saw

operators also offer a VIP version of the malware that

the highest rate of SnakeStealer activity in the spring

contains additional features for a higher fee. As these

after it launched three successive email campaigns,

two versions are quite similar to each other from

with detection spikes occurring close to each other

a technical point of view, our MSIL/Spy.Agent.AES

on March 25, April 3, and April 9. Each of those dates,

detection covers both of them.

the malware hit more than 6,000 detections per day.

Looking at ESET telemetry data, we see that

SnakeStealer accounted for almost a fifth of all

infostealer detections we registered in H1 2025.

After an end-of-year holiday lull, there has been a

The countries that have seen the highest numbers

of attempted SnakeStealer attacks are Türkiye (15%),

Japan (13%), and Spain (11%).

Our tracking also managed to catch several

In these campaigns, SnakeStealer was usually

SnakeStealer campaigns targeting Central and Eastern

packed with either Cassandra Protector or Pure

Europe. Among the monitored countries, Poland and

Crypter, which we detect as MSIL/Kryptik trojan

Latvia saw the highest number of attack attempts:

and MSIL/TrojanDownloader.Agent trojan. A typical

counting only the high-effort attempts that were

example of such a case is the victim receiving an email

either targeted or took considerable measures to

with an ISO file attachment, where the attachment

appear credible, we saw almost 5,000 of them in

contains a Pure Crypter executable, which then

Latvia, and more than 18,000 in Poland from January

downloads, decrypts, and launches SnakeStealer.

to April 2025.

![One of the phishing emails with an attachment delivering SnakeStealer (machine translation: Good day. Please confirm the fulfillment of the
attached order. Best regards)]

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 14

Android Adware

Kaleidoscope and its
evil twin scheme flood
Android with ads

Android adware detections jump by 160%, fueled by new evil twin fraud and the rise of
potentially unwanted apps.

A sophisticated new Android threat dubbed

ESET detects this threat as the .MPP variant of

Kaleidoscope is flooding devices with intrusive ads

Android/TrojanDropper.Agent; it accounts for 28% of

through a deceptive evil twin app scheme. While

detections across the whole Android adware category.

its name seems colorfully harmless, Kaleidoscope is

Kaleidoscope impacts a large number of Android users

actually a ploy designed to deceive advertisers and

worldwide each month: according to ESET telemetry,

app stores.

Kaleidoscope is an Android-based ad fraud operation

uncovered by IAS Threat Lab. Cybercriminals behind

this operation create two nearly identical versions of

most victims are in Latin America, Türkiye, Egypt,

and India, where third-party app stores are popular.

Users in these regions unintentionally install evil twin

apps, resulting in intrusive ads and degraded device

the same app – a harmless one available on official app

stores (decoy twin) and a malicious version distributed

through third-party app stores (evil twin). The evil twin

generates intrusive, unwanted ads to fraudulently earn

advertising revenue.

performance.

The evil twin method used by Kaleidoscope is a clever

deception tactic that pursues the steps described in the

next four sections.

![Geographic distribution of Kaleidoscope in H1 2025]

![Kaleidoscope detection trend in H1 2025, seven-day moving average]

20%

0%

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 15

Creating a decoy twin app

evil twin appears to originate from the harmless and

Users can effectively protect themselves by

First, attackers upload a legitimate app (the decoy

twin) to official app stores. This app is genuinely

harmless; it might be a simple puzzle game or a utility

app. Because it’s on the official store, users trust it.

Creating the evil twin

Next, the attackers create another version of the same

app – but this version is malicious (the evil twin). This

malicious app uses the same app name and unique

identifier, called an app ID, but contains additional

code that generates fraudulent ad impressions. These

fraudulent ads appear unexpectedly and intrusively,

legitimate version. In reality, the intrusive ads are real

understanding how this evil twin deception works,

– but unauthorized – and are generated by the evil

sticking to official app sources, paying attention to

twin, tricking advertisers into paying fraudsters for

unusual app behavior, and carefully managing app

illegitimate ad views.

permissions.

Simply put, the evil twin app steals the legitimate app’s

identity, allowing fraudsters to profit from ads that

appear genuine yet are deceptively intrusive.

Interestingly, when compared, the icons of some evil

twin apps are very different from their decoy twins’

icons – for example, a white circle without a name,

while the decoy twins have a more standard app icon.

even when the user isn’t actively using the app.

When opened, these apps also function differently. For

Distributing the evil twin

Since official app stores actively block known malicious

apps, attackers distribute the evil twin through third-

party app stores or websites. Often, they use deceptive

ads and offers to trick users into believing it to be the

legitimate one found on official app stores, leading

them to download the evil twin version.

Connecting the evil twin to the decoy twin

instance, tapping the decoy twin app icon launches

the Birds on a Wire game. In contrast, tapping the

white evil twin icon only brings up the App Info screen

without the user interface. Both apps are shown in the

images to the right.

Kaleidoscope isn’t entirely new. It evolved from a

similar fraud discovered earlier, named Konfety, which

abused an advertising framework called CaramelAds.

After Konfety was exposed, attackers changed their

The key to Kaleidoscope’s success lies in how the

strategy. They removed references to CaramelAds and

evil twin “pretends” to be the legitimate decoy app.

created new, rebranded software tools (SDKs) with

Both twins share the same unique app ID, which

different names. These new SDKs allowed Kaleidoscope

advertisers and automated systems use to identify

to continue undetected, highlighting its ability to

apps. As a result, fraudulent traffic generated by the

constantly adapt.

![Birds on a wire is the app icon of the decoy twin while the white circle is
the app icon of the evil twin]

![Tapping the decoy twin app icon launches the Birds on a Wire game
(top); tapping the white evil twin icon only brings up the App Info
screen (bottom)]

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 16

Ad-fueled threats still cashing in
on mobile users

malicious actions – such as displaying intrusive ads

ESET Mobile Security allows users to choose whether

– but saw a 60% decrease in detections during this

to block or allow PUAs, offering flexibility for those

period. Altogether, Adware, Clickers, and HiddenApps

willing to tolerate certain intrusive behaviors to use

In H1 2025, ESET observed a significant rise in

accounted for 48% of all Android detections in H1 2025.

an app’s primary functions. However, we strongly

two types of Android detections that profit from

advertisements: Adware and Clickers. Combined,

these categories surged by 160%, far outpacing

the 50% increase seen across all types of Android

detections. Adware shows unsolicited ads on users’

devices, while Clickers generate fraudulent ad revenue

by automatically clicking on ads without the user’s

knowledge. A third category, HiddenApps, hides

itself after installation and can perform various

Some apps exhibiting such behavior are classified by

ESET as potentially unwanted applications (PUAs).

While they may not meet the criteria for malicious

software, PUAs can still exhibit intrusive or misleading

behavior, such as displaying excessive ads, device

slowdowns, battery drain, and unauthorized data

collection, negatively affecting user experience and

potentially exposing users to privacy or security risks.

recommend enabling PUA detection to protect your

device, privacy, and security.

![Android Adware, Clicker, and HiddenApp detection trends in H2 2024 and H1 2025, seven-day moving average]

ESET THREAT REPORT

Executive summary

Foreword

Threat landscape trends

Threat telemetry

Research publications

About this report

About ESET

H1 2025 | 17

Android NFC Scams

The evolution of NFC
fraud: From NGate
to GhostTap to relay
scams

NFC-based fraud soared more than thirty-five-fold, fueled by phishing campaigns and
inventive relay techniques.

![Geographic distribution of NFC-related Android malware and scams in H1 2025]

Near-Field Communication (NFC) technology has

When used legitimately, NFC allows for faster, more

transformed how millions of people make payments

secure payments compared to older methods like

and use banking apps. By simply hovering a phone or

magnetic stripes. Unfortunately, cybercriminals have

tapping a contactless card, in-store purchases and even

also set