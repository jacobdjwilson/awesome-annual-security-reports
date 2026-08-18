# Global Cyber Threat Intelligence (CTI)
## Annual Cyberthreat Trends Report - 2024
### March 2025

Organization: Deloitte  
Report Title: Global-Cyber-Threat-Intelligence-Report  
Year: 2025  

## Table of Contents
- [Executive Overview](#executive-overview)
- [Cross-Industry Threat Vectors](#cross-industry-threat-vectors)
- [Cross-Industry Initial Access Techniques](#cross-industry-initial-access techniques)
- [Threat Vector Highlights](#threat-vector-highlights)
- [Summary of Data](#summary-of-data)
- [Threat Actors](#threat-actors)

---

## Executive overview

The following report highlights overarching cyber trends and emerging issues from January 1 to December 31, 2024.

### Highlights

- Ransomware continued to be the top threat vector for the year. The RaaS model facilitates the easy creation of new groups. Affiliates are not tied to one group, making attack attribution more challenging than in previous years.
- Due to its effectiveness, social engineering continued to trend as an initial access technique for cybercriminals. The exploitation of human behavior and mistakes is again rising as technical protections are increasingly effective.
- In 2024, Deloitte CTI observed a shift from brute-force attacks to using deliberately stolen username and password combinations to authenticate on corporate virtual private networks (VPNs).
- Deloitte IR teams noted on multiple occasions that threat actors used subscription-based cloud services, shifting away from the traditionally known open-source tools that offer similar capabilities.
- Malware, particularly infostealers, remained a prominent threat as many families have developed new iterations. Despite law enforcement's takedown of ResineStealer operations, large sample sets enable the malware to persist.

RansomHub emerged in February and operates under a ransomware-as-a-service (RaaS) model. The RansomHub threat group's differentiator is its ability to seamlessly accommodate affiliates across varying skill and experience levels[^1], [^2].

APT29 (aka. Midnight Blizzard) is a suspected nation-state cyberespionage group targeting government-related organizations globally. In 2024, the group conducted a spearphishing campaign that targeted multiple sectors[^1].

### Top trend incident response (IR) teams

#### Top threat vector observed
- **Ransomware**: With the emergence of over 30 new groups, ransomware remained the top threat vector for 2024. The adoption of artificial intelligence (AI) tools has led to more sophisticated attack techniques. Politically-motivated threat actors are also increasingly collaborating with RaaS operators [^1].
- **Social engineering**: Deloitte’s incident response (IR) teams noted that threat actors are honing their skills to exploit human behaviors as technical protections are increasingly effective. For example, threat actors are combining voice phishing (vishing) with business email compromise (BEC) attacks to steal user credentials [^1].

### Assessments
- Deloitte CTI assesses with high confidence that threat actors will continue to leverage third-party integrations between vendors and clients. Third-party compromises can spread rapidly and can affect multiple organizations with ease.
- Deloitte CTI assesses with moderate to high confidence that social engineering, with the aid of AI, will become a top threat vector in 2025 and beyond. Technical measures to detect AI-generated content and interactions are lagging, increasingly exposing end users to this threat.
- Deloitte CTI assesses with high confidence that nation-state groups will continue to pose significant challenges to global cybersecurity efforts.

---

## Cross-industry threat vectors

Throughout 2024, Deloitte CTI observed several overarching, cross-industry threat vectors not specific to a threat actor type. This section illustrates the impact of ransomware, third-party compromises, malware trends, and Deloitte's internal underground findings.

### Ransomware
- **Impact**: Significant
- **Likelihood**: Likely
- **Details**: 
  - Ransomware continued to remain a formidable threat to organizations globally. RaaS models have continued to mature, enabling less experienced and technical actors to conduct crimes[^3].
  - Emerging in February 2024, RansomHub has become the most active ransomware group in 2024, having claimed over 500 victims across various sectors[^1].
  - The primary method behind ransomware breaches is leveraging VPNs for initial access, with vulnerability exploitation combined with credential-based attacks to bypass multi-factor authentication requirements[^3].
  - Nation-state advanced persistent threats (APTs) have been increasingly deploying ransomware by collaborating with cybercriminal groups or developing their own strains[^4].

### Third-party compromise
- **Impact**: Moderate
- **Likelihood**: Likely
- **Details**: 
  - Third-party compromises increased in 2024, partly due to the use of zero-day exploits for ransomware and extortion attacks[^5].
  - Third-party compromise attacks have the potential to be widespread. Data from these compromises can be leaked on dark web forums for sale[^1].

### Malware trends
- **Impact**: Significant
- **Likelihood**: Likely
- **Details**: 
  - In 2024, security researchers observed new iterations of previously known malware, while law enforcement disrupted some prevalent malware families. In October, a global operation led to the takedown of RedLineStealer. Although activity levels have decreased due to the number of RedLine samples available, malware activity persists[^6].
  - LummaStealer continued to make an impact and experienced high levels of growth during the year[^6].
  - One notable development is a packer-as-a-service (PaaS) dubbed "HeartCrypt" that threat actors used to protect malware by packing malicious code into legitimate binaries[^7].

### Underground trends
- **Impact**: Significant
- **Likelihood**: Roughly even chance
- **Details**: 
  - The cybercriminal underground continued its rapid transformation toward decentralized, specialized, and professionally-structured operations. Due to law enforcement pressure, popular marketplaces splintered, driving activity into closed forums and encrypted channels [^1], [^8], [^9].
  - AI became a key enabler, powering deepfake campaigns, PaaS offerings, and automated translation to target victims worldwide. Ransomware syndicates refined multi-faceted extortion tactics, while thriving initial access brokers (IABs) fueled widespread data breaches and attacks. Meanwhile, criminals embraced privacy-centric payment methods, particularly stablecoins, to evade detection [^1], [^10], [^11].
  - Despite several high-profile takedowns, the underground community demonstrated resilience through collaboration, bulletproof hosting, and corporate-like organizational structures [^1], [^8], [^9], [^12].

---

## Cross-industry initial access techniques

Deloitte CTI observed that the most leveraged initial access techniques in 2024 were vulnerability exploitation, social engineering, a combination of VPN exploitation with stolen passwords, and phishing. These techniques were the most impactful across all industry sectors and verticals.

### Vulnerability exploitation
- **Impact**: Severe
- **Likelihood**: Roughly even chance
- **Details**: 
  - Throughout 2024, threat actors continued to exploit vulnerabilities, including zero-day vulnerabilities, to gain initial access to their victims' networks and environments.
  - Large-scale ransomware groups are among the perpetrators, with Clop exploiting two zero-day vulnerabilities in December[^1].
  - Notably, threat actors continued to exploit old vulnerabilities; some large-impact exploits in 2024 were over five years old [^13].

### Social engineering
- **Impact**: Severe
- **Likelihood**: Roughly even chance
- **Details**: 
  - Due to its effectiveness, social engineering continues to trend as an initial access technique for cybercriminals.
  - In 2024, Deloitte IR teams noted a trend in threat actors combining vishing with BEC attacks in multiple independent investigations, predominantly targeting service providers across multiple industries.
  - This method involves stealing user credentials by calling the service provider's customer support to initiate a password reset for one of their clients, using a pre-registered email domain impersonating the client. One IR case revealed that the squatted domain had only been registered three days before the call, indicating this was a targeted operation [^1].
  - The exploitation of human behavior and mistakes was again on the rise as technical protections are increasingly effective.

### Combination: VPN exploitation with stolen passwords
- **Impact**: Severe
- **Likelihood**: Roughly even chance
- **Details**: 
  - VPN exploitation remains a leading initial access vector. In 2024, Deloitte CTI observed a shift from brute-force attacks to using deliberately stolen username and password combinations to authenticate on the corporate VPN.
  - Threat actors gain credentials from data breaches exposed on the dark web, IABs, or social engineering methods.
  - Additionally, Deloitte IR teams noted threat actors’ expanding toolsets for transversing firewalls with cloud service providers as proxies. Deloitte IR teams noted on multiple occasions that threat actors used subscription-based cloud services, shifting away from the traditionally known open-source tools that offer similar capabilities [^1].

### Phishing
- **Impact**: Severe
- **Likelihood**: Almost certain
- **Details**: 
  - Working with the CTI team, Deloitte's Managed Extended Detection and Response (MXDR) team observed peak phishing detections in February and May 2024, followed by a decline in detections in the third quarter, then picking up again in the fourth quarter.
  - The ability of large language models (LLMs) to generate phishing content presents a significant challenge to traditional threat detection. Threat actors can generate 1,000 phishing emails in under two hours for as little as US$6.00, with LLMs likely contributing to the overall 1,265 percent increase in phishing attacks in 2024 [^1].
  - AI has enabled threat actors to craft highly personalized and timely phishing campaigns, enhancing their relevance and persuasiveness to their intended targets [^1].

---

## Threat vector highlights

### Ransomware

![Bar chart showing the number of attacks ransomware actors claimed responsibility for during 2023 and 2024, peaking in Q4 2024]

- Deloitte CTI observed a 17 percent increase in ransomware attack claims in 2024, peaking in the fourth quarter with 57 percent more claims compared to the fourth quarter of 2023 [^1]. This increase is likely due to the emergence of over 30 new ransomware groups and the increased prevalence of the RaaS model, which groups such as RansomHub utilized throughout 2024 [^3].
- RansomHub, which security researchers first observed in February 2024, was the most active ransomware in 2024, with the highest number of victims listed on its leak site, followed by LockBit and Play Ransomware, who—comparatively—have both been active since early 2022 [^1].
- The most common root causes for successful ransomware attacks were exploited vulnerabilities, compromised credentials, and phishing attacks [^35]. Compromised credentials have traditionally been the primary initial access vector for ransomware attacks; however, the adoption of AI tools and advanced attack techniques has led to more complex and innovative attacks and methods of initial access [^14].
- The average cost of a ransomware data breach reached US$4.91 million [^15].
- Successful initiatives led by international law enforcement agencies are pressuring the ransomware ecosystem at every level. Past initiatives have involved taking down command-and-control (C2) servers, malware dropper botnets, cryptocurrency exchanges, and the arrests of key actors from notable ransomware groups [^16].

#### RaaS highlight
- Top five ransomware variants observed in 2024:
  - LockBit (185)
  - RansomHub (516)
  - Play Ransomware (209)
  - BlackCat/ALPHV (353)
  - Akira (514)
- Before 2024, the dominant groups within the ransomware landscape were the RaaS operators LockBit and ALPHV, who had been the most active groups since 2022 [A]. However, the February 2024 Europol-led "Operation Cronos" resulted in the disruption of LockBit's infrastructure and an exit scam by the ALPHV group, respectively [^17].
- Security researchers estimate that two-thirds of LockBit's new victim announcements since February are duplicated or unverifiable. This activity is likely an attempt to inflate the group's perceived activity levels [3]; no activity has been seen from ALPHV since its exit scam [^1]. While law enforcement activity was initially thought to have intensified distrust and signaled the collapse of the RaaS community, many smaller and more agile ransomware groups have since emerged to capitalize on the void these groups left [^2].
- Security researchers have attributed RansomHub's emergence and success in 2024 to its aggressive affiliate-friendly RaaS model. The group's affiliates have displayed diverse skills, some utilizing advanced techniques while others have relied on simpler and more accessible methods. This variety in operations showcases the group's adaptability and ability to accommodate affiliates with differing experience levels [^2].
- Other notable RaaS operations that emerged in 2024 include El Dorado/BlackLock, Lynx, Fog, and APT73/BASHE, which employ sophisticated, varied tactics, techniques, and procedures (TTPs), and have been aggressively active since their emergence [^2].
- The prevalence of the RaaS model has significantly increased the frequency, destructiveness, and complexity of ransomware operations throughout 2024. IABs continued to specialize in obtaining access to potential victims, and affiliates to focus on navigating compromised networks, payload deployment, and extortion by enabling developers to concentrate on creating and improving ransomware and its components. Aspiring cybercriminals can now specialize in different areas of RaaS operations, lowering the entry barriers for new actors and increasing the potential scale of ransomware operations in the future [^18].
- Many politically-motivated threat groups have been utilizing RaaS in their operations. Notably, the hacktivist group CyberVolk released its own RaaS platform in June 2024 and has been promoting alliances with other hacktivist groups, such as NoName057(16), and pre-emptively advertising its own politically motivated attacks, which are distinct from financially-motivated ransomware attacks [^19].

### Underground trends

During 2024, multinational law enforcement operations increased, resulting in significant takedowns of well-known criminal marketplaces and hosting services; however, sustained disruption continues to be challenging.

#### Evolving countermeasures and community resilience
Throughout 2024, multinational task forces significantly intensified their campaigns against cybercriminal operations. High-profile initiatives, including joint actions spearheaded by Interpol and other law enforcement agencies, targeted well-established dark web marketplaces such as Nemesis Marketplace and BreachForums, which are bulletproof hosting providers, and coordinated ransomware affiliates. These takedowns led to high-impact arrests, the seizure of illicit funds, the dismantling of infrastructure used for malware distribution, and the temporary takedown of LockBit because of significant law enforcement actions involving 12 countries and Eurojust. Seized domains and shuttered marketplaces disrupted criminal revenue streams, created temporary friction within underground communities and complicated actors' ability to trade goods and services [^1], [^8], [^12], [^20], [^21].

Although these concerted efforts yielded visible results, they also underscored the persistent resilience of cybercriminal networks. Many operators seamlessly pivoted to alternative platforms or rebranded under new identities, highlighting the migratory nature of illicit communities. Furthermore, many advanced criminals adept at operational security evaded detection by migrating to invite-only forums and adopting encrypted channels, limiting the success of traditional takedowns. Consequently, law enforcement agencies increasingly partnered with private sector entities, threat intelligence providers, cybersecurity firms, and hosting companies to share real-time data and develop more comprehensive investigations [A], [^13], [^9], [^20].

Going forward, this heightened collaboration between law enforcement and industry is expected to continue shaping future takedown strategies. Efforts such as targeting the financial conduits of cybercrime, improving cross-border legal frameworks, and bolstering digital forensic capabilities are essential to discouraging re-emergence and reducing criminal profitability; however, the cat-and-mouse dynamic remains. As authorities innovate in detection and disruption methods, cybercriminal actors likewise escalate their evasive tactics, test operational security boundaries, and thrive in the dark web's newly fragmented or hidden corners.

#### Implications for organizations and defenders
- **Temporary disruption vs. ongoing adaptation**: While takedowns impede criminal marketplaces, threat actors often reconstitute quickly, indicating a continual need for intelligence-driven defense [^1], [^22].
- **The value of collaboration**: Closer public-private teaming and information-sharing initiatives are essential in forging a broad picture of the threat landscape [^1], [^8], [^22].
- **Preparedness and agility**: Organizations should maintain robust monitoring of new or emerging dark web venues, so they can adapt their defensive strategies when criminals relocate or evolve their operations [^9], [^11].

---

## Summary of data

The Deloitte CTI performs internal threat research and gathers open-source intelligence, including cyber events from forums and news media dedicated to cyberthreat activities. The data in this section summarizes observed activity between January and December 2024.

### Cyber Events Observed by Threat Actor Type
- Cybercriminals
- Nation State
- Hacktivists
- Unattributed

### Cyber Events Observed Targeting Specific Industries
- **GPS**: Government & Public Services
- **TMT**: Technology, Media & Telecommunications
- **C**: Consumer
- **FS**: Financial Services
- **ER&I**: Energy, Resources & Industrials
- **LS&HC**: Life Sciences & Health Care

### Cyber Events Observed by Type
- Cyber espionage
- Data exfiltration
- Botnet
- Supply chain
- Influence operation
- Brute Force
- Others

---

## Threat actors

### Overview

- **Nation-state linked**
  - **Motivation**: Political, espionage, and financial
  - **Likelihood**: Likely, significant long-term impact
  - **Top Actors**: APT29, Salt Typhoon, and Volt Typhoon
  - **Details**: In 2024, nation-state-linked cyber actors intensified their operations, focusing on espionage and intelligence gathering. APT29, aka Cozy Bear, continued its sophisticated cyber-espionage campaigns targeting governmental and non-governmental organizations globally. Salt Typhoon conducted extensive cyber-espionage campaigns globally, particularly against North American targets. Volt Typhoon was active in cyber operations, employing advanced techniques to infiltrate networks, exfiltrate sensitive data, and monitor communications [^23].

- **Cybercriminals**
  - **Motivation**: Financial
  - **Likelihood**: Likely, significant immediate impact
  - **Top Actors**: Clop, LockBit, and RansomHub
  - **Details**: The aggressive activities of ransomware groups marked the cybercriminal landscape in 2024. Clop was responsible for several high-profile attacks, including those exploiting zero-day vulnerabilities. LockBit maintained its position as a dominant ransomware operator in spite of the earlier takedown. RansomHub emerged as a notable player, facilitating numerous attacks by offering RaaS [^24].

- **Hacktivists**
  - **Motivation**: Political
  - **Likelihood**: Roughly even chance, Moderate impact
  - **Top Actors**: CyberVolk and NoName057(16)
  - **Details**: Hacktivist activities in 2024 leveraged cyberattacks to advance political narratives and influence public opinion. CyberVolk targeted entities perceived as adversaries by engaging in website defacements and data leaks. NoName057(16) conducted distributed denial of service (DDoS) attacks against government and media websites in countries supporting European nation-states [^19].

- **Insider threats**
  - **Motivation**: Financial, revenge, fear (e.g., blackmail)
  - **Likelihood**: Malicious: Roughly even chance, severe impact. Unintentional: Likely, significant impact
  - **Top Actors**: Not applicable
  - **Details**: During 2024, insider threats remained a significant concern. Many incidents involved employees exploiting their access to sensitive information for personal gain or corporate espionage, resulting in data breaches, financial losses, and reputational damage [^25].

### Trending and emerging in 2024
![Scatter plot heatmap showing threat actors by likelihood, impact, and spread, highlighting APT29, RansomHub, NoName057(16), LockBit, CyberVolk, Clop, Volt Typhoon, and Salt Typhoon]

### Threat actor profiles | Trending and emerging

#### APT29
- **Category**: Nation state
- **Motive**: Political gain
- **Likelihood**: Likely (Risk Score: 54, Threat Score: 68)
- **Impact**: Significant (Risk Score: 25, Threat Score: 65)
- **Details**: APT29, also known as Midnight Blizzard, is a suspected nation state-sponsored cyber-espionage group with links to intelligence services and has been active since at least 2008. Security researchers have observed the group employing a variety of toolsets, most of which were custom-built and featured in highly targeted campaigns targeting government-related organizations in the Asia-Pacific region, Europe, and North America [^1]. The group leverages open-source tools, including Mimikatz and PsExec, alongside steganography for evasion [^1]. In 2024, the group conducted a spearphishing campaign targeting education, defense, government, and private sector organizations using malicious network communication protocol configuration files [^1].

#### Clop
- **Category**: Cybercriminal
- **Motive**: Financial gain
- **Likelihood**: Likely (Risk Score: 55, Threat Score: 80)
- **Impact**: Moderate (Risk Score: 25, Threat Score: 65)
- **Details**: Clop is a ransomware group operating under the RaaS scheme active since at least February 2019, believed to be operated by TA505 [^1]. It predominantly uses phishing emails and zero-day vulnerabilities, mainly targeting financial, industrial, technology, and health care sectors [^1]. Clop manages its own DLS, "CL0P^_-LEAKS," issuing high ransom demands up to tens of millions of dollars [^1]. In December 2024, the group was observed exploiting two zero-day vulnerabilities [^1].

#### CyberVolk
- **Category**: Hacktivist
- **Motive**: Political gain
- **Likelihood**: Very likely (Risk Score: 55, Threat Score: 80)
- **Impact**: Significant (Risk Score: 55, Threat Score: 80)
- **Details**: Established in March 2024 and officially active since July 1, CyberVolk is an Asia-based hacktivist group aligned with a politically-motivated APT organization including NoName057(16) and Killnet [^26]. It employs ransomware builders like AzzaSec, Diamond, LockBit, and Chaos [^19]. The group targets political entities opposing nation-state interests through website defacements and data leaks [^19]. Initial access is gained via IABs, social engineering, or brute-force attacks [^19].

#### LockBit
- **Category**: Cybercriminal
- **Motive**: Financial gain
- **Likelihood**: Very likely (Risk Score: 55, Threat Score: 80)
- **Impact**: Significant (Risk Score: 55, Threat Score: 80)
- **Details**: LockBit is a ransomware threat group observed since 2019 [^1], operating a RaaS model recruiting affiliates for up to 80 percent of ransoms. Targeting global commercial, communications, financial services, and retail sectors, LockBit updates TTPs continuously and utilizes a double-extortion strategy [^27]. Despite law enforcement interference in February 2024, the group continued targeting victims throughout the year [^1].

#### NoName057(16)
- **Category**: Hacktivist
- **Motive**: Political gain
- **Likelihood**: Very likely (Risk Score: 55, Threat Score: 80)
- **Impact**: Significant (Risk Score: 62, Threat Score: 45)
- **Details**: NoName057(16) is a hacktivist collective conducting HTTPS application-layer DDoS attacks against entities perceived as adversaries to national political interests [^28], [^29]. In September 2024, the group launched DDoS attacks on East Asian targets [^30]. It utilizes the custom crowdsourced botnet "DDOSIA," providing financial incentives to top contributors [^30].

#### RansomHub
- **Category**: Cybercriminal
- **Motive**: Financial gain
- **Likelihood**: Very likely (Risk Score: 62, Threat Score: 45)
- **Impact**: Significant (Risk Score: 62, Threat Score: 45)
- **Details**: RansomHub emerged in February 2024 as a financially motivated RaaS threat group [^1]. Affiliates allegedly retain the ransom payment on their crypto wallets and transfer a 10 percent cut to the operator [^1]. Targeting construction, financial services, retail, and technology sectors worldwide, RansomHub manages its own DLS with countdown timers [^1]. It has been recognized as one of the most prominent ransomware groups, claiming over 500 victims in 2024 [^31], [^1].

#### Salt Typhoon
- **Category**: Nation state
- **Motive**: Cyber espionage
- **Likelihood**: Likely (Risk Score: 18, Threat Score: 44)
- **Impact**: Moderate\* (Risk Score: 24, Threat Score: 49)
- **Details**: Salt Typhoon has conducted espionage operations since at least 2019, targeting government organizations, telecommunications, engineering, hospitality, and law firms [^1]. Distributing custom backdoors like "SparrowDoor" and "GhostSpider," the group breached multiple telecommunications companies in 2024 to steal call data of prominent political figures [^32], [^33]. Recovery efforts are expected to take years [^1].

#### Volt Typhoon
- **Category**: Nation state
- **Motive**: Cyber espionage
- **Likelihood**: Likely (Risk Score: 18, Threat Score: 44)
- **Impact**: Moderate\* (Risk Score: 24, Threat Score: 49)
- **Details**: Volt Typhoon is a nation-state actor observed since mid-2021 targeting communications, construction, education, government, manufacturing, maritime, technology, transportation, and utilities sectors in the Asia-Pacific and Americas [^1]. The group pre-positions itself on US critical infrastructure networks to enable disruption [^34]. It leverages living-off-the-land techniques, exploits known vulnerabilities, and uses tools like Mimikatz and Ntdsutil [^34].

_\*Note: The tangible impact of these threat actors depends on the global geopolitical context at a given time. If an event is averse to the sponsoring entity of these actors, the impact rating assessment will increase accordingly._

---

## Sourcing Statement
- **Tradecraft**: Deloitte CTI applies the Intelligence Community Directive 203 Analytic Standards to its products and reports.
- **Methodology**: Risk ratings are based on weighted factors, including threat actor sophistication, campaigns, frequency of employment, regional spread, and motivation.
- **Collection**: Deloitte CTI combines its proprietary collection with subscriptions to achieve maximum coverage.

---

## References

[^1]: Deloitte internal sources.
[^2]: Melnyk, S., "The New Face of Ransomware: Key Players and Emerging Tactics of 2024," Trustwave, 21 January 2025.
[^3]: Alamri, A.H., "Dragos Industrial Ransomware Analysis: Q3 2024," Dragos, 17 December 2024.
[^4]: Muncaster, P., "APT groups are increasingly deploying ransomware – and that’s bad news for everyone," WeLiveSecurity, 07 January 2025.
[^5]: Staff, "2024 Data Breach Investigations Report," Verizon, 2024.
[^6]: Kropac, J., "ESET Threat Report H2 2024," WeLiveSecurity, 16 December 2024.
[^7]: Tujague, J., & Bunce, D., "Crypted Hearts: Exposing the HeartCrypt Packer-as-a-Service Operation," Unit 42, 13 December 2024.
[^8]: Searchlight Cyber Analysts, "Three Notable Dark Web Law Enforcement Takedowns of 2024 So Far," Searchlight Cyber, 03 June 2024.
[^9]: Mcpherson, P., & Wilson, T., "Telegram app hosts ‘underground markets’ for Southeast Asian crime gangs, UN says," Reuters, 08 October 2024.
[^10]: Burgess, M., & Hay Newman, L., "Pig Butchering Scams Are Going High Tech," Wired, 12 October 2024.
[^11]: Lin, Z., & Cui, J., & Liao, X., & Wang, X., "Malla: Demystifying Real-world Large Language Model Integrated Malicious Services," arXiv, 19 August 2024.
[^12]: Staff, "Bulletproof Hosting: A Critical Cybercriminal Service," Intel471, 22 January 2024.
[^13]: Staff, "2024 Threat Landscape Statistics: Ransomware Activity, Vulnerability Exploits, and Attack Trends," Rapid7, 16 December 2024.
[^14]: Staff, "Ransomware in 2024: Latest Trends, Mounting Threats, and the Government Response," TRM Labs, 11 October 2024.
[^15]: Staff, "Cost of a Data Breach Report 2024," IBM, 30 July 2024.
[^16]: Staff, "Largest ever operation against botnets hits dropper malware ecosystem," Europol, 30 May 2024.
[^17]: Staff, "Law enforcement disrupt world’s biggest ransomware operation," Europol, 20 February 2024.
[^18]: Watson, M., "Ransomware report reveals evolving threat landscape in 2024," Security Brief, 18 December 2024.
[^19]: Walter, J., "CyberVolk | A Deep Dive into the Hacktivists, Tools and Ransomware Fueling Pro-Russian Cyber Attacks," Sentinel Labs, 25 November 2024.
[^20]: Johnson, A., & Thies, B., "Cybercrime News & Analysis to Close Out the Year," SpyCloud Labs, 03 December 2024.
[^21]: "LockBit power cut: four new arrests and financial sanctions against affiliates," Europol, 02 October 2024.
[^22]: Goodchild, J., "What Security Lessons Did We Learn in 2024?," DarkReading, 31 December 2024.
[^23]: Caveza, S., "Salt Typhoon: An Analysis of Vulnerabilities Exploited by this State-Sponsored Actor," Tenable, 23 January 2025.
[^24]: De Oliveira, A., "Ransomware: biggest groups responsible for attacks in 2024," Lumiun, 03 October 2024.
[^25]: Nadeau, J., "83 Percent of organizations reported insider attacks in 2024," SecurityIntelligence, 26 November 2024.
[^26]: Berg, J., & Donyina, F., "Cyber Threat Awareness Report: Emerging Threats from CyberVolk and Qilin Ransomware – October 04, 2024," CVP, 04 October 2024.
[^27]: Staff, "Understanding Ransomware Threat Actors: LockBit," CISA, 14 June 2023.
[^28]: Watt, C., "Threat Intelligence NoName057(16) Threat Actor Profile," Quorum Cyber, 18 April 2024.
[^29]: Nawrocki, M., & Conrad, C., & Arenberg, C., "NoName057(16) Campaign Analysis," NETSCOUT, 16 January 2024.
[^30]: "Pro-Russian Hacktivists Target Organizations in Taiwan With DDoS Attack Campaign," Radware, 13 September 2024.
[^31]: Mahendru, P. "The State of Ransomware in Financial Services 2024," Sophos News, 24 June 2024.
[^32]: Grieg, J., "US agencies confirm Beijing-linked telecom breach involving call records of politicians, wiretaps," The Record, 14 November 2024.
[^33]: Chang, L M., Chen, T., Barmejo, L. and Lee, T., "Game of Emperor: Unveiling Long Term Earth Estries Cyber Intrusions," Trend Micro, 25 November 2024.
[^34]: Staff, "PRC State-sponsored cyber activity: Actions for critical infrastructure leaders," Australian Signals Directorate, March 2024.
[^35]: [Placeholder for internal research reference on root causes].

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-31", "model": "gemini-3.5-flash-lite"} -->
