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

This includes payment card details, passport and ID numbers, travel itineraries, and even health-related data. To meet guest expectations for convenience and connectivity, hospitality businesses increasingly rely on digital technologies, cloud-based services, IoT devices, and mobile platforms.

The Trustwave SpiderLabs team has conducted in-depth analysis of emerging cyber threat tactics, identifying the key trends reshaping the hospitality industry’s risk profile. Building upon our previously published work, the 2023 Hospitality Sector Threat Landscape, our researchers have structured their new findings into a comprehensive breakdown of attack stages, providing hospitality organizations with actionable intelligence they can use to strengthen their defensive posture.

In addition, Trustwave SpiderLabs has produced two detailed supplemental reports:
- Hospitality Sector Deep Dive: A DFIR Case Study
- Hospitality Sector Deep Dive: How Threat Actors Turn Vulnerabilities into Big Business

While these innovations enhance the guest experience, they also expand the industry’s attack surface, making it an attractive target for cybercriminals.

Cybersecurity in the hospitality sector has emerged as a pressing concern in recent years. Hotels, resorts, and travel service providers are often underprepared for the sophistication and persistence of modern cyber threats. The decentralized nature of operations, frequent staff turnover, and reliance on third-party vendors further compound the risk. Threat actors exploit these weaknesses through a variety of tactics, including ransomware attacks, social engineering schemes, data breaches, and attacks on IoT infrastructure.

The consequences of successful cyberattacks in hospitality are significant, ranging from operational disruptions and financial losses to reputational damage and regulatory penalties.

### Key Report Findings for the Hospitality Sector
- **2x** the volume of public-facing SNMP services compared to the next most frequently exposed service
- **~15K** critical vulnerabilities exposed to public Internet
- **61.5%** of initial access attempted to exploit publicly exposed services

## Persistent Threat Landscape in the Hospitality Sector

Hospitality vendors face security threats from every angle. Here are just a few of the major headlines over the past two years:

- How ‘Juice Jackers’ Plant Malware On Your Phone At Airports And Hotels - Forbes, April 20, 2023
- Caesars Entertainment Discloses Cyber Attack, Ransom Payment Made Weeks Before MGM Heist - CPO Magazine, Sept. 19, 2023
- Unsaflok Flaw Can Let Hackers Unlock Millions of Hotel Doors - Bleeping Computer, March 21, 2024
- Vulnerability Exposed Ibis Budget Guest Room Codes to Hackers - Hack Read, April 2, 2024
- Omni Hotels Says Personal Information Stolen in Ransomware Attack - Security Week, April 16, 2024
- Exclusive: Watergategate? Ransomware gang targets famous Watergate Hotel - Cyber Daily, May 1, 2024
- US Hotel Check-In Systems Infiltrated by Spyware App - SC Media, May 23, 2024
- Hotel Check-in Kiosks Expose Guest Data, Room Keys - Dark Reading, June 8, 2024
- Disney Data Breach: Disneyland, Disney Cruise Guests’ and Employee’s Personal Info Leaked - Mashable, Sept. 8, 2024
- Radisson’s Country Inn & Suites Purportedly Breached by Everest Ransomware - SC Media, Oct. 22, 2024
- Gambling Sector Subjected to APT41 Intrusions - SC Media, Oct. 22, 2024
- Gambling and Lottery Giant Disrupted by Cyberattack, Working to Bring Systems Back Online - The Record, Nov. 22, 2024
- Cyberattack Shuts Down Upper Peninsula’s Kewadin Casinos, Tribal Operations - Detroit Free Press, Feb. 12, 2025
- Microsoft Warns of ClickFix Phishing Campaign Targeting Hospitality Sector via Fake Booking[.]com Emails - The Hacker News, March 13, 2025

## Hospitality’s Unique Threat Landscape

The hospitality industry faces unique challenges that many other industries don’t face. This list should serve to alert you to specific areas where you may want to focus on when you begin closing your risk gap.

### Seasonal and Less Sophisticated Workforce
The hospitality sector employs a diverse workforce, with seasonal and less sophisticated staff often engaged during peak periods to meet demand. This turnover presents a distinct risk of insider threat, intentional or not, due to the challenge of providing consistent security training to a continually changing group of employees.

### Constant User/Guest Turnover
Hospitality establishments encounter a fresh set of users virtually every day. This ongoing cycle demands consistent uptime, addresses bandwidth constraints, and strives to minimize potential exposure to security threats.

### Dirty Networks
Given the substantial volume of network users, whether they’re hotel guests or individuals connecting to coffee shop Wi-Fi, organizations within the hospitality sector must operate under the assumption that their networks are highly susceptible to attacks due to the sheer number of untrusted users.

### Physical Security Concerns
Unlike conventional office buildings where employee access is typically controlled through access cards, hospitality establishments face cybersecurity risks due to the accessibility of hardware by guests. For instance, the server closet in a hotel could be left unlocked and easily accessible, or a thumb drive could easily be inserted into a nearby device.

### Franchise Model
The franchise framework leads to disparities in policy consistency and implementation across the industry, including cybersecurity measures. Different franchisers and franchisees adopt varied business models, resulting in divergent cybersecurity practices. Providing guidance or security requirements can be a sensitive issue between the franchisers and franchisees.

With more than 250 cybersecurity experts across the globe, the Trustwave SpiderLabs team puts its resources to task researching the top threats in today’s landscape. We are uniquely positioned to do so, as we perform over 200,000 hours of penetration tests and discover over 30,000 vulnerabilities annually, including 9,000 high/critical severity infrastructure and web app sources. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 2M+ per month that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Advanced Continuous Threat Hunting, Digital Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur, as well as mitigations and controls that your organization can put in place to prevent these compromises.

This report examines the myriads of threats facing the hospitality industry. In addition to supplemental reports focused on the rapid rise of ransomware and common security gaps, Trustwave SpiderLabs will offer recommendations to help hospitality organizations mitigate risks and keep their operations undisrupted.

## Notable and Prominent Trends in Hospitality

From Trustwave’s global perspective we’ve picked a few trends that could be going under the radar for your security team.

## Fraudsters Study and Share Booking Platform Secrets

### The Threat
In underground forums, Telegram groups, and private marketplaces, cybercriminals are actively collaborating, sharing guides, and trading access on how to exploit major booking platforms.

Hackers also often share detailed tutorials on how to insert stolen credit card data into active bookings, bypass verification checks, and avoid detection.

![Figure 1. An educational article about hotel booking types on a dark web forum]

### Mitigations to Reduce Risk
Without aggressive fraud detection, closer vetting of partners, and cross-platform intelligence sharing, the hospitality industry remains vulnerable to a coordinated wave of booking abuse.

Monitoring the dark web and underground forums for “chatter” about your brand can help mitigate this issue and alert the hospitality organization of potential issues with their booking portal.

## Dark Web Travel Agents

### The Threat
Some malicious operators have been reportedly active on the dark web since 2018, offering heavily discounted “all-in-one” travel packages, claiming savings of 50 to 70% on hotel bookings, international flights, car rentals, and even guided excursions.

These underground “travel agencies” promise their customers everything from luxury hotel stays and business-class flights to full holiday itineraries at a fraction of the market price. While the pricing may sound too good to be true, the market for such services has grown steadily, with clients ranging from cybercriminals to individuals simply looking for a cheap getaway, knowingly or unknowingly participating in fraudulent activity.

![Figure 2. The landing page of a dark web-advertised travel agency]

### Mitigations to Reduce Risk
Although these groups do not openly disclose how they operate, their modus operandi likely involves using stolen credit card data, compromised loyalty accounts, or hijacked admin access to travel and booking platforms.

Just like when fraudsters share tips on exploiting a booking system, fraud detection, supply chain vetting, and threat intelligence sharing are the recipes to prevent financial and reputation loss through this fraud.

Monitoring the dark web and underground forums for “chatter” about your brand can help mitigate this issue and alert the hospitality organization of fraudulent sales.

## Publicly Exposed Services

### The Threat
Research and analysis of publicly exposed services in the hospitality sector reveals a massive attack surface.

In April 2025, a total of 95,040 vulnerabilities were discovered with 3,884 unique CVEs for these hospitality companies. There were 14,318 critical vulnerabilities and 1,521 vulnerabilities in the CISA list. SNMP was exposed twice as much as the next highest publicly exposed service. SNMP can be a goldmine for hackers as vulnerabilities and misconfigurations are often plentiful in these environments.

Based on metrics from our own customer base, 61.5% of initial access attempts exploit publicly exposed services.

### Mitigations to Reduce Risk
- **Enhance Cybersecurity Hygiene and Patch Management**: Unpatched vulnerabilities are low-hanging fruit for threat actors. Don’t make it easy for these criminals. Hospitality organizations should ensure that all systems are regularly updated with the latest security patches. The CISA Known Exploited Vulnerabilities (KEV) catalog is a useful resource for identifying and prioritizing patches for critical systems.
- **Employ Network and Host-Based Auditing**: Auditing can provide an early warning of a compromise and an important trail for incident responders in the case of a compromise.
- **Incident Response Planning**: A comprehensive incident response plan is essential to minimizing the impact of any attack. This plan should include clear steps for containing and mitigating the attack, restoring systems, and communicating with stakeholders. Hospitality organizations should test their incident response plans through tabletop exercises and ensure that external cybersecurity experts are ready to assist if needed.

## Threat Actor Techniques by Attack Stage

Credential Access techniques observed in the attacks relied mostly on brute-force attempts and generic brute-force attacks. Activities related to the modifications of the authentication process involved disabling multi-factor authentication (MFA). OS credential dumping by using DCSync and NTLM hash theft were also observed.

All Credential Access techniques have fallen in volume, while Brute Force attempts have increased about 14% since our last Hospitality Threat Report. Since this category also includes Credential Stuffing and Dictionary Attacks, it makes sense that it would still be at the top. Massive credential dumps from compromised organizations seem to drop every day, providing threat actors with instant access, often due to password reuse.

### Credential Access Techniques
- Brute Force T1110: 95.4%
- Modify Authentication Process T1556: 3.6%
- OS Credential Dumping T1003: 0.9%
- Forced Authentication T1178: 0.1%

### Execution Techniques
Execution techniques observed in the security incidents primarily involved the user execution of malicious files and links, followed by malicious uses of PowerShell scripts and commands. Some of the commands were executed remotely via remote Windows Management Instrumentation (WMI) service.

- User Execution T1204: 58.7%
- Command and Scripting Interpreter T1059: 37%
- Windows Management Instrumentation T1047: 2.5%
- Scheduled Task/Job T1053: 1.8%

*(Example script omitted for brevity, showing Lumma infostealer execution)*

### Initial Access Techniques
Initial Access vectors used in the attacks were mainly exploit attempts against publicly accessible services, followed by phishing and the use of compromised accounts. Most phishing attempts were generic and leveraged social engineering with links to external websites.

- Exploit Public-Facing Application T1190: 61.5%
- Phishing T1566: 23.4%
- Valid Accounts T1078: 15.1%

The exploit techniques identified in the initial access attempts targeting web applications primarily included Log4j CVE-2021-44228, which represented 49% of the cases observed. Another widely targeted type of vulnerability was cross-site scripting, which accounted for 26% of records. Meanwhile, SQL injection and directory traversal made up 20.2% of the cases. Notably, some attackers also tried to leverage CVE-2020-1472 (Zerologon) and CVE-2021-26897 (a remote code execution vulnerability in Windows DNS server).

### Privilege Escalation Techniques
Privilege Escalation techniques utilized by attackers relied on the manipulation of valid cloud-based accounts to escalate to a higher privileged role.

- Account Manipulation T1098: 73.7%
- Valid Accounts T1078: 24.6%
- Abuse Elevation Control Mechanism T1548: 1.8%

### Discovery Techniques
Discovery techniques utilized by attackers relied mostly on account and network service discovery.

- Network Service Discovery T1046: 84%
- Account Discovery T1087: 8.6%
- Network Share Discovery T1135: 6.7%
- System Network Configuration Discovery T1016: 0.6%

### Command and Control Techniques
Command and Control techniques observed in the security incidents were mostly based on communication to web services over HTTP(S) protocol as well as with the use of proxy (i.e., communication over TOR network). Another Application Layer Protocols identified in the command-and-control traffic include DNS and SMB.

- Web Service: 36.5%
- Proxy T1090: 29.4%
- Application Layer Protocol T1071: 23%
- Ingress Tool Transfer T1105: 11.1%

### Defense Evasion Techniques
Defense Evasion techniques in the analyzed security incidents generally utilized access token manipulation and process names masquerading. Attackers attempted to impair defenses by disabling local security software such as firewalls. A common target of process injections was the Windows native explorer.exe process.

- Access Token Manipulation T1134: 43.7%
- Masquerading T1036: 33.8%
- Impair Defenses T1562: 14.1%
- Process Injection T1055: 8.5%

### Persistence Techniques
Persistence techniques utilized by attackers relied mostly on Account Creation, but also other techniques such as event-triggered execution, execution upon system start, as well as abuse of legitimate server software components.

- Create Account T1136: 89.3%
- Event Triggered Execution T1546: 5.4%
- Boot or Logon Autostart Execution T1547: 3.6%
- Server Software Component T1505: 1.8%

### Lateral Movement Techniques
Lateral Movement techniques utilized by attackers relied mostly on remote services, specifically Server Message Block (SMB) and the use of alternate authentication material via pass-the-ticket attacks.

- Remote Services T1021: 85.2%
- Use Alternate Authentication Material T1550: 13%

## Publicly Exposed Services in Hospitality

Services are often publicly exposed for a good reason. To allow the public to visit your website, and to receive email from people outside your organization. However, there are many times when services are made public that should not be.

Compared to our previous hospitality report, the metrics have not changed much. There were 62,565 publicly exposed hospitality systems in 2024 compared to our last report, which showed about 65,642 exposed systems, a small decrease of 4.6%. Other metrics were also similar, including the same top three open services and only minor differences in the number of vulnerabilities found.

As of April 2025, 95,040 vulnerabilities were discovered with 3,884 unique CVEs for the hospitality sector. Among these, 14,318 are critical vulnerabilities and 1,521 are vulnerabilities in the CISA KEV list.

### Top 10 Exposed Ports
1. **Port 161 (SNMP)**: 9,627
2. **Port 123 (NTP)**: 5,525
3. **Port 443 (HTTPS)**: Combined with 8443
4. **Port 80 (HTTP)**: 4,372
5. **Port 22 (SSH)**: 2,402
6. **Port 2628 (DICT Protocol)**: 2,178
7. **Port 179 (BGP)**: 1,967
8. **Port 2000 (Cisco SCCP)**: 1,914
9. **Port 53 (DNS)**: 1,130
10. **Port 8443 (Alt HTTPS)**: Combined with 443

### Key Applications in Hospitality with Notable Vulnerabilities
- **OpenSSH**: 1,107 (CVE-2024-6387)
- **Apache httpd**: 1,556 (CVE-2021-41773)
- **Microsoft IIS httpd**: 942 (CVE-2021-31166)
- **MikroTik Bandwidth-Test Server**: 1,275 (CVE-2018-14847)
- **MariaDB**: 1,245 (CVE-2023-22084)
- **nginx**: 1,762 (CVE-2021-23017)
- **ntpd**: 1,607 (CVE-2016-9310)
- **ciscoSystems**: 4,265 (CVE-2023-20198)
- **PPTP**: 930 (Protocol-wide weaknesses)

## Conclusion & Key Takeaways

The hospitality industry — known for its commitment to service, personalization, and customer experience — finds itself at the crossroads of convenience and cyber risk. As digital transformation accelerates, so does the attack surface.

### Key Takeaways for the Hospitality Sector
- **Inventory, Assess, and Patch**: Create a regular ongoing inventory of your networks. Prioritize vulnerability assessments and set up an expected patch cycle.
- **Strengthen Identity and Access Controls**: Enforce MFA across all systems, implement least privileged policies, and regularly audit user roles.
- **Monitor and Control Remote Access Tools**: Inventory and control RMM software, set up alerts for unauthorized remote access software, and use EDR solutions.
- **Secure Third-Party and Supply Chain Relationships**: Conduct risk assessments on vendors, include cybersecurity obligations in contracts, and monitor for dark web leaks involving suppliers.
- **Backups and Business Continuity**: Maintain encrypted, offline, and immutable backups. Test restoration procedures and rehearse business continuity plans.
- **Raise Internal Awareness and Training**: Conduct role-tailored cybersecurity training, run phishing simulations, and educate teams on the risks of leaked credentials and public Wi-Fi.
- **Monitor the Threat Landscape**: Subscribe to threat intelligence feeds, implement dark web monitoring, and participate in information-sharing communities.