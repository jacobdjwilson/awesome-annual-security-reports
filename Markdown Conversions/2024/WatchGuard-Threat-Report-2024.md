# Q1 2024 Internet Security Report

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Firebox Feed Statistics](#firebox-feed-statistics)
- [Malware Trends](#malware-trends)
  - [Top 10 Malware Detections](#top-10-malware-detections)
  - [Top 5 Encrypted Malware Detections](#top-5-encrypted-malware-detections)
  - [Top 5 Most-Widespread Malware Detections](#top-5-most-widespread-malware-detections)
  - [Geographic Threats by Region](#geographic-threats-by-region)
  - [Catching Evasive Malware](#catching-evasive-malware)
  - [Individual Malware Sample Analysis](#individual-malware-sample-analysis)
- [Network Attack Trends](#network-attack-trends)
  - [Top 10 Network Attacks Review](#top-10-network-attacks-review)
  - [New Signatures in the Top 50](#new-signatures-in-the-top-50)
  - [Most-Widespread Network Attacks](#most-widespread-network-attacks)
  - [Network Attacks by Region](#network-attacks-by-region)
  - [Conclusion](#conclusion)
- [DNS Analysis](#dns-analysis)
  - [Top Malware Domains](#top-malware-domains)
  - [Top Compromised Domains](#top-compromised-domains)
  - [Top Phishing Domains](#top-phishing-domains)
- [Firebox Feed: Defense Learnings](#firebox-feed-defense-learnings)
- [Endpoint Threat Trends](#endpoint-threat-trends)
  - [Malware Frequency](#malware-frequency)
  - [Alerts by Number of Machines Affected](#alerts-by-number-of-machines-affected)
  - [Alerts by Top 30 Countries Affected](#alerts-by-top-30-countries-affected)
  - [Top Malware and PUPs](#top-malware-and-pups)
  - [Top 10 Most-Prevalent Malware](#top-10-most-prevalent-malware)
  - [Top 10 Most-Prevalent PUPs](#top-10-most-prevalent-pups)
  - [Defense in Depth](#defense-in-depth)
  - [Attack Vectors](#attack-vectors)
  - [Browser Attack Vectors](#browser-attack-vectors)
  - [Alerts by Exploit Type](#alerts-by-exploit-type)
  - [Threat Hunting](#threat-hunting)
  - [Tactics and Techniques](#tactics-and-techniques)
- [Ransomware Landscape](#ransomware-landscape)
  - [Extortion Groups](#extortion-groups)
  - [Notable Ransomware Breaches](#notable-ransomware-breaches)
- [Conclusion & Defense Highlights](#conclusion-defense-highlights)
- [About WatchGuard Threat Lab](#about-watchguard-threat-lab)
- [About WatchGuard Technologies](#about-watchguard-technologies)
- [Corey Nachreiner](#corey-nachreiner)
- [Marc Laliberte](#marc-laliberte)
- [Trevor Collins](#trevor-collins)
- [Ryan Estes](#ryan-estes)
- [Josh Stuifbergen](#josh-stuifbergen)

Quarter 4, 2022
Q1 2024

Q1 2024 Internet Security Report
2

CONTENTS
The Firebox Feed™ provides quantifiable data and trends 
about hackers’ latest attacks, and understanding these trends 
can help us improve our defenses. 
03  Introduction
 
04  Executive Summary
 
06   Firebox Feed Statistics
08  
Malware Trends
    
09  
Top 10 Malware Detections
    
10  
Top 5 Encrypted Malware Detections
    
10  
Top 5 Most-Widespread Malware Detections
    
11  
Geographic Threats by Region
    
12  
Catching Evasive Malware
    
13  
Individual Malware Sample Analysis  
    
15  
 Network Attack Trends
    
16  
Top 10 Network Attacks Review
    
19  
Most-Widespread Network Attacks
    
21  
Network Attack Conclusion
    
22  
DNS Analysis
    
22  
Top Malware Domains
    
25  
Firebox Feed: Defense Learnings
26  Endpoint Threat Trends
    
30  
Top Malware and PUPs
    
33  
Attack Vectors
    
37  
Ransomware Landscape
41  Conclusion and Defense Highlights
44  About WatchGuard

Q1 2024 Internet Security Report
3
In this report, we cover:
Network-based malware trends:  
 
WatchGuard Fireboxes have three different network-based anti-
malware detection services that block hundreds of thousands 
of network and malware attacks every day. They include 
signature-based malware detection, machine learning, and 
behavioral detection. This section highlights the most prominent 
and widespread malware our unified threat management 
(UTM) products saw during Q1. We illustrate the top threats by 
volume, by most Fireboxes affected, and by region. We cover 
the differences in malware seen over encrypted connections 
and how much malware bypasses signature-based detection 
(which we call zero-day malware). We also highlight interesting 
malware samples in greater detail. During Q1, we saw network 
malware volume drop significantly; however, zero-day malware 
over encrypted connections remains high. We also saw three 
malware variants on our top 10 list that seem associated with the 
GoldenSpy campaign. 
Network attack trends:  
The Firebox’s Intrusion Prevention Service (IPS) blocks many 
client- and server-based network exploits. This section highlights 
the most common network attacks we saw during Q1, which 
include common web browser vulnerabilities, web applications, 
flaws in various web servers and frameworks, and many other 
network service vulnerabilities. This quarter we saw network 
attack volume increase quarter-over-quarter (QoQ). One network 
exploit new to our top 10 list targeted HAProxy, a popular Linux 
load balancer application. Meanwhile,  ProxyLogon remained in 
the #2 spot on our top attack list.
Top malicious domains:  
Using data from our DNSWatch service, we share trends about 
the malicious web links your users click. We prevent your users 
from reaching these domains, thus protecting your organization, 
but we still report on the most popular malicious domains they 
accidentally clicked on. This quarter, DNSWatch found evidence 
of PandoraSpear, an Internet of Things (IoT) botnet that targets 
smart TVs.
Endpoint malware trends:  
We also track the malware trends we see at the endpoint from 
our WatchGuard EPDR and AD360 products. These malware 
trends seem to often differ greatly from what network security 
devices see. While network-detected malware declined, endpoint 
malware detections increased by 75%. However, the amount of 
unique and new malware we detected declined. Higher malware 
volume with less unique malware means that threat actors 
seemed to spam older threats during Q1, and signature-based 
detection caught the vast majority of it quickly. Of the browsers 
used as a malware infection vector, Chromium ones, like Chrome, 
led the pack. We also found that malicious Excel documents are 
the most prevalent type of Office document to hide malware. 
The right defenses for the latest 
attack trends. 
While most this report talks about the latest attack trends, the 
actual point of it is to give you the current intelligence you 
need to adjust your defense strategy. Like the anecdote from 
our introduction, if you know how attacker techniques evolve, 
you might be able to adjust your protections to avoid that 
ransomware infection. Throughout this report, and at the end, 
we share various practical security tips and strategies that could 
protect you from the attacks we see in the wild. 
08
15
22
26

<a id="introduction"></a>
# INTRODUCTION
Every quarter, I introduce this report with a metaphor or quote on why 
following trends in cybersecurity is important to doing better at protecting 
yourself. This time, I figured we’d try a fictional anecdote that isn’t too far 
from examples of reality.
The Tale of the Underprepared Hospital
In 2023, a midsize hospital, we’ll call it “MediCare Health,” operated with an 
arguably reasonable level of cybersecurity measures. They had traditional 
firewalls, basic antivirus software, and regular employee training sessions 
on basic cybersecurity hygiene. However, the hospital’s IT team wasn’t 
particularly vigilant about staying updated on the latest cybersecurity 
trends and assumed their existing measures were sufficient.
However, ransomware attacks were becoming increasingly sophisticated, 
targeting specific industries with tailored tactics. A new major trend in 
ransomware was the exploitation of remote access services that didn’t use 
multi-factor authentication (MFA) or the use of “double extortion,” where 
attackers not only encrypted data but also threatened to release sensitive 
information unless a ransom was paid. Ransomware actors also used more 
living-off-the-land  (LotL) techniques and evasive malware to get past basic 
defenses. These were significant evolutions from how previous ransomware 
actors launched their attacks.
Despite the changing and growing threat, MediCare Health didn’t update 
their ransomware defense strategy. They were unaware of the new trends 
so never considered additional measures such as improved, more-advanced 
endpoint detection and response (EDR) systems, or MFA for all their 
employees’ remote logins. 
As a result, in early 2024 MediCare Health fell victim to ransomware. The 
attackers had monitored the hospital’s network for weeks, understanding 
the critical nature of the data and the hospital’s operations. They broke 
in with a stolen credential that they used to log in to a remote access 
service, which did not use MFA. They launched a double extortion attack, 
encrypting patient records and threatening to release confidential medical 
information if a hefty ransom wasn’t paid.
The hospital’s IT team was caught off guard. Their backup systems were 
outdated, and without EDR software and a good incident response plan, 
they missed the attack until it was too late. In fact, they didn’t even take 
advantage of their service provider’s managed detection and response 
(MDR) service. The attackers demanded a ransom of $22 million, and the 
hospital faced the daunting possibility of patient data being exposed 
publicly.
The attack had severe consequences. The hospital had to shut down its 
systems temporarily, affecting patient care and delaying treatments. They 
eventually decided to pay the full ransom to prevent the data from being 
released, but the incident not only cost them tens of millions in ransom but 
even more in system restoration and lost revenue. Additionally, their repu-
tation suffered greatly, and trust among patients was severely damaged.
The moral of the story? It should be obvious. Attackers change their 
techniques as we change our defenses. What worked yesterday may not 
work today as threat actors evolve due to our protection strategies. If their 
old techniques don’t work, they move on to new ones. This is a completely 
fictional anecdote, but you might notice it shares many similarities to 
incidents that have happened.
Our quarterly Internet Security Report is designed to help you avoid 
becoming the victim of this anecdote. By offering the latest quantifiable 
threat intelligence about cyberattacks our products see each quarter, we 
hope to uncover the latest attack trends for you, so that you can make the 
appropriate updates to any defenses you might have missed.
41

<a id="executive-summary"></a>
# EXECUTIVE SUMMARY
This quarter, our malware trends almost reflectively mirror the opposite of our last report. During Q4 2023, network-based malware detections 
were up, and endpoint malware detection was down. For Q1 2024, network malware detection dropped by almost half (49%). Meanwhile, 
endpoint malware volume rose over 75% – the complete opposite of before. 
Last quarter, evasive malware detected by our behavioral and machine-learning anti-malware services was up. This quarter, all our advanced 
malware detection results are down, but signature-based detections are up, both for network and endpoint products. After many years of 
warning you that you’ll miss over half of malware if you don’t use more advanced detection services, this quarter the good old signature-based 
detection did most the work. 
The network attack story is quite similar. Last time, network attacks had decreased 10%, but during Q1 they increased by 13%. Last quarter, 
attackers tried more unique network exploits (meaning a greater diversity of types of attacks), this quarter unique attacks are down 16%. Mean-
while, there are some similarities between both quarters too. ProxyLogon – a critical Microsoft Exchange vulnerability that could lead to remote 
code execution – remained #2 on our top 10 network attack list. We said it before, but if you didn’t patch this over a year ago, you should get on 
that. 

•	 Total network-based malware detections dropped nearly in 
half, down 49%. This was a surprise and distinctly the opposite of 
last quarter, where it had risen 80%. Malware detections from all 
our proactive anti-malware services, APT Blocker and IntelligentAV 
(IAV), were down significantly as well. The only service with a 
slight increase was our signature-based Gateway AntiVirus service 
(GAV). However, the amount of malware detected over encrypted 
connections increased. 
•	 On the flipside, endpoint malware detections increased greatly, 
growing over 75% QoQ. To some extent, this makes sense. If 
products catch less malware at the network, the endpoint likely 
will see more threats.
•	 Malware hiding behind encryption (TLS) increased to 69% in 
Q1. As we continue to mention, you will miss more than half of 
malware over a network unless you decrypt HTTPS web traffic. It’s 
a free feature – enable it.
•	 Our “per Firebox” malware results for various network malware 
detection services:
    - Average total malware detections per Firebox: 1,224 
(~49% decrease)
    - Average malware detections by GAV per Firebox: 562  
(8% increase)
    - Average malware detections by IAV per Firebox: 587  
(58% decrease)
    - Average malware detections by APT Blocker per Firebox: 75 
(85% decrease)
•	 We extrapolate that if all the currently active (licensed) Fireboxes 
with some services were reporting to us and had all malware 
detection services enabled, we would have had 472,991,544, or 
almost half a billion malware detections during Q1 2024.
•	 Zero-day malware dropped to 36% of all malware during Q1. As 
a reminder, we define zero-day malware as malware that evades 
signature-based protection, only detected by more proactive 
techniques. Our zero-day malware number has historically been 
much higher; 50% or more. This is the first time in a long time we 
have seen it drop so low. While that does mean signature-based 
detection caught a lot last quarter, we still recommend our more 
proactive anti-malware services. 
•	 The Pandoraspear botnet, which targets smart TVs running 
an open-source Android OS, jumped into our top 10 most 
widely detected malware list, highlighting the potential risk of 
vulnerabilities in IoT devices for enterprise security.
•	 A new variant of the Mirai malware family that targeted TP-Link 
Archer devices emerged as one of the most-widespread malware 
campaigns of the quarter. The Mirai variant reached nearly 9% of 
all WatchGuard Fireboxes around the globe. 
•	 Network attacks increased 13% quarter over quarter (QoQ), 
but remain down considerable year-over-year (YoY). On the other 
hand, unique network attacks, which show the variety of different 
network exploits attackers use, declined 16%.
•	 An HAProxy vulnerability was among the top network attacks of 
the quarter. HAProxy is a Linux-based load balancer application. 
The vulnerability, which was first identified in 2023, shows how 
weaknesses in popular software can lead to a widespread security 
problem.
•	 ProxyLogon continues in the #2 spot of top-exploited attacks 
during Q1. As a reminder, this was a critical, remote code 
execution vulnerability against Microsoft Exchange servers that 
you should have patched long ago. It remains in the number two 
spot on our top 10.
Q1 2024 Internet Security Report
5
Now that you know the top highlights from this quarter’s report, it’s time for you to dive into the fascinating and hopefully insightful details. Remember, 
we aren’t just sharing these malicious trends for fun, but will share practical defensive tips and strategy along the way. 
•	 The exploits in our top 10 network attacks by volume account 
for 57% of all detections. Showing that these flaws are by far the 
ones threat actors (and pen testers) spam the Internet with. 
•	 Overall, endpoint malware detections increased over 75% by 
pure volume – a pretty significant increase over previous quarters. 
Perhaps this increase corresponds to our decrease in network-
based malware protections? 
•	 However, our endpoint protection products only blocked 88 
unique malware variants per 100k machines, which is an over 
18% decline compared to Q4 2023. Remember, this has nothing 
to do with volume, but more to do with distinctly unique new 
variants of malware, which also happen to sometimes evade 
signature-based protection. When malware detection volume 
increases, but unique variants per machine decreases, it suggests 
that attackers might be spamming old variants of malware to 
many victims, which will easily get detected by our signature-
based techniques. 
•	 Endpoint ransomware attacks continue to decrease, dropping 
about 23%. Ransomware seems to have plateaued recently. Its 
decrease is likely due to many takedown efforts by the authorities, 
such as Lockbit. We do expect to see these variants eventually 
return despite their takedowns.
•	 This quarter, Chromium-based browsers were found to be 
responsible for producing more than three-quarters (78%) of 
the total volume of malware originating from attacks against 
web browsers or plugins, a significant rise compared to the 
previous quarter (25%). 
•	 Malicious scripts continue to decline as the most prevalent 
malware delivery vector. While malicious PowerShell and 
JavaScript scripts are still the most common living-off-the-land 
(LotL) techniques for delivering malware, they have continued to 
decline as Windows binaries have increased.
•	 DarkGate leverages malicious AWS and faked Akamai 
subdomains to lure victims. Remember, some legit domains 
allow customers to create dangerous subdomains. Meanwhile, 
attackers still like to squat on domains that seem close to the real 
one. 

<a id="firebox-feed-statistics"></a>
# FIREBOX  FEED STATS
Q1 2024 Internet Security Report Malware Trends
7
HELP US IMPROVE 
Our data comes from Fireboxes in our Firebox Feed and the 
more Firebox admins that provide the anonymous data the 
better we can make our reports. If you configure your Firebox 
to do so, we will have more accurate information in this report 
to apply to your network. So please configure your Firebox to 
enable device feedback by following these steps. 
1.	Upgrade to Fireware OS 11.8 or higher  
(we recommend 12.x) 
2.	Enable device feedback in your Firebox settings
3.	Configure WatchGuard proxies and our security 
services, such as GAV, IPS, APT Blocker, and DNSWatch, 
if available
WHAT IS THE FIREBOX FEED? 
 
The Firebox Feed is our source of anonymized primary data from 
Firebox customers that have opted in to sharing threat detections 
with WatchGuard. This data allows us to view the specific malware 
and exploit activity that threat actors are using against small and 
midsize organizations worldwide.
In this section, we detail the high-level quarter-over-quarter 
trends while also diving into the specific top threats that generate 
either the most alert volume or impact the most unique networks. 
Through these lenses, we identify trends in the categories of 
malware or network attacks targeting WatchGuard customer 
networks and use that information to prescribe specific tips for a 
strong defense. 
We break the Firebox Feed up into three main sections built 
off telemetry from five security services running on Firebox 
appliances:
Gateway AntiVirus (GAV): Signature-based malware prevention
IntelligentAV (IAV): Advanced AI-based malware prevention
APT Blocker: Sandboxed, behavioral-based malware prevention
Intrusion Prevention Service (IPS): Network-based client and 
server exploit prevention
DNSWatch: Domain-based threat prevention

<a id="malware-trends"></a>
# MALWARE TRENDS 
 
Most of the data we use from the Firebox Feed comes from proxy 
policies on the Firebox. Unlike typical stateful packet filters, which 
just inspect the source, destination, and ports of network traffic, 
our proxies analyze the body of network packets, allowing our 
security services to investigate more deeply for threats. When 
properly configured by the network administrator, the anonymized 
data from these proxy services allow us to better understand the 
malware your Fireboxes see each quarter in the wild. By comparing 
to past data, we can spot changes in trends and identify new 
techniques that malware adapts to to try to infect more victims. 
We draw our own conclusions based on this data, which we share 
in the report, but we also hope you can use the data to draw 
conclusions that fit your own business or environment. With this 
information, network admins, security professionals, and business 
owners can understand how best to protect themselves from 
future threats. 
We had some interesting malware detection in Q1. One of the 
most-widespread malware detections, Bash.MiraiB.C9B4EC13, 
targets TP-Link Archer devices and uses a newer exploit (CVE-
2023-1389) to gain access to affected wireless routers. It also 
reuses a lot of code from the Mirai botnet to evolve into a variant 
called the Miori botnet. 
Another sample continues the GoldenSpy fiasco, where users 
caught government-owned companies spying on their citizens. We 
saw three different malware variants in our top ten malware related 
to the GoldenSpy campaign, which we describe in more detail 
in our malware analysis below. In other developments, the older 
Agent Tesla malware returns, which leverages an Office exploit and 
targets healthcare providers. 
The malware types we saw during Q1 lead us to believe malware 
will trend towards targeting IoT devices and continue to use 
living-off-the-land (LotL) techniques to hide in legitimate software, 
hoping to enter networks without being detected. During the 
quarter, we saw a significantly lower volume of malware overall, 
but the variants we saw also leveraged more advanced attack 
methods. Before we dive further into these details, let’s begin with 
a high-level overview of the malware trends from Q1 2024.

69%
TLS malware
1,224
Average combined total 
malware hits per Firebox
Average detections per 
Firebox dropped by 49%
562
Basic Gateway AntiVirus 
(GAV) service
Basic malware detections 
increased slightly by 8%
75
APT Blocker (APT)
APT dropped 
significantly by 85%
225
APT Blocker with TLS
TLS detections of evasive 
malware dropped 22%
71
GAV with TLS
TLS detection by GAV 
decreased 76%
587
IntelligentAV (IAV)
IAV hits dropped by 58%
Malware over encrypted 
connections increased 
14%
We not only use the Firebox Feed data to build this report, 
but also to identify areas where we can improve our 
WatchGuard products’ security. If you would like to help with 
these improvements, please enable WatchGuard Device 
Feedback on your device.

<a id="top-10-malware-detections"></a>
# Top 10 Malware Detections
The Top 10 Malware table includes the most detected malware families by total detection volume from reporting Fireboxes. Let’s get into it. In 
Q1, we saw two new malware families, Vundo.FKM and Trojan.Jeki.2. We couldn’t find very many details on Vundo.FKM since we were unable to 
recover a sample of the original file that dropped this malware.  We believe a worm-like virus drops this malware to steal passwords but can’t be 
sure without a sample to analyze. We were able to inspect the other newbie, Trojan.Jeki.2, though. It was a malicious Office document containing 
a macro that runs a PowerShell script to download malware containing the Pyxie remote access trojan (RAT). See our deeper analysis of this 
threat at the end of this section of the report. 
We also found three related samples. The three different variants of Trojan.Heur.RP.Cu2 come from China and arrive as an executable file with 
the name qdfpzsShell.exe. As hinted in the intro of this section, we believe these three samples are a continuation of the GoldenSpy malware 
campaign. We also found the same Fireboxes that detected these GoldenSpy samples, further detected GenericKD.70489621 and Ursu.6302, 
which seemed unusual. However, these malware families don’t seem to relate to GoldenSpy in any other way, so we presume this correlation 
does not offer any causation. GenericKD.70489621 and Ursu.6302 download adware and malware like the 2345Explorer we discussed in our Q1 
2023 report.  
Generic.15257, more of a potentially unwanted program (PUP), identifies the Android version of IPRoyal’s Pawns; a program that pays the user 
to fill out surveys. Like most PUPs and adware, it connects to servers that also spread a lot of malware. We recommend avoiding these shady 
programs, especially in a corporate environment. 

| Threat Name           | Malware Category   | Count   | Last Seen |
|-----------------------|--------------------|---------|-----------|
| Generic.3112968       | Adware             | 885,177 | Q3 2023   |
| GenericKD.70489621    | Dropper            | 787,367 | Q3 2023   |
| Heur.RP.Cu2@b8XQ9afj  | Win Code Injection | 739,807 | Q4 2023   |
| Ursu.6302             | Dropper            | 632,623 | Q2 2023   |
| (Android) Generic.15257 | Adware             | 472,817 | Q4 2023   |
| Heur.RP.Cu2@bGGIINgj  | Win Code Injection | 346,448 | Q4 2023   |
| Linux.XORDDoS.AT      | Dropper            | 166,790 | Q4 2023   |
| Heur.RP.Cu2@b8XPSEbj  | Win Code Injection | 139,265 | Q4 2023   |
| Vundo.FKM            | Password Stealer   | 109,364 | new       |
| Trojan.Jeki.2         | Office Exploit     | 45,636  | new       |

Figure 1. Top 10 Malware Detections

<a id="top-5-encrypted-malware-detections"></a>
# Top 5 Encrypted Malware Detections 
All Fireboxes are capable of inspecting encrypted connections 
and can block malware over these connections. Unfortunately, 
network admins only configure about one in five Fireboxes to 
do this. We encourage all network administrators to configure 
encrypted connection inspection (through our HTTPS proxy) to 
receive the full benefit of our malware inspection and IPS services. 
Since most Internet web traffic uses encryption, we believe the 
malware trends seen within HTTPS connections likely show the real 
picture. However, because so few Fireboxes enable and report on 
this feature, we may only have a partial view. For the Fireboxes that 
do report, 69% of malware detections come from these encrypted 
connections. To show how malware over encrypted connections 
differs from general malware detections, we present the Top 5 
Encrypted Malware table.

<a id="top-5-most-widespread-malware-detections"></a>
# Top 5 Most-Widespread Malware Detections 
Now that we have covered the top malware by raw volume, let’s look at the malware we see on the most Fireboxes. This gives us an 
understanding of widespread malware vs just pure volume. We also believe this better represents what smaller networks see. Smaller networks 
won’t have the same configurations as larger ones, so malware targets these networks differently. Since larger networks see more traffic overall, 
their malware volume may distort our analysis of the most common threats without this normalized, widespread view. 
Two of the top threats in our Top 5 Widespread Malware table, RTF-ObfsObjDat.Gen and MathType-Obfs.Gen, are malicious documents 
exploiting Microsoft Office vulnerabilities, which spread mostly in Europe, the Middle East, and Africa (EMEA). An interesting malware family, 

| Threat Name                       | Malware Category    | Hits   |
|-----------------------------------|---------------------|--------|
| Heur2.ObfDldr.9.63A9E772.Gen      | Office Exploit      | 12,482 |
| GenericKDZ.92453 (Agent Tesla)    | Win code Injection  | 12,237 |
| Agent.GIKS                        | Win Code Injection  | 12,120 |
| Logan.749                         | Password Stealer    | 10,417 |
| Agent.IIQ                         | Password Stealer    | 9,579  |

Figure 2. Top 5 TLS Malware

| Top 5 Most-Widespread Malware | Top 3 Countries by % | EMEA % | APAC % | AMER % |
|-------------------------------|----------------------|--------|--------|--------|
| RTF-ObfsObjDat.Gen            | Greece - 28.54% Hong Kong - 24.14% Germany - 22.04% | 16.16% | 6.58%  | 4.71%  |
| Bash.MiraiB.C9B4EC13          | Sweden - 22.77% Denmark - 15.71% Cyprus - 14.77%  | 6.44%  | 7.52%  | 8.67%  |
| MathType-Obfs.Gen             | Greece - 23.33% Hong Kong - 13.79% Turkey - 13.27% | 9.40%  | 2.95%  | 3.86%  |
| JS.Agent.USF                  | India - 62.56% New Zealand - 14.94% Brazil - 14.93% | 5.50%  | 7.86%  | 9.04%  |
| Zmutzy.1305                   | Cyprus - 15.91% Greece - 14.64% Hong Kong - 14.48% | 7.67%  | 5.67%  | 2.56%  |

Figure 3. Most-Widespread Malware
Bash.MiraiB.C9B4EC13 contains a short script that matches a recent campaign to exploit the TP-Link Archer devices. As the name suggests, it 
contains a variant of the Mirai botnet. We will cover it in more detail later. Finally, Zmutzy.1305 (a loader/dropper that installed Agent Tesla in the 
past) and JS.Agent.USF (a JavaScript redirector) are two malware variants we saw and discussed last quarter. A staggering 63% of Fireboxes in 
India saw JS.Agent.USF.
The top threat in our Top 5 TLS Malware table, Heur2.ObfDldr.9.63A9E772.Gen, is a malicious Microsoft document that exploits an Office 
vulnerability. Not far behind in the total number of detections, GenericKDZ.92453 contains a variant of Agent Tesla like the one discussed in Q4 
of last year. Closely behind that, Agent.GIKS contains a Microsoft Visual Basic Script to inject malicious code. We don’t have a sample to test, but 
we found a large overlap in devices reporting GenericKDZ.92453 (Agent Tesla) with devices reporting Agent.GIKS. A single malware campaign 
likely downloaded both. Finishing off the table, we saw two known password stealers, Logan.749 and Agent.IIQ. 

<a id="geographic-threats-by-region"></a>
# Geographic Threats by Region
Identifying threats geographically helps us better understand the regions malware targets most. To calculate these percentages, we first add the 
total number of malware detections in each region. However, since each region varies in the number of Fireboxes reporting in, we next divide the 
number of detections over the number of Fireboxes in that region to get a normalized number of detections per Firebox in the region. To make 
it easier to read, we finally convert these numbers to percentages. This provides a chart to see what regions detect the most malware without 
regional Firebox sales skewing results. 

| Region | % Share |
|--------|---------|
| AMER   | 22.5%   |
| EMEA   | 14.71%  |
| APAC   | 62.76%  |

![Geographic Threats by Region](https://i.imgur.com/0000000.png)
Figure 4. Geographic Threats by Region
This quarter, we, by far, saw the most malware volume in the Asia-Pacific (APAC) region at 62.7% of regional malware. This was a 20-point 
increase in malware detections in APAC compared to Q4 2023. The increased volume mostly comes from the unusually high number of Heur.
RP.Cu2 variants detected in China. Malware detections in the Americas (AMER) dropped by 16 points for a total of 22.5% and Europe,