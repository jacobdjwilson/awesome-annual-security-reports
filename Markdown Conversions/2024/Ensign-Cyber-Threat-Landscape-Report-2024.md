# ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024

Version 1.4 | 10 May 2024

# EDITOR’S FOREWORD

Cybersecurity remains one of the most pressing challenges facing nations, organisations, and even individuals. Ensign InfoSecurity is dedicated to supporting the cybersecurity needs of a wide variety of clients. We publish this report to share our unique insights and perspectives into threats, trends, and topics with business leaders and cybersecurity professionals.

As Ensign continues to grow our operational presence overseas, this year’s report features coverage of Singapore, Malaysia, Indonesia, South Korea, and our recent expansions in Australia and the Greater China Region (Hong Kong S.A.R. and mainland China). We also bring our cybersecurity expertise, experience, and unique Asia-first lens on cybersecurity challenges to global platforms that we participate in, to help shape global discussions.

We believe in using a Threat-Informed Defence approach. Our Ensign Threat Classification Matrix for identified threat groups helps organisations to prioritise their cyber defences against the territory-contextualised threats. We provide the MITRE ATT&CK heatmaps to support organisations in prioritising their cyber defences against specific adversary techniques and follow-through defensive actions, such as threat hunting, Red Teaming, and tuning of detection rules. We have also laid out the observed top targeted industry groups and top exploited vulnerabilities.

With every case our incident response team handles, we learn a little more about how attackers operate. They are evolving to find gaps in our processes, in addition to pushing harder on the weaknesses in our systems and people. While we design, build, and operate a variety of protective systems for organisations, we also advise our clients that resilience, not just building higher defensive walls, should be the objective towards sustainable and predictable defence outcomes.

We are seeing first-hand how cybersecurity and the foundations of digital trust are being tested by the exploitation of Artificial Intelligence (AI) among threat actors. Our researchers are investigating how they use AI to accelerate malware and exploit development, or evade detection. AI is being extensively used in influence operations through Misinformation, Disinformation, and Malinformation (MDM), which distort reality, especially amidst a cyber crisis. We study these threats and trends to advise clients on how to deal with the risks of emerging technologies.

Our continued investment and contribution towards sharing our insights are aimed at enabling companies to better defend against the threats relevant to them. Companies cannot choose whether they become targets, but they can decide how they respond to a cyber-attack, and whether they can recover smoothly and with predictable outcomes.

## About Ensign InfoSecurity

Ensign InfoSecurity is the largest comprehensive cybersecurity service provider in Asia. Headquartered in Singapore, Ensign offers bespoke solutions and services to address our clients’ cybersecurity needs. Our core competencies are in the provision of cybersecurity advisory and assurance services, architecture design and systems integration services, and managed security services for advanced threat detection, threat hunting, and incident response. Underpinning these competencies is our in-house cybersecurity research and development team. Ensign has two decades of proven track record as a trusted and relevant service provider, serving clients from the public and private sectors in the Asia-Pacific region.

For more information, visit www.ensigninfosecurity.com.

# TABLE OF CONTENTS

1. Executive Summary ………………………………………………………………………………………………………………………………………………………… 4
2. Territorial Insights …………………………………………………………………………………………………………………………………………………………... 7
    a) Overview
    b) Singapore
    c) Malaysia
    d) Indonesia
    e) South Korea
    f) Australia
    g) Greater China Region
3. Top Threat Trends 2023 …………………………………………………………………………………………………………………………………………………… 30
4. Topical Insights for 2023 …………………………………………………………………………………………………………………………………………………. 32
    a. Escalating Threats
        i. Ransomware, Evolved: Shift in Extortion Techniques
        ii. Hacktivists, Unite: Increasing Sophistication of Cause-aligned Groups
    b. Evolving Attacks
        i. Digital Infrastructure Under Fire: Threats Across the Cyber Supply Chain
    c. Emerging Rules
        i. Digital Sheriffs: New Regulatory and Policy Initiatives that Aim to Address Risks of Emerging Technology
        ii. Disclosure Revelations: How Mandatory Incident Reporting is Shining a Light on Corporate Cyber Impact
5. Outlook of Cyber Threats for 2024 ………………………………………………………………………………………………………………………………….. 57
    a. Influential Attackers: Will AI-powered Information Campaigns Shape Election Outcomes and Dismantle Digital Trust?
    b. Securing AI: Will We Overcome the Vexing Dilemma of Imposing Rules on Probabilistic Systems?
    c. Scary AI: The Malicious Use of AI will Make Old Attacks Better, but will They Create New Attacks?
    d. Technology Bifurcation: Managing Supply Chain Risks, but at the Risk of Destabilizing the Internet?
6. Defensive Actions for Cyber Defenders and Leaders ……………………………………………………………………………………………………….. 72
7. Contributors ………………………………………………………………………………………………………………………………………………………………... 78
8. Appendices ……………………………………………………………………………………………………………………………………………. 80

# 1 EXECUTIVE SUMMARY

Cybersecurity continues to be a critical challenge faced by nations, organisations, and individuals. To effectively defend against cyber threats requires, business leaders and cyber professionals must remain informed about the latest threats, risks, and challenges. This year’s report offers increased coverage, due to the expansion of our operational footprint, and deeper analysis attributed to the quality of our data and intelligence sources. These enhancements enable us to provide unique insights and observations for 2023, and forecasts for 2024.

## Territorial Insights

In our analysis of the different territories Ensign operates in, we observed unique differences in each of them. The most targeted industry groups across our territories were Technology, Media and Telecommunications (TMT), Government, Manufacturing, and Financial Services. We continued to observe both state-sponsored threat groups and organised crime groups (notably those which exploit through deployment of Ransomware) in the region. Ransomware remains the dominant threat in nearly every territory we studied. Additionally, we observed a rise in hacktivism (malicious cyber activity motivated by a cause) associated with the spillover effects from the Israel-Hamas conflict, and the normalisation of such activities during the Russia-Ukraine conflict.

### Top Hacktivist Groups

*   Bjorka
*   DragonForce Malaysia
*   SynixCyberCrimMY
*   GhostSec
*   Muslim Cyber Army
*   VulzSec
*   Ganosec Team

### Top Initial Access Brokers

*   APT-C-01 (Poison Ivy)
*   BITTER
*   Scattered Spider
*   UNC5221

### Top Ransomware Groups

*   ALPHV / BlackCat
*   FIN11
*   LockBit Gang

### Top Surveillance-oriented Groups

*   Kimsuky
*   Poison Carp

### Top Commonly Used Solutions with Notable Vulnerabilities

*   MOVEit Managed File Transfer (MFT) software
*   Citrix NetScaler ADC and Gateway
*   Confluence Server and Datacentre
*   Zoho ManageEngine
*   3CX Desktop Application
*   GoAnywhere MFT
*   Ivanti Connect Secure VPN
*   PaperCut Application Server
*   Veam Backup & Replication

## Escalating Threats

With every case our incident response team handles, we learn a little more about how attackers operate. Attackers are exploiting weaknesses in our cyber processes to evade detection; instead of getting in through the “high severity” vulnerabilities that companies tend to patch quickly and monitor closely, they use “low” risk vulnerabilities that are de-prioritised for patching for weeks. Rather than bring in hefty payloads that might trigger detection rules, they have developed sophisticated “living off the land” techniques to stay below the radar.

## Evolving Attacks

Supply chain risks and sophisticated attacks also make it harder to defend every threat vector. Attackers are compromising critical nodes in common commercial network hardware, making defences even harder.

## Emerging Rules

Our active involvement in international platforms like the United Nations (UN), World Economic Forum (WEF), and Geneva Dialogue, allows us to understand the spillover effects of geopolitics into the cyber domain. While malicious activity directly related to the Russia-Ukraine conflict may have dwindled, an uptick in Hamas-Israel hacktivism has filled the void. Additionally, tech bifurcation remains another geopolitically charged issue, complicating procurement decisions in the short term (especially as some countries implement bans on companies using software or hardware from other countries), and possibly worsening cybersecurity for all in the longer term.

We are seeing first-hand how cybersecurity and digital trust is being transformed by Artificial Intelligence (AI) — whether it is infused in our own tools, discovered in a weaponised form through our threat research, or through our expert policy development and advisory guidance to organisations. While Generative AI-driven scams and phishing emails troubled our systems in 2023, 2024 will see a spike in Misinformation, Disinformation, and Malinformation (MDM) amidst an election-filled year around the world. Reality can also be distorted by ruthless attackers, especially amidst a cyber crisis.

In the ever-evolving landscape of cybersecurity, it is paramount for new regulations and policies to be aimed at enhancing data protection, fortifying the security of critical systems, and strengthening digital infrastructure. Many countries are introducing or enhancing cyber and data legislation (some with politicised motives).

While we design, build, and operate a variety of protective systems for organisations, we also advise our clients that resilience, not just building higher defensive walls, should be the objective beyond a certain point.

## Conclusion

Whether you sit at the technical-operational layer, the executive layer, or the board oversight/governance layer, the challenges of navigating the complexities of cybersecurity are significant. In this regard, implementing new regulatory frameworks and policy initiatives will play an instrumental role in building our defences against cyber threats.

Hopefully, the insights and analysis in our report can help you make more informed decisions about what is best for your needs. Ensign stands ready to protect your organisation’s digital journey from the ever-expanding array of threats and risks.

# 2 TERRITORIAL INSIGHTS

## Overview of Territorial Insights

Ensign’s regional offices (Singapore, Malaysia, Indonesia, South Korea, and now Australia and the Greater China Region) are situated in locations within the Asia-Pacific region with high cyber activities, charged by geopolitical tensions (e.g. US-China tensions, South China Sea disagreements, and China-Taiwan tensions), and uneven (but generally growing) economies. Across these territories, Ensign continues to observe increased digitalisation efforts and the use of a wide range of hardware and software solutions, adding to the complexity in managing the cybersecurity risks in the digital attack surface.

Ransomware continues to be lucrative for the threat groups (and the most prominent threat across most regions), not only as a financial gain tool, but due to the sustained investments by cyber weapons developers, become a useful and effective cyber weapon to cause pain to targeted organisations. The most active Ransomware groups observed across the territories include, ALPHV, BlackCat Gang, FIN11, and LockBit Gang.

While we observed both state-sponsored threat groups and organised crime groups active in the region, we also saw rising activities associated with hacktivism due to spillover effects from the Israel-Hamas conflict occurring from the end of 2023. This has generally led to rising partisan collective groups taking actions into their own hands for the ideological causes. Notable hacktivist groups observed active in our region included Bjorka, DragonForce Malaysia, SynixCyberCrimMY, GhostSec, Muslim Cyber Army, VulzSec and Ganosec Team. The challenge in addressing hacktivism stems from their lack of a definitive structure and unique processes and procedures for each group. Instead, individuals involved in adversarial actions leverage their individual competencies and capabilities to further their cause. While organisations who do well in addressing cyber hygiene measures are generally resilient against hacktivist threats, the level of sophistication and effects are also rising. These groups have been observed to perform not just the distributed denial-of-service (DDoS) attacks and website defacements, but now, with the accessibility to offensive services (e.g. Ransomware as a Service), some attacks are inflicting greater harm to organisations when these attacks breach the defences.

Aside from hacktivism, Ensign has seen sustained activities from initial access brokers active in the territories, who have not only been successful in obtaining and selling access to organisations, but also due to rising Law enforcement activities targeting the Ransomware operators, started to opportunistically exfiltrate and sell the victim’s data even before sale of access. This has led to some cyber-attack campaigns having lost the adversaries’ element of surprise due to lack of operational security (OpsSec). Active initial access brokers (IABs) observed across the territories include APT-C-01 (Poison Ivy), BITTER, Scattered Spider, and UNC5221. IABs such as Scattered Spider are known to obtain financial gain through sale of access and opportunistically sell data obtained during acquisition of access.

Aside from initial access brokers and Ransomware groups, 2023 saw 21 threat groups actively targeting the Ensign operating territories. There are more state-sponsored threat groups (16) than organised crime groups (5) observed. Russian-associated threat groups, APT28, FIN7, and Turla, are representative groups that have returned to target the Ensign operating territories. GambleForce and Lazarus Group were observed to have targeted all Ensign’s operating territories.

The five organised crime groups observed across the territories, aside from the aforementioned Ransomware Groups and Initial Access Brokers, are Carderbee, Desorden, FIN7, Patchwork, and Poison Carp. Malaysia and Indonesia generally shared the same threat groups, with the exception of Desorden which continued its targeting of Malaysia, and Turla which targeted Indonesia.

## Overview of Territorial Insights

Due to the aforementioned tensions across the territories, there are more threat groups observed to be motivated by surveillance, information theft and espionage. Particularly on surveillance of populations, we noted that Kimsuky and Poison Carp are threat groups which target mobile devices for surveillance outcomes with the harvesting of personal data and information.

Attacks on network equipment with significant impact were seen across territories. The stealthy and persistent effects of breaches performed by Volt Typhoon were prominent, especially with their KV-Botnet to compromise long-term unpatched and end-of-life networking products (such as Netgear ProSAFE routers, CISCO RV 320/325 routers, Draytek Vigor routers, and AXIS IP cameras). Some of these devices are installed in the operational technology (OT) environment or next-to-OT environments (possibly affecting essential services and other OT-centric businesses such as manufacturing) in territories such as Singapore, Malaysia, Indonesia, and Australia.

Cyber supply chain attacks have also manifested in a big way across the territories in 2023, causing some big brands / organisations to be breached. Notably, cyber-attacks exploiting vulnerabilities are found in commonly used commercial off the shelf (COTS) solutions such as MOVEit Managed File Transfer (MFT) software, Citrix NetScaler ADC and Gateway, Confluence Server and Data Center, Zoho ManageEngine, 3CX Desktop Application, GoAnywhere MFT, Ivanti Connect Secure VPN, PaperCut Application Server, Veam Backup & Replication, and others.

Based on our incident responses, Ensign noted that the minimum Dwell time increased compared to 2022 (0 days). This could be attributed to the increasing technology sprawl as organisations work through technology refresh and the continued use of Cloud-based services. The maximum Dwell time decreased significantly from 1,095 days to 49 days. This is encouraging as it indicates that organisations may be increasing their detection capabilities. Contrasting the average Dwell time observed from 2022, there has also been a decrease to 5 days for Retail, 22 days for TMT, and 33 days for Others, observed this year (last year we observed the average of 71 days average Dwell time for Transport sector and 83 days for Others).

| Industry Group                                | Average Dwell (Days) | Min. (Days) | Max. (Days) |
| :-------------------------------------------- | :------------------- | :---------- | :---------- |
| Retail                                        | 5                    | 3           | 12          |
| Technology, Media and Telecommunications (TMT) | 22                   | 12          | 49          |
| Others                                        | 33                   | 19          | 43          |

Across the territories, the top targeted industry groups were as follows:

*   **SG**: Manufacturing, Professional services, TMT, Financial services, Real estate
*   **MY**: Manufacturing, Government, TMT, Financial services, Retail
*   **ID**: TMT, Financial Services, Government, Energy, Manufacturing
*   **SK**: Government, TMT, Manufacturing, Financial services, Defence
*   **AU**: TMT, Engineering & construction, Retail, Government, Financial services
*   **GCR**: TMT, Manufacturing, Professional services, Healthcare, Defence, Financial Services

The most common industry groups were Technology, Media and Telecommunications (TMT), Government, Financial Services, and Manufacturing.

Across this section, Ensign has provided key MITRE ATT&CK techniques for each relevant context for readers to use for follow-on defensive actions such as Red Teaming, threat hunting, and to tune the detection measures. Full versions of the techniques heatmaps can be found in Appendix A with links to download MITRE ATT&CK Navigator JSON files for further review, and top tactics can be found in Appendix C. Full versions of the vulnerabilities observed in the territories can be found in Appendix B.

## Overview of Territorial Insights

We saw Technology, Media and Telecommunications (TMT) as the top industry group targeted across all the territories. This is attributed to the increased levels of digitalisation post-pandemic and the push for greater productivity through exploitation of higher network bandwidth, AI and automation as well as the push for digital payments and digital trade systems across ASEAN and the Asia Pacific region.

Our analysis of the top techniques observed saw T1110: Brute Force common across Singapore, Malaysia & Indonesia and the Greater China Region. Amongst others, T1595: Active Scanning and T1078: Valid Accounts were observed across Singapore, Malaysia & Indonesia. T1071: Application Layer Protocol was observed across Singapore and the Greater China Region.

The Government industry group was observed to be targeted across Malaysia, Indonesia, South Korea, Australia and the Greater China Region. We attribute this to political events such as elections or geopolitical matters such as the US-China tensions.

The Financial services industry group was observed to be targeted across Singapore, Indonesia, South Korea, Australia and the Greater China Region. We attribute this to the natural concentration of personal data, which is useful for espionage and surveillance related activities, as well as access to funds, especially through cryptocurrency wallets and brokerage accounts.

The Manufacturing industry group was observed to be targeted across Singapore, Malaysia, Indonesia and South Korea. With the rebalancing of manufacturing capacity due to “de-risking” efforts between US and China, Southeast Asian countries and allies of US (i.e. South Korea) benefits from ramped up manufacturing demand which is progressively driving the economic growth post-pandemic. Industrial espionage is also a common reason why threat actors are interested in this industry group. The threat actors typically target the trade secrets and industrial designs, including business relationships and contracts. Additionally, some threat actors are interested in having the capability to cause disruption to the supply chain by targeting the companies in this industry group.

| Territory | Top Techniques Observed