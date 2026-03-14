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

**Organization:** Infoblox  
**Report Title:** DNS-Threat-Landscape-Report  
**Year:** 2025

**The Cyberthreat Fog: How Malicious Actors Use DNS to Deceive and Evade**

Over the past year, threat actors have rapidly advanced their use of deception—scaling operations and leveraging AI to target individuals, organizations, and evade threat research. Infoblox Threat Intel has observed a new level of professionalism and speed in the way actors launch Domain Name System (DNS)-sourced cyberattacks, which affect consumers, businesses, and government agencies alike.

To defend effectively, security teams must understand the threats they face. Gaining insight into adversarial DNS techniques, the actors behind them, and the risks they pose is essential to strengthening defense strategies.

This report draws on vast volumes of real-time DNS telemetry, cutting-edge analytics, and decades of threat expertise to provide a unique perspective on how attackers exploit DNS. It also outlines the business implications and highlights DNS-based intelligence as a critical layer of modern cyberdefense.

## The Untapped Potential of DNS Intelligence

People often refer to DNS as the phonebook of the internet because it translates domain names into IP addresses. Every digital interaction begins with a DNS request, making it a high-fidelity source of telemetry for network operations by providing in-depth visibility into which digital assets are initiating connections over the internet.

DNS is also utilized by malicious actors when phishing, scamming, for detection evasion, and during data extraction. Consequently, analyzing DNS traffic and domain usage is foundational for security analysts. DNS data can be reshaped into predictive threat intelligence by holistically collecting pre-attack telemetry, enriching the data, analyzing it against baselines, and executing deep threat hunts. These insights offer defenders a comprehensive view of adversarial infrastructures, targeted victims, and tactics—before the attacker strikes.

> “DNS unlocks a unique vantage point into past threat activity, which in turn serves as a crystal ball—revealing the precursors to future cyberthreats.” — Dr. Renée Burton, Head of Infoblox Threat Intel

As a result, DNS offers much more than just name resolution and has become both an enforcement point for enterprise security policy and an indicator of potential malicious activity on a network. Organizations like the National Institute of Standards and Technology (NIST) and the Cybersecurity & Infrastructure Security Agency (CISA) have recognized this critical—and early—role that DNS plays in cybersecurity and have highlighted its preemptive security potential in the recently proposed NIST Special Publication (SP) 800-81 Rev. 3.[^1]

[^1]: Secure Domain Name System (DNS) Deployment Guide, National Institute of Standards and Technology (NIST), April 10, 2025.

## Section 1: Top DNS Threat Observations

![Infographic showing 100.8 million newly observed domains in one year and 25.1% of newly observed domains are malicious or suspicious]

### Ephemeral Nature of Domains
As of the end of May 2025, Infoblox was processing and analyzing 70 billion DNS queries daily from over 13,000 Infoblox environments, covering millions of IP addresses across all types of devices.

The fully anonymized data from 1,300+ Infoblox Threat Defense™ customers provides global as well as in-depth visibility into millions of internet interactions, spanning multiple client types, geographies, and industry verticals. Year over year, this DNS telemetry volume increased by 21 percent.

Within all collected data, Infoblox Threat Intel identified 100.8 million newly observed domains (second-level domains) in the past 12 months. This high volume of new domains is often a result of fast-changing infrastructures, short-term advertising campaigns, and branding initiatives.

### Control Evasion Via One-Time-Use Domains
More than one-quarter of the newly observed domains (over 25 million) were classified by Infoblox as malicious or suspicious. Threat actors continuously register, activate, and deploy massive numbers of new domains to evade detection controls. Because it is difficult to identify and classify such large volumes of domains, attackers are able to fly under the radar, bypass blocking mechanisms, and leave minimal forensic evidence.

The isolated usage of identified threat-related domains—both malicious and suspicious—is also significant. Infoblox Threat Intel found that 95 percent of all threat-related domains were observed within a single network environment.

The objective behind this tactic is simple: bypass forensic-based defenses that rely on “patient zero” data by leveraging throwaway domains—of which attackers have unlimited supply.

### Malicious Versus Suspicious Domains
- **Malicious domains** are confirmed threats supported by strong evidence. They do not age out and account for 1.6 percent of over 100 million newly observed domains.
- **Suspicious domains** are potential threats that lack conclusive evidence and account for 23.5 percent of all newly observed domains. If not confirmed, these indicators expire after a few months. Infoblox Threat Intel analysts continuously monitor these domains for new evidence. When additional indicators are discovered, the scores are updated, and suspicious domains may be reclassified as malicious.

### Cloaking Via Domains Part of Traffic Distribution Systems
Adtech (short for advertising technology) refers to the tools, software, and platforms used to automate, manage, target, deliver, and analyze digital advertising. Traffic distribution systems (TDSs) are the platforms or mechanisms used—legitimately or maliciously—to redirect incoming internet traffic to different destinations based on predefined rules. Threat actors also adopted this technology, often referred to as malicious adtech.

Over the past 12 months, 82 percent of all customer environments queried domains that were part of TDS, much of which are operated by malicious adtech operators known for concealing harmful content, such as tailored phishing sites, scareware, scams, and infostealers.

These TDSs often consist of tens of thousands of domains, which are rapidly rotated to evade detection, delivering targeted malicious content to the ideal victims while cloaking that content from threat researchers.

### Domains Linked to Diverse Threat Types
As new threat-related domains are discovered, Infoblox threat researchers investigate the actors behind them and their underlying intent.

**Top 7 List: How Threat Actors Utilize New Domains**
1. Engage in fraudulent activities and scams, such as fake cryptocurrency investment sites.
2. Host illegal content, including gambling (particularly in regions like China) and adult material.
3. Create phishing pages designed to steal personal information or credit card data.
4. Deploy malware. Common examples include infostealers (e.g., Lumma Stealer), loaders via drive-by downloads (e.g., SocGholish), botnets, and ransomware (e.g., BlackBasta).
5. Cloak their activities via TDS and deliver various payloads or trick users into allowing unwanted browser notifications.
6. Distribute potentially unwanted programs (PUPs), such as scareware or unnecessary browser extensions.
7. Conduct spam campaigns and distribute malicious emails.

### Domain Popularity
Infoblox DNS telemetry also provides insights into domain type usage, offering clues about application popularity and the speed at which threat actors are becoming proficient at successfully pushing large volumes of weaponized domains in front of victims.

- **Key Observations:** Eight domain categories—such as content delivery networks (CDNs), technology providers, security vendors, business productivity tools, search engines, storage, cloud services, and net conferencing—account for the majority (approximately 70 percent on a given day) of all domains within customer DNS queries.
- In May 2025, domain queries related to personal internet usage—such as online shopping, gaming, and social media (e.g., TikTok and Facebook)—reached parity with those associated with professional collaboration platforms (e.g., Microsoft Teams, Slack).
- Infoblox Threat Intel observed domains part of TDSs becoming popular in as few as 19 days, 2.35 times faster than in 2024 and 39 times faster than in 2020.

## Section 2: Threat Actors and Research

The 100 million new domains discovered over the past year are not forces of nature—they are always caused by human actions and initiated for specific purposes. Infoblox Threat Intel continuously analyzes and investigates the actors behind threat-related domains by enriching collected telemetry and correlating common patterns.

Since the start of its research, Infoblox Threat Intel discovered a total of 204,000 suspicious domain clusters, each sharing common threat elements, and has identified 662 unique threat actors. In the past 12 months alone, Infoblox researchers have publicly disclosed 10 new actors.

*(Table of key threat actors omitted for brevity, see original report for full list of VexTrio, Hazy Hawk, Enable Scam Actor, etc.)*

## Actor Case Study: Coordination Between WordPress Hackers and VexTrio Viper Cabal

Infoblox recently uncovered a complex alliance between WordPress hackers and a network of malicious adtech companies, notably VexTrio’s TDS.

![Figure 1: Relationship between WordPress hackers and commercial adtech industry showing the flow from compromised sites to TDS infrastructure and finally to malicious content]

**What Happened?**
- **Quick Migration:** When VexTrio’s TDS was disrupted in fall of 2024, multiple malware actors simultaneously shifted to a seemingly new TDS named “Help TDS.” Further analysis revealed that Help TDS is not independent but closely linked to VexTrio.
- **Coordinated Operation:** Infoblox analyzed 4.5 million DNS TXT record responses from compromised websites over six months. This revealed two distinct command-and-control (C2) servers, both hosted on Russian-connected infrastructure.
- **Involvement of Commercial Adtech Firms:** Several adtech companies, including Los Pollos, Partners House, BroPush, and RichAds, were found to be intertwined with VexTrio’s operations.

## Section 3: Malicious DNS Techniques

Threat actors use DNS in various ways and with specific objectives in mind. The most common DNS techniques assigned by Infoblox Threat Intel to threat-related domains include:
- Domains generated by machine algorithms (RDGA, DDGA, and DGA): 54.7%
- Domains used to redirect traffic: 11%
- CNAME or alias domains: 5.8%
- Lookalikes: 5.1%
- Hijacked domains: 5.1%
- Domains used in malicious SMS: 4.2%
- Domains created as part of a TDS: 1.8%
- Domains used for C2 and exfiltration: < 0.4%

### Traffic Distribution Systems Provide a Dangerous Level of Evasion
DNS plays a central role in TDS by covertly redirecting users through multiple intermediary layers—often without their knowledge—based on various attributes like geolocation, device type, or security posture.

### Domain Hijacking to Steal Trust
Threat actors hijack existing domains primarily to exploit the credibility and trust associated with legitimate domains. 
- **Sitting Ducks Attacks:** In 2024, Infoblox estimated that more than 1 million domains are vulnerable to this attack.
- **Dangling CNAMES:** In early 2025, threat actors exploited redirection configurations on high-reputation domains such as cdc[.]gov and several U.S.-based universities.

### Lookalike and Typosquatted Domains Deceive Users
Lookalike domains are slightly altered domain names registered to deceive users. Infoblox identifies several techniques:
- **Homographs/Homoglyphs:** Using visually similar characters from different sets.
- **Typosquats:** Sneaky typing errors.
- **Combosquats:** Combining brand names with keywords like "mail" or "support."
- **Soundsquats:** Domain names that sound similar when spoken aloud.

### DNS Tunneling
While Infoblox observed over 480 unique DNS tunneling domains in some months, an average of more than 100 unique domains related to DNS tunneling were discovered per month between June 2024 and June 2025. Tools include Cobalt Strike, Dnscat2, Sliver, and Iodine.

## Section 4: Challenges for Defenders

### Adversarial AI Bypasses Existing Security Controls
Generative AI (GenAI)—particularly large language models (LLMs)—is driving a transformation in cybersecurity. Adversaries use it to enhance social engineering and detection evasion.

**Case Study: Reckless Rabbit**
Reckless Rabbit recently shifted focus to Japanese-speaking users, promoting fake investment schemes through AI-generated news articles. These sites feature deepfake videos of public figures, like Elon Musk and Masayoshi Son, along with fabricated positive reviews to boost credibility.

### Protecting Brand and Organizational Reputation
Monitoring domains requires tracking not only one’s own domains but also thousands of potential lookalikes. Infoblox detected 28,331 lookalike domains in May 2025.

### Compliance Pressures
Network and security teams face increasing pressure from evolving best practices and new mandates, such as EU NIS2 and NIST SP 800-81 Rev. 3, which require broader oversight—including DNS infrastructure.

## Next Steps
For Threat Researchers:
- Learn more at [https://www.infoblox.com/threat-intel/](https://www.infoblox.com/threat-intel/)
- GitHub: [https://github.com/infobloxopen/threat-intelligence/](https://github.com/infobloxopen/threat-intelligence/)

For Security Teams:
- Request a DNS Security Workshop at [https://info.infoblox.com/sec-ensecurityworkshop-20240901-registration.html](https://info.infoblox.com/sec-ensecurityworkshop-20240901-registration.html)

## Terminology Used
- **Adtech:** Advertising technology.
- **C2:** Command and Control.
- **CDN:** Content Delivery Network.
- **CNAME:** Canonical Name record.
- **DGA:** Domain Generation Algorithm.
- **DNS:** Domain Name System.
- **GDPR:** General Data Protection Regulation.
- **LLM:** Large Language Model.
- **MFA:** Multi-factor authentication.
- **NIST:** National Institute of Standards and Technology.
- **NOD:** Newly Observed Domains.
- **OSINT:** Open-source intelligence.
- **PhaaS:** Phishing-as-a-service.
- **RDGA:** Registered Domain Generation Algorithm.
- **TDS:** Traffic Distribution System.