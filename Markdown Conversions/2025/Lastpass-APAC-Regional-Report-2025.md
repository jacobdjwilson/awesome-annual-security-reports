# APAC-Regional-Report 2025

**Organization:** Lastpass  
**Report Title:** APAC-Regional-Report  
**Year:** 2025  
**Authors:** Michael Kosak (Senior Principal Intelligence Analyst), Stephanie Schneider (Cyber Threat Intelligence Analyst)

## Table of Contents
- [Regional snapshot](#regional-snapshot)
- [Threat landscape: Frequency and Magnitude](#threat-landscape-frequency-and-magnitude)
- [Top malware families targeting APAC](#top-malware-families-targeting-apac)
- [Top threat actors targeting APAC](#top-threat-actors-targeting-apac)
- [Key regional incidents](#key-regional-incidents)
- [Deep dive of the month: Australia’s pension funds](#deep-dive-of-the-month-australias-pension-funds-hit-by-wave-of-credential-stuffing-attacks)
- [Trends on tap](#trends-on-tap)
- [What can you do?](#what-can-you-do)
- [Appendix – Sources & additional reading](#appendix--sources--additional-reading)

---

## Regional snapshot
The Asia-Pacific region (APAC) experienced high-frequency cyber espionage and financially motivated attacks involving phishing, data theft, ransomware, and network access sales. Campaigns involved credential harvesting, malware distribution via fake installers, cryptomining, and exploiting vulnerabilities in Palo Alto and FortiManager products. Additionally, AI-driven attacks and deepfake scams are emerging as new threats.

![Table showing statistics for Most Targeted (34%), Manufacturing (56%), Japan (66%), Credentials (55%), and Australia (46%)]

*   **APAC experienced the largest number of incidents globally in 2024 (34%)**, representing a 13% increase in attacks.
*   **Manufacturing** was the most targeted industry regionally, followed by finance & insurance (16%) and transportation (11%).
*   **Japan** was the most targeted country regionally last year. The Philippines, Indonesia, South Korea, and Thailand each represented 5% of cases.
*   **Stolen credentials** were reported by 55% of breach victims in APAC, indicating their frequent use in initial intrusions. Nearly one in four incidents in 2024 involved stolen data or credentials.
*   **Australia** remained a popular ransomware target. The country remained in the top 10 of countries impacted based on ransomware gang reporting of alleged victims.

---

## Threat landscape: Frequency and Magnitude
**Drivers of regional cyber threat activity:**
*   **Cybercrime:** Investment in emerging cybercrime hubs.
*   **IP theft:** Rise of operational technology.
*   **Reconnaissance:** Economic factors and Great Power competition.
*   **DPRK:** Stealing crypto, targeting job seekers.
*   **Regional disputes:** Semiconductors, China driving geopolitical/cyber activities.
*   **More aggressive:** Rising potential for conflict, ransomware attacks threaten private/public sectors.

**APAC Region Cyber Threat Score:** 6.4 (Google Threat Intelligence)

**Observed events:**
*   Targeting countries in or around the South China Sea by Chinese-backed hackers (Microsoft Threat Intelligence).
*   Top sources of cyber activity targeting Australia originates from Brazil, China, Mexico, North Korea, Russia, and Vietnam (Google Threat Intelligence).

---

## Top malware families targeting APAC

### RANSOMWARE
Akira generally trended as the top ransomware throughout Q1 2025 with a significant spike in posted victims (241) at the end of May. Asia accounted for approximately 11% of global ransomware activity, mainly targeting manufacturing and engineering, with India and Japan seeing significant activity. Oceania accounted for 2% of activity.[^5] Australia emerged as a top regional target, and there were several victims in Taiwan, Singapore, and Japan. Thailand also saw an unusual increase in victims.[^4]

### STEALERS
LUMMAC (aka Lumma) stealer was one of the top malware families targeting APAC in Q1 2025; however, its infrastructure was taken down in May 2025.[^6] LastPass TIME analysts predict a correlated decrease in Lumma stealer infections over the next quarter.[^7] Long-standing groups such as Vidar and Stealc will be well positioned to increase their market share, as well as other newer families like Acreed. HOPLITE has been attributed to the North Korean government and was recently used by suspected India-backed hackers.

Observed malware targeting APAC included CABBEACON (reconnaissance), LUMMAC and HOPLITE (credential stealers), NUMOZYLOD and LIGHTPIPE (downloaders), and various backdoors.

> Want to learn about the infostealer threat? The Australian Cyber Security Center (ACSC) published a report breaking down how cybercriminals use stealer malware to compromise corporate networks.[^8]

---

## Top threat actors targeting APAC

| Actor | AKA | Profile |
| :--- | :--- | :--- |
| **TEMP.Hex** | Mustang Panda, Red Delta, Winnti Group, Earthpreta | Prolific Chinese actor targeting public/private entities aligned with Beijing’s strategic interests. Uses spear-phishing emails. |
| **Salt Typhoon** | GhostEmperor, FamousSparrow | High sophistication; targets government and telecom companies in SE Asia. Compromised Cisco network devices across five telecom networks. |
| **Bitter** | UNC2464 | India-backed espionage group targeting South Asian governments, diplomatic entities, and defense organizations. |
| **APT36** | Transparent Tribe, Mythic Leopard | Pakistani espionage group focused on political/military intelligence. Uses compromised credentials for initial access. |
| **Akira** | N/A | Ransomware variant that steals information and conducts double extortion. Most common ransomware targeting APAC in Q1 2025. |

---

## Key regional incidents

*   **Japan orgs targeted by CoGUI phishing kit:** A campaign used the CoGUI phishing kit to steal usernames, passwords, and payment information from Japanese organizations, spoofing Amazon, banks, and the national tax agency.[^11]
*   **Fog ransomware attack:** A cyberattack on an Asia-based financial institution in May 2025 used legitimate employee monitoring software (Syteca) and open-source pen-testing tools.[^9]
*   **Chinese hackers breached entities in Southeast Asia:** Chinese-backed Billbug (aka Lotus Panda) breached government and business orgs between August 2024 and February 2025 using custom credential stealers.[^10]
*   **Fake Update campaigns:** Researchers reported a rise in Fake Update campaigns, where attackers trick victims into installing supposed browser updates (Chrome/Opera) that deliver malware.[^12]
*   **Australian, New Zealand cyber landscape changing:** CyberCX’s 2025 Threat Report revealed that business email compromise (BEC) remained the top incident type, with 75% of incidents involving session hijacking to bypass MFA.[^13]

---

## Deep dive of the month: Australia’s pension funds hit by wave of credential-stuffing attacks

**Summary:** A credential stuffing campaign during March 29-30, 2025, targeted multiple large Australian superannuation funds, compromising over 20,000 member accounts.[^14]

**How did it happen?**
The attack utilized a coordinated OAuth token manipulation campaign coupled with advanced credential-stuffing techniques targeting API vulnerabilities in member portals. The vector appears to have utilized SQL injection techniques targeting database vulnerabilities in fund administration systems.

**How can you protect yourself?**
Use tools like *Have I Been Pwned* to check for compromised credentials. Use unique credentials for all accounts and implement MFA. Analysts recommend reading the Australian Signals Directorate’s ACSC Annual Cyber Threat Report.[^15]

---

## Trends on tap

*   **Critical infrastructure under attack:** Growing concern about Chinese hacking into global CI, including ISPs and MSPs.
*   **Credentials are key:** Chinese hackers frequently seek credentials to maintain long-term access, move laterally, and spread malware.
*   **Threats are growing:** While China has attacked CI in the past, they have recently become more aggressive, focusing on intelligence gathering and prepositioning for potential conflict.

---

## What can you do?
Following the Australian Signals Directorate’s Essential Eight maturity model:[^18]
1.  **Patch Applications:** Prevent exploitation of known vulnerabilities.
2.  **Patch Operating Systems:** Keep systems updated.
3.  **Use a Password Manager:** Store strong, unique passwords to counter infostealers.
4.  **Enable Multi-Factor Authentication:** Add a layer of security against password exposure.
5.  **Limit Privileges for Users:** Restrict access to only what is necessary to limit potential damage.

---

## Appendix – Sources & additional reading
[^1]: IBM X-Force 2025 Threat Intelligence Index
[^2]: Verizon’s 2025 Data Breach Investigation Report
[^3]: One in Four Cyberattacks in 2024 Traced to Infostealers, Huntress Reports (Hudson Rock)
[^4]: 2025 Ransomware: Business as Usual, Business is Booming (Rapid7)
[^5]: The State of Ransomware in the First Quarter of 2025: Record-Breaking 126% Spike in Public Extortion Cases (Check Point Research)
[^6]: Lumma Stealer Takedown Reveals Sprawling Operation (DarkReading)
[^7]: Dark Side of the Lumma: What the Lumma stealer takedown means for the infostealer market and your personal data (LastPass Blog)
[^8]: The silent heist: cybercriminals use information stealer malware to compromise corporate networks (Australian Signals Directorate)
[^9]: Fog Ransomware: Unusual Toolset Used in Recent Attack (Symantec)
[^10]: Billbug: Intrusion Campaign Against Southeast Asia Continues (Symantec)
[^11]: CoGUI Phish Kit Targets Japan with Millions of Messages (Proofpoint)
[^12]: Gen Q1/2025 Threat Report (Gen Digital)
[^13]: CyberCX 2025 Threat Report reveals cyber landscape is changing (CyberCX)
[^14]: Cybercriminals are trying to loot Australian pension accounts in new campaign (The Record Media)
[^15]: Annual Cyber Threat Report 2023-2024 (Australian Signals Directorate)
[^16]: ACSC 2024 Report Implications (LastPass Blog)
[^17]: Silk Typhoon is targeting remote management tools and cloud services in supply chain attacks (Microsoft Security)
[^18]: Australian Signals Directorate Essential Eight