# Cyber Threat Monitor Report Q3 2023-24

## Table of Contents
- [Comprehending our Cyberspace](#comprehending-our-cyberspace)
- [Regional Infection Profile](#regional-infection-profile)
- [The Metro and Tier-1 Cities - Infection Rate](#the-metro-and-tier-1-cities---infection-rate)
- [Top Infection Rates in Tier-2 Cities](#top-infection-rates-in-tier-2-cities)
- [Infection Rate Comparison Across Platforms](#infection-rate-comparison-across-platforms)
- [Enterprise Insecurity](#enterprise-insecurity)
- [Safety Recommendations](#safety-recommendations)
- [Vulnerabilities Galore](#vulnerabilities-galore)
- [Dangers in the Internet of Things](#dangers-in-the-internet-of-things)
- [Mitigation Techniques](#mitigation-techniques)
- [Windows Under Siege](#windows-under-siege)
- [Windows Exploits](#windows-exploits)
- [Heuristic Host Intrusion Prevention System (HIPS)](#heuristic-host-intrusion-prevention-system-hips)
- [Mitigation Tips](#mitigation-tips)
- [The Mobile Device Story](#the-mobile-device-story)
- [The Omnipresent Trojan](#the-omnipresent-trojan)
- [The Adware Saga](#the-adware-saga)
- [Tips to Stay Safe](#tips-to-stay-safe)
- [Mac Attack](#mac-attack)
- [The Ubiquitous Trojans](#the-ubiquitous-trojans)
- [The Adware Brouhaha](#the-adware-brouhaha)
- [A Pinch of PUPs](#a-pinch-of-pups)
- [Safety Guidelines](#safety-guidelines)
- [Latest Security News](#latest-security-news)
- [Key Takeaways](#key-takeaways)

---

## Comprehending our Cyberspace

While Israel is grappling with attacks by Hamas on its soil, Islamic hacktivist groups have launched a digital war on its digital infrastructure intensifying the conflict further.

A rise in politically and religiously motivated hacktivist groups targeting Israeli critical infrastructure with DDoS attacks was also seen. After Israeli organisations such as media, defence and other critical infrastructures fell victim, its age-old ally India came to its rescue by unleashing its group of hackers to defend their systems and other sensitive digital assets.

On the other hand, its holiday season in the US and the rest of the world. More cyber attacks are foreseen on countries supporting Israel and the subsequent retaliation. It is going to be a different ball game altogether for the threat actors and if played well, they are the ones who are going to benefit the most, be it money or just stopping operations.

A rise in ransomware operations; mainly due to the large attack surface and monetary benefit that it offers for the threat actors, and crypto malware; mining cryptocurrencies is very lucrative and cryptojacking is an inexpensive way to mine, are foreseen. Threat actors are also creating variants of existing malware with enhanced evasion techniques. Ransomware-as-a-service (RaaS) methodology will involve a lot of players in the field, both amateurs and professionals.

The world is reeling under chaotic times and we also foresee a rise in nation-state sponsored threat activity. Nations and organizations need to up their defences by following proper cyber hygiene practices and training their employees to stay safe from this ongoing digital warfare.

We at K7 Labs offer significant protection from emerging and latest threats at the earliest by closely examining and identifying such incidents and providing security at multiple layers.

Our quarterly reports list case studies that ignited our interest and were found worthy of sharing, threat scenarios across major Indian cities, significant vulnerabilities, top threats in Windows, Android, and macOS platforms, and relevant mitigation techniques.

This report explains the what and how of the topics under consideration without getting into deep technical details to suit a broad readership base. However, those interested in a more detailed analysis are more than welcome to read our K7 Labs’ technical blogs.

Kindly read and share the report with your colleagues.
Stay Alert, Stay Vigilant!

![Map of India showing regional infection rates by city]

## Regional Infection Profile

Irrespective of its type, a security breach is a thing to worry about in every aspect of our digital life. And that’s precisely what our infection rate indices indicate.

Those new to our quarterly report would need to understand an important concept called “Infection Rate” (IR) which is used as the base for benchmarking a netizen’s risk.

We use this IR factor to identify the netizens’ exposure to cyber threats. IR is determined as the proportion of K7 users in an area who encountered at least one cyber threat event and which was blocked and reported to our K7 Ecosystem Threat Intelligence infrastructure. The higher the IR, the greater the risk.

The concept of Infection Rate is better explained by the below picturization.

![Diagram showing the flow of K7 Ecosystem Threat Intelligence]

**Infection Rate at XYZ: 4/50 = 8%**

**The overall Pan-India IR in comparison with the previous quarter is given below:**
- Q3_2023-24: 35%
- Q2_2023-24: 38%

The slight reduction in the infection rate doesn’t intend a much safer digital experience. This could be attributed to incidents not reported and products not activated/updated.

## The Metro and Tier-1 Cities - Infection Rate

![Chart showing infection rates for Ahmedabad, Hyderabad, Bengaluru, Kolkata, Chennai, Mumbai, Delhi, and Pune]

## Top Infection Rates in Tier-2 Cities

![Bar chart showing infection rates for various Tier-2 cities]

Threat actors have also started focusing more on Tier-2 cities due to a plethora of factors such as poor cyber hygiene, lack of awareness, etc.

## Infection Rate Comparison Across Platforms

Even though Windows is a closed-source system, its enormous user base presents a lucrative chance for cybercriminals seeking notoriety and bragging rights.

![Comparison chart of Windows IR vs Android IR across major cities]

As the chart reveals, threat actors are also targeting Android users, major Indian cities like Ahmedabad, Bengaluru, Chennai, and Pune witnessing a reasonable volume of attacks. This simply reflects the differing tactics employed by threat actors on each platform.

## Enterprise Insecurity

Cryptomining malware can jeopardize the availability and security of a network or system and can stall an enterprises’ operations. It co-opts the victims’ computing resources to mine cryptocurrencies. It is resource intensive and happens without the knowledge of the victim. It hides on your network and steals the computing resources, thereby slowing down the entire network.

Recently, one of our enterprise customers complained of frequent pop-up notifications from our security product, about a malicious file detected while it was being copied from the local network. This file was deployed in one of the internet facing SQL servers which was poorly protected and was spreading laterally across the network.

**The kill chain is as below:**
![Diagram of the LemonDuck malware kill chain]

## Safety Recommendations

- Deploying tools to monitor your organizations’ network
- Enforcing least privilege access
- Enforcing use of strong passwords and multi-factor authentication (MFA)
- Keeping your devices updated and patched against the latest vulnerabilities
- Protecting your devices by using a high-quality security software such as K7 Endpoint Security and keeping it up-to-date

## Vulnerabilities Galore

### Vulnerability in Skype’s Business Products
CVE-2023-41763, an information disclosure vulnerability, allows an attacker to elevate their privileges.
- Vulnerable products: Skype for Business Server 2015 CU13 < 6.0.9319.869, Skype for Business Server 2019 CU7 < 7.0.246.530

### Wordpad’s Information Disclosure Vulnerability
CVE-2023-36563, in Microsoft Wordpad works by convincing a user into opening a malicious file, which allows the disclosure of NTLM hashes.
- Vulnerable products: Windows 10 and 11, Windows Server 2008, 2012, 2016, 2019 and 2022.

### SmartScreen ByPass Vulnerability
CVE-2023-36025, tricks an user into clicking on a malicious URL, by which an adversary may be able to bypass Windows Defender SmartScreen checks.
- Vulnerable products: Windows 10 and 11, Windows Server 2008, 2012, 2016, 2019 and 2022.

### Google Chrome’s Buffer Overflow Vulnerability
CVE-2023-5217, allows a remote attacker to potentially exploit a heap corruption via a crafted HTML page.
- Vulnerable products: Google Chrome

### RCE Vulnerability in Microsoft’s Excel
CVE-2023-36041, convinces a victim to open a specially crafted file from a website, leading to local attack on their computer.
- Vulnerable products: MS office 2019 & 2016, 365 Apps for Enterprise, Office LTSC for Mac 2021, Office LTSC 2021.

## Dangers in the Internet of Things

### Sophos Command Injection Vulnerability
CVE-2023-1671 in Sophos Web Appliance allows execution of arbitrary code.
- Vulnerable products: Sophos Web Appliance < 4.3.10.4

### Privilege Escalation Vulnerability in Bluetooth module
CVE-2023-45866 is a remote privilege escalation vulnerability in the Bluetooth module (bluez).
- Vulnerable products: Android OS <= 10, macOS <= 14.1.1, Ubuntu <= 23.10, iOS <= 17.1.1.

### Vulnerability in Apple Products
CVE-2023-42916 (out-of-bounds read) and CVE-2023-42917 (memory corruption) in WebKit.
- Vulnerable products: iOS, iPadOS, macOS.

## Mitigation Techniques

- Encrypt your connections
- Ensure you set a unique and strong password for each of your devices in the network
- Connect your devices to only a secure and trusted network
- Regularly check your device permissions and connections

## Windows Under Siege

### Windows Malware Type Breakdown
![Chart showing the split of Windows Top 10 Detections]

## Windows Exploits

![Chart showing the most prevalent exploits]

## Heuristic Host Intrusion Prevention System (HIPS)

![Chart showing Windows Heuristic Behavioural Detections]

This time Injectors increased by a significant percentage in comparison to the previous quarter. Injectors are malware that use legitimate file names or locations to hide behind trusted names so as to evade detection.

## Mitigation Tips

- Use an account without administrator privileges wherever possible
- Set up your operating system to enable auto-updates by default
- Be cautious when installing any software
- Backup your data on a regular basis

## The Mobile Device Story

Imagine your phone not as a sleek device but as a vault overflowing with personal and financial treasures. This allure of readily accessible data makes Android users prime targets.

![Chart showing Adware vs Trojan Proportional Split]

## The Omnipresent Trojan

![Chart showing most prevalent Trojan types]

## The Adware Saga

![Trend line showing the Adware plague]

## Tips to Stay Safe

- Always be extra cautious before downloading and installing any app
- Do not download or install apps from unknown sources or third-party app stores
- Keep your OS and devices updated and patched against the latest vulnerabilities
- Install a robust security product like K7 Mobile Security

## Mac Attack

![Chart showing Trojan, Adware & PUP Proportional Split]

## The Ubiquitous Trojans

![Chart showing Trojan detection trend line]

## The Adware Brouhaha

![Chart showing the trend line of Adware variant detections]

## A Pinch of PUPs

![Chart showing most prevalent PUP types]

## Safety Guidelines

- Keep your macOS updated and patched against the latest vulnerabilities
- Ensure scanning all your applications even if it is being downloaded from the official App Store
- Install a reputable security product like “K7 Antivirus for Mac”

## Latest Security News

### Rusty Droid spells trouble for Android users
A Remote Access Trojan (RAT) dubbed Rusty Droid masquerades as a Chrome browser for Android to track financial activities and steal sensitive information.

### This dangerous “Serpent” will steal your data
“Serpent” is a stealer malware that extracts credentials and sensitive information from various applications and browsers while maintaining stealth.

### How Mallox ransomware evades a Windows OS protection feature
Mallox ransomware has been discovered evading the Antimalware Scan Interface (AMSI) to remain undetected by AV products.

## Key Takeaways

### Enterprise
- Secure your devices by keeping them up-to-date and protected by high-quality security software.
- Establish a secure network for all your endpoints.
- Encrypt and backup your sensitive and critical data.

### Consumer
- Secure your devices with a reputable security product and keep them up-to-date.
- Only use the official app store for app downloads and installations.
- Keep your OS and software updated and patched against the latest vulnerabilities.