# CrowdStrike 2022 Global Threat Report

## Table of Contents
- [Foreword](#foreword)
- [Enterprise risk is coalescing around three critical areas: Endpoints and cloud workloads, Identity, Data](#enterprise-risk-is-coalescing-around-three-critical-areas-endpoints-and-cloud-workloads-identity-data)
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

George Kurtz
CrowdStrike CEO and Co-Founder

---

## Introduction

In 2021, targeted intrusion adversaries continued to adapt to the changing operational opportunities and strategic requirements of technology and world events.

As we reflect upon 2021, two overarching themes come to the forefront: adaptability and perseverance. Businesses are finding paths forward with new technologies and solutions, adapting in the face of adversity and persevering in spite of uncertainty as we continue to navigate the challenges of living through a global pandemic. While these issues will ultimately lead to strength and innovation in organizations around the world, they will also create new risks and vulnerabilities that can be exploited.

Cyber adversaries kept pace in 2021 with many adapting to a changing target landscape. This trend was perhaps best exemplified by the shifts observed in the 2021 eCrime ecosystem, which — while remaining vast and interconnected — comprises many criminal enterprises that exist to support big game hunting (BGH) ransomware operations. Notably, adversaries in 2021 were able to circumvent actions that threatened cessation of their operations, and some even resorted to rebranding as a result. Despite new approaches taken by law enforcement, including attempts to seize ransom payments and criminal funds before they reached adversaries’ hands, CrowdStrike Intelligence observed an 82% increase in ransomware-related data leaks in 2021, compared to 2020. This increase, coupled with other data leaks, is a stark reminder of the value that adversaries place on victim data.

In 2021, targeted intrusion adversaries continued to adapt to the changing operational opportunities and strategic requirements of technology and world events. Russian, Chinese, Iranian and North Korean adversaries were all observed employing new tradecraft or target-scopes meant to respond to global trends. This included: Russia’s targeting of IT and cloud service providers to exploit trusted relationships; China’s weaponization of vulnerabilities at scale to facilitate initial access efforts; Iran’s use of ransomware to blend disruptive operations with authentic eCrime activity; and Democratic People's Republic of Korea’s (DPRK) shift to cryptocurrency-related entities in an effort to maintain illicit revenue generation during economic disruptions caused by the pandemic.

![Image description: A graphic showing key statistics from 2021: 21 newly named adversaries, 45% increase in interactive intrusion campaigns, 170+ total adversaries tracked, and 82% increase in ransomware-related data leaks.](image_description_1.png)

Governments are also adapting. This year, CrowdStrike Intelligence debuted two new adversary animals — WOLF and OCELOT — to label targeted intrusions emanating from Turkey and Colombia, respectively. The presence of these new adversaries underscores the increase in offensive capabilities outside of governments traditionally associated with cyber operations, and highlights the variety of actor end goals. Private sector offensive actors (PSOAs), such as NSO Group and Candiru, continued to serve as hackers-for-hire throughout 2021, providing governments with substitute or supplemental capabilities and further enlarging the global actor space.

In the hacktivist landscape, CrowdStrike Intelligence observed the continued development of grassroots operations and a proliferation of established hacktivist groups across the world. The rise of Belarusian group Cyber Partisans since late 2020, the expanded role and diversification of the broader Iranian hacktivist ecosystem, and the growing participation of various hacktivists in response to Western political developments all exemplify this trend.

As our adversaries adapt, so do we. CrowdStrike Intelligence offered an unparalleled level of coverage throughout 2021, adding 21 named adversaries and raising the total of tracked actors across all motivations to over 170. CrowdStrike Intelligence continues to expand coverage of threat landscapes beyond targeted intrusion, eCrime and hacktivist mission areas; in 2021, we increased support for vulnerability intelligence and mobile intelligence across all our products.

In 2021, CrowdStrike launched Falcon X Recon+ as a companion service for Falcon X Recon™. Falcon X Recon+ analysts manage monitoring, triaging, assessing and mitigating threats across the criminal underground. They also assess and recommend effective mitigation steps, helping customers act decisively and proactively to prevent and detect future attacks. CrowdStrike's Falcon X Elite service was also expanded in 2021 to provide a single point of contact for onboarding, product integration, intelligence clarification, personalized threat briefing and intelligence research. Falcon X Elite analysts continue to provide proactive notifications of threats to CrowdStrike customer organizations.

The CrowdStrike 2022 Global Threat Report summarizes the entirety of analysis performed by the CrowdStrike Intelligence team throughout 2021, including descriptions of notable themes, trends and significant events in cybersecurity. This analysis, combined with case studies from the Falcon OverWatch™ managed threat hunting team, demonstrates how threat intelligence and proactive hunting can provide a deeper understanding of the motives, objectives and activities of these actors — information that can empower swift proactive countermeasures to better defend your valuable data now and in the future.

---

## Naming Conventions

This report follows the naming conventions instituted by CrowdStrike to categorize adversaries according to their nation-state affiliations or motivations. The following is a guide to these adversary naming conventions.

| Adversary | Nation-state or Category |
|---|---|
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

### eCrime Breakout Time

**1 hour 38 minutes**

Today’s eCrime adversaries move with speed and purpose in pursuit of their objectives.

The CrowdStrike Falcon OverWatch team measures breakout time — the time an adversary takes to move laterally from an initially compromised host to another host within the victim environment. Our analysis of the breakout time for hands-on eCrime intrusion activity in 2021 — where such a metric could be derived — revealed an average of just 1 hour 38 minutes.

This number is essentially unchanged from what was reported by CrowdStrike’s Falcon OverWatch team in the CrowdStrike 2021 Threat Hunting Report, when breakout time for eCrime actors was measured at 1 hour 32 minutes. eCrime adversaries continue to show a high degree of sophistication as evidenced by the speed at which they can move through a victim environment, leaving a very short window for defenders to respond.

### Adversary Tactics

Detections indexed by the CrowdStrike Security Cloud in Q4 2021

![Image description: A pie chart showing that 62% of detections were malware-free and 38% involved malware.](image_description_2.png)

Adversaries continue to show that they have moved beyond malware.

62% Malware-Free
38% Malware

Attackers are increasingly attempting to accomplish their objectives without writing malware to the endpoint. Rather, they have been observed using legitimate credentials and built-in tools — an approach known as “living off the land” (LOTL) — in a deliberate effort to evade detection by legacy antivirus products. Of all detections indexed by the CrowdStrike Security Cloud in the fourth quarter of 2021, 62% were malware-free.

In 2021, OverWatch tracked steadily increasing numbers of interactive intrusion campaigns. Compared to 2020, OverWatch observed a near 45% increase in the number of such campaigns, and uncovered more in the fourth quarter than in any other quarter.

![Image description: A line graph showing the quarterly growth in interactive intrusion campaigns by threat type from Q1 2020 to Q4 2021. The graph shows a general upward trend in interactive intrusion campaigns, with eCrime and unattributed campaigns being the most prevalent.](image_description_3.png)

**Types of Threat Activity**
- **eCrime**: Financially motivated criminal intrusion activity
- **Targeted**: State-sponsored intrusion activity that includes cyber espionage, state-nexus destruction attacks and generating currency to support a regime
- **Hacktivist**: Intrusion activity undertaken to gain momentum, visibility or publicity for a cause or ideology
- **Unattributed**: Insufficient data were available to make a confident attribution

Financially motivated eCrime activity continues to dominate the interactive intrusion attempts tracked by OverWatch. Intrusions attributed to eCrime accounted for nearly half (49%) of the observed activity, while targeted intrusions accounted for 18%, hacktivist activity was responsible for 1% and the remaining 32% of attacks remain unattributed. The distribution of these figures is similar to that of 2020.

![Image description: A bar chart comparing interactive intrusion campaigns by threat type for 2020 and 2021. In 2021, eCrime accounted for 49%, targeted for 18%, hacktivist for 1%, and unattributed for 32%. In 2020, eCrime accounted for 52%, targeted for 32%, hacktivist for 1%, and unattributed for 13%.](image_description_4.png)

---

## 2021 Themes

### Ransomware and the Ever-adaptable Adversary

The growth and impact of BGH in 2021 was a palpable force felt across all sectors and in nearly every region of the world. Although some adversaries and ransomware ceased operations in 2021, the overall number of operating ransomware families increased. CrowdStrike Intelligence observed an 82% increase in ransomware-related data leaks in 2021, with 2,686 attacks as of Dec. 31, 2021, compared to 1,474 in 2020. These figures, coupled with other data leaks, highlight how valuable victim data is to adversaries.

![Image description: A bar chart showing the number of ransomware-related attacks leading to data leaks from 2020 to 2021. In 2020, there were 1,474 attacks, and in 2021, there were 2,686 attacks, an 82% increase.](image_description_5.png)

![Image description: A bar chart comparing data leaks by sector for the top 10 sectors in 2020 and 2021. The chart shows a general increase in data leaks across most sectors from 2020 to 2021.](image_description_6.png)

At times, the BGH landscape has been unpredictable, and adversaries have not always been able to immediately gauge the success or outcome of their ransomware operations. This change in landscape fluidity was observed following operations that targeted large organizations and resulted in attention and action from the highest levels of U.S. government and law enforcement, causing some adversaries to rebrand or even deactivate their tools.

The impact of government and law enforcement action on eCrime operations was also observed in the CrowdStrike eCrime Index (ECX). For example, increased media and law enforcement attention after the Colonial Pipeline and JBS Foods incidents conducted by CARBON SPIDER and PINCHY SPIDER affiliates resulted in a reduction in data leaks and access broker advertisements, which caused the ECX to dip, recover and remain volatile to date. For more detail, read this blog.

New tactics, techniques and procedures (TTPs) used in data theft attacks in 2021 aided adversaries in extorting their victims. For example, adversaries such as BITWISE SPIDER avoided using publicly available exfiltration tools by developing their own. Another major development was increased data theft and extortion without the use of ransomware, leading to the establishment of new marketplaces dedicated to advertising and selling victim data.

However, one key theme highlighted throughout 2021 is that adversaries will continue to react and move operations to new approaches or malware wherever possible, demonstrating that the ever-adaptable adversary remains the key threat within the eCrime landscape.

#### WIZARD SPIDER Accesses Multiple Servers During Targeted BGH Operation

WIZARD SPIDER was a prolific figure on the ransomware scene in 2021. With a wealth of custom tooling at their disposal and proficiency at using native utilities to progress their intrusions, WIZARD SPIDER identified and developed a successful business model. OverWatch uncovered this threat actor in an intrusion against an organization in the engineering vertical. The TTPs observed throughout this intrusion were consistent with targeted BGH activity seen from WIZARD SPIDER in the past. The intrusion spanned four domain controllers and two valid accounts.

![Image description: A diagram illustrating the steps of a WIZARD SPIDER intrusion, including Defense Evasion and Discovery, Command and Control (C2), Persistence, Credential Access, and Lateral Movement. The diagram shows the adversary accessing multiple domain controllers.](image_description_7.png)

**Case Study**
Falcon OverWatch

---

### Iran and the New Face of Disruptive Operations

Since late 2020, multiple Iran-nexus adversaries and activity clusters have adopted the use of ransomware as well as “lock-and-leak” disruptive information operations (IO) to target multiple organizations within the U.S., Israel and the greater Middle East and North Africa (MENA) region. Lock-and-leak operations are characterized by criminal or hacktivist fronts using ransomware to encrypt target networks and subsequently leak victim information via actor-controlled personas or entities. Since they inauthentically operate as a criminal or hacktivist entity, these types of operations conduct activity beneath a veneer of deniability. Through the use of dedicated leak sites, social media and chat platforms, these actors are able to amplify data leaks and conduct IO against target countries.

At present, CrowdStrike Intelligence is tracking several adversaries and activity clusters that are engaged in lock-and-leak operations. Based on available data, PIONEER KITTEN was the first adversary to switch from conducting likely traditional targeted intrusion operations to lock-and-leak activities in 2021. Following that, SPECTRAL KITTEN (aka BlackShadow), the ChaoticOrchestra activity cluster (aka Deus) and the SplinteredEnvoy activity cluster (aka Moses Staff) were observed primarily targeting Israeli entities with lock-and-leak operations throughout 2021 using multiple ransomware families.

In contrast to the publicity-seeking operations and lock-and-leak campaigns observed throughout 2021, disruptive activity associated with the NEMESIS KITTEN adversary lacked a distinct messaging component and largely operated discreetly. NEMESIS KITTEN conducted wide-ranging scanning and exploitation operations to establish footholds in various networks, and in select instances, conducted ransomware operations using BitLocker, a likely unique ransomware variant called SunDawn, and, in one case, a custom wiper.

The use of high-profile lock-and-leak operations, as well as the more subdued but pervasive NEMESIS KITTEN activity, provides Iran with an effective capability to disruptively target its rivals in the region and abroad. Given the success of these operations, Iran will likely continue to use disruptive ransomware into 2022.

#### NEMESIS KITTEN Thwarted at Every Turn

In late 2021, OverWatch uncovered a hands-on intrusion against a South American technology entity. The observed TTPs, along with the use of specific tooling including the Fatedier Reverse Proxy tool, were consistent with activity previously attributed to the threat actor tracked by CrowdStrike Intelligence as NEMESIS KITTEN. The actor’s efforts were largely unsuccessful because they were blocked at every turn by the Falcon sensor.

![Image description: A diagram illustrating the steps of a NEMESIS KITTEN intrusion, including Defense Evasion, Discovery, Persistence and C2, Credential Access, and Lateral Movement. The diagram shows multiple attempted attack techniques blocked by the Falcon sensor.](image_description_8.png)

**Case Study**
Falcon OverWatch

---

### China Emerges as Leader in Vulnerability Exploitation

CrowdStrike Intelligence observed China-nexus actors deploying exploits for new vulnerabilities at a significantly elevated rate in 2021, when compared to 2020.

In 2020, CrowdStrike Intelligence confirmed the exploitation by China-nexus actors — including WICKED PANDA — of two vulnerabilities published in 2020: CVE-2020-14882 (Oracle WebLogic) and CVE-2020-10189 (Zoho ManageEngine). In 2021, CrowdStrike Intelligence confirmed China-nexus actor exploitation of 12 vulnerabilities published in 2021, affecting nine different products. Ten named adversaries or activity clusters were linked to the exploitation of these vulnerabilities and a number of other incidents were identified in which activity was likely linked to unnamed Chinese actors.

Chinese actors have long developed and deployed exploits to facilitate targeted intrusion operations; however, 2021 highlighted a shift in their preferred exploitation methods. For years, Chinese actors relied on exploits that required user interaction, whether by opening malicious documents or other files attached to emails or visiting websites hosting malicious code. In contrast, exploits deployed by these actors in 2021 focused heavily on vulnerabilities in internet-facing devices or services.

![Image description: A timeline showing the timeline of zero-day exploits deployed by China-nexus actors in 2021. It highlights the exploitation of 12 published vulnerabilities in 2021 compared to 2 in 2020.](image_description_9.png)

In 2021, Chinese actors focused significant attention on a series of vulnerabilities in Microsoft Exchange — now collectively known as ProxyLogon and ProxyShell — and used them to launch intrusions against numerous organizations worldwide. Chinese adversaries also continued to exploit internet-routing products such as VPNs and routers for both infrastructure acquisition and initial access purposes. Enterprise software products hosted on internet-facing servers were also popular targets. CrowdStrike Intelligence observed Chinese actors exploit products for initial access in a range of intrusions such as Zoho ManageEngine, Atlassian Confluence and GitLab.¹

Activity from China-nexus actors in 2021 highlighted their range of exploit-acquisition capabilities. Chinese targeted intrusion actors likely independently developed a number of the observed exploits or acquired them from in-country security researchers. In particular, the Tianfu Cup hacking competition demonstrates the significant exploitation development talent within China’s hacker community. Exploits submitted at the Tianfu Cup have later been acquired by Chinese targeted intrusion actors for use in their operations. In several 2021 incidents, Chinese actors demonstrated an ability to rapidly operationalize public proof-of-concept (POC) exploit code for newly acknowledged vulnerabilities.

![Image description: A timeline of zero-day exploits deployed by China-nexus actors in 2021.](image_description_10.png)

¹ Relevant zero-day vulnerabilities exploited in connection to this activity affected Zoho ManageEngine (CVE-2021-40539, CVE-2021-44515 and CVE-2021-440077), Atlassian Confluence (CVE-2021-26084) and GitLab (CVE-2021-22205).

#### Suspected PANDA Exploits Microsoft Exchange Server Vulnerabilities Against Think Tank

Falcon OverWatch uncovered a targeted threat actor conducting a hands-on intrusion against a Europe-based think tank. The activity, which spanned multiple Windows-based hosts, began after the successful exploitation of a known Microsoft Exchange vulnerability. The adversary employed several notable TTPs in an effort to secure a persistent foothold in the victim environment. The adversary also showed a particular interest in gathering credential information, using four distinct credential dumping and harvesting techniques.

![Image description: A diagram illustrating the steps of a suspected PANDA intrusion, including Initial Access, Execution, Persistence and Lateral Movement, Discovery, and Credential Access. The diagram shows the adversary exploiting Microsoft Exchange vulnerabilities and using various techniques to gain access and harvest credentials.](image_description_11.png)

**Case Study**
Falcon OverWatch

---

### Log4Shell Sets the Internet on Fire

Routine discovery, disclosure and subsequent exploitation of a series of high-profile vulnerabilities occurred throughout 2021. Due to the number of potentially affected endpoints, Log4Shell received more attention than any other vulnerability.

Apache’s Log4j2 is an ubiquitous logging library used by many web applications. A vulnerability reported in November 2021 and tracked as CVE-2021-44228 and “Log4Shell” can be exploited by remote attackers to inject arbitrary Java code into affected services. Specially crafted requests may result in access to the system, delivery of malware or acquisition of sensitive data such as user credentials.

Between Dec. 9-31, 2021, a variety of groups incorporated Log4Shell exploitation into their arsenal (Figure 5). Opportunistic eCrime actors aggressively engaged in widespread Log4Shell exploitation most commonly affiliated with commodity botnet malware (e.g., Muhstik). However, other eCrime-focused actors — including affiliates of DOPPEL SPIDER and WIZARD SPIDER — adopted Log4Shell as an access vector to enable ransomware operations. Additionally, state-nexus actors, including NEMESIS KITTEN and AQUATIC PANDA, were also affiliated with probable Log4Shell exploitation before the end of 2021.

![Image description: A timeline of Log4Shell events and affiliated actors from November to December 2021. It shows the disclosure of the vulnerability, the release of weaponized exploits, and the involvement of various eCrime and state-nexus actors.](image_description_12.png)

The initial wave of opportunistic Log4Shell attacks was very simple, and each exploit was structured nearly identically. However, achieving reliable remote code execution (RCE) via CVE-2021-44228 on various impacted platforms potentially requires the actor to tailor the Log4Shell exploit for a specific target. While this adds effort, this tailoring has not prevented actors such as AQUATIC PANDA from leveraging more specific versions of CVE-2021-44228 exploits. In particular, CrowdStrike Intelligence and industry sources linked Log4Shell exploitation to the compromise of VMware products.

Due to the widespread nature of the Log4j2 logging library, it is difficult to assess which products are vulnerable and ensure they are protected against exploitation. Targeting of CVE-2021-44228 by criminal threat groups is increasing and will continue into 2022.

Many state-operated actors are likely to integrate Log4Shell exploits into their toolchain, since this logging library provides a method through which actors can gain access to target environments via vulnerable entry point systems or move laterally by exploiting internal servers on already compromised networks. This assessment is based on the vulnerability’s massive prevalence. However, all impacted products cannot be exploited with the same technique, and tailoring of exploits for specific targets may be required.

CrowdStrike Intelligence assesses that actors will continue to integrate increasingly effective exploit chains to rapidly achieve RCE. This assessment is made with moderate confidence based on the substantial number of incidents facilitated by multistage exploit chains — such as ProxyShell and ProxyLogon — that proved commonplace during 2021.

STAY UP-TO-DATE ON LOG4SHELL
Visit the CrowdStrike Log4j/"Log4Shell" Vulnerability Learning Center.

#### PROPHET SPIDER Leverages Log4j Exploit for Attempted Credential Harvesting from a Cloud Workspace Service

PROPHET SPIDER is a prolific access broker with a track record of successfully leveraging known vulnerabilities to gain access to web servers and cloud services in order to harvest credentials. OverWatch recently uncovered a hands-on intrusion against a U.S.-based financial services entity following the successful compromise of a VMware Horizon web component. Observed TTPs were consistent with those previously seen from PROPHET SPIDER and included the retrieval of tooling from an actor-controlled IP, along with host and domain reconnaissance.

![Image description: A diagram illustrating the steps of a PROPHET SPIDER intrusion, including C2 and Persistence, Execution and Discovery, Discovery, and Defense Evasion. The diagram shows the adversary leveraging a Log4j exploit to gain access and attempt credential harvesting.](image_description_13.png)

**Case Study**
Falcon OverWatch

---

### Increasing Threats to Cloud Environments

Cloud-based services now form crucial elements of many business processes, easing file sharing and collaboration. However, these same services are increasingly abused by malicious actors in the course of computer network operations (CNO), a trend that is likely to continue in the foreseeable future as more businesses seek hybrid work environments. Common cloud attack vectors used by eCrime and targeted intrusion adversaries include cloud vulnerability exploitation, credential theft, cloud service provider abuse, use of cloud services for malware hosting and C2, and the exploitation of misconfigured image containers.

#### Cloud Vulnerability Exploitation

Malicious actors tend to opportunistically exploit known RCE vulnerabilities in server software, typically scanning for vulnerable servers without focusing on particular sectors or regions. After initial access, actors may deploy a variety of tools. Wider criminal exploitation of cloud services for initial access includes the exploitation of Accellion FTA vulnerabilities. Since January 2021, multiple companies have self-disclosed breaches related to the exploitation of such vulnerabilities.

VMware has also been targeted by threat actors, including CVE-2021-21972 — a critical vulnerability impacting VMware ESXi, vCenter Server and Cloud foundation products. Targeting this vulnerability provides a simple and reliable method for exploitation that threat actors can use across multiple host-operating systems, attack vectors and intrusion stages. Multiple adversaries, particularly BGH actors, have likely leveraged this vulnerability.

#### Credential Theft

Credential-based intrusions against cloud environments are among the more prevalent exploitation vectors used by eCrime and targeted intrusion adversaries. Criminal actors routinely host fake authentication pages to harvest legitimate authentication credentials for cloud services such as Microsoft Office 365 (O365), Okta or online webmail accounts. Actors then use these credentials to attempt to access victim accounts.

Access to cloud-hosted email or file-hosting services can also facilitate espionage and theft of information. In April 2021, CrowdStrike observed COSMIC WOLF targeting victim data stored within the Amazon Web Services (AWS) cloud environment. The adversary compromised the AWS environment via a stolen credential that allowed the operator to interact with AWS using the command line. Employing this technique, the adversary altered security group settings to allow direct SSH access from malicious infrastructure.

#### Cloud Service Provider Abuse

Adversaries have leveraged cloud service providers to abuse provider trust relationships and gain access to additional targets through lateral movement from enterprise authentication assets hosted on cloud infrastructure. If an adversary can elevate their privileges to global administrator levels, they may be able to pivot between related cloud tenants to further their access.

This issue is particularly significant if the initially targeted organization is a managed service provider (MSP). In this case, global administrator access can be used to take over support accounts used by the MSP to make changes to their customer networks, thereby creating multiple opportunities for vertical propagation to many more networks. This technique was used by COZY BEAR throughout 2020, with evidence of continued intrusion in MSP networks continuing into 2021.

#### Malware Hosting and Command and Control

Both eCrime and targeted intrusion adversaries extensively leverage legitimate cloud services to deliver malware; targeted actors also use these services for command and control. This tactic has the advantage of being able to evade signature-based detections, because top-level domains of cloud hosting services are typically trusted by many network scanning services. Using legitimate cloud services, including chat applications, can enable adversaries to evade some security controls by blending into normal network traffic. Moreover, using cloud-hosting providers for C2 allows the adversary to switch or remove payloads from an affiliated C2 URL with ease.

#### Exploitation of Misconfigured Image Containers

Criminal actors have periodically exploited improperly configured Docker containers. Docker images are templates used for creating containers. These images can be used either on a standalone basis, for users to directly interact with a tool or service, or as the parent to another application. Because of this hierarchical mode, if an image has been modified to contain malicious tooling, any container derived from it will also be infected.

In 2021, CrowdStrike Intelligence reported on the malware family Doki, which uses containers as both an initial infection vector and as a means for parallel track tasking. Once malicious actors gain access, they can abuse these escalated privileges to accomplish lateral movement and then proliferate throughout the network.

CrowdStrike Intelligence has also continued to track adversary operations involving the access and modification of constituent parts of Kubernetes clusters. Kubernetes is an open-source container-orchestration system that automates the deployment, scaling and management of applications and their associated shared resources. Falcon OverWatch has observed increasing adversary interest in Kubernetes clusters operating within corporate environments. The Kubernetes framework is a complex system comprising a number of constituent parts allowing ample opportunity for misconfiguration that could provide an adversary with initial access to one component and subsequent lateral propagation opportunities that provide access to desired resources.

#### Threat Highlight: Russian Adversaries Look to the Cloud

##### FANCY BEAR

The FANCY BEAR adversary is associated with the 85th Main Center of the Special Services (aka Military Unit 26165) of Russia’s Main Intelligence Directorate (GRU). Earlier in its operational lifespan, when conducting victim exploitation and credential collection, the adversary extensively used spear-phishing emails containing malicious documents or links that redirected to malicious infrastructure. However, after multiple exposures of its operations — particularly by the U.S. Department of Justice (DOJ) in 2018 — FANCY BEAR appears to have reevaluated their operational tradecraft and decreased their use of malware while shifting toward increased use of credential-harvesting tactics including both large-scale scanning techniques and victim-tailored phishing websites.

Credential harvesting plays a significant role in FANCY BEAR’s acquisition of intelligence and primary access into target organizations or individuals. Adapting to the trend of public and private entities increasingly hosting parts of their internal infrastructure (e.g., email, internal chat, or identity and device-management services) via cloud services, the adversary has targeted numerous cloud-based email providers with a variety of collection methodologies throughout 2021. Examples of targeted email providers include enterprise services such as Microsoft 365 or GSuite, as well as webmail services more likely used by individuals. The adversary’s credential-collection operations have technically matured over the years while maintaining a consistently high volume and tempo.

##### COZY BEAR

Throughout 2021, COZY BEAR also repeatedly demonstrated a high level of post-exploitation proficiency, particularly involving the enumeration of, and lateral movement within, cloud environments. During a CrowdStrike Services investigation, COZY BEAR operators were identified using authentication cookie theft to bypass multifactor authentication (MFA) restrictions implemented on target networks. This technique leverages existing local network access and has been used to access user accounts in possession of enterprise cloud service privileges. This technique highlights the adversary’s ability to use a range of post-compromise activities to expand their access and maximize intelligence collection.

Future operations consistent with this cluster of COZY BEAR-associated activity are highly likely to continue mirroring this behavior, particularly through the successive identification and compromise of user accounts that are assigned administrative or special privileges on cloud services and tenants. This assessment is made with moderate confidence based on the increasing application of MFA restrictions on cloud service access and the consistency of COZY BEAR-related operations identified to date.

---

## Conclusion

CrowdStrike Intelligence continues to provide industry-leading actor profiles, malware analysis and campaign tracking through its suite of intelligence reporting products and coverage of threat landscapes.

In 2021, CrowdStrike Intelligence observed adversaries continue to adapt to security environments impacted by the ongoing COVID pandemic. These adversaries are likely to look at novel ways in which they can bypass security measures to conduct successful initial infections, impede analysis by researchers and continue tried-and-tested techniques into 2022.

BGH operations will continue to dominate the eCrime landscape in 2022, likely significantly increasing their use of ransomware from ransomware-as-a-service (RaaS) operations in an effort to allow for a wider array of adversarial skill sets. The access broker market will also continue as an avenue for ransomware operators to gain victims, removing the initial access step and allowing swifter deployment of malware.

Targeted intrusion adversaries are expected to continue to capitalize on trends in technology and the broader threat landscape throughout 2022 in attempts to maximize impacts while minimizing effort. (In 2021, this behavior was reflected in Iran’s shift to disruptive ransomware, China’s emphasis on vulnerability exploitation — often at scale — to achieve initial access to