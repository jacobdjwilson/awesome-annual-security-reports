# Cyber-Threat-Intelligence-Report-Vol2

## Table of Contents
- [Key trends](#key-trends)
- [Ransomware attacks still prove profitable](#ransomware-attacks-still-prove-profitable)
- [Supply chains offer attack foothold](#supply-chains-offer-attack-foothold)
- [Infostealers boost the malware market](#infostealers-boost-the-malware-market)
- [Cloud-centricity prompts new attack vectors](#cloud-centricity-prompts-new-attack-vectors)
- [Vulnerability exploits see high volume buying and selling](#vulnerability-exploits-see-high-volume-buying-and-selling)
- [References](#references)
- [Contacts](#contacts)
- [About Accenture](#about-accenture)

Accenture has been creating relevant, timely and actionable threat intelligence for more than 20 years. Our cyber threat intelligence and incident response team is continually investigating numerous cases of financially motivated targeting and suspected cyber espionage.

During these investigations, our threat intelligence and incident response analysts have gained firsthand visibility into the tactics, techniques and procedures (TTPs) employed by some of the most sophisticated cyber adversaries. This report reflects analysis during the second half of calendar year 2021 (H2 2021).

## Key trends

Following analysis in H2 2021, Accenture identified five trends affecting the cybersecurity landscape:

1. Ransomware attacks still prove profitable
2. Supply chains offer attack footholds
3. Information stealers boost the malware market
4. Cloud-centricity prompts new attack vectors
5. Vulnerability exploits see high volume buying and selling

## Ransomware attacks still prove profitable

Despite technology enabling threat actors to become even more sophisticated, there are still active and evolving risks from tried and tested ransomware techniques. And there is consistency of ranking for the top targeted industries throughout Q3 of calendar year 2021, with ransomware threat actors proving most successful against the manufacturing industry, followed by financial services, healthcare, technology and construction.

Ransomware attacks continued to be profitable; among the most active ransomware groups in 2021 were LockBit and Conti, but tracking individual groups remains challenging due to continuous “retirements” and rebranding into new groups due to law enforcement pressure or internal group dynamics.

Conflict between ransomware affiliates and their operators led to information leaks. Arguments between involved parties serve as one example of the unintended consequences of ransom-affiliate payment schemes. Despite these problems, ransomware operations remain highly profitable.

What is more, increasingly, ransomware operators abused cloud infrastructure and introduced new encryption techniques to better evade detection and increase impact.

Based on data collection from Accenture incident response engagements, ransomware and extortion operations made up almost 35% of intrusion volume in 2021 and represented a 107% year-over-year increase from 2020.

In addition, the United States was again the top region impacted by ransomware and extortion threats, representing approximately 45% of intrusion volume in 2021.

![Figure 1. Ransomware by geography (Incident response)]

### What’s happening?

*   **Top four industry targets remain the same**: The number of ransomware attacks decreased slightly in Q3 compared to Q2 of calendar year 2021, with manufacturing, financial services, healthcare and technology remaining the most targeted industries.
*   **New RAMP forum creates rampage**: Following the DarkSide group’s dissolution after the Colonial Pipeline attack,[^1] the Groove ransomware collective emerged in September 2021 and created the RAMP forum, which connects orphaned affiliates with ransomware-as-a-service (RaaS) operators.
*   **Affiliate disputes are on the rise**: There’s a growing number of disputes between ransomware affiliates and ransomware group operators.
*   **Media reporting increases impact**: Active media reporting reflects a “scoop-and-scandal”-driven culture in the cybersecurity community and unintentionally increases cyber threat actors’ influence.
*   **Attack playbook isn’t the whole story**: The Conti Playbook suggests Conti affiliates tend to use options like well-established cybercrime botnets, malicious spam and spear phishing.
*   **Cloud plays into ransomware’s hands**: Cloud environments were and continue to be attractive targets. This comparison of the rate of code change highlights significant threat actor investment in cloud-focused tools—particularly in modifying pre-existing tools.[^2]
*   **Underground forum members are trading in endpoint accesses**: Underground forums are showing increased interest in accessing compromised virtual private networks (VPNs) via stolen credentials and the use of public and zero-day exploits.[^5]
*   **Data extortion is rising without ransomware deployment**: In the second half of 2021, Accenture observed new threat groups establishing infrastructure and ramping up attacks solely focused on data exfiltration and extortion.
*   **Actors infer insidious insiders**: Along with an unsubstantiated claim of insider access at Accenture, actors using LockBit implied in November 2021 they have an insider at another major corporation.[^6]

## Supply chains offer attack foothold

Since the revelation of the SolarWinds supply chain campaign in December 2020,[^7] increasingly, malicious operators have realized the potential of supply chain attacks. In addition to the complexities of asset and vendor management and visibility into software bill of materials, moving to the cloud has meant many organizations further increased the risk and consequences of supply chain insecurities.

### What’s happening?

*   **Widely reported threat increases**: During October and November 2021, numerous cybersecurity publications mentioned supply chain attack campaigns referencing developer library and software platform compromises.
*   **Backdoor threats are more prevalent**: Accenture noted references to at least nine malicious node package managers (NPMs) masquerading as legitimate packages. There were also two legitimate NPM packages with backdoors built into them.[^8]

## Infostealers boost the malware market

The increased popularity of underground endpoint marketplaces that sell packages of compromised login data continues to pose a substantial threat to organizations across industries and geographies.

Compromised endpoints—which underground actors have bundled and sold as so-called “bots”—contain login credentials, sensitive system information and cookie sessions. Actors siphon this information from victims’ machines using credential-stealing malware and sell it on Dark Web marketplaces for as little as US$10 to US$200.

![Figure 3. Malware by category (Incident response)]

## Cloud-centricity prompts new attack vectors

Increasingly, threat actors are exploiting public-facing cloud infrastructure to deploy offensive toolsets and use internal access points to organizations’ cloud environments.

### What’s happening?

*   **Rapid cloud growth feeds attack opportunities**: Forecasts of global end-user spending on public cloud services show it reaching US$482B in 2022—a 21.7% increase from 2021’s expected US$396B.[^18]
*   **Cloud-centric toolset threats are escalating**: Accenture has observed a highly evolved and active cloud-centric toolset from TeamTNT. On October 29, 2021, security researchers leaked TeamTNT’s toolset for attacking public-facing cloud platforms.[^19]

## Vulnerability exploits see high volume buying and selling

Accenture has observed a huge growth in the underground market for vulnerability exploits, especially for those that enable adversaries to gain unauthorized access to a corporate network.

### Actors begin to capitalize on Log4j vulnerability

On December 9, 2021, Log4j maintainers reported details surrounding a remote code execution vulnerability,[^22] identified as both CVE-2021-44228 and Log4Shell. CISA estimates there are 100 million affected software and technology instances across a wide range of technology products and vendors.

![Figure 7. Log4j Exploitation Trends and Volume, December 2021]

---

## References

[^1]: Accenture Cyber Threat Intelligence, “Colonial Pipeline Ransomware,” May 9 2021. IntelGraph reporting.
[^2]: Accenture Cyber Threat Intelligence, “Ransomware Trends Q3 2021,” November 11, 2021. IntelGraph Reporting; 2021 IBM Security X-Force Cloud Threat Landscape Report.
[^3]: Accenture Cyber Investigations and Forensic Response research.
[^4]: vx-underground Twitter post, October 28, 2021.
[^5]: Accenture Cyber Threat Intelligence, “A View from the Dark Web: Are Ransomware Gangs Shifting Their Focus towards Europe?” November 15, 2021. IntelGraph reporting.
[^6]: @darktracer Twitter account, November 17, 2021.
[^7]: “Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims with SUNBURST Backdoor.” Mandiant. December 13, 2020.
[^8]: “Two NPM Packages With 22 Million Weekly Downloads Found Backdoored,” The Hacker News. November 7, 2021.
[^9]: Ibid.
[^10]: “APT trends report Q3 2021,” Kaspersky, October 26, 2021.
[^11]: “TeleBots are back: Supply-chain attacks against Ukraine,” ESET. June 30, 2017.
[^12]: Accenture “Application Security”.
[^13]: “SUNSPOT: An Implant in the Build Process,” CrowdStrike, January 11, 2021.
[^14]: “Japanese government official says Olympic ticket data leaked,” ZDNet, July 21, 2021.
[^15]: Accenture Cyber Threat Intelligence, “Technical Analysis of REDLINE Stealer,” April 19, 2021. IntelGraph Reporting.
[^16]: “Hackers leak full EA data after failed extortion attempt,” The Record, July 31, 2021.
[^17]: Aggarwal, Gaurav, “How the pandemic has accelerated cloud adoption,” Forbes, January 15, 2021.
[^18]: Gartner® Press Release, Gartner says Four Trends are Shaping the Future of Public Cloud, August 2, 2021.
[^19]: vx-underground Twitter post, October 28, 2021.
[^20]: Accenture Cyber Threat Intelligence, “TeamTNT Operations Show the Cloud Is the New Battleground”, January 14, 2022, Intelgraph reporting.
[^21]: “TeamTNT with new campaign aka ‘Chimaera’,” AT&T. September 8, 2021.
[^22]: Accenture Cyber Threat Intelligence, “Log4j Unauthenticated RCE CVE-2021-44228 Vulnerability,” January 4, 2022, Intelgraph reporting.
[^23]: Accenture Cyber Threat Intelligence, “Account “leopoldo787” Advertises List of 500,000 IP Addresses Potentially Vulnerable to Log4j Exploitation,” January 2, 2022, IntelGraph reporting.
[^24]: Accenture Cyber Threat Intelligence, “Log4j Unauthenticated RCE CVE-2021-44228 Vulnerability,” January 4, 2022, Intelgraph reporting.

## Contacts

- **Joshua Ray**, Managing Director, Accenture Security, joshua.a.ray@accenture.com
- **Howard Marshall**, Managing Director, Accenture Security, howard.marshall@accenture.com
- **Robert Boyce**, Managing Director, Accenture Security, Global Cyber Investigations, Forensics & Response (CIFR) Lead, r.boyce@accenture.com
- **Christopher Foster**, Senior Principal – Security Innovation, Accenture Cyber Threat Intelligence Product Strategy Lead, c.foster@accenture.com
- **Valentino De Sousa**, Senior Principal – Security Innovation, Europe and Latin America Cyber Threat Intelligence Lead, valentino.de.sousa@accenture.com

## About Accenture

Accenture is a global professional services company with leading capabilities in digital, cloud and security. Combining unmatched experience and specialized skills across more than 40 industries, we offer Strategy and Consulting, Interactive, Technology and Operations services—all powered by the world’s largest network of Advanced Technology and Intelligent Operations centers.

### About Accenture Security
Accenture Security is a leading provider of end-to-end cybersecurity services, including advanced cyber defense, applied cybersecurity solutions and managed security operations.