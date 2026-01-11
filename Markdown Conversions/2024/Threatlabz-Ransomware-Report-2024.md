ThreatLabz

2024 Ransomware
Report

©2024 Zscaler, Inc. All rights reserved.

## Table of Contents

Executive Summary

Key Findings

Ransomware Landscape: Top Trends and Targets

Overall rise in ransomware attacks

Industry verticals most impacted by ransomware

Geographical distribution of victim organizations

Most active ransomware groups in 2023-2024

Major vulnerabilities used in ransomware attacks

Ransomware Roundup: What’s Making Headlines

The ransomware plague in healthcare

The impact of the SEC’s cybersecurity ruling

Impact of law enforcement actions

Top 5 Ransomware Families to Watch in 2024-2025

#1 Dark Angels

#2 LockBit

#3 BlackCat

#4 Akira

#5 Black Basta

ThreatLabz Ransomware Notes Archive

2025 Predictions

How Zscaler Simplifies Ransomware Protection

Holistic prevention at each stage of the attack chain

Related Zscaler products

Ransomware Prevention Guidance

Report Methodology

About ThreatLabz

About Zscaler

3

4

5

6

7

9

12

13

14

14

15

16

20

20

21

22

23

24

25

26

29

31

32

33

35

35

35

2

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

## Executive Summary

Ransomware attacks have reached new heights of ambition and audacity over the past year, marked by a notable surge in extortion attacks. Adding to the increase in ransomware attacks, ThreatLabz research uncovered an unprecedented ransom payout of US$75 million—the largest ever paid by one company. This amount is nearly double the highest publicly known ransom payment.¹ In 2023 alone, ransomware payments exceeded $1 billion, highlighting the escalating financial impact of these cybercrimes.

Ransomware threat actors’ tactics have become increasingly sophisticated and bold. Notably, they have surpassed the traditional boundaries of the corporations they attack, even going so far as to target the children of executives to provoke faster and higher ransoms.² From critical infrastructure³ and major corporations⁴ to small and medium-sized enterprises, no organization is immune to finding themselves in the crosshairs of the next campaign or evolution of attacks.

Despite law enforcement takedowns of multiple initial access brokers under special ops “Operation Endgame” and “Operation Duck Hunt,” many of the largest active ransomware families continue to rapidly regroup and launch new attacks while barely skipping a beat. Unfortunately, many ransomware actors are beyond the reach of law enforcement, making them virtually immune to criminal prosecution. As detailed in this report, law enforcement agencies have augmented their pressure tactics through reward money, sanctions, trolling, and exposing the individuals behind ransomware using various forms of psychological tactics.

As ransomware actors continuously evolve their tactics, it is crucial to stay up to date on how the threat landscape is changing.

The Zscaler ThreatLabz 2024 Ransomware Report offers an overview of the ransomware threat landscape from April 2023 through April 2024, detailing the latest trends, targets, ransomware families, and effective defense strategies.

ThreatLabz found that ransomware attacks increased by 17.8% year-over-year based on blocked attempts in the Zscaler cloud, while ransomware attacks identified through data leak site analysis surged by 57.8%. The most common targets were businesses in the manufacturing, healthcare, and technology sectors, putting critical operations and infrastructure squarely in the line of attack.

The findings presented in this report underscore the need for organizations to prioritize protection against the relentless tide of ransomware. The insights and strategies in the report serve as a crucial guide for improving your ransomware defenses. By understanding the latest trends and vulnerabilities, and implementing recommended best practices, you can significantly reduce the risk of becoming a ransomware victim and better protect your organization’s critical assets and data.

¹ Bloomberg, CNA Financial Paid $40 Million in Ransom After March Cyberattack, May 20, 2021.

² Business Insider, Hackers are now targeting the children of corporate executives in ransomware attacks, May 12, 2024.

³ Dark Reading, Ascension Healthcare Suffers Major Cyberattack, May 10, 2024.

⁴ CyberScoop, Boeing confirms attempted $200 million ransomware extortion attempt, May 8, 2024.

3

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

## Key Findings

*   Zscaler ThreatLabz research uncovered a record-breaking ransom payment of US$75 million—the largest ransomware payment by a company in history—nearly double the highest publicly known payout.
*   Ransomware attacks blocked by the Zscaler cloud increased by 17.8%, and the number of extorted companies on data leak sites grew by 57.8% in the same period year-over-year despite numerous law enforcement operations, including the seizure of infrastructure along with arrests, criminal indictments, and sanctions.
*   The manufacturing, healthcare, and technology sectors were the top targets of ransomware attacks, while the energy sector experienced a 500% year-over-year spike as critical infrastructure and susceptibility to operational disruptions make it particularly attractive to cybercriminals.
*   The United States remains the top target of ransomware, experiencing 49.95% of overall attacks, followed by the United Kingdom, Germany, Canada, and France.
*   ThreatLabz identified 19 new ransomware families during the analysis period, bringing the total number to 391 since our tracking started.
*   The most active ransomware families were LockBit (22.1%), BlackCat (a.k.a. ALPHV) (9.2%), and 8Base (7.9%).
*   Vulnerabilities remain an all-too-common ransomware attack vector, emphasizing the importance of timely patching and unified vulnerability management, underpinned by a zero trust architecture to provide protection even when patches are not available.
*   Voice-based social engineering attacks are increasingly being used to gain access to corporate networks—a technique used by Scattered Spider and the Qakbot threat group.

4

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

## Ransomware Landscape: Top Trends and Targets

The dynamic nature of ransomware has placed it at the forefront of security concerns in recent years. Threat actors are constantly evolving their methods of attack and extortion, leveraging advances in artificial intelligence (AI) technology, leaked source code, and advanced encryption to maximize their impact and profitability.

This report examines the following ransomware attack trends from April 2023 through April 2024:

*   Overall rise in ransomware attacks
*   Industry verticals most impacted by ransomware
*   Geographical distribution of victim organizations
*   Top ransomware threats and record-breaking ransom payments
*   Increased law enforcement action against ransomware groups and initial access brokers

5

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

### Overall rise in ransomware attacks

The latest ThreatLabz analysis reveals a concerning trend, with a 17.84% year-over-year increase in ransomware attacks based on blocked attempts observed across the Zscaler cloud. The rise in ransomware activity translates to significant disruptions and financial impacts to victim organizations of all sizes. These attacks often disrupt business operations, causing extended downtime, substantial data loss, and high recovery costs. The financial burden is considerable; not only is there a ransom demand at play, but system restoration and damage control can come at a hefty price. In light of these escalating threats, the need for robust ransomware defense measures has never been greater.

![Graph showing the number of ransomware attempts blocked in Zscaler cloud from 2021 to April 2024, with a significant increase in the last period.](placeholder_image_1.png)
*Figure: NUMBER OF ATTEMPTS BLOCKED IN ZSCALER CLOUD*

6

ThreatLabz 2024 Ransomware Report©2024 Zscaler, Inc. All rights reserved.

### Industry verticals most impacted by ransomware

Ransomware attacks pose significant risks to businesses of all sizes and industries. These attacks can compromise sensitive data, lead to heavy financial losses, disrupt business continuity, and damage reputations. Different industries face unique ransomware challenges based on how they operate, the data they handle, and their technological infrastructure.

Despite the variables, ransomware extortion attacks have consistently surged, with the number of victim companies listed on data leak sites increasing by 57.81% since last year’s ThreatLabz report on ransomware trends. The manufacturing industry was by far the most targeted industry, accounting for 653 attacks—more than two times as many as any other industry.

![Bar chart showing ransomware attacks by industry, with Manufacturing at the top with 653 attacks, followed by Healthcare (312) and Technology (265).](placeholder_image_2.png)
*Figure 1: Ransomware attacks by industry based on data leak sites (top 20 industries only).*

7

ThreatLabz 2024 Ransomware Report©2024 Zscaler, Inc. All rights reserved.

#### Year-over-year trends

The energy sector experienced a 527.27% year-over-year increase in ransomware attacks, likely due to its critical nature and the high ransom potential it offers to attackers.

Similarly, the restaurants, bars, and food services industry saw a 333.33% rise in such attacks. This may be attributed to the sector’s rapid digitization, driven by the adoption of advanced point-of-sales systems and online ordering platforms. While these technologies may streamline operations and improve customer experiences, they can also introduce potential vulnerabilities.

While this rise highlights the prevalence of ransomware attacks, it may not capture the full extent of ransomware incidents. Many attacks go unreported or are resolved privately through ransom payments without public disclosure. Thus, these figures should be seen as indicative of broader ransomware trends rather than a comprehensive representation of the entire threat landscape.

![Bar chart showing year-over-year percentage change in ransomware extortion attacks by industry.](placeholder_image_3.png)
*Figure 2: Year-over-year percentage change in ransomware extortion attacks by industry. Note that some sectors had a relatively low baseline of attacks in last year’s report, making their growth appear more substantial.*

8

ThreatLabz 2024 Ransomware Report©2024 Zscaler, Inc. All rights reserved.

### Geographical distribution of victim organizations

The United States faced a markedly higher volume of ransomware attacks than any other country, accounting for about 50% of all incidents globally. In comparison, the United Kingdom was the second-most targeted nation, experiencing nearly 6% of ransomware attacks, followed by Germany (4.09%), Canada (3.51%), and France (3.26%). Figure 3 shows a heatmap illustrating countries impacted by ransom extortions between April 2023 and April 2024.

![World map showing the percentage breakdown of ransomware victims by country. The United States has the largest share at 49.95%.](placeholder_image_4.png)
*Figure 3: Breakdown of ransomware victims by country.*

9

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

Understanding the distribution of ransomware attacks is essential for risk assessment, resource allocation, policy development, international cooperation, and public awareness efforts in combating ransomware threats.

*   **Risk assessment**: Analyzing heavily targeted regions helps organizations in those areas to assess their own risk levels and implement stronger cybersecurity. In ThreatLabz research, the US accounts for 50% of global ransomware attacks, calling for organizations within its borders to prioritize stringent security protocols.
*   **Policy development**: Governments can use insights from regional ransomware attacks to inform legislation, improve security standards, promote international cooperation, and facilitate public-private sector information sharing. As a recent notable example, the SEC’s new cybersecurity rules mark a major step in enhancing transparency and accountability amid growing threats.
*   **Public awareness**: Highlighting frequently targeted countries may urge individuals, organizations, and governments to take more proactive measures when it comes to cybersecurity training, incident response planning, and investment in defensive technologies.
*   **Resource allocation**: Targeted data enables governments and organizations to strategically allocate resources, enhancing their security posture by prioritizing support, funding, and expertise in areas with the highest threat levels.
*   **International cooperation**: Identifying the most targeted countries allows coordinated efforts between law enforcement, organizations, and governments to combat ransomware at the national and international levels. Operation Duck Hunt and Operation Endgame exemplify how international cooperation can disrupt cybercriminal activities.

10

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

#### Year-over-year trends

ThreatLabz compared ransomware attacks from this year's report with the ThreatLabz 2023 Ransomware Report to assess rates of change. Among the top 15 most targeted countries, the US experienced a notable year-over-year increase of 101.88%, and Sweden saw a staggering 350% rise, although it accounted for a significantly smaller share of the total attacks.

While analyzing ransomware trends at a global level is invaluable, it is also important to examine the specific developments in different regions of the world. Studying regional breakdowns helps organizations create tailored security plans and aid governments in developing more effective cybersecurity policies.

![Table showing year-over-year comparison of ransomware attacks by country in the US, UK, Germany, Canada, France, Italy, Australia, Brazil, Spain, Mexico, Netherlands, India, Switzerland, Japan, and Sweden.](placeholder_image_5.png)
*Figure 5: Year-over-year comparison of ransomware attacks by country.*

![Table showing year-over-year comparison of ransomware attacks by country in the EMEA region.](placeholder_image_6.png)
*Figure 6: Year-over-year comparison of ransomware attacks by country in the EMEA region.*

![Table showing year-over-year comparison of ransomware attacks by country in the APAC region.](placeholder_image_7.png)
*Figure 7: Year-over-year comparison of ransomware attacks by country in the APAC region.*

11

ThreatLabz 2024 Ransomware Report©2024 Zscaler, Inc. All rights reserved.

### Most active ransomware groups in 2023-2024

LockBit (22.1%), BlackCat (9.2%), and 8Base (7.9%) were the most active ransomware extortion groups over the past year, each responsible for a significant number of attacks. Figure 8 shows the number of data leak victims per ransomware family during this period.

![Bar chart showing the number of ransomware attacks revealed on data leak websites by ransomware family. LockBit is the most active with 988 attacks.](placeholder_image_8.png)
*Figure 8: Ransomware attacks revealed on maliciously operated data leak websites.*

#### Newest ransomware groups on the scene

Figure 9 showcases a timeline of new ransomware groups that began publishing data on leak sites as part of their extortion strategy.

![Timeline graphic showing the emergence of new ransomware groups from April 2023 to March 2024.](placeholder_image_9.png)
*Figure 9: New ransomware groups with data leak sites.*

12

ThreatLabz 2024 Ransomware Report©2024 Zscaler, Inc. All rights reserved.

### Major vulnerabilities used in ransomware attacks

Vulnerabilities in software, systems, and the overall digital infrastructure can serve as critical entry points for ransomware attacks. Organizations must be aware of these vulnerabilities and take proactive measures to address them.

The Cybersecurity & Infrastructure Security Agency (CISA) maintains a comprehensive list of vulnerabilities,⁵ including those actively exploited by ransomware groups. It is highly recommended that organizations closely monitor this list and prioritize the mitigation of vulnerabilities mentioned therein. Proactive vulnerability management is essential for strengthening the overall cybersecurity posture of an organization.

In many cases, the vulnerabilities exploited by ransomware groups impact internet-connected assets in organizations’ external attack surface, such as gateways, VPNs, and other remote connectivity technologies. Because they are internet-facing, these vulnerabilities are significantly easier for threat actors to scan for and exploit. CISA’s latest guidance⁶ further emphasizes vulnerabilities in VPNs and remote connectivity solutions as critical points of concern, advising the adoption of the most current approaches, such as zero trust architecture, SSE, and SASE, which are based on granular access control policies.

Over the past year, prominent ransomware families have targeted and exploited the vulnerabilities shown in figure 10, significantly impacting a wide range of systems.

> >> >> >> >
>
> ConnectWise ScreenConnect
> (exploited by LockBit, Black
> Basta, and Bl00dy)
>
> CVE-2024-1708: Allows
> attackers to gain
> unauthorized access to
> directories and files
> beyond restricted areas,
> resulting in information
> disclosure and control over
> compromised systems.
>
> CVE-2024-1709: Allows
> attackers to circumvent
> authentication mechanisms
> and directly access
> confidential information
> or critical systems.
>
> Cisco's ASA and
> FTD software
> (exploited by Akira)
>
> CVE-2020-3259: Allows
> unauthenticated remote
> attackers to retrieve
> memory contents from an
> impacted device, resulting
> in the disclosure of
> confidential information.
>
> Cisco's remote
> access VPN feature
> (exploited by Akira)
>
> CVE-2023-20269: Allows
> unauthenticated remote
> attackers to conduct
> brute-force attacks to
> identify valid username and
> password combinations, and
> authenticated remote
> attackers to establish a
> clientless SSL VPN session
> with an unauthorized user.
>
> Citrix NetScaler ADC
> and NetScaler Gateway
> (exploited by INC Ransom,
> LockBit, and BlackCat)
>
> CVE-2023-4966 (a.k.a. Citrix
> Bleed): Allows attackers to
> bypass password
> authentication and MFA to
> gain unauthorized access to
> networks using leaked
> session tokens.
>
> CVE-2023-3519: Allows
> attackers to exploit remote
> code execution flaws.

![Diagram listing prevalent vulnerabilities exploited by ransomware from April 2023-April 2024, including ConnectWise ScreenConnect, Cisco ASA/FTD, Cisco VPN, and Citrix NetScaler.](placeholder_image_10.png)
*Figure 10: Prevalent vulnerabilities from April 2023-April 2024.*

⁵ Cybersecurity & Infrastructure Security Agency, Known Exploited Vulnerabilities Catalog, accessed June 25, 2024.

⁶ Cybersecurity & Infrastructure Security Agency, Modern Approaches to Network Access Security, June 18, 2024.

Available patches for these vulnerabilities should be applied as soon as possible, along with the following mitigation measures:

*   Disable remote access to servers
*   Use strong passwords and multifactor authentication
*   Monitor servers for suspicious activity

ThreatLabz 2024 Ransomware Report

13

©2024 Zscaler, Inc. All rights reserved.

## Ransomware Roundup: What’s Making Headlines

Ransomware is pervasive and transcends industries—and when one group is shut down, another is reborn or emerges anew. Here are some recent stories highlighting the ever-evolving ransomware landscape.

### The ransomware plague in healthcare

The healthcare industry faced significant challenges throughout 2023 and into 2024 as it was heavily targeted by ransomware groups. The repercussions of disrupting healthcare operations are serious: ambulances get rerouted, prescriptions are delayed, and essential medical procedures have to be postponed. Moreover, the theft of sensitive health data can have far-reaching consequences, including identity theft and healthcare fraud, further exacerbating vulnerabilities in the healthcare ecosystem.

This is a stark reminder that the old adage “there is no honor among thieves” holds true for ransomware attacks. Even if ransoms are paid, there is no guarantee that the threat group will not still post or delete stolen data. In addition, some ransomware decryption tools contain bugs that prevent successful data recovery, and may take longer to recover data than from a backup.

#### UNFORESEEN CONSEQUENCES OF RANSOM PAYMENTS

A healthcare technology provider for payment solutions fell victim to a ransomware attack orchestrated by the BlackCat group. Despite complying with the attackers’ demands and paying a staggering $22 million ransom, the ordeal took an unexpected turn. BlackCat reneged on their promise to share a portion of the ransom with the affiliate behind the attack (a so-called “exit scam”), prompting the affiliate to threaten the healthcare provider with the release of sensitive data.

#### DOUBLE EXTORTION, DOUBLE VICTIMIZATION

In February 2023, a prominent US pharmaceutical distributor confirmed that their IT systems had been compromised. The breach affected one of the distributor’s subsidiaries, with the stolen files later leaked by the Lorenz ransomware group.⁷ Then, in February 2024, the same distributor faced another ransomware attack.⁸ This appears to be part of a growing trend ThreatLabz has observed, where a company has been subject to multiple ransomware incidents within one year.

⁷ BleepingComputer, Drug distributor AmerisourceBergen confirms security breach, February 8, 2023.

⁸ BleepingComputer, Pharmaceutical giant Cencora says data was stolen in a cyberattack, February 27, 2024.

14

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

### The impact of the SEC’s cybersecurity ruling

In 2023, the SEC introduced new cybersecurity disclosure rules to enhance transparency and accountability among publicly traded companies. Effective December 15, 2023, these rules mandate the timely reporting of material cybersecurity incidents and require detailed information about a company’s cybersecurity risk management, strategy, and governance. Key components of the SEC rulings include the addition of Item 1.05 to for 8-K, which necessitates reporting of material cybersecurity incidents within four business days of the company’s determination of materiality. Additionally, Form 10-K now requires annual reporting on cybersecurity risk management and strategy, starting with fiscal years ending on or after December 15, 2023. Foreign private issuers must also comply with comparable disclosures on Form 6-K and Form 20-K.

The rulings present a new challenge for ransomware actors offering publicly traded companies private payment resolution services, as the companies are now still required to fully disclose the attack. On the positive side, the new mandate undercuts encryptionless extortion attacks, an emerging trend by which ransomware actors rely solely on the threat of leaking stolen data to demand ransoms.

#### HOW THE NEW RULES IMPACT COMPANIES

The SEC’s cybersecurity rulings can pose serious challenges for companies in terms of compliance and risk management. While intended to enhance transparency and investor protection, these rules require companies to navigate complex reporting requirements and provide prompt disclosure of material incidents.

One major impact is the increased pressure on companies to quantify and assess cyber incidents accurately. Determining materiality and the potential impact of cyber incidents requires careful analysis, which can be costly and may require companies (big and small) to rethink their incident response protocols and update their disclosures to meet the SEC’s requirements.

Moreover, compliance timelines vary based on the size and reporting status of companies, adding another layer of complexity. Smaller reporting companies often have different, and typically longer, compliance deadlines compared to larger corporations. And while larger corporations must adhere to tighter deadlines, their scale also affords them more resources to analyze the materiality of a cybersecurity incident.

The new disclosure requirements also eliminate the possibility for public companies to pay ransoms quietly without incurring reputational damage and the backlash that follows after openly sharing information about a breach.

#### SOME COMPANIES ARE ALREADY IN VIOLATION OF THE SEC’S RULES

Despite the SEC’s clear guidelines, some companies have already fallen short of compliance with the new cybersecurity rules. Recent disclosures from well-known companies have raised concerns about noncompliance and the adequacy of their incident reporting.⁹ Many of these disclosures lack quantitative data and detailed assessments of the financial and operational implications of the cyber incidents, which is precisely what the SEC now mandates. This trend, where companies provide deficient cyber incident disclosures despite the SEC ruling, may call for enhanced guidance and regulatory oversight to ensure consistent and effective compliance.

The SEC’s cybersecurity rulings represent a significant regulatory shift aimed at improving transparency and accountability in incident reporting. Adhering to these new rules consistently and in good faith will require ongoing collaboration between regulators, companies, and industry stakeholders.

⁹ Forbes, Companies Are Already Not Complying With The New SEC Cybersecurity Incident Disclosure Rules, March 4, 2024.

15

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

### Impact of law enforcement actions

#### Qakbot disrupted by “Operation Duck Hunt”

On August 29, 2023, in a coordinated multinational effort, the Federal Bureau of Investigation (FBI) and the Department of Justice (DOJ) announced Operation Duck Hunt. Zscaler ThreatLabz provided significant technical assistance to law enforcement for this operation.¹⁰ Qakbot’s infrastructure was designed to be resilient against takedown attempts through a multi-tiered infrastructure, as shown in figure 11.

This infrastructure provided several layers of resiliency, with each tier requiring a coordinated effort to dismantle. The first tier of Qakbot’s infrastructure included infected systems running a supernode plugin that relayed traffic upstream to several proxies designed to hide the master Qakbot backend server.

Operation Duck Hunt redirected the supernode’s upstream proxy servers to a set of sinkhole servers to immediately take over Qakbot’s infrastructure as shown in figure 12.

![Diagram illustrating Qakbot's multi-tiered infrastructure, showing infections, supermode modules, upstream proxies, and the master backend server.](placeholder_image_11.png)
*Figure 11: Qakbot’s multi-tiered infrastructure.*

![Diagram showing Qakbot architecture after redirecting upstream proxies to sinkhole servers.](placeholder_image_12.png)
*Figure 12: Qakbot architecture after redirecting each supernode’s upstream proxies.*

¹⁰ US Department of Justice, Qakbot Malware Disrupted in International Cyber Takedown, August 29, 2023.

¹¹ TechCrunch, How the FBI took down the notorious Qakbot botnet, September 1, 2023.

Once the FBI hijacked the supernodes, the sinkhole servers instructed victim computers to download shellcode that reflectively loaded a DLL that neutralized the malware. This successfully disinfected the victim computers and prevented further attacks.

At the time of the takedown, Qakbot had infected more than 700,000 computers worldwide, including more than 200,000 in the United States alone.¹¹ Prior to this operation, Qakbot was active for nearly 15 years, originally designed to facilitate credit card and wire fraud. In 2019, the group pivoted to serving as an initial access broker for ransomware groups including Conti, ProLock, Egregor, REvil, MegaCortex, and Black Basta.

Qakbot malware was typically distributed through spam emails containing malicious attachments or links. Once infected, Cobalt Strike was frequently deployed for lateral movement and the eventual deployment of ransomware.

Unfortunately, there were no arrests or unsealed indictments against any of the threat actors, and Qakbot resurfaced in December 2023. The group updated the malware to support 64-bit versions of Windows, changed the internal configuration format, and modified the network communication to use AES encryption. As we will discuss later in the report, the Qakbot threat actor has significantly changed their TTPs since Operation Duck Hunt.

16

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

#### “Operation Endgame” simultaneously targeted multiple initial access brokers

On May 28, 2024, in collaboration with numerous international law enforcement agencies, Europol announced Operation Endgame, which simultaneously targeted multiple initial access brokers. This led to more than a dozen global searches, several arrests, and the shutdown of more than 100 servers used for criminal activity. These servers were integral to the operations of various malware downloaders (a.k.a. “loaders”) that had been used to infiltrate victims’ computers, deploying malicious software including ransomware.

The malware families targeted in this operation were responsible for infecting millions of computers around the globe, including in healthcare facilities and critical infrastructure services. As part of the operation, action was taken against SmokeLoader, Pikabot, Bumblebee, and IcedID.

Zscaler ThreatLabz provided critical technical assistance for Operation Endgame’s SmokeLoader sinkhole and remediation efforts.

SmokeLoader, active since 2011, was used by several initial access brokers for ransomware, including Raspberry Robin and the Stop (a.k.a. DJVU) ransomware gang. Operation Endgame seized more than 1,000 SmokeLoader domains used by these threat groups. The domains were then redirected to a sinkhole server controlled by law enforcement. The map in figure 13 depicts infected systems that communicated with the SmokeLoader sinkhole.

This map demonstrates the far-reaching impact that SmokeLoader had around the world, with significant infections in Latin America, Asia, North America, and Europe.

![World map showing the global distribution of SmokeLoader infections communicating with the Operation Endgame sinkhole.](placeholder_image_13.png)
*Figure 13: Map of SmokeLoader infections communicating with the Operation Endgame sinkhole. (Source: Zscaler ThreatLabz)*

17

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

When systems infected with SmokeLoader connected to the sinkhole server, they received the malware’s own built-in uninstall command. To date, more than 40,000 systems infected with SmokeLoader have been cleaned, as shown in figure 14.

![Line graph showing the number of SmokeLoader systems cleaned by Operation Endgame from May 28, 2024, to June 21, 2024.](placeholder_image_14.png)
*Figure 14: SmokeLoader systems cleaned by Operation Endgame.*

Pikabot originally emerged in early 2023 and exhibited significant activity in the latter half of the year. This increase was due to the malware becoming the initial access broker of choice for Black Basta ransomware after Operation Duck Hunt disrupted Qakbot. In February 2024, Pikabot reemerged with significant changes in its code base and structure. Pikabot was observed by ThreatLabz regularly deploying Cobalt Strike and Metasploit’s Meterpreter.

Bumblebee was introduced in March 2022 and had ties to the former Conti ransomware group. The malware was the successor to the group’s BazarLoader malware tool, which they used for initial access for Conti and Diavol ransomware attacks. ThreatLabz frequently observed both BazarLoader and Bumblebee deploying Cobalt Strike payloads for lateral movement. Bumblebee has also been associated with Akira and Black Basta ransomware attacks.

Similar to Qakbot, IcedID was originally designed as a banking trojan when it appeared in 2017. However, the group later shifted their focus to serving as an initial access broker for ransomware. Over the years, the malware code for IcedID has been forked and modified for various purposes. In addition, the same developers created a new malware loader known as Latrodectus, released in November 2023, which was also likely used to deploy ransomware.

Following Operation Endgame, there has been minimal activity for most of these initial access brokers with the exception of Latrodectus, which resurfaced in less than a month. However, the lull is likely to be short-lived as the threat actors regroup.

18

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

#### Hive ransomware reborn as Hunters International

In January 2023, the Hive ransomware group’s infrastructure was shut down. After a seven-month covert operation, the FBI successfully infiltrated Hive’s servers, recovering more than 300 decryption keys that prevented approximately $130 million in ransom payments. Operating since June 2021, the Hive collective targeted and victimized more than 1,500 organizations worldwide, amassing over $100 million in ransom payments.¹² Victims included hospitals, school districts, financial institutions, and various other entities. However, no arrests associated with Hive were made, and the group rebranded as Hunters International in October 2023. Cybercriminals often use this rebranding strategy after a major disruption.

The group made one noticeable change to their operation: they will no longer offer discounts or negotiate with victims from the initial ransom demand, as shown in figure 15.

¹² US Department of Justice, U.S. Department of Justice Disrupts Hive Ransomware Variant, January 26, 2023.

![Screenshot of the Hunters International victim portal, showing a message about no price discounts or negotiations.](placeholder_image_15.png)
*Figure 15: Hunters International victim portal with no price discounts or negotiations.*

The non-negotiable price policy is very uncommon with ransomware groups, which frequently offer significant discounts from the original ransom demand. This decision by the Hunters team will likely lead to lower overall payment volume, but higher overall payment amounts.

Hunters International continues to launch new attacks and is likely to remain a formidable threat without further arrests and criminal indictments.

19

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report

## Top 5 Ransomware Families to Watch in 2024-2025

As ransomware and other cyberthreats continue to evolve in complexity and sophistication, staying informed about the most prevalent and dangerous ransomware families is crucial for maintaining an effective security posture. This section highlights five ransomware families that pose some of the most significant risks to businesses, providing insights into their tactics, potential impact, and recent activity.

### #1 Dark Angels

The Dark Angels ransomware group, which operates the Dunghill data leak site, emerged around May 2022. The group has conducted some of the largest ransomware attacks, yet has managed to attract very minimal attention. In early 2024, ThreatLabz uncovered a victim who paid