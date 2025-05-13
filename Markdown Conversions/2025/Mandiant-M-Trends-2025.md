```markdown
# EMBARGO
# SPECIAL REPORT: MANDIANT M-TRENDS 2023
# Google Cloud Security 
# 2025 Report
# M-Trends
  
# Mandiant M-Trends 2025 Report
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
- [MITRE ATT&CK](#mitre-att&ck)
- [Bibliography](#bibliography)

# Introduction
Mandiant M-Trends 2025 Report
A key takeaway from M-Trends 2025 is that 
attackers are seizing every opportunity to 
further their objectives. One way they are 
doing this is through the use of infostealer 
malware, which is increasingly being used to 
enable intrusions using stolen credentials. 
Another growing trend is the targeting of 
unsecured data repositories, which is brought 
on by the lack of basic security hygiene. 
Additionally, attackers are exploiting the 
gaps and risks introduced as organizations 
continue their migrations to the cloud. 
The most common way attackers breached 
organizations in 2024 was through exploits, 
which we observed as the initial infection 
vector in 33% of our investigations. The finan-
cial sector continues to be the most targeted 
industry, making up a little more than 17% of 
our investigations. Global median dwell time 
has risen to 11 days from 10 days in 2023. 
This marks the first increase since the publi-
cation of the inaugural M-Trends in 2010 but 
is still below the 16 days reported in 2022. In 
M-Trends 2025, we take a look at how  
adversary notifications—notably in ransom-
ware incidents—influence the global median 
dwell time metric.
By providing data and other security metrics 
in M-Trends, along with deeper dives on 
attacker trends, we illustrate how threat 
actors are conducting their operations, how 
they are achieving their goals, and what 
organizations need to be doing to prevent, 
detect, and respond to threats. Infostealer     
malware, unsecured data repositories, and 
cloud migrations are just a few challenges 
organizations will face. We additionally cover:
- Insider risk brought on by Democratic 
People’s Republic of Korea (DPRK) IT workers
- Growth of blockchain technology leading to 
cryptocurrency and Web3 threats 
- Iran-nexus threat actor operations amid 
Middle East tensions
Mandiant consultants are regularly on the 
frontlines of cyber incidents, where they 
conduct in-depth investigations and analysis 
of the most recent attacks. This firsthand 
experience results in a deep understanding of 
threats and the effective strategies required 
to defend against them. 
Mandiant uses this knowledge to proactively 
assess client security postures, comparing 
them against the latest attacker tactics, 
techniques, and procedures. Furthermore, 
we provide critical support for remediation 
efforts, security transformation initiatives, 
and comprehensive security education.
Through the release of our annual M-Trends 
report, we share our learnings with the 
greater security community, building on our 
dedication to providing critical knowledge to 
those tasked with defending organizations. 
The information in this report has been  
sanitized to protect the identities of victims 
and their data.

# M-Trends
# By the Numbers
Mandiant M-Trends 2025 Report
Since 2010, Mandiant has provided statistics  
and analysis of threats observed in the 
previous year’s incident response investiga-
tions. In M-Trends 2025, Mandiant examines 
data collected from more than 450k+ hours 
of incident response engagements globally, 
highlighting trends and significant insights. 
This information can be useful to inform 
risk assessments and to support planning 
for threat hunts, which can improve an orga-
nization’s abilities to counter future threats 
effectively. 
The metrics reported in M-Trends 2025 are 
based on Mandiant Consulting investigations 
conducted between Jan. 1 and Dec. 31, 2024, 
that found targeted attack activity. 

# Campaigns  
#   & Global Events
When Mandiant experts identify threat activity that is actively impacting multiple organizations, 
a Campaign or a Global Event is created. Campaigns represent focused efforts by one or more 
threat groups with a single objective. Global Events encompass multiple threat groups pursuing 
different objectives but using similar tactics, such as exploiting a newly disclosed vulnerability.
Mandiant delivers dynamic updates throughout the lifespan of each Campaign and Global Event, 
including details of indicators of compromise (IOCs) and tactics, techniques, and procedures 
(TTPs) unique to the event. Where possible, Mandiant provides examples, context, and informa-
tion about threat actor behaviors, tools, and malware as well as actionable defensive and  
preventative measures. This intelligence is based on real-world data collected from Mandiant 
investigations and research, enabling our clients to respond effectively and decisively to active 
threats at first discovery and as they evolve. 
In 2024, Mandiant initiated 83 campaigns and five global events and continued to track activity 
identified in previous years. These campaigns affected every industry vertical and 73 countries 
across six continents. ![Campaigns and global events related to 2024 Mandiant incident response investigations] depicts 33 campaigns and three global events, a subset of all 
campaigns and global events with direct relation to Mandiant incident response engagements. 
For example, Campaign 23.042 began in April 2023 when the financially motivated group 
UNC3944 obtained network access to various organizations via SMS phishing and social engi-
neering. With this access, UNC3944 ultimately stole proprietary data and deployed the ALPHV 
ransomware.
Other examples include Russian cyber espionage groups like APT28 and APT44. Campaign 
23.056 tracked a subcluster of Russian cyber espionage group APT28 that, starting in late 
August, conducted credential harvesting and exploited Microsoft Outlook vulnerability 
CVE-2023-23397. Campaign 24.004 tracks APT44 activity leveraging trojanized software 
installers distributed via torrents on Ukrainian- and Russian-language forums as a means of 
achieving opportunistic initial access to potential targets of interest. In observed cases, victims 
of interest to APT44 received publicly available malware, such as DARKCRYSTALRAT[^2], for 
follow-on exploitation. 
To facilitate tracking and analysis of large-scale events, such as widespread exploitation of a  
vulnerability, Mandiant utilizes global events as a framework to encapsulate multiple distinct 
campaigns. For instance, Global Event 24.004 groups three campaigns (CAMP.24.026, 
CAMP.24.030, CAMP.24.031) associated with different threat actors exploiting CVE-2024-3400. 
Each campaign tracks unique tactics, techniques, and procedures (TTPs), such as SNOWLIGHT 
downloader deployment, reconnaissance targeting configuration files, and BEACON backdoor 
usage. Global Event 24.002 tracks zero-day exploitation of CVE-2023-46805 and CVE-2024-
21887, encompassing UNC5221 deploying custom malware and web shells, and another actor 
deploying SLIVER and TERRIBLETEA backdoors.

[^2]: Footnote content here.

![Campaigns and global events related to 2024 Mandiant incident response investigations]

# Targeted  
#      Attacks
## Targeted Industries
Mandiant responded to incidents affecting the financial sector more than any other sector in 
2024. Business and professional services, high tech, government, and healthcare made up the 
next most frequently observed sectors. These top industries are consistent with prior years, 
with slight variations. For example, in 2023, investigations associated with retail and consumer 
goods and services organizations slightly outpaced those associated with healthcare and 
government entities, while the opposite was true in 2024. 

![Targeted Industries, 2024]

## Initial Infection Vector
For the fifth year in a row, 
exploits were the most 
frequently observed initial infec-
tion vector in Mandiant incident 
response investigations. For 
intrusions in which an initial 
infection vector was identified, 
33% began with exploitation of 
a vulnerability. This is a decline 
from 2023, during which exploits 
represented the initial intrusion 
vector for 38% of intrusions, but 
nearly identical to the share of 
exploits in 2022, 32%.
Stolen credentials overtook email phishing as the second most frequently observed initial 
infection vector in 2024, representing 16% of intrusions, compared to 14% for email phishing. In 
2023, email phishing was determined to be the initial infection vector in 17% of intrusions and 
stolen credentials in just 10%. While email phishing remains a common and effective method 
for obtaining initial access, adversaries can obtain credentials in a variety of ways, including 
purchasing leaked or stolen credentials on underground forums, mining large data leaks for 
credentials, and actively pursuing credentials by infecting users with keyloggers and infoste-
alers. The continued prevalence of phishing and credential theft underscores the importance of 
implementing multifactor authentication (MFA), preferably FIDO2-compliant MFA methods.
The percentage of intrusions that began with web compromise increased from 5% in 2023 to 9% 
in 2024. Web compromise encompasses drive-by compromise, the use of malicious advertise-
ments, search engine optimization (SEO) poisoning, and compromised websites. To help mitigate 
risk from web compromise, organizations should consider a multilayered approach encompassing 
endpoint script blocking, content filtering for malicious redirects and software, policies against 
browser credential storage, and consistent patching of all systems.

![Phishing Declines as an Initial Infection Vector, 2022-2024]

![Initial Infection Vector, 2024]
In 2024, prior compromise remained a relatively common initial infection vector, occurring in 8% 
of investigations. The continued prevalence of this vector likely reflects the enduring effective-
ness of threat actors specializing in establishing initial access, then providing that access to other 
threat actors.
Insider threat, typically a negligible proportion of Mandiant’s incident response investigations, 
emerged as a surprisingly consequential initial infection vector in 2024. Specifically, a surge in 
North Korean IT workers seeking employment under false pretenses led to insider threat  
representing 5% of identified initial infection vectors. Mandiant primarily tracks this activity  
as UNC5267.
Mandiant also observed threat actors gain access to targeted systems through brute-force 
attacks, third-party compromise, social engineering voice calls (voice phishing or vishing),  
SIM swapping, supply chain compromise, and Bring Your Own Device (BYOD)—typically  
infected USBs.
Mandiant was unable to determine an initial infection vector for 34% of 2024 intrusions. Although 
numerous factors can contribute to an unknown vector, this considerable proportion indicates 
potential deficiencies in enterprise logging and detection capabilities.

## Most Frequently Exploited Vulnerabilities
Among the Mandiant incident response investigations performed in 2024, the most frequently 
exploited vulnerabilities affected security devices, which are, due to their function, typically 
placed at the edge of the network. Three of the four vulnerabilities were first exploited as zero-
days. While a broad selection of threat actors have recently targeted edge devices, Mandiant also 
specifically noted an increase[^3] in targeting from Russian[^4] and Chinese[^5] cyber espionage actors.

[^3]: https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Year_in_Review_of_ZeroDays.pdf
[^4]: https://cloud.google.com/blog/topics/threat-intelligence/gru-disruptive-playbook
[^5]: https://cloud.google.com/blog/topics/threat-intelligence/chinese-espionage-tactics
 
![Most Frequently Exploited Vulnerabilities]

### CVE-2024-3400
CVE-2024-3400 is a vulnerability in the GlobalProtect feature of Palo Alto Networks PAN-OS 
software that, when exploited, allows command injection through arbitrary file creation. 
Mandiant observed one threat group exploit this vulnerability as a zero-day. Within two weeks of 
its disclosure on April 12, 2024, and the publishing of proof-of-concept (PoC) code on April 13, 
2024, Mandiant observed more than a dozen separately tracked groups exploiting this  
vulnerability, including a RANSOMHUB affiliate that used initial access established using this 
vulnerability to conduct multifaceted extortion.

### CVE-2023-46805 and CVE-2024-21887
On Jan. 10, 2024, Ivanti disclosed[^6] two vulnerabilities, CVE-2023-46805 and CVE-2024-21887, 
impacting Ivanti Connect Secure VPN (“CS,” formerly Pulse Secure) and Ivanti Policy Secure 
appliances. Successful exploitation of these vulnerabilities allows authentication bypass and 
command injection, respectively. When chained together, these allowed for unauthenticated 
arbitrary command execution on systems. Mandiant identified[^7] UNC5221, a suspected Chinese 
cyber espionage threat cluster, exploiting these vulnerabilities in the wild as zero-days as early 
as December 2023. UNC5221 leveraged multiple custom malware families, in several cases 
trojanizing legitimate CS files with malicious code. The malware functionality and observed 
activity suggest that UNC5221 was primarily focused on establishing persistent access, avoiding 
detection, and performing internal reconnaissance.
Ivanti worked closely with Mandiant, affected clients, government partners, and Volexity to 
address these vulnerabilities. They released a blog post with mitigations, patches, an enhanced 
external integrity checker tool,[^8] and a disclosure for a subsequently discovered vulnerability, 
CVE-2024-21893. CVE-2024-21983 is a server-side request forgery vulnerability that allows a 
remote attacker to obtain unauthorized access. Mandiant also released a remediation and  
hardening guide.[^9]
In mid-January 2024, Mandiant identified UNC5135 scanning Ivanti Connect Secure appliances 
but did not directly observe UNC5135 successfully exploit these vulnerabilities. Mandiant 
assesses with moderate confidence that UNC5135 is linked to UNC3236, which we suspect to 
align with the publicly reported Volt Typhoon. 
By April 2024, Mandiant observed[^10] eight distinct clusters involved in the exploitation of one or 
more of the three vulnerabilities: CVE-2023-46805, CVE-2024-21887, and CVE-2024-21893. Of 
these eight clusters, Mandiant tracked five suspected Chinese cyber espionage threat clusters 
that exhibited distinct post-compromise behavior and used different malware after exploiting 
the vulnerabilities for initial access.

[^6]: https://forums.ivanti.com/s/article/CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways
[^7]: https://cloud.google.com/blog/topics/threat-intelligence/suspected-apt-targets-ivanti-zero-day
[^8]: https://www.ivanti.com/blog/security-update-for-ivanti-connect-secure-and-policy-secure
[^9]: https://services.google.com/fh/files/misc/ivanti-connect-secure-remediation-hardening.pdf

### CVE-2023-48788
CVE-2023-48788 is a SQL injection vulnerability in the FortiClient Endpoint Management Server. 
Mandiant observed a financially motivated threat cluster exploit this vulnerability to execute 
arbitrary SQL commands within two weeks of its March 12, 2024, disclosure. In observed oper-
ations, the threat cluster deployed the SimpleHelp remote administration tool, likely to establish 
persistent access before offering that access for sale to other threat actors. 
In October and November 2024, a suspected FIN8 threat cluster gained access to a targeted 
organization by exploiting CVE-2023-48788, deployed SNAKEBITE ransomware, and used the 
publicly available backup utility RESTIC for data theft.

![Global Detection by Source, 2024]
## Global Detection by Source 
The majority of organizations, 57%, first learned of a 2024 compromise from an external source. 
External notifications can be further divided into adversary notifications and external entity 
notifications. Adversary notifications typically take the form of ransom notes and represented 14% 
of total detection sources in 2024. Notifications from external entities, such as law enforcement 
or cybersecurity companies, comprised 43% of total detection sources. Organizations discovered 
an intrusion through internal mechanisms in 43% of 2024 investigations. These figures are roughly 
similar to our findings in 2023 investigations, which saw 54% external notifications and 46% internal 
notifications overall.

![Global Detection by Source, 2024]

## Global Median Dwell Time
The 2024 global median dwell time remained largely in line with 2023 figures. While the median 
overall value increased by one day from 2023 to 2024, the year-over-year trend continues to 
indicate that dwell times have declined significantly over the long term. For example, overall 
dwell time in 2014 was 205 days, compared to just 11 days in 2024. Dwell time for internally 
discovered intrusions remained less than that of all externally notified intrusions in 2024. 

![Median Dwell Time, 2011-2024]

![Median Dwell Time by Detection Source, 2024]
The median adversary notification time was just five days, while 
external partners notified in a median of 26 days. This discrepancy is 
not surprising given that the vast majority of adversary notifications 
originate from extortion actors who benefit from monetizing  
intrusions quickly. 

## Global Dwell Time Distribution
Dwell time distribution plots intrusions that Mandiant investigated across ranges of dwell time. The 
distribution heat map demonstrates that the prevailing trend across Mandiant investigations from 
2018 to 2024 is toward shorter and shorter dwell times. Comparing 2023 to 2024, the percentage 
of investigations that were discovered in one week or less increased from 43.3% to 45.1%.

![Global Dwell Time Distribution, 2018-2024]

## Post-Compromise Activity
### Financial Gain
In 2024, financially motivated intrusions, where  
a monetization technique was directly observed,  
represented 35% of all Mandiant incident response 
investigations. Ransomware-related intrusions repre-
sented 21% of all 2024 intrusions and approximately 
two-thirds of financially motivated intrusions. These 
proportions are also comparable to 2023, when 
ransomware was involved in 23% of all cases and about 
two-thirds of financially motivated intrusions.
In addition to ransomware-related events, Mandiant 
also responded to a variety of other financially moti-
vated intrusions in 2024, including data theft extortion 
without ransomware encryption, illicit cryptomining, 
North Korean IT worker employment fraud, business 
email compromise, cryptocurrency theft, and cases in 
which threat actors attempted to monetize intrusions 
by offering access to targeted organizations or stolen 
data for sale.

![Financial Gain, 2020-2024]

### Data Theft
In 37% of 2024 investigations, Mandiant identified 
evidence of data theft, which is consistent with 2023. 
Data theft extortion events in which no ransomware 
was deployed represented 11% of all cases, and multi-
faceted extortion, which includes both data theft and 
ransomware encryption, represents 6% of all cases.
Mandiant also observed attackers focus on theft of 
credentials and information useful for performing 
further reconnaissance of compromised networks. In 
addition, Mandiant identified attackers, such as the 
Russian cyber espionage actor APT28 and Chinese 
cyber espionage groups including APT41, conducting 
more targeted data theft. APT28 conducted selective 
data theft, demonstrating interest in personnel-related 
data, as well as email content and documents relevant 
to geopolitical topics consistent with Russian inter-
ests. In a campaign targeting multiple organizations in 
Europe, the Middle East, and Africa (EMEA) and Japan 
and Asia Pacific (JAPAC), APT41 leveraged SQLULDR2 
to export data from Oracle Databases and used 
PINEGROVE to systematically and efficiently exfiltrate 
large volumes of sensitive data from the compromised 
networks, transferring to OneDrive to enable exfiltra-
tion and subsequent analysis.

### Insider Threats
Mandiant responded to a number of incidents involving a unique variety of insider threat, North 
Korean IT workers. Mandiant primarily tracks this activity as UNC5267. North Korean IT workers 
use stolen and fabricated identities to apply for high-paying jobs in order to generate revenue 
for the North Korean regime in violation of international sanctions. Mandiant identified IT 
workers at diverse organizations, including in the financial services, telecommunications, media 
and entertainment, retail, and technology industries. In incident response engagements to date, 
North Korean IT workers have primarily functioned within the scope of their job responsibili-
ties. However, the remote workers often gain elevated access to modify code and administer 
network systems. This heightened level of access granted to fraudulent employees presents a 
significant security risk. Moreover, in several cases in the latter half of 2024, Mandiant observed 
evidence of North Korean IT workers stealing proprietary data from targeted organizations and, 
following discovery and termination, threatening to release it publicly if the organization did not 
pay a ransom. 
Mandiant released detailed guidance for detecting North Korean IT worker job applicants in 
Staying a Step Ahead: Mitigating the DPRK IT Worker Threat.[^11] 

[^11]: https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat

![Data Theft, 2020-2024]

## Malware
In 2024, Mandiant began tracking 632 net new malware families. In investigations, Mandiant 
observed 205 malware families, 83 of which were both newly tracked and observed in at least 
one incident response investigation. This number of newly tracked families is on par with the 626 
families Mandiant began tracking in 2023, bringing the total number of tracked malware fami-
lies to more than 5,500 unique families. The 83 newly tracked families that Mandiant observed 
in incident response investigations in 2024 is lower than the 128 families observed in the same 
category in 2023. This continues a trend observed during the past three years of fewer new 
malware families being identified in investigations. This decrease showcases threat actors’ 
continued willingness to leverage tools already present within the targeted environment as well 
as their ability to use and misuse tools rather than constructing new malware or configuring 
known post-exploitation tools. A growing number of compromises use no malware at all. 

![Malware Families, 2024]
Looking further into the corpus of malware tracked by Mandiant, malware effective on Windows 
remains most prevalent. In both newly tracked (76%) and observed malware (62%) in 2024, 
Mandiant experts observed that malware was more likely to be effective exclusively on the 
Windows operating system. However, Mandiant has seen a decrease in the proportion of 
malware designed for Windows systems over the years. 
Malware effective exclusively on Linux operating systems continues to increase slowly, 
accounting for 12% of newly tracked malware families and 22% of observed malware in 2024, 
compared to 11% of newly tracked and 17% of observed in 2023. The comparative reduction in 
Windows malware does not signify decreased risk associated with Windows systems but may 
indicate the risk to Linux environments is slowly increasing.

## Malware Families by Category
Of the 632 malware families that Mandiant began to track in 2024, backdoors remained the 
predominant category, representing 31% of malware families. The next most observed catego-
ries were downloaders (19%), droppers (12%), credential stealers (6%), and ransomware (5%). 
The “Other” category is made up of utilities, tunnelers, data miners, rootkits, keyloggers, and 
point-of-sale malware, each of which make up less than 5% of the malware population. These 
findings continue to remain consistent year over year with little movement in position. 

![Newly Tracked Malware Families by Category, 2024]

![Observed Malware Families by Category, 2024]
Similarly, observed malware family categories remained relatively consistent with the findings 
from previous years. Of the 205 unique malware families observed in investigations conducted 
during the 2024 calendar year, backdoors remained most used by attackers, with 35% of 
observed malware families with that primary purpose. The remaining malware family categories 
are made up of ransomware (14%), droppers (8%), downloaders (7%), tunnelers (6%), and  
credential stealers (5%).
In both the newly tracked and observed malware families by category, Mandiant continues to see 
a large portion of the percentage of malware residing in the “Other” category. This likely reflects 
the diversity of both attackers and objectives that Mandiant encounters in investigations. 

## Malware Category
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

## Most Frequently Seen Malware Families
For the fifth consecutive year, BEACON was identified as the most frequently observed malware 
family in Mandiant investigations globally and was identified in 5.4% of all intrusions. BEACON usage 
has decreased dramatically since 2021, when it was observed in 28% of Mandiant investigations. 

![BEACON Usage, 2020-2024]

![Most Frequently Seen Malware Families, 2024]
Of note, in July of 2024, Europol[^12] provided an update on Operation MORPHEUS, a global action 
against the illicit use of the unlicensed versions of the Cobalt Strike red teaming tool. This  
operation, conducted with law enforcement and private sector partners, successfully disrupted 
infrastructure linked to cyber criminal activities. The initiative, which began in 2021, involved  
flagging 690 IP addresses, 593 of which were taken down by online service providers. Fortra,[^13] 
the maintainers of the Cobalt Strike framework, also announced the number of unauthorized 
copies of Cobalt Strike observed in the wild has decreased by 80% over the past two years as a 
result of their participation in Operation MORPHEUS. Observed declines in percentages of inves-
tigations where Mandiant identified BEACON since 2021 may reflect the success of this effort. 

[^12]: https://www.europol.europa.eu/media-press/newsroom/news/europol-coordinates-global-action-against-criminal-abuse-of-cobalt-strike
[^13]: https://www.cobaltstrike.com/blog/update-stopping-cybercriminals-from-abusing-cobalt-strike

## Malware Family
- **BASTA**: BASTA is a ransomware written in C++ that encrypts local files. The ransomware is capable of deleting volume shadow copies. BASTA generates a random ChaCha20 key to encrypt each file; the key is encrypted and appended to the end of the file. The malware has been observed using .basta as the extension for encrypted files; however, some samples have used a random nine-character alphanumeric extension.
- **BEACON**: BEACON is a backdoor written in C/C++ that is part of the Cobalt Strike framework. Supported backdoor commands include shell command execution, file transfer, file execution, and file management. BEACON can also capture keystrokes and screenshots as well as act as a proxy server. BEACON may also be tasked with harvesting system credentials, port scanning, and enumerating systems on a network. BEACON communicates with a command-and-control (C2 or C&C) server via HTTP or DNS.
- **GOOTLOADER**: GOOTLOADER is a JavaScript downloader that comes in an obfuscated form. It downloads another JavaScript file that drops and executes the intended payload.
- **LOCKBIT**: LOCKBIT is a ransomware written in C that encrypts files stored locally and on network shares. LOCKBIT can also identify additional systems on a network and propagate via SMB. Prior to encrypting files, LOCKBIT clears event logs, deletes volume shadow copies, and terminates processes and services that may impact its ability to encrypt files. LOCKBIT has been observed using the file extension ".lockbit" for encrypted files.
- **RANSOMHUB**: RANSOMHUB is ransomware written in GoLang capable of encrypting data using ChaCha20, xChaCha20 or AES256 algorithms. The symmetric encryption key is per-file and protected by elliptic curve cryptography, ed25519. RANSOMHUB can be configured to encrypt a targeted directory, local disks, or network shares. RANSOMHUB provides the capability to reboot in safe mode before running or as a safe mode instance and can be configured for standard out logging.
- **REDBIKE**: REDBIKE (also known as Akira) is ransomware written in C++ that encrypts local files. Encrypted files have the extension ".akira" appended to the filename. Files are encrypted using ChaCha20, and a ransom note is written to every folder with encrypted files. REDBIKE has some code overlaps with CONTI ransomware.
- **SYSTEMBC**: SYSTEMBC is a tunneler written in C that retrieves proxy-related commands from a C2 server using a custom binary protocol over TCP. A C2 server directs SYSTEMBC to act as a proxy between the C2 server and a remote system. SYSTEMBC is also capable of retrieving additional payloads via HTTP. Some variants may utilize the Tor network for this purpose. Downloaded payloads may be written to disk or mapped directly into memory prior to execution. SYSTEMBC is often utilized to hide network traffic associated with other malware families. Observed families include DANABOT, SMOKELOADER, and URSNIF.
- **WIREFIRE**: WIREFIRE is a web shell written in Python that exists as trojanized logic to a component of the Pulse Secure appliance. WIREFIRE supports downloading files to the compromised device and executing arbitrary commands.

## Threat Groups
In 2024, Mandiant identified and 
began tracking 737 new threat  
clusters, bringing the grand total of  
threat groups Mandiant tracks to more 
than 4,500. During 2024 incident 
response engagements, Mandiant 
observed 302 different threat groups, 
233 of which were newly identified 
within the year. These figures are on 
par with 2023, during which Mandiant 
experts identified 719 new threat 
clusters and observed 316 groups in 
incident response investigations,  
with 220 of those groups also being 
newly identified. 
Organizations faced four advanced persistent threat (APT) groups from China, Russia, and Iran; 
one named financial threat (FIN) group; and 297 UNC groups from various geolocations in 2024 
engagements. Mandiant continues to see groups that have been tracked for more than one year, 
and in some cases, up to 10 years. However, the majority of newly tracked and observed threat 
groups are new clusters of activity observed within Mandiant Consulting engagements in 2024. 
The composition of this set of threat clusters indicates that organizations continue to face a 
variety of both established and novel threats.

![Threat Groups, 2024]

## Observed Groups by Goal
The majority of attackers active in 2024 were 
financially motivated (55%). This proportion is 
slightly larger than the 