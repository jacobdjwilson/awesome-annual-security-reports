# Attacks From All Angles

## 2021 Midyear Cybersecurity Report

## Table of Contents
- [Contents](#contents)
- [Modern Ransomware Attacks Prompt Multi-State Emergency Responses and Multimillion Dollar Payouts](#modern-ransomware-attacks-prompt-multi-state-emergency-responses-and-multimillion-dollar-payouts)
- [How Active Were Ransomware Actors in the First Half of 2021?](#how-active-were-ransomware-actors-in-the-first-half-of-2021)
- [How Did Modern Ransomware Spread in the First Half of 2021?](#how-did-modern-ransomware-spread-in-the-first-half-of-2021)
- [How Was Data Exfiltrated in 2021?](#how-was-data-exfiltrated-in-2021)
- [How Were Legitimate Tools Misused by Ransomware Gangs?](#how-were-legitimate-tools-misused-by-ransomware-gangs)
- [Enterprise and Government Response to Ransomware Attacks](#enterprise-and-government-response-to-ransomware-attacks)
- [Ransomware Arrests: Egregor, Clop, Emotet](#ransomware-arrests-egregor-clop-emotet)
- [APTs Find Exploitable Cracks in Online Portals and Webmail Servers](#apts-find-exploitable-cracks-in-online-portals-and-webmail-servers)
- [TeamTNT](#team-tnt)
- [Water Pamola](#water-pamola)
- [Earth Wendigo](#earth-wendigo)
- [Earth Vetala](#earth-vetala)
- [Iron Tiger](#iron-tiger)
- [PlugX](#plugx)
- [A Look at Upgraded Criminal Campaigns and Unexplored Flaws in Unsecured Technology](#a-look-at-upgraded-criminal-campaigns-and-unexplored-flaws-in-unsecured-technology)
- [XCESSET](#xcesset)
- [PandaStealer](#pandastealer)
- [Covid-19-Related Scams and Fake Products](#covid-19-related-scams-and-fake-products)
- [Unexplored Risks and Unpatched Flaws](#unexplored-risks-and-unpatched-flaws)
- [SHAREit flaw](#shareit-flaw)
- [LoRaWAN](#lorawan)
- [5G Campus Networks](#5g-campus-networks)
- [VPNFilter](#vpnfilter)
- [Widely Used and Vulnerable Technology Actively Attacked Through Critical Flaws](#widely-used-and-vulnerable-technology-actively-attacked-through-critical-flaws)
- [Windows 11](#windows-11)
- [VPN Vulnerabilities](#vpn-vulnerabilities)
- [Old Cloud Threats Reemerge to Find New Targets](#old-cloud-threats-reemerge-to-find-new-targets)
- [TeamTNT](#team-tnt-1)
- [Linux](#linux)
- [Attacks From All Angles Require Multifaceted Defenses](#attacks-from-all-angles-require-multifaceted-defenses)
- [The Threat Landscape in Review](#the-threat-landscape-in-review)
- [References](#references)

---

## Contents

4
Modern Ransomware Attacks Prompt

Multi-State Emergency Responses and

Multimillion Dollar Payouts

14
APTs Find Exploitable Cracks in Online

Portals and Webmail Servers

19
A Look at Upgraded Criminal Campaigns

and Unexplored Flaws in Unsecured

Technology

27
Widely Used and Vulnerable Technology

Actively Attacked Through Critical Flaws

32
Old Cloud Threats Reemerge to Find

New Targets

37
Attacks From All Angles Require

Multifaceted Defenses

39

The Threat Landscape in Review

Published by
Trend Micro Research

Stock image used under license from

Shutterstock.com

TREND MICRO LEGAL DISCLAIMERThe information provided herein is for general information and educational purposes only. It is not intended and should not be construed to constitute legal advice. The information contained herein may not be applicable to all situations and may not reflect the most current situation. Nothing contained herein should be relied on or acted upon without the benefit of legal advice based on the particular facts and circumstances presented and nothing herein should be construed otherwise. Trend Micro reserves the right to modify the contents of this document at any time without prior notice.Translations of any material into other languages are intended solely as a convenience. Translation accuracy is not guaranteed nor implied. If any questions arise related to the accuracy of a translation, please refer to the original language official version of the document. Any discrepancies or differences created in the translation are not binding and have no legal effect for compliance or enforcement purposes.Although Trend Micro uses reasonable efforts to include accurate and up-to-date information herein, Trend Micro makes no warranties or representations of any kind as to its accuracy, currency, or completeness. You agree that access to and use of and reliance on this document and the content thereof is at your own risk. Trend Micro disclaims all warranties of any kind, express or implied. Neither Trend Micro nor any party involved in creating, producing, or delivering this document shall be liable for any consequence, loss, or damage, including direct, indirect, special, consequential, loss of business profits, or special damages, whatsoever arising out of access to, use of, or inability to use, or in connection with the use of this document, or any errors or omissions in the content thereof. Use of this information constitutes acceptance for use in an “as is” condition.

Cybercriminals across the board were busy in the first half of 2021, with no signs of slowing down. Within the last six months, we saw a ransomware group shut down a major gas provider and leave half of the US East Coast without fuel. Other ransomware operators used double extortion tactics to get million-dollar payouts from enterprises. Advanced persistent threat (APT) teams compromised integral enterprise tools like Amazon Web Services (AWS) cloud servers, Kubernetes, and a popular webmail platform in Asia, all with different agendas: Some attempted to steal financial account information, while others attempted to load cryptocurrency miners. Critical bugs in major server clients and in popular printer technology were also exploited.

Our research into the first few months of the year examines dangerous vulnerabilities across different types of devices and operating systems, including the threats targeting these flaws. One example of this is our three-part investigation into the security of low-powered Long Range Wide Area Network (LoRaWAN) technology that is widely used in internet of things (IoT) configurations around the world. We also analyzed threats aimed at new Mac devices, specifically machines that use ARM64 architecture, as well as vulnerabilities in Windows operating systems and Linux machines.

Covid-19 threats continued as well, as pandemic-themed scams began revolving around a much-awaited vaccine and plans about its distribution rather than the disease-focused topics previously seen in 2020. Indeed, though the discovery of the vaccine has created a new sense of optimism, vigilance in securing the cybersecurity threshold remains indispensable.

In looking back at the threats that surfaced in the past six months, we hope that our midyear report encourages both enterprises and ordinary users to build a better and more effective defense that covers all angles of their security posture.

## Modern Ransomware Attacks Prompt Multi-State Emergency Responses and Multimillion Dollar Payouts

Modern ransomware continues to be a significant threat to enterprises and government organizations. Cybercriminal groups have taken on more sophisticated business models and adopted new technologies to create efficient and stealthy ransomware attacks. These evolved attacks have certain features that separate them from traditional ransomware activities: data exfiltration rather than simple encryption, covert online collaboration, the extended use of affiliate programs, and APT-like victim targeting, among others.¹

Most notably, in the first half of the year we saw modern ransomware actors successfully extorting companies and extracting valuable enterprise data using a double extortion technique: On top of demanding ransom in exchange for decrypting data, attackers placed increased duress on their victims by threatening to release their private data on a leak site. Enterprises that hold valuable intellectual property will view this as a serious concern, as data leaks come with regulatory penalties, lawsuits, and reputational damage. We also saw the rise of triple distributed denial-of-service (DDoS) attacks and quadruple extortion models to harass customers and increase their possibility of payment.

We researched the ransomware-as-a-service (RaaS) sites of 16 ransomware actors² and investigated how these actors extort money from their victims. Some keep terabytes of stolen data online for over a year and threaten to leak increasing amounts of data over time, though most keep stolen data publicly available for several months. Some of these data leak sites are on Tor-hidden servers, while others are hosted using bulletproof hosting. RaaS actors also use commercially available and free file-sharing platforms, or even host files on websites on the clear web.

4 | Attacks From All Angles: 2021 Midyear Cybersecurity Report

### How Active Were Ransomware Actors in the First Half of 2021?

Our data shows that over 7.3 million ransomware threats were detected in the first six months of 2021, which is almost half the number of detections we found in the same period in 2020. There are several factors that might have contributed to this decrease. First, it signals the shift to the more targeted modern ransomware³ that we have been analyzing, which involves attackers moving from the less effective, quantity-focused model of ransomware to big-game hunting. We can also attribute this decrease to an improvement in the detection and blocking capabilities of security solutions. Threats were stopped and blocked before they even reached users, and so detections also dropped. It’s important to note that modern ransomware uses phishing and exploits as the first step in the infection process, so when security solutions block this initial intrusion, the deployment of ransomware is prevented. Furthermore, an incident with the DarkSide ransomware brought heightened attention to ransomware operators, which might have prompted some of them to lie low. Meanwhile, law enforcement agencies across the world conducted a series of ransomware operations takedowns that might have left an impact on wide-reaching active groups.

The WannaCry and Locky families made up most of the detection count, continuing the trend we saw in our 2020 Annual Roundup.⁴ WannaCry is a familiar threat that started plaguing enterprises and users since 2017; however, this year, there was a marked decrease in WannaCry detection numbers. The longevity of this family shows how long a network worm can persist if devices are not patched properly, even when the actors are not maintaining the attack.

Meanwhile, DarkSide, Nefilim, and Conti are also among the top 10 families detected in this period and stand out significantly in terms of attack scope, tools, and techniques.

In terms of targeted industries, ransomware actors focused on many of the same sectors as last year. The most affected organizations were in banking, government, and manufacturing. We saw a surge in ransomware attempts on banking groups, although RaaS is opportunistic with regard to its targeting style. This means that attackers are not likely singling out banking businesses in particular.

![A half-year comparison of total detected ransomware monthly threats by layer](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/threat-reports/roundup/attacks-from-all-angles-2021-midyear-security-roundup/~/media/trendmicro/global/security-content/research-and-analysis/threat-reports/roundup/attacks-from-all-angles-2021-midyear-security-roundup/images/figure1.png)
*Figure 1. A half-year comparison of total detected ransomware monthly threats by layer*

![The differences in modern and premodern ransomware](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/threat-reports/roundup/attacks-from-all-angles-2021-midyear-security-roundup/~/media/trendmicro/global/security-content/research-and-analysis/threat-reports/roundup/attacks-from-all-angles-2021-midyear-security-roundup/images/figure2.png)
*Figure 2. The differences in modern and premodern ransomware*

![File-only count of ransomware family detections in the first half of 2020 compared to the first half of 2021](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/threat-reports/roundup/attacks-from-all-angles-2021-midyear-security-roundup/~/media/trendmicro/global/security-content/research-and-analysis/threat-reports/roundup/attacks-from-all-angles-2021-midyear-security-roundup/images/figure3.png)
*Figure 3. File-only count of ransomware family detections in the first half of 2020 compared to the first half of 2021*
*Source: Trend Micro™ Smart Protection Network™ infrastructure*

![The top three malware families that affected the top five industries in the first half of 2020 and the first half of 2021](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/threat-reports/roundup/attacks-from-all-angles-2021-midyear-security-roundup/~/media/trendmicro/global/security-content/research-and-analysis/threat-reports/roundup/attacks-from-all-angles-2021-midyear-security-roundup/images/figure4.png)
*Figure 4. The top three malware families that affected the top five industries in the first half of 2020 and the first half of 2021*

5 | Attacks From All Angles: 2021 Midyear Cybersecurity Report

The Nefilim ransomware continued to target companies with billion-dollar yearly revenues, a tactic that we analyzed as the model for modern ransomware.⁵ In May, the DarkSide⁶ ransomware shut down Colonial Pipeline, a company responsible for providing fuel to nearly half the US East Coast. As a result, the Federal Motor Carrier Safety Administration (FMCSA) had to declare a state of emergency in 18 states to help with the shortages. The incident was so considerable that it spawned a group that posed⁷ as DarkSide and sent extortionist emails to companies’ generic email addresses. There was also DarkSide Linux,⁸ another version of the ransomware that targets files related to virtual machines (VMs) on VMware ESXI servers. It kills VMs, encrypts files on the infected machine, collects system information, and sends it to a remote server. Meanwhile, Conti⁹ is known as the successor to the popular Ryuk ransomware family, with its threat actors victimizing targets using the same methods used with Ryuk. In fact, Trickbot, Emotet, and BazarLoader are now used to distribute Conti.

In the succeeding sections, we discuss these families, as well as other ransomware attacks and developments that were significant in the first half of 2021. The tactics and tools used to conduct these malicious activities show how ransomware has evolved over the years.

### How Did Modern Ransomware Spread in the First Half of 2021?

Modern ransomware attackers are now becoming more mature by using APT-level tools and techniques to access and move deeper into the victim’s system, exfiltrate data, and then deliver their payloads. In May 2021, we saw that the Microsoft Exchange Server vulnerability called ProxyLogon,¹⁰ discovered in 2020, was used to deliver three types of malware, including the BlackKingdom ransomware. One other example is the aforementioned ransomware Conti,¹¹ which targeted Ireland’s Department of Health in May.¹² Conti has been seen compromising victims through firewall vulnerabilities CVE-2018-13379 and CVE-2018-13374, which are more sophisticated entry points than traditional ransomware. After exploiting the vulnerable firewall, the ransomware tries to move laterally within the system.

REvil or Sodinokibi¹³ was yet another modern ransomware that was active throughout 2021, specifically targeting tech company Acer in March, Apple in April, and the world’s largest meat processor, JBS, in June.¹⁴ This family also used techniques that indicate a targeted approach. For example, it used the remote code execution (RCE) CVE-2019-2725 vulnerability, and we observed that it was loaded in the memory of PowerShell through reflective-load instead of binary execution. The Hello ransomware,¹⁵ which uses .hello as its extension, arrives at a target system via Microsoft SharePoint vulnerability CVE-2019-0604. Our analysis revealed that after the exploit is abused for intrusion, the China Chopper web shell (detected by Trend Micro as Backdoor.ASP.WEBSHELL.SMYAAIAS) is deployed to execute PowerShell commands to facilitate the succeeding malicious actions and ultimately push the payload.

Sophisticated methods of accessing and entering an organization sometimes come from a source outside the group that actually creates or distributes the ransomware. This is where affiliate programs come in. These programs, which flourished in the first half of 2021, are basically collaborations that allow actors to share their tools, such as customizable software, new and readily available technologies for improved victim-targeting, and more. Specifically, we saw many actors with access to compromised assets (such as avenues into a victim’s network) collaborate with other actors who hold ransomware. Nevertheless, while this means that certain cybercriminals can take advantage of other groups’ tools and resources, there are downsides to this option.

For example, the high-profile DarkSide attacks in May had multiple victims apart from Colonial Pipeline, and it was reported that there were different affiliate groups behind the attacks. This is one of the issues that arise with affiliate programs: The ransomware group does not have oversight into the victims of its partners. For its part, the DarkSide group apologized¹⁶ and said that it will target less controversial organizations in the future, adding that it will start checking companies that its partners want to target and encrypt.

It should be noted that these ransomware also use traditional means to gain initial access into a victim’s system: malspam emails with spear-phishing links or attachments, remote desktop protocol (RDP) access that uses valid accounts, compromised websites, and others.

### How Was Data Exfiltrated in 2021?

After initial access, lateral movement within a victim’s system is a key phase in the modern ransomware process. Groups use this movement either to identify valuable data within the victim organization for exfiltration, or to drop malicious payloads. In the case of most modern ransomware, after gaining initial access, additional tools are downloaded. Nefilim, Conti, and Hello all use Cobalt Strike beacons. They are typically used to establish a remote connection to the environment, tag valuable data, and execute commands. We observed that Sodinokibi uses RDP and PsExec for lateral movement, dropping and executing other components and the ransomware itself. Conti operators also remotely create the scheduled tasks of the payload (which can include Cobalt Strike, KillAV scripts, and Conti) that can be remotely executed using scheduled tasks and batch files.

> **Predictions**
> In our security predictions last year, we speculated that there would be an increase in sophisticated attacker groups relying on penetration testing tools. We also predicted that Cobalt Strike, the source code for which was allegedly leaked in the second half of 2020, would be among these tools.

Data exfiltration and extortion tactics differ from the various ransomware families we saw in 2021. Typically, however, the data is used in double extortion schemes — the ransomware actors post the stolen information from non-paying victims on data leak sites as a way of pressuring them further into paying the ransom. These data leak sites are on public file-sharing platforms and sometimes on the clear web. We also noted that the exfiltration tools used by ransomware groups are usually open-source, free public resources.

For example, we found that Conti operators use the cloud storage synchronization tool Rclone to upload files to the Mega cloud storage service. Similarly, DarkSide operators use Mega client for exfiltrating files to cloud storage, 7-Zip for archiving, and PuTTY application for network file transfers.

After data is exfiltrated, the payload is dropped. Many modern ransomware actors take over networks in multiple human-supervised stages, unlike with traditional attacks that use click-on-the-link automatic events. They spend weeks or even months conquering different parts of the victim’s network before they execute the ransomware payload. This is another feature that makes modern ransomware attacks seem like nation-state APT attacks. One example of this is the Nefilim¹⁷ ransomware, which stays silently working in the victim’s network for weeks to fully exfiltrate the data before executing the ransomware payload.

### How Were Legitimate Tools Misused by Ransomware Gangs?

We mentioned previously that ransomware distributors sometimes use legitimate tools to perform malicious activities, but the scope of misuse is worth exploring further. On their own, most of the tools exploited by ransomware are used to help in security research or to improve efficiency. Many of them are open-source and can be used and modified by the public freely. Conversely, the features that make them good tools also make them useful for cybercriminals.¹⁸

| Tool          | Intended use                                                              | How it is used for ransomware campaigns                                                                                             | Ransomware campaigns that used this tool