# The 2024 InsurSec Report: Ransomware Edition

## Table of Contents
- [Introduction](#introduction)
- [Key Findings](#key-findings)
- [Chapter 1: The Ransomware Landscape](#chapter-1-the-ransomware-landscape)
- [Chapter 2: Ransomware Attack Vectors](#chapter-2-ransomware-attack-vectors)
- [Chapter 3: Negotiating Ransom Demands](#chapter-3-negotiating-ransom-demands)
- [Conclusion](#conclusion)
- [Methodology](#methodology)

---

## Introduction

Ransomware didn’t just grow in 2023. It evolved.

In 2023, ransomware frequency increased by 64% overall when compared to 2022, mostly driven by a 415% increase in indirect ransomware (an incident where an organization is indirectly impacted by a cyber event on their vendor or partner). Meanwhile, direct ransomware (a ransomware incident where an organization is directly targeted by a cyberattack) also rose 17%, though below the record levels we saw in 2021.

In addition to the return of ransomware, we’ve seen more and more threat actors use both encryption and exfiltration tactics in their attacks, in what we refer to as “double leverage.” Over half of all ransomware claims we saw in 2023 used this tactic, resulting in the highest average ransoms paid when compared to attacks that were either encryption-only or exfiltration-only.

Double leverage attacks are a serious problem because of their downstream domino effect. Oftentimes, the sensitive data exposed by attackers includes data that belongs to the victim’s customers or partners — creating data privacy liabilities to those partners who become collateral damage.

The damage caused by this domino effect is exacerbated when the victim company serves a particular industry, like many vertical Software-as-a-Service (SaaS) companies that tailor their products to specific market segments. This can lead to widespread fallout across entire industries. An outsized example of this occurred in 2023 with the MOVEit breach.

Attackers also evolved with regard to their preferred attack vectors. In 2023, we saw bad actors continue to exploit remote access technologies, making perimeter access tools an increasingly weak link in the chain. Cybercriminals shifted their focus in 2023 from Remote Desktop Protocol (RDP) to targeting self-managed Virtual Private Networks (VPNs) — those implemented on-premises and maintained in-house — which accounted for a whopping 63% of the year’s ransomware events where remote access was the initial entry vector.

Businesses deserve more transparency, software companies responsible for the worst outcomes should be held accountable, and the risk associated with threat actors’ evolving tactics should be laid out in precise terms. We believe this information can help turn the tide against ransomware and further safeguard businesses of all sizes.

By combining expertise from our Cyber Research team along with technical claims data from our Claims and Incident Response teams, we present the full commercial impact caused by ransomware in 2023. By publishing this report, we aim to show the greater business community what has led us to this point and what can be done to reduce the risk that has resulted from this complexity.

---

## Key Findings

1. **DIRECT RANSOMWARE CLAIMS FREQUENCY INCREASED BY 17% IN 2023.**
   In 2023, ransomware claims frequency as a whole jumped 64% year over year, primarily driven by an explosion in indirect ransomware claims frequency that rose 415% over 2022.

2. **REMOTE ACCESS CONTINUES TO BE THE PRIMARY ENTRY VECTOR ACCOUNTING FOR 58% OF CLAIMS.**
   Attackers continued to exploit remote access technology, with 58% of direct ransomware events attributable to a remote access vulnerability. In addition, we saw attackers shift their focus from RDP to targeting self-managed VPNs, which accounted for 63% of the remote access ransomware events in 2023.

3. **ORGANIZATIONS USING SELF-MANAGED VPNS BY CISCO AND CITRIX WERE 11X MORE LIKELY TO FALL VICTIM TO A DIRECT ATTACK IN 2023.**
   The use of self-managed VPNs was correlated with worse outcomes compared to using a cloud-managed VPN or no VPN at all. Two of the most popular self-managed VPNs, Cisco and Citrix, stood out the most when compared to cloud based VPNs or no VPNs at all.

4. **AVERAGE DIRECT RANSOMWARE SEVERITY IN 2023 WAS $370K.**
   Severity was 24% lower than in 2022. Law firms had the highest severity for direct ransomware attacks in 2023, experiencing 32% higher severity than the average.

5. **THE AVERAGE RANSOM PAYMENT IN 2023 WAS $282K.**
   The average ransom demand by attackers was $1.26M, though only 46% of incidents actually ended in a ransom being paid. The average amount paid was over 77% lower than the initial demand.

6. **LOCKBIT AND BLACKCAT WERE USED IN 35% OF RANSOMWARE ATTACKS.**
   We recorded 41 unique ransomware strains used in attacks in 2023, with LockBit and BlackCat/ALPHV overshadowing all others.

7. **THE COMBINATION OF ENCRYPTION AND EXFILTRATION WAS USED IN 51% OF INCIDENTS.**
   A combination of data encryption and exfiltration was the most common direct ransomware tactic. This double leverage tactic was also the most costly for businesses. Encryption and exfiltration events saw the highest median ransom paid ($195K) over encryption-only incidents ($66K) or exfiltration-only incidents ($110K).

> **DIRECT VS. INDIRECT RANSOMWARE**
> For the purposes of this report, we distinguish between two types of ransomware incidents. We define them as:
> * **Direct Ransomware**: A direct attack on an organization resulting in encryption and/or exfiltration of data to hold the organization to ransom.
> * **Indirect Ransomware**: A ransomware attack on a vendor or partner of the organization which results in damages to the organization, typically data privacy breach and/or business interruption.

---

## Chapter 1: The Ransomware Landscape

### Ransomware Frequency Increased 64% in 2023
Ransomware is alive and well. After seeing a decline in ransomware in 2022, in 2023 we saw overall ransomware frequency grow by 64%, with increases in both direct and indirect ransomware.

Direct ransomware claims frequency increased in 2023 by 17%, after a brief reprieve in 2022. Despite its increase in 2023, direct ransomware frequency was still well below 2021 levels. Larger companies saw higher frequencies of direct ransomware, which is no surprise as larger companies tend to have deeper pockets for payouts and more at stake. However, we also saw a 48% increase in direct ransomware for the smallest companies in our portfolio (those with less than $25M in annual revenue).

2023 also revealed a disconcerting trend: a precipitous rise in companies experiencing an indirect ransomware attack. In 2023, indirect ransomware frequency increased by 415% compared to 2022, much of it stemming from the MOVEit vulnerability. Unlike direct ransomware, where the largest companies experienced the highest frequency of attacks, indirect ransomware impacted every revenue band nearly equally.

![Figure 1: Indexed Ransomware Claim Frequency by Year]

### Anatomy of a Supply Chain Attack: MOVEit
In May 2023, threat actors exploited two zero-day vulnerabilities[^1][^2] in the well-known file transfer software MOVEit. This event led to thousands of organizations being impacted, either directly or via the software supply chain. The ransomware gang responsible for the attack, CL0P, used the MOVEit vulnerabilities to infiltrate organizations, steal sensitive personal identifiable information (PII), and threaten to publicly release the data if their ransom demands weren’t met.

The MOVEit incident had a significant impact on organizations in the educational services sector, along with businesses in finance and insurance, due to a handful of vertical (i.e. industry-specific) software products compromised by the attack.

Specifically, threat actors leveraged the MOVEit vulnerabilities to attack the education nonprofit National Student Clearinghouse (NSC). NSC, which produces data and reports on North American high schools, colleges, and universities, partners with 25,000 schools. The attack on the organization led to 890 schools being breached[^3], impacting tens of millions of students and alumni.

Across our portfolio, indirect ransomware related to MOVEit alone increased claims frequency in the education sector by 3.4X compared to 2022.

In a similar case, attackers used the MOVEit vulnerability to attack Pension Benefits Information (PBI), a pension records auditor used by many financial institutions[^4]. This attack alone drove the financial sector to experience 81% higher indirect claims frequency compared to direct ransomware in 2023.

### Ransomware Severity Decreased in 2023
In contrast to ransomware frequency, in 2023 both direct and indirect ransomware severity[^5] in our portfolio dropped year over year. Average direct ransomware severity was $370K, a 24% decrease from 2022, while average 2023 severity for indirect ransomware events came in 55% lower than 2022 at $47K.

We believe this year-over-year decrease in severity may be attributed to clients’ ability to successfully restore from backups more often. When they do, they’re less likely to pay a ransom. We discovered this trend in our recent Backups Report (see Figure 6). Companies who failed to restore their data were 3X more likely to pay a ransom than those who were able to successfully restore from backups.

---

## Chapter 2: Ransomware Attack Vectors

### VPNs Unseat RDP as Leading Entry Vector
Attacks that targeted remote access tools accounted for 58% of ransomware claims in 2023 where an entry vector could be determined. Vulnerabilities in these tools are frequently abused by attackers because these tools are gateways into the network.

Of the ransomware claims where we identified remote access as the initial entry vector, 63% were tied to self-managed VPNs, a reflection of a shift in attackers’ tactics. For years, RDP has been the most popular ransomware attack vector, leading companies to better secure the service and insurers to better account for its risk. This has, in turn, motivated attackers to focus on other types of remote access technology — namely VPNs.

### The Problem with Self-Managed VPNs
Our data shows that businesses that use self-managed VPNs, a version of the technology that is implemented on-premises and maintained by in-house IT teams, are associated with a considerably higher risk of a security incident than businesses that don’t use self-managed VPNs, use more secure cloud-hosted VPNs, or use other remote access technology.

Two particular self-managed VPNs stood out in our ransomware claims data. When normalized for their prevalence in our portfolio, organizations using two of the most popular self-managed VPNs, Cisco ASA and Citrix SSL, were 11X more likely to fall victim to an attack than those who use a cloud VPN or no self-managed VPNs.

* **Cisco ASA**: A flaw in Cisco’s Adaptive Security Appliance (ASA) and Firepower Threat Defense (FTD) appliances (CVE-2023-20269) was responsible for over 10% of direct ransomware claims where remote access was the initial entry vector.
* **CitrixBleed**: Two vulnerabilities in Citrix’s NetScaler products publicly announced in 2023 led to a wave of attacks. Known as “CitrixBleed,” exploitation of these vulnerabilities results in threat actors bypassing security measures like multi-factor authentication (MFA).

---

## Chapter 3: Negotiating Ransom Demands

### Outcomes Can be Heavily Negotiated
The initial ransom demand in 2023 was $1.26 million on average. However, actual ransom payments were only made less than half of the time — and typically at a dramatically lower price than initially demanded. In 2023, the average amount paid by a victim organization ($282k) was 77% less than what was initially demanded by threat actors on average.

### Two Malware Strains Accounted for the Majority of Direct Ransomware Claims
Among the claims we analyzed in 2023, we found 41 unique strains of ransomware used. Yet even with the breadth of variants, LockBit and BlackCat/ALPHV overshadowed all others, accounting for a combined 35% of all claims tied to direct ransomware attacks.

When examining how attacks are spread across different sizes of businesses and industries, it’s crucial to understand that these operations function under a Ransomware-as-a-Service (RaaS) model. This means that the core attackers aren’t launching individual attacks; instead, they distribute their ransomware code to a wide network of affiliates who then carry out the attacks.

### How Threat Actors Use Double Leverage
Threat actors seek to increase their revenue potential by maximizing leverage over a victim. As such, in addition to encrypting company systems, they have evolved to also exfiltrate data. More than half of ransomware attacks we saw in 2023 involved both encryption and exfiltration, or what we call double leverage.

Our data shows claims with both an exfiltration and encryption event had the highest median ransom demand ($600K), as well as highest median payment ($195K). Exfiltration-only events had the second highest ransom paid ($110K).

---

## Conclusion
Ransomware continues to be costly for businesses large and small. Most attacks leverage malware strains developed by a handful of attack groups, and attackers continue to target popular remote access technologies as an initial vector of entry.

The data also confirms what we’ve known to be true for several years: managing IT on-premises significantly increases the risk of an attack. Another noteworthy evolution was the exfiltration of data to achieve double leverage by combining it with encryption tactics. The rise in double leverage incidents caused a meaningful increase in the “blast radius” of each ransomware attack, when multiple partners of each organization found themselves indirectly hit by having their private data included in the exfiltration.

By combining the prevention of security and the protection of insurance, companies can achieve better security and reduce risk. This is the power of the InsurSec model.

---

## Methodology
At-Bay’s analysis is based on claims information from 2021 through the end of 2023. Incidents reviewed included those related to ransomware, either direct or indirect.

**Definition of the Various Ransomware Types Mentioned in This Report**
* **Direct Ransomware**: A ransomware incident where an organization is directly targeted by a cyberattack.
* **Indirect Ransomware**: An incident where an organization is indirectly impacted by a cyber event on their vendor or partner.

**HOW WE CALCULATE SEVERITY FOR THIS REPORT**
Severity calculations include the total incurred loss of a ransomware claim, with development to ultimate selected using actuarial methods leveraging historical experience.

---

[^1]: National Vulnerability Database, https://nvd.nist.gov/vuln/detail/CVE-2023-34362
[^2]: National Vulnerability Database, https://nvd.nist.gov/vuln/detail/CVE-2023-35708
[^3]: California Office of the Attorney General, https://oag.ca.gov/system/files/Exhibit%20A_6.pdf
[^4]: The MOVEit Cyberattack – What happened. PBI’s response. What’s next., https://www.pbinfo.com/the-moveit-cyberattack-what-happened-pbis-response-whats-next/
[^5]: Severity is the financial loss or damages related to a claim