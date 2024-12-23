# M A N D I A N T S P E C I A L R E P O R T

## Table of Contents
- [EXECUTIVE SUMMARY](#executive-summary)
- [BY THE NUMBERS](#by-the-numbers)
- [Data From Mandiant Investigations](#data-from-mandiant-investigations)
- [NOTABLE AND RECENTLY GRADUATED THREAT GROUPS](#notable-and-recently-graduated-threat-groups)
- [How a Threat Cluster Becomes an APT or FIN Group](#how-a-threat-cluster-becomes-an-apt-or-fin-group)
- [FIN12 Prioritizes Speed to Deploy Ransomware Against High-Value Targets](#fin12-prioritizes-speed-to-deploy-ransomware-against-high-value-targets)
- [FIN13 Prioritizes Targets Based in Mexico](#fin13-prioritizes-targets-based-in-mexico)
- [Grasping the Complexity of UNC2891](#grasping-the-complexity-of-unc2891)
- [UNC1151 and Ghostwriter Linked to Belarusian Interests](#unc1151-and-ghostwriter-linked-to-belarusian-interests)
- [FOCUS ON MULTIFACETED EXTORTION AND RANSOMWARE](#focus-on-multifaceted-extortion-and-ransomware)
- [Financially Motivated Threat Actors Increasingly Targeting Virtualization Infrastructure](#financially-motivated-threat-actors-increasingly-targeting-virtualization-infrastructure)
- [Red Team Full Backup Takeover](#red-team-full-backup-takeover)
- [Observations on Multifaceted Extortion and Ransomware Recovery Operations](#observations-on-multifaceted-extortion-and-ransomware-recovery-operations)
- [DIGGING PAST A CRAFTY COINMINER](#digging-past-a-crafty-coinminer)
- [Introduction](#introduction)
- [The Value of Robust Logging Practices](#the-value-of-robust-logging-practices)
- [Considerations for Security Advancement](#considerations-for-security-advancement)
- [CHINA REINVENTS APPROACH TO CYBER OPERATIONS](#china-reinvents-approach-to-cyber-operations)
- [Background](#background)
- [Realignment and Retooling](#realignment-and-retooling)
- [Espionage Activity Reemerges](#espionage-activity-reemerges)
- [Outlook](#outlook)
- [COMMON MISCONFIGURATIONS THAT LEAD TO COMPROMISE](#common-misconfigurations-that-lead-to-compromise)
- [On-Premises Misconfigurations](#on-premises-misconfigurations)
- [Microsoft Azure and Microsoft 365 Configuration Risks](#microsoft-azure-and-microsoft-365-configuration-risks)
- [CONCLUSION](#conclusion)

# EXECUTIVE SUMMARY
SPECIAL REPORT | MANDIANT M-TRENDS 2022

Recent cyber events are a stark reminder that our work as defenders is never done. Critical vulnerabilities such as “Log4Shell” highlight the dangers of the unknown and the complexity of patching. The supply chain is as attractive a target as ever, providing a potential entry point into multiple vendors. And we must remain vigilant about protecting our industrial control systems, especially given that 1 in 7 multifaceted extortion attacks leak critical operational technology information.

Mandiant responders are on the frontlines every day, investigating and analyzing the latest attacks and threats, and understanding how best to respond to and mitigate them. Everything we learn is passed on to our customers through our various services, giving them a much-needed advantage in a constantly evolving threat landscape.

Every year the M-Trends report provides some of that same critical intelligence to the greater security community. M-Trends 2022 continues that tradition, offering details on the evolving cyber landscape, mitigation recommendations, and a wide variety of security incident-related metrics.

Let’s start with a win for defenders: the global median dwell time has continued its decline in 2021. For intrusions investigated between October 1, 2020 through December 31, 2021, the median number of days between compromise and detection was 21 days (down from 24 days in 2020). Although this may demonstrate improved visibility and response, the pervasiveness of ransomware has helped drive this number down.

Ransomware and multifaceted extortion continue to be concerning. We highlight an increase in targeting of virtualization infrastructure and offer mitigations. We also provide guidance on ransomware preparedness (via red teaming) and recovery operations.

Other topics covered in M-Trends 2022 include:

By the Numbers The global median dwell time for intrusions identified by external third parties and disclosed to the victims dropped to 28 days from 73 days in 2020, a stellar improvement. In less desirable news, when the initial infection vector was identified, supply chain compromise accounted for 17% of intrusions in 2021 compared to less than 1% in 2020. Other signature metrics include detection by source, industry targeting, threat groups, malware and attacker techniques.

Recently Graduated Threat Groups A detailed analysis of two financially motivated groups we graduated in 2021: FIN12 and FIN13. We also highlight two noteworthy uncategorized groups: UNC2891 and UNC1151.

Microsoft Exchange Case Study Our observations responding to more than 20 incidents involving exploitation of on-premises Microsoft Exchange servers. In one testament to dedicated investigation and analysis, the deployment of cryptocurrency coinminers by one financially-motivated threat group led to the discovery of two nation-state actors in the same environments.

China Cyber Operations We review China’s realignment and retooling, explore reemerging espionage activity and highlight actors such as APT10 and APT41.

Misconfiguration Mitigations We observed various compromises due to misconfigurations when using on-premises Active Directory with Azure Active Directory to achieve a single integrated identity solution.

M-Trends 2022 builds on our transparency to continue providing critical knowledge to those tasked with defending organizations. The information in this report has been sanitized to protect identities of victims and their data.

# BY THE NUMBERS
SPECIAL REPORT | MANDIANT M-TRENDS 2022

# Data From Mandiant Investigations
The metrics reported in M-Trends 2022 are based on Mandiant investigations of targeted attack activity conducted between October 1, 2020 and December 31, 2021.

This edition of M-Trends covers a 15-month period compared to a 12-month period in previous editions.

![Image description]

In APAC and EMEA, the majority of intrusions in 2021 were identified externally--a reversal of what was observed in 2020. The detection by source for Americas held steady with most intrusions continuing to be detected internally.

Detection by Source by Region, 2021

Detection by Source

Across the board, there was an increase in external notification of intrusions in 2021 compared to 2020. However, awareness of most intrusions continues to come about through internal detections. The percentage of intrusions detected internally has maintained a gradual upwards trend with moderate fluctuation over the last six years.

Detection by Source, 2011-2021

![Image description]

Internal detection is when an organization independently discovers it has been compromised.

External notification is when an outside entity informs an organization it has been compromised. This includes when a compromised organization is first notified of an incident by an attacker via an extortion note.

SPECIAL REPORT | MANDIANT M-TRENDS 2022

![Image description]

Detection by Source by Region, 2017–2021

In Americas, organizations detected intrusions internally in 60% of cases in 2021 compared to 61% of cases in 2020. There is relative stability in detection by source trends for Americas from 2017 to 2021.

Organizations in APAC were notified by an external entity in 76% of intrusions in 2021 compared to 48% of intrusions in 2020. Observations for 2021 are in line with observations for APAC from 2019. Mandiant experts have seen relatively large shifts in detection by source metrics for APAC over the past five years.

In EMEA, organizations were notified of an incident by an external entity in 62% of intrusions in 2021 compared to 47% of intrusions in 2020. Similar to APAC, when analyzing the five-year trend, there remains variability in detection by source in EMEA. The variability observed for both APAC and EMEA can be explained in part by continued maturity of organizations’ security programs as well as external entities’ notification ability in these regions.

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Dwell Time

The global median dwell time continued to improve in 2021 with organizations now detecting intrusions in three weeks. The global median dwell time for organizations that learned about their security incident through an external third party notification improved markedly in 2021. Not only are external entities doing more notifications of intrusions to organizations compared to 2020, they are also notifying them more quickly, resulting in shorter dwell times. The median dwell time for internally detected intrusions lengthened in 2021 compared to 2020 but remained shorter than median dwell time for external notifications.

Global Dwell Time

The global median dwell time for 2021 was 21 days compared to 24 days in 2020. This 13% improvement in global median dwell time was comprised of noteworthy changes in relation to source of detection. The global median dwell time for incidents which were identified externally dropped from 73 to 28 days. Conversely, incidents which were identified internally saw a lengthening of global median dwell time from 12 to 18 days.

There were significant improvements to global median dwell time when an external entity was the notification source. External entities are now detecting intrusions and notifying organizations in less than a month—62% faster compared to 2020. This speaks to improved detection capabilities of external entities in addition to more established communications and outreach programs.

Mandiant experts observed a 50% increase in global median dwell time for internally detected intrusions. The global median dwell time for internally detected intrusions rose from 12 days in 2020 to 18 days in 2021. While median dwell time for internal detections was slower compared to 2020, internal detections were still 36% faster than external notifications.

Dwell time is calculated as the number of days an attacker is present in a victim environment before they are detected. The median represents a value at the midpoint of a data set sorted by magnitude.

Global Median Dwell Time, 2011-2021

Change in Median Dwell Time
24 DAYS IN 2020
21 DAYS IN 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

![Image description]

Global Dwell Time Distribution

Global dwell time distribution continues to improve at both ends of the spectrum. In 2021, 55% of investigations had dwell times of 30 days or fewer with 67% of these (37% of total intrusions) being discovered in one week or less.

Mandiant experts observed a spike in dwell times between 90 and 300 days with 20% of investigations falling into this range. This could indicate intrusions going undetected until more impactful actions occur in the environment following initial infection and reconnaissance phases of the targeted attack lifecycle. This may also highlight a disparity between organizational detection capabilities and the types of attacks organizations face.

Fewer intrusions are going undetected for extensive periods of time. Only 8% of intrusions investigated in 2021 had a dwell time of more than a year and half of these (4% of total intrusions) had dwell times greater than 700 days.

Global Dwell Time Distribution, 2018–2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

![Image description]

Investigations involving Ransomware

Mandiant experts observed that the percentage of intrusions involving multifaceted extortion and ransomware was relatively stable from 2020 to 2021. In 2021, 23% of intrusions involved ransomware compared to 25% in 2020. These types of attacks continue to be a driving force of reduced median dwell times. Ransomware-related intrusions had a median dwell time of 5 days compared to 36 days for non-ransomware intrusions, making dwell times for ransomware intrusions one-seventh the duration of non-ransomware. While median dwell time for ransomware-related intrusions in 2021 remained the same as 2020, Mandiant experts noted a 20% reduction in median dwell time for non-ransomware intrusions year over year.

Global Dwell Time by Investigation Type, 2021

Change in Investigations Involving Ransomware
25% IN 2020
23% IN 2021

No Change in Global Median Dwell Time: Ransomware
5 DAYS IN 2020
5 DAYS IN 2021

Change in Global Median Dwell Time: Non-ransomware
45 DAYS IN 2020
36 DAYS IN 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

![Image description]

Americas Median Dwell Time, 2016–2021

Americas Median Dwell Time

The median dwell time for intrusions investigated in Americas remained constant at 17 days in 2021 compared to 2020. When considering detection source, there was a 9-percentage point increase in median dwell time for intrusions detected internally, increasing from 9 days in 2020 to 18 days in 2021. While median dwell time for internal detection did lengthen in 2021 compared to 2020, the six-year trend continues towards faster internal detections. Americas median dwell time for internal detections in 2020 demonstrated a major improvement, making it unsurprising this metric reverted some in 2021.

Intrusions with an external notification source had a median dwell time of 49 days in 2020 compared to only 15 days in 2021. External entities notified organizations in Americas 69% faster in 2021 compared to 2020.

In Americas 57% of intrusions were detected in fewer than 30 days in 2021, and 68% of these intrusions (39% of total Americas intrusions) were detected in less than one week. Not only are nearly half of intrusions being detected in two weeks or less, but also fewer intrusions are going undetected for extended periods of time. Mandiant experts observed a spike in intrusions with dwell times between 90 and 300 days, accounting for 22% of intrusions in Americas. Further, only 4% of intrusions in Americas had dwell times longer than one year.

AMERICAS

SPECIAL REPORT | MANDIANT M-TRENDS 2022

![Image description]

Americas Dwell Time by Investigation Type, 2021

Americas Dwell Time Distribution, 2021

In 2021, 22% of intrusions in Americas were related to ransomware—a 5.5-percentage point decrease compared to 2020. Even though there were fewer ransomware-related intrusions in Americas, these intrusions continue to impact the median dwell time. Ransomware intrusions in Americas had a median dwell time of 4 days compared to 32 days for non-ransomware intrusions.

Change in Investigations Involving Ransomware
27.5% IN 2020
22% IN 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

![Image description]

APAC Median Dwell Time, 2016–2021

APAC Median Dwell Time

All median dwell time metrics improved in APAC in 2021. The median dwell time for intrusions in APAC was just 21 days in 2021 compared to 76 days in 2020, a 72% improvement in median dwell time year over year.

In APAC, organizations are detecting intrusions quicker and external entities are notifying organizations of intrusions faster. Intrusions in APAC that were detected internally had a median dwell time of 22 days in 2021 compared to 33 days in 2020. The median dwell time for intrusions with an external notification source was 16 days in 2021 compared to 137 days in 2020—an 88% reduction.

The dwell time distribution for APAC reveals 60% of intrusions had dwell times of 30 days or fewer with 60% of these (36% of all APAC intrusions) detected in one week or less. At the other end of the spectrum, similar to observations from previous years, dwell time distribution in APAC continues to show that several intrusions go undetected for extended periods of time. Mandiant experts observed that 13% of intrusions in APAC in 2021 had dwell times that exceeded three years. Organizations in APAC have impressive detection capabilities. However, intrusions that go undetected initially can remain undetected, resulting in extensive dwell times when they are ultimately detected.

APAC

SPECIAL REPORT | MANDIANT M-TRENDS 2022

![Image description]

APAC Dwell Time by Investigation Type, 2021

APAC Dwell Time Distribution, 2021

Ransomware was more prevalent in APAC in 2021 compared to previous years. Ransomware-related intrusions accounted for 38% of intrusions investigated in APAC in 2021 compared to 12.5% of intrusions in 2020 and 18% of intrusions in 2019. Median dwell time in APAC for ransomware-related intrusions was 9 days compared to 38 days for non-ransomware intrusions.

Change in Investigations Involving Ransomware
12.5% IN 2020
38% IN 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

![Image description]

EMEA Median Dwell Time, 2016–2021

EMEA Median Dwell Time

In 2021, EMEA showed improvement in median dwell times across the board with the shortest dwell times ever observed for EMEA in all categories. The median dwell time for intrusions investigated in EMEA was just 48 days in 2021 compared to 66 days in 2020 and 54 days in 2019.

For intrusions detected internally in EMEA, the median dwell time improved from 29 days in 2020 to 13 days in 2021. Similarly, median dwell time for EMEA intrusions involving external notifications dropped from 225 days in 2020 to 60 days in 2021.

When examining dwell time distribution, 47% of intrusions in EMEA were detected within 30 days; 70% of these intrusions (33% of all EMEA intrusions) were detected within one week. EMEA also showed improvement in the percentage of intrusions with extended dwell times. In 2021, 5.5% of intrusions in EMEA had dwell times longer than three years, which is a 2.5-percentage point improvement over 2020.

EMEA

SPECIAL REPORT | MANDIANT M-TRENDS 2022

![Image description]

EMEA Dwell Time by Investigation Type, 2021

EMEA Dwell Time Distribution, 2021

In 2021, fewer investigations in EMEA were ransomware related—17% compared to 22% in 2020. However, the quick nature of ransomware intrusions contributed to the overall improvement of the median dwell time in EMEA. Mandiant experts observed that the 2021 median dwell time in EMEA for ransomware-related intrusions was only 4 days compared to 60 days for non-ransomware intrusions.

Change in Investigations Involving Ransomware
22% IN 2020
17% IN 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Industry Targeting

Mandiant continues to see consistent industry targeting by adversaries. In 2021 business/professional services and financial were the top targeted industries across the globe. Retail and hospitality, healthcare and high tech round out the top five industries favored by adversaries. Mandiant continues to see these same industries targeted across the globe every year.

![Image description]

Global Industries Targeted, 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Initial Infection Vector, 2021 (When Identified)

Targeted Attacks

Initial Infection Vector

Exploits remained the most frequently identified initial infection vector in 2021. In intrusions where the initial infector vector was identified, 37% started with an exploit—an 8-percentage point increase over 2020.

Supply chain compromise was the second most prevalent initial infection vector identified in 2021. When the initial infection vector was identified, supply chain compromise accounted for 17% of intrusions in 2021 compared to less than 1% in 2020. Further, 86% of supply chain compromise intrusions in 2021 were related to the SolarWinds breach and SUNBURST.[^1]

In 2021, Mandiant experts observed an uptick in intrusions with an initial infection vector due to a prior compromise. These intrusions include handoffs from one group to another and prior malware infections. Prior compromises accounted for 14% of intrusions where the initial infection vector was identified.

Mandiant experts observed far fewer intrusions initiated via phishing in 2021. When the initial compromise was identified, phishing was the vector in only 11% of intrusions in 2021 compared to 23% in 2020. This speaks to organizations’ ability to better detect and block phishing emails as well as enhanced security training of employees to recognize and report phishing attempts.

[^1]: Mandiant (December 13, 2021). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor.

![Image description]

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Threat actors continue to prioritize data theft as a primary mission objective. In 2021, Mandiant identified data theft in 29% of intrusions. In 32% of intrusions involving data theft (9% of all intrusions) the stolen data was specifically targeted for use as the threat actor’s leverage during negotiations for payment. In 12% of intrusions involving data theft (4% of all intrusions) the data theft likely supported intellectual property or espionage end goals.

In 2021 Mandiant experts observed a slight uptick in compromises that likely served only to compromise architecture for further attacks. In 2021, this activity was identified in 4% of intrusions, a 1-percentage point increase compared to 2020. Likewise, insider threat continues to be rare with only 1% of intrusions investigated by Mandiant related to insider threat. These metrics have remained relatively stable over years of reporting.

Financially motivated intrusions continue to be a mainstay in 2021, with adversaries seeking monetary gain in 3 out of 10 intrusions through methods such as extortion, ransom, payment card theft and illicit transfers. The percentage of financially motivated intrusions dropped to 30% in 2021 compared to the 38% of intrusions observed in 2020. Mandiant experts observed a 2-percentage point decrease specifically in ransomware-related incidents in 2021. Another likely contributing factor for decreased financial gain operations in 2021 was an increase in law enforcement action taken against financially motivated actors leading to arrests, takedown of servers and seizure of extorted funds.

![Image description]

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Multiple Threat Groups Identified, 2019-2021

Environment

In 2021, Mandiant experts identified that a quarter of victim environments had more than one distinct threat group. These environments included investigations with threat groups working together and attractive target environments enticing multiple threat actors independently. While the percentage of victim environments with multiple threat groups decreased in 2021 compared to 2020, the three-year trend demonstrates likely continued growth.

Adversaries frequently leveraged exploits in 2021 with 30% of all intrusions involving exploit activity. In 2021, major vulnerabilities were discovered in products such as Microsoft Exchange[^2],[^3], SonicWall’s Email Security (ES) product[^4], Pulse Secure VPN appliances[^5] and Apache’s Log4j 2 utility[^6] among others. Adversaries exploited these vulnerabilities to initiate and further intrusions. Mandiant experts even observed adversaries leverage vulnerabilities to deploy ransomware.[^7]

Exploit Activity

Change in Multiple Threat Groups Identified (per environment)
29% IN 2020
25% IN 2021

[^2]: Mandiant (March 4, 2021). Detection and Response to Exploitation of Microsoft Exchange Zero-Day Vulnerabilities.
[^3]: Mandiant (November 17, 2021). ProxyNoShell: A Change in Tactics Exploiting ProxyShell Vulnerabilities.
[^4]: Mandiant (April 20, 2021). Zero-Day Exploits in SonicWall Email Security Lead to Enterprise Compromise.
[^5]: Mandiant (April 20, 2021). Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day
[^6]: Mandiant (December 15, 2021). Log4Shell Initial Exploitation and Mitigation Recommendations.
[^7]: Mandiant (February 23, 2021). (Ex)Change of Pace: UNC2596 Observed Leveraging Vulnerabilities to Deploy Cuba Ransomware.

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Threat Groups

Mandiant experts currently track more than 2,800 threat groups, which include 1100+ newly tracked threat groups for this M-Trends reporting period. Mandiant continues to expand its extensive threat actor knowledgebase through clustering and attributing adversary activity observed not only during frontline investigations, but also from analysis of public reporting, information sharing and other research.

In 2021, Mandiant experts graduated two groups to named threat groups, FIN12[^8] and FIN13.[^9] Additionally, Mandiant merged 185 threat groups into other threat groups based on extensive research into activity overlaps. For details on how Mandiant defines and references UNC groups and merges, please see, “How Mandiant Tracks Uncategorized Threat Actors.”[^10]

![Image description]

Newly Tracked and Observed Threat Groups in 2021

Threat Groups 2021

[^8]: Mandiant (October 7, 2021). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets
[^9]: Mandiant (December 7, 2021). FIN13: A Cybercriminal Threat Actor Focused on Mexico
[^10]: Mandiant (December 17, 2020). DebUNCing Attribution: How Mandiant Tracks Uncategorized Threat Actors
*Mandiant tracks Advanced Persistent Threat (APT) groups 0-41. Over the years, APT 11 and APT 13 were merged into other groups and subsequently deprecated resulting in 40 APT groups actively tracked by Mandiant.

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Malware

Mandiant continuously expands its body of knowledge on malware based on insights gained from the frontlines of cyber incidents, public reporting and various other research avenues. In 2021, Mandiant began tracking over 700 new malware families. This number continues to grow in line with previous trends with no indication of slowing down.

In 2021, Mandiant experts observed adversaries use 365 distinct malware families during investigations of compromised environments. This number continues to grow in line with the number of observed malware families compared to previous years. Of the 365 malware families observed by Mandiant experts during intrusions, 154 were malware families which Mandiant began tracking in 2021.

A malware family is a program or set of associated programs with sufficient “code overlap” among the members that Mandiant considers them to be the same thing, a “family”. The term family broadens the scope of a single piece of malware as it can be altered over time, which in turn creates new, but fundamentally overlapping pieces of malware.

![Image description]

Newly Tracked and Observed Malware Families in 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Malware Category

A malware category describes a malware family’s primary purpose. Each malware family is assigned only one category that best describes its primary purpose, regardless of functionality for more than one category.

| Primary Purpose | Malware Category |
| ----------- | ----------- |
| A program whose primary purpose is to allow a threat actor to interactively issue commands to the system on which it is installed. | Backdoor |
| A utility whose primary purpose is to access, copy or steal authentication credentials. | Credential Stealer |
| A program whose sole purpose is to download (and perhaps launch) a file from a specified address, and which does not provide any additional functionality or support any other interactive commands. | Downloader |
| A program whose primary purpose is to extract, install and potentially launch or execute one or more files. | Dropper |
| A program whose primary purpose is to launch one or more files. Differs from a dropper or an installer in that it does not contain or configure the file, but merely executes or loads it. | Launcher |
| A program whose primary purpose is to perform some malicious action (such as encrypting data), with the goal of extracting payment from the victim in order to avoid or undo the malicious action. | Ransomware |
| Includes all other malware categories such as utilities, keyloggers, point-of-sale (POS), tunnelers and data miners. | Other |

Malware Families by Category

Of the 733 newly tracked malware families in 2021, the top five categories were backdoors (31%), downloaders (13%), droppers (13%), ransomware (7%), launchers (5%) and credential stealers (5%). These categories remain consistent with previous years.

![Image description]

Newly Tracked Malware Families by Category, 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Observed Malware Families by Category

Backdoors continue to be preferred by adversaries and consistently comprise the largest malware family category observed during Mandiant investigations over the years. Of the 365 malware families observed in 2021, the top categories were backdoors (40%), droppers (12%), ransomware (10%), downloaders (7%), credential stealers (5%) and launchers (4%).

Similar to newly tracked malware families, 22% of observed malware families in 2021 were comprised of the "other" malware family category. Compared to previous years, this number remains stable as adversaries create and use a variety of different tools to achieve their missions.

Mandiant observed a rise in the variety of ransomware malware families used by adversaries, growing the observed population from 8% in 2020 to 10% in 2021.

An observed malware family is a malware family identified during an investigation by Mandiant experts.

![Image description]

Observed Malware Families by Category, 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Newly Tracked Malware Families by Availability, 2021

Mandiant experts observed that 86% of newly tracked malware families were non-public whereas 14% were publicly available. The majority of new malware families tracked continue the trend of availability being restricted or likely privately developed.

Observed Malware Families by Availability, 2021

Similar to availability for newly tracked malware families, Mandiant experts observed 72% of malware families used by adversaries during an intrusion in 2021 were non-public and 28% were publicly available. Adversaries use both publicly and non-publicly available malware to accomplish missions across intrusions. While many adversaries often use the same publicly available malware families such as BEACON, Mandiant continues see adversaries innovate and adapt to be effective in victim environments.

A non-public tool or code family is, to the best of our knowledge, not publicly available (either for free or for sale). They may include tools that are privately developed, held or used, as well as tools that are shared among or sold to a restricted set of customers.

A publicly available tool or code family is readily obtainable without restriction. This includes tools that are freely available on the Internet, as well as tools that are sold or purchased, as long as they can be purchased by any buyer.

![Image description]

SPECIAL REPORT | MANDIANT M-TRENDS 2022

Most Frequently Seen Malware Families

The malware families seen most frequently during intrusions investigated by Mandiant experts were BEACON, SUNBURST, METASPLOIT, SYSTEMBC, LOCKBIT and RYUK. BEACON was once again the most prevalent malware family observed in 2021—three times more often than the second most frequently seen malware family. Further, use of BEACON across intrusions increased from 24% of intrusions in 2020 to 28% in 2021. BEACON remains by far the favorite malware family among adversaries and Mandiant expects its use will likely increase in the years to come.

SUNBURST[^12] was observed in 9% of all intrusions investigated by Mandiant in 2021. SUNBURST was delivered at scale to victim environments across the globe through a malicious update, resulting in widespread compromised access. This metric is in line with the observed relationship between the second most prevalent initial infection vector, supply chain compromises and the use of SUNBURST in intrusions.

RYUK and LOCKBIT were the most used ransomware families during intrusions investigated by Mandiant in 2021. Notably, newly graduated FIN12[^13] leveraged RYUK, BEACON, SYSTEMBC and METASPLOIT to carry out some of the most prolific intrusions seen throughout 2021. Ransomware families continue to contribute to the malware family collection every year.

Adversaries continue to use a variety of malware to carry out missions. In 2021, Mandiant observed just 3.8% of malware families being used in 10 or more intrusions while 81% of malware families were observed in only one or two intrusions. Over the years, Mandiant has observed adversary toolsets become more diverse as adversaries continue to evolve. This diversification is demonstrated by a continuation of limited retooling across intrusions.

Change in the use of BEACON
24% OF INTRUSIONS IN 2020
28% OF INTRUSIONS IN 2021

[^12]: Mandiant (December 13, 2020). FIN12: Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor
[^13]: Mandiant (October 7, 2021). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets

![Image description]

Most Frequently Seen Malware Families, 2021

SPECIAL REPORT | MANDIANT M-TRENDS 2022

BEACON is a backdoor that is commercially available as part of the Cobalt Strike software platform and commonly used for penetration testing network environments. The malware supports several capabilities, such as injecting and executing arbitrary code, uploading and downloading files and executing shell commands. Mandiant has seen BEACON used by a wide range of named threat groups including APT19, APT32, APT40, APT41, FIN6, FIN7, FIN9, FIN11, FIN12 and FIN13, as well as nearly 650 UNC groups.

SUNBURST is a .NET-based backdoor that initially communicates via DNS. SUNBURST generates the domain of the initial remote server using a domain generation algorithm. The DNS response returns a CNAME record containing the domain of the C2 server used for subsequent communication via HTTP. Supported backdoor commands include file download and execution, file management, registry manipulation, and process termination. SUNBURST can also disable targeted services to avoid detection and upload basic system information that includes the system’s IP address, DHCP configuration, and domain information. Mandiant has observed UNC2452 leverage SUNBURST.[^14]

METASPLOIT is a penetration testing platform that enables users to find, exploit, and validate vulnerabilities. Mandiant has seen METASPLOIT used by APT40, APT