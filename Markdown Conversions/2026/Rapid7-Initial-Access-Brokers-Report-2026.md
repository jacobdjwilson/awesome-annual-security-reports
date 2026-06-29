# Initial Access Brokers Report: 2026

**Organization:** Rapid7  
**Report Date:** March 31, 2026  
**Category:** Threat Research

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
*   **Focus on government access:** The **Government sector** is the most frequently targeted industry vertical, at 14.2% (Retail and Information Technology follow with 13.1% and 10.8%, respectively). 'Admin panel' access is the most commonly observed type offered for this sector, with DarkForums serving as the principal platform for its sale.

## IAB and cybercrime forum landscape in 2026
Just as in 2025, cybercriminal forums continue to serve as the primary marketplaces for the promotion and sale of pirated network access. Platforms such as Exploit, BreachForums, XSS, DarkForums, and RAMP have remained central pillars of the cybercriminal underground through 2025 and into 2026, despite sustained law-enforcement pressure, infrastructure seizures, and repeated cycles of disruption and rebirth. In response to the continued relevance, Rapid7 threat intelligence researchers expanded their monitoring to include all five forums, tracking activity from January through December 2025.

## Why cybercrime forums matter in 2026
We selected these five forums for their continued relevance, the concentration of experienced actors, and their distinct functional roles within the cybercriminal ecosystem. Collectively, they represent the full lifecycle of modern cybercrime from initial compromise and access brokerage to data monetization, extortion, and ransomware enablement. Despite repeated takedowns and administrator arrests, the past two years have demonstrated that forum resilience, brand persistence, and rapid reconstitution remain defining characteristics of the underground economy.

## Exploit, XSS, DarkForums, BreachForums, and RAMP: Combined data analysis
Last year, in *The Rapid7 2025 Access Brokers Report*, we analyzed the data of three main cybercrime forums, Exploit, XSS, and BreachForums. This year, we have expanded this list to include two additional (and very popular) forums, DarkForums and RAMP.

In fact, the newly analyzed forums were the most active in the past six months in terms of initial access and privileges offered for sale: DarkForums with 221 sale threads, followed by RAMP with 208, then Exploit with 53, Breached with 30, and XSS with 18.

![Chart showing forum activity distribution]

The average alleged revenue of the organizations whose access is being sold in these forums was $3.242 billion, and the average base price for the offerings was $113,275. Both numbers manifest a substantial rise compared to last year (average revenue - $2.232 billion, average base price - $2,726), with the average base price of the offerings increasing by approximately 4055% compared to last year.

## Initial access vectors and privilege types
Analysis of the access types offered for sale revealed 29 distinct types of access. The most frequently advertised access types were RDP (21.2%, 91 offers), VPN (12.8%, 55 offers), and RDWeb (11.2%, 48 offers).

![Chart showing access vector distribution]

The most common privilege types were Domain User with 144 instances (42.9%), followed by Domain Admin with 108 (32.1%) and Local Admin with 42 (12.5%).

![Chart showing privilege type distribution]

Additionally, in RAMP, we observed an exploit targeting a vulnerability in the Oracle E-Business Suite (CVE-2025-61882) being offered for sale. CVE-2025-61882 is a critical vulnerability in Oracle E-Business Suite (versions 12.2.3–12.2.14). This flaw allows unauthenticated attackers to execute arbitrary code via HTTP, resulting in complete system compromise.

## Demographic information
A comprehensive analysis of the underground market for illicit network access points reveals that most available listings concern networks in the United States, totaling 155 unique listings. This substantial figure constitutes a significant 30.9% of the total global data on illicit network access available for purchase.

![Chart showing top targeted countries]

The top 10 targeted countries list is very similar to the one from last year, which also placed the United States at the top. In addition, an analysis of the offerings indicates a pronounced concentration on particular sectors. The government sector is the most frequently targeted category, accounting for 14.2% of the observed offerings.

![Chart showing top targeted sectors]

## Individual analysis of Exploit, XSS, DarkForums, BreachForums, and RAMP

### Exploit
Exploit has continued to function as one of the most technically rigorous Russian-language cybercrime forums. Between 2024 and 2026, it increasingly served as a venue for enterprise network access, VPN, and EDR-bypassed footholds, and post-exploitation tooling. Unlike last year’s offerings that focused on RDP access, the H2 2025 data shows that Exploit’s IABs are more focused on RDweb.

### BreachForums (AKA Breached)
BreachForums has experienced the most visible volatility. By 2025, BreachForums had largely reestablished itself as a data-leak-centric marketplace, with less emphasis on technical exploitation and a greater focus on breached databases, stealer logs, and extortion-related disclosure tactics. The number of IAB threads found this year was around 52% less than in 2024.

### XSS (formerly DaMaGeLaB)
XSS has retained its status as a premier Russian-language forum for initial access sales, ransomware partnerships, and credentialed access to corporate environments. Compared to last year's assessment, this forum showed the most significant shift, going from the most dominant forum for IAB threads to the lowest among the five examined.

### DarkForums
DarkForums rose to prominence as an English-language alternative following repeated disruptions to BreachForums. DarkForums is one of the two new forums that were included in this year’s analysis, and the most dominant in terms of IAB threads. It had a somewhat unique access type, leading the board, Fortinet, followed by SSH, RDP, and Root access.

### RAMP (Russian Anonymous Marketplace)
RAMP has continued to operate as a high-trust, invite-only ecosystem. RAMP listings observed during this period emphasized full domain access, long-term persistence, and revenue-sharing models. The most dominant type of access being sold by RAMP’s IABs was RDP, followed by VPN and Citrix.

## Threat actors active across multiple forums
This research revealed that a subset of threat actors maintains an active presence across multiple forums, with the greatest overlap observed between Breached and DarkForums. This overlap is understandable, since DarkForums was intentionally designed as a "spiritual successor" and a like-for-like replacement for Breached.

## Recommendations
No security strategy can remain static. Policy frameworks and compliance controls alone are insufficient. Continuous monitoring of real-world access behavior is essential. Anomalous logins, unexpected privilege escalations, access outside normal business hours, or activity from unfamiliar locations should be treated as early indicators of compromise.

An effective defense requires making stolen access difficult to exploit. Enforcing least-privilege principles, tightly controlling administrative rights, hardening remote access services with MFA, and accelerating intrusion detection all materially limit an attacker’s ability to escalate and persist.

## Conclusion
The comparison between 2024 and 2025 highlights how initial access brokers continue to adapt to increasingly robust defensive measures. In 2025, high-privilege credentials, such as domain or local administrator accounts, command greater value because they enable rapid lateral movement and immediate operational impact. Access vectors are evolving in parallel; as VPN infrastructure becomes more hardened, attackers are pivoting to RDP, RDWeb, and SSH services that are operationally critical, widely exposed, and often subject to less rigorous scrutiny.