# Initial Access Brokers Report: 2026

**Organization:** Rapid7  
**Date:** March 31, 2026  
**Report Type:** Threat Research  

## Table of Contents
- [Key findings](#key-findings)
- [IAB and cybercrime forum landscape in 2026](#iab-and-cybercrime-forum-landscape-in-2026)
- [Why cybercrime forums matter in 2026](#why-cybercrime-forums-matter-in-2026)
- [Exploit, XSS, DarkForums, BreachForums, and RAMP: Combined data analysis](#exploit-xss-darkforums-breachforums-and-ramp-combined-data-analysis)
- [Initial access vectors and privilege types](#initial-access-vectors-and-privilege-types)
- [Demographic information](#demographic-information)
- [Individual analysis of Exploit, XSS, DarkForums, BreachForums, and RAMP](#individual-analysis-of-exploit-xss-darkforums-breachforums-and-ramp)
- [Threat actors active across multiple forums](#threat-actors-active-across-multiple-forums)
- [Recommendations](#recommendations)
- [Conclusion](#conclusion)

---

## Key findings
Our detailed analysis of six months of data from Exploit, XSS, BreachForums, DarkForums, and RAMP reveals the following key findings:

*   **Access prices and target organization size increased dramatically:** The average alleged victim revenue and offering base price have increased significantly compared to the previous year, indicating that IABs are targeting larger, higher-value enterprises and charging premium prices for quality access.
*   **Primary access vectors haven’t changed:** RDP, VPN, and RDWeb remain the top access vectors being offered for sale, which means that remote access infrastructure is still the primary attack surface for initial access sales.
*   **High-privilege access is increasingly prioritized:** Most common privilege levels being offered by IABs are Domain User (42.9%), Domain Admin (32.1%), and Local Admin (12.5%), with a visible decline in lower-privilege offerings, such as Local User privileges. It seems the market is shifting from volume to high-impact access that enables faster and more efficient malicious operations, such as ransomware and extortion attacks.
*   **Certain underground marketplaces have become favored over others:** DarkForums (221 threads) and RAMP (208 threads) were the most active forums for initial access sales in H2 2025, accounting together for 81% of the observed threads. At the same time, older, historically dominant forums such as XSS and Exploit saw significant declines in IAB activity.
*   **IABs target specific industries:** IAB activity is primarily concentrated on sectors offering the highest potential for financial gain or intelligence acquisition: Government, Retail, and Information Technology (IT).
*   **Focus on government access:** The Government sector is the most frequently targeted industry vertical, at 14.2% (Retail and Information Technology follow with 13.1% and 10.8%, respectively). 'Admin panel' access is the most commonly observed type offered for this sector, with DarkForums serving as the principal platform for its sale.

## IAB and cybercrime forum landscape in 2026
Just as in 2025, cybercriminal forums continue to serve as the primary marketplaces for the promotion and sale of pirated network access. Platforms such as Exploit, BreachForums, XSS, DarkForums, and RAMP have remained central pillars of the cybercriminal underground through 2025 and into 2026, despite sustained law-enforcement pressure, infrastructure seizures, and repeated cycles of disruption and rebirth. In response to the continued relevance, Rapid7 threat intelligence researchers expanded their monitoring to include all five forums, tracking activity from January through December 2025.

## Why cybercrime forums matter in 2026
We selected these five forums for their continued relevance, the concentration of experienced actors, and their distinct functional roles within the cybercriminal ecosystem. Collectively, they represent the full lifecycle of modern cybercrime from initial compromise and access brokerage to data monetization, extortion, and ransomware enablement.

## Exploit, XSS, DarkForums, BreachForums, and RAMP: Combined data analysis
Last year, in *The Rapid7 2025 Access Brokers Report*, we analyzed the data of three main cybercrime forums, Exploit, XSS, and BreachForums. This year, we have expanded this list to include two additional (and very popular) forums, DarkForums and RAMP.

The newly analyzed forums were the most active in the past six months: DarkForums (221 sale threads), RAMP (208), Exploit (53), Breached (30), and XSS (18). 

![Chart showing forum activity distribution]

The average alleged revenue of the organizations whose access is being sold was $3.242 billion, and the average base price for the offerings was $113,275. These numbers manifest a substantial rise compared to last year (average revenue - $2.232 billion, average base price - $2,726).

## Initial access vectors and privilege types
Analysis of the access types offered for sale revealed 29 distinct types of access. The most frequently advertised access types were RDP (21.2%), VPN (12.8%), and RDWeb (11.2%).

![Chart showing access vector distribution]

The most common privilege types were Domain User (42.9%), Domain Admin (32.1%), and Local Admin (12.5%). Notably, the updated dataset contains no instances of Local User privilege sales.

![Chart showing privilege type distribution]

Additionally, in RAMP, we observed an exploit targeting a vulnerability in the Oracle E-Business Suite (CVE-2025-61882) being offered for sale.

## Demographic information
Most available listings concern networks in the United States, totaling 155 unique listings (30.9% of total global data). The top 10 targeted countries list is very similar to last year, placing the United States at the top, followed by the United Kingdom, India, and Brazil.

![Chart showing top targeted countries]

The government sector is the most frequently targeted category (14.2%), followed by Retail (13.1%) and Information Technology (10.8%).

![Chart showing top targeted sectors]

## Individual analysis of Exploit, XSS, DarkForums, BreachForums, and RAMP

### Exploit
Exploit has continued to function as one of the most technically rigorous Russian-language cybercrime forums. In H2 2025, IABs shifted focus from RDP to RDWeb. While the average alleged revenue of targeted organizations dropped, the base price of offerings increased 6 times compared to last year.

### BreachForums (AKA Breached)
BreachForums has experienced significant volatility. Following multiple seizures, it has reestablished itself as a data-leak-centric marketplace. IAB threads dropped by approximately 52% compared to 2024.

### XSS (formerly DaMaGeLaB)
XSS has retained its status as a premier Russian-language forum. However, it saw the most significant decline in IAB activity, dropping from the most dominant forum to the lowest among the five examined, likely due to actors shifting to newer forums like DarkForums and RAMP.

### DarkForums
DarkForums rose to prominence as an English-language alternative. It is the most dominant forum in terms of IAB threads. It features unique access types, with Fortinet access leading the board, followed by SSH, RDP, and Root access.

### RAMP (Russian Anonymous Marketplace)
RAMP operates as a high-trust, invite-only ecosystem. The most dominant type of access sold was RDP. Most analyzed threads (78.8%) belonged to only two users: Big-Bro and lacrim.

## Threat actors active across multiple forums
This research revealed that a subset of threat actors maintains an active presence across multiple forums, with the greatest overlap observed between Breached and DarkForums, which share a nearly identical visual and structural layout.

## Recommendations
*   **Continuous Monitoring:** Treat anomalous logins, unexpected privilege escalations, and access from unfamiliar locations as early indicators of compromise.
*   **Proactive Intelligence:** Use threat intelligence to anticipate targeted access methods.
*   **Hardening:** Enforce least-privilege principles, control administrative rights, and harden remote access services with MFA.

## Conclusion
The comparison between 2024 and 2025 highlights how initial access brokers continue to adapt to defensive measures. The shift toward high-privilege credentials and specific access vectors like RDWeb and SSH reflects a pragmatic "path-of-least-resistance" strategy. Organizations must evolve their defenses in step with these brokers to increase the cost and reduce the effectiveness of cybercriminal operations.