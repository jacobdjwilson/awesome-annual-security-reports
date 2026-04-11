# Global Threat Report 2022

## Table of Contents
- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Threat Landscape Overview](#threat-landscape-overview)
- [2021 Themes](#2021-themes)
- [Ransomware and the Ever-adaptable Adversary](#ransomware-and-the-ever-adaptable-adversary)
- [Iran and the New Face of Disruptive Operations](#iran-and-the-new-face-of-disruptive-operations)
- [China Emerges as Leader in Vulnerability Exploitation](#china-emerges-as-leader-in-vulnerability-exploitation)
- [Log4Shell Sets the Internet on Fire](#log4shell-sets-the-internet-on-fire)
- [Increasing Threats to Cloud Environments](#increasing-threats-to-cloud-environments)
- [Conclusion](#conclusion)
- [Recommendations](#recommendations)
- [About CrowdStrike](#about-crowdstrike)
- [CrowdStrike Products and Services](#crowdstrike-products-and-services)

---

## Foreword

The CrowdStrike 2022 Global Threat Report provides crucial insights into what security teams need to know about to stay ahead of today's threats in an increasingly ominous threat landscape.

For security teams on the front lines and those of us in the business of stopping cyberattacks and breaches, 2021 provided no rest for the weary. In the face of massive disruption brought about by the COVID-driven social, economic and technological shifts of 2020, adversaries refined their tradecraft to become even more sophisticated and brazen. The result was a series of high-profile attacks that rocked many organizations and, on their own, represented watershed moments in cybersecurity.

As organizations scrambled at the start of 2021 to protect supply chains and interconnected systems in the face of the incredibly sophisticated Sunburst attack, adversaries exploited zero-day vulnerabilities and architectural limitations in legacy systems like Microsoft to leave many reeling. At the same time, eCrime syndicates refined and amplified big game hunting (BGH) ransomware attacks that ripped across industries, sowing devastation and sounding the alarm on the frailty of our critical infrastructure.

For security teams already dealing with an ongoing skills shortage, these issues proved challenging enough on their own. But the strain on security teams was amplified even more at the end of the year when the ubiquitous Log4Shell vulnerability threatened a complete security meltdown.

Understanding these events gives visibility into the shifting dynamics of adversary tactics, which is critical for staying ahead of today’s threats. This is the context that the CrowdStrike 2022 Global Threat Report delivers. Developed based on the firsthand observations of our elite CrowdStrike Intelligence and Falcon OverWatch™ teams, combined with insights drawn from the vast telemetry of the CrowdStrike Security Cloud, this year’s report provides crucial insights into what security teams need to know about an increasingly ominous threat landscape.

Enterprise risk is coalescing around three critical areas:
- Endpoints and cloud workloads
- Identity
- Data

Among the details you’ll learn in this year’s report:
- How state-sponsored adversaries targeted IT and cloud service providers to exploit trusted relationships and supply chain partners
- How state-sponsored adversaries weaponized vulnerabilities to evade detection and gain access to critical applications and infrastructure
- How sophisticated adversaries exploited stolen credentials and identities to amplify ransomware BGH attacks and infiltrate cloud environments
- How malicious actors intensified attacks on critical cloud infrastructure with new, sophisticated approaches

Our annual report also paints a picture that shows enterprise risk is coalescing around three critical areas: endpoints and cloud workloads, identity and data. Threat actors continue to exploit vulnerabilities across endpoints and cloud environments, and ramp up innovation on how they use identities and stolen credentials to bypass legacy defenses — all to reach their goal, which is your data. CrowdStrike has observed that 62% of attacks comprise non-malware, hands-on-keyboard activity. As adversaries advance their tradecraft in this manner to bypass legacy security solutions, autonomous machine learning alone is not good enough to stop dedicated attackers.

CrowdStrike is relentless in our drive to keep you ahead of adversaries today and into the future. To meet the adversaries head-on, we’re unifying a modern approach to security with a platform that connects the machine both to the identity and the data to deliver full Zero Trust protection. As adversaries shift to targeting cloud workloads, we’re providing deep visibility and proactive security across the entire cloud-native stack. To alleviate the burden of the constant cycle of patching, we’re prioritizing the vulnerabilities that create the most risk. And for the most sophisticated attacks, we’ve delivered powerful new extended detection and response (XDR) capabilities to help overwhelmed security teams automate response and reduce the time it takes to hunt across domains.

2021 taught us that no matter how much adversity we face, the adversary will not rest. Attacks are growing more destructive, causing mass disruption in all aspects of our daily lives. But this is the challenge we’ve accepted and a fight that we will win together. I hope you find this report informative and that it gives you the same clarity of purpose it gives me: to be unrelenting in our drive to stop adversaries from stopping business and our way of life.

**George Kurtz**
CrowdStrike CEO and Co-Founder

---

## Introduction

In 2021, targeted intrusion adversaries continued to adapt to the changing operational opportunities and strategic requirements of technology and world events.

As we reflect upon 2021, two overarching themes come to the forefront: adaptability and perseverance. Businesses are finding paths forward with new technologies and solutions, adapting in the face of adversity and persevering in spite of uncertainty as we continue to navigate the challenges of living through a global pandemic. While these issues will ultimately lead to strength and innovation in organizations around the world, they will also create new risks and vulnerabilities that can be exploited.

Cyber adversaries kept pace in 2021 with many adapting to a changing target landscape. This trend was perhaps best exemplified by the shifts observed in the 2021 eCrime ecosystem, which — while remaining vast and interconnected — comprises many criminal enterprises that exist to support big game hunting (BGH) ransomware operations. Notably, adversaries in 2021 were able to circumvent actions that threatened cessation of their operations, and some even resorted to rebranding as a result. Despite new approaches taken by law enforcement, including attempts to seize ransom payments and criminal funds before they reached adversaries’ hands, CrowdStrike Intelligence observed an 82% increase in ransomware-related data leaks in 2021, compared to 2020. This increase, coupled with other data leaks, is a stark reminder of the value that adversaries place on victim data.

In 2021, targeted intrusion adversaries continued to adapt to the changing operational opportunities and strategic requirements of technology and world events. Russian, Chinese, Iranian and North Korean adversaries were all observed employing new tradecraft or target-scopes meant to respond to global trends. This included: Russia’s targeting of IT and cloud service providers to exploit trusted relationships; China’s weaponization of vulnerabilities at scale to facilitate initial access efforts; Iran’s use of ransomware to blend disruptive operations with authentic eCrime activity; and Democratic People's Republic of Korea’s (DPRK) shift to cryptocurrency-related entities in an effort to maintain illicit revenue generation during economic disruptions caused by the pandemic.

![Infographic showing 21 newly named adversaries, 45% increase in interactive intrusion campaigns, 170+ total adversaries tracked, and 82% increase in ransomware-related data leaks.]

Governments are also adapting. This year, CrowdStrike Intelligence debuted two new adversary animals — WOLF and OCELOT — to label targeted intrusions emanating from Turkey and Colombia, respectively. The presence of these new adversaries underscores the increase in offensive capabilities outside of governments traditionally associated with cyber operations, and highlights the variety of actor end goals. Private sector offensive actors (PSOAs), such as NSO Group and Candiru, continued to serve as hackers-for-hire throughout 2021, providing governments with substitute or supplemental capabilities and further enlarging the global actor space.

In the hacktivist landscape, CrowdStrike Intelligence observed the continued development of grassroots operations and a proliferation of established hacktivist groups across the world. The rise of Belarusian group Cyber Partisans since late 2020, the expanded role and diversification of the broader Iranian hacktivist ecosystem, and the growing participation of various hacktivists in response to Western political developments all exemplify this trend.

As our adversaries adapt, so do we. CrowdStrike Intelligence offered an unparalleled level of coverage throughout 2021, adding 21 named adversaries and raising the total of tracked actors across all motivations to over 170. CrowdStrike Intelligence continues to expand coverage of threat landscapes beyond targeted intrusion, eCrime and hacktivist mission areas; in 2021, we increased support for vulnerability intelligence and mobile intelligence across all our products.

In 2021, CrowdStrike launched Falcon X Recon+ as a companion service for Falcon X Recon™. Falcon X Recon+ analysts manage monitoring, triaging, assessing and mitigating threats across the criminal underground. They also assess and recommend effective mitigation steps, helping customers act decisively and proactively to prevent and detect future attacks. CrowdStrike's Falcon X Elite service was also expanded in 2021 to provide a single point of contact for onboarding, product integration, intelligence clarification, personalized threat briefing and intelligence research. Falcon X Elite analysts continue to provide proactive notifications of threats to CrowdStrike customer organizations.

The CrowdStrike 2022 Global Threat Report summarizes the entirety of analysis performed by the CrowdStrike Intelligence team throughout 2021, including descriptions of notable themes, trends and significant events in cybersecurity. This analysis, combined with case studies from the Falcon OverWatch™ managed threat hunting team, demonstrates how threat intelligence and proactive hunting can provide a deeper understanding of the motives, objectives and activities of these actors — information that can empower swift proactive countermeasures to better defend your valuable data now and in the future.

---

## Naming Conventions
This report follows the naming conventions instituted by CrowdStrike to categorize adversaries according to their nation-state affiliations or motivations. The following is a guide to these adversary naming conventions.

| Adversary | Nation-state or Category |
| :--- | :--- |
| BEAR | RUSSIA |
| BUFFALO | VIETNAM |
| CHOLLIMA | DPRK (NORTH KOREA) |
| CRANE | ROK (REPUBLIC OF KOREA) |
| JACKAL | HACKTIVIST |
| KITTEN | IRAN |
| LEOPARD | PAKISTAN |
| LYNX | GEORGIA |
| OCELOT | COLOMBIA |
| PANDA | PEOPLE’S REPUBLIC OF CHINA |
| SPIDER | ECRIME |
| TIGER | INDIA |
| WOLF | TURKEY |

---

## Threat Landscape Overview

### eCrime Breakout Time: 1 hour 38 minutes
Today’s eCrime adversaries move with speed and purpose in pursuit of their objectives.

The CrowdStrike Falcon OverWatch team measures breakout time — the time an adversary takes to move laterally from an initially compromised host to another host within the victim environment. Our analysis of the breakout time for hands-on eCrime intrusion activity in 2021 — where such a metric could be derived — revealed an average of just 1 hour 38 minutes.

This number is essentially unchanged from what was reported by CrowdStrike’s Falcon OverWatch team in the CrowdStrike 2021 Threat Hunting Report, when breakout time for eCrime actors was measured at 1 hour 32 minutes. eCrime adversaries continue to show a high degree of sophistication as evidenced by the speed at which they can move through a victim environment, leaving a very short window for defenders to respond.

### Adversary Tactics
Detections indexed by the CrowdStrike Security Cloud in Q4 2021:
- **Malware-Free**: 62%
- **Malware**: 38%

Adversaries continue to show that they have moved beyond malware. Attackers are increasingly attempting to accomplish their objectives without writing malware to the endpoint. Rather, they have been observed using legitimate credentials and built-in tools — an approach known as “living off the land” (LOTL) — in a deliberate effort to evade detection by legacy antivirus products. Of all detections indexed by the CrowdStrike Security Cloud in the fourth quarter of 2021, 62% were malware-free.

In 2021, OverWatch tracked steadily increasing numbers of interactive intrusion campaigns. Compared to 2020, OverWatch observed a near 45% increase in the number of such campaigns, and uncovered more in the fourth quarter than in any other quarter.

![Figure 1: Quarterly Growth in Interactive Intrusion Campaigns by Threat Type, Q1 2020 to Q4 2021]

Financially motivated eCrime activity continues to dominate the interactive intrusion attempts tracked by OverWatch. Intrusions attributed to eCrime accounted for nearly half (49%) of the observed activity, while targeted intrusions accounted for 18%, hacktivist activity was responsible for 1% and the remaining 32% of attacks remain unattributed. The distribution of these figures is similar to that of 2020.

---

## 2021 Themes

### Ransomware and the Ever-adaptable Adversary
The growth and impact of BGH in 2021 was a palpable force felt across all sectors and in nearly every region of the world. Although some adversaries and ransomware ceased operations in 2021, the overall number of operating ransomware families increased. CrowdStrike Intelligence observed an 82% increase in ransomware-related data leaks in 2021, with 2,686 attacks as of Dec. 31, 2021, compared to 1,474 in 2020. These figures, coupled with other data leaks, highlight how valuable victim data is to adversaries.

![Figure 2: Number of Ransomware-related Attacks Leading to Data Leaks, 2020 vs. 2021]
![Figure 3: Comparison of Data Leaks by Sector (Top 10), 2020 vs. 2021]

At times, the BGH landscape has been unpredictable, and adversaries have not always been able to immediately gauge the success or outcome of their ransomware operations. This change in landscape fluidity was observed following operations that targeted large organizations and resulted in attention and action from the highest levels of U.S. government and law enforcement, causing some adversaries to rebrand or even deactivate their tools.

The impact of government and law enforcement action on eCrime operations was also observed in the CrowdStrike eCrime Index (ECX). For example, increased media and law enforcement attention after the Colonial Pipeline and JBS Foods incidents conducted by CARBON SPIDER and PINCHY SPIDER affiliates resulted in a reduction in data leaks and access broker advertisements, which caused the ECX to dip, recover and remain volatile to date.

New tactics, techniques and procedures (TTPs) used in data theft attacks in 2021 aided adversaries in extorting their victims. For example, adversaries such as BITWISE SPIDER avoided using publicly available exfiltration tools by developing their own. Another major development was increased data theft and extortion without the use of ransomware, leading to the establishment of new marketplaces dedicated to advertising and selling victim data.

However, one key theme highlighted throughout 2021 is that adversaries will continue to react and move operations to new approaches or malware wherever possible, demonstrating that the ever-adaptable adversary remains the key threat within the eCrime landscape.

#### Case Study: WIZARD SPIDER Accesses Multiple Servers During Targeted BGH Operation
WIZARD SPIDER was a prolific figure on the ransomware scene in 2021. With a wealth of custom tooling at their disposal and proficiency at using native utilities to progress their intrusions, WIZARD SPIDER identified and developed a successful business model. OverWatch uncovered this threat actor in an intrusion against an organization in the engineering vertical. The TTPs observed throughout this intrusion were consistent with targeted BGH activity seen from WIZARD SPIDER in the past. The intrusion spanned four domain controllers and two valid accounts.

- **Defense Evasion and Discovery**: WIZARD SPIDER utilized RDP to authenticate into a Windows Domain Controller via a valid domain account. The Falcon sensor raised the first of multiple detections when malware was injected into the legitimate MSTSC process by a custom shellcode loader, ShellStarter.
- **Command and Control (C2)**: The actor pushed a rogue DLL file to another server before executing the DLL using the Microsoft signed binary Rundll32. In this instance, the WIZARD SPIDER tool, AnchorDNS, was used to perform C2 connections over the DNS protocol.
- **Credential Access**: Minutes later, WIZARD SPIDER moved laterally using RDP to access a second domain controller using the same valid credentials. Here they used the built-in Ntdsutil utility to harvest credentials by copying the NTDS database.
- **Lateral Movement**: WIZARD SPIDER moved laterally to a third domain controller through a Windows administrative share and set AnchorDNS to run as a service using native tooling.
- **Persistence**: Acting on CrowdStrike's notifications, the victim organization’s incident response took over at this point and began eliminating the actor within the environment. During remediation, OverWatch identified WIZARD SPIDER returning to a fourth domain controller using a new administrator account.

---

### Iran and the New Face of Disruptive Operations
Since late 2020, multiple Iran-nexus adversaries and activity clusters have adopted the use of ransomware as well as “lock-and-leak” disruptive information operations (IO) to target multiple organizations within the U.S., Israel and the greater Middle East and North Africa (MENA) region. Lock-and-leak operations are characterized by criminal or hacktivist fronts using ransomware to encrypt target networks and subsequently leak victim information via actor-controlled personas or entities.

At present, CrowdStrike Intelligence is tracking several adversaries and activity clusters that are engaged in lock-and-leak operations. Based on available data, PIONEER KITTEN was the first adversary to switch from conducting likely traditional targeted intrusion operations to lock-and-leak activities in 2021. Following that, SPECTRAL KITTEN (aka BlackShadow), the ChaoticOrchestra activity cluster (aka Deus) and the SplinteredEnvoy activity cluster (aka Moses Staff) were observed primarily targeting Israeli entities with lock-and-leak operations throughout 2021 using multiple ransomware families.

In contrast to the publicity-seeking operations and lock-and-leak campaigns observed throughout 2021, disruptive activity associated with the NEMESIS KITTEN adversary lacked a distinct messaging component and largely operated discreetly.

#### Case Study: NEMESIS KITTEN Thwarted at Every Turn
In late 2021, OverWatch uncovered a hands-on intrusion against a South American technology entity. The observed TTPs, along with the use of specific tooling including the Fatedier Reverse Proxy tool, were consistent with activity previously attributed to the threat actor tracked by CrowdStrike Intelligence as NEMESIS KITTEN. The actor’s efforts were largely unsuccessful because they were blocked at every turn by the Falcon sensor.

- **Defense Evasion**: The actor was observed making numerous attempts to disable Windows Defender, including modifying the Windows registry to disable Windows Defender real-time monitoring.
- **Persistence and C2**: The actor attempted to create a scheduled task to download and execute the Fatedier Reverse Proxy tool. This attempt was prevented by the Falcon sensor.
- **Discovery**: After the failed attempts to establish persistence and C2, NEMESIS KITTEN undertook host and user reconnaissance.
- **Credential Access**: Finally, the actor attempted to perform credential harvesting by modifying the registry to enable WDigest and allow for the storage of credentials in plain text. This attempt proved unsuccessful as well.

---

### China Emerges as Leader in Vulnerability Exploitation
CrowdStrike Intelligence observed China-nexus actors deploying exploits for new vulnerabilities at a significantly elevated rate in 2021, when compared to 2020.

In 2020, CrowdStrike Intelligence confirmed the exploitation by China-nexus actors — including WICKED PANDA — of two vulnerabilities published in 2020. In 2021, CrowdStrike Intelligence confirmed China-nexus actor exploitation of 12 vulnerabilities published in 2021, affecting nine different products.

Chinese actors have long developed and deployed exploits to facilitate targeted intrusion operations; however, 2021 highlighted a shift in their preferred exploitation methods. For years, Chinese actors relied on exploits that required user interaction. In contrast, exploits deployed by these actors in 2021 focused heavily on vulnerabilities in internet-facing devices or services.

![Figure 4: Timeline of Zero-day Exploits Deployed by China-nexus Actors in 2021]

#### Case Study: Suspected PANDA Exploits Microsoft Exchange Server Vulnerabilities Against Think Tank
Falcon OverWatch uncovered a targeted threat actor conducting a hands-on intrusion against a Europe-based think tank. The activity, which spanned multiple Windows-based hosts, began after the successful exploitation of a known Microsoft Exchange vulnerability.

- **Initial Access**: The adversary gained initial access to the primary host following the successful compromise of the Microsoft Exchange application pool MSExchangeOWAAppPool.
- **Persistence and Lateral Movement**: In a likely attempt to preserve access, the adversary deployed implants across several hosts and attempted execution using trusted utilities including the Microsoft .NET ClickOne Launch Utility and Rundll32.
- **Credential Access**: The adversary attempted multiple LOTL techniques to extract the contents of the LSASS memory space and seek credential information stored in files.

---

### Log4Shell Sets the Internet on Fire
Routine discovery, disclosure and subsequent exploitation of a series of high-profile vulnerabilities occurred throughout 2021. Due to the number of potentially affected endpoints, Log4Shell received more attention than any other vulnerability.

Apache’s Log4j2 is an ubiquitous logging library used by many web applications. A vulnerability reported in November 2021 and tracked as CVE-2021-44228 and “Log4Shell” can be exploited by remote attackers to inject arbitrary Java code into affected services.

Between Dec. 9-31, 2021, a variety of groups incorporated Log4Shell exploitation into their arsenal. Opportunistic eCrime actors aggressively engaged in widespread Log4Shell exploitation most commonly affiliated with commodity botnet malware (e.g., Muhstik). However, other eCrime-focused actors — including affiliates of DOPPEL SPIDER and WIZARD SPIDER — adopted Log4Shell as an access vector to enable ransomware operations.

![Figure 5: Timeline of Log4Shell Events and Affiliated Actors]

CrowdStrike Intelligence assesses that actors will continue to integrate increasingly effective exploit chains to rapidly achieve RCE. This assessment is made with moderate confidence based on the substantial number of incidents facilitated by multistage exploit chains — such as ProxyShell and ProxyLogon — that proved commonplace during 2021.

---

### Increasing Threats to Cloud Environments
Cloud-based services now form crucial elements of many business processes, easing file sharing and collaboration. However, these same services are increasingly abused by malicious actors in the course of computer network operations (CNO). Common cloud attack vectors used by eCrime and targeted intrusion adversaries include cloud vulnerability exploitation, credential theft, cloud service provider abuse, use of cloud services for malware hosting and C2, and the exploitation of misconfigured image containers.

- **Cloud Vulnerability Exploitation**: Malicious actors tend to opportunistically exploit known RCE vulnerabilities in server software. VMware has also been targeted by threat actors, including CVE-2021-21972.
- **Credential Theft**: Credential-based intrusions against cloud environments are among the more prevalent exploitation vectors. Criminal actors routinely host fake authentication pages to harvest legitimate authentication credentials.
- **Cloud Service Provider Abuse**: Adversaries have leveraged cloud service providers to abuse provider trust relationships and gain access to additional targets through lateral movement from enterprise authentication assets hosted on cloud infrastructure.
- **Exploitation of Misconfigured Image Containers**: Criminal actors have periodically exploited improperly configured Docker containers. In 2021, CrowdStrike Intelligence reported on the malware family Doki, which uses containers as both an initial infection vector and as a means for parallel track tasking.

---

## Conclusion
In 2021, CrowdStrike Intelligence observed adversaries continue to adapt to security environments impacted by the ongoing COVID pandemic. These adversaries are likely to look at novel ways in which they can bypass security measures to conduct successful initial infections, impede analysis by researchers and continue tried-and-tested techniques into 2022.

BGH operations will continue to dominate the eCrime landscape in 2022, likely significantly increasing their use of ransomware from ransomware-as-a-service (RaaS) operations. Targeted intrusion adversaries are expected to continue to capitalize on trends in technology and the broader threat landscape throughout 2022 in attempts to maximize impacts while minimizing effort.

In response to these evolving threats, CrowdStrike Intelligence continues to provide industry-leading actor profiles, malware analysis and campaign tracking through its suite of reporting products and coverage of threat landscapes spanning targeted intrusion, eCrime, hacktivist, vulnerability and mobile threat intelligence.

---

## Recommendations
1. **Protect All Workloads**: Secure all critical areas of enterprise risk: endpoints and cloud workloads, identity and data.
2. **Know Your Adversary**: If you know the adversaries that target the industry or the geolocation your organization resides in, you can prepare yourself to better defend against the tools and tactics they employ.
3. **Be Ready When Every Second Counts**: Security teams of all sizes must invest in speed and agility for their daily and tactical decision making by automating preventive, detection, investigative and response workflows.
4. **Stop Modern Attacks**: Nearly 80% of cyberattacks leverage identity-based attacks. Use advanced AI and behavioral analytics to enforce risk-based conditional access.
5. **Adopt Zero Trust**: Connect the machine to the identity and the data to deliver full Zero Trust protection.
6. **Monitor the Criminal Underground**: Leverage digital risk monitoring tools like Falcon X Recon to monitor imminent threats to your brand, identities or data.
7. **Eliminate Misconfigurations**: Set up new infrastructure with default patterns that make secure operations easy to adopt.
8. **Invest in Elite Threat Hunting**: The combination of technology with expert threat hunters is mandatory to see and stop the most sophisticated threats.
9. **Build a Cybersecurity Culture**: Initiate user awareness programs to combat phishing and social engineering.

---

## About CrowdStrike
CrowdStrike Holdings, Inc. (Nasdaq: CRWD), a global cybersecurity leader, has redefined modern security with the world’s most advanced cloud-native platform for protecting critical areas of enterprise risk-endpoints and cloud workloads, identity and data.

---

## CrowdStrike Products and Services
- **Endpoint Security**: Falcon XDR, Falcon Insight, Falcon Prevent, Falcon Firewall Management, Falcon Device Control.
- **Threat Intelligence**: Falcon X, Falcon X Premium, Falcon X Recon, Falcon Sandbox.
- **Managed Services**: Falcon OverWatch, Falcon Complete.
- **Cloud Security**: Falcon Cloud Workload Protection, Falcon Horizon.
- **Security and IT Operations**: Falcon Discover, Falcon Spotlight, Falcon FileVantage, Falcon Forensics.
- **Identity Protection**: Falcon Identity Threat Detection, Falcon Identity Threat Protection.
- **Log Management**: Humio.
- **Services**: CrowdStrike Services (IR and Proactive).