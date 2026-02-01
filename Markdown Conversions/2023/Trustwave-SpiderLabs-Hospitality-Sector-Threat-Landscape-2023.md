# 2023 Hospitality Sector Threat Landscape

The official report URL is: https://levelblue.com/resources/research-reports/2023-hospitality-sector-threat-landscape-trustwave-threat-intelligence-briefing-and-mitigation-strategies

# 2023 Hospitality Sector Threat Landscape

T R U S T W A V E   T H R E A T   I N T E L L I G E N C E
B R I E F I N G   A N D   M I T I G A T I O N   S T R A T E G I E S

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
  - [Generative AI and Large Language Models (LLMs)](#generative-ai-and-large-language-models-llms)
  - [Contactless Technology](#contactless-technology)
  - [Third-party Risk and Exposure](#third-party-risk-and-exposure)
- [Dissecting the Attack Flow for Hospitality](#dissecting-the-attack-flow-for-hospitality)
  - [Attack Flow Overview](#attack-flow-overview)
  - [Attack Flow Steps](#attack-flow-steps)
  - [Initial Foothold: Phishing and Business Email Compromise (BEC)](#initial-foothold-phishing-and-business-email-compromise-bec)
  - [Initial Foothold: Logging in](#initial-foothold-logging-in)
  - [Initial Foothold: Vulnerability Exploitation](#initial-foothold-vulnerability-exploitation)
  - [Initial Foothold: Supply Chain](#initial-foothold-supply-chain)
  - [Initial Payload](#initial-payload)
  - [Expansion / Pivoting](#expansion--pivoting)
  - [Malware: Infostealers](#malware-infostealers)
  - [Malware: RATs](#malware-rats)
  - [Malware: Ransomware](#malware-ransomware)
  - [Exfiltration / Post Compromise](#exfiltration--post-compromise)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)
- [Appendix/Reference](#appendixreference)
  - [Threat Groups](#threat-groups)
    - [ALPHV/BlackCat](#alphvblackcat)
    - [BianLian](#bianlian)
    - [Black Basta](#black-basta)
    - [BlackShadow](#blackshadow)
    - [Clop](#clop)
    - [Conti](#conti)
    - [Hive](#hive)
    - [Karakurt](#karakurt)
    - [LockBit](#lockbit)
    - [LV](#lv)
    - [Magniber](#magniber)
    - [Medusa](#medusa)
    - [Play](#play)
    - [Qillin, Royal](#qillin-royal)
    - [Ragnar](#ragnar)
    - [Vice Society](#vice-society)

SEPTEMBER 2023

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies

# 3

## Appendix/Reference

### Threat Groups

#### ALPHV/BlackCat
- BlackCat/ALPHV first appeared in late 2021. This ransomware group was the fourth most active in the second quarter of 2022 and third most active in the third quarter 2022. Intel471 reported the group was responsible for about 6.5% of the total reported ransomware cases during this period. While the amount is smaller compared to LockBit or Black Basta, newcomer BlackCat has managed to stand out from the crowd. The group developed a search function in July 2022 for indexed stolen data that had not been seen previously. The group claimed this was done to aid other cybercriminals in finding confidential information which can be used to add pressure to victim organizations forcing them to pay the ransom. This idea was quickly copied with LockBit adding its own, lighter version to its toolset.
- ALPHV has also set other trends. According to the FBI, ALPHV was the first group to successfully utilize Rust to ransom a victim, well before Hive made the switch. ALPHV’s ability to develop capabilities and functionality that are quickly adopted by other threat actors most likely indicates that its members are most likely ransomware veterans and there are indications the group was linked to the infamous Darkside and BlackMatter gangs.

#### BianLian
- Starting in June 2022, BianLian has been an active cybercriminal group involved in ransomware development, deployment, and data extortion. It has targeted crucial US infrastructure sectors, alongside Australian infrastructure, professional services, and property development. Their entry point often involves exploiting valid Remote Desktop Protocol (RDP) credentials, utilizing open-source tools and command-line scripts for data discovery and credential gathering.
- After accessing victim systems, the BianLian group extracts data using File Transfer Protocol (FTP), Rclone, or Mega and then threatens to publish this data unless a ransom is paid. Initially utilizing a double-extortion approach, they encrypted systems and stole data, but shifted towards focusing on data exfiltration-based extortion around January 2023. To maintain control, the group often deploys custom Go-written backdoors tailored to each victim, accompanied by remote access tools like TeamViewer, Atera Agent, SplashTop, and AnyDesk for continued command and control.

#### Black Basta
- One of the newest ransomware groups is Black Basta. The group has had alleged ties to other gangs, such as Conti, REvil, and Fin7 (aka Carbanak). These ties come in the form of possible former members/affiliates, in the case of Conti, or custom tools, which are potentially linked to Fin7. With potentially experienced members, the group was able to publish more than 20 organizations to its name-and-shame blog within the first two weeks of the group being identified in April 2022, according to Intel471. Since the initial identification of the group, they have compromised over 90 organizations as of September 2022 with no sign of slowing down.
- The group has had unprecedented success for the short period that they have been active. This success can be linked to a couple of factors. First, Black Basta does not publicly recruit affiliates and most likely only collaborates with actors with whom it has worked with previously. This collaborative methodology is possible because it has been assessed that the Black Basta was formed from members of other successful ransomware groups, so they know other actors. Additionally, the group outsources its capabilities utilizing established tools, such as QakBot and Cobalt Strike, or network access brokers, allowing the group to have a high success rate once inside a victim's environment.

#### BlackShadow
- Traces of BlackShadow's operations have been identified dating back to early 2019, indicating a long-standing presence. The group employs its own .NET backdoors and custom tools for various actions on compromised systems, including downloading files, executing commands, and exfiltrating data.
- Often associated with Iranian state sponsorship, BlackShadow is notably linked to the Pay2Key ransomware, which typically targets Israeli entities. However, their motives differ from typical ransomware groups, as they are not primarily financially driven.

#### Clop
- Clop is a ransomware family that was first observed in February 2019 and has been used against retail, transportation and logistics, education, manufacturing, engineering, automotive, energy, financial, aerospace, telecommunications, professional and legal services, healthcare, and high-tech industries. Clop is a variant of the CryptoMix ransomware.
- In addition to exploiting a previously undisclosed vulnerability (CVE-2023-34362) in MOVEit Transfer, group has a history of conducting similar campaigns using zero-day exploits, targeting Accellion File Transfer Appliance (FTA) devices in 2020 and 2021, as well as Fortra/Linoma GoAnywhere MFT servers in early 2023.

#### Conti
- Emerging in 2020, Conti ransomware has been associated with the Ryuk strain through shared code and demonstrates links to cybercrime clusters like Karakurt and TrickBot / Wizard Spider. A notable occurrence was an affiliate's release of the group's playbook in August 2021, detailing tactics and vulnerabilities exploited. A significant development occurred with the release of ContiLeaks in February 2023, which disseminated Conti's internal chat messages and exposed domains compromised with BazarBackdoor malware, facilitating network access. These leaks have prompted changes in the group's dynamics, potentially leading to internal divisions and a diminished rivalry with other RaaS entities, resulting in a noticeable slowdown in their ongoing operations.
- Leveraging insights from the historical attacks as well as mentioned leaks, Conti actors often choose to exploit vulnerabilities in unpatched assets, further escalating privileges and enabling lateral movement within victim networks. They also known to exhibit reliance on TrickBot malware for certain post-exploitation tasks. Conti's tactics underscore a comprehensive strategy that combines existing software, strategic tool additions, credential compromise, and vulnerability exploitation to maintain persistence, escalate privileges, and conduct lateral movements within targeted networks.

#### Hive
- Hive ransomware emerged in June 2021, operating as an affiliate-driven ransomware campaign targeting diverse sectors worldwide, including healthcare, nonprofits, retailers, and energy providers. Their reach extends from the US to Japan, employing tactics such as phishing with malicious attachments and leveraging Remote Desktop Protocol (RDP) for lateral movement within networks.
- The group faced law enforcement action, with authorities seizing their Dark Web sites on January 26, 2023. The seizure, executed through a collaboration involving entities like the US Department of Justice, FBI, Secret Service, Europol, and European countries, marked a significant blow to Hive ransomware's extortion and data leak activities.

#### Karakurt
- Established in June 2021, the Karakurt Hacking Team operates adeptly by deploying Cobalt Strike beacons, utilizing tools like Mimikatz and AnyDesk, and employing diverse techniques for network traversal and privilege escalation. Their extortion strategy centers on data deletion and confidentiality, although breaches of trust have been reported even after ransom payment.
- Karakurt's unconventional tactics involve targeting victims previously attacked by other ransomware groups, potentially involving data purchases. They have also engaged in simultaneous attacks alongside other ransomware actors, occasionally employing exaggeration about breach severity or stolen data, showcasing their deceptive approach.

#### LockBit
- LockBit has continued its reign as the most prominent ransomware group in 2022. For those that don't closely follow these groups, LockBit is and continues to be, the group that dominates the ransomware space. They utilize high payments for recruiting experienced malicious actors, purchasing new exploits, and even run a bug bounty program that offers high-paying bounties - a first for a ransomware group[1]to identity of one of its users. With all these programs and the continued effectiveness of the group, it is forecasted that it will remain the most active and effective group for the foreseeable future.
- As for developments, the group has developed LockBit 3.0, the newest iteration of the ransomware. The updated version, released in June 2022, and includes additional features that can automate permission elevation, disable Windows Defender, a "safe mode" to bypass installed Antivirus, and the ability to encrypt Windows systems with two different ransomware strains to decrease the chance of decryption from a third party. With these new features, the group has been able to conduct successful attacks, accounting for roughly 44% of successful ransomware attacks so far in 2022 according to Infosecurity Magazine.
- On a law enforcement note, a member of the LockBit group was recently arrested in Canada and is awaiting extradition to the United States. A dual Russian and Canadian national has allegedly participated within the LockBit campaign and has been charged with conspiracy to intentionally damage protected computers and to transmit ransom demands. The charges carry a maximum of five years in prison.

#### LV
- Operating since late 2020, the LV group functions as a RaaS entity, with purported ties to the REvil (Sodinokibi) ransomware. While the exact relationship remains uncertain, indications suggest that LV's developers modified REvil's binary script, possibly acquired through a partnership where access to source code was shared, stolen, or sold. LV ransomware seems to have repurposed a REvil v2.03 beta version by altering configurations for their own ransomware activities. This shift highlights their collaborative approach with underground actors, enabling them to target a broad spectrum of regions and industries. The success of a ransomware variant extends beyond new features, emphasizing the significance of expansive reach and improved distribution networks.
- Collaborating with threat actors holding underground access, LV ransomware has effectively expanded its impact across various regions and industries. This underscores the point that the influence of a ransomware strain is not solely shaped by augmenting functionalities, but also hinges on factors like strategic partnerships and robust distribution networks.

#### Magniber
- The initial detection of the Magniber ransomware took place towards the end of 2017, when it was observed employing the Magnitude Exploit Kit for malvertising attacks specifically targeting users in South Korea. Despite its early identification, the ransomware has remained active and has continuously enhanced its strategies by adopting novel methods of obfuscation and evasion. In April 2022, Magniber gained infamy for masquerading as a Windows update file, enticing victims into unwittingly installing it. Subsequently, it began propagating through JavaScript starting in September 2022.
- In early 2022, Magniber distributed itself through fake installers in APPX and MSI formats. The ransomware was executed using the MSI CustomAction table, which called a malicious DLL within the package. The installer also dropped a malware file called Fodscript, used for privileged escalation. Magniber employed various tactics, including posing as fake installers, Windows updates, and COVID-19-related files to deceive users. Additionally, it utilized malformed digital signatures to bypass execution blocks and exploit vulnerabilities such as CVE-2022-44698.

#### Medusa
- MedusaLocker is a ransomware strain that emerged in 2019 and has since spawned various versions, though core functionalities remain unchanged. Alterations include modified file extensions for encrypted data and variations in the appearance of the ransom note. Ransom payments from victims are typically divided between the affiliate (55-60%) and the developer.
- This ransomware often infiltrates victim systems via vulnerable Remote Desktop Protocol (RDP) setups, alongside employing email phishing and direct attachment of the ransomware to emails in spam campaigns for initial access.

#### Play
- Unveiled in June 2022, Play ransomware concentrates its attacks primarily on Latin American nations, with Argentina and Brazil as key targets. Drawing inspiration from Russian counterparts Hive and Nokoyawa, Play employs akin encryption methods.
- Leveraging reused or leaked credentials, Play breaches networks and systems, relying on tools like Cobalt Strike, SystemBC, Empire, and Mimikatz for lateral movement. Its unique employment of AdFind sets it apart from Hive and Nokoyawa, emphasizing a potential affiliation through shared tactics and tools.

#### Qillin, Royal
- Royal is ransomware that first appeared in early 2022; a version that also targets ESXi servers was later observed in February 2023. Royal employs partial encryption and multiple threads to evade detection and speed encryption. Royal has been used in attacks against multiple industries worldwide--including critical infrastructure.
- Royal operates as a private group, distinguishing themselves from other cybercrime operations by purchasing direct access to corporate networks from underground Initial Access Brokers (IABs). Security researchers have identified similarities in the encryption routines and TTPs used in Royal and Conti attacks and noted a possible connection between their operators (the group suspected of being primarily composed of former members of the Conti ransomware group operates discreetly and in a secretive manner. This group, referred to as Team One, consists of ex-members who have come together to form this new entity).
- Royal has been observed employing various methods to gain initial access to vulnerable systems, often including - callback phishing, SEO poisoning and exploiting exposed RDP accounts. Once they have successfully gained access, the group utilizes a range of tools to facilitate their intrusion operations. These tools include Chisel, a TCP/UDP tunneling software, and AdFind, an Active Directory query tool, among others.

#### Ragnar
- Active since December 2019, Ragnar Locker is a ransomware strain that predominantly targets English-speaking users. Both the ransomware group and its binary share the name "Ragnar Locker." This ransomware scans and terminates running services on infected machines, focusing on decrypted services. Operating on Windows and Linux systems, it exfiltrates data, utilizes the Salsa20 encryption algorithm for file encryption, and demands payment for data recovery.
- Employing a dual approach, the Ragnar Locker group practices double extortion. Victims are required to pay not only for file decryption but also to prevent the public release of stolen data. Furthermore, the group promises insights into the attack's origin and security recommendations for those complying with their financial demands. The ransomware goes beyond encryption, erasing volume shadow copies to hinder file recovery and terminating services like vss, sql, veeam, and logmein to maximize impact.

#### Vice Society
- The Vice Society ransomware group gained attention between late 2022 and early 2023 due to a series of high-profile attacks, including one affecting San Francisco's rapid transit system. While primarily focused on education and healthcare, evidence indicates they are also often targeting the manufacturing sector, suggesting a diverse industry penetration approach through compromised credentials procurement.
- Initially known for exploiting the PrintNightmare vulnerability, Vice Society utilized ransomware strains like Hello Kitty/Five Hands and Zeppelin. Recently, they developed their own ransomware builder and adopted stronger encryption techniques. A joint advisory by FBI, CISA, and MS-ISAC in September 2022 highlighted the group's disproportionate targeting of the education sector, with expectations of heightened attacks coinciding with the 2022-23 school year.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies