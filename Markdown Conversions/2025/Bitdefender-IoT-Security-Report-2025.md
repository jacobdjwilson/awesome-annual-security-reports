# THE 2025 IOT SECURITY LANDSCAPE REPORT

[WWW.BITDEFENDER.COM/IOT](WWW.BITDEFENDER.COM/IOT)

## Table of Contents
- [About This Report](#about-this-report)
- [Key Stats at a Glance](#key-stats-at-a-glance)
- [Notable IoT Incidents in 2025](#notable-iot-incidents-in-2025)
- [Sunlight, Panels and a Dark Side](#sunlight-panels-and-a-dark-side)
- [IoT Flaws Turn Private Lives into Public Show](#iot-flaws-turn-private-lives-into-public-show)
- [22.2 Tbps – The Rise of Router Botnets](#222-tbps--the-rise-of-router-botnets)
- [Smart Home Trends in 2025](#smart-home-trends-in-2025)
- [The Smart Home](#the-smart-home)
- [The Smart Home Building Blocks](#the-smart-home-building-blocks)
- [High-Tech Ding-Dong-Ditch](#high-tech-ding-dong-ditch)
- [Top Vulnerable Devices](#top-vulnerable-devices)
- [BADBOX - Factory-Infected Devices](#badbox---factory-infected-devices)
- [Smart TV Sets](#smart-tv-sets)
- [Smart Plugs](#smart-plugs)
- [NAS Devices](#nas-devices)
- [Top CVEs in Firmware](#top-cves-in-firmware)
- [A Predilection for Fresh Kernel CVEs](#a-predilection-for-fresh-kernel-cves)
- [Devices by Vulnerability Type](#devices-by-vulnerability-type)
- [Vulnerabilities by Targeted Outcome](#vulnerabilities-by-targeted-outcome)
- [Observations and Trends](#observations-and-trends)
- [Vulnerability Types and Risk Values](#vulnerability-types-and-risk-values)
- [Looking Ahead at 2026](#looking-ahead-at-2026)
- [How to Stay Safe in 2026](#how-to-stay-safe-in-2026)
- [A Multi-Layered Approach to Home Security](#a-multi-layered-approach-to-home-security)

---

## About This Report

Bitdefender has built deep expertise in detecting, analyzing, and mitigating threats across the Internet of Things (IoT) ecosystem. Our IoT Lab monitors global trends and publishes insights into new attack vectors, vulnerability types and best practices for securing connected devices - from smart TVs and routers to wearables and phones.

This report draws on threat intelligence from 6.1 million smart homes across the US, Australia and Europe, protected by Bitdefender IoT Security technologies such as NETGEAR Armor. Our research team examined data from over 58 million IoT devices, analyzing 4.6 billion vulnerabilities* and 13.6 billion IoT attacks to build a precise snapshot of the smart home security landscape. By combining large-scale insights with behavioral analysis, we aim to reveal how modern threats evolve, propagate and exploit the devices we rely on most - and how users can stay ahead of them.

*Bitdefender has blocked 4.6 billion attempts at exploiting non-unique device vulnerabilities. These attempts can leverage one or more known attack vectors multiple times.

The data used in this report was collected and analyzed between January 1 and October 1, 2025, capturing the most recent developments in IoT threat activity and vulnerability trends. The findings reflect the threat dynamics shaping the smart home ecosystem today.

## Key Stats at a Glance

![Infographic showing 12 million threats blocked daily, 6 million households, 22 devices per household, 29+ attacks every 24h, and 4.6 billion vulnerabilities.]

## Notable IoT Incidents in 2025

![Timeline of 2025 IoT security incidents including the 13,000-device botnet, PUMABOT, Dahua camera vulnerabilities, FBI 'BADBOX' warning, 22.2 Tbps DDoS attack, CISA CVE-2025-1316 disclosure, US Cyber Trust Mark launch, and CISA KEV catalog additions.]

## Sunlight, Panels and a Dark Side

In late 2024, our research team uncovered a startling reality: solar inverters – small devices sitting quietly in homes and businesses – could be chained together into an attack force powerful enough to destabilize national power grids.

IoT is no longer just about smart homes, baby monitors or lightbulbs. When connected devices control the flow of energy, water or healthcare equipment, they stop being personal conveniences and start being public risks.

This is no theoretical risk – it's a real threat. Tens of thousands of inverters were accessible online because of vulnerabilities in device firmware. If compromised, these devices could be commanded to push or pull electricity into the grid in synchronized bursts. That could take down portions of a country’s critical infrastructure.

These inverters are technically consumer electronics. They sit in garages, on rooftops and in backyards. They are marketed for their efficiency and eco-friendliness, not resilience against cyberattacks. But when millions of households become miniature power plants, the line between consumer gadget and national infrastructure blurs.

Germany has already raised the alarm. With one of the highest rates of solar adoption in Europe, the country is acutely aware that millions of small-scale inverters, each connected to the internet, represent a critical vulnerability. Policymakers and grid operators worry that if attackers synchronized control over these devices, it could ripple across the national grid and disrupt energy stability at scale.

The future grid will be decentralized, green and digital - but it will also be dangerously fragile unless security keeps pace.

## IoT Flaws Turn Private Lives into Public Show

In one recent case, unsecured smart cameras turned ordinary people into unwitting stars of an underground reality stream broadcast from retail fitting rooms, swimming pools and private homes in Italy.

In June 2025, five men were convicted of distributing thousands of hours of footage taken from compromised surveillance cameras. Private moments were streamed and shared across Telegram and other platforms, often with degrading comments and location tags. Most victims still don’t know they were filmed.

These weren’t state-sponsored hackers or corporate-grade intrusions. This was voyeurism at scale, enabled by a common flaw in the form of unsecured IoT surveillance camera devices.

Cheap, poorly configured cameras promise security but deliver the opposite. Devices exposed to the internet, left with factory-default credentials, or manufactured with poor security practices become open doors. In the Milan case, the attackers weren’t hacking wizards. They were simply patient enough to scan the internet for publicly accessible cameras.

## 22.2 Tbps – The Rise of Router Botnets

In September 2025, Cloudflare reported a 22.2 terabit-per-second distributed denial-of-service (DDoS) attack - the largest in history. The event, which lasted only 40 seconds, generated over 10.6 billion packets per second, a torrent of malicious traffic equivalent to streaming a million 4K videos at once.

The AISURU botnet, uncovered by QiAnXin’s XLab, shows how large-scale exploitation of consumer-grade networking gear can generate unprecedented attack volumes. AISURU enslaved hundreds of thousands of routers worldwide, combining them into a weaponized mesh that saturates backbone links and overwhelms infrastructures.

The assault was autonomously detected and mitigated, setting a new benchmark for both attack scale and defense automation. While the culprits are not yet known, the scale and coordination suggest a link to hyper-volumetric botnets built from compromised routers and IoT devices.

The 22.2 Tbps incident highlights the shifting power balance between consumer IoT exploitation and core Internet stability. It’s yet another reminder that IoT devices - not data centers - are now the backbone of global cyber offense, and that the line between residential compromise and disruption of critical infrastructure grows thinner every year.

## Smart Home Trends in 2025

A look at the most popular devices and the top vulnerabilities affecting them.

## The Smart Home

The smart home ecosystem is dominated by mobile devices and screens, with phones representing nearly 20% of all connected endpoints – more than double the share of smart TVs. This reflects a shift: the smartphone has become the universal remote for the digital household.

Together with TVs, streaming devices, and tablets, entertainment and content consumption hardware make up more than a third of all connected nodes – convenience and leisure still drive most IoT adoption.

## The Smart Home Building Blocks

![Chart showing device distribution: Phone (19.57%), TV Set (9.46%), Streaming Device (7.28%), Network Equipment (5.98%), Computer (6.13%), Tablet (4.95%), Speakers (4.51%), Laptop (4.26%), IP Camera (3.46%), Unclassified (4.42%), and Other (29.98%).]

The connected home of 2025 is a dense ecosystem dominated by mobile phones (19.6%), which serve as the control hub for automation, entertainment and personal data. Smart TVs (9.5%) and streaming devices (7.3%) highlight how connectivity still revolves around screens, while traditional computers and laptops (10.3% combined) have shifted from the center of the network to become just another layer.

Nearly 30% of devices fall under “Other,” a mix of smart plugs, sensors, appliances, and unseen infrastructure that expands the household’s digital footprint. Along with network equipment, tablets, and speakers, the modern home increasingly resembles a small enterprise - always online, highly interdependent, and reliant on robust, network-level protection.

## High-Tech Ding-Dong-Ditch

We analysed 13 billion security events targeting routers to understand the threat dynamics of the Internet, from the moment you plug a new router into the WAN connection provided by your Internet Service Provider.

More than 93% of the intercepts of our Network Attack Defense technology in 2025 are port scans - HighPorts and generic scanning. This shows the Internet never sleeps – it’s constantly poking every exposed IP, over and over. It’s not targeted malice so much as ambient hostility in the form of bots sweeping the net for open doors. The sheer scale shows how networks swim in a sea of low-skill, high-volume reconnaissance.

![Chart showing attack types: High Ports scanning (70.63%), Low Ports scanning (23.20%), Password over HTTP (1.35%), Others (3.96%), and smaller percentages for DNS DOS, Bot Genua, Command Injection, Ping Flood, Bot DGA, and RDP bruteforce.]

## Top Vulnerable Devices

![Chart showing vulnerable device distribution: Streaming Device (25.94%), TV (21.34%), IP Camera (8.62%), Speakers (6.94%), Unknown (3.88%), Extender (3.78%), Printer (2.01%), Home Automation (1.57%), NAS (1.49%), Switch (1.43%), and Others (21.01%).]

The distribution of vulnerable IoT devices paints a different picture of the modern smart home. Streaming devices now dominate, accounting for more than a quarter of all detected vulnerabilities, followed by smart TVs and IP cameras. Together, entertainment and surveillance gear represent over half of all exposed devices – yet another sign of how easily everyday consumer electronics can become security liabilities.

## BADBOX - Factory-Infected Devices

The biggest threats to smart homes often start long before they get deployed on the household network. In June, the FBI warned streaming device owners about a new threat targeting their living rooms. The BADBOX botnet, now spanning more than a million Android-based and IoT devices worldwide, thrives on cheap, uncertified hardware sold online under obscure brands. Many of these devices - streaming boxes and projectors - arrive with malicious firmware already installed, silently enlisting their buyers into a network that launders traffic, commits ad fraud, and supports other criminal operations.

Once active, BadBOX turns compromised gadgets into residential proxies, allowing attackers to disguise their origin and push secondary payloads. The infections stretch across more than 220 regions, with the highest concentration in markets where low-cost imports dominate. Investigators have traced the operation to coordinated groups in China, where rebranded devices share identical backdoors and connect to the same control infrastructure.

## Smart TV Sets

Smart TVs account for 21.34% of all vulnerable IoT devices in our dataset. That's a near-perfect storm of risk: complex software stacks, long lifespans, and dismal update cycles. Most households keep TVs for five to eight years – far longer than manufacturers release security patches. Once vendor support ends, the device remains online, unpatched, and fully integrated into the home network.

## Smart Plugs

Smart plugs are cheap, ubiquitous, and often forgotten once installed. Their firmware is rarely updated, yet they’re always online, serving as easy botnet recruits or network footholds. In 2025, the surge in smart energy automation and remote-controlled outlets drew renewed attention from attackers.

## NAS Devices

With cloud fatigue pushing consumers toward local storage, NAS boxes have become prized ransomware targets. QNAP’s Photo Station RCE (CVE-2024-27130) and Synology’s DSM command-injection flaws were re-used in multiple ransomware campaigns. Groups such as Qilin and RA Group automated exploitation using Shodan to scan for exposed devices, encrypt data locally, and exfiltrate credentials to offshore servers.

## Top CVEs in Firmware

| CVE | Description / Root Cause | Severity / Impact | Affected Component |
| :--- | :--- | :--- | :--- |
| CVE-2025-37803 | Buffer size overflow in Linux kernel udmabuf_create() | CVSS 3.1 = 7.8 (High) | Linux kernel versions |
| CVE-2025-37838 | Use-after-free (UAF) in Linux kernel’s HSI ssi_protocol driver | CVSS 3.1 = 7.8 (High) | Kernel versions 6.7 to <6.12.24 |
| CVE-2025-21751 | Error flow mis-handling in “matcher disconnect” path (HWS) | CVSS 3.1 = 7.8 (High) | mlx5 kernel driver |

## A Predilection for Fresh Kernel CVEs

Modern attacks prioritize the Linux kernel – the universal denominator across IoT ecosystems, from NAS units to cameras. These devices often run with minimal patching and exposed services. The spike in 2025-dated CVEs doesn’t necessarily mean attackers are chasing novelty; it reflects that many IoT vendors ship firmware based on kernel trees that inherited vulnerabilities from upstream without integrating the corresponding fixes.

## Devices by Vulnerability Type

![Chart comparing vulnerability types (Denial of Service, Overflow, SQL Injection, HTTP, Memory Corruption, Execute Code, Gain Privileges) across Router, IP Camera, TV, NAS, and Smart Plug.]

## Vulnerabilities by Targeted Outcome

![Chart showing frequency of outcomes: Overflow, Denial of Service, Gain Privileges, Code Execution, Memory Corruption, Bypass a Restriction, Obtain Information, Information Leak, Directory Traversal, and SQL Injection.]

## Observations and Trends

Streaming devices, smart TVs, and IP cameras now sit at the top of the vulnerability pyramid, collectively representing more than half of all CVE-class issues detected in smart homes. Most flaws still fall into the overflow and denial-of-service categories, exposing these devices to system crashes and remote code execution attempts.

## Vulnerability Types and Risk Values

![Chart showing CVE (99.43%), HTTP Basic Authentication (0.30%), and Weak Password (0.27%).]

The distribution of CVSS scores attests to a persistent pattern in IoT security: most vulnerabilities fall within the High severity range (7.0 - 7.8). These vulnerabilities, while not immediately catastrophic, represent systemic weaknesses in firmware and network-facing services that remain exploitable over long periods.

## Looking Ahead at 2026

### 1. Router Botnets Go Industrial
IoT botnets are expected to continue their evolution, with router-based networks expanding beyond consumer environments into the infrastructure of small and medium-sized businesses.

### 2. Firmware Supply Chain Becomes Ground Zero
In 2026, attackers are likely to focus further up the supply chain, targeting firmware components and development kits used across entire product ecosystems.

### 3. Privacy Erosion and Data Oversharing
IoT ecosystems continue to generate unprecedented amounts of behavioural, environmental, and biometric data. In 2026, data protection authorities are expected to strengthen oversight of how IoT vendors store, process, and share user information.

## How to Stay Safe in 2026

- **Know what’s connected**: Keep an updated inventory of all IoT and networked devices.
- **Replace legacy hardware**: Devices that are no longer supported are permanent liabilities.
- **Segment your network**: Keep smart plugs, cameras and appliances on a separate network.
- **Patch devices**: Update firmware as soon as versions become available.
- **Use secure routers**: Utilize gateways with built-in security.
- **Avoid exposure**: Do not expose LAN devices to the Internet unless necessary.

## A Multi-Layered Approach to Home Security

The data is clear: the modern household faces continuous, automated cyber threats, averaging nearly 30 attacks every day. NETGEAR Armor™, powered by Bitdefender®, helps deliver that protection. Available through Nighthawk routers and Orbi Mesh WiFi systems, Armor helps to detect and block known and emerging threats, identify vulnerabilities, and strengthen privacy across network connected devices.