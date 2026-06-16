# THE 2025 IOT SECURITY LANDSCAPE REPORT

WWW.BITDEFENDER.COM/IOT

## Table of Contents
- [About This Report](#about-this-report)
- [Key Stats at a Glance](#key-stats-at-a-glance)
- [Notable IoT Incidents in 2025](#notable-iot-incidents-in-2025)
- [Sunlight, Panels and a Dark Side](#sunlight-panels-and-a-dark-side)
- [IoT Flaws Turn Private Lives into Public Show](#iot-flaws-turn-private-lives-into-public-show)
- [22.2 Tbps – The Rise of Router Botnets](#222-tbps--the-rise-of-router-botnets)
- [Smart Home Trends in 2025](#smart-home-trends-in-2025)
- [The Smart Home Building Blocks](#the-smart-home-building-blocks)
- [High-Tech Ding-Dong-Ditch](#high-tech-ding-dong-ditch)
- [Top Attacks](#top-attacks)
- [Top Vulnerable Devices](#top-vulnerable-devices)
- [BADBOX - Factory-Infected Devices](#badbox---factory-infected-devices)
- [Smart TV Sets: The Aging Tech of the Living Room](#smart-tv-sets-the-aging-tech-of-the-living-room)
- [Smart Plugs: The Silent Victims of the Modern Smarthome](#smart-plugs-the-silent-victims-of-the-modern-smarthome)
- [NAS Devices: Data Goldmines Under Siege](#nas-devices-data-goldmines-under-siege)
- [Top CVEs in Firmware](#top-cves-in-firmware)
- [A Predilection for Fresh Kernel CVEs](#a-predilection-for-fresh-kernel-cves)
- [Vulnerabilities by Targeted Outcome](#vulnerabilities-by-targeted-outcome)
- [Observations and Trends](#observations-and-trends)
- [Vulnerability Types and Risk Values](#vulnerability-types-and-risk-values)
- [A Guide to IoT CVE Outcomes](#a-guide-to-iot-cve-outcomes)
- [Looking Ahead at 2026](#looking-ahead-at-2026)
- [How to Stay Safe in 2026](#how-to-stay-safe-in-2026)
- [A Multi-Layered Approach to Home Security](#a-multi-layered-approach-to-home-security)

---

## About This Report
Bitdefender has built deep expertise in detecting, analyzing, and mitigating threats across the Internet of Things (IoT) ecosystem. Our IoT Lab monitors global trends and publishes insights into new attack vectors, vulnerability types and best practices for securing connected devices - from smart TVs and routers to wearables and phones.

This report draws on threat intelligence from 6.1 million smart homes across the US, Australia and Europe, protected by Bitdefender IoT Security technologies such as NETGEAR Armor. Our research team examined data from over 58 million IoT devices, analyzing 4.6 billion vulnerabilities[^1] and 13.6 billion IoT attacks to build a precise snapshot of the smart home security landscape. By combining large-scale insights with behavioral analysis, we aim to reveal how modern threats evolve, propagate and exploit the devices we rely on most - and how users can stay ahead of them.

[^1]: Bitdefender has blocked 4.6 billion attempts at exploiting non-unique device vulnerabilities. These attempts can leverage one or more known attack vectors multiple times.

The data used in this report was collected and analyzed between January 1 and October 1, 2025.

## Key Stats at a Glance
- **6 million households**: Sharing information about 13 billion attack attempts on routers and connected devices.
- **22 devices per household**: The average household has 22 connected devices.
- **29+ attacks every 24h**: Home network devices face an average of 29 attacks on connected devices per day.
- **4.6 billion vulnerabilities**: This report is based on analysis of 4.6 billion vulnerabilities exploitation attempts against live IoT targets.
- **12 million threats a day**: Bitdefender smart home technologies block 12 million threats a day around the world.

## Notable IoT Incidents in 2025
![Timeline of 2025 IoT incidents including PUMABOT, Dahua camera vulnerabilities, BadBox malware, 22.2 Tbps DDoS attack, Edimax zero-day, D-Link vulnerabilities, and US Cyber Trust Mark launch.]

## Sunlight, Panels and a Dark Side
In late 2024, our research team uncovered a startling reality: IoT is no longer just about smart homes, baby monitors or solar inverters – small devices sitting quietly in homes and lightbulbs. When connected devices control the flow of energy, water or healthcare equipment, they stop being personal conveniences and start being public risks.

Tens of thousands of inverters were accessible online because of vulnerabilities in device firmware. If compromised, these devices could be commanded to push or pull electricity into the grid in synchronized bursts. That could take down portions of a country’s critical infrastructure.

## IoT Flaws Turn Private Lives into Public Show
In one recent case, unsecured smart cameras turned ordinary people into unwitting stars of an underground reality stream broadcast from retail fitting rooms, swimming pools and private homes in Italy. In June 2025, five men were convicted of distributing thousands of hours of footage taken from compromised surveillance cameras.

## 22.2 Tbps – The Rise of Router Botnets
In September 2025, Cloudflare reported a 22.2 terabit-per-second distributed denial-of-service (DDoS) attack - the largest in history. The AISURU botnet, uncovered by QiAnXin’s XLab, shows how large-scale exploitation of consumer-grade networking gear can generate unprecedented attack volumes.

## Smart Home Trends in 2025
A look at the most popular devices and the top vulnerabilities affecting them.

## The Smart Home Building Blocks
The connected home of 2025 is a dense ecosystem dominated by mobile phones (19.6%), which serve as the control hub for automation, entertainment and personal data. Smart TVs (9.5%) and streaming devices (7.3%) highlight how connectivity still revolves around screens.

![Chart showing device distribution: Phone 19.57%, Other 29.98%, TV Set 9.46%, Streaming Device 7.28%, Tablet 5.98%, Network Equipment 4.95%, Speakers 4.51%, Unclassified 4.42%, Computer 4.26%, Laptop 4.26%, IP Camera 3.46%]

## High-Tech Ding-Dong-Ditch
We analyzed 13 billion security events targeting routers. More than 93% of the intercepts of our Network Attack Defense technology in 2025 are port scans - HighPorts and generic scanning.

## Top Attacks
![Chart of top attacks: High Ports scanning attack 70.63%, Bot Genua 23.20%, Others 3.96%, Password over HTTP 1.35%, DNS DOS 0.18%, Low Ports scanning attack 0.23%, Command Injection 0.12%, Ping Flood 0.12%, Bot DGA 0.12%, RDP bruteforce attack 0.09%]

## Top Vulnerable Devices
![Chart of vulnerable devices: Streaming Device 25.94%, TV 21.34%, IP Camera 8.62%, Speakers 6.94%, Unknown 3.88%, Extender 3.78%, Printer 2.01%, Home Automation 1.57%, NAS 1.49%, Switch 1.43%, Others 21.01%]

## BADBOX - Factory-Infected Devices
The BADBOX botnet, now spanning more than a million Android-based and IoT devices worldwide, thrives on cheap, uncertified hardware sold online under obscure brands. Many of these devices arrive with malicious firmware already installed.

## Smart TV Sets: The Aging Tech of the Living Room
Smart TVs account for 21.34% of all vulnerable IoT devices. Most households keep TVs for five to eight years – far longer than manufacturers release security patches.

## Smart Plugs: The Silent Victims of the Modern Smarthome
Smart plugs are cheap, ubiquitous, and often forgotten once installed. Their firmware is rarely updated, yet they’re always online, serving as easy botnet recruits.

## NAS Devices: Data Goldmines Under Siege
With cloud fatigue pushing consumers toward local storage, NAS boxes have become prized ransomware targets. QNAP’s Photo Station RCE and Synology’s DSM command-injection flaws were re-used in multiple ransomware campaigns.

## Top CVEs in Firmware
| CVE | Description / Root Cause | Severity / Impact | Affected Component |
| :--- | :--- | :--- | :--- |
| CVE-2025-37803 | Buffer size overflow in Linux kernel udmabuf_create() due to casting mismatch | CVSS 3.1 = 7.8 (High) | Many Linux kernel versions prior to patched versions |
| CVE-2025-37838 | Use-after-free (UAF) in Linux kernel’s HSI ssi_protocol driver due to race | CVSS 3.1 = 7.8 (High) | Kernel versions 6.7 up to <6.12.24 |
| CVE-2025-21751 | Linux kernel net/mlx5: error flow mis-handling in “matcher disconnect” path | CVSS 3.1 = 7.8 (High) | Affects mlx5 kernel driver |

## A Predilection for Fresh Kernel CVEs
Modern attacks prioritize the Linux kernel – the universal denominator across IoT ecosystems. New CVEs are easier to weaponize at scale.

## Vulnerabilities by Targeted Outcome
![Chart showing vulnerability types: Overflow, Denial of Service, Code Execution, Gain Privileges, Memory Corruption, SQL Injection, Directory Traversal, Information Leak, Obtain Information, Bypass a Restriction]

## Observations and Trends
Streaming devices, smart TVs, and IP cameras now sit at the top of the vulnerability pyramid.

## Vulnerability Types and Risk Values
Known (and fixed) CVEs represent the vast majority of IT vulnerabilities.
- **Known CVEs**: 99.43%
- **Weak Password**: 0.27%
- **HTTP Basic Authentication**: 0.30%

## A Guide to IoT CVE Outcomes
| CVSS Score | % of Total | Notes |
| :--- | :--- | :--- |
| 7.0 | 15.5% | HIGH severity, remotely reachable |
| 7.1 | 15% | HIGH severity, recurring auth flaws |
| 7.5 | 6.2% | HIGH severity; persistent network-facing |
| 7.6 | 0.7% | HIGH severity, auth bypass |
| 7.8 | 34.3% | HIGH severity; common IoT baseline flaw |
| 8.3 | 2.1% | HIGH severity; improper access control |
| 8.8 | 1.5% | CRITICAL severity, privilege escalation |
| 9.4 | 2.6% | CRITICAL severity; unauthenticated RCE |
| 9.8 | 1% | CRITICAL severity; lateral movement |
| 10 | 2.6% | CRITICAL severity; total device takeover |

## Looking Ahead at 2026
1. **Router Botnets Go Industrial**: Expansion beyond consumer environments into small and medium-sized businesses.
2. **Firmware Supply Chain Becomes Ground Zero**: Targeting firmware components and development kits used across entire product ecosystems.
3. **Privacy Erosion and Data Oversharing**: Growing concern regarding how IoT vendors store, process, and share user information.

## How to Stay Safe in 2026
- Know what’s connected.
- Replace legacy hardware.
- Segment your network.
- Patch devices as soon as a new firmware version becomes available.
- Use routers or gateways with built-in security.
- Avoid exposing LAN devices to the Internet unless necessary.

## A Multi-Layered Approach to Home Security
NETGEAR Armor™, powered by Bitdefender®, helps detect and block known and emerging threats, identify vulnerabilities, and strengthen privacy across network connected devices.