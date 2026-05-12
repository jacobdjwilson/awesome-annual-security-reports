# 2023 SonicWall Cyber Threat Report

## Table of Contents
- [Introduction](#introduction)
- [A Note From Bob](#a-note-from-bob)
- [2022 Global Attack Trends](#2022-global-attack-trends)
- [Ransomware Down … But Not Out](#ransomware-down--but-not-out)
- [Top Data Breaches of 2022](#top-data-breaches-of-2022)
- [Ransomware Remains Top of Mind in 2022](#ransomware-remains-top-of-mind-in-2022)
- [CVEs](#cves)
- [Published CVEs Break 25,000 for First Time](#published-cves-break-25000-for-first-time)
- [Log4j](#log4j)
- [Log4j Intrusion Attempts Surpass 1 Billion](#log4j-intrusion-attempts-surpass-1-billion)
- [Ukraine](#ukraine)
- [Ukraine Sees Unprecedented Attack Volume in 2022](#ukraine-sees-unprecedented-attack-volume-in-2022)
- [Capture ATP & RTDMI](#capture-atp--rtdmi)
- [RTDMI Detections Continue to Rise](#rtdmi-detections-continue-to-rise)
- [Cryptojacking](#cryptojacking)
- [Cryptojacking Continues Record-Breaking Run](#cryptojacking-continues-record-breaking-run)
- [Encrypted Attacks](#encrypted-attacks)
- [Encrypted Attacks Fall 28%](#encrypted-attacks-fall-28)
- [Intrusion Attempts](#intrusion-attempts)
- [Overall Intrusion Attempts Up](#overall-intrusion-attempts-up)
- [Malicious PDF/Office Files](#malicious-pdfoffice-files)
- [Malicious PDFs Up by More than a Third](#malicious-pdfs-up-by-more-than-a-third)
- [IoT Malware](#iot-malware)
- [IoT Malware Nearly Doubles](#iot-malware-nearly-doubles)
- [Breach and Attack Simulation](#breach-and-attack-simulation)
- [Cybercriminals Shifting from Cobalt Strike to Sliver](#cybercriminals-shifting-from-cobalt-strike-to-sliver)
- [Non-Standard Ports](#non-standard-ports)
- [Non-Standard Port Attacks Defy Expectations](#non-standard-port-attacks-defy-expectations)
- [Key Findings from 2022](#key-findings-from-2022)
- [Malware](#malware)
- [Malware Up for the First Time Since 2018](#malware-up-for-the-first-time-since-2018)
- [Ransomware](#ransomware)
- [Ransomware Reverses Course](#ransomware-reverses-course)
- [Phishing](#phishing)
- [Health and Finances Top Phishing Topics for 2022](#health-and-finances-top-phishing-topics-for-2022)
- [Conclusion](#conclusion)
- [The Next Step is Up to You](#the-next-step-is-up-to-you)
- [About the SonicWall Capture Labs Threat Network](#about-the-sonicwall-capture-labs-threat-network)

---

# INTRODUCTION

## A NOTE FROM BOB

This marks our 11th year of publishing the annual SonicWall Cyber Threat Report. Over the last 30-plus years, we’ve deployed millions of firewalls and endpoints globally. To this day, SonicWall has more than 1.1 million active sensors that report threat information multiple times a day, providing us with rich sets of threat data. This threat intelligence contributes to our strong security efficacy, but also highlights key real-time trends in the market.

Over the past year, cybercriminals faced with increasing media attention, heightened awareness and intensifying law-enforcement pressure began shifting away from established hotspots to new areas. As a result, organizations already dealing with macroeconomic pressures, supply-chain challenges and continued geopolitical strife often found themselves confronted with a cyberattack.

2022 reinforced the need for cybersecurity in every industry, and every facet of business, as threat actors targeted anything and everything. For instance, while the retail and finance industries typically see lower cyberattack volume compared with other industries, in 2022 both verticals experienced double-digit increases in malware, including triple-digit increases in IoT malware attacks and cryptojacking.

These trends were compounded by the fact that new tactics are being developed with breathtaking speed. 2022 brought growth in pure extortion attacks, the fall of ‘Big Ransomware,’ widespread expansion to Linux and cloud targets, the adoption of powerful new languages and platforms, and the growing specter of AI and quantum attacks.

In this volatile threat environment, preparation is more critical than ever before. And today, being prepared means more than just deploying the most advanced solutions. It means developing comprehensive cybersecurity strategies, based on the most current threat intelligence available.

The 2023 SonicWall Cyber Threat Report is your guide to attackers’ rapidly evolving tactics. On behalf of our network of trusted partners and the entire SonicWall team, including our Capture Labs threat researchers, we’re pleased to share these key insights on cybercrime’s shifting frontlines, as well as the actionable threat intelligence you need to arm your organization against today’s ever-changing threat environment.

**Bob VanKirk**
President & CEO
SonicWall

---

# 2022 GLOBAL ATTACK TRENDS

![Infographic showing 2022 global attack trends including: 7.3 Million Encrypted Threats (+87%), 493.3 Million Ransomware Attacks (-21%), 5.5 Billion Malware Attacks (+2%), 6.3 Trillion Intrusion Attempts (+19%), 139.3 Million Cryptojacking Attacks (+43%), and 112.3 Million IoT Malware (-28%).]

*As a best practice, SonicWall routinely optimizes its methodologies for data collection, analysis and reporting. This includes improvements to data cleansing, changes in data sources and consolidation of threat feeds. Figures published in previous reports may have been adjusted across different time periods, regions or industries.*

While the past several years have given the cybersecurity world plenty to worry about, there have nonetheless been a few things we could count on. Malware was falling. Ransomware was rising. And attackers continued to prioritize targets in the U.S.

But from start to finish, 2022 was characterized by change. Ushered in by the announcement of the historic Log4j vulnerabilities just weeks before, the year brought a seismic shift in cybercriminal behavior that sent ripples across every region and every industry.

---

# Ransomware Down … But Not Out

For the past two years, ransomware has been on a tear, increasing 62% year over year in 2020 and another 105% in 2021. During this time, Ransomware-as-a-Service (RaaS) took off, compromised credentials became cheaper and more plentiful than ever, and the number of vulnerabilities continued hitting record highs.

But despite there being fewer barriers of entry for new threat actors than ever before, in 2022, SonicWall Capture Labs threat researchers observed a 21% drop in ransomware year over year. Other vendors have noted a similar decline, as have U.S. government agencies.

## As Goes Russia, So Goes Ransomware
In May, U.S. National Security Agency (NSA) Cybersecurity Director Rob Joyce remarked on the decreasing ransomware levels. “There’s probably a lot of different reasons why that is, but I think one impact is the fallout of Russia-Ukraine,” Joyce said.

With roughly two-thirds of state-sponsored cyberattacks coming from Russia, and 75% of money generated by ransomware in 2021 going to groups “highly likely to be affiliated with Russia,” anything affecting that country has an outsized effect on cybercriminals, and in turn, cybercrime.

According to Joyce, sanctions have made it harder for cybercriminals to move money and buy infrastructure needed for attacks, making cybercriminals less effective. But while becoming “less effective” should result in an even decrease across the board, what’s actually being observed are huge decreases in places that generally see the most ransomware — particularly the United States, where ransomware fell by nearly half.

## Ransomware or Bust
2021 was a banner year for ransomware busts. Cybercriminals associated with Netwalker, Egregor, Lockergoga, MegaCortex and the Trickbot malware were brought to heel amid a flurry of headlines, and when a 30-month investigation involving INTERPOL, South Korea, Ukraine and the U.S. resulted in the arrests of the Cl0p ransomware kingpins, it sent the message that the U.S. was no longer the safe profit center it once was.

But two bigger wake-up calls were yet to come. In January 2022, the Darkside members responsible for the Colonial Pipeline attack were arrested by Russian authorities. Then, in another rare (and no doubt politically motivated) show of cooperation with the U.S., Russian intelligence services arrested members of the infamous REvil gang the same week. Cybercriminals, who had been accustomed to acting with impunity, suddenly became aware that there were very few places left to hide.

In January 2022, a sampling of Dark Web cybercriminal chatter published by ZDNet revealed an undercurrent of fear running through the underworld. “This is a big change. I have no desire to go to jail,” one said in response to the REvil arrests. Another seemed to take them as a warning, saying that anybody who expected Russia to protect them would be “greatly disappointed.” Still others worried that Dark Web admins might reveal their identities to law enforcement.

But as the risk of attacking targets in the U.S. went up, the perceived payoff dropped. Mounting cyberinsurance requirements and the specter of mandatory reporting offered businesses even more motivation to harden defenses. And in 2022, the U.S. government created the Virtual Asset Exploitation Unit, increasing tracking and enforcement efforts against ransomware operators.

Faced with a risk/benefit analysis no longer working in their favor, some cybercriminals shifted targets, leading to double-digit ransomware increases in places like Europe and Asia. Still others are diversifying their tactics.

## Jack of All Trades
Unlike ransomware, which announces its presence, thrives on branding and notoriety, and relies heavily on direct contact with victims, cryptojacking can succeed in complete silence. And for some cybercriminals feeling the heat from increased enforcement efforts and ongoing geopolitical conflict, a consistent, lower-risk income stream may be worth sacrificing a potentially higher payday.

“[Cryptojacking] has a lower potential of being detected by the victim; unsuspecting users across the world see their devices get unaccountably slower, but it’s hard to tie it to criminal activity, much less point to the source,” Terry Greer-King, SonicWall Vice President for EMEA, told Tech Monitor.

---

# Top Data Breaches of 2022

| NAME | INDUSTRY | DATE | IMPACT |
| :--- | :--- | :--- | :--- |
| Philippines COMELEC | Government | January | 60 GB of data, including usernames and PINs for vote-counting machines |
| U.S. Department of Education | Government | January | 820,000 student records |
| Texas Dept. of Insurance | Government | January | 1.8 million records |
| Crypto.com | Finance | January | 500+ cryptocurrency wallets (more than $30M) |
| ICRC | Charity | January | 515,000 records |
| Flexbooker | Software | January | 3.7 million records |
| GiveSendGo | Fundraising | February | 90,000 records |
| Harbour Plaza Hotel Management | Hospitality | February | 1.2 million records |
| Credit Suisse | Finance | February | 18,000 Credit Suisse accounts |
| Nvidia | Technology | February | 71,000+ employee records |
| Microsoft | Software | March | Bing, Bing Maps & Cortana partial source code |
| Ronin Bridge Hack | Finance | March | $625 million in crypto |
| Pegasus Airlines | Travel | March | 6.5 TB of data, including source code, flight crew PII and passwords/secret keys |
| Morgan Stanley Clients | Finance | March | Unknown number of client accounts |
| Cash App | Finance | April | 8.2 million records |
| Elephant Insurance | Insurance | May | 2.7 million records |
| SuperVPN, GeckoVPN & ChatVPN | Technology | May | 21 million records |
| Cost Rican Government | Government | May | 670GB data |
| National Registration Dept. of Malaysia | Government | May | 22.5 million records |
| Alameda Health System | Healthcare | May | 90,000 records |
| Verizon | Telecommunications | June | Hundreds of employee records |
| Flagstar Bank | Finance | June | 1.5 million records |
| Shields Health Care Group | Healthcare | June | 2 million records |
| Choice Health Insurance | Healthcare | June | 600MB of data, including names, SSNs, and other PII |
| OpenSea | Finance | July | $1.7 million in NFTs |
| Neopets | Entertainment | July | 69 million records |
| Twitter | Social Media | July | 5.4 million accounts |
| Uber | Travel | July | 57 million records |
| OneTouchPoint | Marketing | August | 2.65 million records |
| Cisco | Technology | August | 2.75 GB of data, including engineering files and NDAs |
| Plex | Software | August | 20 million records |
| Okta | Technology | August | 169 domains |
| Nelnet Servicing | Finance | September | 2.5 million records |
| Optus | Telecommunications | September | 9.8 million records |
| Samsung | Technology | September | Unknown |
| North Face | Apparel | September | 200,000 records |
| Revolut | Finance | September | 50,150 records |
| Mydeal | Retail | October | 2.2 million records |
| Vinomofo | Food & Beverage | October | 500,000 records |
| Medibank | Healthcare | November | 9.7 million records |

---

# Ransomware Remains Top of Mind in 2022

While ransomware was on the decline in 2022, it was still ranked as the top threat in SonicWall’s inaugural Threat Mindset survey, released in August.

For this survey, SonicWall surveyed customers across a variety of industries located around the globe, asking a series of questions to evaluate the sentiments of those “on the ground” in the war on cybercrime.

When asked what types of cyberattack they’re most concerned about, 91% of respondents answered ransomware. Phishing and spear-phishing, which are often used as vectors for ransomware, were ranked second, with roughly three-quarters of respondents rating them as a concern.

> WHEN ASKED WHAT TYPES OF CYBERATTACK THEY’RE MOST CONCERNED ABOUT, 91% OF RESPONDENTS ANSWERED RANSOMWARE.

![Chart: Which types of cyberattacks are you most concerned about? Ransomware (91%), Phishing and spear-phishing (76%), Encrypted malware (66%), File-less attacks (39%), Memory-based malware (24%), Cryptojacking (23%), IoT malware (22%), Side-channel attacks (18%).]

---

# CVEs

## Published CVEs Break 25,000 for First Time

A total of 26,448 Common Vulnerabilities and Exposures (CVEs) were published in 2022, according to NIST. This marks the sixth year in a row that a record number of vulnerabilities has been discovered, and the first time in history that the number of CVEs has passed 25,000.

While this milestone represents the hard work those in the cybersecurity industry are doing to identify vulnerabilities more quickly and efficiently, it isn’t necessarily cause for celebration. It also reflects the pernicious trends that make quicker and more efficient work necessary in the first place.

As organizations deploy more software and tools, the attack surface continues to grow. And the more products a company utilizes, the more likely it is that one will be vulnerable. (A good example of this is the Apache Log4j vulnerabilities; see page 13)

The most severe vulnerabilities, the ones rated a nine or above on the 10-point scale, become entry points for cybercriminals, and attackers are increasingly utilizing this means of entry to deploy ransomware and other malware and to exfiltrate data.

![Chart: CVEs by Year. 2017: 14,714; 2018: 16,557; 2019: 17,344; 2020: 18,325; 2021: 20,171; 2022: 26,448.]

---

# LOG4J

## Log4j Intrusion Attempts Surpass 1 Billion

It’s now been more than a year since the announcement of the Apache Log4j vulnerabilities sent shockwaves through the tech community. Since December 2021, SonicWall Capture Labs threat researchers have been tracking attempted exploits of this vulnerability, and so far, attack volumes show no signs of slowing.

SonicWall logged a total of 1.12 billion intrusion attempts against the Log4j vulnerabilities in 2022. While some had hoped for an initial frenzy of attacks followed by a gradual decrease, our researchers have observed the opposite: 61.9 million attempts were observed in December 2021, the month the attacks were announced — and every month in 2022 exceeded that total by at least 10 million.

Worse, these attempts seemed to pick up steam as 2022 went on: The second half of the year had 15% more intrusion attempts than the first half.

![Chart: Malicious Log4Shell Exploit Attempts showing a steady rise throughout 2022.]

---

# UKRAINE

## Ukraine Sees Unprecedented Attack Volume in 2022

While the Russia-Ukraine conflict may have resulted in suppressed ransomware attack volume in the rest of the world, it had a dark side: It sent attack levels through the roof in Ukraine, as cyber warfare zeroed in on both military targets and critical civilian and communication infrastructure.

Because SonicWall requires a minimum of 1,000 active sensors in a region for public reporting, and our footprint in Ukraine falls far short of that threshold, we don’t generally report on cybercrime in Ukraine. But amid the ongoing conflict, the sensors we do have there recorded an enormous amount of malicious activity.

Despite Ukraine’s relatively small number of sensors, the country appears high in the rankings when compared with other nations. With 7.1 million attacks in 2022, Ukraine ranks No. 13 in total ransomware volume, and also had the third-highest ransomware spread percentage at 2.23%.

These numbers were fueled by a massive 8,105% increase in total malware and a 5,835% increase in ransomware.

---

# BREACH AND ATTACK SIMULATION

## Cybercriminals Shifting from Cobalt Strike to Sliver

The practice of using legitimate system administration, forensic or security tools to conduct cyberattacks has become so ubiquitous that it even has a name: “Living off the Land (LotL) attacks.”

This method is attractive because the necessary tools are already deployed and available for threat actors, allowing them to operate without raising suspicion. And because they’re legitimate tools/binaries/scripts, they’re significantly less likely to be flagged as malicious by anti-malware solutions.

In a similar fashion, threat actors have increasingly utilized legitimate offensive security tools such as Cobalt Strike, a commercial penetration testing tool that allows security teams to replicate the tactics and techniques of advanced adversaries in a network. Over the past several years, the abuse of Cobalt Strike has skyrocketed, increasing by 161% between 2019 and 2020 alone.

But Cobalt Strike has several strikes against it. Due to its widespread adoption and use in high-profile attacks such as SolarWinds, there’s been an increased focus on detecting and mitigating attacks using the tool.

Ever on the lookout for better ways to evade cyber defenses, attackers have recently begun to supplement or replace Cobalt Strike with a similar (but more obscure) tool, known as Sliver, in their attacks.

---

# Key Findings from 2022

- **Malware**: Malware rose for the first time since 2018, reaching 5.5 billion attacks — a 2% increase year over year. Skyrocketing cryptojacking and IoT malware rates fueled much of this jump.
- **Ransomware**: On the heels of 2021’s meteoric highs, ransomware fell in 2022, with volumes dipping to 493.3 million. While this represents a 21% year-over-year decrease, it’s still far above the levels seen in 2017, 2018, 2019 or 2020.
- **RTDMI Discoveries**: SonicWall’s patented Real-Time Deep Memory Inspection™ discovered 465,501 never-before-seen malware variants in 2022. This new high-water mark pushed the all-time detection total past the 1 million mark.
- **Cryptojacking**: As cybercriminals shifted to lower-profile revenue sources in 2022, the number of cryptojacking attempts rose to a record high of 139.3 million.
- **IoT Malware**: With the number of connected devices continuing to rise, IoT malware jumped 87% year over year to a new high of 112.3 million.
- **Intrusions**: The number of overall intrusion attempts in 2022 hit 6.3 trillion, a 19% increase over 2021’s total. Fortunately, however, the number of malicious intrusions fell 10%.
- **Malicious PDF and Office Files**: SonicWall Capture Advanced Threat Protection (ATP) sandbox recorded a 35% increase in the number of new PDF-based attacks in 2022. These attacks now make up 19% of total malicious files identified by Capture ATP.
- **Phishing**: Phishing decreased 17% globally in 2022, with Financial/Mortgage, Cryptocurrency, Healthcare and Pandemic the top themes for malicious emails.
- **Encrypted Attacks**: Encrypted attacks fell 28% year-over-year to 7.3 million, down from 10.1 million in 2021.

---

# MALWARE

## Malware Up for the First Time Since 2018

After three straight years of decline, malware reversed course in 2022, rising to 5.5 billion hits — a 2% increase year over year. While the increase is small, it’s being fueled by massive growth in two areas. In 2022, cryptojacking rose 43% and IoT malware jumped 87%. Together, these increases were more than enough to offset a 21% drop in global ransomware volume, pushing overall malware trends into positive territory for the first time since 2018.

While the increase is small, it’s being fueled by massive growth in two areas. In 2022, cryptojacking rose 43% and IoT malware jumped 87%. Together, these increases were more than enough to offset a 21% drop in global ransomware volume, pushing overall malware trends into positive territory for the first time since 2018.

---

# CONCLUSION

## The Next Step is Up to You

The 2023 SonicWall Cyber Threat Report highlights a year of transition. While ransomware volume has dipped, the threat landscape remains as volatile as ever. Cybercriminals are not disappearing; they are evolving, shifting their tactics, and finding new ways to exploit vulnerabilities and target organizations.

The rise in cryptojacking, the persistence of Log4j, and the shift toward extortion-based attacks demonstrate that the threat environment is constantly changing. Organizations must remain vigilant, prioritize cybersecurity, and adopt a proactive approach to defense.

The next step is up to you. By leveraging the insights provided in this report and implementing robust security strategies, you can better protect your organization against the ever-evolving threat landscape.

---

# About the SonicWall Capture Labs Threat Network

SonicWall Capture Labs threat researchers collect, analyze and vet cross-vector threat information from the SonicWall Capture Threat Network, which consists of global devices and resources, including:

- More than 1.1 million security sensors in over 215 countries and territories.
- Cross-vector threat telemetry from firewalls, email security, endpoint security, cloud security and mobile security solutions.
- Honeypots and remote sandboxing.
- Internal and external research projects.

This data is used to provide actionable intelligence to our customers, partners and the broader cybersecurity community, helping to defend against the latest threats and vulnerabilities.

---

re

21.4% in 2021, to 18.7% in 2022.

spread: Rhode Island.)

Conversely, Texas was the lowest: only 12.7% of sensors

there logged a malware attempt.

2022 Brings Surge in Wiper Malware

SonicWall in 2022 observed an uptick in so-called wiper

Another wiper targeting Ukrainian networks, CaddyWiper,

malware. In contrast with ransomware, intended to render files

was analyzed by SonicWall in March. This malware iterates

unusable until a ransom is paid, wiper malware is designed to

through files, including critical system files, and replaces their

“wipe” or render data unusable permanently.

contents with null bytes. Once the data is overwritten, the

In February, SonicWall Capture Labs threat research team

analyzed a sample believed to be targeting Ukrainian

physical drive is also overwritten with null bytes, rendering the

machine unbootable.

organizations. Known as HermeticWiper, the malware prevents

In October, SonicWall analyzed yet another wiper, this one a

Windows from recording any information in the memory dump

multicomponent infection purporting to be a picture. It arrives

file and disables the VSS (Volume Shadow Copy Service, which

as a file titled “SexyPhotos.jpg,” but is actually a self-extracting

is used to back up application data). Finally, it corrupts the first

archive. While a ransom note is displayed, the malware only

512 bytes, the Master Boot Record (MBR) for every physical

gives the appearance of encrypting files — instead, it’s

drive. It then initiates a reboot and, once completed, the

intended to delete all data on a given drive.

missing OS prompt is displayed, leaving the system unusable.

31     |     2023 SonicWall Cyber Threat Report     |     Malware

Malware by Industry
Malware targeting those in the healthcare industry fell 15%

year over year, while government customers saw an even

larger drop of 58%. Retail and finance, on the other hand,

experienced double-digit increases, with overall malware

attack volume rising 50% and 86%, respectively.

The largest increase, however, was in education, where

malware volume jumped 157%. But this is actually the

average of two outcomes: Attacks targeting higher

education customers rose a (relatively) modest 26%, while

attacks targeting K-12 institutions skyrocketed 323%.

When it comes to the average percentage of customers

targeted by malware in 2022, every industry we studied

showed a decrease from 2021’s average. The percentage

of healthcare customers targeted in 2022 slightly edged

out the percentage of retail customers targeted, but the

rankings remained otherwise unchanged.

Malware Attack
Volumes by Industry

2021

2022

  1.  Government

  1.  Education

  2.  Healthcare

  2.  Healthcare

  3.  Education

  3.  Finance

  4.  Retail

  5.  Finance

  4.  Retail

  5.  Government

% of Customers Targeted by Malware in 2022

40

35

30

25

20

15

10

5

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

Finance

www.sonicwall.com

32     |     2023 SonicWall Cyber Threat Report     |     Malware

RANSOMWARE

Ransomware Reverses Course

2022 brought a bit of a reprieve from 2021’s sky-high

This is especially concerning because ransomware in 2022

ransomware volumes. In 2022, SonicWall Capture Labs

wasn’t that low to begin with. Despite dropping by a little

threat researchers recorded 493.3 million ransomware

more than a fifth, 2022 was still the second-highest year on

attempts, down 21% year-over-year.

record for ransomware attacks globally. And it’s far closer to

Unfortunately, however, we’re already seeing signs of a

potential reversal. After ransomware bottomed out in

June, bringing the lowest attack volume we’d seen since

July 2020, the trend line began reversing. When attacks

doubled between September and October, it pushed Q4

ransomware totals to 154.9 million — the highest quarter

we’ve seen since Q3 2021.

the stratospheric volumes we saw in 2021 than it is to prior

years, outpacing 2017 (+155%), 2018 (+127%), 2019 (+150%),

and 2020 (+54%) by significant margins.

Global Ransomware Volume by Year

600M

400M

200M

0

,

0
0
0
0
0
6
3
8
1
2017

,

,

0
0
0
0
0
4
6
0
2
2018

,

,

3
5
0
9
0
9
7
8
1
2019

,

,

7
8
9
8
3
6
4
0
3
2020

,

,

7
7
8
4
5
2
3
2
6
2021

,

,

1
5
1
7
2
3
3
9
4
2022

,

www.sonicwall.com

33     |     2023 SonicWall Cyber Threat Report     |     Ransomware

,

8
3
6
4
2
6
9
5

,

,

7
1
8
8
5
7
1
6

,

,

6
8
1
2
6
3
8
7

,

,

6
4
3
3
9
8
4
0
1

,

,

4
9
9
2
9
7
5
1
1

,

,

0
8
5
2
0
9
8
8
1

,

,

0
8
4
2
6
0
5
8
1

,

,

3
2
8
6
9
4
3
3
1

,

,

2
9
1
0
4
9
9
2
1

,

,

9
7
4
4
5
1
6
0
1

,

,

3
0
8
7
9
2
2
0
1

,

,

7
7
6
4
3
9
4
5
1

,

Global Ransomware Volume

www.sonicwall.com

80M

60M

40M

20M

0

,

3
8
6
7
6
1
3
4

,

,

3
7
5
9
5
0
8
4

,

,

6
9
9
4
6
3
6
3

,

,

1
6
6
0
9
3
5
4

,

,

5
1
3
0
6
2
6
3

,

,

8
5
9
9
8
4
6
3

,

,

3
4
2
1
1
0
8
4

,

,

4
2
1
7
7
0
9
3

,

,

7
9
3
4
8
4
2
6

,

,

6
1
2
3
4
2
3
4

,

,

0
4
9
6
0
4
8
7

,

,

9
3
1
4
3
8
3
2

,

,

7
5
0
1
6
6
5
4

,

,

5
9
3
2
7
2
5
3

,

,

2
6
3
7
5
0
7
6

,

,

6
7
2
0
5
8
0
3

,

,

1
6
0
4
4
3
2
7

,

,

2
3
1
5
7
1
6
3

,

,

9
3
4
5
9
7
6
4

,

,

1
2
0
5
3
2
6
7

,

,

1
8
2
0
4
6
7
3

,

,

4
8
8
6
1
1
3
5

,

,

3
0
1
1
6
0
9
4

,

,

2
7
7
2
8
5
5
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

Sept

Oct

Nov

Dec

2021

2022

www.sonicwall.com

34     |     2023 SonicWall Cyber Threat Report     |     Ransomware

Ransomware by Region

Earlier in this report, we mentioned that attackers were

Summer was also a turning point for attack volumes in

beginning to shift their crosshairs from the U.S. to targets

Asia, resulting in two very unbalanced halves. In the first six

in Europe and Asia. This turn in tactics brought double-digit

months of 2022, a total of 6.6 million ransomware attempts

change to both regions, with North America’s attack volumes

were recorded in Asia. In the second half this total jumped to

falling 48% year-over-year, and Europe’s volumes rising 83%.

10.7 million, fueling a year-over-year increase of 39%.

The inflection point for this change seems to have occurred

In LATAM, where ransomware attacks fell 33%

in mid-year: In May, ransomware volume in North America

year-over-year, 2022 brought uncharacteristic volatility.

fell below that of Europe for the first time since 2019. After

From Q1 to Q2, ransomware dropped 77%, then fell another

rebounding slightly, North America’s attack volumes dipped

83% from Q2 to Q3. But November brought ransomware

again in August, and remained below those of Europe for the

totals 12 times those observed in October, setting a new high

rest of the year.

While a large number of attacks early in the year kept North

America’s full-year total above that of Europe, at 222.6 million

versus 204.8 million, the two regions haven’t been this close

at any point in recent memory.

point for the year. But these gains were completely erased

in December, when total attacks fell a staggering 99% to by

far the lowest point seen all year. One possible explanation

for these highly erratic trends is that, while attackers seem

to be targeting LATAM less on average, there are still large

campaigns being run.

35     |     2023 SonicWall Cyber Threat Report     |     Ransomware

217,486,516

2022 Ransomware Volume | Top 10 Countries

United States

United Kingdom

Spain

Brazil

71,350,221

52,681,013

21,808,229

Germany

20,166,920

Colombia

15,519,964

y
r
t
n
u
o
C

Netherlands

13,636,729

Italy

12,471,704

Norway

8,355,138

Australia

7,621,554

20M

40M

60M

80M

100M

120M
Volume

140M

160M

180M

200M

220M

240M

Ransomware by Country

www.sonicwall.com

Despite a 48% year-over-year drop, the United States

One newcomer to this list was Spain: Last year, the country

once again saw the highest ransomware attack volume of

wasn’t even in the top 10 for ransomware volume, but 2022

any country in 2022 — but with a 112% jump, the U.K. is

brought a massive spike that propelled the country all the

beginning to catch up. In contrast, ransomware attacks in

way up to No. 3 on the list. And while India’s ransomware

Germany fell 42%, moving it from the second-highest attack

volumes still fall short of making the top 10, it also saw

volume to fifth.

a large jump in 2022, with ransomware volumes up 51%

year over year.

36     |     2023 SonicWall Cyber Threat Report     |     Ransomware

… But There’s a Catch

While overall attack volume was down in 2022, the attacks that

Perhaps most frightening, however, were the attacks on

did occur were often worse, for several reasons.

governments. On Nov. 15, Miller County, Ark., was hit by

a ransomware attack that spread through a mainframe,

ultimately affecting a total of 55 counties. While no data

was stolen, more than a week later many were still unable

to turn on their computers and relying on pen and paper

for daily operations. The disruption ultimately stretched

well into December.

But 2022 also proved that, should attackers ever set their

sights on disrupting governance at the national level, they

could potentially succeed. When Costa Rica was hit by

ransomware in April 2022, it marked the first time a country

had ever declared a national emergency in response to a

cyberattack. When the country refused to pay the outlandish

ransom demand, the country’s import and export logistics

collapsed, endangering scores of perishable items stored in

the tropical country’s cold storage.

While this attack is now believed to have been little more than

a diversionary tactic (see page 39), rather than a legitimate

attempt to destabilize a nation, it provides a terrifying

proof of concept for how successful such a ransomware

attack could be.

Due to better prevention and response techniques, the

percentage of people willing to pay a ransom continued to

drop in 2022. While this is a positive change, it’s put a squeeze

on ransomware operators’ profits. In an attempt to recoup

some of these losses, attackers responded by increasing

the amounts demanded, pushing the average ransomware

payment ever higher.

Even for the victims that paid these princely sums, the

nightmare often wasn’t over: Double extortion tactics

also increased in 2022, with one report showing a 120%

year-over-year spike in the number of victims facing

subsequent ransom demands.

More ruthless than how cybercriminals were attacking,

however, was who they were attacking. Despite PR messages

from some ransomware groups promising not to attack

hospitals and healthcare facilities, SonicWall found that these

ransomware attacks grew 8% year-over-year, often with

catastrophic effects.

In April, a healthcare conglomerate consisting of 65 hospitals

and 450 healthcare facilities across the U.S. experienced a

ransomware attack, incurring a staggering $100 million in lost

revenue and mitigation costs. That same month, a ransomware

attack on a medical center in Yuma, Ariz., resulted in the theft of

Social Security numbers, health insurance information, names

and medical information for more than 700,000 patients.

But while SonicWall observed an increase in attacks on

healthcare in 2022, it observed a significantly larger 275%

spike in attacks on education. While schools often don’t have

the money to pay the large ransoms demanded of them,

their networks contain a great deal of student data, which

cybercriminals can use to open credit cards or sell for a high

price on the dark web.

In one particularly egregious example, attackers took advantage

of the U.S.’s long Labor Day weekend to launch an attack on

the Los Angeles Unified School District (LAUSD), the second-

largest school system in the country. After LAUSD refused to

pay the ransom demand, the threat actors published 500GB of

stolen data including Social Security numbers, bank account

info, W-9 forms and sensitive student health information.

37     |     2023 SonicWall Cyber Threat Report     |     Ransomware

Ransomware by Industry

As with the regional and country data, the industry-specific

But this double-digit drop serves as a counterbalance to an

data also showed a huge variety in outcomes. Customers

absolutely massive increase in attacks on K-12 institutions

in government and the retail industry saw double-digit

and primary schools. Attacks on these schools rose

decreases in ransomware, with attack volumes falling 82%

827%, disproportionately impacting the world’s children

and 50%, respectively.

and educators.

But the other industries studied saw the opposite. With an

The per-customer data showed education customers once

8% year-over-year increase, healthcare saw the smallest

again inordinately affected by ransomware. In addition to

jump, but customers in finance (+41%) and education (+275%)

being the only industry studied to have a higher average

weren’t so lucky.

A 275% jump is bad enough on its own — but as we saw in

the malware data (see page 32), this number is actually the

confluence of disparate trends. Higher education customers

experienced a 29% decrease in ransomware, putting it

roughly in the middle on the list of industries we studied when

taken on its own.

percentage of customers targeted this year than last year,

ransomware attacks spiked in the second half — pushing

education to a distant first in terms of how many education

customers saw a ransomware attempt.

% of Customers Targeted by Ransomware in 2022

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

Finance

www.sonicwall.com

38     |     2023 SonicWall Cyber Threat Report     |     Ransomware

2022 Ransomware Trends

Is This the End for Big Ransomware?
While some ransomware groups were busy retraining their

crosshairs on new targets in 2022, others were reorganizing,

rebranding or simply going inactive. The DarkSide group

kicked off this trend when it publicly announced it was

disbanding amid an investigation into its attack on Colonial

Pipeline. But over the past year, we’ve seen the fall of

several other large ransomware groups, including PYSA,

Conti and REvil.

Following a spate of attacks on education institutions

in the U.K. and 12 U.S. states, the U.S. Cybersecurity &

Infrastructure Security Agency (CISA) released a warning

about the PYSA group in March 2021, but it did little to

slow the group’s growth: One report found that attacks

increased 50% between August and November 2021, at

times surpassing even Conti. But despite being one of the

top three ransomware groups in the final months of 2021, the

group appears to have stopped operating entirely sometime

in the first half of 2022.

Conti itself also disappeared in 2022 — but it chose to

burn out rather than fade away. In 2021, IC3 reported that

Conti was responsible for more ransomware attacks on

critical infrastructure than any other variant. The group

also conducted a number of attacks on high-profile targets,

such as Ireland’s health services and Japanese electronics

company JVCKenwood, demanding ransoms in the

millions of dollars.

But in 2022, amid the worsening Russia/Ukraine conflict,

Conti — reportedly based out of Russia — published a blog

vowing its “full support” for the Russian government. In

retaliation, an unknown pro-Ukrainian hacker gained access

to the group’s internal messaging server, then began leaking

nearly two years’ worth of private chats, laying bare virtually

every aspect of the group’s operation.

About a month and a half later, the group carried out its

highly publicized and disruptive ransomware attack on

the Costa Rican government. But despite a $10 million

dollar ransom demand, it’s now believed that the attack

wasn’t financially motivated — instead, it was intended as a

REvil also seems to have shut down in 2022, though its true

fate is uncertain. Four months after the arrest of group

leaders, the REvil’s TOR servers began operating again

— only this time, it sent visitors to a completely different-

looking site, ostensibly belonging to a new operation with

no discernible name. While it’s still unclear whether original

REvil members or hijackers are behind the new operation,

signs point to a rebrand, likely in an attempt to escape the

smokescreen, giving the group time to disband its operation

group’s notoriety.

and filter members into smaller, affiliated groups.

39     |     2023 SonicWall Cyber Threat Report     |     Ransomware

Attackers Continue Adopting Rust
While its use in malware isn’t new, 2022 brought an

Notable Ransomware Developments in 2022
SonicWall researchers took a closer look at several new

increase in the number of ransomware strains pivoting

trends and development in 2022. Here are a few of the

to Rust. This program language touts fast and memory-

most noteworthy:

efficient performance and a better user experience, as

well as guaranteed memory-safety and thread-safety for

JANUARY

greater stability.

ALPHV/BlackCat was the first major cybercrime group to

Jan. 14

Linux-Based Ransomware Found Targeting
VMWare ESXi Servers

adopt Rust for ransomware, and in July, the Hive ransomware

gang followed. Other strains observed using Rust include

FEBRUARY

Nevada, Agenda, Luna, Nokoyawa and RansomExx.

Intermittent Encryption Becoming
a RaaS Selling Point
Ransomware attacks have a high profit potential, but

it traditionally hasn’t been a quick process: It isn’t rare

for an attack to be spotted and stopped during the

encryption process.

However, a newer technique, known as intermittent

encryption, promises to make encryption faster while making

detection more difficult. Intermittent encryption works by

encrypting some parts of a file while skipping others. This

cuts the encryption time significantly, but still renders the

Feb. 4

Argos 2.0 Ransomware Threat Actor Gives Up
Decryption Key

Feb. 11

Ransomware Asking Victims To Subscribe To A
YouTube Channel

Feb. 25

Bitpylock Ransomware Leaves Decryption Key
Visible In Decompiled Code

MARCH

March 4

A Look At Partyticket Ransomware Targeting
Ukrainian Systems

March 25

Ransomware Not Asking For Payment But Asks
The Victim To Help The Needy

file unusable. Because less of each file is being encrypted,

the process also is less intensive, making it less likely to be

APRIL

flagged as malicious.

April 15

”Targetcompany” Ransomware

Speed advantages like this make strong selling points

for RaaS offerings. After Lockbit 2.0, which incorporates

JULY

intermittent encryption, was released, the LockBit group

published data showing its encryption speeds beat those of

its competitors. Not content to take cybercriminals at their

word, Splunk conducted its own speed tests, confirming

that LockBit was indeed fastest, and took only half

as long as Ryuk.

Perhaps uncoincidentally, in 2022 SonicWall observed

a 70.7% decrease in attacks using Ryuk, with total

July 13

Android Ransomware Purports To Be A Free Social
Media Follower Application

July 22

New Lilith Ransomware In Early Development

SEPTEMBER

Sept. 30

Clipboard Hijacker Dropped By Stop Ransomware

volume dropping from 180.4 million hits in 2021 to just 52

NOVEMBER

million a year later.

Nov. 11

Tor Chat With Black Basta Ransomware Operator
Runs Dry

DECEMBER

Dec. 16

Cryptonite Ransomware Leaves Files
Unrecoverable

40     |     2023 SonicWall Cyber Threat Report     |     Ransomware

2022’s Biggest Busts

2022 was another banner year for ransomware busts, as law

enforcement in the U.S., U.K., Canada, Brazil and even Russia

brought some of ransomware’s key players to justice:

January 14, 2022 – Based on intelligence provided by the

U.S., Russia announced that it had “dismantled” the REvil

ransomware gang. During the bust, Russian authorities seized

more than 426 million rubles in cash and cryptocurrency,

as well as luxury cars that had been purchased with

ransomware proceeds.

March 24, 2022 – Seven members of the Lapsus$ extortion

group were arrested in London, including one of its leaders

who was only 16 years old.

September 23, 2022 – A 17-year-old hacker suspected of

being involved in cyberattacks on Uber and Rockstar games

was arrested in London. While these two attacks did not

involve ransomware or extortion, both the suspect and the

attacks were determined to be connected with Lapsus$.

October 19, 2022 – Following an investigation on the breach

of Brazil’s Ministry of Health, Brazilian authorities arrested

another suspect allegedly connected with Lapsus$.

October 26, 2022 – After an investigation involving authorities

from France, the U.S., Canada and Europol’s European

Cybercrime Centre, Mikhail Vasiliev was arrested at his Ontario,

Canada, home. Known to Europol as “one of the world’s most

prolific ransomware operators,” Vasiliev was allegedly linked to

the Lockbit ransomware and several high-profile attacks.

January 26, 2023 – Months after it penetrated Hive’s

networks, the U.S. FBI announced in January that it had

successfully disrupted the group’s operations in 2022. While

no arrests have been made as of publication, Hive’s website

has been seized and its decryption keys were captured and

provided to victims.

41     |     2023 SonicWall Cyber Threat Report     |     Ransomware

CAPTURE ATP & RTDMI

RTDMI™ Detections Continue to Rise

SonicWall’s patented Real-Time Deep Memory Inspection™

(RTDMI) continued to raise the bar in 2022. The technology

identified and mitigated 465,501 never-before-seen malware

variants — more than in any other year since the technology

was introduced and an average of 1,279 per day.

This increase was enough to push the all-time number of

never-before-seen malware variants detected past the

1 million mark. The 2022 count also represented the first

time a yearly detection total surpassed 450,000.

But that wasn’t all that set 2022 apart. In March alone, the

technology detected 59,259 new variants, more than in any

other month. Combined with higher-than-average detections

in January and February, this helped push Q1 to a total of

147,851 never-before-seen malware variants — the highest

of any quarter on record.

“Zero-Day” vs.
“Never-Before-Seen” Attacks

The “zero-day attack” is one of the most well-known

cybersecurity concepts due to its connection to

high-profile breaches. These attacks are completely new

and unknown threats that target a zero-day vulnerability

without any existing protections (such as patches,

updates, etc.) from the target vendor or company.

Conversely, SonicWall tracks detection and mitigation

of “never-before-seen attacks,” which is the first

time SonicWall Capture ATP identifies a signature as

malicious. These discoveries often closely align with

zero-day attack patterns due to the volume of attacks

analyzed by SonicWall.

500K

400K

300K

200K

100K

0

'Never(cid:2)(cid:3)e(cid:18)ore(cid:2)(cid:10)een' Malware Variants Discovered by RTDMI

153,909
2019

268,362
2020

442,151
2021

465,501
2022

www.sonicwall.com

42     |     2023 SonicWall Cyber Threat Report     |     Capture ATP & RTDMI™

Since it was added to SonicWall’s Capture Advanced Threat

RTDMI is not only highly effective — it’s getting even

Protection — a multi-engine sandbox service designed to

more effective over time. By leveraging machine learning

mitigate new and more evasive forms of malware — RTDMI

capabilities, it continually improves its ability to recognize

has served as a force multiplier to SonicWall’s already robust

and mitigate cyberattacks never before seen by anyone in

threat detection capabilities. RTDMI is capable of finding

cybersecurity.

www.sonicwall.com

malware that relies on various anti-evasion techniques, such

as repacking, recompiling or otherwise obfuscating itself

in an effort to evade all existing industry detections. That

includes malware that hides its weaponry via encryption and

hasn’t yet displayed any malicious behavior.

43     |     2023 SonicWall Cyber Threat Report     |     Capture ATP & RTDMI™

CRYPTOJACKING

Cryptojacking Continues
Record-Breaking Run

As cybercriminals complemented ransomware with more

After attack volume dropped dramatically in November,

low-profile revenue streams in 2022, cryptojacking rates

December came with a vengeance, bringing with it 30.4

began to accelerate significantly. By year’s end, SonicWall

million cryptojacking attempts. This unprecedented total

Capture Labs threat researchers recorded 139.3 million

not only exceeded the previous monthly record by roughly

cryptojacking attempts, a 43% year-over-year increase.

12 million, it also surpassed the total for all but three

Not only did 2022 mark the first time that yearly attack

quarters on record.

volume surpassed 100 million, it was also more cryptojacking

Even so, highly suppressed volume in November, combined

than SonicWall had ever observed in a single year.

with sustained high rates of cryptojacking at the beginning of

Monthly record totals were set as well: In January,

cryptojacking attempts rose to 18.4 million, surpassing

the previous monthly record (set in March 2020) by

nearly 3 million.

2022, meant that Q1, not Q4, ended the year with the highest

volume on record.

Global Cryptojacking Volume by Year

100M

50M

0

57,549,267
2018

64,115,622
2019

81,901,858
2020

97,057,897
2021

139,260,751
2022

www.sonicwall.com

44     |     2023 SonicWall Cyber Threat Report     |     Cryptojacking

Cryptojacking by Region
While LATAM recorded a 66% drop in cryptojacking volume

year over year, it was the only region to see a drop.

XMRig Now Used in Nearly 90%
of Cryptojacking Attempts
Due to its high availability and ease of use, XMRig was

In North America, which typically sees by far the most

attacks, volume rose from 78.0 million in 2021 to 105.9

million in 2022 — a 36% increase, and more than the entire

world saw the year before.

Asia saw an even larger year-over-year increase of 129%,

jumping from 3 million to 6.9 million. But it was Europe

where cryptojacking grew the fastest: Volume there

soared from 3.4 million in 2021 to 22.0 million in 2022, an

increase of 548%.

Despite skyrocketing attack volumes in Europe, the United

States remained the country with the highest volume.

Cryptojacking attempts there rose 41% year over year.

once again the cryptominer of choice. In 2022, 89.4% of all

cryptojacking attempts recorded by SonicWall were based

on XMRig, up from 67.4% in 2021.

XMRig is an open-source, cross-platform miner that,

while not malicious on its own, is frequently abused by

cybercriminals to illegally mine the privacy coin Monero on

victims’ computers.

The miner can be dropped on a victim’s machine through a

variety of means, such as the modular Glupteba malware and,

increasingly, malware targeting Linux.

)

D
S
U

(
$

480

415

350

285

220

155

90

25

18,391,069

16,177,143

10,503,983

9,526,560

4,700,504

7,354,130

16,693,844

4,806,230

6,447,604

11,415,563

2,886,965

30,357,156

www.sonicwall.com

45     |     2023 SonicWall Cyber Threat Report     |     Cryptojacking

Linux Increasingly in the Crosshairs
With more than 96% of the world’s top web servers running

Cryptojacking Goes to the “Dogs”
TeamTNT’s techniques were also built upon for a campaign

Linux, attackers have been observed targeting the operating

spotted in September. Named “Kiss-a-dog” based on the

system in increasing numbers. Because Linux offers a

domain used to trigger a shell script payload, this variant

pathway into multi-cloud environments, it can make the

targets vulnerable Docker and Kubernetes instances. In

infection process easier: While there are many cloud tenants

addition to installing XMRig, the malware also tries to escape

to choose from (GCP, Azure, AWS, etc.), Linux is a ubiquitous

from and create backdoors to compromised containers,

platform across all environments. In other words, there’s a

move laterally in the network, and gain persistence — while

much more limited scope of technology that attackers need to

at the same time attempting to terminate and uninstall any

be familiar with.

cloud monitoring services.

In addition to being faster, this method also tends to be

Many of these tactics used in Kiss-a-dog were also present

lower risk: Most antimalware solutions focus primarily on

in an earlier campaign wearing the TeamTNT banner, this one

identifying and mitigating Windows-based attacks, as

detected by SonicWall in May 2022. This variant seems to

opposed to the Linux-based operating systems underpinning

specifically target Alibaba Cloud/Aliyun Linux deployments,

many private and public cloud deployments. As a result, a

but unlike the Kiss-a-dog campaign, it installs the Xanthe

growing amount of sensitive data and infrastructure are left

bitcoin-mining software.

vulnerable to compromise.

Another similar campaign was discovered in June, this one

Unfortunately, as with traditional cryptojacking, attacks on

targeting misconfigured Docker Engine API endpoints and

cloud environments are designed to be as subtle as possible

Redis servers. The attack involved several payloads and

while still achieving the desired output — so it’s unlikely there

was capable of disabling Alibaba Cloud Agent security and

will be any perceptible disruption to operations.

wormlike propagation in addition to XMRig mining. While

the scripts feature TeamTNT logos and messages such as

“TeamTNT likes the Borg,” the mining address and other

factors suggest that this campaign is actually the work of the

WatchDog group.

CYBERCRIMINALS AREN’T
JUST MAKING THEIR
ATTACKS MORE SUBTLE.
THEY’RE ALSO MAKING THEM
MORE SOPHISTICATED.

More Diverse Capabilities = More
Powerful Campaigns
Cybercriminals aren’t just making their attacks more subtle,

however. They’re also making them more sophisticated.

In November, a Linux-targeting cryptojacking campaign

incorporating a remote-access trojan (RAT) was discovered.

This free, open-source RAT, called Chaos RAT, adds a

diverse set of capabilities to the traditional cryptojacking

repertoire — such as the ability to access file explorer; upload,

download and delete files; take screenshots; and connect to a

command-and-control server that can use used for deploying

additional malware.

Another cryptomining Trojan was detected by SonicWall in

June, this one purporting to be from well-known malware

group TeamTNT. After finding, killing and removing any

cryptominers that may already be running (a technique

pioneered by groups like ROCKE), this variant downloads and

installs XMRig, then gains secure access to the victim machine

over an unsecured network. Finally, it launches another

open-source tool, punk[.]py, which collects usernames, SSH

keys, and known hosts from a Unix system, then attempts to

connect via SSH to all the combinations found.

46     |     2023 SonicWall Cyber Threat Report     |     Cryptojacking

Secure Your Redis Servers … or Pay
Redis servers are a growing target for opportunistic

attackers. Since they’re meant to be used inside the network,

rather than exposed to the internet, authentication isn’t

enabled by default. If they aren’t secured, they can easily be

compromised by malware, such as the Headcrab malware.

In practice a botnet (due to its ability to exploit Redis’

SLAVEOF command), this custom malware had already

infected at least 1,200 Redis servers as of February 2023.

Headcrab runs in memory, bypasses volume-based scans,

deletes logs and communicates with legitimate IP addresses.

These tactics have made it so stealthy that, until recently, it

was virtually undetectable.

The botnet’s primary function is to mine Monero, and it

seems to be unusually good at it: Researchers estimate

that each infected endpoint could be expected to generate

around $4,500 per year.

Big Tech Bites Back
Big tech firms, such as Amazon, Alibaba and Google, are

well aware of the attacks on their cloud servers. But since

the privacy of data and workflows is part and parcel of the

product they sell, they’re limited in how they can protect

customer organizations against cryptojacking.

The true catalysts for 2022’s “crypto winter” were

But the threat is growing. In its 2021 Threat Horizons report,

Google Cloud reported that 86% of compromised cloud

macroeconomic uncertainty and the complete collapse of

two so-called “stable coins”: Luna and TerraUSD.

instances were being used to illegally mine cryptocurrency.

As investors fled the crypto market, cybercriminals upped the

In response, some cloud providers have been working to

increase their ability to detect cryptojacking. Microsoft has

improved its Defender for Endpoint, and Google Cloud has

ante, resulting in a record-breaking year for both the number

of heists and — with an estimated $3.56 billion (USD) stolen —

the amount of losses.

introduced the Virtual Machine Threat Detection (VMTD).

In the first week of August, the Nomad cryptocurrency bridge

But with the entry points for cloud-based cryptojacking

remaining largely the same as for traditional cryptojacking —

such as phishing, misconfigurations and poor patch hygiene

— following established best practices will go a long way.

The Bust, the Breaches and the Late Bitzlato
If you started 2022 with one bitcoin, by the end of the year,

you’d be … highly disappointed.

was attacked, resulting in a loss of almost $200 million of its

funds. The very next day, attackers reportedly exploited a

vulnerability in Slope wallets to steal at least $6 million worth

of crypto tokens from more than 9,000 wallets.

In October, the Binance Smart Chain network saw an attack

bigger than both of these combined, when criminals stole

$570 million. But the biggest heist — not just of 2022, but

of all time — took place in March. That month, attackers

After starting 2022 at nearly $50,000 — already down

breached the Ronin bridge and stole a staggering $650

significantly from its peak of nearly $69,000 — bitcoin prices

million. Researchers now believe the Lazarus group,

soon sank rapidly, ending 2022 at $16,556, roughly a third of

who was responsible for stealing $100 million in an

their Jan. 1 value. But while BTC prices were among the most

attack on Harmony’s Horizon bridge in June, was also

visible aspects of the crash, they were only a symptom.

behind this breach.

47     |     2023 SonicWall Cyber Threat Report     |     Cryptojacking

But while several crypto companies were a target for

In February 2023, Bitzlato’s CEO, a sales executive, the

cybercriminals, one was reportedly a haven for them. In

marketing director and others were apprehended in Spain,

January 2023, Anton Shkurenko, founder of cryptocurrency

bringing the total number of arrests to six. But despite

exchange Bitzlato, was arrested after an investigation found

ongoing enforcement efforts, Shkurenko has vowed that this

Bitzlato had violated U.S. anti-money laundering regulations.

isn’t the end, and that the new Bitzlato would be based out of

Russia and “out of the reach of law enforcement authorities.”

According to U.S. Attorney Breon Peace, the exchange

“sold itself to criminals as a no-questions-asked

cryptocurrency exchange,” and processed over $4.5 billion

in cryptocurrency transactions, including more than $15

million in ransomware proceeds.

Bitzlato was reportedly associated with several cybercriminal

groups, including DarkSide, Phobos and Conti. It also worked

closely with Hydra, which, prior to its shutdown, was the

world’s biggest and longest-running darknet marketplace,

specializing in stolen financial information, fraudulent

identification documents, money laundering services

and narcotics.

According to the U.S. Justice Department, “Hydra buyers

routinely funded their illicit purchases from cryptocurrency

accounts hosted at Bitzlato, and in turn, sellers of illicit goods

and services on the Hydra site routinely sent their illicit

proceeds to accounts at Bitzlato.”

48     |     2023 SonicWall Cyber Threat Report     |     Cryptojacking

% of Customers Targeted by Cryptojacking in 2022

0.50

0.45

0.40

0.35

0.30

0.25

0.20

0.15

0.10

0.05

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

Finance

www.sonicwall.com

Cryptojacking by Industry
Among the most volatile of our data sets, 2022’s data on

cryptojacking by industry highlights the rapid evolution

of cybercriminal behavior. The least movement was seen

in education, where total attack volume increased 20%

over 2021’s totals. Government and healthcare also saw

double-digit movement, with attack volumes falling 83% and

76% respectively.

Attacks on finance customers increased 352% in 2022,

enough to move it from No. 4 to No. 3 for attack volume.

But even this triple-digit spike wasn’t the worst observed:

those in retail saw year-over-year attack volume jump a

staggering 2,810%. But despite retail having the highest

total attack volume, these customers were the least likely

to see an attack: it was education customers that had the

highest percentage of customers targeted.

Cryptojacking Attack
Volumes by Industry

2021

2022

  1.  Healthcare

  1.  Retail

  2.  Education

  2.  Education

  3.  Government

  3.  Finance

  4.  Finance

  4.  Healthcare

  5.  Retail

  5.  Government

49     |     2023 SonicWall Cyber Threat Report     |     Cryptojacking

ENCRYPTED ATTACKS

Encrypted Attacks Fall 28%

In 2022, SonicWall Capture Labs threat researchers

But then December came, bringing with it more than twice

recorded 7.3 million encrypted attacks, down from 10.1

the number of attacks that LATAM recorded in the other

million in 2021. But in 2022, the total was closer to last year’s

11 months combined. This late-year blitz was enough to

record high than to the volumes seen in 2019 (3.7 million) and

singlehandedly push encrypted attacks in the region from a

2020 (3.8 million).

62% year-over-year decrease to a 29% increase.

But while a 28% decrease is somewhat modest compared

While it lacked the volatility seen in other regions, double-

with some of the movement we’ve seen elsewhere, it hides a

digit movement was also seen in North America and Europe,

great deal of regional variation.

which experienced a drop of 39% and an increase of

In Asia, attack volumes fell dramatically in 2022, dropping

85% year over year. For most of the year, LATAM appeared

to be going the same direction. By November, attack

volumes for 2022 were less than half that seen in 2021.

22%, respectively.

% of Customers Targeted by Malware Over HTTPs

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

2022

2021

* Organization must have a SonicWall firewall with DPI-SSL activated.

* Organization must have a SonicWall firewall with DPI-SSL activated.

www.sonicwall.com

50     |     2023 SonicWall Cyber Threat Report     |     Encrypted Attacks

Encrypted Attacks by Industry
For the industries studied, the news ranged from good,

to bad, to worse. Retail and finance received a welcome

reprieve from encrypted attacks, with attack volumes for

these industries falling 79% and 45%, respectively.

In contrast, healthcare saw a 35% jump in malware attacks

over HTTPs — but this was small compared with what was

experienced by customers in education and healthcare. Both

of these industries experienced triple-digit attack volume

increases, with attacks on education rising 411% and attacks

on government spiking 887%.

The huge increase in attacks on government organizations

can also be observed in the per-customer data. Government

was the only industry studied to see a year-over-year

increase in the average percentage of customers targeted.

This increase pushed it above education, the industry that

saw the most attacks per customer in 2021.

What Are Encrypted Threats?

Put simply, TLS (Transport Layer Security) is used to

create an encrypted tunnel for securing data over

an internet connection. While TLS provides security

benefits for web sessions and internet communication,

this encryption protocol is also increasingly used by

cybercriminals who want to hide malware, ransomware,

zero-day attacks and more.

Legacy firewalls and other traditional security controls

lack the capability or processing power required to

detect, inspect and mitigate cyberattacks sent via

HTTPs traffic, making this a highly successful avenue for

skilled threat actors to deploy and execute malware.

% of Customers Targeted by Malware Over HTTPs in 2022

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

Finance

* Organization must have a SonicWall firewall with DPI-SSL activated.

* Organization must have a SonicWall firewall with DPI-SSL activated.

www.sonicwall.com

51     |     2023 SonicWall Cyber Threat Report     |     Encrypted Attacks

INTRUSION ATTEMPTS

Overall Intrusion Attempts Up

Intrusion attempts continued to climb in 2022, hitting a new

But while there was no reshuffling of the regions with regards

high of 6.3 trillion. This represents a 19% increase over 2021’s

to who was hardest hit, the gap between North America and

total, and is roughly six times the number of overall attempts

Europe, which had the second-highest attack volume, is

observed in 2013, the first year SonicWall recorded this data.

continuing to grow — making it likely that malicious intrusion

attempts will continue to disproportionately affect this region

for the foreseeable future.

But while there may be more overall intrusions, a majority of

this increase is due to low-severity hits associated with pings

and other actions that are typically benign. The number of

moderate- or high-severity intrusion attempts, also known as

malicious intrusion attempts, observed in 2022 actually fell,

dipping to 10.6 billion — a 10% year-over-year drop.

Even larger decreases were recorded in Europe and Asia,

where malicious intrusions fell 28% and 17%, respectively.

In North America, malicious intrusion attempts remained

essentially unchanged from 2021 levels. Only LATAM saw

a statistically significant increase: Malicious intrusion

attempts there rose 8%.

Global Intrusion Attempts

Global Intrusion Attempts

1.5B

1.5B

1B

1B

0.5B

0.5B

0

0

,

5
1
8
5
4
3
3
0
6
1

,

,

,

.

0
0
6
5
9
4
3
8
0
7
9

,

,

5
1
8
5
4
3
3
0
6
1

,

,

Jan

,

.

0
0
6
5
9
4
3
8
0
7
9

,

,

5
8
4
9
8
1
4
2
4
1

,

,

,

.

0
0
4
1
3
3
1
7
1
7
8

,

,

5
8
4
9
8
1
4
2
4
1

,

,

Feb

,

.

0
0
4
1
3
3
1
7
1
7
8

,

,

3
9
7
4
4
1
1
0
5
1

,

,

,

.

0
0
6
2
7
9
2
1
7
3
9

,

,

3
9
7
4
4
1
1
0
5
1

,

,

Mar

,

.

0
0
6
2
7
9
2
1
7
3
9

,

,

8
3
9
4
2
3
4
7
8

,

,

.

0
0
9
6
0
7
9
4
4
2
9

,

,

8
3
9
4
2
3
4
7
8

,

Apr

,

9
0
4
0
3
6
5
9
8

,

,

.

0
0
8
4
8
7
1
8
4
6
9

,

,

9
0
4
0
3
6
5
9
8

,

May

,

.

0
0
8
4
8
7
1
8
4
6
9

,

,

.

0
0
9
6
0
7
9
4
4
2
9

,

Jan

Feb

Mar

Apr

May

,

7
2
2
1
3
9
6
9
6

,

,

.

0
0
3
0
3
3
7
4
5
2
0
1

,

,

,

Jun

7
2
2
1
3
9
6
9
6
2021

,

,

1
0
8
9
4
1
7
7
6

,

,

9
0
3
3
5
2
6
6
0
1

,

,

,

1
0
8
9
4
1
7
7
6

,

Jul

,

1
6
9
5
6
8
3
5
7

,

,

4
6
7
4
5
7
4
0
9

,

,

1
6
9
5
6
8
3
5
7

,

Aug

,

4
6
7
4
5
7
4
0
9

,

,

9
0
3
3
5
2
6
6
0
1

,

,

,

.

0
0
3
0
3
3
7
4
5
2
0
1

,

,

,

0
8
5
6
9
3
0
5
8

,

,

8
9
6
3
0
5
2
3
7

,

,

0
8
5
6
9
3
0
5
8

,

,

4
6
4
5
6
2
8
6
9

,

,

4
6
0
2
4
4
1
6
7

,

,

4
6
4
5
6
2
8
6
9

,

Oct

,

4
6
0
2
4
4
1
6
7

,

,

8
9
6
3
0
5
2
3
7

,

,

9
5
5
1
4
0
3
0
7

,

,

2
7
2
2
9
1
6
5
7

,

,

9
5
5
1
4
0
3
0
7

,

Nov

,

9
3
8
0
3
3
7
0
9

,

,

8
4
2
2
3
1
3
3
7

,

,

9
3
8
0
3
3
7
0
9

,

Dec

,

8
4
2
2
3
1
3
3
7

,

,

2
7
2
2
9
1
6
5
7

,

Sept

Jun

2022

Jul

Aug

Sept

Oct

Nov

Dec

Note: Only includes malicious medium- and high-risk intrusion attempts.

Note: Only includes malicious medium- and high-risk intrusion attempts.
2021

2022

Note: Only includes malicious medium- and high-risk intrusion attempts.

52     |     2023 SonicWall Cyber Threat Report     |     Intrusion Attempts

www.sonicwall.com

www.sonicwall.com

What is an Intrusion Attempt?

A malicious intrusion attempt is a

Malicious intrusions also include the

What SonicWall records is detection

security event in which a cybercriminal,

exploitation of vulnerabilities that are

and prevention of vulnerabilities coming

hacker, threat actor or intruder tries to

not yet well publicized or haven’t been

from both external and internal sources.

gain access to a system or resource

published — the dreaded zero-day

When a piece of code that constitutes

by exploiting a vulnerability without

vulnerabilities.

authorization. Such vulnerabilities

are generally public and published

as CVEs (see page 10). While these

vulnerabilities are public, not everyone

patches at the same rate, giving

attackers an opportunity to take

advantage of unpatched software or

appliances that can be used as an entry

point into a network.

Vulnerability exploitation doesn’t

stop once attackers get inside the

network. In fact, it usually accelerates.

a vulnerability passes a firewall with

Intrusion Prevention enabled, and the

firewall detects and neutralizes that

code, an intrusion attempt is counted.

Attackers attempt to gain network

As noted, malicious intrusions

persistence and lateral movement by

consist of moderate- and

exploiting other, internal vulnerabilities

high-severity intrusion attempts —

in unpatched systems and software

low-severity intrusion attempts are

inside the network.

typically harmless.

The Rise of RCEs
While very little in the cybersecurity world has returned to

While this type of intrusion attempt made up less than 10%

its 2019 state, malicious intrusion types are one exception:

of total malicious intrusions in 2021, their numbers grew

Just like we saw four years ago, Remote Code Executions

tremendously in 2022, and they now make up 21.5% of

(RCEs) are once again the most common form of malicious

malicious intrusion attempts globally.

intrusion we observed.

53     |     2023 SonicWall Cyber Threat Report     |     Intrusion Attempts

www.sonicwall.com

What is an RCE?

An RCE attack takes place when a threat actor uses a

Here are some of the RCEs SonicWall Capture Labs threat

vulnerability to remotely run malicious programming

researchers reported in 2022:

code, usually in an unexpected path and with system-level

privileges. (The infamous Bluekeep vulnerability is one

EmbedThis Goahead Web Server CGI RCE

example of this.) These vulnerabilities are among the most

dangerous on software systems and are frequently used to

spread ransomware.

Samba vfs_fruit Module RCE Vulnerability

Java Spring Framework Spring4Shell RCE
Vulnerability

VMware Workspace One Access & Identity
Manager RCE Vulnerability

WSO2 API Manager RCE Vulnerability

2/4/22

3/4/22

4/1/22

4/22/22

4/29/22

Parse Server Databasecontroller RCE Vulnerability

5/6/22

Follina MS-MSDT RCE Vulnerability

Atlassian Confluence OGNL Vulnerability

Oracle MySQL NDB Cluster RCE

Ivanti Avalanche RCE Vulnerability

Zimbra Collaboration RCE Vulnerability

Microsoft Exchange Server Zero-Day
Vulnerabilities

Zimbra Collaboration Suite TAR RCE

Follina Vulnerability Is Being Used to
Deliver Redline Info Stealer

6/1/22

6/10/22

7/22/22

8/5/22

9/2/22

9/30/22

10/20/22

11/2/22

Malicious Intrusions by Industry
The industry-specific intrusion data for 2022 showed less

But a look at the per-customer data shows that while most

volatility than some other threat types, but that doesn’t mean

of the industries studied saw an increase, that doesn’t

there weren’t still some significant upticks.

necessarily mean more of these customers are seeing an

Government organizations saw the worst of it: malicious

attack. In fact, we observed the opposite.

intrusion attempts on these customers spiked 74% year

The biggest decrease in percentage of customers targeted

over year. With a 55% increase, the finance industry didn’t

by malicious intrusion attempts was for government: In

fare much better. Healthcare and retail saw significantly

2021, 40.7% of these customers saw an attack, but in 2022,

more modest increases of 5% and 3%, respectively.

only 33.1% did.

Only education saw a decrease — total malicious

intrusions targeting these organizations dropped 17%

from 2021’s levels.

Combined with the 74% increase in attacks on government

overall, this suggests that malicious intrusion attempts on

government are becoming much more targeted.

54     |     2023 SonicWall Cyber Threat Report     |     Intrusion Attempts

The opposite held true for education customers.

After remaining in the middle of the pack for the first half

While education saw a sizeable drop in overall attacks,

of the year, in July the percentage of education customers

per-customer data showed the least-favorable trend, with

targeted rose several percentage points — and the

the percentage of customers targeted falling only 3.2%

percentage of attacks on government customers fell by

year-over-year.

These averages (and their accompanying rankings) are

largely courtesy of an odd divergence that began in Q3.

nearly the same amount. Both trends persisted through

the end of the year, suggesting a sustained change in

cybercriminal behavior.

% of Customers with an Intrusion Attempt in 2022

50

45

40

35

30

25

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

Finance

www.sonicwall.com

55     |     2023 SonicWall Cyber Threat Report     |     Intrusion Attempts

MALICIOUS PDF/OFFICE FILES

Malicious PDFs Up by
More than a Third

In 2022, SonicWall Capture Advanced Threat Protection

But in 2021, the trend began to shift in favor of PDFs — and in

(ATP), which includes patented Real-Time Deep Memory

2022, the number of malicious PDFs was double the number

Inspection™ (RTDMI), logged 119,549 new PDF-based

of malicious Office files.

attacks. This 35% increase pushed the number of attacks

past the 100,000 mark for the first time since SonicWall

began tracking these threats.

But while malicious PDFs and Office files are among the

most dangerous malicious filetypes, due to their ability to

blend in with legitimate and expected attachments in a work

The number of malicious Microsoft Office files rose too, but

environment, they aren’t the most common. For the second

just barely — the total number of malicious Office files in

year in a row, that dubious distinction belonged to .exe files.

2022 was 54,371, just 3% higher than 2021’s total.

2021 turned out to be an inflection point in attacks using

PDF versus attacks using Office files. Weaponized office files

were the preferred means of attack in 2018, 2019 and 2020.

2022 New Malicious File Type Detections | Capture ATP

Other 4.33%

PDF 19.28%

Scripts 19.87%

Archive 16.17%

Executables 31.58%

Oﬃce 8.77%

www.sonicwall.com

56     |     2023 SonicWall Cyber Threat Report     |     Malicious PDF/Office Files

1
2
0
2
L
L
U
F

2
2
0
2
D
M

I

2
2
0
2
L
L
U
F

2%

1%

1%

XLM

No Macro

VBA

VBA_XLM

www.sonicwall.com

A Macro-Level Difference
For the past several years, XLM macros, also known as Excel

That year, researchers began to observe coordinated

4.0 macros, have been a popular tool for cybercriminals.

attempts by cybercriminals to exploit these macros, but

These macros were first included in Microsoft Excel in 1992,

it would be another five years before widespread attacks

but were quickly replaced by XLM’s successor, VBA.

leveraging Excel 4.0 macros really took off. In 2020, the

For decades, XLM was little more than a relic — but in 2015,

Microsoft released its Antimalware Scan Interface (AMSI),

which included the capability to scan for malicious use of

use of this tactic accelerated dramatically, and eventually

included campaigns utilizing the macros to spread Emotet,

Trickbot, Zloader and more.

VBA macros. Ever on the lookout for ways to circumvent

But between 2021 and 2022, SonicWall Capture Labs threat

defensive measures, threat actors seized on the less capable

researchers observed that the use of XLM dropped from

but largely forgotten XLM macros as a way to continue to slip

three-quarters to not much more than half. What happened?

under the radar.

57     |     2023 SonicWall Cyber Threat Report     |     Malicious PDF/Office Files

Rabota Retires,
Posik Punches In

In last year’s Cyber Threat Report, we noted that the

most commonly observed author of malicious Office files

was Rabota: Nearly 50% of those with an author listed

were credited to this name.

In 2022, however, Rabota fell off the Top 10

list altogether. The heir apparent? Posik, who

allegedly authored roughly as many files in 2022 as

Rabota did in 2021.

The shakeup was apparently widespread: Aside

from expected aliases like Admin, Test and User, the

only author from 2021’s list to appear on the list for

2022 is “brian.”

Deciphering the Drop

Two things, actually. In October 2021, Microsoft

announced it would begin disabling Excel 4.0 macros by

default in Microsoft 365 — a measure that was rolled out

in January 2022.

Then, in February 2022, the company announced that VBA

macros obtained from the internet would soon be blocked

by default on Windows devices running its Access, Excel,

PowerPoint, Visio and Word apps. This change was rolled

out in mid-July.

So what we’re likely seeing reflected in these graphs is, first,

the announcement regarding XLM causing the number of

XLM macros to drop 11% in the first six months of 2022,

accompanied by a corresponding near-doubling in the

use of VBA files.

Then, in the next six months — during which time the

announcement regarding VBA was made — we see a

significant slowdown in the growth of VBA macros, but

sustained growth in malicious Excel files using no macros.

The Future of Malicious Office Files

Unless new evasiveness tactics are developed, it’s likely

that we’ll continue to see a drop in XLM macros and the

beginnings of a drop in VBA macros as we make our way

through 2023. In their place, we’re likely to see accelerating

growth in the use of malicious files without any macros,

such as those exploiting vulnerabilities in MS-Office, making

use of things like Dynamic Data Exchange (DDE) fields, or

requiring a victim to click on a phishing link.

58     |     2023 SonicWall Cyber Threat Report     |     Malicious PDF/Office Files

IoT MALWARE

IoT Malware Nearly Doubles

When IoT malware attack volume rose just 6% in 2021 —

after jumping 218% in 2019 and another 66% in 2020 — it

offered hope that wild acceleration might be giving way to

slower and more stable growth. Unfortunately, this easing

would prove temporary: In 2022, SonicWall Capture Labs

threat researchers recorded 112.3 million instances of IoT

malware, an 87% increase over 2021.

This spike easily exceeded the previous record for IoT

malware attacks observed by SonicWall in a single year, and

it also pushed the number of attacks past the 100 million

mark for the first time.

Within this overall yearly record were several smaller

records. The global attack volume for January reached 12.54

million, surpassing the previous high-water mark by nearly

2 million. And in June, attack volume soared even higher,

reaching 12.98 million. These higher-than-usual monthly

attack volumes pushed quarterly totals to new records, as

well. The only quarter not to set a new attack volume record

was Q3 — and it wasn’t far off, at that.

What is IoT Malware?

IoT malware is a type of malware specifically designed to take

Once connected, these devices can work together to perform

over connected, or IoT, devices. This malware gains entry

malicious activities, such as launching of Distributed Denial of

through vulnerabilities, exploit kits, weak or compromised

Service (DDoS) attacks, installing and running cryptojacking

credentials, and other means. Because these devices are

malware, conducting brute-force attacks to deploy

often not very powerful on their own, IoT malware is generally

ransomware or steal data, or sending spam emails.

deployed en masse with the intention of creating botnets of

many infected IoT devices. These botnets are controlled either

via a command-and-control server that connects to each

infected device, or through the use of peer-to-peer networking.

The Mirai botnet is the most famous example of this type of

malware, but there have been many others.

59     |     2023 SonicWall Cyber Threat Report     |     IoT Malware

120M

100M

80M

60M

40M

20M

0

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

Global IoT Malware Volume by Year

32,700,982
2018

34,296,891
2019

56,949,058
2020

60,139,968
2021

112,294,990
2022

www.sonicwall.com

Global IoT Malware Volume

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

5
7
4
2
4
5
2
1

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

0
3
3
9
4
6
5

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

7
1
1
1
8
1
0
1

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

1
7
9
0
3
8
6

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

4
3
9
9
5
8
8

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

3
4
6
2
8
9
2
1

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

0
7
5
1
1
8
8

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

7
1
0
2
8
3
0
1

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

7
4
1
0
3
1
6

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

8
4
0
4
6
9
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

8
1
8
5
1
4
1
1

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

,

8
9
8
2
4
5
0
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

2021

2022

www.sonicwall.com

60     |     2023 SonicWall Cyber Threat Report     |     IoT Malware

IoT Malware by Region
Given the global IoT malware increase, it’s unsurprising that

IoT Malware by Industry
For the second year in a row, SonicWall Capture Labs threat

there were significant, across-the board increases at the

researchers observed increases in IoT malware volume

regional level. IoT malware volume in Europe increased 21%,

across every industry studied — and this year, the increases

followed by the LATAM (65%) and Asia (73%) regions.

were even bigger.

And while overall malware, ransomware and other threat

Healthcare customers saw the least change, with a 33%

types saw attacks fall in the hardest-hit regions, IoT malware

year-over-year increase in attacks. Government, which saw a

did not follow this pattern. North America, which experienced

jump of 40%, wasn’t far behind.

the biggest increase at 145% year-over-year, already led

the pack in IoT malware attacks — and it has for three

years running.

The news gets considerably worse from here, however:

Retail experienced a 159% increase in attack volume, and

education wasn’t much better off at 146%. But it was finance

As cybercriminals doubled down on attacking targets in

that saw the brunt of the increase: attacks on finance

North America last year, the gulf between it and the second-

customers skyrocketed 252% year over year.

highest region widened from just a few million to roughly 40

million: By the end of 2022, North America had recorded 62.9

million attacks, versus 23.2 million in Europe.

On a per-customer basis, the rankings remained mostly the

same in 2022 as they were in 2021, with the only exceptions

being retail and finance. Always close in terms of the

On a country-by-country level, the two countries that

percentage of customers targeted, this year retail surpassed

typically see the highest IoT malware attack volume also

finance, but only by the tiniest margin.

saw triple-digit increases. The U.K., which has the second-

highest attack volume, saw IoT malware increase 163%. And

in the U.S., which typically sees the most attacks, attack

volume rose 169%.

% of Customers Targeted by IoT Malware in 2022

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

Finance

www.sonicwall.com

61     |     2023 SonicWall Cyber Threat Report     |     IoT Malware

Safeguarding Your Smart Devices

While the number of connected devices coming online

continues to grow — currently  estimated at 17 billion and

counting — the types of devices most targeted for attack

remains roughly the same year after year. In 2022, SonicWall

continued to observe the highest attack volumes targeting

routers, cameras, firewalls, load balancers and Network

Attached Storage (NAS) devices. As of February 2023,

SonicWall has 438 signatures protecting more than 136 IoT

device families from various threats, including the device

types seen here:

PRODUCT LINE

D-Link Router

Hikvision IP Camera

NETGEAR DGN

Dasan GPON Router

ZyXEL Firewall/NAS

9

2

2

3

11

Cisco Adaptive Security Appliance

8

D-Link products

F5 BIG-IP

Vacron NVR

Draytek Vigor

21

8

1

2

NUMBER OF
SIGNATURES HITS

PRODUCT LINE

NUMBER OF
SIGNATURES HITS

31,016,331

Yealink

19,251,146

Drobo products

14,451,612

Tenda Router

7,823,114

4,381,335

4,161,243

3,626,533

3,366,830

1,140,007

1,119,891

NETGEAR products

WIFICAM

Buffalo Routers

HiSilicon-based Devices

Netlink GPON Router

TP-Link Router

Wavlink

1

1

5

9

1

1

1

1

4

2

1,067,806

990,225

867,765

353,208

261,672

152,545

149,151

137,718

133,183

115,765

The Ever-Evolving Landscape of IoT Regulations
For anyone putting their trust in IoT devices, 2022 was an

Given the persistent and egregious lack of security in

many connected devices, it’s no wonder that in 2022,

eye-opening year. Microsoft announced in December that

many governing bodies around the world set their sights

75% of industrial control devices — such as the ones used

on tightening regulations around IoT security. Here

in water treatment facilities, power plants and more — have

severe, unpatched vulnerabilities.

are just a few:

United States

Not that our increasingly connected vehicles are much safer.

In February, the National Institute for Standards and

In January, a 19-year-old researcher announced he could

Technology (NIST) published its Recommended Criteria for

exploit a bug on the TeslaMate dashboard to run commands

Cybersecurity Labeling for Consumer Internet of Things.

on over 25 vehicles in 13 countries. Five months later,

Based on these recommendations, private sector leaders,

another researcher used a Bluetooth device to enroll his own

academic institutions and the U.S. government convened

NFC key and take control of a vehicle.

And as the year drew to a close, we learned our robot

vacuums and other IoT devices could record us doing … well,

pretty much anything.

in October to advance a national cybersecurity labeling

program for IoT devices. Discussions centered around how

to best implement the labeling program, how to generate a

globally recognized label, and how to work toward improved

security standards for connected devices. Rollout for the

program is expected to begin in spring 2023.

62     |     2023 SonicWall Cyber Threat Report     |     IoT Malware

United Kingdom

European Union

On Dec. 6, the Product Security and Telecommunications

The European Union’s Cyber Resilience Act was proposed

Infrastructure Act of 2022, or PSTI Act, became law. These

in September 2022. This legislation aims to address the

new regulations ensure that consumer IoT devices are more

lack of cybersecurity in consumer IoT products, as well

secure against threats by banning default passwords and

as a lack of updates or patches to address vulnerabilities.

stipulating that manufacturers disclose how long they plan

Unlike the voluntary guidance issued by some nations, the

to offer product security updates. To ensure compliance with

Cyber Resilience Act allows for large fines and penalties

the new regulations, the law sets up an enforcement regime

for violators, and it specifies that products failing to meet

that includes civil and criminal sanctions, and also ensures

the outlined safety requirements will not be permitted

that manufacturers have a point of contact for reporting

to go to market.

issues and vulnerabilities.

Singapore, Canada and United Kingdom

A collaborative effort between Singapore, Canada and the

U.K. was announced in November 2022. The three countries

plan to work together to support and promote the creation of

international standards and security requirements to replace

the current fragmented patchwork of regulations worldwide.

“Through this global alignment,” the announcement

read, “we can reduce duplication of testing and similar

assessments and the challenge for industry of needing to

apply to multiple schemes underpinned by identical or very

similar requirements.”

63     |     2023 SonicWall Cyber Threat Report     |     IoT Malware

NON-STANDARD PORTS

Non-Standard Port Attacks Defy Expectations

In past cyber threat reports, we’ve noted that non-standard

With full-year data tabulated, 2022’s second half had fewer

port attacks have followed a predictable pattern since

attacks via non-standard ports, not more. And with 14% of

SonicWall began tracking them in 2018. Attacks would rise in

attacks going through non-standard ports in 2022, it was

even-numbered years and fall in odd-numbered years, with

the first time SonicWall had ever seen these attacks drop

odd-numbered years seeing more attacks in the first half

two years in a row.

and even years seeing more in the second half.

While it’s too early to say what the new paradigm will be,

Based on how many other longstanding trends fared in

there are some emerging trends. Our prediction that

2022, you may have some idea of where this is going.

attacks likely wouldn’t dip back into the single digits held

In the first half of 2022, SonicWall Capture Labs threat

researchers found, on average, that 14.5% of attacks came

through non-standard ports — more or less in line with

expectations. But in the second half, something unusual

happened: Attacks began to fall instead of rise.

true in 2022, but nor did they come close to approaching

the heights we’ve seen in previous years. This decrease in

variation, coupled with just a 2% year-over-year change,

indicates we may be seeing attacks begin to stabilize.

2021-22 Global Malware Attacks

100%

80%

60%

40%

20%

79%

87%

84%

86%

82%

89%

85%

87%

0%

21%
Q1 2021

13%
Q2 2021

16%
Q3 2021

14%
Q4 2021

11%
Q1 2022

18%
Q2 2022

15%
Q3 2022

13%
Q4 2022

Non-Standard Ports

Standard Ports

www.sonicwall.com

64     |     2023 SonicWall Cyber Threat Report     |     Non-Standard Ports

IN THE FIRST HALF OF 2022,
SONICWALL CAPTURE LABS
THREAT RESEARCHERS FOUND,
ON AVERAGE, THAT 14.5% OF
ATTACKS CAME THROUGH
NON-STANDARD PORTS.

What is a Non-Standard Port Attack?

In networking, a port number uniquely identifies the endpoint

Traditional proxy-based firewalls generally focus their

of a connection and directs data to a particular service. While

protection on traffic going through the standard ports — but

around 40,000 ports are registered, only a handful — the

with so many ports to monitor, these legacy firewalls are

“standard” ports — are generally used. For instance, HTTP

unable to mitigate attacks coming over non-standard ports.

uses port 80, HTTPs uses port 443, and SMTP uses port 25.

Any service using a port other than the one assigned to it by

default, usually as defined by the IANA port numbers registry,

is using a non-standard port.

As a result, threat actors target non-standard ports to

increase the odds of remaining undetected as they deploy

their payloads. That’s why it’s important to ensure your

network is secured by a modern firewall capable of analyzing

There’s nothing inherently wrong with using non-standard

specific artifacts (as opposed to all traffic), and thus able to

ports, but they can present cybersecurity challenges.

identify these attacks.

65     |     2023 SonicWall Cyber Threat Report     |     Non-Standard Ports

PHISHING

Health and Finances Top Phishing
Topics for 2022

In 2022, phishing topics again tracked closely with

themselves caught between increased interest rates, a record

current events. The top themes were Financial/Mortgage,

low in housing supply and still-rising home prices.

Cryptocurrency, Healthcare and Pandemic.

In December, we see a similar spike in health-related emails,

As COVID-19 continued to shift from pandemic to endemic,

coinciding with the open enrollment periods of many

SonicWall observed a drop in pandemic-related phishing, which

insurance programs and headlines warning of a flu, RSV and

contributed to a 17% decrease in phishing globally.

COVID-19 “tripledemic.”

But attackers aren’t just sending fewer emails, they’re sending

In contrast, while we see an uptick in cryptocurrency-

different ones: the number of finance- and mortgage-related

related emails in April, around when Bitcoin began to fall,

phishing sent in 2022 saw a corresponding increase. These

cryptocurrency (and related topics such as NFTs) were hot

emails spiked in February, as falling economic indicators in

topics all year, corresponding with a fairly steady and sustained

many countries stoked recession fears and homebuyers found

rate of crypto-related phishing.

% of Phishing Attempts in 2022 by Topic

20

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

Financial & Mortgage

Cryptocurrency

Healthcare

Pandemic

Ready to Test Your Phishing IQ?

With over 90% of data breaches starting with a phishing attack, it’s never been more

critical to know how to spot a phish. But today’s phishing attacks are more subtle and

sophisticated than ever before. Will you be able to spot the imposters?

www.sonicwall.com

TAKE THE QUIZ

66     |     2023 SonicWall Cyber Threat Report     |     Phishing

CONCLUSION

The Next Step is Up to You

While threat research is a vital part of a larger cybersecurity

plan, it’s what you do with these insights that will make or

break your security strategy. In conjunction with the 2023

SonicWall Cyber Threat Report, SonicWall threat researcher

Immanuel Chavoya is offering an in-depth discussion

on some of the best ways to put this data to work for

your organization.

This webinar covers the importance of:

•  Performing regular security assessments and penetration

testing to identify vulnerabilities and weaknesses

•  How to choose the best security monitoring and log

management tools for your network

•  Improving incident response plans and protocols to

quickly and effectively contain attacks

•  Developing a comprehensive disaster recovery (DR) plan

•  How and when to regularly review and update security

policies, standards and procedures to align with the latest

threat information and best practices

•  Why communication — with your employees, other

organizations and industry groups — is key to upleveling

your security posture

•  And more

As cyber threats continue to evolve, it’s essential for

organizations to have a comprehensive understanding of

the behaviors and tactics of threat actors. This webinar

covers the importance of implementing and enhancing

countermeasures based on the latest data. By understanding

and addressing the specific tactics and techniques used by

threat actors, organizations can more effectively prepare for,

defend against and respond to cyberattacks.

RESERVE YOUR SEAT

67     |     2023 SonicWall Cyber Threat Report     |     Conclusion

ABOUT THE SONICWALL
CAPTURE LABS THREAT NETWORK

Intelligence for the 2023 SonicWall Cyber Threat Report

was sourced from real-world data gathered by the SonicWall

Capture Threat Network, which securely monitors and

collects information from global devices including:

•  More than 1.1 million security sensors in 215 countries

and territories

•  Cross-vector, threat-related information shared among

SonicWall security systems, including firewalls, email

security devices, endpoint security solutions, honeypots,

content filtering systems and the SonicWall Capture

Advanced Threat Protection (ATP) multi-engine sandbox

•  SonicWall internal malware analysis

automation framework

•  Malware and IP reputation data from tens of thousands of

firewalls and email security devices around the globe

•  Shared threat intelligence from more than 50 industry

collaboration groups and research organizations

•  Analysis from freelance security researchers

1.1m+

Global Sensors

215+

Countries & Territories

Monitoring

24x7x365
<24hrs

Threat Response

140k+

Malware Samples Collected Daily

28m+

Malware Attacks Blocked Daily

68     |     2023 SonicWall Cyber Threat Report     |     About the Sonicwall Capture Labs Threat Network

SonicWall Inc.
1033 McCarthy Boulevard
Milpitas, CA 95035

Refer to our website for additional information.
www.sonicwall.com

© 2023 SonicWall Inc.

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

2023-CyberThreatReport-JK-7606