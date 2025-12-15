# 2025H1 Threat Review

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Trends in the First Half of 2025](#key-trends-in-the-first-half-of-2025)
  - [Cybercrime – Ransomware and Infostealers](#cybercrime--ransomware-and-infostealers)
  - [Healthcare – Malware and Data Breaches](#healthcare--malware-and-data-breaches)
  - [OT – The Growth of Opportunistic Attacks](#ot--the-growth-of-opportunistic-attacks)
- [Statistics](#statistics)
  - [Vulnerabilities](#vulnerabilities)
  - [Threat Actors](#threat-actors)
  - [Ransomware](#ransomware)
- [Deep Dive: APT IRAN and Shifting Identities – A Continuum of Iranian Hacktivist Threats to OT/ICS](#deep-dive-apt-iran-and-shifting-identities--a-continuum-of-iranian-hacktivist-threats-to-otics)
  - [A Tale of Three Identities](#a-tale-of-three-identities)
  - [Comparative Analysis](#comparative-analysis)
  - [What Does It All Mean?](#what-does-it-all-mean)
- [Mitigation Recommendations](#mitigation-recommendations)

---

## 1. Executive Summary

In the first half of 2025, Forescout Research – Vedere Labs published a broad range of blog posts and reports analyzing prominent vulnerabilities, threat actors, and ransomware operations. This mid-year review builds on our 2024 analysis, highlighting both persistent trends and emerging shifts in adversary behavior, attack surfaces, and defensive gaps.

Cybercriminals continue to rely on IT-centric techniques for malware delivery. ClickFix, in particular, has become a favored tool among infostealer and ransomware operators. Ransomware groups are expanding the types of assets leveraged in their attacks, frequently in attempts to bypass EDR solutions. Network infrastructure remains a major initial access vector, with over 20% of newly exploited vulnerabilities affecting such devices. Recent attacks highlight the growing role of IP cameras and BSD systems in lateral movement and impact – validating our 2022 R4IoT scenario that predicted this very convergence.

Beyond cybercrime, the line between hacktivist and state-sponsored activity is increasingly blurred, especially in attacks on critical infrastructure. Once the domain of shadowy state actor groups, these attacks are now frequently attributed to hacktivist front groups or hybrid personas. We analyzed this trend in detail in an April report, but since then, rising tensions in the Middle East have escalated the threat of Iranian-linked hacktivist attacks on Western targets. The tactics observed recall the lead-up to the late 2023 Unitronics campaign orchestrated by CyberAv3ngers.

This report reviews the threat landscape from January 1 to June 30, 2025 (2025H1) comparing it with the same period in 2024. It also includes a detailed case study on Iranian threat activity, showcasing how a continuum of personas, from ICTUS TEAM to APT IRAN, reflects a sophisticated OT/ICS targeting playbook that evolves in lockstep with regional conflicts and attribution pressures.

Crucially, many of the threats in 2025H1 exploited known vulnerabilities: 47% of newly exploited CVEs were published before 2025, and many targeted perimeter infrastructure. This underscores a core theme; proactive defense gaps remain the greatest liabilities.

## 2. Key Trends in the First Half of 2025

### 2.1. Cybercrime – Ransomware and Infostealers

Most cybercriminal activity we analyzed in 2025H1 relied on two dominant malware types: ransomware and infostealers. While the growth of ransomware is addressed in section 3, this section focuses on the evolving TTPs observed in campaigns delivering both malware types.

*   **Initial Access**: Increased use of Initial Access Brokers (IABs) and exploitation of vulnerabilities in specific public-facing applications, including VPNs, remote access solutions, and file transfer applications.
*   **Persistence, Execution, and C2**: Remote monitoring and management (RMM) tools become a preferred mechanism for persistence and execution. Attackers often abuse native functionality, such as remote shell access, to execute commands. Legacy techniques like user creation, scheduled tasks and web shells also remain prevalent.
*   **Privilege Escalation**: Use of Cobalt Strike for post-exploitation has declined, though it remains in use for credential dumping and token manipulation.
*   **Defense Evasion**: Obfuscation has taken a back seat to aggressive EDR bypass techniques. Tools such as KillAV, TrueSightKiller, and EDR Kill Shifter, and ‘bring your own vulnerable driver’ (BYOVD) methods are now standard. These tools are replacing traditional event-log purging and malware obfuscation.
*   **Discovery**: To evade detection, threat actors increasingly use Active Directory Service Interfaces (ADSI) instead of prebuilt PowerShell tools for internal reconnaissance.
*   **Exfiltration**: Data exfiltration is now routine across most groups. Many show preferences for specific tools, like Rclone or MEGA for this phase.

Two incidents in March 2025 illustrate how ransomware operators continue to expand the device types leveraged in their attacks, particularly to evade EDR:

*   Akira ransomware was deployed to Windows endpoints via a compromised IP camera. echoing our 2022 R4IoT scenario, which demonstrated how attackers could leverage IoT, IT and OT assets in a chained attack.
*   A new group dubbed VanHelsing introduced a multi-platform encryptor that includes support for BSD UNIX. BSD, while niche, is gaining attention from ransomware operators. The trend began in 2021, with a variant of Hive and continued into late 2024, with reports of Interlock running on the system. By 2025H1, new BSD-compatible variants emerged from RansomHub and Hunters International.

We expect both asset types – IP cameras and BSD systems – to be increasingly targeted in the near future.

Infostealers continue to grow in both volume and sophistication. As covered in our 2024 Threat Roundup, this malware category became the most common last year. In 2025H1, ClickFix campaigns became the leading innovation in delivery tactics. ClickFix campaigns use social engineering to trick victims into copying and executing attacker-supplied malicious commands (usually PowerShell). This technique, first observed in late 2024 has accelerated in popularity in 2025.

The table below summarizes recent infrastructure components and observed TTPs used by threat actors distributing infostealers.

| Infrastructure Component | Details                                     | Purpose                                    |
| :----------------------- | :------------------------------------------ | :----------------------------------------- |
| Command and control domains | TLDs like .shop, .top, .club, .run          | C2 Communication                           |
| GitHub repositories      | Used for distribution and updates           | Initial payload delivery                   |
| Telegram                 | Channels with bots sharing stolen data      | Distribution, command and control and exfiltration |
| SEO                      | Distribution of ClickFix campaign links     | Initial infection vector                   |
| Bulletproof hosting      | Hosting malicious payloads                  | Payload storage                            |
| Cracked software sites   | Distribution of Trojanized applications     | Initial infection vector                   |

### 2.2. Healthcare – Malware and Data Breaches

Healthcare continues to be among the most targeted industries, as detailed in Section 3 of this report.

In February, we identified a cluster of 29 sophisticated malware samples masquerading as DICOM viewers. These samples delivered ValleyRAT, a backdoor remote access trojan used by the Chinese threat actor Silver Fox to take control of infected machines. A follow-up threat hunt, uncovered further compromise of healthcare-specific systems including central monitoring stations infected with commodity malware, and botnet samples targeting credentials for cardiology information systems. These findings underscore a key reality: IT malware is increasingly being delivered through, or against, medical systems, either directly or by exploiting weak configurations.

Ransomware and data breaches remain the most frequent and damaging types of cyber incidents in the healthcare sector. The Health-ISAC recently cited ransomware, VPN vulnerabilities and compromised credentials as the most persistent threats for healthcare organizations in 2025.

One notable case involved the Interlock ransomware group (initially tracked as Chaya_002) which has increasingly targeted healthcare organizations. In February, we documented their use of ClickFix as a part of initial access and infection chains. Since that report, Interlock has claimed attacks against four additional large US healthcare institutions. In the most recent case, the group claimed to have stolen 941GB of data across 732,490 files. The affected organization required three weeks to restore normal operations.

The real-world consequences of these attacks continue to escalate. In June, multiple media outlets reported that a patient in the UK died in 2024, in part due to a delayed blood test result caused by a ransomware attack attributed to the Qilin group. Investigators linked the attack to 170 additional patient cases, most classified as low severity, but the cumulative effect has amplified concerns about the direct impact of ransomware on patient safety.

In our review of data breaches across sectors, we found that healthcare remains the most impacted across all industries. In addition, we analyzed 238 data breaches reported to the US Department of Health and Human Services (HHS) from Jan 1 to April 30, 2025. Below, we update those findings to include the whole 2025H1 period:

*   341 healthcare breaches affecting over 500 individuals each were reported. Of those, 306 are still under investigation. This is an average of almost two breaches per day.
*   29,799,648 individuals were impacted in total, averaging 87,388 individuals per breach.
*   Five breaches affected more than one million individuals each.
*   74% of breaches occurred at healthcare providers; the remaining 26% at business associates, health plans, or clearing houses.
*   76% of breaches were attributed to hacking/IT incidents.
*   In 62% of breaches, the compromised data was on network servers; 24% involved e-mail.

These findings highlight that healthcare remains highly vulnerable to both opportunistic and targeted attacks, with often outsized consequences due to its sensitive data and operational interdependencies.

### 2.3. OT – The Growth of Opportunistic Attacks

Opportunistic attacks on OT environments are increasing, not due to targeted campaigns, but because threat actors are broadening their scope to include any exposed or vulnerable system. These threat actors who are not pursuing specific victims but instead aim to cause disruption wherever feasible. We observe this trend through two complementary lenses:

1.  **Hacktivist Activity Against OT.**
    Hacktivist groups are increasingly aligning with state interests and targeting cyber-physical systems. In some cases, state-sponsored actors operate under hacktivist fronts to conduct disruptive attacks while obscuring attribution.

    Key Examples from 2025H1 include:
    *   GhostSec and Arabian Ghosts (pro-Iranian): Attacks on PLCs in Israel.
    *   Sector16 and Z-Pentest (pro-Russian): Disruptive campaigns against oil and gas facilities in the US.

    As discussed in greater depth in Section 4, the emerging Iranian actor, APT IRAN, exemplifies the merging of traditional APT-grade capabilities with hacktivist-style messaging and operations.

2.  **Internet-wide Scanning and Attacks on Honeypots.**
    Each year, we analyze traffic to our Adversary Engagement Environment (AEE), a global honeypot network designed to monitor malicious activity. This data provides insight into how attackers scan, identify, and test potential targets across OT networks.

    Key findings from 2025H1:
    *   Modbus remains the most scanned OT protocol, involved in 57% of OT interactions, up from 40% in 2024.
    *   Ethernet/IP holds second place at 20%, down from 28%.
    *   BACnet has risen to third place with 8% up from 7%, overtaking KNX and Fox protocols.

    These shifts reflect sustained attacker interest in industrial automation and building management systems, particularly by threat actors scanning opportunistically for devices.

    **PLC Honeypot Observations**
    Between December 2024 and March 2025, we deployed real PLC honeypots simulating a water treatment environment. Over the 90-day period, the honeypot received 1,444,095 requests – about 16,000 per day or 11 per minute.

    The PLCs honeypots had the following services enabled: S7comm, S7comm-plus, Modbus, HTTP and HTTPS.

    *   98% of requests used standard web protocols (HTTP/HTTPS), not OT-specific protocols.
    *   Only 2% used OT-native protocols like Modbus or S7comm.

    Most Modbus or S7comm requests were attempts to identify or read device data, suggesting either benign scanning or early reconnaissance. However, we observed occasional attempts to:

    *   Alter variables stored in the PLC.
    *   Stop the PLC via its web interface
    *   Connect using an engineering workstation – possibly to reprogram ladder logic.

    These actions resemble real-world TTPs seen in hacktivist-posted videos and social media propaganda.

**Summary**
Opportunistic OT attacks now fall into two main categories:

1.  Real-world disruption, often targeting critical services like manufacturing, or water treatment.
2.  Wide-area scanning, laying the groundwork for exploitation or assessing exposure.

Together, these underscore the persistent interest in OT systems, even among threat actors not traditionally associated with ICS expertise. Attackers are increasingly willing to exploit any system they find exposed regardless of sector or impact sensitivity.

## 3. Statistics

### 3.1. Vulnerabilities

In the first half of 2025, 23,581 vulnerabilities were published, averaging 130 new CVEs per day or 3,930 per month. This represents a 15% increase compared to the same period in 2024, which saw 20,533 disclosures. Figure 1 provides a monthly breakdown of vulnerability publication rates across H1 2023, H1 2024 and H1 2025.

![Figure 1 – New vulnerabilities per month](Image description: A bar chart showing the number of new vulnerabilities published per month for H1 2023, H1 2024, and H1 2025. The chart indicates an increasing trend in vulnerability publications over the years.)

Many CVEs published in H1 2025 are still awaiting CVSS scoring, pending NVD analysis. Among those with assigned scores, 45% were rated low or medium, while 43% were rated high or critical. The proportions are similar to 2024, showing that volume continues to rise, but the distribution of severity remains largely unchanged, as illustrated in Figure 2.

![Figure 2 – New vulnerabilities by CVSS score](Image description: A pie chart illustrating the distribution of new vulnerabilities by their CVSS score (low, medium, high, critical) for H1 2025. The proportions are similar to 2024.)

Raw CVE volume is one thing, but exploitation is what defines real-world risk. In 2025H1, 63 vulnerabilities were exploited as 0-days, up from the 43 in 2024H1, a 46% increase. These 0-days impacted products from 27 vendors, as shown in Figure 3. At this pace, 2025 is on track to exceed the record 100 exploited 0-days, set in 2024.

![Figure 3 – Distribution of new exploited 0-days per month and vendor](Image description: A chart showing the distribution of new exploited 0-day vulnerabilities per month and by vendor for H1 2025. It also indicates the total number of vendors affected.)

Beyond 0-days, 132 CVEs were added to the CISA Known Exploited Vulnerabilities (KEV) catalog in 2025H1. That’s an 80% increase from the 73 added in 2024H1, bringing the cumulative total to 1,371 CVEs. Figure 4 shows a breakdown of new vulnerabilities added to CISA KEV per month and vendor.

![Figure 4 – Distribution of new KEV per month and vendor](Image description: A chart detailing the distribution of new vulnerabilities added to the CISA KEV catalog per month and by vendor for H1 2025. It also shows the total number of vendors affected.)

On average, 22 new vulnerabilities were added to CISA KEV each month in 2025H1. The 132 new additions affected products from 62 vendors, an 88% increase from the 33 vendors affected in 2024H1. 26 of these vendors had more than one vulnerability added during the period.

Almost half of the new CISA KEV entries (47%) were for vulnerabilities published before 2025, a similar proportion as the previous year. Six of the vulnerabilities affected affect end-of-life products, which means no patches are available for this equipment: CVE-2024-0769, CVE-2023-33538, CVE-2021-32030, CVE-2024-11120, CVE-2024-6047, CVE-2025-1316. This underscores how legacy CVEs continue to represent active risk, as illustrated in Figure 5.

![Figure 5 – New known exploited vulnerabilities by year of publication](Image description: A bar chart showing the number of new known exploited vulnerabilities categorized by their year of publication for H1 2025. It highlights the prevalence of older vulnerabilities being exploited.)

The trend of exploits targeting perimeter and network infrastructure devices, first noted in 2023H1 and reported again in 2024H1, remains consistent in 2025. In 2025H1, 28 of the KEV entries (21%) targeted network infrastructure and security appliances. This is more than one in every five exploited vulnerabilities, aligning with last year. These figures reinforce our recent finding, that network infrastructure such as firewalls and routers are among the riskiest IT devices in 2025. These asset types are frequently internet-exposed, often undermanaged and highly attractive for lateral movement and persistent access.

### 3.2. Threat Actors

Forescout Research – Vedere Labs currently tracks 885 threat actors, of whom 137 had notable activity updates in 2025H1. Live tracking and actor profiles are available on our Threat Actor Dashboard. As shown in Figure 6, the majority of these 137 actors are:

*   Cybercriminals (51%), including ransomware groups
*   State-sponsored actors (40%)
*   Hacktivists (9%)

This distribution has remained largely unchanged since 2023H1.

![Figure 6 – Distribution of solar power system vendors per country (top 5)](Image description: A pie chart showing the distribution of threat actors by category: Cybercriminals, State-sponsored actors, and Hacktivists. The percentages for each category are displayed.)

Figure 7 shows that most active threat actors in 2025H1 continue to originate from China, Russia and Iran, accounting for 46% of tracked activity. This top three has remained unchanged year over year.

In 2025H1, we analyzed campaigns from Chinese threat actors targeting medical systems and enterprise software, and other researchers also reported their continued preference for targeting small office and home (SOHO) routers to create proxy botnets and continued activity against telecom and critical infrastructure providers. These campaigns reinforce China’s continued interest in both espionage and infrastructure exploitation.

Russian and Iranian actors included hacktivist-style personas, such as NoName057(16) and Handala Group, whose attacks we analyzed in a recent report. These groups have focused on disruptive messaging and infrastructure impact, often aligning their activities with geopolitical flashpoints. On June 30, 2025, the CISA, FBI and NSA jointly issued an alert warning of the potential for increased targeting of US critical infrastructure by Iranian-linked actors.

![Figure 7 – Threat actors by country of origin](Image description: A bar chart displaying the top countries of origin for active threat actors in H1 2025. China, Russia, and Iran are highlighted as the top three.)

In total, threat actors in our dataset have targeted 159 countries. As seen in Figure 8, the US, India and the UK represent the primary targets. One notable shift: China dropped out of the top 10 list and was replaced by the Philippines. A similar pattern of minor reshuffling occurred in targeted industry verticals, as shown in Figure 9. The top 10 sectors remained consistent with 2024, with only minor changes in rank. Financial services dropped from second to third place, for example, and energy rose from eighth to fifth, reflecting increased threat activity against this sector.

![Figure 8 – Top 10 targeted countries (by number of threat actors)](Image description: A bar chart listing the top 10 countries targeted by threat actors in H1 2025, ranked by the number of threat actors. The US, India, and UK are at the top.)

![Figure 9 – Top 10 targeted industries (by number of threat actors)](Image description: A bar chart listing the top 10 industry verticals targeted by threat actors in H1 2025, ranked by the number of threat actors. Financial services and energy sector positions are noted.)

### 3.3. Ransomware

Based on open-source tracking of ransomware leak sites, we observed 3,649 attacks in 2025H1, a 36% increase over the 2,676 attacks recorded in the same of 2024. This averages to 608 attacks per month or 20 per day.

![Figure 10 – Ransomware incidents per month](Image description: A bar chart showing the number of ransomware incidents per month for H1 2024 and H1 2025, illustrating a significant increase in attacks in H1 2025.)

Figure 11 shows a breakdown of attacks by ransomware group in 2025H1 and 2024H1. Key developments: Cl0p became the most active group, overtaking LockBit, which dropped to 19th position following a major law enforcement operation in February 2024 and a leak of their affiliate panel data in 2025. Only four groups from last year’s top 10 remained in the top tier: Akira, RansomHub, Play and Medusa. Overall, the ransomware landscape continues to fragment and expand although growth is slowing. The top 10 groups accounted for 59% of attacks in 2024H1 and 60% in 2025H1, while the number of active groups increased from 82 to 89, an 8.5% increase.

![Figure 11 – Ransomware incidents per group](Image description: A comparison chart showing the top ransomware groups by incident count for H1 2024 and H1 2025. Cl0p is shown as the most active in H1 2025, and LockBit's decline is noted.)

As in 2024, the top 10 targeted countries suffered 79% of all ransomware attacks. The U.S. alone accounted for 53% of global ransomware attacks, an increase from 48% in 2023 and 20% in 2024. Ransomware victims were recorded in 112 countries, a 9% increase from the 103 countries impacted in 2024H1. The top 10 country list remained consistent, with minor ranking changes. Canada overtook the UK to become the second most targeted country, and France surpassed Spain to move into sixth place.

![Figure 12 – Ransomware incidents per target country](Image description: A bar chart displaying ransomware incidents by target country for H1 2025. The US is the most targeted country, followed by Canada and the UK.)

Figure 13 illustrates the industry verticals most targeted by ransomware in 2025H1, showing little change from the previous period. The top five industries had only one minor change: services, manufacturing, technology, retail and healthcare – while in 2024H1 healthcare had more attacks than retail.

![Figure 13 – Ransomware incidents per target industry](Image description: A bar chart showing ransomware incidents by target industry for H1 2025. Services, manufacturing, technology, retail, and healthcare are the top targeted industries.)

## 4. Deep Dive: APT IRAN and Shifting Identities – A Continuum of Iranian Hacktivist Threats to OT/ICS

Iranian hacktivist groups, often best described as state-sponsored faketivists, have consistently targeted operational technology and industrial control systems (OT/ICS) in the US and Israel since at least 2020. These attacks are frequently tied to geopolitical flashpoints and often accompanied by exaggerated or fabricated claims designed to maximize psychological impact.

With heightened tensions and conflict escalation in the Middle East in June 2025, CISA issued a warning that “Iranian cyber actors may target vulnerable US networks and entities of interest.” Soon after, the UK Parliament’s Intelligence and Security Committee published a comprehensive threat report on Iran, highlighting “rising and unpredictable threats” including the country’s cyber capabilities. The report noted Iran’s motivation to build OT/ICS capabilities likely as a retaliatory evolution, specifically following attacks suffered in 2010 (Stuxnet) and 2012 (Wiper).

One critical omission in both reports is attribution to specific groups that may launch these attacks. We argue this is intentional, or at least understandable. Iran’s threat landscape is now characterized by frequent identity shifting, which undermines the utility of tracking discrete group names.

Over the past five years, Iranian hacktivists have operated under multiple evolving personas. The most notorious, CyberAv3ngers, was attributed by the US in early 2024 to the Islamic Revolutionary Guard Corps – Cyber-Electronic Command (IRGC-CEC) and specifically to six senior officials within that organization.

The tactic of rotating identities, whether using hacktivist fronts or more covert rebranding, has precedent. IRGC-linked groups use this tactic to stay ahead of sanctions and attribution. Groups like APT33 (aka Elfin) and APT35 (aka Charming Kitten) have repeatedly cycled through public-facing identities, domains, and Telegram personas to evade attribution, minimize reputational cost, and complicate response efforts.

In this section, we demonstrate clear overlaps in targeting, capabilities and social media behavior across multiple Iranian personas. Our analysis indicates that CyberAv3ngers the Iranian Cyber Army and APT IRAN, likely form part of a deliberate continuum of state-directed or state-aligned activity, all converging on a core target set: Western OT and ICS infrastructure.

### 4.1. A Tale of Three Identities

Over the past five years, Iranian hacktivist operations targeting OT/ICS have appeared under multiple group names. Even a brief examination of three of these personas - ICTUS TEAM, CyberAv3ngers, and APT IRAN - reveals a pattern of calculated identity confusion, likely designed to hinder attribution and enable sustained disruptive activity with plausible deniability.

The first group which operated under the names ICTUS TEAM and Tapesh Digital Security Team Iran, used multiple logos throughout its activity, and deleted its posts on at least two occasions. Its logos included Iranian flag motifs biohazard symbols often used to represent computer viruses, and stylized references to their Persian name “Tapesh”, meaning heartbeat.

The second group has maintained a consistent name, but has used multiple spellings interchangeably, CyberAv3ngers, CyberAveng3rs, CyberAvengers and Cyber Avengers. It also changed Telegram channels following a supposed account takeover by a rival Israeli group. Its logo prominently features the colors of the Palestinian flag and an image of a bird.

The third group, APT IRAN, has thus far only altered its logos and Telegram channels. The images below show its original logo, a bacteriophage, a virus that infects bacteria, (again possibly alluding to computer viruses) and its recent version, where the virus is depicted piercing a bird, possibly a sparrow in allusion to Israel’s “Predatory Sparrow” group, which was responsible for high profile intrusions into Iran’s Sepah Bank and Nobitex crypto exchange, both of which were extensively discussed by APT IRAN on Telegram.

While recurring imagery such as birds, national flag colors and virus iconography may not, on their own, confirm a connection between these identities, since these visual clues are used by others as well, the operational, thematic and behavioral links among them will become evident in the sections that follow.

**Early activity – ICTUS TEAM and the Iranian Cyber Army**
In December 2020, the persona known as ‘ICTUS TEAM’ (created earlier that year on April 25 and also known as Tapesh Digital Security Team Iran) published claims on Telegram that it had compromised the human machine interfaces (HMIs) of an American water facility and a Israeli energy provider. These claims, however, were never independently confirmed, and the actual impact remains unknown.

Throughout 2020 other Iranian groups including Bax026 and Unidentified Security Team reported similar attacks, asserting they had gained control over the HMIs of multiple Israeli facilities. Many of these actors aligned themselves with the “Iranian Cyber Army,” a loosely defined coalition of Iranian hacktivists that primarily targeted Israeli organizations and their allies.

This wave of OT/ICS targeting coincided with, and was accompanied by, defacement campaigns against American and Israeli websites, some of which were later compiled into propaganda videos by ICTUS TEAM. All this activity happened during the early stages of the US government’s ‘maximum pressure’ campaign against Iran and particularly in the aftermath of the assassination of Iranian general Qassem Soleimani. His image was frequently featured in website defacements carried out by these groups, reinforcing the political motivations behind their operations.

Many of these actors also distributed hacking tutorials and custom tooling. ICTUS TEAM, for example, shared exploit and malware code via a now-deleted repository (github.com/TAPESH-TEAM), and posted instructional videos to YouTube until 2022. The Unidentified Security Team published tools such as a “Network Bruter” through its own GitHub page (github.com/Unidentified-security-team).

These materials, often technical in nature, were accompanied by propaganda and commentary on Telegram, where most posts were written in Farsi. In contrast, their defacement messages were typically presented in English, likely intended for international audiences.

There were several periods of activity and hiatus among these groups, often reflecting geopolitical developments or internal disruptions:

*   The Unidentified Security Team remained active until June 2022, then resurfaced in February 2023 and has continued operations through to the present.
*   Bax026 maintained consistent activity until September 2022, followed by sporadic appearances in 2023 and 2024. The group returned on June 13, 2025 – coinciding with Israel’s strikes on Iran.
*   ICTUS TEAM deleted its original Telegram posts on 3 February 2022, and redirected members to the BiskooitPedar channel, which had been created in March 2021 to share hacking tutorials. On February 12, ICTUS TEAM resumed activity by reposting content from BiskooitPedar. Then, on 12 September 2022, the group again wiped its post history, formally announced its dissolution and encouraged followers to migrate to other groups, including APT IRAN, which we examine in detail below. ICTUS TEAM also submitted their defacements to Zone-H, though activity on that platform ceased in 2022, with only two entries recorded in June 2024 before a brief return in April 2025.

The hiatuses or declared dissolutions of several of these groups occurred around the same time as the wave of civil unrest in Iran following the death of Mahsa Amini in police custody. That period of internal upheaval, which lasted roughly a year, likely disrupted coordination among Iranian hacktivist actors. Notably, the end of that unrest coincided with the emergence of a new and more globally visible hacktivist persona: CyberAv3ngers.

**CyberAv3ngers**
CyberAv3ngers started posting on Telegram on September 13, 2023, with three introductory messages: “Hello world!”, “We Are Back Again!”, and “Do You Remember Us?” These posts strongly suggest that the persona was a rebranding or revival of a previously active group.

The earliest reference to “Cyber Avengers” dates back to 2020 when the name was associated with claimed attacks including a gas tank explosion and disruption to Israel’s railway system, claims later denied by the Israeli government. These messages circulated on various Telegram channels, accompanied by propaganda videos in English, as seen in the screenshots below.

Throughout 2023, CyberAv3ngers continued to publish claims of cyberattacks, many of which appeared to be fabricated or exaggerated. A notable example was the group’s claim to have hacked Israel’s Dorad power station. However, the materials they shared were reused images from a prior leak attributed to the Iranian group Moses Staff.

From the outset, CyberAv3ngers posted exclusively in English – a marked shift from the Iranian Cyber Army’s Farsi-language communications. This linguistic choice suggests the group aimed to gain international visibility, a goal they achieved in late 2023 and early 2024 through a campaign of confirmed attacks on Israeli-made Unitronics programmable logic controllers (PLCs). These attacks defaced PLCs across multiple countries and, unlike prior claims from ICTUS and CyberAv3ngers, the attacks were verified by numerous victims, including at least 29 incidents in the US, the majority of which were water utilities.

In February 2024, the US Department of the Treasury sanctioned six IRGC officials allegedly affiliated with the group. CyberAv3ngers remained active publicly until April 2024, when their original Telegram channel was supposedly taken over by an Israeli actor known as “WeRedEvilsOG”. Around the same time, the identity of one of the sanctioned IRGC officers was further exposed. In response, the group shifted its activity to its X (formerly Twitter) account, where it posted a defiant message, “wait for next steps”, and published a letter condemning the “oppression of Telegram platform.”

Reports published later in 2024 confirmed
