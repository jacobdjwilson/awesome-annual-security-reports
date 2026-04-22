# Advanced Threat Research Report (January 2022)

## Table of Contents
- [Letter from our Chief Scientist](#letter-from-our-chief-scientist)
- [Log4j: The Memory That Knew Too Much](#log4j-the-memory-that-knew-too-much)
- [Ransomware](#ransomware)
- [Attack Pattern Techniques](#attack-pattern-techniques)
- [Advanced Threat Research](#advanced-threat-research)
- [Threats to Countries, Continents, Sectors and Vectors](#threats-to-countries-continents-sectors-and-vectors)
- [Living off the Land: Q3 2021](#living-off-the-land-q3-2021)
- [Bug Report](#bug-report)
- [Additional ATR Q3 2021 Data and Research](#additional-atr-q3-2021-data-and-research)
- [Resources](#resources)

---

## Letter from our Chief Scientist

Welcome to our new threat report and our new company.

As we look ahead in this new year, we must acknowledge a threatscape that left us all exhausted from a particularly challenging end to 2021. In our new company’s first threat report, we acknowledge the Log4j issue that dominated not only headlines, but the focus of defenders and enterprise security teams. We also look back at the third and fourth quarters of 2021, but let’s first detail our wealth of resources available to help you combat Log4j.

Fundamentally, as more details of the Log4j threat emerge, it’s imperative to connect to our research and updated resources for help. Beyond the product status, we continuously monitor for any active campaigns leveraging this vulnerability and detailing the coverage status for the new payloads.

When details of the Log4j vulnerability appeared we very quickly responded with the availability of network-based signatures and a write-up of the vulnerability. We quickly followed up with additional assets detailed in this report.

To understand more about current Log4j threat activity, as well as, other prevalent threats, please see our valuable threat dashboard.

In addition, please check out our Trellix Threat Labs blogs featuring our latest threat content, videos and links to the security bulletin.

Of course, Log4j isn’t the only threat to your enterprise’s security. This report also spotlights the looming shadow and disruption of ransomware, and other prevalent threats and attacks observed in the wild.

Happy 2022 and welcome to a new company.

—Raj Samani
Fellow and Chief Scientist
Twitter: @Raj_Samani

---

## Log4j: The Memory That Knew Too Much

In what is becoming a threatening tradition, Log4j, a new vulnerability affecting a widely used Log4j library was released just in time for the holidays. What has been described as the most serious cybersecurity flaw in decades called Trellix and the cybersecurity industry to action in the fourth quarter of 2021. The Log4j vulnerability threatened a potentially massive impact on any product which has integrated the Log4j library into its applications and websites including products and services from Apple iCloud, Steam, Samsung Cloud storage and many others.

Our team has been closely tracking Log4j since its discovery. We released a network signature KB95088 for customers leveraging Network Security Platform (NSP). The signature detects attempts to exploit CVE-2021-44228 over LDAP. This signature may be expanded to include other protocols or services, and additional signatures may be released to complement coverage.

### Log4j Timeline
- **December 9** – The Log4j vulnerability (CVE-2021-44228) was released on Twitter along with a POC on Github for the Apache Log4j logging library. The bug was originally disclosed to Apache on November 24.
- **December 10** – Steve Povolny and Douglas McKee posted a Log4j blog with an overview of our immediate findings. Our initial goal was to determine the ease of exploitation using the public PoC, which we have reproduced and confirmed. This was done using the public Docker container, and a client-server architecture leveraging both LDAP and RMI, along with marshalsec to exploit Log4j version 2.14.1.
- **December 14** – Log4j version 1.2’s vulnerability to similar attacks through the JMSAppender component was confirmed and CVE-2021-4104 issued.
- **December 18** – A new denial of service (DOS) vulnerability CVE-2021-45105 was discovered affecting versions 2.0-alpha1 through 2.16.0 of Log4j.

### Log4j Attack
Our team quicky researched and outlined what happens in the execution of a common web-based Log4j attack:

![LOG4J FLOW OF EXECUTION]

- **Step 1** – An attacker sends a specially crafted string to the web server hosting the vulnerable application. This string, as we have seen, can be obfuscated to bypass network-based signatures.
- **Step 2** – The application proceeds to deobfuscate this string to load it in memory. Once loaded into memory, the application initiates a LDAP connection to request the malicious class location’s address.
- **Step 3** – The attacker-controlled LDAP server responds with the location of the malicious Class file by indicating the HTTP URL address of where it’s hosted.
- **Step 4** – The vulnerable application initiates a download for the malicious class file.
- **Step 5** – The vulnerable application will load and run the malicious class file from Step 4.

### Trellix ATR Log4j Defenses
To protect an environment against attacks like Log4j, a layered strategy comprised of network security coupled by targeted endpoint memory scans allows defenders to effectively detect and prevent the attack execution flow against vulnerable systems exposed via network vectors. Our ENS Expert Rules and Custom Scan reactions are designed to enable defenders with such capabilities so they can apply precise countermeasure against these emerging threats.

CISA.gov also provides a Log4j scanner to help organizations identify potentially vulnerable web services affected by the Log4j vulnerabilities.

---

## Ransomware

In the third quarter of 2021, high-profile ransomware groups disappeared, reappeared, reinvented, and even attempted to rebrand, while remaining relevant and prevalent as a popular and potentially devastating threat against an increasing spectrum of sectors.

Even though ransomware activity was denounced and banned from numerous cybercriminal forums in Q2 2021, our team has observed activity among the same threat actors on several forums using alternate personas.

### Trellix Aids In Ransomware Arrests and Ransom Seisures
In December 2021, Trellix provided research that assisted FBI and Europol in the arrest of REvil affiliates and the seizure of $2 million in ransom.

Notable Q3 2021 ransomware trends and campaigns included:
- **BlackMatter** – This ransomware threat, discovered near the end of July 2021, started with a strong group of attacks that threatened to reveal proprietary business data of U.S. based agricultural supply-chain company New Cooperative.
- We released our belief that the Groove Gang is associated with the Babuk gang, either as a former affiliate or subgroup.
- **REvil/Sodinokibi** claimed responsibility for successfully infecting more than 1 million users through a ransomware attack on managed service software provider Kaseya VSA.
- **LockBit 2.0** surfaced in July 2021 and eventually listed more than 200 victims on its data-leak site.

### Government Response to Ransomware Threats
In Q3, the U.S. government initiated a proactive campaign to reduce ransomware’s prevalence with the launch of StopRansomware.gov hub offering rewards up to $10 million for information identifying or locating state-sponsored threat actors involved in cyber activities against critical U.S. infrastructure.

### Ransomware Family Detections
![Figure 1. Sodinokibi (41%) was the most prevalent Ransomware Family detected in Q3 2021, followed by DarkSide (14%) and Egregor (13%).]

---

## Attack Pattern Techniques

The team tracks and monitors APT campaigns and its associated indicators and techniques. Our team research reflects APT Threat Actors, Tools, Client Countries, Customer Sectors and MITRE ATT&CK Techniques from Q3 of 2021.

### APT Threat Actors
![Figure 2. APT41 (24%) and APT29 (22%) were the most prevalent APT Threat Actors in Q3 2021 and responsible for nearly half of APT activity monitored.]

### APT Tools
![Figure 3. Cobalt Strike (34%) was the most prevalent APT tool detected in Q3 of 2021 followed by Mimikatz (27%), Net.exe (26%), and PsExec (20%). Cobalt Strike attack suite abused by nation state actors was detected in over a third of APT activity.]

---

## Advanced Threat Research

Our team tracked threat categories in the third quarter of 2021. The research reflects percentages of detections in the type of ATR Malware used, Client Countries, Customer Sectors, MITRE ATT&CK techniques used in attacks and industry sectors.

### ATR Tool Threats
![Figure 4. Formbook (36%), Remcos RAT (24%), and LokiBot (19%) amounted to almost 80% of ATR Tool Threats detections in Q3 2021.]

---

## Threats to Countries, Continents, Sectors and Vectors

### Countries & Continents: Q3 2021
- North America recorded the most incidents among continents but saw a 12% decrease from Q2 to Q3 2021.
- The United States experienced the most reported incidents in Q3 2021, but incidents decreased 9% from Q2 2021.
- France recorded the highest increase (400%) of incidents reported in Q3 2021.
- Russia experienced the largest decrease (-79%) of Q3 2021 incidents compared to Q2 2021.

### Attack Sectors: Q3 2021
- Multiple Industries (28%) were targeted most often, followed by Healthcare (17%), and Public (15%).
- Notable sector increases from Q2 to Q3 2021 include Finance/Insurance (21%) and Healthcare (7%).

### Attack Vectors: Q3 2021
- Malware was the technique used most often in reported incidents in Q3 2021 but reported malware incidents decreased 24% compared to Q2 2021.
- Sector increases from Q2 to Q3 2021 include Distributed Denial of Service (112%) and Targeted Attack (55%).

---

## Living off the Land: Q3 2021

Cybercriminals use Living off the Land (LotL) techniques that use legitimate software and functions in a system to perform malicious actions on that system.

### Native OS Binaries
| Binary | MITRE ID | Comments |
| :--- | :--- | :--- |
| Powershell | T1059.001 | Often used to execute scripts and commands. |
| Windows Command Shell | T1059.003 | Primary CLI utility for Windows. |
| Rundll32 | T1218.011, T1564.004 | Used to execute local DLL files. |
| WMIC | T1218, 1564.004 | Command line interface for WMI. |
| Excel | T1105 | Used to retrieve payloads from remote locations. |
| Schtasks | T1053.005 | Used to maintain persistence. |
| Regsvr32 | T1218.010 | Used to register DLL files. |
| MSHTA | T1218.005 | Used to execute JavaScript/VBScript. |
| Certutil | T1105, 1564.004, T1027 | Used to gather remote tools. |
| Net.exe | T1087 | Used for reconnaissance. |
| Reg.exe | 1003.002, 1564.004 | Used to modify registry values. |

### Administrative Tools
- **Remote Services**: (AnyDesk, ConnectWise Control, RDP, UltraVNC, PuTTY, WinSCP) Used to gain remote access.
- **Archive Utilities**: (7-Zip, WinRAR, WinZip) Used to compress/decompress data.
- **PsExec**: Used to execute commands on remote systems.
- **BITSAdmin**: Used to maintain persistence.
- **fodhelper.exe**: Used to run malicious files with elevated privileges.
- **ADFind**: Used to discover active directory information.

---

## Bug Report

### Bugs on the Windshield
The team tracks and evaluates new vulnerabilities each month. We report what we feel are the most important based on a gut check of experience rather than just CVSS scores.

### A Moment of Reflection
Apache had a rough year with both its webserver (CVE-2021-41773) and Log4j component (CVE-2021-44228). Palo Alto also deserves an honorable mention with a bug found in their Global Protect VPN (CVE-2021-3064). The Log4j vulnerability is by far the biggest bug of 2021.

### Termites
A Microsoft Windows Installer Service local privilege escalation bug, CVE-2021-41379, was the proverbial termite of November. Microsoft disclosed the bug as requiring local access and allegedly fixed it, but the strategy backfired when the patch didn't work as expected.

---

## Additional ATR Q3 2021 Data and Research

- **Ransomware Client Countries**: ![Figure 5. Clients based in the United States accounted for more than one third of the total Ransomware detections in Q3 2021.]
- **Ransomware Customer Sectors**: ![Figure 6. Banking/Financial (22%), Utilities (20%), and Retail (16%) accounted for almost 60% of total Ransomware Customer detections in Q3 2021.]
- **Ransomware MITRE ATT&CK Techniques**: ![Figure 7. Data Entry (2.6%), File and Directory Discovery (2.5%), and Obfuscated Files or Information (2.4%) topped the Ransomware MITRE ATT&CK Techniques detected in Q3 2021.]
- **APT Client Countries**: ![Figure 8. Client detections of Attack Pattern Techniques in Turkey accounted for 17% of total detections in Q3 of 2021, followed by the United States (15%) and Israel (12%).]
- **APT Customer Sectors**: ![Figure 9. The most APT detections in Q3 2021 occurred in the Banking/Financial sector (37%) followed by Utilities (17%), Retail (16%), and Government (11%).]
- **APT MITRE ATT&CK Techniques**: ![Figure 10. Spearphishing Attachment (16.8%), Obfuscated Files or Information (16.7%), and PowerShell (16%) were the most prevalent APT MITRE ATT&CK Techniques detected in Q3 of 2021.]
- **ATR Client Countries**: ![Figure 11. More than half of total ATR tool threats detected in Q3 2021 were in Germany (32%) and the United States (28%).]
- **ATR Customer Sectors**: ![Figure 12. Banking/Financial ATR customer sector detections (45%) were most prevalent by far in Q3 2021.]
- **ATR MITRE ATT&CK Techniques**: ![Figure 13. Obfuscated Files or Information amounted to 5% of all ATR MITRE ATT&CK Technique detections in Q3 2021.]

---

## Resources

To keep track of the latest threats and research, see our team’s resources:

- **Threat Center**—Today’s most impactful threats have been identified by our team.
- **Twitter**: Trellix Labs, Raj Samani, Christiaan Beek, John Fokker, Steve Povolny, Douglas McKee.

### About Trellix
Trellix is a global company redefining the future of cybersecurity. The company’s open and native extended detection and response (XDR) platform helps organizations confronted by today’s most advanced threats gain confidence in the protection and resilience of their operations. More at [www.trellix.com](http://www.trellix.com).

Copyright ©️ 2022 Musarubra US LLC