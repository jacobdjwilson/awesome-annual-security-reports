# 2024 State of Threat and Exposure Management Report

## Table of Contents
- [Introduction](#introduction)
- [Volume 1: Measuring the Vulnerability Landscape](#volume-1-measuring-the-vulnerability-landscape)
  - [Vulnerability Prevalence](#vulnerability-prevalence)
  - [Vulnerability Exploitation](#vulnerability-exploitation)
  - [Risk Ratings](#risk-ratings)
  - [Remediation Timelines](#remediation-timelines)
  - [Celebrity Vulnerabilities](#celebrity-vulnerabilities)
- [Volume 2: NopSec Risk Score Calculations In Real Life Scenarios](#volume-2-nopsec-risk-score-calculations-in-real-life-scenarios)
  - [The Vulnerability Sample Selection](#the-vulnerability-sample-selection)
  - [CVE-2022-22965 - Spring Framework JDK 9+ Remote Code Execution Vulnerability](#cve-2022-22965---spring-framework-jdk-9-remote-code-execution-vulnerability)
  - [CVE-2021-26084 - Atlassian Confluence Server and Data Center OGNL injection unauthenticated remote code execution vulnerability](#cve-2021-26084---atlassian-confluence-server-and-data-center-ognl-injection-unauthenticated-remote-code-execution-vulnerability)
  - [CVE-2021-44832 - Apache Log4J2 Remote Code Execution Vulnerability](#cve-2021-44832---apache-log4j2-remote-code-execution-vulnerability)
  - [CVE-2021-34527 - Windows Print Spooler Service Remote Code Execution Vulnerability](#cve-2021-34527---windows-print-spooler-service-remote-code-execution-vulnerability)
  - [CVE-2021-26855 - Microsoft Exchange Server Remote Code Execution Vulnerability](#cve-2021-26855---microsoft-exchange-server-remote-code-execution-vulnerability)
  - [CVE-2023-35315 - Windows Layer-2 Bridge Network Driver Remote Code Execution Vulnerability](#cve-2023-35315---windows-layer-2-bridge-network-driver-remote-code-execution-vulnerability)
  - [CVE-2021-40444 - Microsoft MSHTML Remote Code Execution Vulnerability](#cve-2021-40444---microsoft-mshtml-remote-code-execution-vulnerability)
- [Volume 3: Cyber Threat & Exposure Management](#volume-3-cyber-threat--exposure-management)
  - [Mapping MITRE ATT&CK Taxonomies to CVEs](#mapping-mitre-attck-taxonomies-to-cves)
  - [ATT&CK Framework and LLMs](#attck-framework-and-llms)
  - [Mapping CVE by ATT&CK Technique](#mapping-cve-by-attck-technique)
  - [Where Do We Go From Here?](#where-do-we-go-from-here)
  - [Why Does This Matter?](#why-does-this-matter)
  - [Conclusions](#conclusions)
- [References](#references)
- [Appendix](#appendix)
  - [Appendix A: Mapping CVE by ATT&CK Tactic and Technique](#appendix-a-mapping-cve-by-attck-tactic-and-technique)
  - [Appendix B: Mapping CVE by ATT&CK Technique with a Single Sentence](#appendix-b-mapping-cve-by-attck-technique-with-a-single-sentence)

---

# 2024 State of Threat and Exposure Management Report

This 2024 iteration of NopSec annual state of vulnerability management focuses on the crossroad between threat-based prioritization and contextual risk management, delving deeper on how NopSec Risk Score prioritizes riskier vulnerabilities and how vulnerabilities CVE and ATT&CK framework can be mapped together to expand the threat and contextual risk vision of attack surface management. This report is divided into three parts: how the vulnerability landscape is measured in terms of vulnerability prevalence and remediation efficiency, how the NopSec Risk Score works in real-life vulnerability scenarios, and how CVE and ATT&CK taxonomies are mapped to expand the risk scenarios beyond vulnerability management.

www.nopsec.com

## Volume 1: Measuring the Vulnerability Landscape

An independent analysis of real-world vulnerability and remediation data in collaboration with the Cyentia Institute

THIS SECTION analyzes 36 million vulnerabilities detected by organizations using NopSec to help prioritize remediation efforts. We begin by examining the prevalence of those vulnerabilities across assets to determine which ones are most common. Then we measure how quickly those vulnerabilities are remediated and what factors speed up or slow down that process. The section closes by identifying examples of vulnerabilities that are prone to slip through the cracks of traditional prioritization strategies so your organization won’t waste valuable time and energy chasing after the wrong things.

### Vulnerability Prevalence

We’ll begin our foray into the wilds of the vulnerability landscape by examining the product vendors that shape it. This is important because these technologies are commonly used, thus vulnerabilities affecting them can have a widespread impact on cyber risk posture.

We measure vulnerability prevalence in three basic ways:

1.  Vulnerabilities published on the CVE List,
2.  Enterprise assets affected by those vulnerabilities, and
3.  The total number of detected vulnerabilities (open and closed) across all assets.

Each of these measures offers a different perspective of the vulnerability landscape and is captured in the columns of Figure 1.

![Figure 1: Prevalence of 15 most common vendors across CVEs, assets, and vulnerabilities](Image description: A bar chart showing the prevalence of the 15 most common vendors across CVEs, assets, and vulnerabilities. The chart has three sets of bars for each vendor, representing CVEs, Assets, and Vulnerabilities.)

Microsoft immediately jumps out from Figure 1. That single vendor is behind 11% of all published CVEs, which together affect 55% of all organizational assets and comprise 40% of all vulnerabilities detected. Debian, Oracle, RedHat, Adobe, and Apple are also worth highlighting since those vendors make the top five in at least one of the columns in Figure 4.

We need to be careful, however, about jumping to the conclusion that many vulnerabilities equate to insecure or poorly managed products. These are big numbers, to be sure, but not too surprising given their massive footprint. Plus, numerous vulnerabilities can actually be a sign of vendors making a concerted effort to identify, disclose, and fix issues affecting their products.

Speaking of fixing issues, the rightmost column in the chart shows the ratio of open and closed vulnerabilities. This makes it easy to discern that some vendors (e.g., Google and Adobe) boast high closure rates, whereas others show the opposite (e.g., Oracle and NetApp). Overall, 49% of all vulnerabilities had been closed by the time we pulled data for this analysis. We’ll dive deeper into remediation rates in a moment.

### Vulnerability Exploitation

When a new vulnerability emerges, questions like “Is it being exploited?” and “How exploitable is it?” quickly follow. Given that, we figured a view of various vulnerability factors that help answer such questions would be appropriate for this analysis. We list several in Figure 2.

![Figure 2: Commonality of vulnerability factors relevant to exploitation](Image description: A bar chart showing the commonality of various vulnerability factors relevant to exploitation. Factors include phishing, remote attacks, lateral movement, functional exploits, malware, and celebrity status.)

There’s a lot to soak in from Figure 2. In the top half, we see that vulnerabilities that enable phishing and/or remote attacks are quite common, affecting over half of all organizational assets. The enablement of lateral movement is (thankfully) less common among CVEs and detected vulnerabilities but still affects a quarter of assets.

The last trait listed in Figure 2. concerns the celebrity status of vulnerabilities. It’s quite rare among the plethora of published CVEs and even detected vulnerabilities. But over 20% of assets are plagued with a celebrity vuln. Like Hollywood celebrities, they tend to capture a lot of media attention. But are they the ones you should be paying attention to? More to come on that.

We see the same basic pattern for the existence of functional exploits and malware—they are less common among all vulnerabilities but very common across assets. And that’s arguably what matters most since protecting assets is the goal of remediating vulnerabilities.

### Risk Ratings

With so many open vulnerabilities placing organizational assets at risk, prioritizing remediation efforts has surged to the forefront of VM strategy. That’s usually done by identifying which vulnerabilities represent the highest risk, but how to do that best isn’t always clear. Thus, many organizations default to CVSS for determining which vulnerabilities warrant priority remediation.

Figure 3 shows the downside of that strategy. According to CVSS, over 70% of all detected vulnerabilities are rated high or critical severity. That’s unrealistic from a risk assessment standpoint and sets unrealistic expectations for remediation as well. Few organizations have the capacity to handle so many vulnerabilities.

![Figure 3: Breakdown of CVSSv3 and NopSec Business Risk Scores for detected vulnerabilities](Image description: A stacked bar chart comparing the breakdown of CVSSv3 and NopSec Business Risk Scores for detected vulnerabilities. The chart shows the percentage of vulnerabilities falling into Critical, High, Medium, and Low severity categories for both scoring systems.)

That’s why NopSec assigns a Business Risk Score to each vulnerability so customers can better prioritize their remediation efforts. The lower chart in Figure 3 shows a breakdown of detected vulnerabilities according to this score. A much more manageable 20% of vulnerabilities are rated as high or critical. In a later section, we’ll demonstrate how this contributes to significantly improved remediation rates over CVSS.

### Remediation Timelines

We mentioned in the last section that 49% of all detected vulnerabilities had been successfully remediated. But how long did that process take and how does it vary across different types of vulnerabilities? That’s exactly what we explore in this section.

There are multiple ways to measure how quickly vulnerabilities are closed, with mean-time-to-remediation (MTTR) using a straight average being the most common. There are several issues with that approach, however, which is why we favor a technique called survival analysis. It’s more appropriate for long-tailed distributions like remediation timelines and handles the fact that so many vulnerabilities haven’t yet been closed (“censored data”).

Based on a survival analysis of all vulnerabilities in our dataset, we calculate the overall average time-to-remediation at 212 days. This dying off (closing out) of vulnerabilities over time is traced by the dark gray “Overall” curve in Figure 4. But as you probably suspect, that timeline varies dramatically across organizations, assets, and different types of vulnerabilities.

![Figure 4: Comparison of vulnerability remediation timelines among asset categories](Image description: A survival analysis chart showing the comparison of vulnerability remediation timelines among different asset categories: Workstations, Domain Controllers, and Servers. The Y-axis represents the percentage of vulnerabilities closed, and the X-axis represents time in months.)

Figure 4 offers an example of such variation, comparing remediation timelines for three different categories of assets. Here we see that 80% of vulnerabilities affecting workstations have been closed three months after their initial discovery. But the reverse is true for servers; about 80% remain unresolved at the three-month mark. Domain controllers fall in the middle but actually catch up with and surpass workstations after nine months.

We could create numerous survival curves like these comparing all sorts of things, but we thought focusing on a dozen or so attributes of particular interest would be a better option. Figure 5 summarizes the effect of the selected attributes on remediation timelines.

![Figure 5: Effect of vulnerability attributes on average remediation timelines](Image description: A bar chart showing the effect of various vulnerability attributes on average remediation timelines. Attributes include asset categories, OS, exploitation signals, and internet-facing status. The bars represent the change in days to remediation.)

We’ve already seen the effect for a few of the attributes in Figure 5. Workstations reduce the average remediation time by 168 days, and servers typically tack on a couple of months. It’s also apparent that the operating system (OS) of the vulnerable asset makes a big difference. Microsoft Windows shaves 115 days, on average, while Linux systems take 98 days longer to remediate.

Some of the exploitation signals presented earlier also have an impact. Vulnerabilities that enable phishing and lateral movement are closed more quickly, but those that enable remote access or have been used in malware actually show longer remediation timelines. We find the latter particularly curious, as such vulnerabilities should ostensibly warrant priority remediation. The same logic applies to internet-facing assets. Based on our analysis, these traits don’t directly hamper remediation. Rather, they often tend to correlate with other impeding factors (e.g., Linux servers are often internet-facing and prone to remote access).

Hoping for a view of the attack surface and remediation speed for a larger collection of vendors? If so, Figure 6 is just what you’re looking for. It compares vendors based on overall vulnerability prevalence (x) and remediation speed (y). It’s admittedly busy, but it effectively communicates a huge amount of useful information. We’ll help you get your bearings and let you explore on your own from there.

Unlike the Gartner Magic Quadrant, you DO NOT want to be in the upper right area of this chart. Those vendors represent very common, slowly remediated vulnerabilities—which translate to a large and persistent attack surface. In the lower left, Microsoft and Google vulnerabilities are extremely common but tend to get fixed quickly. Vulnerabilities in the upper left may by flying under the radar remediation efforts because they’re relatively rare and yet remain unresolved for a long time.

![Figure 6: Comparison of vendors based on vulnerability prevalence and remediation speed](Image description: A scatter plot comparing vendors based on vulnerability prevalence (X-axis) and remediation speed (Y-axis). Vendors are plotted as points, with different quadrants indicating different risk profiles.)

We touched on the topic of prioritizing vulnerabilities earlier, and it deserves more attention here because it’s critical to the success of VM programs. It’s clear that some risk factors like enabling phishing and lateral movement correlate with faster remediation, but what about overall risk scores? Do we see any evidence that they help guide prioritization and streamline remediation? Yes, we do!

Figure 7 compares remediation timelines for escalating ranges of NopSec’s Business Risk Score. The green line corresponds to the highest tier of risk, and it’s clear that organizations close out those vulnerabilities much faster than others. The average time-to-remediation for those is approximately two months faster than the overall average. Almost 60% of those riskiest vulnerabilities are successfully closed within three months of discovery. Compare that to the lowest risk tier (blue line)—60% of those are still around after a full year.

![Figure 7: Vulnerability remediation timelines for NopSec’s Business Risk Score ranges](Image description: A survival analysis chart showing vulnerability remediation timelines for different ranges of NopSec’s Business Risk Score. The lines represent Low, Medium, High, and Critical risk scores.)

Since it’s impossible for organizations to fix all vulnerabilities all the time, success means knocking out the most risky ones most of the time. Figure 7 demonstrates that’s not just a pie-in-the-sky aspiration. Organizations can efficiently drive down risk in the real world when following a calculated approach to prioritization.

### Celebrity Vulnerabilities

Earlier we saw that so-called celebrity vulns tend to be fixed faster than average. This probably has a lot to do with many of them getting scary names and logos as well as the imminent end-of-the-internet cries of doom that often accompany them. But is that a good thing? Are celebrity vulnerabilities the ones that deserve priority remediation? Do they represent the highest risk?

We created Figure 8 to help explore these important questions. Before trying to interpret it, let’s get oriented to the format. All CVEs are plotted according to their assigned CVSSv3 rating on the horizontal axis and NopSec Business Risk Score on the vertical axis. Those given celebrity status are colored orange amid the field of dark gray regular ‘ol vulns.

![Figure 8: CVEs plotted by CVSSv3 vs. NopSec Business Risk Score with “celebrity vulns” highlighted in orange](Image description: A scatter plot with CVSSv3 score on the X-axis and NopSec Business Risk Score on the Y-axis. CVEs are plotted as points, with celebrity vulnerabilities highlighted in orange.)

Any CVE to the right of the diagonal line has a CVSS score that’s comparatively higher than its NopSec Score. Left of the line indicates the opposite. From that, the bias of CVSS toward higher scores is immediately apparent. For VM teams, that bias leads to systemic over-prioritization and inefficient risk reduction.

Also apparent from Figure 8 is the fact that celebrity status doesn’t necessarily correlate with high risk. The orange dots are all over the place—even in the portion of the chart where both CVSS and NopSec agree that vulnerabilities represent low risk. Thus, chasing celebrity vulns probably shouldn’t be a key factor in your prioritization strategy.

Figure 9 offers a different but complementary perspective. It plots CVEs based on the prevalence of vulnerable assets (x-axis) and NopSec Risk Score (same as the prior chart). We did this to highlight different zones or scopes of risk. Most concerning is the upper-right quadrant, which contains high-risk vulnerabilities that affect large numbers of assets. Remediating those should top the list for prioritization to achieve maximum risk reduction.

While many celebrity vulns occupy the upper-right of Figure 9, the prior takeaway holds. Your prioritization strategy is better focused on risk than chasing the celebrity spotlight.

![Figure 9: CVEs plotted by NopSec Business Risk Score vs. prevalence across assets with “celebrity vulns” highlighted in orange](Image description: A scatter plot with NopSec Business Risk Score on the X-axis and prevalence across assets on the Y-axis. CVEs are plotted as points, with celebrity vulnerabilities highlighted in orange.)

You probably noticed that several specific CVEs are annotated in Figures 8 and 9. We did that to identify specific examples of vulnerabilities that receive a detailed analysis in the next section. This will serve to demonstrate the importance of properly assessing risk when prioritizing remediation.

## Volume 2: NopSec Risk Score Calculations In Real Life Scenarios

THIS SECTION analyzes 36 million vulnerabilities detected by organizations using NopSec to help prioritize remediation efforts. We begin by examining the prevalence of those vulnerabilities across assets to determine which ones are most common. Then we measure how quickly those vulnerabilities are remediated and what factors speed up or slow down that process. The section closes by identifying examples of vulnerabilities that are prone to slip through the cracks of traditional prioritization strategies so your organization won’t waste valuable time and energy chasing after the wrong things.

For relevance, we selected vulnerabilities for further analysis from three main categories:

*   Both celebrity and non-celebrity vulnerabilities with high NopSec score and low CVSSv3 score. This category of vulnerabilities highlights the reprioritization performed by NopSec risk scoring algorithm.
*   Both celebrity and non-celebrity vulnerabilities with high CVSSv3 score and low NopSec risk score. This category of vulnerabilities highlights the deprioritization performed by NopSec risk scoring algorithm.
*   Both celebrity and non-celebrity vulnerabilities with high NopSec risk score present in a high percentage of assets. This category of vulnerabilities highlights the prevalence of high NopSec risk score vulnerabilities in high % of assets.

Out of these three main categories we selected a sample of seven vulnerabilities, chosen for their risk relevance and variety out of the three above mentioned categories. The selected vulnerabilities with their respective CVSSv3 score, percentage of Assets present, and NopSec Risk Score are presented in the chart below.

![Chart showing selected vulnerabilities with CVSSv3 score, percentage of assets present, and NopSec Risk Score](Image description: A table listing seven selected vulnerabilities with their CVSSv3 score, percentage of assets present, and NopSec Risk Score.)

The seven chosen vulnerabilities will be analyzed based on the threat information present in our system at the time of writing, explaining why the selected ones were prioritized, de-prioritized and overall relevant in terms of asset prevalence. This analysis would shed light on the necessary and professional process of prioritizing security vulnerabilities as part of a modern vulnerability management program.

### The Vulnerability Sample Selection

The following is the sample of vulnerabilities we selected based on the three categories highlighted above and based on their risk relevance. Below we will analyze each one of them based on their risk profile explaining why the NopSec risk score prioritized or de-prioritize them.

### 1. CVE-2022-22965 - Spring Framework JDK 9+ Remote Code Execution Vulnerability

A Spring MVC or Spring WebFlux application running on JDK 9+ may be vulnerable to remote code execution (RCE) via data binding. The specific exploit requires the application to be run on Tomcat as a WAR deployment. If the application is deployed as a Spring Boot executable jar, i.e. the default, it is not vulnerable to the exploit. However, the nature of the vulnerability is more general, and there may be other ways to exploit it.

The vulnerability is inherently important because the Spring framework is used by several software vendors in their products, including Cisco, VMware, Siemens, and obviously Oracle.
The vulnerability is also included in the CISA KEV because the exploit is used in the wild in several active attack campaigns. The vulnerability is also identified as a celebrity vulnerability under the given name “Spring4Shell”.

The vulnerability has a CVSS score of 7.5 and a CVSSv3 score of 9.8. The vulnerability’s EPSS score is quite high at 97.48%, reflecting several exploits in the public domain, including Metasploit and several attacks observed in the wild.

Our NopSec Risk Score is at 9.263, which is 2.5 points difference to the CVSS score. This increase reflects the following feature components that made the algorithm decide for a score increase:

*   Number of exploit references. Value of 9.
*   Number of cyber exploit sources. Value of 803
*   Number of cyber exploit sightings. Value of 2,152
*   CVSSv3 score. Value of 9.8
*   NLP relevant keyword: Remote code execution

The followings are the NopSec Scoe details for it to make such a score increase decision:

`"nopsec_score_details": {"is_threat": true, "prediction": 0.9263079762458801, "has_exploit": true, "has_func_exp": true}, "nopsec_threat_vectors": {"is_malware": true, "is_ransomware": false, "is_exploitable": true, "is_command_exec": true, "is_cred_compromise": true, "is_phishing_attack": false, "is_priv_escalation": true, "is_unauthenticated": true, "is_remote_attack_scenario": true, "is_lateral_movement_scenario": true}, "nopsec_threat_vector_list": ["Remote Attack Scenario", "Known Threat", "Allows Command Execution", "Allows Credential Compromise", "Known Exploit", "Authentication Not Required", "Allows Privilege Escalation", "Lateral Movement Scenario"]`

Therefore, we can see from this details that the vulnerability is not only a celebrity vulnerability present in the CISA KEV list but it is associated with public exploits and public exploit sightings, it is associated with malware, it is a remote code execution of an unauthenticated vulnerability which could lead to credentials compromised, privilege escalation and lateral movement scenarios. Therefore this vulnerability not only needs to be prioritized in the remediation effort but it is quite common in our clients’ organization sample and it is actively remediated.

### 2. CVE-2021-26084 - Atlassian Confluence Server and Data Center OGNL injection unauthenticated remote code execution vulnerability

In affected versions of Confluence Server and Data Center, an OGNL injection vulnerability exists that would allow an unauthenticated attacker to execute arbitrary code on a Confluence Server or Data Center instance. The affected versions are before version 6.13.23, from version 6.14.0 before 7.4.11, from version 7.5.0 before 7.11.6, and from version 7.12.0 before 7.12.5.

The vulnerability is inherently important because the Atlassian Confluence platform is used in DevOps across several organizations to document business requirements and other internal documentation related to software development.

The vulnerability is also included in the CISA KEV because the exploit is used in the wild in several active attack campaigns. The vulnerability is also identified as a celebrity vulnerability.

The vulnerability has a CVSS score of 7.5 and a CVSSv3 score of 9.8. The vulnerability’s EPSS score is quite high at 97.45%, reflecting several exploits in the public domain, including Metasploit and several attacks observed in the wild.

Our NopSec Risk Score is at 9.282, which is 2.5 points difference to the CVSS score. This increase reflects the following feature components that made the algorithm decide for a score increase:

*   Number of exploit references. Value of 12.
*   Number of cyber exploit sources. Value of 409
*   Number of cyber exploit sightings. Value of 1,034
*   CVSSv3 score. Value of 9.8
*   Number of references on NVD. Value of 2

The followings are the NopSec Scoe details for it to make such a score increase decision:

`"nopsec_score_details": {"is_threat": true, "prediction": 0.9282200932502747, "has_exploit": true, "has_func_exp": true}, "nopsec_threat_vectors": {"is_malware": true, "is_ransomware": false, "is_exploitable": true, "is_command_exec": true, "is_cred_compromise": true, "is_phishing_attack": false, "is_priv_escalation": true, "is_unauthenticated": true, "is_remote_attack_scenario": true, "is_lateral_movement_scenario": true}, "nopsec_threat_vector_list": ["Remote Attack Scenario", "Known Threat", "Allows Command Execution", "Allows Credential Compromise", "Known Exploit", "Authentication Not Required", "Allows Privilege Escalation", "Lateral Movement Scenario"]}`

Therefore, we can see from this details that the vulnerability is not only a celebrity vulnerability present in the CISA KEV list but it is associated with public exploits and public exploit sightings, it is associated with malware, it is a remote code execution of an unauthenticated vulnerability which could lead to credentials compromised, privilege escalation and lateral movement scenarios. Therefore this vulnerability not only needs to be prioritized in the remediation effort but it is quite common in our clients’ organization sample. However, it has not been actively remediated.

### 3. CVE-2021-44832 - Apache Log4J2 Remote Code Execution Vulnerability

Apache Log4j2 versions 2.0-beta7 through 2.17.0 (excluding security fix releases 2.3.2 and 2.12.4) are vulnerable to a remote code execution (RCE) attack when a configuration uses a JDBC Appender with a JNDI LDAP data source URI when an attacker has control of the target LDAP server. This issue is fixed by limiting JNDI data source names to the java protocol in Log4j2 versions 2.17.1, 2.12.4, and 2.3.2.

The vulnerability is inherently important because the Log4J2 library is used in several Java softwares for event logging purposes and therefore it makes the vulnerability attack surface wide spread.

The vulnerability is not currently included in the CISA KEV critical vulnerability risk. However, the vulnerability is labeled as celebrity vulnerability as it is associated with a potential exploitable element in the past (log4j) under the name “Log4Shell”.

The vulnerability has a CVSS score of 8.5 and a CVSSv3 score of 6.6. The vulnerability’s EPSS score is not that high at 2.24%, since there are not that many exploits in the public domain; however, attacks have been identified in the wild.

Our NopSec Risk Score is at 3.835, which is 1.5 points difference to the CVSS score. This increase reflects the following feature components that made the algorithm decide for a score increase:

*   Presence in malware. Value of 0
*   Working public exploits. Value of 0
*   Number of cyber exploit sightings. Value of 0
*   Number of references on NVD. Value of 2

The followings are the NopSec Scoe details for it to make such a score increase decision:

`"nopsec_score_details": {"is_threat": false, "prediction": 0.3835675120353699, "has_exploit": false, "has_func_exp": false}, "nopsec_threat_vectors": {"is_malware": false, "is_ransomware": false, "is_exploitable": false, "is_command_exec": true, "is_cred_compromise": true, "is_phishing_attack": false, "is_priv_escalation": true, "is_unauthenticated": false, "is_remote_attack_scenario": true, "is_lateral_movement_scenario": true}, "nopsec_threat_vector_list": ["Remote Attack Scenario", "Allows Command Execution", "Allows Credential Compromise", "Allows Privilege Escalation", "Lateral Movement Scenario"]}`

Therefore, even though the vulnerability is listed as a celebrity vulnerability because it is associated with a vulnerable software component in the past, it is not listed in CISA KEV listing and it is not associated with working public exploits or malware / targeted attacks. No exploit sightings have been recorded. Therefore, the vulnerability’s NopSec risk score have been increased from its CVSS score but not as important as in other vulnerabilities since its exploitation probability and profile is not as prominent.

### 4. CVE-2021-34527 - Windows Print Spooler Service Remote Code Execution Vulnerability

A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations. An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights.

The vulnerability is inherently important because it allows injecting dynamic content and DLL into memory using the vulnerability exploitation. It is the perfect vulnerability to be weaponized as malware and still used in the wild by several threat actors. Several weaponized exploits and exploit frameworks are publicly available.

The vulnerability is also included in the CISA KEV because the exploit is used in the wild in several active attack campaigns. The vulnerability is also identified as a celebrity vulnerability under the name “PrintNightmare”.

The vulnerability has a CVSS score of 9.0 and a CVSSv3 score of 8.8. The vulnerability’s EPSS score is quite high at 96.74%, reflecting several exploits and exploitation frameworks in the public domain, including Metasploit and several attacks observed in the wild.

Our NopSec Risk Score is at 9.279, which is 1 point difference to the CVSS score. This increase reflects the following feature components that made the algorithm decide for a score increase:

*   Number of exploit references. Value of 6.
*   Number of cyber exploit sources. Value of 804
*   Number of cyber exploit sightings. Value of 2,006
*   CVSSv3 score. Value of 8.8
*   Number of references on NVD. Value of 2

The followings are the NopSec Scoe details for it to make such a score increase decision:

`"nopsec_score_details": {"is_threat": true, "prediction": 0.9279255867004395, "has_exploit": true, "has_func_exp": true}, "nopsec_threat_vectors": {"is_malware": true, "is_ransomware": false, "is_exploitable": true, "is_command_exec": true, "is_cred_compromise": true, "is_phishing_attack": false, "is_priv_escalation": true, "is_unauthenticated": false, "is_remote_attack_scenario": true, "is_lateral_movement_scenario": true}, "nopsec_threat_vector_list": ["Remote Attack Scenario", "Known Threat", "Allows Command Execution", "Allows Credential Compromise", "Known Exploit", "Allows Privilege Escalation", "Lateral Movement Scenario"]}`

Therefore, we can see from this details that the vulnerability is not only a celebrity vulnerability present in the CISA KEV list but it is associated with public exploits and public exploit sightings, it is associated with malware, it is a remote code execution of an unauthenticated vulnerability which could lead to credentials compromised, privilege escalation and lateral movement scenarios. Therefore this vulnerability not only needs to be prioritized in the remediation effort but it is quite common in our clients’ organization sample. At the same time, it has been actively remediated.

### 5. CVE-2021-26855 - Microsoft Exchange Server Remote Code Execution Vulnerability

Vulnerability on Microsoft Exchange Server allows an attacker bypassing the authentication, impersonating as the admin (CVE-2021-26855) and writing an arbitrary file (CVE-2021-27065) to get the RCE (Remote Code Execution).

The vulnerability is inherently important because it allows an unauthenticated attacker to either impersonate an admin or write arbitrary files to get remote code execution with SYSTEM privileges. It is the perfect vulnerability that was weaponized to create self-spreading malware.

The vulnerability is also included in the CISA KEV because the exploit is used in the wild in several active attack campaigns. The vulnerability is also identified as a celebrity vulnerability under the name “ProxyLogon”.

The vulnerability has a CVSS score of 7.5 and a CVSSv3 score of 9.8. The vulnerability’s EPSS score is quite high at 97.48%, reflecting several exploits and exploitation frameworks in the public domain, including Metasploit and several attacks observed in the wild.

Our NopSec Risk Score is at 9.275, which is 0.88 point difference to the CVSS score. This increase reflects the following feature components that made the algorithm decide for a score increase:

*   Number of exploit references. Value of 23.
*   Number of cyber exploit sources. Value of 874
*   Number of cyber exploit sightings. Value of 3,364
*   CVSSv3 score. Value of 9.1

The followings are the NopSec Scoe details for it to make such a score increase decision:

`"nopsec_score_details": {"is_threat": true, "prediction": 0.9275614619255066, "has_exploit": true, "has_func_exp": true}, "nopsec_threat_vectors": {"is_malware": true, "is_ransomware": false, "is_exploitable": true, "is_command_exec": true, "is_cred_compromise": true, "is_phishing_attack": false, "is_priv_escalation": true, "is_unauthenticated": true, "is_remote_attack_scenario": true, "is_lateral_movement_scenario": true}, "nopsec_threat_vector_list": ["Remote Attack Scenario", "Known Threat", "Allows Command Execution", "Allows Credential Compromise", "Known Exploit", "Authentication Not Required", "Allows Privilege Escalation", "Lateral Movement Scenario"]}`

Therefore, we can see from these details that the vulnerability is not only a celebrity vulnerability present in the CISA KEV list but it is associated with public exploits and public exploit sightings, it is associated with malware, it is a remote code execution of an unauthenticated vulnerability which could lead to credentials compromised, privilege escalation and lateral movement scenarios. Therefore this vulnerability not only needs to be prioritized in the remediation effort but it is quite common in our clients’ organization sample. At the same time, it has been actively remediated.

### 6. CVE-2023-35315 - Windows Layer-2 Bridge Network Driver Remote Code Execution Vulnerability

An unauthenticated attacker could exploit the vulnerability by sending a specially crafted request to a Windows Server configured as a Layer-2