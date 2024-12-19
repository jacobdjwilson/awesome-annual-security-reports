# M-TRENDS 2021
## FIREEYE MANDIANT SERVICES | SPECIAL REPORT

**Table of Contents**

[Executive Summary](#executive-summary)
[Expanding Knowledge by Sharing Intrusion Realities](#expanding-knowledge-by-sharing-intrusion-realities)
[By the Numbers](#by-the-numbers)
[Data From FireEye Mandiant Investigations](#data-from-fireeye-mandiant-investigations)
[Detection by Source](#detection-by-source)
[Dwell Time](#dwell-time)
[Industry Targeting](#industry-targeting)
[Targeted Attacks](#targeted-attacks)
[Threat Groups](#threat-groups)
[Malware](#malware)
[Ransomware](#ransomware)
[Ransomware Evolves Into Multifaceted Extortion](#ransomware-evolves-into-multifaceted-extortion)
[Steps toward Proactive Hardening Against Ransomware in Multiple Environments](#steps-toward-proactive-hardening-against-ransomware-in-multiple-environments)
[Recovery and Reconstitution Challenges in Post-Ransomware Scenarios](#recovery-and-reconstitution-challenges-in-post-ransomware-scenarios)
[Newly Named Threat Groups](#newly-named-threat-groups)
[FIN11](#fin11)
[Pandemic-Related Threats](#pandemic-related-threats)
[Threats Against Organizations Working with COVID-19 Information and Research](#threats-against-organizations-working-with-covid-19-information-and-research)
[UNC2452](#unc2452)
[Mapping UNC2452 Activity to the Targeted Attack Lifecycle Framework](#mapping-unc2452-activity-to-the-targeted-attack-lifecycle-framework)
[Case Studies](#case-studies)
[Insider Threat Risks to Flat Environments](#insider-threat-risks-to-flat-environments)
[Red Team Makes the Most of Social Engineering and System Misconfigurations](#red-team-makes-the-most-of-social-engineering-and-system-misconfigurations)
[Conclusion](#conclusion)
[More Security Awareness to Build Best Practices](#more-security-awareness-to-build-best-practices)

---

SPECIAL REPORT  M-TRENDS 2021       2

## Executive Summary

SPECIAL REPORT  M-TRENDS 2021       5

Security practitioners faced a series of challenges in this past year which forced organizations into uncharted waters. As ransomware operators were attacking state and municipal networks alongside hospitals and schools, a global pandemic response to COVID-19 necessitated a move to remote work for a significant portion of the economy. Organizations had to adopt new technologies and quickly scale outside of their normal growth plans. As organizations settled into a new understanding of “normal,” UNC2452, a suspected nation-state threat actor, conducted one of the most advanced cyber espionage campaigns in recent history. Many security teams were forced to suspend wide-ranging analyses around the adoption of remote work policies and instead focus on a supply chain attack from a trusted platform.

## Expanding Knowledge by Sharing Intrusion Realities

SPECIAL REPORT  M-TRENDS 2021       6

Nation states taking a cyber espionage approach to COVID research, threat groups working together to achieve their objectives, exploitation of quickly adopted work-from-home strategies and a wake-up call for global supply chain compromise – experiences in 2020 will shape security policies for years to come.

Themes covered in M-Trends 2021 include: :
*   59% of the security incidents investigated by Mandiant last year were initially detected by the organizations themselves, an improvement of 12% from the prior year.
*   Ransomware has evolved into multifaceted extortion where actors not only deploy ransomware encryptors across victim environments, but also employ a variety of other extortion tactics to coerce victims into complying with demands.
*   FIN11, a recently named financially motivated threat group, was responsible for widespread phishing campaigns, that conducted several multifaceted extortion operations.
*   Pervasive ransomware campaigns drove down the median dwell time as threat actors sought to capitalize on shifting trends in the workspace and a global crisis.

SPECIAL REPORT  M-TRENDS 2021       7

*   UNC2452, a suspected state-sponsored group, undertook a broad-scale espionage campaign after injecting a trojanized DLL into the SolarWinds Orion build process. Mandiant identified the campaign and worked with law enforcement agencies and industry partners to protect organizations and respond to the adversary.
*   Mandiant experts observed the use of 63% of MITRE ATT&CK techniques, and just over a third of techniques observed were seen in more than 5% of intrusions.
*   Threat actors took advantage of infrastructure supporting work-at-home with an increased focus on vulnerability exploitation.

One of the most striking trends for the period of October 1st, 2019 to September 30th, 2020 was the significant reduction in the global median dwell time. At 24 days, this is the first time Mandiant has observed the global median dwell time dip below one month. While this reduction in dwell time may correlate to better visibility and response, it is also likely the preponderance of ransomware helped drive down the time between initial infection and identification.

With the inclusion of all the observations listed above, the addition of new metrics reported in By The Numbers, the introduction of the named threat group FIN11, new case studies, and many other topics, M-Trends 2021 builds on our transparency to continue providing critical knowledge to those tasked with defending organizations. The information in this report has been sanitized to protect identities of victims and their data.

SPECIAL REPORT  M-TRENDS 2021       8

## BY THE NUMBERS

SPECIAL REPORT  M-TRENDS 2021       9

The metrics reported in M-Trends 2021 are based on FireEye Mandiant investigations of targeted attack activity conducted between October 1, 2019 and September 30, 2020.

### Data from FireEye Mandiant Investigations

### Detection by Source

Organizations continue to improve their ability to discover compromises within their environments. While M-Trends 2020 noted a drop in internal notifications for 2019 compared to 2018, Mandiant experts observed a return to organizations detecting the majority of incidents internally in 2020. Organizations increased internal incident detection to 59% in 2020—a 12-point increase compared to 2019. This return to organizations detecting the majority of intrusions within their environments is in line with the overall trend towards increased internal detection observed over the last decade. It shows a continued dedication to the expansion and enhancement of organic detection and response capabilities. The increase in ransomware activity affects this category as well.

Internal detection is when an organization independently discovers it has been compromised. External notification is when an outside entity informs an organization it has been compromised.

SPECIAL REPORT  M-TRENDS 2021       10

**Image Description:** A line graph titled "DETECTION BY SOURCE, 2011-2020" shows the percentage of internal and external detections from 2011 to 2020. Internal detections are represented by a solid line, and external detections by a dotted line. The graph shows a general trend of increasing internal detections and decreasing external detections over time. The values for each year are also displayed on the graph.

**Image Description:** A set of three bar charts titled "DETECTION BY SOURCE BY REGION, 2019-2020 COMPARISON" shows the percentage of internal and external detections in the Americas, EMEA, and APAC regions for 2019 and 2020. Each region has two bars, one for internal detections and one for external detections. The chart shows that internal detections increased in all regions in 2020 compared to 2019.

**Image Description:** A set of three pie charts titled "DETECTION BY SOURCE BY REGION, 2020" shows the percentage of internal and external detections in the Americas, EMEA, and APAC regions for 2020. Each pie chart is divided into two sections, one for internal detections and one for external detections. The chart shows the proportion of internal and external detections in each region.

SPECIAL REPORT  M-TRENDS 2021       11

### Dwell Time

Organizations continue to find and contain adversaries faster than in previous years. Over the past decade, there has been a marked reduction in median dwell time, from just over one year (2011) to just under one month (2020).

| Compromise Notifications | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 416 | 243 | 229 | 205 | 146 | 99 | 101 | 78 | 56 | 24 |
| External Notification | — | — | — | — | 320 | 107 | 186 | 184 | 141 | 73 |
| Internal Detection | — | — | — | — | 56 | 80 | 57.5 | 50.5 | 30 | 12 |

GLOBAL MEDIAN DWELL TIME, 2011-2020

Dwell time is calculated as the number of days an attacker is present in a victim environment before they are detected. The median represents a value at the midpoint of a data set sorted by magnitude.

#### Global Dwell Time

In 2020, the global median dwell time dropped below one month for the first time. Organizations are now detecting incidents in only 24 days—more than twice as fast as 2019. These improvements in detection hold true regardless of the notification source. Global median dwell time for incidents which were detected internally dropped to just 12 days and incidents with external notification sources came in at 73 days.

Median Dwell Time
416 DAYS IN 2011
24 DAYS IN 2020

SPECIAL REPORT  M-TRENDS 2021       12

#### Global Median Dwell Time Distribution

Globally, organizations are detecting more incidents within the first 30 days of an intrusion and fewer incidents with a dwell time longer than 700 days. The distribution of global dwell time continues to show an increased proportion of incidents with a dwell time of 30 days or fewer. In 2020, 52% of the compromises investigated by Mandiant experts had dwell times of 30 days or fewer, compared to 41% in 2019 and 31% in 2018. There were also improvements at the other end of the spectrum; Mandiant observed a 3% decrease in investigations with dwell times greater than 700 days.

The overall trends across multiple years could be explained by continued development and improvement of organizational detection capabilities and an evolution of the threat landscape.

**Image Description:** A stacked bar chart titled "GLOBAL MEDIAN DWELL TIME DISTRIBUTION, 2018-2020" shows the distribution of dwell times in days for the years 2018, 2019, and 2020. The chart shows that in 2020, a higher percentage of incidents had dwell times of 30 days or fewer compared to previous years.

SPECIAL REPORT  M-TRENDS 2021       13

A major factor contributing to the increased proportion of incidents with dwell times of 30 days or fewer is the continued surge in the proportion of investigations that involved ransomware, which rose to 25% in 2020 from 14% in 2019. Of these ransomware intrusions, 78% had dwell times of 30 days or fewer compared to 44% of non-ransomware intrusions. Mandiant experts also observed that only 1% of ransomware intrusions had dwell times of 700 days or more compared to 11% of non-ransomware intrusions.

**Image Description:** A bar chart titled "GLOBAL DWELL TIME BY INVESTIGATION TYPE, 2020" shows the percentage of investigations with different dwell time ranges for all investigations, ransomware investigations, and non-ransomware investigations. The chart shows that ransomware investigations have a significantly higher proportion of incidents with dwell times of 30 days or fewer compared to non-ransomware investigations.

Investigations Involving Ransomware
14 % IN 2019
25 % IN 2020

SPECIAL REPORT  M-TRENDS 2021       14

#### Americas Median Dwell Time

The Americas saw median dwell time continue to decrease in 2020. The dwell time for incidents which were discovered internally improved the most—from 32 days down to nine days. This is the first time Mandiant has observed the median dwell time in any region dip into single digits.

Median dwell time in the Americas was 3.5 times shorter in 2020 than in 2019. Companies were detecting incidents internally 3.6 times faster and receiving external notification of compromises 2.1 times faster.

In 2020, 27.5% of incidents investigated in the Americas involved ransomware. The large number of investigations which involved ransomware undoubtedly drove down the median dwell time. Ransomware incidents in the Americas had a median dwell time of just three days and accounted for 41% of incidents with a dwell time of 14 days or fewer.

Change in Americas Median Dwell Time
60 DAYS IN 2019
17 DAYS IN 2020

**Image Description:** A line graph titled "AMERICAS MEDIAN DWELL TIME, 2016-2020" shows the median dwell time in days for all, internal, and external notifications in the Americas region from 2016 to 2020. The graph shows a general trend of decreasing dwell times over the years, with a significant drop in 2020.

SPECIAL REPORT  M-TRENDS 2021       15

#### APAC Median Dwell Time

The median dwell time for APAC increased from 54 days in 2019 to 76 days in 2020. APAC saw a decrease in the number of ransomware-related breaches which accounted for 12.5% of incidents investigated in 2020 as compared to 18% in 2019. The reduction in ransomware-related incidents was a likely contributor to the overall increase in median dwell time for APAC.

Adversaries continue to maintain access in compromised organizations in APAC for extensive periods of time. Consistent with observations in 2019, 10% of breaches investigated in APAC during 2020 showed dwell times of more than three years and 4% were greater than nine years.

Change in APAC Median Dwell Time
76 DAYS IN 2020
54 DAYS IN 2019

**Image Description:** A line graph titled "APAC MEDIAN DWELL TIME, 2016-2020" shows the median dwell time in days for all, internal, and external notifications in the APAC region from 2016 to 2020. The graph shows that the dwell time increased in 2020 compared to 2019.

SPECIAL REPORT  M-TRENDS 2021       16

#### EMEA Median Dwell Time

The median dwell time for EMEA increased from 54 days in 2019 to 66 days in 2020. Mandiant experts observed that 28% of incidents in EMEA had a dwell time of one week or less, and 8% of incidents had dwell times longer than three years. Organizations in EMEA continue to respond to long-standing intrusions while also contending with faster paced compromises such as ransomware.

When separated by notification source, median dwell time for EMEA increased for incidents discovered internally but decreased when companies were notified of a compromise by an external entity. For incidents that were detected internally, EMEA saw median dwell time increase by 20%, from 23 days in 2019 to 29 days in 2020. Conversely, compromises in EMEA with an external notification source had a 25% decrease in median dwell time, from 301 days in 2019 to 225 days in 2020.

Change in EMEA Median Dwell Time
66 DAYS IN 2020
54 DAYS IN 2019

**Image Description:** A line graph titled "EMEA MEDIAN DWELL TIME, 2016-2020" shows the median dwell time in days for all, internal, and external notifications in the EMEA region from 2016 to 2020. The graph shows that the dwell time increased in 2020 compared to 2019.

SPECIAL REPORT  M-TRENDS 2021       17

### Industry Targeting

Mandiant has observed that the most targeted industries continue to remain consistent year over year. The top five most targeted industries in 2020 were business and professional services, retail and hospitality, financial, healthcare, and high technology. Over the past decade, business and professional services and financial have consistently placed in the top five most targeted industries. Overall, the top targeted industries change little while position in the rankings is somewhat fluid.

#### Big Movers

Mandiant experts observed that retail and hospitality organizations were targeted more heavily in 2020, coming in as the second most targeted industry, compared to 11th in 2019. Healthcare rose to 3rd most targeted industry in 2020, compared to 8th in 2019. In the other direction, Mandiant experts observed a decrease in targeting of entertainment and media which dropped from the most targeted industry in 2019 to 6th in 2020.

SPECIAL REPORT  M-TRENDS 2021       18

**Image Description:** A table titled "TARGETED INDUSTRIES, 2015-2020" shows the ranking of different industries based on the number of targeted attacks from 2015 to 2020. The table shows that Business/Professional Services and Financial industries have consistently been among the top targeted industries. The table also shows that Retail/Hospitality and Healthcare industries have moved up in the rankings in 2020.

SPECIAL REPORT  M-TRENDS 2021       19

## Targeted Attacks

Mandiant experts responded to a wide variety of intrusions in 2020, making observations about initial infection vectors, adversary operations and victim environments.

### Initial Infection Vector

While phishing remains an effective vector for initial compromise, in 2020, Mandiant observed adversaries leveraging exploits more often than other vectors. In cases where the initial vector of compromise was identified, evidence of exploits was found in 29% of intrusions whereas phishing accounted for 23% of intrusions. Mandiant experts also observed adversaries used stolen credentials or brute forcing as the initial attack vector in 19% of the investigations. Prior compromise accounted for 12% of the intrusions in which the initial compromise was identified.

### Adversary Operations

Adversaries continue to use intrusions for monetary gain through methods that include extortion, ransom, payment card theft and illicit transfers. Direct financial gain was the likely motive for 36% of intrusions and an additional 2% of intrusions were likely perpetrated to resell access.

In 2020, data theft remained an important mission objective for threat actors. In 32% of intrusions adversaries stole data and in 29% of those cases (9% of all cases) the data theft likely supported intellectual property or espionage end goals. Approximately 3% of intrusions likely only served to compromise architecture for further attacks, and insider threats remain rare, represented by fewer than 1% of intrusions.

### Environment

In 29% of cases, Mandiant experts identified more than one distinct threat group in the victim environment—nearly twice the percentage noted in 2019.

Multiple Threat Groups Identified (per environment)
29 % in 2020
15 % in 2019

**Image Description:** A set of three pie charts showing the breakdown of initial infection vectors, objectives for financial gain, and objectives for data theft. The pie chart for initial infection vectors shows that exploits and phishing are the most common vectors. The pie chart for financial gain shows that direct financial gain is the primary motive. The pie chart for data theft shows that data theft is a significant objective, with a portion of it supporting IP/Espionage.

Initial Infection Vector (when identified)
Exploits 29%
Phishing 23%

Objective: Financial Gain
Direct 36%
Resell Access 2%

Objective: Data Theft
IP/Espionage 9%
Data Theft 32%

SPECIAL REPORT  M-TRENDS 2021       20

## Threat Groups

Over the course of Mandiant’s history, Mandiant experts have tracked more than 2,400 threat groups, which includes 650+ newly tracked threat groups in 2020. Mandiant experts have combined or eliminated approximately 500 of these groups over the years, leaving more than 1,900 distinct threat groups tracked at this time. By expanding and refining a vast threat actor knowledgebase, Mandiant can support a broad spectrum of investigations while maintaining fidelity within that dataset. In 2020, Mandiant experts graduated one group to a named threat group and merged 75 threat groups based on extensive research into activity overlaps. For details on how Mandiant defines and references UNC groups and merges, please see, “How Mandiant Tracks Uncategorized Threat Actors.”<sup>1</sup>

In 2020, Mandiant experts investigated intrusions that involved 246 distinct threat groups. Organizations faced intrusions by four named financial threat (FIN) groups; six named advanced persistent threat (APT) groups, including groups from the nation-states of China, Iran and Vietnam; and 236 uncategorized threat (UNC) groups. Of the 246 threat groups observed at intrusion clients, 161 of these threat groups were newly tracked threat groups in 2020.

**Image Description:** A graphic titled "THREAT GROUPS, 2020" shows the breakdown of threat groups tracked by Mandiant in 2020. The graphic shows that there are 1900+ total groups, with 652 UNC groups identified in 2020 (75 merged), 11 FIN groups (1 graduated), and 41 APT groups. The graphic also shows that there were 236 active UNC groups, 4 active FIN groups, and 6 active APT groups in 2020. The graphic also lists the geolocations and nation-states associated with the active groups.

1.  FireEye (December 17, 2020). DebUNCing Attribution: How Mandiant Tracks Uncategorized Threat Actors.

**Image Description:** A graphic showing the number of newly tracked, newly tracked and observed, and observed threat groups in 2020. The graphic shows that 652 threat groups were newly tracked, 161 were newly tracked and observed, and 246 were observed.

SPECIAL REPORT  M-TRENDS 2021       21

## Malware

Mandiant continually expands its knowledgebase of malware families based on insights gained from frontline Mandiant investigations, public reporting, information sharing and other research. In 2020, Mandiant began tracking more than 500 new malware families. This is on par with the number of newly tracked malware families compared to the previous year.

Mandiant responds to hundreds of diverse intrusions each year where adversaries provide organizations with unique challenges. In 2020, Mandiant experts observed 294 distinct malware families in use during investigations into compromised environments. Of the nearly 300 malware families observed by Mandiant experts during intrusions, 144 were malware families which Mandiant began tracking in 2020. Adversaries not only use established malware but also continue to innovate and adapt to be effective in victim environments.

A malware family is a program or set of associated programs with sufficient “code overlap” among the members that Mandiant considers them to be the same thing, a “family”. The term family broadens the scope of a single piece of malware as it can be altered over time, which in turn creates new, but fundamentally overlapping pieces of malware.

**Image Description:** A graphic showing the number of newly tracked, newly tracked and observed, and observed malware families in 2020. The graphic shows that 514 malware families were newly tracked, 144 were newly tracked and observed, and 294 were observed.

SPECIAL REPORT  M-TRENDS 2021       22

**Image Description:** A pie chart titled "NEWLY TRACKED MALWARE FAMILIES BY CATEGORY, 2020" shows the distribution of newly tracked malware families by category. The chart shows that backdoors are the most common category, followed by downloaders, droppers, launchers, and ransomware.

### Malware Families by Category

The malware category distribution remains relatively consistent year over year. Of the 514 newly tracked malware families in 2020, the top five categories were backdoors (36%), downloaders (16%), droppers (8%), launchers (7%) and ransomware (5%).

A malware category describes a malware family’s primary purpose. Each malware family is assigned only one category that best describes its primary purpose, regardless if it has functionality for more than one category.

| Malware category | Primary purpose |
|---|---|
| Backdoor | A program whose primary purpose is to allow a threat actor to interactively issue commands to the system on which it is installed. |
| Credential Stealer | A utility whose primary purpose is to access, copy or steal authentication credentials. |
| Downloader | A program whose sole purpose is to download (and perhaps launch) a file from a specified address, and which does not provide any additional functionality or support any other interactive commands. |
| Dropper | A program whose primary purpose is to extract, install and potentially launch or execute one or more files. |
| Launcher | A program whose primary purpose is to launch one or more files. Differs from a dropper or an installer in that it does not contain or configure the file, but merely executes or loads it. |
| Ransomware | A program whose primary purpose is to perform some malicious action (such as encrypting data), with the goal of extracting payment from the victim in order to avoid or undo the malicious action. |
| Other | Includes all other malware categories such as utilities, keyloggers, point of sale (POS), tunnelers and data miners. |

SPECIAL REPORT  M-TRENDS 2021       23

**Image Description:** A pie chart titled "OBSERVED MALWARE FAMILIES BY CATEGORY, 2020" shows the distribution of observed malware families by category. The chart shows that backdoors are the most common category, followed by downloaders, droppers, ransomware, and launchers.

### Observed Malware Families by Category

Backdoors are a mainstay for adversaries and consistently comprise the largest malware family category observed during investigations. Mandiant experts observed that attackers deployed at least one backdoor in more than half of the intrusions investigated. Of the 294 malware families observed in 2020, the top five categories were backdoors (41%), downloaders (9%), droppers (9%), ransomware (8%) and launchers (6%).

An observed malware family is a malware family identified during an investigation by Mandiant experts.

SPECIAL REPORT  M-TRENDS 2021       24

**Image Description:** A pie chart titled "NEWLY TRACKED MALWARE FAMILIES BY AVAILABILITY, 2020" shows the distribution of newly tracked malware families by availability. The chart shows that 81% of newly tracked malware families were non-public, and 19% were public.

### Newly Tracked Malware Families by Availability

Mandiant experts observed that 81% of newly tracked malware families were non-public whereas 19% were publicly available. While adversaries do use publicly available tools and code, the majority of malware families tracked were likely privately developed or their availability is restricted.

A publicly available tool or code family is readily obtainable without restriction. This includes tools that are freely available on the Internet, as well as tools that are sold or purchased, as long as they can be purchased by any buyer. A non-public tool or code family is, to the best of our knowledge, not publicly available (either for free or for sale). They may include tools that are privately developed, held or used, as well as tools that are shared among or sold to a restricted set of customers.

SPECIAL REPORT  M-TRENDS 2021       25

**Image Description:** A pie chart titled "OBSERVED MALWARE FAMILIES BY AVAILABILITY, 2020" shows the distribution of observed malware families by availability. The chart shows that 78% of observed malware families were non-public, and 22% were public.

### Observed Malware Families by Availability

Similar to the availability for newly tracked malware families, in 2020, Mandiant experts observed that 78% of malware families used by adversaries during an intrusion were non-public and 22% were publicly available.

SPECIAL REPORT  M-TRENDS 2021       26

**Image Description:** A bar chart titled "MOST FREQUENTLY SEEN MALWARE FAMILIES, 2020" shows the percentage of intrusions in which the top 5 most frequently seen malware families were observed. The chart shows that BEACON was the most frequently seen malware family, followed by EMPIRE, MAZE, NETWALKER, and METASPLOIT.

### Most Frequently Seen Malware Families

The top five malware families seen most frequently during intrusions investigated by Mandiant experts were BEACON, EMPIRE, MAZE, NETWALKER, and METASPLOIT. BEACON was so prevalent in 2020 that it was observed at nearly a quarter of all the intrusions Mandiant investigated. Mandiant experts also observed a lack of cross-pollination with respect to the malware used across incidents. Just 3.4% of malware families seen during an intrusion were observed at 10 or more intrusions, and 70% percent of malware families seen were only observed during a single intrusion.

*   BEACON is a backdoor that is commercially available as part of the Cobalt Strike software platform and commonly used for pen-testing network environments. The malware supports several capabilities, such as injecting and executing arbitrary code, uploading and downloading files and executing shell commands. Mandiant has seen BEACON used by a wide range of named threat groups including APT19, APT32, APT40, APT41, FIN6, FIN7, FIN9 and FIN11, as well as nearly 300 UNC groups.
*   EMPIRE is a publicly available PowerShell post-exploitation framework that allows users to run PowerShell agents without the use of powershell.exe. PowerShell Empire also allows actors to run various types of post-exploitation modules and make adaptable communications while evading detection. Mandiant experts track 90 threat groups that have utilized EMPIRE including APT19, APT33, FIN10, FIN11 and 86 UNC Groups.
*   MAZE is a ransomware family that encrypts files stored locally and on network shares. MAZE can be configured to infect remote and removable drives as well as send basic system information via HTTP. Mandiant has observed a dozen distinct financially motivated threat groups leverage MAZE ransomware.
*   NETWALKER is a ransomware family capable of deleting volume shadow copies and encrypting files on a victim host and any mapped network drives using a combination of SALSA20 and Curve25519 encryption algorithms. Mandiant tracks eight threat groups that have used NETWALKER ransomware to further their monetary end goals.
*   METASPLOIT is a penetration testing platform that enables users to find, exploit, and validate vulnerabilities. Mandiant has seen METASPLOIT used by APT40, APT41, FIN6, FIN7, FIN11 and 40 UNC groups with end goals ranging from espionage and financial gain to penetration testing.

SPECIAL REPORT  M-TRENDS 2021       27

**Image Description:** A set of two pie charts titled "EFFECTIVENESS OF NEWLY TRACKED MALWARE FAMILIES BY OPERATING SYSTEM, 2020" and "EFFECTIVENESS OF OBSERVED MALWARE FAMILIES BY OPERATING SYSTEM, 2020" showing the effectiveness of malware families on different operating systems. The charts show that the majority of malware families are effective on Windows.

### Operating System Effectiveness

In keeping with previous trends, the majority of newly tracked malware families were effective on Windows. Only 8% and 3% of newly tracked malware families were effective on Linux and MacOS, respectively.

Similar to trends seen for newly tracked malware families, the majority of malware families observed during Mandiant investigations were effective on Windows. Malware effective on Linux and MacOS was also observed but accounted for only 13% and 5% of malware families, respectively.

The operating system effectiveness of a malware family is the operating system(s) that the malware can be used against.

SPECIAL REPORT  M-TRENDS 2021       28

## Threat Techniques

Mandiant continues to support community and industry efforts by mapping its findings to the MITRE ATT&CK framework. In 2020, significant changes were made to the MITRE ATT&CK framework with the introduction of sub-techniques and the incorporation of PRE-ATT&CK in Enterprise ATT&CK. Due in part to these changes and the continued refinement of its data model, Mandiant now has MITRE ATT&CK techniques mapped to more than 1800 Mandiant techniques and subsequent findings.

When making security decisions, organizations must consider the likelihood of specific techniques being used during an intrusion. In 2020, Mandiant experts observed attackers use 63% of MITRE ATT&CK techniques and 24% of sub-techniques. However, only 37% of the techniques observed (23% of all techniques) were seen in more than 5% of intrusions.

In more than half of the intrusions investigated in 2020, Mandiant observed that adversaries used obfuscation, such as encryption or encoding, on files or information to make detection and subsequent analysis more difficult (T1027). Adversaries regularly used a command or scripting interpreter to further intrusions (T1059) and 80% of those cases involved the use of PowerShell (T1059.001). System services (T1569) were also a popular execution method, represented in 31% of intrusions, all of which used Windows services (T1569.002). Adversaries also used Remote Services (T1021) to further intrusions, with 88% of those using the Remote Desktop Protocol (T1021.001). Adversaries often take advantage of what is available in a victim’s environment; this tendency is highlighted by how frequently adversaries used PowerShell, Windows services and Remote Desktop.

MITRE ATT&CK® is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base is used as a foundation for the development of specific threat models and methodologies in the private sector, government and the cyber security product and service community.

**Image Description:** A graphic showing the percentage of MITRE ATT&CK techniques observed in Mandiant investigations and the percentage of those techniques seen in more than 5% of intrusions.

MITRE ATT&CK TECHNIQUES USED MOST FREQUENTLY, 2020
Observed in Mandiant Investigations 63%
Seen in More Than 5% of Intrusions 23%

SPECIAL REPORT  M-TRENDS 2021       29

**Image Description:** A graphic titled "FREQUENTLY TARGETED TECHNOLOGIES, 2020" showing the most frequently targeted technologies for intrusions using remote services (T1021), system services (T1569), and command or scripting interpreter (T1059).

FREQUENTLY TARGETED TECHNOLOGIES, 2020

for intrusions using remote services (T1021)
88% Remote Desktop Protocol (T1021.001)
Used in 25% of all intrusions

for intrusions using system services (T1569)
100% Windows services (T1569.002)
Used in 31% of all intrusions

for intrusions using command or scripting interpreter (T1059)
80% PowerShell (T1059.001)
Used in 41% of all intrusions

SPECIAL REPORT  M-TRENDS 2021       30

**Image Description:** A table titled "MITRE ATT&CK TECHNIQUES RELATED TO ATTACK LIFECYCLE, 2020" showing the MITRE ATT&CK techniques used in different