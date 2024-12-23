# SPECIAL REPORT: MANDIANT M-TRENDS 2024

## Table of Contents
- [Introduction](#introduction)
- [By the Numbers](#by-the-numbers)
- [Global Trends](#global-trends)
- [Campaigns and Global Events](#campaigns-and-global-events)
- [Regional Trends](#regional-trends)
  - [Americas](#americas)
  - [JAPAC](#japac)
  - [EMEA](#emea)
- [MITRE ATT&CK](#mitre-attck)
- [Articles](#articles)
  - [Chinese Espionage Operations Targeting The Visibility Gap](#chinese-espionage-operations-targeting-the-visibility-gap)
  - [Attacker Operations Involving Zero-Days Vary Depending on Motivation](#attacker-operations-involving-zero-days-vary-depending-on-motivation)
  - [Evolution of Phishing Amid Shifting Security Controls](#evolution-of-phishing-amid-shifting-security-controls)
  - [How Attackers Leverage AiTM to Overcome MFA](#how-attackers-leverage-aitm-to-overcome-mfa)
  - [Cloud Intrusion Trends](#cloud-intrusion-trends)
  - [Artificial Intelligence in Red (and Purple) Team Operations](#artificial-intelligence-in-red-and-purple-team-operations)
- [Conclusion](#conclusion)
- [Bibliography](#bibliography)

# Introduction
One of the big takeaways from our 2023 engagements, and consequently a key theme of M-Trends 2024, is that attackers are focusing more on evasion. They are aiming to avoid detection technologies (such as endpoint detection and response) and maintain persistence on networks for as long as possible, either by targeting edge devices, leveraging “living off the land” and other techniques, or through the use of zero-day vulnerabilities in security and other solutions prevalent throughout enterprises.

Despite attackers’ efforts to evade detection, defenders are continuing to get better at identifying compromises. The global median dwell time—dwell time is the number of days an attacker is on a system from compromise to detection—continued its downward trend in 2023, and is now 10 days (from 16 days in the previous year). It’s a big victory for the good guys, but ransomware is still a key factor in driving down dwell time since it tends to be detected more quickly. Furthermore, Mandiant red teams typically achieve their objectives in 5 to 7 days, so defenders must remain vigilant.

M-Trends 2024 features data and other security metrics that readers have come to expect, highlights zero-day use by espionage and financially-motivated attackers, and dives deep into evasive actions conducted particularly by Chinese espionage groups. Other key takeaways in this report include:
- Evolving phishing trends such as attacker use of social media, SMS and other communications technologies
- Tactics to bypass multi-factor authentication such as adversary-in-the-middle and other techniques
- Cloud intrusion trends such as targeting of cloud infrastructure as well as attacker use of cloud resources
- Use of AI in red and purple team engagements, with a focus on how new technologies can help produce better outcomes for organizations

Mandiant consultants are always on the frontlines, investigating and analyzing the latest cyber attacks, and understanding how best to defend against them. Consultants proactively assess clients against the latest attacker tactics, techniques and procedures, and help with remediation, transformation and education.

Through the release of our annual M-Trends report, we share our learnings with the greater security community, building on our dedication to providing critical knowledge to those tasked with defending organizations. The information in this report has been sanitized to protect the identities of victims and their data.

# By the Numbers
## Detection by Source
In 2023, more than half of compromised organizations (54%) first learned of a compromise from an external source, while 46% first identified evidence of a compromise internally. However, separating out ransomware-related intrusions reveals that it was much more common for an organization to learn of a ransomware-related incident from an external source. For ransomware-related intrusions, 70% of organizations were externally notified, in most cases, via a ransom demand from the attacker. For intrusions that were not linked to ransomware, the ratio of internal versus external discovery was even, 50% to 50%. Of the internally discovered intrusions, 85% did not involve ransomware.

The percentage of externally notified intrusions decreased from 63% in 2022 to 54% in 2023. Mandiant also responded to more ransomware-related intrusions in 2023 than in 2022. Ransomware events are most often discovered through external means. Despite this, Mandiant observed a nine point drop in external notifications. This year-over-year shift, along with the high proportion of internally discovered compromises in cases other than ransomware, suggests that organizations are experiencing higher rates of success in detecting malicious behavior on their networks.

Internal detection is when an organization independently discovers it has been compromised, such as through an internal security appliance alert or internal personnel notification of suspicious activity.

External notification is when an outside entity, such as law enforcement agencies, cybersecurity companies, or industry partners, informs an organization it has been compromised. In some cases, attackers will perform this notification, such as through a ransom note.

The metrics reported in M-Trends 2024 are based on Mandiant Consulting investigations of targeted attack activity conducted between January 1, 2023 and December 31, 2023.

![Detection by Source, 2011-2023]

## Ransomware-Related Intrusions
In 70% of cases, organizations learned of ransomware-related intrusions from external sources. Organizations were notified of a ransomware incident by an attacker ransom note in three fourths of those intrusions. This is consistent with the extortion business model in which attackers intentionally and abruptly notify organizations of a ransomware intrusion and demand payment. The remaining quarter of external notifications for ransomware intrusions came from external partners, such as law enforcement or security companies.

In 2022, attacker notifications represented two thirds of external notifications for ransomware intrusions, compared to one third coming from external partners.

A ransomware-related intrusion provides access for or is associated with an attacker that has the primary goal of encrypting data, with the intention of extracting payment from the target in order to avoid further harm or to undo the malicious action.

![Detection by Source, by Investigation Type, 2023]
![Ransomware External Notification Source, 2023]

## Dwell Time
Global median dwell time continued a downward trend marking another notable shortest time period between initial intrusion and detection for all M-Trends reporting periods. In 2023, most organizations detected intrusions within 10 days of the initial intrusion. This is a decline of nearly one week compared to 16 days in 2022.

Mandiant defenders observed notable improvements in global median dwell time in 2023 across all notification sources. With the shortest periods across the board, global median dwell time for external notification sources decreased to 13 days in 2023 from 19 days in 2022. This likely indicates improved communication between organizations targeted and external parties making notifications. Another likely explanation for this decrease could be the increase of ransomware-related adversary notifications.

Maintaining the ongoing trend, when defenders detect adversary intrusions internally, they do so faster than the overall median dwell time. The global median dwell time for intrusions detected internally was nine days in 2023, down from 13 days in 2022 and from 18 days in 2021.

Dwell time is calculated as the number of days an attacker is present in a compromised environment before they are detected. The median represents a value at the midpoint of a dataset sorted by magnitude.

![Global Median Dwell Time, 2011-2023]

Change in Median Dwell Time
days in 2022: 16
days in 2023: 10

## Global Dwell Time Distribution
Dwell time distribution measures the percentage of Mandiant-investigated intrusions with a specific range of dwell time. In 2023, Mandiant experts continued to see intrusions detected earlier, with 43% of intrusions being detected in one week or less. Nearly two thirds of all intrusions in 2023 were detected within 30 days. This likely indicates that detection capabilities continue to improve across organizations, allowing defenders to be notified of threats during the initial infection or reconnaissance phases of the targeted attack lifecycle, similar to previous M-Trends reports.

Mandiant observed a decrease in intrusions that remain undiscovered for long periods of time compared to previous years. In 2023, 6% of investigations identified activity that remained undetected for between 1 and 5 years, compared to 11% in 2022 and higher percentages prior to 2020. Although organizations are still facing intrusions that go undetected for longer periods of time, defenders will likely see the distribution of dwell time move to the left as external parties, such as security vendors and law enforcement, increase their involvement and pace of notifications. However, detection capabilities and continuous hunting throughout environments have been effective at unearthing long-standing intrusions. As actionable information is shared, detection capabilities will continue to improve.

Broadly, the long-term trends of declining median dwell time and increasing rates of internal discovery of compromises indicate that organizations have made meaningful, measurable improvements in their defensive capabilities.

![Global Dwell Time Distribution, 2018-2023]

## Investigations Involving Ransomware
In 2023, global investigations involving ransomware increased five percentage points to 23% of investigations in 2023 compared to 18% in 2022. This brings the percentage of ransomware-related intrusions back to where it was previously in 2021.

Globally, organizations detected ransomware or received a ransom demand faster in 2023–in five days compared to nine days in 2022–regardless of notification source. Non-ransomware-related intrusions were detected in 13 days, compared to 17 days in 2022. Intrusions involving ransomware were detected in six days when the notification came from an internal source, compared to 12 days in 2022. Defenders were notified of ransomware-related intrusions from an external party in five days in 2023, two days quicker than what was observed in 2022.

![Global Dwell Time by Investigation Type, 2023]

Change in Global Investigations Involving Ransomware
in 2022: 18%
in 2023: 23%

Change in Global Dwell Time—Ransomware
days in 2022: 9
days in 2023: 5

Change in Global Dwell Time—Non-Ransomware
days in 2022: 17
days in 2023: 13

Ransomware attacks have continued to be a driving factor in reducing dwell time over the years. However, in 2023, Mandiant experts observed notable improvements in decreased dwell time across all notification sources and investigation types.

Intrusions that did not involve ransomware were identified in a shorter period of time in 2023. Notably, intrusions that occurred in 2023 were identified internally in little over a week, with nine days between initial intrusion and detection, compared to 13 days in 2022. Organizations were notified by an external party of an intrusion one week faster in 2023, resulting in a 20-day median dwell time for externally notified, non-ransomware-related intrusions, compared to 27 days in 2022.

![Global Median Dwell Time by Detection Source]

## Industry Targeting
In 2023, Mandiant most frequently responded to intrusions at financial services organizations, followed by business and professional services, high tech, retail and hospitality, and healthcare. All of these sectors have access to a variety of sensitive information, including proprietary business information, personally identifiable information (PII), protected health information (PHI), and financial data. Attackers have also abused service providers and technology organizations to facilitate third-party compromises or to obtain access to data or networks belonging to many organizations through a single compromise. Mandiant consistently finds these sectors toward the top of the list for share of investigations. Government sector investigations declined from first to tied for fifth with healthcare in 2023, potentially reflecting fewer new investigations related to the war in Ukraine compared to 2022.

![Global Industries Targeted, 2023]

## Targeted Attacks
### Initial Infection Vector
In 2023, Mandiant experts once again saw exploits used as the most prevalent adversary initial infection vector. In intrusions where the initial intrusion vector was identified, 38% of intrusions started with an exploit. This is a six percentage point increase from 2022, consistent with what defenders faced in 2021. For more information, please see “Attacker Operations Involving Zero-Days Vary Depending on Motivation”.

Phishing remained the second most common intrusion vector. However it declined in 2023, with 17% of intrusions, compared to 22% in 2022. Phishing remains an effective method to establish an initial foothold and a popular threat vector for adversaries. Full analysis can be found in “Evolution of Phishing Among Shifting Security Controls”.

Prior compromises were the third most significant intrusion vector used by attackers in 2023. Mandiant investigators noted a three percentage point increase in 2023 compared to what was observed in 2022 with 15% of intrusions beginning with access provided by a prior compromise. This increase is likely related to the ransomware ecosystem and the continued partnership between ransomware affiliates and various malware operators selling initial access.

![Initial Infection Vector (When Identified)]

Stolen credentials pose a serious security risk to organizations and were the fourth most notable initial intrusion vector in 2023. Attackers often obtain credentials due to password reuse or users inadvertently downloading trojanized software on corporate devices. Infostealers are frequently delivered through trojanized software. In 2023, 10% of intrusions began with evidence of stolen credentials, compared to 14% observed in 2022. The prevalence of both widespread information stealer malware and credential purchasing continue to challenge defenders.

Brute-force attacks round out the top five initial intrusion vectors observed in 2023, representing 6% of intrusions. Proper implementation of multi-factor authentication has been pivotal to slowing down attackers in their attempts to compromise environments. Attackers continue to leverage effective tactics to gain access to target environments and conduct their operations. While the most popular infection vectors fluctuate, organizations must focus on defense-in-depth strategies. This approach can help mitigate the impact of both common and less frequent initial intrusion methods.

In 2023, when the initial intrusion vector was identified, an exploit was observed 38% of the time. Mandiant continues to observe both cyber espionage and financially motivated attackers leveraging zero-day vulnerabilities to conduct their operations. The most prevalent vulnerability Mandiant investigators observed in 2023 was CVE-2023-34362[^1], an SQL injection vulnerability in MOVEit Transfer that Mandiant rated as high risk.[^2] The second most prevalent vulnerability was CVE-2022-21587, a critical unauthenticated file upload vulnerability in Oracle E-Business Suite. The third most prevalent vulnerability in 2023 was CVE-2023-2868. CVE-2023-2868 is a critical command injection vulnerability in Barracuda Email Security Gateways (physical appliances). These vulnerabilities were heavily exploited by attackers, and notably the first and third most targeted vulnerabilities were related to edge devices. For more information on the continued targeting of these devices, please see Chinese Espionage Operations Targeting The Visibility Gap.

However, Mandiant experts also observed attackers’ continued use of exploits throughout the attack lifecycle to maintain access, move laterally, and complete their mission. Mandiant continues to observe a handful of vulnerabilities related to older technologies, such as Microsoft Access 2003 (CVE-2008-2463),[^3] Microsoft Windows Server 2016 (CVE-2017-0144),[^4] and Telerik (CVE-2019-18935).[^5]

![Most Frequently Seen Vulnerabilities]

## Post-Compromise Activity
### Financial Gain
The proportion of intrusions Mandiant responded to that served financially motivated objectives increased from more than a quarter of all investigations, 26%, in 2022 to more than a third, 36%, in 2023. Ransomware-related intrusions represented almost two thirds of financially motivated intrusions and 23% of all 2023 intrusions.

The remaining financially motivated intrusions included data theft extortion without ransomware encryption, attackers establishing initial access to facilitate other operations, business email compromise (BEC) fraud, and cryptocurrency theft events. Mandiant attributed several financially motivated intrusions to likely North Korean[^6] state-sponsored attackers, including cryptocurrency theft and IT worker wage theft. Mandiant continues to track North Korean threat groups that conduct financially motivated activity to cover both operational costs as well as larger scale activity intended to generate revenue for the state.[^7]

The upward trend in ransomware and other extortion-related investigations in 2023 is consistent with Mandiant and open-source observations of a marked increase in listings on data leak sites (DLS) and extortion revenue estimates.[^8] DLS are websites where the illicitly retrieved data of companies that refuse to pay a ransom are published. While this data is skewed toward targets who refused to pay attackers’ ransom demands, it is still useful for understanding broad trends in extortion operations. The FIN11 MOVEit exploitation campaign and UNC3944[^9] activity described in the Evolution of Phishing section showcase the prevalence of extortion intrusions without ransomware encryption.

![Financial Gain, 2020-2023]
![Count of DLS Listings per Quarter, 2021-2023]

### Data Theft
Mandiant identified data theft in 37% of 2023 intrusions, which is slightly lower than the 40% of intrusions reported in 2022. In 11% of intrusions, attackers directly monetized stolen data through extortion. In an additional 7%, they used a combination of data theft, ransomware, and extortion, also known as multifaceted extortion. Mandiant also observed attackers steal credentials and other data likely to facilitate reconnaissance of target networks. Several cases involved large-scale data theft that included intellectual property. Mandiant also identified instances of targeted or selective data theft by groups such as the Russian cyber espionage group APT29[^10] and the suspected Chinese cyber espionage cluster UNC4841.[^11]

![Data Theft, 2020-2023]
![Data Theft]

### Environment
In 2023, Mandiant experts continued to observe attackers use compromised architecture to conduct email spam, distribute botnets, and perform some types of cryptomining activity. During the past three years, intrusions related to compromised architecture have been heavily automated following the mass exploitation of vulnerabilities. Publicly released proof-of-concept (PoC) code for new exploits increases the ease of automating attacks, accelerating the attack cycle for adversaries abusing compromised infrastructure. Publicly available PoC code for vulnerabilities makes it simple for attackers to automate their exploits using scanning tools.

In 2023, Mandiant noted a decrease in the number of investigations that identified multiple threat groups in a single environment. In 17% of investigations, Mandiant experts uncovered more than one threat group operating in the target environment. This likely is related to the volume of targeted zero-days that Mandiant investigated. The 10 percentage point decrease from 2022 (27%) suggests a positive trend, potentially resulting from defenders’ efforts to limit the ability of additional attackers to infiltrate environments.

Compromised Architecture
in 2022: 6%
in 2023: 6%

Multiple Threat Groups Identified (per environment)
in 2022: 27%
in 2023: 17%

## Threat Groups
Mandiant tracks more than 4,000 threat groups, 719 of which were newly tracked in 2023. Mandiant investigators encountered 316 different threat groups when responding to intrusions in 2023, 220 groups were both newly tracked and observed in Mandiant investigations in 2023. These counts are largely in line with 2022 observations. For example in 2022, 265 groups were both newly tracked and observed in Mandiant investigations. In 2023, organizations faced intrusions by two named advanced persistent threat (APT) groups from Russia and Iran; four named financial threat (FIN) groups; and 310 uncategorized (UNC) groups. While 253 of these UNC groups were newly identified, Mandiant has tracked the remaining 57 UNC groups for periods ranging from one to 10 years. This distribution of threat groups suggests that organizations contend with both established and new threats on a regular basis.

![Threat Groups]

Mandiant tracks Advanced Persistent Threat (APT) groups 0-43. Over the years, APT11 and APT13 were merged into other groups and subsequently deprecated resulting in 42 APT groups actively tracked by Mandiant.

More than half of the attackers observed in 2023 (52%) were primarily motivated by financial gain, and 10% principally pursued espionage activities. A very small percentage, just 2%, included threat clusters Mandiant judged to be operating for hacktivist motivations, attackers focused on disruption or destruction, and pentesters. For the remaining 36% of threat clusters, there was not sufficient evidence to determine a specific motivation with a high degree of confidence. Compared to 2022, Mandiant observed modest declines in the proportion of attackers pursuing objectives of espionage, disruption and destruction, hacktivism, and influence operations. Financially motivated groups made up a larger share of observed attackers in 2023, 52%, compared to 48% in 2022, a shift at least partially explained by the growth in ransomware- and extortion-related activity in 2023.

### Graduation
In 2023, Mandiant graduated one new named threat group, APT43, and merged 189 activity clusters into other threat groups based on extensive research into activity overlaps. For details on how Mandiant defines and references UNC groups and merges, please see, “How Mandiant Tracks Uncategorized Threat Actors.”[^12]

APT43 is a prolific cyber operator that supports the interests of the North Korean Government. The group combines moderately sophisticated technical capabilities with aggressive social engineering tactics, especially against South Korean and U.S. government organizations, academics, and think tanks focused on geopolitical issues surrounding the Korean Peninsula. In addition to its espionage campaigns, we believe APT43 funds itself through cyber crime operations to support its primary mission of collecting strategic intelligence. The group creates numerous spoofed and fraudulent personas for use in social engineering as well as cover identities for purchasing operational tooling and infrastructure. APT43 has collaborated with other North Korean espionage operators on multiple operations, underscoring the major role APT43 plays in North Korea’s cyber apparatus. For more details, see the full APT43 report.[^13]

UNC Group When Mandiant encounters new threat activity that cannot confidently be linked to an existing group, an UNC group designation is created to tie together observable artifacts associated with the activity cluster. As new information and artifacts are discovered that can be tied back to the same activity cluster, Mandiant analysts build on the initial understanding of the attacker, potentially merging it with other tracked threat clusters and ultimately graduating the UNC to an APT or FIN group.

![Observed Threat Groups by Goal, 2023]

## Malware
In 2023, Mandiant began tracking 626 new malware families, 128 of which were seen in incident response investigations. This is the highest number of net new malware families Mandiant has identified in a single year to date. However, this figure is not drastically higher than the 588 malware families that were newly tracked in 2022, which suggests that adversaries could be increasing their toolsets at a similar rate.

While Mandiant observed an increase in the number of newly tracked malware families in 2023, the total number of observed families declined from 321 to 277. This decrease may reflect the increased use of previously established tools and/or the rising number of compromises that use no malware at all. Of all 277 malware families observed in intrusions, 128 were newly tracked in 2023.

![Malware]

### New Malware Families by Category
The top five malware categories have remained relatively consistent year over year. Of the 626 newly tracked malware families, the top five categories include backdoors (33%), downloaders (16%), droppers (15%), credential stealers (7%), and ransomware (5%). Newly tracked credential stealers return to the top five categories in 2023 after a brief hiatus observed in 2022. Another notable change in rankings is the decrease in newly tracked ransomware families, from 7% of malware families to 5% of newly tracked families in 2023. Although Mandiant responded to a similar proportion of ransomware intrusions in 2023 as in 2021, the decline in net new ransomware families may reflect the prevalence of ransomware strains that existed prior to 2023, such as LOCKBIT, ALPHV, BASTA, and ROYALLOCKER.

![Newly Tracked Malware Families by Category, 2023]

A malware category describes a malware family’s primary purpose. Each malware family is assigned only one category that best describes its primary purpose, regardless of functionality for more than one category.

### Observed Malware Families by Category
Observed malware family categories were also relatively consistent with the findings from previous years. Mandiant experts observed 277 malware families during investigations conducted in 2023. Backdoors remain the favorite among attackers, making up 34% of the observed malware dataset. This is up one percentage point from 2022. The remaining observed malware family categories show ransomware (11%), droppers (9%), downloaders (9%), and tunnelers (6%) rounding out the top five.

Mandiant continues to see a rise in attacker use of remote administration tools and other utilities to conduct their operations, noted in the continued increase in the “Other” category year over year. Of the 20% of malware families in this category, 8% represent legitimate utilities or remote administration tools. While not inherently malicious, attackers often leverage these tools in intrusions to evade detection, demonstrating their continued resourcefulness. To remain undetected and carry out further operations, attackers use living-off-the-land (LotL) techniques by employing system tools that are already in the environment or they abuse remote administrator tools that are less likely to be flagged by default in security technologies like Endpoint Detection and Response tooling.

![Observed Malware Families by Category, 2023]

An observed malware family is a malware family identified during an investigation by Mandiant experts.

### Malware Category Definitions
| Malware Category | Primary Purpose |
| --- | --- |
| Backdoor | A program whose primary purpose is to allow an attacker to issue interactive commands to the system on which it is installed. |
| Credential Stealer | A utility whose primary purpose is to access, copy, or steal authentication credentials. |
| Datamine | A utility whose primary purpose is to gather data, typically for theft. Excludes utilities that gather data such as credentials used for the purpose of escalating privileges or information used for system or network reconnaissance. |
| Downloader | A program whose sole purpose is to download (and perhaps launch) a file from a specified address and which does not provide any additional functionality or support any other interactive commands. |
| Dropper | A program whose primary purpose is to extract, install, and potentially launch or execute one or more files. |
| Launcher | A program whose primary purpose is to launch one or more files. Differs from a dropper or an installer in that it does not contain or configure the file, but merely executes or loads it. |
| Ransomware | A program whose primary purpose is to perform some malicious action (such as encrypting data) with the goal of extracting payment from the target in order to avoid or undo the malicious action. |
| Tunneler | A program that proxies or tunnels network traffic. |
| Other | Includes other categories, such as utilities, remote admin technologies, keyloggers, and point of sale. |

Observed Malware Families 2022 to 2023
| Category | 2022 | 2023 |
| --- | --- | --- |
| Backdoor | 33% | 34% |
| Ransomware | 10% | 11% |
| Dropper | 9% | 9% |
| Downloader | 10% | 8% |
| Tunneler | 5% | 6% |
| Launcher | 5% | 4% |
| Other | 28% | 20% |

### Malware by Availability
Malware family availability for both newly tracked and observed malware families remains more heavily weighted toward non-public in 2023, similar to previous M-Trends reporting. In both categories, malware families are more often privately developed or have restricted availability. Adversaries traditionally use a variety of non-public malware to conduct their operations. However, the share of publicly available malware families observed in investigations has increased by one percentage point from 2021 to 2022 and again from 2022 to 2023 to arrive at 30%. The increased use of publicly available malware likely reflects the rise in financially motivated attackers who prioritize speed and efficiency over long-term stealth.

A publicly available tool or malware family is readily obtainable without restriction. This includes tools that are freely available on the internet as well as tools that are sold or purchased, as long as they can be purchased by any buyer.

A non-public tool or malware family is, to the best of our knowledge, not publicly available (either for free or for sale). They may include tools that are privately developed, held or used, as well as tools that are shared among or sold to a restricted set of customers.

![Newly Tracked Malware Families by Availability, 2023]
![Observed Malware Families by Availability, 2023]

### Most Frequently Seen Malware
BEACON remains the most frequently observed malware family in Mandiant investigations globally and was identified in 10% of all intrusions. While BEACON remains the favorite among attackers, during the past three years Mandiant has seen a decrease in BEACON usage. In 2021, 28% of intrusions had at least one BEACON backdoor used. At the time, ransomware groups were actively compromising organizations across the globe and frequently used BEACON to conduct operations. In 2022, there was a global decrease in ransomware-related intrusions, and once again the usage of BEACON reflected that decrease. However, in 2023, Mandiant defenders noted BEACON usage at an all time low, despite an increase in ransomware intrusions.

This decrease could align with attackers moving to evade endpoint security technology with memory resident malware, utilizing third-party remote administration tools, and employing more LotL techniques, or the abuse of native tools and processes on a system. Another possibility could be that attackers are migrating away from the command and control (C2) framework Cobalt Strike and the use of BEACON as their primary backdoor. As robust security community driven detections have created increased mitigations for the Cobalt Strike framework, attackers will increasingly turn to other C2 avenues such as SLIVER, Brute Ratel, and Mythic, to support operations.

ALPHV and LOCKBIT were the second and fifth most frequently observed malware families, respectively, in 2023. Mandiant encountered ALPHV ransomware in 5% of Mandiant led investigations in 2023 compared to 2% in 2022.

The third and sixth most prevalent malware families Mandiant observed were related to the first and third most exploited vulnerabilities. LEMURLOOT (5%) and SEASPY (2%) are backdoors used by attackers following exploitation of the MOVEit and Barracuda technologies respectively. The remaining frequently observed malware families have been used by multiple attackers, some also in conjunction with ALPHV, LOCKBIT, LEMURLOOT and SEASPY.

![Most Frequently Seen Malware Families, 2023]
![BEACON Usage, 2020-2023]

### Malware Definitions
| Malware | Description |
| --- | --- |
| BEACON | A backdoor written in C/C++ that is part of the Cobalt Strike framework. Supported backdoor commands include shell command execution, file transfer, file execution, and file management. BEACON can also capture keystrokes and screenshots as well as act as a proxy server. BEACON may also be tasked with harvesting system credentials, port scanning, and enumerating systems on a network. BEACON communicates with a C2 server via HTTP or DNS. Mandiant has seen BEACON used by a wide range of named threat groups including APT19, APT32, APT40, APT41, FIN6, FIN7, FIN9, FIN11, FIN12 and FIN13, as well as more than 800 UNC groups. |
| ALPHV | Ransomware written in Rust. The ransomware may contain a plaintext JSON configuration that specifies the ransomware functionality. ALPHV may be able to escalate its privileges and bypass UAC, likely contains AES and ChaCha20 (or Salsa) encryption functionality, may use the Restart Manager as part of its operations, deletes volume shadow copies, may enumerate disk volumes and network shares, and may kill processes and services. Mandiant has seen more than 20 UNC groups with financial gain goals use ALPHV. |
| LEMURLOOT | LEMURLOOT is a web shell written in C# tailored to interact with the MOVEit Transfer platform. The malware authenticates incoming connections via a hard-coded password and can run commands that will download files from the MOVEit Transfer system, extract its Azure system settings, retrieve detailed record information, create and insert a particular user, or delete this same user. Data returned to the system interacting with LEMURLOOT is Gzip compressed. Based on Mandiant observations, FIN11 is the primary user of LEMURLOOT. |
| SYSTEMBC | A tunneler written in C that retrieves proxy-related commands from a C2 server using a custom binary protocol over TCP. A C2 server directs SYSTEMBC to act as a proxy between the C2 server and a remote system. SYSTEMBC is also capable of retrieving additional payloads via HTTP. Some variants may use the Tor network for this purpose. Downloaded payloads may be written to disk or mapped directly into memory prior to execution. SYSTEMBC is often used to hide network traffic associated with other malware families. Observed families include DANABOT, SMOKELOADER, and URSNIF. Mandiant has seen FIN12 and more than 40 UNC groups with financial gain goals use SYSTEMBC. |
| LOCKBIT | A ransomware written in C that encrypts files stored locally and on network shares. LOCKBIT can also identify additional systems on a network and propagate via SMB. Prior to encrypting files, LOCKBIT clears event logs, deletes volume shadow copies, and terminates processes and services that may impact its ability to encrypt files. LOCKBIT has been observed using the file extension “.lockbit” for encrypted files. Mandiant has seen more than 30 UNC groups with financial gain goals use LOCKBIT. |
| SEASPY | SEASPY is a backdoor that establishes a PCAP filter on port 25 (SMTP) and is activated when a “magic packet” is received. SEASPY masquerades as a legitimate Barracuda Network Service and changes its process in memory for further evasion. Mandiant has only seen UNC4841 use SEASPY. |
| METASPLOIT | A penetration testing framework whose features include vulnerability testing, network enumeration, payload generation and execution, and defense evasion. The framework contains exploits for numerous applications and popular operating systems such as Windows, Linux, and macOS. METASPLOIT is commonly used to generate a stager payload, which is responsible for downloading and executing the framework’s METERPRETER backdoor. Mandiant has seen APT32, APT41, APT43, FIN6, FIN7, FIN11, FIN13, and more than 160 UNC groups use Metasploit. |
| REGEORG | An open-source utility used to tunnel webshell traffic. Mandiant has seen APT28, APT29, APT41 and 30 UNC groups use REGEORG. |

### Notable Law Enforcement Actions
In a December 2023 press release, the United States Federal Bureau of Investigation (FBI) reported[^14] that ALPHV, also known as BlackCat, had targeted more than 1,000 organizations. The FBI’s press release also outlined the disruption campaign and the development of a decryption tool that allowed the FBI to offer help to a number of impacted organizations. Mandiant tracks the ALPHV ransomware operator as UNC3507, and several other clusters of activity as affiliates, most notably UNC3944, UNC4696, and UNC4896.

The fifth most