# On the State of Vulnerabilities, Top Exploits, and Five Risk Facts Learned by Threat Analytics for Improving Security Posture from 2022 Data
2023 QUALYS TRURISK RESEARCH REPORT

## Table of Contents
- [Foreword](#foreword)
- [Introduction](#introduction)
- [State of Vulnerabilities](#state-of-vulnerabilities)
- [Top Exploits in 2022](#top-exploits-in-2022)
  - [CVE-2022-30190 — Follina](#cve-2022-30190-follina)
  - [CVE-2022-26134 — Atlassian Confluence Remote Code Execution Vulnerability](#cve-2022-26134-atlassian-confluence-remote-code-execution-vulnerability)
  - [CVE-2022-22954 — VMware Workspace ONE Server-Side Template Injection Vulnerability](#cve-2022-22954-vmware-workspace-one-server-side-template-injection-vulnerability)
  - [CVE-2022-1040 — Sophos Firewall Authentication Bypass](#cve-2022-1040-sophos-firewall-authentication-bypass)
  - [CVE-2022-24521 — Windows CLFS Driver Privilege Escalation Vulnerability](#cve-2022-24521-windows-clfs-driver-privilege-escalation-vulnerability)
- [Five Risk Facts Learned from Threat Analytics in 2022](#five-risk-facts-learned-from-threat-analytics-in-2022)
  - [Risk Fact 1: Speed Is the Key to Out-Maneuvering Adversaries](#risk-fact-1-speed-is-the-key-to-out-maneuvering-adversaries)
  - [Risk Fact 2: Automation is the Difference Between Success and Failure](#risk-fact-2-automation-is-the-difference-between-success-and-failure)
  - [Risk Fact 3: Initial Access Brokers Attack What Organizations Ignore](#risk-fact-3-initial-access-brokers-attack-what-organizations-ignore)
  - [Risk Fact 4: Misconfigurations Still Prevalent in Web Applications](#risk-fact-4-misconfigurations-still-prevalent-in-web-applications)
  - [Risk Fact 5: Infrastructure Misconfigurations Open the Door to Ransomware](#risk-fact-5-infrastructure-misconfigurations-open-the-door-to-ransomware)
    - [On-Premises Misconfigurations](#on-premises-misconfigurations)
    - [Linking Misconfigurations to Ransomware](#linking-misconfigurations-to-ransomware)
    - [Ransomware-Specific Misconfigurations](#ransomware-specific-misconfigurations)
- [Recommendations](#recommendations)
- [Qualys Products](#qualys-products)
- [About Qualys Threat Research Unit (TRU)](#about-qualys-threat-research-unit-tru)
- [About Qualys](#about-qualys)
- [Contributors to the 2023 Qualys TruRisk Research Report](#contributors-to-the-2023-qualys-trurisk-research-report)
- [Appendix A: CVE Listing](#appendix-a-cve-listing)

## Foreword
The explosion of digital transformation in every business today is inevitable. Companies are 
increasingly competing by enhancing their customers’ digital experience. Similarly, global 
government organizations are significantly accelerating digital programs enabling citizens 
with e-governance, biometric identities and cardless payments to overcome financial 
exclusion. This has led to staggering amounts of software being developed in the last few 
years and a surge in software vulnerabilities with many more to come. Combine this with 
the shortage of skilled cybersecurity professionals, and CISOs and security teams are left 
with the daunting challenge of keeping up with the sheer volume of information coming at 
them. CISOs and security teams must continuously work to keep up with the fast pace of 
technological advancement and evolving cyber threats to reach their goal of reducing their 
organization’s risk.  

Today’s cybersecurity tools, which solely focus on generating more and more detections 
and alerts are not enough to help secure organizations. Organizations require assistance in 
prioritizing the most severe vulnerabilities present in their critical assets and resolving them 
before attackers exploit them. Additionally, they need a risk-based approach to quantify and 
align cyber risk to their business and communicate effectively with their executives and boards. 
 
Qualys’ passion and vision for helping companies minimize cyber risks has driven us to 
innovate by launching VMDR with TruRisk and patch management on our platform. Over 
the past 20+ years, we have operated a vast cloud platform that conducted 6+ billion scans, 
managed 90+ million agents, and deployed 45+ million patches in 2022 alone. This large 
pool of anonymized, real-time data allows us the opportunity to provide insights that assist 
organizations in enhancing their security programs.  
Our research team took a deep dive into our platform and its 13+ trillion anonymized data 
points to determine which vulnerabilities cause the highest risk to organizations. This data, 
overlayed with threat intelligence and original research conducted by The Qualys Threat 
Research Unit (TRU), exposes the intricacies of threat actor activities and operations. With 
vulnerability management, patching and endpoint detection and response (EDR) on a 
single platform, our TRU researchers get valuable insights into how threat actors behave 
pre and post-exploitation. 
Defining risk is more important than ever in setting a cybersecurity strategy. Today’s 
security teams must think holistically about attack paths, examine threat actor behaviors 
to understand what could wreak the most havoc, and quickly control threat activity when a 
breach occurs.
We encourage everyone – from practitioners to CISOs – to leverage the data and insights 
in this report to support their security initiatives and help facilitate more profound 
conversations with executives and board members that will enhance security posture. The 
report offers a reliable resource for security practitioners seeking data-driven, real-world, 
and actionable perspectives on vulnerabilities and trends critical to organizations across all 
industries and sizes. We hope that these insights will assist your teams in overcoming those 
seeking to harm your digital infrastructure. 
Sumedh Thakar 
President and CEO, Qualys

Many cybersecurity companies today focus solely on detection, which is a large part of the 
overall equation. But detection alone is not enough to reduce and eliminate risks within your 
environment. Stakeholders must also discover and remediate the risks that threaten  
a company or forever play a game of catch-up with threat actors. 
You can brush your teeth and floss every day, or you can risk cavities, or worse, and hope 
a dentist can fix larger problems later. Using detection tools alone provides a diagnostic, 
confirming a cavity — but still requires the painful path of extracting the infection. A  
wise approach is to focus first on finding flaws and reducing risk. This strategy requires 
understanding how vulnerabilities and misconfigurations are commonly leveraged and how 
to reduce the mean time to remediation (MTTR). Which do you prefer: brushing your teeth or 
being numbed by Novocain? 
No matter the difference in size, geography or industry, a CISO’s number one job is to 
manage cyber risk. Qualys helps organizations understand their risk exposure by providing 
comprehensive information on their unique environments and associated risks — which, left 
unattended, could upend their operations. Adversaries make it their business to understand 
the vulnerabilities and weaknesses within their victims’ environments, which can shift the 
balance of power and control in their favor, enabling cybercriminals to exploit vulnerabilities 
that organizations may not be aware of. In this report, the Qualys Threat Research Unit (TRU)  
investigates the primary techniques explored by adversaries to exploit vulnerabilities, 
compromise systems and infiltrate organizations. 
TRU works to secure and defend the digital world from threat actors who seed chaos and 
erode trust in business operations. From building vulnerability signatures, to writing detection 
rules, researching and finding zero-day threats, finding and reversing custom malware, 
reducing attack surface exposure and other advanced threat research activities — TRU works 
day and night to protect our customers’ cyber assets.
I hope this report offers you the same opportunity and direction that it offers me: to increase 
awareness of what attackers are adding to their Swiss Army knife of tools so you can create 
swift countermeasures. Above all, I want to inspire defenders by showing that their work does 
make a difference!
 
Travis Smith 
Vice President, Threat Research Unit, Qualys

## Introduction
Key Findings
In 2022, Qualys detected more than 2.3 billion vulnerabilities around the globe. By mining 
anonymous detection statistics from our global platform, TRU discovered unique insights into 
the vulnerabilities found on many devices, security of web applications, misconfiguration of on-
premises devices, and cloud security posture. These data points reveal Risk Facts that universally 
apply across industries and organizations:
1.  Speed is the key to out-maneuvering adversaries 
2.  Automation is the difference between success and failure 
3.  Initial Access Brokers (IABs) attack what organizations ignore 
4.  Misconfigurations still prevalent in web applications
5.  Infrastructure misconfigurations open the door to ransomware 

Methodology 
1.  This report focuses on 163 unique Common Vulnerabilities and Exposures (CVEs) announced 
in 2022, capable of introducing the highest level of risk to organizations across industries  
and all sizes.
2.  Anonymous detection statistics for the 163 CVEs were analyzed to establish their impact on 
enterprise security and the potential for breaches. 
3.  Anonymous Web Application Security (WAS) data was examined, and detections were 
mapped to the OWASP Top 10 application security risks.
4.  Anonymous detections from Policy Compliance (PC) scans related to endpoint scans using 
Center for Internet Security (CIS), Defense Information Systems Agency (DISA) Security 
Technical Information Guides (STIGs), and Qualys Ransomware Protection policies to analyze 
commonly failing controls.
5.  Discovery of the most common failing controls was enabled by analysis of anonymous scan 
detections from CIS Hardening Benchmarks for Amazon Web Services (AWS), Microsoft 
Azure, and Google Cloud Platform (GCP).

![Image description: Security Events collected in real time: Trillion 2+, Scanner appliances Thousand 50+, IP Scans/Audits a Year Billion 6+, Active Scanners, Cloud Agents across servers, endpoints, clouds & containers Million 84, • Physical • Virtual • Passive • Cloud/Container • API • Cloud Agents, Cloud Agents Scaling Security with Diverse Sensors, Scanners and Agent]

Figure 1: Qualys Platform — Deploying Anywhere 

## State of Vulnerabilities
The total number of reported vulnerabilities has exploded in recent years. The 1990s clocked 
2,594 vulnerabilities in total, which rose 796% to 37,231 in the 2000s; since 2010 another 135,284 
were discovered. A cumulative growth rate in vulnerabilities of 5,116% over this period seems 
startling. The trend continued during 2022 when more than 25,000 vulnerabilities received  
a unique CVE.
Given the wide assortment of classifications and Common Vulnerability Scoring System (CVSS) 
scores, not all 25,000 are created equal. Some are more dangerous than others based on their 
malicious usage by threat actors or patch difficulty — and many are still unprioritized.

![Image description: Evolution of vulnerability threat landscape, 1988 – 2022: 100% 192,036 All Known Vulnerabilities, 34.3% 65,920 Vulnerabilities With Exploits Available, 2.3% 4,492 Vulnerabilities With Weaponized Exploit Code, 0.54% 1,043 Exploited by Malware, 0.45% 868 CISA Known Exploited Vulnerabilities, 0.29% 575 Named Vulnerabilities (Log4Shell, Heartbleed), 0.22% 440 Exploited by Threat Actors, 0.12% 236 Exploited by Ransomware, 1988 — 2022]

Figure 2: Evolution of vulnerability threat landscape, 1988 – 2022

Within the universe of more than 192,000 known vulnerabilities, only a subset of those introduce 
the most risk to the organization. While the absolute number of vulnerabilities causing risk might 
be small, it is a dynamically evolving subset with older vulnerabilities getting new exploits regularly. 
This makes it important to continuously monitor threat intelligence and focusing on vulnerabilities 
that cause risk at any given point of time. By assessing cyber risk in terms of business risk, 
individual organizations can put these astronomical numbers into perspective. This report 
describes which are the most dangerous, categorizing them into one or more of the following:
*   **Exploit Available**: A weaponized exploit available publicly
*   **Threat Actor**: Exploited by and associated with a named threat actor 
*   **Malware**: One or more pieces of malware known to exploit the vulnerability
*   **Ransomware**: Ransomware known to exploit the vulnerability
*   **CISA KEV**: Was added to the U.S. Cybersecurity and Infrastructure Security 
Agency (CISA) Known Exploited Vulnerabilities (KEV) Catalog
*   **Named Vulnerability**: Name was given to the vulnerability by security industry or media

![Image description: Evolution of vulnerability threat landscape in 2022: 100% 25,228 All Known Vulnerabilities, 30% 7,786 Vulnerabilities With Exploits Available, 0.6% 159 Vulnerabilities With Weaponized Exploit Code, 0.36% 93 Exploited by Malware, 0.28% 73 CISA Known Exploited Vulnerabilities, 0.11% 28 Named Vulnerabilities (Log4Shell, Heartbleed), 0.09% 23 Exploited by Threat Actors, 0.07% 18 Exploited by Ransomware, 2022]

Figure 3: Evolution of vulnerability threat landscape in 2022

During 2022, the proportion of weaponized vulnerabilities among all published vulnerabilities 
decreased. Nonetheless, numerous vulnerabilities from previous years were utilized for the first 
time by threat actors or malware, resulting in weaponization. Throughout the year, a total of 
539 such vulnerabilities from previous years were exploited in some capacity. Of the 539 newly 
weaponized vulnerabilities, 118 were older than three years and were as old as CVE-2004-0210 
which was published in August 2004.

![Image description: Vulnerability Count: CISA KEV 453, WEAPONIZED 237, THREAT ACTOR 62, RANSOMWARE 50]

Figure 4: Vulnerabilities published prior to 2022 which are now being exploited in 2022

What this shows is that threat actors are not only adopting new vulnerabilities which are new 
and novel, they are also looking at exploiting vulnerabilities which remain unpatched within the  
organizations they encounter. This highlights that organizations need to take into account the  
threat landscape to fully understand how to prioritize vulnerabilities to address in their environments. 

## Top Exploits in 2022
The criteria to define which vulnerabilities were the most exploited during calendar year 2022 was  
simple: those which wreaked the most havoc. These vulnerabilities fall under the six categories 
mentioned above, which are presented in Table 1 and followed by individual descriptions.

| CVE        | QVS | CISA KEV | THREAT ACTOR (COUNT) | RANSOMWARE | MALWARE (COUNT) | MTTR (DAYS) | PATCH RATE |
|------------|-----|----------|----------------------|------------|-----------------|-------------|------------|
| CVE-2022-30190 | 100 | Y        | 4                    | Y          | 6               | 28.4        | 91.21%     |
| CVE-2022-26134 | 100 | Y        | 1                    | Y          | 4               | 28.5        | 58.30%     |
| CVE-2022-22954 | 100 | Y        | 1                    | Y          | 2               | 14.3        | 87.38%     |
| CVE-2022-1040  | 100 | Y        | 3                    | Y          | 1               | 70.0        | 34.70%     |
| CVE-2022-24521 | 95  | Y        | 2                    | Y          | 4               | 20.6        | 90.00%     |

Table 1: Top Exploited Vulnerabilities in 2022

### CVE-2022-30190  
Follina
This vulnerability poses a significant threat to organizations because an attacker can execute 
arbitrary code via various applications such as Microsoft Word. The exploit leverages the built-
in Microsoft URL handlers to trigger the msdt.exe process, which can then be used to run 
PowerShell commands. This allows Remote Code Execution (RCE), which can provide the ability 
to install programs, access/modify data, or create new user accounts. 
This vulnerability has been leveraged by at least 4 named threat actors and multiple malware 
families. The notorious Fancy Bear and Wizard Spider groups are known to exploit this CVE, as  
are the lesser known Luckycat and UAC-0098 groups. Some of the more well-known ransomware  
families to leverage this vulnerability are Qakbot, Skeeyah, and Black Basta. While the U.S. 
National Institute of Standards and Technology’s National Vulnerability Database (NVD) 
published the Follina CVE on June 1, 2022, and was known to be weaponized in less than a day, 
CISA did not add it to the KEV Catalog until 13 days following its disclosure on that month’s 
Microsoft Patch Tuesday. During 2022, this CVE was detected 12.8 million times around the world 
and patched on average in 28.1 days, reaching an effective patch rate of 91.21%.

### CVE-2022-26134  
Atlassian Confluence Remote Code Execution Vulnerability
This critical severity vulnerability allows unauthenticated remote code execution. As an Object-
Graph Navigation Language (OGNL) injection vulnerability, it allows an unauthenticated attacker 
to execute arbitrary code on a Confluence Server or Data Center instance. The CVE can be 
exploited by sending a specially crafted Hypertext Transfer Protocol (HTTP) request containing 
an OGNL expression in the Uniform Resource Identifier (URI) to the target server, which results in 
remote code execution. This CVE was an active vulnerability in all Confluence Servers and Data 
Center versions prior to distribution of a patched version.
This vulnerability was exploited by the Sparkling Goblin threat actors’ group, while also known 
to be leveraged by two ransomware families — particularly the Cerber and AvosLocker variants. 
While this CVE was detected only about 3,000 times, it poses significant risk due to the 
information it stores, its exposure to the internet, and its ease of exploitation. This vulnerability 
was added to the CISA KEV before being published by the NVD. This vulnerability is the second 
slowest (behind the Sophos Firewall Authentication Bypass [CVE-2022-1040] vulnerability) for 
remediations, being patched in 28.5 days with a 58.3% patch efficacy. 

### CVE-2022-22954  
VMware Workspace ONE Server-Side Template Injection Vulnerability
This CVE is a remote code execution vulnerability arising from a server-side template injection in  
the VMware Workspace ONE Access and Identity Manager. The vulnerability can be easily exploited  
with a specially crafted HTTP request and poses a significant risk because anyone with network 
access to a vulnerable instance can initiate this exploit to execute arbitrary code on the system.
Multiple vulnerabilities were discovered in VMware Workspace ONE in 2022 — five were 
weaponized and two were added to the CISA KEV list, yet only one was leveraged by threat 
actors and ransomware groups. This vulnerability was weaponized in less than a day and added 
to the CISA KEV list within just three days following its disclosure. Only the Rocket Kitten group is 
known to be exploiting this vulnerability in the wild. However multiple malware and ransomware 
families do leverage this, particularly the RAR1Ransom and Clop families. Patching has been faster 
for this vulnerability, within 14.3 days for an 87.3% patch efficacy. 

### CVE-2022-1040  
Sophos Firewall Authentication Bypass
CVE-2022-1040 is an authentication bypass vulnerability in the user portal and web admin of the 
Sophos Firewall running version v18.4 MR3 or older. Successful exploitation allows an attacker to 
bypass authentication and gain unauthorized access to the firewall to execute arbitrary code.
This vulnerability is leveraged by two threat actors, LuckyCat and DriftingCloud, and is leveraged 
by the Ragnarok ransomware family. Considering the target is a firewall device allowing direct 
connection to the internet, this CVE poses a serious issue that requires urgent remediation. It 
was added to CISA KEV six days after its publication to the NVD. Qualys found more than 6,000 
vulnerable instances resolved on average in 70 days with a 34.7% patch efficacy. 

### CVE-2022-24521  
Windows CLFS Driver Privilege Escalation Vulnerability
This CVE affects the Windows Common Log File System (CLFS) driver for Microsoft Windows. 
Successful exploitation allows for privilege escalation and is likely to be used in tandem with 
additional exploit techniques for gaining code execution abilities. It results in an Elevation of 
Privilege (EoP) in the Windows Common Log File System (CLFS) driver. Vulnerabilities like 
this CVE are typically leveraged after an attacker has already gained access to the vulnerable 
system. The attacker will then use the EoP vulnerability to gain higher permissions such as 
administrator-level access. CVE-2022-24521 was reported to Microsoft by the National Security 
Agency (NSA). It was detected in more than 14 million instances and added to the CISA KEV 
two days before NVD published the CVE. Two threat actors, UNC2596 and Vice Society, have 
been known to leverage this vulnerability. Other exploits were by four malware families, including 
four ransomware families: N13V/RedAlert, Cuba, and Yunluowang. Organizations patched this 
vulnerability within 20.6 days at a 90% patch efficacy during 2022. 

## Five Risk Facts Learned from Threat Analytics in 2022

### Risk Fact 1: Speed Is the Key to Out-Maneuvering Adversaries
The doubling of disclosed vulnerabilities over the last five years, the speed at which vulnerabilities 
are weaponized, and the cyber talent shortage have left teams struggling to wade through a 
mountain of vulnerabilities with no way to fix them all. Security teams need a systematic approach 
to cut through the noise and prioritize fixing the most critical vulnerabilities that will reduce risk 
and enable them to keep up with threat actors.
On average, weaponized vulnerabilities are patched within 30.6 days while only being patched 
an average of 57.7% of the time. These same vulnerabilities are weaponized by attackers in 19.5 
days on average. This means that attackers have 11.1 days of exploitation opportunities before 
organizations begin patching. Arguably the remediation activity accelerates after weaponization 
happens. Hence, it is very important to predict which vulnerabilities could be weaponized and 
patch them as early as possible so an emergency drill can be avoided.
A defender’s mean time to remediation (MTTR) shows a slight change in how organizations 
respond to urgent threats. Vulnerabilities known to be leveraged by named threat actors were 
remediated eight days faster than those without association to known threat actors. But while 
defenders are quick to address these, attackers are also quick to weaponize. Threat actors  
were faster to leverage vulnerabilities that are known to be exploited or were cataloged on  
CISA’s Known Exploited Vulnerabilities list when compared to those leveraged by malware  
and ransomware.

![Image description: Time to Weaponize vs. MTTR for Vulnerabilities in 2022: 19.5 Days Time to Weaponize, 11.1 Days Exploitation Opportunities, 30.6 Days Mean Time to Remediate, 57.7% Remediated Vulnerabilities, Weaponized Vulns, Malware, Ransomware, Threat Actors, CISA KEV, 10 0 20 30 40 Days, Time to Weaponize, Mean Time to Remediation]

Figure 5: Time to Weaponize vs. MTTR for Vulnerabilities in 2022

Attribution of a vulnerability to a named threat actor is a time-consuming and extremely difficult 
process. On average, attribution happens 95 days (about three months) after a vulnerability is 
published and 74.3 days (about two and a half months) after the CVE is patched. Data suggests 
that when a vulnerability is associated with a named threat actor, it does not necessarily lead 
to faster patching due to various factors. Organizations often need more resources for their 
cybersecurity teams, which means they prioritize patching based on criticality and active 
exploitation, not necessarily on threat actor association. Patch management can be complex, 
involving compatibility testing, scheduling downtime, and coordinating with multiple teams, 
causing delays in patch deployment. Accurate attribution of a cyberattack to a specific threat 
actor is complex, and uncertainty in attribution can affect patch prioritization. Additionally, 
organizations might underestimate the risk associated with a vulnerability if they believe the 
named threat actor is not targeting their industry or region, which may result in slower patch 
deployment. Finally, patches for specific vulnerabilities may not be immediately available from 
the vendor, causing delays in patching even when organizations are aware of the risk.
The analysis found that Microsoft Windows and Google Chrome represented every spot in the 
top 10 most detected CVEs in 2022, as shown in Table 2. This makes sense since Windows and 
Chrome are at the top in terms of market share for operating systems and browsers, respectively.

| CVE          | TITLE                                                                        | DETECTIONS (MILLION) | MTTR (DAYS) |
|--------------|------------------------------------------------------------------------------|----------------------|-------------|
| CVE-2022-2856  | Google Chrome Intents Insufficient Input Validation Vulnerability           | 22.4                 | 11.5        |
| CVE-2022-41049 | Microsoft Windows Mark of the Web (MOTW) Security Feature Bypass Vulnerability | 17.1                 | 10.3        |
| CVE-2022-4135  | Google Chromium Heap Buffer Overflow Vulnerability                          | 17.0                 | 2.03        |
| CVE-2022-2294  | WebRTC Heap Buffer Overflow Vulnerability                                 | 16.5                 | 13.8        |
| CVE-2022-3075  | Google Chromium Insufficient Data Validation Vulnerability                  | 16.1                 | 9.8         |
| CVE-2022-30170 | Windows Credential Roaming Service Elevation of Privilege Vulnerability     | 15.4                 | 13.2        |
| CVE-2022-24521 | Microsoft Windows Common Log File System CLFS Driver Privilege Escalation Vulnerability | 14.0                 | 20.5        |
| CVE-2022-26904 | Microsoft Windows User Profile Service Privilege Escalation Vulnerability    | 13.9                 | 10.8        |
| CVE-2022-37969 | Microsoft Windows CLFS Driver Privilege Escalation Vulnerability            | 13.7                 | 10.8        |
| CVE-2022-1096  | Google Chromium V8 Type Confusion Vulnerability                             | 13.3                 | 21.0        |

Table 2: Top 10 Vulnerabilities in 2022 Affecting Windows or Chrome

Visualizing the vulnerability data in scatter charts shows the full story. Figure 6 compares  
the age (X-axis) of a vulnerability to the percentage remediated (Y-axis) — a vivid picture of  
how organizations tackle these issues. The speed of remediation in Figure 6 varied wildly  
across all vulnerabilities.

![Image description: Comparing Weaponized Vulnerabilities in 2022 by Age vs. Percentage Remediated: Patch Rate, Days Since Vulnerability Publication, 100% 80% 60% 40% 20% 0% 50 100 150 200 250 300 350]

Figure 6: Comparing Weaponized Vulnerabilities in 2022 by Age vs. Percentage Remediated

Filtering the scatter chart to represent the top detections — Windows and Chrome — shows a 
definitive trendline of how organizations prioritize patching for the quickest result. As shown 
in Figure 7, results leveled out around a 90% patch rate, which suggests that the patches are 
deployed to approximately 90% of the organization’s infrastructure before the next wave of 
monthly patching begins. 

![Image description: Comparing Weaponized Chrome/Windows Vulnerabilities in 2022 by Age vs. Percentage Remediated: Patch Rate, Days Since Vulnerability Publication, 100% 80% 60% 40% 20% 0% 50 100 150 200 250 300 350]

Figure 7: Comparing Weaponized Chrome/Windows Vulnerabilities  
in 2022 by Age vs. Percentage Remediated

The higher patch rate for weaponized Chrome/Windows vulnerabilities stems from two 
reasons. First, the number of critical vulnerabilities these two products receive are significantly 
higher than others, and organizations are quick to prioritize critical vulnerabilities that have 
the potential to pose the most risk. Second, both Windows and Chrome patches are easily 
automated — critical for allowing defenders the opportunity to catch up to the speed at which 
threat actors operate.
However, removing Windows and Chrome shows a much different story (Fig. 8) with no clear 
patterns in remediation prioritization for the remaining vulnerabilities. The extreme variations can 
be attributed to factors such as an inability to automate patching (representative of patching 
niche software, which is often more difficult), or security teams deciding that patching the 
vulnerability is of little importance unless it is moved to CISA’s KEV list.

![Image description: Comparing Weaponized Non-Chrome/Windows Vulnerabilities in 2022 by Age vs. Percentage Remediated: Patch Rate, Days Since Vulnerability Publication, 100% 80% 60% 40% 20% 0% 50 100 150 200 250 300 350]

Figure 8: Comparing Weaponized Non-Chrome/Windows Vulnerabilities in 2022 
by Age vs. Percentage Remediated

### Risk Fact 2: Automation is the Difference Between Success and Failure
Automation across security infrastructure has become a necessity for every cyber arsenal. It 
allows organizations to eliminate manual and tedious tasks, which ultimately reduces the time 
and effort it takes to remediate vulnerabilities and frees up security staff to address more 
pressing concerns. Qualys Patch Management customers deployed more than 45 million  
patches, highlighting the shift in organizations migrating to more automated means to combat 
threat actors. 
Most weaponized vulnerabilities discussed in the body of this study were in Chrome or Windows, 
due to the high prevalence of that browser and operating system. The mean time to remediation 
for these products globally is 17.4 days (about 2 and a half weeks) with an effective patch rate of 
82.9%. Windows and Chrome are patched twice as fast and twice as often as other applications.

![Image description: MTTR vs. Patch Rate for Chrome in Windows Vulnerabilities in 2022: 0 10 20 30 40 Days, All, All, Windows + Chrome, Windows + Chrome, 17.4 Days, 30.6 Days, 82.9%, 42.3%, Time to Remediation, Patch Rate, Patched Twice as Fast, Patched Twice as Often, 0% 20% 40% 60% 80%]

Figure 9: MTTR vs. Patch Rate for Chrome in Windows Vulnerabilities in 2022 

![Image description: MTTR vs. Patch Rate for Chrome in Windows Vulnerabilities in 2022: Time to Remediation, Patch Rate, 0 10 20 30 40 0% 20% 40% 60% 80% Weaponized, Named Vulns, CISA KEV, APT, Weaponized, Named Vulns, CISA KEV, APT, Days, Non-Windows + Chrome, Windows + Chrome]

Figure 10: MTTR vs. Patch Rate for Chrome in Windows Vulnerabilities in 2022

Chrome and Windows comprise one-third of the weaponized vulnerabilities dataset, with 75% 
of these leveraged by named threat actors. Knowing these are prime risk vectors, organizations 
typically patch them first and most thoroughly. 
The study reveals patches that are known to have the opportunity to be deployed automatically 
were deployed 45% more often and 36% faster than those of a manual nature. Vulnerabilities 
that were automatable with a patch management solution have a mean time to remediation of 
25.5 days; where manually patched vulnerabilities were remediated in 39.8 days. The patch rate 
for the automatable set was 72.5% compared to 49.8% for those in the manual set. The extreme 
variations can be attributed to factors such as an inability to automate patching.

![Image description: Automated Patching Improves MTTR for Vulnerabilities in 2022: Time to Remediation, Patch Rate, 0 10 20 30 40 0% 20% 40% 60% 100% 80% Days, Manual, Manual, Automated, Automated, 25.5 Days, 39.8 Days, 72.5%, 49.8%, 32.6% Improvement, 54.6% Improvement, Automated Patching Is Key]

Figure 11: Automated Patching Improves MTTR for Vulnerabilities in 2022

### Risk Fact 3: Initial Access Brokers Attack What Organizations Ignore
A growing trend in the threat actor landscape is a category called Initial Access Brokers (IABs), 
sometimes called “affiliates.” TRU research shows the initial access point for IABs will follow one 
of multiple paths. In Figure 12, the top lane is where IABs seek to exploit the perimeter devices of  
their intended target, such as firewalls and web applications. IABs seek misconfigurations such as  
default passwords or exposed services to find a way in or exploit