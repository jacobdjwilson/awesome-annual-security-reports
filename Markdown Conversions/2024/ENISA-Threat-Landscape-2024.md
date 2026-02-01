# ENISA THREAT LANDSCAPE 2024

## About ENISA

The European Union Agency for Cybersecurity, ENISA, is the Union’s agency dedicated to achieving a high common level of cybersecurity across Europe. Established in 2004 and strengthened by the EU Cybersecurity Act, the European Union Agency for Cybersecurity contributes to EU cyber policy, enhances the trustworthiness of ICT products, services and processes with cybersecurity certification schemes, cooperates with Member States and EU bodies and helps Europe prepare for the cyber challenges of tomorrow. Through knowledge sharing, capacity building and awareness raising, the Agency collaborates with its key stakeholders to strengthen trust in the connected economy, to boost resilience of the Union’s infrastructure and, ultimately, to keep Europe’s society and citizens digitally secure. More information about ENISA and its work can be found at: www.enisa.europa.eu.

## Contact

To contact the authors, please use etl@enisa.europa.eu
For media enquiries about this paper, please use press@enisa.europa.eu

## Editors

Ifigeneia Lella, Marianthi Theocharidou, Erika Magonara, Apostolos Malatras, Rossen Svetozarov Naydenov, Cosmin Ciobanu, Georgios Chatzichristos – European Union Agency for Cybersecurity

## Contributors

Claudio Ardagna, Stephen Corbiaux, Koen Van Impe

## Acknowledgements

We would like to thank the ENISA Advisory Group and the National Liaison Officers network for their valuable feedback, as well as ENISA colleagues Jamila Boutemeur and Johannes Clos for their invaluable review.

We would also like to thank the Information Integrity and Countering Foreign Information Manipulation and Interference Division (SG. STRAT.4) for sharing the data on information manipulation and revising and contributing to Chapter 9.

## Legal Notice

This publication represents the views and interpretations of ENISA, unless stated otherwise. It does not endorse a regulatory obligation of ENISA or of ENISA bodies pursuant to the Regulation (EU) No 2019/881.

ENISA has the right to alter, update or remove the publication or any of its contents. It is intended for information purposes only and it must be accessible free of charge. All references to it or its use as a whole or partially must contain ENISA as its source.

Third-party sources are quoted as appropriate. ENISA is not responsible or liable for the content of the external sources including external websites referenced in this publication.

Neither ENISA nor any person acting on behalf of ENISA is responsible for the use that might be made of the information contained in this publication.

ENISA maintains its intellectual property rights in relation to this publication.

## Copyright Notice

© European Union Agency for Cybersecurity (ENISA), 2024

This publication is licenced under CC-BY 4.0 “Unless otherwise noted, the reuse of this document is authorised under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence (https://creativecommons.org/licenses/by/4.0/). This means that reuse is allowed, provided that appropriate credit is given and any changes are indicated”.

For any use or reproduction of photos or other material that is not under the ENISA copyright, permission must be sought directly from the copyright holders.

ISBN: 978-92-9204-675-0, DOI: 10.2824/0710888

---

# Table of Contents

1.  THREAT LANDSCAPE OVERVIEW
2.  THREAT ACTOR TRENDS
3.  VULNERABILITIES LANDSCAPE
4.  RANSOMWARE
5.  MALWARE
6.  SOCIAL ENGINEERING
7.  THREATS AGAINST DATA
8.  THREATS AGAINST AVAILABILITY: DENIAL OF SERVICE
9.  INFORMATION MANIPULATION AND INTERFERENCE
A ANNEX: MAPPING TO MITRE ATT&CK FRAMEWORK
B ANNEX: RECOMMENDATIONS

---

# Executive Summary

2024 marks the 20th anniversary of the European Union Agency for Cybersecurity, ENISA. ENISA has been constantly monitoring the cybersecurity threat landscape and monitoring on its state with its annual ENISA Threat Landscape (ETL) report and additionally with a series of situational awareness and cyber threat intelligence products.

Over time, the ETL has served as a crucial tool for comprehending the present state of cybersecurity within the European Union (EU), furnishing insights into trends and patterns. This, in turn, has guided pertinent decisions and prioritisation of actions and recommendations in the domain of cybersecurity.

Reporting over the course of 2023 and 2024, ETL highlights findings on the cybersecurity threat landscape during a yearlong geopolitical escalation. Throughout the latter part of 2023 and the initial half of 2024, there was a notable escalation in cybersecurity attacks, setting new benchmarks in both the variety and number of incidents, as well as their consequences. The ongoing regional conflicts still remain a significant factor shaping the cybersecurity landscape. The phenomenon of hacktivism has seen steady expansion, with major events taking place (e.g. European Elections) providing the motivation for increased hacktivist activity.

7 prime cybersecurity threats were identified, with threats against availability topping the chart and followed by ransomware and threats against data, and the report provides a relevant deep-dive on each one of them by analysing several thousand publicly reported cybersecurity incidents and events:

*   Ransomware
*   Malware
*   Social Engineering
*   Threats against data
*   Threats against availability: Denial of Service
*   Information manipulation and interference
*   Supply chain attacks

The report is complemented by a detailed analysis of the vulnerability landscape during 2023 and 2024, as well as a detailed analysis of four distinct threat actors’ categories, namely:

*   State-nexus actors;
*   Cybercrime actors and hacker-for-hire actors;
*   Private Sector Offensive actors (PSOA);
*   Hacktivists.

With 2024 being the year that NIS2 Directive comes into force, an analysis of the cybersecurity threat landscape across different sectors is provided. Notably, we have again observed a large number of events targeting organisations in the public administration (19%), transport (11%) and finance (9%) sectors.

The key findings and judgments in this assessment are based on multiple and publicly available resources. The report is mainly targeted at strategic decision-makers and policy-makers, while also being of interest to the technical cybersecurity community.

---

# 1. THREAT LANDSCAPE OVERVIEW

In its twelfth edition, the ENISA Threat Landscape (ETL) report offers a broad overview of the cybersecurity threat landscape. Over time, the ETL has served as a crucial tool for comprehending the present state of cybersecurity within the European Union (EU), furnishing insights into trends and patterns. This, in turn, has guided pertinent decisions and prioritisation of actions and recommendations. The ETL report combines strategic and technical elements, catering to both technical and non-technical audiences. The ETL 2024 report has been validated and supported by the ENISA Advisory Group and the ENISA National Liaison Officers (NLO) Network.

Throughout the latter part of 2023 and the initial half of 2024, there was a notable escalation in cybersecurity attacks, setting new benchmarks in both the variety and number of incidents, as well as their consequences. The ongoing regional conflicts still remain a significant factor shaping the cybersecurity landscape. The phenomenon of hacktivism has seen steady expansion, marked by the emergence of numerous new groups. Major events taking place at a national or European level provided the motivation for increased hacktivist activity during the reporting period (e.g. European Elections).

The ETL 2024 report follows the same customary approach, drawing on diverse open-source data and cyber threat intelligence sources. It pinpoints significant threats, discerns emerging trends and offers practical high-level strategies for mitigating risk. This year's ETL continues to use the officially endorsed ENISA Cyber Security Threat Landscape Methodology ¹, which was released in 2022. The ENISA CTL Methodology serves as a foundational framework for the transparent and systematic creation of comprehensive cybersecurity threat landscapes, spanning horizontal, thematic and sector-specific perspectives. This process is characterised by rigorous data collection and analysis procedures.

## 1.1 METHODOLOGY

The ENISA Cybersecurity Threat Landscape (CTL) methodology ² was used to produce the ETL 2024 report. The methodology was published in July 2022.

The ENISA Threat Landscape (ETL) 2024 report is based on information from open sources, mainly of a strategic nature and ENISA’s own Cyber Threat Intelligence (CTI) capabilities. It covers more than one sector, technology and context. The report aims to be industry and vendor agnostic. It references or cites the work of various security researchers, security blogs and news media articles throughout the text in multiple footnotes to validate findings and statements. The time span of the ETL 2024 report is July 2023 to June 2024 and is referred to as the 'reporting period' throughout the report.

During the reporting period, ENISA gathered a list of major incidents as they appeared in open sources through situational awareness. This list serves as the foundation for identifying the list of prime threats and the source material for several trends and statistics in the report.

¹ https://www.enisa.europa.eu/publications/enisa-threat-landscape-methodology.
² ENISA Cybersecurity Threat Landscape (CTL) methodology, July 2022. https://www.enisa.europa.eu/publications/enisa-threat-landscape-methodology.

Subsequently, an in-depth desk research of available literature from open sources such as news media articles, expert opinion, intelligence reports, incident analysis and security research reports were conducted by ENISA and external experts. Note that many intelligence and research reports are written on the basis of a January to December year, contrary to the ETL’s reporting period which is from July to June. Through continuous analysis, ENISA derived trends and points of interest. The key findings and assessments are based on multiple and publicly available resources which are provided in the references used for the development of this document.

Within the report, we differentiate between what has been reported by our sources and what is our assessment. When conducting an assessment, we convey probability by using words that express an estimate of likelihood³.

When we refer to threat actors in this report, we use the naming convention used by the company revealing the campaign, as well as a number of aliases⁴ commonly used in the industry.

## 1.2 PRIME THREATS

According to the findings detailed in this report, the ENISA Threat Landscape 2024 report highlights and directs attention toward eight prime threat types (see Figure 1). These particular threat types have been singled out due to their prominence over the years, their widespread occurrence and the significant impact resulting from the realisation of these threats.

*   **Ransomware**
    According to ENISA’s Threat Landscape for Ransomware Attacks⁵ report, ransomware is defined as a type of attack where threat actors take control of a target’s assets and demand a ransom in exchange for the return of the asset’s availability or in exchange for publicly exposing the target’s data. This definition is needed to cover the changing ransomware threat landscape, the prevalence of multiple extortion techniques and the various goals, other than solely financial gains, of the perpetrators. Ransomware has been, once again, one of the prime threats during the reporting period, with several high profile and highly publicised incidents.

*   **Malware**
    Malware, also referred to as malicious code and malicious logic, is an overarching term used to describe any software or firmware intended to perform an unauthorised process that will have an adverse impact on the confidentiality, integrity or availability of a system.

*   **Social Engineering**
    Social engineering encompasses a broad range of activities that attempt to exploit human error or human behaviour with the objective of gaining access to information or services. It uses various forms of manipulation to trick victims into making mistakes or handing over sensitive or secret information. Users may be lured to open documents, files or e-mails, to visit websites or to grant access to systems or services. Although the lures and tricks used may abuse technology, they rely on a human element to be successful. This threat canvas consists mainly of the following attack vectors: phishing, spear-phishing, whaling, smishing, vishing, watering hole attack, baiting, pretexting, quid pro quo, honeytraps and scareware. While social engineering techniques are often used to gain initial access, they may also be

³ MISP estimative language https://www.misp-project.org/taxonomies.html#_estimative_language.
⁴ MISP Galaxies and Clusters https://github.com/MISP/misp-galaxy.
⁵ ENISA Threat Landscape for Ransomware Attacks https://www.enisa.europa.eu/publications/enisa-threat-landscape-for-ransomware-attacks.

used at later stages in an incident or breach. Notable examples are business e-mail compromise (BEC)⁶, fraud, impersonation, counterfeit and, more recently, extortion.

*   **Threats against data**
    A data breach is defined in the GDPR as any breach of security leading to the accidental or unlawful destruction, loss, alteration or unauthorised disclosure of or access to personal data transmitted, stored or otherwise processed (article 4.12 GDPR). Technically speaking, threats against data can be broadly classified as data breach or data leak. Though often used as interchangeably, they entail fundamentally different concepts that mostly lie in how they happen⁷ ⁸.

    Data breach is an intentional cyber-attack brought by a cybercriminal with the goal of gaining to unauthorised access and release sensitive, confidential or protected data. In other words, a data breach is a deliberate attack against a system or organisation with the intention of stealing data. Data leak is an event (such as misconfigurations, vulnerabilities or human errors) that can cause the unintentional loss or exposure of sensitive, confidential or protected data (intentional attacks are sometimes referred to as data exposure).

*   **Threats against availability: Denial of Service**
    DDoS targets system and data availability and, though it is not a new threat, it plays a significant role in the cybersecurity threat landscape⁹ ¹⁰. Attacks occur when users of a system or service are not able to access relevant data, services or other resources. This can be accomplished by exhausting the service and its resources or overloading the components of the network infrastructure¹¹.The impact of DDoS attacks is often limited and symbolic ¹².

*   **Information Manipulation**
    Foreign Information Manipulation and Interference (FIMI) describes a mostly non-illegal pattern of behaviour that threatens or has the potential to negatively impact values, procedures and political processes. Such activity is manipulative in character, conducted in an intentional and coordinated manner. FIMI can be carried out by state or non-state actors, including their proxies inside and outside their own territory; in this report we study the threat regardless of its origin.

It should be noted that the aforementioned threats involve categories and refer to collections of diverse types of threats that have been consolidated into the seven areas mentioned above. Each of the threat categories is further analysed in a dedicated chapter in this report with the exception of the supply chain, which elaborates on its particularities and provides more specific information on findings, trends, attack techniques and mitigation vectors.

⁶ Internet Organised Crime Threat Assessment IOCTA 2024.pdf (europa.eu)
⁷ https://blog.f-secure.com/data-breach-and-data-leak-whats-the-difference.
⁸ https://www.upguard.com/blog/data-breach-vs-data-leak#:~:text=Simply%20put%2C%20a%20data%20leak,Apps%20data%20leak%20in%202021.
⁹ Federal Office for Information Security (BSI), The State of IT Sec in Germany, September 2020.
¹⁰ Europol, Internet Organised Crime Threat Assessment (IOCTA) 2020, https://www.europol.europa.eu/activities-services/main-reports/internet-
organised-crime-threat-assessment-iocta-2020.
¹¹ CISA, Understanding Denial-of-Service Attacks, November 2019. https://www.uscert.gov/ncas/tips/ST04-015.
¹² Nederlandse organisaties doelwit van DDoS-aanvallen | Nieuwsbericht | Nationaal Cyber Security Centrum (ncsc.nl)

![Figure 1: ENISA Threat Landscape 2024 - Prime threats](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-1-enisa-threat-landscape-2024-prime-threats)

In the following figure it can be seen that for another year ransomware and DDoS attacks were the most reported forms of attacks during the reporting period and accounted for more than half of the observed events followed by threats related to data. In several cases incidents involved more than one threat category and were thus analysed in the context of all respective categories. Given that the ETL is based on publicly available information and the fact that such information might not always provide the full picture, in certain cases incidents could not be classified into any threat category.

![Figure 2: Breakdown of analysed incidents by threat type (July 2023 till June 2024)](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-2-breakdown-of-analysed-incidents-by-threat-type-july-2023-june-2024)

## 1.3 KEY TRENDS

The list below summarises the main trends observed in the cyber threat landscape during the reporting period. Further details and analysis of the trends may be found throughout the various chapters that comprise the ENISA threat landscape of 2024.

*   Threats against availability (DDoS) and Ransomware ranked at the top during the reporting period for another year.
*   Living Off Trusted Sites (LOTS): Threat actors extended their stealth techniques into the cloud, using trusted sites and legitimate services to avoid detection and disguising Command and Control communications (C2) as ordinary traffic or innocuous messages on platforms like Slack and Telegram.
*   Geopolitics continued to be a strong driver for cyber malicious operations.
*   Advancements in defensive evasion techniques: Cybercrime groups, especially ransomware operators, evaded detection by using Living Off The Land (LOTL) techniques. to blend into environments and mask their malicious activities.
*   There has seen a sharp increase¹³ ¹⁴ in Business Email Compromise (BEC) incidents¹⁵
*   Extortion by weaponizing disclosure requirements, pushing companies to fulfil extortion demands ahead of the required reporting deadline.
*   Ransomware attacks appear to have stabilized in quite high numbers in regards to the previous reporting period
*   Ever more impactful law enforcement operations, such as Operation Chronos and Operation Endgame.
*   AI tools for cyber criminals: Threat actors used tools such as FraudGPT and large language models to co-author scam emails and generate malicious PowerShell scripts.
*   19,754 vulnerabilities were identified with 9.3% fell into the ‘critical’ category and 21.8% were categorised as ‘high’.
*   Information stealers continue to be heavily used by threat actors: Due to the popularity of IABs and downloaders. Information stealers are now essential components in attack chains.
*   Hacktivists overlapping their activities with State-nexus actors: A notable trend is the increasing similarity between State-nexus actors and alleged hacktivist activities.
*   Data leak site have started being considered to be unreliable. Many of the data leaks posted are duplicates of previous attacks or wrongly attributed to the Lockbit ransomware group. This follows the disruption of their operations by Operation Chronos.
*   Recent surge in mobile banking trojans has been observed, with a concomitant increase in the complexity of their attack vectors.
*   Malware-as-a-Service (MaaS) offerings continued to be a significant and rapidly evolving threat, particularly since mid-2023.
*   Supply chain compromises through social engineering are emerging: for example, in March 2024, backdoor code was introduced in an open-source project XZ Utils, a set of tools and libraries used for data compression ¹⁶.
*   Data compromise increased in 2023-2024. There was a rise in data compromises leading up to 2021 and although this trend remained relatively stable in 2022, it began to increase once more in 2023 and showed signs of maintaining this momentum in 2024.
*   DDoS-for-Hire allows large-scale attacks to be launched by unskilled users having access to DDoS services.
*   Information manipulation continues to be a key element of Russia’s war of aggression against Ukraine, although an effort to further localise content and, at the same time, to globalise its presence is observed. Manipulating information in response of specific news seems to have increased, probably because 2024 has been marked by many major events, elections in particular.
*   The threat of AI-enabled information manipulation has been observed, but still on a limited -albeit evolving - scale. For example, some threat actors are experimenting with AI for information manipulation seemingly to assess how AI can be exploited in this context.

## 1.4 EU PRIME THREATS

Cyber-attacks continue to increase on the global scale; however, ENISA’s scope is primarily focused on EU member states and thus more emphasis is placed on the landscape within the EU.

Figure 3 shows a significant increase in events in the EU in the first half of 2024 compared to the second half of 2023, though on a global scale (non-EU) the spread seems to be more even. It's important to recognise that the observed number of events can be influenced by various factors. An increase in reported cyber-attacks doesn't necessarily indicate an actual rise in the number or severity of attacks. This surge could be due to heightened media or public attention to specific events, leading to more incidents being documented in open-source intelligence (OSINT) channels, or threat actors claiming victims with no real impact on those victims.

![Figure 3: Break down of Global and EU events (July 2023 – June 2024)](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-3-breakdown-of-global-and-eu-events-july-2023-june-2024)

Throughout the reporting period, EU Member States continued to be affected by ongoing geopolitical crises, with a growing number of threat actors directing their efforts against both public and private organisations. These kinds of events more often fall under the DDoS threat (chapter 2, section 4, and chapter 7) with little to no impact in most of the cases reported through OSINT. Ransomware attacks have shown a decrease (chapter 4) in the EU.

ENISA observed 11,079 incidents, including 322 incidents specifically targeting two or more EU Member States (labelled ‘EU’) as it can be seen in Figure 4 which shows a timeline of when the events where first reported through open-source channels. In addition, throughout this iteration of the ETL it can be seen that ransomware and DDoS still remained the two prime threats for the EU as shown in Figure 5.

![Figure 4: Timeline of EU events (count of number of observed incidents a month)](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-4-timeline-of-eu-events-count-of-number-of-observed-incidents-a-month)

![Figure 5: EU breakdown of number of threats by threat group](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-5-eu-breakdown-of-number-of-threats-by-threat-group)

## 1.5 SUPPLY CHAIN

Supply chain attacks has become a threat on a horizontal level touching upon multiple of the other threats. The reason why for this year it was decided not to have a separate chapter even though was that few incidents were reported to be of a supply chain attack. This does not mean that we did not have incidents just that maybe they were not reported publicly as being or affecting supply chains.

One of the most controversial incidents during the reporting period was of the incident with 3CX which offered a glimpse into the potentials threats we face. In March 2024, backdoor code was introduced in an open-source project XZ Utils¹⁷, a set of tools and libraries used for data compression.¹⁸ Luckily, the vulnerability was discovered by a software engineer who investigated CPU spikes resulting from the backdoor. The vulnerability was considered critical, as it allowed for easy remote code execution through SSH. This was possible as the malicious actor was made maintainer of the project after a long-lasting social engineering campaign.

The account creation dates to 2021, and the user’s first code commit in the project was pushed in 2022. In that period, different (but as it would later seem, connected) accounts started pressuring the original maintainer, accusing him of standing in the way of the project’s advancement, suggesting that he would start giving over the reigns over the project. In January, the threat actor took over as primary contact over the project. Over 2023 and 2024, different steps were then performed to prepare the environment and eventually push the backdoor.¹⁹

In a similar case the OpenJS Foundation received a suspicious series of emails with similar messages, bearing different names and overlapping GitHub-associated emails, asking OpenJS to take action to update one of its popular JavaScript projects to “address any critical vulnerabilities,”. They also requested OpenJS to designate them as a new maintainer of the project despite having almost no prior involvement. The Open Source Security (OpenSSF) and OpenJS Foundations called out all open source maintainers to be alert for social engineering takeover attempts, to recognize the early threat patterns emerging, and to take steps to protect their open source projects. ²⁰

Recent public reports also have highlighted a general high interest ²¹ , primarily from North Korean-nexus groups ²², characterised by more aggressive and expansive intrusions across multiple networks. There has also been a focus²³ ²⁴ on attacks that target update mechanisms or compromise the open-source software supply chain. Such attacks²⁵ ²⁶ ²⁷ involve name or repository confusion, tricking developers into using compromised software, or embedding malware in test files. A notable instance involved the introduction of a backdoor in XZ Utils. The sophistication, meticulous planning, and duration of this campaign suggest the involvement of a well-resourced actor, although specific attribution remains unclear at this time. Build systems became²⁸ ²⁹ a popular target as well for groups associated with Russia and North Korea, but primarily due to vulnerabilities in publicly accessible systems.

¹⁷ The XZ-factor: social vulnerabilities in open source projects | By our experts | National Cyber Security Centre (ncsc.nl)
¹⁸ https://lists.debian.org/debian-security-announce/2024/msg00057.html
¹⁹ https://gist.github.com/thesamesam/223949d5a074ebc3dce9ee78baad9e27
²⁰ https://openssf.org/blog/2024/04/15/open-source-security-openssf-and-openjs-foundations-issue-alert-for-social-
engineering-takeovers-of-open-source-projects/
²¹ Mandiant - Assessed Cyber Structure and Alignments of North Korea in 2023 -
https://www.mandiant.com/resources/blog/north-korea-cyber-structure-alignment-2023
²² Notice | Media Center | NIS NATIONAL INTELLIGENCE SERVICE
²³ NSPX30: A sophisticated AitM-enabled implant evolving since 2005
https://www.welivesecurity.com/en/eset-research/nspx30-sophisticated-aitm-enabled-implant-evolving-since-2005/
²⁴ AVAST - GuptiMiner: Hijacking Antivirus Updates - https://decoded.avast.io/janrubin/guptiminer-hijacking-antivirus-
updates-for-distributing-backdoors-and-casual-mining/
²⁵ JPCERT - New Malicious PyPI Packages used by Lazarus - https://blogs.jpcert.or.jp/en/2024/02/lazarus_pypi.html
²⁶ APIIRO - Over 100,000 Infected Repos Found on GitHub - https://apiiro.com/blog/malicious-code-campaign-github-repo-
confusion-attack/
²⁷ Cyware - North Korean Hackers Targeting Developers with Malicious npm Packages - https://cyware.com/news/north-
korean-hackers-targeting-developers-with-malicious-npm-packages-2a033144
²⁸ CERT.pl - Russian Foreign Intelligence Service (SVR) Cyber Actors Use JetBrains TeamCity CVE in Global Targeting -
https://cert.pl/en/posts/2023/12/apt29-teamcity/
²⁹ Microsoft - Multiple North Korean threat actors exploiting the TeamCity CVE-2023-42793 vulnerability -
https://www.microsoft.com/en-us/security/blog/2023/10/18/multiple-north-korean-threat-actors-exploiting-the-teamcity-cve-
2023-42793-vulnerability/

Finally, out of the observed events that ENISA collected, the following ones affected sectors that offer services and products to other sectors: Digital infrastructure (8%), manufacturing (6%) business services (8%), energy (3%) and ICT service management (3%).

## 1.6 SECTORIAL ANALYSIS

Cyber threats are indiscriminate, impacting a wide range of industries and sectors. This is a direct consequence of our hyper-connected digital world. As the following figures illustrate, threat actors target every sector, highlighting the universal nature of cyber risk.

The sectors analysed in this report follow, in general, the classification of the sector categories in the Network and Information Security Directive (NIS2)³⁰. There are however some deviations, derived by the samples used, as the report may include events affecting sectors beyond the scope of the NIS2 directive. Examples include defence, education³¹, media and entertainment, retail and more. We have also grouped under the term ‘Digital service provider’, the sectors listed in NIS2 as ICT service management (MSPs and MSSPs) and digital providers. There is also a separate category, labelled as ‘all sectors’ which is used when events have an effect across sectors. During the analysis, other sectors were identified that are not currently within the scope of the NIS2 directive, such as consulting, legal, and hospitality services etc, which are grouped under the category ‘Services’.

![Figure 6 Targeted sectors per number of incidents (July 2023 - June 2024)](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-6-targeted-sectors-per-number-of-incidents-july-2023-june-2024)

During this reporting period in the overall global landscape, we have again observed a large number of events (Figure 6) targeting organisations in the public administration (19%), transport (11%) and finance (9%) sectors. Events targeting digital infrastructure (8%) and business services form a substantial portion of the events observed. We also observed a considerable number of events targeting civil society and not necessarily a particular sector (these are

³⁰ https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022L2555.
³¹ The education sector was coupled in our sample with the research sector, as they are often intertwined. While the research sector is considered to be within the scope of the NIS2 directive, educational organisations are not included.

labelled as ‘General Public’ and amount to 8% of the events observed). They consist of social engineering or information manipulation campaigns.

The prime threat was DDoS and it appears to target the entire range of the sectors (Figure 7). The most targeted sectors were public administration (33% out of DDoS events), transport (21% out of DDoS events), banking (12% out of DDoS events) and digital infrastructure (6% out of DDoS events).

These are followed by ransomware attacks and data-related threats. Ransomware appears to target different sectors indiscriminately during this reporting period, with Business services (18% out of ransomware events), Manufacturing (17% out of ransomware events) and Health (8% out of ransomware events) being more affected. Data related threats targeted all sectors, with the ones that hold personal information being more affected. Out of data related events, these affected general public (15%), public administration (12%), digital infrastructure (10%), finance (9%) and business services (8%).

29% of the events involving malware affected the general public, followed by malware infections in digital infrastructure (25%) and in public administration (11%). 9% of observed malware events affects all sectors.

Out of the observed events related to social engineering, 28% focused on the general public, followed by digital infrastructure (15%), public administration (10%) and finance (10%) sectors. Likewise, information manipulation campaigns targeted general public in most of the collected events.

![Figure 7: Observed events related to prime ETL threats in terms of the affected sectors](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-7-observed-events-related-to-prime-etl-threats-in-terms-of-the-affected-sectors)

More information on how each sector is affected during the reporting can be found in the following figure.

![Figure 8: ETL threats per sector](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-8-etl-threats-per-sector)

In the breakdown of the top 20 ‘active’ threat actors during the reporting period, the trend that actors are often sector-agnostic becomes evident once more, as nearly all of them are dispersed across various sectors. Similarly to 2023, public administration and transport remains a preference by the active Hacktivists groups.

![Figure 9 Threat actor per sector](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-9-threat-actor-per-sector)

## 1.7 MOTIVATION

Understanding the enemy and the motivation behind a cybersecurity incident or targeted attack is important because it can determine what an adversary is after. Assessing the motives provides an idea of the intentions of attackers and helps entities focus their efforts in defence on the most likely attack scenario for any particular asset.

For the third year ETL 2024 includes an assessment of the motivation behind the incidents observed during the reporting period. For this purpose, five distinct kinds of motivation that can be linked to threat actors have been defined:

*   Financial gain: any financially related action (carried out mostly by cybercrime groups);
*   Espionage: gaining information on IP (intellectual property), sensitive data, classified data (mostly executed by state-sponsored groups);
*   Destruction: any destructive action that could have irreversible consequences;
*   Ideological: any action backed up with an ideology behind it (such as hacktivism).

It is apparent that in the majority of cases the primary threats can be attributed to one or more motivations, with certain motivations emerging as more dominant than others. As with the previous iteration within the realm of Ransomware attacks, while the primary motivation typically revolves around financial gain, there is a small percentage where a disruptive motive also plays a role.

Following financial gain as the top motivation, disruption was the second most common motive, primarily due to the prevalence of DDoS attacks during the reporting period. These disruptive attacks were aimed at causing operational downtime.

![Figure 10: Motivation of threat actors per threat category](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024/files/figure-10-motivation-of-threat-actors-per-threat-category)

Additionally, most data-related threats were linked to multiple motivations, with financial gain being the primary driver. Ideology and espionage also played significant roles, as attackers sought to advance specific agendas or exfiltrate strategic information. This highlights the diverse motivations behind cyber threats, ranging from financial incentives to ideological and intelligence-gathering objectives.

For a considerable number of the events we have gathered, the motivation remains unclear. This lack of clarity could be due to either limited or undisclosed information or the victims themselves being unaware of the underlying motive.

## 1.8 STRUCTURE OF THE REPORT

The ENISA Threat Landscape (ETL) 2024 has maintained the core structure of previous ETL reports for highlighting the prime cybersecurity threats in 2023. Those familiar with previous versions will observe that the current editions now incorporate the CVE landscape within chapters that offer an overview of the most significant CVEs identified during the