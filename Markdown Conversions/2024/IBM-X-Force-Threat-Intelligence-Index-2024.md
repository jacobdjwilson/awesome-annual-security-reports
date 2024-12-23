# X-Force Threat Intelligence Index 2024

## Table of Contents
- [Executive summary](#executive-summary)
- [Report highlights](#report-highlights)
- [Top initial access vectors](#top-initial-access-vectors)
- [Top actions on objectives](#top-actions-on-objectives)
- [Top impacts](#top-impacts)
- [Cyberwarfare](#cyberwarfare)
- [Generative AI: The new cyberthreat frontier](#generative-ai-the-new-cyberthreat-frontier)
- [Geographic trends](#geographic-trends)
- [Industry trends](#industry-trends)
- [Recommendations](#recommendations)
- [About us](#about-us)

## Executive summary
The biggest shift the IBM® X-Force® team observed in 2023 was a pronounced surge in cyberthreats targeting identities. Attackers have a historical inclination to choose the path of least resistance in pursuit of their objectives. In this era, the focus has shifted towards logging in rather than hacking in, highlighting the relative ease of acquiring credentials compared to exploiting vulnerabilities or executing phishing campaigns. Lack of identity protections was corroborated by IBM X-Force penetration testing data for 2023, which ranked identification and authentication failures as the second most common finding.

Additionally, X-Force observed a 100% increase in “Kerberoasting" during incident response engagements. Kerberoasting is a technique focused on compromising Microsoft Windows Active Directory credentials through Kerberos tickets. This indicates a technique shift in how attackers are acquiring identities to carry out their operations.

The prominence of valid accounts as a preferred initial access technique among cybercriminals—tying with phishing for the first time—was another notable development. This access technique is accompanied by an upsurge in malware designed to steal information, known as infostealer malware, activities that bolster the dark web’s stolen credentials marketplace. This multifaceted shift underscores the symbiotic relationship among various elements in the cybercrime ecosystem.

It’s clear that attackers have recognized the difficulty defenders have in distinguishing between legitimate identity use and unauthorized misuse. This escalation in targeting of identities in cyberattacks underscores the critical importance for organizations to proactively identify, eliminate and audit potential attack vectors within their dynamic networks. These measures are pivotal in reducing the attack surface, unveiling latent risks and autonomously remediating incidents that are independent of impending threats.

Last year will also go down in history as a generative artificial intelligence (gen AI) breakout year. Policy makers, business executives and cybersecurity professionals are all feeling the pressure to adopt AI within their operations. And the rush to adopt gen AI is currently outpacing the industry’s ability to understand the security risks these new capabilities will introduce. However, a universal AI attack surface will materialize once adoption of AI reaches a critical mass, forcing organizations to prioritize security defenses that can adapt to AI threats at scale.

In an attempt to identify key milestones that will indicate when a common AI threat landscape will mature, X-Force assessed previous technology disrupters and their threat maturity milestones. Based on the analysis, X-Force predicts threat actors will begin to target AI broadly once the market coalesces around common deployment models and a small number of vendors. This analysis suggests that AI market dominance is the milestone that will trigger attacker investment in attack toolkits targeting AI.

Despite looming gen AI-enabled threats, X-Force hasn’t observed any concrete evidence of generative AI-engineered cyberattacks to date or a rapid shift in attackers’ goals and objectives from previous years. Although X-Force observed a notable drop in ransomware attacks on enterprises in 2023, extortion-based attacks continue to be a driving force of cybercrime this past year. These extortion-based attacks were only surpassed by data theft and leak as the most common impact observed in X-Force incident response engagements globally.

The IBM X-Force Threat Intelligence Index offers these insights as a resource to IBM clients, researchers in the security industry, policy makers, the media and the broader community of security professionals and business leaders. It’s our intent to keep all parties informed of the current threat landscape so they can make the best decisions for reducing risk.

## Report highlights
- **Increase year over year in volume of attacks using valid credentials**: For the first time ever, abusing valid accounts became cybercriminals’ most common entry point into victim environments. It represented 30% of all incidents X-Force responded to in 2023.
- **Drop in enterprise ransomware incidents**: Despite remaining the most common action on objective (20%), X-Force observed a drop in enterprise ransomware incidents. This drop is likely to impact adversaries’ revenue expectations from encryption-based extortion as larger organizations are stopping attacks before ransomware is deployed and opting against paying and decrypting in favor of rebuilding if ransomware takes hold.
- **Percentage of data theft and leak incidents**: Data theft and leak rose to the most common impact for organizations, indicating more groups are favoring this method to obtain financial gains.
- **Upsurge in use of infostealers**: X-Force has observed threat groups who have previously specialized in ransomware showing increasing interest in infostealers. And a number of prominent new infostealers recently debuted and demonstrated increased activity in 2023, such as Rhadamanthys, LummaC2 and StrelaStealer.
- **Share of security misconfigurations among web application vulnerabilities identified**: X-Force penetration testing engagements revealed that the most observed web application risk across client environments globally was security misconfigurations. Of these misconfigurations, the top offenses included allowing concurrent user sessions in the application, which could weaken multifactor authentication (MFA) through session hijacking.
- **Percentage of incidents that involved malicious use of legitimate tools**: Nearly one-third of incidents that X-Force responded to were cases where legitimate tools were used for malicious purposes, such as credential theft, reconnaissance, remote access or data exfiltration.
- **Market share threshold likely to trigger attacks against AI platforms**: X-Force analysis indicates that the establishment of AI market dominance will signal AI attack surface maturity. This analysis suggests that once a single AI technology approaches 50% market share, or when the market consolidates to three or less technologies, the cybercriminal ecosystem will be incentivized to invest in developing tools and attack paths targeting AI technologies.
- **Share of manufacturing attack incidents within the top 10 attacked industries**: Manufacturing was once again the top attacked industry in 2023 for the third year in a row, representing 25.7% of incidents within the top 10 attacked industries. Malware was the top action on objective observed at 45%. Ransomware accounted for 17% of incidents.
- **Percentage of critical infrastructure incidents where initial access vector could have been mitigated**: For a majority of incidents on critical infrastructure that X-Force responded to, the initial access vector could have been mitigated with best practices and security fundamentals, such as asset and patch management, credential hardening and the principle of least privilege.
- **Increase in attacks year over year in Europe**: Europe also experienced the highest percentage of incidents (32%) out of the five geographic regions. Malware was the most observed action on objective accounting for 44% of incidents.

## Top initial access vectors
One of the top initial access vectors in 2023—jumping from third to first place—was the abuse of valid accounts identified in 30% of the observed incidents X-Force responded to. As defenders increase their detection and prevention capabilities, attackers are finding that obtaining valid credentials is an easier route to achieving their goals, considering the alarming volume of compromised yet valid credentials available—and easily accessible—on the dark web. X-Force found that cloud account credentials alone make up 90% of for sale cloud assets on the dark web, making it easy for threat actors to take over legitimate user identities to establish access into victim environments. Attacker use of valid accounts as an initial access vector appears to have a significant impact on the required response efforts, as well.

![Figure 1: Top initial access vectors X-Force observed in 2022 and 2023. Sources: X-Force and MITRE ATT&CK Matrix1 for Enterprise framework]

Top initial access vectors in 2023 versus 2022
- **2023**
  - Valid accounts (T1078): 30%
  - Phishing (T1566): 30%
  - Exploit public-facing application (T1190): 29%
  - External remote services (T1133): 9%
  - Drive-by compromise (T1189): 3%
  - Trusted relationship (T1199): 3%
  - Replication through removable media (T1091): 1%
- **2022**
  - Phishing (T1566): 41%
  - Exploit public-facing application (T1190): 26%
  - Valid accounts (T1078): 16%
  - External remote services (T1133): 12%
  - Drive-by compromise (T1189): 1%
  - Trusted relationship (T1199): 1%
  - Replication through removable media (T1091): 4%

In 2023, major incidents where the attacker leveraged a valid account for initial access were associated with more complex response measures by defenders—190% greater than the average incident.

As we will analyze further in the report, we identified a concerning trend in the rise of infostealers and ransomware groups pivoting to infostealing malware. These shifts suggest that threat actors have revalued credentials as a reliable and preferred initial access vector. As threat actors invest in infostealers to grow their credential repository, enterprises are pushed into a new defense landscape where identity can no longer be guaranteed.

Phishing, whether through an attachment, link or as a service, also comprised 30% of all incidents remediated by X-Force in 2023. Although tied for first place in 2023, the volume of phishing is down by 44% from 2022.

The significant drop in observed compromises through phishing is likely a reflection of both continued adoption and revaluation of phishing mitigation techniques and strategies, as well as attackers shifting to the use of valid credentials to gain initial access. Using compromised valid credentials is a quick, direct route into the environment. Whereas IBM X-Force Red data indicates that human-crafted phishing emails are time-intensive, requiring on average 16 hours to craft one. However, it’s worth noting that X-Force assesses that phishing is expected to be one of the first malicious use cases of AI that cybercriminals will invest in, theorizing that it’s far from done scaling. In fact, X-Force data shows that AI can generate a deceptive phish in 5 minutes, a potential time savings of nearly 2 days for attackers.

Furthermore, X-Force responded to multiple cases involving email compromises that circumvented MFA measures using adversary-in-the-middle (AitM) attacks. These attacks started with an initial phishing message that directed users to a reverse-proxy phishing page, which allowed attackers to relay traffic between the user and the legitimate site and thus collect user credentials, MFA input and session cookies. In multiple cases, X-Force observed the threat actor leverage their initial access to carry out both internal and external phishing attempts, as well as further abuse of credentials, to access additional applications.

New to the 2024 IBM X-Force Threat Intelligence Index, X-Force reviewed hundreds of findings from our penetration testing data to reveal the top Open Worldwide Application Security Project (OWASP) web application security risks. The most observed risk across client environments globally was security misconfigurations, accounting for 30% of total findings. Of this category, penetration testers found more than 140 findings of ways that attackers can exploit misconfigurations. Of these misconfigurations, the top offenses included allowing concurrent user sessions in the application at 15%, which could weaken MFA through session hijacking, verbose error messages at 12% and excessive session timeouts at 8%.

In second place, identification and authentication failures made up 21% of the most observed web application security risks. Of these findings, the top offenses were weak password policies that included Active Directory password policies (19%), usernames verifiable through errors (17%), Server Message Block (SMB) signing not required and URLs containing sensitive information at 8% each.

![Figure 2. Top OWASP web application security risks based on penetration testing data. Source: X-Force]

Security misconfigurations top web application risk

In third place, exploitation of public-facing applications—defined as adversaries taking advantage of a weakness in an internet-facing computer or program—was identified in 29% of incidents, which is slightly higher than what we observed in 2022.

In 2023, numerous organizations experienced cyberattacks as a result of widespread exploitation of managed file transfer (MFT) tools, such as MOVEit and GoAnywhere. MFT exploitation poses a high risk, as these internet-connected file transfer services facilitate the immediate access of sensitive enterprise data by attackers. Until 2023, many defenders overlooked the high-risk nature of MFT tools, leading to inadequately protected deployments without proper detection and response strategies. This lack of consideration provided threat actors with a significant time advantage, allowing them to scale their attacks undetected. Last year’s mass exploitation of MFTs, and the ongoing efforts of ransomware groups focusing on data extortion, underscore the need for organizations to fully understand their enterprise architecture. To facilitate this understanding, organizations should develop threat models that map out their systems and the associated attack paths to their sensitive data stored on premises, in the cloud, or through third parties.

Every year there are a few vulnerabilities that catch enterprises by surprise and cause widespread damage. In 2023, the CL0P ransomware group exploited a vulnerability in the file transfer application MOVEit, common vulnerabilities and exposures (CVE)-2023-34362, to expose information on millions of individuals.

![Figure 3: The growth of vulnerabilities, exploits and zero days since 1993. Also included is a timeline of major events involving vulnerabilities since 1993. The X-Force Vulnerability Database is one of the oldest and largest vulnerability databases in the world and reached its 30-year anniversary in 2023.]

Zero-day decline

While zero-day vulnerabilities garner notoriety, the reality is that zero-day vulnerabilities make up a very small percentage of the vulnerability attack surface—currently at 3% of total vulnerabilities tracked by X-Force. In 2023, there was a 72% drop in the number of zero days compared to 2022 with only 172 new zero-day vulnerabilities. Furthermore, from 2021 to 2022, there was a 44% decrease of new zero-day vulnerabilities, from 1,105 CVEs added in 2021 to 614 CVEs added in 2022. This decrease is likely indicative of attackers finding other less resource-intensive methods to gain entry, such as exploitation of older vulnerabilities or use of valid credentials, compromised or purchased.

The vulnerability problem
- **Category** | **Number** | **%**
- Total vulnerabilities | 260,473 | N/A
- Total vulnerabilities with weaponized exploits | 84,245 | 32%
- Total zero days | 7,506 | 3%
- Critical | 2,872 | 1%
- High | 100,609 | 39%
- Medium | 130,553 | 50%
- Low | 25,781 | 10%
- Cumlative vulnerabilities, exploits and zero days since 1988

The importance of securing Linux® systems has risen in prominence as increasing amounts of malicious activity targeting Linux have appeared. Malware developers are increasingly developing Linux malware and creating Linux variants of existing malware families. These changes to the Linux threat landscape highlight the criticality of systems hardening and monitoring for malicious activity.

Methodical vulnerability management is a key aspect of proactive defense. According to Red Hat® Insights vulnerability data from 2023, 92% of customers were found to have at least one CVE with known exploits in their environment at the time of scanning. Furthermore, 81% had three or more CVEs with known exploits in their environment. More than half (67%) had at least one CVE rated as Critical, while 25% had five or more Critical CVEs in their environment. Additionally, the majority (80%) of the top ten vulnerabilities with the highest number of hits detected across systems in 2023 were given a High or Critical Common Vulnerability Scoring System (CVSS) base severity score.

Most threat activity targeting Red Hat Enterprise Linux systems in 2023 was associated with widely distributed threats. According to statistics from the Red Hat Insights malware detection service, the top threats detected were Linux rootkits, malware associated with the recently dismantled IPStorm botnet, which enabled proxying of malicious traffic through compromised devices, and the PGMiner cryptocurrency mining botnet.

![Figure 4: Percentage of client environments with Critical CVEs or CVEs with known exploits. Source: Red Hat Insights]

Linux vulnerabilities

## Top actions on objectives
According to IBM X-Force Incident Response data, deployment of malware was the most common action threat actors took on victim networks, occurring in 43% of all reported incidents. Of the total incidents, 20% were ransomware cases. Backdoors and crypto miners were discovered in 6% and 5% of cases, respectively. The remaining malware incidents included infostealers, loaders, bots, worms, web shells and downloaders.

![Figure 5: Top actions on objectives observed by X-Force in 2023. Incidents can have more than one top action on objective observed. Source: X-Force]

Top actions on objectives 2023
- **Malware** 43%
  - 20% Ransomware
  - 6% Backdoor
  - 5% Cryptominer
  - 4% Infostealer
  - 4% Loader
  - 4% Bot
  - 3% Other
  - 2% Downloader
  - 2% Webshell
  - 2% Worm
- **Tools** 32%
  - 13% Credential theft (credential acquisition)
  - 10% Remote access
  - 6% Recon and scanning
- **Server access** 18%
- **Data exfiltration** 11%
- **BEC** 7%
- **Spam campaign** 6%

Although X-Force responded to less ransomware cases in 2023, down 11.5% year over year, ransomware and ransomware-affiliated groups continued to target organizations globally, with multiple variants receiving upgrades to expand their targeting and functionality. The top ransomware variants observed by X-Force were BlackCat, CL0P, LockBit, BlackBasta and Royal.

In 2022, ransomware was topped slightly by backdoors as the top attack X-Force responded to after dominating the IBM X-Force Incident Response activity since 2018. In 2023, although ransomware moved back to the top action on objective, X-Force observed a continued reduction in ransomware incident response activity.

Ransomware

However, analysis of ransomware extortion sites indicate ransomware activity globally has increased in 2023. The contradictory data points appear to be attributed to similar data presented in last year’s IBM X-Force Threat Intelligence Index. X-Force clients have continued to improve their capabilities to detect and respond to the precursors of a ransomware event, backdoors, lateral movement and identity abuse. For instance, X-Force responded to several cases involving Qakbot and other types of infections that were caught before ransomware would have likely been deployed. In addition, as we’ll indicate in the next section, data theft and leaks remain the top impacts observed across IBM X-Force Incident Response engagements.

This year, X-Force also reviewed cases to identify where legitimate tools were used for malicious purposes, which was observed in 32% of cases. For example, X-Force has observed vulnerability scanners used to conduct reconnaissance or adversary simulation tools to exfiltrate data. These tools were used to perform credential theft in 13% of total cases, followed by data exfiltration (11%), remote access (10%) and reconnaissance (6%).

These operations also appear to share many of the same connections to initial access malware distribution groups, such as IcedID, Emotet, Bumblebee, Qakbot and Gozi. X-Force also discovered a campaign likely undertaken by former members of the Conti ransomware group that leveraged a false claim of successful data theft as lure material. As such, the criminal core behind ITG23 is still prominent on the cybercriminal threat landscape.

Ransomware operations that maintained their branding upgraded their operations, demonstrating resiliency. BlackCat developers, for instance, debuted a new variant of the malware dubbed Sphynx in early 2023, which introduced a number of new capabilities to make the ransomware more difficult to detect. Affiliates also have been observed evolving their tactics, techniques and procedures (TTPs) across the attack chain, including using a QR code for victims to access the ransom note. Additionally, ransomware operators continue to develop Linux versions of their ransomware. In 2023, new Linux variants of ransomware families were introduced, including CL0P and Royal.

These observations suggest that threat actors are no longer limiting themselves to ransomware attacks to commit extortion. They’re looking at other attack types to deliver on their objectives. For example, X-Force responded to multiple incidents associated with the CL0P ransomware group’s widespread data extortion attacks through MOVEit exploitation.

Although the names of the most prominent ransomware operations continued to shift, X-Force uncovered new evidence linking many current families to past operations. While the Conti ransomware group—tracked by X-Force as ITG23—famously shut down in 2022, X-Force found evidence indicating connections to new ransomware projects. These new projects included Quantum, Royal, Zeon and BlackBasta ransomware, as well as the Karakurt data extortion group.

![Figure 6: Time between initial access and ransomware deployment. Source: X-Force]

X-Force performed an analysis of ransomware attacks between 2022 and 2023 to determine if there were any changes in the time it takes for an attacker to carry out a ransomware attack. The average duration of an enterprise ransomware attack—the time between initial access and ransomware deployment—reduced slightly to 92.21 hours (3.84 days) in 2023 from 92.48 hours (3.85 days) in 2022.

This minimal reduction in the ransomware attack lifecycle appears to be directly related to a 38.44% reduction in time spent between obtaining domain administrator privileges and ransomware deployment. Analyzing the incident data from the attacks, with the largest reductions of time between obtaining domain administrator privileges and ransomware deployment, indicates that the attackers spent less time exfiltrating data than in previous years. It appears attackers are requiring more time to obtain administrative privileges to Active Directory compared to 2021. However, this additional time may be an indication that 2021 was a statistical outlier and mainly due to attackers leveraging exploits like Zerologon and PrintNightmare. X-Force analysis didn’t reveal any substantial changes in the tools, techniques and procedures used by threat actors leveraged in ransomware attacks in 2023 compared to 2021. It’s worth noting that this year’s analysis includes data from all mass deployment ransomware attacks, as opposed to our 2022 original analysis, which examined a subset based on initial access.

Ransomware attack timelines
- Initial access to ransomware deployment

## Top impacts
The top impact to organizations was data theft and leak, making up 32% of the incidents X-Force responded to—accounting for 19% of the incidents in 2022. This increase aligns with the rise in observed infostealer activity and use of legitimate tools to exfiltrate data. Furthermore, extortion incidents more than doubled in 2023, and the share of all incidents that were extortion increased from 21% in 2022 to 24% in 2023.

As mentioned, extortion-based attacks remained one of the driving forces of cybercrime in 2023 with threat actors leveraging various attack types to deliver on their extortion objectives.

![Figure 7: Top impacts X-Force observed in incident response engagements in 2023. Incidents can have more than one impact observed. Source: X-Force]

Top impacts 2023
- Data theft and leak: 32%
- Extortion: 24%
- Credential harvesting: 23%
- Brand reputation: 9%
- Data destruction: 9%
- **2022**
  - Data theft and leak: 19%
  - Extortion: 21%
  - Credential harvesting: 11%

The proliferation of ransomware attacks over the past few years, coupled with the massive efforts taken to combat and prevent them, has potentially pushed threat actors into simplifying their process. For example, threat actors are increasingly experimenting with extortion-based campaigns that do not rely on ransomware to encrypt data. Instead, the threat can be related to theft of and exposure to sensitive internal victim data. Not only is this method a less resource-intensive attack path, it may also be an indicator that data extortion tactics create the most pressure to elicit payment.

Evolution of malware delivery mechanisms
Threat actors have reacted to changes in the security environment by introducing increasingly complex infection chains and attempting new methods of malware delivery. In 2023, X-Force observed2 actors using popular methods, such as email campaigns, leveraging:
- OneNote files with embedded scripts
- PDF files containing malicious links
- Microsoft Software Installer (MSI) and Nullsoft Scriptable Install System (NSIS) executables disguised as document files

The malware landscape
Another tactic that X-Force observed, one which gained popularity in 2023 but appears to have since declined, is HTML smuggling. This method leverages HTML5 and JavaScript functionality to download or construct a malicious payload when the HTML page is opened in a web browser. X-Force also frequently observes .url (internet shortcut) files in attack chains leading to the final payload. Malware distribution through malicious disk image files (ISO, IMG and VHD) and LNK files, which was noted in the 2023 X-Force Threat Intelligence Index, has also continued to be observed with decreased frequency.

There has also been an observed uptick in email campaigns using Microsoft Office documents to deliver malware through exploits rather than malicious macros. Documents weaponized with CVE-2017-11882, an arbitrary code execution vulnerability within the Microsoft Office equation editor, increased in popularity in the past year. Remote template injection, a technique to bypass email gateway controls by sending phishing emails that retrieve malicious office templates after delivery, was also observed in 2023.

In addition, threat actors have increasingly turned to malware delivery vectors beyond email, the most noteworthy of which is the use of fraudulent Google and Bing Ads, also known as malvertising, to distribute malware through fake software downloads. Their payloads have included infostealers and backdoors, some of which have led to ransomware attacks.

X-Force has also observed additional threat actors using fake browser updates to distribute malware, including infostealers and the NetSupport remote administration tool. The Gootloader group continues to use SEO poisoning effectively to infect organizations, which can lead to ransomware attacks. X-Force also continued to observe SEO poisoning leveraged by SolarMarker, which has both infostealer and backdoor capabilities.

The past year has seen a significant rise in the number of and threat actor interest in infostealers. Infostealers can be leveraged to facilitate fraud or theft by compromising financial or personal information. However, infostealers have also been frequently linked to more impactful attacks against enterprises by facilitating initial access through stolen credentials.

X-Force noted a 266% increase in infostealer-related activity in 2023 compared to 2022. That upward trend likely contributed to the rise of abuse of valid accounts, the top initial access vector X-Force observed. Infostealers have long been a staple of the criminal underground marketplace, and many operate as a malware-as-a-service (MaaS) model.

Infostealers on the rise
In addition to the well-established stealers, such as RedLine, Vidar and Raccoon, several prominent new infostealers, which debuted in the latter half of 2022, demonstrated increased activity throughout 2023, such as Rhadamanthys, LummaC2 and StrelaStealer. Different infostealer families target different types of information, from platform-specific credentials to password managers to browser history.

Also, observations of established stealers, such as Agent Tesla, FormBook, Snake Keylogger, Vidar, AZORult and Lokibot, X-Force observed activity by the following recently introduced stealer families:

| Infostealer name | Target Information | Description |
|---|---|---|
| Ducktail | Targets Facebook credentials, Facebook-related cookies, anti-cross-site request forgery (CSRF) tokens, MFA codes and data associated with Facebook Ads Manager | Ducktail targets information required to hijack Facebook business accounts, which is then used to carry out malicious advertisement campaigns. It uses the Telegram messaging application for its command and control infrastructure (C2). |
| Sys01 Stealer | Steals cookies, login information and other sensitive information, including Facebook business account information | Sys01 Stealer is written in Hypertext Preprocessor (PHP) and, like Ducktail, also focuses on stealing Facebook information, such cookies and login data. |
| StrelaStealer | Steals Outlook and Thunderbird email credentials | StrelaStealer focuses on stealing email credentials and has been observed by X-Force as being distributed in phishing campaigns targeting Spain and Italy, and to a lesser extent Germany. |
| Rhadamanthys | Collects information from multiple applications, including browsers, mail clients, virtual private network (VPN) services, two-factor authentication (2FA), password managers, file transfer protocol (FTP) clients, notes, chat and messenger apps, cryptocurrency wallets, remote desktop apps and gaming clients | Rhadamanthys is a jack-of-all-trades infostealer that can also find and exfiltrate files from the file system and gather detailed system information. |
| DarkCloud | Targets information primarily related to credentials, credit card data and cryptocurrency | DarkCloud is a general-purpose stealer that can also log keystrokes and take screenshots. |
| Nemesis | Stores credentials, cookies, credit cards, bookmarks, autofill data, browser history, crypto wallet data and clipboard data | Nemesis is a .NET infostealer observed by X-Force as being deployed by the FIN7-linked Minodo backdoor during campaigns operated by former members of the TrickBot/Conti syndicate. |
| StealC | Collects system information, files, cryptocurrency wallets, browser data and data from email and messaging applications, including Outlook, Discord, Telegram and Steam Chat | StealC steals targeted information based on instructions from its C2 server and can download and execute payloads in addition to stealing data commonly targeted by infostealers. |
| LummaC2 | Collects sensitive data, including login credentials; bank details; cryptocurrency wallet information, such as Binance and Ethereum; browser extension details, for example, MetaMask for 2FA; and data from applications such as AnyDesk and KeePass; and targets Windows operating systems (Windows 7 to 11) and at least 10 browsers, including Google Chrome, Microsoft Edge and Mozilla Firefox | LummaC2, also known as Lumma, is written in C and distributed through a MaaS model. It first emerged in 2022 and includes a loader capable of delivering additional payloads. |

The success of infostealers has not gone unnoticed by other players in the cybercrime marketplace. Threat groups who have largely specialized in ransomware, such as ITG23, also known as TrickBot and Conti, and LockBit have both been linked to infostealers. Campaigns linked to ITG23 have been observed distributing the Vidar infostealer in late 2022. In 2023, ITG23’s interest in infostealers grew to include campaigns involving the LummaC2 and Nemesis stealers during the first half of the year followed by the Rhadamanthys stealer in November. Meanwhile, LockBit announced its desire to purchase the Raccoon Stealer source code.

Research contributions by Intezer further highlight the increasing value of infostealers to the criminal ecosystem. By performing an analysis on how much a malware family’s source code is changing based on uniqueness of code versus code recycling, Intezer found that infostealers topped the list in 2023 for most unique malware samples targeting Microsoft Windows. It made up 17.8% of samples, indicating continued investment in infostealer innovation.

As threat actors invest in infostealers and X-Force observes a developing trend around identity abuse—through credential harvesting or abuse of valid accounts—we expect it to impact defenders’ detection timelines.

Threat actors continue to abuse a wide range of public and private cloud services for malware distribution and operation, allowing them to evade network detection mechanisms by masquerading as legitimate traffic.

Discord and Telegram in particular have attracted significant threat actor attention, as multiple aspects of the platforms' functionality can be abused in service of malicious activity. Threat actors have misused Discord for C2, abused the functionality of the platform’s content delivery network (CDN) to host and distribute malware, and used its webhook functionality to exfiltrate data from infected systems. Additionally, X-Force observed a novel technique in 2023 whereby a Discord C2 channel used the native Discord bot capabilities. WailingCrab, a malware discovered by X-Force in 2023, is a multistage malware that uses the Discord CDN to host further WailingCrab stages and other additional payloads. In addition to Discord, the malware was also notable for abusing the MQ Telemetry Transport (MQTT) protocol, which is a lightweight protocol designed for communication between Internet of Things (IoT) devices. WailingCrab uses the public MQTT broker EMQX for its C2 communications, which lets it hide the true address of its C2, as well as allowing the C2 communications to masquerade as legitimate MQTT traffic.

Abuse of cloud services
GraphicalNeutrino malware is another notable example, which uses the cloud-based collaboration platform Notion for its C2 communications. This malware uses the platform’s API to send requests to a Notion database where it stores victim information and receives commands and additional payloads. Notably, this malware is used by a group that has been assessed to overlap with Russian espionage group APT29, which IBM tracks as ITG11.

We expect that a variety of threat actors and groups may explore the functionality of cloud services for malicious use.

Threat actors have remained interested in leveraging identity abuse to carry out their attacks and, in 2023, X-Force observed threat actors targeting identity services for privilege escalation rather than endpoint credential harvesting techniques. The shift in behaviors appears to be in response to improvements in endpoint detection and response capabilities in preventing traditional credential harvesting techniques such as OS Credential Dumping: LSASS Memory (T1003.001).

Between 2022 and 2023, X-Force noted a 100% increase in Kerberoasting attacks, targeting the Kerberos authentication protocol commonly used in Microsoft Windows Active Directory environments. This method involves extracting password hashes by manipulating service principal names (SPNs) to request Kerberos tickets on behalf of other accounts, enabling attackers to crack passwords and gain unauthorized access.

X-Force observed attackers focusing on SPNs associated with service accounts, as these accounts often hold higher permissions, facilitating broader access to data and systems. Financially motivated attackers in 2023 also targeted Active Directory Certificate Services (AD CS) for privilege escalation, exploiting CVE-2022–26923 to potentially elevate their privileges to domain administrator. Although Microsoft patched this vulnerability in update KB5014754, successful attacks can still occur depending on key distribution center (KDC) configurations, underscoring the importance of vigilant patch management and secure service settings.

![Figure 8: Active Directory Certificate Services attack diagram. Source: X-Force]

Adoption of penetration testing techniques

## Cyberwarfare
Throughout the course of 2023, X-Force has actively monitored countless Russian state-sponsored attacks, leveraging evolving tools and TTPs to carry out offensive operations against Ukraine and its allies. Of note, Hive0051, which shared overlap with Gamaredon, has accelerated its development efforts to support expanding operations since the onset of the ongoing conflict. X-Force analysis identified three key changes to capabilities: an improved multichannel approach to Domain Name System (DNS) fluxing, obfuscated multistage scripts and the use of fileless PowerShell variants of the Gamma malware.

As of October 2023, X-Force observed a significant increase in Hive0051 activity. This activity features a new multichannel approach of rapidly rotating C2 infrastructure. The approach facilitated at least 1,027 active infections with more than 327 unique malicious domains observed in a single 24-hour period. While Hive0051 has used DNS fluxing to avoid detection as early as December 2022, the automated synchronized fluxing of dynamic DNS records across Telegram channels and Telegraph sites at scale suggests an elevation in actor resources and capability.

Russia-Ukraine conflict
In addition, by deploying multiple consecutive stages of the Hive0051 exclusive Gamma variant malware, the actor is able to remap victims to separate sets of actor-controlled C2 fluxing clusters.

Looking forward