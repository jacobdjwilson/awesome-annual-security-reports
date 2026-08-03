Organization: Mandiant
Report Title: M-Trends
Year: 2025

SPECIAL REPORT: MANDIANT M-TRENDS 2023 1
Google Cloud Security
O
M-Trends
2025 Report
G
R
A
B
M
E

Mandiant M-Trends 2025 Report 2

## Table of Contents
- [Introduction](#introduction)
- [By the Numbers](#by-the-numbers)
- [Campaigns and Global Events](#campaigns-and-global-events)
- [Targeted Attacks](#targeted-attacks)
- [Ransomware](#ransomware)
- [Cloud Compromises](#cloud-compromises)
- [Threat Techniques](#threat-techniques)
- [Regional Reports](#regional-reports)
- [Americas](#americas)
- [EMEA](#emea)
- [JAPAC](#japac)
- [Articles](#articles)
- [Infostealer Malware Continues to Create a Threat to Enterprise Systems](#infostealer-malware-continues-to-create-a-threat-to-enterprise-systems)
- [Democratic People’s Republic of Korea Insider Threats](#democratic-peoples-republic-of-korea-insider-threats)
- [The 2024 Iranian Threat Landscape](#the-2024-iranian-threat-landscape)
- [Evolution of Data Theft in Cloud and Software-as-a-Service Environments](#evolution-of-data-theft-in-cloud-and-software-as-a-service-environments)
- [Common Themes in Cloud Compromise Investigations](#common-themes-in-cloud-compromise-investigations)
- [Security Recommendations for Diverse Cloud and Hybrid Environments](#security-recommendations-for-diverse-cloud-and-hybrid-environments)
- [Threats to Web3 and Cryptocurrency](#threats-to-web3-and-cryptocurrency)
- [Unsecured Data Repositories](#unsecured-data-repositories)
- [Conclusion](#conclusion)
- [MITRE ATT&CK](#mitre-attck)
- [Bibliography](#bibliography)

SPECIAL REPORT: MANDIANT M-TRENDS 2023 3

## Introduction O
G
R
A
B
M
E

Mandiant M-Trends 2025 Report 4

A key takeaway from M-Trends 2025 is that malware, unsecured data repositories, and attackers are seizing every opportunity to further their objectives. One way they are doing this is through the use of infostealer malware, which is increasingly being used to enable intrusions using stolen credentials. Another growing trend is the targeting of unsecured data repositories, which is brought on by the lack of basic security hygiene. Additionally, attackers are exploiting the gaps and risks introduced as organizations continue their migrations to the cloud.

The most common way attackers breached organizations in 2024 was through exploits, which we observed as the initial infection vector in 33% of our investigations. The financial sector continues to be the most targeted industry, making up a little more than 17% of our investigations. Global median dwell time has risen to 11 days from 10 days in 2023. This marks the first increase since the publication of the inaugural M-Trends in 2010 but is still below the 16 days reported in 2022. In M-Trends 2025, we take a look at how adversary notifications—notably in ransomware incidents—influence the global median dwell time metric.

By providing data and other security metrics in M-Trends, along with deeper dives on attacker trends, we illustrate how threat actors are conducting their operations, how they are achieving their goals, and what organizations need to be doing to prevent, detect, and respond to threats. Infostealer cloud migrations are just a few challenges organizations will face. We additionally cover:

- Insider risk brought on by Democratic People’s Republic of Korea (DPRK) IT workers
- Growth of blockchain technology leading to cryptocurrency and Web3 threats
- Iran-nexus threat actor operations amid Middle East tensions

Mandiant consultants are regularly on the frontlines of cyber incidents, where they conduct in-depth investigations and analysis of the most recent attacks. This firsthand experience results in a deep understanding of threats and the effective strategies required to defend against them.

Mandiant uses this knowledge to proactively assess client security postures, comparing them against the latest attacker tactics, techniques, and procedures. Furthermore, we provide critical support for remediation efforts, security transformation initiatives, and comprehensive security education.

Through the release of our annual M-Trends report, we share our learnings with the greater security community, building on our dedication to providing critical knowledge to those tasked with defending organizations.

The information in this report has been sanitized to protect the identities of victims and their data.

SPECIAL REPORT: MANDIANT M-TRENDS 2023 5

## By the Numbers O
M-Trends
G
R
A
B
M
E

Mandiant M-Trends 2025 Report 6

Since 2010, Mandiant has provided statistics and analysis of threats observed in the previous year’s incident response investigations. In M-Trends 2025, Mandiant examines data collected from more than 450k+ hours of incident response engagements globally, highlighting trends and significant insights. This information can be useful to inform risk assessments and to support planning for threat hunts, which can improve an organization’s abilities to counter future threats effectively.

The metrics reported in M-Trends 2025 are based on Mandiant Consulting investigations conducted between Jan. 1 and Dec. 31, 2024, that found targeted attack activity.

Mandiant M-Trends 2025 Report 7

## Campaigns & Global Events

Campaigns are a set of impactful intrusions conducted by an attacker or multiple attackers in cooperation toward a single objective at multiple targets within a relevant time frame.[^1]

Global Events are a set of impactful intrusions conducted by multiple unrelated adversaries in parallel campaigns involving a similar theme, target, or resource.

When Mandiant experts identify threat activity that is actively impacting multiple organizations, a Campaign or a Global Event is created. Campaigns represent focused efforts by one or more threat groups with a single objective. Global Events encompass multiple threat groups pursuing different objectives but using similar tactics, such as exploiting a newly disclosed vulnerability.

Mandiant delivers dynamic updates throughout the lifespan of each Campaign and Global Event, including details of indicators of compromise (IOCs) and tactics, techniques, and procedures (TTPs) unique to the event. Where possible, Mandiant provides examples, context, and information about threat actor behaviors, tools, and malware as well as actionable defensive and preventative measures. This intelligence is based on real-world data collected from Mandiant investigations and research, enabling our clients to respond effectively and decisively to active threats at first discovery and as they evolve.

In 2024, Mandiant initiated 83 campaigns and five global events and continued to track activity identified in previous years. These campaigns affected every industry vertical and 73 countries across six continents. Figure 1 depicts 33 campaigns and three global events, a subset of all campaigns and global events with direct relation to Mandiant incident response engagements.

For example, Campaign 23.042 began in April 2023 when the financially motivated group UNC3944 obtained network access to various organizations via SMS phishing and social engineering. With this access, UNC3944 ultimately stole proprietary data and deployed the ALPHV ransomware.

Other examples include Russian cyber espionage groups like APT28 and APT44. Campaign 23.056 tracked a subcluster of Russian cyber espionage group APT28 that, starting in late August, conducted credential harvesting and exploited Microsoft Outlook vulnerability CVE-2023-23397. Campaign 24.004 tracks APT44 activity leveraging trojanized software installers distributed via torrents on Ukrainian- and Russian-language forums as a means of achieving opportunistic initial access to potential targets of interest. In observed cases, victims of interest to APT44 received publicly available malware, such as DARKCRYSTALRAT, for follow-on exploitation.

To facilitate tracking and analysis of large-scale events, such as widespread exploitation of a vulnerability, Mandiant utilizes global events as a framework to encapsulate multiple distinct campaigns. For instance, Global Event 24.004 groups three campaigns (CAMP.24.026, CAMP.24.030, CAMP.24.031) associated with different threat actors exploiting CVE-2024-3400. Each campaign tracks unique tactics, techniques, and procedures (TTPs), such as SNOWLIGHT downloader deployment, reconnaissance targeting configuration files, and BEACON backdoor usage. Global Event 24.002 tracks zero-day exploitation of CVE-2023-46805 and CVE-2024-21887, encompassing UNC5221 deploying custom malware and web shells, and another actor deploying SLIVER and TERRIBLETEA backdoors.

| Mandiant M-Trends 2025 Report | 8 |
| --- | --- |

### 2024 Campaigns and Global Events Related to Mandiant Incident Response Investigations

![Figure 1: Campaigns and global events related to 2024 Mandiant incident response investigations]

Mandiant M-Trends 2025 Report 9

## Targeted Attacks

### Targeted Industries

An industry category describes an organization’s primary industry. Organizations are typically assigned to only one category that best describes its primary industry, though many organizations have links to multiple industries. For example, a cryptocurrency exchange relates both to the financial and technology sectors, but for the purposes of this section, it would be categorized as a financial sector organization.

Mandiant responded to incidents affecting the financial sector more than any other sector in 2024. Business and professional services, high tech, government, and healthcare made up the next most frequently observed sectors. These top industries are consistent with prior years, with slight variations. For example, in 2023, investigations associated with retail and consumer goods and services organizations slightly outpaced those associated with healthcare and government entities, while the opposite was true in 2024.

#### Targeted Industries, 2024

| Industry | Percent of Investigations |
| --- | --- |
| Financial | 17.4% |
| Business and Professional Services | 11.1% |
| High Tech | 10.6% |
| Government | 9.5% |
| Healthcare | 9.3% |
| Retail, Consumer Goods and Services | 7.9% |
| Telecommunications | 5.7% |
| Transportation and Logistics | 4.5% |
| Entertainment and Media | 4.5% |
| Energy | 4.3% |
| Education | 3.8% |
| Other | 3.4% |
| Construction and Engineering | 2.9% |
| Utilities | 1.8% |
| Aerospace and Defense | 1.6% |
| Nonprofits | 1.4% |
| Agricultural and Forestry | 0.2% |

Mandiant M-Trends 2025 Report 10

### Initial Infection Vector

For the fifth year in a row, exploits were the most frequently observed initial infection vector in Mandiant incident response investigations. For intrusions in which an initial infection vector was identified, 33% began with exploitation of a vulnerability. This is a decline from 2023, during which exploits represented the initial intrusion vector for 38% of intrusions, but nearly identical to the share of exploits in 2022, 32%.

Stolen credentials overtook email phishing as the second most frequently observed initial infection vector in 2024, representing 16% of intrusions, compared to 14% for email phishing. In 2023, email phishing was determined to be the initial infection vector in 17% of intrusions and stolen credentials in just 10%. While email phishing remains a common and effective method for obtaining initial access, adversaries can obtain credentials in a variety of ways, including purchasing leaked or stolen credentials on underground forums, mining large data leaks for credentials, and actively pursuing credentials by infecting users with keyloggers and infostealers. The continued prevalence of phishing and credential theft underscores the importance of implementing multifactor authentication (MFA), preferably FIDO2-compliant MFA methods.

The percentage of intrusions that began with web compromise increased from 5% in 2023 to 9% in 2024. Web compromise encompasses drive-by compromise, the use of malicious advertisements, search engine optimization (SEO) poisoning, and compromised websites. To help mitigate risk from web compromise, organizations should consider a multilayered approach encompassing endpoint script blocking, content filtering for malicious redirects and software, policies against browser credential storage, and consistent patching of all systems.

Mandiant M-Trends 2025 Report 11

In 2024, prior compromise remained a relatively common initial infection vector, occurring in 8% of investigations. The continued prevalence of this vector likely reflects the enduring effectiveness of threat actors specializing in establishing initial access, then providing that access to other threat actors.

Insider threat, typically a negligible proportion of Mandiant’s incident response investigations, emerged as a surprisingly consequential initial infection vector in 2024. Specifically, a surge in North Korean IT workers seeking employment under false pretenses led to insider threat representing 5% of identified initial infection vectors. Mandiant primarily tracks this activity as UNC5267.

Mandiant also observed threat actors gain access to targeted systems through brute-force attacks, third-party compromise, social engineering voice calls (voice phishing or vishing), SIM swapping, supply chain compromise, and Bring Your Own Device (BYOD)—typically infected USBs.

Mandiant was unable to determine an initial infection vector for 34% of 2024 intrusions. Although numerous factors can contribute to an unknown vector, this considerable proportion indicates potential deficiencies in enterprise logging and detection capabilities.

### Most Frequently Exploited Vulnerabilities

Among the Mandiant incident response investigations performed in 2024, the most frequently exploited vulnerabilities affected security devices, which are, due to their function, typically placed at the edge of the network. Three of the four vulnerabilities were first exploited as zero-days. While a broad selection of threat actors have recently targeted edge devices, Mandiant also specifically noted an increase in targeting from Russian and Chinese cyber espionage actors.[^3] [^4] [^5]

- **CVE-2024-3400**: PAN-OS GlobalProtect (Palo Alto Networks)
- **CVE-2023-46805 & CVE-2024-21887**: Connect Policy Secure Secure VPN (Ivanti)
- **CVE-2023-48788**: FortiClient EMS (Fortinet)

#### CVE-2024-3400
CVE-2024-3400 is a vulnerability in the GlobalProtect feature of Palo Alto Networks PAN-OS software that, when exploited, allows command injection through arbitrary file creation. Mandiant observed one threat group exploit this vulnerability as a zero-day. Within two weeks of its disclosure on April 12, 2024, and the publishing of proof-of-concept (PoC) code on April 13, 2024, Mandiant observed more than a dozen separately tracked groups exploiting this vulnerability, including a RANSOMHUB affiliate that used initial access established using this vulnerability to conduct multifaceted extortion.

Mandiant M-Trends 2025 Report 12

#### CVE-2023-46805 and CVE-2024-21887
On Jan. 10, 2024, Ivanti disclosed two vulnerabilities, CVE-2023-46805 and CVE-2024-21887, impacting Ivanti Connect Secure VPN (“CS,” formerly Pulse Secure) and Ivanti Policy Secure appliances.[^6] Successful exploitation of these vulnerabilities allows authentication bypass and command injection, respectively. When chained together, these allowed for unauthenticated arbitrary command execution on systems.[^7] Mandiant identified UNC5221, a suspected Chinese cyber espionage threat cluster, exploiting these vulnerabilities in the wild as zero-days as early as December 2023. UNC5221 leveraged multiple custom malware families, in several cases trojanizing legitimate CS files with malicious code. The malware functionality and observed activity suggest that UNC5221 was primarily focused on establishing persistent access, avoiding detection, and performing internal reconnaissance.

Ivanti worked closely with Mandiant, affected clients, government partners, and Volexity to address these vulnerabilities. They released a blog post with mitigations, patches, an enhanced external integrity checker tool, and a disclosure for a subsequently discovered vulnerability, CVE-2024-21893.[^8] CVE-2024-21983 is a server-side request forgery vulnerability that allows a remote attacker to obtain unauthorized access. Mandiant also released a remediation and hardening guide.[^9]

In mid-January 2024, Mandiant identified UNC5135 scanning Ivanti Connect Secure appliances but did not directly observe UNC5135 successfully exploit these vulnerabilities. Mandiant assesses with moderate confidence that UNC5135 is linked to UNC3236, which we suspect to align with the publicly reported Volt Typhoon.[^10]

By April 2024, Mandiant observed eight distinct clusters involved in the exploitation of one or more of the three vulnerabilities: CVE-2023-46805, CVE-2024-21887, and CVE-2024-21893. Of these eight clusters, Mandiant tracked five suspected Chinese cyber espionage threat clusters that exhibited distinct post-compromise behavior and used different malware after exploiting the vulnerabilities for initial access.

#### CVE-2023-48788
CVE-2023-48788 is a SQL injection vulnerability in the FortiClient Endpoint Management Server. Mandiant observed a financially motivated threat cluster exploit this vulnerability to execute arbitrary SQL commands within two weeks of its March 12, 2024, disclosure. In observed operations, the threat cluster deployed the SimpleHelp remote administration tool, likely to establish persistent access before offering that access for sale to other threat actors.

In October and November 2024, a suspected FIN8 threat cluster gained access to a targeted organization by exploiting CVE-2023-48788, deployed SNAKEBITE ransomware, and used the publicly available backup utility RESTIC for data theft.

Mandiant M-Trends 2025 Report 13

### Global Detection by Source

Internal detection is when an organization independently discovers it has been compromised, such as through an internal security appliance alert or internal personnel notification of suspicious activity.

External notification is when an outside entity informs an organization it has been compromised, such as law enforcement agencies, cybersecurity companies, or industry partners (External Entity). In some cases, attackers will perform this notification, such as through a ransom note (Adversary).

The majority of organizations, 57%, first learned of a 2024 compromise from an external source. External notifications can be further divided into adversary notifications and external entity notifications. Adversary notifications typically take the form of ransom notes and represented 14% of total detection sources in 2024. Notifications from external entities, such as law enforcement or cybersecurity companies, comprised 43% of total detection sources. Organizations discovered an intrusion through internal mechanisms in 43% of 2024 investigations. These figures are roughly similar to our findings in 2023 investigations, which saw 54% external notifications and 46% internal notifications overall.

Mandiant M-Trends 2025 Report 14

### Global Median Dwell Time

Dwell time is calculated as the number of days an attacker is present in an environment that has been compromised before they are detected. The median represents a value at the midpoint of a data set sorted by magnitude.

The 2024 global median dwell time remained largely in line with 2023 figures. While the overall value increased by one day from 2023 to 2024, the year-over-year trend continues to indicate that dwell times have declined significantly over the long term. For example, overall dwell time in 2014 was 205 days, compared to just 11 days in 2024. Dwell time for internally discovered intrusions remained less than that of all externally notified intrusions in 2024.

#### Median Dwell Time by Detection Source, 2024
- **All**: 11 days
- **Adversary**: 5 days
- **External Entity**: 26 days
- **Internal**: 10 days

The median adversary notification time was just five days, while external partners notified in a median of 26 days. This discrepancy is not surprising given that the vast majority of adversary notifications originate from extortion actors who benefit from monetizing intrusions quickly.

Mandiant M-Trends 2025 Report 15

### Global Dwell Time Distribution

Dwell time distribution plots intrusions that Mandiant investigated across ranges of dwell time. The distribution heat map demonstrates that the prevailing trend across Mandiant investigations from 2018 to 2024 is toward shorter and shorter dwell times. Comparing 2023 to 2024, the percentage of investigations that were discovered in one week or less increased from 43.3% to 45.1%.

Mandiant M-Trends 2025 Report 16

### Post-Compromise Activity

#### Financial Gain
In 2024, financially motivated intrusions, where a monetization technique was directly observed, represented 35% of all Mandiant incident response investigations. Ransomware-related intrusions represented 21% of all 2024 intrusions and approximately two-thirds of financially motivated intrusions. These proportions are also comparable to 2023, when ransomware was involved in 23% of all cases and about two-thirds of financially motivated intrusions.

In addition to ransomware-related events, Mandiant also responded to a variety of other financially motivated intrusions in 2024, including data theft extortion without ransomware encryption, illicit cryptomining, North Korean IT worker employment fraud, business email compromise, cryptocurrency theft, and cases in which threat actors attempted to monetize intrusions by offering access to targeted organizations or stolen data for sale.

Mandiant M-Trends 2025 Report 17

#### Data Theft
In 37% of 2024 investigations, Mandiant identified evidence of data theft, which is consistent with 2023. Data theft extortion events in which no ransomware was deployed represented 11% of all cases, and multifaceted extortion, which includes both data theft and ransomware encryption, represents 6% of all cases.

Mandiant also observed attackers focus on theft of credentials and information useful for performing further reconnaissance of compromised networks. In addition, Mandiant identified attackers, such as the Russian cyber espionage actor APT28 and Chinese cyber espionage groups including APT41, conducting more targeted data theft. APT28 conducted selective data theft, demonstrating interest in personnel-related data, as well as email content and documents relevant to geopolitical topics consistent with Russian interests. In a campaign targeting multiple organizations in Europe, the Middle East, and Africa (EMEA) and Japan and Asia Pacific (JAPAC), APT41 leveraged SQLULDR2 to export data from Oracle Databases and used PINEGROVE to systematically and efficiently exfiltrate large volumes of sensitive data from the compromised networks, transferring to OneDrive to enable exfiltration and subsequent analysis.

#### Insider Threats
Mandiant responded to a number of incidents involving a unique variety of insider threat, North Korean IT workers. Mandiant primarily tracks this activity as UNC5267. North Korean IT workers use stolen and fabricated identities to apply for high-paying jobs in order to generate revenue for the North Korean regime in violation of international sanctions. Mandiant identified IT workers at diverse organizations, including in the financial services, telecommunications, media and entertainment, retail, and technology industries. In incident response engagements to date, North Korean IT workers have primarily functioned within the scope of their job responsibilities. However, the remote workers often gain elevated access to modify code and administer network systems. This heightened level of access granted to fraudulent employees presents a significant security risk. Moreover, in several cases in the latter half of 2024, Mandiant observed evidence of North Korean IT workers stealing proprietary data from targeted organizations and, following discovery and termination, threatening to release it publicly if the organization did not pay a ransom.

Mandiant released detailed guidance for detecting North Korean IT worker job applicants in *Staying a Step Ahead: Mitigating the DPRK IT Worker Threat*[^11].

Mandiant M-Trends 2025 Report 18

### Malware

A malware family is a program or set of associated programs with sufficient “code overlap” among the variants that Mandiant considers them to be largely the same thing, a “family.” The term family broadens the scope of a single piece of malware as it can be altered over time, which in turn creates new, but fundamentally overlapping pieces of malware.

An observed malware family is a malware family identified during an investigation by Mandiant experts.

The operating system effectiveness of a malware is the operating system(s) that the malware can target.

In 2024, Mandiant began tracking 632 net new malware families. In investigations, Mandiant observed 205 malware families, 83 of which were both newly tracked and observed in at least one incident response investigation. This number of newly tracked families is on par with the 626 families Mandiant began tracking in 2023, bringing the total number of tracked malware families to more than 5,500 unique families. The 83 newly tracked families that Mandiant observed in incident response investigations in 2024 is lower than the 128 families observed in the same category in 2023. This continues a trend observed during the past three years of fewer new malware families being identified in investigations. This decrease showcases threat actors’ continued willingness to leverage tools already present within the targeted environment as well as their ability to use and misuse tools rather than constructing new malware or configuring known post-exploitation tools. A growing number of compromises use no malware at all.

Looking further into the corpus of malware tracked by Mandiant, malware effective on Windows remains most prevalent. In both newly tracked (76%) and observed malware (62%) in 2024, Mandiant experts observed that malware was more likely to be effective exclusively on the Windows operating system. However, Mandiant has seen a decrease in the proportion of malware designed for Windows systems over the years.

Malware effective exclusively on Linux operating systems continues to increase slowly, accounting for 12% of newly tracked malware families and 22% of observed malware in 2024, compared to 11% of newly tracked and 17% of observed in 2023. The comparative reduction in Windows malware does not signify decreased risk associated with Windows systems but may indicate the risk to Linux environments is slowly increasing.

Mandiant M-Trends 2025 Report 19

### Malware Families by Category

A malware category describes a malware family’s primary purpose. Each malware family is assigned only one category that best describes its primary purpose, regardless of functionality for more than one category.

Of the 632 malware families that Mandiant began to track in 2024, backdoors remained the predominant category, representing 31% of malware families. The next most observed categories were downloaders (19%), droppers (12%), credential stealers (6%), and ransomware (5%). The “Other” category is made up of utilities, tunnelers, data miners, rootkits, keyloggers, and point-of-sale malware, each of which make up less than 5% of the malware population. These findings continue to remain consistent year over year with little movement in position.

Similarly, observed malware family categories remained relatively consistent with the findings from previous years. Of the 205 unique malware families observed in investigations conducted during the 2024 calendar year, backdoors remained most used by attackers, with 35% of observed malware families with that primary purpose. The remaining malware family categories are made up of ransomware (14%), droppers (8%), downloaders (7%), tunnelers (6%), and credential stealers (5%).

In both the newly tracked and observed malware families by category, Mandiant continues to see a large portion of the percentage of malware residing in the “Other” category. This likely reflects the diversity of both attackers and objectives that Mandiant encounters in investigations.

Mandiant M-Trends 2025 Report 20

### Malware Category

- **Backdoor**: A program whose primary purpose is to allow a threat actor to interactively issue commands to the system on which it is installed
- **Credential Stealer**: A utility whose primary purpose is to access, copy, or steal authentication credentials
- **Data Miner**: A utility whose primary purpose is to gather (“mine”) data, typically for theft by threat actors. Excludes utilities that gather data such as credentials used for the purpose of escalating privileges or information used for system or network reconnaissance.
- **Downloader**: A program whose sole purpose is to download (and perhaps launch) a file from a specified address, and which does not provide any additional functionality or support any other interactive commands
- **Dropper**: A program whose primary purpose is to extract, install, and potentially launch or execute one or more files
- **Launcher**: A program whose primary purpose is to execute an external payload or shell command. A launcher does not contain or configure a payload it executes. Examples include a program that starts an executable file located on disk and a program that reads a payload from disk and executes it in memory
- **Ransomware**: A program whose primary purpose is to perform some malicious action (such as encrypting data), with the goal of extracting payment from the victim in order to avoid or undo the malicious action
- **Tunneler**: A program that proxies or tunnels network traffic
- **Utility**: A program that has a specialized purpose that does not fit into any other defined category (such as keylogger or sniffer)
- **Other**: Includes all other malware categories such as rootkits, keyloggers, and point-of-sale malware

Mandiant M-Trends 2025 Report 21

### Most Frequently Seen Malware Families

For the fifth consecutive year, BEACON was identified as the most frequently observed malware family in Mandiant investigations globally and was identified in 5.4% of all intrusions. BEACON usage has decreased dramatically since 2021, when it was observed in 28% of Mandiant investigations.

Of note, in July of 2024, Europol provided an update on Operation MORPHEUS, a global action against the illicit use of the unlicensed versions of the Cobalt Strike red teaming tool.[^12] This operation, conducted with law enforcement and private sector partners, successfully disrupted infrastructure linked to cyber criminal activities. The initiative, which began in 2021, involved flagging 690 IP addresses, 593 of which were taken down by online service providers.[^13] Fortra, the maintainers of the Cobalt Strike framework, also announced the number of unauthorized copies of Cobalt Strike observed in the wild has decreased by 80% over the past two years as a result of their participation in Operation MORPHEUS. Observed declines in percentages of investigations where Mandiant identified BEACON since 2021 may reflect the success of this effort.

Mandiant M-Trends 2025 Report 22

### Malware Family Details

- **BASTA**: BASTA is a ransomware written in C++ that encrypts local files. The ransomware is capable of deleting volume shadow copies. BASTA generates a random ChaCha20 key to encrypt each file; the key is encrypted and appended to the end of the file. The malware has been observed using .basta as the extension for encrypted files; however, some samples have used a random nine-character alphanumeric extension.
- **BEACON**: BEACON is a backdoor written in C/C++ that is part of the Cobalt Strike framework. Supported backdoor commands include shell command execution, file transfer, file execution, and file management. BEACON can also capture keystrokes and screenshots as well as act as a proxy server. BEACON may also be tasked with harvesting system credentials, port scanning, and enumerating systems on a network. BEACON communicates with a command-and-control (C2 or C&C) server via HTTP or DNS.
- **GOOTLOADER**: GOOTLOADER is a JavaScript downloader that comes in an obfuscated form. It downloads another JavaScript file that drops and executes the intended payload.
- **LOCKBIT**: LOCKBIT is a ransomware written in C that encrypts files stored locally and on network shares. LOCKBIT can also identify additional systems on a network and propagate via SMB. Prior to encrypting files, LOCKBIT clears event logs, deletes volume shadow copies, and terminates processes and services that may impact its ability to encrypt files. LOCKBIT has been observed using the file extension ".lockbit" for encrypted files.
- **RANSOMHUB**: RANSOMHUB is ransomware written in GoLang capable of encrypting data using ChaCha20, xChaCha20 or AES256 algorithms. The symmetric encryption key is per-file and protected by elliptic curve cryptography, ed25519. RANSOMHUB can be configured to encrypt a targeted directory, local disks, or network shares. RANSOMHUB provides the capability to reboot in safe mode before running or as a safe mode instance and can be configured for standard out logging.
- **REDBIKE**: REDBIKE (also known as Akira) is ransomware written in C++ that encrypts local files. Encrypted files have the extension ".akira" appended to the filename. Files are encrypted using ChaCha20, and a ransom note is written to every folder with encrypted files. REDBIKE has some code overlaps with CONTI ransomware.
- **SYSTEMBC**: SYSTEMBC is a tunneler written in C that retrieves proxy-related commands from a C2 server using a custom binary protocol over TCP. A C2 server directs SYSTEMBC to act as a proxy between the C2 server and a remote system. SYSTEMBC is also capable of retrieving additional payloads via HTTP. Some variants may utilize the Tor network for this purpose. Downloaded payloads may be written to disk or mapped directly into memory prior to execution. SYSTEMBC is often utilized to hide network traffic associated with other malware families. Observed families include DANABOT, SMOKELOADER, and URSNIF.
- **WIREFIRE**: WIREFIRE is a web shell written in Python that exists as trojanized logic to a component of the Pulse Secure appliance. WIREFIRE supports downloading files to the compromised device and executing arbitrary commands.

Mandiant M-Trends 2025 Report 23

### Threat Groups

What is an UNC group? When Mandiant encounters new threat activity that cannot confidently be linked to an existing group, an UNC group designation is created to tie together observable artifacts associated with the activity. As new information and artifacts are discovered that can be tied back to the same activity cluster, Mandiant analysts build on the initial understanding of the attacker, potentially merging it with other tracked threat clusters and ultimately graduating the UNC to an APT or FIN group.

In 2024, Mandiant identified and began tracking 737 new threat clusters, bringing the grand total of threat groups Mandiant tracks to more than 4,500. During 2024 incident response engagements, Mandiant observed 302 different threat groups, 233 of which were newly identified within the year. These figures are on par with 2023, during which Mandiant experts identified 719 new threat clusters and observed 316 groups in incident response investigations, with 220 of those groups also being newly identified.

Organizations faced four advanced persistent threat (APT) groups from China, Russia, and Iran; one named financial threat (FIN) group; and 297 UNC groups from various geolocations in 2024 engagements. Mandiant continues to see groups that have been tracked for more than one year, and in some cases, up to 10 years. However, the majority of newly tracked and observed threat groups are new clusters of activity observed within Mandiant Consulting engagements in 2024. The composition of this set of threat clusters indicates that organizations continue to face a variety of both established and novel threats.

Mandiant M-Trends 2025 Report 24

### Observed Groups by Goal

The majority of attackers active in 2024 were financially motivated (55%). This proportion is slightly larger than the 52% observed in 2023 and 48% observed in 2022. The growing share of financially motivated threat groups in Mandiant incident response investigations is likely due, in part, to the overall growth of impactful extortion intrusions. Espionage-motivated attackers represented 8% of threat groups identified in 2024 intrusions, compared to 10% in 2023. This is at least partially attributable to the number of distinct suspected Chinese cyber espionage activity clusters involved in vulnerability exploitation campaigns. A small percentage, 2%, included threat clusters Mandiant judged to be operating for hacktivist motivations and attackers focused on disruption or destruction. Several of these intrusions were linked to geopolitical motivations, including the conflicts in Ukraine and Gaza. Based on the evidence available at the time, Mandiant was unable to determine a motivation for the final 35% of groups.

### Actor Graduations and Merges

In 2024, Mandiant graduated two new named threat groups, APT44 and APT45, and merged 204 activity clusters into other threat groups based on extensive research into activity overlaps. For details on how Mandiant defines and references UNC groups and merges, please see “How Mandiant Tracks Uncategorized Attackers.”[^14]

#### APT44
Sponsored by Russian military intelligence, APT44 (aka Sandworm, FROZENBARENTS) is a dynamic and operationally mature threat actor that is actively engaged in the full spectrum of espionage, attack, and influence operations.[^15] APT44 has aggressively pursued a multipronged effort to help the Russian military gain a wartime advantage and is responsible for nearly all of the disruptive and destructive operations against Ukraine over the past decade. APT44’s support of the Kremlin’s political objectives has resulted in some of the largest and most consequential cyberattacks in history. These operations include first-of-their-kind disruptions of Ukraine’s energy grid in the winters of 2015 and 2016, the global NotPetya attack timed to coincide with Ukraine’s Constitution Day in 2017, and the disruption of the opening ceremony of the 2018 Pyeongchang Olympics in response to Russia’s doping ban from the games. Due to its history of aggressively using network attack capabilities across political and military contexts, APT44 presents a persistent, high-severity threat to governments and critical infrastructure operators globally where Russian national interests intersect.

---

[^1]: Campaign and Global Event definition reference.
[^2]: DARKCRYSTALRAT reference.
[^3]: Edge device targeting reference 1.
[^4]: Edge device targeting reference 2.
[^5]: Edge device targeting reference 3.
[^6]: Ivanti CVE disclosure reference.
[^7]: Chained vulnerability reference.
[^8]: Ivanti advisory reference.
[^9]: Mandiant hardening guide reference.
[^10]: Volt Typhoon reference.
[^11]: Staying a Step Ahead: Mitigating the DPRK IT Worker Threat.
[^12]: Operation MORPHEUS reference.
[^13]: Europol IP takedown reference.
[^14]: How Mandiant Tracks Uncategorized Attackers.
[^15]: APT44 / Sandworm tracking reference.

---

Observed Threat Groups by Goal, 2024
60
%
55
40
%
35
20
% %
8 2
0
Financial Gain Unknown Espionage Other
APT44

Mandiant M-Trends 2025 Report 25
APT45
APT45
16
Mandiant assesses with high confidence that APT45 is a moderately
sophisticated cyber operator that supports the interests of the
Democratic People’s Republic of Korea (DPRK). Since at least 2009,
APT45 has carried out a range of cyber operations aligned with the
shifting geopolitical interests of the North Korean state. Although the
group’s earliest observed activities consisted of espionage campaigns
against government agencies and defense industries, APT45 has
expanded its remit to financially motivated operations, including
targeting of the financial vertical; we also assess with moderate confidence that APT45 engaged
in the development of ransomware. In 2019, APT45 directly targeted nuclear research facilities
and nuclear power plants, such as the Kudankulam Nuclear Power Plant in India, marking one of
the few publicly known instances of North Korean cyber operations targeting critical infrastructure.

Mandiant M-Trends 2025 Report 26
Ransomware
A ransomware- Ransomware, data theft extortion, and multifaceted extortion are and will continue to be the
related intrusion
most disruptive type of cyber crime globally, both due to the volume of intrusions and the scope
provides access
for or is associated of potential damage for each event. The impact of ransomware and extortion operations extends
with a malicious far beyond the initial victim. Mandiant responded to ransomware-related intrusions affecting
actor that has the
healthcare, local government, energy, high tech, education, financial sector organizations, and
primary goal of
encrypting data others across JAPAC, EMEA, and the Americas. Ransomware-related events accounted for just
with the intention of
over one-fifth (21%) of all Mandiant incident response investigations in 2024.
extracting payment
from the target.
Initial Infection Vector
In contrast to the overall dataset, the most commonly observed initial infection vector for
ransomware-related intrusions, when the vector could be identified, was brute-force attacks.
Password spraying, virtual private network (VPN) devices compromised through default
credentials, and high-volume Remote Desktop Protocol (RDP) login attempts are examples of
the types of brute-force attacks that Mandiant observed in 2024. Use of this tactic reinforces
the importance of auditing and configuring internet-exposed infrastructure to require multifactor
authentication (MFA), to require verification for remote attempts to register MFA on an account
for the first time, and to lock accounts after a certain number of failed login attempts.
Stolen credentials and exploits were tied for the second most common initial infection vector
for 2024 ransomware-related intrusions at 21% each, followed by prior compromise at 15%, and
third-party compromise at 10%.
Initial Infection Vector, 2024
Initial Infection Vector, 2024
RRaannssoommwwaarree--RReelalatteedd
Stolen Prior
Brute Compromise
Credentials
% %
Force
15
21
Third-Party Other
Exploit Compromise
% %
%
%
2621 10 7

Mandiant M-Trends 2025 Report 27
Detection by Source
Detection by external sources was more common for ransomware-related than non-ransomware
related intrusions, with notifications directly from adversaries representing the majority of the
variance. This is consistent with the extortion business model in which attackers intentionally
and abruptly notify organizations of a ransomware intrusion and demand payment. In 2024,
adversaries notified organizations of ransomware-related compromises in 49% of cases, other
external entities in 21% of cases, and organizations discovered compromises internally in 30%
of cases. In investigations without a ransomware component, adversaries represented only 5%
of detection sources, while other external entities notified in 48% of cases, and organizations
identified evidence of malicious behavior for themselves in 47% of cases.
DDeetetectciotino bny b Syo uSrocue,r 2c0e2, 42024
%
5
100% Adversary
% %
14 49 % External Entity
48
% Internal
75% 43
50%
%
21 %
% 47
43
25% %
30
0%
All Ransomware Non-Ransomware
These figures are largely consistent with Mandiant’s 2023 findings. External notifications in
2023 were also more common for ransomware-related intrusions (70%) than non-ransomware
related intrusions (50%). Adversary notifications in 2023 represented approximately three
quarters of external notifications for ransomware-related intrusions, while in 2024, the propor-
tion of adversary notifications declined slightly to seven out of 10 of all external notifications for
ransomware-related events.

Mandiant M-Trends 2025 Report 28
Ransomware-Related Dwell Time
vs Global Dwell Time
Median dwell time for ransomware-related intrusions was 11 days overall, five days for adversary-
notified events, five days for compromises discovered by external entities such as law
enforcement and cybersecurity companies, and 29 days for intrusions discovered internally.
Dwell Time Distribution for Ransomware-
Related Intrusions
The dwell time distribution for ransomware-related intrusions is even more concentrated toward
shorter time intervals between the first evidence of malicious activity and discovery of the
incident. Events with a week or less of dwell time represent 56.5% of the ransomware-related
intrusions that Mandiant investigated in 2024, compared to 45.1% of all intrusions discovered
within one week. This finding is consistent with the extortion business model, in which attackers
are incentivized to complete their objectives without being detected and swiftly and abruptly call
the target organizations’ attention to their activities.
Global Dwell Time Distribution, 2024
Global Dwell Time Distribution 2024
| All | % 17.6% | 23.9% |     |     |
| --- | ------- | ----- | --- | --- |
45.1
|     |     |     | 5.9% | 7.0% 0.5% |
| --- | --- | --- | ---- | --------- |
snoitagitsevnI 4202 fo %
| Ransomware | % 18.5% | 19.6% |     |     |
| ---------- | ------- | ----- | --- | --- |
56.5
|               |                       |             | 2.2%       | 3.3% 0%            |
| ------------- | --------------------- | ----------- | ---------- | ------------------ |
| N o n -       | % 17.4%               | 25.1%       |            |                    |
| Ransom w a re | 42.2                  |             |            |                    |
|               |                       |             | 6.8%       | 8.0% 0.6%          |
|               | ≤ 1 week 8 to 30 days | 31 days     | > 6 months | > 1 year 5 years   |
|               |                       | to 6 months | to 1 year  | to 5 years or more |

Mandiant M-Trends 2025 Report 29
Malware
Unsurprisingly, the top malware category observed in 2024 ransomware intrusions was ransom-
ware, which made up 34% of the malware data set. The next most prevalent categories are in
line with the overall malware landscape observed in 2024. Credential stealers made up 12%
of malware observed in ransomware-related intrusions, followed by backdoors (10%), utilities
(10%), tunnelers (7%), downloaders (6%), and droppers (5%). The other 16% of malware families
had other primary purposes such as keyloggers, launchers, installers, and uploaders.
Compared to the overall
Observed Malware Families by Category, 2024  metrics, ransomware-
Ransomware-Related
related intrusions saw a higher
percentage of BEACON usage
|            |     |       | Credential | Utility | Tunneler |                              |
| ---------- | --- | ----- | ---------- | ------- | -------- | ---------------------------- |
| Ransomware |     | Other |            |         |          |                              |
|            |     |       | Stealer    |         |          | (15%). However, that may be  |
attributable to the bias of the
|     |     |     |     | %   |     | smaller dataset of ransom- |
| --- | --- | --- | --- | --- | --- | -------------------------- |
ware-related intrusions rather
% %
than a true increase in the
12
|     |     |     |     | 10  | 7   | rate of BEACON usage when  |
| --- | --- | --- | --- | --- | --- | -------------------------- |
Backdoor
|     |     | %   |     | Downloader | Dropper |     |
| --- | --- | --- | --- | ---------- | ------- | --- |
compared to all investigations.
|     |     |     | %   | %   |     | The next four most frequently  |
| --- | --- | --- | --- | --- | --- | ------------------------------ |
|     |     |     |     |     | % % |                                |
observed malware families
were ransomware varieties:
| 34  |     | 1610 |     | 6   | 5   |     |
| --- | --- | ---- | --- | --- | --- | --- |
RANSOMHUB (10%), REDBIKE
(aka Akira) (10%), BASTA
(9%), and LOCKBIT (9%). The tunneler SYSTEMBC (7%) was the sixth most commonly observed
malware in ransomware-related intrusions, though it was the fourth most commonly observed
family in all investigations. Several of these also appear in the overall most frequently seen
malware families: BEACON, RANSOMHUB, REDBIKE, BASTA, LOCKBIT, and SYSTEMBC. The
overlap of most frequently seen families for both overall and ransomware-related intrusions
highlights how pervasive and prolific ransomware-related intrusions are.
Compared to global metrics, ransomware-
Most Frequently Seen Malware, 2024  Most Frequently Seen Malware, 20re2la4ted intrusions saw more malware category
Ransomware-Related
Ransomware-Related variation; however, the ransomware-related
| 15  |     |     |     |     | malware dataset contains a much smaller  |     |
| --- | --- | --- | --- | --- | ---------------------------------------- | --- |
%
15
proportion of backdoors. Within ransomware
operations, this likely coincides with threat
snoisurtnI fo % 10 actors continuing to rely on remote control and
|     | %   | %   |     |     |                                                 |     |
| --- | --- | --- | --- | --- | ----------------------------------------------- | --- |
|     | 10  | 10  | % % |     | administration tools. Credential stealers also  |     |
|     |     |     | 9 9 |     |                                                 |     |
make up double the percentage of the dataset
%
|     |     |     |     | 7   | in ransomware-related intrusions in 2024  |     |
| --- | --- | --- | --- | --- | ----------------------------------------- | --- |
5
compared to the overall dataset. Threat actors
using ransomware are more likely to rely on
| 0      |     |         |         |     | publicly available and legitimate tools, such as  |     |
| ------ | --- | ------- | ------- | --- | ------------------------------------------------- | --- |
| BEACON |     | REDBIKE | LOCKBIT |     |                                                   |     |
credential extraction tools (credential stealers
|     | RANSOMHUB | (Akira) | BASTA | SYSTEMBC |     |     |
| --- | --------- | ------- | ----- | -------- | --- | --- |
and remote administration tools), to accom-
Malware Family
plish their objectives.

Mandiant M-Trends 2025 Report 30
Threat actors that conduct ransomware-related intrusions often rely on commercially avail-
able or legitimate tools to facilitate operations. This affords threat actors with various oppor-
tunities to blend in with the target environment, presumably delaying detection and therefore
leading to more successful ransomware deployments against targets. Of these commercially
available or legitimate tools, Mandiant observed that 37% of the tools used during intrusions in
2024 were utilities. This category includes utilities such as PsExec. Credential stealers made up
nearly a fifth (18%) of tools observed in 2024 intrusions. Remote control and administration tools
captured 12% of tools observed, followed by reconnaissance tools (11%) and tunnelers (8%).
The remaining 14% of tools
observed in ransomware-
Observed Tools, 2024
related intrusions fall into
Ransomware-Related
categories such as crypto-
Utility C St r e e a d le e r ntial Other R C e o m nt o r t o e l and mining tools, data mining tools,
Administration
or tools used for lateral
Tool
movement.
%
%
14 12
% Reconnaissance Tunneler
Tool
% % %
37 18 11 8
Tool Category
Credential A utility whose primary purpose is to access, copy, or steal authentication credentials
Stealer
Reconnais- A program whose primary purpose is to conduct some type of system or network recon-
sance Tool naissance (for example, enumerating accounts or systems, or conducting port scanning)
Remote A legitimate program whose primary purpose is to remotely access and control or
Control and administer a system
Administration
Tool
Tunneler A program that proxies or tunnels network traffic
Utility A program that has a specialized purpose that does not fit into any other defined
category (such as keylogger or sniffer)
Other Includes all other tool categories such as cryptomining tools, data mining tools, or tools
used for lateral movement

Mandiant M-Trends 2025 Report 31
Tools observed in 2024 ransomware
Most Frequently Seen Tools, 2024
intrusions were most frequently designed
Ransomware-Related
for the Windows operating system,
almost certainly due to the operating
system’s high market share on desk-
tops. SoftPerfect Network Scanner
(NETSCAN), a network administration tool
for Windows, mac OS, and Linux as well
as PSEXEC, a Windows-native utility used
to execute processes and launch interac-
tive command prompts on other systems,
were both observed in 29% of intrusions.
NLTEST (19%) is often leveraged in ransom-
ware deployment scripts or used manually
by threat actors in the internal recon-
naissance stage of the Targeted Attack
17
Lifecycle, as it is designed to help system
administrators maintain domain controllers
and active directory domains services,
which serve as a main target in ransomware-related intrusions. The remainder of these tools are
also publicly available—MIMIKATZ (18%), RCLONE (17%), ADVIPSCAN (15%), and AnyDesk (15%).
snoisurtnI
fo
%
Most Frequently Seen Tools, 2024
Ransomware-Related
30
% %
29 29
20
%
19 %
18 % 17
% %
15 15
10
0
NETSCAN NLTEST RCLONE AnyDesk
PsExec MIMIKATZ ADVIPSCAN
Tool Family
Tools
ADVIPSCAN ADVIPSCAN is a publicly available network scanner developed by Famatech that has
remote control capabilities.
AnyDesk AnyDesk is a commercially available remote monitoring and management (RMM) applica-
tion that is supported on Windows, macOS, Linux, Android, and ChromeOS devices.
MIMIKATZ MIMIKATZ is a credential stealer written in C that targets Windows authentication
credentials. Techniques employed include stealing password hashes, keys, and Kerberos
tickets. Credentials can be printed to the console or saved to disk. MIMIKATZ also
supports privilege escalation, extracting credentials from the Windows Local Security
Authority Subsystem Service (LSASS) and Security Account Managers (SAM) database,
and service manipulation.
NETSCAN NETSCAN, the SoftPerfect Network Scanner, is a free multi-threaded IPv4/IPv6 scanner
that pings computers, scans for listening TCP/UDP ports, discovers shared folders, and
retrieves information about network computers via WMI, SNMP, HTTP, and NetBios.
NLTEST NLTEST is the Microsoft nltest.exe utility, a command-line tool that is built into Windows
Server 2008 and Windows Server 2008 R2.
PsExec The PsExec utility, developed by Mark Russinovich as part of Sysinternals, is available
from Microsoft.
RCLONE RCLONE is a publicly available command-line utility to sync files and directories to and
from numerous cloud-based resources, such as Amazon Drive, Dropbox, FTP, Google
Drive, HTTP, Mega, Microsoft OneDrive, rsync.net, SFTP, and the local file system.

Mandiant M-Trends 2025 Report 32
Ransomware Operations
Data leak sites
RANSOMHUB
(DLS) are websites
that publish stolen
The RANSOMHUB ransomware-as-a-service (RaaS) and associated DLS launched in early 2024.
data of companies
that refuse to pay By the second half of 2024, RANSOMHUB RaaS became the most prolific DLS that Mandiant
a ransom. While tracks, taking the top spot from LockBit after its activity declined following law enforcement
this data is skewed
action. RANSOMHUB was also tied for most frequently observed ransomware in Mandiant
toward targets
who refused to incident response investigations performed in 2024. Mandiant currently tracks multiple threat
pay attackers’ clusters that have used this ransomware brand, including UNC2165, UNC5227, and others.
ransom demands,
it is still useful for
understanding
broad trends
in extortion
operations.
Jan Feb March April May June July Aug Sept Oct Nov Dec
sgnitsiL
SLD
fo
tnuoC
LockBit vs. RANSOMHUB DLS Listings, 2024
200
LockBit
RANSOMHUB
150
100
50
00
18
UNC2165 is a financially motivated threat cluster that has been active since at least 2019 and
has conducted ransomware and data theft extortion operations using HADES, LOCKBIT, CONTI,
and RANSOMHUB ransomware. UNC2165 has primarily gained access to victim organizations
from FAKEUPDATES infections, although, since late 2020, some intrusions appeared to leverage
stolen credentials. UNC2165 has used various methods to escalate privileges conducting
Mimikatz and Kerberoasting attacks, targeting authentication data stored in the Windows
registry, and searching for documents or files associated with password managers or that may
contain plaintext credentials. Historically, UNC2165 operations heavily relied on BEACON for
lateral movement and to maintain access to the victim environment; however, since late 2023,
UNC2165 has used the MYTHIC post-exploitation framework and VIPERTUNNEL tunneler in
intrusions. In most cases, UNC2165 has also stolen data from victims using Rclone or MEGASync.
UNC5227 is a financially motivated threat cluster active since at least November 2023 that has
monetized access via ransomware deployment and data theft extortion. In some cases, UNC5227
has gained access to victim networks via brute-force attacks or stolen VPN credentials obtained
from a separate threat cluster. UNC5227 relies on open-source tools, including MIMIKATZ and
OPENSSH, to compromise additional accounts and move laterally through the network. They
have also used PORTLIGHT, a custom Windows PowerShell utility for port-forwarding access
using SecureShell (SSH) to maintain persistence, which may be exclusive to UNC5227. UNC5227
also uses EXMATTER, a private file upload tool, on compromised devices for data staging and
theft before deploying ransomware. UNC5227 has deployed LOCKBIT.BLACK, ALPHV, RHYSIDA,
and RANSOMHUB ransomware, based on direct observations as well as overlaps observed in the
wild with EXMATTER and reverse Secure Shell (SSH) infrastructure.

Mandiant M-Trends 2025 Report 33
REDBIKE (aka Akira)
The REDBIKE (aka Akira) RaaS first emerged in early 2023 and has remained one of the most
active based on the quantity of successfully compromised organizations posted to its DLS.
REDBIKE matched RANSOMHUB for most frequently observed ransomware in Mandiant incident
response investigations performed in 2024. Mandiant tracks multiple threat clusters that have
deployed this ransomware, including UNC5277 and UNC5280.
UNC5277 is a financially motivated threat cluster that has deployed REDBIKE ransomware in
extortion operations involving both Windows and ESXi environments. In intrusions where the
initial access vector is known, UNC5277 has leveraged stolen credentials to gain access to victim
VPNs and has relied on publicly available tools to perform internal reconnaissance, escalate
privileges, and maintain a presence in the environment. UNC5277 has used FORGEDGRIT, a
public exploit for CVE-2023-27532, to steal credentials from Veeam backup servers in multiple
intrusions. This threat cluster has stolen data via WinSCP for use in data theft extortion attempts.
UNC5280 is a financially motivated threat cluster active since at least December 2023 that
has deployed REDBIKE ransomware and engaged in data theft operations. UNC5280 has
leveraged valid VPN credentials to gain access to victim environments. UNC5280 initiated a SSH
connection via FreeSSHd or MobaXterm and likely transferred REDBIKE samples to other
hosts. Prior to the deployment of REDBIKE, UNC5280 has used Metasploit and surveyed
target systems to exfiltrate both data and credentials. The threat cluster has also deleted
forensic artifacts.

Mandiant M-Trends 2025 Report 34
Cloud
Compromises
Cloud In 2024 investigations, Mandiant observed threat actors compromise cloud assets through a
compromises
variety of means. The most commonly observed initial infection vectors included email phishing
consist of intrusions
where threat actors (39%), stolen credentials (35%), SIM swapping (6%), and voice phishing or vishing (6%). Mandiant
access a target’s also noted use of prior compromise, exploits, third-party compromise, brute-force attacks, and
cloud environment,
malicious insiders—specifically North Korean IT workers applying for jobs under false pretenses—
excluding the
misuse of cloud in order to gain access to
services for attacker Cloud Initial Infection Vectors, 2024 cloud systems.
operations or Cloud Initial Infection Vectors, 2024
infrastructure such
In terms of objectives, data
as staging payloads Stolen Other
or data theft. Email theft was observed in nearly
Credentials
two-thirds of cloud compro-
Phishing %
mises (66%). Over a third of
cases (38%), served financially
motivated goals, including
14
% SIM Voice data theft extortion without
% Swapping Phishing
ransomware encryption (16%),
% %
business email compromise
(BEC) (13%), ransomware (9%),
39 35 6 6 as well as cryptocurrency theft
and employment fraud.
Two of the most frequently observed threat actors in cloud intrusions were UNC3944 and
19 20
UNC5537. Beginning in spring 2024, UNC5537 used stolen credentials to gain access to data
belonging to clients of the Snowflake cloud data warehousing platform. The threat actor down-
loaded data and attempted to extort targeted organizations or sell the data on cyber crime
forums. Mandiant found no evidence that a breach of Snowflake’s environment occurred, only
Snowflake client credentials.
21
UNC3944 used persistent social engineering techniques to gain access to targeted organi-
zations, often calling service desks and convincing staff to reset passwords and multi-factor
authentication (MFA) methods, including for privileged accounts. After obtaining access,
Mandiant observed UNC3944 use a number of techniques to manipulate cloud hosted systems
and services. The threat actor abused single sign on (SSO) solutions, for example assigning a
compromised account to every application linked to an SSO instance, expanding the scope of
the intrusion beyond on-premises infrastructure to cloud and SaaS applications. Mandiant iden-
tified UNC3944 using SSO applications to create new virtual machines (VMs), which they used
to conduct follow-on activities. UNC3944 used compromised accounts to identify and access
a variety of additional SaaS applications. In at least one case, UNC3944 used RANSOMHUB
ransomware to encrypt an organization’s virtualized environment. UNC3944 also abused cloud
synchronization utilities, to move data from cloud-hosted data sources in the targeted environ-
ment to external attacker-owned cloud storage resources.

Mandiant M-Trends 2025 Report 35
Threat
Techniques
MITRE ATT&CK® is a Since the M-Trends 2020 report, Mandiant has supported the security industry by aligning its
globally accessible
findings with the MITRE ATT&CK framework. To help organizations bolster their security,
knowledge base of
adversary tactics Mandiant provides metrics around the most commonly observed adversary tactics and
and techniques sub-techniques. This information can enable organizations to prioritize the development of
based on real-world
detection capabilities that address these prevalent threats, then inform strategic decisions on
observations. The
ATT&CK knowledge further security planning to improve security capabilities.
base is used as
a foundation for In October 2024, MITRE released ATT&CK framework version 16.1, which aligned techniques and
the development
sub-techniques to better reflect real-world adversary activity and improved platform descrip-
of specific threat
models and tions. This change did not introduce a significant number of new techniques and sub-techniques
methodologies in
to the already established framework. Mandiant began tracking two new ATT&CK techniques
the private sector,
government, and and 29 new sub-techniques in 2024 and mapped an additional 570 Mandiant techniques to the
the cybersecurity MITRE ATT&CK framework. Mandiant now tracks over 4,000 Mandiant Techniques that map to
product and service
the ATT&CK framework, which totals 203 techniques and 456 sub-techniques. The observed
community.
MITRE ATT&CK techniques mapped to the Mandiant Targeted Attack Lifecycle can be found in
the appendix of this report.
MITRE ATT&CK Techniques Used
Most Frequently
Mandiant experts observed adversaries use 71% of MITRE ATT&CK techniques and 40% of
sub-techniques during 2024 intrusions. This is relatively consistent with the two previous
M-Trends reporting periods, during which nearly three-fourths of techniques and nearly half of
sub-techniques were actively observed by Mandiant experts.
MITRE ATT&CK techniques in 2024 largely mirrored those of 2023, showing that these techniques
have remained remarkably stable for several years. In nearly half of investigations, Mandiant
investigators noted the use of a command or scripting interpreter (T1059) by attackers. Notable
divergences from 2023 relate to Data Encrypted for Impact (T1486) and the use of External
Remote Services (T1133). Data Encrypted for Impact (T1486) appears for the first time in the
top 10 most frequently used techniques in 2024, indicating continued popularity of ransom-
ware operations. While the use of Remote Services (T1027) has remained in the top 10 tech-
niques for the past three years, the notable differences between Remote Services (T1027) and
External Remote Services (T1133) lie within their definitions. Remote Services (T1027) relates to
an attacker moving laterally through an environment with valid credentials, using system-based
services that accept remote connections, which has been a typical attacker tactic over the
years. The use of External Remote Services (T1133), or an adversary leveraging external-facing
remote services such as virtual private networks (VPNs), Citrix, or other mechanisms to gain
initial access to an environment, has been a focus for a number of threat clusters that Mandiant
has tracked for years. However, it became popular among threat actors deploying ransomware
throughout 2023 and 2024 and is now reflected in the M-Trends dataset.

Mandiant M-Trends 2025 Report 36
Top 10 Most Frequently Seen MITRE ATT&CK Techniques
| Rank | Technique                                      | Percent |
| ---- | ---------------------------------------------- | ------- |
| 1    | T1059: Command and Scripting Interpreter       | 44.6%   |
| 2    | T1027: Obfuscated Files or Information         | 37.3%   |
| 3    | T1021: Remote Services                         | 35.3%   |
| 4    | T1083: File and Directory Discovery            | 34.2%   |
| 5    | T1070: Indicator Removal                       | 29.4%   |
| 6    | T1082: System Information Discovery            | 26.0%   |
| 7    | T1140: Deobfuscate/Decode Files or Information | 24.7%   |
| 8    | T1486: Data Encrypted for Impact               | 22.9%   |
| 9    | T1071: Application Layer Protocol              | 22.4%   |
| 9    | T1133: External Remote Services                | 22.4%   |
Top 5 Most Frequently Seen MITRE ATT&CK Sub-Techniques
| Rank | Technique                          | Percent |
| ---- | ---------------------------------- | ------- |
| 1    | T1059.001: PowerShell              | 26.2%   |
| 2    | T1021.002: SMB/Windows Admin Share | 23.3%   |
| 3    | T1021.001: Remote Desktop Protocol | 22.6%   |
| 4    | T1070.004: File Deletion           | 21.7%   |
| 5    | T1569.002: Service Execution       | 19.0%   |

Mandiant M-Trends 2025 Report 37
Regional
        Reports
Most Frequently Seen Initial Infection Vectors by Region-AMERICAS Map
Americas
Americas
The metrics reported in this section are based on Mandiant Consulting investigations
affecting organizations that are located in North, Central, or South America.
Targeted Attacks
Initial Infection Vector
For compromises in the Americas in 2024 in which Mandiant was able to determine an initial
infection vector, the most commonly observed vectors were exploits (28%), followed by stolen
credentials (18%) and email phishing (16%). The distribution of initial infection vectors for the
Americas is similar to what Mandiant observed globally in 2024 investigations.
AMERICAS
Exploit
%
28
AMERICAS
| Stolen Credentials |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- |
%
| 18  | Exploit |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- |
28%
Email Phishing
| %   |     | Detection by Source |     |     |     |     |
| --- | --- | ------------------- | --- | --- | --- | --- |
16
 Stolen Credentials
In 2024 Mandiant investigations in the Americas, organizations were first notified of malicious
18%
activity in their environments by external parties 54% of the time and discovered evidence of
 Email Phishing suspicious activity internally 46% of the time. External notifications can be divided into 36%
16% coming from external partners such as law enforcement and cybersecurity companies and
18% coming from attackers, largely in the form of ransom notes. These proportions are largely
consistent with global figures for 2024.
Americas Detection by Source, 2017-2024
Americas Detection by Source, 2017-2024
|     |     | 100 |     |     |     | 0   |
| --- | --- | --- | --- | --- | --- | --- |
Internal
|     |     | )tnecreP( noitceteD lanretnI |           |           | Average Trend  | External Detection (Percent) |
| --- | --- | ---------------------------- | --------- | --------- | -------------- | ---------------------------- |
|     |     | 80                           |           |           |                | 20                           |
|     |     | 60                           |           |           |                | 40                           |
|     |     | 40                           |           |           |                | 60                           |
|     |     | 20                           |           |           |                | 80                           |
|     |     | 0                            |           |           |                | 100                          |
|     |     | 2017 2018                    | 2019 2020 | 2021 2022 | 2023 2024      |                              |

Mandiant M-Trends 2025 Report 38
For 2024 ransomware-related intrusions in the Americas, adversaries first notified organizations
of a compromise in 62% of cases, while external partners such as law enforcement or cyberse-
curity companies informed organizations in 9% of cases. Organizations discovered evidence of
a ransomware-related incident internally in 29% of cases. This frequent rate of adversary
notifications reflects the nature of extortion operations, which require contacting impacted
organizations to initiate ransom negotiations.
Compared to global ransomware-  AAmmeerricicasa sD eDteecteticonti boyn S boyu rScoe,u 2r0c2e4, 2024
related intrusion numbers, the Americas
%
| experienced higher rates of adversary  |     |     |     |     |     | 6   |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
100
|                                      |     |     |     | %   | %   |     |     |                  |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ---------------- |
| notifications (62% compared to 49%)  |     |     |     |     |     |     |     | Adversary        |
|                                      |     |     | 18  |     | 62  |     | %   |                  |
| and lower rates of external partner  |     |     |     |     |     |     |     | External Entity  |
44
Internal
| notifications (9% compared to 21%). It  |     |     | 75  | %   |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
36
is possible that the quantity of ransom-
ware and extortion operations in North
America accounts for this difference—
50
%
| the high volume of adversary activity  |     |     |     | %   |     | 50  |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                        |     |     | 46  |     | %   |     |     |     |
is great enough that adversary
9
| notifications outpace external entity  |     |     | 25  |     | %   |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
29
notifications by a larger margin in the
Americas than globally. According to
| extortion data leak site (DLS) listings,  |     |     | 0   |     |            |            |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ---------- | ---------- | --- | --- |
|                                           |     |     |     | All | Ransomware | Non-       |     |     |
| the United States and Canada represent    |     |     |     |     |            | Ransomware |     |     |
the first and third largest share of orga-
nizations, with United States organiza-
tions alone comprising half of all DLS listings.
DLS Listings for the US vs. All Other Countries, 2020-2024
DLS Listings for the US vs. All Other Countries, 2020-2024
1000
Excluding US
United States
sgnitsiL SLD fo tnuoC
750
500
250
0
| Q1 Q2 | Q3 Q4 Q1 | Q2 Q3 | Q4 Q1 Q2 | Q3 Q4 | Q1 Q2 | Q3 Q4 | Q1   | Q2 Q3 Q4 |
| ----- | -------- | ----- | -------- | ----- | ----- | ----- | ---- | -------- |
| 2020  | 2021     |       | 2022     |       | 2023  |       | 2024 |          |

Mandiant M-Trends 2025 Report 39
Median Dwell Time
The median dwell time for intrusions Mandiant investigated in the Americas in 2024 was 10 days
overall, matching the median dwell time for 2023 and 2022. The median dwell time for internally
and externally notified events in 2024 was also 10 days, which is also fairly consistent with prior
years’ data from the Americas as well as global trends. For ransomware-related events in the
Americas in 2024, the median dwell time was six days versus 12 days for non-ransomware-
related events. These numbers are similar to global numbers.
Americas Median Dwell Time, 2016-2024
150
All
External
125
Internal
)syaD( emiT llewD 100
75
50
25
10 10 10
0
|     | 2016 | 2017 |     | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
| --- | ---- | ---- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
The dwell time distribution for the Americas in 2024 shows that, in aggregate, organizations
continue to reduce the proportion of intrusions that remain undiscovered for long periods of
time and increase the proportion of compromises that are discovered within a week of malicious
activity. The percent of intrusions that lasted one week or less in the Americas in 2024 was
46.6%, compared to 45% in 2023.
Americas Dwell Time Distribution, 2021-2024
| 2021 | %    |      | %   |      | %   | %    | %   |     | %   |     |
| ---- | ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- | --- |
|      | 38.8 | 18.0 |     | 28.2 |     | 11.1 | 3.6 | 0.4 |     |     |
| 2022 | %    |      | %   |      | %   | %    | %   |     | %   |     |
|      | 44.5 | 19.4 |     | 26.2 |     | 4.5  | 2.6 | 2.8 |     |     |
|      | %    |      | %   |      | %   | %    | %   |     | %   |     |
2023
|      | 45.0     | 23.5 |              | 22.3        |         | 4.8        | 4.2        | 0.3 |          |     |
| ---- | -------- | ---- | ------------ | ----------- | ------- | ---------- | ---------- | --- | -------- | --- |
| 2024 | %        |      | %            |             | %       | %          | %          |     | %        |     |
|      | 46.6     | 18.4 |              | 23.8        |         | 6.6        | 5.0        | 0.0 |          |     |
|      | ≤ 1 week |      | 8 to 30 days |             | 31 days | > 6 months | > 1 year   |     | 5 years  |     |
|      |          |      |              | to 6 months |         | to 1 year  | to 5 years |     | or more  |     |

Mandiant M-Trends 2025 Report 40
Threat Groups
The most frequently observed attacker in the Americas was UNC5267, which is the primary
activity cluster Mandiant has designated to track North Korean IT workers. Mandiant responded
to numerous intrusions involving North Korean malicious insiders who had applied to work at
targeted organizations under false pretenses, misrepresenting their identities, locations, and
legal status in order to generate revenue for the North Korean state.
The second most frequently encountered threat actor in Mandiant incident response investi-
gations in the Americas in 2024 was the suspected Chinese cyber espionage actor UNC5221.
The majority of observed activity was related to UNC5221 exploiting CVE-2023-46805 and
CVE-2024-21887 in December 2023 and early 2024 to gain access to a number of organizations.
Mandiant investigators also identified UNC2565 at numerous investigations in the Americas in
2024. UNC2565 is a financially motivated threat cluster that uses the GOOTLOADER downloader
to deliver a variety of secondary payloads, including BEACON, CLEANBOOST, LIGHTDUTY,
SNOWCONE, and WORDFRAME. These intrusions have stemmed from victims accessing
compromised websites. GOOTLOADER infections have been observed leading to data theft
exfiltration and/or ransomware deployment.

Mandiant M-Trends 2025 Report 41
Most Frequently Seen Initial Infection Vectors by Region-EMEA Map
EMEA
The metrics reported in this section are based on Mandiant Consulting investigations
affecting organizations in Europe, the Middle East, and Africa (EMEA).
Targeted Attacks
Initial Infection Vector
The most frequently identified initial infection vectors in Mandiant incident response investi-
gations in EMEA in 2024 were exploits (39%), followed by email phishing (15%) and brute-force
attacks (10%). In EMEA, email phishing and brute-force attacks represented larger proportions
EMEA  of observed initial infection vectors than Mandiant encountered in global investigations.

Exploit
39%
 Email Phishing
15%
Detection by Source
Brute Force
10% The intrusions that Mandiant investigated in EMEA in 2024 were first discovered internally 41% of
the time, while in 59% of cases, an external organization first notified organizations of a
compromise. These figures are similar to the global numbers (43% internal and 57% external).
EMEA Detection by Source, 2017-2024
EMEA Detection by Source, 2017-2024
| 100 |     |     |     | 0   |
| --- | --- | --- | --- | --- |
Internal
| )tnecreP( noitceteD lanretnI |           |           | Average Trend  | External Detection (Percent) |
| ---------------------------- | --------- | --------- | -------------- | ---------------------------- |
| 80                           |           |           |                | 20                           |
| 60                           |           |           |                | 40                           |
| 40                           |           |           |                | 60                           |
| 20                           |           |           |                | 80                           |
| 0                            |           |           |                | 100                          |
| 2017 2018                    | 2019 2020 | 2021 2022 | 2023 2024      |                              |

Mandiant M-Trends 2025 Report 42
In contrast to the distribution observed  EMEA Detection by Source, 2024
EMEA Detection by Source, 2024
globally, in Mandiant investigations in
%
EMEA in 2024, adversary notifications
100 3
| comprised a relatively small share of  |     |      | % % |                  |
| -------------------------------------- | --- | ---- | --- | ---------------- |
|                                        |     | % 12 | 61  | Adversary        |
| notifications overall (3%) and         |     | 57   |     |                  |
|                                        |     |      | %   | External Entity  |
Internal
| ransomware-related events as well   |     | 44  |     |     |
| ----------------------------------- | --- | --- | --- | --- |
75
(12%). In all Mandiant investigations
in 2024, adversary notifications
represented 14% of overall incident
50
discoveries, while adversaries notified
%
| organizations of a breach in 49% of  |     | %   | %   |     |
| ------------------------------------ | --- | --- | --- | --- |
44
|                             |     | 40  | 39  |     |
| --------------------------- | --- | --- | --- | --- |
| ransomware-related events.  |     | 25  |     |     |
0
|     |     | All Ransomware | Non- |     |
| --- | --- | -------------- | ---- | --- |
Ransomware
Median Dwell Time
The median dwell time for EMEA 2024 investigations was 27 days overall, 20 days for internally
discovered events, and 32 days for externally notified events. While the 2024 median dwell times
are higher than 2023 numbers for overall (22 days) and for externally notified events (12 days),
over the long term, dwell times continue to decline. The median dwell time for ransomware-
related events that Mandiant investigated in EMEA in 2024 was seven days, compared to 36 days
for non-ransomware related intrusions.
EMEA Median Dwell Time, 2016-2024
500
All
450
External
400
Internal
)syaD( emiT llewD
350
300
250
200
150
100
| 50  |     |     |     | 2732 |
| --- | --- | --- | --- | ---- |
20
0
| 2016 2017 | 2018 2019 | 2020 2021 | 2022 2023 | 2024 |
| --------- | --------- | --------- | --------- | ---- |

Mandiant M-Trends 2025 Report 43
The dwell time distribution for Mandiant incident response investigations in 2024 in EMEA shows
that the long-term trend is leading to fewer intrusions remaining undiscovered for long periods
of time. The proportion of intrusions that were discovered within one week increased to 36.7%
in 2024.
EMEA Dwell Time Distribution, 2021-2024
2021 % % % % % %
33.0 14.0 22.0 12.0 14.0 6.0
2022 % % % % % %
41.6 12.2 17.7 10.2 11.5 7.0
2023 % % % % % %
35.9 20.5 23.1 6.4 14.1 0.0
2024 % % % % % %
36.7 16.5 27.8 3.8 12.7 2.5
≤ 1 week 8 to 30 days 31 days > 6 months > 1 year 5 years
to 6 months to 1 year to 5 years or more
Threat Groups
Mandiant experts frequently encountered UNC4393 in 2024 investigations in EMEA. UNC4393 is
a financially motivated threat cluster that has monetized access by deploying BASTA ransom-
ware. In at least one case, Mandiant observed UNC4393 leveraging initial access established
by a separate threat actor, UNC5155, using SILENTNIGHT malware. In other investigations,
UNC4393 used brute-force attacks or stolen credentials to gain access to targeted environments.
22
In Europe, particularly in Ukraine, Mandiant continued to respond to APT44 intrusions in 2024.
Mandiant believes that APT44 remains a core contributor to cyber operations related to the
conflict and recently described how APT44 and other Russian cyber espionage threat clusters
have demonstrated a focus on targeting mobile messaging applications for intelligence collection.

Mandiant M-Trends 2025 Report 44
AMPoAstC Frequently Seen Initial Infection Vectors by Region-JAPAC Map
JAPAC
The metrics reported in this section are based on Mandiant Consulting investigations
affecting organizations in Japan and Asia Pacific (JAPAC).
Targeted Attacks
Initial Infection Vector
The most frequently seen initial infection vectors in Mandiant investigations in 2024 in the
JAPAC region, when they could be identified, were exploits (64%), followed by stolen credentials
(14%) and web compromise (7%). Exploits and stolen credentials also topped the list for global
investigations. Both in JAPAC and globally, use of stolen credentials eclipsed email phishing as
an initial infection vector in 2024. The popularity of infostealer malware, as well as the wide-
spread availability of credentials in data leaks and underground forums, may have contributed
to increased incidences of this tactic. Organizations seeking to reduce exposure to the use of
stolen credentials should ensure identity and access management policies that include
multifactor authentication (MFA) are enforced across all user and account types.
Detection by Source
Organizations identified the first evidence of malicious activity internally in 31% of Mandiant
investigations in the JAPAC region in 2024. External notifications accounted for 69% of detection
sources. These figures are identical with detection sources for Mandiant investigations in the
region in 2023.
)tnecreP(
noitceteD
lanretnI
External
Detection
(Percent)
JAPAC
Exploit
64%
Stolen Credentials
14%
Web Compromise
7%
JAPAC Detection by Source, 2017-2024
JAPAC Detection by Source, 2017-2024
100 0
Internal
Average Trend
80 20
60 40
40 60
20 80
0 100
2017 2018 2019 2020 2021 2022 2023 2024

Mandiant M-Trends 2025 Report 45
External notifications can also be divided
JAPAC Detection by Source, 2024 JAPAC Detection by Source, 2024
into adversary notifications and external
%
entity notifications from organizations
|                                       |     |     | 100 |     |     | 6   |           |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --------- |
| such as law enforcement or cybersecu- |     |     |     | %   | %   |     |           |
|                                       |     |     |     | 12  | 33  | %   | Adversary |
rity companies. In 2024, Mandiant inves-
|                                 |     |     |     |     | %   | 58  | External Entity  |
| ------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- |
| tigations in JAPAC, adversary   |     |     |     | 57  |     |     | Internal         |
75
notifications represented a smaller share
%
of overall and ransomware-related
56
events than in global numbers, with 12%
50
adversary notifications in all investiga-
tions and 33% in ransomware-related
%
| intrusions, compared to 14% and 49%  |     |     |     | 25 % |     | 36  |     |
| ------------------------------------ | --- | --- | --- | ---- | --- | --- | --- |
31
globally. External entity notifications for
| 2024 JAPAC investigations were propor-   |     |     |     |     | %          |            |     |
| ---------------------------------------- | --- | --- | --- | --- | ---------- | ---------- | --- |
| tionally higher than global numbers, at  |     |     |     | 0   | 11         |            |     |
|                                          |     |     |     | All | Ransomware | Non-       |     |
| 57% overall compared to 43% globally.    |     |     |     |     |            | Ransomware |     |
Median Dwell Time
The median dwell time for all intrusions in JAPAC in 2024 was six days overall, 10 days for
externally notified events, and six days for internally discovered intrusions. For ransomware-
related intrusions in JAPAC in 2024, the median dwell time was just four days. For non-
ransomware-related compromises, the median dwell time increased to 12 days.
JAPAC Median Dwell Time, 2016-2024
1100
1000
All
External
500
| )syaD( emiT llewD |     |     |     |     |     |     | Internal  |
| ----------------- | --- | --- | --- | --- | --- | --- | --------- |
450
400
350
300
250
200
150
100
50
6 10 6
0
|     | 2016 | 2017 2018 | 2019 | 2020 | 2021 | 2022 2023 | 2024 |
| --- | ---- | --------- | ---- | ---- | ---- | --------- | ---- |

Mandiant M-Trends 2025 Report 46
The dwell time distribution for JAPAC indicates incremental improvement each year in reducing
the number of long-tailed compromises and increasing the proportion of malicious events that
are discovered within the first week. In 2024, more than half of JAPAC investigations were identi-
fied within seven days of the first evidence of malicious behavior, an increase from 48.1% in 2023.
JAPAC Dwell Time Distribution, 2021-2024
2021 % % % % % %
36.4 23.6 20.0 3.6 3.6 12.7
2022 % % % % % %
37.7 11.7 21.6 8.4 16.7 5.0
2023 % % % % % %
48.1 18.5 20.4 7.4 5.6 0.0
2024 % % % % % %%
51.2 14.0 18.6 4.7 11.6 00..00
≤ 1 week 8 to 30 days 31 days > 6 months > 1 year 5 years
to 6 months to 1 year to 5 years or more
Threat Group
Mandiant incident response investigators identified UNC5221 activity during multiple engage-
ments in JAPAC in 2024. UNC5221 is a suspected Chinese cyber espionage actor that exploited
CVE-2023-46805 and CVE-2024-21887 in December 2023 and early 2024 to gain access to a
number of organizations.

SPECIAL REPORT: MANDIANT M-TRENDS 2023 47
Articles O
G
R
A
B
M
E

Mandiant M-Trends 2025 Report 48
Infostealer Malware Continues to
Create a Threat to Enterprise Systems
In the past several years, Mandiant has seen increased attention on a specific category of malware known as info-
stealers and their role in enabling often short-lived, yet deeply impactful intrusions using stolen credentials. Although
infostealers and stolen credentials have always been a serious concern in cybersecurity, the recently renewed focus on
infostealers by malicious actors and—consequently cybersecurity organizations—could signal drastic shifts in the ways
cyber criminals abuse and/or monetize data obtained from infostealers.
Specifically, Mandiant has observed a resurgence in the use of stolen credentials as a means of initial access for
compromises. While the use of stolen credentials by threat actors had dropped from 14% in 2022 to 10% in 2023,
Mandiant identified stolen credentials in 16% of the intrusions observed in 2024. This resurgence is likely fueled, at least
in part, by the large tranches of stolen credentials offered within cyber crime communities that have facilitated this rise
in demand by offering stolen credentials in large tranches and on an individual basis.
Infostealers and broader credential theft are not new threats, but they are seeing a resurgence and have always posed
significant risks to organizations that may not realize employee credentials have been compromised and exposed—
sometimes years prior.
on the system. This information allows threat actors to
The Infostealer Problem
more easily identify targets that align with the interests of
Infostealers are a broad classification of malware that
their particular operations.
have the capability of collecting and stealing a range of
sensitive user information, such as credentials, browser Mandiant has identified corporate credentials in infos-
data and cookies, email data, and cryptocurrency wallets. tealer logs, which highlight the risk to organizations.
Notably, Mandiant does not classify malware used for Successful compromise of an individual user could
mass data theft or collection of basic system survey infor- result in a threat actor gaining further access into an
mation as infostealers. Examples of prominent infostealers environment.
include VIDAR, RACCOON, and REDLINESTEALER.
While many infostealers are built specifically for these Example: UNC5537 Targets
purposes, they may also include basic backdoor and/or Snowflake Customer Instances
remote access trojan (RAT) capabilities, allowing them to
for Data Theft and Extortion
be used to facilitate various attack lifecycle stages during
intrusion operations. Further, infostealer capabilities can Beginning in April 2024, a financially motivated threat
be added to traditional backdoors and RATs to extend the actor, UNC5537, used stolen credentials to access the
functionality of existing malware. For example, TRICKBOT, Snowflake customer instances of multiple organizations.
a malware family infamous for its use as a banking trojan These credentials were primarily obtained from infostealer
and in intrusion operations, was also able to load a malware campaigns that infected the work or personal
credential theft module for infostealing capabilities. computers of the employees and contractors that
accessed Snowflake customer instances. This allowed
Information and credentials obtained via infostealers are the threat actor to gain access to the affected customer
commonly referred to as “logs” and are widely shared and accounts and led to the theft of a significant volume of
sold across underground markets and criminal commu- customer data from their respective Snowflake customer
nities. Threat actors are able to search infostealer logs for instances. Subsequently, the threat actor attempted to
information of interest specific to their targets. Infostealer extort many of the victims directly and sought to sell the
logs can contain data that indicates the use of specific stolen customer data on cyber criminal forums.
websites by users or even the specific software installed

Mandiant M-Trends 2025 Report 49
Mandiant identified that the threat actor used Snowflake infostealer infections are often shared openly in cyber
23
customer credentials previously exposed via criminal communities. This proliferation of infostealer logs
several infostealer malware variants, including VIDAR, and stolen credentials in these communities allows the
RISEPRO, REDLINE, RACCOON STEALER, LUMMA, and information to remain available to threat actors indefi-
METASTEALER. The earliest compromised credential nitely, where it can be used to impact organizations long
leveraged by the threat actor was associated with an after the infostealer infection occurred—in some cases
infostealer infection dating back to November 2020. years later.
In several Snowflake-related investigations, Mandiant
A major advantage of obtaining accesses from infostealer
observed that the initial compromise of infostealer
logs is they can allow threat actors to search for specific
malware occurred on contractor systems that were also
types of accounts depending on their goals. The broad
used for personal activities, including gaming and down-
distribution of infostealers, coupled with the wide range
loading pirated software.
of information they can collect from victims, provides
UNC5537’s campaign against Snowflake customer a plethora of credentials and sensitive information for
instances was not the result of any particularly novel threat actors to work with. Accounts and services found
or sophisticated tool, technique, or procedure. This in these logs, such as credentials for corporate virtual
campaign’s broad impact was the consequence of the private networks (VPNs) and other enterprise services,
growing infostealer marketplace, and it highlights the risk can act as a foothold for further lateral movement within
posed by the sheer volume of credentials circulating in a network. Alternatively, actors may search infostealer
these markets. logs for accesses tailored to other operations, including
systems containing sensitive information for data theft
extortion operations or cloud assets for illicit crypto-
Unique Challenges of Infostealers
currency mining activity.
for Enterprise Environments
Infostealers are often distributed broadly, typically
Example: TRIPLESTRENGTH
targeting individuals, but they can also create unique chal-
Leverages Stolen Credentials
lenges for organizations. Unlike other forms of credential
theft, such as phishing and credential stuffing that can be for Cloud Assets for Illicit
used to target credentials for a specific system, infoste-
Cryptocurrency Mining
alers can collect wide swaths of user data and credentials
Since 2023, teams across Google Cloud have worked
from a single host. Further, in cases where employees or
to disrupt a financially motivated actor that the Google
contractors leverage personal devices for work purposes,
Threat Intelligence Group (GTIG) tracks as TRIPLES-
the threat of infostealers can manifest outside of the
TRENGTH. This actor engaged in a variety of threat
scope of enterprise security and detection measures. For
activity, including cryptocurrency mining operations on
example, corporate credentials could be compromised
hijacked cloud resources. To take over cloud service
when used on an infected personal device, or a compro-
accounts, TRIPLESTRENGTH leveraged stolen credentials
mised personal account could be leveraged in a password
and cookies to gain access to victim cloud environments.
reuse attack against a corporate system. Browsers that
Once authenticated, the actor uses hijacked cloud projects
support synchronization of passwords between instances
to mine cryptocurrencies. Based on analysis of attacker-
can result in corporate passwords being synced to the
owned infrastructure, GTIG determined that the actor has
personal systems of employees and may result in expo-
relied on RACCOON infostealer logs as the source of at
sure. Policies to disallow and detect the use of browser
least a portion of the stolen credentials and cookies used
syncing can help limit this exposure, especially when
in cloud hijacking activities and that the actor had access
paired with user education, which trains employees to
to credentials for Google Cloud, Amazon Web Services,
keep personal and corporate account use separate.
and Linode. Additionally, in monitoring Telegram channels,
Contractors’ devices, often used to access the systems Mandiant has observed personas connected to the group
of multiple organizations, present a significant risk. If routinely advertise access to servers, including those from
compromised by infostealer malware, a single contractor’s prominent hosting providers and cloud platforms, such
device can facilitate threat actor access across multiple as Google Cloud, Amazon Web Services, Microsoft Azure,
organizations. In addition to being sold on underground Linode, OVHCloud, and Digital Ocean.
markets, stolen credentials and information from

Mandiant M-Trends 2025 Report 50
Recommendations Detection Methods Based
To mitigate the risk of infostealers, Mandiant recommends Around the Attack Lifecycle
organizations leverage adversary-in-the-middle (AiTM)-
of Infostealers
resistant multifactor authentication (MFA) methods, such
Threat actors introduce infostealers using a variety of
as hardware security keys or mobile authenticator apps.
deceptive tactics. Phishing emails are a common method
Organizations should consider implementing cookie
that involve using malicious attachments disguised as
expiration and password rotation policies to require
legitimate files or malicious links that lead to compromised
regular password changes for accounts. This will limit the
websites or files hosting the malware. Compromised
lifespan of any compromised credentials and cookies.
websites can also trigger drive-by downloads to automat-
Additionally, developing a robust access policy that
ically install the infostealer, sometimes using exploit kits to
restricts access from unknown or untrusted locations can
compromise browser or plugin vulnerabilities. Infostealers
limit threat actors’ use of stolen credentials.
may also be bundled with infected software downloads
To further strengthen an organization’s security posture from untrusted sources or included in trojanized versions
against information-stealing malware, implementing of legitimate software. Finally, attackers use social engi-
endpoint detection and response (EDR) and intrusion neering to manipulate users into downloading or installing
detection systems (IDS) allows for fine-grained monitoring the malware.
of environments. When configured and monitored effec-
To prevent infostealer infections upon initial delivery,
tively, these tools can provide comprehensive protection
organizations should use existing security infrastructure
by detecting, preventing, and eradicating infections. As
to analyze network traffic and email. Email gateway
infostealers will commonly extract data from an end user’s
monitoring can flag suspicious emails that bypass initial
browser, organizations should apply controls to the
filters, enabling further review and potential interven-
browser to restrict third-party cookies, disable the use
tion. Additionally, monitoring outbound network traffic
of autofill for passwords, and disable browser extensions
via proxies and intrusion detection systems, as well as
that have not been approved for use.
reviewing DNS requests, can help detect malicious down-
To reduce the risk posed by external devices, such as loads. Most enterprise firewalls, DNS servers, and proxies
personal devices, organizations should develop policies offer built-in monitoring capabilities. Ensuring these
that strictly separate the use of personal and corporate detections are sent to a security information and event
systems. Organizations that rely on Bring Your Own Device management (SIEM) platform and reviewed by a security
(BYOD) should design policies or establish restrictions team is a crucial step in limiting the spread of infoste-
regarding appropriate use cases and ensure that alers. If these events are not investigated, malware may
additional measures, such as endpoint instrumentation be detected but not properly remediated if the infection
for BYOD devices and MFA for passwords, are conditions bypasses EDR and antivirus.
that must be met for use. This will help to prevent malware
Infostealers often evade antivirus and EDR tools by
threats from manifesting outside the scope of enterprise
manipulating system resources and behaviors. For
detections. Organizations should also review the secu-
instance, dynamic-link library (DLL) side-loading takes
rity controls that third-party suppliers and contractors
advantage of the Windows loading process to substitute
enforce on their devices to ensure malware threats from
malicious DLLs for legitimate ones, thereby hijacking
infostealers are not introduced via the supply chain.
application functionality. They may also disable or modify
Finally, infostealers are commonly distributed by security tools, either by altering configurations or outright
disguising the malware as legitimate or cracked software. disabling them. To further conceal their presence,
Organizations should establish software use policies and infostealers sometimes use hidden files and directories,
conduct training to prevent users from downloading soft- complicating malware analysis and identification.
ware from untrusted sources. Organizations could also
consider implementing an enterprise application store,
where end users are empowered to download approved
applications. IT security staff should validate these
applications to ensure they are free from malware prior to
being made available.

Mandiant M-Trends 2025 Report 51
Conclusion
While infostealers and broader credential theft are not
novel techniques, we anticipate that actors of varying
motivations and levels of sophistication will continue to
demonstrate a significant interest in leveraging stolen
credentials as an initial intrusion vector. Infostealers can
be an effective method for obtaining stolen credentials as
they are capable of collecting wide swaths of user data,
are readily available in underground communities, and
allow actors to easily search logs for special accesses
of interest. Given the wide availability and long-standing
presence of infostealers in underground communities and
illicit operations, organizations must be aware of the direct
and indirect risks posed by infostealers.

Mandiant M-Trends 2025 Report 52
Democratic People’s Republic of Korea
Insider Threats
Due to international sanctions placed on the country in 2003, the Democratic People’s Republic of Korea (DPRK) has
sought to identify means through which they can continue to fund national interests. As sanctions intensified in 2016 in
response to the DPRK’s testing of nuclear weaponry and as a means to further impact the ruling class in North Korea,
the country found itself cut off from financial systems in the West, further limiting its ability to generate revenue. In
response, the DPRK has pursued a variety of means to evade sanctions, including illegal weapons sales, front companies
operating in international regions, and outright theft. As technology has progressed, the revenue-generating schemes
pursued by the DPRK have evolved. Ranging from the theft of more than $100 million USD through fraudulent SWIFT
24
transactions in 2016 to compromises targeting cryptocurrency in 2024, technical proficiency leveraged for theft has
been a primary focus for the DPRK.
Since 2022, Mandiant has tracked a threat cluster it refers to as UNC5267, which represents the DPRK’s efforts to place
thousands of its citizens in countries outside of North Korea to pose as remote IT contractors for Western companies.
These citizens, commonly referred to as “DPRK IT workers,” are directed to seek employment in high-tech companies
headquartered among Western countries and funnel salaries back to the DPRK to fund national interests, including the
continued investment in weapons of mass destruction. DPRK IT workers most commonly work through job placement
services and recruiters but have been observed pursuing direct employment as well. Their operations are supported
through a broad network of false or stolen identities and third-party accomplices. Outside the fraudulent activity
necessary to place a DPRK IT worker in a Western organization, Mandiant identified evidence of direct malicious activity
in fewer than five investigations in 2024. However, the access to corporate infrastructure necessary for the high-tech
jobs that DPRK IT workers pursue places organizations at heightened risks of extortion, espionage, data theft, and
disruption, which may escalate as the campaign continues.
single identity is a taxing endeavor. For DPRK IT workers,
Pre-Hiring Tradecraft
however, it appears they maintain a substantial array of
The fraud and identity theft guardrails surrounding
false identities.
employment in Western countries require both applicants
and employers to adhere to a strict set of processes The competitive nature of the IT industry makes
designed to limit the hiring of individuals using fraudulent individual efforts at placing a DPRK IT worker in a high-
identities. As such, long-term employment of a North paying position far from guaranteed. In 2024, Mandiant
Korean citizen with the ultimate goal of funneling money identified a suspected DPRK IT worker using at least
back to the DPRK without exposure requires the creation 12 personas while seeking employment in the US and
of a complex network of false personas and supporting Europe. DPRK IT workers have been observed providing
documents. DPRK IT workers have been observed using references to recruiters for other false personas
stolen identities and identities that appear to be wholly controlled by the DPRK. In at least one instance, two
fabricated to support their operations. Each persona and false identities were considered for a job in a US
supporting document—or element of a falsified online company, with one DPRK IT worker winning out over the
presence—comes with its own care and feeding require- other. In at least three investigations, Mandiant identi-
ments to maintain the illusion of a potential dedicated fied multiple suspected DPRK IT workers hired by the
employee. Similarly, the language requirements needed customer. In one such example, four suspected DPRK IT
to navigate the interview process successfully can add workers had been employed within a 12-month period
an additional strain on the upkeep of the false persona in at a single organization. Successfully navigating an
use. While the DPRK has invested heavily in education for organization’s hiring process may give DPRK IT workers
the English language, science, and math, maintaining what adequate experience such that they can continue to
is effectively a cover identity in a foreign language for a target that organization using additional false personas.

Mandiant M-Trends 2025 Report 53
Mandiant has identified suspected DPRK IT worker profiles suspected DPRK IT worker was supplied with a security
hosted on job-posting platforms such as LinkedIn and challenge password that, when translated from Chinese,
Indeed that contain false testimonies, fabricated employ- referred to “silver star.” The reuse of key artifacts in back-
ment and educational histories, and which claim a wide ground material for false personas reduces the level of
range of technical proficiency. Online profiles maintained effort needed to maintain a variety of ready-to-use identi-
by suspected DPRK IT workers are often carefully crafted, ties containing a mixture of fabricated data often overlaid
with some even going so far as to interact with officers atop identities stolen from US citizens.
of the universities from which they claim to have gradu-
ated. A pattern commonly found on resumes of suspected
Post-Hiring Tradecraft
DPRK IT workers is one in which the persona claims to
reside at a local US-based address but to have studied DPRK IT workers have been reported as residing primarily
27
abroad at international universities. This pattern is not in Russia and China, with smaller groups suspected to
wholly consistent across all suspected DPRK IT worker reside in Africa and Southeast Asia. Geographical location
profiles but may serve to hinder the efforts of potential has long been a reliable means for detecting fraudulent
employers seeking to confirm the educational background activity across many security realms. While network traffic
of a false persona. Similarly, when an applicant undergoes originating from North Korea would raise immediate alarm
a background check during the interview process, DPRK IT bells in an organization’s security operations center, the
workers have been observed providing education histories countries most accessible to DPRK agents, such as Russia
that do not match the program of study or the years of and China, share the same threat characteristics for
attendance listed on their resume. many Western organizations. Even for organizations that
might not alert over simple geographical associations, the
Much like any organization facing administrative burdens, disparity between the location of the falsified persona and
DPRK IT workers have found they can alleviate some of the region from which their connections originate expose
the overhead through simple reuse. Resumes associated additional risk for detection. To reduce the risk of expo-
with suspected DPRK IT workers can be seen borrowing sure, once engaged with an unsuspecting employer, DPRK
heavily from publicly available resumes, and even reusing IT workers rely on a variety of techniques to maintain
those among the corpus of resumes for DPRK IT workers. operational functionality while obfuscating their identity
Mandiant’s analysis of a Netlify page associated with and location.
25
a suspected DPRK IT worker uncovered two distinct
resumes that presented separate identities with unique Since Mandiant began tracking DPRK IT worker activity in
personal information, such as phone numbers and email 2022, Mandiant has observed suspected DPRK IT workers
addresses. The resumes listed differing educational connect through virtual private network (VPN) sessions
and professional backgrounds, but both included associated with the Astrill VPN in 72% of investigations.
identical uncommon phrases, which could be used to tie Threat actors across all levels of complexity and motiva-
the resumes to a potential singular author. The supporting tions have recognized that a VPN can raise the level of
sites, which are used to bolster the false persona used effort required for network defenders to identify poten-
by a DPRK IT worker, also appear subject to a degree of tially malicious network sessions effectively. This can be
“templatization.” Sites suspected to be part of DPRK IT as simple and useful as threat actors using services that
worker operations often reuse common themes, layout, terminate in a Western country, while the threat actors
and content or leave key sections unaltered from themselves operate from a country that would appear
their defaults. more suspicious. To combat this kind of threat among
a growing remote workforce, many companies rely on
Among the content found on suspected DPRK IT worker impossible travel analysis to identify sessions that indicate
sites, resumes, and postings, Mandiant has identified a user has connected from a region they could not have
additional patterns of use for various key artifacts. Email traveled to in the time between successive connections.
addresses and domains commonly include a series of Mandiant has observed advanced threat actors going as
themes, including specific words or numbers. The words far as to ensure their connections originate from the same
“panda,” “dev,” “star,” “silver,” and “sun” are often reused region as a legitimate connection would originate for a
across a series of indicators associated with DPRK IT specific compromised user. During such incidents,
workers. In an affidavit filed by the US Federal Bureau investigators must work to differentiate the expected
26
of Investigation (FBI) in 2023, the FBI attested that a activity from malicious activity among multiple sessions
freelance worker who provided account sharing to a occurring in close geographical proximity. For suspected

Mandiant M-Trends 2025 Report 54
DPRK IT workers, however, VPN analysis is further On the other end of the spectrum of support provided
complicated due to the kinds of work the operative by facilitators, some operate full “laptop farms,” which
engages in on behalf of their employer and an overall lack host the corporate laptops of their customers for remote
of malicious activity. In cases involving suspected DPRK access. This provides a stable location from which
IT workers, the actions taken rarely, if ever, step into the network connections will be sourced, which matches
category of malicious activity commonly associated with the country in which the company is headquartered.
threat actors. Instead, their activity blends into legitimate Facilitators ensure laptops remain active and available for
network traffic almost entirely. their customers and install remote access software that
their customers use to access the corporate laptop. In two
Since the wide adoption of remote work, provisioning
separate investigations performed by Mandiant incident
and shipping a corporate laptop to newly hired remote
responders, suspected DPRK IT workers provided the
workers has become a common onboarding process for
same shipping address for their corporate laptop during
many organizations. This provides organizations more 28
onboarding. A US grand jury indictment filed in 2024
control over the individual systems that connect back to
against a suspected facilitator estimated that the accused
the corporate environment. Similarly, security teams have
knowingly assisted in fraud schemes, including running a
an opportunity to apply policies and instrumentation to
laptop farm, which ultimately impacted more than 300 US
the endpoint, which grants a greater degree of visibility
companies using over 60 stolen identities, and resulted in at
and the ability to limit the specific applications allowed on
least $6.8 million USD in revenue for the DPRK.
the endpoint. This model for onboarding new hires intro-
duces an additional avenue of risk for DPRK IT workers While preconfiguring a system and onboarding remote
as shipping a laptop to their physical locations is likely users with a corporate-owned laptop is a common
to raise an immediate alarm within the organization. This process, ongoing monitoring and restrictions on unnec-
has led suspected DPRK IT workers to rely on in-country essary applications is a less consistent operation. Remote
“facilitators” who perform services for a fee. Facilitators management tooling is common in both legitimate and
supporting DPRK IT workers have been identified in the US malicious use. DPRK IT workers are not unique in their
and in Europe. The services provided by facilitators range understanding that legitimate remote access management
from simple singular interactions to contracts with an tools have as much or more value in maintaining long-
expectation of ongoing support. term access to an environment. While malware such as
backdoors might provide more features, for threat groups
In some cases, facilitators may assist with cashing
pursuing more clandestine operations, the use of remote
paychecks or receiving physical mail, including corporate
management tools reduces their detectable footprint.
hardware on behalf of their customers. In one case, a
Much like the use of location-specific VPN sessions,
facilitator was used to pass an in-person drug test for
DPRK IT workers enjoy a substantially reduced detection
a DPRK IT worker hired by a US company. Mandiant
footprint as their day-to-day workflows are often indistin-
investigated a suspected DPRK IT worker compromise in
guishable from those of legitimate employees.
2023 during which the operative’s corporate laptop was
shipped to an apartment block in a major US city. When
law enforcement investigated the location, they found Detection and Mitigation
an empty apartment and the box in which the laptop was Detecting potential DPRK IT workers requires a strict
shipped. An analysis of connection logs indicated that employee data verification pipeline and a comprehensive
the suspected DPRK IT worker connected to corporate baseline of endpoint and network monitoring. The best
resources through an Astrill VPN session that masked the means through which organizations are able to protect
origin of the connection. A subset of the network sessions themselves from this kind of risk are preventative
recorded showed the VPN connection appeared to fail measures. Additional scrutiny in the hiring process and
and, before being reestablished, IP addresses associ- improvements in the overall instrumentation and moni-
ated with China were observed connecting to the same toring post-hiring are also valuable tools for organizations
corporate resource from the same system. A facilitator employing remote workforces.
was used in this case to receive and potentially reship the
laptop from its expected location to the true location of During the interview process and when onboarding new
the remote DPRK IT worker. In this instance, the customer remote workers, identifying disparities between the
had not suspected their employee of operating under a purported facts and the observed facts grants orga-
false persona until notified by law enforcement. nizations an opportunity to protect themselves. Strict

Mandiant M-Trends 2025 Report 55
background checks that include the collection of to a follow-on destination. In the event that a remote hire
biometric information from the new hire, which is requests corporate resources be sent to an address not
subsequently used for specialized background checking listed on their employment documents, delaying shipment
services, may help detect forged identities. Even identi- and reviewing the associated background checks may
fying the service associated with the applicant’s phone help reduce the hiring organization’s exposure to risk.
numbers could be a valuable check in the interview and
From a technical standpoint, ensuring corporate
onboarding process. Mandiant has observed suspected
resources are delivered with monitoring tools such as
DPRK IT workers supplying phone numbers associated
endpoint detection and response tooling pre-installed
with Voice over Internet Protocol (VoIP) services instead of
helps organizations build baseline application use metrics.
consumer phone lines. Similarly, logging and reviewing key
Monitoring solutions should be configured to identify and
artifacts, such as the email address and phone number
alert on the use of remote access software and connec-
used by applicants, can help develop a dataset against
tions originating from VPN services. Endpoint detection
which hiring organizations can compare current and
and monitoring solutions should be configured to log
previous applicants to identify someone trying to reuse
details of any human interface devices (HID) plugged into
information under a different identity.
the laptop, and this data should be reviewed. Mandiant
DPRK IT workers have often demonstrated an unwilling- has observed DPRK IT workers and facilitators use
ness to appear on camera during interviews and once network-based KVM switches to control corporate laptops
hired. Differences in the personas they adopted in order housed within laptop farms. Reviewing HID connect and
to be interviewed, especially when using stolen identities, disconnect logs is a crucial opportunity to identify poten-
may become apparent to hiring managers and coworkers tial DPRK IT workers.
when they are forced to appear on screen. Rescheduling
Appropriately siloing data and conforming to a security
or outright cancelling interviews with candidates for
framework that enforces the principle of least privilege
remote work who refuse to appear on screen raises the
should be a standard part of an organization’s security
burden for potential DPRK IT workers during the interview
posture. Ransomware operators, insider threats, and
process. Forcing operatives to match their false personas
espionage groups all rely on access to data that exceeds
to a specific physical presentation or rely on unproven
what is necessary for most corporate roles. While
technology such as video face-swapping services to
evidence of direct malicious activity has been limited,
bypass immediate detection also increases the chances
in at least two cases Mandiant investigated in 2024, the
they are detected by external security organizations and
suspected DPRK IT worker resorted to extorting their
law enforcement.
employer after they were exposed. In both instances,
Many of the suspected DPRK IT worker cases Mandiant the exposed employees demanded money in exchange
investigated in 2024 stemmed from notifications provided for promises to not publish confidential corporate
to impacted organizations by law enforcement organi- data. Ensuring users only have access to the data and
zations, such as the FBI. Once hired, the detection resources needed to perform their duties helps limit
opportunities available to organizations rely less on impact from a variety of threats, including those posed by
comprehensive security practices and more on identi- DPRK IT workers.
fying inconsistencies and exploiting mistakes made by
suspected DPRK IT workers. Disparities between the
Conclusion
geographical region in which a suspected DPRK IT worker
purports to live and the addresses provided for shipping The organizations DPRK IT workers target appear to
documents and corporate resources provide another align more with opportunistic targeting than with a given
opportunity for detection. DPRK IT workers have been targeting objective. Additionally, the limited instances
observed using stolen identities and falsified identification of direct malicious cyber activity point more toward
credentials that retain the address of the original identity. targeting of high-paying job roles. One of North Korea’s
In such cases, they often request corporate resources primary strategies for avoiding the negative effects of
to be shipped to the address of an in-country facilitator. international sanctions is by finding ways to generate
Requiring in-person pickup of corporate laptops with full revenue. Furthermore, the continued pursuit of weapons
verification based on a valid ID limits the ability for DPRK of mass destruction is a primary goal of the Kim regime,
operatives to ship corporate hardware to laptop farms or with ever-growing budgetary demands. A large portion of
suspected DPRK IT workers are reportedly subordinate

Mandiant M-Trends 2025 Report 56
to organizations under the 313 General Bureau of the
29
Munitions Industry Department, which is responsible for
the nuclear program in North Korea.
Organizations outside North Korea are natural targets
for DPRK-nexus threat actors, either through the data
they produce and store or by the simple fact that they
generate revenue that can be funneled into the DPRK illic-
itly. The DPRK IT workers are the latest in a long series of
tactics undertaken by a regime that is focused on evading
international punitive measures. If not curtailed, DPRK IT
workers operating within Western organizations pose a
significant risk to businesses and national security beyond
simple fraudulent employment.

Mandiant M-Trends 2025 Report 57
The 2024 Iranian Threat Landscape
As tensions in the Middle East escalated throughout 2024, Mandiant observed the scale of Iran-nexus threat actor
operations increase across the region. Iran-nexus threat actors continued to sustain cyber operations against targets of
strategic and operational relevance, while increasingly focusing on Israeli targets.
Mandiant observed Iran-nexus threat actors combine several approaches to heighten the likelihood of successful
intrusions. Most notably, they significantly expanded their arsenal of custom malware for use in the full spectrum
of cyber operations. At the same time, they also maximized their use of publicly available resources such as cloud infra-
structure and legitimate tools to evade detection. Mandiant observed threat actors employ increasingly effective social
engineering schemes that quickly integrated worldwide events, computer security incidents, and employment themes.
This resulted in effective campaigns through which Iran-nexus threat actors pursued cyber operations in alignment with
national and strategic objectives.
the year by the same groups. These campaigns are often
Expanding Arsenal of
coordinated with exposure efforts by online personas with
Custom Malware
the ultimate goal of manipulating the public narrative
When conducting cyber operations, threat actors can surrounding regional issues. Ongoing hack-and-leak
choose to create their own malware or use readily avail- operations from various online personas affiliated with
able public tools. Proprietary malware allows the threat Iran-nexus threat actors aided in this endeavor.
actor to tailor the malware to operational requirements.
The online personas that support disruptive operations
However, the flexibility provided by custom malware
often operate under the guise of cyber activism, also
comes at the cost of resource-intensive development and
known as hacktivism, in an attempt to hide their affiliation
maintenance. In the event that custom malware is discov-
with state-level entities. The online personas “Karma” and
ered, replacing the capability can be costly for threat
“Homeland Justice” have claimed credit for operations
actors. In comparison, publicly available tools are more
targeting organizations in Israel and Albania. In 2022,
easily replaceable but may not fit all the threat actor’s
Homeland Justice claimed credit for an attack targeting
needs. Mandiant observed Iran-nexus threat actors align
30
Albania with the ROADSWEEP malware. In 2023 and
with the first approach throughout 2024 as they signifi-
31
2024, Karma claimed credit for wiper attacks on Israeli
cantly increased their arsenal of custom malware.
organizations. Public reporting has asserted that both of
Mandiant tracked a 35% surge in malware attributed to the online personas were provided access to their targets
32
Iran-nexus threat actors compared to 2023, with more through prior compromises from UNC1860, which is
than 45 new malware families discovered in 2024. This publicly referred to as “Sacred Manticore.” UNC1860 is
increase may be due, in part, to the escalation of geopolit- likely affiliated with the primary intelligence agency of
ical tensions as a result of Iran’s proxy war with Israel and Iran, the Ministry of Intelligence and Security (MOIS).
its steady investment in offensive capabilities as part of a
Similarly, the online persona “Handala Hack” claimed
broader strategy to enhance cyber operations.
responsibility for numerous cyberattacks that targeted
Israeli government and financial organizations with the
Destructive and Disruptive Malware
proprietary COOLWIPE wiper in December 2023. In July
In 2024, Israel-based targets were a focal point for 2024, Handala Hack claimed responsibility for a phishing
destructive and disruptive operations from Iran-nexus campaign that deployed COOLWIPE to Israeli targets. A
and pro-Iran threat actors. During these campaigns, more recent campaign delivered malware masquerading
Iran-nexus threat actors relied heavily on wipers, a type as a security patch for a faulty security vendor update.
of malware designed to erase or corrupt the data of the However, to date, evidence supporting the claims made by
computer it infects. While organizations associated with Handala Hack has not been provided.
Israel were heavily targeted, entities in other regions, such
as Albania, were also targeted with wiper malware early in

The 2024 IranianMa nTdiahnt Mr-Terenadst 20 25 Report 58
Landscape 1/3
Figure 1
The online group “Cyber Toufan” has also been linked to
wiper activity and claimed responsibility for hack-and-
leak operations targeting Israeli companies, government
entities, and individuals. On the one-year anniversary of
the Oct. 7 attack against Israel, Cyber Toufan promoted
a video on their Telegram channel that corresponded
with an operation that targeted Israel-based users with
the proprietary POKYBLIGHT wiper. The same group was
linked to Android and Windows wiper campaigns targeting
Israel-based users earlier in 2024. In each instance, the
phishing emails masqueraded as alerts to security fixes
and safety guidelines from an Israeli government institute.
Proprietary Malware
Mandiant identified more than 20 proprietary malware
families—including droppers, downloaders, and
Figure 3.1: Wizard installation window displayed to the victim
backdoors—used in campaigns in the Middle East. Six
previously unknown custom malware families were
deployed in 2024 as part of suspected APT34 operations In July 2024, a suspected Iran-nexus threat actor distrib-
targeting Iraqi government entities. APT34 is an Iran- uted the CACTUSPAL backdoor, 36 which masqueraded
nexus cyber espionage group that has been operational as an installer for the Palo Alto Networks GlobalProtect
since at least 2014 and has been largely focused on remote access client. Upon execution, an installation
phishing efforts to benefit Iranian nation-state interests. wizard that mimicked a legitimate Palo Alto Networks
Two of the six newly identified backdoors, DODGYLAFFA and installer was displayed to the user while CACTUSPAL’s .NET
33
SPAREPRIZE, overlap with a public report of suspected payload was written to disk. Once the targeted user
Iranian operations targeting Iraqi government networks. closed the dialog window, the GUI thread aborted, and the
main CACTUSPAL execution continued. The CACTUSPAL
34
UNC3313, an Iran-nexus threat group that carries out
backdoor is designed to verify that only one instance of
surveillance and strategic information-gathering
the process is running when executed before it initializes
operations, was observed distributing a series of custom
the staging directory and running configuration prior to
dropper and backdoor malware during spear-phishing
the start of command-and-control (C2 or C&C) activity.
campaigns in 2024. The threat actor hosted malware on
popular file-sharing services and embedded links within UNC2428, an Iran-nexus threat actor that conducts
training- and webinar-themed phishing lures. In one such cyber espionage-related operations, is suspected to
campaign, UNC3313 distributed the JELLYBEAN dropper have distributed the MURKYTOUR backdoor through a
and CANDYBOX backdoor to organizations and individuals complex chain of deception techniques in October 2024.
targeted by their phishing operations. UNC3313 is UNC2428’s social engineering campaign targeted individ-
suspected to be affiliated with MuddyWater, a group the US uals while posing as a recruitment opportunity from Israeli
35
Government reported as being subordinate to the MOIS. defense contractor, Rafael. Individuals who interacted with
the campaign were redirected to a site purporting to be
Prevalence of Graphical User Interfaces part of Rafael’s web presence, where users could down-
load a tool to assist with applying for a job. The installer,
in Malware
named RafaelConnect.exe, was the LONEFLEET installer
In 2024, Mandiant observed an increased focus on
malware, which presented the user with a GUI front-end
deception techniques used to improve the chances of
through which they could provide personal information
success when targeting individuals. Iran-nexus threat
and an opportunity to submit a resume. After the form was
actors incorporated graphical user interfaces (GUIs) to
submitted, the MURKYTOUR backdoor was launched as a
disguise malware execution and installation as legitimate
background process. UNC2428’s activity overlaps with the
applications or software. The addition of a GUI that pres-
Israel National Cyber Directorate’s attribution to a group
ents the user with a typical installer and is configured to 37
called “Black Shadow.”
mimic the form and function of the lure used can reduce
suspicions from targeted individuals.

Mandiant M-Trends 2025 Report 59
Phishing Email
RafaelConnect.ese cscapi.dill MsDef.ese
hxxps://rafaelcon- ‘RafaelConnect’
LONEFLEET LEAFPILE MURKYTOUR
nect[.]com/down- Archive
installer launcher backdoor
load
Figure 3.2: Suspected Black Shadow attack flow
in phishing campaigns over the year. During these
Leveraging Cloud and Public
campaigns, the threat actor would host the installer for
Resources to Evade Detection
a given RMM on major file-sharing services, with links
While Iran-nexus threat actors have invested in developing to the installers included in various phishing lures. Upon
custom malware in recent years, they have also taken installation, the RMM was configured to provide access to
steps to reduce the detectable footprint of their intrusions. the system from attacker-controlled infrastructure. Since
Mandiant observed Iran-nexus threat actors adopt greater the RMMs used by UNC3313 had legitimate use cases, the
use of legitimate remote monitoring and management likelihood of detection by network or endpoint agents was
(RMM) tools and tailor their operational infrastructure to reduced when compared to a custom backdoor. Where a
mimic those used by their targets. threat actor’s use of custom malware can be exposed and
quickly integrated into blocklists or endpoint detection
RMMs are legitimate tools that allow IT personnel to
and response (EDR) tooling, RMMs are rarely included
access a computer remotely in order to manage the
in automated detect-and-block mechanisms due to the
system on which the tool is installed. UNC3313 relied
nature of the tools themselves. This can lead to a much
heavily on RMMs during the initial access phase of many
delayed response between identification and actioning
of their intrusions in 2024. Mandiant identified at least
within an organization.
nine different RMM agents disseminated by UNC3313
The 2024 Iranian Threat Landscape 3/3
Figure 3
Archived Remote
Compromised Spear-phishing
UNC3313 Cloud-hosted URL Monitoring and
email addresses dissemination
Management (RMM)
Figure 3.3: UNC3313 attack flow
A number of Iran-nexus threat actors have also been suspected to have built C2 infrastructure and hosted
observed taking additional steps to ensure the infrastruc- payloads in the cloud while also tailoring the domain
ture used during their attacks blended in with commonly names they used to match common domains. In some
used infrastructure. As cloud adoption continues to grow cases, UNC1549 customized the domains used in their
year-over-year, threat actors have taken advantage of campaign on a per-target basis, and in others, went so far
the centralization of resources among the major cloud as to ensure servers were geolocated near their targets.
vendors. In addition to techniques such as typosquatting
39
APT42, a prolific Iran-nexus threat actor known for
and domain reuse, threat actors have found that hosting
its meticulous social engineering efforts and rapport
C2 nodes or payloads on cloud infrastructure and using
building, maintained a series of credential harvesting
cloud-native domains reduces the scrutiny that may be
campaigns in 2024. Active since at least 2015, APT42
applied to their operations.
commonly maintains contact with targeted individuals as
38
UNC1549, a suspected Iran-nexus threat actor that has they attempt to build trust; they also often build well-
targeted the aerospace, aviation, and defense industries tailored decoy sites during campaigns. Mandiant recently
in Middle East countries, regularly used cloud infra- observed the threat actor deploying fake login sites
structure during intrusions in 2024. The threat actor is mimicking Google, Microsoft, and Yahoo as part of their

Mandiant M-Trends 2025 Report 60
credential harvesting campaigns. APT42 used cloud- As Iran-nexus threat actors continue to pursue cyber
based platforms and services, such as Google Sites operations that align with the interests of the Iranian
and Dropbox, in operations that directed targets to fake regime, they will alter their methodologies to adapt to the
Google Meet landing pages or login pages. The threat current security landscape. While evolutions in a threat
40
actors also targeted Israel and the US in 2024, including actor’s tactics, techniques, and procedures can result
individuals affiliated with presidential campaigns, military in temporary detection challenges, a comprehensive
personnel, diplomats, academics, and non-governmental understanding of the factors that can fuel operations for
organizations (NGOs). APT42 deployed infrastructure that these groups can help organizations in their threat hunting
aligned with the specific individuals and entities that were endeavors. Perhaps most importantly, collaboration
being targeted and launched complex social engineering across industries and sectors threatened by Iran-nexus
schemes to lure targets to interact with the malicious actors is necessary to safeguard organizations from the
sites. The lures that APT42 used were customized to risk posed by these groups.
include references to legitimate entities such as think tanks
and, in at least one case, the threat actors referenced a
specific target’s name.
Conclusion
Attackers evolve, and so must defenses, but the funda-
mental principles that make up a robust security program
remain critical. Some Iran-nexus threat actors continue to
rely on credential harvesting and multifactor authentication
(MFA) bypass for initial access. Any practice that raises
the effort required to bypass MFA has a subsequent
negative effect on threat actors. Enforcing phishing-
resistant MFA methods, such as certificate-based
authentication (CBA) and FIDO2 security keys, wherever
possible, remains a core security practice—especially
when it comes to privileged accounts. Similarly, as
organizations continue to adopt cloud technology, a
security-first design should be implemented to blend
the business and operational needs with the security
responsibilities of cloud operations. A design that seeks
not only to define the security controls, but also ensures
adequate visibility into all cloud-based activities, provides
the necessary data for threat hunting, incident response,
and ongoing monitoring. Finally, user awareness training—
especially training that seeks to engender a community
of responsibility when it comes to the security of the
organization, its customers, and their data—is critical to
the protection of any organization. Social engineering
campaigns are becoming increasingly complex, and
organizations should educate users on the ways in which
they might be targeted outside of work-based perimeters.

Mandiant M-Trends 2025 Report 61
Evolution of Data Theft in Cloud and
Software-as-a-Service Environments
In recent years, Mandiant has observed a dramatic increase in cloud computing and software-as-a-service (SaaS)
adoption, with organizations embracing these technologies for their scalability and flexibility. This shift, however, intro-
duces a model where security responsibilities are shared between the provider and the customer in a highly contextual
manner. While cloud and SaaS offerings bring numerous benefits, they also present unique security challenges for IT
professionals, business leaders, and security practitioners tasked with securing these environments. Mandiant has
observed attackers adapting to this shift in IT infrastructure and modifying the techniques they rely on for data theft. By
understanding the evolving motivations and tactics, network defenders are able to embrace and build on practices that
better address gaps in visibility, challenges with identity management, and complexities in strategic security plans.
cloud-native solutions, Mandiant observed threat actors
Early Patterns of Data Theft
shift their attack techniques in kind. While security funda-
Data theft followed a relatively predictable pattern
mentals stayed relatively the same, many of the traditional
prior to the ready availability of cloud infrastructure. A
security controls that were once effective in detection and
typical scenario involved an attacker gaining access to
mitigation of data theft started to fall behind.
a network, often through phishing or exploiting vulner-
abilities in internet-facing systems. Once the attacker
gained internal access to a targeted environment, they Shifting Tactics: Attacker
typically performed internal reconnaissance to map the Adaptation and Exploitation
network and identify valuable resources and data. Once
Throughout 2024, Mandiant observed attackers increas-
they identified resources that fit their objective, threat
ingly eschewing traditional on-premises network infiltra-
actors escalated privileges to gain access to sensitive
tion in favor of targeting cloud-based stores of centralized
information stored within. That data would be copied to a
authority, such as single sign-on (SSO) web portals. When
compromised system in the environment and then stolen
successful, these centralized authorities could grant a
and stored on attacker infrastructure. This pattern was
threat actor broad-scale access to an environment.
reliable enough to form the basis of the steps taken to
In the past, attackers would have to compromise a single
identify threat actors during investigations.
system and move laterally through an environment before
To address the risk posed by threat actors, organizations finally acquiring high-privilege access, such as domain
relied on a combination of security controls and detection admin credentials. The centralized nature of cloud identity
sources that they could build into their environment. At and access management (IAM) technologies can provide
the time, this approach was made more effective by the a shortcut with fewer opportunities for exposure. High-
existence of clear perimeters in a network and the relative value accounts can often be used to bridge access
simplicity of infrastructure that allowed it to be success- between cloud and on-premises environments. Attackers
fully managed by small organizations. Security instrumen- are targeting user credentials for cloud services and
tation was developed over time to give greater degrees of subsequently social engineering corporate help desk
visibility into network traffic, endpoint activity, and data teams to reset passwords and enroll new multifactor
transfers, while security information and event manage- authentication (MFA) devices to gain access to corporate
41
ment (SIEM) platforms were developed to aggregate and identity solution portals. Threat actors such as UNC3944
highlight risk concerns. While this paradigm for detection used compromised SSO credentials to access virtual
and security served business needs well for decades, infrastructure management platforms and launched
the value proposition of cloud-based technologies could virtual machines (VMs) to support post-compromise
not be ignored, and organizations leapt at the chance activities and data theft. Mandiant has observed threat
to do more for less. As client environments shifted away actors compromise on-premises accounts configured
from traditional on-premises infrastructure to hybrid and with certain cloud-related privileges and configurations.

Mandiant M-Trends 2025 Report 62
In cases where the account is sufficiently privileged, these
Managing Responsibilities
accounts can provide a very effective means to impact
and Risk
cloud environments from on-premises resources.
As the value presented by cloud infrastructure has
Where compromising a single privileged account can be
become more apparent, situations have emerged where
a boon to threat actors, a threat actor gaining privileged
the priority of business operations has grown at a pace
access to SSO and identity management platforms can
that outstrips the ability of security teams to identify risk
only be described as a windfall. These platforms are
and design security solutions. An area where this may
capable of granting broad-scale access across the cloud
become apparent is in the identification of realms of
and SaaS environments with which they integrate. Once
responsibility. Cloud platforms function under a shared
attackers gain access to these systems, they can often
responsibility model, where the responsibility for securing
escalate privileges and pivot to other applications and
the environment stack is divided between the customer
services associated with these management consoles.
and the provider. The shared responsibility model, when
Mandiant observed attackers with compromised SSO
not well understood, can lead to unmanaged risk and
credentials add themselves to privileged groups that
significant impacts to an investigation in the event of
granted access to a wider range of SaaS applications.
a compromise.
Attackers are employing hybrid approaches, using both
Not fully understanding the shared responsibility model
on-premises and cloud resources during their operations.
may lead organizations to make assumptions that can
During one investigation, Mandiant identified evidence
damage their security posture. If an organization mistak-
that the threat actor discovered cloud access keys stored
enly believes that security is the sole responsibility of
in plain text on the compromised on-premises network.
the provider, the security of the data, applications, and
The threat actor was able to use the keys to access and
access controls in their environment can be placed at
steal data from the client’s cloud storage buckets. When
risk. This can be critical when the sensitivity of the data
the actor transferred the data they were stealing from the
implies requirements under legal frameworks, such as
cloud buckets, they used a destination cloud bucket they
the Sarbanes-Oxley Act. While the provider is commonly
controlled, which was hosted on the same platform. This
responsible for the security of the underlying infrastruc-
helped the activity blend in with legitimate activity in the
ture, customers are ultimately responsible for the security
platform monitoring logs.
of their data and the applications they build. Fully under-
standing the organizations’ responsibilities regarding
In addition to traditional social engineering of accounts
security in a shared responsibility model is a critical
with privileged access to on-premises solutions, Mandiant
aspect of designing secure environments.
has observed a rise in the use of social engineering to
target users that threat actors suspect have privileged
In a similar vein, organizations should ensure they have
access to SaaS environments. Deceiving a targeted user
a full accounting of where necessary log data is gener-
into providing credentials or approving MFA requests
ated and by whom. It is an organization’s responsibility
provides threat actors with an immediate escalation into
to understand logging requirements from a forensic and
cloud resources without having to compromise on-
regulatory perspective. It is important to collaborate with
premises networks where security operations teams may
the cloud or SaaS provider to understand and verify the
have better visibility. This follow-on effect of targeting
regulatory requirements with which they are compliant.
seeks to exploit potential gaps in understanding and
Not all subscription levels provide the detail necessary to
visibility, while quickly accelerating the speed at which a
fully capture relevant information. Ensuring your subscrip-
threat actor can complete their mission objectives. The
tion matches your requirements will assist with not only
more a customer understands their subscription, the
regulatory compliance, but security visibility.
breakdown of responsibilities, and the means through
which an investigation may be performed, the better Many legal frameworks related to the security of sensitive
prepared they are to not only withstand attacks, but to data have log generation and retention requirements.
investigate them as well. The quality and storage of cloud and SaaS-generated
telemetry can also affect the pace of investigations into
suspicious activity.

Mandiant M-Trends 2025 Report 63
Mandiant has encountered multiple organizations that is also highly desirable as it supports not only business
do not fully understand the implications of their specific operations but investigative activities as well.
subscription levels within the cloud and SaaS platforms
To monitor cloud environments effectively and detect
they use. Even logs critical to audit logging for SaaS appli-
potential data theft attempts, organizations should ensure
cations can be dependent on the customer’s subscription
comprehensive logging is enabled across their cloud
level. Many investigations into cloud environments have
services. The following log sources provide necessary
been slowed or otherwise negatively impacted when the
visibility into various aspects of cloud infrastructure and
assumed logging level does not match the reality of the
should be enabled and regularly reviewed. Whenever
subscription service. Audit logging provides substantial
possible, configuring alerts for suspicious log events
value to network defenders tasked with monitoring for
and enabling timely detection and response to potential
and investigating suspicious activity. The quality and
security incidents can help minimize the impact of
quantity of the recorded logs can greatly decrease the
successful attacks.
time required to resolve an investigation and increase the
confidence in the findings. The better a customer under-
stands the features included at their subscription level, Network Traffic Logs
the associated breakdown of responsibilities, and how
it may affect their visibility into critical areas of security, VPC Flow Logs
VPC flow logs (GCP and AWS)
the better prepared they will be to identify risk and make
informed changes. NSG flow logs
VNet flow logs (Azure)
Visibility Challenges in the Cloud
VPC flow logs capture information about IP traffic flowing
One of the most significant challenges in securing cloud
to and from network interfaces within your virtual private
environments is gaining the appropriate level of visibility
cloud (VPC) or virtual network (VNet). They are essential
into the environment. Where traditional environments
for detecting unusual traffic patterns, identifying potential
have clear boundaries and choke points that could be
command-and-control (C2 or C&C) communication, and
instrumented, cloud environments scale more broadly
understanding network access to sensitive resources.
and require an in-depth understanding of a variety of
logging options. While the verbosity and availability of Verify that flow logs are enabled for each VPC, subnet, or
logs can vary greatly depending on the provider and the network interface as needed.
customer’s subscription level, some log sources should be
prioritized for collection and auditing. Firewall Logs
Organizations should strive for logging that encompasses Firewall logs, whether from a dedicated network firewall
user logins and logouts, data access and modifications, or integrated with your VPC/VNet, record details about
administrative actions, system/configuration changes, and traffic, which is allowed or denied based on your firewall
other security-related events. These logs should capture rules. These logs help monitor network access to your
details such as timestamps, user identities, IP addresses, resources and identify potential attempts to bypass
device information, and specific actions performed. security controls.
Increased logging may lead to additional costs tied to a
Verify that logs are stored in a centralized location, such
combination of cloud storage, processing, and service
as a SIEM.
tiers. These costs have a ripple effect impacting managed
service provider (MSP) pricing and organizations with
Storage Access Logs
limited security budgets.
Cloud Storage access logs (GCP)
Organizations should also take into consideration regu- S3 Server access logs (AWS)
latory requirements and security capabilities when Storage Analytics logs (Azure)
determining an appropriate log retention period. Ideally,
customers should have easy and secure access to these
Storage access logs provide detailed records of requests
logs with the ability to search, filter, and export data for
made to your cloud storage buckets. They are crucial for
analysis. The ability to integrate logs with SIEM tools for
identifying unauthorized access, the scope of data exposure,
centralized log management, correlation, and analysis
and understanding how data is being accessed and used.

Mandiant M-Trends 2025 Report 64
Evolution of Data Theft in
Cloud and Software as a
Service Environments 1/1
Confirm that access logging is enabled for all sensitive
Traditional New Cloud
data storage buckets.
Technique Adaptation
Compute and Resource Monitoring Internal Reconnaissance via Cloud Storage Object
gcloud logging API (GCP) SMB Scanning (MITRE T1135) Discovery (MITRE T1619)
CloudWatch metrics (AWS)
Data Staging (MITRE T1074) Modify Cloud Compute
Azure monitor metrics Infrastructure (MITRE T1578)
While not traditional logs, these services provide Data Collection from Local/ Data collection directly from
Network Systems (MITRE cloud storage services like S3,
performance and operational metrics for various cloud
T1005/T1039) Azure Blob Storage, or Google
resources, including compute instances and storage Cloud Storage (MITRE T1530)
volumes. Monitoring these metrics can help identify unusual
resource utilization, which could indicate malicious activity, Exfiltration Over C2 Channels Data exfiltration directly to
(MITRE T1041) cloud storage services (MITRE
such as cryptomining or unauthorized data processing.
T1567.002) or attacker-con-
trolled accounts (MITRE T1537),
Confirm that logging is set appropriately, validated, and in
blending exfiltration traffic with
a place where security personnel can review. legitimate cloud usage
Audit Logging Table 4.1: Traditional data theft technique adaptations for cloud and SaaS
Cloud Audit Logs (GCP) environments
CloudTrail Logs (AWS)
Azure Activity Logs
It is recommended to not only capture and store any IAM-
specific logging but to set up relevant alerts and monitoring
Audit logs record API calls and management actions for security personnel to continuously review and audit.
made within a cloud environment and provide an audit
trail of who did what and when. These logs are critical for
Adapting Traditional Methods to
detecting unauthorized configuration changes, privilege
escalation attempts, and other suspicious adminis- the Cloud
trative activity.
While threat actors continue to evolve to meet new
technologies, they are not abandoning their tried-and-
Ensure that the logs are activated for any and all cloud
true data theft techniques. Instead, they are simply
environments and in a place where security personnel
adapting them to the cloud environment, creating a hybrid
can review.
approach that leverages both on-premises and
cloud resources.
Database Logs
Database logs can record accesses and commands
Conclusion
executed against databases. Databases in both traditional
and cloud technologies provide a target opportunity for The migration to cloud and SaaS environments has funda-
sensitive information and are frequently an area mentally changed the landscape of data theft. Attackers
containing visibility gaps. are adapting quickly, exploiting potential complexities
of cloud infrastructure and security to their advantage.
Enable database-specific audit logs to monitor access and
Relying solely on traditional security approaches designed
activity within your managed databases.
for on-premises environments can lead organizations into
areas of unsuspected risk. A security-first approach to
Identity and Access Management Logs cloud adoption is essential. By understanding the evolving
Many cloud providers offer specific logs related to IAM threat landscape, implementing robust security controls,
activities. IAM logs could include logs for authentication and fostering a culture of security awareness, organiza-
events, authorization failures, and changes to IAM policies. tions can reduce the risks of cloud data theft and harness
the full potential of cloud computing.

Mandiant M-Trends 2025 Report 65
Common Themes in Cloud Compromise
Investigations
As organizations migrate to the cloud, protecting cloud and hybrid environments has grown increasingly complex. Organi-
zations often look at their cloud infrastructure in isolation, focus on cloud-native controls, and aim to secure data and
operations within the cloud itself. However, the evolving threat landscape is challenging the efficacy of this approach.
As a result, threat actors are capitalizing on misconfigurations that extend beyond the cloud’s perimeter. By abusing
these misconfigurations, attackers are able to gain access to cloud environments. This can be seen even in organizations
with mature cloud security instrumentation. For example, Mandiant has encountered environments where the customer
has deployed endpoint detection and response (EDR) tooling across all cloud-hosted virtual machines. With administra-
tive access to the EDR managed through a federated identity provider, protections are often not designed to secure the
EDR admin console in the event the identity store is compromised. Were an attacker to compromise the identity store
in an environment such as this, they would be able to access the virtual machines (VMs) in the cloud through the EDR
agents directly. This example, taken from frontline investigations performed by Mandiant, demonstrates how a compro-
mise outside the boundary of the cloud environment can lead to a compromise of workloads in the cloud.
Common identity architecture
In 2024, Mandiant responded to more breaches that
On-Premises Directory Service
involved a cloud component than ever before. In (Active Directory)
On-Premises
the investigations Mandiant performed, three major
Synchronization Service
themes contributed to threat actor successes in these
Cloud
environments: Federated Identity Provider
(Microsoft Entra ID, Okta, OneLogin, Google Workspace)
1. Identity solutions that lack sufficient security controls
2. Improperly secured on-premises integrations Cloud Infrastructure
AWS Azure Google Cloud
3. Poor visibility into extended cloud attack surface
AWS Identity Center Azure RBAC Roles Google Cloud Identity
AWS IAM Roles Google Cloud IAM Roles
Taken as a whole, these factors signal a need for a secu-
rity approach that bridges the gaps between on-premises
and cloud, while also recognizing that the cloud’s attack Figure 5.1: A common organizational identity architecture
surface is not isolated, but part of an interconnected
ecosystem that demands proactive integrated defenses.
Identity Architecture
Securing Identities
A common organizational identity architecture typically
Identity in cloud and/or hybrid environments serves as the includes an on-premises directory service, a federated
first line of defense as many cloud incidents stem from identity provider, and a cloud Identity and Access
compromised identities. Typically, these incidents origi- Management (IAM) infrastructure service.
nate from two key weaknesses: an identity architecture
Organizations often adopt this architecture to unify
that does not protect against the use of compromised
their identity program and streamline authentication and
credentials and identity practices that include policies
authorization across all layers. While this setup is conve-
attackers can exploit.
nient, it can also introduce attack vectors that attackers
frequently exploit. Attackers often target on-premises
directory services, particularly when those services are
used to manage and administer cloud environments. This
creates a critical point of failure that can compromise

Mandiant M-Trends 2025 Report 66
the entire system. Once an on-premises identity store is operations, granting them unlimited and unrestricted
compromised, attackers can reuse those stolen creden- access often introduces considerable risk. Attackers
tials to access and compromise cloud resources directly. frequently set their sights on third-party providers in the
hopes that by compromising a single vendor, they can
Identity Practices open pathways into multiple downstream organizations.
Attackers often seek the easiest and most efficient ways Organizations that lack sufficient controls around access
to compromise privileged identities and execute their to critical cloud data and infrastructure expose their
attack chain—whether through malware deployment, data identity stores to even greater risk. Because it is difficult
theft, or other malicious activities. The most common to differentiate between compromised and legitimate
methods of identity compromise include brute forcing credentials, security surrounding access should be
using common/guessable passwords, replaying stolen commensurate with the sensitivity of the resources. By
credentials from a previous breach, credential stuffing, increasing the level of effort required to authenticate and
phishing, and social engineering. Additionally, improperly interact with critical data and infrastructure, additional
secured identity practices often serve as a path of least onus is applied to threat actors seeking to compromise
resistance when attackers need to escalate privileges the environment. Critical identity measures, such as privi-
during a compromise. Mandiant categorizes commonly leged identity management (PIM) and phishing-resistant
abused identity practices into three major areas: MFA, are relatively simple to implement and substantially
multifactor authentication (MFA), self-service, and third- improve security but require significant operational load to
party identities. maintain and operate. Tying access to specific geograph-
ical locations or requiring privileged access workstations
Mandiant regularly observes that organizations are not
creates additional conditions that a threat actor must
protecting privileged accounts with MFA. The absence of
meet in order to gain access.
MFA leaves these accounts vulnerable to basic credential
attacks, such as password spraying and credential An aspect that sometimes gets overlooked is the security
stuffing. Even when implemented, MFA methods such as risk posed by members of the extended workforce.
SMS, phone calls, or push notifications are susceptible As organizations cannot enforce security controls on
to a variety of bypass techniques. These include adver- systems they do not own, the resources that contractors
sary-in-the-middle (AiTM) attacks, account takeover and vendors interact with should be tightly controlled.
via manipulation of the MFA registration process, social This includes enforcing limitations on the remote access
engineering, SIM swapping, intercepting MFA codes, and management tools that are permitted to access critical
exploitating MFA fatigue. Additionally, many organiza- resources and ensuring that a clear barrier between full-
tions do not secure the MFA registration and modification time employees and the extended workforce exists. A
process sufficiently, which allows attackers in possession common way to accomplish this is to onboard third-party
of compromised valid credentials to register their own vendors into their own identity store separate from the
MFA methods and continue operating undetected. corporate identity store.
Mandiant has frequently observed attackers exploit
password reset portals and related technologies to obtain On-Premises Integrations
credentials that grant them direct access to targeted
As organizations deploy cloud infrastructure, it’s common
organizations. Portals that are only protected by single-
to create integrations with on-premises infrastructure to
factor authentication or those that can be accessed
reduce friction for users and allow network and compute
from any device or location are particularly vulnerable
connectivity with existing systems. While this architecture
to password-spraying attacks. Additionally, systems like
has operational benefits, if an attacker is able to gain
interactive voice response (IVR), which rely on limited veri-
access to either of these environments, the integration
fication data such as date of birth, corporate information,
could allow vertical movement between cloud and
employee IDs, or Social Security numbers, can be easily
on-premises or vice versa. Mandiant has regularly
bypassed through social engineering campaigns.
observed evidence of threat actors having crossed the
on-premises to cloud boundaries during intrusions. While
Many organizations depend on third-party vendors,
threat group motivations may vary, the risk presented
such as managed service providers (MSPs), to manage
by not securing integrations has been demonstrated
elements of their cloud environments. While external
by prolific threat groups such as APT29, UNC3661,
partners can streamline data, infrastructure, or security
and UNC3944 crossing environments as they pursue

Mandiant M-Trends 2025 Report 67
operational objectives. Even with state-of-the-art cloud The cloud attack surface encompasses the data attackers
security controls, improperly secured integrations with can enumerate about an organization’s cloud environment.
on-premises systems can allow an attacker to bypass This includes details about identities, security configura-
these controls and compromise a cloud environment. tions, settings, and resource configurations. This infor-
These integrations can be broken down into two main mation is often accessible outside a network perimeter
categories: trusted service infrastructure and compute to low-privileged or even unauthenticated users. Freely
and network integrations. available tools can collect significant volumes of data
regarding cloud tenants if not properly secured.
Trusted Service Infrastructure
Credential sprawl, including long-lived service account
Trusted service infrastructure is typically associated with keys, also forms a critical component of the cloud attack
the management interfaces for platforms and technolo- surface. Inadvertent publishing of these credentials in
gies that provide core administrative services. Examples public code repositories, shared documents, or other
of trusted service infrastructure include: insecure locations often provides initial access and lateral
movement opportunities. In addition, these credentials
• Asset and patch management tools
are often collected and posted for sale on dark web
• Network management tools and devices
forums and chats. This is especially risky when cloud
• Backup technologies service accounts are assigned default or basic roles,
• Security tooling such as Owner or Contributor. Organizations that do not
centrally manage and secure service account creden-
• Virtualization consoles
tials are susceptible to these types of attacks. Mandiant
• Privileged access management systems often encounters environments where service accounts
As these are already associated with legitimate are not properly documented and a baseline of their use
infrastructure within an environment, attackers will often does not exist. This can make recovery of a compromised
target these platforms and abuse their intended environment a high-friction process as the ability to rotate
functionality. Mandiant has observed attackers targeting credentials is slowed.
trusted service infrastructure to pivot between cloud and
Lastly, publicly exposed and accessible resources expand
on-premises infrastructure.
the cloud attack surface. This can be from the perspective
of both IaaS and platform-as-a-service (PaaS) compo-
Compute and Network Integrations 42
nents. Risks with IaaS typically arise from VMs with
Compute and network integrations are commonly used public IP addresses and firewall rules allowing traffic from
when organizations leverage infrastructure-as-a-service the internet on administrative ports. In PaaS environ-
(IaaS) cloud components that are tightly integrated with ments, where the cloud provider manages the underlying
on-premises environments. These integrations can allow infrastructure, misconfigured API or resource sharing
an attacker that has compromised on-premises servers or can pose significant risks. These misconfigurations can
virtual machines (VMs) to gain access to cloud VMs. Often allow access from external accounts or even anonymous
in this scenario, the fact that these VMs are hosted in the access from the internet.
cloud does not affect the attacker’s techniques or motiva-
These factors require organizations to identify and reduce
tions. For example, an attacker that has compromised an
their cloud attack surface proactively and use tools that
Active Directory privileged user account could impact a
provide views into their environment similar to what an
domain-joined VM hosted in the cloud. This could be via
attacker would see. Cloud security posture management
Group Policy Object deployment or, if the VMs share
platforms have many valuable features, including the
network connectivity, the attacker could remotely access the
ability to provide a comprehensive inventory of cloud
machine over RDP or SSH from the on-premises network.
resources. This enables organizations to build a cloud
asset management program, set standards on what
Extended Cloud Attack Surface should be exposed publicly, and then detect and reme-
Mandiant has often observed that organizations manage diate a non-compliant resource. Many platforms have
their attack surface from the perspective of a defined attack surface management capabilities that provide
network boundary or perimeter. While network exposure visibility into internet-accessible resources, what software
remains a risk, the attack surface in cloud environments is running, and if there are vulnerabilities or entry points.
extends further.

Mandiant M-Trends 2025 Report 68
Common Themes in Cloud Compromise Investigations 3/3
Action 1 Action 3 Action 5 Action 7
End user unknowingly Through Kerberoasting, Attacker logged into the Attacker stole data from
downloaded a fake remote attacker escalated cloud using the compromised storage
administration installer that privileges to domain compromised cloud services to attacker-
executed a malware administration rights. administrator account controlled infrastructure.
downloader from an infected and performed additional
website, which installed a reconnaissance.
backdoor malware on
system Patient 0.
Action 2 Action 4 Action 6 Action 8
Attacker performed Using the compromised Attacker modified Access Attacker leveraged a
reconnaissance activity domain administrator Control Lists to allow cloud feature used to
against the on-premises account, attacker reset the traffic to malicious IP execute scripts and
identity store listing specific password for a cloud- addresses across storage commands across
configurations, user, group synchronized administration services within the cloud-hosted virtual
membership, and role account within the compromised cloud machines to mass deploy
assignment. on-premises identity store. environment. encryption.
Figure 5.2: Incident Response Case Study
Incident Response Case Study Conclusion
Mandiant was engaged by a customer to respond to an Mitigating evolving attacker techniques in the cloud
incident that included improper access to the customer’s requires more than a single tool, configuration, or control.
cloud environment. Mandiant incident responders It demands a comprehensive, multilayered approach
identified evidence of a threat actor moving through the that includes carefully applied restrictions, hardening
customer’s hybrid environment and bypassing security measures, ongoing detection strategies, and proactive
controls to steal data before mass deploying ransomware. response actions. By integrating these protections across
every layer—from managed identities and resources to
The attack chain began when a user unknowingly down-
network and endpoint defenses—organizations can build
loaded a fake remote administration installer, resulting
a resilient security posture that anticipates and mitigates
in the installation of a backdoor. The attacker then
the complexities of today’s hybrid threat landscape.
conducted reconnaissance of the on-premises identity
store and used Kerberoasting to escalate privileges to
Domain Administrator.
Due to the fact that the targeted organization leveraged
their on-premises identity store to create and manage
cloud administrator accounts, the attacker was able to
acquire the password for a cloud administrative account.
With this foothold established, the attacker moved into the
cloud environment, performed additional reconnaissance,
and modified access control lists to allow for communi-
cations to the attacker-controlled external infrastructure.
This communication channel was then used for data
theft. Lastly, the attacker leveraged a native cloud feature
commonly used to deploy scripts to initiate a large-scale
ransomware attack by encrypting cloud-based VMs.

Mandiant M-Trends 2025 Report 69
Security Recommendations for Diverse
Cloud and Hybrid Environments
In any given year, Mandiant consultants respond to, assess, and advise thousands of clients across the various
consulting services we provide. Engagements that include cloud or software-as-a-service (SaaS) components have
become the norm as customers have expanded their environments to capitalize on the value presented by cloud tech-
nologies. While each environment is unique and poses its own challenges for security professionals, over the years,
Mandiant consultants have identified a set of recommendations that can help provide a baseline for better security
across diverse cloud and hybrid environments. By designing environments around identity and infrastructure controls
that limit potential impacts of common threat actor activity, organizations can better secure their environments and
meet their critical day-to-day business needs. Pairing controls with logging and detection capabilities that can provide
substantial insight into activity in the environment gives network defenders the necessary visibility to validate controls,
monitor for anomalies, and engage in threat hunting activities.
• Modern authentication clients and protocols that
1. Reduce the Impact of
require and enforce multifactor authentication (MFA)
Stolen Credentials
challenges should be configured for all accounts.
Stolen and compromised credentials are a common initial
• Access to applications should require phishing-
access vector used by threat actors regardless of skillset
resistant MFA, such as FIDO2 security keys.
or objective. Organizations should train employees on the
risks of password reuse and secure password management • Privileged account access should be restricted to
practices, which should be made available to employees known locations, IP addresses, and specific devices.
and refreshed regularly. Technical controls applied to how • All access requests should be evaluated for potential
users authenticate to and within the environment provide indicators of compromise prior to issuing authentica-
an additional layer of identity security. Organizations can tion tokens.
reduce the impact of compromised credentials by imple-
• The lifespan of individual sessions should be limited to
menting access control policies that evaluate necessary
short periods of time and require re-authentication with
conditions dynamically before granting access for a user.
MFA upon expiration.
Such conditions should include the following:
• Cyber threat intelligence data, such as credential
• All applications and resources should only be accessed
monitoring services, should be integrated into identity
through managed endpoints that are compliant with
Reduce the impact of stolen crmeandageemnentt itoa dlestect accounts that have been
organizational policies.
compromised and automatically expire active sessions.
Single-Factor Weak Multifactor Strong MFA Identity + Device Multicontext Criteria Risk/Consequence
Authentication (SFA) Authentication Enforcement? Validation? Identity + Device + Geo of Stolen Credentials
+ Origin Bound
Permitted? (MFA) Enforcement?
Yes No No No No High
Yes No No Yes No Elevated
No Yes No No No Elevated
No Yes Optional No No Medium
No No Yes No No Lower
No No Yes Yes No Low
No No Yes Yes Yes Lowest
Table 6.1: Control implementation to reduce the impact of stolen credentials

Mandiant M-Trends 2025 Report 70
2. Protect Cloud Infrastructure
from On-Premises Compromise
Organizations should focus on segmenting both cloud
identities and resources to protect against on-premises
compromise and vice versa. Privileged cloud accounts
should not be synced to an on-premises identity store;
instead, isolate privileged cloud accounts and limit their
use to administrative tasks. Similarly, privileged accounts
used to administer on-premises environments should not
be synced to the cloud to protect against the same kind of
lateral movement. Access to privileged accounts should
be controlled using the principle of just-in-time access,
which grants temporary privileges only when necessary.
For any trusted service infrastructure, the following
actions are recommended:
• Limit the accounts that are allowed to authenticate to
and access infrastructure tooling.
• Review and validate MFA enforcement for all accounts.
• Implement network restrictions to allow authentication
and access from trusted IPs/networks only. Additionally,
implement similar attribute-based access controls
that can restrict access from specific identities, device
types, and/or operating systems, where applicable.
• Create detections that focus on monitoring authentica-
tions and the activity performed within trusted service
infrastructure.
3. Align Logging and Detection
Strategy with Cloud Threats
and Risks
Lack of visibility into cloud environments and logging
limitations limit the efficacy of threat hunting, incident
detection, and response activities. A comprehensive
strategy defined to identify and address both general and
specific risks to an organization’s cloud infrastructure can
help ensure investigations into suspicious activities are
not impeded. Organizations should ensure that logging
for storage bucket access, database access, and network
flow logs are included in their configuration. Proactively
reviewing the logging configurations beyond the default
settings, validating the activity they capture, and
centralizing logging to a SIEM should be a priority for
security teams seeking better visibility into their cloud
environment. Threat hunting and simulated attacker
scenarios can help identify gaps in logging that may
impede an investigation before they are able to negatively
impact the process.

Mandiant M-Trends 2025 Report 71
Threats to Web3 and Cryptocurrency
Malicious cyber operations involving Web3 technologies—cryptocurrencies, blockchains, and other decentralized
user-centric technologies—are diverse, ranging from theft and money laundering to financing terrorist and military
programs. Over the last three years, Mandiant has observed an increased targeting of the cryptocurrency industry,
signaling an uptrend motivated by a variety of factors, such as its fast adoption, the security posture of the targets, and
the inherent technical difficulty in disrupting these campaigns. While Web3 is not new, it is still considered a technology
in emergence that is currently being integrated across industries beyond start-ups, including traditional finance institu-
tions, the video game industry, and health and life insurance services.
Historically, emergent technology presents unique challenges to the entities adopting them, and Web3 is no exception.
The financial sector is currently the most commonly targeted industry by threat activity and is also the largest adopter
43 44
of Web3 technologies. Financial industries have introduced blockchain into their platforms, created digital currencies,
45
and launched new products for financial markets as financial regulations expand. This confluence of adoption and
consistent threat actor activity has highlighted the need for additional scrutiny as organizations seek to protect their
users, data, and digital assets.
The Rise of Web3: Opportunities Democratic People’s Republic of Korea
Cyber Crime
and Risks
In recent years, threat actors affiliated with the
One of the inherent challenges organizations face when
Democratic People’s Republic of Korea (DPRK) have
adopting new technologies is balancing the speed of
regularly targeted organizations and individuals who
integration while maintaining a robust security posture.
have adopted Web3 and cryptocurrency. In the past
As technologies mature, the methodologies through
three years, Mandiant has investigated heists attributed
which threat actors target them also grow. Mandiant
to DPRK-nexus threat actors that resulted in over
has observed threat actors targeting blockchain-native
$500 million USD in stolen digital assets as a means of
and blockchain-adopting industries in pursuit of a wide
bypassing international sanctions. The focus on Web3 and
range of objectives. From leveraging cryptocurrency theft
46 cryptocurrency appears to be primarily financially moti-
for financial gain to the distribution of malicious code
vated due to the heavy sanctions that have been placed
through censorship-resistant features of decentralized
on North Korea. Historically, the DPRK-nexus threat actor
networks, threat actors are identifying ways to enrich
APT38 has been primarily responsible for attacks against
themselves at the cost of the organizations and users
financial institutions and some of the largest thefts of
exploring the benefits of Web3.
funds through cyberattacks.
Cryptocurrency transactions, though recorded on a
DPRK-nexus threat actors appear to have access to a
blockchain, pose challenges for both public institutions
substantial cache of custom tooling written in a variety of
and private industry. Obfuscated fund flows and money
languages, including Golang, C++, and Rust. These tools
laundering hinder large-scale tracing, while the immu-
are often obfuscated with anti-analysis software, such
tability of smart contracts can prevent malicious code
as VMProtect and the open-source tool Garble. While
removal. These factors reduce threat actors’ risk of iden-
obfuscating code is not a new tactic, nor is it impene-
tification, sanctions, or prosecution. Coupled with threat
trable to analysis, raising the level of effort needed to
actors’ adaptation to Web3, specialized phishing tools
reverse engineer their malware—or simply slowing the
such as “drainers” targeting crypto wallets and Web3
analysis—is sufficient cause for its use in many cases.
projects create an ongoing threat, undermining trust in
Mandiant has also observed these threat actors deploying
the ecosystem.
malicious tools designed for a variety of operating
systems, including Windows, Linux, and macOS. Given
the widespread use of macOS by developers, especially
in the Web3 industry, the ability to compromise multiple

Mandiant M-Trends 2025 Report 72
operating systems with custom tooling provides flexibility software services, biotech, and media. UNC5342 distrib-
during cyber operations. These activities aim to generate uted the BEAVERTAIL downloader via malicious crypto-
financial gains, reportedly funding North Korea’s currency-themed NPM and Python packages hosted on
weapons of mass destruction (WMD) program and other GitHub. BEAVERTAIL downloads the INVISIBLEFERRET
strategic assets. backdoor, granting UNC5342 extensive endpoint control.
UNC1069, UNC4899, and UNC5342 have adapted their
methodologies to target members of the cryptocurrency Crypto Drainers and Smart-
and blockchain-development community more effectively. Contract Abuse
Specifically, they have come to target developers working
The new technologies and feature sets on which Web3
individually and professionally on Web3-adjacent projects
rely have created novel areas of expansion for threat actor
to obtain illicit access both to the cryptocurrency wallets
techniques. Immutable elements of the blockchain and
of individual users and to the organizations that employ
the decentralized nature of Web3 and cryptocurrency
the impacted developers. UNC4736, on the other hand,
itself have been used by threat actors to create take-
is a prolific actor that targeted the blockchain industry in
down-resistant infrastructure for use during campaigns.
recent years by trojanizing trading software applications.
In traditional architectures, interorganizational cooper-
ation is sufficient to perform takedown activities when
UNC1069
a threat actor campaign is exposed. In 2024, the FBI
UNC1069, active since at least April 2018, targets diverse 48
and the US DOJ dismantled the 911 S5 botnet, which
industries for financial gain. The group uses social engi-
affected millions of endpoints across the globe. However,
neering, often posing as investors from reputable firms on
by including components of Web3 technologies, such
Telegram. UNC1069 has relied on spearphishing and social
as smart contracts, threat actors can ensure that when
engineering to gain initial access and has been observed
a campaign is exposed, their activities can continue to
sending fake meeting invites (sometimes via compromised
operate as takedown activities coordinated over a decen-
Telegram accounts) to Web3 and cryptocurrency
tralized ecosystem can be extremely difficult.
organizations to gain illicit access to digital assets and
cryptocurrency. Smart contracts are an element that can be included in a
blockchain to self-execute upon completion of a config-
UNC4899 ured set of conditions that must be met. Once a smart
contract is executed, the process is irreversibly recorded
UNC4899, a suspected DPRK-nexus threat actor active
in the blockchain. Mandiant has observed threat actors
since 2022, employs sophisticated social engineering and
using malicious smart contracts to steal digital assets
accesses via supply chain compromise. In 2024, UNC4899
and store key malware infrastructure elements within
targeted cryptocurrency professionals on social media
smart contracts.
with job postings for a prominent firm and gained access
to Web3 organizations to steal digital assets. UNC4899
Drainer operations often blend traditional tactics, such
has previously conducted supply chain compromises to
as phishing and social engineering, with malicious smart
likely gain arbitrary access for financial gain.
contracts that execute when a targeted user provides
access to their cryptowallet. By luring users to approve
UNC4736
malicious smart contracts, threat actors transfer the
UNC4736, a sophisticated North Korean threat actor, contents of a user’s cryptowallet to one they control.
conducted a cascading software supply chain attack While the Ethereum network has been the primary target
47
in 2022, compromising a trading software entity and of most drainer operations, Mandiant observed operations
subsequently causing a second supply chain compromise from DPRK-nexus threat actors expand their targeting
that affected at least nine other organizations. This group of Ethereum to include the TRON and Solana blockchain
has relied on trojanized trading and cryptocurrency soft- platforms in 2023 and 2024, respectively. The DPRK-nexus
ware to gain network access for financial gain. UNC4736 threat actor UNC3782 commonly conducts large-scale
also targeted decentralized finance platforms in 2024. phishing campaigns that focus on cryptocurrency indus-
tries. In 2023, UNC3782 conducted phishing operations
UNC5342 against TRON users and transferred more than $137 million
Mandiant began tracking UNC5342 in January 2024, USD worth of assets in a single day. UNC3782 launched
following their social engineering campaign targeting a campaign in 2024 to target Solana users and direct

Mandiant M-Trends 2025 Report 73
them to pages that contained cryptocurrency drainers. Crypto-native organizations in 2024 prioritized technical
Unlike their campaigns in 2023, however, Mandiant has not security for core wallet infrastructure and cryptographic
observed funds in Solana-based cryptocurrency wallets controls, sometimes neglecting other standard controls.
that are controlled by UNC3782, and the page hosting the This focus, combined with rapid development and distrib-
Solana-based drainer was offline as of March 2024. uted workforces, often creates technical debt, expanding
the attack surface. Challenges with evidence availability
More than 1,200 fake sites associated with drainer opera-
and quality, particularly regarding outsourced wallet
tions have been created since January 2024. The financial
infrastructure where log verification is often lacking,
gains found in drainer operations have led to the creation
often hampers investigations. To address these issues,
of drainer-as-a-service (DaaS) providers, who supply 50
Mandiant recommends enhanced transaction data
threat actors with the tools necessary to engage in drainer
monitoring and enrichment, combining with endpoint and
operations. DaaS providers advertise their services on
security telemetry for better malicious activity detection.
underground forums and Telegram and receive a portion
of the assets drained from user wallets as payment.
While the auto-executing nature of smart contracts can
be used as a means to drain a user’s assets in drainer
operations, the immutability of smart contracts also allows
threat actors to host takedown-resistant infrastructure on
the blockchain. UNC5142, a financially motivated
threat cluster tracked by Mandiant, targeted vulnerable
49
WordPress websites and injected code to retrieve
data stored in a malicious smart contract. UNC5142’s
campaign ultimately resulted in the installation of infoste-
aler malware and relied on the presence of the malicious
smart contract, which contained second-stage code to
fetch a payload from a remote server. This process of
storing elements of an attack chain within smart contracts
is commonly referred to as EtherHiding. When used during
a campaign, EtherHiding allows for takedown-resistant
infrastructure that can be updated as long as the smart
contract is not executed and rendered immutable.
Motivated threat actors leverage smart contracts to bypass
traditional takedown measures and redirect their malware
to use new infrastructure when existing infrastructure
is disabled.
Conclusion
The rapid growth of blockchain technology across diverse
industries has opened new avenues for adversaries to
exploit. This includes targeting and manipulating the tech-
nology itself, while also enabling the misuse of cryptocur-
rencies. Ultimately, the nature of decentralized systems,
coupled with a lack of security controls, lowers the
perceived risks for malicious actors and poses challenges
to law enforcement to intervene and react. Underground
and darknet forums also play a role in criminalizing
cryptocurrency by fueling an economy of illegal goods
and services.

Mandiant M-Trends 2025 Report 74
Unsecured Data Repositories
While organizations pour resources into fortifying their perimeters against external threats, many overlook the basic
security hygiene of their internal data repositories. These repositories often hold sensitive information, such as user
credentials, financial data, and intellectual property, that are accessible to employees with standard privileges. This
oversight creates an exploitable attack vector that enables threat actors to escalate privileges, steal data, and disrupt
business operations.
Despite the risks posed by these caches of important data, this issue remains largely overlooked and is overshad-
owed by concerns of more sophisticated attacks. However, as organizations increasingly adopt cloud-based services
and collaborative tools, the attack surface of unsecured repositories expands and further amplifies the risk. As threat
actors target unsecured data repositories, a shift from a perimeter-centric security approach to a data-centric security
approach has become necessary.
Mandiant uses similar tactics in Red Team engagements to model the common methodologies of threat actors. These
engagements allow Mandiant to gain cross-industry security response data, and also bolster client threat defenses. The
following red team and blue team case studies illustrate the efficacy of this attack vector on data repositories.
In cloud-native environments, classic security assessment
The Ripple Effect of Unsecured
TTPs can be less effective as cloud-native architectures
Data: A Red Team Case Study
generally implement stronger authentication and autho-
Mandiant security assessments often identify sensitive rization techniques than typical enterprise environments.
data residing in readily accessible document repositories. Cloud environments that use a zero-trust model can also
Network file shares, SharePoint sites, Jira instances, be more challenging to navigate for a threat actor as
Confluence spaces, and GitHub repositories often systems may be segregated into isolated virtual local area
contain a wealth of valuable information (e.g., credentials, networks (VLANs). In addition, because cloud providers
privateckeys, financial documents, personally identifiable often maintain the underlying infrastructure and are more
information [PII], and intellectual property). This data, rigorous in their patching schedules, impactful vulnerabili-
typically accessible to employees with standard ties are often managed better within cloud-native environ-
privileges, presents a significant security risk that many ments than their on-premises counterparts.
organizations fail to recognize.
As part of their reconnaissance efforts for the engage-
During Red Team engagements, Mandiant emulates ment, Mandiant generated a comprehensive list of docu-
advanced threat actors by performing custom and widely ment repositories that were accessible to the average
known tactics, techniques, and procedures (TTPs) in an employee. Mandiant identified a highly varied collection of
attempt to compromise organizational data and achieve data stores that allowed broad access, regardless of job
engagement objectives. Mandiant consultants take inspi- role or group membership. Among the list, the customer’s
ration from observed threat actor activity to recreate the SharePoint document store and GitHub Enterprise repos-
strategies that threat actors use during intrusions. itories were prioritized for further analysis. SharePoint
and GitHub are both widely adopted across many indus-
Mandiant was tasked by a customer to evaluate the
tries and organizations. Both platforms allow users to
security of a specific, cloud-native architecture backed
store arbitrary files, which are often used to support a
by a massive data lake storing customer information. The
diverse set of operations within an organization. Due to
customer detailed a set of objectives, which included
the often broad use case for these data stores, the data
successfully accessing specific data stores and
itself commonly outpaces the permissions that are applied
compromising administrative systems. For the purpose
to them. This can result in misconfigurations that allow
of this project, Mandiant was provided with standard
for broader access than originally intended. Mandiant
employee credentials that could be used to access the
has observed that regular reviews of data stores, the
customer environment remotely.

Mandiant M-Trends 2025 Report 75
classifications of the data they contain, and subsequent present a valuable target to motivated threat actors,
review of access controls to match the classification are regardless of the mission objective. Mandiant tracks
commonly overlooked steps in a security program. the motivations of thousands of threat actors identified
through incident response engagements and intelligence-
Both SharePoint and GitHub provide built-in search func-
gathering operations. Mandiant has observed financially
tionality that allows for fine-grained querying, including
motivated threat actors, such as FIN11, UNC2891, and
the ability to filter keywords and file types. Mandiant inci-
UNC3944, steal data from unsecured data repositories on
dent responders regularly identify threat actors querying
which they can build high-price extortion demands from
data repositories for file types likely to aid the attacker
targeted organizations. On the other end of the spectrum,
in various stages of the targeted attack lifecycle. Files
Mandiant has observed advanced persistent threat (APT)
ending in .pem or .key commonly store private keys that
groups such as APT29, a threat actor attributed to Russia’s
threat actors can use to access remote systems. Queries
Foreign Intelligence Service, steal data from information
for filenames matching common Secure Shell (SSH)
stores in pursuit of espionage objectives.
private key filenames, or even simple queries for files that
include the word “password,” have often been identified While unsecured data repositories are often overlooked
in browser search histories and application logs during by security teams, threat actors have recognized their
an investigation. inherent value as both a potential windfall for operational
objectives and a cache of intel on their target environment.
A series of searches through the identified repositories
As such, threat actors across all levels of sophistication
led Mandiant to SSH private keys, application secrets, and
are likely to find factors that can drive the success of
user passwords that were stored in plain text with minimal
their operations. Depending on organizational needs,
access controls. By combining the stored secrets identi-
centralized data repositories may house critical informa-
fied in GitHub with the SSH private keys from SharePoint,
tion pertaining to day-to-day business operations. Data
Mandiant was able to initiate a chain of lateral movement
repositories often grow over time to contain more and
through the customer environment. With each system that
more sensitive data as the use of the repository outstrips
Mandiant moved to, further searches and reconnaissance
the original data classification against which the access
through technical documentation, password vaults, and
controls were defined. Similarly, data lifecycle manage-
credentials stored within a variety of virtual machines
ment processes are often deprioritized by operational
allowed Mandiant to progress one system closer to the
teams, which results in organizations keeping data long
objectives laid out by the customer. Network documen-
past the business case under which the repository was
tation identified in SharePoint was used as a navigation
originally established. Insufficiently safeguarding repos-
plane through which Mandiant tested credentials pulled
itories that contain sensitive data inherently lowers the
from corporate password vaults. Identities that were
level of effort required for threat actors to pursue their
compromised during each lateral move were subsequently
mission objectives.
used to access different sets of document stores, which
fed into the cyclical process of identification, testing, Financially motivated threat groups have historically
and actioning. Mandiant continued to compromise relied on disruption of service through ransomware as
systems within the environment until user credentials a means to apply pressure to targeted organizations,
yielded access to privileged credentials, which then led to with offers of relief available after a substantial payout.
administrative credentials. Ultimately, Mandiant was able Over the years, organizations recognized the threat to
to engineer a path to the mission objectives by esca- their continued operation presented by ransomware and
lating their privileges to an administrator level and gaining invested in technology such as early warning systems
access to sensitive data stores. Mandiant performed and disaster recovery to ensure they could return to an
this attack chain without the use of malware, zero-day active state without an exorbitant payout. More recently,
vulnerabilities, or any other more advanced attacker threat actors have responded in kind by adding a more
methodologies. material extortion to the mix. Instead of smash-and-
grab ransomware operations where the time to encryp-
tion was made a priority, threat groups such as FIN11,
Exploitation in the Wild: An
UNC2891, and UNC3944 have progressed and prioritized
Incident Responder’s View selective data theft prior to encryption. The release of
Due to the nature of the information commonly stored sensitive data stolen from the targeted organization is
in centralized data repositories, these repositories often then used as additional leverage during the negotiation

Mandiant M-Trends 2025 Report 76
for the decryption of the environment. Mandiant has security models encountered, findings regarding basic
even observed threat actors such as UNC3944 request security hygiene tend not to cluster so dramatically.
follow-on payments to ensure stolen data is not leaked
While the traditional model of looking at a corporate
once payment has been made to decrypt the environment.
computer network from the perspective of its perimeter
However, the direct impact of stolen data is not always and component systems has been valuable, augmenting
as obvious when a threat actor is concerned more with that view with a layer for data residency and controls can
espionage than with financial gain. APT29 is highly sophis- help build more robust models. Focusing on where data
ticated and known for persistence in maintaining access resides—whether on-premises, in the cloud, or in separate
to compromised environments, even after activity has software-as-a-service applications—should be a focal
been identified. As their remit is commonly more targeted point for security teams. Given the data-centric nature
toward the acquisition of valuable intelligence, targeting of modern organizations, this task is not a trivial one and
unsecured repositories that may contain sensitive data is involves a multitiered approach:
a natural step for APT29, which can provide an abbrevi-
1. Perform inventory of data repositories: Begin by
ated path toward their mission objectives. Mandiant has
pinpointing where sensitive data resides. This includes
observed APT29 steal data on targeted personnel and
PII, financial records, corporate secrets, IT data, intel-
critical infrastructure from data repositories where the
lectual property, and anything subject to regulatory
level of protection did not match the classification of the
compliance (e.g., GDPR, HIPAA, etc.).
data. Even in cases where the stolen dataset does not
meet a threat actor’s objectives, Mandiant has observed
2. Routinely audit data repositories: Data repositories
threat actors pursue data that simply aligns with the prog-
should be routinely audited with automated tools to
ress of their intrusion.
identify exposed credentials and secrets.
The ongoing support requirements of an organization’s
3. Implement robust access controls: Blanket permis-
business and operational needs often rely on the quality
sions are a commonly abused vector through which
and quantity of a set of well-maintained documentation.
threat actors gain access to sensitive data. Ensure
From network diagrams and troubleshooting guides, to
users have only the minimum accesses to data
full incident playbooks and application design documents,
necessary to perform their jobs. Similarly, distinguish
these stores of information, by necessity, exist to ensure
between users who require read access and those
the organization runs smoothly. Unfortunately, they also
who require read/write access.
represent an added risk of information exposure, which
threat actors rely on during the targeted attack lifecycle. 4. Educate users: Educate users about data security
Where manual reconnaissance of an environment can be best practices, the importance of protecting sensi-
noisy and risk exposing a threat actor’s activity, manually tive data, and the consequences of data breaches.
reviewing network architecture documentation can Employees should be trained to identify and report
provide the same if not better information to a threat instances of sensitive data in open data repositories
actor. UNC2891, known for targeting environments with or secrets stored in code bases.
Linux and Solaris systems, has been observed using data
5. Validate data is encrypted: Encrypt data both in
from unsecured repositories to inform lateral movement
transit using protocols such as TLS/SSL and at rest to
in targeted networks. Similarly, Mandiant has observed
limit windows of exposure.
APT29 steal information on systems of interest prior to
moving laterally and compromising them. 6. Configure multifactor authentication (MFA):
Enforcing MFA for all accesses to sensitive data
repositories adds an extra layer of security beyond
Shifting to a Data-Centric
passwords. For single sign-on (SSO)-based data
Approach: Defensive Strategies
repositories, ensure MFA is enforced when accessing
and Recommendations SSO resources.
A review of recent security assessments performed by
7. Implement data loss prevention (DLP): Consider
Mandiant revealed that roughly 46% of the engagements
implementing DLP solutions to prevent sensitive data
identified insecure storage of credentials or secrets as a
from leaving your environment through observable
risk factor. Given the diverse nature of the environments
network sessions such as email attachments or
into which Mandiant is contracted and the breadth of
file transfers.

Mandiant M-Trends 2025 Report 77
8. Regularly audit the content of data repositories:
Conclusion
Review data repositories to ensure their contents
match the classification of the original use case. Any The presence of sensitive data within unsecured docu-
sensitive data identified outside of secured containers ment repositories is pervasive and represents a signifi-
should be logged, removed, and necessitate the start cant yet often overlooked security risk. Despite investing
of a full search for similar data outside of secured heavily in perimeter defenses, improper controls applied
locations. Data that is no longer needed for business to internal data stores can leave organizations and their
purposes should be removed to keep the organi- data vulnerable to exploitation. Addressing and subse-
zation’s data footprint within a manageable size. quently maintaining solutions to vulnerabilities in an envi-
Automated tools can be used to facilitate data foot- ronment helps reduce an organization’s exposure to risk
print reduction and track down sensitive files and provides a firm baseline of security on which further
of interest. advancements can be built.
9. Implement zero trust and microsegmentation: By Expanding an organization’s security measures to include
adapting a zero-trust model in addition to microsegmen- the data that drives its success strengthens its existing
tation, leaked credentials become significantly harder security systems. While the perimeter of an environ-
to abuse. Internal firewalls, context-aware access, and ment may often represent the first chance to detect and
zero trust-based authentication all act as methods to inhibit threat actor activity, the systems that collect an
restrict connectivity to a resource even if valid organization’s data can represent the last opportunity
credentials are obtained. defenders have to prevent data theft. Placing barriers
between threat actors or insider threats and sensitive
10. Perform dynamic secret management: Tools that data managed by an organization not only limits access
provision just-in-time access to secrets along with but adds opportunities through which security teams
automated rotation after use, reduce the opportunities can detect misuse. Comprehensive access controls,
for a threat actor to misuse stolen credentials. Even continuous monitoring, data tagging, and regular audits
if a credential is leaked, a dynamic secret manage- of repositories should form the starting point and inform
ment system should limit the impact by automatically the growth of a data-centric environment. By priori-
rotating the credential and expiring active sessions. tizing data security across all platforms and cultivating a
This technique also reduces administrative security-conscious culture, organizations can strengthen
overhead along with providing detailed tracking of their overall security posture and better safeguard their
credential usage. valuable assets.
11. Integrate CI/CD pipelines with dynamic secret
management systems: As software and systems are
built and maintained, integrating continuous inte-
gration and continuous delivery/deployment (CI/CD)
pipelines with dynamic secret management systems
provides an opportunity to rotate credentials as
infrastructure and assets move from development
to production. Credentials for active, live systems
with production data could be automatically rotated
as code and configurations change, lessening the
chance that a leaked credential remains valid.
12. Perform regular security assessments: Recurrent
and regular security assessments help determine
the impact and overall exploitability of any identified
credentials. These tests also highlight how closely an
organization follows their intended process, gaining
a ground truth assessment of security control’s
effectiveness.

SPECIAL REPORT: MANDIANT M-TRENDS 2023 78
Conclusion O
G
R
A
B
M
E

Mandiant M-Trends 2025 Report 79
In 2024, we saw attackers take advantage of covers all aspects of the enterprise, from cloud
opportunities. This includes leveraging creden- and on-premises environments to IT/OT systems
tials obtained in infostealer campaigns for initial and all assets, that is powered by strong detec-
access, taking advantage of misconfigurations tion and proactive threat hunting capabilities, and
and weakly secured identities in hybrid environ- informed by impactful threat intelligence. And of
ments, gaining access to data as a result of poor course, employee education is a must.
basic security hygiene, and targeting cryptocur-
The Mandiant mission is to help keep every orga-
rency and Web3 amidst its rapid adoption.
nization secure from cyber threats and confident
We also saw threat actors create opportunities, in their readiness. Our annual M-Trends report,
as seen with the Democratic People’s Republic of featuring data and learnings from our engage-
Korea IT workers. These actors are brazen in their ments, plays a big part in advancing that mission.
approach, notably targeting gaps in onboarding We will continue to share our frontline knowledge
processes to obtain employment through decep- in M-Trends to improve our collective security
tive means, and ultimately achieving their goals of awareness, understanding, and capabilities.
funding the regime while also maintaining insider
access to an organization.
Defending against the threats covered in
M-Trends 2025 is no easy task. Effective cyber
defense requires an extensive and multi-layered Mandiant, part of Google Cloud, has been at the
forefront of cyber security and threat intelligence
approach. Security teams must be rigorously
since 2004. Our incident responders are on the
tested through red team exercises and other
frontlines of the world’s most complex breaches.
simulations. Security teams should partner with
We have a deep understanding of both existing
Communications, Legal, and other relevant teams and emerging threat actors, as well as their rapidly
to conduct regular tabletop exercises to validate changing tactics, techniques, and procedures.
and improve incident response plans throughout Mandiant helps organizations quickly get back to
business after a security breach and applies front-
the year. A cyber incident response retainer
line expertise to guide effective threat detection,
ensures immediate access to expert help, mini-
preparation, and to reduce business risk and build
mizing downtime and damage during a critical
overall resiliency—before, during, and after an
cyberattack.
incident. Since 2010, Mandiant has been dedicated
to publishing comprehensive trends based on our
Exploits (33%), stolen credentials (16%), and
incident response engagements, providing critical
phishing (14%) were the most common initial insights into the evolving threat landscape through
infection vectors in our 2024 investigations. the M-Trends report.
Foundational security practices, such as vulner-
If your organization suspects a cyber incident, or
ability management, least privilege, and system
you are experiencing a security breach, please
hardening, are essential. Organizations should contact Mandiant for Incident Response Assistance.
build a comprehensive security program that

Appendix: Mandiant M-Trends 2025 Report 80
MITRE
|   ATT&CK |     |     | Techniques Related to   |     |
| -------- | --- | --- | ----------------------- | --- |
Mandiant Targeted
Mandiant’s Targeted Attack Lifecycle is
the predictable sequence of events cyber  Attack Lifecycle, 2024
attackers use to carry out their attacks.
Initial Reconnaissance
Reconnaissance
cloud_icon_font
|        i ndicates  | T1598: Phishing for Information   |                                | 1.3% |                 |
| ------------------ | --------------------------------- | ------------------------------ | ---- | --------------- |
| techniques         |                                   | cloud_icon_fonttnof_noci_duolc |      | cloud_icon_font |
T1595: Active Scanning   0.6% T1595.002: Vulnerability Scanning   0.6%
in the Cloud
matrix, intro-
duced in
ATT&CK v16.
Resource Development
|     |     | cloud_icon_font |     | cloud_icon_font |
| --- | --- | --------------- | --- | --------------- |
T1588: Obtain Capabilities   15.4% T1588.003: Code Signing Certificates   14.8%
cloud_icon_font
T1588.004: Digital Certificates   0.4%
cloud_icon_font
T1588.007: Artificial Intelligence   0.2%
|     |     | cloud_icon_font | cloud_icon_font |     |
| --- | --- | --------------- | --------------- | --- |
T1608: Stage Capabilities   12.3% T1608.005: Link Target   3.8%
cloud_icon_font
T1608.003: Install Digital Certificate   3.2%
cloud_icon_font
T1608.001: Upload Malware   1.7%
f_noci_duolc
T1608.006: SEO Poisoning   1.3%
cloud_icon_font
T1608.002: Upload Tool   1.3%
cloud_icon_font
T1608.004: Drive-by Target   0.6%
cloud_icon_font
|     | T1584: Compromise Infrastructure   |                 | 4.4% |                 |
| --- | ---------------------------------- | --------------- | ---- | --------------- |
|     |                                    | cloud_icon_font |      | cloud_icon_font |
4.0% 4.0%
T1583: Acquire Infrastructure   T1583.003: Virtual Private Server
|     |     | cloud_icon_font |     | cloud_icon_font |
| --- | --- | --------------- | --- | --------------- |
T1587: Develop Capabilities   0.2% T1587.003: Digital Certificates   0.2%
|     |     | cloud_icon_font | cloud_icon_font |     |
| --- | --- | --------------- | --------------- | --- |
T1585: Establish Accounts   0.2% T1585.002: Email Accounts   0.2%

Appendix: Mandiant M-Trends 2025 Report 81
Initial Compromise
Initial Access
cloud_icon_font
| T1190: Exploit Public-Facing Application   | 23.5% |     |
| ------------------------------------------ | ----- | --- |
cloud_icon_font
| T1133: External Remote Services   | 20.9% |     |
| --------------------------------- | ----- | --- |
cloud_icon_font cloud_icon_font
T1078: Valid Accounts   19.5% T1078.004: Cloud Accounts   12.1%%
cloud_icon_font cloud_icon_font
| T1566: Phishing   | 12.3% T1566.002: Spearphishing Link   | 5.5% |
| ----------------- | ------------------------------------- | ---- |
|                   | T1566.001: Spearphishing Attachment   | 1.7% |
cloud_icon_font
|     | T1566.004: Spearphishing Voice       | 1.5% |
| --- | ------------------------------------ | ---- |
|     | T1566.003: Spearphishing via Service | 1.3% |
cloud_icon_font
4.4%
T1189: Drive-by Compromise
cloud_icon_font
| T1199: Trusted Relationship                | 0.8% |     |
| ------------------------------------------ | ---- | --- |
| T1091: Replication Through Removable Media | 0.4% |     |
T1195: Supply Chain Compromise 0.2% T1195.002: Compromise Software Supply Chain 0.2%
| T1200: Hardware Additions | 0.2% |     |
| ------------------------- | ---- | --- |

Appendix: Mandiant M-Trends 2025 Report 82
Establish Foothold
Persistence
cloud_icon_font
| T1133: External Remote Services   | 20.9% |     |
| --------------------------------- | ----- | --- |
cloud_icon_font cloud_icon_font
T1078: Valid Accounts   19.5% T1078.004: Cloud Accounts   12.1%
T1543: Create or Modify System Process 19.2% T1543.003: Windows Service 11.0%
|     | T1543.004: Launch Daemon   | 0.4% |
| --- | -------------------------- | ---- |
|     | T1543.002: Systemd Service | 0.2% |
cloud_icon_font
T1098: Account Manipulation   18.6% T1098.007: Additional Local or Domain Groups 6.3%
cloud_icon_font
|     | T1098.005: Device Registration   | 4.7% |
| --- | -------------------------------- | ---- |
|     | T1098.004: SSH Authorized Keys   | 1.5% |
cloud_icon_font
|     | T1098.001: Additional Cloud Credentials   | 0.2% |
| --- | ----------------------------------------- | ---- |
cloud_icon_font
|     | T1098.003: Additional Cloud Roles   | 0.2% |
| --- | ----------------------------------- | ---- |
cloud_icon_font
|     | T1098.006: Additional Container Cluster Roles   | 0.2% |
| --- | ----------------------------------------------- | ---- |
cloud_icon_font
T1053: Scheduled Task/Job   13.5% T1053.005: Scheduled Task 12.7%
|     | T1053.003: Cron | 0.8% |
| --- | --------------- | ---- |
T1547: Boot or Logon Autostart Execution 11.0% T1547.001: Registry Run Keys / Startup Folder 10.8%
|     | T1547.005: Security Support Provider | 0.8% |
| --- | ------------------------------------ | ---- |
|     | T1547.009: Shortcut Modification     | 0.6% |
|     | T1547.002: Authentication Package    | 0.2% |
T1505: Server Software Component 7.0% T1505.003: Web Shell 7.0%
|     | T1505.004: IIS Components | 0.2% |
| --- | ------------------------- | ---- |
cloud_icon_font
| T1136: Create Account   | 6.6% T1136.001: Local Account | 4.4% |
| ----------------------- | ----------------------------- | ---- |
|                         | T1136.002: Domain Account     | 0.2% |
T1574: Hijack Execution Flow 6.3% T1574.011 Services Registry Permissions Weakness 5.5%
|     | T1574.002: DLL Side-Loading           | 0.8% |
| --- | ------------------------------------- | ---- |
|     | T1574.001: DLL Search Order Hijacking | 0.2% |
T1546: Event Triggered Execution 3.6% T1546.003: WMI Event Subscription 2.5%
|     | T1546.008: Accessibility Features                 | 0.2% |
| --- | ------------------------------------------------- | ---- |
|     | T1546.004: Unix Shell Configuration Modification  | 0.2% |
|     | T1546.015: Component Object Model Hijacking       | 0.2% |
|     | T1546.012: Image File Execution Options Injection | 0.2% |
| tno | t                                                 |      |
T1556: Modify Authentication Proces 2.1% T1556.006: Multi-Factor Authentication 1.1%
cloud_icon_font
|     | T1556.009: Conditional Access Policies   | 0.4% |
| --- | ---------------------------------------- | ---- |
T1037: Boot or Logon Initialization Scripts 0.8% T1037.001: Logon Script (Windows) 0.2%
| T1554: Compromise Client Software Binary | 0.4% |     |
| ---------------------------------------- | ---- | --- |
cloud_icon_font cloud_icon_font
T1137: Office Application Startup   0.2% T1137.006: Add-ins   0.2%

Appendix: Mandiant M-Trends 2025 Report 83
Escalate Privileges
Privilege Escalation
cloud_icon_font cloud_icon_font
T1078: Valid Accounts 19.5% T1078.004: Cloud Accounts 12.1%
T1543: Create or Modify System Process 19.2% T1543.003: Windows Service 11.0%
T1543.004: Launch Daemon 0.4%
T1543.002: Systemd Service 0.2%
T1098: Account Manipulation 18.6% T1098.007: Additional Local or Domain Groups 6.3%
cloud_icon_font
T1098.006: Additional Container Cluster Roles 0.2%
T1055: Process Injection 15.0% T1055.001: Dynamic-link Library Injection 0.6%
T1055.003: Thread Execution Hijacking 0.6%
T1055.012: Process Hollowing 0.4%
T1055.004: Asynchronous Procedure Call 0.2%
T1055.009: Proc Memory 0.2%
T1055.002: Portable Executable Injection 0.2%
cloud_icon_font
T1053: Scheduled Task/Job 13.5% T1053.005: Scheduled Task 12.7%
T1053.003: Cron 0.8%
T1547: Boot or Logon Autostart Execution 11.0% T1547.001: Registry Run Keys / Startup Folder 10.8%
T1547.005: Security Support Provider 0.8%
T1547.009: Shortcut Modification 0.6%
T1547.002: Authentication Package 0.2%
T1134: Access Token Manipulation 7.6% T1134.001: Token Impersonation/Theft 2.7%
T1574: Hijack Execution Flow 6.3% T1574.011: Services Registry Permissions Weakness 5.5%
T1574.002: DLL Side-Loading 0.8%
T1574.001: DLL Search Order Hijacking 0.2%
T1546: Event Triggered Execution 3.6% T1546.003: WMI Event Subscription 2.5%
T1546.004: Unix Shell Configuration Modification 0.2%
T1546.015: Component Object Model Hijacking 0.2%
T1546.012: Image File Execution Options Injection 0.2%
T1546.008: Accessibility Features 0.2%
T1037: Boot or Logon Initialization Scripts 0.8% T1037.001: Logon Script (Windows) 0.2%
cloud_icon_font
T1484: Domain Policy Modification 0.8% T1484.001: Group Policy Modification 0.8%
cloud_icon_font
T1068: Exploitation for Privilege Escalation 0.4%
T1548: Abuse Elevation Control Mechanism 0.2% T1548.002: Bypass User Account Control 0.2%

Appendix: Mandiant M-Trends 2025 Report 84
Internal Reconnaissance
Discovery
T1083: File and Directory Discovery 32.1%
cloud_icon_font
T1082: System Information Discovery 24.5%
toci_duolc
T1033: System Owner/User Discovery 20.3%
cloud_icon_font
T1087: Account Discovery 18.2% T1087.002: Domain Account 8.2%
T1087.001: Local Account 7.2%
cloud_icon_font
T1087.004: Cloud Account 0.4%
T1016: System Network Configuration Discovery 17.5% T1016.001: Internet Connection Discovery 9.9%
cloud_icon_font cloud_icon_font
T1518: Software Discovery 16.7% T1518.001: Security Software Discovery 0.6%
T1057: Process Discovery 16.7%
T1012: Query Registry 15.0%
T1622: Debugger Evasion 10.8%
T1614: System Location Discovery 9.5% T1614.001: System Language Discovery 4.9%
cloud_icon_font
T1069: Permission Groups Discovery 9.1% T1069.002: Domain Groups 6.1%
T1069.001: Local Groups 1.3%
cloud_icon_font
T1069.003: Cloud Groups 0.6%
T1497: Virtualization/Sandbox Evasion 9.1% T1497.001: System Checks 7.2%
T1482: Domain Trust Discovery 8.0%
cloud_icon_font
T1049: System Network Connections Discovery 6.1%
T1010: Application Window Discovery 5.5%
T1007: System Service Discovery 5.3%
T1018: Remote System Discovery 4.9%
T1135: Network Share Discovery 3.8%
cloud_icon_font
T1046: Network Service Discovery 2.3%
T1124: System Time Discovery 1.3%
cloud_icon_font
T1580: Cloud Infrastructure Discovery 1.1%
T1619: Cloud Storage Object Discovery 0.8%
T1615: Group Policy Discovery 0.6%
cloud_icon_font
T1538: Cloud Service Dashboard 0.6%
T1654: Log Enumeration 0.4%
T1217: Browser Bookmark Discovery 0.2%
T1201: Password Policy Discovery 0.2%
T1120: Peripheral Device Discovery 0.2%
cloud_icon_font
T1613: Container and Resource Discovery 0.2%
T1040: Network Sniffing 0.2%
T1652: Device Driver Discovery 0.2%

Appendix: Mandiant M-Trends 2025 Report 85
Lateral Movement
Lateral Movement
T1021: Remote Services 33.2% T1021.002: SMB/Windows Admin Shares 21.8%
T1021.001: Remote Desktop Protocol 21.1%
T1021.004: SSH 12.3%
T1021.006: Windows Remote Management 1.3%
T1021.005: VNC 1.1%
T1570: Lateral Tool Transfer 1.3%
cloud_icon_font
T1550: Use Alternate Authentication Material 1.3% T1550.002: Pass the Hash 1.1%
cloud_icon_font
T1550.001: Application Access Token 0.2%
cloud_icon_font
T1534: Internal Spearphishing 0.6%
T1072: Software Deployment Tools 0.4%
T1091: Replication Through Removable Media 0.4%
T1210: Exploitation of Remote Services 0.2%

Appendix: Mandiant M-Trends 2025 Report 86
Maintain Presence
Persistence
cloud_icon_font
| T1133: External Remote Services   | 20.9% |     |
| --------------------------------- | ----- | --- |
cloud_icon_font cloud_icon_font
T1078: Valid Accounts   19.5% T1078.004: Cloud Accounts   12.1%
T1543: Create or Modify System Process 19.2% T1543.003: Windows Service 11.0%
|     | T1543.004: Launch Daemon   | 0.4% |
| --- | -------------------------- | ---- |
|     | T1543.002: Systemd Service | 0.2% |
cloud_icon_fontnof_noci_duolc
T1098: Account Manipulation     18.6% T1098.007: Additional Local or Domain Groups 6.3%
cloud_icon_font
|     | T1098.005: Device Registration   | 4.7% |
| --- | -------------------------------- | ---- |
|     | T1098.004: SSH Authorized Keys   | 1.5% |
cloud_icon_font
|     | T1098.001: Additional Cloud Credentials   | 0.2% |
| --- | ----------------------------------------- | ---- |
cloud_icon_font
|     | T1098.003: Additional Cloud Roles   | 0.2% |
| --- | ----------------------------------- | ---- |
cloud_icon_font
|     | T1098.006: Additional Container Cluster Roles   | 0.2% |
| --- | ----------------------------------------------- | ---- |
cloud_icon_font
T1053: Scheduled Task/Job   13.5% T1053.005: Scheduled Task 12.7%
|     | T1053.003: Cron | 0.8% |
| --- | --------------- | ---- |
T1547: Boot or Logon Autostart Execution 11.0% T1547.001: Registry Run Keys/Startup Folder 10.8%
|     | T1547.005: Security Support Provider | 0.8% |
| --- | ------------------------------------ | ---- |
|     | T1547.009: Shortcut Modification     | 0.6% |
|     | T1547.002: Authentication Package    | 0.2% |
T1505: Server Software Component 7.0% T1505.003: Web Shell 7.0%
|     | T1505.004: IIS Component | 0.2% |
| --- | ------------------------ | ---- |
cloud_icon_font
| T1136: Create Account   | 6.6% T1136.001: Local Account | 4.4% |
| ----------------------- | ----------------------------- | ---- |
|                         | T1136.002: Domain Account     | 0.2% |
T1574: Hijack Execution Flow 6.3% T1574.011: Services Registry Permissions Weakness 5.5%
|     | T1574.002: DLL Side-Loading           | 0.8% |
| --- | ------------------------------------- | ---- |
|     | T1574.001: DLL Search Order Hijacking | 0.2% |
T1546: Event Triggered Execution 3.6% T1546.003: WMI Event Subscription 2.5%
|     | T1546.008: Accessibility Features                 | 0.2% |
| --- | ------------------------------------------------- | ---- |
|     | T1546.004: Unix Shell Configuration Modification  | 0.2% |
|     | T1546.015: Component Object Model Hijacking       | 0.2% |
|     | T1546.012: Image File Execution Options Injection | 0.2% |
cloud_icon_font
T1556: Modify Authentication Process 2.1% T1556.006: Multi-Factor Authentication   1.1%
cloud_icon_font
|     | T1556.009: Conditional Access Policies   | 0.4% |
| --- | ---------------------------------------- | ---- |
T1037: Boot or Logon Initialization Scripts 0.8% T1037.001: Logon Script (Windows) 0.2%
| T1554: Compromise Client Software Binary | 0.4% |     |
| ---------------------------------------- | ---- | --- |
cloud_icon_font cloud_icon_font
T1137: Office Application Startup   0.2% T1137.006: Add-ins   0.2%

Appendix: Mandiant M-Trends 2025 Report 87
Mission Completion
Collection
T1560: Archive Collected Data 12.9% T1560.001: Archive via Utility 6.3%
|                 | T1560.002: Archive via Library |                 | 0.8% |
| --------------- | ------------------------------ | --------------- | ---- |
| cloud_icon_font |                                | cloud_icon_font |      |
T1213: Data from Information Repositories   12.3% T1213.002: Sharepoint   7.6%
cloud_icon_font
|     | T1213.003: Code Repositories   |     | 0.4% |
| --- | ------------------------------ | --- | ---- |
cloud_icon_font
|     | T1213.001: Confluence   |     | 0.2% |
| --- | ----------------------- | --- | ---- |
cloud_icon_font cloud_icon_font
T1114: Email Collection   7.4% T1114.002: Remote Email Collection   0.6%
cloud_icon_fontof_noci_duolc
|     | T1114.003: Email Forwarding Rule   |     | 0.6% |
| --- | ---------------------------------- | --- | ---- |
|     | T1114.001: Local Email Collection  |     | 0.2% |
cloud_icon_font
T1074: Data Staged   6.1% T1074.001: Local Data Staging   5.3%
cloud_icon_font
|     | T1074.002: Remote Data Staging   |     | 0.6% |
| --- | -------------------------------- | --- | ---- |
cloud_icon_font cloud_icon_font
| T1056: Input Capture                  | 3.8% T1056.001: Keylogging   |                 | 3.8% |
| ------------------------------------- | ---------------------------- | --------------- | ---- |
| T1113: Screen Capture                 | 3.4%                         |                 |      |
| T1039: Data from Network Shared Drive | 2.3%                         |                 |      |
| T1115: Clipboard Data                 | 2.1%                         |                 |      |
| T1005: Data from Local System         | 1.5%                         |                 |      |
| T1125: Video Capture                  | 1.5%                         |                 |      |
| cloud_icon_font                       |                              | cloud_icon_font |      |
|                                       | 1.1%                         |                 | 0.2% |
T1602: Data from Configuration Repository   T1602.001: SNMP (MIB Dump)
cloud_icon_font
|     | T1602.002: Network Device Configuration Dump   |     | 1.1% |
| --- | ---------------------------------------------- | --- | ---- |
cloud_icon_font
| T1530: Data from Cloud Storage   | 0.6% |     |     |
| -------------------------------- | ---- | --- | --- |
| T1123: Audio Capture             | 0.6% |     |     |
| T1119: Automated Collection      | 0.2% |     |     |

Appendix: Mandiant M-Trends 2025 Report 88
Mission Completion
Exfiltration
T1567: Exfiltration Over Web Service 2.7% T1567.002: Exfiltration to Cloud Storage 1.5%
T1567.001: Exfiltration to Code Repository 0.4%
T1041: Exfiltration Over C2 Channel 1.1%
cloud_icon_font
T1020: Automated Exfiltration 0.4%
Impact
cloud_icon_font
T1486: Data Encrypted for Impact 24.1%
T1657: Financial Theft 10.8%
T1489: Service Stop 8.5%
T1529: System Shutdown/Reboot 5.9%
T1490: Inhibit System Recovery 4.9%
T1565: Data Manipulation 4.4% T1565.001: Stored Data Manipulation 4.4%
cloud_icon_font
T1485: Data Destruction 3.2%
cloud_icon_font
T1496: Resource Hijacking 3.0%
cloud_icon_font cloud_icon_font
TT1491: Defacement 1.3% T1491.002: External Defacement 0.8%

Appendix: Mandiant M-Trends 2025 Report 89
Other
Command and Control
T1071: Application Layer Protocol 21.4% T1071.001: Web Protocols 16.9%
|                              | T1071.004: DNS | 4.9% |
| ---------------------------- | -------------- | ---- |
| T1105: Ingress Tool Transfer | 20.9%          |      |
cloud_icon_font
| T1095: Non-Application Layer Protocol   | 18.0% |     |
| --------------------------------------- | ----- | --- |
| T1572: Protocol Tunneling               | 8.7%  |     |
T1573: Encrypted Channel 5.9% T1573.002: Asymmetric Cryptography 5.7%
|     | T1573.001: Symmetric Cryptography | 0.2% |
| --- | --------------------------------- | ---- |
cloud_icon_font cloud_icon_font
| T1090: Proxy                  | 3.6% T1090.003: Multi-hop Proxy   | 1.5% |
| ----------------------------- | --------------------------------- | ---- |
|                               | T1090.001: Internal Proxy         | 0.6% |
| T1219: Remote Access Software | 2.3%                              |      |
T1102: Web Service 1.3% T1102.002: Bidirectional Communication 0.2%
| T1132: Data Encoding        | 0.8% T1132.001: Standard Encoding | 0.8% |
| --------------------------- | --------------------------------- | ---- |
| T1571: Non-Standard Port    | 0.6%                              |      |
| T1008: Fallback Channels    | 0.2%                              |      |
| T1104: Multi-Stage Channels | 0.2%                              |      |
Execution
cloud_icon_font
T1059: Command and Scripting Interpreter   42.7% T1059.001: PowerShell 24.5%
|     | T1059.003: Windows Command Shell | 15.0% |
| --- | -------------------------------- | ----- |
|     | T1059.004: Unix Shell            | 4.2%  |
|     | T1059.006: Python                | 3.4%  |
|     | T1059.007: JavaScript            | 1.5%  |
cloud_icon_font
|     | T1059.009: Cloud API           | 0.6% |
| --- | ------------------------------ | ---- |
|     | T1059.010: AutoHotKey & AutoIT | 0.6% |
|     | T1059.005: Visual Basic        | 0.2% |
|     | T1059.002: AppleScript         | 0.2% |
cloud_icon_font
|     | T1059.011: Lua   | 0.2% |
| --- | ---------------- | ---- |
T1569: System Services 17.8% T1569.002: Service Execution 17.8%
cloud_icon_font
T1053: Scheduled Task/Job   13.5% T1053.005: Scheduled Task 12.7%
|     | T1053.003: Cron | 0.8% |
| --- | --------------- | ---- |
cloud_icon_font
|     | 10.4% T1204.002: Malicious File | 6.8% |
| --- | ------------------------------- | ---- |
T1204: User Execution
|                                           | T1204.001: Malicious Link | 3.6% |
| ----------------------------------------- | ------------------------- | ---- |
| T1047: Windows Management Instrumentation | 6.3%                      |      |
| T1559: Inter-Process Communication        | 0.8%                      |      |
| T1203: Exploitation for Client Execution  | 0.4%                      |      |
| T1072: Software Deployment Tools          | 0.4%                      |      |
| T1129: Shared Modules                     | 0.2%                      |      |

Mandiant M-Trends 2025 Report 90
Bibliography
1. https://www.mandiant.com/resources/blog/attacker-visibility-threat-campaigns
2. https://cloud.google.com/blog/topics/threat-intelligence/analyzing-dark-crystal-rat-backdoor/
3. https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Year_in_Review_of_ZeroDays.pdf
4. https://cloud.google.com/blog/topics/threat-intelligence/gru-disruptive-playbook
5. https://cloud.google.com/blog/topics/threat-intelligence/chinese-espionage-tactics
6. https://forums.ivanti.com/s/article/CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-
Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways
7. https://cloud.google.com/blog/topics/threat-intelligence/suspected-apt-targets-ivanti-zero-day
8. https://www.ivanti.com/blog/security-update-for-ivanti-connect-secure-and-policy-secure
9. https://services.google.com/fh/files/misc/ivanti-connect-secure-remediation-hardening.pdf
10. https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement
11. https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
12. https://www.europol.europa.eu/media-press/newsroom/news/
europol-coordinates-global-action-against-criminal-abuse-of-cobalt-strike
13. https://www.cobaltstrike.com/blog/update-stopping-cybercriminals-from-abusing-cobalt-strike
14. https://www.mandiant.com/resources/blog/how-mandiant-tracks-uncategorized-threat-actors
15. https://cloud.google.com/blog/topics/threat-intelligence/apt44-unearthing-sandworm
16. https://cloud.google.com/blog/topics/threat-intelligence/apt45-north-korea-digital-military-machine
17. https://cloud.google.com/security/resources/insights/targeted-attack-lifecycle
18. https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions
19. https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
20. https://cloud.google.com/blog/topics/threat-intelligence/unc3944-targets-saas-applications
21. https://cloud.google.com/blog/topics/threat-intelligence/unc4393-goes-gently-into-silentnight
22. https://cloud.google.com/blog/topics/threat-intelligence/russia-targeting-signal-messenger
23. https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
24. https://medium.com/@RadiantCapital/radiant-capital-incident-update-e56d8c23829e
25. https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
26. https://www.justice.gov/opa/media/1320156/dl?inline
27. https://ofac.treasury.gov/media/923126/download?inline
28. https://www.justice.gov/usao-dc/media/1352191/dl
29. https://ofac.treasury.gov/media/923126/download?
30. https://cloud.google.com/blog/topics/threat-intelligence/
likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against
31. https://research.checkpoint.com/2024/bad-karma-no-justice-void-manticore-destructive-activities-in-is-
rael/
32. https://cloud.google.com/blog/topics/threat-intelligence/unc1860-iran-middle-eastern-networks

Mandiant M-Trends 2025 Report 91
33. https://research.checkpoint.com/2024/iranian-malware-attacks-iraqi-government/
34. https://cloud.google.com/blog/topics/threat-intelligence/telegram-malware-iranian-espionage
35. https://www.cybercom.mil/Media/News/Article/2897570/
iranian-intel-cyber-suite-of-malware-uses-open-source-tools/
36. https://www.trendmicro.com/en_us/research/24/h/threat-actors-target-middle-east-using-fake-tool.html
37. https://www.gov.il/BlobFolder/reports/alert_1817/he/ALERT-CERT-IL-W--1817.pdf
38. https://cloud.google.com/blog/topics/threat-intelligence/
suspected-iranian-unc1549-targets-israel-middle-east
39. https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations
40. https://blog.google/threat-analysis-group/iranian-backed-group-steps-up-phishing-campaigns-against-
israel-us/
41. https://cloud.google.com/blog/topics/threat-intelligence/unc3944-targets-saas-applications
42. https://cloud.google.com/learn/paas-vs-iaas-vs-saas?hl=en
43. https://www.reuters.com/business/finance/goldman-sachs-plans-spin-out-its-digital-assets-platform-
bloomberg-news-reports-2024-11-18/
44. https://www.jpmorgan.com/kinexys/digital-payments
45. https://www.blackrock.com/us/financial-professionals/investments/products/bitcoin-investing
46. https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise
47. https://cloud.google.com/blog/topics/threat-intelligence/examining-web3-heists
48. https://www.justice.gov/archives/opa/pr/911-s5-botnet-dismantled-and-its-administrator-arrested-coor-
dinated-international-operation
49. https://www.virustotal.com/gui/collection/campaign--a35afe10-cd7e-5c2c-b2d4-21cdaf3d9a75
50. https://cloud.google.com/blog/topics/threat-intelligence/securing-cryptocurrency-organizations

SPECIAL REPORT: MANDIANT M-TRENDS 2023 92
O
G
R
A
B
M
E
For more information, visit cloud.google.com.