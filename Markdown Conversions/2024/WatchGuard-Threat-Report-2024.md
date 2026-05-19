# Threat-Report 2024

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
- [Most-Widespread Network Attacks](#most-widespread-network-attacks)
- [Network Attack Conclusion](#network-attack-conclusion)
- [DNS Analysis](#dns-analysis)
- [Top Malware Domains](#top-malware-domains)
- [Firebox Feed: Defense Learnings](#firebox-feed-defense-learnings)
- [Endpoint Threat Trends](#endpoint-threat-trends)
- [Top Malware and PUPs](#top-malware-and-pups)
- [Attack Vectors](#attack-vectors)
- [Ransomware Landscape](#ransomware-landscape)
- [Conclusion and Defense Highlights](#conclusion-and-defense-highlights)
- [About WatchGuard](#about-watchguard)

---

## Introduction

Every quarter, I introduce this report with a metaphor or quote on why following trends in cybersecurity is important to doing better at protecting yourself. This time, I figured we’d try a fictional anecdote that isn’t too far from examples of reality.

### The Tale of the Underprepared Hospital

In 2023, a midsize hospital, we’ll call it “MediCare Health,” operated with an arguably reasonable level of cybersecurity measures. They had traditional firewalls, basic antivirus software, and regular employee training sessions on basic cybersecurity hygiene. However, the hospital’s IT team wasn’t particularly vigilant about staying updated on the latest cybersecurity trends and assumed their existing measures were sufficient.

However, ransomware attacks were becoming increasingly sophisticated, targeting specific industries with tailored tactics. A new major trend in ransomware was the exploitation of remote access services that didn’t use multi-factor authentication (MFA) or the use of “double extortion,” where attackers not only encrypted data but also threatened to release sensitive information unless a ransom was paid. Ransomware actors also used more living-off-the-land (LotL) techniques and evasive malware to get past basic defenses. These were significant evolutions from how previous ransomware actors launched their attacks.

Despite the changing and growing threat, MediCare Health didn’t update their ransomware defense strategy. They were unaware of the new trends so never considered additional measures such as improved, more-advanced endpoint detection and response (EDR) systems, or MFA for all their employees’ remote logins.

As a result, in early 2024 MediCare Health fell victim to ransomware. The attackers had monitored the hospital’s network for weeks, understanding the critical nature of the data and the hospital’s operations. They broke in with a stolen credential that they used to log in to a remote access service, which did not use MFA. They launched a double extortion attack, encrypting patient records and threatening to release confidential medical information if a hefty ransom wasn’t paid.

The hospital’s IT team was caught off guard. Their backup systems were outdated, and without EDR software and a good incident response plan, they missed the attack until it was too late. In fact, they didn’t even take advantage of their service provider’s managed detection and response (MDR) service. The attackers demanded a ransom of $22 million, and the hospital faced the daunting possibility of patient data being exposed publicly.

The attack had severe consequences. The hospital had to shut down its systems temporarily, affecting patient care and delaying treatments. They eventually decided to pay the full ransom to prevent the data from being released, but the incident not only cost them tens of millions in ransom but even more in system restoration and lost revenue. Additionally, their reputation suffered greatly, and trust among patients was severely damaged.

The moral of the story? It should be obvious. Attackers change their techniques as we change our defenses. What worked yesterday may not work today as threat actors evolve due to our protection strategies. If their old techniques don’t work, they move on to new ones. This is a completely fictional anecdote, but you might notice it shares many similarities to incidents that have happened.

Our quarterly Internet Security Report is designed to help you avoid becoming the victim of this anecdote. By offering the latest quantifiable threat intelligence about cyberattacks our products see each quarter, we hope to uncover the latest attack trends for you, so that you can make the appropriate updates to any defenses you might have missed.

---

## Executive Summary

This quarter, our malware trends almost reflectively mirror the opposite of our last report. During Q4 2023, network-based malware detections were up, and endpoint malware detection was down. For Q1 2024, network malware detection dropped by almost half (49%). Meanwhile, endpoint malware volume rose over 75% – the complete opposite of before.

- **Total network-based malware detections dropped nearly in half, down 49%.**
- **Zero-day malware dropped to 36% of all malware during Q1.**
- **Endpoint malware detections increased greatly, growing over 75% QoQ.**
- **The Pandoraspear botnet** jumped into our top 10 most widely detected malware list.
- **Malware hiding behind encryption (TLS) increased to 69% in Q1.**
- **A new variant of the Mirai malware family** that targeted TP-Link Archer devices emerged.
- **Network attacks increased 13% quarter over quarter (QoQ).**
- **ProxyLogon continues in the #2 spot** of top-exploited attacks during Q1.

---

## Firebox Feed Statistics

![Firebox Feed diagram showing data sources from GAV, IAV, APT Blocker, IPS, and DNSWatch]

The Firebox Feed is our source of anonymized primary data from Firebox customers that have opted in to sharing threat detections with WatchGuard. This data allows us to view the specific malware and exploit activity that threat actors are using against small and midsize organizations worldwide.

---

## Malware Trends

![Chart showing average combined total malware hits per Firebox: 1,224]

We had some interesting malware detection in Q1. One of the most-widespread malware detections, `Bash.MiraiB.C9B4EC13`, targets TP-Link Archer devices and uses a newer exploit (CVE-2023-1389) to gain access to affected wireless routers. It also reuses a lot of code from the Mirai botnet to evolve into a variant called the Miori botnet.

---

## Top 10 Malware Detections

| Threat Name | Malware Category | Count | Last Seen |
| :--- | :--- | :--- | :--- |
| Generic.3112968 | Adware | 885,177 | Q3 2023 |
| GenericKD.70489621 | Dropper | 787,367 | Q3 2023 |
| Heur.RP.Cu2@b8XQ9afj | Win Code Injection | 739,807 | Q4 2023 |
| Ursu.6302 | Dropper | 632,623 | Q2 2023 |
| (Android) Generic.15257 | Adware | 472,817 | Q4 2023 |
| Heur.RP.Cu2@bGGIINgj | Win Code Injection | 346,448 | Q4 2023 |
| Linux.XORDDoS.AT | Dropper | 166,790 | Q4 2023 |
| Heur.RP.Cu2@b8XPSEbj | Win Code Injection | 139,265 | Q4 2023 |
| Vundo.FKM | Password Stealer | 109,364 | new |
| Trojan.Jeki.2 | Office Exploit | 45,636 | new |

---

## Top 5 Encrypted Malware Detections

| Threat Name | Malware Category | Hits |
| :--- | :--- | :--- |
| Heur2.ObfDldr.9.63A9E772.Gen | Office Exploit | 12,482 |
| GenericKDZ.92453 (Agent Tesla) | Win code Injection | 12,237 |
| Agent.GIKS | Win code Injection | 12,120 |
| Logan.749 | Password Stealer | 10,417 |
| Agent.IIQ | Password Stealer | 9,579 |

---

## Top 5 Most-Widespread Malware Detections

| Threat Name | Top 3 Countries by % | EMEA % | APAC % | AMER % |
| :--- | :--- | :--- | :--- | :--- |
| RTF-ObfsObjDat.Gen | Greece - 28.54% | 16.16% | 6.58% | 4.71% |
| Bash.MiraiB.C9B4EC13 | Sweden - 22.77% | 6.44% | 7.52% | 8.67% |
| MathType-Obfs.Gen | Greece - 23.33% | 9.40% | 2.95% | 3.86% |
| JS.Agent.USF | India - 62.56% | 5.50% | 7.86% | 9.04% |
| Zmutzy.1305 | Cyprus - 15.91% | 7.67% | 5.67% | 2.56% |

---

## Geographic Threats by Region

- **APAC**: 62.8%
- **AMERICAS**: 22.5%
- **EMEA**: 14.71%

---

## Catching Evasive Malware

![Chart showing 36% Zero-Day malware vs 64% Other]

During Q1 2024, 36% of zero-day malware used advanced evasive techniques to bypass our signature-based anti-malware (GAV). When it comes to malware arriving over encrypted connections, zero-day malware accounts for 64% of malware.

---

## Individual Malware Sample Analysis

### Bash.MiraiB.C9B4EC13
This widespread sample contains a short script that connects to the IP `103[.]14[.]226[.]142` associated with the Mirai botnet. One line in the script caught our eye: `exec=”your device just got infected to a bootnoot “`. This is associated with the Miori botnet, a variant of Mirai.

### GoldenSpy and GoldenHelper
We found variants of related malware campaigns coming from China, appearing to be a continuation of the GoldenSpy tax software spyware. The malware attempts to hide by using filenames similar to legitimate Windows audio services (e.g., `audiosrv2.exe`).

### Trojan.Jeki.2 (Pyxie RAT)
Our investigation found this is part of the Pyxie RAT trojan. It starts as a booby-trapped Office document that uses a base64-encoded PowerShell script to download further malicious payloads.

---

## Network Attack Trends

There was a slight increase in the number of network threats targeting WatchGuard customers in Q1 2024, with the average number of detections per Firebox device increasing to 98, up 13% from the previous quarter.

---

## Top 10 Network Attacks Review

| Signature | Type | Name | Affected OS | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 1056773 | Buffer overflow | WEB Web Server Connection Header Buffer Overflow | Windows | 12.57% |
| 1138800 | Web threats | WEB Microsoft Exchange Server RCE (CVE-2021-26855) | Windows | 6.89% |
| 1054837 | Web threats | WEB Remote File Inclusion /etc/passwd | Windows, Linux, etc. | 6.80% |
| 1058470 | Web threats | WEB SQL injection attempt -17.h | Windows, Linux, etc. | 5.45% |
| 1231780 | Web threats | WEB HAProxy Empty Header Access Control Bypass | Network Device | 4.96% |
| 1132793 | Web threats | WEB SQL injection select from attempt -5.h | Windows, Linux, etc. | 4.64% |
| 1133253 | Exploits | WEB Remote Command Execution via Shell Script | Linux, etc. | 4.11% |
| 1059958 | Web threats | WEB Directory Traversal -27.u | Windows, Linux | 3.82% |
| 1131523 | Buffer overflow | WEB-CLIENT IE Memory Corruption (CVE-2015-2425) | Windows | 3.78% |
| 1059877 | Exploits | WEB Directory Traversal -8 | Windows, Linux, etc. | 3.67% |

---

## DNS Analysis

DNS firewalling services like DNSWatch monitor domain name resolution requests and redirect victims to a safe location when they detect a threat.

### Top Malware Domains
- `ocmtancmi2c4t[.]xyz`
- `akamai[.]la`
- `ec2-14-122-45-127[.]compute-1[.]amazonaws[.]cdnprivate[.]tel`
- `hhplaytom[.]com`
- `pandoramain-1794008345[.]us-west-2[.]elb[.]amazonaws[.]com`

---

## Conclusion and Defense Highlights

Malware authors find sneaky ways to gain footholds onto their victims’ networks. We must have defenses for each of these infection methods, but no one size will fit all. Regular updates will prevent infection from vulnerabilities but won’t prevent the GoldenSpy attack. Host-based EDR can protect against botnets and RATs but won’t protect network devices like the TP-Link Archer. Perimeter-based protection using advanced sandboxing does well at protecting against all of these but doesn’t do well for social engineering attacks. We should educate users to identify social engineering attacks. Only with all layers of defenses can we hope to protect our users.

---

## About WatchGuard

WatchGuard® Technologies, Inc. is a global leader in network security, endpoint security, secure Wi-Fi, multi-factor authentication, and network intelligence. The company’s award-winning products and services are trusted around the world by more than 18,000 security resellers and service providers to protect more than 250,000 customers.

---

e function names to
make analysis more difficult.

After de-obfuscating the script, it’s a bit easier to see what it
attempted to accomplish.

Q1 2024 Internet Security Report DNS Analysis23Figure 23. Top phishing domainsFigure 24. blawx[.]com pageFigure 25. Powershell codeFigure 26. Obfuscated scriptThe zip archive contains several libraries, executables, and other
files. The PowerShell script executes one of the executable files,
client32.exe, after extracting it from the zip archive. Finally, to gain
persistence, the script adds a new entry for the executable to a Win-
dows registry location responsible for auto-running applications
when the computer is rebooted.

The executable file is a malicious copy of the NetSupport remote
access tool in the form of a remote access trojan (RAT). As the name
suggests, this malware gives attackers remote access to the victim’s
machine, which they can then use to steal information and execute
other malware.

The last two lines of the script are lines of JavaScript that create
a new Wscript.Shell object, a programming object that lets it
execute code other than JavaScript. It then passes in a variable that
contains the other 20 lines of code and executes it.

The bulk of the script is a series of PowerShell variable declarations
and commands. The PowerShell script downloads a base64-encod-
ed string from an attacker-controlled website, decodes it into raw
data, and saves it in a variable. It then generates a random number
and uses that to build a folder in the user’s ApplicationData
directory and save the downloaded data (a zip archive). The script
then extracts the downloaded zip archive and hides the folder
containing everything (the zip archive and its extracted contents).

Q1 2024 Internet Security Report DNS Analysis24Figure 27. De-obfuscated scriptFigure 28. Extracted contentsFIREBOX FEED: DEFENSE LEARNINGS

A strong, secure network doesn’t happen overnight. Only with consistency will we have the protection we need. New and
innovative defenses will help protect us in the future, but we must also keep our defenses strong today or we’ll see another
Mirai-like botnet causing more damage than it should. Over eight years have passed since officials caught Daniel Kaye, the
author of Mirai. We must not forget the lessons learned and new lessons from the new trends in malware. We have learned
these lessons from the Firebox Feed data on how to protect our networks from future threats.

01

02

03

Use Zero Trust to Isolate Networks Against Botnet Infections

In Q1 2024 and Q4 of last year, we see two new botnets starting to spread.  DarkGate and the Miori botnet start off by
infecting an unprotected device. Once it gains a foothold it will spread to other devices in the network. If we don’t segment
the network by separating departments, then it could infect critical servers as well. Don’t allow networks with lower security
to have unprotected access to networks with higher security.

Old and Unusual Programs Still Need Software Updates

Some of us still use older software because it just works. We see nothing wrong with using old software so long as security
updates are provided. WinRAR doesn’t hold the same popularity it once did, but some users will still use it. Researchers
recently found a vulnerability in WinRAR. RARlabs, the company behind the software fixed this vulnerability but users need
to apply the update. Security updates for WinRAR may not happen for much longer though. Any software, however old or
obscure, should still have security updates. If not, then we must look at other options immediately.

All Devices Need Multilayer Protection

Advanced endpoint protection can’t protect all devices. It will protect Windows- , macOS-, or Linux-based online devices but
what about the rest? We can’t use endpoint protection on IoT devices. We see this in the exploit of TP-Link Archer devices
and the infection of Miori. We have no way of protecting with any type of endpoint protection. We need to use network
perimeter protection to protect these devices alongside the host-based protections on other devices.

Q1 2024 Internet Security Report25

ENDPOINT
THREAT
TRENDS

Q1 2024 Internet Security Report26The Internet Security Report wouldn’t be complete without
showcasing our comprehensive endpoint data set. Over the past
few years, we’ve ingested additional data to share with our readers.
Initially, we only had a handful of data points: attack vectors,
browser attacks, ransomware, and cryptocurrency alerts. Since
then, we’ve expanded on each of those, aside from cryptocurrency
alerts, which we currently omit because these are mainly catego-
rized as information stealers instead of only cryptocurrency miners
or stealers. Now, we report on the following data points, including
new Office-based attack vector detections:

•  New malware threats per 100k active machines

•  Total malware threats (unique MD5 hashes)

•  The number of alerts by the number of machines affected

•  The top 30 affected countries each quarter

•  The top 10 most-prevalent malware

•  The top 10 most-prevalent potentially unwanted programs

(PUPs)

•  The number of alerts by which WatchGuard technology

invoked the alert

•  Attack vectors

•  Browser-based attack vector detections

•  Office-based attack vector detections (NEW!)

•  Alerts by exploit type

•  MITRE ATT&CK tactics and techniques (Threat hunting)

•  Ransomware detections (WatchGuard)

•  Ransomware double extortion landscape

•  Notable ransomware breaches

Our approach to the endpoint section is not just about presenting
data but also about continuous improvement. We proactively
review previous quarters to identify areas for better explanation,
graphics for simplification, and new data to incorporate. This
quarter, we’ve made three specific alterations or improvements to
the endpoint section, reflecting our commitment to providing you
with the most accurate and up-to-date information.

The first is the introduction of Office-Based Attack Vectors, as listed
above. This data point is akin to the Browser-Based Attack Vector
detections but for Microsoft Office. The second is difficult to notice
but essential – we’ve switched the order in which the proceeding
Malware Frequency section is written. The Total Malware Threats
appear first because they provide the most-widespread viewpoint
of the malware threat landscape. On the other hand, New Mal-
ware Threats are more straightforward to describe after the Total
Malware Threats because new threats are a subset of all malware
threats. Finally, the third alteration is the enhancement of the Pub-
lic Extortions By Group graph. This is the large red bar graph near
the end of the section. We felt it needed larger fonts and bolder
lines to differentiate between the groups. With that, we begin with
the newly tweaked Malware Frequency section.

MALWARE FREQUENCY
As mentioned, we begin the Malware Frequency section this
quarter with the total malware threats instead of the new ones.
The total malware threats are the sum of all MD5 hashes detected
during the quarter classified as malware. This quarter, the graph
speaks for itself. Throughout 2024, total malware threats remained
stagnant; it hovered around 100,000 each quarter. Then, this
quarter, we observed almost 175,000 total malware threats – a
75.71% increase.

We don’t have an exact explanation for this sharp increase. How-
ever, we have an educated guess. As you’ll see later in this section,
we also observed a similar surge in samples found on only one
machine (by one machine, we don’t literally mean one machine in
the world, we mean a lot of this new malware volume consisted of
unique variants that only affected a single machine) and malware
caught by EPDR’s first line of defense – endpoint antivirus. Taken
holistically, we observed a bunch of malware that ended up on only
one machine and was instantly caught by the endpoint’s antivirus.
An example of malware that fits this narrative could be a phishing
campaign with malicious attachments that slightly differ from each
other for each target victim. The target victim downloaded and
executed the attachment, and EPDR immediately caught it.

Unique Attacks Blocked per
100k Active Machines

173,751

200,000

180,000

160,000

140,000

120,000

100,000

80,000

60,000

40,000

20,000

0

173,751

114,351

108,934

105,033

95,586

Q1

Q2

Q3

Q4

Q1

Interestingly, the significant increase in total threats didn’t contain
many never-before-seen malware. Instead of an increase in new
malware threats, we observed a slight decrease quarter-to-quarter
of 18.52%. This means all the malware we detected in Q1 were the
same malicious files we’ve already seen. Since we began tracking
this data point, there has only been a decrease. However, -18.52% is
our lowest decrease yet. So, perhaps it has plateaued, and we may
see additional new malware next quarter, but we hope not!

New Threats Blocked per
100k Active Machines

88

Q1 2024 Internet Security Report Endpoint Threat Trends27Figure 29: Q1 2024 QoQ Total Malware Threats1068

981

Alerts by Number of Machines Affected

Alerts

1

>= 2 & < 5

>= 5 & < 10

>= 10 & < 50

>= 50 & < 100

>=100

86%

88%

90%

92%

94%

96%

98%

100%

Alerts
184,697

12,525

2,369

1,821

165

137

1

>= 2 & < 5

>= 5 & < 10

>= 10 & < 50

>= 50 & < 100

>=100

As usual, the threats on only one machine outpaced the other
categories with 105,115 alerts. Conveniently, as the number of
machines increases, the number of alerts decreases. There is a
direct inverse correlation this quarter. The number of threats that
appeared on two to five machines was 12,480; 2,854 for threats that
appeared on five to ten machines; 1,732 threats appeared on ten
to 50 machines; 174 for threats appearing on 50 to 100 machines;
and finally, 159 threats appearing on more than 100 machines. All
categories decreased from Q4 except for threats affecting two and
five machines. You can observe the differences in the table.

1200

1000

800

600

400

200

0

171

Q1

Q2

Q3

108

Q4

88

Q1

Alerts by Number of Machines Affected
Filtering malware with different telemetry metrics can help us
understand how it arrives and behaves on the endpoint. One such
filter determines how many machines each malware has appeared
on throughout the quarter. We use the following parameters for
this filter:

•  1 – Exactly one machine alerted on this file/process.

•  >=2 & < 5 – Between two and five machines alerted on this

file/process.

•  >=5 & < 10 – Between five and ten machines alerted on this

file/process.

•  >=10 & < 50 – Between ten and fifty machines alerted on

this file/process.

•  >=50 & < 100 – Between fifty and 100 machines alerted on

this file/process.

•  >=100 – More than 100 machines alerted on this file/

process.

As we touched on earlier, we saw a similar surge in malware
appearing only on one machine, which was immediately caught
by EPDR endpoint detection antivirus. From Q4 2023 to Q1
2024, there was a 75.71% increase in malware appearing on one
machine. Malware appearing on two to five machines and ten to
50 machines saw minor increases of 0.36% and 5.14%, respectively.
Malware appearing on 50 to 100 machines saw a minor decrease
of 5.17%, and malware appearing on over 100 machines saw a
modest decline of 13.84% QoQ. That may seem like a slight decline,
relatively speaking, but each tally is for malware appearing on over
100 machines. This means that 101 instances of malware are the
minimum for each tally. Finally, malware appearing on five to ten
machines saw the largest decrease in QoQ at roughly 17%.

Q1 2024 Internet Security Report DNS Analysis28Figure 30.  2023 QoQ New Threats Blocked per 100k Active MachinesFigure 31. Alerts by Number of Machines AffectedNumber of
Machines

Q4 Alerts

Q1 Alerts Difference from Q4

Percentage Difference
from Q4

1

105,115

184,697

79,582

>= 2 & < 5

>= 5 & < 10

>= 10 & < 50

>= 50 & < 100

>=100

12,480

2,854

1,732

174

159

12,525

2,369

1,821

165

137

45

-485

89

-9

-22

75.71%

0.36%

-16.99%

5.14%

-5.17%

-13.84%

Alerts by Top 30 Countries Affected
The next filter we apply to the data is geographical. We use the
machine’s location that triggered the alert, sum all the numbers
up by country, and then display the top 30 here. Of course, the
countries with the most-active machines each quarter would
naturally appear at the top of this list because the more machines
there are, the more opportunities there are for malware. It’s simple
logic. To combat this, we use the Alert Coefficient, a fancy term for
the ratio of malware detections over active machines. It’s a de facto
per capita formula for malware and active machines.

As usual, the top 30 countries for Q1 are vastly different than the
prior quarter. Six countries appeared on the list that didn’t appear
in Q4: Colombia, Ghana, Malaysia, Tajikistan, Uruguay, and Zimba-
bwe. Most of these appeared towards the bottom of the rankings,
except for Tajikistan and Zimbabwe. Laos ranked first in Q1 with
an Alert Coefficient of 1.31. Cuba was again second with a flat 1.00
Alert Coefficient. Several other countries increased in rankings this
quarter, with Nigeria increasing the most, up 12 places.

On the other hand, Angola declined 11 rankings, which is the most
for Q1. A handful of others had a lower Alert Coefficient, as you can
observe in the Top 30 Countries table. Most of the time, it’s not only
about which countries are affected the most; it can also tell which
regions are affected the most. For example, if we take the top 30
countries and highlight them on a map, we can see that Southeast
Asia, Africa, and South America appear to be the most impacted in
Q1.

Country

Alert Coefficient

Order Difference
from Q2

Sao Tome and Principe

Cuba

Grenada

Laos

Saudi Arabia

Morocco

Pakistan

Mozambique

Bosnia and Herzegovina

Vietnam

Bolivia

United Arab Emirates

Bangladesh

Trinidad and Tobago

Paraguay

Kenya

India

Angola

Turkey

Macedonia

Indonesia

Armenia

Nigeria

Venezuela

Guatemala

Thailand

Botswana

Jordan

Cyprus

Bulgaria

7.14

1.19

1.00

0.79

0.50

0.46

0.42

0.35

0.24

0.16

0.14

0.14

0.13

0.12

0.11

0.11

0.10

0.10

0.10

0.09

0.09

0.09

0.08

0.08

0.07

0.06

0.06

0.06

0.06

0.05

+11

+3

NEW

-1

NEW

-

-

+1

-1

+1

+3

+12

+2

+16

+3

-3

+4

-8

+7

-3

+7

-6

-

+3

-3

NEW

-8

-24

NEW

NEW

Q1 2024 Internet Security Report Endpoint Threat Trends29Figure 32. Alerts by Number of Machines AffectedFigure 34. Q1 2024 Alerts by Top 30 Countries AffectedFigure 33. Alerts by Top 30 Countries AffectedTOP MALWARE AND PUPS
Digging deeper into the data, we can extract the specific samples
that made the most noise, the samples we blocked the most. We
determine the top 10 most-prevalent malware by counting the
number of machines affected by any given malware sample. For
example, the most-prevalent malware for Q1 2024 was a specific
sample of Glupteba. Ironically, this exact sample appeared in the
top 10 list last quarter. So, this particular Glupteba sample has been
causing a lot of trouble for some time. It was the top ranked in Q4
2023 and Q3 2023, and in Q2 2023 it was second.

Top 10 Most-Prevalent Malware
Three other repeats from Q4 were MyloBot, Conficker, and an
unknown malware injector. The Mylobot and Conficker samples
also appeared in the top 10 from prior quarters, but enough of the
rehashed malware samples. Six different samples appeared in the
top 10 in Q1, three of which were various instances of FormBook,
an information stealer. Another two were GuLoader, one that
delivered AgentTesla. The other new addition to the top 10 was a
malicious use of a remote administration tool called NetSupport.
NetSupport itself isn’t malicious, but this threat actor(s) trojanized
it and retooled it for malicious use. Below are the top 10 list and
descriptions of each malware family.

MD5

Signature

Affected Machines
per 100k

Classification Attestation

6CC8D5F1CB1819791E4897F902FAF365*

W97M/Downloader.
DDE

3E86685246C1FDCC9EEF8B95986BA4E4*

Trj/RnkBend.A

FBD8778D87C08492EF10A95AC7C30612*

6F4E93F54CE193843C7686161E28D414

FB8B15D6BD446628322C1B99B8FA8FD6

69893879DFB7420CC301C2097D529607

2253836BB8B0B5479A1F77974B82B1F0*

8A1422827315B9DB63CD6B399A454FAB

AF646CC23394C41B50BBD36C2F33F4F9

6D6B404AD6830E4F76F0B83E4EB6DA24

Trj/WLT.F

Trj/CI.A

Trj/Agent.AY

Trj/Agent.SRT

Trj/RnkBend.A

Trj/RnkBend.A

Trj/Chgt.AD

Trj/Agent.RP

1,459

Glupteba

732

647

318

288

206

182

163

145

140

MyloBot delivering Khalesi

Conficker

Malicious Use Of NetSupport

GuLoader delivering Agent Tesla

Formbook

Unknown Malware (Injector)

GuLoader

Formbook

Formbook

Glupteba

Khalesi

Glupteba is a multi-faceted malware-as-a-service (MaaS) with
capabilities such as (down)loading other malware, acting as a
botnet, stealing information, stealthily mining cryptocurrency, and
more that targets victims seemingly indiscriminately worldwide.
In 2021, Google disrupted the botnet, but it made a resurgence in
late 2022 into early 2023. Like GuLoader, threat actors commonly
use evasive downloaders to deliver additional malware. Although,
unlike GuLoader, Glupteba is arguably more sophisticated and
has more capabilities. It’s an evasive trojan that researchers have
observed taking control commands from the Bitcoin blockchain,
among many other techniques for evasion.

MyloBot

MyloBot has been active for around five years, and interestingly,
the botnet operators are known to have attempted to extort
victims via email. More ubiquitously, the malware’s primary intent
is to infect a machine without the victim’s knowledge, allowing
attackers to leverage any device within its botnet to perform
actions on the attacker’s behalf. Like other botnets and loaders,
the malware downloads the final payload after multiple stages of
evasively downloading malicious files in a daisy-chain fashion.

Khalesi is an information-stealing malware that does what typical
information stealers do. Once executed on an endpoint, these
types of malware steal passwords, Internet cookies and browser
data, password vaults, cryptocurrency wallets, and more based on
the information stealer variant. Khalesi steals web browser data,
cryptocurrency wallets, user credentials, and third-party appli-
cation data. It then prints this stolen data into a temp file before
sending it to a C2 server.

Conficker

Conficker has been around since 2008. It’s usually spread via USB
thumb drives and attempts to self-propagate to other systems
and networks because it’s a worm. What’s unique about Conficker
is that it uses a domain-generation algorithm (DGA) to connect
to URLs that host additional malware or act as a command and
control server (C2). A DGA algorithm dynamically creates a domain
for the malware to connect to using a specific pattern. For exam-
ple, a malicious file could have a DGA that dynamically creates
domains that are 16 alphanumeric characters and end in ‘.net’ (e.g.,
01234567890abdef.net).

Q1 2024 Internet Security Report Endpoint Threat Trends30Figure 35. Top 10 Most-Prevalent MalwareMalicious Use of NetSupport

FormBook

FormBook is a malware-as-a-service (MaaS) information stealer that
allows users to purchase a pre-compiled toolkit and C2 infrastruc-
ture. Therefore, all users only need to tweak it to their specific
needs and perform any nefarious acts. We observe FormBook
samples in malicious documents from phishing emails. FormBook
can steal clipboard data, user credentials, keystrokes, web browser
data, and a long list of targeted third-party applications.

Unknown Malware (Injector)

An “unknown malware” is one we can’t attribute to a specific mal-
ware family, but we can at least generically identify it as a malware
tool. An injector is malware that “injects” itself or a payload into
another process. An example is when malware creates a process
in suspended mode, injects a payload into it, and continues its
execution.

NetSupport is a legitimate remote access control tool. Other
remote access tools include RMM, MeshAgent, TeamViewer, Any-
Desk, and others. These all have legitimate purposes. However, they
are also some of the most commonly used tools by threat actors
because they allow them to remotely control a machine easily.
Ransomware groups commonly use them to deploy ransomware
after infiltrating a network. The instance of NetSupport in the top
10 malware list was a malicious use of NetSupport. In other words,
this particular sample was actively being used by threat actors to
deploy malware onto remote victim machines.

GuLoader

Attackers send this malware in waves by sending spam phishing
emails with malicious attachments containing the first stage of
their campaigns – GuLoader. GuLoader is commonly used to down-
load additional malware, such as infamous information stealers like
RedLine Stealer, Racoon Stealer, Vidar, and FormBook. It is per-
sistently on the top 10 list, or close to it, and is the most-observed
prevalent malware since we’ve started tracking this data.

Agent Tesla

Agent Tesla is another information stealer and remote access
trojan (RAT). It’s been one of the most prevalent for the past several
quarters. Surprisingly, it made the top 10 list for the first time in
Q3 because there are a lot of different versions. It’s difficult for one
single hash to affect so many machines as opposed to other spam
malware campaigns such as GuLoader and Glupteba. Agent Tesla
is a .NET program that appears to be an authentic file. These files
come in various types, but threat actors fully coded them to appear
as authentic as possible, appearing as calculators, educational
programs, and more.

Q1 2024 Internet Security Report Endpoint Threat Trends31Top 10 Most-Prevalent PUPs
PUPs, or PUAs, stand for potentially unwanted programs or potentially unwanted applications. They are interchangeable and mean the same
thing. PUPs describe files that are between malware and legitimate programs (goodware). They’re not overtly malicious or easy-to-understand
goodware. They are in the middle, and many are described as suspicious. However, if a PUP were to perform any malicious action, then we’d
classify it as malware.

In Q1, there were seven repeat PUPs from Q4 2023. Therefore, there are only three new PUPs. The most-prevalent PUP this quarter, which we’ve
never observed before, is a hacking tool called SM Host. This tool is used to view a machine’s internal network. Nefarious threat actors commonly
abuse these tools for discovery once on a victim’s network. The second new addition to the top 10 is Mail PassView, a password recovery tool for
Outlook. It is another NirSoft tool that is similar to the previous one. The final new PUP is a cracked Microsoft Office 2013-2019 version. Those
three and the other seven are described below.

MD5

8D74E04C022CADAD5B05888D1CAFEDD0

8D0C31D282CC9194791EA850041C6C45*

2914300A6E0CDF7ED242505958AC0BB5*

CFE1C391464C446099A5EB33276F6D57*

6A58B52B184715583CDA792B56A0A1ED*

FC3B93E042DE5FA569A8379D46BCE506

30C7E8E918403B9247315249A8842CE5*

Signature

PUP/Generic

HackingTool/
AutoKMS

HackingTool/
AutoKMS

HackingTool/
AutoKMS

Hacktool/
PortScanner

PUP/Hacktool

HackingTool/
AutoKMS

1E2A99AE43D6365148D412B5DFEE0E1C*

PUP/BundleOffer

C9E4916575FC95BEDBD12415AB55CC84*

PUP/Hacktool

4C506F1B0E46ED1442EB0CAEB2812244

HackingTool/
AutoKMS

Affected Machines
per 100k

Classification Attestation

5,942

2,722

1,016

892

822

817

696

623

603

595

SM Host

KMSPico

KMS_VL_ALL_AIO

AutoPico

Advanced Port Scanner

Mail PassView

Unknown Software Installer

PDF Power 4.0.1.0 Setup Wizard

CVE-2014-0160 (Heartbleed)
JavaScript Exploit Script

Office 2013-2019 C2R Install
v7.0.4 Crack

PUP/Generic

PUP/Hacktool

This is arguably the most generic classification possible. The most
likely scenario for a sample to earn this classification is if it didn’t
fit within any other signature. Another reason for a file to earn this
classification is if the sample performed suspicious actions that
weren’t exactly malicious but performed actions not commonly
associated with legitimate behaviors. Many of these behaviors
consider the sample’s context and telemetry.

HackingTool/AutoKMS

AutoKMS is an umbrella term encompassing any cracked Microsoft
software that allows users to use Microsoft products without a
license, or it’s a file that facilitates the bypass of Microsoft licensing.

Hacktool/PortScanner

This signature is yet another generic classification for a hack tool,
but with a bit more specificity. Hashes with this classification
perform port scanning actions on networks. Like the PUP/Hacktool
classification above, we can’t be sure whether a penetration tester
or malicious threat actor uses these tools. If given more informa-
tion, we could make a more specific determination.

PUP/Hacktool is a generic classification for any tool or software
used for hacking purposes. Both legitimate penetration testers and
malicious threat actors use these tools. For this reason, we classify
these as PUPs because we can’t be sure whether these tools are
malicious. However, if we capture telemetry or additional context
that allows us to determine if a malicious threat actor uses a hack
tool, there’s a chance we classify it as malware. Most open-source
tools are PUPs or goodware. It’s the proprietary ones that we
usually label as malware.

PUP/BundleOffer

A classification reserved for installers that include third-party soft-
ware or “offers.” Usually, the third-party software is adware, which is
particularly unwanted.

Q1 2024 Internet Security Report Endpoint Threat Trends32Figure 36. Top 10 Most-Prevalent PUPsDefense in Depth
For our Defense in Depth analysis, we zoom back out and filter the
malware detections by which technology caught and classified
each malicious sample. We previously discussed how the endpoint
detection technology caught the vast majority of malware this
quarter, and we saw a massive increase in these detections for Q1.
We believe this surge is correlated to the total malware threats and
malware that ended up on only one machine. The other technolo-
gies, shown below, performed similarly to other quarters.

Alerts

0

20,000

40,000

60,000

80,000

100,000

120,000

140,000

160,000

180,000

AD360 Endpoint Detection

Behavi oral/Machine Learning

Cloud

Digital Si gnature

Manual Attestati on

Defined Rules

•  Endpoint Detection – The typical, legacy endpoint antivirus

solution, Endpoint Detection, displays the number of
hashes invoking an alert located in our known-malicious
hash database. This is commonly called a signature-based
detection antivirus solution.

•  Behavioral/Machine Learning – Behavioral/Machine Learn-
ing is a step above signature-based detections because
it analyzes the file’s actions upon executing in a sandbox.
We create rules based on these behaviors and determine
whether they are malware.

•  Cloud – Alerts that fall under the Cloud category are files
sent to WatchGuard’s Cloud servers for further analysis
beyond signature-based detections and behavior/machine
learning. The files that are malicious activate the counter
here.

•  Digital Signature – Digital Signatures are methods of deter-
mining the authenticity and legitimacy of the sending user
and ensuring nothing has been tampered with (integrity).
We make malware determinations based on these digital
signatures. If an attacker altered it in transit, it is a digital
signature from a known malicious user, or if we know the
signature is compromised, we make a further decision.

•  Manual Attestation – Manual Attestation is a fancy way
of saying that a human analyst scrutinizes the file. If the
file makes it past all of the other technologies and still
looks suspicious, one of WatchGuard’s attestation analysts
performs the analysis and makes a classification. Once a file
reaches this stage, a classification, whether goodware, PUP,
or malware, is always determined.

•  Defined Rules – The final technology, Defined Rules, are
predefined behaviors that, if a file were to perform, we
would determine are malware. Most people associate
defined rules with threat hunting, but these rules can also
apply to endpoint detection.

Our Endpoint Detection technology increased 169.29% from Q4
2023 to Q1 2024, over two and a half times quarter to quarter.
Interestingly, we saw increases in all other technologies except
Cloud detections. Behavioral Learning saw a modest increase of
36.92%, Digital Signature detections increased by 8.22%, Manual
Attestation analysts classified 4.90% more samples this quarter,
and Defined Rules increased by almost 12%. On the other hand,
Cloud-based detections decreased by 16.61%.

AT TACK VEC TORS
The Attack Vectors subsection is the longest-running one in the
endpoint section. We have years of historical data to reference.
For example, more often than not, scripts comprise the majority
of all attack vectors each quarter – specifically, PowerShell. There
have been a few exceptions, but this quarter is one such exception.
Before explaining that, here are the Attack Vector descriptions so
everyone is on the same page.

Attack Vector Descriptions
Acrobat – Adobe Acrobat, a suite of software services provided
by Adobe, Inc., is primarily used to manage and edit PDF files. PDF
files’ ubiquity and ability to bypass email and file transfer filters
make Acrobat services ripe for malicious use.

Browsers –Internet browsers are familiar products for all mod-
ern-day computer users that allow access to the World Wide
Web (WWW). Common browsers include Chrome, Firefox, Safari,
and Edge, among many others. Current browsers store personal
information – if you allow them – including passwords, cookies,
cryptocurrency private keys, and even credit cards, making them
common targets for information-stealing malware.

Office – Office software is the sum of all detections derived from
Microsoft Office executables. This includes Word, Excel, PowerPoint,
Outlook, and Office Suite executables. Not only is Microsoft Office
one of the most popular business-related suites of tools, but the
features of the software, such as macro-enablement, allow for an
increased attack surface.

Other – The Other attack vector is “everything else.” Detections
within this category are those that did not fit any other category.
This includes AutoKMS tools, Remote Services, and third-party
applications, among many others that change every quarter.

Scripts – Scripts, which always invoke the most detections each
quarter, are those files derived from or using a scripting program-
ming language. Malware utilizes PowerShell, Python, Bash, and
AutoIT scripts to download other malware and deliver payloads,
among many other things. Considering Windows is the most
commonly attacked operating system, it is no wonder PowerShell
continues to skew the results for Windows detections.

Q1 2024 Internet Security Report Endpoint Threat Trends33Figure 37. Alerts by TechnologyWindows – Under the hood, Windows-based software houses the
most data points of any attack vector. It contains the most detec-
tions but not in the highest quantities. The files included under the
Windows name ship with the Windows operating system. Examples
include explorer.exe, msiexec.exe, rundll32.exe, and notepad.exe.
Trojans commonly impersonate these files or inject malicious code
into them because they exist on every Windows machine out of the
box and are inherently trusted.

Acrobat
1%

Browsers
4%

Office
2%

Other
9%

Windows
36%

Scripts
48%

Attack Vector

Q3 Count

Q4 Count

Raw Difference
From Q3

Percentage Difference
From Q3

Acrobat

Browsers

Office

Other

Scripts

Windows

692

4319

1190

2120

110855

10662

332

1134

598

2556

13511

10142

-360

-3,185

-592

436

-97,344

-520

-52.02%

-73.74%

-49.75%

20.57%

-87.81%

-4.88%

This quarter, attack vectors declined almost across the board. This invokes the question, “How are total malware threats way up and Attack Vec-
tors way down?” That’s because attack vectors are derived from malware detections from process names, which try to run on victim machines.
Some malware doesn’t even get the chance to execute and is caught by EPDR before it runs. Thus, a process doesn’t exist because it is never
executed.

As you can see in the table, there’s a lot of red. Acrobat, Browsers, Office, Scripts, and Windows each saw declines in detections. Acrobat and
Office attack vectors decreased by around 50%, Browser detections declined by 3.74%, and the largest quarterly decrease was with Scripts. We
saw an unexplained lack of malicious PowerShell invocations. Windows saw the most minor decrease (-4.88%). The only Attack Vector to increase
quarter to quarter is the Other category, a catch-all for any attack vector not within any other category. This increased by 20.57%.

Browser Attack Vectors
The browser-based attack vectors are difficult to predict because they vary significantly from quarter to quarter. Q1 2024 is no different. In Q4
2023, Firefox had the majority share of detections. In Q1 2024, Firefox only had 6%, and Chrome took the majority with 78%. Internet Explorer
remained steady at 16%.

6%

16%

78%

Chrome

Internet Explorer

Firefox

Q1 2024 Internet Security Report Endpoint Threat Trends34Figure 38. Top Exploited SoftwareFigure 39. Attack VectorsFigure 40. Comparative Browser DetectionsAlerts by Exploit Type
The next data point still looks at the process level, but instead of using the process names, we extract the threat actor’s techniques. In other
words, what actions does the malware take to achieve its objective? Always near the top is process hollowing, a common technique attackers
use to “hollow” out a legitimate process on a machine and inject a malicious payload. This way, the process looks legitimate from the outside but
performs malicious actions in the background. This technique took the top spot in Q1; that technique had the most alerts.

The other increases in alerts were from reflective loading, thread hijacking, LSASS process memory dumping, and APC local code execution.
On the flip side, NET reflective loaders (and Metasploit and Cobalt Strike loaders), shellcodes, ROP, GodMode, and dynamic execution without
permissions all saw decreases. There was one new exploit type this quarter and it’s the most generic exploit type of all – Generic. Not only that
but there was only one detection of this exploit. Frankly, there’s not much to gather from that.

Exploit

Alert Count

Description of Exploit

RunPE

PsReflectiveLoader1

RemoteAPCInjection

NetReflectiveLoader

ShellcodeBehavior

AmsiBypass

WinlogonInjection

ThreadHijacking

ROP1

DumpLsass

APC_Exec

IE_GodMode

DynamicExec

HookBypass

JS2DOT

ReverseShell

ReflectiveLoader

Exploit.gen

8,252

4,789

4,051

4,025

3,226

1,713

1,554

439

352

260

236

138

52

30

15

15

8

1

Process Hollowing Techniques

Files that leverage PowerShell to allocate and inject payloads directly within the memory of it's
own process (E.g. Mimikats) (Local)

Remote code injection via APCs

Code execution on MEM_PRIVATE pages that do not correspond to a PE

.NET files that allocate and inject payloads directly within the memory of it's own process
(Assembly.Load)

Techniques that bypass Windows' Antimalware Scan Interface (AMSI)

Remote Code Injection into winlogon.exe process

A process injection technique that allows the execution of arbitrary code in a separate process

Return Oriented Programming

LSASS Process Memory Dump

Local code execution via APC

GodMode technique in Internet Explorer

Execution of code in pages without execution permissions (32 bits only)

Detection of memory allocation in base addresses; typical of heap spraying

.NET Reflective Loading Technique

Detection of reverse shell

Reflective executable loading (Metasploit, Cobalt Strike, etc.)

Generic or unknown exploit

THREAT HUNTING
Our threat-hunting data points are external to the malware
data discussed previously. This data explains the specific tactics,
techniques, and procedures (TTPs) used by attackers from our
threat-hunting service. This service proactively inspects endpoints
to determine if threat actors are actively on an endpoint or
network. These inspections begin with an alert categorized by the
MITRE ATT&CK matrix. We then take that data and share it with
you here. The way we explain this data is on the following page.

Tactics and Techniques
That does it for malware and PUP frequency for Q4. This section
migrates the conversation toward proactive approaches instead of
reactive ones. In other words, we dissect our threat-hunting rules
and efforts to discern which indicators of compromise (IoCs) alert-
ed us the most in Q4 instead of malware observed on endpoints.
IoCs aren’t always malicious; they’re more considered suspicious.
This is why WatchGuard and Panda threat hunters must proactively
investigate these alerts before determining whether they are mali-
cious. The data herein shows the most-observed suspicious alerts
for each tactic, technique, and sub-technique described below.

Q1 2024 Internet Security Report Endpoint Threat Trends35Figure 41. Comparative Browser DetectionsMITRE Tactic – The primary tactic used. (e.g., TA0002 is Execution)

MITRE Technique – The technique used. (e.g., TA1059.001 is
Command and Scripting Interpreter and PowerShell)

Tactic :: Technique :: Sub-Technique – The combined tactic,
technique, and sub-technique.

Technique Count – The number of occurrences for each technique.

Tactic Sum – The sum of all technique counts for a given tactic.

In Q4 2023, we removed some of this data to retain only the most
significant tactics and techniques. We continue to include only
the top 10 techniques to ensure we focus on the most-observed
ones. Our threat-hunting efforts continue to observe a significant
number of PowerShell (TA0002::T1059.001), having the most
detections this quarter again. The rest of the techniques shuffled
around, but there were no notable changes to report except one. A
brand new technique made the top 10 list this quarter – container
service persistence  (TA0003::T1543.005) – ranking ninth. Examples
of persistence via containers are Docker containers or Kubernetes
in an environment.

MITRE Tactic MITRE Technique

Tactic :: Technique :: Sub-Technique

Technique
Count

Rank

TA0002

TA0003

TA0004

TA0005

TA0007

TA0011

TA0040

TA0002

T1059.001

TA0003

T1543.005

TA0004

TA0005

Execution

Execution :: Command and Scripting Interpreter :: PowerShell

Persistence

Persistence :: Create or Modify System Process :: Container Service

Privilege Escalation

Defense Evasion

T1218.009

Defense Evasion :: System Binary Proxy Execution :: Rundll32

TA0007

TA0011

T1561.001

Discovery

Command and Control

Impact :: Disk Wipe :: Disk Content Wipe

4,508,846

7,026,089

5,596,558

1,516,818

3,898,070

4,208,658

1,309,493

5,250,951

2,781,561

5,818,836

5

1

3

9

7

6

10

4

8

2

TA0002-0

TA0002-T1059.001

TA0003-0

4,508,846

7,026,089

5,596,558

TA0003-T1543.005

1,516,818

TA0004-0

TA0005-0

3,898,070

4,208,658

TA0005-T1218.009

1,309,493

TA0007-0

TA0011-0

5,250,951

2,781,561

TA0040-T1561.001

5,818,836

0

1,000,000

2,000,000

3,000,000

4,000,000

5,000,000

6,000,000

7,000,000

8,000,000

9,000,000

10,000,000

Q1 2024 Internet Security Report Endpoint Threat Trends36Figure 42. Exploits by MITRE ATT&CK Tactic and Technique, Q1 2024Figure 43. Exploits by MITRE ATT&CK Tactic and Technique, Q1 2024TA0001

TA0002

TA0003

TA0004

TA0005

TA0006

TA0007

TA0008

881,631

1,741,533

518,450

TA0009

1,237

TA0011

TA0042

1,412

3,756,000

12,938,919

10,964,860

5,703,076

5,253,489

8,864,107

0

2,000,000

4,000,000

6,000,000

8,000,000

10,000,000

12,000,000

14,000,000

RANSOMWARE LANDSCAPE
The ransomware landscape is eventful each quarter, and Q1 2024
was no different. Various new ransomware groups popped up this
quarter, and many active groups from Q4 are now dormant or have
ceased operations. Two of the biggest ransomware operations,
LockBit and ALPHV, saw disruptions to their cyber activities. ALPHV
performed what is likely an exit scam, which is a term that means
they took the money and ran, and LockBit saw their infrastructure
seized by law enforcement, hindering their operations. But more
on those two ransomware groups later.

As usual, we begin with showing the ransomware alerts detected
on WatchGuard EPDR-protected endpoints. Then, we pivot to the
overall ransomware landscape, sharing our internal tracking data
for all known ransomware groups active for each quarter. Thank-
fully, there is good news across the board regarding the numbers.
We observed a continuing decline in ransomware detections across
all active endpoints and ransomware group double extortions also
decreased. For EPDR-protected endpoints, we observed a 23.37%
reduction in detections. However, ransomware detections remain
relatively elevated, and there is still much work cybersecurity
professionals need to do to ensure these attacks are less effective
and less frequent.

There are two likely explanations for the continuing decline in
ransomware detections across the board. The first is that it is likely
that ransomware attacks are being caught at the network level
before they even get to the endpoint. For example, many malware
attacks, including ransomware attacks, begin with a phishing
email. It’s likely that users or email filters are successfully detecting
these attacks before they can execute on the endpoint. The second
reason relates to human-operated ransomware (HumOR) and more
precise ransomware attack attempts. HumOR requires that the
threat actor manually deploys ransomware on a victim’s machine or
network. This means that modern ransomware attacks occur when

the threat actor has remote control of the machine and is actively
operating within a victim network. These attackers will likely get
caught before the ransomware deployment even takes place.
Hence the reduced overall numbers.

593

465

421

338

259

700

600

500

400

300

200

100

0

Q1

Q2

Q3

Q4

Q1

Extortion Groups
The WatchGuard ransomware detections and extortion group
numbers typically follow the same pattern. As discussed, the
WatchGuard QoQ detections declined, as did the number of
observed double extortions. So, that trend continues. Summing
up all of the known double extortions this quarter, we ended up
counting 1,124 across all of the known ransomware groups we
track internally and on our Ransomware Tracker. That is 13.87% less
than Q1 2023. This means there have been three straight quarterly
declines, peaking at 1,531 in the last few quarters.

Q1 2024 Internet Security Report Endpoint Threat Trends37Figure 44. Exploits by MITRE ATT&CK® Tactics Summation Figure 45. 2023-2024 QoQ Ransomware Detections by Quarter1531

1432

1305

1124

1800

1600

1400

1200

1000

800

600

400

200

0

862

Q1

Q2

Q3

Q4

Q1

So, who were the groups behind these numbers? As usual, we
begin by mentioning the new ransomware operations that began
in Q1:

New Groups:

•  AlphaLocker
•  APT73
•  dAn0n
•  DarkVault
•  Dispossessor
•  DoNex
•  Handala
•  Kill Security
•  NO-NAME
•  RansomHub
•  Red
•  Slug
•  Trisec

What’s interesting about the new groups this quarter is that three
directly copied LockBit 3.0’s data leak site (DLS) and used it as their
own – DarkVault, Dispossessor, and NO-NAME. Another group, Red,
also mimicked LockBit’s DLS, but it wasn’t a direct mirror. These four
groups combined for 53 double extortions this quarter, or a little
under 5% of all extortions.

The other notable ransomware operations are Handala, Ransom-
Hub, and Slug. Handala is a hacktivist group that began wiping
operations after the October 7 attacks in Israel. They started a
Telegram page that posted all of their actions, including doxing
and wiping operations, with associated screenshots. RansomHub
has been the most active of the new groups since its inception, and
they are possibly the most cause for concern. On the other hand,
Slug posted one victim on their DLS, a large Aviation organiza-
tion headquartered in Ireland. Then, they appear to have halted
operations.

Groups with increases
from Q3 to Q4

Groups with decreases
from Q3 to Q4

Abyss (+8)

Akira (+10)

0mega (-1)

8base (-9)

BianLian (+15)

Arvin Club (-6)

Black Basta (+13)

ALPHV (-39)

Blacksuit (+6)

Cactus (+15)

Cl0p (+2)

Everest (+4)

Hunters Internation-

al (+38)

Arvin Club (-7)

Cuba (-5)

DAIXIN (-3)

DragonForce (-10)

INC Ransom (-6)

Medusa Blog (+9)

Knight (-17)

Qilin (+16)

LockBit 3.0 (-45)

Ransom House (+2)

Lorenz (-7)

Stormous (+7)

Trigona (+12)

Malek Team (-5)

Mallox (-1)

MedusaLocker (-4)

Meow Leaks (-6)

Metaencryptor (-4)

Money Message (-3)

Monti (-5)

NoEscape (-58)

Play (-58)

RA Group (-3)

Ragnar Locker (-5)

RansomExx2 (-3)

Raznatovic (-14)

Rhysida (-15)

Snatch (-6)

Toufan (-116)

Werewolves (-8)

Q1 2024 Internet Security Report Endpoint Threat Trends38Figure 46. Ransomware Detections by QuarterFigure 47. Increases and Decreases from Quarter PriorThe most significant decrease from Q4 to Q1 was Toufan, a group
similar to Handala that performed most of their actions against
Israel. The steep decline was due to a self-defined 30 days of
hacking in Q4. Thus, in Q1, those actions ceased, hence the large
decrease. As for increases, the largest QoQ increase was Hunters
International, which is believed to be the successor to Hive ransom-
ware. Hopefully, Hunter’s International will have lower numbers in
Q2, along with all other groups, and we continue to see a decline in
ransomware detections. For now, we end the endpoint section with
notable alleged ransomware breaches from the quarter.

As for the returning groups from Q4, we’re encouraged to see more
groups with decreasing trends than those with increases. Of course,
this makes sense, considering the double extortion numbers
were down. What’s most surprising is that LockBit 3.0 significantly
decreased due to Operation Cronos. This operation, led by the
United Kingdom’s National Crime Agency (NCA), in coordination
with several other Europol countries, disrupted LockBit’s operation
and brought down their DLS momentarily. Unfortunately, LockBit
continued operations shortly after that using different Onion
domains.

Another group with an operational disruption was ALPHV, more
commonly called Black Cat. Law enforcement didn’t take down
their infrastructure. Instead, the ALPHV group exit-scammed after
an affiliate ransomed Change Healthcare, part of UnitedHealth. This
breach eventually made it to the United States Senate. During that
hearing, and by public reporting, that breach cost the company
around 1.5 billion dollars in damages and recovery efforts. Part of
that amount was a $22 million ransom payment to the hackers, as
admitted by the CEO.

0 M E G A
8 B A S E
A BY S S
A K I R A
A L P H A L O C K E R
A P T 7 3
B I A N L I A N
B L A C K   B A S TA
B L A C K BY T E
B L A C KC AT   ( A L P H V )
B L A C K S U I T
C A C T U S
C I P H B I T
C L O A K
C L O P
C U B A
D A N 0 N
D A R K VA U LT
D I S P O S S E S S O R
D O N E X
D O N U T   L E A K S
D R A G O N F O R C E
D U N G H I L L   L E A K
E V E R E S T
H A N D A L A
H U N T E R S   I N T E R N AT I O N A L
I N C   R A N S O M
K I L L   S E C U R I T Y
K N I G H T
L O C K B I T   3 . 0
M A L E K   T E A M
M A L L OX
M E D U S A   B L O G
M E O W   L E A K S
M O N E Y   M E S S A G E
M O N T I
N O - N A M E
P L AY
Q I L I N
R A   G R O U P
R A N S O M   H O U S E
R A N S O M E X X 2
R A N S O M H U B
R E D
R H Y S I D A
S L U G
S N AT C H
S TO R M O U S
T H R E E A M
T R I G O N A
T R I S E C
U N S A F E
W E R E W O LV E S

1

1

1

2

2
3

9
9

8

5

3

1

5

3

8

1

3

1

4

1

1

9

9
9

9

3
2
3

0

14

11

18

21

12

22

26

69

59

72

54

56

47

60

52

12

31

66

22

12
11

12

15

19

217

50

100

150

200

250

Q1 2024 Internet Security Report Endpoint Threat Trends39Figure 48. Q1 2024 Public Extortions by GroupNotable Ransomware Breaches
ALPHV
Change Healthcare – Toward the end of February, Change Health-
care experienced a ransomware attack from an affiliate of ALPHV.
This quickly made the news because patients could not get their
prescriptions and services on time. Furthermore, Change Health-
care is a UnitedHealth subsidiary that affects many Americans. The
CEO confirmed they paid a $22 million ransom to ALPHV. At that
point, ALPHV exit-scammed the affiliate and hasn’t been seen since.
Change Healthcare was left with an estimated 1.5 billion dollar bill
from the ordeal.

Prudential Financial – On February 12, 2024, Prudential Financial
($PRU) filed a Form 8-K reporting a cybersecurity incident on
February 4, 2024. Shortly after that, the ALPHV group took respon-
sibility for the attack. It’s apparent that those two events are likely
related. Around the same time, the group also claimed to have data
from LoanDepot. This was likely one affiliate who was targeting
the financial sector and happened to possibly have some success.
Thankfully, ALPHV no longer exists as an active ransomware group.

Backmydata (Phobos)

Hipocrate Information Systems (HIS) – Hospitals in Romania
experienced a massive ransomware attack that encrypted critical
systems nationwide. It was arguably the most tangibly destructive
attack of the quarter. Around a couple dozen hospitals were
affected, and many more were disconnected from the Internet as a
precautionary measure. The threat actors, reportedly an unknown
group called Backmydata, using a Phobos ransomware derivative,
asked for little – only a few bitcoins.

LockBit 3.0

Fulton County, GA – This ransomware-related breach is notable
because it has political connotations. Fulton County, Georgia, is
in the spotlight because of the racketeering case against former
president Donald Trump. So, when LockBit posted this entry on
their DLS, suspicions arose about whether this breach was polit-
ically motivated or if some of the data possibly exfiltrated by the
group contained sensitive information related to the case. As of this
writing, we don’t have evidence that LockBit obtained information
about that case.

Subway – This attack is notable for a few reasons. The first is that
Subway is a big name, has a lot of revenue, and employs many
people. Thus, any ransomware attack on this organization is some-
what notable. Second, this was one of the first victims listed on
LockBit’s refreshed DLS after Operation Cronos, making it naturally
suspicious. It was believed that this was an attempt to save face.
However, after they were listed, not much came about regarding
news or remediation efforts from Subway. Who knows if the claims
are legitimate.

Medusa Blog

Water for People – Seemingly, there is a ransomware attack or
breach once every quarter that targets the organizations hosting
or helping the most vulnerable in the population. Unfortunately,
this is such an attack. Water for People provides drinking water to
water-scarce regions for those in need in nine countries – Bolivia,
Guatemala, Honduras, India, Malawi, Peru, Rwanda, Tanzania, and
Uganda. The group behind the Medusa Blog not only encrypted
and exfiltrated their systems but then demanded $300k as extor-
tion for the data.

RansomExx2

Kenya Airways – One of the first detected victims listed on a DLS
for Q1 was Kenya Airways, but that’s not why it’s notable. It’s
notable for its name and responsibilities for the safety of thousands
of people a year. It’s also notable because the operators behind
RansomExx claim to have stolen information on passengers and
accident reports. This type of information could lead to further
damage to the company. That is, if the information is legitimate.

Unknown
Integris Health – INTEGRIS Health is a not-for-profit medical group
located in Oklahoma. On Christmas Eve, the organization had to
take the unfortunate step of notifying patients that threat actors
compromised their data in a cyber incident occurring in November.
They claimed that patient data was in the bundle of compromised
data and included name, date of birth, contact information,
demographic information, and social security numbers. The com-
promised data differed from patient to patient. At the beginning of
2024, class action lawsuits began to arrive and are still ongoing. It is
unknown which threat actors were responsible for this attack.

In summary, Q1 was a change from the norm in terms of malware
frequency. We observed a surge in total malware threats, specifical-
ly those caught by EPDR’s first line of defense. Many of these repeat
malware samples continue to be Glupteba, GuLoader, Formbook,
and Agent Tesla. Our data shows that these malicious loaders
and information stealers are continuously delivered via phishing
email attachments. This quarter, we specifically saw a rise in Excel
attachments. It is paramount to not only perform phishing training
and become familiar with the latest phishing tactics but also to use
your gut instincts and common sense not to interact with unsolic-
ited attachments. Thankfully, EPDR has multiple layers of detection
and prevention to atone for such mistakes.

Q1 2024 Internet Security Report Endpoint Threat Trends40CONCLUSION
& DEFENSE
HIGHLIGHTS

Q1 2024 Internet Security Report41CONCLUSION AND
DEFENSE HIGHLIGHTS

Hopefully, you have found all the threat intelligence we gathered for Q1 2024 insightful.

While we saw network decreases in malware, they were mirrored by endpoint increases of malware, which evens everything out to about the
same amount of malware volume as ever. Interestingly, signature-based detection found many more threats this quarter than the more proac-
tive malware detection services, yet we still see that 64% of malware arriving over encrypted connections requires the proactive detection to
block.

Network attacks have increased in volume but decreased in diversity. Headline-making vulnerabilities, like ProxyLogon, continue to remain
popular, but we also see attackers targeting older niche vulnerabilities in Linux services like HAProxy.

At the endpoint, attackers leverage Office files, especially Excel ones, to sneak malware onto our users’ computers.

Protect and update your hardware
(smart TVs) too
Hopefully, you already have a consistent routine for patching your
traditional computer software. If not, know that WatchGuard’s
EPDR product has a great patch management module. Patching
software is critically important to preventing network attacks, as
the continued prevalence of the ProxyLogon exploit illustrates.
However, you cannot forget to patch your hardware either. IT
sometimes forgets hardware that have racked up in LAN rooms
or hung in meeting rooms, but the firmware those devices run
is still software and likely contains many of the same operating
systems and open-source packages as normal computers do. If
they are unprotected, they can succumb to cyberattacks just as
easily as a normal computer – sometimes even easier. This quarter
we found evidence of threat actors continuing to target smart
TVs with the PandoraSpear botnet. You should make sure that
all your IoT devices, including that benign-looking TV hanging in
your meeting room, has good defenses. Update its firmware so
it doesn’t suffer from any known vulnerabilities. Segment it from
the rest of your trusted network, so it can’t cross-contaminate any
computers containing critical data. Finally, if you segment it, make
sure the gateway security device (like a Firebox) is applying all our
security scanning services to that segment, so that they can block
any network attacks or malware to protect that hardware. In short,
remember that your IoT hardware requires the same defenses as
your traditional computers and servers do.

Train your users about the danger from
unsolicited Office documents.
This quarter we added data about the most common types of
Office documents to deliver malware. While all Office documents
– Word, PowerPoint, and Excel – can be booby-trapped to help
deliver malware, it turns out malicious Excel documents are the
most common type to contain malware. If you use the right protec-
tions, including endpoint protection products like EPDR, or even
advanced network malware detection services like APT Blocker,
they should detect and prevent malicious Office documents
from making it to your users. However, nothing is perfect. Some
malicious document will bypass your defenses. It is important to
specifically train your users that Office documents can be danger-
ous. While the majority of computer users, even consumers, might
realize emailed files like executables are risky, Office documents
do not have a similar bad reputation. In fact, in businesses Office
documents are the exact thing your employees would share with
one another to collaborate. This means users are likely less aware
that Office documents can be risky. Be sure to disabuse your users
of that misconception. Threat actors commonly use Office docu-
ments as a malware delivery vector. Train your users of the proper
Office document handling practices. First, never immediately trust
an unsolicited Office document, even if it comes from someone
you know. Attackers can sometimes masquerade as others. Rather,
if you don’t expect the document already, ask that coworker about
it first, preferably through another channel. That way you verify an
attacker isn’t pretending to be them. Second, never handle Office
documents from outside sources you don’t know, without heavy
scanning and validation. While you might be able to trust the
people you think you know, you can’t trust a random document at
all. If you do decide to open an Office document, which you should
only consider after heavy scanning and validation, avoid enabling
any special features. Office documents like Excel files might ask
you to enable macros, or “enable content.” Doing so also enables
some dynamic Office features that may also help attackers install
malware. You should only ever allow those options if you are 100%
sure you are dealing with a valid, internal document that requires
the features to work.

Q1 2024 Internet Security Report42Defend against botnets!
During Q1, we found evidence of many different botnets, including
Miori, DarkGate, and PandoraSpear. Obviously, the swiss army
knife functionality of botnet trojans are a draw to threat actors
who can leverage their zombie-machine army for anything from
distributed denial of service attacks, spamming, or just installing
additional malware payloads. Obviously, you should already have
a layer of defenses to try to keep botnets from infecting you at all.
Firewalls, layers of network and endpoint anti-malware services,
and intrusion prevention services can all prevent some of the many
different tactics attackers use to get a botnet into your network.
However, you should also deploy security controls and strategies
that help prevent a botnet from doing its dirty work even if it does
infect one of your computers. Security appliances like the Firebox
often have botnet command and control (C2) blocking services.
If enabled, these can prevent botnets that have infected you
from calling home; and if they can’t call home, they can’t receive

additional malicious instructions. You should also configure “egress”
filtering on your firewall (specifically your Firebox). Most admins
spend a lot of time setting up rules for traffic that can’t come into
your network (ingress filtering). You should spend equal time
configuring rules for the minimal traffic you want to go out (egress
filtering), rather than allowing ALL traffic out. If you limit the types
of traffic that leave your network to just what you expect, you may
inadvertently block the C2 channel some botnets use. Two of the
three botnets we mentioned target IoT devices, so be sure to also
refer to the hardware protection advice above. And finally, segment
your network by trust. If you take a “zero trust” approach internally
and make sure your most critical devices are segmented from IoT
or less trusted computers, that will lessen the diameter of collateral
damage if a botnet does infect one of your computers. Botnets
often try to scan internally once they infect a victim, in order to
find new victims. Network segmentation might prevent or limit the
radius of that scan.

That’s it for our Q1 2024 Internet Security report. We hope you found some of these trends and attack details enlightening and have been
inspired to update your defenses, or at least monitor your security logs and policies for any issues. Be sure to come back next quarter to keep up
with the latest changes in the threat landscape. As always, leave your comments or feedback about our report at
SecurityReport@watchguard.com, and keep frosty online!

Q1 2024 Internet Security Report43COREY NACHREINER
Chief Security Officer
Recognized as a thought leader in IT security, Corey spearheads WatchGuard’s security vision. Corey has operated at the frontline of cybersecurity for 22
years, evaluating and making accurate predictions about information security trends. Corey has the expertise to dissect complex security topics, making
him a sought-after speaker at forums such as Gartner, Infosec and RSA. He is also a regular contributor to leading publications including CNET, Dark Reading,
Forbes, Help Net Security, and more. Find him on www.secplicity.org.

MARC LALIBERTE
Director of Security Operations
Specializing in network security technologies, Marc’s industry experience allows him to conduct meaningful information security research and educate
audiences on the latest cybersecurity trends and best practices. With speaking appearances at IT conferences and regular contributions to online IT and
security publications, Marc is a security expert who enjoys providing unique insights and guidance to all levels of IT personnel.

TREVOR COLLINS
Information Security Analyst
Trevor Collins is a information security analyst at WatchGuard Technologies, specializing in network and wireless security. Trevor earned his security know-
how and several certifications through his past military experience in the United States Air Force. Trevor is a regular contributor to Secplicity.org where
he provides easily understood data analysis and commentary to IT professionals. Trevor’s experience with a wide range of network security vendors and
technologies allows him to provide unique perspectives to the industry.

RYAN ESTES
Intrusion Analyst
Ryan is an intrusion analyst at WatchGuard Technologies operating primarily within DNSWatch, WatchGuard’s DNS filtering and security service. For DNSWatch,
Ryan helps customers better understand potential threats to their organization using tailored domain analysis and threat intelligence. Outside of DNSWatch,
his research interests include web application security, Wi-Fi communications, and malware analysis. Ryan embraces a ‘never stop learning’ lifestyle allowing
him to stay on top of the latest cybersecurity and malware trends. In turn, Ryan passes this knowledge on to our customers and even shares certain topics on
his personal blog.

JOSH STUIFBERGEN
Intrusion Analyst
Josh is an intrusion analyst at WatchGuard Technologies operating primarily within DNSWatch, WatchGuard’s DNS filtering and security service. For DNSWatch,
Josh helps customers better understand potential threats to their organization using tailored domain analysis and threat intelligence. Josh’s multidisciplinary
background with a political science BA and cybersecurity BS offers an added perspective into the geopolitical nature of cybersecurity threats. Past experience
researching container security in Kubernetes deployments, and building a Zero-Trust Proof of Concept environment for small organizations contributes to his
insights on how organizations face the difficulties of increasingly complex managed environments. His role includes contributing to the Secplicity blog.

ABOUT WATCHGUARD THREAT LAB
WatchGuard’s Threat Lab is a group of dedicated threat researchers committed to discovering and studying the latest malware and Internet attacks. The Threat Lab team analyzes data from
WatchGuard’s Firebox Feed, internal and partner threat intelligence, and a research honeynet, to provide insightful analysis about the top threats on the Internet. Their smart, practical security
advice will enable you to better protect your organization in the ever-changing threat landscape.

ABOUT WATCHGUARD TECHNOLOGIES
WatchGuard® Technologies, Inc. is a global leader in unified cybersecurity. Our Unified Security Platform® approach is uniquely designed for managed service providers to deliver world-class
security that increases their business scale and velocity while also improving operational efficiency. Trusted by more than 17,000 security resellers and service providers to protect more than
250,000 customers, the company’s award-winning products and services span network security and intelligence, advanced endpoint protection, multi-factor authentication, and secure
Wi-Fi. Together, they offer five critical elements of a security platform: comprehensive security, shared knowledge, clarity & control, operational alignment, and automation. The company is
headquartered in Seattle, Washington, with offices throughout North America, Europe, Asia Pacific, and Latin America. To learn more, visit WatchGuard.com.

For additional information, promotions and updates, follow WatchGuard on Twitter @WatchGuard, on Facebook, and on the LinkedIn Company page. Also, visit our InfoSec blog, Secplicity, for
real-time information about the latest threats and how to cope with them at www.secplicity.org.

©2024 WatchGuard Technologies, Inc. All rights reserved.  WatchGuard and the WatchGuard logo, IntelligentAV, Fireware, DNSWatch, Unifed Security Platform and Firebox are trademarks or registered trade-
marks of WatchGuard Technologies, Inc. in the United States and/or other countries. All other tradenames are the property of their respective owners. Part No. WG_060324

Q1 2024 Internet Security Report44