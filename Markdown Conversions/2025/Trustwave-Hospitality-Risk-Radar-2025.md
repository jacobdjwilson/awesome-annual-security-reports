# 2025 Trustwave Risk Radar Report: Hospitality Sector

## Table of Contents
- [Persistent Threat Landscape in the Hospitality Sector](#persistent-threat-landscape-in-the-hospitality-sector)
- [Hospitality’s Unique Threat Landscape](#hospitalitys-unique-threat-landscape)
- [Notable and Prominent Trends in Hospitality](#notable-and-prominent-trends-in-hospitality)
- [Fraudsters Study and Share Booking Platform Secrets](#fraudsters-study-and-share-booking-platform-secrets)
- [Dark Web Travel Agents](#dark-web-travel-agents)
- [Publicly Exposed Services](#publicly-exposed-services)
- [Threat Actor Techniques by Attack Stage](#threat-actor-techniques-by-attack-stage)
- [Publicly Exposed Services in Hospitality](#publicly-exposed-services-in-hospitality)
- [Conclusion & Key Takeaways](#conclusion--key-takeaways)

---

The hospitality industry plays a critical role in the global economy, encompassing a wide range of services including lodging, food and beverage, travel, tourism, and event planning. With millions of travelers and guests interacting with hospitality services daily, the sector handles vast amounts of sensitive personal and financial information.

The Trustwave SpiderLabs team has conducted in-depth analysis of emerging cyber threat tactics, identifying the key trends reshaping the hospitality industry’s risk profile. Building upon our previously published work, the 2023 Hospitality Sector Threat Landscape, our researchers have structured their new findings into a comprehensive breakdown of attack stages, providing hospitality organizations with actionable intelligence they can use to strengthen their defensive posture.

This includes payment card details, passport and ID numbers, travel itineraries, and even health-related data. To meet guest expectations for convenience and connectivity, hospitality businesses increasingly rely on digital technologies, cloud-based services, IoT devices, and mobile platforms.

### Key Report Findings for the Hospitality Sector
*   2x the volume of public-facing SNMP services compared to the next most frequently exposed service.
*   ~15K critical vulnerabilities exposed to public Internet.
*   61.5% of initial access attempted to exploit publicly exposed services.

---

## Persistent Threat Landscape in the Hospitality Sector

Hospitality vendors face security threats from every angle. Here are just a few of the major headlines over the past two years:

- How ‘Juice Jackers’ Plant Malware On Your Phone At Airports And Hotels - *Forbes*, April 20, 2023
- Caesars Entertainment Discloses Cyber Attack, Ransom Payment Made Weeks Before MGM Heist - *CPO Magazine*, Sept. 19, 2023
- Unsaflok Flaw Can Let Hackers Unlock Millions of Hotel Doors - *Bleeping Computer*, March 21, 2024
- Vulnerability Exposed Ibis Budget Guest Room Codes to Hackers - *Hack Read*, April 2, 2024
- Omni Hotels Says Personal Information Stolen in Ransomware Attack - *Security Week*, April 16, 2024
- Exclusive: Watergategate? Ransomware gang targets famous Watergate Hotel - *Cyber Daily*, May 1, 2024
- US Hotel Check-In Systems Infiltrated by Spyware App - *SC Media*, May 23, 2024
- Hotel Check-in Kiosks Expose Guest Data, Room Keys - *Dark Reading*, June 8, 2024
- Disney Data Breach: Disneyland, Disney Cruise Guests’ and Employee’s Personal Info Leaked - *Mashable*, Sept. 8, 2024
- Radisson’s Country Inn & Suites Purportedly Breached by Everest Ransomware - *SC Media*, Oct. 22, 2024
- Gambling Sector Subjected to APT41 Intrusions - *SC Media*, Oct. 22, 2024
- Gambling and Lottery Giant Disrupted by Cyberattack, Working to Bring Systems Back Online - *The Record*, Nov. 22, 2024
- Cyberattack Shuts Down Upper Peninsula’s Kewadin Casinos, Tribal Operations - *Detroit Free Press*, Feb. 12, 2025
- Microsoft Warns of ClickFix Phishing Campaign Targeting Hospitality Sector via Fake Booking[.]com Emails - *The Hacker News*, March 13, 2025

---

## Hospitality’s Unique Threat Landscape

The hospitality industry faces unique challenges that many other industries don’t face.

### Seasonal and Less Sophisticated Workforce
The hospitality sector employs a diverse workforce, with seasonal and less sophisticated staff often engaged during peak periods to meet demand. This turnover presents a distinct risk of insider threat, intentional or not, due to the challenge of providing consistent security training to a continually changing group of employees.

### Constant User/Guest Turnover
Hospitality establishments encounter a fresh set of users virtually every day. This ongoing cycle demands consistent uptime, addresses bandwidth constraints, and strives to minimize potential exposure to security threats.

### Dirty Networks
Given the substantial volume of network users, whether they’re hotel guests or individuals connecting to coffee shop Wi-Fi, organizations within the hospitality sector must operate under the assumption that their networks are highly susceptible to attacks due to the sheer number of untrusted users.

### Physical Security Concerns
Unlike conventional office buildings where employee access is typically controlled through access cards, hospitality establishments face cybersecurity risks due to the accessibility of hardware by guests. For instance, the server closet in a hotel could be left unlocked and easily accessible, or a thumb drive could easily be inserted into a nearby device.

### Franchise Model
The franchise framework leads to disparities in policy consistency and implementation across the industry, including cybersecurity measures. Different franchisers and franchisees adopt varied business models, resulting in divergent cybersecurity practices.

---

## Notable and Prominent Trends in Hospitality

### Fraudsters Study and Share Booking Platform Secrets
In underground forums, Telegram groups, and private marketplaces, cybercriminals are actively collaborating, sharing guides, and trading access on how to exploit major booking platforms. Hackers also often share detailed tutorials on how to insert stolen credit card data into active bookings, bypass verification checks, and avoid detection.

![Figure 1: An educational article about hotel booking types on a dark web forum]

**Mitigations to Reduce Risk**: Without aggressive fraud detection, closer vetting of partners, and cross-platform intelligence sharing, the hospitality industry remains vulnerable to a coordinated wave of booking abuse.

### Dark Web Travel Agents
Some malicious operators have been reportedly active on the dark web since 2018, offering heavily discounted “all-in-one” travel packages, claiming savings of 50 to 70% on hotel bookings, international flights, car rentals, and even guided excursions.

![Figure 2: The landing page of a dark web-advertised travel agency]

**Mitigations to Reduce Risk**: Fraud detection, supply chain vetting, and threat intelligence sharing are the recipes to prevent financial and reputation loss through this fraud.

---

## Publicly Exposed Services

Research and analysis of publicly exposed services in the hospitality sector reveals a massive attack surface. In April 2025, a total of 95,040 vulnerabilities were discovered with 3,884 unique CVEs. There were 14,318 critical vulnerabilities and 1,521 vulnerabilities in the CISA list. SNMP was exposed twice as much as the next highest publicly exposed service.

**Mitigations to Reduce Risk**:
- **Enhance Cybersecurity Hygiene and Patch Management**: Ensure all systems are regularly updated. Use the CISA Known Exploited Vulnerabilities (KEV) catalog.
- **Employ Network and Host-Based Auditing**: Provide early warning of compromise.
- **Incident Response Planning**: Test plans through tabletop exercises.

---

## Threat Actor Techniques by Attack Stage

### Credential Access
Techniques observed relied mostly on brute-force attempts and generic brute-force attacks. Activities related to the modifications of the authentication process involved disabling multi-factor authentication (MFA).

### Execution Techniques
Primarily involved the user execution of malicious files and links, followed by malicious uses of PowerShell scripts and commands.

### Initial Access
Vectors used in the attacks were mainly exploit attempts against publicly accessible services, followed by phishing and the use of compromised accounts.

### Privilege Escalation
Techniques utilized by attackers relied on the manipulation of valid cloud-based accounts to escalate to a higher privileged role.

### Discovery
Techniques utilized by attackers relied mostly on account and network service discovery.

### Command and Control
Mostly based on communication to web services over HTTP(S) protocol as well as with the use of proxy (i.e., communication over TOR network).

### Defense Evasion
Generally utilized access token manipulation and process names masquerading. Attackers attempted to impair defenses by disabling local security software such as firewalls.

### Persistence
Techniques utilized by attackers relied mostly on Account Creation, but also other techniques such as event-triggered execution, execution upon system start, as well as abuse of legitimate server software components.

### Lateral Movement
Techniques utilized by attackers relied mostly on remote services, specifically Server Message Block (SMB) and the use of alternate authentication material via pass-the-ticket attacks.

---

## Publicly Exposed Services in Hospitality

As of April 2025, 95,040 vulnerabilities were discovered with 3,884 unique CVEs for the hospitality sector.

### Top 10 Exposed Ports
1. **Port 161 (SNMP)**: Used to monitor and manage hotel systems like HVAC, lighting, IP cameras, and building management systems.
2. **Port 123 (NTP)**: Used to synchronize clocks on systems like keycard readers.
3. **Ports 443 / 8443 (HTTPS / Alt HTTPS)**: Secure communication for booking portals and guest Wi-Fi.
4. **Port 80 (HTTP)**: Unencrypted access to legacy sites.
5. **Port 22 (SSH)**: Secure remote login for hotel IT teams.
6. **Port 2628 (DICT Protocol)**: Legacy dictionary services.
7. **Port 179 (BGP)**: Internet routing.
8. **Port 2000 (Cisco SCCP)**: Cisco-based VoIP systems.
9. **Port 53 (DNS)**: Resolves hostnames to IP addresses.

---

## Conclusion & Key Takeaways

The hospitality industry finds itself at the crossroads of convenience and cyber risk. As digital transformation accelerates, so does the attack surface.

### Key Takeaways for the Hospitality Sector
- **Inventory, Assess, and Patch**: Create a regular ongoing inventory of your networks and prioritize patching.
- **Strengthen Identity and Access Controls**: Enforce MFA across all systems and implement least privileged policies.
- **Monitor and Control Remote Access Tools**: Inventory and control the use of RMM software.
- **Secure Third-Party and Supply Chain Relationships**: Conduct risk assessments on vendors and include cybersecurity obligations in contracts.
- **Backups and Business Continuity**: Maintain encrypted, offline, and immutable backups.
- **Raise Internal Awareness and Training**: Conduct cybersecurity training for all employees and run phishing simulations.
- **Monitor the Threat Landscape**: Subscribe to industry-specific threat intelligence feeds and implement dark web monitoring.