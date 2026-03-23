# Global Cyber Threat Intelligence (CTI)
## Annual Cyberthreat Trends Report - 2024

March 2025

## Table of Contents
- [Executive overview](#executive-overview)
- [Cross-industry threat vectors](#cross-industry-threat-vectors)
- [Cross-industry initial access techniques](#cross-industry-initial-access-techniques)
- [Threat vector highlights](#threat-vector-highlights)
- [Summary of data](#summary-of-data)
- [Threat actors](#threat-actors)

---

## Executive overview
High-level presentation of top threat actors, threat vectors, incidents, and overall assessment.

The following report highlights overarching cyber trends and emerging issues from January 1 to December 31, 2024.

| Feature | Most impactful threat actor | Most pervasive threat actor |
| :--- | :--- | :--- |
| **Name** | RansomHub | APT29 |
| **Category** | Cybercriminal | Nation state |
| **Motive** | Financial gain | Political gain |
| **Likelihood** | Very likely | Likely |
| **Impact** | Significant | Significant |

*RansomHub emerged in February and operates under a ransomware-as-a-service (RaaS) model. The RansomHub threat group's differentiator is its ability to seamlessly accommodate affiliates across varying skill and experience levels [1], [2].*

*APT29 (aka. Midnight Blizzard) is a suspected nation-state cyberespionage group targeting government-related organizations globally. In 2024, the group conducted a spearphishing campaign that targeted multiple sectors.[1]*

### Highlights
- Ransomware continued to be the top threat vector for the year. The RaaS model facilitates the easy creation of new groups. Affiliates are not tied to one group, making attack attribution more challenging than in previous years.
- Due to its effectiveness, social engineering continued to trend as an initial access technique for cybercriminals. The exploitation of human behavior and mistakes is again rising as technical protections are increasingly effective.
- In 2024, Deloitte CTI observed a shift from brute-force attacks to using deliberately stolen username and password combinations to authenticate on corporate virtual private networks (VPNs).
- Deloitte IR teams noted on multiple occasions that threat actors used subscription-based cloud services, shifting away from the traditionally known open-source tools that offer similar capabilities.
- Malware, particularly infostealers, remained a prominent threat as many families have developed new iterations. Despite law enforcement's takedown of Resine Stealer operations, large sample sets enable the malware to persist.

### Assessments
- Deloitte CTI assesses with high confidence that threat actors will continue to leverage third-party integrations between vendors and clients. Third-party compromises can spread rapidly and can affect multiple organizations with ease.
- Deloitte CTI assesses with moderate to high confidence that social engineering, with the aid of AI, will become a top threat vector in 2025 and beyond. Technical measures to detect AI-generated content and interactions are lagging, increasingly exposing end users to this threat.
- Deloitte CTI assesses with high confidence that nation-state groups will continue to pose significant challenges to global cybersecurity efforts.

---

## Cross-industry threat vectors
Throughout 2024, Deloitte CTI observed several overarching, cross-industry threat vectors not specific to a threat actor type.

### Ransomware
- **Impact**: Significant | **Likelihood**: Likely
- Ransomware continued to remain a formidable threat to organizations globally. RaaS models have continued to mature, enabling less experienced and technical actors to conduct crimes.[3]
- Emerging in February 2024, RansomHub has become the most active ransomware group in 2024, having claimed over 500 victims across various sectors.[1]
- The primary method behind ransomware breaches is leveraging VPNs for initial access, with vulnerability exploitation combined with credential-based attacks to bypass multi-factor authentication requirements.[3]
- Nation-state advanced persistent threats (APTs) have been increasingly deploying ransomware by collaborating with cybercriminal groups or developing their own strains.[4]

### Third-party compromise
- **Impact**: Moderate | **Likelihood**: Likely
- Third-party compromises increased in 2024, partly due to the use of zero-day exploits for ransomware and extortion attacks.[5]
- Third-party compromise attacks have the potential to be widespread. Data from these compromises can be leaked on dark web forums for sale.[1].

### Malware trends
- **Impact**: Significant | **Likelihood**: Likely
- In 2024, security researchers observed new iterations of previously known malware, while law enforcement disrupted some prevalent malware families. In October, a global operation led to the takedown of RedLine Stealer. Although activity levels have decreased due to the number of RedLine samples available, malware activity persists.[6]
- LummaStealer continued to make an impact and experienced high levels of growth during the year.[6]
- One notable development is a packer-as-a-service (PaaS) dubbed "HeartCrypt“ that threat actors used to protect malware by packing malicious code into legitimate binaries.[7]

### Underground trends
- **Impact**: Significant | **Likelihood**: Roughly even chance
- The cybercriminal underground continued its rapid transformation toward decentralized, specialized, and professionally-structured operations. Due to law enforcement pressure, popular marketplaces splintered, driving activity into closed forums and encrypted channels. [1],[8],[9]
- AI became a key enabler, powering deepfake campaigns, PaaS offerings, and automated translation to target victims worldwide. Ransomware syndicates refined multi-faceted extortion tactics, while thriving initial access brokers (IABs) fueled widespread data breaches and attacks. Meanwhile, criminals embraced privacy-centric payment methods, particularly stablecoins, to evade detection.[1],[10],[11]
- Despite several high-profile takedowns, the underground community demonstrated resilience through collaboration, bulletproof hosting, and corporate-like organizational structures.[1],[8],[9],[12]

---

## Cross-industry initial access techniques
Deloitte CTI observed that the most leveraged initial access techniques in 2024 were vulnerability exploitation, social engineering, a combination of VPN exploitation with stolen passwords, and phishing.

### Vulnerability exploitation
- **Impact**: Severe | **Likelihood**: Roughly even chance
- Throughout 2024, threat actors continued to exploit vulnerabilities, including zero-day vulnerabilities, to gain initial access to their victims' networks and environments.
- Large-scale ransomware groups are among the perpetrators, with Clop exploiting two zero-day vulnerabilities in December.[1]
- Notably, threat actors continued to exploit old vulnerabilities; some large-impact exploits in 2024 were over five years old. [13].

### Social engineering
- **Impact**: Severe | **Likelihood**: Roughly even chance
- In 2024, Deloitte IR teams noted a trend in threat actors combining vishing with BEC attacks in multiple independent investigations, predominantly targeting service providers across multiple industries.
- This method involves stealing user credentials by calling the service provider's customer support to initiate a password reset for one of their clients, using a pre-registered email domain impersonating the client. One IR case revealed that the squatted domain had only been registered three days before the call, indicating this was a targeted operation [1].

### Combination: VPN exploitation with stolen passwords
- **Impact**: Severe | **Likelihood**: Roughly even chance
- VPN exploitation remains a leading initial access vector. In 2024, Deloitte CTI observed a shift from brute-force attacks to using deliberately stolen username and password combinations to authenticate on the corporate VPN.
- Threat actors gain credentials from data breaches exposed on the dark web, IABs, or social engineering methods.
- Additionally, Deloitte IR teams noted threat actors’ expanding toolsets for transversing firewalls with cloud service providers as proxies. Deloitte IR teams noted on multiple occasions that threat actors used subscription-based cloud services, shifting away from the traditionally known open-source tools that offer similar capabilities.[1]

### Phishing
- **Impact**: Severe | **Likelihood**: Almost certain
- Working with the CTI team, Deloitte's Managed Extended Detection and Response (MXDR) team observed peak phishing detections in February and May 2024, followed by a decline in detections in the third quarter, then picking up again in the fourth quarter.
- The ability of large language models (LLMs) to generate phishing content presents a significant challenge to traditional threat detection. Threat actors can generate 1,000 phishing emails in under two hours for as little as US$6.00, with LLMs likely contributing to the overall 1,265 percent increase in phishing attacks in 2024 [1].
- AI has enabled threat actors to craft highly personalized and timely phishing campaigns, enhancing their relevance and persuasiveness to their intended targets.[1]

---

## Threat vector highlights
![Chart showing number of attacks ransomware actors claimed responsibility for during 2023 and 2024]

### Ransomware trends
- Deloitte CTI observed a 17 percent increase in ransomware attack claims in 2024, peaking in the fourth quarter with 57 percent more claims compared to the fourth quarter of 2023.[1]
- RansomHub, which security researchers first observed in February 2024, was the most active ransomware in 2024.
- The average cost of a ransomware data breach reached US$4.91 million.[15]

### RaaS highlight
- Before 2024, the dominant groups were LockBit and ALPHV. However, the February 2024 "Operation Cronos" disrupted LockBit, and ALPHV conducted an exit scam.[17]
- Many smaller and more agile ransomware groups have since emerged to capitalize on the void.
- Other notable RaaS operations that emerged in 2024 include El Dorado/BlackLock, Lynx, Fog, and APT73/BASHE.[2]
- Many politically-motivated threat groups have been utilizing RaaS in their operations, such as CyberVolk.[19]

### Underground trends
- Multinational task forces targeted well-established dark web marketplaces such as Nemesis Marketplace and BreachForums.
- Despite these efforts, cybercriminal networks show resilience by migrating to invite-only forums and encrypted channels.

---

## Summary of data
![Chart of cyber events observed by threat actor type]
![Chart of cyber events observed targeting specific industries]
![Chart of cyber events observed by type]

---

## Threat actors
### Nation-state linked
- **Motivation**: Political, espionage, and financial
- **Top Actors**: APT29, Salt Typhoon, and Volt Typhoon

### Cybercriminals
- **Motivation**: Financial
- **Top Actors**: Clop, LockBit, and RansomHub

### Hacktivists
- **Motivation**: Political
- **Top Actors**: CyberVolk and NoName057(16)

### Insider threats
- **Motivation**: Financial, revenge, fear
- **Likelihood**: Malicious (Roughly even chance), Unintentional (Likely)

![Heatmap of trending and emerging threat actors in 2024]

---

### Footnotes and References
[^1]: Deloitte internal sources.
[^2]: Melnyk, S., "The New Face of Ransomware: Key Players and Emerging Tactics of 2024," Trustwave, 21 January 2025.
[^3]: Alamri, A.H., "Dragos Industrial Ransomware Analysis: Q3 2024," Dragos, 17 December 2024.
[^4]: Muncaster, P., "APT groups are increasingly deploying ransomware," WeLiveSecurity, 07 January 2025.
[^5]: Staff, "2024 Data Breach Investigations Report," Verizon, 2024.
[^6]: Kropac, J., "ESET Threat Report H2 2024," WeLiveSecurity, 16 December 2024.
[^7]: Tujague, J., & Bunce, D., "Crypted Hearts: Exposing the HeartCrypt Packer-as-a-Service Operation," Unit 42, 13 December 2024.
[^8]: Searchlight Cyber Analysts, "Three Notable Dark Web Law Enforcement Takedowns of 2024 So Far," Searchlight Cyber, 03 June 2024.
[^9]: Mcpherson, P., & Wilson, T., "Telegram app hosts ‘underground markets’ for Southeast Asian crime gangs, UN says," Reuters, 08 October 2024.
[^10]: Burgess, M., & Hay Newman, L., "Pig Butchering Scams Are Going High Tech," Wired, 12 October 2024.
[^11]: Lin, Z., & Cui, J., & Liao, X., & Wang, X., "Malla: Demystifying Real-world Large Language Model Integrated Malicious Services," arXiv, 19 August 2024.
[^12]: Staff, "Bulletproof Hosting: A Critical Cybercriminal Service," Intel471, 22 January 2024.
[^13]: Staff, "2024 Threat Landscape Statistics," Rapid7, 16 December 2024.
[^14]: Staff, "Ransomware in 2024," TRM Labs, 11 October 2024.
[^15]: Staff, "Cost of a Data Breach Report 2024," IBM, 30 July 2024.
[^16]: Staff, "Largest ever operation against botnets," Europol, 30 May 2024.
[^17]: Staff, "Law enforcement disrupt world’s biggest ransomware operation," Europol, 20 February 2024.
[^18]: Watson, M., "Ransomware report reveals evolving threat landscape in 2024," Security Brief, 18 December 2024.
[^19]: Walter, J., "CyberVolk," Sentinel Labs, 25 November 2024.
[^20]: Johnson, A., & Thies, B., "Cybercrime News & Analysis," SpyCloud Labs, 03 December 2024.
[^21]: "LockBit power cut," Europol, 02 October 2024.
[^22]: Goodchild, J., "What Security Lessons Did We Learn in 2024?," DarkReading, 31 December 2024.
[^23]: Caveza, S., "Salt Typhoon," Tenable, 23 January 2025.
[^24]: De Oliveira, A., "Ransomware: biggest groups responsible for attacks in 2024," Lumiun, 03 October 2024.
[^25]: Nadeau, J., "83 Percent of organizations reported insider attacks in 2024," SecurityIntelligence, 26 November 2024.
[^26]: Berg, J., & Donyina, F., "Cyber Threat Awareness Report," CVP, 04 October 2024.
[^27]: Staff, "Understanding Ransomware Threat Actors: LockBit," CISA, 14 June 2023.
[^28]: Watt, C., "Threat Intelligence NoName057(16) Threat Actor Profile," Quorum Cyber, 18 April 2024.
[^29]: Nawrocki, M., & Conrad, C., & Arenberg, C., "NoName057(16) Campaign Analysis," NETSCOUT, 16 January 2024.
[^30]: "Pro-Russian Hacktivists Target Organizations in Taiwan With DDoS Attack Campaign," Radware, 13 September 2024.
[^31]: Mahendru, P. "The State of Ransomware in Financial Services 2024," Sophos News, 24 June 2024.
[^32]: Grieg, J., "US agencies confirm Beijing-linked telecom breach," The Record, 14 November 2024.
[^33]: Chang, L M., Chen, T., Barmejo, L. and Lee, T., "Game of Emperor," Trend Micro, 25 November 2024.
[^34]: Staff, "PRC State-sponsored cyber activity," Australian Signals Directorate, March 2024.
[^35]: Deloitte internal data.