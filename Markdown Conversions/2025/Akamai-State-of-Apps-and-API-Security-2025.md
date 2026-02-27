Organization: Akamai
Report Title: State of Apps and API Security 2025
Year: 2025
Volume: 11, Issue 02

# State of Apps and API Security 2025: How AI Is Shifting the Digital Terrain

## Table of Contents
- [Introduction](#introduction)
- [Key Insights of the Report](#key-insights-of-the-report)
- [Evolving Our API Threat Intelligence](#evolving-our-api-threat-intelligence)
- [Web Attacks: Year-over-Year Comparison and Trends](#web-attacks-year-over-year-comparison-and-trends)
- [Layer 7 DDoS Attacks: Year-over-Year Comparison and Trends](#layer-7-ddos-attacks-year-over-year-comparison-and-trends)
- [Industry Trends](#industry-trends)
- [Regional Trends](#regional-trends)
- [Compliance](#compliance)
- [Mitigation](#mitigation)
- [Methodology](#methodology)
- [Credits](#credits)

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

## Key Insights of the Report

- **AI-powered APIs are more unsecure than their counterparts.** The majority of artificial intelligence (AI)–powered APIs are externally accessible and many rely on inadequate authentication mechanisms — a vulnerability that’s compounded by the growing array of AI-driven attacks that are targeting them.
- **AI fuels technical advancement for threat actors.** This includes advancements like AI-driven malware, vulnerability scanning, attacks on AI-integrated systems, and sophisticated web scraping capabilities.
- **32% Increase in OWASP API Security Top 10–related incidents.** API security incidents are rising, with Open Worldwide Application Security Project (OWASP) API Security Top 10 issues revealing authentication and authorization flaws that expose sensitive data and functionality.
- **30% Growth in security alerts related to the MITRE security framework.** Attackers are using advanced techniques, including automation and AI, to exploit APIs. The MITRE framework can help defenders more quickly and accurately identify these attacks.
- **33% Increase in global web attacks year over year.** The surge in attacks directly correlates with the rapid adoption of cloud services, microservices, and AI applications, which expand attack surfaces and introduce new security challenges.
- **230 billion+ web attacks hit commerce organizations.** This makes it the most impacted industry with nearly triple the number of attacks experienced by high technology (the second most attacked industry).
- **73% Increase in total web attacks year over year in the Asia-Pacific and Japan (APJ) region**, rising from 29 billion in 2023 to 51 billion in 2024.
- **37% of web attacks in the Europe, Middle East, and Africa (EMEA) region targeted APIs**, which is the highest concentration of such attacks across all regions.
- **94% Growth in quarterly Layer 7 distributed denial-of-service (DDoS) attacks** between Q1 2023 and Q4 2024.
- **11.9 trillion Layer 7 DDoS attacks targeted North America** during the two-year period Q1 2023 through Q4 2024.
- **7 trillion Layer 7 DDoS attacks targeted the high technology industry** from January 2023 through December 2024, making it the most affected industry.
- **7.4 trillion Layer 7 DDoS attacks targeted the APJ region** during the two-year period Q1 2023 through Q4 2024.
- **20% of Layer 7 DDoS API-related attacks targeted the EMEA region**, representing the highest concentration of this attack type across all regions.

## Evolving Our API Threat Intelligence

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

For this report, we’ve analyzed a 30-day data sample to highlight general activity by threat actors across each of the cybersecurity frameworks and compliance standards (Figure 1).

| Framework/Standard | 30-Day Activity | Monthly Increase |
| :--- | :--- | :--- |
| OWASP | 5,907,000 | 32% |
| MITRE | 2,817,000 | 30% |
| ISO | 832,000 | 22% |
| GDPR | 669,000 | 21% |
| PCI DSS | 881,000 | 16% |

![Fig. 1: Breakdown of security alerts according to security frameworks and compliance standards]

### MITRE alerts

Over a 30-day period, we observed a 30% increase in incidents related to MITRE techniques among our customers. Notably, attackers frequently employed T1078 (Valid Accounts), leveraging legitimate credentials to gain unauthorized access to systems or networks. Since APIs often rely on tokens for authorization, adversaries who obtain these tokens can access sensitive data without detection.

We also identified T1566 (Phishing), in which attackers launched phishing campaigns to steal API tokens or credentials for future attacks. Additionally, alerts related to T1190 (Exploit Public-Facing Application) revealed attackers using application flaws to infiltrate networks. Another observed technique was T1580 (Cloud Infrastructure Discovery), in which adversaries used APIs for reconnaissance by probing exposed cloud endpoints via API calls.

### OWASP alerts

During the 30-day sample period, our analysis revealed a 32% increase in OWASP-related incidents. Notably, vulnerabilities such as Broken Object Property Level Authorization (BOPLA), Broken Function Level Authorization, and Broken Authentication expose sensitive data or critical functions directly to attackers.

**Broken Object Level Authorization (BOLA)** remains a critical API security vulnerability, but its detection is challenging due to its reliance on business logic flaws. Organizations should employ API security solutions that establish behavioral baselines via machine learning algorithms.

**BOPLA** exploits granular field-level access issues in APIs. Unlike BOLA, which requires changing entire object IDs, BOPLA attacks target specific properties within objects. For instance, a DELETE API call that exposes sensitive personally identifiable information (PII) in its response constitutes a BOPLA vulnerability.

**Unrestricted Resource Consumption** is another critical vulnerability that attackers can exploit to cause service disruptions through resource exhaustion or DDoS-like attacks. This leads to increased operational costs and heightened risks of brute-force attacks.

**Unsafe consumption of APIs** stems from inadequate validation, filtering of data, and lack of security mechanisms during third-party API integrations. A recent study revealed that more than 80% of surveyed organizations faced problems with third-party APIs.

### Ensuring API compliance

Best practices for ensuring API compliance include tagging each alert with the specific compliance and regulatory standards it violates. Security alerts related to PCI DSS and GDPR increased by 16% and 21%, respectively, while ISO 27001–related alerts rose by 22%.

- **GDPR**: Emphasizes integrating data protection and customer privacy throughout the entire API lifecycle.
- **PCI DSS**: Emphasizes securing APIs that handle payment card data. Requirements 10 and 11 specifically call for comprehensive logging and monitoring of API activities.
- **ISO 27001**: Provides a framework for managing information security risks, including access control (API keys), end-to-end encryption, and monitoring for anomalous behavior.

### API visibility gaps: The hidden passages to data

**API abuse**
In November 2024, threat actors exploited a core component of an electronic signature provider's document management API to send fraudulent invoices. This underscores how malicious actors exploit APIs beyond their intended design.

**Challenges in API abuse detection**
Only 13% of surveyed organizations test their APIs daily, a marked decrease from 37% in 2023. This decline is alarming given the current threat landscape.

**Unmanaged APIs: Zombie and shadow APIs**
47% of AppSec teams maintain full API inventories but fail to identify APIs that handle sensitive data. Zombie APIs (outdated, active interfaces) and Shadow APIs (developed outside standard processes) are leading causes of security incidents. Research indicates that one-third of malicious API transactions target shadow APIs.

### Security spotlight

In Q1 2025, an ecommerce company was attacked via an unauthenticated "send SMS" API. Attackers used 200+ IP addresses and random mobile numbers to cause financial damage through SMS gateway charges.

![Fig. 2: Threat actors flood the unsecure API with requests, showing a high volume of POST requests with varying mobile number parameters.]

## Web Attacks: Year-over-Year Comparison and Trends

Akamai research revealed a 65% growth in web attacks from Q1 2023 through Q4 2024. Monthly attack volumes increased from nearly 14 billion to more than 29 billion by October 2024.

![Fig. 3: Line chart showing monthly web attacks targeting web applications and APIs from January 2023 to December 2024, illustrating a steady upward trend.]

### API request constraint violations: A growing threat

API request constraint violations (requests failing to adhere to predefined parameters) saw a 24% surge from 2023 to 2024, with more than 83 billion attacks recorded in two years.

![Fig. 4: Bar chart showing API attacks by vector, with Request Constraint Violations being the most prevalent at over 83 billion.]

### Active attack sessions: Unique attacks that call for a creative solution

Akamai uses a "penalty box" approach to identify and track suspicious behavior. Active attack sessions accounted for more than 69 billion attacks in 2023, surging to 113 billion in 2024 (a 63% increase).

![Fig. 5: Bar chart comparing web attack vectors for web apps and APIs, showing Active Attack Sessions as the dominant vector.]

### Why we can’t ignore traditional web vulnerabilities in modern infrastructure

SQL injection (SQLi) and command injection experienced 60% and 34% year-over-year growth, respectively. Despite the rise of behavior-based attacks, these traditional vulnerabilities remain highly effective for compromising system integrity.

## Layer 7 DDoS Attacks: Year-over-Year Comparison and Trends

Akamai documented a 94% growth in Layer 7 DDoS attacks from Q1 2023 through Q4 2024. Monthly volumes surged from 500 billion to more than 1.1 trillion.

![Fig. 6: Line chart showing the 94% increase in monthly Layer 7 DDoS attacks against web applications and APIs.]

### The attackers’ AI transmission: Driving the API road via manual or automatic

The AI API market is projected to reach US$179.14 billion by 2030. Attackers are leveraging AI for:
- **Strategic targeting**: Crafting tailored exploits.
- **Automated attacks**: Using AI-powered bots.
- **Volumetric attacks**: Overwhelming APIs with traffic.
- **Behavioral-based attacks**: Creating "low and slow" attacks to evade detection.

### AI-powered web application attacks and defense strategies

- **AI-enhanced malware**: Malicious code designed with generative AI assistance (e.g., AsyncRAT).
- **AI-powered vulnerability scanning**: Automating searches for SQLi, XSS, and SSRF.
- **Attacks on AI-involved systems**: Prompt injection, data poisoning, and jailbreaking of LLMs.
- **Sophisticated web scraping**: LLM scraping for real-time data, costing organizations US$0.01 to US$0.50 per request.
- **AI-powered WAF systems**: Using machine learning for pattern recognition and anomaly detection.

## Industry Trends

Commerce experienced nearly triple the number of overall web attacks compared to high technology.

![Fig. 7: Bar chart showing web attacks by industry, with Commerce, High Technology, and Financial Services as the top three.]

For Layer 7 DDoS, high technology was the most targeted industry (7 trillion+ attacks), followed by social media and commerce.

![Fig. 8: Bar chart showing Layer 7 DDoS attacks by industry, highlighting High Technology as the primary target.]

### Commerce
Commerce entities represent lucrative targets due to sensitive customer and payment data. Retail is the most heavily targeted segment, especially during seasonal traffic spikes (25% to 30% increase in cybercrime during the winter holidays).

### Financial services
Web attacks totaled 79 billion and Layer 7 DDoS attacks totaled 761 billion. Banking is the most targeted segment within this industry.

![Fig. 9: Bar chart showing financial services web attacks, with Banking significantly higher than Insurance or other services.]

### High technology
This industry saw 81.7 billion web attacks and 7 trillion Layer 7 DDoS attacks. Telecommunications and IoT devices are major areas of concern, with many devices lacking robust security.

## Regional Trends

| Region | Web Attack Counts | Layer 7 DDoS Attack Counts | Top Web Attack Vectors | Top Target Areas | Top Target Industries |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **APJ** | 80B, 14% API | 7.4T, 6% API | Active attack session, LFI, XSS | Australia, India, Singapore | Financial services, commerce, social media |
| **EMEA** | 116B, 37% API | 2.6T, 20% API | Active attack session, API request constraint violation, LFI | UK, Netherlands, Spain, Germany | Commerce, video media, financial services |
| **LATAM** | 3B, 12% API | 258B, 18% API | Active attack session, WAT, SSRF | Brazil, Mexico | Commerce, other digital media, video media |
| **N. America** | 327B, 29% API | 11.9T, 16% API | Active attack session | USA, Canada | Commerce, financial services |

![Fig. 10: Regions at a glance table summarizing attack data from January 2023–December 2024.]

### Two application and API attack trends

1. **API attacks were widespread in EMEA**: 37% of web attacks in EMEA targeted APIs, the highest concentration globally.
2. **APJ experienced the second highest level of Layer 7 DDoS attacks**: 7.4 trillion attacks, largely driven by attempts against social media.

![Fig. 11: Bar charts comparing web attacks and Layer 7 DDoS attacks by region.]

### A deeper dive into APJ, EMEA, and LATAM

![Fig. 12: Line chart showing monthly web attacks in the APJ region, illustrating fluctuations between January 2023 and December 2024.]

EMEA: Monthly Web Attacks
EMEA: Monthl

---

y Web Attacks
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024

Target

Web App

API

LATAM: Monthly Web Attacks
LATAM: Monthly Web Attacks
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024

Target

Web App

API

7B

6B

5B

4B

3B

2B

1B

0B

2.5B

2.0B

1.5B

1.0B

0.5B

0B

t
n
u
o
C
k
c
a
t
t
A

t
n
u
o
C
k
c
a
t
t
A

Fig. 12: Web application attack activity drove an increase in the total number of web attacks
in APJ and EMEA, while attacks in LATAM declined steeply

APJ experienced a significant 73% increase in total web attacks year over year, from 29

billion in 2023 to 51 billion in 2024. In EMEA, the year-over-year increase was a moderate

16% (from 54 billion to 62 billion) — but this smaller increase is affected by an outlier event

recorded in the data that, if removed, would boost the number closer to 33%. In LATAM,

web attacks dropped considerably from a total of 16 billion in 2023 to 6 million in 2024,

a 61% year-over-year decrease.

Akamai.com   |   30

State of Apps and API Security 2025  I  Volume 11, Issue 02April 2023January 2023July 2023October 2023January 2024April 2024July 2024October 2024April 2023January 2023July 2023October 2023January 2024April 2024July 2024October 2024

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

Target

Web App

API

Active Attack
Session

Local File
Inclusion

Cross-Site
Scripting

SQL Injection

Web Attack Tool

Active Attack
Session

API Request
Constraint Violation

Local File
Inclusion

Web Attack Tool

SQL Injection

0B

5B

10B

15B

20B

25B

30B

Attack Count

EMEA: Web Attacks by Vector
January 1, 2023 – December 31, 2024

EMEA: Web Attacks by Vector
January 1, 2023 – December 31, 2024

Target

Web App

API

0B

10B

20B

30B

40B

Attack Count

Akamai.com   |   31

State of Apps and API Security 2025  I  Volume 11, Issue 02LATAM: Web Attacks by Vector
LATAM: Web Attacks by Vector
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024

Target

Web App

API

Active Attack
Session

Web Attack Tool

Server-Side
Request Forgery

Data Harvesting

SQL Injection

0B

1B

2B

3B

4B

5B

6B

7B

8B

9B

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

 Ź

In each region, web attack tool was in the top five. Threat actors use this vector to

probe the target to solicit information about its security, configurations, or potential

vulnerabilities that could be leveraged for nefarious purposes.

For more details on these top vectors, see the Web attacks section.

Akamai.com   |   32

State of Apps and API Security 2025  I  Volume 11, Issue 02Web application and API attacks: Top targets

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
APJ: Web Attacks by Industry
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024

Target

Web App

API

Financial
Services

Commerce

Social Media

High Technology

Other Digital
Media

Commerce

Video Media

Financial
Services

Manufacturing

High Technology

0B

5B

10B

15B

20B

25B

30B

Attack Count
EMEA: Web Attacks by Industry
January 1, 2023 – December 31, 2024
EMEA: Web Attacks by Industry
January 1, 2023 – December 31, 2024

Target

Web App

API

0B

5B

10B

15B

20B

25B

30B

35B

40B

45B

50B

55B

60B

Attack Count

Akamai.com   |   33

State of Apps and API Security 2025  I  Volume 11, Issue 02LATAM: Web Attacks by Industry
January 1, 2023 – December 31, 2024

LATAM: Web Attacks by Industry
January 1, 2023 – December 31, 2024

Target

Web App

API

Commerce

Financial
Services

0B

3B

6B

9B

12B

15B

18B

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

Akamai.com   |   34

State of Apps and API Security 2025  I  Volume 11, Issue 02Layer 7 DDoS attacks: Traffic analysis

A comparison of monthly Layer 7 DDoS attack trends among regions reveals that APJ

was a hotspot, and EMEA and LATAM experienced an ebb and flow of attacks (Figure 15).

APJ: Monthly Layer 7 DDoS Attacks
APJ: Monthly Layer 7 DDoS Attacks
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024

Target

Web App

API

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

t
n
u
o
C
k
c
a
t
t
A

t
n
u
o
C
k
c
a
t
t
A

EMEA: Monthly Layer 7 DDoS Attacks
EMEA: Monthly Layer 7 DDoS Attacks
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024

Target

Web App

API

Akamai.com   |   35

State of Apps and API Security 2025  I  Volume 11, Issue 02April 2023January 2023July 2023October 2023January 2024April 2024July 2024October 2024April 2023January 2023July 2023October 2023January 2024April 2024July 2024October 2024

LATAM: Monthly Layer 7 DDoS Attacks
LATAM: Monthly Layer 7 DDoS Attacks
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024

Target

Web App

API

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

t
n
u
o
C
k
c
a
t
t
A

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

Akamai.com   |   36

State of Apps and API Security 2025  I  Volume 11, Issue 02April 2023January 2023July 2023October 2023January 2024April 2024July 2024October 2024
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

APJ: Layer 7 DDoS Attacks by Industry
APJ: Layer 7 DDoS Attacks by Industry
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024

Target

Web App

API

Social Media

Other Digital
Media

Commerce

Financial
Sevices

High
Technology

0.0T

0.5T

1T

1.5T

2T

2.5T

3T

3.5T

4T

4.5T

5T

Attack Count

Akamai.com   |   37

State of Apps and API Security 2025  I  Volume 11, Issue 02EMEA: Layer 7 DDoS Attacks by Industry
EMEA: Layer 7 DDoS Attacks by Industry
January 1, 2023 – December 31, 2024
January 1, 2023 – December 31, 2024

Target

Web App

API

100B

LATAM: Layer 7 DDoS Attacks by Industry
550B
200B
400B
600B
350B
January 1, 2023 – December 31, 2024
Attack Count

300B

500B

450B

250B

150B

650B

700B

750B

800B

LATAM: Layer 7 DDoS Attacks by Industry
January 1, 2023 – December 31, 2024

Target

Web App

API

Commerce

Other Digital
Media

Video Media

High
Technology

Social Media

0B

50B

Commerce

Financial
Services

0B

10B

20B

30B

 40B

50B

70B

60B
Attack Count

80B

90B

100B

110B

120B

130B

140B

Fig. 16: The top impacted industries per region remained unchanged since our past analysis;
commerce was consistently the industry that was most targeted by Layer 7 DDoS attacks on APIs

In EMEA, commerce remained the most impacted industry for Layer 7 DDoS attacks,
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

Akamai.com   |   38

State of Apps and API Security 2025  I  Volume 11, Issue 02Fig. 16 C: Web Attacks by VectorCompliance

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

Akamai.com   |   39

State of Apps and API Security 2025  I  Volume 11, Issue 02These include mandatory continuous API discovery, monitoring, and protection against

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

Akamai.com   |   40

State of Apps and API Security 2025  I  Volume 11, Issue 02In terms of APIs, the APJ region is witnessing a growing emphasis on API security, partly

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

Akamai.com   |   41

State of Apps and API Security 2025  I  Volume 11, Issue 02The Cyber Resilience Act (CRA). which entered into force on December 10, 2024, introduces

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

Akamai.com   |   42

State of Apps and API Security 2025  I  Volume 11, Issue 02There are promising developments in the realm of API-specific regulations. Mexico, for

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

State of Apps and API Security 2025  I  Volume 11, Issue 02

Akamai.com   |   43
Akamai.com   |   43

State of Apps and API Security 2025  I  Volume 11, Issue 02Mitigation

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

 Ź

Implement robust cybersecurity measures: Use an adaptive security engine
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

Akamai.com   |   44

State of Apps and API Security 2025  I  Volume 11, Issue 02 Ź Defend against ransomware threats: Use a layered approach to combat

ransomware. Implement Zero Trust solutions to block malicious traffic, use

microsegmentation for detailed visibility and precise access control, and leverage

the MITRE ATT&CK framework to understand attack patterns and enhance

response strategies.

 Ź Be prepared for AI: Employ  a comprehensive defense strategy that includes bot
defense solutions, AI-powered security tools, specialized firewalls, and proactive

measures like continuous assessments and Zero Trust models to address the new

security risks introduced by the increasing use of AI. Secure AI systems with a

multifaceted approach: Address specific threats, such as prompt injection and

data poisoning, through awareness of models and datasets; perform proactive

vulnerability testing; and use robust defenses like behavioral monitoring, content

validation, and automated attack responses that are integrated across both

development and runtime environments.

State of Apps and API Security 2025  I  Volume 11, Issue 02

Akamai.com   |   45
Akamai.com   |   45

State of Apps and API Security 2025  I  Volume 11, Issue 02Methodology

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

Akamai.com   |   46

State of Apps and API Security 2025  I  Volume 11, Issue 02Credits

Research director

Mitch Mayne

Editorial and writing

Charlotte Pelliccia

Badette Tribbey

Lance Rhodes

Maria Vlasak

Review and subject matter contribution

Stas Neyman

Steve Winterfeld

Tom Emmons

Reuben Koh

Richard Meeus

Data analysis

Chelsea Tuttle

Promotional materials

Barney Beal

Ashley Linares

Marketing and publishing

Georgina Morales Hampe

Emily Spinks

State of the Internet/Security

Read back issues and watch for upcoming

releases of Akamai’s acclaimed State of the
Internet/Security reports. akamai.com/soti

Akamai threat research

Stay updated with the latest threat intelligence

analyses, security reports, and cybersecurity
research. akamai.com/security-research

Access data from this report

View high-quality versions of the graphs

and charts referenced in this report. These

images are free to use and reference,

provided that Akamai is duly credited as

a source and the Akamai logo is retained.

akamai.com/sotidata

Akamai security research

Read the Akamai security research blog

for a rapid response perspective on today’s
most important research. akamai.com/
blog/security-research

Akamai Security protects the applications that drive your business at every point of interaction, without compromising performance or
customer experience. By leveraging the scale of our global platform and its visibility to threats, we partner with you to prevent, detect, and
mitigate threats, so you can build brand trust and deliver on your vision. Learn more about Akamai’s cloud computing, security, and content
delivery solutions at akamai.com and akamai.com/blog, or follow Akamai Technologies on X, formerly known as Twitter, and LinkedIn.
Published 04/25.

State of Apps and API Security 2025  I  Volume 11, Issue 02

Akamai.com   |   47