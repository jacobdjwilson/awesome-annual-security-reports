# Financial-Sector-Threat-Landscape 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [1 Introduction](#1-introduction)
  - [1.1 Objectives](#11-objectives)
- [2 Background](#2-background)
  - [2.1 Miseducation Regarding Threats](#21-miseducation-regarding-threats)
  - [2.2 Historical Ransomware Vulnerabilities](#22-historical-ransomware-vulnerabilities)
    - [2.2.1 Introduction](#221-introduction)
    - [2.2.2 Vulnerability Pattern Analysis](#222-vulnerability-pattern-analysis)
    - [2.2.3 Gap Analysis and Future Impact](#223-gap-analysis-and-future-impact)
    - [2.2.4 Security-Posture Improvements from 2018 to Present](#224-security-posture-improvements-from-2018-to-present)
    - [2.2.5 Future Impact Analysis](#225-future-impact-analysis)
  - [2.3 Ransomware Losses for the Financial Services Industry](#23-ransomware-losses-for-the-financial-services-industry)
    - [2.3.1 Case Study 1 - LockBit 3.0’s Targeted Attack on a Brazilian Bank](#231-case-study-1---lockbit-30s-targeted-attack-on-a-brazilian-bank)
    - [2.3.2 Case Study 2 - Play Ransomware’s Attack on a Chilean Financial Firm](#232-case-study-2---play-ransomwares-attack-on-a-chilean-financial-firm)
  - [2.4 Ransomware Response Capabilities](#24-ransomware-response-capabilities)
    - [2.4.1 Regional Response Infrastructure Assessment](#241-regional-response-infrastructure-assessment)
    - [2.4.2 Technical Response Capabilities and Resource Constraints](#242-technical-response-capabilities-and-resource-constraints)
    - [2.4.3 Cross-Border Response Coordination](#243-cross-border-response-coordination)
    - [2.4.4 Information-Sharing Mechanisms and Their Impact on Financial Sector Vulnerability](#244-information-sharing-mechanisms-and-their-impact-on-financial-sector-vulnerability)
    - [2.4.5 Variation in Public–Private Coordination Frameworks](#245-variation-in-public-private-coordination-frameworks)

---

**Organization**: Digiamericas  
**Report Title**: Financial-Sector-Threat-Landscape  
**Year**: 2025

**CC BY-NC-SA**: This license allows re-users to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator. If you remix, adapt, or build upon the material, you must license the modified material under identical terms. The contents expressed in this document are presented exclusively for informational purposes and do not represent the official opinion or position of the Center for Cybersecurity Policy and Law, or any of its members. For more information, please contact admin@digiamericas.org

## Executive Summary
Latin America is among the least prepared regions for cyber attacks, according to the UN Cybersecurity Index.[^1] This vulnerability stems from underinvestment in cybersecurity, the scarcity of skilled professionals, and weak regulatory frameworks.[^2] While a digital revolution arose in sectors like fintech and e-commerce after the COVID-19 pandemic, these advancements were not matched by adequate security measures. As the founder of the Latin American Cybersecurity Research Network, Louise Marie Hurel, notes, “Latin America’s entrepreneurial and innovative spirit does not come with a concern for security”.[^3]

The growing threat is exemplified by high-profile incidents, such as the ransomware attack on Costa Rica’s Finance Ministry and Brazil’s court system, underscoring the need to address the proliferating threat. Moreover, only 7 of the 32 countries in the region have plans to protect their critical infrastructure, and just 20 have operational Computer Security Incident Response Teams (CSIRTs). As the global cyber-threat landscape matures, with a 34.5% rise in data breaches and an 84% increase in ransomware attacks in 2023, Latin America’s cybersecurity challenges are increasingly urgent.[^4]

The LATAM Threat Landscape research from Duke University, utilizing data from Recorded Future’s Intelligence Graph, discusses the three principal threat-actor groups that are targeting the Latin American financial sector and the suggested controls that can be implemented to avert cyber attacks and mitigate their impact. The extensive data analysis ultimately identified five aggressive threat actors: CL0P, LockBit, Mispadu, Horabot, and Mispadu.

Cyber breaches have become increasingly common in Latin American financial institutions, with distinct cybersecurity challenges. Data from 2023 reveals that Latin American countries experience the highest rate of ransomware attacks on organizations, with 79% of incidents involving ransomware, compared to the global average of 53%.[^5] This report explores the approaches and motivations of key threat actors—CL0P, Mispadu, Horabot, Blind Eagle, and LockBit—and the finding that these threat actors utilized similar TTPs.

![Figure 1: Financial Sector Cyber Incidents and Losses]

The Latin America region presents vulnerabilities within financial institutions that are unique within the global landscape and require careful consideration. Primary target countries for threat-actor groups include Brazil, Mexico, Argentina, Colombia, and Peru. These countries accounted for 50% of the victim countries that attackers targeted in 2023, with 12% of the total cyber attacks in the world occurring in Latin America.[^6]

![Figure 2: Distribution of Successful Attacks in Latin America]

In 2023, LATAM faced 1,498 ransomware attacks and 6,048 phishing attacks by 33 distinct groups (SOCRader, 2024, pp. 4–5).[^7] Insufficient investment in cybersecurity, volatile economies, and a highly unregulated environment are believed to have magnified institutional risks.

![Figure 3: Distribution of Dark Web Threats by Primary Target Country]

The data gathered to create this report offers a broad understanding of the evolving threat landscape while considering the limitations of open-source intelligence, such as labor-intensive processes, limited effectiveness, and the potential to overlook smaller threats when prioritizing higher-profile threat actors.[^8] This report provides vital observations to improve recommendations on cybersecurity defenses that can create a more resilient Latin American financial ecosystem.

The LATAM financial services sector should consider the use of a cybersecurity defense strategy that is threat-actor informed to mitigate impacts from cyber attacks. Organizations from the financial services industry that use an informed strategy can prepare themselves for common tactics, techniques, and procedures (TTPs) used by threat actors. By reviewing and incorporating the mapped TTPs that these threat-actor groups use, cyber defenders can more effectively implement cybersecurity controls.

## 1 Introduction
In recent years, the financial sector in Latin America has undergone a rapid digital transformation, fueled by the expansion of fintech services, increased internet penetration, and a growing demand for digital banking. However, this technological progress has outpaced the development of robust cybersecurity practices, leaving financial institutions increasingly vulnerable to sophisticated cyber threats. As cybercrime becomes more organized and opportunistic, the financial sector, which is already a high-value target, faces heightened risks that threaten economic stability, consumer trust, and national security.

This paper investigates the cybersecurity landscape of the Latin American financial market, with a particular focus on the actors, methods, and systemic vulnerabilities that define the region’s current risk posture. Drawing on threat intelligence data, regional case studies, and insights from security researchers, this study seeks to analyze the motivations and tactics of prominent threat actors targeting Latin American financial systems. It also explores the structural challenges such as regulatory gaps, talent shortages, and underinvestment that hinder effective cybersecurity defense.

The objective of this research is twofold: first, to provide a comprehensive overview of the evolving threat environment facing financial institutions in Latin America, and second, to recommend practical, threat-informed strategies for improving cyber resilience in the region. Particular emphasis is placed on the activities of five major threat actor groups—CL0P, LockBit, Mispadu, Blind Eagle, and Horabot—whose operations exemplify broader trends in cybercrime targeting the financial sector.

The following sections of this paper are organized as follows: Section 2 outlines the threat landscape and introduces the key cybercriminal groups active in the region, as well. Section 3 evaluates the region’s cybersecurity readiness, institutional vulnerabilities, and national response strategies. Section 4 highlights the regulatory gaps that currently exist in Latin America. Section 5 dives into 5 different APTs, their activity in the region, their TTPs, and recommendations to organizations on how to deal with these threats. Finally, Section 6 provides a series of strategic recommendations for cybersecurity in Latin America’s financial sector.

### 1.1 Objectives
The research team evaluated open-source data from the Recorded Future platform to form an assessment of how different threat-actor groups might use similar TTPs when attacking financial services firms in LATAM. This report offers analysis with four primary objectives:

1. Identifying major threat-actor groups targeting Latin American financial institutions and their operational bases.
2. Analyzing the TTPs employed by these threat actors.
3. Assessing the impact of their targeting strategies on financial institutions in the region.
4. Formulating actionable recommendations for mitigating the identified TTPs, leveraging the MITRE ATT&CK framework and insights for cybersecurity professionals.

## 2 Background
Cyber attacks on financial institutions in Latin America have significantly increased over the past five years, reflecting the global trend of rising cyber threats, which have grown at an annual rate of 25% over the past decade, as of 2024.[^9] According to the 2024 Global Financial Stability Report,[^10] the risk of extreme cyber-related losses has more than quadrupled since 2017, reaching $2.5 billion. Furthermore, the 2024 LATAM CISO Report highlights that countries such as Costa Rica, Mexico, Brazil, and Argentina attribute the frequency and success of these attacks to gaps in response preparedness. These gaps ranged from deficiencies in technical capabilities to communication breakdowns between public- and private-sector entities between 2020 and 2025. Only about half of the countries surveyed had a national cybersecurity strategy specifically focused on the financial sector or had implemented dedicated cybersecurity regulations.

Consequently, Latin America alone accounted for 12% of the total cyber attacks worldwide in 2022, surpassing the Middle East and Africa, which comprised 7%, despite being comparably under-resourced.[^11] Attackers primarily targeted organizations and individuals in Brazil, Mexico, and Argentina, which together accounted for 44% of all attacks. These countries have the largest economies and financial institutions in Latin America, making them attractive targets for cybercriminals.[^12] As cyber incidents continue to rise, the region's financial stability is increasingly at risk given that financial institutions are among the key targets for cyber-threat actors and constitute a significant portion of the target sectors. The financial and insurance sector alone accounts for 39.47% of disclosed cyber incidents in Latin America.[^13] If left unaddressed, these threats could lead to severe economic repercussions, highlighting the need for robust cybersecurity measures.

### 2.1 Miseducation Regarding Threats
Latin American financial institutions face heightened susceptibility to cyber attacks due to a combination of factors, which include the following:

1. **A lack of cybersecurity awareness and training within financial institutions**: The primary challenge is not only a general lack of cybersecurity awareness but a training and learning gap within financial institutions. Employees need comprehensive cybersecurity training, while consumers require awareness campaigns against potential cyber threats.
2. **The absence of cybersecurity standards and regulations, which leaves many financial institutions vulnerable to cyber threats**: Organizations choose not to implement the Cybersecurity Framework (NIST CSF) or ISO 27001 frameworks voluntarily, leaving themselves exposed to cyber attacks from threat-actor groups that must find only one vulnerability to compromise a victim company.
3. **Insufficient investment in technology at hardware and software levels**: The use of outdated software creates security gaps in critical infrastructure and weakens the region's defenses against cyber attacks. The technological disparity between Latin American countries and their more developed counterparts in North America and Europe exacerbates these vulnerabilities, making it more difficult for the region to effectively counter sophisticated cyber threats.[^14]

The financial impact of cybersecurity breaches has been staggering worldwide. According to IBM Security, “the average data breach cost in 2020 was estimated at $3.86 million" including the cost of legal fees, compliance fines, reputational damage, and loss of customer trust.[^15] In May 2021, the Colonial Pipeline ransomware attack crippled fuel distribution across the United States, disrupting critical infrastructure and causing widespread shortages. The attack, attributed to the DarkSide ransomware group, forced the company to halt operations, leading to panic-buying and fuel-price surges. In response, Colonial Pipeline paid a $4.4 million ransom to regain access to its systems, but the economic repercussions persisted long after, such as supply-chain disruptions and heightened regulatory scrutiny.[^16] This incident exposed critical cybersecurity vulnerabilities in industrial control systems, highlighting the urgent need for stronger cybersecurity frameworks and proactive risk-mitigation strategies to prevent similar large-scale attacks.

The vulnerabilities exploited in the Colonial Pipeline attack, and the resulting harm, highlight Latin America's susceptibility to cyber threats due to insufficient regulatory frameworks, weaker cybersecurity infrastructure, and lower business and consumer awareness, which cybercriminals manipulate for financial gain. Latin America has the highest percentage of ransomware attacks at 79% compared to the global average of 53%, with 94% of attacks attributed to system intrusion, social engineering, and basic web-application attacks.[^17] The average cost of a data breach has risen to USD 4.45,[^18] and to the highest since 2020 at USD 2.46M in Latin America.[^19] Latin America has the lowest levels of cybersecurity preparedness, making it the most susceptible to attacks according to the 2020 Global Cybersecurity Index.[^20] This will continue to impact the region’s economy.

### 2.2 Historical Ransomware Vulnerabilities

#### 2.2.1 Introduction
The Latin American financial sector experienced a significant surge in sophisticated cyber attacks between 2018 and 2024, highlighting critical vulnerabilities in the region's digital infrastructure. This analysis examines 12 major incidents that targeted banks, financial institutions, and government systems across Chile, Brazil, Mexico, Argentina, and other Latin American countries. The attacks, ranging from the $10 million Banco de Chile heist in 2018 [^21] [^22] to the 2024 Bankingly data leak affecting 135,000 clients,[^23] demonstrate an evolving threat landscape dominated by ransomware and advanced persistent threat (APT) groups.

The investigation reveals a concerning pattern: attackers increasingly target third-party service providers and financial-technology platforms to breach multiple institutions simultaneously. Organizations increasingly rely on various third-party providers, exposing them to distinct cyber risks. Software and SaaS (Software as a Service) providers face vulnerabilities and supply-chain attacks, where flaws in widely used applications, such as Progress Software’s Managed File Transfer solution, can lead to mass data exfiltration.[^24] Likewise, Infrastructure as a Service environments can present risks due to misconfigurations, access-control weaknesses, and service outages, potentially disrupting business operations. The Bankingly breach, involving a SaaS-based digital fintech platform, compromised seven Latin American banks due to misconfigured storage buckets lacking proper authentication, exposing sensitive customer data.[^25] These incidents highlight the need for stronger third-party risk management, continuous monitoring, and zero-trust security models to mitigate cascading threats.

Most attacks followed a similar pattern: initial compromise through phishing or vulnerable systems, lateral movement through networks, data exfiltration, and often deployment of ransomware. The financial impact of these incidents is substantial, with losses exceeding 1% of some countries' GDP and potentially rising to 6% if critical infrastructures are targeted.[^26] A 1% GDP loss from cybercrime equates to USD 25 billion for Brazil, USD 15 billion for Mexico, and USD 6.1 billion for Argentina, while a 6% loss could reach USD 150 billion, USD 90 billion, and USD 36.6 billion, respectively. Smaller economies such as Chile ($3.9B–$23.5B) and Colombia ($3.2B–$19.3B) also face major risks.[^27] With Brazil, Mexico, and Argentina among the hardest hit, cyber attacks threaten business continuity, investor confidence, and long-term economic stability across the region. The scale of potential economic damage underscores the urgent need for strengthened cybersecurity measures, particularly in third-party risk management and critical-infrastructure protection within Latin America's financial sector.

#### 2.2.2 Vulnerability Pattern Analysis
This section analyzes prevalent technical vulnerabilities, industry-specific weaknesses in the financial sector, and regional security challenges, providing organizations with insights into common risk patterns. By understanding these vulnerabilities, businesses can identify gaps in their security posture and implement proactive defenses. The findings in this section aim to help organizations recognize recurring vulnerability patterns, understand their potential business impact, and take preemptive actions to mitigate risks before they escalate into security incidents. Section 6: Strategic Recommendations, at the end of this paper, provides actionable remediations to address these vulnerabilities effectively.

**Commonly Observed Technical Vulnerabilities:**
- Weak network segmentation
- Insufficient internal-access controls
- Inadequate incident-response protocols
- Employee susceptibility to social engineering
- Over-reliance on legacy systems
- Weak third-party security
- Limited monitoring of internal transactions

**Industry-Specific Patterns and Vulnerabilities (Finance):**
- Inadequate network segmentation between critical systems
- Weak access controls on internal networks
- Insufficient authentication on the systems of third-party service providers
- Vulnerable public-facing infrastructure
- Sophisticated banking trojans using legitimate authorities to deceive users

**Region-Specific Patterns and Vulnerabilities:**
- Heavy reliance on social engineering targeting regional trust in financial authorities
- Sophisticated phishing campaigns exploiting tax-related concerns
- Cross-border nature of banking operations creating security inconsistencies
- Widespread adoption of digital banking in rural areas through potentially vulnerable channels
- Centralized payment-processing systems (like Brazil's SPEI) becoming high-value targets[^28]

#### 2.2.3 Gap Analysis and Future Impact
This section examines key cybersecurity gaps in Latin America, focusing on their root causes, recent improvements, and anticipated future risks. The analysis highlights systemic issues, such as underinvestment, outdated infrastructure, and insufficient collaboration, all of which contribute to persistent security challenges. By reviewing past incidents and their impact on financial institutions, organizations can better understand evolving threats. Additionally, this section explores emerging risks from AI-driven cyberattacks, supply-chain vulnerabilities, and geopolitical risks. Section 6: Strategic Recommendations, at the end of this paper provides concrete solutions to address these vulnerabilities and strengthen regional cybersecurity resilience.

**Root-Cause Analysis:**
1. **Chronic underinvestment in cybersecurity**: Latin America faces significant cybersecurity vulnerabilities due to underinvestment.[^29] According to the Organization of American States (OAS), Latin American countries allocate <1% of GDP to cybersecurity infrastructure,[^30] leaving financial systems vulnerable to advanced attacks. The region has the lowest average cybersecurity score globally, at 10.2 out of 20.[^31]
2. **Insufficient cross-border collaboration**: There is a lack of harmonization between national laws, creating challenges for multinational companies.[^32] However, recent efforts, such as the EU-LAC Digital Alliance, aim to strengthen bi-regional partnerships.[^33]
3. **Outdated infrastructure and software**: Many companies still operate with outdated systems or use pirated software, leaving gaps that attackers can easily exploit.[^34]
4. **Cybersecurity skills gap**: There is an urgent need for upskilling current teams and fostering the next generation of cybersecurity professionals.[^35]
5. **Inadequate legislation and enforcement**: Cybersecurity laws in some countries are either outdated or poorly enforced. Only three out of 21 countries in Latin America have a defined national digital-security strategy.[^36]
6. **Lack of public awareness**: Many Latin American countries have not yet widely publicized the dangers of the internet. There is a lack of preventative programs despite some countries adopting national cyber strategies.[^37]

#### 2.2.4 Security-Posture Improvements from 2018 to Present
The security posture of Latin American financial institutions has significantly transformed between 2018 and 2024. In 2018, as evidenced by the Banco de Chile attack, financial institutions primarily relied on reactive security measures, such as system disconnection, forensic investigation after the breach, and restoration from backups. The bank was unaware of the malware in its systems until it was faced with the KillMBR alert, which caused a widespread system shutdown. Compared to best practices, such as proactive threat detection, network segmentation, and real-time monitoring, the bank’s incident response lacked early threat identification, precise containment, and security controls to prevent financial loss.[^38]

The case of Mexico's SPEI system in 2018 further highlighted the prevalent weak network segmentation and limited monitoring capabilities of the era.[^39] The heist exposed severe vulnerabilities in the Sistema de Pagos Electrónicos Interbancarios (SPEI) system, with hackers identified as part of the APT38 group, a financially motivated threat-actor group believed to be backed by North Korea.[^40] APT38 infiltrated the banking networks, compromised endpoints handling SPEI transactions, and injected fraudulent payment requests. Exploiting weak network security, including poor network segmentation and access controls, they were able to alter transfer instructions without triggering immediate alarms, ultimately stealing USD 15–20 million and moving the funds to mule accounts before laundering them internationally.[^41]

As of 2024, the security landscape of Latin American financial institutions has advanced significantly, with organizations adopting more structured incident-response protocols and improving coordination through national CERT teams. A notable example is the Chilean Customs’ swift containment of the Black Basta ransomware attack, demonstrating enhanced response capabilities and collaboration.[^42] However, despite these advancements, financial institutions continue to grapple with an evolving threat landscape driven by rapid digitalization, increased interconnectivity, and emerging vulnerabilities in third-party SaaS and software integrations.

A prime example is the 2024 Bankingly breach, which affected 135,000 clients across multiple LATAM countries, exposing critical data due to misconfigurations in Azure Blob Storage.[^43] The breach was traced back to misconfigured Azure Blob Storage buckets used by Bankingly to store customer data. These misconfigurations left the data exposed to unauthorized access, highlighting significant vulnerabilities in third-party integrations and cloud-service configurations.[^44]

Similarly, the Banco Português de Gestão data leak, caused by a misconfiguration in Nearsoft’s systems, exposed highly sensitive client financial data due to missing authentication controls. Alarmingly, Nearsoft failed to comply with critical security standards like ISO 27001 and PCI DSS, leaving data unencrypted and vulnerable to unauthorized access.[^45] These incidents highlight persistent security gaps stemming from poor risk management, cloud misconfigurations, and inadequate vendor oversight. As such, they underscore the risks associated with modern digital infrastructure. While financial institutions have strengthened defenses, such incidents reveal that security misconfigurations and insufficient oversight remain key weaknesses. Addressing these gaps will be essential to mitigating future risks and maintaining a strong security posture in an increasingly digital financial ecosystem.

#### 2.2.5 Future Impact Analysis
1. **AI-driven Cyber Attacks**: Threat actors are increasingly leveraging AI to create destructive malware, sophisticated phishing campaigns, convincing deep fakes, and advanced cyberespionage operations that exploit infrastructure vulnerabilities.[^46] The primary challenge when tackling these sophisticated attacks is the critical shortage of professionals with specialized expertise to understand and design appropriate risk-management frameworks. Success depends on building technical competency to effectively assess and mitigate these sophisticated, emerging threats through proper governance and controls.
2. **Exploitation of Digital-Transformation Vulnerabilities**: As Latin American countries promote further digitization to foster socioeconomic growth, they become more vulnerable to cyber criminals. The increased use of technology also escalates the potential for attacks.[^47]
3. **Supply-Chain Vulnerabilities**: Notably, 54% of large organizations identified supply-chain challenges as the biggest barrier to achieving cyber resilience. The increasing complexity of supply chains, coupled with a lack of visibility into the security levels of suppliers, has emerged as a leading cybersecurity risk.[^48]
4. **Geopolitical Influences**: Geopolitical tensions are contributing to a more uncertain cybersecurity environment. For example, 97% of organizations saw an increase in cyber threats since the start of the Russia–Ukraine war in 2022, demonstrating the profound effect of geopolitical tensions on cybersecurity.[^49]
5. **Regional Disparities**: Latin America is projected to experience a greater increase in cyberattacks than other regions. In Q2 2024, cyber attacks increased by 53% year-over-year in Latin America, and this trend is likely to continue.[^50]

## 2.3 Ransomware Losses for the Financial Services Industry
As of 2024, the financial services industry in LATAM has become a primary target for ransomware attacks, reflecting a broader trend of escalating cyber threats in the region. Brazil, Mexico, and Chile have been the hardest-hit countries, with ransomware groups such as LockBit 3.0, Akira, and Play being identified as the actors behind the attacks. These groups leverage sophisticated methods, including exploiting vulnerabilities in software and deploying ransomware-as-a-service (RaaS) models. The financial losses attributed to ransomware incidents in the LATAM financial sector are estimated to exceed hundreds of millions of dollars in 2024 as organizations face costs related to ransom payments, data recovery, operational downtime, and reputational damage. This surge in attacks underscores the critical need for robust cybersecurity measures within the region’s financial institutions.

### 2.3.1 Case Study 1 - LockBit 3.0’s Targeted Attack on a Brazilian Bank
In July 2024, the LockBit 3.0 ransomware group conducted a highly targeted attack against a major Brazilian financial institution. The attackers exploited a vulnerability in the bank's virtual-desktop infrastructure to gain unauthorized access and encrypt critical operational files. To further pressure the victim, LockBit 3.0 threatened to publish sensitive stolen data on dark-web forums unless the institution complied with their ransom demand of $2.5 million in Bitcoin.

The attack resulted in significant operational and financial damage. The bank experienced a prolonged downtime of online banking services, disrupting customer transactions and access to accounts. This not only eroded customer trust but also subjected the institution to regulatory scrutiny. Additionally, the financial costs extended beyond the ransom demand to include expenses for system recovery, forensic investigations, and public-relations efforts to restore its reputation.

### 2.3.2 Case Study 2 - Play Ransomware’s Attack on a Chilean Financial Firm
Also in July 2024, the Play ransomware group targeted a Chilean financial firm by deploying a Linux variant specifically engineered to exploit VMware ESXi environments. The attackers infiltrated the firm's virtualized infrastructure, encrypted critical server data, and left a ransom note demanding $1.8 million in cryptocurrency.

The attack caused extensive financial and operational repercussions for the firm. In addition to the ransom demand, the organization incurred costs related to restoring its IT systems and reinforcing its cybersecurity defenses. The incident also resulted in reputational harm, as clients and partners expressed concerns over the firm's ability to protect sensitive data. These cumulative losses further underscored the growing threat of ransomware to the LATAM financial services sector.

In conclusion, ransomware remains a pressing and escalating threat to the financial services industry in LATAM, with countries such as Brazil, Chile, and Mexico emerging as primary targets in 2024. Ransomware groups such as LockBit 3.0 and Play have demonstrated increasing sophistication by exploiting vulnerabilities in virtualized infrastructures and leveraging RaaS models to scale their operations. The financial losses incurred far surpass ransom payments, encompassing system restoration, downtime, and reputational damage, collectively amounting to hundreds of millions of dollars across the region. As the financial sector in LATAM continues to digitalize, organizations must prioritize comprehensive cybersecurity strategies, including vulnerability management, employee training, and advanced threat-detection systems, to mitigate the impact of these pervasive attacks. The resilience of the financial services sector hinges on proactive measures to counteract the evolving tactics of ransomware operators.

## 2.4 Ransomware Response Capabilities
The growing trend of ransomware attacks across LATAM has exposed critical gaps in regional response capabilities that create immediate vulnerabilities for the financial services sector. This section examines how institutional frameworks, technical capabilities, and coordination mechanisms in LATAM contribute to elevated ransomware risk exposure for financial institutions.

### 2.4.1 Regional Response Infrastructure Assessment
Recent comparative data, including Fortinet’s Global Ransomware Report, reveals important nuances in LATAM’s response capabilities relative to other regions.[^51] [^52] [^53] While Latin American organizations demonstrate stronger capabilities in rapid attack detection and social-engineering resistance,[^54] this relative strength in detection capabilities should be contextualized within the broader regional infrastructure limitations. Namely, the data suggests that while individual enterprise capabilities may be developing, systemic response infrastructure gaps persist. The uneven disclosure landscape and limited number of LATAM countries with established plans for critical-infrastructure protection (let alone in the financial services sector) is evidence of this gap.

One 2022 study introduces a comprehensive cybersecurity disclosure index examining practices across major LATAM markets between 2016 and 2020 on a 0–1 scale. The research developed a 27-element framework across four dimensions: governance (5 elements), strategy (6 elements), risk management (13 elements), and financial implications (3 elements). These dimensions were based on international standards, including ISO 27000; SEC guidelines; GDPR; and frameworks from OECD, IDB, OAS, and GRI.[^55]

The research reveals a complex landscape of cybersecurity disclosure in LATAM's financial sector, with financial institutions maintaining the highest disclosure levels across sectors, increasing from 0.28 in 2016 to 0.52 in 2020.[^56] This leadership position is particularly evident in Argentina, where financial institutions comprise 57% of sampled companies, with 86% filing SEC Form 20-F reports.[^57] However, despite this relative maturity, significant governance disclosure gaps persist. While board involvement in cybersecurity supervision improved from 0.18 in 2016 to 0.53 in 2020, specialized committee disclosure remained weak at 0.24 in 2020, and the oversight disclosure of audit committees scored only 0.20.[^58]

The governance gap is particularly concerning given the evolution of financial malware exploiting regional institutional contexts, such as specific banking implementations. By conducting a longitudinal study of Brazilian financial malware between 2012 and 2020, researchers revealed how malicious tactics rapidly evolve based on new attack opportunities. For example, threat actors are curating social engineering and malware scripts to local banking contexts that diverge from global or historical trends (e.g., malware targeting PIN-based credit cards, Brazilian Portuguese VBE code).[^59] Ransomware is no exception to these evolving tactics. Therefore, setting risk tolerance at the highest level through board-level cybersecurity governance is necessary to ensure local countermeasures are context-aware (i.e., attentive to geographic and enterprise characteristics).

Other concerns include findings regarding risk-management disclosure (0.40 in 2020); alignment with international security standards (0.39 in 2020); and ongoing cybersecurity-investment disclosure, improving only from 0.02 in 2016 to 0.21 in 2020.[^60] These scores suggest that, while financial institutions may have security frameworks in place, they struggle to effectively communicate their security investments and alignment with international standards. The research identifies clear correlations between regulatory frameworks and disclosure quality, with early adopters of data-protection laws and national cybersecurity strategies, such as Argentina (2016) and Brazil (2018), showing stronger financial sector disclosures than countries like Peru, where lower disclosure scores (0.25 in 2020) correlate with the absence of a national strategy.[^61]

The trends suggest a broader pattern: while LATAM financial institutions lead in cybersecurity disclosure compared to other sectors, their performance varies significantly based on regulatory maturity and national cybersecurity frameworks. The sector's critical role in national infrastructure and international financial networks makes these gaps particularly concerning, suggesting a need for more standardized disclosure practices and improved alignment with international standards across the region.

The comprehensive nature of the research findings indicates significant implications for ransomware incident-response capabilities across LATAM financial institutions. The disparity between strategic disclosure scores (0.53) and operational risk-management scores (0.40) suggests potential vulnerabilities in actual incident-response execution.[^62] Of particular concern are the low scores for the disclosure of incident-response procedures (0.36) and monitoring effectiveness (0.47). These scores indicate potential gaps in operational response capabilities that could directly impact an institution's ability to detect, contain, and recover from ransomware attacks.[^63] When combined with the previously discussed findings about disclosure practices and regulatory frameworks, these gaps suggest that, while LATAM financial institutions may have basic ransomware response plans in place, their actual operational readiness for complex attacks may be insufficient.

This supposition is well-founded. The Inter-American Development Bank reports that only seven of the 32 Latin American countries have established plans for critical-infrastructure protection, while just 20 have operational CSIRTs.[^64] This fragmented response landscape has created specific challenges for financial institutions operating across borders. For example, this rift was particularly acute during Colombia's September 2023 ransomware incident, where the blast radius spread to financial entities in Argentina, Panama, and Chile due to limited coordination mechanisms.[^65]

---
[^1]: https://www.itu.int/en/ITU-D/Cybersecurity/pages/global-cybersecurity-index.aspx
[^2]: https://www.itu.int/en/ITU-D/Cybersecurity/pages/global-cybersecurity-index.aspx
[^3]: https://www.americasquarterly.org/article/new-aq-hackers-paradise-why-latin-america-is-so-vulnerable/#:~:text=%E2%80%9CLatin%20America's%20entrepreneurial%20and%20innovative,cyberbreaches-%20start%20from%20human%20error.
[^4]: https://go.flashpoint.io/2024-global-threat-intelligence-report-download
[^5]: https://www.ptsecurity.com/ww-en/analytics/latam-cybersecurity-threatscape-2022-2023-en/
[^6]: https://www.ibm.com/reports/threat intelligence
[^7]: https://doi.org/CyberThreatIntelligenceAnalysis
[^8]: https://www.ptsecurity.com/ww-en/analytics/latam-cybersecurity-threatscape-2022-2023-en/
[^9]: https://blogs.worldbank.org/en/latinamerica/seguridad-cibernetica-en-america-latina-y-el-caribe
[^10]: https://www.ptsecurity.com/ww-en/analytics/latam-cybersecurity-threatscape-2022-2023-en/
[^11]: https://www.ibm.com/reports/threat-intelligence
[^12]: https://www.statista.com/statistics/802640/gross-domestic-product-gdp-latin-america-caribbean-country/
[^13]: https://blogs.worldbank.org/en/latinamerica/seguridad-cibernetica-en-america-latina-y-el-caribe
[^14]: 10.3390/informatics10030071 10.47460/athenea.v3i9.43
[^15]: https://www.ibm.com/reports/threat intelligence
[^16]: https://www.cnn.com/business/live-news/us-cyberattacks-cybersecurity-06-08-21/index.html
[^17]: https://latinlawyer.com/guide/the-guide-corporate-compliance/fifth-edition/article/mitigating risk-data-breaches-and-cyber-incidents-surge-in-latin-america#:~:text=Globally%2C%20the%20average%20cost%20of,regions%20included%20in%2 0the%20report.
[^18]: https://latinlawyer.com/guide/the-guide-corporate-compliance/fifth-edition/article/mitigating risk-data-breaches-and-cyber-incidents-surge-in-latin-america#:~:text=Globally%2C%20the%20average%20cost%20of,regions%20included%20in%2 0the%20report
[^19]: https://www.americaeconomia.com/en/business-industries/cybersecurity-new-center-concern latin-american-companies
[^20]: https://www.cisa.gov/news events/cybersecurity-advisories/aa23-158a
[^21]: https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html
[^22]: https://www.zdnet.com/article/north-korea-s-apt38-hacking-group-behind-bank-heists-of-over-100-million/
[^23]: https://cybernews.com/security/bankingly-dataleak/#:~:text=On%20May%2024th%2C%20the,anyone%20online.&text=identified%20seven%20Azure%20Blob,anyone%20online.&text=authentication.%20The%20misconfiguration%20exposed,anyone%20online.&text=of%20ne arly%20135%2C000%20clients,anyone%20online
[^24]: https://unit42.paloaltonetworks.com/threat-brief-moveit-cve-2023-34362/
[^25]: https://cybernews.com/security/bankingly-dataleak/#:~:text=On%20May%2024th%2C%20the,anyone%20online.&text=identified%20seven%20Azure%20Blob,a nyone%20online.&text=authentication.%20The%20misconfiguration%20exposed,anyone%20online.&text=of%20nearly%20135%2C000%20clients,anyone%20online
[^26]: https://latam.cs4ca.com/wp-content/uploads/2024-Annual-Report-The-State-of-OT-Cyber-Security-in-LATAM.pdf
[^27]: https://www.statista.com/statistics/802640/gross-domestic-product-gdp-latin-america-caribbeancountry/#:~:text=In%202024%2C%20Brazil%20and,and%20the&text=were%20expected%20to%20be,and%20the&text=countries%20with%20the%20largest,and% 20the&text=domestic%20product%20%28GDP%29%20in,and%20the
[^28]: https://www.wired.com/story/mexico-bank-hack/
[^29]: https://www.centerforcybersecuritypolicy.org/insights-and-research/insights-from-the-annual-latam-ciso-summit-costa-rica
[^30]: https://grcoutlook.com/cybersecurity-risks-latin-america-versus-asia-a-rising-concern/
[^31]: https://blogs.worldbank.org/en/latinamerica/seguridad-cibernetica-en-america-latina-y-el-caribe
[^32]: https://www.wired.com/story/mexico-bank-hack/
[^33]: https://www.eeas.europa.eu/eeas/europe-and-latin-america-caribbean-step-cooperation-cybersecurity_en
[^34]: https://www.datto.com/blog/ransomware-and-cybersecurity-in-latin-america/
[^35]: https://www.centerforcybersecuritypolicy.org/insights-and-research/insights-from-the-annual-latam-ciso-summit-costa-rica
[^36]: https://www.wired.com/story/mexico-bank-hack/
[^37]: https://latam.cs4ca.com/wp-content/uploads/2024-Annual-Report-The-State-of-OT-Cyber-Security-in-LATAM.pdf
[^38]: https://www.infosecurity-magazine.com/news/bank-of-chile-suffers-10m-loss/
[^39]: https://latam.cs4ca.com/wp-content/uploads/2024-Annual-Report-The-State-of-OT-Cyber-Security-in-LATAM.pdf
[^40]: https://attack.mitre.org/groups/G0082/
[^41]: https://latam.cs4ca.com/wp-content/uploads/2024-Annual-Report-The-State-of-OT-Cyber-Security-in-LATAM.pdf
[^42]: https://therecord.media/chile-black-basta-ransomware-attack-customs-department
[^43]: https://cybernews.com/security/bankingly-dataleak/#:~:text=On%20May%2024th%2C%20the,anyone%20online.&text=identified%20seven%20Azure%20Blob,anyone%20online.&text=authentication.%20The%20misconfiguration%20exposed,anyone%20online.&text=of%20ne arly%20135%2C000%20clients,anyone%20online
[^44]: https://cybernews.com/security/bankingly-dataleak/#:~:text=On%20May%2024th%2C%20the,anyone%20online.&text=identified%20seven%20Azure%20Blob,anyone%20online.&text=authentication.%20The%20misconfiguration%20exposed,anyone%20online.&text=of%20ne arly%20135%2C000%20clients,anyone%20online
[^45]: https://cybernews.com/security/banco-portugues-de-gestao-data-leak/
[^46]: https://insightcrime.org/news/four-ways-ai-is-shaping-organized-crime-in-latin-america/
[^47]: https://grcoutlook.com/cybersecurity-risks-latin-america-versus-asia-a-rising-concern/
[^48]: https://www.weforum.org/publications/global-cybersecurity-outlook-2025/digest/
[^49]: https://www.accenture.com/content/dam/accenture/final/accenture-com/document/Accenture-State-Cybersecurity.pdf
[^50]: https://blog.checkpoint.com/research/check-point-research-reports-highest-increase-of-global-cyber-attacks-seen-in-last-two-years-a-30-increase-in-q2-2024-global-cyber-attacks/
[^51]: https://www.fortinet.com
[^52]: https://doi.org/10.1145/3429741
[^53]: https://doi.org/10.3390/su14031390
[^54]: https://www.fortinet.com
[^55]: https://doi.org/10.3390/su14031390
[^56]: https://doi.org/10.3390/su14031390
[^57]: https://doi.org/10.3390/su14031390
[^58]: https://doi.org/10.3390/su14031390
[^59]: https://doi.org/10.1145/3429741
[^60]: https://doi.org/10.3390/su14031390
[^61]: https://doi.org/10.3390/su14031390
[^62]: https://doi.org/10.3390/su14031390
[^63]: https://doi.org/10.3390/su14031390
[^64]: https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
[^65]: https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf

---

Private Coordination across both individual and corporate stakeholders.88
Frameworks The rise of technology-focused trade associations, such
as Chiletec, with its membership of over 100 Chilean
There are substantial gaps in public–private coordination technology companies, provides additional infrastructure
across most LATAM countries that directly impact for coordinating cybersecurity efforts.89
financial sector resilience.82. For instance, while
Ecuador has 14 CSIRTs dedicated to offering incident-
response services to companies, there is no financial
CSIRT.83 Additionally, while these response teams
span critical infrastructure and commercial domains
76 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
77 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
78 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
79 https://elpais.com/america-colombia/2023- 09-14/el-gobierno-aun-no-sabe-cuantas-entidades-estan-afectadas-por-el-hackeo-a-ifx networks.html
80 https://therecord.media/colombia government-ministries-cyberattack
81 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
82 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
83 https://doi.org/10.1007/978-3-030-60467-7_24
84 https://doi.org/10.1007/978-3-030-60467-7_24
85 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
86 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
87 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
88 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
89 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
18

The integration of public–private cybersecurity
coordination in Colombia demonstrates a sophisticated
approach to financial sector resilience, particularly
through collaboration between government entities
(ColCERT, CCOC, MINTIC) and private-sector initiatives
like Asobancaria's CSIRT.90 This partnership exemplifies
how regulatory frameworks can effectively merge with
industry-led operational capabilities to create robust
defense mechanisms.
The operational impact of this coordination is particularly
noteworthy in the financial sector. According to recent
data, Colombia's financial system has demonstrated
remarkable resilience: out of nearly 20 billion cyber
attacks in the past year, only two achieved successful
penetration.91 This success rate can be attributed to
Asobancaria's CSIRT deployment of 17 cybersecurity
experts who have processed over 300 security events
and managed more than 450 early alerts in early 2024
alone.92
The scale of this collaboration is evident in how
Asobancaria's CSIRT functions as both a national and
international focal point for crisis management and
incident response within the financial sector. Their
Operations Center and Information Exchange Program
has established itself as one of Latin America's most
advanced cybersecurity-operations centers, serving
as a model for how public–private partnerships can
enhance sector-wide cyber resilience. This is particularly
significant given Colombia's position as the second most
targeted country for cyber attacks in Latin America.
The success of this approach provides valuable insights
for other LATAM nations seeking to develop similar
public–private cybersecurity frameworks, particularly in
protecting critical financial infrastructure.
90 https://doi.org/10.25062/9789585216549
91 https://www.mintic.gov.co/portal/inicio/
92 https://www.mintic.gov.co/portal/inicio/
19

3 Industry Trends
3.1 Major Cyber-Threat Actors Targeting the been desperately seeking professionals who can protect
Financial Industry in Latin America their digital assets.98 As cyber hygiene and issues around
threat-awareness training make containment efforts
The development of organizational cybersecurity challenging, updating national strategies and developing
programs in Latin America is mirrored by the expansion incident protocols have increased in priority for Latin
of ransomware as a significant cyber threat. The National American security professionals.99 A skilled workforce
Cybersecurity Index (NCSI) highlighted the void in is not traditionally considered part of physical critical
robust cybersecurity policies and regulations across infrastructure. However, it is essential for the security
the LATAM region and, more so, revealed the risks of the infrastructure and is a crucial void in LATAM that
and consequences of ransomware attacks for financial CISOs must prioritize. The human factor remains one of
institutions.93 According to the LATAM CISO 2024 report, the most vulnerable points within an organization.100
in April 2022, Costa Rica’s Ministry of Finance faced a
$10M ransomware attack from Russia-based threat actor Training and global partnerships in academia can be
Conti, which shut down tax-filing systems and caused an investment in a skilled cybersecurity workforce.
economic turmoil and mandates for more skilled workers A shortage of cybersecurity professionals renders
in cybersecurity.94 financial institutions vulnerable to the advanced attacks
experienced by many within the region, as indicated in
As increasing cyber risks are explored within the financial a report by the International Telecommunication Union
sector, the Latin American industry trends of skilled (ITU). Critical infrastructure plans for cyber attacks
workers, capital, investments, and user preferences are only established in seven of 32 LATAM countries,
are vital to this ecosystem. Ultimately, they provide and 20 of 32 have CSIRTs. The Inter-American Bank
quantifiable insights into what voids and best practices assessment also notes that LATAM requires significant
cybersecurity professionals must prioritize to address capacity improvements in skilled professionals.101 This
their cyber-hygiene needs. highlights an urgency for regional improvement in cyber
readiness.102
3.1.1 More Cybersecurity Professionals Needed
Highlight: Critical enhancement in trained IT
According to Vergara Cobos in the “2024 Latin professionals, incident-response plans, and cybersecurity
America and Caribbean” report, from 2023 to 2024, policies are priorities in improving LATAM’s cyber posture.
the global cybersecurity industry grew by 14%, and the Planning, playbooks, and assessment exercises with
global workforce gap grew to 4M, which is twice the third-party organizations are essential. Due to the lack
growth rate of the IT sector and four times that of the of trained staffing and tools to communicate challenges
worldwide economy. This presents significant potential across sectors in response, preparedness is consistently
for job creation via investments in cyber training and revealed as one of the most pressing challenges Training
awareness.95 The LATAM cybersecurity industry is and education initiatives can help address the region's
predicted to grow by 8% in 2025, with growth in a skilled shortage of skilled cybersecurity professionals.
workforce at 15%.96
3.1.2 Greater Cybersecurity Budget to Address
Although industry growth and workforce development are Increased Cyber Threats
on par globally, Latin America’s regional cyber readiness
suggests low confidence in its nations’ ability to resolve In Latin America, banks are the most attacked
cyber attacks with its current critical infrastructure. North organizations, with health and educational institutions
America and Europe show the highest confidence levels trailing shortly behind. When considering specific
at 15%. Meanwhile, Africa and Latin America have the countries, Brazil has the most cyber attacks, with
lowest confidence levels at 36%, and 42% of security Mexico and Colombia following. However, the frequency
professionals in these regions doubt their country’s ability and severity of cyber attacks in other Latin American
to resolve cyber attacks.97 Latin American countries have countries are not reduced.103
93 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
94 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
95 https://blogs.worldbank.org/en/latinamerica/seguridad-cibernetica-en-america-latina-y-el-caribe
96 https://www.nucamp.co/blog/coding-bootcamp-mexico-mex-mexico-cybersecurity-job-market-trends-and-growth-areas-for-2025
97 https://www.nucamp.co/blog/coding-bootcamp-mexico-mex-mexico-cybersecurity-job-market-trends-and-growth-areas-for-2025
98 https://www.nucamp.co/blog/coding-bootcamp-mexico-mex-mexico-cybersecurity-job-market-trends-and-growth-areas-for-2025
99 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
100 https://mexicobusiness.news/cybersecurity/news/beyond-spending-strategic-investment-cybersecurity-2025
101 https://www.mordorintelligence.com/industry-reports/latin-america-cyber-security-market
102 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
103 https://www.americaeconomia.com/en/business-industries/cybersecurity-new-center-concern-latin-american-companies
20

Due to emerging technology such as AI and cyber
attacks worsening in 2024, Latin America has increased
its investments in overcoming cybercrime.104 The cost
of cyber attacks in 2023 was USD 6T globally and USD
2.4M in Latin America. The growth in 2025 is expected
to increase by 60% globally and 76% in Latin America,
which is an all-time high for the region since 2020.105
Notably, while 77% of Latin American organizations
plan to increase cybersecurity budgets, only 25% of
organizations in LATAM have adopted comprehensive
cybersecurity plans.106 Global spending on cybersecurity
will exceed USD 1T in 2025, which creates opportunities
to address Latin America’s confidence in cybersecurity
readiness.107 Budgeting for cybersecurity often reflects
the economic conditions of an area, which is becoming
a spending priority as an organization understands the Figure 4: Latin American
need for data assurance and trust in their brand.108 Cybersecurity Market
Highlight: The United States has committed to providing
Latin America Cybersecurity Market
advanced hardware, specialized training, and logistic
Market Size in USD Billion
support, offering USD 25M by 2026 to help Costa Rica
CAGR 6.95%
enhance its cybersecurity capabilities. In June 2022,
USD 24M was allocated by the Costa Rican government
for incident response and security operations. The
severity of the LATAM threat landscape is not attributed USD 13.35 B
to the increasing funds sowed into their commitment
to cyber defense. More so, it is based on the nation
becoming the first globally to declare a state of
emergency due to a cyber attack.109
USD 9.54 B
As highlighted in Figure 4, the Latin American
cybersecurity market is estimated to be USD 9.54B in
2025. It is expected to reach USD 13.35B by 2030, at a
CAGR of 6.95% from 2025 to 2030, which is driven by
the rapid digitalization of financial services and banking
infrastructure.110 Budgets reflect the current, more
established plans for cyber readiness and response to
cyber attacks, whereas investments attest to awareness
and proactive preparation to create a more effective 2025 2030
regional cyber posture. Increased investments in cyber-
readiness solutions and services suggest an impact on
the growing recognition of cybersecurity’s importance in
Latin America.111
104 https://www.americaeconomia.com/en/business-industries/cybersecurity-new-center-concern-latin-american-companies
105 https://www.americaeconomia.com/en/business-industries/cybersecurity-new-center-concern-latin-american-companies
106 https://mexicobusiness.news/cybersecurity/news/beyond-spending-strategic-investment-cybersecurity-2025
107 https://mexicobusiness.news/cybersecurity/news/beyond-spending-strategic-investment-cybersecurity-2025
108 https://www.pwc.com/gx/en/services/forensics/gecs/2024-global-economic-crime-survey.pdf
109 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
110 https://www.mordorintelligence.com/industry-reports/latin-america-cyber-security-market
111 https://www.mordorintelligence.com/industry-reports/latin-america-cyber-security-market
21

3.1.3 Reasons for Investments Investing in cybersecurity can create positive economic
effects, with an expected increase of 1.5% GDP per
The digitization of the financial industry in LATAM capita if cyber protections are enhanced and cyber
requires more investments in cybersecurity, which incidents are reduced from 50 to seven major incidents.
includes machine learning and AI for improved threat The “Cybersecurity Economics for Emerging Markets”
detection and response capabilities. If not, many reports how digitalization has outpaced the region’s
regional fintech startups will become highly attractive cybersecurity capacity. As of 2024, Latin America and
targets for cybercriminals. Overall, this suggests a need the Caribbean are the least protected regions, with an
for more cybersecurity investments in Latin America. average cyber score of 10.2 out of 20, and the world’s
fastest-growing regions for disclosed cyber incidents
Unfortunately, the increase in digitalization is not scaling at a 25% annual growth rate over the last 10 years.114
with the risk associated with the government sector, and Rapid digitalization in Latin America has increased cyber
it is imperative that ransomware threats be addressed threats, specifically in the financial sector.
due to the lack of maturity in organizational cybersecurity
programs and policies for critical infrastructure in Internet usage corresponds to the share of the
LATAM.112 population using the internet. Figure 5 highlights that
LATAM went from 68% to 81% between 2019 and 2023,
Highlight: It is imperative to address cyber risks according to ITU.
regarding data protection and national security. Due
to significant ransomware attacks, 200 executive-level
security professionals in the public and private sectors
agree on prioritizing cybersecurity.113
Figure 5: Effect of LAC’s Digitalization
13
percentage point
increase in the
share of the
population online
145% 280%
increase in internet rise in e-commerce
of things devices volume
Greater adoption of
e-government tools
20 20
20 19 19 19
18
17 17 17
16
15 15 1515 15 15
Lowest scores 15 14 13 14 13 14 13 14
12 12 12
in Cybersecurity 10 10 11 10 10
Commitments 10 8 9 8 8
5
0
NA ECA MENA EAP SA SSA LAC
Capacity building International cooperation Legal measures
Organizational structures Technical and procedural measures
Source: Cybersecurity Economics for Emerging Markets (2024).115
112 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
113 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
114 https://blogs.worldbank.org/en/latinamerica/seguridad-cibernetica-en-america-latina-y-el-caribe
115 https://blogs.worldbank.org/en/latinamerica/seguridad-cibernetica-en-america-latina-y-el-caribe
22

3.1.4 Shift from Brick & Mortar to Online and App- measures common in more established markets. A study
Based Banking by the IMF highlights that these cybersecurity challenges
stem from factors such as low awareness, outdated
Financial institutions both in Latin America and globally software, insufficient standards, critical-infrastructure
focus on enhancing front-end user experience through gaps, and limited professional training.120
easy-to-use apps and web-based features. However,
this shift has created new vulnerabilities in sophisticated 3.2.2 Reliance on Outdated Systems
social engineering and phishing methods, primarily
in online-banking markets.116 Convenience drives Due to developing infrastructure and lackluster
digital and mobile banking solutions favored by Latin technological and data systems, many economic
American consumers, and users too often accept new enterprises in Latin America often rely on outdated
technology or solutions based on ease of use versus systems. An analysis published in MDPI's Informatics
security requirements, which increases the risk of social journal identifies the use of outdated software as a
engineering attacks like phishing.117 critical vulnerability in Latin American countries.121 This
dependency on obsolete technology leaves these
Highlight: Colombia is focused on improving incident systems vulnerable to newer threats as they often lack
tracing; Costa Rica has prioritized international essential security updates and patches. Even when
partnerships for response capabilities, such as digital updates are available, the underlying architecture of
forensics and skilled-workforce training; and Chile these outdated systems may remain susceptible due to
established cyber standards in its Digital Agenda 2035 hardware limitations. Consequently, financial institutions
initiative to address digitization and cybersecurity.118 To with such poor systems can be easily targeted by
ensure that cybersecurity measures do not negatively cybercriminals. Addressing this issue requires substantial
impact the user experience, financial institutions and investment in modernizing IT infrastructure and the
banks must be aware of user preferences for digital implementation of maintenance protocols. Encouraging
services. financial institutions to move to the cloud would provide
modern, more secure systems and automated updates.
Investments in cybersecurity for the financial industry According to the World Economic Forum's report on
in Latin America are rising. Nonetheless, the industry Latin America's cybersecurity challenges, adopting risk-
must improve the culture of cyber awareness and adopt management frameworks (RMFs) and using public cloud
innovative solutions to address ongoing threats to technologies to improve cyber resilience and protect
protect assets and customers. An enhanced security vital infrastructure could combat ransomware attacks.122
posture will help confront the complex cyber-threat To fully realize the security infrastructure gains of the
landscape of organized cybercriminals, state-sponsored cloud, financial institutions would need to hire or rely on
actors, and insider threats. third parties to ensure security controls are in place and
consistent.
3.2 Contextual Socio-Economic Factors Impacting
Risk Exposure
3.2.1 Rapid Fintech Growth
Latin America's fintech sector has grown considerably
over the past six years, driven by socio-economic
factors such as increasing mobile-phone adoption
and large underbanked populations. This growth is
characterized by a 340% increase in the number of
financial technology companies, which rose from
703 across 18 countries in 2017 to 3,069 across 26
countries by 2023.119. Notably, this expansion surpasses
the growth observed in more established markets
like the United States, where fintech innovation has
been significant but limited to its more mature market.
However, this rapid development has exposed new
vulnerabilities as many emerging fintech companies
in Latin America often lack the robust cybersecurity
116 https://www.mordorintelligence.com/industry-reports/latin-america-cyber-security-market
117 https://www.statista.com/statistics/1481783/online-bankingpenetration-latin-america-forecast/:~:text=Online%20banking%20penetration%20in%20
Latin%20America%20increased%20gradually%20between%202019,to%2033%20percent%20in%202023
118 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
119 https://www.iadb.org/en/news/study-fintech-ecosystem-latin-america-and-caribbean-exceeds-3000-startups
120 https://www.imf.org/en/Publications/fintech-notes/Issues/2023/03/28/The-Rise-and-Impact-of-Fintech-in-Latin-America-531055
121 https://www.mdpi.com/2227-9709/10/3/71
122 https://www.weforum.org/stories/2024/05/latin-america-cybersecurity-report-ransomware attacks/
23

3.2.3 Economic & Digital Disparities
Latin America exhibits significant economic and digital
disparities across its territory, leading to a pronounced
digital divide. As of 2022, 67.3% of households in the
region had internet access, compared to 91.1% in OECD
countries.123 This disparity poses challenges for small and
medium-sized enterprises (SMEs), which are vital to the
region's economy.124 Many of these enterprises operate on
limited budgets, restricting their ability to invest in robust
cybersecurity measures. This financial constraint makes
them attractive targets for cybercriminals as SMEs often
lack the advanced defenses found in larger corporations.
Investing in digital infrastructure to reduce the digital divide
among individuals and SMEs can improve cybersecurity
and mitigate prominent risks.
123 https://www.undp.org/latin-america/blog/missed-connections-incomplete-
digital-revolution-latin-america-and-caribbean-0
124 https://www.iadb.org/en/news/ninety-six-percent-banks-latin-america-
and-caribbean-view-small-and-medium-enterprises#:~:text=Ninety%2Dsix%20
percent%20of%20the,policy%20for%20SMEs%20in%20place.
24

4 Regulatory Gaps
4.1 Ransomware Breach Reporting Requirements This fragmented regulatory landscape creates significant
and Lack of Standards gaps, making LATAM increasingly susceptible to
ransomware attacks. Countries with limited or no
Cybersecurity reporting requirements across LATAM mandatory reporting, such as Central American
are inconsistent, leading to vulnerabilities in the region’s nations, face challenges in tracking and responding
ability to combat cyber threats effectively. to threats due to insufficient data sharing and threat-
intelligence coordination.129 The lack of harmonized
For instance, consider the following: security standards results in inconsistent practices
across the region, leaving weak points for cybercriminals
1. Brazil’s General Data Protection Law (LGPD) to exploit.130 Furthermore, inadequate cybersecurity
mandates organizations to report breaches to the infrastructure, insufficient education, and limited
National Data Protection Authority (ANPD) within two resources exacerbate these vulnerabilities, especially in
business days and notify affected individuals.125 sectors such as manufacturing and finance, which have
faced over 100 ransomware incidents since 2023.131 132
2. Colombia requires organizations to report security- The absence of stringent reporting frameworks also
code violations to the Delegatura para la Protección delays breach response times, allowing ransomware
de Datos Personales (Office for the Protection of operators to further exploit compromised systems.133
Personal Data) and affected data subjects.126 Rapid digital transformation in LATAM, especially
within financial services, has outpaced regulatory
3. Mexico enforces reporting of "data vulnerabilities" developments, creating additional attack surfaces.134
impacting individuals’ rights but does not specify a 135 Without robust incident-reporting requirements and
timeline. coordinated defense strategies, many LATAM nations
are struggling to combat increasingly sophisticated
4. Argentina merely recommends voluntary reporting ransomware threats targeting government and financial
as a best practice.127 institutions.136 137
5. Many countries, such as Peru, Ecuador, and Costa
Rica, lack comprehensive reporting frameworks
altogether.128
125 https://iapp.org/news/a/reporting-cyber-incident-requirements-in-some-latin-american-jurisdictions
126 https://iapp.org/news/a/reporting-cyber-incident-requirements-in-some-latin-american-jurisdictions
127 https://iapp.org/news/a/reporting-cyber-incident-requirements-in-some-latin-american-jurisdictions
128 https://www.dacbeachcroft.com/en/What-we-think/Stepping-up-in-Latin-America-Chile-enacts-a-new-Cybersecurity-Law
129 https://www.moodys.com/web/en/us/insights/credit-risk.html
130 https://www.moodys.com/web/en/us/insights/credit-risk.html
131 https://www.cloudsek.com/whitepapers-reports/latin-america-latam-cyber-threat-landscape-2023-24
132 https://www.recordedfuture.com/research/latin-american-governments-targeted-by-ransomware
133 https://www.datto.com/blog/ransomware-and-cybersecurity-in-latin-america/
134 https://www.datto.com/blog/ransomware-and-cybersecurity-in-latin-america/
135 https://www.trustwave.com/en-us/resources/blogs/trustwave-blog/trustwave-spiderlabs-reveals-the-ransomware-threats-targeting-latin-american-financial-
and-government-sectors/
136 https://www.trustwave.com/en-us/resources/blogs/trustwave-blog/trustwave-spiderlabs-reveals-the-ransomware-threats-targeting-latin-american-financial-
and-government-sectors/
137 https://industrialcyber.co/analysis/recorded-future-detects-escalation-of-ransomware-attacks-across-latam-government-entities/
25

5 Threat-Actor Profiles
5.1 CL0P Impact and Scale of CL0P’s Operations:
CL0P emerged in early 2019 as a derivative of the • CL0P's activities saw a 340% increase in victims
Cryptomix ransomware family.138 The ransomware compared to the previous quarter, potentially due to
group quickly evolved from utilizing traditional the MOVEit zero-day vulnerability exploitation.145
ransomware-deployment methods into a sophisticated • The group is expected to earn $75–100 million from
cyber-threat group targeting global enterprises.139 The extorting victims in their massive MOVEit data-theft
group's ransomware is characterized by its unique campaign.146
".clop" file extension and the distinctive "Don't Worry
CL0P" string in its ransom notes.140 The group's initial 5.1.2 Malware Capabilities and Functionality
operations relied primarily on traditional ransomware
deployment through phishing campaigns. However, their CL0P's technical sophistication is evident in their
methodology underwent a significant transformation carefully structured attack chains. Their initial access
as they adopted a RaaS model. This transition proved vectors have evolved from simple phishing campaigns to
crucial, allowing them to leverage relationships with sophisticated zero-day exploitation techniques.147. The
sophisticated threat actors, including TA505, FIN11, and group maintains a diverse toolkit, including specialized
UNC 2546, for deployment operations. malware, such as SDBot for lateral movement, Cobalt
Strike for post-exploitation activities, and custom tools
5.1.1 Victim Profile and Impact Analysis like FlawedAmmyy/FlawedGrace for command-and-
control operations.148
Analyzing CL0P’s victim list suggests that the
ransomware group primarily targets large enterprises CL0P’s use of TrueBot, an advanced malware
with revenues exceeding USD 5M.141 The main target component associated with the Silence Group,
entities of CL0P are from the following sectors: banking demonstrates their connections to sophisticated financial
and finance, healthcare, manufacturing, education, and threat actors. TrueBot's capability to deploy additional
energy.142 CL0P’s activities have been prevalent in the payloads while maintaining stealth through self-deletion
United States, United Kingdom, Germany, Canada, mechanisms showcases their focus on operational
Brazil, and Mexico, which account for 77.3% of their security.149 Furthermore, the malware's association
attacks.143 with TA505 and its use of an exclusive backdoor
named FlawedGrace, indicates CL0P's position
The impact of CL0P's operations in Latin American within a sophisticated cyber-threat ecosystem.150 The
countries has been substantial, particularly in Brazil and group’s initial network penetration typically follows an
Mexico.144 In LATAM, where cybersecurity frameworks orchestrated multi-stage approach:
are nascent, organizations face amplified vulnerabilities
due to interconnected systems and limited incident- 1. The exploitation of public-facing web applications
response capabilities. Moreover, financial institutions using the LEMURLOOT web shell, written in C#
in Latin America face a dual threat: direct attacks on coding language and disguised as an ASP.NET file.
banking systems and supply-chain compromises, such 2. Credential-harvesting operations enabling lateral
as the MOVEit zero-day exploit, which affected hundreds movement and access to sensitive data. 3. Data-theft
of organizations. operations showing careful attention to operational
security, focusing on exfiltration rather than encryption.151
138 https://www.sangfor.com/blog/cybersecurity/Cl0p ransomware-gang-what-you-need-to-know
139 https://unit42.paloaltonetworks.com/cl0p-group-distributes-ransomware-data-with-torrents/
140 https://www.sangfor.com/blog/cybersecurity/Cl0p ransomware-gang-what-you-need-to-know
141 https://www.sangfor.com/blog/cybersecurity/Cl0p ransomware-gang-what-you-need-to-know
142 https://www.securin.io/blog/all-about-clop-ransomware/
143 https://socradar.io/dark-web-threat-profile-clop-ransomware/
144 https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware spotlight-clop
145 https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q3- 2023/
146 https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q3- 2023/
147 https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware spotlight-clop
148 https://blog.talosintelligence.com/breaking-the-silence-recent-truebot-activity/
149 https://em360tech.com/tech-article/what-is-cl0p-ransomware
150 https://em360tech.com/tech-article/what-is-cl0p-ransomware
151 https://em360tech.com/tech-article/what-is-cl0p-ransomware
27

5.1.3 Evolution of CL0P’s Operations The move towards only data exfiltration is a logical
evolution of CL0P's tactics for several reasons:
1. Shift in attack vector: Initially, CL0P relied
primarily on phishing campaigns with macro-enabled 1. Reduced detection risk: Without file encryption,
documents to deliver the Get2 malware dropper.152 there are fewer obvious indicators of compromise
In recent campaigns, they have pivoted to exploiting (IOCs), making it difficult for organizations to quickly
zero-day vulnerabilities in widely used file-transfer identify an ongoing attack.
applications.153 154
2. Extended access: By not alerting victims through
2. Focus on data exfiltration: While their initial encryption, CL0P can potentially maintain access
attacks involved both file encryption and data theft, to systems for longer periods, allowing for more
recent campaigns have concentrated more on data comprehensive data theft.
exfiltration without necessarily encrypting files.155 156
3. Simplified operations: Focusing solely on data
3. Scale of attacks: Recent campaigns have exfiltration streamlines the attack process, potentially
targeted significantly more victims simultaneously allowing CL0P to target more victims simultaneously.
through supply-chain attacks. For example,
the MOVEit exploit in 2023 impacted up to 400 4. Increased pressure: The threat of leaking sensitive
organizations.157 data can be just as effective as file encryption in
forcing victims to pay, without the added complexity
4. Sophistication of techniques: CL0P has evolved of providing decryption tools.
to use more advanced evasion techniques, including
digital signatures to bypass endpoint detection.158 The success of this approach is evident in CL0P's recent
campaigns, such as the 2023 MOVEit attack, where they
5. Expansion to new platforms: Initially targeting claimed to have breached hundreds of companies by
only Windows systems, CL0P developed a Linux exploiting a zero-day vulnerability (CVE-2023-34362) to
variant in late 2022, broadening their potential victim mass download organizations' data without encrypting
base.159 files.162 By adopting this stealthier approach, CL0P can
potentially increase the success rate of their attacks and
6. Ransom approach: Recent campaigns have seen the likelihood of ransom payments as organizations may
CL0P directly contacting upper level executives with feel more pressure to prevent the leak of sensitive data.
ransom demands, rather than leaving traditional
ransom notes on infected systems.160 Although there is less concrete evidence for CL0P’s shift
explicitly to stealth, cybersecurity experts acknowledge
7. Exploitation timeline: CL0P has shown increased that groups are adopting only data extortion to
patience and strategic planning, with evidence circumvent traditional defenses. Data exfiltration
suggesting they may have been preparing the MOVEit provides ransomware groups with a greater advantage
exploit since 2021.161 over their victims in several ways:
CL0P's shift from encrypting devices to focusing solely 1. Prolonged extortion potential: Once data is
on data exfiltration makes their attacks potentially stolen, cybercriminals can continue exploiting it for
stealthier and more difficult to detect. This change additional extortion long after the initial incident, even
in modus operandi could allow CL0P to operate if the original ransom is paid.163
undetected for longer periods as there are no immediate
signs of compromise, such as encrypted files or ransom 2. Tailored demands: Exfiltrated data allows
notes. attackers to customize their extortion demands
based on the sensitivity and value of the stolen
information.164 165
152 https://www.nuspire.com/blog/a-deep-dive-into-cl0p-ransomware/
153 https://em360tech.com/tech-article/what-is-cl0p-ransomware
154 https://www.criticalstart.com/threat-research-cl0p-ransomware-increases-activity
155 https://em360tech.com/tech-article/what-is-cl0p-ransomware
156 https://www.criticalstart.com/threat-research-cl0p-ransomware-increases-activity
157 https://www.criticalstart.com/threat-research-cl0p-ransomware-increases-activity
158 https://em360tech.com/tech-article/what-is-cl0p-ransomware
159 https://www.criticalstart.com/threat-research-cl0p-ransomware-increases-activity
160 https://em360tech.com/tech-article/what-is-cl0p-ransomware
161 https://em360tech.com/tech-article/what-is-cl0p-ransomware
162 https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/ransomware double-extortion-and-beyond-revil-clop-and-conti
163 https://www.grcilaw.com/blog/top-3-reasons ransomware-groups-are-focusing-more-on-data-exfiltration-than-encryption
164 https://www.grcilaw.com/blog/top-3-reasons ransomware-groups-are-focusing-more-on-data-exfiltration-than-encryption
165 https://www.vadesecure.com/en/blog/data-exfiltration-why ransomware-is-about-more-than-the-ransom
28

3. Increased pressure: The threat of leaking sensitive 4. Compliance requirements: Many FTAs, like
data can be more effective than file encryption in MOVEit, are approved for use in regulated industries,
forcing victims to pay as it exploits fears of regulatory meaning they often contain highly sensitive data.176
fines, reputational damage, and competitive
disadvantage.166 167 5. High-value targets: Organizations using FTAs
often include large enterprises and government
4. Bypassing backups: While organizations can agencies, which are lucrative targets for ransomware
restore encrypted files from backups, they cannot attacks.177 178
retrieve data that has already been stolen, which
makes traditional backup solutions ineffective against 6. Stealth: Accessing systems through legitimate
modern ransomware attacks.168 file-transfer tools can make malicious activities appear
normal, helping attackers evade detection.
5. Secondary-attack potential: Compromised data
can fuel future breaches through tactics such as This approach has proven highly effective for CL0P, as
credential stuffing, social engineering, and password- evidenced by their successful attacks on the Accellion
reuse attacks.169 FTA, GoAnywhere MFT, and MOVEit Transfer, each
affecting hundreds of organizations and potentially
6. Higher profitability: Stolen data can be more exposing millions of individuals' data.179 180
valuable than ransom payments as it can be sold on
the dark web or used for ongoing blackmail.170 5.1.4 Impact on Financial Infrastructure
This shift towards data exfiltration demonstrates The systematic nature of CL0P's operations against
the evolving tactics of ransomware groups as they financial institutions has revealed fundamental
adapt to improved organizational defenses and seek vulnerabilities in sector-wide security architectures.
more effective ways to pressure victims into paying The group’s successful exploitation of managed file-
ransoms.171 172 transfer systems has exposed critical weaknesses in the
financial sector's approach to secure data transfer and
The ransomware group has significantly evolved its the integration of third-party software.181 The MOVEit
operational methodology since its emergence in 2019, campaign serves as a particularly instructive example,
becoming one of the most feared ransomware groups by where a single vulnerability in a widely used platform led
2023. The group's focus on zero-day vulnerabilities in file to compromises across multiple financial institutions.182
transfer applications (FTAs) is driven by several factors:
Additionally, the impact extends beyond immediate
1. Widespread use: FTAs are commonly used in operational disruption. Financial institutions affected
corporate environments, providing attackers with by CL0P operations have faced complex challenges
numerous potential entry points.173 in maintaining regulatory compliance and developing
updated policies while managing ongoing compromise
2. Supply-chain attack potential: Exploiting FTA scenarios. In Peru alone, 47% of CISOs list complying
vulnerabilities allows CL0P to potentially compromise with geographically fragmented and overly prescriptive
multiple organizations simultaneously.174 175 regulations as their most stressful responsibility. Of
all industries, the financial services industry is most
3. Efficient data exfiltration: FTAs are designed for concerned about fragmented regulations, with 67% of
efficient data transfer, facilitating the theft of large global CISOs in the sector anticipating that international
amounts of data. regulations will become more complex and difficult
to manage in the next year. Accordingly, CL0P’s
understanding of financial sector regulatory frameworks
has allowed them to structure their extortion demands in
166 https://www.grcilaw.com/blog/top-3-reasons ransomware-groups-are-focusing-more-on-data-exfiltration-than-encryption
167 https://www.infosecurity-magazine.com/news/ransomware defense-evasion-data/
168 https://www.grcilaw.com/blog/top-3-reasons ransomware-groups-are-focusing-more-on-data-exfiltration-than-encryption
169 https://www.grcilaw.com/blog/top-3-reasons ransomware-groups-are-focusing-more-on-data-exfiltration-than-encryption
170 https://www.infosecurity-magazine.com/news/ransomware defense-evasion-data/
171 https://www.vadesecure.com/en/blog/data-exfiltration-why ransomware-is-about-more-than-the-ransom
172 https://www.infosecurity-magazine.com/news/ransomware defense-evasion-data/
173 https://cyberint.com/blog/dark-web/cl0p-ransomware/
174 https://cyberint.com/blog/dark-web/cl0p-ransomware/
175 https://www.cisa.gov/sites/default/files/2023- 06/aa23-158a-stopransomware-cl0p-ransomware-gang-exploits-moveit-vulnerability_5.pdf
176 https://cyberint.com/blog/dark-web/cl0p-ransomware/
177 https://cyberint.com/blog/dark-web/cl0p-ransomware/
178 https://www.cisa.gov/sites/default/files/2023- 06/aa23-158a-stopransomware-cl0p-ransomware-gang-exploits-moveit-vulnerability_5.pdf
179 https://cyberint.com/blog/dark-web/cl0p-ransomware/
180 https://www.cisa.gov/sites/default/files/2023- 06/aa23-158a-stopransomware-cl0p-ransomware-gang-exploits-moveit-vulnerability_5.pdf
181 https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware spotlight-clop
182 https://securityandtechnology.org/blog/2023-rtf-global-ransomware-incident-map
29

ways that create maximum pressure within a patchwork 3. Insufficient Mandatory Reporting Requirements
of emerging regulatory obligations [26]. Based on
their MOVEit campaign, CL0P has demonstrated the Many Latin American countries lack comprehensive
advanced timing of releases and extortion demands as it mandatory breach reporting requirements, particularly
batch-releases victim data to maximize pressure.183 for financial institutions. This regulatory gap aligns with
CL0P's documented tactics of exploiting information
With over 1,600 cyber-attack attempts per second on asymmetries and delayed incident detection.190 The
Latin American companies, LATAM financial institutions absence of stringent reporting requirements can extend
have faced specific challenges due to the interconnected the window of opportunity for sophisticated gangs like
nature of regional financial networks.184 The exploitation CL0P to maintain persistence and expand their access
of shared infrastructure and common software within compromised networks.
platforms has created cascading effects across multiple
institutions.185 This regional impact is exemplified by the 4. Data-Protection Implementation Challenges
aftermath of the GoAnywhere MFT campaign, where
multiple regional institutions discovered compromises While countries such as Brazil, Argentina, Mexico,
through shared infrastructure dependencies.186 Panama, and Colombia have enacted data-protection
laws, implementation and enforcement remain
5.1.5 Regulatory and Policy Gaps inconsistent. This creates vulnerabilities for financial
institutions handling sensitive customer data, aligning
1. Limited Frameworks for Critical-Infrastructure with CL0P's demonstrated focus on data theft and
Protection multi-stage extortion operations targeting financial
services providers. Their use of FlawedAmmyy/
One fundamental vulnerability stems from Latin FlawedGrace for command-and-control operations
America’s nascent frameworks for critical-infrastructure demonstrates specific adaptation to regional financial
protection. According to the Inter-American sector security controls, allowing them to maintain
Development Bank, only seven of 32 Latin American persistent access.
countries have established plans to protect critical
infrastructure from cyber attacks, with only 20 attesting 5.1.6 Market Structure and Digital-Transformation
to any CSIRTs.187 This regulatory immaturity particularly Context
affects financial institutions, which lack federal sector-
specific security protocols and incident-reporting The Latin American banking market remains the
requirements standardized across LATAM jurisdictions.188 fastest-growing globally, with revenue before cost of
risk growing at a compound annual rate of 12% since
2. Fragmented Incident-Response Coordination 2012, reaching $418 billion in 2017.191 Since 2020,
the LATAM retail-banking sector has nearly doubled
The absence of centralized cybersecurity governance its compound annual-revenue growth rate (measured
creates significant coordination challenges during in trillions USD) from 2013 to 2019.192 Furthermore,
cybersecurity incidents. This gap was evident in both LATAM has experienced significant growth in online-
Costa Rica’s 2022 ransomware crisis and Colombia's payments revenues and is projected to outpace all
September 2023 IFX Networks attack, which initially other regions until 2027.193. This rapid historical growth,
affected 20 public entities and indirectly impacted combined with relatively low banking penetration rates
another 78 public entities and 762 private companies— of 30–50% compared to 90%+ in developed markets,
including financial institutions across multiple LATAM creates pressure for rapid digital transformation that
nations.189 The lack of standardized incident-response often outpaces security implementation.194With the
protocols across the region creates opportunities for number of LATAM consumers who prefer mobile and
threat actors like CL0P to exploit gaps in cross-border card payments doubling since 2021, LATAM banks are
coordination. CL0P has demonstrated a sophisticated shifting to a mobile-first delivery strategy while prioritizing
understanding of these gaps, as demonstrated by IT investments to improve user experiences.195
their systematic targeting of widely used enterprise
software platforms that can affect multiple institutions
simultaneously.
183 https://www.cisa.gov/sites/default/files/2023- 06/aa23-158a-stopransomware-cl0p-ransomware-gang-exploits-moveit-vulnerability_5.pdf
184 https://www.cisa.gov/sites/default/files/2023- 06/aa23-158a-stopransomware-cl0p-ransomware-gang-exploits-moveit-vulnerability_5.pdf
185 https://www.cisa.gov/sites/default/files/2023- 06/aa23-158a-stopransomware-cl0p-ransomware-gang-exploits-moveit-vulnerability_5.pdf
186 https://www.cisa.gov/sites/default/files/2023- 06/aa23-158a-stopransomware-cl0p-ransomware-gang-exploits-moveit-vulnerability_5.pdf
187 https://publications.iadb.org/publications/english/document/2020-Cybersecurity-Report-Risks-Progress-and-the-Way-Forward-in-Latin-America-and-the-
Caribbean.pdf
188 https://iapp.org/news/a/reporting-cyber-incident-requirements-in-some-latin-american-jurisdictions
189 https://www.metabaseq.com/e-book/cyber-readiness-in-latin-american-public-sectors/
190 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
191 https://www.mckinsey.com/industries/financial-services/our-insights/lessons-from-leaders-in-latin-americas-retail-banking-market
192 https://www.mckinsey.com/industries/financial-services/our-insights/global-banking-annual-review
193 https://www.mckinsey.com/industries/financial-services/our-insights/global-banking-annual-review
194 https://www.mckinsey.com/industries/financial-services/our-insights/lessons-from-leaders-in-latin-americas-retail-banking-market
195 https://www.mckinsey.com/industries/financial-services/our-insights/global-banking-annual-review
30

5.1.7 Profitability Pressures Creating Security 3. Workforce-Development Challenges
Tradeoffs
A critical industry vulnerability stems from the severe
While Latin American banks were once the most shortage of cybersecurity professionals across Latin
profitable globally, with an ROE of 14% in 2017, they America. For example, Chile alone faces an annual deficit
continue to face significant cost-efficiency challenges. of approximately 6,000 IT professionals.200 This human-
Operating expenses average 3.9% of assets, which is capital gap particularly affects financial institutions' ability
1.5% higher than the next closest region.196 This cost to do the following:
pressure creates vulnerabilities as institutions balance
digital-transformation investments with security spending. • Implement sophisticated security controls
Furthermore, consumer finance and mortgage services • Maintain effective security operations
(which account for more than one-third of after-risk • Respond rapidly to emerging threats
revenues) are especially attractive for threat actors due to • Adapt to evolving attack methodologies
their high concentration of sensitive customer data.197
The workforce shortage aligns with CL0P's documented
5.1.8 Sector-Specific Vulnerabilities tactics of exploiting gaps in security monitoring and
incident-response capabilities.
1. Digital-Transformation Pressures
4. Infrastructure Dependencies
The Latin American financial services sector is
undergoing rapid digital transformation, particularly Latin American financial institutions frequently rely
accelerated by the bankarization (the level of access to on shared infrastructure and common technology
and the degree of use of financial and banking services) platforms, creating systemic vulnerabilities that CL0P
after the COVID-19 pandemic. This creates an expanded has proven adept at exploiting. The September 2023
attack surface that CL0P has demonstrated proficiency IFX Networks attack demonstrated how the compromise
in exploiting. The adoption of managed file transfer (MFT) of a single service provider could impact multiple
solutions often outpaces security implementations, as financial institutions across several countries.201 Such
evidenced by the widespread impact of CL0P's MOVEit interdependence is exacerbated by the gap in the
campaign across the region's financial institutions.198 region’s infrastructure-protection frameworks.
Financial institutions should ensure they have adequate
security and operational resilience “know-how” before 5.1.9 Public-Sector Gaps Creating Downstream Risk
onboarding technology to assure the safety and
soundness of the institution. 1. Resource-Allocation Disparities
2. Operational Vulnerability Drivers Public-sector cybersecurity budgets in Latin America
consistently lag behind private-sector investments. This
The banking sector's vulnerabilities can be traced to creates particular challenges for financial institutions that
three distinct market archetypes identified in the region199: must interface with government systems, especially in
areas such as the following:
• Efficiency-Driven Markets: These markets, such
as Chile, operate with lean cost structures but • Tax collection and reporting
may underinvest in security infrastructure. Their • Regulatory-compliance systems
operational expense ratio below 3.4% of assets often • National payment infrastructures
necessitates reduced security spending. • Identity-verification services
• Balanced Markets: Markets like Brazil combine
moderate revenue generation (4.5–7% of assets)
with mid-range operational costs, creating potential
security gaps when balancing competing investment
priorities.
• Revenue-Driven Markets: Markets like Argentina
generate high revenues but operate with operational
expenses above 5.5% of assets, potentially lacking
efficiency in security operations despite higher
spending.
196 https://www.mckinsey.com/industries/financial-services/our-insights/lessons-from-leaders-in-latin-americas-retail-banking-market
197 https://www.mckinsey.com/industries/financial-services/our-insights/lessons-from-leaders-in-latin-americas-retail-banking-market
198 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
199 https://www.mckinsey.com/industries/financial-services/our-insights/lessons-from-leaders-in-latin-americas-retail-banking-market
200 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
201 https://www.metabaseq.com/e-book/cyber-readiness-in-latin-american-public-sectors/
31

CL0P's targeting methodology often exploits these effect makes the region particularly attractive for
public–private interconnections, as demonstrated in both sophisticated ransomware operations seeking maximum
the Costa Rica and Colombia incidents.202 leverage for extortion demands.
5.1.10 Convergence of Vulnerabilities Creating 5.1.11 Forward-Looking Implications
Strategic Opportunity for CL0P
Evolving Threat Landscape
The combination of regulatory gaps and industry
trends creates multiple vectors that align with CL0P's The combination of regulatory gaps and industry
sophisticated targeting methodology and operational pressures suggests the continued targeting of Latin
patterns: American financial institutions by sophisticated threat
actors. CL0P's demonstrated ability to adapt their
1. Multi-Stage Exploitation Opportunities tactics to regional vulnerabilities indicates the following:
CL0P's documented preference for multi-stage extortion • Attack sophistication will likely increase
operations has proven effective in Latin America due to • Cross-border incidents will become more common
the convergence of several factors: • Supply-chain compromises will continue to be
leveraged
• Delayed detection capabilities due to workforce • Multi-stage extortion operations will expand
shortages
• Complex cross-border coordination requirements
• Inconsistent incident-reporting frameworks
• Regional interconnectivity of financial systems
This environment enables CL0P to maximize both initial
access and lateral movement opportunities.203
2. Financial Sector Attack Surface
The financial services industry's digital-transformation
initiatives, combined with regulatory-compliance
requirements, create an expanded attack surface that
CL0P has demonstrated expertise in exploiting. The
group's sophisticated understanding of financial sector
operational patterns is evidenced in their targeting of the
following:
• Managed file-transfer systems essential for
regulatory reporting
• Weak authentication and access-control protocols
• Shared service providers serving multiple institutions
• Cross-border payment and settlement systems
• Core banking platforms with regional deployments
This targeting aligns with the documented capabilities of
their advanced malware toolkit, which includes TrueBot
and FlawedGrace, which are specifically adapted to
financial sector security controls.204
3. Regional Amplification Effects
The interconnected nature of Latin American financial
markets creates opportunities for threat actors to amplify
the impact of single compromises. This multiplicative
202 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
203 https://digiamericas.org/wp-content/uploads/2024/05/LATAM-CISO-REPORT-2024_.pdf
204 https://blog.talosintelligence.com/breaking-the-silence-recent-truebot-activity/
32

5.1.12 CL0P Tactics, Techniques, & Procedures
| Tactics | Techniques | Procedures |
| ------- | ---------- | ---------- |
Uses phishing and social engineering
| Reconnaissance   | T1592: Gathering Host  |     |
| ---------------- | ---------------------- | --- |
tactics to collect information about
| (TA0043) | Information |     |
| -------- | ----------- | --- |
their targets
Gains access to target’s credentials
|     | T1589.002: Email Addresses | through phishing, social engineering,  |
| --- | -------------------------- | -------------------------------------- |
and IABs
|     | T1589.001: Credentials | To be determined |
| --- | ---------------------- | ---------------- |
Gains access to target’s network
T1590: Gather Victim Network
information through phishing, social
Information
engineering, and IABs
Gains access to target’s network
T1589: Gather Victim Identity
information through phishing, social
Information
engineering
Compromises existing accounts with
Resource Development
|     | T1586: Compromise Accounts | techniques such as phishing, social  |
| --- | -------------------------- | ------------------------------------ |
(TA0042)
engineering and, IABs.
Initial Access   T1133: External Remote-Services  Access to enterprise network through
| (TA0001) | Compromise | compromised user accounts |
| -------- | ---------- | ------------------------- |
Scans for public-facing application
T1190: Exploit Public-Facing
to identify and exploit zero-day
Applications
vulnerabilities
Sends phishing emails to targets to
|     | T1566: Phishing | gain access to their systems and  |
| --- | --------------- | --------------------------------- |
exfiltrate data and credentials
|     | T1091: Replication Through  | Checks for available system drives  |
| --- | --------------------------- | ----------------------------------- |
|     | Removable Media             | (often done to infect USB drives)   |
|     | T1078.003: Local Accounts   | To be determined                    |
Execution
|     | T1059.001: PowerShell  | To be determined |
| --- | ---------------------- | ---------------- |
(TA0002)
T1059.003: Windows Command
To be determined
Shell
|     | T1047: Windows Management  | Queries BIOS Information (via WMI,  |
| --- | -------------------------- | ----------------------------------- |
|     | Instrumentation            | Win32_Bios)                         |
|     | T1106: Native API          | To be determined                    |
|     | T1053.003: Cron            | To be determined                    |
|     | T1053.005: Scheduled Task  | To be determined                    |
|     | T204.002: Malicious File   | To be determined                    |
Uses compromised accounts to
| Persistence   |     | escalate administrator privileges or  |
| ------------- | --- | ------------------------------------- |
T1098: Account Manipulation
| (TA0003)  |     | create new accounts with admin  |
| --------- | --- | ------------------------------- |
privilege
|     | T1574.001: Registry Run/ Startup  | Stores files to the Windows startup  |
| --- | --------------------------------- | ------------------------------------ |
|     | Folder                            | directory                            |
|     | T1037.004: RC Scripts             | To be determined                     |
33

| Tactics | Techniques | Procedures |
| ------- | ---------- | ---------- |
Uses compromised accounts to
escalate to administrator privileges
T1136: Create Account
or create new accounts with admin
privilege
|     | T1543.002: Systemd Service        | To be determined              |
| --- | --------------------------------- | ----------------------------- |
|     | T1133: External Remote Services   | To be determined              |
|     | T1574.002: DLL Side-Loading       | Attempts to load missing DLLs |
|     | T1053.003: Cron                   | To be determined              |
|     | T1053.005: Scheduled Task         | To be determined              |
|     | T1505: Server Software Component  | To be determined              |
|     | T1505.001: SQL Stored Procedure   | To be determined              |
|     | T1505.003: Web Shell              | To be determined              |
Uses compromised accounts to
escalate to administrator privileges
T1078: Valid Accounts
or create new accounts with admin
privilege
Uses compromised accounts to
escalate to administrator privileges
T1078.003: Local Accounts
or create new accounts with admin
privilege
Privilege Escalation   T1548.002: Bypass User Account  Runs malicious code with
| (TA00 04) | Control | administrator privileges  |
| --------- | ------- | ------------------------- |
Uses compromised accounts to
escalate administrator privileges or
T1098: Account Manipulation
create new accounts with admin
privilege
|     | T1574.001: Registry Run/ Startup  | Stores files to the Windows startup  |
| --- | --------------------------------- | ------------------------------------ |
|     | Folder                            | directory                            |
|     | T1037.004: RC Scripts             | To be determined                     |
|     | T1543.002: Systemd Service        | To be determined                     |
Exploits known vulnerabilities in
T1068: Exploitation For Privilege
software or applications to escalate
Escalation
privileges
|     | T1574.002: DLL Side-Loading  | Attempts to load missing DLLs  |
| --- | ---------------------------- | ------------------------------ |
|     | T1053.003: Cron              | To be determined               |
Deletes volume shadow copies to
T1053.005: Scheduled Task
prevent system recovery
Uses compromised accounts to
escalate to administrator privileges
T1078.003: Local Accounts
or create new accounts with admin
privilege
| Defense Evasion   | T1222.002: Linux and Mac file and  |     |
| ----------------- | ---------------------------------- | --- |
To be determined
| (TA0005)  | Directory Permissions Modification |     |
| --------- | ---------------------------------- | --- |
References anti-VM strings targeting
T1497.001: System Checks
Xen
Uses compromised accounts to
escalate to administrator privileges
T1078: Valid Accounts
or create new accounts with admin
privilege
34

| Tactics | Techniques | Procedures |
| ------- | ---------- | ---------- |
Uses compromised accounts to
escalate to administrator privileges
T1078.003: Local Accounts
or create new accounts with admin
privilege
|     | T1218.007: Msiexec       | To be determined |
| --- | ------------------------ | ---------------- |
|     | T1218.010: Regsvr32      | To be determined |
|     | T1218.011: Rundll32      | To be determined |
|     | T1553.002: Code Signing  | To be determined |
Uses registry keys to establish
|     | T1112: Modify Registry | persistence and disable security  |
| --- | ---------------------- | --------------------------------- |
systems on infected systems
T1070.002: Clear Linux or Mac
To be determined
System Logs
|     | T1574.002: DLL Side-Loading  | Attempts to load missing DLLs  |
| --- | ---------------------------- | ------------------------------ |
T1140: Deobfuscate/Decode Files or
To be determined
Information
Sample may be VM or debugger-
|     | T1622: Debugger Evasion | aware; queries disk information (often  |
| --- | ----------------------- | --------------------------------------- |
used to detect virtual machines)
|     | T1548.002: Bypass User Account  | Runs malicious code with  |
| --- | ------------------------------- | ------------------------- |
|     | Control                         | administrator privileges  |
Credential Access
|     | T1003.001: LSASS Memory  | To be determined |
| --- | ------------------------ | ---------------- |
(TA0006)
|     | T1552.007: Container API  | To be determined |
| --- | ------------------------- | ---------------- |
Sample may be VM or debugger-
Discovery (TA0007)  T1622: Debugger Evasion aware; queries disk information (often
used to detect virtual machines)
Enumerates the file system, reads INI
files, enumerates files on Windows,
T1083: File and Directory Discovery
enumerates files recursively, and
acquires file size
|     | T1135: Network Share Discovery  | Enumerates network shares  |
| --- | ------------------------------- | -------------------------- |
Queries a list of all running processes
T1057: Process Discovery
and enumerates processes
Queries or enumerates registry value
|     | T1012: Query Registry | and queries or enumerates registry  |
| --- | --------------------- | ----------------------------------- |
key
Queries BIOS information (via
WMI, Win32 Bios), queries the
volume information (name, serial
T1082: System Information Discovery
number, etc.) of a device, reads
software policies, and acquires disk
information
|                    | T1497.001: System Checks     | To be determined |
| ------------------ | ---------------------------- | ---------------- |
| Lateral Movement   | T1021.002 SMB/Windows Admin  |                  |
To be determined
| (TA0008) | Shares         |                  |
| -------- | -------------- | ---------------- |
|          | T1021.002 SSH  | To be determined |
T1021.006 Windows Remote
To be determined
Management
35

| Tactics | Techniques                  | Procedures                          |
| ------- | --------------------------- | ----------------------------------- |
|         | T1091: Replication Through  | Checks for available system drives  |
|         | Removable Media             | (often done to infect USB drives)   |
T1021.001: Remote Desktop
To be determined
Protocol
Collection
|     | T1005: Data from Local System  | Collects disk information |
| --- | ------------------------------ | ------------------------- |
(TA0009)
Uses application layer protocol to
Command and Control (C2)
|     | T1071.001: Web Protocols | download malware and encryption  |
| --- | ------------------------ | -------------------------------- |
(TA0011)
keys
T1573.001: Symmetric Cryptography
|     | T1105: Ingress Tool Transfer  | To be determined |
| --- | ----------------------------- | ---------------- |
|     | T1104: Multi-Stage channels   | To be determined |
|     | T1571: Non-Standard Port      | To be determined |
Establishes connection with C2
Exfiltration
|     | T1041: Exfiltration Over C2 Channel | server over HTTPS to download  |
| --- | ----------------------------------- | ------------------------------ |
(TA0010)
malware and encryption keys
Checks for available system drives
T1052.001: Exfiltration Over USB
(often done to infect USB drives)
T1567.002: Exfiltration to Cloud
To be determined
Storage
Impact
|     | T1485: Data Destruction  | To be determined |
| --- | ------------------------ | ---------------- |
(TA00 40)
|     | T1486: Data Encrypted for Impact  | To be determined |
| --- | --------------------------------- | ---------------- |
|     | T1565: Data Manipulation          | To be determined |
|     | T1496: Resource Hijacking         | To be determined |
|     | T1489: Service Stop               | To be determined |
36

Indicators of Compromise (IoCs):
Hashes:
• 004ba25f40b641a3a276b84ebdc44971
• 00773e87ad74417abaf825839c4dd014
• 00a276d2a09a49b684237013d26a91dc
• 00a60855a14e458896d70c052e22e11c
• 00e815ade8f3ad89a7726da8edd168df13f96ccb6c3daaf995aa9428bfb9ecf
• 010428443d5547a58995767d14d1c785
• 013f0f61bf96431e8a10e3cb982f4af5
• 01a0e1d97f97455a8da6012977169b40
• 01dc7dc6ad774b39a36d13d55d273a52
IP Address:
Internet Domain Name:
• 103.151.172.28
• 4ad.onion • 109.172.45.28
• abcwdl.co.uk • 109.172.45.77
• aclara.com • 141.98.82.201
• adaresec.com • 143.244.188.172
• aha.org • 146.70.116.20
• ajoomal.com • 147.78.47.219
• alektum.com • 147.78.47.231
• alogent.com • 147.78.47.235
• amerisave.com • 147.78.47.241
• amf.se • 157.230.143.100
• androidauthority.com • 158.255.2.244
• antiy.cn • 158.255.2.245
• arrow.com • 158.255.225.25
• awaze.com
• axisbank.com Mentioning the CVEs, etc.:
Malware Signature: • CVE-2021-30116
• CVE-2023-27532
• BlackByte Ransomware • CVE-2023-40044
• IceFire Ransomware • CVE-2023-36884
• Conti Ransomware • CVE-2018-4878
• Akira Ransomware • CVE-2017-0144
• AtomSilo Ransomware • CVE-2017-11882
• Money Message Ransomware • CVE-2022-41040
• Karma Ransomware • CVE-2019-11043
• Snatch • CVE-2023-20269
• AvosLocker Ransomware • CVE-2021-26084
• Black Kingdom Ransomware • CVE-2021-34527
• Monti Ransomware • CVE-2023-3519
• Rorschach • CVE-2019-19781
• CVE-2023-28252
• CVE-2019-15846
• CVE-2021-45105
• CVE-2019-7192
37

5.1.13 CL0P Technical/Tactical Recommendations T1566 (Phishing)
The following tactical recommendations are designed to 1. Deploy advanced email-filtering solutions to
provide technical mitigations to CL0P’s MITRE ATT&CK detect and block phishing attempts: Implement
techniques. The techniques are categorized based on secure email gateways (SEGs) with AI-driven filtering
criticality level, as determined by their potential impact capabilities to analyze email headers, body content,
and risk to business continuity, data security, and and attachments for phishing indicators. Configure
operational resilience. rules to block or flag emails containing suspicious
links, unexpected attachments, or impersonation
Grounded in MITRE’s D3FEND mitigation knowledge attempts. Use threat-intelligence feeds to update
graph, these recommendations outline prescriptive filtering mechanisms against evolving phishing tactics.
instructions, desired outcomes, and key considerations Advanced filtering reduces the likelihood of phishing
for implementation and resource allocation. These emails reaching end users.
recommendations are not meant to be exhaustive but
rather are most suited for mitigating the respective 2. Combine homoglyph detection with user
ATT&CK technique. training to prevent domain-impersonation attacks:
Deploy tools that detect domain similarity to identify
Recommendations for High-Criticality Attack lookalike domains used in phishing campaigns.
Techniques: Implement continuous monitoring for newly registered
domains that mimic internal or trusted domains.
T1190 (Exploit Public-Facing Applications) Conduct regular employee training sessions to
enhance awareness of social-engineering tactics,
1. Deploy and configure web application firewalls domain-manipulation techniques, and suspicious
(WAFs) to filter malicious traffic: Implement WAFs email indicators. Provide hands-on exercises,
to inspect and block exploit attempts targeting web phishing simulations, and real-world examples to
applications, including SQL injection, cross-site reinforce recognition skills. A combined approach of
scripting (XSS), and remote code execution (RCE). automated detection and educated users significantly
Configure rule sets to detect known attack patterns reduces the risk of falling victim to domain spoofing
and anomalous request behaviors. Regularly update and spear-phishing attacks.
WAF policies to address emerging threats and reduce
false positives. WAFs provide an essential layer of 3. Implement anti-spoofing and email-
protection by filtering exploit traffic before it reaches authentication mechanisms to verify sender
the application. legitimacy: Implement a sender policy framework
(SPF) to verify authorized email senders; DomainKeys
2. Segment externally facing services from Identified Mail (DKIM) to ensure message integrity;
internal systems: Use a demilitarized zone (DMZ) and Domain-Based Message Authentication,
or isolated hosting infrastructure to separate public- Reporting, and Conformance (DMARC) to define
facing applications from internal networks. Implement policies for handling unauthorized emails. Enforce
strict firewall rules to control traffic flow between these authentication mechanisms within the
these segments and limit the exposure of sensitive organization and encourage external partners to
resources. Enforce access controls to prevent lateral adopt them. Configure email-security policies to
movement from compromised services. Network reject or quarantine messages that fail authentication
segmentation reduces the attack surface and checks. These measures reduce the risk of email
mitigates the impact of a successful breach. spoofing and phishing-based impersonation attacks.
3. Regularly scan and patch externally facing T1078 (Valid Accounts – Domain Accounts)
applications: Conduct frequent vulnerability scans
on public-facing systems to identify weaknesses 1. Continuously monitor domain accounts
before attackers exploit them. Establish a structured for unauthorized access: Deploy user behavior
patch-management process to apply security analytics (UBA) and anomaly-detection tools to
updates promptly, prioritizing critical vulnerabilities. identify deviations in login patterns, such as unusual
Use automated tools to track software versions and locations, excessive failed attempts, or logins
enforce update policies. Proactive scanning and outside business hours. Configure automated alerts
patching help minimize the risk of exploitation through for suspicious activity and integrate with a security
known vulnerabilities. information and event management (SIEM) platform
for investigation. Proactive monitoring helps detect
compromised accounts before they can be exploited.
38

2. Enforce strong authentication and least- patterns while maintaining detailed logs for forensic
privilege access: Require multi-factor authentication analysis. Consider storage requirements for metadata
(MFA) for all privileged accounts and enforce role- collection and processing overhead for real-time
based access controls (RBAC) to limit account analysis.
permissions. Implement just-in-time (JIT) access
controls for high-privilege accounts to minimize T1003.001 (LSASS Memory Dumping – Credential Theft)
persistent access risks. Regularly review and disable
inactive accounts to reduce potential attack surfaces. 1. Deploy process-monitoring tools that
These measures limit adversaries’ ability to exploit specifically track spawn attempts targeting local
valid credentials for lateral movement. security authority subsystem service (LSASS)
memory space and related system processes:
3. Regularly review and manage domain accounts: Configure the detailed logging of process attributes
Conduct periodic audits of domain accounts to (e.g., user context, image path, and security content)
ensure only active and necessary accounts exist. for all process-creation events. Implement automated
Implement automated lifecycle management for alerts for any unauthorized process-spawn attempts
account creation, modification, and deactivation targeting LSASS while maintaining whitelists for
based on user roles and employment status. Enforce legitimate security tools. Consider the processing
strict offboarding procedures to immediately disable overhead of continuous process monitoring and
accounts when employees leave the organization. storage requirements for process-creation logs.
Reducing unnecessary accounts helps prevent
adversaries from leveraging dormant credentials. 2. Implement hardware-based isolation
mechanisms using technologies such as IOMMU
T1041 (Exfiltration Over C2 Channel) to prevent unauthorized memory access between
processes: Configure strict memory-access controls
1. Deploy both inbound and outbound traffic that prevent direct memory access to LSASS process
filtering at network boundaries, enforcing strict space from unauthorized sources. Deploy monitoring
egress controls to known-good destinations and solutions to track any attempted violation of process
protocols: Implement application-layer filtering to isolation boundaries while maintaining business
allow only authorized data-transfer protocols and continuity for legitimate authentication processes.
block commonly abused services. Configure filtering Consider the hardware requirements and potential
rules to segment different business units, especially performance impact on system resources.
those handling sensitive financial data, while
maintaining logs of all blocked connection attempts. 3. Configure automated process-termination
Consider performance impact on legitimate business responses for any unauthorized processes
traffic and allocate sufficient resources for real-time attempting to access LSASS memory space:
filtering without introducing latency. Implement proper access controls and permissions
for process-termination capabilities while ensuring
2. Establish baseline profiles of normal client– legitimate security tools remain functional. Set up
server communication patterns specific to logging and alerting for all process-termination events
financial services applications and data flows: with detailed context about the terminated process
Deploy monitoring solutions that can analyze payload and reason for termination. Consider the potential
characteristics (e.g., size, frequency, and entropy) impact of false positives and establish clear escalation
across all client–server communications. Configure procedures for security teams.
automated alerts for any statistical deviations that
could indicate data-exfiltration attempts while Recommendations for Moderate- to High-Risk
maintaining historical profiles for trend analysis. Attack Techniques:
Consider the computational resources required for
real-time profiling and the potential impact on system T1059.001 (PowerShell Execution)
performance.
1. Set PowerShell execution policy to only allow
3. Implement comprehensive protocol metadata signed scripts: Configure PowerShell to allow only
collection and analysis focusing on session signed scripts to run, preventing the execution of
characteristics, timing patterns, and protocol- untrusted or malicious scripts. Restrict PowerShell
specific attributes: Deploy real-time analysis usage to administrators to limit the attack surface.
capabilities that can identify statistical outliers in Doing so reduces the likelihood of malicious
protocol usage, particularly protocols that could PowerShell-based attacks.
be used for data exfiltration. Set up adaptive
thresholding based on historical protocol usage
39

2. Disable/restrict the Windows Remote T1021.001 (Remote Desktop Protocol)
Management (WinRM) Service to prevent remote
execution: Disable or limit access to the WinRM 1. Restrict and monitor remote desktop protocol
service to prevent attackers from executing PowerShell (RDP) access: Limit RDP access by enforcing network
remotely. Use firewall rules to restrict WinRM access to segmentation and firewall rules that block unnecessary
trusted hosts only. Doing so prevents unauthorized use external connections. Require VPN or zero-trust network
of PowerShell for remote command execution. access for remote desktop usage and enforce MFA
for all RDP sessions. Implement strict access controls
3. Use PowerShell Constrained Language Mode and using allowlists for authorized IP addresses. These
application control: Enable PowerShell Constrained restrictions reduce exposure to brute-force attacks and
Language Mode to restrict access to sensitive unauthorized access attempts.
functionality, such as executing arbitrary Windows APIs.
Utilize application whitelisting tools to control which 2. Detecting and analyzing abnormal RDP activity:
applications and scripts can run, reducing the potential Deploy network monitoring tools to analyze RDP
for abuse. Doing so mitigates the risk of PowerShell session patterns, geolocation inconsistencies, and
being leveraged for malicious activities. excessive failed login attempts. Use host and network-
based anomaly detection to identify suspicious behavior,
T1068 (Exploitation for Privilege Escalation) such as unexpected administrative logins or persistent
connections. Implement alerting mechanisms for
1. Regularly assess and remediate system unusual RDP activity to enable rapid investigation and
vulnerabilities: Perform routine vulnerability scans and response. Monitoring reduces dwell time and helps
manual security assessments to identify and mitigate identify potential intrusions.
system weaknesses. Implement a structured patch-
management process to address critical security flaws 3. Audit and control remote-access tools: Maintain a
before exploitation. Use configuration-management strict inventory of approved remote-access applications
tools to enforce security baselines and harden and prohibit the use of unauthorized tools through
guidelines. Regular assessments help reduce the attack application whitelisting. Regularly audit endpoint and
surface and ensure compliance with security policies. network logs for indicators of unauthorized remote-
access attempts. Enforce execution-control policies to
2. Restrict unnecessary services and enforce least prevent unapproved portable remote-access software
privilege: Disable non-essential system services from running. Doing so ensures only sanctioned remote
and restrict administrative-tool usage to minimize management tools are used, reducing the risk of
potential attack vectors. Implement RBAC and privilege compromise.
management solutions to enforce the least-privilege
principle. Regularly review user permissions and remove T1021.002 (SMB/Windows Admin Shares)
excessive access rights to reduce lateral movement
opportunities. These measures significantly lower the 1. Filter and monitor SMB network traffic to detect
risk of privilege escalation. unauthorized access: Apply network segmentation and
firewall rules to restrict SMB traffic to only authorized
3. Deploy exploit detection and mitigation controls: systems. Monitor SMB authentication logs and detect
Enable security mechanisms such as kernel-integrity anomalous access patterns, such as unexpected
verification, exploit-protection frameworks, and memory- connections or excessive failed login attempts.
based attack prevention. Utilize endpoint detection Analyzing traffic helps prevent unauthorized access and
and response (EDR) solutions to monitor for behavioral data exfiltration over SMB.
indicators of privilege-escalation attempts. Configure
logging and alerting to detect and respond to suspicious 2. Deny remote use of local admin credentials to log
process injections or unauthorized modifications. into systems: Restrict the use of local administrator
These techniques enhance system resilience against accounts for remote logins by enforcing Group Policy
exploitation attempts. settings and implementing the Local Administrator
Password Solution (LAPS). Ensure that unique and
complex passwords are used for each system’s local
administrator account. Preventing credential reuse
reduces the risk of lateral movement if an account is
compromised.
40

3. Monitor for remote execution attempts using should use behavioral analytics to identify patterns
WMI and SMB shares: Deploy endpoint monitoring indicative of UAC bypass techniques. Early detection
to detect the use of WMI’s Win32_Process class of unauthorized privilege-elevation attempts allows for
and the creation of remote processes through SMB. timely response and mitigation.
Correlate activity with known attack techniques to
identify potential lateral movement or remote code- 3. Implement executable denylisting to prevent
execution attempts. Early detection of abnormal unauthorized privilege escalation: Use application-
behavior helps prevent unauthorized system control policies to block the execution of untrusted
compromise. administrative utilities
T1574.002 (DLL Side-Loading) commonly abused for UAC bypass. Maintain an up-to-
date denylist of known bypass techniques to proactively
1. Enforce strict application controls to prevent mitigate threats. Enforce strict execution policies using
unauthorized dynamic link library (DLL) execution: operating-system security controls to block non-
Use application whitelisting to allow only trusted administrative users from executing high-risk binaries.
applications and libraries to execute. Implement Preventing the execution of malicious or unapproved
code-signing verification to prevent the execution applications reduces the attack surface and strengthens
of unsigned or tampered DLLs. Restricting DLL endpoint security.
execution ensures adversaries cannot exploit weak
application controls for persistence. T1133 (External Remote Services)
2. Regularly update software to patch DLL 1. Implement automated session-termination
side-loading vulnerabilities: Maintain an effective controls for all external remote services including
patch-management process to address known DLL VPN and remote management tools with strict
side-loading risks. Review application dependencies timeout parameters: Configure forced session
and remove or replace vulnerable libraries with secure disconnection after a period of inactivity while
versions. Keeping software updated reduces the maintaining detailed logs of all termination events
risk of adversaries exploiting outdated DLL loading for audit purposes. Ensure that session-termination
mechanisms. policies account for legitimate business needs
while preventing unauthorized persistence through
3. Enable behavioral-based detections to identify abandoned sessions. Consider the impact on user
DLL side-loading techniques: Use EDR capabilities productivity and establish clear communication
to detect anomalies such as a process-loading DLL channels for users who require extended sessions.
from non-standard directories, unexpected DLL
injection into high-privilege applications, or abnormal 2. Implement network segmentation using proxies,
memory-access patterns. Implement heuristic and gateways, and firewalls to control and monitor
machine-learning-based detections to flag deviations all remote-access paths into the network: Deploy
from normal DLL loading behavior. a defense-in-depth approach that forces all remote
connections through designated security checkpoints
T1548.002 (Bypass User Account Control)
while maintaining detailed access logs. Configure
1. Harden User Account Control (UAC) settings strict boundary controls that prevent direct remote
and monitor for bypass attempts: Enable UAC in access to internal systems while ensuring business
“Always Notify” mode to require explicit approval for continuity through properly secured access
administrative actions. Conduct regular assessments channels. Consider the complexity of implementing
to identify systems with weak UAC configurations segmentation and the potential impact on network
and enforce security best practices. Disabling auto- performance and legitimate remote-access needs.
elevation prevents attackers from leveraging system
utilities to bypass UAC controls. Strengthening 3. Deploy MFA for all external remote service
UAC configurations reduces the attack surface and accounts including VPN and remote management
minimizes unauthorized privilege-escalation attempts. tools: Implement a robust MFA solution that
combines multiple authentication factors while being
2. Monitor process execution for suspicious UAC aware of potential MFA interception techniques.
bypass attempts: Track the execution of known Configure the detailed logging of all authentication
UAC bypass tools and processes, such as eventvwr. attempts while maintaining proper procedures for
exe and sdclt.exe, that can elevate privileges without handling legitimate MFA issues or lockouts. Consider
user consent. Implement endpoint-detection rules to the user-experience impact, support-resource
correlate process execution with privilege-escalation requirements, and the need for backup authentication
events and flag anomalous behavior. Organizations methods for critical access scenarios.
41

Stealth and Persistence Risk (Evasion & Long-Term to notify security teams when unauthorized log
Compromise): tampering is detected. Correlate log events across
multiple sources to identify patterns of malicious
T1140: (Deobfuscate/Decode Files or Information) activity. Continuous monitoring helps detect and
mitigate threats before they escalate.
1. Monitor and log process execution to detect
file extraction or decryption attempts: Implement T1574.00: (Registry Run/Startup Folder)
process monitoring to detect the execution of file-
extraction utilities and scripts attempting to decrypt or 1. Deploy file integrity monitoring focused on
manipulate files. Correlate activity with unauthorized Windows Registry run keys and startup folder
file modifications or unexpected system behavior to location with real-time/near real-time alerting for
identify potential malicious activity while reducing modifications: Implement baseline comparisons
false positives. that track any changes to autostart locations while
maintaining detailed audit logs of all modifications.
2. Restrict and validate script execution to prevent Configure whitelisting for known good startup
unauthorized decoding attempts: Configure entries while ensuring proper change-management
logging to capture script executions, especially procedures for legitimate modifications. Consider the
those occurring outside of standard administrative performance impact on continuous monitoring and
tasks. Restrict unauthorized script execution and storage requirements for audit logs.
analyze captured scripts for potential malicious intent.
Monitoring script activity helps identify adversary 2. Implement strict application-allowlisting
attempts to automate obfuscation or payload controls that prevent unauthorized executables
decoding. from being added to startup locations or run keys:
Configure policies that only permit trusted/signed
3. Detect and block misuse of built-in utilities applications to continue through startup procedures
commonly used for deobfuscation: Monitor the while maintaining a comprehensive inventory of
usage of built-in system utilities that can be leveraged approved applications. Set up automated alerts
for decoding, extracting, or modifying files. Set up
alerts for unauthorized or unexpected executions and for any attempted violations of allowlisting policies
correlate them with system activity. Detecting the while ensuring business continuity for legitimate
misuse of such utilities early can prevent unauthorized software updates. Consider the administrative
data access and the execution of malicious code. overhead of maintaining allowlists and the impact on
software deployment processes.
T1070.002: (Clear Linux or Mac System Logs)
3. Deploy continuous monitoring of system-
1. Encrypt and centralize log storage: Use strong initialization configurations related to the
encryption protocols to protect system logs at rest registry and startup folder: Implement analysis
and in transit, preventing unauthorized modifications. capabilities that can detect anomalous changes to
Implement centralized logging solutions that forward startup configurations while maintaining baselines
logs to secure remote storage with integrity- of legitimate startup entries. Configure automated
verification mechanisms, such as cryptographic responses to unauthorized configuration changes.
hashing. Encrypted and centralized logs ensure
forensic integrity and prevent attackers from T1078.003: (Local Accounts – Persistence)
tampering with evidence.
1. Monitor local-account creation, modification,
2. Enforce strict log access controls: Apply and usage patterns across all systems: Deploying
granular file permissions to restrict log modification real-time alerting for suspicious local-account
and deletion rights to authorized system processes activities can help detect potential malicious activity
and administrators. Implement mandatory access associated with off-hours usage, unauthorized
control (MAC) frameworks to enforce security policies privilege escalation, or unusual access patterns.
at the operating-system level. Regularly audit log Configure detailed logging of all local account
access permissions to identify and mitigate potential operations while maintaining baselines of normal
privilege abuse. These controls help prevent attackers account behavior. Consider the storage requirements
from erasing forensic evidence. for account activity logs and processing overhead for
real-time analysis.
3. Monitor and alert on log-tampering attempts:
Configure security monitoring tools to track log-file
modifications, deletions, and unexpected clearing
activities. Implement real-time alerting mechanisms
42

2. Deploy automated account locking triggered 5.2 LockBit
by suspicious activities or policy violations on
local accounts: Implement progressive lockout 5.2.1 Relevant Threat-Actor Activity
policies that increase lockout duration with repeated
violations while maintaining proper procedures for LockBit is a highly active ransomware group primarily
legitimate account unlocking. Configure notifications targeting medium-to-large-sized businesses, including
for security teams when accounts are locked due to Royal Mail, Ion Group, and TSMC.205 The group gains
suspicious activity while ensuring business continuity initial access to target networks through purchased
through proper backup access procedures for critical access, unpatched vulnerabilities, insider access, and
services. While lockout mechanisms may evict threat zero-day exploits. LockBit is designed to operate in the
actors, consider the impact on legitimate users and United States, Canada, Europe, Asia, and Latin America.
help-desk resource protocols for secure account In late February of 2024, LockBit underwent a significant
unlocking requests. takedown in which over 200 cryptocurrency accounts
were frozen, sanctions were enforced, and 34 servers
3. Implement strict permission controls and and 14,000 accounts were shut down.206 Since then, this
access restrictions for all local accounts based takedown has significantly disrupted LockBit’s activities.
on the principle of least privilege (PoLP): Configure However, despite substantial law enforcement, LockBit
regular permission reviews and automated detection remains the most prominent ransomware organization.207
of unauthorized privilege changes while maintaining
detailed documentation of approved access
levels. Establish alerts for any attempts to modify
account permissions while ensuring proper change-
management procedures for legitimate permission
updates. Consider the administrative overhead of
managing granular permissions and the impact on
operational efficiency.
Figure 6: Lifecycle of a Ransomware Incident
Source: CISA208
205 https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware spotlight-lockbit
206 https://globalinitiative.net/analysis/the-lockbit-takedown law-enforcement-trolls-ransomware-gang/
207 https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
208 https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
43

LockBit operates as a RaaS model, recruiting affiliates 5.2.3 Correlation
to execute ransomware attacks using LockBit tools
and infrastructure. This results in significant variation LockBit attacks often use a double-extortion strategy
in TTPs across different attacks.209 A standard method to pressure victims into paying, first to recover access
used by LockBit affiliates involves exploiting unpatched to their encrypted files and second to stop their stolen
vulnerabilities or using compromised credentials to gain data from being publicly released. This double-extortion
initial access to a target network. Once inside, they often technique, in particular, allows LockBit to not only profit
deploy tools like Mimikatz to extract credentials and from the data ransom but also recover data from the
escalate privileges, allowing lateral movement across user’s end and potentially even utilize additional data
the network. Data can be reached and compromised leakage if the victim does not comply.
through these methods, allowing for data exfiltration or
encryption. LockBit and CL0P operate as RaaS, using affiliates or
initial access brokers (IABs) to deploy the initial malware
The impact of LockBit has been profound, particularly or secure access to a target organization's systems.
in Latin America financial institutions, leading to Like LockBit, CL0P has gained notoriety for its large-
significant disruptions and financial losses. It was scale attacks, such as exploiting zero-day vulnerabilities
reported that RaaS groups, including LockBit, have in widely used software such as MOVEit. Moreover,
exerted continuous pressure on the region's economic- both groups use techniques like DLL side-loading and
and government-services sectors.210 Since April 2022, advanced persistence mechanisms to maintain control
countries such as Costa Rica, Peru, Mexico, Ecuador, of compromised systems.
Brazil, and Argentina have faced ransomware attacks,
likely involving Russian-speaking threat actors, including 5.2.4 LockBit Techniques, Tactics, & Procedures
LockBit.211
LockBit employs sophisticated TTPs to compromise
5.2.2 Background and control victim networks. For privilege escalation,
LockBit uses methods such as bypassing User Account
Lockbit was first observed in September 2019 and Control (UAC) via the ucmDccwCOM Method from
has evolved through multiple versions, with the current UACMe, exploiting boot or login autostart execution and
version, LockBit 3.0, discovered in June 2022. LockBit modifying domain policies through Group Policy to allow
maintained the top position throughout 2022, accounting its control over systems.
for over a third of victim organizations in the first three
quarters.212 Lockbit maintains a strong presence in Latin Additionally, it employs token impersonation to replicate
America. In October 2022, ransomware occurred in a and assume the privileges of other processes, causing
bank in Brazil using the LockBit malware. The attackers deeper network infiltration. LockBit also exploits zero-
requested 50 bitcoins—the equivalent of 1 million USD— day and n-day vulnerabilities to gain unauthorized
and caused data leakage and temporary disruptions in access and execute remote code, with notable cases
client services. including the exploitation of the Fortra GoAnywhere MFT
Vulnerability (CVE-2023-0669) and the Apache Log4j2
In addition to this incident, LockBit's victims span Vulnerability.
various sectors. Among the most significant is the
private sector, where LockBit has targeted industries LockBit utilizes tools such as Splashtop for remote
ranging from finance to manufacturing.213 The group access and Cobalt Strike for navigating networks in
has also impacted other critical-infrastructure sectors, lateral movement. By targeting SMB shares and utilizing
such as energy, healthcare, and transportation.214 Admin Shares or Domain Group Policy, LockBit affiliates
Furthermore, governmental entities have been affected, achieve seamless movement across compromised
leading to national crises, as seen in the case of Costa environments.
Rica.215 These industries are particularly appealing to
LockBit due to their high importance, data sensitivity,
and potential to create national crises. Their substantial
financial resources also make them lucrative targets,
increasing the likelihood of ransom payments.
209 https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
210 https://doi.org/102279083/1729705714101/module_128102279083_Global-Header
211 https://www.recordedfuture.com/research/latin-american-governments targeted-by-ransomware
212 https://global.ptsecurity.com/analytics/latam-cybersecurity-threatscape-2022-2023
213 https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
https://www.logpoint.com/wp-content/uploads/2023/07/etp-lockbit.pdf
214 https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
215 https://www.recordedfuture.com/research/latin-american-governments targeted-by-ransomware
44

For command and control, the ransomware group relies on various protocols and software, including FileZilla for file
transfers, ThunderShell for HTTP-based remote access, and Ligolo for creating secure SOCKS5 tunnels. Tools such
as Plink automate SSH activities, while commonly used in remote-access software like AnyDesk and TeamViewer,
further facilitate LockBit’s ability to maintain access to infected systems. The following table, representing LockBit’s
tactics, techniques, and procedures, showcase LockBit’s flexible operation and persistence, posing a severe threat to
cybersecurity across various sectors, particularly in LATAM.216
| Tactics | Techniques | Procedures |
| ------- | ---------- | ---------- |
Abuses Windows command prompt
Execution
|     | T1059.003: Windows Command Shell  | to access almost any part of the  |
| --- | --------------------------------- | --------------------------------- |
(TA0002)
system
Leverages system services to execute
|     | T1072: Software Development Tools | or launch malicious code as a  |
| --- | --------------------------------- | ------------------------------ |
persistence mechanism
Uses PsExec to execute commands
T1569.002: System Services
or payloads
Persistence  T1547: Boot or Logon Autostart  Enables automatic logon for
| (TA0003) | Execution | persistence |
| -------- | --------- | ----------- |
Uses compromised user accounts
|     | T1078: Valid Accounts  | to maintain persistence on the target  |
| --- | ---------------------- | -------------------------------------- |
network
LockBit affiliates gain access through
Initial Access
|     | T1189: Drive-By Compromise  | a user visiting a compromised  |
| --- | --------------------------- | ------------------------------ |
(TA0001)
website
|     | T1190: Exploit Public-Facing  | Exploits vulnerabilities (e.g., Log4Shell)  |
| --- | ----------------------------- | ------------------------------------------- |
|     | Application                   | in internet-facing systems                  |
Exploits RDP to gain access to victims’
T1133: External Remote Services
networks
Uses phishing and spear-phishing to
T1566: Phishing
gain network access
Uses User Account Control
| Privilege Escalation   | T1548: Abuse Elevation Control  |     |
| ---------------------- | ------------------------------- | --- |
(UAC) bypass techniques (e.g.,
| (TA0004) | Mechanism |     |
| -------- | --------- | --- |
ucmDccwCOM method)
|     | T1547: Boot or Logon Autostart  | Enable automatic logon for privilege  |
| --- | ------------------------------- | ------------------------------------- |
|     | Execution                       | escalation                            |
T1484.001: Domain Policy
Modifies Group Policy for lateral
Modification: Group Policy
movement.
Modification
Uses compromised user accounts to
T1078: Valid Accounts
escalate privileges
Decrypts or continues execution only
| Defense Evasion   | T1480.001: Execution Guardrails:  |     |
| ----------------- | --------------------------------- | --- |
if certain environmental factors are
| (TA0005) | Environmental Keying |     |
| -------- | -------------------- | --- |
present
|     | T1562.001: Impair Defenses: Disable  | Disables EDR tools (e.g., using      |
| --- | ------------------------------------ | ------------------------------------ |
|     | or Modify Tools                      | Backstab, Process Hacker, etc.)      |
|     | T1070.001: Indicator Removal: Clear  | Clears Windows Event Log files to    |
|     | Windows Event Logs                   | avoid detection                      |
|     | T1070.004: Indicator Removal: File   | LockBit 3.0 deletes itself from the  |
|     | Deletion                             | disk after execution                 |
216 https://www.logpoint.com/wp-content/uploads/2023/07/etp-lockbit.pdf
45

| Tactics | Techniques | Procedures |
| ------- | ---------- | ---------- |
Encrypts or obfuscates host and bot
T1027: Obfuscated Files or
information during communication
Information
with C2 servers
|                     | T1027.002: Obfuscated Files or  | Uses software packing or virtual   |
| ------------------- | ------------------------------- | ---------------------------------- |
|                     | Information: Software Packing   | machine protection to conceal code |
| Credential Access   |                                 | Uses brute force VPN or RDP        |
T1110: Brute Force
| (TA0006) |     | credentials for initial access |
| -------- | --- | ------------------------------ |
T1555.003: Credentials from
Recovers stored credentials from
Password Stores: Credentials from
Firefox using PasswordFox
Web Browsers
Uses tools like ExtPassword or
|     | T1003: OS Credential Dumping  | LostMyPassword to recover system  |
| --- | ----------------------------- | --------------------------------- |
credentials
Uses Microsoft Sysinternals ProDump
T1003.001: OS Credential Dumping:
or Mimikatz to dump credentials from
LSASS Memory
LSASS
Uses SoftPerfect Network Scanner,
Discovery
|     | T1046: Network Service Discovery  | Advanced IP Scanner, or Advanced  |
| --- | --------------------------------- | --------------------------------- |
(TA0007)
Port Scanner to scan victim networks
Enumerates system information,
|     | T1082: System Information Discovery  | including hostname, configuration,  |
| --- | ------------------------------------ | ----------------------------------- |
and domain information
|     | T1614.001: System Location  | LockBit 3.0 avoids infecting systems   |
| --- | --------------------------- | -------------------------------------- |
|     | Discovery: System Language  | with specific language settings based  |
|     | Discovery                   | on an exclusion list                   |
Uses Splashtop or similar remote
| Lateral Movement   | T1021.001: Remote Services:  |     |
| ------------------ | ---------------------------- | --- |
desktop software to facilitate lateral
| (TA0008) | Remote Desktop Protocol. |     |
| -------- | ------------------------ | --- |
movement
T1021.002: Remote Services:
Uses Cobalt Strike to target SMB
Server Message Block (SMB)/Admin
shares for lateral movement
Windows Shares
Collection   T1560.001: Archive Collected Data:  Uses 7-zip to compress or encrypt
| (TA0009) | Archive via Utility | data before exfiltration |
| -------- | ------------------- | ------------------------ |
Command and Control   T1071.002: Application Layer  Uses FileZilla to communicate with
| (TA0011) | Protocol: File Transfer Protocols | C2                                |
| -------- | --------------------------------- | --------------------------------- |
|          | T1071.001: Application Layer      | Uses ThunderShell to communicate  |
|          | Protocol: Web Protocols           | via HTTP requests                 |
Uses Ligolo to establish SOCKS5
T1095: Non-Application Layer
or TCP tunnels from reverse
Protocol
connections
Uses PuTTY Link (Plink) to automate
T1572: Protocol Tunneling
SSH actions on Windows
Uses AnyDesk, Atera RMM,
|     | T1219: Remote-Access Software  | ScreenConnect, or TeamViewer for  |
| --- | ------------------------------ | --------------------------------- |
remote access
| Exfiltration   |     | Uses publicly available file-sharing  |
| -------------- | --- | ------------------------------------- |
T1567: Exfiltration Over Web Service
| (TA0010) |     | services to exfiltrate data |
| -------- | --- | --------------------------- |
Uses tools like Rclone or
T1567.002: Exfiltration Over Web
FreeFileSync to exfiltrate data to
Service: Exfiltration to Cloud Storage
cloud storage (e.g., MEGA)
46

Tactics Techniques Procedures
Deletes log files and empties the
Impact
T1485: Data Destruction recycle bin to prevent recovery of
(TA0040)
information
Encrypts data on target systems
T1486: Data Encrypted for Impact to disrupt availability of network
resources
T1491.001: Defacement: Internal Changes the system’s wallpaper and
Defacement icons to LockBit branding
Deletes volume shadow copies to
T1490: Inhibit System Recovery
prevent system recovery
Terminates processes and services
T1489: Service Stop to facilitate encryption and prevent
recovery
IOCs:
• File hashes
• IP addresses
• Domain names
• Malicious URLs
• Ransom notes
CVEs:
• Proxy Shell: CVE-2021-34473, CVE-2021-34523, CVE-2021-31207
• Paper Cut: CVE-2023-27350
• Citrix Bleed: CVE-2023-4966 (Latest)
• CVE-2022-22279
• CVE-2021-31207, CVE-2023-4966
• CVE-2021-22986
• CVE-2018-13379
• CVE-2021-36942
• CVE-2021-20028
• CVE-2020-0787
• CVE-2022-36537
47

5.2.5 LockBit Technical/Tactical Recommendations and complexity requirements, and implement
password managers to reduce credential reuse.
Recommendations for Critical-Attack Techniques with Regularly rotate credentials and disable inactive
High Impact on Business & Data Security accounts to prevent unauthorized access.
The tactical recommendations below are designed to 3. Detect and respond to unauthorized account
mitigate LockBit’s techniques, following the MITRE use: Monitor account activity using SIEM and user
ATT&CK framework. They are categorized based on and entity behavior analytics (UEBA) solutions. Flag
the extent of their impact, with higher criticality levels anomalous behavior, including access from new
indicating a greater risk, such as a potential network locations, excessive login attempts, or privilege
takeover. Therefore, these recommendations outline key escalation. Enable automated alerts and implement
considerations and actions that can be taken to mitigate real-time response mechanisms to detect and contain
the associated ATT&CK techniques. potential account compromises.
T1133 (External Remote Services) T1566 (Phishing)
1. Enforce multi-factor authentication (MFA) for 1. Implement advanced email security and
all remote access: Require MFA and cloud-based filtering: Deploy secure email gateways (SEGs) and
remote access to prevent unauthorized logins, even if advanced phishing-protection solutions to filter out
credentials are compromised. Use phishing-resistant malicious emails before they reach users. Enable
authentication methods, such as FIDO2 or certificate- domain-based email-authentication protocols,
based authentication. MFA significantly reduces the such as SPF, DKIM, and DMARC, to prevent email
risk of unauthorized access. spoofing. Use AI-driven threat detection to identify
and quarantine phishing attempts in real time.
2. Restrict remote access with network
segmentation and allowlisting: Limit remote 2. Conduct continuous user-awareness training
access to approved IP ranges and enforce network and simulated phishing tests: Educate employees
segmentation to isolate remote services from critical on recognizing phishing attempts, including
financial systems. Use Zero Trust Network Access social-engineering tactics, malicious attachments,
(ZTNA) and role-based access controls (RBAC) to and deceptive links. Regularly conduct phishing
minimize exposure. Restricting access reduces the simulations to test user awareness and provide
attack surface and limits lateral movement. targeted training based on performance. Reinforce
a culture of cybersecurity vigilance to reduce the
3. Monitor and log remote-access sessions likelihood of successful phishing attacks.
for anomalies: Deploy security information and
event management (SIEM) solutions to log and 3. Deploy anti-phishing browser protections
analyze remote-access sessions. Enable behavior- and URL analysis: Use web filtering and domain
based anomaly detection to flag unusual login reputation services to block access to known
attempts, such as off-hours access or logins from phishing sites. Implement browser isolation for high-
new locations. Real-time monitoring facilitates the risk users and automatically scan URLs in emails
detection of and response to unauthorized access. for malicious indicators before allowing access.
Encourage the use of password managers to prevent
T1078 (Valid Accounts) credential harvesting by auto-filling only on legitimate
sites.
1. Enforce least-privilege and account
segmentation: Limit account permissions based T1003 (OS Credential Dumping)
on the principle of least privilege (PoLP). Implement
separate accounts for administrative and non- 1. Implement credential-protection mechanisms
administrative tasks to reduce exposure. Use just-in- to prevent unauthorized access to stored
time (JIT) access provisioning and RBAC to minimize credentials: Configure Windows Defender Credential
persistent high-privilege access. Restricting access Guard to protect LSASS memory and prevent
helps mitigate the risk of account misuse. credential-dumping attacks. Use EDR solutions
to detect suspicious access attempts targeting
2. Strengthen authentication and credential credential stores. Disable unnecessary administrative
security: Require MFA for all privileged and sensitive privileges to limit exposure to credential-dumping
accounts, prioritizing phishing-resistant methods, techniques. These protections help prevent attackers
such as FIDO2 or certificate-based authentication. from extracting stored credentials.
Enforce strong password policies, including length
48

2. Restrict access to sensitive system processes T1567.002 (Exfiltration Over Web Service: Exfiltration to
and enforce process auditing: Configure endpoint Cloud Storage)
security solutions to monitor and block unauthorized
access to LSASS and registry hives containing 1. Implement Data Loss Prevention (DLP)
stored credentials. Implement process auditing to log solutions to monitor and restrict unauthorized
and alert on attempts to access credential stores. data transfers: Deploy DLP solutions to monitor, log,
Regularly review security logs and conduct forensic and block unauthorized data transfers to external
analysis on suspicious events. Monitoring process cloud storage services such as Google Drive,
interactions helps detect and prevent credential- Dropbox, and OneDrive. Configure policies to detect
dumping attempts. anomalous data movement and enforce automatic
encryption of sensitive financial data before transfer.
3. Deploy strong credential encryption and DLP solutions help prevent unauthorized exfiltration of
minimize credential storage: Use strong encryption sensitive banking data.
standards for credential storage and enforce security
best practices for managing secrets. Implement JIT 2. Monitor and restrict access to cloud storage
privilege escalation to reduce persistent access to services from financial institution networks:
high-value accounts. Minimize password caching on Implement firewall and proxy controls to restrict
endpoints to limit credential exposure. Strengthening access to unauthorized cloud storage platforms.
credential storage reduces the risk of successful Use Secure Access Service Edge (SASE) solutions
credential-dumping attacks. to enforce content filtering and detect suspicious
data uploads. Configure alerts for high-volume data
T1486 (Data Encrypted for Impact – Ransomware) transfers and unusual access patterns indicative of
exfiltration attempts. Restricting access to external
1. Deploy robust endpoint protection and storage services minimizes exfiltration risks.
behavior-based ransomware detection: Implement
next-generation antivirus (NGAV) and EDR solutions 3. Encrypt sensitive financial data at rest and in
to monitor ransomware-specific behaviors, such transit to prevent unauthorized exposure: Use
as mass file encryption, deletion of backups, strong encryption protocols (AES-256, TLS 1.2+) for
and unauthorized registry changes. Configure all sensitive financial data stored or transmitted within
automatic containment of infected devices to the organization. Enforce strict access controls and
prevent ransomware propagation. Early detection of MFA for cloud storage access. Implement logging and
encryption related activity helps mitigate the impact of monitoring for cloud storage interactions to detect
ransomware attacks. and investigate anomalies. Encrypting sensitive data
mitigates the risk of unauthorized disclosure, even if
2. Enforce strict data-backup policies with exfiltrated.
immutable storage and offline recovery:
Implement a 3-2-1 backup strategy with offline, Recommendations for High-Risk Attack Techniques
immutable backups stored separately from with Severe Operational & Security Risks
production environments. Regularly test backup-
restoration procedures to ensure a quick recovery T1547 (Boot or Logon Autostart Execution)
from ransomware attacks. Use backup encryption
and access controls to protect stored data from 1. Enforce application control and prevent
unauthorized modifications. Secure backups provide unauthorized persistence mechanisms: Implement
a critical recovery mechanism in case of ransomware application allowlisting using Windows Defender
infection. Application Control (WDAC) or AppLocker to prevent
unauthorized execution of malware at system
3. Implement network segmentation and startup. Restrict administrative privileges to prevent
application allowlisting to prevent ransomware unauthorized registry modifications, scheduled
spread: Segment critical banking infrastructure from task creation, or service installations. Enforce
general IT environments using strict access controls digital signature verification to ensure only trusted
and firewall policies. Deploy application allowlisting applications can persist. These measures reduce the
to prevent unauthorized execution of ransomware ability of attackers to establish persistence through
payloads. Monitor file-system changes and restrict startup mechanisms.
write access to sensitive directories. Isolating critical
systems reduces the attack surface and limits the 2. Monitor and audit system startup
impact of a ransomware outbreak. configurations for anomalies: Deploy EDR solutions
to monitor modifications to startup locations such as
the Windows registry, scheduled tasks, and service
49

configurations. Configure security information and T1562.001 (Impair Defenses: Disable or Modify Tools)
event management (SIEM) alerts for unauthorized
changes to auto-start entries. Regularly audit 1. Implement endpoint protection with tamper-
system startup settings to identify and remove proof security controls: Deploy EDR solutions
suspicious persistence mechanisms. Continuous with tamper protection to prevent adversaries from
monitoring helps detect and respond to unauthorized disabling security tools. Restrict administrative access
modifications before adversaries can leverage them. to security software and enforce role-based access
control (RBAC) to limit modification privileges. Lock
3. Harden system integrity and enforce secure down security settings with group policies to prevent
boot mechanisms: Enable Secure Boot to prevent unauthorized changes. These protections prevent
unauthorized boot modifications and ensure only attackers from disabling defenses during an attack.
trusted OS components load at startup. Implement
tamper protection for critical system configurations to 2. Monitor and log security tool modifications:
prevent adversaries from modifying autostart entries. Configure SIEM solutions to log and alert on security
Use host-based intrusion prevention systems (HIPS) tool modifications, such as antivirus disabling, logging
to block suspicious persistence attempts. Hardening being turned off, or firewall rules being changed.
boot processes reduces the risk of malware Deploy host-based intrusion prevention systems
persistence in banking terminals and ATMs. (HIPS) to detect and block unauthorized attempts to
modify security configurations. Regular monitoring
T1484.001 (Domain Policy Modification: Group Policy ensures rapid detection of adversarial attempts to
Modification) disable security tools.
1. Implement role-based access control (RBAC) 3. Restrict execution of scripts and administrative
to restrict domain policy modifications: Restrict tools used for disabling defenses: Implement
Group Policy modification privileges to a limited set of PowerShell script block logging and enforce
administrators. Use privileged access management execution policies to prevent unauthorized scripts
(PAM) solutions to enforce just-in-time (JIT) access from modifying security configurations. Restrict the
and prevent unauthorized changes. Regularly review use of tools such as Process Hacker, GMER, and
and remove unnecessary administrative privileges. PsExec that attackers commonly use to disable
These measures limit the attacker's ability to security defenses. Using applications that allow
manipulate security policies for lateral movement. listing, block execution of unauthorized security-
disabling tools. These measures help maintain the
2. Continuously monitor and log Group Policy integrity of security defenses.
changes: Deploy SIEM solutions to log and alert on
Group Policy modifications. Use Microsoft Advanced T1046 (Network Service Discovery)
Threat Analytics (ATA) or Azure Sentinel to detect
suspicious policy changes indicative of an attack. 1. Limit exposure of network services through
Regularly review domain controller logs to identify firewall and access controls: Restrict inbound
unauthorized modifications. Monitoring policy and outbound traffic to essential services only using
changes helps detect and respond to malicious strict firewall rules. Disable unnecessary services and
activity before it spreads across the network. network protocols on critical banking infrastructure.
Implement network segmentation to isolate high-value
3. Enforce secure baseline configurations and systems from general IT environments. Restricting
backup Group Policy objects (GPOs): Implement a service exposure reduces the attack surface for
secure baseline configuration using CIS benchmarks adversarial reconnaissance.
or Microsoft Security Baselines. Regularly backup
Group Policy Objects (GPOs) and enable rollback 2. Deploy network monitoring and anomaly
capabilities to restore security settings in case of detection for unauthorized scans: Use intrusion
compromise. Use version control and audit logs to detection systems (IDS) and network traffic analysis
track changes and revert unauthorized modifications. (NTA) tools to monitor for anomalous network
Secure baselines and backups ensure quick recovery scanning activities. Configure SIEM solutions to
from malicious policy alterations. generate alerts on excessive network connection
attempts or unusual service queries. Implement
deception technology (honeypots) to detect and
track attackers attempting network reconnaissance.
Monitoring network activity enables early detection of
threat actor reconnaissance attempts.
50

3. Harden network protocols and enforce strict compromised RDP sessions. Continuous monitoring
authentication: Disable legacy protocols such as helps detect unauthorized remote access attempts.
SMBv1 and enforce TLS encryption on all network
communications. Implement mutual authentication for 3. Harden RDP settings and implement session
sensitive network services to prevent unauthorized security controls: Configure RDP to use network
access. Require certificate-based authentication level authentication (NLA) to prevent unauthorized
for remote administrative services. Strengthening access before authentication. Enforce TLS encryption
network security protocols makes service discovery for all RDP traffic. Use time-based access controls
more difficult for attackers. to limit RDP access to predefined maintenance
windows. Regularly review RDP session logs
T1082 (System Information Discovery) to identify suspicious activity. Hardening RDP
configurations reduces the risk of unauthorized
1. Restrict access to system and hardware access and lateral movement.
information: Configure group policies to prevent
non-administrative users from accessing system Recommendations for Indirect Impact Attach Techniques
information commands such as systeminfo, wmic, Used for Lateral Movement & Evasion
and tasklist. Disable remote access to system
enumeration tools on banking endpoints. Prevent T1059.003 (Windows Command Shell – Executes
adversaries from collecting detailed information about scripts to automate malicious actions in financial
financial institution infrastructure. systems)
2. Deploy endpoint monitoring to detect 1. Restrict execution of unauthorized command-
suspicious discovery activities: Use EDR solutions line scripts and commands: Implement application
to monitor and alert on system enumeration allowlisting using Windows Defender Application
commands executed by unauthorized users. Control (WDAC) or AppLocker to block unauthorized
Configure SIEM rules to log and flag attempts to execution of cmd.exe and batch scripts. Enforce
access system details. Detecting reconnaissance PowerShell script block logging and execution policies
activity early helps prevent further exploitation. to prevent malicious scripts from running. Limit access
to command-line interpreters for non-administrative
3. Enforce strict access controls for system users. Restricting command shell execution prevents
management tools: Restrict administrative access adversaries from automating malicious actions within
to system management utilities such as PowerShell, financial systems.
WMI, and Task Scheduler. Use just-in-time (JIT)
privilege escalation to grant temporary access 2. Monitor and log suspicious command-line
only when necessary. Regularly audit access logs activity: Deploy EDR solutions to track command-line
for unusual queries against system information usage and detect suspicious scripts executing system
databases. These measures limit an attacker’s ability modifications. Configure SIEM alerts to flag unusual
to gather intelligence on banking infrastructure. shell commands such as net user, taskkill, or reg add.
Proactively monitoring shell activity allows security teams
T1021.001 (Remote Services: Remote Desktop Protocol to detect and mitigate unauthorized script execution.
– RDP)
3. Enforce strict access controls on administrative
1. Restrict RDP access with strong authentication command execution: Implement JIT privilege escalation
and network segmentation: Implement MFA for to restrict access to administrative command-line
all RDP connections. Restrict RDP access using interfaces. MFA is required for privileged sessions using
firewalls, allowing only pre-approved IP addresses. cmd.exe or PowerShell. Log all administrative shell
Use virtual desktop infrastructure (VDI) with brokered activities for forensic analysis. These measures limit
authentication to limit direct exposure of RDP adversaries’ ability to execute malicious scripts and
services. Enforcing strict access controls reduces maintain persistence in banking systems.
unauthorized remote access attempts.
T1072 (Software Development Tools – Utilized to
2. Monitor and log RDP session activity to compile and execute malicious code within banking
detect unauthorized access: Enable logging for environments)
RDP sessions, capturing successful and failed
connection attempts. Configure SIEM solutions to 1. Restrict installation and execution of
generate alerts for anomalous RDP usage, such unauthorized development tools: Use application
as logins from unusual locations or repeated failed allowlisting to prevent unauthorized execution of
attempts. Implement behavioral analytics to detect compilers, scripting environments, and development
51

frameworks within banking networks. Limit installation T1572 (Protocol Tunneling – Conceals malicious network
permissions for tools such as Visual Studio, GCC, traffic to bypass security controls)
and Python to authorized users only. Blocking
unapproved software development tools reduces the 1. Implement deep packet inspection (DPI) to
risk of adversaries compiling and executing malicious detect and block tunneling activity: Deploy network
code. intrusion detection and prevention systems (IDS/IPS)
with DPI capabilities to analyze encrypted traffic for
2. Monitor developer tool usage for anomalies: protocol tunneling signatures. Use threat intelligence
Deploy endpoint monitoring solutions to track the feeds to update detection rules for known tunneling
execution of software development tools and identify tools. DPI ensures that unauthorized protocol
unauthorized usage. Configure SIEM rules to generate tunneling attempts are identified and blocked before
alerts when suspicious code compilation or execution reaching critical systems.
occurs outside approved development environments.
Continuous monitoring ensures rapid detection of 2. Restrict outbound network connections to
adversarial use of development tools. only approved protocols and services: Configure
firewalls to block unauthorized outbound connections
3. Enforce strict code execution policies in using protocols commonly leveraged for tunneling,
financial systems: Digital signature verification such as ICMP, DNS, and HTTP over non-standard
is required for all executables and scripts before ports. Implement strict egress filtering policies to limit
execution. Implement sandboxing for unverified external communications to pre-approved domains
code execution to prevent direct interaction with and IP addresses. Reducing unauthorized outbound
production systems. Use EDR to analyze the behavior traffic minimizes the effectiveness of tunneling
of compiled binaries before allowing execution. techniques.
Enforcing execution controls mitigates the risk of
malicious code being deployed in banking networks. 3. Monitor network traffic for anomalies indicative
of tunneling attempts: Use network traffic analysis
T1110 (Brute Force – Attempts to crack banking (NTA) tools to detect irregular data transfer patterns,
credentials for unauthorized access) such as encrypted payloads over unexpected
ports. Configure SIEM solutions to generate alerts
1. Enforce strong password policies and account when suspicious tunneling behaviors are detected.
lockout mechanisms: Require complex passwords Continuous monitoring helps security teams identify
with a minimum length of 12-15 characters and and respond to adversarial attempts to bypass
enforce automatic password expiration. Implement security controls.
account lockout policies after multiple failed login
attempts to prevent brute-force attacks. Use T1071.002 (Application Layer Protocol: File Transfer
password blacklisting to prevent the use of standard Protocols – Used for staging and transferring stolen
or easily guessed passwords. Strong authentication financial data)
policies significantly reduce the effectiveness of brute-
force attacks. 1. Restrict unauthorized use of file transfer
protocols: Block unauthorized FTP, SFTP, and
2. Deploy anomaly detection for login attempts HTTP file transfers using network firewalls and
and implement multi-factor authentication (MFA): web proxies. Limit outbound file transfers to pre-
Use behavioral analytics to detect abnormal login approved cloud storage and internal repositories. For
activity, such as repeated failed attempts from a single auditing purposes, authentication is required for all
IP address. Implement MFA for all privileged accounts file transfers and log activity. Restricting file transfer
and remote access points to prevent unauthorized protocol usage prevents adversaries from exfiltrating
access even if credentials are compromised. Anomaly financial data.
detection and MFA create multiple layers of defense
against brute-force attacks. 2. Monitor and log file transfer activities for
suspicious behavior: Deploy security monitoring
3. Restrict external access to authentication tools to track large or unexpected file transfers from
portals and enforce geofencing rules: Limit access financial systems. Configure SIEM alerts for high-
to authentication systems using IP whitelisting and volume uploads to external servers or anomalous
geofencing to block login attempts from high-risk transfer patterns. Regularly auditing file transfer logs
regions. Use identity threat detection tools to analyze helps detect data exfiltration attempts before they
authentication requests for signs of automated brute- result in financial losses.
force attempts. Restricting access to authentication
portals minimizes exposure to credential stuffing and
password brute-forcing.
52

3. Encrypt sensitive financial data at rest and in 5.3 Mispadu
transit to prevent unauthorized access: Enforce
end-to-end encryption for all file transfers using Mispadu is a highly sophisticated banking trojan
secure protocols such as SFTP, TLS, and IPsec. that poses a significant threat to the financial sector,
Implement data loss prevention (DLP) solutions particularly in LATAM. Originally discovered in 2019,
to automatically detect and block the transfer of Mispadu has since expanded its reach beyond its initial
sensitive banking data to unauthorized destinations. targets in Brazil and Mexico to include other LATAM
Encryption and DLP policies ensure financial data countries and even European nations.217 218
remains secure even if it is exfiltrated.
The trojan's effectiveness in targeting financial
T1219 (Remote Access Software – Enables attackers to institutions stems from its multi-stage infection strategy
maintain persistent control over compromised banking and stealthy nature. Mispadu primarily focuses on
systems) Spanish and Portuguese-speaking users, making it
particularly dangerous for banks and credit unions in
1. Block unauthorized remote access tools and LATAM.219 220 Its ability to bypass numerous endpoint
restrict remote desktop access: Use application protection solutions, including many well-known anti-
allowlisting to prevent execution of unauthorized remote virus products, has allowed it to infiltrate a wide range
access tools such as TeamViewer, AnyDesk, and VNC. of industries, with the financial sector being a primary
Disable remote desktop access (RDP) on critical financial target.221
systems unless explicitly required. Restrict remote
access to VPN-only connections with MFA enforcement. Mispadu's impact on the financial sector is substantial:
Blocking unauthorized remote access tools reduces the
attack surface for persistent control. • Credential theft: The trojan steals banking
credentials, credit card information, and other
2. Continuously monitor and log remote access sensitive financial data using keylogging and screen
sessions: Deploy endpoint monitoring solutions to track capture techniques.222
all remote access sessions and detect unusual login
behaviors. Use behavioral analytics to identify anomalies, • Cryptocurrency targeting: Mispadu monitors for
such as remote sessions originating from unusual cryptocurrency wallet addresses and can replace
geolocations or during non-business hours. Logging them with attacker-controlled addresses, potentially
and monitoring remote access activities help detect redirecting transactions.223
persistent adversary presence.
• Widespread infections: In one campaign, Mispadu
3. Enforce network segmentation and limit remote affected numerous government websites and online
access privileges: Isolate remote access services from banking platforms across Chile, Mexico, and Peru,
core banking networks using network segmentation. compromising hundreds of financial institutions.224
Implement just-in-time (JIT) access provisioning to grant
temporary remote access only when necessary. Use A notable example of Mispadu's effectiveness was
privilege access management (PAM) solutions to enforce a campaign that targeted users with fake discount
strict session recording and auditing for all remote coupons, demonstrating the trojan's ability to adapt
connections. Segmentation and privilege restrictions its social engineering tactics to lure victims.225 This
prevent attackers from leveraging remote access tools adaptability, combined with its focus on LATAM
for lateral movement. financial institutions, makes Mispadu a persistent and
evolving threat to the region's banking sector. To evade
detection, the malware uses advanced techniques
like obfuscation, sandbox detection, and geofencing.
Morphisec's intelligence reports reveal that Mispadu's
final payload was delivered through a decrypted AutoIT
script, which loads the trojan into memory. Hackers
have been using weaponized PDF files for distribution,
217 https://blog.morphisec.com/mispadu-infiltration-beyond-latam
218 https://www.feedzai.com/blog/
219 https://www.feedzai.com/blog/
220 https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/mispadu-banking-trojan-resurfaces
221 https://blog.morphisec.com/mispadu-infiltration-beyond-latam
222 https://www.feedzai.com/blog/
223 https://www.feedzai.com/blog/
224 https://www.metabaseq.com/threat/mispadu-banking-trojan/
225 https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/mispadu-banking-trojan-resurfaces
53

and Mispadu is known for stealing browser and email 5.3.2 Tactics, Techniques, and Procedures
passwords and actively monitoring user activity. Initially
targeting Latin America, it now affects Europe, stealing Mispadu employs a sophisticated array of TTPs
credentials through phishing emails and malicious.226 designed to maximize its effectiveness as a banking
trojan. Its infection campaigns often begin with social
5.3.1 Mispadu’s Methods and Exploitation of engineering through phishing emails, distributing
LATAM Infrastructure malicious HTML pages, or password-protected
PDF attachments that entice users into executing
The Mispadu campaign's methods are strategically the malware.228 The trojan also leverages malicious
tailored to exploit the unique vulnerabilities present advertisements and compromised legitimate websites,
in LATAM’s regulatory, legal, and IT ecosystems. One including vulnerable WordPress-based platforms, to
primary factor is the lack of stringent cybersecurity serve as Command and Control (C2) servers for payload
regulations and inconsistent enforcement across the delivery.229 Additionally, Mispadu adopts multi-stage
region, which provides a low-risk environment for cyber infection chains, using obfuscated scripts and loaders
criminals. By targeting regions with weak cybersecurity such as AutoIT and VBScript to deliver its final payload,
awareness, Mispadu ensures that phishing email which is a hallmark of its operational complexity.
campaigns achieve higher success rates, as users are
less likely to recognize and report malicious activity.227 To evade detection, Mispadu employs anti-analysis
Furthermore, outdated systems and software prevalent techniques, including virtual machine detection and
in LATAM organizations make it easier for the malware language checks, to ensure the malware only executes
to exploit known vulnerabilities, such as those in CMS in environments matching the targeted victim profile.
platforms like WordPress. It also utilizes fake certificates to disguise the malware
and bypass security defenses.230 The malware includes
Mispadu capitalizes on insufficient incident response functionality for credential theft, employing backdoors
capabilities within the region, ensuring prolonged that allow it to capture keystrokes, take screenshots,
undetected operations. The adoption of anti-analysis and display fake browser overlays to extract sensitive
measures and multi-layered infection chains not only information. Moreover, Mispadu leverages the dual-C2
improves evasion but also exploits the limited forensic infrastructure and advanced techniques like the
and mitigation capabilities of regional cybersecurity exploitation of the Windows SmartScreen vulnerability
teams. The geographically targeted approach, filtering (CVE-2023-36025) to bypass security warnings,
victims by system language settings, ensures that only ensuring its payloads are delivered stealthily and
intended demographics are affected, thereby increasing effectively.231
the efficiency and profitability of the campaigns. Finally,
by leveraging the Windows SmartScreen bypass,
Mispadu circumvents built-in protections, exploiting the
lack of technical maturity and reliance on default security
configurations in many LATAM organizations. These
strategies highlight the trojan’s effectiveness in exploiting
the regulatory and technical gaps of the region to sustain
its malicious operations.
226 https://www.morphisec.com/blog/mispadu-infiltration-beyond-latam/
227 https://blog.morphisec.com/mispadu-infiltration-beyond-latam
228 https://blog.morphisec.com/mispadu-infiltration-beyond-latam
229 https://www.metabaseq.com/threat/mispadu-banking-trojan/
230 https://www.feedzai.com/blog/
231 https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/mispadu-banking-trojan-resurfaces
54

5.3.3 Mispadu Tactics, Techniques, and Procedures
| Tactics | Techniques | Procedures |
| ------- | ---------- | ---------- |
Reconnaissance
|     | NA  | NA  |
| --- | --- | --- |
(TA0043)
Resource Development
|     | NA  | NA  |
| --- | --- | --- |
(TA0042)
Spam campaigns, the victim is led
Initial Access
|     | T1566.001: Phishing | to the payload by a malicious link or  |
| --- | ------------------- | -------------------------------------- |
(TA0001)
attachment
Exploit a weakness in an Internet-
T1190: Exploit Public-Facing
|     |     | facing host or system to initially  |
| --- | --- | ----------------------------------- |
Application
access a network.
Executes when the user opens
Execution   T1204.002: User Execution Malicious  malicious attachments or files
| (TA0002) | File: Malware | downloaded from compromised  |
| -------- | ------------- | ---------------------------- |
websites.
| Persistence   |     | Employs scheduled tasks to maintain  |
| ------------- | --- | ------------------------------------ |
T1053.005: Scheduled Task/Job
| (TA0003) |     | persistence on infected systems. |
| -------- | --- | -------------------------------- |
T1055: Process Injection
| Privilege Escalation   |     | Injects its payload into legitimate  |
| ---------------------- | --- | ------------------------------------ |
T1055.012: Process Hollowing
| (TA0004) |     | processes to avoid detection.  |
| -------- | --- | ------------------------------ |
T1055.013: Process Doppelganging
Defense Evasion
|     | T1036: Masquerading | Masquerades as a discount coupon |
| --- | ------------------- | -------------------------------- |
(TA0005)
Uses obfuscation and encryption to
T1027: Obfuscated Files or
evade detection by security tools,
|     | Information   |     |
| --- | ------------- | --- |
including anti-analysis and sandbox
T1027.013: Encrypted/Encoded File
detection.
T1555: Credentials from Password
Credential Access   Stores   Obtains credentials from mail clients
| (TA0006) | T1555.003: Credentials from Web  | and web browsers.  |
| -------- | -------------------------------- | ------------------ |
Browsers
|     | T1003: OS Credential Dumping  | Uses tools like WebBrowserPassView  |
| --- | ----------------------------- | ----------------------------------- |
  T1003.008: etc/password and etc/ and MailPassView to steal passwords
|     | shadow                           | from browsers and email clients.       |
| --- | -------------------------------- | -------------------------------------- |
|     | T1056: Input Capture T1056.001:  | Captures keystrokes and screenshots    |
|     | Keylogging                       | to steal credentials and sensitive     |
|     | T1056.003: Web Portal Capture    | data.                                  |
|     | T1082: System and Information    | Extracts the version of the operating  |
Discovery
|     | Discovery  | system, computer name and  |
| --- | ---------- | -------------------------- |
(TA0007)
|     | T1083: File and Directory Discovery | language ID. |
| --- | ----------------------------------- | ------------ |
Lateral Movement
|     | NA  | NA  |
| --- | --- | --- |
(TA0008)
| Collection   |     | Contains a command to take  |
| ------------ | --- | --------------------------- |
T1113: Screen Capture
| (TA0009) |     | screenshots.  |
| -------- | --- | ------------- |
Collects credentials, browser history,
  T1005: Data from Local System and system information from the
victim's machine.
55

Tactics Techniques Procedures
Communicates with C2 servers using
Command and Control (C2) T1573: Encrypted Channel Command HTTPS or other encrypted channels
(TA0011) and Control (C2) for data exfiltration and command
execution.
Uses an existing, legitimate external
T1102: Web ServiceT1102.002:
Web service as a means for relaying
Bidirectional Communication
data to/from a compromised system.
Transfer tools or other files from an
T1105: Ingress Tool Transfer external system into a compromised
environment.
Sends the data it collects to its C&C
Exfiltration (TA0010) T1041: Exfiltration Over C2 Channel
server.
Uses an existing, legitimate external
Web service to exfiltrate data rather
T1567: Exfiltration Over Web Service
than their primary command and
control channel
Impact(TA0040) NA
Mispadu IOCs
• Mispadu exfiltrates stolen data, including credentials and system information, via encrypted C2 channels.
• Hashes: 72e83b133a9e4cecd21fdb47334672f6, e5967a8274d40e0573c28b664670857e IP addresses:
104.238.182.44, 140.82.47.181
• Domain: germogenborya.top, russk22.icu, germogenborya.at
Other Mispadu IOCs
• SHA256 C++ dropper non-obfuscated version
• dbb2e294a65eb3fa1bbe1a25c2baf352a01250d567cfa953d4f942c2b5f08e53
• SHA256 C++ dropper obfuscated version
• d56863d940d5ccd1922bbbdf65471c493701e3b10be5c522851c8efbdaeb9fae
• SHA256.NET dropper
• ac97f893f8243db3c5ccfbc89d83b97534c1b73d0289ccb61bfb2c035f539126
• SHA256HTA dropper
• f873062ff206ad60cb4b790c2ba83624c510f15dbc4905d5c96668f87999c16a
• SHA256D2 downloader
• 7b6444e5be24ce95cdcac357cf20ddc77abda142a16202ab3677b7d29a1e0da3
• SHA256 payload version 96
• 78e3e51ddeac0519d434a8b192bae61bbaa278154a9511676c8a58079d95beb5
• SmokeBot download URL that served Mispadu
• http[:]//84.54.50[.]102/FX_432661.exe
• SmokeBot download URL that served a Rhadamanthys payload connected to Mispadu
• http[:]//amx55[.]xyz/rh111.exe
Mispadu CVE: CVE-2023-3602
5.3.3 Mispadu Mitigations
Reconnaissance (TA0043)
• Monitor network traffic for suspicious scanning activities using IDS/IPS.
• Deploy honeypots to detect early reconnaissance attempts.
56

Resource Development (TA0042)
Monitor domain registrations and look for spoofed domains mimicking your organization.
Use threat intelligence feeds to track adversary infrastructure.
Initial Access (TA0001)
T1566.001: Phishing
• Implement email security solutions (DMARC, DKIM, SPF).
• Conduct employee security awareness training on phishing threats.
• Use sandboxing for email attachments to detect malicious content.
T1190: Exploit Public-Facing Application
• Perform regular vulnerability scanning and patching of internet-facing applications.
• Implement Web Application Firewalls (WAFs) to detect and block exploit attempts.
Execution (TA0002)
T1204.002: User Execution - Malicious File
• Enable application whitelisting to restrict unauthorized execution.
• Use EDR tools to identify suspicious execution.
Persistence (TA0003)
T1053.005: Scheduled Task/Job
• Audit scheduled tasks regularly and restrict user privileges.
• Use PowerShell logging to detect abnormal script execution.
Privilege Escalation (TA0004)
T1055: Process Injection (including T1055.012 and T1055.013)
• Enable Windows Defender Credential Guard to prevent credential theft.
• Use behavior-based detection for injected processes.
Defense Evasion (TA0005)
T1036: Masquerading
• Deploy heuristic-based detection for disguised malware.
• Analyze file metadata for anomalies in timestamps and signatures.
T1027: Obfuscated Files or Information
• Implement automated malware analysis in a sandbox environment.
• Enable real-time file integrity monitoring for unexpected changes.
Credential Access (TA0006)
T1555: Credentials from Password Stores
• Disable password autocomplete in browsers and applications.
• Enforce MFA for critical systems.
T1003: OS Credential Dumping
• Monitor Windows Event Logs for abnormal LSASS access attempts.
• Disable unencrypted credential storage in OS configurations.
T1056: Input Capture (Keylogging, Web Portal Capture)
• Deploy behavior-based keylogger detection.
• Enforce least privilege access to prevent unauthorized software installations.
57

Discovery (TA0007)
Impact (TA0040)
T1082: System and Information Discovery • Implement ransomware protection with endpoint
• Restrict system information access using Group rollback capabilities.
Policy settings. • Use network segmentation to limit the spread of
• Monitor command-line activity for reconnaissance malware.
attempts.
5.4 Horabot
Collection (TA0009)
Horabot is a sophisticated malware that has been
T1113: Screen Capture designed to target spanish-speaking users, mainly
• Implement DLP solutions to monitor and restrict across Latin American countries. Horabot uses multi-
unauthorized screenshots. modular techniques to steal sensitive information
• Use virtual desktops to limit malware persistence. and spreads itself further, focusing on Latin American
systems. Based on the evidence gathered by Cisco
T1005: Data from Local System Talos, there are patterns revealing the highly targeted
• Enforce data encryption at rest and in transit. attacks in these regions where cybersecurity measures
• Deploy file integrity monitoring to detect are not as robust.232
unauthorized data access.
Horabot was first observed as a significant threat in
Command and Control (TA0011) late 2020, identified by Cisco’s Talos team as part of a
phishing campaign with tax-related themes to entice
T1573: Encrypted Channel victims.233 Horabot targets individuals and businesses
• Monitor network traffic for unusual encrypted in Mexico, Uruguay, Brazil, Venezuela, Argentina,
connections. Guatemala and Panama.234 These malware campaigns
• Implement SSL/TLS decryption and inspection typically disguise themselves as legitimate emails from
where feasible. the tax agencies, presenting users with a malicious
HTML attachment that upon clicking redirects the users
T1102: Web Service to a malicious HTML application. The phishing emails
• Block known malicious domains using threat use Spanish as their primary language which aligns with
intelligence feeds. the target region and utilizes regional tax deadlines to
• Deploy anomaly detection to identify irregular data trick the users into clicking on the malicious attachments
traffic. and increase the infection rate.235
T1105: Ingress Tool Transfer Primary Targets and Sectors:
• Restrict file downloads from unknown external
sources. • The main target entities of Horabot are from
• Use content filtering solutions to block unauthorized the following sectors: accounting, construction,
transfers. engineering, wholesale distribution, and
investments.236
Exfiltration (TA0010) • By nature, organizations in these industries would
generally be more susceptible to phishing as they
T1041: Exfiltration Over C2 Channel often engage in transactional emails.237
• Implement DLP controls to monitor outbound data
flows. 5.4.1 Capabilities and Malware Functionality
• Detect data exfiltration patterns using network
analytics. Horabot utilizes banking trojan and spam tools and is
deployed at different stages of the infection.
T1567: Exfiltration Over Web Service
• Block unauthorized external file transfers via web • The banking trojan fetches sensitive information
proxies. related to banking login credentials, information
• Implement API monitoring to detect abnormal data about operating systems, keystrokes, one-
movements. time passwords and soft tokens from banking
232 https://blog.talosintelligence.com/new-horabot-targets-americas/
233 https://blog.talosintelligence.com/new-horabot-targets-americas/
234 https://blog.talosintelligence.com/new-horabot-targets-americas/
235 https://www.welivesecurity.com/2019/08/01/banking-trojans-amavaldo/
236 https://blog.talosintelligence.com/new-horabot-targets-americas/
237 https://www.welivesecurity.com/2019/08/01/banking-trojans-amavaldo/
58

applications. This functionality directly exploits
the security protocols of Latin American financial
institutions, placing user accounts at risk and
enabling unauthorized access to funds.238
• The role played by the spam tool is to compromise
Yahoo, Gmail, and Outlook accounts to harvest
and exfiltrate the email addresses of the target's
contacts. Once these addresses are harvested, the
malware sends phishing emails using the victim’s
legitimate email account and organization’s server,
increasing the emails’ credibility and decreasing the
likelihood of detection.239
Figure 7: Attack Flowchart
User Open Malicious
HTML attachment
User clic¶s
Loads Malicious lin¶
Initial Phishing Email R A ed W ir S e c E t C s 2 to Ma A li p c p io li u c s a t H io T n ML Downloads RAR File
Malicious CMD File
Powershell
Downloader Script A=ter (cid:23)1 seconds
s#stem restarts
Downloads (cid:5)
executes
Initates
s#stem re(cid:30)oot
Zip Files Startup Files Execute
Executes downloads
Downloads (cid:5) DLL Sideloadin(cid:17) Additional PS scripts
executes Contains
Usin(cid:17)
script (cid:23) script 2
Le(cid:17)itimate Executa(cid:30)les ^
Pa#load DLLs DLLs
Powershell Downloader Hora(cid:30)ot
238 https://blog.talosintelligence.com/new-horabot-targets-americas/
239 https://blog.talosintelligence.com/new-horabot-targets-americas/
59

5.4.2 Correlation Between Horabot and Mispadu

Horabot and Mispadu have striking similarities in their TTPs, and both frequently target Latin American organizations.
Some similarities that have been observed are:

•  Both malware families have been targeting financial institutions and users in Latin America who speak Spanish,
through mostly phishing attacks that involve HTML-based malicious payloads that initiate multi-step infection
chains.
•  They leverage the MITRE ATT&CK techniques T1204.001 (User Execution: Malicious Link) and T1566 (Phishing),
enabling them to propagate efficiently through social engineering tactics designed to evade detection on legitimate
email servers
•  Horabot and Mispadu commonly employ obfuscation techniques and payload encryption, evading static signature-
based detections on endpoint solutions.
•  Both malwares implement geolocation filters to target Spanish- and Portuguese-speaking regions. Hardcoded
Spanish keywords and financial institution names align with their focus on Latin America, especially Mexico and
Brazil.

5.4.3 Horabot Tactics, Techniques & Procedures
| Tactics | Techniques | Procedures |
| ------- | ---------- | ---------- |
Resource Development   Compromise third-party infrastructure
T1584: Compromise Infrastructure
| (TA0042) |     | that can be used during targeting. |
| -------- | --- | ---------------------------------- |
Compromise numerous third-party
T1584.005: Compromise
|     |     | systems to form a botnet that can be  |
| --- | --- | ------------------------------------- |
Infrastructure: Botnet
used during targeting.
| Initial Access   |     | Send phishing messages to gain  |
| ---------------- | --- | ------------------------------- |
T1566: Phishing
| (TA0001) |     | access to victim systems. |
| -------- | --- | ------------------------- |
Send spear phishing emails with a
T1566.001: Phishing: Spear Phishing
|     |     | malicious attachment in an attempt to  |
| --- | --- | -------------------------------------- |
Attachment
gain access to victim systems.
Attempt to exploit a weakness in
T1190: Exploit Public-Facing
|     |     | an Internet-facing host or system to  |
| --- | --- | ------------------------------------- |
Application
initially access a network.
Obtain and abuse credentials of
existing accounts as a means of
  T1078: Valid Accounts gaining Initial Access, Persistence,
Privilege Escalation, or Defense
Evasion.
Abuse command and script
| Execution   | T1059: Command and Scripting  |     |
| ----------- | ----------------------------- | --- |
interpreters to execute commands,
| (TA0002) | Interpreter  |     |
| -------- | ------------ | --- |
scripts, or binaries.
|     | T1059.001: Command and Scripting  | Abuse PowerShell commands and  |
| --- | --------------------------------- | ------------------------------ |

|     | Interpreter: PowerShell  | scripts for execution. |
| --- | ------------------------ | ---------------------- |
Rely upon specific actions by a user
|     | T1204: User Execution |     |
| --- | --------------------- | --- |
in order to gain execution.
|     | T1204.001: User Execution:  | Rely upon a user clicking a malicious  |
| --- | --------------------------- | -------------------------------------- |

|     | Malicious Link | link in order to gain execution. |
| --- | -------------- | -------------------------------- |
Interact with the native OS
|     | T1106: Native API | application programming interface  |
| --- | ----------------- | ---------------------------------- |
(API) to execute behaviors.
60

| Tactics | Techniques | Procedures |
| ------- | ---------- | ---------- |
Execute their own malicious payloads
Persistence
|     | T1574: Hijack Execution Flow | by hijacking the way operating  |
| --- | ---------------------------- | ------------------------------- |
(TA0003)
systems run programs.
|     | T1574.002: Hijack Execution Flow:  | Execute their own malicious payloads  |
| --- | ---------------------------------- | ------------------------------------- |

|     | DLL Side-Loading                    | by side-loading DLLs.          |
| --- | ----------------------------------- | ------------------------------ |
|     | T1547.001: Boot or Logon Autostart  | Achieve persistence by adding  |
  Execution: Registry Run Keys /  a program to a startup folder or
|     | Startup Folder | referencing it with a Registry run key. |
| --- | -------------- | --------------------------------------- |
Create or modify shortcuts that can
T1547.009: oot or Logon Autostart
|     |     | execute a program during system  |
| --- | --- | -------------------------------- |
Execution: Shortcut Modification
boot or user login.
Attempt to manipulate features of
| Defense Evasion   |     | their artifacts to make them appear  |
| ----------------- | --- | ------------------------------------ |
T1036: Masquerading
| (TA0005) |     | legitimate or benign to users and/or  |
| -------- | --- | ------------------------------------- |
security tools.
Attempt to make an executable or
file difficult to discover or analyze by
T1027: Obfuscated Files or
|     |     | encrypting, encoding, or otherwise  |
| --- | --- | ----------------------------------- |
Information
obfuscating its contents on the
system or in transit.
Employ various means to detect
T1497: Virtualization/Sandbox
|     |     | and avoid virtualization and analysis  |
| --- | --- | -------------------------------------- |
Evasion
environments.
|     | T1070.004: Indicator Removal: File  | Delete files left behind by the actions  |
| --- | ----------------------------------- | ---------------------------------------- |

|     | Deletion | of their intrusion activity. |
| --- | -------- | ---------------------------- |
Credential Access   T1056.001: Input Capture:  Log user keystrokes to intercept
| (TA0006) | Keylogging  | credentials as the user types them. |
| -------- | ----------- | ----------------------------------- |
Attempt to dump credentials to
obtain account login and credential
|     | T1003: OS Credential Dumping |     |
| --- | ---------------------------- | --- |
material, normally in the form of a
hash or a clear text password.
Attempt to get detailed information
about the operating system and
Discovery
|     | T1082: System Information Discovery | hardware, including version,  |
| --- | ----------------------------------- | ----------------------------- |
(TA0007)
patches, hotfixes, service packs, and
architecture.
Enumerate files and directories or
may search in specific locations of
|     |  T1083: File and Directory Discovery |     |
| --- | ------------------------------------ | --- |
a host or network share for certain
information within a file system.
The malware uses a spam tool to
Lateral Movement
|     |  T1534: Internal Spear Phishing  | exfiltrate the contact’s email address  |
| --- | -------------------------------- | --------------------------------------- |
(TA0008)
and sends targeted phishing email
Attempt to take screen captures of
Collection
|     | T1113: Screen Capture | the desktop to gather information  |
| --- | --------------------- | ---------------------------------- |
(TA0009)
over the course of an operation.
The threat actor group exfiltrated the
| Impact   |     | banking login credentials of the victim  |
| -------- | --- | ---------------------------------------- |
 T1657: Financial Theft
| (TA0040) |     | to access their bank accounts and  |
| -------- | --- | ---------------------------------- |
cause financial loss

61

IOCs:
IP Addresses
Domain Names
• 139[.]177[.]193[.]74
• tributaria[.]website • 185[.]45[.]195[.]226
• facturacionmarzo[.]cloud • 216[.]238[.]70[.]224
• m9b4s2[.]site • 51[.]38[.]235[.]152
• wiqp[.]xyz • 137[.]220[.]53[.]87
• ckws[.]info • 212[.]46[.]38[.]43
• amarte[.]store • 191[.]101[.]2[.]101
URLs
• hxxps[://]tributaria[.]website/
• hxxps[://]tributaria[.]website/ESP/12/151222/UP/UP
• hxxps[://]tributaria[.]website/A/08/150822/AU/TST/INDEX[.]PHP?LIST
• hxxps[://]tributaria[.]website/a/09/01092022/au/tst/index[.]php?list
• hxxps[://]tributaria[.]website/a/08/150822/up/up
• hxxps[://]tributaria[.]website/esp/12/151222/up/up
• hxxps[://]tributaria[.]website/a/W_/X\\W_YY/au/au
• hxxps[://]tributaria[.]website/a/08/150822/au/au
• hxxp[://]tributaria[.]website:443/
• hxxps[://]tributaria[.]website/A/08/150822/AU/AU
• hxxps[://]tributaria[.]website/esp/12/151222/au/au
• hxxp[://]139[.]177[.]193[.]74/a/08/150822/au/adjuntos_0703[.]html
• hxxp[://]139[.]177[.]193[.]74/esp/12/151222/au/adjuntos_0703[.]html
• hxxp[://]139[.]177[.]193[.]74/a/08/150822/au/logs/index[.]php?CHLG
• hxxp[://]139[.]177[.]193[.]74/
• hxxp[://]139[.]177[.]193[.]74/a/08/150822/au/tst/index[.]php?list
• hxxp[://]139[.]177[.]193[.]74/a/08/150822/au/adjuntos_2102[.]html
• hxxp[://]139[.]177[.]193[.]74/09/01092022/au/adjuntos_2102[.]html
• hxxp[://]139[.]177[.]193[.]74/a/08/150822/au/adjuntos_0102[.]htm
• hxxp[://]139[.]177[.]193[.]74:443/
• hxxps[://]facturacionmarzo[.]cloud/m/archivos[.]pdf[.]html
• hxxps[://]facturacionmarzo[.]cloud/e/archivos[.]pdf[.]html
Malicious Batch scripts
• 63535100bbc1ba8ce9afb5883a59a4138e95c8e33a4585b8285ea7a39e0ead3e
• 720c126f372b68ff79ef13bd1ae6fc9a6aef10669269490d7e8fb589d7d49064
• ffd43b32655fc6f1e1c10f88660b68e2c2ad7da271b0f2e3eda70ccdcb3bcee4
Powershell Downloader
• aaf456575c8761f3af9b61e015282d9162325ed09b699732bf65b53ae7b7d252
Banking Trojan
39194718b460ea174784f6a7edbccd1e3324fe1043be806927cece7a86f15611
474b25badb40f524a7b2fe089e51eb7dbafd2e3e03a9f6750f72055d05b13d76
Spam Tool
07f7575af922da1aea5aa26436a3cfcd91b419bbf31d77bf6c9d921290bc04da
62

5.5 Blind Eagle
5.5.1 Relevant Threat Actor Activity
Blind Eagle (APT-C-36) is a sophisticated Latin American threat actor known for cyber
espionage operations that impact sectors including government, finance, and energy
in Colombia, Ecuador, Chile, and Panama.240 Active since at least 2018, Blind Eagle
consistently leverages spear-phishing campaigns, impersonating legitimate regional
institutions to deliver remote access trojans (RATs).241 These attacks exploit human
vulnerabilities through deceptive emails with malicious links or attachments.
Blind Eagle’s activities showcase their adaptability and extensive knowledge of Latin
America’s institutional structures. The group’s increasing technical sophistication includes
techniques like process hollowing, a stealthy code injection method that helps them evade
detection and maintain persistent access. In process hollowing, Blind Eagle begins by
launching a legitimate process in a suspended state, then “hollows out” its memory by
removing the legitimate code. They then inject their own malicious code, often in the form
of Remote Access Trojans such as QuasarRAT or AsyncRAT, into this emptied memory
space. Once the process resumes, it runs the attacker’s code while retaining its original,
trusted name. This camouflages the malicious activity, as the process appears legitimate
to endpoint detection systems. Additionally, they use custom malware loaders, such as
Hijack Loader, to deploy Remote Access Trojans covertly, maintaining remote control over
infected devices and continuously adjusting tactics to avoid detection. The straightforward
flow chart is shown in Figure 8.
Figure 8: Blind Eagle’s Attack Activity
Hallow out Process
Launch Legitimate Suspend the Process and Memory by Removing
Process in Suspend State Prepare for Injection Legitimate Code
Deploy RATs Covertly Resume Process with Inject Malicious Code
by Hijack Loader Malicious Code Running
240 https://securelist.com/blindeagle-apt/113414/
241 https://research.checkpoint.com/2023/blindeagle-targeting-ecuador-with-sharpened-tools/
63

The impact on financial institutions has been approach is a common technique, used by numerous
substantial, as Blind Eagle’s espionage and credential threat actors to infiltrate organizations through trusted
theft campaigns have disrupted critical systems and regional personas. However, Blind Eagle’s unique
compromised sensitive information. Studies indicate characteristics lie in their extensive use of process
that Latin America has experienced a notable rise in injection, particularly process hollowing, and their
cybercrime costs, with the financial sector bearing custom malware delivery tools, like Hijack Loader, which
the brunt. According to the Organization of American are less frequently observed among other threat actors.
States (OAS) and the Inter-American Development Bank The combination of RAT deployment with advanced
(IDB), Latin American cyber incidents cost the region stealth techniques allows Blind Eagle to maintain
an estimated $90 billion annually, a significant portion a persistent presence in critical systems, posing
of which impacts financial institutions due to espionage significant challenges to detection and removal. Unlike
and credential theft campaigns.242 By capturing browser more generalized attackers, their operations are highly
data, often through keylogging and screen-capturing tailored to the LATAM region, with phishing emails that
trojans, Blind Eagle can siphon financial credentials, incorporate detailed knowledge of local government
directly compromising the security of financial institutions and financial systems, adding to their effectiveness and
in the region. This persistent cybersecurity threat uniqueness.
underscores the critical need for FIs to enhance their
defenses to keep pace with Blind Eagle’s evolving 5.5.4 Recommendations
tactics.
• Email Filtering: Implement robust filtering to catch
5.5.2 Background spear-phishing indicators like spoofed domain
names and unusual attachments, reducing the
Blind Eagle is a cyber-espionage group concentrated likelihood of phishing emails reaching employees.
in Latin America, particularly targeting Colombia
and Ecuador’s high-value government and financial • Endpoint Detection and Response (EDR):
sectors.243 Their primary method of exploitation begins Strengthen EDR solutions to detect process
with spear-phishing emails that disguise malware as injection activities, such as process hollowing,
official communications. These emails carry attachments enhancing visibility, and enabling a swift response to
or links designed to deploy RATs like QuasarRAT and threats.
AsyncRAT on victim systems, allowing Blind Eagle full
remote access. • Local Threat Intelligence: Develop intelligence
focused on LATAM threat actors to identify attack
QuasarRAT and AsyncRAT are popular tools for patterns and anticipate tactics used by groups
groups like Blind Eagle due to their accessibility like Blind Eagle, allowing for proactive defense
and adaptability—both are open-source and easily strategies.
customizable, making them highly versatile for specific
espionage needs. Additionally, these RATs offer powerful • Workforce Training: Conduct regular phishing drills
capabilities such as keylogging, screen capturing, and and establish a dedicated spam reporting channel
data exfiltration, allowing attackers to capture sensitive for IT/Security, helping employees recognize
information and monitor user behavior effectively. Their phishing attempts and alerting IT to potential threats
built-in evasion techniques, including encryption and in real-time.
obfuscation, enable them to bypass traditional antivirus
software, which is essential for the sustained covert 5.5.5 Techniques, Tactic and Procedures
access needed in targeted espionage campaigns. These
factors make QuasarRAT and AsyncRAT highly effective Blind Eagle employs a distinctive set of TTPs that
tools in Blind Eagle’s operations against financial and combine spear-phishing, sophisticated process injection,
governmental institutions. and custom malware loaders to target LATAM's high-
value sectors. Their campaigns begin with spear-
5.5.3 Correlation phishing emails, often tailored to local government or
financial entities, tricking recipients into downloading
Blind Eagle’s tactics share some overlap with other or opening malicious attachments. These attachments
Latin American-focused threat actors, such as their use commonly deploy RATs like QuasarRAT and AsyncRAT,
of spear-phishing and remote access trojans (RATs) tools enabling Blind Eagle to remotely monitor, control,
for credential theft and espionage. The spear-phishing and extract sensitive data.
242 https://publications.iadb.org/publications/english/document/2020-Cybersecurity-Report-Risks-Progress-and-the-Way-Forward-in-Latin-America-and-the-
Caribbean.pdf
243 https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-insurance-sector-blotchyquasar
64

The group's unique TTPs include advanced process
injection techniques such as process hollowing,
allowing malware to run within legitimate applications’
memory spaces. This technique is critical to Blind
Eagle's strategy, as it allows their malware to blend into
legitimate system processes, reducing the likelihood of
detection by conventional security tools and endpoint
defenses.
Another notable TTP is their use of the Hijack Loader,
a custom-built malware loader that delivers RATs more
covertly by masking its functions. This loader adapts to
a target’s defense system, aiding in both initial evasion
and ongoing access. Their sophisticated, regionally
focused approach also leverages local knowledge to
enhance the believability of their phishing campaigns,
strengthening their initial foothold in high-value targets.
Blind Eagle selects victims based on potential data
value and criticality within LATAM’s infrastructure.
Their persistence techniques and adaptability in RAT
deployment reflect a deliberate, long-term strategy
aimed at extracting data while remaining undetected,
posing an enduring threat to the cybersecurity
landscape of LATAM.
Tactics Techniques Procedures
BlindEagle uses DDNS services to
Resource Development T1583.001 create third-level domains. Those
domains serve as C2.
BlindEagle controlled a Google
Resource Development T1586.002 Drive folder owned by a Colombian,
regional, administration organization.
BlindEagle is operating
BlotchyQuasar, which may be
Resource Development T1587.001
considered a customized variant of
QuasarRAT.
BlindEagle staged a BlotchyQuasar
Resource Development T1608.001 sample on a compromised and
publicly available Google Drive folder.
BlindEagle attempted to gain initial
access to the victim’s system by
Initial Access T1566.002
using a phishing email including a link
to download BlotchyQuasar malware.
BlindEagle renamed the
BlotchyQuasar sample to be
User Execution T1204.002 consistent with the phishing email
lure and push the victim to manually
execute the malware.
65

Tactics Techniques Procedures
BlindEagle’s attack chain starts with
the victim clicking on a link included
User Execution T1204.001
in the email body and in the attached
PDF file.
Blind Eagle is delivered via a phishing
Initial Access T1566 email containing the link to retrieve
the password-protected archive.
Persistence is achieved via the
Persistence T1547.001
Registry Run Keys / Startup folder
The VBS script spawns PowerShell to
Execution T1059.001
execute Ande Loader
Blind Eagle is using process
Defense Evasion, Privilege Escalation T1055.012
hollowing to inject the final payload
DNS
• hXXps://pastebin[.]com/raw/XAfmb6xp
• edificiobaldeares.linkpc[.]net
• equipo.linkpc[.]net
• perfect5.publicvm[.]com
• perfect8.publicvm[.]com
• rxms.duckdns[.]org:57832
• njnjnjs[.]duckdns.org
• 91.213.50[.]74
Hashes
• a73057824a65a5ac982e298a80febf61
• bd4505316254f00329431fb8b2888643
• d2fc372302180fbabe18c425aa4a0a72
• c944cb638364c74431bf1dbe7dd329ff
• 64e6ad512eff12e971efdd8979086c5c
• a1f5091ad4e12f922a8e760e0980ab66
• ad578125b337168c976ff5e7e1b190b8
• e21b4c9d9da81deea2381f9b988b0f99
• 07f661aeeb0774f0cb84b0a5e970c2a5
• c4a946903cc9e9a84763ac1731cdd7dd
• 75a40cc019c39e3c2800fb2fe5aba1d3
• 0fa40788b75896a452398b6a49cc62b6
• 59a4f7aed1e3a0718592fb536e987a1d
• 456211df625002df378cf0f4af9d1a6f
• 0f35306ad4fede9a9ba0276a5e788138
• 6044b126afb86682b4a3440e2924c079
• b432e8ff5797fbaf5808d95d46524647
• a31ff54f33ced7b4180f87afb18185a7
• e3239ac16c6fe9c99d6fac0867121a88
• 2784a9fc64d244b14e7d8e4d03f41265
• 3125ae6b1462b0b48dc06bc47d8ddbc7
• b83f6c57aa04dab955fadcef6e1f4139
• a68cac786b47575a0d747282ace9a4c75e73504d
• ec2dd6753e42f0e0b173a98f074aa41d2640390c163ae77999eb6c10ff7e2edd
• 18eb0a413b80a548d2b615e11fc580cd
66

5.5.6 Blind Eagle Mitigations
Initial Access
• T1566.001 – Spearphishing Attachment
› Mitigation:
» Implement email security gateways with advanced
phishing detection.
» Train users to identify phishing attempts, including
suspicious attachments.
» Enable attachment sandboxing to detect malicious
payloads before delivery.
Execution
• T1204.001 – Malicious Link in Email
• T1204.002 – Malicious File Execution
› Mitigation:
» Enable application whitelisting to prevent unauthorized
execution.
» Use safe browsing solutions that flag malicious links
before clicking.
» Enforce attachment scanning with behavior-based
analysis.
• T1059.001 – Command and Scripting Interpreter: PowerShell
• T1059.003 – Command and Scripting Interpreter: Windows
Command Shell
• T1059.005 – Command and Scripting Interpreter: Visual
Basic
› Mitigation:
» Restrict PowerShell and scripting languages via Group
Policy.
» Enable PowerShell logging (Script Block Logging) to
monitor suspicious scripts.
» Disable macro execution in Office applications unless
necessary.
Persistence
• T1053.005 – Scheduled Task
› Mitigation:
» Monitor and restrict user permission to create scheduled
tasks.
» Regularly audit Task Scheduler logs to detect
unauthorized jobs.
• T1547.001 – Registry Run Keys / Startup Folder
› Mitigation:
» Restrict write access to registry keys used for
persistence.
» Monitor autorun registry entries and startup items for
suspicious modifications.
» Defense Evasion
• T1218.009 – Signed Binary Proxy Execution: Regsvr32
• Mitigation:
» Restrict execution of regsvr32.exe if not required.
» Use application control (Microsoft Defender ASR rules,
AppLocker).
» Monitor child processes spawned by regsvr32.exe for
anomalies.
67

68

Strategic Recommendations for Cybersecurity
6
in Latin America’s Financial Sector
6.1 Implement Regional-Specific Security Controls 6.6 Enhance Third-Party Risk Management &
Monitoring
Financial institutions should adopt security controls
tailored to regional banking architectures and threats. • Establish continuous vendor risk assessments and
compliance checks (ISO 27036, NIST 800-161).
• Establish dedicated threat intelligence teams • Enforce contractual security requirements aligned
analyzing region-specific malware and attack with global cybersecurity standards.
patterns (MITRE ATT&CK, NIST SP 800-53). • Strengthen real-time threat monitoring and
automated incident detection.
• Invest in local threat-hunting capabilities and
collaboration with regional security researchers (ISO 6.7 Harmonize Reporting Requirements
27001, NIST 800-150).
• LATAM should adopt the CRI Profile to streamline
• Conduct red team exercises reflecting local attack regulatory compliance, enhance cyber resilience,
vectors and regulatory requirements (NIST 800- and unify risk management under a standardized
115). framework.244
• Develop a regional cybersecurity framework with
6.2 Establish Financial Sector CSIRT Networks standardized reporting protocols (ISO 29147, NIST
800-61).
• Develop sector-specific incident response teams • Mandate breach disclosure timelines similar to
modeled after Colombia’s financial CSIRT (ISO Brazil’s LGPD.
27035, NIST 800-61). • Establish a unified cybersecurity authority to oversee
• Foster national and regional collaboration through reporting and response efforts.
public-private partnerships.
• Implement structured information-sharing protocols 6.8 Enhance Information Sharing
for real-time threat intelligence.
• Create a secure platform for cross-border threat
6.3 Strengthen Cross-Border Incident Response intelligence sharing.
• Strengthen public-private partnerships for
• Standardize incident response frameworks across coordinated response (NIST 800-150, ISO 27010).
jurisdictions (NIST 800-61, ISO 27035). • Develop cooperation agreements for rapid response
• Establish direct partnerships with regional CERTs to transnational cyber threats.
and international law enforcement.
• Conduct multi-jurisdictional tabletop exercises to 6.9 Strengthen Cybersecurity Infrastructure
test response readiness.
• Allocate 2-3% of GDP to cybersecurity initiatives
6.4 Strengthen Human-Centric Security Awareness (OECD cybersecurity recommendations).
• Enforce strong encryption standards and MFA
• Implement role-specific cybersecurity training and across critical sectors (NIST 800-175, ISO 27001).
phishing simulations (NIST 800-50, ISO 27002). • Develop national cybersecurity strategies prioritizing
• Enforce strong authentication measures, including critical infrastructure protection.
MFA and secure credential hygiene (NIST 800-63,
ISO 27001). 6.10 Improve Cybersecurity Education and
• Foster a security-first culture to mitigate social Workforce Development
engineering risks.
• Launch industry-specific cybersecurity education
6.5 Secure Digital Transformation & Access Control programs (NIST NICE framework, ISO 27021).
• Conduct regular cybersecurity drills to test resilience
• Integrate Zero Trust Architecture (NIST SP 800-207) (NIST 800-84).
to enforce least privilege access. • Establish certification programs to build a skilled
• Implement adaptive MFA and biometric workforce.
authentication (ISO 27001, NIST 800-63B).
• Upgrade outdated systems with secure-by-design
principles to meet regulatory standards.
244 https://cyberriskinstitute.org/the-profile/
69

6.11 Strengthen Regulatory Frameworks
• Enforce comprehensive data protection laws
where lacking (ISO 27701, GDPR, NIST Privacy
Framework).
• Implement stricter penalties for non-compliance with
breach reporting.
• Regularly update cybersecurity regulations to align
with emerging threats and technologies.
6.12 Foster International Collaboration
• Participate in global cybersecurity forums to
exchange best practices (ENISA, ITU Global
Cybersecurity Index).
• Strengthen cooperation with international law
enforcement to combat cybercrime (Budapest
Convention on Cybercrime).
• Seek technical assistance from countries with
advanced cybersecurity capabilities.
These measures, aligned with international best
practices, will strengthen Latin America’s financial sector
against emerging cyber threats, fostering resilience and
trust in the region’s digital economy.
70

7
Appendix
7.1 Segmented Data
These Threat IDs commonly referred as Techniques are the commonalities between all three threat actors.
CLOP Data for MITER
Recon: tactics
| mitre:T1592     | T1592     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1589.002 | T1589.002 | MitreAttackIdentifier |
| mitre:T1589.001 | T1589.001 | MitreAttackIdentifier |
| mitre:T1589     | T1589     | MitreAttackIdentifier |
| mitre:T1590     | T1590     | MitreAttackIdentifier |
| mitre:TA0043    | TA0043    | MitreAttackIdentifier |

Resource Development:
| mitre:T1586 | T1586 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |

Initial Access:
| mitre:T1190     | T1190     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1133     | T1133     | MitreAttackIdentifier |
| mitre:T1566     | T1566     | MitreAttackIdentifier |
| mitre:T1078.003 | T1078.003 | MitreAttackIdentifier |
| mitre:T1091     | T1091     | MitreAttackIdentifier |
| mitre:TA0001    | TA0001    | MitreAttackIdentifier |

Execution:
| mitre:T1059     | T1059     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1059.001 | T1059.001 | MitreAttackIdentifier |
| mitre:T1059.003 | T1059.003 | MitreAttackIdentifier |
| mitre:T1106     | T1106     | MitreAttackIdentifier |
| mitre:T1053.003 | T1053.003 | MitreAttackIdentifier |
| mitre:T1053.005 | T1053.005 | MitreAttackIdentifier |
| mitre:T1204.002 | T1204.002 | MitreAttackIdentifier |
| mitre:T1047     | T1047     | MitreAttackIdentifier |

Persistence:
| mitre:T1098     | T1098     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1547.001 | T1547.001 | MitreAttackIdentifier |
| mitre:T1037.004 | T1037.004 | MitreAttackIdentifier |
| mitre:T1136     | T1136     | MitreAttackIdentifier |
| mitre:T1543.002 | T1543.002 | MitreAttackIdentifier |
| mitre:T1133     | T1133     | MitreAttackIdentifier |
| mitre:T1574.002 | T1574.002 | MitreAttackIdentifier |
71

| mitre:T1053.003 | T1053.003 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1053.005 | T1053.005 | MitreAttackIdentifier |
| mitre:T1505     | T1505     | MitreAttackIdentifier |
| mitre:T1505.001 | T1505.001 | MitreAttackIdentifier |
| mitre:T1505.003 | T1505.003 | MitreAttackIdentifier |
| mitre:T1078     | T1078     | MitreAttackIdentifier |
| mitre:T1078.003 | T1078.003 | MitreAttackIdentifier |

Privilege Escalation:
| mitre:T1548.002 | T1548.002 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1098     | T1098     | MitreAttackIdentifier |
| mitre:T1547.001 | T1547.001 | MitreAttackIdentifier |
| mitre:T1037.004 | T1037.004 | MitreAttackIdentifier |
| mitre:T1543.002 | T1543.002 | MitreAttackIdentifier |
| mitre:T1068     | T1068     | MitreAttackIdentifier |
| mitre:T1574.002 | T1574.002 | MitreAttackIdentifier |
| mitre:T1053.003 | T1053.003 | MitreAttackIdentifier |
| mitre:T1053.005 | T1053.005 | MitreAttackIdentifier |
| mitre:T1078.003 | T1078.003 | MitreAttackIdentifier |
| mitre:T1078     | T1078     | MitreAttackIdentifier |

Defense Evasion:
| mitre:T1222.002 | T1222.002 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1497.001 | T1497.001 | MitreAttackIdentifier |
| mitre:T1078.003 | T1078.003 | MitreAttackIdentifier |
| mitre:T1078     | T1078     | MitreAttackIdentifier |
| mitre:T1218.007 | T1218.007 | MitreAttackIdentifier |
| mitre:T1218.010 | T1218.010 | MitreAttackIdentifier |
| mitre:T1218.011 | T1218.011 | MitreAttackIdentifier |
| mitre:T1553.002 | T1553.002 | MitreAttackIdentifier |
| mitre:T1112     | T1112     | MitreAttackIdentifier |
| mitre:T1070.002 | T1070.002 | MitreAttackIdentifier |
| mitre:T1574.002 | T1574.002 | MitreAttackIdentifier |
| mitre:T1140     | T1140     | MitreAttackIdentifier |
| mitre:T1622     | T1622     | MitreAttackIdentifier |
| mitre:T1548.002 | T1548.002 | MitreAttackIdentifier |

Credential Access:
| mitre:T1003.001 | T1003.001 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1552.007 | T1552.007 | MitreAttackIdentifier |

72

Discovery:
| mitre:T1622 | T1622 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |
| mitre:T1083 | T1083 | MitreAttackIdentifier |
| mitre:T1135 | T1135 | MitreAttackIdentifier |
| mitre:T1057 | T1057 | MitreAttackIdentifier |
| mitre:T1012 | T1012 | MitreAttackIdentifier |
| mitre:T1082 | T1082 | MitreAttackIdentifier |

Lateral Movement:
| mitre:T1021     | T1021     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1021.001 | T1021.001 | MitreAttackIdentifier |
| mitre:T1021.002 | T1021.002 | MitreAttackIdentifier |
| mitre:T1021.004 | T1021.004 | MitreAttackIdentifier |
| mitre:T1021.006 | T1021.006 | MitreAttackIdentifier |
| mitre:T1091     | T1091     | MitreAttackIdentifier |

Collection:
| mitre:T1005 | T1005 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |

C&C:
| mitre:T1071.001 | T1071.001 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1573.001 | T1573.001 | MitreAttackIdentifier |
| mitre:T1105     | T1105     | MitreAttackIdentifier |
| mitre:T1104     | T1140     | MitreAttackIdentifier |
| mitre:T1571     | T1571     | MitreAttackIdentifier |

Exfiltration:
| mitre:T1041     | T1041     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1052.001 | T1052.001 | MitreAttackIdentifier |
| mitre:T1567.002 | T1567.002 | MitreAttackIdentifier |

Impact:
| mitre:T1485 | T1485 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |
| mitre:T1486 | T1486 | MitreAttackIdentifier |
| mitre:T1565 | T1565 | MitreAttackIdentifier |
| mitre:T1496 | T1496 | MitreAttackIdentifier |
| mitre:T1489 | T1489 | MitreAttackIdentifier |

MITER Mobile:
| mitre:T1406.002 | T1406.002 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |

73

LockBit Data for MITER
1. Recon:
2. Resource Development:
3. Initial Access:
| mitre:T1190 | T1190 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |
| mitre:T1078 | T1078 | MitreAttackIdentifier |

4. Execution:
| mitre:T1059 | T1059 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |

5. Persistence:
| mitre:T1543 | T1543 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |

6. Privilege Escalation:
7. Defense Evasion:
| mitre:T1562 | T1562 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |

8. Credential Access:
| mitre:T1003 | T1003 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |

9. Discovery:
| mitre:T1087 | T1087 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |

10. Lateral Movement:
| mitre:T1021.001 | T1021.001 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |

11. Collection:
| mitre:T1560 | T1560 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |

12. C&C:
13. Exfiltration:
14. Impact:
| mitre:T1486 | T1486 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |

Mispadu Data for MITER
1. Recon:
2. Resource Development:
3. Initial Access:
| mitre:T1566     | T1566     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1566.001 | T1566.001 | MitreAttackIdentifier |
| mitre:T1190     | T1190     | MitreAttackIdentifier |

74

4. Execution:
| mitre:T1204     | T1204     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1204.002 | T1204.002 | MitreAttackIdentifier |

5. Persistence:
6. Privilege Escalation:
| mitre:T1055.012 | T1055.012 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1055.013 | T1055.013 | MitreAttackIdentifier |

7. Defense Evasion:
| mitre:T1036 | T1036 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |
| mitre:T1027 | T1027 | MitreAttackIdentifier |

8. Credential Access:
| mitre:T1056.001 | T1056.001 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1056.003 | T1555.003 | MitreAttackIdentifier |

9. Discovery:
| mitre:T1082 | T1082 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |
| mitre:T1083 | T1083 | MitreAttackIdentifier |

10. Lateral Movement:
11. Collection:
| mitre:T1005 | T1005 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |
| mitre:T1113 | T1113 | MitreAttackIdentifier |

12. C&C:
| mitre:T1573     | T1573     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1105     | T1105     | MitreAttackIdentifier |
| mitre:T1102.002 | T1102.002 | MitreAttackIdentifier |

13. Exfiltration:
| mitre:T1041 | T1041 | MitreAttackIdentifier |
| ----------- | ----- | --------------------- |
| mitre:T1567 | T1567 | MitreAttackIdentifier |

Horabot Data for Miter
1. Recon:
2. Resource Development:
| mitre:T1584     | T1584     | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1584.005 | T1584.005 | MitreAttackIdentifier |

75

3. Initial Access:
| mitre:TA0001    | TA0001    | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1566     | T1566     | MitreAttackIdentifier |
| mitre:T1566.001 | T1566.001 | MitreAttackIdentifier |
| mitre:T1190     | T1190     | MitreAttackIdentifier |
| mitre:T1078     | T1078     | MitreAttackIdentifier |

4. Execution:
| mitre:TA0002    | TA0002    | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:TA1059    | TA1059    | MitreAttackIdentifier |
| mitre:T1059.001 | T1059.001 | MitreAttackIdentifier |
| mitre:T1204     | T1204     | MitreAttackIdentifier |
| mitre:T1204.001 | T1204.001 | MitreAttackIdentifier |
| mitre:T1106     | T1106     | MitreAttackIdentifier |

5. Persistence:
| mitre:TA0003    | TA0003    | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1574     | T1574     | MitreAttackIdentifier |
| mitre:T1574.002 | T1574.002 | MitreAttackIdentifier |
| mitre:T1547.009 | T1547.009 | MitreAttackIdentifier |
| mitre:T1547.001 | T1547.001 | MitreAttackIdentifier |

6. Privilege Escalation:
| mitre:TA0004 | TA0004 | MitreAttackIdentifier |
| ------------ | ------ | --------------------- |

7. Defense Evasion:
| mitre:TA0005    | TA0005    | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1036     | T1036     | MitreAttackIdentifier |
| mitre:T1027     | T1027     | MitreAttackIdentifier |
| mitre:T1497     | T1497     | MitreAttackIdentifier |
| mitre:T1070     | T1070     | MitreAttackIdentifier |
| mitre:T1070.004 | T1070.004 | MitreAttackIdentifier |

8. redential Access:
| mitre:T1056.001 | T1056.001 | MitreAttackIdentifier |
| --------------- | --------- | --------------------- |
| mitre:T1003     | T1003     | MitreAttackIdentifier |
| mitre:T1083     | T1083     | MitreAttackIdentifier |

9. Discovery:
| mitre:TA0007 | TA0007 | MitreAttackIdentifier |
| ------------ | ------ | --------------------- |
| mitre:T1082  | T1082  | MitreAttackIdentifier |

76

10. Lateral Movement:
11. Collection:
| mitre:TA0009 | TA0009 | MitreAttackIdentifier |
| ------------ | ------ | --------------------- |
| mitre:T1115  | T1115  | MitreAttackIdentifier |
| mitre:T1113  | T1113  | MitreAttackIdentifier |

12. C&C:
| mitre:TA0011 | TA0011 | MitreAttackIdentifier |
| ------------ | ------ | --------------------- |

13. Exfiltration:
14. Impact:
| mitre:TA0040 | TA0040 | MitreAttackIdentifier |
| ------------ | ------ | --------------------- |

77

7.2 Definitions Worms: Self-replicating malware that spreads rapidly
across networks, potentially damaging files or installing
Tactics, Techniques, and Procedures: The most additional malware.
common behaviors, strategies, and methods used by
attackers to develop and execute cyber-attacks on Rootkits: Software that provides an attacker with
financial institutions.245 stealthy, persistent control over a compromised system.
Phishing: Phishing is a type of pf cyber-attack where the Mobile Malware: Malicious software specifically
attacker uses various techniques to lure victims to reveal designed to target mobile devices, often delivered
their personal or business-related information. Various through malicious apps or compromised networks.
types of phishing include:
Exploits: Software or code that takes advantage of
1. Spear Phishing: Spear phishing is a type of attack vulnerabilities in operating systems or applications to
in which individuals from organizations are targeted, gain unauthorized access.249
usually through a malicious link prompting them to
reveal login credentials. This leads to unauthorized Scareware: Malware that attempts to frighten users into
third-party access to the company's data. believing their systems are infected, often promoting
fake antivirus software.
2. Whaling: Whaling is a phishing attack targeting
C-level executive members/ employees to reveal Keyloggers: Software that records keystrokes entered
sensitive information.246 on a device, potentially capturing sensitive information.
3. Smishing: Smishing is a type of attack where the Botnets: Networks of compromised devices controlled
attacker sends malicious or fraudulent messages/ by an attacker to launch various malicious activities.
links through messages, and in most cases, people
are lured into revealing usernames, passwords, etc. Malspam: Spam emails containing malicious
attachments or links designed to deliver malware.
4. Vishing: Voice Phishing is commonly known
as Vishing. Here, attackers make fraudulent calls Wiper Attacks: Malware designed to permanently delete
representing organizations and lure them into or corrupt data on targeted systems, often used in
revealing their data using manipulation. cyberwarfare or hacktivism.
Malware: This is malicious software or a program or just DOS/DDOS: Denial-of-Service (DoS) attacks are cyber
a tiny piece of code which exploits a vulnerability. attacks aimed at disrupting a network, server, or website
by overwhelming traffic. This can render the target
Ransomware: A malicious software that encrypts a inaccessible to legitimate users. Distributed Denial-of-
victim's data and demands a ransom for decryption. Service (DDoS) attacks are a more sophisticated variant
Often delivered through phishing emails or exploited of DoS attacks. They involve coordinating multiple
vulnerabilities. compromised systems (known as bots) to launch
simultaneous attacks on a target, amplifying the Impact
Fileless Malware: Malware that operates without and making it more difficult to defend against.
installing any files on the infected system, making
detection difficult. Injection Attacks: Injection attacks are a type of cyber
attack where malicious code is inserted into a vulnerable
Spyware: Software that secretly monitors a user's online application or system. This can lead to a variety of
activity to collect sensitive information. harmful consequences, including unauthorized access,
data theft, and system disruption.250
Adware: A type of spyware that displays unwanted
advertisements to the user.247
Trojans: Malicious programs disguised as legitimate
software, often downloaded through social engineering
tactics.248
245 https://www.nextias.com/ca/current-affairs/14-09-2023/cybercrime-investigation-tool)
246 https://es.cryoserver.com/blog/how-to-avoid-phishing-scams/
247 https://top10antivirus.site/the-intricacies-of-spyware-a-breakdown-of-their-invasive-techniques/
248 https://softwarelab.org/best-antivirus-with-firewall/
249 https://www.mobiletracker.org/law-enforcement-implications-in-hacking-mobile-devices_wpg_881/
250 https://www.securityjourney.com/post/owasp-top-10-injection-attacks-explained
78

Common Types of Injection Attacks: • Provides threat intelligence and vulnerability
information specifically tailored for the financial
• SQL Injection: Exploiting vulnerabilities in SQL sector.
queries to execute unauthorized commands.
• Shares indicators of compromise and threat
• Command Injection: Executing arbitrary intelligence to help financial institutions protect
commands on the operating system through themselves.
vulnerable input parameters.
MITRE ATT&CK Framework:
• Cross-Site Scripting (XSS): Injecting malicious
scripts into web pages to steal user data or hijack
• Provides a knowledge base of adversary tactics and
sessions.251
techniques based on real-world observations.255
• XML Injection: Exploiting vulnerabilities in XML
• Used by financial institutions to understand and
processing to inject malicious XML code.
defend against sophisticated attack methods.
• LDAP Injection: Injecting malicious LDAP queries
to gain unauthorized access to directory services. 7.4 Indicators of Compromise (IOCs)
7.3 Common Vulnerabilities, Exposures, and • File Hashes: Unique values representing files that
Indicators of Compromise might be used to detect malicious activity.
• IP Addresses: Addresses associated with known
The most common glossary of classified vulnerabilities
malicious activities.
in financial institutions has been analyzed and evaluated
based on the threat level of the vulnerability. Managing • URLs/Domains: Attackers use web addresses to
vulnerabilities and threats is crucial for financial control malware or exfiltrate data.
institutions due to the sensitive nature of the data they
• Email Addresses: Addresses involved in phishing or
handle.252 Here are some commonly used glossaries and
other email-based attacks.
frameworks for classified vulnerabilities and indicators of
compromise (IoCs).
These tools and frameworks help financial institutions
effectively manage and mitigate cybersecurity threats,
Common Vulnerabilities and Exposures (CVE):
ensuring the protection of their sensitive data.
• A standardized list of publicly known cybersecurity
7.5 Forensic Evidence
vulnerabilities.
• Each CVE entry includes an identification number, The top three forensic evidence of potential intrusions on
a description, and references to related security a host system or network for Financial Institutions.256
advisories.
• Privilege Escalation: This indicates that an attacker
• Financial institutions use CVE to track and assess
has gained higher-level access than initially
vulnerabilities in their systems.
intended, allowing them to execute more damaging
• Common Vulnerability Scoring System (CVSS): actions.
• A framework for assessing the severity of • Lateral Movement: This shows that an attacker has
vulnerabilities.253 moved from one compromised system to another
within the network, potentially spreading malware or
• It assigns a score based on exploitability and
gaining access to sensitive data.
Impact, helping institutions prioritize their response.
• Exfiltration of Data: This is the most critical sign of
• National Vulnerability Database (NVD):
a successful intrusion, as it means that sensitive
• A U.S. government repository of vulnerability data has been stolen and may be used for malicious
management data, including CVE entries, CVSS purposes.
scores, and additional metadata.
• Widely used by financial institutions for vulnerability
assessment and management.
• Financial Services Information Sharing and Analysis
Center (FS-ISAC):254
251 https://datapacket.net/website-security/
252 https://neovera.com/cybersecurity-outlook-for-financial-institutions/
253 https://hadrian.io/blog/tag/security-solutions
254 https://www.ibm.com/reports/threat-intelligence
255 https://nsarchive.gwu.edu/media/29421/ocr
256 https://core.ac.uk/download/346450152.pdf
79

81