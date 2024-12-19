# CYBER SECURITY REPORT 2023

## Contents

- [Chapter 1: Introduction to the 2023 Cybersecurity Report](#chapter-1-introduction-to-the-2023-cybersecurity-report)
- [Chapter 2: Timeline of Key 2022's Cyber Events](#chapter-2-timeline-of-key-2022s-cyber-events)
- [Chapter 3: 2022's Cyber Security Trends](#chapter-3-2022s-cyber-security-trends)
    - [Russo-Ukrainian Conflict](#russo-ukrainian-conflict)
    - [The Year of Unrestrained Wiper Disruption](#the-year-of-unrestrained-wiper-disruption)
    - [Hacktivism Graduates to Major Player on Geopolitical Stage](#hacktivism-graduates-to-major-player-on-geopolitical-stage)
    - [Weaponization of Legitimate Tools](#weaponization-of-legitimate-tools)
    - [Ransomware Extortion—Shifting focus from encryption to data extortion](#ransomware-extortion-shifting-focus-from-encryption-to-data-extortion)
    - [Mobile Malware Landscape—The Risk of Trusting the Familiar](#mobile-malware-landscape-the-risk-of-trusting-the-familiar)
    - [Cloud: Third Party Threat](#cloud-third-party-threat)
- [Chapter 4: Global Analysis](#chapter-4-global-analysis)
- [Chapter 5: High Profile Global Vulnerabilities](#chapter-5-high-profile-global-vulnerabilities)
- [Chapter 6: Incident Response Perspective](#chapter-6-incident-response-perspective)
- [Chapter 7: 2023 Insights for CISOs: Disruption and Destruction](#chapter-7-2023-insights-for-cisos-disruption-and-destruction)
- [Chapter 8: Prevention is at Reach](#chapter-8-prevention-is-at-reach)
- [Chapter 9: Malware Family Descriptions](#chapter-9-malware-family-descriptions)
- [Chapter 10: Conclusion](#chapter-10-conclusion)


<br>

# Chapter 1: Introduction to the 2023 Cybersecurity Report

BY MAYA HOROWITZ

# Chapter 2: Timeline of 2022's Key Cyber Events

# Chapter 3: 2022's Cyber Security Trends

## Russo-Ukrainian Conflict

> As was the case on the physical battleground, the Russians apparently did not prepare for a long cyber campaign. Their cyber operations, which in the early stages included carefully planned precise attacks, have all but ceased. Multiple new tools and wipers, that were characteristic of the initial stages, have been replaced with a different operational mode. Current offensive cyberattacks are mostly rapid exploitations of opportunities as they arise and use already known attack tools. These are not intended to assist tactical combat efforts but rather create a psychological effect by damaging the Ukrainian civil infrastructure. The recruitment of cyber professionals, criminals, and other civilians to the military cyber effort—on both sides of the conflict—has further blurred the distinction between nation-state actors, cyber criminals, and hacktivists. The Ukrainian government has established an army of hacktivists whose management is very different from anything we have seen before. Previously characterized by loose cooperation between individuals in an ad hoc fashion, new-hacktivist organizations conduct recruitment, training, intelligence-gathering and allocation of targets and battlefield status compilation in a military manner. Attacks on Russian entities, which were once considered off-limits by many cybercrime entities, have now increased and Russia is struggling under an unprecedented hacking wave that combines state-sponsored activity, political cyber warriors and criminal action. On the other side, multiple Russian-affiliated hacktivist groups were established that target not only Ukraine but also Europe, North America and Japan. For more details, see our section on Hacktivism.

> The ongoing Russian-Ukrainian war has had a profound effect on cyberspace and caused a significant increase in cyber-attacks in 2022. Hacktivism has been transformed, and the use of destructive malware by state-sponsored groups and independent entities has become more prevalent globally.

> The role of cyberwarfare has been well documented in this first full-blown hybrid conflict, where battles are fought online as well as on physical ground. The Russians revealed new cyber tools and achieved tactical objectives that affected military and civil communications, including blocking public media transmissions. While cyber activity cannot win the war on its own, it does play a significant part in tactical operations and has an indisputable psychological and economic effect. For cyber-operations to be effective, is not just a matter of employing malware. Much like conventional warfare, cyberwarfare also requires meticulous and thorough preparations. Reconnaissance, intelligence gathering and assessment, target-bank compilation and prioritization, dedicated-payload development and network infiltration are all prerequisites for a successful campaign.

Sergey Shykevich
Threat Intelligence Group Manager, Check Point Software Technologies

> The role of cyberwarfare has been well documented in this first full-blown hybrid conflict, where battles are fought online as well as on physical ground. The Russians revealed new cyber tools and achieved tactical objectives that affected military and civil communications, including blocking public media transmissions. While cyber activity cannot win the war on its own, it does play a significant part in tactical operations and has an indisputable psychological and economic effect.


## The Year of Unrestrained Wiper Disruption

> Wipers and other types of destructive malware are carefully designed to cause irreversible damage, and if tightly woven into cyberwarfare, the effect can be catastrophic. This is probably why we have only seen limited use of wipers over the years, and they were usually associated with nation states. Until recently, countries primarily used cyberattacks for the purpose of espionage and intelligence gathering, and only rarely resorted to destructive cyber tools. In 2022 we have seen a change in the appearance of multiple new wiper families that are used to destroy thousands of machines.

> Wipers are destructive malware, designed to inflict damage with limited potential for financial gain for attackers. Early use of wipers to showcase attackers’ capabilities was thus limited and short-lived. But in all the cases, the main purpose of the wipers is to interrupt operations or to irreversibly destruct data. While the process of data destruction has several technological implementations.

Eli Smadja
Security Research Group Manager, Check Point Software Technologies

> Wipers and other types of destructive malware are carefully designed to cause irreversible damage, and if tightly woven into cyberwarfare, the effect can be catastrophic. This is probably why we have only seen limited use of wipers over the years, and they were usually associated with nation states. Until recently, countries primarily used cyberattacks for the purpose of espionage and intelligence gathering, and only rarely resorted to destructive cyber tools. In 2022 we have seen a change in the appearance of multiple new wiper families that are used to destroy thousands of machines.


## Hacktivism Graduates to Major Player on Geopolitical Stage

> Hacktivism, the act of carrying out politically or socially motivated cyberattacks, was traditionally associated with loosely managed entities such as Anonymous. These previously decentralized and unstructured groups were made up of individuals cooperating ad hoc for a variety of agendas. Over the last year, following developments in the Russian-Ukrainian conflict, the hacktivist ecosystem has matured. Hacktivist groups have tightened up their level of organization and control, and now conduct military-like operations including recruitment and training, sharing tools, intelligence and allocation of targets. Most of the new hacktivist groups have a clear and consistent political ideology that is affiliated with governmental narratives. Others are less politically driven but have nonetheless made their operations more professional and organized.

Alexandra Gofman
Threat Intelligence Analysis Team Leader, Check Point Software Technologies

> The boundaries between state-sponsored cyber operations and hacktivism have become increasingly blurred, which allows nation-states to act with a degree of anonymity without feat of retaliation. This also provides hacktivists with the opportunity to publicly claim responsibility for cyber attacks and draw significant attention to their cause, which can be just as significant as the actual damage caused. Non-state affiliated hacktivist groups are better organized and more effective than ever before, and this is expected to increase in the future.


## Weaponization of Legitimate Tools

> The basic layer of cyber protection is recognizing malicious tools and behaviors before they can strike. Security vendors invest substantial resources in the research and mapping of malware types and families, and their attribution to specific threat actors and the associated campaigns, while also identifying TTPs (Techniques, Tactics and Procedures) that inform the correct security cycles and security policy.

> To combat sophisticated cybersecurity solutions, threat actors are developing and perfecting their attack techniques, which increasingly rely less on the use of custom malware and shift instead to utilizing non-signature tools. They use built-in operating system capabilities and tools, which are already installed on target systems, and exploit popular IT management tools that are less likely to raise suspicion when detected. Commercial off-the-shelf pentesting and Red Team tools are often used as well. Although this is not a new phenomenon, what was once rare and exclusive to sophisticated actors has now become a widespread technique adopted by threat actors of all types.

> There are several reasons why the use of legitimate tools is an attractive option for cybercriminals. First, as these tools are not inherently malicious, they often evade detection and are difficult to distinguish from regular users or IT operations. Second, many of these tools are open-source or available for purchase, so threat actors have easy access to them. In addition, when threat actors share tools, it makes it harder to identify who is responsible for a particular attack.

Lotem Finkelstein
Director, Threat Intelligence & Research, Check Point Software Technologies

> There are several reasons why the use of legitimate tools is an attractive option for cybercriminals. First, as these tools are not inherently malicious, they often evade detection and are difficult to distinguish from regular users or IT operations. Second, many of these tools are open-source or available for purchase, so threat actors have easy access to them. In addition, when threat actors share tools, it makes it harder to identify who is responsible for a particular attack.


## Ransomware Extortion—Shifting focus from encryption to data extortion

> Seeking to maximize the pressure on their victims, ransomware actors employ multiple-extortion tactics. Data on the victims’ systems is encrypted, with decryption keys released only after the ransom payment. Unless they pay, companies know their data could be openly published, sold or even used to extort their employees and customers directly. Some ransomware affiliates, which have now become more dominant in the ransomware crime scene, and better skilled at identifying sensitive information in victims’ networks, even skip the encryption phase altogether and rely solely on data publication threats to generate ransom payments. This may have serious implications for defense mechanisms, attribution, and future analysis of the ransomware ecosystem.

Itay Cohen
Technology Leader, Check Point Software Technologies

> As this data extortion model becomes prevalent, possible ramifications include increased fragmentation of the ransomware ecosystem. Attribution of ransomware operations and tracking threat actors may become even harder and existing protection mechanisms which are based on detecting encryption activity could prove less effective. In its place, cybersecurity providers will need to focus more on data wiping and exfiltration detection.


## Mobile Malware Landscape—The Risk of Trusting the Familiar

> Mod APKs (Android Package Kits; applications for Android devices) are reworked copies of well-known applications, designed to provide users with extended functionalities or access that are not available in the original version. In the past few years, we have seen modified versions of a variety of applications, from instant messaging and social media apps, to live streaming, VPN services and more. The apps are usually distributed through unofficial channels to users looking for free versions of known apps, or for additional features that do not exist in the original versions. In some cases, users are targeted and offered direct links to the modified APKs. In others, users seek them out voluntarily due to limited access to official applications. For example, FMWhatsApp allows users to redesign their WhatsApp interface and edit the “last seen” and “blue tick” functionalities. These Mods are not scrutinized as carefully as the official version, which makes them a natural exploitation target for threat actors. Often the infection is achieved through advertisement SDKs, used by the Mods’ developers. This was the case with HMWhatsApp infection with the Triada Trojan in August 2021, and APKPure later that year.

> In our 2022 mid-year report we reviewed some major events in the mobile threat landscape, including the vast increase in the number of malicious applications infiltrating Google and Apple stores. Often disguised as innocent applications like QR readers, external Bluetooth apps, flashlights or games, they are designed to attract as little attention as possible. In our latest analysis, we focus on attempts to hide mobile malware in “unofficial” versions of well-known applications. Mostly, these are malicious modified versions (aka Mods), typically distributed through third-party app stores and downloaded by users who prefer an unofficial version for a variety of reasons. This is not a completely unheard of threat, but 2022 has seen multiple attacks using apps that are well known, trusted, and widely used.

Shani Springer
Data Research Analysis Team Leader, Check Point Software Technologies

> Mobile devices are targeted by hostile entities for a variety of reasons and motivations. Attackers often target the most popular, well-known and widely used applications which users would consider safe. Exploits can come in either the form of modified or fake applications, or through the exploitation of vulnerabilities in the original versions. We should take this as a reminder of the need to stay vigilant, especially when using the most popular and widely used applications.


## Cloud: Third Party Threat

> Over the past few years, Check Point Research (cp<r>) has been tracking the increasing adoption of cloud infrastructure in corporate environments, as well as the evolution of the cloud threat landscape. Currently, around 98% of organizations use cloud-based services, and 76% of them have multi-cloud environments that incorporate services from two or more cloud providers.

> When comparing the past two years, we have seen a significant increase in the number of attacks on cloud-based networks per organization, which shot up by 48% in 2022 compared with 2021. Although the overall number of attacks on cloud-based networks is 17% lower than non-cloud networks, a closer examination of the types of attacks shows that newly disclosed vulnerabilities (2020-2022) are exploited more frequently on cloud-based than on-premise environments. This might indicate a shift that some threat actors now prefer to scan the IP range of cloud providers. This might enable to gain easier access to sensitive information or critical services.

Omer Dembinsky
Data Research Group Manager, Check Point Software Technologies

> When comparing the past two years, we have seen a significant increase in the number of attacks on cloud-based networks per organization, which shot up by 48% in 2022 compared with 2021. Although the overall number of attacks on cloud-based networks is 17% lower than non-cloud networks, a closer examination of the types of attacks shows that newly disclosed vulnerabilities (2020-2022) are exploited more frequently on cloud-based than on-premise environments. This might indicate a shift that some threat actors now prefer to scan the IP range of cloud providers. This might enable to gain easier access to sensitive information or critical services.


# Chapter 4: Global Analysis

# Chapter 5: High Profile Global Vulnerabilities

# Chapter 6: Incident Response Perspective

# Chapter 7: 2023 Insights for CISOs: Disruption and Destruction

# Chapter 8: Prevention is at Reach

# Chapter 9: Malware Family Descriptions

# Chapter 10: Conclusion

CONTACT US

WORLDWIDE HEADQUARTERS
5 Ha’Solelim Street, Tel Aviv 67897, Israel 
Tel: 972-3-753-4555 | Fax: 972-3-624-1100 
Email: info@checkpoint.com

U.S. HEADQUARTERS
959 Skyway Road, Suite 300, San Carlos, CA 94070 
Tel: 800-429-4391 | 650-628-2000 | Fax: 650-654-4233

UNDER ATTACK?
Contact our Incident Response Team: 
emergency-response@checkpoint.com

CHECK POINT RESEARCH PODCAST  
Tune in to cp<radio> to get CPR’s latest research,  
plus behind the scenes and other exclusive content. 
Visit us at https://research.checkpoint.com/category/cpradio/

WWW.CHECKPOINT.COM

© 1994-2023 Check Point Software Technologies Ltd. All Rights Reserved.

