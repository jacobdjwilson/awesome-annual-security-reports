THREAT RESEARCH

Initial Access Brokers have Shifted
to High-Value Targets and Premium
Pricing

Rapid7 Labs

Mar 31, 2026 | Last updated on Mar 31, 2026 | 16 min read

DISCOVER RAPID7 MDR

Initial Access Brokers (IABs) are a key component of the cybercrime ecosystem, offering hassle-free building blocks

for ransomware, data theft, and extortion. Rapid7’s analysis of H2 2025 activity across five major forums grants fresh

insight into a power balance shift toward initial access sales from newer marketplaces, such as RAMP and

DarkForums. Higher asking prices and more focus on high-value sectors and large organizations, such as

Government, Retail, and IT, reveal a mature and profit-focused IAB market.

This blog highlights key access trends and pricing, pinpoints the most targeted industries and regions, and gives

actionable recommendations for identifying and isolating potential breaches via popular IAB offerings.

Key findings

Our detailed analysis of six months of data from Exploit, XSS, BreachForums, DarkForums, and RAMP reveals the

following key findings:

Access prices and target organization size increased dramatically: The average alleged victim revenue and

offering base price have increased significantly compared to the previous year, indicating that IABs are targeting

larger, higher-value enterprises and charging premium prices for quality access.

Primary access vectors haven’t changed: RDP, VPN, and RDWeb remain the top access vectors being offered

for sale, which means that remote access infrastructure is still the primary attack surface for initial access sales.

High-privilege access is increasingly prioritized: Most common privilege levels being offered by IABs are

Domain User (42.9%), Domain Admin (32.1%), and Local Admin (12.5%), with a visible decline in lower-privilege

offerings, such as Local User privileges. It seems the market is shifting from volume to high-impact access that

enables faster and more efficient malicious operations, such as ransomware and extortion attacks.

Certain underground marketplaces have become favored over others: DarkForums (221 threads) and RAMP

(208 threads) were the most active forums for initial access sales in H2 2025, accounting together for 81% of the

observed threads. At the same time, older, historically dominant forums such as XSS and Exploit saw significant

declines in IAB activity.

IABs target specific industries: IAB activity is primarily concentrated on sectors offering the highest potential

for financial gain or intelligence acquisition: Government, Retail, and Information Technology (IT).

Focus on government access: The Government sector is the most frequently targeted industry vertical, at 14.2%

(Retail and Information Technology follow with 13.1% and 10.8%, respectively). 'Admin panel' access is the most

commonly observed type offered for this sector, with DarkForums serving as the principal platform for its sale.

IAB and cybercrime forum landscape in 2026

Just as in 2025, cybercriminal forums continue to serve as the primary marketplaces for the promotion and sale of

pirated network access. Platforms such as Exploit, BreachForums, XSS, DarkForums, and RAMP have remained

central pillars of the cybercriminal underground through 2025 and into 2026, despite sustained law-enforcement

pressure, infrastructure seizures, and repeated cycles of disruption and rebirth. In response to the continued

relevance, Rapid7 threat intelligence researchers expanded their monitoring to include all five forums, tracking

activity from January through December 2025. The primary objective was to benchmark Initial Access Broker (IAB)

activity and adjacent services, including an in-depth analysis of tactics, techniques, and procedures (TTPs), initial

access vectors, credential and session pricing, victim geographies, and evolving monetization strategies.

Why cybercrime forums matter in 2026

We selected these five forums for their continued relevance, the concentration of experienced actors, and their

distinct functional roles within the cybercriminal ecosystem. Collectively, they represent the full lifecycle of modern

cybercrime from initial compromise and access brokerage to data monetization, extortion, and ransomware

enablement. Despite repeated takedowns and administrator arrests, the past two years have demonstrated that

forum resilience, brand persistence, and rapid reconstitution remain defining characteristics of the underground

economy. Monitoring activity across these platforms, particularly from reputable, high-volume IABs and repeat

sellers, provides critical insight into shifting attacker priorities, preferred access vectors, and pricing dynamics.

Exploit, XSS, DarkForums, BreachForums, and
RAMP: Combined data analysis

Last year, in The Rapid7 2025 Access Brokers Report, we analyzed the data of three main cybercrime forums, Exploit,

XSS, and BreachForums. This year, we have expanded this list to include two additional (and very popular) forums,

DarkForums and RAMP.

In fact, the newly analyzed forums were the most active in the past six months in terms of initial access and

privileges offered for sale: DarkForums with 221 sale threads, followed by RAMP with 208, then Exploit with 53,

Breached with 30, and XSS with 18. This might indicate a certain change in shifts in terms of popularity between the

newer forums and the older ones.

⠀

The average alleged revenue of the organizations whose access is being sold in these forums was $3.242 billion, and

the average base price for the offerings was $113,275. However, it is important to keep in mind that victim revenue

numbers are broker-provided based on their own online research, and as such, they may not necessarily be

accurate.

Both numbers manifest a substantial rise compared to last year (average revenue - $2.232 billion, average base price

- $2,726), with the average base price of the offerings increasing by approximately 4055% compared to last year.

Notably, these numbers are especially affected by DarkForums, with tremendously high values in both counts. They

show that IABs have become more resourceful, finding weak spots in larger organizations, and also much greedier

in terms of the price of their offerings.

Initial access vectors and privilege types

Analysis of the access types offered for sale revealed 29 distinct types of access. The most frequently advertised

access types were RDP (21.2%, 91 offers), VPN (12.8%, 55 offers), and RDWeb (11.2%, 48 offers).

⠀

The most common privilege types were Domain User with 144 instances (42.9%), followed by Domain Admin with

108 (32.1%) and Local Admin with 42 (12.5%).

In many observed cases, VPN and RDWeb access are sold with the Domain User privilege, while RDP is sold with

either Domain User or Domain Admin.

If we compare the numbers of the top 5 access types offered for sale to last year’s data, we can see that RDP access

has become more prevalent than VPN, although both access types remain the leading two categories. In addition, it

seems that RDweb is much more popular among the sellers.

⠀

As for the privilege types, the clear dominance of the Domain User privilege offered for sale has declined, though it

remains the most common privilege type sold by IABs. In addition, the newer dataset lacks any mentions of the

Local User privilege. The data indicates a decline in the previously dominant Domain User access offering. Despite

this decrease, Domain User access remains the most frequently sold privilege level among Initial Access Brokers

(IABs). Notably, the updated dataset contains no instances of Local User privilege sales.

This shift likely reflects evolving IAB monetization strategies and changing buyer demand. While Domain User

access remains valuable for its broad network reach, its reduced dominance may signal heightened market

competition, stronger defensive controls, or strategic diversification into alternative access types. The complete

absence of Local User privileges suggests diminishing operational relevance and limited resale value, as threat

actors increasingly prioritize access that facilitates lateral movement, privilege escalation, and rapid operational

impact.

⠀

Additionally, in RAMP, we observed an exploit targeting a vulnerability in the Oracle E-Business Suite (CVE-2025-

61882) being offered for sale.

⠀

⠀

CVE-2025-61882 is a critical vulnerability in Oracle E-Business Suite (versions 12.2.3–12.2.14). This flaw allows

unauthenticated attackers to execute arbitrary code via HTTP, resulting in complete system compromise.

The vulnerability has been exploited as a zero-day by the Cl0p criminal organization to exfiltrate financial and

human resources data for subsequent extortion attempts, as documented in the Rapid7 blog.

Demographic information

A comprehensive analysis of the underground market for illicit network access points reveals that most available

listings concern networks in the United States, totaling 155 unique listings.

This substantial figure constitutes a significant 30.9% of the total global data on illicit network access available for

purchase. The dominance of the U.S. in this domain suggests a confluence of factors, including the sheer size and

connectivity of its network infrastructure, the high value associated with compromised U.S. enterprise and

government networks, and the relative wealth of potential buyers seeking access to these environments. The

visibility of U.S.-based access points on darknet marketplaces underscores a considerable vulnerability and

highlights the attractiveness of U.S. targets to cybercriminal syndicates seeking initial access for subsequent

malicious activities such as data exfiltration, ransomware deployment, or espionage.

⠀

The top 10 targeted countries list is very similar to the one from last year, which also placed the United States at the

top, with a large margin from the following countries (the United Kingdom, India, and Brazil).

In addition, an analysis of the offerings indicates a pronounced concentration on particular sectors. The government

sector is the most frequently targeted category, accounting for 14.2% of the observed offerings, likely due to the

substantial value of sensitive data held. The retail industry closely follows at 13.1%, attracting IABs due to the

presence of payment card information (PCI) and personally identifiable information (PII). The Information

Technology (IT) sector is the third most frequent target, at 10.8%, valued for its potential as a supply chain vector to

compromise a wide range of clients.

This strategic focus on Government, Retail, and IT underscores the IAB community's prioritization of targets that

promise the greatest financial return, intelligence acquisition, or potential for systemic disruption.

⠀

Unlike the top 10 countries list, the top 10 targeted sectors list is very different from last year’s, which was

dominated by the Financial Services and IT sectors, with few network access offerings from organizations in the

Government and Retail sectors. This is likely due to the inclusion of DarkForums in this year’s analysis, which usually

contain many sellers offering access to government networks.

Individual analysis of Exploit, XSS, DarkForums,
BreachForums, and RAMP

The following is a detailed, individual analysis of the five forums, covering their history, operations, and key trends

from the latter half of 2025. This includes an examination of common illicit listings, typical base price ranges, and

frequently targeted regions.

Exploit

Exploit has continued to function as one of the most technically rigorous Russian-language cybercrime forums.

Historically focused on exploits, malware development, and high-end IAB offerings, Exploit has maintained a

comparatively stable operational posture over the past two years. While selectively restricting access and tightening

vetting following multiple international law enforcement takedowns of peer forums, Exploit has benefited from its

long-standing reputation system and senior moderator structure. Between 2024 and 2026, it increasingly served as a

venue for enterprise network access, VPN, and EDR-bypassed footholds, and post-exploitation tooling, rather than

commodity credential sales.

Unlike last year’s offerings that focused on RDP access, the H2 2025 data shows that Exploit’s IABs are more focused

on RDweb. The shift from RDP access to RDWeb access in H2 2025 is likely due to improved defenses against direct

exposure to the RDP protocol. Faced with reduced capabilities to secure or remove RDP access points exposed to

the internet, attackers are adapting by targeting RDWeb portals, which are often vulnerable and sometimes less

well-protected. RDWeb offers reliable access to enterprise environments, making it an attractive alternative for initial

access brokers. The United States remains the most targeted country, accounting for approximately 40% of cases in

which the organization’s location is specified.

⠀

Interestingly, while the average alleged revenue of the targeted organizations dropped from approximately $314

million to only $58 million, the base price of the offerings has gone 6 times higher than last year.

BreachForums (AKA Breached)

BreachForums has experienced the most visible volatility. Following multiple seizures and arrests in 2023–2024, the

forum underwent several reboots under new administrators, each attempting to inherit the brand equity of the

original platform. By 2025, BreachForums had largely reestablished itself as a data-leak-centric marketplace, with

less emphasis on technical exploitation and a greater focus on breached databases, stealer logs, and extortion-

related disclosure tactics. Trust erosion from repeated compromises, however, pushed higher-tier IABs and

ransomware affiliates toward more closed or Russian-language platforms, reducing BreachForums’ role in elite

access brokerage by 2026.

The precarious status of the Breached forum, as it is now called, is reflected by the number of IAB threads found this

year (around 52% less than in 2024). This is likely due to the disappearance of very dominant players in the IAB

community, such as IntelBroker (real name: Kai West), who was apprehended by law enforcement and charged in

the U.S. with his crimes. Accordingly, the variety of access types was much more limited, dominated by remote code

execution (RCE) and Shell access. However, unlike last year, which included only Domain Admin, this year we noticed

additional privilege types offered: Domain User and Local Admin.

⠀

Just like in the other examined forums, the United States is the most targeted country (17.4%) in Breached, but by a

substantially smaller percentage compared to last year.

As for the pricing, we see an opposite trend compared to Exploit - while the average alleged revenue of the

targeted organizations has slightly increased in 2025, the base price of the offerings in Breached was cut in half.

XSS (formerly DaMaGeLaB)

XSS has retained its status as a premier Russian-language forum for initial access sales, ransomware partnerships,

and credentialed access to corporate environments. Following intermittent downtime and administrator turnover in

2024, XSS emerged in 2025 with reinforced operational security practices and stricter membership controls. Over

the past two years, XSS has increasingly served as a coordination hub for post-access collaboration, including

handoffs between IABs, ransomware operators, and data theft specialists. Pricing trends observed on XSS indicate a

shift toward higher-value, lower-volume access, particularly in Western enterprise environments.

Compared to last year's assessment, this forum showed the most significant shift. It went from being the most

dominant forum for IAB threads to the lowest among the five forums we examined. In H2 of 2025, we only located

around 20 threads (compared to almost 200 in 2024). This small number of threads makes XSS stats so statistically

negligible as to be unanalyzable. This decline is likely due to many IABs shifting to newer, “shinier” cybercrime

forums, such as DarkForums and RAMP.

DarkForums

DarkForums rose to prominence as an English-language alternative following repeated disruptions to

BreachForums. Between 2024 and 2026, DarkForums positioned itself as a hybrid marketplace, blending breach data

sales, low- to mid-tier IAB offerings, and fraud services. While it lacks the technical depth of Exploit or XSS,

DarkForums has become a key on-ramp for emerging actors, especially those operating stealer malware or reselling

access obtained using phishing and MFA fatigue attacks. Its relatively open registration model has resulted in higher

signal-to-noise ratios, but it remains valuable for tracking early-stage monetization trends.

DarkForums is one of the two new forums that were included in this year’s analysis, and the most dominant in terms

of IAB threads. It had a somewhat unique access type, leading the board, Fortinet, followed by SSH, RDP, and Root

access. The Fortinet access points were predominantly sold by a very active DarkForums user, BigBro. Interestingly,

we also found another user, Big-Bro, active on RAMP, who is likely the same user, although selling different types of

access points.

⠀

Similar to the other forums, the most targeted country on DarkForums was the United States (25.8%); however,

unlike the others, many of the network access offerings were from organizations in the Government and Retail

sectors.

As for the pricing, DarkForums had the highest average of alleged targeted organization revenue and offering base

price by a very large margin compared to the rest.

RAMP (Russian Anonymous Marketplace)

RAMP has continued to operate as a high-trust, invite-only ecosystem following its resurgence after earlier

disruptions by law enforcement. By 2025–2026, RAMP solidified its role as a convergence point for ransomware

affiliates, IABs, and cash-out services, rather than a general discussion forum. RAMP listings observed during this

period emphasized full domain access, long-term persistence, and revenue-sharing models, reflecting a mature,

partnership-driven cybercrime economy. Its closed nature limits visibility, but the activity that does surface suggests

alignment with the most operationally sophisticated threat actors.

RAMP was another newly examined forum and the second-highest in terms of IAB threads. The most dominant type

of access being sold by RAMP’s IABs was RDP, followed by VPN and Citrix by a large margin. The most common

privilege types for sale were Domain User (56.4%) and Domain Admin (33.9%). Notably, most of the threads that

were analyzed for this forum (78.8%) belonged to only two users, Big-Bro (mentioned earlier) and an allegedly

Albanian user, lacrim.

⠀

In RAMP, the United States continued to lead the list of targeted countries (36.5%). The average alleged targeted

organization revenue was approximately $440 million, and the average base price was almost $6400.

Threat actors active across multiple forums

This research revealed that a subset of threat actors maintains an active presence across multiple forums, with the

greatest overlap observed between Breached and DarkForums. This overlap is understandable, since DarkForums

was intentionally designed as a "spiritual successor" and a like-for-like replacement for Breached following the

latter's frequent law-enforcement disruptions. Consequently, the two platforms share a nearly identical visual and

structural layout, both utilizing the MyBB forum software to create a familiar environment for users.

Recommendations

No security strategy can remain static. Policy frameworks and compliance controls alone are insufficient. Continuous

monitoring of real-world access behavior is essential. Anomalous logins, unexpected privilege escalations, access

outside normal business hours, or activity from unfamiliar locations should be treated as early indicators of

compromise.

Proactive threat intelligence further enables defenders to anticipate which access methods are most likely to be

targeted. An effective defense requires making stolen access difficult to exploit. Enforcing least-privilege principles,

tightly controlling administrative rights, hardening remote access services with MFA, and accelerating intrusion

detection all materially limit an attacker’s ability to escalate and persist. While breaches may still occur, rapid

identification and containment can prevent them from becoming full-scale incidents. Organizations that evolve their

defenses in step with access brokers can erode the attackers’ advantage, increasing the cost and reducing the

effectiveness of cybercrime.

Conclusion

The comparison between 2024 and 2025 highlights how initial access brokers continue to adapt to increasingly

robust defensive measures. As organizations strengthen their security postures, attackers refine the types of access

they steal and monetize to maintain effectiveness. In 2025, high-privilege credentials, such as domain or local

administrator accounts, will command greater value because they enable rapid lateral movement and immediate

operational impact, leaving defenders little time to detect and respond. Lower-privilege access is steadily losing

value, signaling a clear shift from volume-driven access sales to a focus on quality and impact. Access vectors are

evolving in parallel. As VPN infrastructure becomes more hardened and closely monitored, attackers are pivoting to

RDP, RDWeb, and SSH services that are operationally critical, widely exposed, and often subject to less rigorous

scrutiny. This shift reflects a pragmatic path-of-least-resistance strategy rather than any decline in attacker

sophistication.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-23", "model": "gemini-3.5-flash-lite"} -->
