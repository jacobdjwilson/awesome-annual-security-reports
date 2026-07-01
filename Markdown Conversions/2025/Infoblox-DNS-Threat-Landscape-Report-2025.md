# 2025 DNS THREAT LANDSCAPE REPORT

## Table of Contents
- [The Untapped Potential of DNS Intelligence](#the-untapped-potential-of-dns-intelligence)
- [Section 1: Top DNS Threat Observations](#section-1-top-dns-threat-observations)
- [Section 2: Threat Actors and Research](#section-2-threat-actors-and-research)
- [Actor Case Study: Coordination Between WordPress Hackers and VexTrio Viper Cabal](#actor-case-study-coordination-between-wordpress-hackers-and-vextrio-viper-cabal)
- [Section 3: Malicious DNS Techniques](#section-3-malicious-dns-techniques)
- [Section 4: Challenges for Defenders](#section-4-challenges-for-defenders)
- [Next Steps](#next-steps)
- [Terminology Used](#terminology-used)

---

2025 DNS THREAT LANDSCAPE REPORT
The Cyberthreat Fog: How Malicious Actors Use DNS to Deceive and Evade

Over the past year, threat actors have rapidly advanced their use of deception—scaling operations and leveraging AI to target individuals, organizations, and evade threat research. Infoblox Threat Intel has observed a new level of professionalism and speed in the way actors launch Domain Name System (DNS)-sourced cyberattacks, which affect consumers, businesses, and government agencies alike.

To defend effectively, security teams must understand the threats they face. Gaining insight into adversarial DNS techniques, the actors behind them, and the risks they pose is essential to strengthening defense strategies.

This report draws on vast volumes of real-time DNS telemetry, cutting-edge analytics, and decades of threat expertise to provide a unique perspective on how attackers exploit DNS. It also outlines the business implications and highlights DNS-based intelligence as a critical layer of modern cyberdefense.

## The Untapped Potential of DNS Intelligence

People often refer to DNS as the phonebook of the internet because it translates domain names into IP addresses. Every digital interaction begins with a DNS request, making it a high-fidelity source of telemetry for network operations by providing in-depth visibility into which digital assets are initiating connections over the internet.

DNS is also utilized by malicious actors when phishing, scamming, for detection evasion, and during data extraction. Consequently, analyzing DNS traffic and domain usage is foundational for security analysts. DNS data can be reshaped into predictive threat intelligence by holistically collecting pre-attack telemetry, enriching the data, analyzing it against baselines, and executing deep threat hunts. These insights offer defenders a comprehensive view of adversarial infrastructures, targeted victims, and tactics—before the attacker strikes.

As a result, DNS offers much more than just name resolution and has become both an enforcement point for enterprise security policy and an indicator of potential malicious activity on a network. Organizations like the National Institute of Standards and Technology (NIST) and the Cybersecurity & Infrastructure Security Agency (CISA) have recognized this critical—and early—role that DNS plays in cybersecurity and have highlighted its preemptive security potential in the recently proposed NIST Special Publication (SP) 800-81 Rev. 3.[^1]

> “DNS unlocks a unique vantage point into past threat activity, which in turn serves as a crystal ball—revealing the precursors to future cyberthreats.” — Dr. Renée Burton, Head of Infoblox Threat Intel

This report addresses four key questions:
- What are the key DNS observations from the past 12 months?
- Who are the DNS threat actors and what recent activities have been discovered?
- What are the main malicious tactics behind DNS techniques and why are they dangerous?
- What are the key challenges for defenders, and what opportunities does DNS-based threat intelligence offer?

[^1]: Secure Domain Name System (DNS) Deployment Guide, National Institute of Standards and Technology (NIST), April 10, 2025.

## Section 1: Top DNS Threat Observations

![Infographic showing 100.8 million newly observed domains in one year and 25.1% of newly observed domains are malicious or suspicious]

### Ephemeral Nature of Domains
As of the end of May 2025, Infoblox was processing and analyzing 70 billion DNS queries daily from over 13,000 Infoblox environments, covering millions of IP addresses across all types of devices.

The fully anonymized data from 1,300+ Infoblox Threat Defense™ customers provides global as well as in-depth visibility into millions of internet interactions, spanning multiple client types, geographies, and industry verticals. Year over year, this DNS telemetry volume increased by 21 percent.

Within all collected data, Infoblox Threat Intel identified 100.8 million newly observed domains (second-level domains) in the past 12 months. This high volume of new domains is often a result of fast-changing infrastructures, short-term advertising campaigns, and branding initiatives.

### Control Evasion Via One-Time-Use Domains
More than one-quarter of the newly observed domains (over 25 million) were classified by Infoblox as malicious or suspicious. Threat actors continuously register, activate, and deploy massive numbers of new domains to evade detection controls. Because it is difficult to identify and classify such large volumes of domains, attackers are able to fly under the radar, bypass blocking mechanisms, and leave minimal forensic evidence.

![Infographic showing 95% of threat-related domains were observed in only one customer environment]

The isolated usage of identified threat-related domains—both malicious and suspicious—is also significant. Infoblox Threat Intel found that 95 percent of all threat-related domains were observed within a single network environment. The objective behind this tactic is simple: bypass forensic-based defenses that rely on “patient zero” data by leveraging throwaway domains—of which attackers have unlimited supply.

### Malicious Versus Suspicious Domains
- **Malicious domains** are confirmed threats supported by strong evidence. They do not age out and account for 1.6 percent of over 100 million newly observed domains.
- **Suspicious domains** are potential threats that lack conclusive evidence and account for 23.5 percent of all newly observed domains. If not confirmed, these indicators expire after a few months. Infoblox Threat Intel analysts continuously monitor these domains for new evidence. When additional indicators are discovered, the scores are updated, and suspicious domains may be reclassified as malicious.

### Cloaking Via Domains Part of Traffic Distribution Systems
Adtech (short for advertising technology) refers to the tools, software, and platforms used to automate, manage, target, deliver, and analyze digital advertising. Traffic distribution systems (TDSs) are the platforms or mechanisms used—legitimately or maliciously—to redirect incoming internet traffic to different destinations based on predefined rules.

![Infographic showing 82% of customers queried a domain part of a traffic distribution system]

Over the past 12 months, 82 percent of all customer environments queried domains that were part of TDS, much of which are operated by malicious adtech operators known for concealing harmful content, such as tailored phishing sites, scareware, scams, and infostealers.

These TDSs often consist of tens of thousands of domains, which are rapidly rotated to evade detection, delivering targeted malicious content to the ideal victims while cloaking that content from threat researchers.

### Domains Linked to Diverse Threat Types
As new threat-related domains are discovered, Infoblox threat researchers investigate the actors behind them and their underlying intent.

**Table 1. Actors’ purpose for newly observed domains.**
1. Engage in fraudulent activities and scams, such as fake cryptocurrency investment sites.
2. Host illegal content, including gambling (particularly in regions like China) and adult material.
3. Create phishing pages designed to steal personal information or credit card data.
4. Deploy malware. Common examples include infostealers (e.g., Lumma Stealer), loaders via drive-by downloads (e.g., SocGholish), botnets, and ransomware (e.g., BlackBasta).
5. Cloak their activities via TDS and deliver various payloads or trick users into allowing unwanted browser notifications.
6. Distribute potentially unwanted programs (PUPs), such as scareware or unnecessary browser extensions.
7. Conduct spam campaigns and distribute malicious emails.

### Domain Popularity
Infoblox DNS telemetry also provides insights into domain type usage, offering clues about application popularity and the speed at which threat actors are becoming proficient at successfully pushing large volumes of weaponized domains in front of victims.

![Infographic showing 19 days as the time needed for a TDS domain to become popular]

- **Key Observations:**
    - Eight domain categories—such as content delivery networks (CDNs), technology providers, security vendors, business productivity tools, search engines, storage, cloud services, and net conferencing—account for the majority (approximately 70 percent on a given day) of all domains within customer DNS queries.
    - In May 2025, domain queries related to personal internet usage—such as online shopping, gaming, and social media (e.g., TikTok and Facebook)—reached parity with those associated with professional collaboration platforms (e.g., Microsoft Teams, Slack).
    - Infoblox Threat Intel observed domains part of TDSs becoming popular in as few as 19 days, 2.35 times faster than in 2024 and 39 times faster than in 2020.

## Section 2: Threat Actors and Research

![Infographic showing 204K total identified suspicious DNS domain clusters, 662 total identified threat actors, and 10 new actors publicly disclosed in the past 12 months]

Since the start of its research, Infoblox Threat Intel discovered a total of 204,000 suspicious domain clusters, each sharing common threat elements, and has identified 662 unique threat actors. In the past 12 months alone, Infoblox researchers have publicly disclosed 10 new actors.

### Actor Case Study: Coordination Between WordPress Hackers and VexTrio Viper Cabal

Infoblox recently uncovered a complex alliance between WordPress hackers and a network of malicious adtech companies, notably VexTrio’s TDS.

![Figure 1: Relationship between WordPress hackers and commercial adtech industry]

**What Happened?**
- **Quick Migration:** When VexTrio’s TDS was disrupted in fall of 2024, multiple malware actors simultaneously shifted to a seemingly new TDS named “Help TDS.” Further analysis revealed that Help TDS is not independent but closely linked to VexTrio.
- **Coordinated Operation:** Infoblox analyzed 4.5 million DNS TXT record responses from compromised websites over six months. This revealed two distinct command-and-control (C2) servers, both hosted on Russian-connected infrastructure.
- **Involvement of Commercial Adtech Firms:** Several adtech companies, including Los Pollos, Partners House, BroPush, and RichAds, were found to be intertwined with VexTrio’s operations.

## Section 3: Malicious DNS Techniques

**Table 2. DNS techniques assigned to threat-related domains (Jan 2025 – June 2025)**
- Domains generated by machines algorithms (RDGA, DDGA and DGA): 54.7%
- Domains used to redirect traffic: 11%
- CNAME or alias domains: 5.8%
- Lookalikes: 5.1%
- Hijacked domains: 5.1%
- Domains used in malicious SMS: 4.2%
- Domains created as part of a TDS: 1.8%
- Domains used for C2 and exfiltration: < 0.4%

### Traffic Distribution Systems Provide a Dangerous Level of Evasion
DNS plays a central role in TDS by covertly redirecting users through multiple intermediary layers. Malicious adtech delivers the right content to the right victim at the right moment.

![Figure 2: A high-level picture of the three players in malicious adtech; affiliates, operators, and malicious advertisers]

**Table 4. TDS operators and delivered malicious content**
| DNS Operators | Malware | Scams | Phishing | Hijacked Domain |
| :--- | :---: | :---: | :---: | :---: |
| Vacant Viper | X | X | | X |
| Vane Viper | X | X | X | |
| Vextrio Viper | X | X | X | X |
| Hasty Hawk | | | X | X |
| Sophisticated Chickens | | | X | X |
| Black TDS | X | | X | |
| Parrot TDS | X | | | |
| R0bl0ch0n TDS | | X | | |

### Domain Hijacking to Steal Trust
Threat actors hijack existing domains primarily to exploit the credibility and trust associated with legitimate domains.
- **Sitting Ducks Attacks:** In 2024, Infoblox estimated that more than 1 million domains are vulnerable to this attack.
- **Dangling CNAMES:** In early 2025, threat actors exploited redirection configurations on high-reputation domains such as `cdc[.]gov` and several U.S.-based universities.

### Lookalike and Typosquatted Domains Deceive Users
Lookalike domains are slightly altered domain names registered to deceive users. Infoblox identified several techniques:
- **Homographs/Homoglyphs:** Visually similar characters from different sets.
- **Typosquats:** Sneaky typing errors.
- **Combosquats:** Combining brand names with keywords (e.g., "mail", "security").
- **Soundsquats:** Domains that sound similar when spoken aloud.

### DNS Tunneling Used by Threat Actors, Pentesters and Legitimate Security Tools
DNS tunneling encodes data within DNS queries and responses. An average of more than 100 unique domains related to DNS tunneling were discovered per month between June 2024 and June 2025. Prevalent tools include Cobalt Strike, Dnscat2, DNS Exfiltrator, Sliver, Weasel, Pupy, and Iodine.

## Section 4: Challenges for Defenders

![Infographic showing 88% of AI-generated malware evades detection]

### Adversarial AI Bypasses Existing Security Controls
Generative AI is lowering the barrier to creating deceptive content.
- **Deepfake Scams:** Criminals are using voice cloning and deepfake videos to commit fraud at scale.
- **Case Study:** Reckless Rabbit uses deepfake videos of public figures like Elon Musk and Masayoshi Son to promote fake investment schemes to Japanese-speaking victims.
- **AI-Powered Chatbots:** Actors use chatbots to automate and scale personalized, long-term social engineering scams.

### Protecting Brand and Organizational Reputation
- Infoblox detected 28,331 lookalike domains in May 2025.
- 87 percent of discovered high-risk domains are registered with entities sanctioned by OFAC, making takedowns difficult.

### Compliance Pressures and DNS Challenges
Frameworks like EU NIS2 and NIST SP 800-81 Rev. 3 require broader oversight of DNS infrastructure. Challenges include operational complexity, fragmented tooling, limited resources, and budget constraints.

## Next Steps
- **For Threat Researchers:** Visit [Infoblox Threat Intel](https://www.infoblox.com/threat-intel/), follow on Mastodon at `infobloxthreatintel@infosec.exchange`, or access indicators on [GitHub](https://github.com/infobloxopen/threat-intelligence/).
- **For Security Teams:** Request a [DNS Security Workshop](https://info.infoblox.com/sec-ensecurityworkshop-20240901-registration.html) or learn more about [Infoblox Threat Defense](https://www.infoblox.com/products/threat-defense/).

## Terminology Used
- **Adtech:** Advertising technology.
- **BYOD:** Bring your own device.
- **C2:** Command and control.
- **CDN:** Content delivery network.
- **CNAME:** Canonical Name record.
- **DDGA:** Dictionary domain generation algorithm.
- **DDI:** DNS, DHCP, and IP address management.
- **DGA:** Domain generation algorithm.
- **DNS:** Domain Name System.
- **GDPR:** General Data Protection Regulation.
- **HIPAA:** Health Insurance Portability and Accountability Act.
- **LLM:** Large language model.
- **MFA:** Multi-factor authentication.
- **MX Abuse:** Misuse of mail exchange records.
- **NIST:** National Institute of Standards and Technology.
- **NOD:** Newly observed domains.
- **OFAC:** Office of Foreign Assets Control.
- **OSINT:** Open-source intelligence.
- **PCI DSS:** Payment Card Industry Data Security Standard.
- **PhaaS:** Phishing-as-a-service.
- **RDGA:** Registered domain generation algorithm.
- **SASE:** Secure Access Service Edge.
- **TDS:** Traffic distribution system.