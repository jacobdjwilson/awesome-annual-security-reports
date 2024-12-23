# SONICWALL CYBER THREAT REPORT 2023

## Table of Contents
- [Introduction](#introduction)
- [A Note From Bob](#a-note-from-bob)
- [2022 Global Attack Trends](#2022-global-attack-trends)
- [Ransomware Down … But Not Out](#ransomware-down-but-not-out)
- [Top Data Breaches of 2022](#top-data-breaches-of-2022)
- [Ransomware Remains Top of Mind in 2022](#ransomware-remains-top-of-mind-in-2022)
- [CVEs](#cves)
- [Published CVEs Break 25,000 for First Time](#published-cves-break-25000-for-first-time)
- [Log4j](#log4j)
- [Log4j Intrusion Attempts Surpass 1 Billion](#log4j-intrusion-attempts-surpass-1-billion)
- [Ukraine](#ukraine)
- [Ukraine Sees Unprecedented Attack Volume in 2022](#ukraine-sees-unprecedented-attack-volume-in-2022)
- [Breach and Attack Simulation](#breach-and-attack-simulation)
- [Cybercriminals Shifting from Cobalt Strike to Sliver](#cybercriminals-shifting-from-cobalt-strike-to-sliver)
- [Key Findings from 2022](#key-findings-from-2022)
- [Malware](#malware)
- [Malware Up for the First Time Since 2018](#malware-up-for-the-first-time-since-2018)
- [Ransomware](#ransomware)
- [Ransomware Reverses Course](#ransomware-reverses-course)
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
- [Non-Standard Ports](#non-standard-ports)
- [Non-Standard Port Attacks Defy Expectations](#non-standard-port-attacks-defy-expectations)
- [Phishing](#phishing)
- [Health and Finances Top Phishing Topics for 2022](#health-and-finances-top-phishing-topics-for-2022)
- [Conclusion](#conclusion)
- [The Next Step is Up to You](#the-next-step-is-up-to-you)
- [About the SonicWall Capture Labs Threat Network](#about-the-sonicwall-capture-labs-threat-network)

## Introduction
This marks our 11th year of publishing the annual SonicWall Cyber Threat Report. Over the last 30-plus years, we’ve deployed millions of firewalls and endpoints globally. To this day, SonicWall has more than 1.1 million active sensors that report threat information multiple times a day, providing us with rich sets of threat data. This threat intelligence contributes to our strong security efficacy, but also highlights key real-time trends in the market.

Over the past year, cybercriminals faced with increasing media attention, heightened awareness and intensifying law-enforcement pressure began shifting away from established hotspots to new areas. As a result, organizations already dealing with macroeconomic pressures, supply-chain challenges and continued geopolitical strife often found themselves confronted with a cyberattack. 2022 reinforced the need for cybersecurity in every industry, and every facet of business, as threat actors targeted anything and everything. For instance, while the retail and finance industries typically see lower cyberattack volume compared with other industries, in 2022 both verticals experienced double-digit increases in malware, including triple-digit increases in IoT malware attacks and cryptojacking.

These trends were compounded by the fact that new tactics are being developed with breathtaking speed. 2022 brought growth in pure extortion attacks, the fall of ‘Big Ransomware,’ widespread expansion to Linux and cloud targets, the adoption of powerful new languages and platforms, and the growing specter of AI and quantum attacks.

In this volatile threat environment, preparation is more critical than ever before. And today, being prepared means more than just deploying the most advanced solutions. It means developing comprehensive cybersecurity strategies, based on the most current threat intelligence available. The 2023 SonicWall Cyber Threat Report is your guide to attackers’ rapidly evolving tactics. On behalf of our network of trusted partners and the entire SonicWall team, including our Capture Labs threat researchers, we’re pleased to share these key insights on cybercrime’s shifting frontlines, as well as the actionable threat intelligence you need to arm your organization against today’s ever-changing threat environment.

## A Note From Bob
Bob VanKirk  
President & CEO 
SonicWall

As a best practice, SonicWall routinely optimizes its methodologies for data collection, analysis and reporting. This includes improvements to data cleansing, changes in data sources and consolidation of threat feeds. Figures published in previous reports may have been adjusted across different time periods, regions or industries.

## 2022 Global Attack Trends
![Image of infographic showing the following data: Malware Attacks +2% 5.5 Billion, Intrusion Attempts +19% 6.3 Trillion, Cryptojacking Attacks +43% 139.3 Million, IoT Malware +87% 112.3 Million, Encrypted Threats -28% 7.3 Million, Ransomware Attacks -21% 493.3 Million]

While the past several years have given the cybersecurity world plenty to worry about, there have nonetheless been a few things we could count on. Malware was falling. Ransomware was rising. And attackers continued to prioritize targets in the U.S.

But from start to finish, 2022 was characterized by change. Ushered in by the announcement of the historic Log4j vulnerabilities just weeks before, the year brought a seismic shift in cybercriminal behavior that sent ripples across every region and every industry.

## Ransomware Down … But Not Out
For the past two years, ransomware has been on a tear, increasing 62% year over year in 2020 and another 105% in 2021. During this time, Ransomware-as-a-Service (RaaS) took off, compromised credentials became cheaper and more plentiful than ever, and the number of vulnerabilities continued hitting record highs.

But despite there being fewer barriers of entry for new threat actors than ever before, in 2022, SonicWall Capture Labs threat researchers observed a 21% drop in ransomware year over year. Other vendors have noted a similar decline, as have U.S. government agencies.

### As Goes Russia, So Goes Ransomware
In May, U.S. National Security Agency (NSA) Cybersecurity Director Rob Joyce remarked on the decreasing ransomware levels. “There’s probably a lot of different reasons why that is, but I think one impact is the fallout of Russia-Ukraine,” Joyce said.

With roughly two-thirds of state-sponsored cyberattacks coming from Russia, and 75% of money generated by ransomware in 2021 going to groups “highly likely to be affiliated with Russia,” anything affecting that country has an outsized effect on cybercriminals, and in turn, cybercrime. According to Joyce, sanctions have made it harder for cybercriminals to move money and buy infrastructure needed for attacks, making cybercriminals less effective. But while becoming “less effective” should result in an even decrease across the board, what’s actually being observed are huge decreases in places that generally see the most ransomware — particularly the United States, where ransomware fell by nearly half.

### Ransomware or Bust
2021 was a banner year for ransomware busts. Cybercriminals associated with Netwalker, Egregor, Lockergoga, MegaCortex and the Trickbot malware were brought to heel amid a flurry of headlines, and when a 30-month investigation involving INTERPOL, South Korea, Ukraine and the U.S. resulted in the arrests of the Cl0p ransomware kingpins, it sent the message that the U.S. was no longer the safe profit center it once was.

But two bigger wake-up calls were yet to come. In January 2022, the Darkside members responsible for the Colonial Pipeline attack were arrested by Russian authorities. Then, in another rare (and no doubt politically motivated) show of cooperation with the U.S., Russian intelligence services arrested members of the infamous REvil gang the same week. Cybercriminals, who had been accustomed to acting with impunity, suddenly became aware that there were very few places left to hide.

In January 2022, a sampling of Dark Web cybercriminal chatter published by ZDNet revealed an undercurrent of fear running through the underworld. “This is a big change. I have no desire to go to jail,” one said in response to the REvil arrests. Another seemed to take them as a warning, saying that anybody who expected Russia to protect them would be “greatly disappointed.” Still others worried that Dark Web admins might reveal their identities to law enforcement.

But as the risk of attacking targets in the U.S. went up, the perceived payoff dropped. Mounting cyberinsurance requirements and the specter of mandatory reporting offered businesses even more motivation to harden defenses. And in 2022, the U.S. government created the Virtual Asset Exploitation Unit, increasing tracking and enforcement efforts against ransomware operators.

Faced with a risk/benefit analysis no longer working in their favor, some cybercriminals shifted targets, leading to double-digit ransomware increases in places like Europe and Asia. Still others are diversifying their tactics.

### Jack of All Trades
Unlike ransomware, which announces its presence, thrives on branding and notoriety, and relies heavily on direct contact with victims, cryptojacking can succeed in complete silence. And for some cybercriminals feeling the heat from increased enforcement efforts and ongoing geopolitical conflict, a consistent, lower-risk income stream may be worth sacrificing a potentially higher payday.

“[Cryptojacking] has a lower potential of being detected by the victim; unsuspecting users across the world see their devices get unaccountably slower, but it’s hard to tie it to criminal activity, much less point to the source,” Terry Greer-King, SonicWall Vice President for EMEA, told Tech Monitor.

## Top Data Breaches of 2022
| NAME                                 | INDUSTRY         | DATE      | IMPACT                                                                                                       |
| :----------------------------------- | :--------------- | :-------- | :----------------------------------------------------------------------------------------------------------- |
| Philippines COMELEC                  | Government       | January   | 60 GB of data, including usernames and PINs for vote-counting machines                                         |
| U.S. Department of Education          | Government       | January   | 820,000 student records                                                                                      |
| Texas Dept. of Insurance             | Government       | January   | 1.8 million records                                                                                          |
| Crypto.com                           | Finance          | January   | 500+ cryptocurrency wallets (more than $30M)                                                                   |
| ICRC (International Committee of the Red Cross ) | Charity          | January   | 515,000 records                                                                                          |
| Flexbooker                           | Software         | January   | 3.7 million records                                                                                          |
| GiveSendGo                           | Fundraising      | February  | 90,000 records                                                                                               |
| Harbour Plaza Hotel Management       | Hospitality      | February  | 1.2 million records                                                                                          |
| Credit Suisse                        | Finance          | February  | 18,000 Credit Suisse accounts                                                                                 |
| Nvidia                               | Technology       | February  | 71,000+ employee records                                                                                     |
| Microsoft                            | Software         | March     | Bing, Bing Maps & Cortana partial source code                                                                  |
| Ronin Bridge Hack                    | Finance          | March     | $625 million in crypto                                                                                       |
| Pegasus Airlines                     | Travel           | March     | 6.5 TB of data, including source code, flight crew PII and passwords/secret keys                               |
| Morgan Stanley Clients               | Finance          | March     | Unknown number of client accounts                                                                            |
| Cash App                             | Finance          | April     | 8.2 million records                                                                                          |
| Elephant Insurance                   | Insurance        | May       | 2.7 million records                                                                                          |
| SuperVPN, GeckoVPN & ChatVPN          | Technology       | May       | 21 million records                                                                                           |
| Cost Rican Government                | Government       | May       | 670GB data                                                                                                   |
| National Registration Dept. of Malaysia | Government       | May       | 22.5 million records                                                                                         |
| Alameda Health System                | Healthcare       | May       | 90,000 records                                                                                               |
| Verizon                              | Telecommunications| May       | Hundreds of employee records                                                                                 |
| Flagstar Bank                        | Finance          | June      | 1.5 million records                                                                                          |
| Shields Health Care Group            | Healthcare       | June      | 2 million records                                                                                            |
| Choice Health Insurance              | Healthcare       | June      | 600MB of data, including names, SSNs, and other PII                                                           |
| OpenSea                              | Finance          | June      | $1.7 million in NFTs                                                                                         |
| Neopets                              | Entertainment    | July      | 69 million records                                                                                           |
| Twitter                              | Social Media     | July      | 5.4 million accounts                                                                                         |
| Uber                                 | Travel           | July      | 57 million records                                                                                           |
| OneTouchPoint                        | Marketing        | July      | 2.65 million records                                                                                         |
| Cisco                                | Technology       | August    | 2.75 GB of data, including engineering files and NDAs                                                        |
| Plex                                 | Software         | August    | 20 million records                                                                                           |
| Okta                                 | Technology       | August    | 169 domains                                                                                                  |
| Nelnet Servicing                     | Finance          | August    | 2.5 million records                                                                                          |
| Optus                                | Telecommunications| September | 9.8 million records                                                                                          |
| Samsung                              | Telecommunications| September | Unknown                                                                                                      |
| North Face                           | Apparel          | September | 200,000 records                                                                                            |
| Revolut                              | Finance          | September | 50,150 records                                                                                               |
| Mydeal                               | Retail           | October   | 2.2 million records                                                                                          |
| Vinomofo                             | Food & Beverage  | October   | 500,000 records                                                                                            |
| Medibank                             | Healthcare       | November  | 9.7 million records                                                                                          |

In 2022, SonicWall researchers recorded a 43% increase in cryptojacking, on the heels of a 19% increase in 2021. This growth set a new record and pushed observed attack volumes past the 100-million mark for the first time ever.

At least one ransomware gang, Astralocker, publicly announced it’s leaving ransomware entirely in favor of cryptojacking, and a comparison of our ransomware data with our cryptojacking findings suggests others could be using these attacks along with or in place of ransomware.

But while some criminals are slowing or abandoning ransomware in favor of cryptojacking and other attack types, others are abandoning the “ware” but keeping the “ransom.”

### The Rise of Extortion Groups
An increased awareness of ransomware motivated many organizations to create and maintain strong backups and incident response plans, making file encryption less effective than it once was.

In response, 2022 brought a growth in the number of ransomware groups no longer actually deploying ransomware. These attackers, referred to as “extortion groups,” include both Lapsus$ and Karakurt — both of which became major threats without encrypting a single endpoint. By using social engineering, vulnerability exploits, stolen credentials or other tactics, these groups gain illegal access to a target network. Then, once they’ve stolen data, they threaten to leak the information if victims don’t pay up.

But while these attacks involve reputational damage, data leaks, and the risk of compliance issues and lawsuits like traditional ransomware, they’re much harder to trace. Since there’s no actual ransomware involved, tracking is often conflated under “malware.” However, this is a distinct form of extortion and needs to be tracked by vendors despite a lack of encrypting endpoints.

### When Will Ransomware Rebound?
While several factors could be responsible for the drop in ransomware, there are also many signs it could soon make a turnaround.

First, it bears mentioning that we aren’t actually seeing any sort of widespread abandonment of ransomware. While attacks are down 21%, 2022’s ransomware volume is still much closer to the sky-high totals we saw in 2021 than to what we saw in 2018, 2019 and 2020. If we remove 2021 as an outlier, ransomware is still on the rise.

In fact, many criminals actually doubled down on ransomware in 2022. Several new ransomware groups formed, including Black Basta, Quantum, Lilith, Stormous and more, and in November, a new version of the highly popular LockBit ransomware was released.

And as 2022 wound down, larger campaigns were once again making headlines. In December, the U.K. news site The Guardian was attacked, and in early 2023, a new ESXiArgs campaign infected over 3,800 victims with ransomware. Perhaps not coincidentally, SonicWall observed an uptick in ransomware in Q4, when attack volume rose to the highest level since Q3 2021. While we can’t be sure yet whether this is a sign of sustained growth, we can be sure ransomware isn’t going anywhere soon.

### A Lapsus in Judgment
In early 2022, a new cybercriminal group began dominating the headlines. Calling themselves “Lapsus$,” they quickly became known for their brazen tactics: Instead of lurking in the corners of the Dark Web, this group actively cultivated a social media presence, accumulating more than 50,000 followers on Telegram. Here, they solicited input on who should be targeted next, ultimately engaging in some of the biggest big-game hunting imaginable: Okta, Nvidia, Samsung, Microsoft and others were all breached. To facilitate these breaches, the group publicly recruited new accomplices, offering money for inside information or assistance.

By mid-September, less than a year after becoming active, the group was gone, its members nabbed in three high-profile arrests. None was older than 21.

In Latin, a “lapsus” refers to a “lapse, slip or error.” And it quickly became clear that much of the group’s trademark attention-seeking was exactly that.

Seemingly operating with a presumption of invincibility, they failed to recognize the main reason they’d been able to earn so much attention in the first place: Most of the world’s other cybercriminals had suddenly become very, very quiet.

## Ransomware Remains Top of Mind in 2022
While ransomware was on the decline in 2022, it was still ranked as the top threat in SonicWall’s inaugural Threat Mindset survey, released in August.

For this survey, SonicWall surveyed customers across a variety of industries located around the globe, asking a series of questions to evaluate the sentiments of those “on the ground” in the war on cybercrime.

When asked what types of cyberattack they’re most concerned about, 91% of respondents answered ransomware. Phishing and spear-phishing, which are often used as vectors for ransomware, were ranked second, with roughly three-quarters of respondents rating them as a concern.

![Image of a bar graph showing the percentage of respondents concerned about different types of cyberattacks. Ransomware 91%, Phishing and spear-phishing 76%, Encrypted malware 66%, File-less attacks 39%, Memory-based malware 24%, Cryptojacking 23%, IoT malware 22%, Side-channel attacks 18%]

> Which types of cyberattacks are you most concerned about?
> www.sonicwall.com
> Source: 2022 SonicWall Threat Mindset Survey.

> WHEN ASKED WHAT TYPES OF CYBERATTACK THEY’RE MOST CONCERNED ABOUT, 91% OF RESPONDENTS ANSWERED RANSOMWARE.

What’s more, 66% of respondents reported being more concerned about attacks this year than last year, with another 29% reporting that they have roughly the same amount of concern about attacks as they did in 2021. Only 5% reported being less concerned.

The survey’s open-ended questions provided a more in-depth look at how respondents were perceiving their risk, along with what they planned to do about it.

“Frankly, I live in terror of a ransomware attack and state-sponsored intrusions. On my logs, I have seen massive increases in probes from Russia, China and a handful of other (what I would call) enemy nations,” a business professional employed at a small business healthcare company said.

Another respondent, an IT director for a financial services business, said that they were doubling down on training in response to the recent increase in attacks.

“The evolving cyber landscape has made us train users a lot more,” they said. “It’s made us spend more on cybersecurity. It scares the hell out of me that an end user can click on something and bring our systems down — even though we’re well protected.”

For more on how SonicWall customers perceive the current state of cybersecurity — and their place in it — download the 2022 SonicWall Threat Mindset Survey.

![Image of a pie chart showing the percentage of respondents who are more, less, or about the same level of concern about cyberattacks in 2022 compared to previous years. More concerned 66%, Less concerned 5%, About the same 29%]

> Are you more or less concerned about cyberattacks in your organization in 2022 than in previous years?
> www.sonicwall.com
> Source: 2022 SonicWall Threat Mindset Survey.

## CVEs
### Published CVEs Break 25,000 for First Time
A total of 26,448 Common Vulnerabilities and Exposures (CVEs) were published in 2022, according to NIST. This marks the sixth year in a row that a record number of vulnerabilities has been discovered, and the first time in history that the number of CVEs has passed 25,000.

While this milestone represents the hard work those in the cybersecurity industry are doing to identify vulnerabilities more quickly and efficiently, it isn’t necessarily cause for celebration. It also reflects the pernicious trends that make quicker and more efficient work necessary in the first place.

As organizations deploy more software and tools, the attack surface continues to grow. And the more products a company utilizes, the more likely it is that one will be vulnerable. (A good example of this is the Apache Log4j vulnerabilities; see page 13)

The most severe vulnerabilities, the ones rated a nine or above on the 10-point scale, become entry points for cybercriminals, and attackers are increasingly utilizing this means of entry to deploy ransomware and other malware and to exfiltrate data.

![Image of a bar graph showing the number of CVEs published each year from 2017 to 2022. 2017: 14,714, 2018: 16,557, 2019: 17,344, 2020: 18,325, 2021: 20,171, 2022: 26,448]

> CVEs by Year
> www.sonicwall.com

| CVE             | VENDOR/PROJECT | PRODUCT                               | TYPE                      |
| :-------------- | :------------- | :------------------------------------ | :------------------------ |
| CVE-2021-44228  | Apache         | Log4j                                 | Remote code execution (RCE) |
| CVE-2021-40539  | Zoho           | ManageEngine AD SelfService Plus      | RCE                       |
| CVE-2021-34523  | Microsoft      | Exchange Server                       | Elevation of privilege     |
| CVE-2021-34473  | Microsoft      | Exchange Server                       | RCE                       |
| CVE-2021-31207  | Microsoft      | Exchange Server                       | Security feature bypass    |
| CVE-2021-27065  | Microsoft      | Exchange Server                       | RCE                       |
| CVE-2021-26858  | Microsoft      | Exchange Server                       | RCE                       |
| CVE-2021-26857  | Microsoft      | Exchange Server                       | RCE                       |
| CVE-2021-26855  | Microsoft      | Exchange Server                       | RCE                       |
| CVE-2021-26084  | Atlassian      | Confluence Server and Data Center     | Arbitrary code execution  |
| CVE-2021-21972  | VMware         | vSphere Client                        | RCE                       |
| CVE-2020-1472   | Microsoft      | Microsoft Netlogon Remote Protocol (MS-NRPC) | Elevation of privilege     |
| CVE-2020-0688   | Microsoft      | Microsoft Exchange Server             | RCE                       |
| CVE-2019-11510  | Ivanti         | Pulse Secure Pulse Connect Secure     | Arbitrary file reading    |
| CVE-2018-13379  | Fortinet       | FortiOS and FortiProxy                | Path traversal            |

> Source: CISA, Top Routinely Exploited Vulnerabilities, 2022 (Alert AA22-117A).

### Top 15 Most Exploited Vulnerabilities
### 2022 Brought Progress in Patching
In July 2022, CISA released its list of top vulnerabilities exploited by criminals in 2021 (Alert AA22-117A), and within it was some encouraging news.

In 2020, each of the top 10 most exploited vulnerabilities had a patch or updated version available. Even so, only two of them were actually discovered in 2020, with some going back as far as 2017. In other words, most cybercriminals weren’t exploiting zero-day vulnerabilities — instead, they were exploiting vulnerabilities that should have been patched months or years before.

The outlook was much better in 2021, however. In this list, all of the top 10 most exploited vulnerabilities were discovered the same year. (We actually had to make our list longer before any from previous years showed up — of these, only a single entry, CVE-2018-13379, appeared on last year’s list.)

While some of these rankings are undoubtedly due to how much the newer vulnerabilities are being exploited (case in point: Log4Shell), the fact that a majority of the old vulnerabilities on the more recent list are not the same old vulnerabilities that were on the 2020 list suggest that we may finally be seeing some progress on the patching front.

### 2022 Zero-Day Vulnerabilities
Of the more than 26,000 vulnerabilities published in 2022, SonicWall Capture Labs threat researchers tracked 35 zero-days being actively exploited in 2022. This is a 150% increase from 2021’s total of 14.

| MONTH     | CVE             | NAME                                                                                               |
| :-------- | :-------------- | :------------------------------------------------------------------------------------------------- |
| January   | CVE-2022-22587  | Apple Memory Corruption Vulnerability                                                               |
| February  | CVE-2022-24086  | Adobe Commerce and Magento Open Source Improper Input Validation Vulnerability                       |
| February  | CVE-2022-22620  | Apple Webkit Remote Code Execution Vulnerability                                                    |
| March     | CVE-2022-1096   | Google Chromium V8 Type Confusion Vulnerability                                                     |
| March     | CVE-2022-22965  | Spring Framework JDK 9+ Remote Code Execution Vulnerability [Spring4Shell]                          |
| March     | CVE-2022-26485  | Mozilla Firefox Use-After-Free Vulnerability                                                        |
| March     | CVE-2022-26486  | Mozilla Firefox Use-After-Free Vulnerability                                                        |
| June      | CVE-2022-26134  | Remote code execution in Atlassian Confluence Server                                                |
| June      | CVE-2022-30190  | Microsoft Windows Support Diagnostic Tool MSDT Remote Code Execution Vulnerability [Follina]        |
| August    | CVE-2022-32893  | Multiple vulnerabilities in Apple macOS Monterey                                                    |
| August    | CVE-2022-32894  | Multiple vulnerabilities in Apple macOS Monterey                                                    |
| August    | CVE-2022-2856   | Multiple vulnerabilities in Google Chrome                                                            |
| September | CVE-2022-3236   | Remote code execution in Sophos Firewall                                                           |
| September | CVE-2022-37969  | Privilege escalation in Microsoft Windows common log file system driver                             |
| September | CVE-2022-40139  | Multiple vulnerabilities in Trend Micro Apex One                                                    |
| September | CVE-2022-32917  | Multiple vulnerabilities in Apple macOS Monterey                                                    |
| September | CVE-2022-3180  | Remote code execution in WPGateway plugin for WordPress                                            |
| September | CVE-2022-31474  | Arbitrary file read in BackupBuddy WordPress plugin                                                 |
| September | CVE-2022-41040  | Microsoft Exchange Server Elevation of Privilege                                                   |
| September | CVE-2022-41082  | Microsoft Exchange Server Remote Code Execution                                                    |
| September | CVE-2022-41352  | Zimbra TAR Remote Code Execution                                                                    |
| September | CVE-2022-3075   | Remote code execution in Google Chrome                                                             |
| October   | CVE-2022-3723   | Remote code execution in Google Chrome                                                             |
| October   | CVE-2022-42827  | Multiple vulnerabilities in Apple iOS 16 and iPadOS 16                                            |
| October   | CVE-2022-41033  | Privilege escalation in Microsoft Windows COM+ Event System Service                                 |
| November  | CVE-2022-4135   | Remote code execution in Google Chrome                                                             |
| November  | CVE-2022-41091  | Multiple vulnerabilities in Microsoft Windows Mark of the Web                                       |
| November  | CVE-2022-41125  | Privilege escalation in Microsoft Windows CNG Key Isolation Service                                 |
| November  | CVE-2022-41128  | Remote code execution in Microsoft Windows Scripting Languages                                      |
| November  | CVE-2022-41073  | Privilege escalation in Microsoft Windows Print Spooler service                                      |
| December  | CVE-2022-42856  | Remote code execution in Apple iOS                                                                 |
| December  | CVE-2022-27518  | Remote code execution in Citrix ADC and Citrix Gateway                                             |
| December  | CVE-2022-44698  | SmartScreen MOTW bypass in Microsoft Windows                                                        |
| December  | CVE-2022-42475  | Remote code execution in FortiOS sslvpnd                                                            |
| December  | CVE-2022-4262   | Remote code execution in Google Chrome                                                             |

## Log4j
### Log4j Intrusion Attempts Surpass 1 Billion
It’s now been more than a year since the announcement of the Apache Log4j vulnerabilities sent shockwaves through the tech community. Since December 2021, SonicWall Capture Labs threat researchers have been tracking attempted exploits of this vulnerability, and so far, attack volumes show no signs of slowing.

SonicWall logged a total of 1.12 billion intrusion attempts against the Log4j vulnerabilities in 2022. While some had hoped for an initial frenzy of attacks followed by a gradual decrease, our researchers have observed the opposite: 61.9 million attempts were observed in December 2021, the month the attacks were announced — and every month in 2022 exceeded that total by at least 10 million.

Worse, these attempts seemed to pick up steam as 2022 went on: The second half of the year had 15% more intrusion attempts than the first half.

### What Are the Log4j Vulnerabilities?
These vulnerabilities affect Log4j, a highly popular Full Open-Source Software (FOSS) logging library with two primary branches, 1.x and 2.x, the former of which is at end of life. This software is used to record, or log, security and performance information. Because the software was widely used, and the Log4j vulnerability existed for eight years before it was announced, the vulnerabilities affect millions of consumer and business products — everything from the Minecraft video game to the Mars 2020 helicopter mission Ingenuity.

![Image of a line graph showing the number of malicious Log4Shell exploit attempts each month from December 2021 to December 2022. The graph shows a general upward trend over the course of the year.]

> Malicious Log4Shell Exploit Attempts
> www.sonicwall.com

### How Attackers Targeted Log4j
Given how widespread and easily exploited these vulnerabilities were, it’s no surprise that threat actors sprang into action almost immediately.

In late December 2021, just weeks after the vulnerabilities were announced, major Vietnamese crypto trading platform ONUS was attacked via a payment system running a vulnerable version of Log4j. Soon after, the attackers threatened to publish ONUS customer data unless they paid a $5 million ransom.

Then in November 2022, a CISA alert warned of attacks by an Iranian government-sponsored APT. This group had exploited the Log4Shell vulnerability to gain access to an unpatched VMware Horizon server in a federal civilian executive branch organization. Once inside, it installed the XMRig cryptominer, moved laterally to the domain controller, compromised credentials, and finally placed Ngrok reverse proxies to maintain persistence.

Campaigns such as these have involved a large variety of malware. A new ransomware family, known as Khonsari, was discovered after it successfully targeted a small group of Minecraft players running servers vulnerable to Log4j. There’s also been a recent resurgence in Mirai botnet malware, this time using vulnerable Log4j deployments to gain initial access to publicly exposed routers, network cameras and other connected devices.

### The Worst May Be Yet to Come
But despite the numerous attacks that occurred in 2022, it’s unlikely we’ve seen the worst of it. First, we still have no idea how many threat actors leveraged the vulnerability shortly after it was disclosed to quickly install backdoors before silently moving