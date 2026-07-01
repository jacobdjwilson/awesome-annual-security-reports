# Cyber-Threat-Monitor-Report 2024

## Table of Contents
- [Comprehending our Cyberspace](#comprehending-our-cyberspace)
- [Regional Infection Profile](#regional-infection-profile)
- [The Metro and Tier-1 Cities - Infection Rate](#the-metro-and-tier-1-cities---infection-rate)
- [Top Infection Rates in Tier-2 Cities](#top-infection-rates-in-tier-2-cities)
- [Infection Rate Comparison Across Platforms](#infection-rate-comparison-across-platforms)
- [Enterprise Insecurity](#enterprise-insecurity)
- [Vulnerabilities Galore](#vulnerabilities-galore)
- [Dangers in the Internet of Things](#dangers-in-the-internet-of-things)
- [Windows Under Siege](#windows-under-siege)
- [The Mobile Device Story](#the-mobile-device-story)
- [Mac Attack](#mac-attack)
- [Latest Security News](#latest-security-news)
- [Key Takeaways](#key-takeaways)

---

## Comprehending our Cyberspace

While Israel is grappling with attacks by Hamas on its soil, Islamic hacktivist groups have launched a digital war on its digital infrastructure intensifying the conflict further. A rise in politically and religiously motivated hacktivist groups targeting Israeli critical infrastructure with DDoS attacks was also seen. After Israeli organisations such as media, defence and other critical infrastructures fell victim, its age-old ally India came to its rescue by unleashing its group of hackers to defend their systems and other sensitive digital assets.

On the other hand, its holiday season in the US and the rest of the world. More cyber attacks are foreseen on countries supporting Israel and the subsequent retaliation. It is going to be a different ball game altogether for the threat actors and if played well, they are the ones who are going to benefit the most, be it money or just stopping operations.

A rise in ransomware operations; mainly due to the large attack surface and monetary benefit that it offers for the threat actors, and crypto malware; mining cryptocurrencies is very lucrative and cryptojacking is an inexpensive way to mine, are foreseen. Threat actors are also creating variants of existing malware with enhanced evasion techniques. Ransomware-as-a-service (RaaS) methodology will involve a lot of players in the field, both amateurs and professionals.

The world is reeling under chaotic times and we also foresee a rise in nation-state sponsored threat activity. Nations and organizations need to up their defences by following proper cyber hygiene practices and training their employees to stay safe from this ongoing digital warfare.

We at K7 Labs offer significant protection from emerging and latest threats at the earliest by closely examining and identifying such incidents and providing security at multiple layers.

---

## Regional Infection Profile

We use the "Infection Rate" (IR) factor to identify the netizens’ exposure to cyber threats. IR is determined as the proportion of K7 users in an area who encountered at least one cyber threat event and which was blocked and reported to our K7 Ecosystem Threat Intelligence infrastructure.

![Diagram showing the calculation of Infection Rate: K7 users at location XYZ / Blocked Threat Event = Infection Rate]

**The overall Pan-India IR in comparison with the previous quarter:**
- Q3_2023-24: 35%
- Q2_2023-24: 38%

---

## The Metro and Tier-1 Cities - Infection Rate

![Table showing infection rates across Ahmedabad, Bengaluru, Chennai, Delhi, Hyderabad, Kolkata, Mumbai, and Pune, broken down by Web Protection, Firewall Protection, Behaviour Protection, and ScanEngine Protection]

---

## Top Infection Rates in Tier-2 Cities

Threat actors have also started focusing more on Tier-2 cities due to a plethora of factors such as poor cyber hygiene, lack of awareness, etc.

![Bar chart showing infection rates in various Tier-2 cities including Bhubaneswar, Guwahati, Jaipur, Kakinada, Kurnool, Lucknow, Ludhiana, Mangalore, Mathura, Patna, Thrissur, Vijayawada, and Visakhapatnam]

---

## Infection Rate Comparison Across Platforms

Even though Windows is a closed-source system, its enormous user base presents a lucrative chance for cybercriminals.

![Chart comparing Windows IR vs Android IR across major Indian cities]

---

## Enterprise Insecurity

Cryptomining malware can jeopardize the availability and security of a network or system. Recently, one of our enterprise customers complained of frequent pop-up notifications about a malicious file detected while it was being copied from the local network. This file was deployed in one of the internet-facing SQL servers which was poorly protected and was spreading laterally across the network.

**The kill chain:**
1. After enumerating the network machines, it brute forces them.
2. To help, Mimikatz has been deployed.
3. The malware uses `taskkill` to kill a set number of processes. Windows Defender is then disabled.
4. It creates a new user with elevated privileges.
5. After user creation, the XMR Miner software is downloaded and executed.

### Safety Recommendations
- Deploying tools to monitor your organizations’ network
- Enforcing least privilege access
- Enforcing use of strong passwords and multi-factor authentication (MFA)
- Keeping your devices updated and patched against the latest vulnerabilities
- Protecting your devices by using a high-quality security software such as K7 Endpoint Security

---

## Vulnerabilities Galore

- **Skype’s Business Products (CVE-2023-41763)**: Information disclosure allowing privilege elevation.
- **Wordpad (CVE-2023-36563)**: Disclosure of NTLM hashes.
- **SmartScreen ByPass (CVE-2023-36025)**: Bypasses Windows Defender SmartScreen checks.
- **Google Chrome (CVE-2023-5217)**: Buffer overflow/heap corruption.
- **Microsoft Excel (CVE-2023-36041)**: RCE vulnerability allowing local attack and privilege gain.

---

## Dangers in the Internet of Things

- **Sophos Command Injection (CVE-2023-1671)**: Allows execution of arbitrary code in Sophos Web Appliance.
- **Bluetooth Module (CVE-2023-45866)**: Remote privilege escalation in Android, iOS, macOS, and Linux.
- **Apple Products (CVE-2023-42916, CVE-2023-42917)**: Out-of-bounds read and memory corruption in WebKit.

### Mitigation Techniques
- Encrypt your connections
- Ensure you set a unique and strong password for each of your devices
- Connect your devices to only a secure and trusted network
- Regularly check your device permissions and connections

---

## Windows Under Siege

![Chart showing the split of Windows Top 10 Detections including HACK.WIN32.ADDUSER, HACK.WIN32.MSIL.IDLEKMS.E, etc.]

### Windows Exploits
![Chart comparing Q2 and Q3 2023-24 exploits, highlighting the prevalence of BLOCK POWERSHELL REMOTING PORT]

### Heuristic Host Intrusion Prevention System (HIPS)
Heuristic behavioural detections are ideal for defending against new threats (0-days) and new variants of existing malware.

![Chart showing Windows Heuristic Behavioural Detections including Injectors, Droppers, and Registry modifications]

---

## The Mobile Device Story

The allure of readily accessible data makes Android users prime targets. Unlike Apple’s tightly controlled App Store, the Android landscape thrives on diverse, often unregulated third-party stores.

![Chart showing Adware vs Trojan Proportional Split]

### The Omnipresent Trojan
Trojans are versatile, ranging from remote access tools to zero-day exploits.
![Chart showing most prevalent Trojan types: Andr.TrjDrop, Andr.Trj.Agent, Andr.TrjSpy, etc.]

### The Adware Saga
Adware can affect your mobile device’s performance and security. Andr.Ad.JgPck topped the chart this quarter.

---

## Mac Attack

The rise in popularity has attracted threat actors to Apple’s ecosystem.

![Chart showing Trojan, Adware & PUP Proportional Split]

### The Ubiquitous Trojans
TrojanDownloader is the most significant contender, holding over half of the attacks.

### The Adware Brouhaha
Bundlore and Pirrit continue to hold the reign in the macOS space.

### A Pinch of PUPs
Apps masquerading as system cleaners or key generators continue to remain prevalent.

---

## Latest Security News

- **Rusty Droid**: A Remote Access Trojan (RAT) masquerading as a Chrome browser for Android to track financial activities.
- **Serpent**: A stealer malware that steals credentials and sensitive information from applications and browsers.
- **Mallox**: Ransomware that evades the Antimalware Scan Interface (AMSI) to stay stealthy.

---

## Key Takeaways

| Enterprise | Consumer |
| :--- | :--- |
| Keep devices up-to-date and patched | Use a reputable security product (K7 Total Security, etc.) |
| Establish a secure network for all endpoints | Only use official app stores |
| Encrypt and backup sensitive data | Keep OS and software updated |

---
*Copyright © 2023 K7 Computing Private Limited, All Rights Reserved.*