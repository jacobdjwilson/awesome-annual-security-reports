# State of Apps and API Security 2025

## Table of Contents
- [Introduction](#introduction)
- [Key insights of the report](#key-insights-of-the-report)
- [Evolving our API threat intelligence](#evolving-our-api-threat-intelligence)
- [Web attacks: Year-over-year comparison and trends](#web-attacks-year-over-year-comparison-and-trends)
- [Layer 7 DDoS attacks: Year-over-year comparison and trends](#layer-7-ddos-attacks-year-over-year-comparison-and-trends)
- [Industry trends](#industry-trends)
- [Regional trends](#regional-trends)
- [Compliance](#compliance)
- [Mitigation](#mitigation)
- [Methodology](#methodology)
- [Credits](#credits)

---

## Introduction
The web application security landscape in early 2025 reflects unprecedented complexity and sophistication in threat vectors. Organizations are confronting a marked increase in attacks that target web applications — Akamai observed more than 311 billion web application and API attacks in 2024 alone, representing a 33% year-over-year increase. This surge correlates directly with the accelerated adoption of cloud services, microservices architectures, and artificial intelligence (AI)–powered applications. Geopolitical factors have further intensified this landscape, with the high technology, commerce, and social media industries experiencing the most significant volume of Layer 7 (application-layer) distributed denial-of-service (DDoS) attacks. Notably, threat actors are now deploying AI-generated kill chains that automate the entire attack lifecycle.

Concurrently, APIs have emerged as primary targets, with Akamai documenting more than 150 billion API attacks from January 2023 through December 2024. The integration of AI-driven software as a service (SaaS) tools with core platforms via APIs has substantially expanded the attack surface. The financial implications are severe — API security issues currently cost organizations approximately US$87 billion annually, and projections indicate that this figure could exceed US$100 billion by 2026 without adequate intervention. Shadow and zombie APIs present particularly vulnerable attack vectors within increasingly complex API ecosystems.

### The role of AI in web application and API security
AI is transforming both web application and API security landscapes by enhancing threat detection and response capabilities, while also introducing new challenges. In web applications, AI is used to automate threat detection, predict potential breaches, and improve incident response times. However, AI also enables attackers to generate AI-driven malware and sophisticated web scraping and to automate the attack lifecycle with dynamic attack methodologies.

For APIs, AI plays a crucial role in managing and securing the vast number of API interactions. AI-powered tools are essential for detecting anomalies, identifying misuse patterns, and automating responses to threats in real time. AI-driven API management will continue to evolve by integrating predictive analytics and automated security measures to protect against increasingly sophisticated attacks. Despite these advancements, AI-powered attacks on APIs, such as credential stuffing and business logic exploits, remain a significant concern, necessitating robust security frameworks to counter these threats effectively.

### Divergent yet interconnected: Web application and API attack strategies
Web application attacks and API attacks, while related, target different aspects of an application’s infrastructure:
- **Web application attacks** target user-facing components of web applications, such as public-facing login pages, and often employ less sophisticated techniques.
- **API attacks** focus on exploiting vulnerabilities in an application’s API endpoints and back-end logic, requiring a deeper understanding of the API’s structure and behavior.

The key differences lie in their attack surface and complexity. Web application attacks typically target the visible parts of an application, while API attacks exploit the communication channels among different software components. However, they can both provide unauthorized access to sensitive data and system resources when successful.

Understanding cybersecurity measures for both web application and API attacks simultaneously is critical because modern applications increasingly rely on APIs for functionality. Organizations expect a 39% increase in web applications within two years, so the interdependence of web and API security has become more pronounced. Neglecting either aspect can leave an organization vulnerable to sophisticated, multi-vector attacks that exploit weaknesses in both the front end and back end of applications.

### Akamai’s unique perspective: Unveiling threat patterns
Akamai’s analysis of this complexity benefits from its network infrastructure, which processes more than one-third of global web traffic, providing unmatched visibility into threat patterns. This perspective, combined with insights from its research and data science teams, enables Akamai to deliver intelligence that is both comprehensive and actionable. Its findings offer security leaders the strategic insights necessary to make decisions on where to focus on reducing risks to maximize the return on security investments.

---

## Key insights of the report
- **AI-powered APIs are more unsecure than their counterparts.** The majority of artificial intelligence (AI)–powered APIs are externally accessible and many rely on inadequate authentication mechanisms — a vulnerability that’s compounded by the growing array of AI-driven attacks that are targeting them.
- **AI fuels technical advancement for threat actors.** This includes advancements like AI-driven malware, vulnerability scanning, attacks on AI-integrated systems, and sophisticated web scraping capabilities.
- **32% increase in OWASP API Security Top 10–related incidents.** API security incidents are rising, with Open Worldwide Application Security Project (OWASP) API Security Top 10 issues revealing authentication and authorization flaws that expose sensitive data and functionality.
- **30% growth in security alerts related to the MITRE security framework.** Attackers are using advanced techniques, including automation and AI, to exploit APIs. The MITRE framework can help defenders more quickly and accurately identify these attacks.
- **33% increase in global web attacks year over year.** The surge in attacks directly correlates with the rapid adoption of cloud services, microservices, and AI applications, which expand attack surfaces and introduce new security challenges.
- **230 billion+ web attacks hit commerce organizations.** This makes it the most impacted industry with nearly triple the number of attacks experienced by high technology (the second most attacked industry).
- **73% increase in total web attacks year over year in the APJ region.** Rising from 29 billion in 2023 to 51 billion in 2024.
- **37% of web attacks in the EMEA region targeted APIs.** This is the highest concentration of such attacks across all regions.
- **94% growth in quarterly Layer 7 DDoS attacks.** Measured between Q1 2023 and Q4 2024.
- **11.9 trillion Layer 7 DDoS attacks targeted North America.** During the two-year period Q1 2023 through Q4 2024.
- **7 trillion Layer 7 DDoS attacks targeted the high technology industry.** From January 2023 through December 2024, making it the most affected industry.
- **7.4 trillion Layer 7 DDoS attacks targeted the APJ region.** During the two-year period Q1 2023 through Q4 2024.
- **20% of Layer 7 DDoS API-related attacks targeted the EMEA region.** Representing the highest concentration of this attack type across all regions.

---

## Evolving our API threat intelligence
Akamai’s integration of Noname Security has significantly enhanced our API threat research and reporting capabilities, offering a fresh perspective on API-specific risks. Akamai is using this new dataset (still in the early stages of data integration) to enhance our existing threat intelligence and provide an expanded view of API security issues.

### Mapping alerts to security frameworks
Over time, this new dataset will map deeper security alert details to critical cybersecurity frameworks and compliance standards, including the:
- MITRE Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK)
- General Data Protection Regulation (GDPR)
- Payment Card Industry Data Security Standard (PCI DSS)
- International Organization for Standardization (ISO)
- Open Worldwide Application Security Project (OWASP)

These enhancements significantly strengthen Akamai’s ability to provide robust protection for clients. By aligning with these frameworks, organizations can gain a clearer understanding of their security posture, meet regulatory requirements, and effectively prioritize their security efforts.

### Analyzing a 30-day data sample
For this report, we’ve analyzed a 30-day data sample to highlight general activity by threat actors across each of the cybersecurity frameworks and compliance standards.

| Framework/Standard | 30-Day Activity | Monthly Increase |
| :--- | :--- | :--- |
| OWASP | 5,907,000 | 32% |
| MITRE | 2,817,000 | 30% |
| ISO | 832,000 | 22% |
| GDPR | 669,000 | 21% |
| PCI DSS | 881,000 | 16% |

![Breakdown of security alerts according to security frameworks and compliance standards]

### MITRE alerts
Over a 30-day period, we observed a 30% increase in incidents related to MITRE techniques among our customers. Notably, attackers frequently employed T1078 (Valid Accounts), leveraging legitimate credentials to gain unauthorized access. We also identified T1566 (Phishing), T1190 (Exploit Public-Facing Application), and T1580 (Cloud Infrastructure Discovery).

### OWASP alerts
During the 30-day sample period, our analysis revealed a 32% increase in OWASP-related incidents. Notably, vulnerabilities such as Broken Object Property Level Authorization (BOPLA), Broken Function Level Authorization, and Broken Authentication expose sensitive data or critical functions directly to attackers.

- **Broken Object Level Authorization (BOLA)**: Remains a critical API security vulnerability, but its detection is challenging due to its reliance on business logic flaws.
- **BOPLA**: Exploits granular field-level access issues in APIs, which are often overlooked during security testing.
- **Unrestricted Resource Consumption**: Attackers can exploit this to cause service disruptions through resource exhaustion or DDoS-like attacks.
- **Unsafe consumption of APIs**: Stems from inadequate validation, filtering of data, and lack of security mechanisms during third-party API integrations.

---

## Web attacks: Year-over-year comparison and trends
Akamai’s research revealed a substantial increase in web attacks that targeted web applications and APIs during the reporting period of January 2023 through December 2024. Monthly attack volumes increased from nearly 14 billion at the beginning of 2023 to more than 29 billion by October 2024. This represents a 65% growth in web attacks from Q1 2023 through Q4 2024.

![Monthly Web Attacks chart]

### API request constraint violations: A growing threat
A comprehensive analysis of API endpoints over a two-year period reveals that API request constraint violations represent an area of concern for organizations. These violations manifest when requests or responses fail to adhere to predefined parameters or established requirements. More than 83 billion request constraint violations were recorded in two years, a 24% surge from 2023 to 2024.

### Active attack sessions
Akamai’s solutions employ a proprietary mechanism to detect active attack sessions. The system flags threat actors and implements a “penalty box” approach. In 2023, it accounted for more than 69 billion attacks. This figure surged to more than 113 billion attacks in 2024, a 63% year-over-year increase.

---

## Layer 7 DDoS attacks: Year-over-year comparison and trends
From January 2023 through December 2024, Akamai research documented a dramatic rise in Layer 7 (application-layer) DDoS attacks against web applications and APIs. Monthly attack volumes surged from slightly over 500 billion in early 2023 to more than 1.1 trillion by December 2024. This represents a 94% growth in Layer 7 DDoS attacks from Q1 2023 through Q4 2024.

![Monthly Layer 7 DDoS Attacks chart]

---

## Industry trends
Among industries, commerce towered over all the others with nearly triple the number of overall web attacks experienced as high technology (the second most attacked industry) from Q1 2023 through Q4 2024.

- **Commerce**: Incurred more than 230 billion web attacks and more than 4.8 trillion Layer 7 DDoS attacks during 2023 and 2024.
- **Financial Services**: Totaled more than 79 billion web attacks and more than 761 billion Layer 7 DDoS attacks.
- **High Technology**: Experienced more than 81.7 billion web attacks and more than 7 trillion Layer 7 DDoS attacks.

---

## Regional trends
We have categorized regional reporting into North America, APJ, EMEA, and LATAM.

- **EMEA**: Experienced the highest concentration of web attacks on APIs (37% of 116 billion total web attacks).
- **APJ**: Experienced the second highest level of Layer 7 DDoS attacks globally at 7.4 trillion.
- **North America**: Recorded 327 billion total web attacks, with 29% targeting APIs.

![Regions at a glance table]

---

## Compliance
Compliance standards serve as essential guardrails for organizations to protect sensitive data.
- **GDPR**: Emphasizes integrating data protection and customer privacy throughout the entire API lifecycle.
- **PCI DSS**: Mandates protection against web vulnerabilities and regular testing for APIs handling payment card data.
- **ISO 27001**: Provides a framework for managing information security risks, including access control and end-to-end encryption.

---

## Mitigation
To counter the evolving threat landscape, organizations should:
1. Implement a Zero Trust security model.
2. Utilize advanced API discovery and monitoring solutions to identify shadow and zombie APIs.
3. Conduct frequent automated testing during development cycles.
4. Deploy AI-powered WAF systems to proactively identify and mitigate zero-day threats and bot-driven attacks.
5. Enforce strict rate limiting, logging, and role-based access control (RBAC).

---

## Methodology
This report is based on data collected from the Akamai Intelligent Edge Platform, which processes more than one-third of global web traffic. The analysis covers the period from January 1, 2023, through December 31, 2024.

---

## Credits
State of Apps and API Security 2025 | Volume 11, Issue 02 | Akamai.com

---

on, we highlight some key trends within APJ, EMEA, and LATAM. We also include
data specific to areas within these regions where we have sufficient attack event data to
provide statistically significant insights.
Web application and API attacks: Traffic analysis
A comparison of monthly web attack trends between regions is a study in contrasts (Figure 12).
APJ: Monthly Web Attacks
January 1, 2023 – December 31, 2024
7B
6B
5B
4B
3B
2B
1B
0B
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 29
tnuoC
kcattA
APJ: Monthly Web Attacks
January 1, 2023 – December 31, 2024
Target Web App API
January 2
023
April 2
023
July 2
023
October 2
023
January 2
024
April 2
024
July 2
024
October 2
024

EMEA: Monthly Web Attacks
January 1, 2023 – December 31, 2024
7B
6B
5B
4B
3B
2B
1B
0B
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 30
tnuoC
kcattA
EMEA: Monthly Web Attacks
January 1, 2023 – December 31, 2024
Target Web App API
January 2
023
April 2
023
July 2
023
October 2
023
January 2
024
April 2
024
July 2
024
October 2
024
LATAM: Monthly Web Attacks
January 1, 2023 – December 31, 2024
2.5B
2.0B
1.5B
1.0B
0.5B
0B
tnuoC
kcattA
LATAM: Monthly Web Attacks
January 1, 2023 – December 31, 2024
Target Web App API
January 2
023
April 2
023
July 2
023
October 2
023
January 2
024
April 2
024
July 2
024
October 2
024
Fig. 12: Web application attack activity drove an increase in the total number of web attacks
in APJ and EMEA, while attacks in LATAM declined steeply
APJ experienced a significant 73% increase in total web attacks year over year, from 29
billion in 2023 to 51 billion in 2024. In EMEA, the year-over-year increase was a moderate
16% (from 54 billion to 62 billion) — but this smaller increase is affected by an outlier event
recorded in the data that, if removed, would boost the number closer to 33%. In LATAM,
web attacks dropped considerably from a total of 16 billion in 2023 to 6 million in 2024,
a 61% year-over-year decrease.

Growth in web application attacks appears to be driving an increase in total web attack counts
since API attacks remained at low levels, particularly in APJ and LATAM.
In EMEA, following the spike in the first half of 2023 (which was related to large-scale focused
attacks on the commerce sector in Spain), API attack levels declined and remained at lower
levels throughout 2024, though they were still comparatively high with respect to other regions.
In LATAM, web attacks declined as threat actors shifted their focus from the commerce sector
to other industries, including pharmaceuticals and business services, and to other attack types
such as ransomware.
Web application and API attacks: Trending tactics
Over the last two years, threat actors continued to rely on traditional tried-and-true methods,
but modern, behavioral-based web attack vector use was also high (Figure 13).
APJ: Web Attacks by Vector
APJ: Web Attacks by Vector
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024
Target Web App API
Active Attack
Session
Local File
Inclusion
Cross-Site
Scripting
SQL Injection
Web Attack Tool
0B 5B 10B 15B 20B 25B 30B
Attack Count
EMEA: Web Attacks by Vector
EMEA: Web Attacks by Vector
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024
Target Web App API
Active Attack
Session
API Request
Constraint Violation
Local File
Inclusion
Web Attack Tool
SQL Injection
0B 10B 20B 30B 40B
Attack Count
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 31

LALTAATMA:M W: Webe Ab tAttatcakcsk sb by yV Veecctotorr
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024
Target Web App API
Active Attack
Session
Web Attack Tool
Server-Side
Request Forgery
Data Harvesting
SQL Injection
0B 1B 2B 3B 4B 5B 6B 7B 8B 9B
Attack Count
Fig. 13: Across the regions, top attack vectors included traditional methods and
modern behavioral-based methods specifically aimed at API abuse
Consistent with global trends, across the regions, traditional attack vectors persist, including
LFI, SQLi, and XSS, along with SSRF observed in LATAM. We underscored the staying power
of XSS and its continued relevance for protection against traditional web vulnerabilities in our
Defenders’ Guide 2025.
What’s different during this period, as threat actors increasingly focus on API abuse, is the
increase in issues with modern, behavioral-based attack vectors. Threat actors use these
vectors to discover vulnerabilities to exploit. Tracking these vectors at a regional level,
Akamai researchers observed:
Ź The top attack vector in each region was active attack session, for which our
intelligent controls are used to proactively block requests from known threat actors
for a length of time.
Ź API request constraint violation was the second most prevalent in EMEA, where the
concentration of API-focused attacks is greatest. Attackers attempt to abuse APIs
by evading requirements such as rate limits and data inputs.
Ź In each region, web attack tool was in the top five. Threat actors use this vector to
probe the target to solicit information about its security, configurations, or potential
vulnerabilities that could be leveraged for nefarious purposes.
For more details on these top vectors, see the Web attacks section.
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 32

Web application and API attacks: Top targets
By looking specifically at where attackers focused within each region, we see that in APJ,
Australia (20.3 billion), India (17.3 billion), and Singapore (15.9 billion) bore the brunt of web
application and API attacks, followed by Japan (6.3 billion), China (6.2 billion), South Korea
(4.9 billion), New Zealand (2.9 billion), and Hong Kong SAR (2.2 billion).
In EMEA, the countries most impacted by web application and API attacks were the United
Kingdom (30.3 billion), the Netherlands (19.5 billion), Spain (14.2 billion), and Germany (12.8
billion). Austria followed at 8.2 billion, along with France (7.5 billion), Italy (4.1 billion),
Switzerland (3.7 billion), Belgium (3.5 billion), and Israel (3.3 billion).
In LATAM, web application and API attack volume was concentrated in Brazil (19.3 billion),
with the next closest countries, Mexico (2.0 billion) and Chile (0.4 billion), experiencing just
a fraction of attacks in the region.
Industry targets
Analysis by industry trends found that across APJ, EMEA, and LATAM, commerce and financial
services were consistently among the top three industries targeted by web attacks (Figure 14).
APJ: Web Attacks by Industry
JAanPuJa:r Wy 1,e 2b0 A23t t–a Dcekcse bmyb Ienr d31u, s2t0r2y4
January 1, 2023 – December 31, 2024
Target Web App API
Financial
Services
Commerce
Social Media
High Technology
Other Digital
Media
0B 5B 10B 15B 20B 25B 30B
Attack Count
EMEA: Web Attacks by Industry
EJaMnuEaAry: 1W, 2e0b23 A –t Dtaecckems bbeyr I 3n1d, 2u0s2t4ry
January 1, 2023 – December 31, 2024
Target Web App API
Commerce
Video Media
Financial
Services
Manufacturing
High Technology
0B 5B 10B 15B 20B 25B 30B 35B 40B 45B 50B 55B 60B
Attack Count
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 33

LATAM: Web Attacks by Industry
January 1, 2023 – December 31, 2024
LATAM: Web Attacks by Industry
January 1, 2023 – December 31, 2024
Target Web App API
Commerce
Financial
Services
0B 3B 6B 9B 12B 15B 18B
Attack Count
Fig. 14: Commerce and financial services were among the top three targeted
industries in the APJ, EMEA, and LATAM regions
In APJ, the financial services industry had the highest number of total web attacks at 27 billion;
commerce was second at 18 billion. This represents a year-over-year growth of 52% and 161%,
respectively. Other digital media was the most targeted industry for API attacks at 22%,
followed by commerce (18%), and financial services (15%).
In EMEA, commerce was the industry that was most impacted by web attacks at 54 billion,
which is more than three times the number of the next closest industry. Despite the high
concentration, total web attacks against commerce entities decreased by 10% year over year
because of a spike in 2023 that skewed the data in the region. However, EMEA still recorded a
16% year-over-year increase in total web attacks driven by an uptick in attacks against other
industries, including financial services (152%) and manufacturing (96%). By taking a closer
look at API-directed attacks in the region, we see that 63% of total web attacks against
commerce targeted APIs.
We see a similar trend in LATAM, where the total number of web attacks against commerce
reached 17 billion, towering over other industries, but year-over-year attacks on the
commerce industry decreased by 76%. Meanwhile, the pharmaceuticals and business
services industries experienced year-over-year increases of 107% and 129%, respectively.
Additionally, 11% of attacks that targeted commerce focused on APIs, and financial services
had an even higher concentration of attacks against APIs at 23%.
The financial services and commerce industries share attributes that contribute to their
appeal as targets for web application and API attacks: both operate within complex
ecosystems, have a high reliance on APIs, and possess valuable data. Threat actors
use a blend of traditional and emerging attack techniques to achieve their goals.
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 34

Layer 7 DDoS attacks: Traffic analysis
A comparison of monthly Layer 7 DDoS attack trends among regions reveals that APJ
was a hotspot, and EMEA and LATAM experienced an ebb and flow of attacks (Figure 15).
APJ: Monthly Layer 7 DDoS Attacks
January 1, 2023 – December 31, 2024
500B
450B
400B
350B
300B
250B
200B
150B
100B
50B
0B
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 35
tnuoC
kcattA
APJ: Monthly Layer 7 DDoS Attacks
January 1, 2023 – December 31, 2024
Target Web App API
January 2
023
April 2
023
July 2
023
October 2
023
January 2
024
April 2
024
July 2
024
October 2
024
EMEA: Monthly Layer 7 DDoS Attacks
January 1, 2023 – December 31, 2024
150B
140B
130B
120B
110B
100B
90B
80B
70B
60B
50B
40B
30B
20B
10B
0B
tnuoC
kcattA
EMEA: Monthly Layer 7 DDoS Attacks
January 1, 2023 – December 31, 2024
Target Web App API
January 2
023
April 2
023
July 2
023
October 2
023
January 2
024
April 2
024
July 2
024
October 2
024

LATAM: Monthly Layer 7 DDoS Attacks
January 1, 2023 – December 31, 2024
18B
17B
16B
15B
14B
13B
12B
11B
10B
9B
8B
7B
6B
5B
4B
3B
2B
1B
0B
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 36
tnuoC
kcattA
LATAM: Monthly Layer 7 DDoS Attacks
January 1, 2023 – December 31, 2024
Target Web App API
January 2
023
April 2
023
July 2
023
October 2
023
January 2
024
April 2
024
July 2
024
October 2
024
Fig. 15: Layer 7 DDoS attacks were on the rise in APJ and EMEA,
whereas attacks in LATAM declined in 2024
APJ experienced 66% year-over-year growth in Layer 7 DDoS attacks and reached a
24-month high, peaking at 504 billion in December 2024. The growth was primarily
driven by attacks focused on the social media industry.
In EMEA, Layer 7 DDoS attacks peaked in March 2024 at nearly 145 billion and, after a
drop, resumed climbing, realizing 20% year-over-year growth. This can be attributed to a
confluence of geopolitical and technological factors. Ongoing tensions in the region have
fueled hacktivist activities. This trend is exacerbated by the rise of AI-enhanced tools and
DDoS as a service platforms, which have lowered the barrier to entry for cybercriminals.
LATAM experienced a significant increase in Layer 7 DDoS attack attempts earlier in
the reporting period, which coincided with an increase in HTTP flood attacks aimed at
overwhelming API resources (an attack vector discussed in more detail in the Layer 7 DDoS
attacks: Year-over-year comparison and trends section. Activity peaked in August 2023 at
16.8 billion and then declined during the remainder of the period to bottom out at 7.5 billion,
marking a 15% year-over-year decrease in attacks.

Layer 7 DDoS attacks: Top targets
Within each region, we observed little to no change to the areas and industries targeted
by threat actors as compared with our previous Layer 7 DDoS attack analysis.
In APJ, Singapore experienced the highest concentration of attacks at 4.7 trillion, followed
by India (1.1 trillion), South Korea (607 billion), Indonesia (283 billion), China (246 billion),
Japan (111 billion), Australia (108 billion), and Taiwan (81 billion).
In EMEA, the countries with the highest number of Layer 7 DDoS attacks were Germany
(569 billion) and the United Kingdom (506 billion), followed by Israel (205 billion), Sweden
(193 billion), and Malta (160 billion). Italy (158 billion), Switzerland (147 billion), France
(129 billion), the Netherlands (111 billion), and Spain (96 billion) rounded out the top 10.
In LATAM, Brazil experienced the highest concentration of Layer 7 DDoS attacks at
175 billion, followed by Mexico (39 billion) and Costa Rica (19 billion).
Industry targets
The top industries impacted by Layer 7 DDoS attacks in APJ and EMEA (Figure 16) have not
changed since our previous secure apps SOTI report. As we discussed in greater detail in
that report, Layer 7 DDoS attacks on social media platforms in APJ surged from January
2023 through June 2024 in correlation with broader military conflicts and highly mediated
electoral events worldwide — which is not surprising since social media platforms receive
heavy traffic volumes during times of geopolitical upheaval. As anticipated, the trend
intensified during the remainder of 2024 due to elections in both APJ and the United States.
These factors contributed to the 130% year-over-year growth in attacks on the sector.
AAPJP:J L: aLyaeyer r7 7 D DDDooSS A Atttatacckkss b byy I nIndduussttrryy
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024
Target Web App API
Social Media
Other Digital
Media
Commerce
Financial
Sevices
High
Technology
0.0T 0.5T 1T 1.5T 2T 2.5T 3T 3.5T 4T 4.5T 5T
Attack Count
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 37

EMEA: Layer 7 DDoS Attacks by Industry
EMJEaAnu: aLrayy 1e, 2r 072 D3 D– DoSec Aemttbaecrk 3s1 ,b 2y0 I2n4dustry
January 1, 2023 – December 31, 2024
Target Web App API
Commerce
Other Digital
Media
Video Media
High
Technology
Social Media
LATAM: Layer 7 DDoS Attacks by Industry
0B 50B 100B 150BJ 2 a 00nBua 2 r 50yB 1, 2 30 00B23 3 – 50 BDe 4 c 00eBmb 450eBr 3 5 1 0 ,0 B202 55 40B 600B 650B 700B 750B 800B
Attack Count
LATAM: Layer 7 DDoS Attacks by Industry
January 1, 2023 – December 31, 2024
Target Web App API
Commerce
Financial
Services
0B 10B 20B 30B 40B 50B 60B 70B 80B 90B 100B 110B 120B 130B 140B
Attack Count
Fig. 16: The top impacted industries per region remained unchanged since our past analysis;
commerce was consistently the industry that was most targeted by Layer 7 DDoS attacks on APIs
In EMEA, commerce remained the most impacted industry for Layer 7 DDoS attacks,
Fig. 16 C: Web Attacks by Vector
followed by other digital media and video media. The industries that experienced the
greatest year-over-year growth in these attacks included high technology (70%), social
media (23%), and commerce (14%). These shifts show how quickly attackers can change their
focus among industries and regions and illustrate that it is worth tracking broader trends.
Commerce was also the top targeted industry in LATAM for Layer 7 DDoS attacks, with
financial services second. During the reporting period, ongoing levels of Layer 7 DDoS attack
activity remained fairly consistent across industries.
Reflecting the global trend, among the industries most targeted by Layer 7 DDoS attacks, the
commerce industry experienced the highest concentration of attacks on APIs in each region.
In EMEA, 43% of attacks against commerce targeted APIs, 21% in LATAM, and 16% in APJ.
For reasons including the geopolitical upheaval and the potential economic impact of
disruptions to highly visible services, commerce, media, and financial services have been
prime targets for Layer 7 DDoS attacks in EMEA and LATAM over the past two years. See the
Industry trends section for a detailed discussion of the drivers and methods behind the high
level of activity against the commerce and financial services industries.
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 38

Compliance
Global and North America perspective
The global cybersecurity landscape in 2025 is characterized by unprecedented complexity
and volatility. Geopolitical tensions, particularly the ongoing conflicts in Ukraine and the
Middle East, have intensified cyberthreats and state-sponsored attacks. The rise of hacktivism,
especially from pro-Russian groups targeting Western nations, has further complicated
the threat landscape. Economically, the rapid digital transformation across industries has
expanded the attack surface, with cybercriminals increasingly targeting critical infrastructure
and leveraging advanced technologies like AI to enhance their capabilities.
These factors, combined with the global economic pressures and political shifts in key
countries, have created a perfect storm for cybersecurity professionals worldwide. Protecting
web applications and APIs is an essential challenge for organizations. Efforts by ethical
hackers, cybersecurity professionals, and organizations such as Akamai to address the
imperative of securing these entry points complement rising compliance considerations.
Regulatory bodies around the world are implementing more stringent cybersecurity
compliance requirements for applications. In North America, the focus has shifted toward
comprehensive risk management strategies and mandatory incident reporting. The Cyber
Incident Reporting for Critical Infrastructure Act in the United States, which is expected to
go into effect in 2026, mandates that critical infrastructure organizations inventory their
information systems, categorize cyber risks, and assess their cybersecurity posture at least
annually. This act emphasizes the need for robust security measures in applications,
particularly those used in critical sectors such as energy, chemical manufacturing, and
information technology.
Similarly, Canada and Mexico are aligning their regulations with international standards,
focusing on data protection and critical infrastructure security. While specific regulations vary,
the global trend is toward more rigorous security requirements for applications, including
enhanced input validation, secure development practices, and regular security audits.
The API security landscape is experiencing parallel challenges, with APIs becoming prime
targets for cybercriminals because of their critical role in enabling service integration and
data exchange. Regulatory bodies worldwide are responding by introducing more stringent
regulations that require organizations to implement robust API security measures.
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 39

These include mandatory continuous API discovery, monitoring, and protection against
evolving threats. In North America, the focus is on thorough risk assessments of API
ecosystems, emphasizing secure development practices, robust authentication
mechanisms, and real-time threat detection capabilities. The rapid adoption of AI-driven
SaaS tools, often integrated via APIs, has significantly expanded the attack surface,
prompting regulators to demand more sophisticated security approaches.
As the complexity of API environments grows, particularly with the rise of AI and machine
learning applications, compliance requirements are evolving to mitigate risks associated
with data breaches, unauthorized access, and service disruptions. While regions like APJ,
LATAM, and EMEA are developing their own specific regulations, the global trend is toward
harmonization of API security standards to address the interconnected nature of modern
digital architecture.
APJ perspective
The APJ region is experiencing a significant shift in its regulatory landscape, with new
compliance mandates that are impacting organizations across various sectors. In Singapore,
recent amendments to its cybersecurity bill have expanded the scope to include both
physical and virtual critical information infrastructure systems, including those hosted on
cloud platforms and located overseas. Japan has updated its National Center of Incident
Readiness and Strategy for Cybersecurity laws, while India has overhauled its IT Act with the
passing of the Digital Personal Data Protection Bill. Australia has introduced its 2023–2030
Cyber Security Strategy, further emphasizing the region’s focus on strengthening
cybersecurity measures. As part of that strategy, amendments were made during late 2024
to the Australian Security of Critical Infrastructure Act and a new Cyber Security Act 2024
became law; enforcement will now include secondary assets like IoT devices, applications,
and APIs that process sensitive data. These regulatory changes are compelling organizations
to reassess and enhance their web application security practices, with a particular emphasis
on protecting critical infrastructure and sensitive data.
The PCI DSS v4.0.1 is set to have a significant impact on organizations that handle payment
card data; the compliance deadline was March 31, 2025. This new version introduces more
stringent requirements for web applications, including the implementation of controls for all
payment page scripts executed in consumers’ browsers and the use of automated technical
solutions to continually detect and prevent web-based attacks. Organizations in the APJ
region must now conduct thorough gap analyses, update their security policies, and
implement necessary technical changes to meet these enhanced security standards
for their web applications.
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 40

In terms of APIs, the APJ region is witnessing a growing emphasis on API security, partly
driven by the increasing adoption of open banking initiatives. Although the region has not yet
fully embraced open banking regulations to the extent seen in EMEA, there is an opportunity
for APJ countries to proactively address API security concerns. An August 2024 survey of API
security insights from this region highlights that internal APIs are the most commonly used,
but external user access remains the primary concern for API access control. This indicates
a need for organizations to implement robust API security measures, including strong
authentication and authorization protocols, data encryption, and continuous API discovery
and monitoring. As the region moves toward open banking directives, organizations will need
to prioritize API security to ensure compliance with evolving regulations and protect against
emerging threats.
EMEA perspective
The cybersecurity landscape in EMEA is undergoing significant transformation, driven by
a complex interplay of geopolitical tensions, technological advancements, and regulatory
shifts. The region faces unique challenges, with ongoing conflicts in Ukraine and the
Middle East intensifying cyberthreats and state-sponsored attacks. Additionally, the rise
of hacktivism, particularly from pro-Russian groups that are targeting European countries,
has made the region a prime focus for politically motivated cyber operations.
The API landscape within EMEA is experiencing parallel challenges. APIs have become prime
targets for cybercriminals because of their critical role in enabling service integration and
data exchange. And the rapid adoption of AI-driven SaaS tools, often integrated via APIs,
has significantly expanded the attack surface.
In response to these escalating threats, the European Union has introduced a suite of
comprehensive cybersecurity regulations. The updated Network and Information Systems
(NIS2) Directive, effective from January 2025, significantly expands its scope to include 18
critical sectors, mandating stringent cybersecurity measures for medium and large entities.
For the financial sector, the Digital Operational Resilience Act (DORA), enforced from
January 17, 2025, supersedes NIS2, requiring robust information and communication
technology risk management frameworks, incident reporting mechanisms, and digital
operational resilience testing programs for applications used in financial services. In addition,
the PCI DSS v4.0.1, which became mandatory on March 31, 2025, introduces new compliance
requirements centered on evolving security needs, continuous security processes, flexible
methodologies, and enhanced validation procedures. The upcoming revised EU Payment
Services Directive (PSD3) aims to address shortcomings in PSD2 by tightening data-sharing
mechanisms, reinforcing security requirements, and enhancing oversight in the financial
services sector.
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 41

The Cyber Resilience Act (CRA). which entered into force on December 10, 2024, introduces
mandatory cybersecurity standards for products with digital elements sold in the European
Union, requiring manufacturers to implement security measures throughout a connected
product’s lifecycle. For application developers and users, the CRA encompasses smartphones
and tablets as significant risk vectors. This inclusion necessitates that organizations treat
mobile terminals as fundamental components of their overall cybersecurity strategy,
implementing rigorous security measures throughout the application lifecycle.
In the United Kingdom, the upcoming Cyber Security and Resilience Bill will improve U.K.
cyber defenses and protect essential public services. The bill’s crucial updates to the legacy
regulatory framework will expand the scope to protect more digital services and supply
chains, strengthen enforcement, and increase reporting requirements.
LATAM perspective
The cybersecurity landscape in LATAM is rapidly evolving, shaped both by global
technological trends and by economic and political challenges unique to the region. In this
context, the rapid digital transformation across LATAM countries, coupled with the
vulnerabilities of increasingly interconnected systems, has made the region an attractive
target for cybercriminals and state-sponsored actors alike. The commerce and financial
services sectors have emerged as prime targets for cyberattacks. Online retailers, payment
processors, banks, insurance companies, fintech startups, and cryptocurrency exchanges are
particularly vulnerable to threats that target their digital infrastructure, especially their web
applications and APIs.
LATAM countries recognize these challenges and are making significant strides in developing
and implementing cybersecurity regulations, with a growing focus on web application and API
security. Brazil has taken a leading role with the implementation of the Lei Geral de Proteção
de Dados Pessoais (LGPD), which came into effect with stringent requirements for data
protection and security. Although it does not specifically address web applications or APIs,
the LGPD has driven organizations to enhance their overall cybersecurity posture, including
the security of their digital interfaces.
Similarly, Chile has enacted its Framework Law on Cybersecurity, which came into force on
January 1, 2025. This law establishes the National Cybersecurity Agency and outlines
comprehensive measures to prevent, report, and resolve cybersecurity incidents across
various sectors, including those heavily reliant on web applications and APIs. Also in January
2025, Argentina published its Federal Plan for the Prevention of Cybercrime and Strategic
Management of Cybersecurity (2025–2027).
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 42

There are promising developments in the realm of API-specific regulations. Mexico, for
instance, has implemented legislation focusing on the financial sector, including fintech, with
detailed requirements for credit bureaus and clearinghouses to develop secure APIs. This
approach reflects a growing recognition of the critical role APIs play in modern digital
ecosystems and the need for targeted security measures. Additionally, the Federal Law on
the Protection of Personal Data Held by Private Parties in Mexico regulates the processing of
personal data and establishes obligations for companies and organizations.
Colombia has also been advancing its regulatory framework, expanding its legal scope by
releasing public policy on cybersecurity for public institutions, and creating a digital security
risk management system with different levels of incident response reporting. While not
exclusively focused on APIs, these measures will inevitably impact API security practices
within organizations.
Across the region, there is a growing trend toward adopting industry-specific initiatives, such
as open finance frameworks, which set API security standards to protect consumer data.
These frameworks are particularly relevant in the financial sector, where the security of APIs
is crucial for maintaining the integrity of financial transactions and protecting sensitive
customer information. As LATAM countries continue to prioritize security advancements and
align their cybersecurity regulations with international standards, we can expect to see more
comprehensive and specific guidelines emerge for web application and API security.
SSttaattee ooff AAppppss aanndd AAPPII SSeeccuurriittyy 22002255 II VVoolluummee 1111,, IIssssuuee 0022 AAkkaammaaii..ccoomm || 4433

Mitigation
In an evolving threat landscape with more sophisticated attack techniques on the
rise, protecting web applications and APIs is an essential challenge for organizations.
Some of the safeguarding and mitigation techniques we recommend include:
Ź Establish a comprehensive API security plan: Implement a shift-left and
DevSecOps approach, integrating security from API design through post-
production. Ensure continuous discovery and visibility to understand the full
attack surface, including hidden APIs (shadow, legacy, and zombie APIs).
Strengthen security with strict authentication and authorization (OAuth 2.0,
mTLS, role-based access control/attribute-based access control), rate limiting,
and bot mitigation to prevent abuse. Implement real-time threat detection,
anomaly monitoring, and runtime protection to identify and stop attacks as they
happen. Ensure compliance with regulations like DORA, GDPR, HIPAA, NIS2, and
PCI DSS while enforcing API governance policies to maintain security at scale.
Ź Implement robust cybersecurity measures: Use an adaptive security engine
that continuously monitors and responds to threats in real time and provides
threat intelligence and runtime protection. Also use API testing tools like dynamic
application security testing (DAST) to help ensure that security requirements —
including secure access, encryption, and authentication — are met.
Ź Take a proactive defense against threats: Use specialized DDoS protection
tools, configure rate limiting and CDN caching, and implement measures
like patch management, access control policies, and network segmentation.
Also protect DNS infrastructure with continuous traffic monitoring and
hybrid platforms.
Ź Mitigate API vulnerabilities: Follow established security guidelines, such as
those provided by OWASP, to ensure robust API security and address the risks
of poor coding practices and misconfigurations in API architecture, which can
create exploitable vulnerabilities that allow hackers to gain unauthorized access
or manipulate data.
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 44

Ź Defend against ransomware threats: Use a layered approach to combat
ransomware. Implement Zero Trust solutions to block malicious traffic, use
microsegmentation for detailed visibility and precise access control, and leverage
the MITRE ATT&CK framework to understand attack patterns and enhance
response strategies.
Ź Be prepared for AI: Employ a comprehensive defense strategy that includes bot
defense solutions, AI-powered security tools, specialized firewalls, and proactive
measures like continuous assessments and Zero Trust models to address the new
security risks introduced by the increasing use of AI. Secure AI systems with a
multifaceted approach: Address specific threats, such as prompt injection and
data poisoning, through awareness of models and datasets; perform proactive
vulnerability testing; and use robust defenses like behavioral monitoring, content
validation, and automated attack responses that are integrated across both
development and runtime environments.
SSttaattee ooff AAppppss aanndd AAPPII SSeeccuurriittyy 22002255 II VVoolluummee 1111,, IIssssuuee 0022 AAkkaammaaii..ccoomm || 4455

Methodology
Web application and Layer 7 DDoS attacks
This data describes application-layer alerts on traffic seen through our web application
firewall (WAF). The web application attack alerts are triggered when we detect a malicious
payload within a request to a protected website, application, or API. The Layer 7 DDoS
alerts are triggered when we detect volumetric anomalies in the number of requests to a
protected website, application, or API. These alerts can be triggered by both malicious
and benign requests. Typically, the requests themselves are benign, but the high volume
of requests indicates malicious intent. The alerts do not indicate the successfulness of an
attack. Although these products allow a high level of customization, we collected the data
presented here in a manner that does not consider custom configurations of the
protected properties.
The data was drawn from an internal tool for analysis of security events detected on
Akamai Cloud, a network of approximately 340,000 servers in more than 4,000 locations
on nearly 1,300 networks in 130+ countries. Our security teams use this data, measured in
petabytes per month, to research attacks, flag malicious behavior, and feed additional
intelligence into Akamai’s solutions.
This data covered the 24-month period from January 1, 2023, through December 31, 2024.
API security attack data
Akamai’s integration of Noname Security has enhanced our API threat research and
reporting capabilities. This dataset is still in the early stages of integration and analysis. For
this report, we took a 30-day data sample from Q1 2025 to analyze the breakdown of API
security alerts according to their corresponding security frameworks and compliance
standards. This dataset will continue to progress and provide an expanded view of API
security issues in the future.
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 46

Credits State of the Internet/Security
Read back issues and watch for upcoming
releases of Akamai’s acclaimed State of the
Internet/Security reports. akamai.com/soti
Research director
Mitch Mayne Akamai threat research
Stay updated with the latest threat intelligence
Editorial and writing
analyses, security reports, and cybersecurity
Charlotte Pelliccia Badette Tribbey research. akamai.com/security-research
Lance Rhodes Maria Vlasak
Access data from this report
Review and subject matter contribution
View high-quality versions of the graphs
Tom Emmons Stas Neyman and charts referenced in this report. These
Reuben Koh Steve Winterfeld images are free to use and reference,
Richard Meeus provided that Akamai is duly credited as
a source and the Akamai logo is retained.
Data analysis
akamai.com/sotidata
Chelsea Tuttle
Akamai security research
Promotional materials
Read the Akamai security research blog
Barney Beal Ashley Linares for a rapid response perspective on today’s
most important research. akamai.com/
Marketing and publishing
blog/security-research
Georgina Morales Hampe Emily Spinks
Akamai Security protects the applications that drive your business at every point of interaction, without compromising performance or
customer experience. By leveraging the scale of our global platform and its visibility to threats, we partner with you to prevent, detect, and
mitigate threats, so you can build brand trust and deliver on your vision. Learn more about Akamai’s cloud computing, security, and content
delivery solutions at akamai.com and akamai.com/blog, or follow Akamai Technologies on X, formerly known as Twitter, and LinkedIn.
Published 04/25.
State of Apps and API Security 2025 I Volume 11, Issue 02 Akamai.com | 47