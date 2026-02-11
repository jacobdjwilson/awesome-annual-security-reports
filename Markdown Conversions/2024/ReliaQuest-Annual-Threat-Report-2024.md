# ReliaQuest Annual Cyber-Threat Report

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Data-Driven Threat Insights](#data-driven-threat-insights)
- [Incident Metrics](#incident-metrics)
- [Critical Security Incidents Data](#critical-security-incidents-data)
- [What We Observed & Forecast](#what-we-observed--forecast)
- [Business Email Compromise Making A Big Impact](#business-email-compromise-making-a-big-impact)
- [Extortion Threat Looms Large](#extortion-threat-looms-large)
- [Social Engineering](#social-engineering)
- [Malware-Free and LotL Activity](#malware-free-and-lotl-activity)
- [TTP Evolution](#ttp-evolution)
- [Conclusions and Recommendations](#conclusions-and-recommendations)
- [Conclusions Based on 2023 Data and Analysis](#conclusions-based-on-2023-data-and-analysis)
- [General Recommendations and Best Practices](#general-recommendations-and-best-practices)
- [How ReliaQuest Can Help](#how-reliaquest-can-help)
- [Reference List](#reference-list)
- [Appendix A: Methodology](#appendix-a-methodology)
- [Appendix B: Endnotes](#appendix-b-endnotes)

---

# Introduction

The ReliaQuest Annual Cyber-Threat Report provides a comprehensive overview of the key cyber threats we observed targeting organizations from January 1 to December 31, 2023 (the reporting period).

The ReliaQuest Threat Research team based this report on quantitative and qualitative analysis of cyber attacks.

Our aim is to empower organizations with actionable intelligence, delving into threat actors’ motives and tactics, techniques, and procedures (TTPs).

This intelligence fosters a more profound understanding of threat operations, enabling security leaders to make informed decisions and refine cybersecurity tactics to accommodate an ever-changing cyber-threat landscape.

Our analysis brings to light the most pressing cyber threats, such as business email compromise (BEC), extortion, Living off the Land (LotL) attacks, and sophisticated social engineering. This report charts threat actors’ evolution, but also anticipates potential shifts in their TTPs as we look to the future. We offer a forward-looking perspective to prepare organizations for emerging challenges they are likely to face.

Based on our observations and response to threat activity, this report provides strategic recommendations to bolster your security posture. But our mission extends beyond immediate threat mitigation. A preventative approach to cybersecurity—focusing on proactive measures and cost-effectiveness—embodies the ReliaQuest core principles:

*   Increase Visibility
*   Reduce Complexity
*   Manage Risk

These principles are the bedrock of our methodology and ensure that, as a force-multiplier, we amplify your capabilities to navigate the murky waters of cyber threats. We hope that this report will serve as a valuable source of thorough analysis and actionable insights, thereby contributing to our mission to Make Security Possible.

1 Make Security Possible

---

# Executive Summary

Over 2023, cyber-threat actors continued to select from a wide range of TTPs to infiltrate systems and networks. Their choices varied according to specific contexts, and would have been influenced by tool or access availability, motive, and geopolitical tensions, among other factors. Our responses to incidents revealed the following key metrics and insights.

*   **Resolution Time Depends on Context**: Incidents with the longest mean time to resolve (MTTR) occurred in sectors that rely heavily on physical infrastructure and operational technology (OT) systems.
*   **Incident Response is Improving**: Organizations utilizing traditional approaches saw an average Mean Time to Respond (MTTR) of 2.3 days. Those who opted to leverage some level of AI and automation saw a reduction to 58 minutes: a 98.8% decrease from 2022. Organizations who fully leveraged AI and automation are seeing reductions of MTTR down to 7 minutes or less.
*   **Phishing Remains Popular**: Phishing links or attachments were used in 71.1% of all incidents. These methods were commonly used to aid initial access to networks or systems.
*   **Business Email Compromise (BEC) Has Surged**: BEC is bolstered by phishing-as-a-service (PhaaS) platforms, often providing threat actors with access to critical services, leading to widespread infections. One trend is combining credential harvesters with adversary-in-the-middle (AITM) activity to bypass multifactor authentication (MFA).
*   **Social Engineering Attacks Proliferated Dramatically**: September saw a surge in social engineering, with a 51% increase in QR code phishing (quishing) compared to the total from January through August. Threat actors also targeted cloud and on-premises environments through social engineering, frequently employing MFA fatigue attacks.
*   **Living off the Land Binaries (LOLBins) Are in Frequent Use**: LOLBINs are popular with threat actors performing LotL activity—especially developers of fileless malware. They accounted for a significant portion of critical security incidents: 22.3%. Of these, 92% involved Rundll32, Msiexec, and Mshta.
*   **Extortion Continues to Flourish**: Extortion activity increased by 74.3%, with a record 4,819 compromised entities named on data-leak websites. Just on its own, the “LockBit” ransomware group named an unprecedented 1,000-plus entities. “Clop,” “ALPHV,” and other groups adopted new extortion tactics, including filing SEC complaints, using cloned domains to leak data, and leaking data via torrents.
*   **AI and Automation Are Aiding Threat Actors**: Threat actors are increasingly leveraging automation to identify and exploit vulnerabilities more quickly; this was observed with the mass exploitation of the Citrix Bleed vulnerability. It is also likely that automation and Generative AI will increasingly assist threat actors in conducting phishing at scale.
*   **Billions of Exposed Credentials Pose a Significant Threat**: In 2023 we discovered more than 6 billion exposed credentials in breached data on the clear and dark web, bringing the total number we have found to 36 billion-plus. Threat actors frequently use stolen credentials to gain initial access or launch credential stuffing attacks.

**Attackers Favor Certain TTPs in High-Risk, High-Impact Activity**

Analyzing our critical security incidents, we found that the most commonly used TTPs, categorized by MITRE ATT&CK® categories, were:

*   **Initial Access**: Drive-by compromise was used in 29.2% of incidents related to initial access.
*   **Persistence**: Scheduled tasks were abused in 32.8% of incidents.
*   **Defense Evasion**: Obfuscation techniques were employed in 23.5% of incidents.
*   **Lateral Movement**: Remote desktop protocol (RDP) and Server Message Block (SMB)—both Windows-supported protocols—were used in 59.3% of incidents.
*   **Execution**: 64.9% of incidents involved the abuse of command and scripting interpreters.
*   **Privilege Escalation**: In 24.1% of incidents, attackers used valid domain accounts to escalate privileges.
*   **Command-and-Control (C2)**: 80% of incidents involved HTTPS traffic or ingress tool transfers.
*   **Impact**: Financial theft was the desired impact in 88.4% of incidents, making it the primary motive.

2 Make Security Possible

---

# Data-Driven Threat Insights

The ReliaQuest GreyMatter® security operations platform responds to thousands of incidents every day, aiding organizations in detecting threats rapidly and reliably. In addition to providing automated alerts, we proactively hunt within our customers’ environments for threats that may have evaded security measures. In this section we present analysis of data from two sources (see Appendix A for full definitions):

*   **Incident metrics**, pertaining to all incidents identified as true positives; we discuss the average response time across technologies and industries, and the most commonly observed MITRE ATT&CK techniques.
*   **Critical security incidents**, which are a smaller subset of true positive incidents that had the potential to result in data breaches or theft (e.g., involving extortion, espionage, custom malware, hands-on-keyboard operations, commodity threats); we describe the most common MITRE ATT&CK techniques observed at various attack stages.

4 Make Security Possible

---

# Incident Metrics

## Mean Time to Resolve

MTTR is an important metric: the measurement of the average time between incident detection and customer resolution. A shorter MTTR indicates a more efficient and effective response, reducing the potential damage caused by the incident and minimizing downtime. Various factors can influence MTTR, including the complexity of the incident, the availability of resources, the effectiveness of incident response procedures, and the expertise of the response team.

By analyzing the average MTTR across sectors, we can discern which sectors are responding well and which are not, and explain why. As shown in Figure 1, the sector with the longest average MTTR was Mining, Quarrying, and Oil and Gas Extraction:

**5.1 days**

This was followed by Public Administration, with an MTTR of 4.8 days— slightly higher than the MTTR of the subsequent three sectors, which ranged from approximately 3 to 4 days.

![Figure 1: MTTR by sector in 2023](Image description: A bar chart showing Mean Time to Resolve (MTTR) by sector in 2023. The Mining, Quarrying, and Oil and Gas Extraction sector has the highest MTTR at 5.1 days. Public Administration is second highest at 4.8 days.)

These numbers showed an improvement from 2022: The administrative support sector had the highest MTTR in 2022, with 20.5 days, and education and mining sectors followed, both with 14.1 days. The average MTTR across all sectors in 2022 was 3.4 days, meaning that most organizations responded to threats in fewer than 4 days. In 2023, the MTTR dropped to 2.6 days, highlighting an improvement in customer response to incidents.

The mining sector’s long MTTR can be attributed to an emphasis on physical operations and historically isolated OT systems, which now face security challenges, given increasing IT integration.

Incident remediation processes can be complicated by the specialized nature of OT systems and the imperative to maintain operational continuity.

For public administration entities, MTTR is affected by the complexity of their extensive, regulated systems and budgetary constraints, necessitating efficient use of resources and strategic planning.

5 Make Security Possible

---

## In All Sectors, There Was a Significant Reduction in MTTR from 2022 to 2023

This signifies that companies are becoming more adept and efficient at incident response, likely because of increased awareness of cyber threats and their impacts. The standardization of security responses, and the of some level of automation into the response workflows over the past year, probably also helped reduce the MTTR.

### Automating Incident Response With AI

Organizations who opted to leverage some level of AI and automation saw a reduction in their MTTR to 58 minutes: a 98.8% decrease from 2022.

Those who fully leveraged AI and automation are seeing reductions of MTTR down to 7 minutes or less.

![Reduction in MTTR](Image description: A graphic illustrating a significant reduction in Mean Time to Resolve (MTTR) with the use of AI and automation in incident response.)

## GreyMatter Incident TTPs

Financially motivated cybercriminal groups continue to indiscriminately attack companies in almost all sectors and regions. The three most observed MITRE ATT&CK techniques in our true-positive¹ data set involved phishing activity, accounting for approximately 71.1% of all observed TTPs in the reporting period.

As seen in Figure 2, attempts to exploit weaknesses, such as a software vulnerability or misconfiguration in a public-facing application (e.g., internet-facing system or host), were also prevalent. Web servers remained prime targets for exploitation, along with databases, network administration tools, and any internet-accessible services. This exploitation is often an effective way to secure initial access, which frequently paves the way for a threat actor to move laterally in a compromised network and extend their access.

The majority of MITRE techniques we identified in customer incidents were discovered and stopped in early attack stages (see Figure 3). The prevalence of techniques related to initial access highlights threat actors’ continued persistence in attempts to infiltrate organizations. Most of these attempts were intercepted at this stage, reflecting increased resilience among companies, complemented by GreyMatter’s efficacy in identifying and halting attacks early, often before traditional reconnaissance activities are typically detected.

6 Make Security Possible

---

![Figure 2: GreyMatter true-positive incidents’ TTPs in 2023](Image description: A pie chart showing the distribution of MITRE ATT&CK TTPs observed in GreyMatter true-positive incidents in 2023. Phishing is the largest segment.)

All sectors face risks posed by their systems’ weaknesses, especially when externally facing infrastructure is mismanaged or neglected. Patching is complex, and failing to apply patches in a timely manner opens opportunities for threat actors to exploit vulnerabilities.

To combat these threats, streamline your patch-management processes—creating test environments or maintaining redundant systems to prevent downtime during patching—and reinforce security measures for all public-facing infrastructure.

![Figure 3: Number of incidents associated with MITRE tactics in customer incidents in 2023](Image description: A bar chart showing the number of incidents associated with different MITRE ATT&CK tactics in customer incidents in 2023. Initial Access has the highest number of associated incidents.)

7 Make Security Possible

---

# Critical Security Incidents Data

Recommendations for protecting against the threats discussed in this section can be found in the General Recommendations and Best Practices section.

## Initial Access

Most TTPs used to achieve initial access to a compromised customer’s environment during the reporting period were linked to user interaction or error. This indicates that attackers overwhelmingly gained initial access by exploiting the trust and vulnerability of unsuspecting individuals.

Drive-by compromise has been traditionally defined as the automatic download of a malicious file from a compromised website without user interaction. However, in most cases we reviewed during the reporting period, user action was involved—facilitating initial access in 29.2% of incidents. Individuals were frequently tricked into downloading disguised malicious files, such as via a fake Chrome update. (Such activity is now being categorized within a broader scope of drive-by compromise.)

These attacks commonly deployed malware loaders and information stealers. Most frequently deployed was “SocGholish” (aka FAKEUPDATES), a malware loader often used by initial access brokers (IABs; these threat actors typically sell network access to ransomware operators). SocGholish was typically distributed in drive-by compromise attacks when someone visited a compromised website and was encouraged to download a seemingly benign malicious file.

“SolarMarker” came next in the ranking of malware most deployed through drive-by compromise. SolarMarker gained notoriety by targeting browser data to intercept credentials, then stealing information stored in web browsers. Such data can give threat actors initial access to an organization’s network.

![Figure 4: Initial-access TTPs observed in ReliaQuest customer incidents in 2023](Image description: A bar chart showing the most common Initial Access TTPs observed in ReliaQuest customer incidents in 2023. Drive-by compromise is the most prevalent.)

![Figure 5: Malware distributed through drive-by compromise in 2023, by type of malware](Image description: A pie chart showing the types of malware distributed through drive-by compromise in 2023. SocGholish is the most common.)

## Post-Exploitation Activity

Threat actors who achieved initial access in 2023 went on to perform careful and stealthy maneuvering; success in evading detection largely depended on their motives, knowledge, and experience.

### Execution

To execute malicious code on a compromised system, threat actors frequently exploited scripting interpreters, such as PowerShell and JavaScript.

These tools offer attackers flexibility and widespread support on Windows systems. Threat actors can abuse them to pre-define complex and autonomous post-exploitation actions, increasing attack efficiency and speed. PowerShell alone was involved in nearly a quarter of execution activity, highlighting its prevalence in enterprise organizations and its role in facilitating cyber threats.

The continued use of Windows in enterprise environments has led to the abuse of PowerShell and Windows Command Shell (cmd.exe) in over half of all execution activity. Threat actors will probably continue to pursue this kind of exploitation—encouraged by the deep integration of scripting languages into IT infrastructure, and the difficulty for defenders in distinguishing legitimate use from harmful use. Without enhanced monitoring and stricter controls, attackers will continue to exploit the inherent trust that configurations place in scripting tools for effective cyber attacks.

9 Make Security Possible

---

![Figure 6: Execution-related TTPs observed in 2023](Image description: A bar chart showing the most common Execution-related TTPs observed in 2023. Abuse of command and scripting interpreters is the most prevalent.)

### Persistence

In 32.8% of customer incidents, attackers abused scheduled tasks² to maintain access to a compromised system.

This included setting a task to execute a PowerShell command that established or re-established a connection to a C2 server. Such abuse can be particularly challenging to detect, as threat actors can assign tasks nondescript or system-like names, embed them in legitimate processes, and/or manipulate task properties.

![Figure 7: Persistence-related TTPs observed in 2023](Image description: A bar chart showing the most common Persistence-related TTPs observed in 2023. Scheduled tasks are the most frequently abused.)

However, the robust event logging for scheduled tasks in Windows environments enables organizations to cost-effectively monitor for such events. The second most-observed technique for persistence, accounting for 23.1% of cases, involved the MITRE technique known as boot or logon autostart execution: registry run keys / startup folder³. Threat actors modify specific registry keys or place files in startup folders to auto-execute malicious programs or scripts every time the system boots up or when a user logs in. This technique poses a challenge for defenders as it requires in-depth analysis and monitoring of a system’s startup processes and registry entries.

10 Make Security Possible

---

### Privilege Escalation

Threat actors often exploit the trust placed in valid accounts to gain greater access to an organization’s network or systems.

They obtain access to such accounts when individuals use their corporate account credentials for personal services. This introduces a significant risk, as breaches of personal-service providers can expose the credentials to those corporate accounts. By obtaining or compromising legitimate user credentials, such as those hardcoded in scripts, saved in user files, or taken from LSASS memory, attackers can bypass security controls and escalate privileges.

Acquiring valid account credentials, whether for domain (24.1% of the cases in our data set) or local (10.3%) accounts, can be achieved in various ways. Threat actors can search breach directories, scour cybercriminal forums for shared databases, use lookup services to scan cloud-stored logs, and transact with IABs.

The exploitation of valid accounts poses a severe threat by enabling attackers to masquerade as legitimate account users. They can then move laterally across a network, access sensitive information, and carry out malicious activities without raising immediate suspicion. The use of compromised credentials poses a particularly high threat because it can weaken conventional security perimeters. Credential compromise prevention should be a critical focal point of any cyber-defense strategy.

![Figure 8: Privilege-escalation–related TTPs observed in 2023](Image description: A bar chart showing the most common Privilege Escalation TTPs observed in 2023. Valid accounts are the most frequently exploited.)

### Defense Evasion

To avoid detection during an attack, threat actors used obfuscated commands in payloads 23.5% of the time.

This technique is effective in enhancing the complexity of strings and patterns found within commands, making the payloads harder to detect and analyze and obscuring an attacker’s objectives. One popular method was the use of Base64-encoded PowerShell strings with the “-encoded” cmdlet. This was often combined with other obfuscation techniques, such as the addition of escape characters or whitespace, and command reordering using the “-f” format operator.

We also saw the use of AES-encrypted PowerShell, where the payload was first encrypted with a hardcoded key, then Base64 encoded and compressed, sometimes with an additional layer of encoding. With multiple layers of obfuscation, attackers hope to evade automated security detection by making it challenging to decode and decompress the payload. Masquerading, when paired with obfuscation methods mentioned above, make up a complex strategy that attackers use to disguise their activities and avoid detection.

In 6.4% of customer incidents, we detected the use of masquerading techniques, particularly in the dissemination of SocGholish malware, which deceives users with fake browser update prompts.

11 Make Security Possible

---

![Figure 9: Defense-evasion–related TTPs observed in 2023](Image description: A bar chart showing the most common Defense Evasion TTPs observed in 2023. Obfuscated commands are the most prevalent.)

### Discovery

Of all the MITRE techniques, discovery accounts for the widest range of TTPs we observed in customer incidents.

Threat actors are using diverse strategies and methods to gather information and identify potential targets. Often, they used a variety of built-in tools—a multitude of techniques are available for attackers to “live off the land”⁴ and use a system’s own features (e.g., whoami, nltest) to achieve their objectives. Given that these native tools are commonly used for discovery, organizations should establish a baseline behavior for them and apply detection alerts for anomalies.

The most commonly observed TTPs were system information discovery and system owner/user discovery, each making up 11% of discovery-related customer incidents.

These TTPs provide attackers with a detailed understanding of a target environment, including system configurations and user privileges, which is essential for planning subsequent activity.

![Figure 10: Discovery-related TTPs observed in 2023](Image description: A bar chart showing the most common Discovery-related TTPs observed in 2023. System information discovery and system owner/user discovery are tied for the most prevalent.)

12 Make Security Possible

---

### C2 Activity

During the reporting period, 44.2% of C2 activity used HTTPS to establish communication with compromised systems.

![Figure 11: C2-related TTPs observed in 2023](Image description: A bar chart showing the most common C2-related TTPs observed in 2023. HTTPS is the most frequently used protocol.)

Threat actors favor HTTPS for its ability to encrypt communications and blend with legitimate traffic, evading detection by security tools. Although HTTPS is commonly allowed, by default, through firewalls, in 2023 attackers also separately ingressed tools to complement their C2 capabilities. They did so to fill gaps not covered by the C2 infrastructure alone, like enabling specialized data exfiltration or privilege escalation. We have previously observed the default ports for HTTPS, ports 443 and 80, as the most commonly used to establish communications with Cobalt Strike team servers.

In 35.8% of customer incidents, threat actors opted for ingress tool transfer to move sophisticated tools (e.g., netscan, Rclone, BloodHound) onto compromised systems, surpassing the capabilities of custom-built malware.

These effective tools provided advanced functionality and reliability for establishing backdoors. In a 2023 incident, attackers used a vulnerable driver to disable EDR agents before executing ransomware, then used Rclone for data exfiltration. Threat actors often use LOLBins, which are trusted system executables, to ingress tools and bypass security undetected.

Given their legitimate status, LOLBins typically evade traditional antivirus software. Attackers also use content delivery networks (CDNs), such as Discord, for file ingress, exploiting their widespread use and low alert profiles in security systems. The strategic abuse of LOLBins is a significant security challenge because it exploits systems’ inherent trust of legitimate software, evading many antivirus measures.

13 Make Security Possible

---

Remote monitoring and management (RMM) software, while intended for legitimate IT system administration, can potentially be abused by attackers as a secondary C2 channel due to its ability to remotely control systems and generate traffic that may be indistinguishable from legitimate network activity.

Because RMM software is essential to enterprise businesses, it is a popular target for more technically adept attackers and nation-state threat actors. More than a third of all intrusion events ReliaQuest responded to between 2022 and 2024 involved RMM tools, such as Atera, Splashtop, and Anydesk.

### Lateral Movement

The native integration of RDP⁵ in Windows systems, the ease with which RDP enables remote control of systems, and the frequent absence of usage restrictions all make it popular for threat actors seeking lateral movement.

RDP was seen in 34.3% of lateral-movement activity in our customer incidents.

RDP was seen in 34.3% of lateral-movement activity in our customer incidents. RDP can grant full graphical control of a system, which is particularly appealing for threat actors wanting to execute complex tasks, exfiltrate data, or deploy malware without a physical presence.

Another Windows-supported protocol that was frequently observed is SMB, which, when combined with RDP, accounted for 59.3% of all lateral movement activity. In one incident, a threat actor used RDPWinst, an open-source wrapper library tool designed to enable remote desktop host support, permitting concurrent RDP sessions. This tool is frequently subject to abuse, granting attackers an RDP connection to the targeted host for remote access and, potentially, lateral movement.

![Figure 12: Lateral-movement–related TTPs in 2023](Image description: A bar chart showing the most common Lateral Movement TTPs observed in 2023. RDP and SMB are the most frequently used protocols.)

14 Make Security Possible

---

### Impact

In attempts to manipulate, interrupt, or destroy systems and data, financial theft stood out as the primary objective in 2023, driving 88.4% of customer incidents.

Most attempts were unsuccessful, but cybercriminals pose a persistent threat; attackers motivated by financial gain—through ransomware, BEC, data theft, and cryptocurrency scams—present the most likely and immediate risks to any business operation. Beyond financial theft, threat actors attempted to impact ReliaQuest customers via data encryption (4.3% of incidents) and data manipulation (2.9%). But by comparison, it’s clear that the overwhelming focus of attacks is financial gain.

![Figure 13: Impact-related TTPs in 2023](Image description: A bar chart showing the most common Impact-related TTPs observed in 2023. Financial theft is the overwhelming primary motive.)

The broad rise in financially motivated threat activity prominently involves ransomware and data-theft extortion—the “Clop” ransomware group demonstrated remarkable success in soliciting ransom payments via data theft only.

2023 was a record-breaking year for ransomware activity; compared to 2022, ReliaQuest observed approximately 74.3% more organizations named on ransomware data-leak websites.

For guidance in mitigating financially motivated threats, such as ransomware and BEC, see the General Recommendations and Best Practices section.

15 Make Security Possible

---

# What We Observed & Forecast

This Section Provides an Overview of the Significant Threats Targeting our Customers in 2023, Case Studies, and a Forecast for 2024, Covering:

*   Extortion
*   Social engineering
*   Malware-free and LotL activity
*   TTP evolution

Our case studies include the findings from investigations into security incidents, methodically broken down by MITRE ATT&CK techniques.

In each investigation, we seek to determine the potential impact and corresponding response, thoroughly analyzing the incident to understand its nature, scope, and impact.

This entails investigating relevant data, such as logs, system artifacts, network traffic, and other sources of evidence.

16 Make Security Possible

---

# Business Email Compromise Making A Big Impact

In 2023, ReliaQuest observed a significant increase in BEC attacks. BEC typically involves sending phishing emails to deceive employees into making payments for fraudulent bills. Our investigation of incident metrics data revealed that attackers frequently use BEC-compromised email accounts to conduct additional phishing operations. This strategy is effective because it uses legitimate email addresses, which can easily pass basic security checks; the potential results include additional breaches and reputational damage.

Threat actors can initially compromise email accounts in various ways, including social engineering or phishing, but they typically rely on a generic credential harvester, combined with an AITM⁶ component, to bypass MFA. In some cases, credentials for accounts not protected by MFA are acquired via infostealers (information-stealing malware).

## The Threat

The impact of BEC goes beyond fraud-related financial loss: Brands can suffer severe reputational damage, and overall business integrity can also be harmed. Additionally, depending on an organization’s configurations, the compromise of a business email account can grant access to crucial services, posing even greater risks:

*   **VPN** – If no device certification is required, or additional access policies are not in place, attackers can gain unauthorized virtual private network (VPN) access.
*   **SSO** – When portal access is not limited to the VPN and is publicly accessible, threat actors can potentially access all SSO applications, exposing significant amounts of data and gaining the ability to affect business systems, whether in the cloud or on premises.

Most organizations conduct wire transfers and have email services accessible from external networks and personal devices; with BEC being relatively easy, requiring little overhead and offering an optimal risk-to-reward ratio, it’s an attractive prospect for a cybercriminal.

### Where Can Credentials Be Found?

Would-be attackers seeking account credentials have options besides social engineering and infostealers.

In a thriving criminal ecosystem of marketplaces, automated vending cart (AVC) services, and IABs, threat actors advertise and sell compromised credentials and RDPs, in addition to other illicitly gained material.

It is extremely simple to purchase methods of access to targeted organizations that can bypass MFA and other controls.

This makes it important for organizations to use IAM solutions, perimeter scanning (for services like RDP), and heuristic detections and controls focusing on network access.

The FBI’s Internet Crime Complaint Center (IC3) reported that in 2022, it received 21,832 BEC complaints, with adjusted losses exceeding $2.7 billion⁷. This almost certainly represents only a fraction of BEC events that have been reported to federal agencies.

17 Make Security Possible

---

The surge in BEC can be attributed to three primary factors:

*   **Phishing kits and services are widely available on criminal platforms, making it easier to execute BEC.** One notable phishing “shop” is W3LL Store, a site where threat actors offer a wide variety of phishing kits (see Figure 14). Kits have grown more sophisticated, capable of creating real-time clones of websites, simulating two-factor authentication prompts, dumping cookies, and bypassing a CAPTCHA. Many services are offered on a monthly subscription basis.

![Figure 14: Screenshot of phishing offerings available on the W3LL Store shop](Image description: A screenshot of a website displaying various phishing kits and services available for purchase.)

*   **Attackers can now automate several initial steps of the attack process, before human intervention becomes necessary to hijack an existing email thread.** Automation in cyber attacks has reduced attacker dwell time⁸, forcing security teams to conduct quicker and more frequent investigations to mitigate threats that previously allowed more response time.
*   **Cybercriminals are increasingly relying on such services as “BulletProofLink” (aka BulletProftLink or Anthrax): a well-known PhaaS offering of a wide range of tools and features that support BEC, including templates, hosting services, and automation tools.** Such resources enable the threat actor to execute BEC campaigns more efficiently and effectively. BEC threat actors frequently use VPN services, often employing five or six of them for a single account compromise. By acquiring IP addresses that match the locations of their victims, cybercriminals can effectively blend into targets’ environments using VPNs and proxies. This adds an additional layer of anonymity to threat actors’ activities and makes it challenging to trace their origins.

## Stopping BEC Attacks

To safeguard against BEC attacks, take a multilayered approach to security:

*   **Enhance system-wide logging**: Ensuring logging for all emails, rules, and events related to mailbox manipulation.
*   **Configure forward proxy devices to block access to high-risk domain categories, such as newly registered domains.**
*   **Implement device certificates with CA trust, renewal, and MFA to thwart BEC attacks.**
*   **Regularly train employees to be aware of and report BEC tactics.**
*   **Enforce verification protocols for financial transactions and sensitive data exchanges.**

18 Make Security Possible

---

## Case Study: Storm-1167’s AITM Phishing Campaign Brings BEC

In October 2023, ReliaQuest notified a customer of an incident where an attacker sent more than 1,000 phishing email messages to the customer’s users via a compromised third-party business email account. The attack, linked to the “Storm-1167” threat actor through known infrastructure domains, tricked victims with a phishing link that led to a fake Microsoft sign-in page, capturing their session tokens. The attacker used these tokens to access internal email accounts and cloud services.

A compromised internal account was then used to send 1,300 additional emails with a credential harvester, suggesting an attempt to target higher-privilege accounts and widen the attack’s impact. ReliaQuest escalated this incident and advised the customer’s security team to rotate account credentials, block the sender and domain, and purge emails from recipients’ inboxes.

*   **Initial Access**: To initially access the targeted organization, Storm-1167:
    *   Deployed an AITM phishing kit.
    *   Sent phishing emails that resulted in compromised credentials.
*   **Execution**: To gain execution, Storm-1167 relied on user interaction by using a phishing email to induce the recipient to click a malicious link.
*   **Defense Evasion**: To delay detection and maintain access, Storm-1167 created email rules to auto-forward emails containing specific keywords to a designated folder.
*   **Lateral Movement**: To access additional accounts and increase their footprint within the environment, Storm-1167 conducted internal spearphishing.
*   **Collection & Credential Access**: To steal and collect credentials, Storm-1167 hosted a malicious Microsoft credential harvester designed to capture account information and session data.

19 Make Security Possible

---

## Forecast

BEC attacks will very likely become more frequent in 2024. They are becoming more sophisticated, and generative AI (GenAI) technology will help craft more believable messages. In particular, GenAI will help mimic communication styles and languages unfamiliar to attackers, making fake interactions much harder to detect. Malicious AI tools are now readily available in forums (see Figure 17).

GenAI also has the potential to automate spearphishing tactics used in BEC. Machine-learning algorithms can analyze vast amounts of personal information available online, to create personalized profiles of victims. By “learning” a target’s preferences, relationships, and activities, AI systems can craft highly deceptive emails.

BEC attacks can manifest through phone calls (vishing, or voice phishing), email messages, and text messages. AI systems can now replicate a voice using a sample; fraudulent calls with cloned voices impersonating family members have already been reported⁹, as well as video-call deepfakes.¹⁰ Threat actors will likely use such techniques to deceive businesses in 2024.

# Extortion Threat Looms Large

Cyber extortion has posed a very high threat to organizations since the beginning of double extortion¹¹ and big game hunting.¹² This threat has continually increased, as numerous financially motivated threat actors have entered the lucrative ransomware business. In 2022, it was estimated that these threat actors earned more than $500 million from ransom payments.¹³ Projections from the same source for 2023 suggest that ransomware profits could approach a staggering $900 million: an 80% increase.

## The Threat

In 2023, ransomware and other means of cyber extortion persisted as significant threats to organizations, with more than 4,800 companies named on dark-web data-leak websites.¹⁴ That’s 74.3% more than were named in 2022. Double extortion continued to be a prevalent ransomware technique, but the Clop group has demonstrated success in single-extortion campaigns. Clop stole data from hundreds of organizations by exploiting zero-day vulnerabilities in MOVEit and GoAnywhere software.

Throughout the reporting period, extortion groups posed a high threat to critical sectors. More than 140 government organizations were named on data-leak sites, and the “Rhysida” ransomware group launched numerous campaigns targeting healthcare organizations. The threats to critical sectors further intensified after the “ALPHV” group removed its restrictions on targeting certain sectors following an FBI seizure of its data-leak site.

Ransomware activity soared to new heights; in the second quarter of 2023, we observed a record-breaking 1,378 compromised organizations named on ransomware data-leak sites. LockBit became the first ransomware group to name more than 1,000 companies within a year. The surge has probably been driven by the growth of ransomware operations and victims’ increasing reluctance to pay ransom demands, resulting in more compromised entities named.

20 Make Security