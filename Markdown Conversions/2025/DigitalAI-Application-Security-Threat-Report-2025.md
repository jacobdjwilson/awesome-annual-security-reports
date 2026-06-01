# 2025 Application Security Threat Report

## Table of Contents
- [Introduction](#introduction)
- [Key Findings](#key-findings)
- [Methodology](#methodology)
- [Market and Industry Trends](#market-and-industry-trends)
- [Attack Data](#attack-data)
- [Threat Perspectives](#threat-perspectives)
- [Malware](#malware)
- [Conclusion](#conclusion)
- [Appendix](#appendix)

## Introduction
Imagine a scenario where an unknown actor systematically examines the security of four out of five houses in your neighborhood, checking to see if the doors are locked. Some houses are merely observed, while others with unsecured entries are explored, potentially leading to stolen blueprints or other goods. In the most egregious cases, the actor takes everything of value and ransacks the rest.

In January 2025, 83% of the client-side apps monitored by Digital.ai had their front door “checked” (Figure 1). What does this mean? These apps[^1] were either run in an unsafe environment—such as a jailbroken or rooted phone, or worse, in a debugger or emulator—or they were probed for weaknesses. In the worst-case scenarios, they were actively tampered with.

![Figure 1: In January 2025, 83% of Digital.ai-monitored client-side apps were attacked]

> “Threat actors are not only picking locks, they’re systematically checking every digital front door, and they’re armed with increasingly sophisticated technologies.”

Our digital neighborhoods are growing at an unprecedented rate, and they are under constant threat. In the face of such intrusions, and with the cost of a data breach approaching 5 million USD[^2], organizations cannot delay in fortifying their investments. With an explosion of freely available tools and AI-powered capabilities, threat actors can now effortlessly reverse-engineer, analyze, and exploit applications at an alarming scale.

## Key Findings
1. **Rising Attacks on Client-Side Apps**: The percentage of apps experiencing attacks has surged from 65% in February 2024 to 82.7% in January 2025, with mobile platforms (iOS: 88.1%, Android: 90.4%) being even more frequently targeted (Figure 2).
2. **More Apps Are Released More Frequently**: Organizations continue the frenetic pace of delivering apps to their customers. Apple’s App Store® and the Google Play™ store offered nearly 4 million apps[^3] with 137.8 billion downloads in 2024.
3. **Threats Are not Limited to FinServ Apps**: While financial services have traditionally been a primary target, new data highlights significant attacks in the Telecom (91%) and Automotive (86%) industries (Figure 3).
4. **Urgent Need for App Security**: Organizations must prioritize resilience against reverse engineering and tampering.

![Figure 2: Attacks rose on client-side apps from 2024-2025 across device types]
![Figure 3: Significant attacks in the Telecom and Automotive industries in 2025]

## Methodology
The report is based on data collected between January 1–31, 2025, from select customers of Digital.ai’s Application Security offerings. The attack types discussed (integrity, environment, and instrumentation) are the threats identified by the Organization of Worldwide Application Security Professionals (OWASP®) and documented in the OWASP Mobile Application Security Verification Standard (MASVS)[^4].

## Market and Industry Trends
### Market Trends
Mobile apps provide organizations with a direct, data-driven channel to understand, personalize, and enhance customer interactions in real-time. We live in an app-obsessed world, but threat actors are arguably even more enthusiastic.

### Industry Trends
- **Telecom**: As Telecom apps become essential gateways to content, connectivity, and financial transactions, they become more attractive targets for credential theft, fraud, and app manipulation.
- **Financial Services (FinServ)**: A trend towards embedding "Banking as a Service" (BaaS) into non-FinServ apps creates a decentralized and ripe target for threat actors.
- **Automotive**: The shift from hardware-centric to software-defined vehicles—with OTA updates and AI-powered driver assistance—provides prime opportunities for threat actors.
- **Healthcare**: The rise of digital health platforms and mobile health-tracking apps makes patient data susceptible to reverse-engineering.

## Attack Data
82.7% of apps experienced attacks in January 2025—a 27% increase from 2024. This is driven by tool democratization (Frida, Ghidra), the proliferation of AI tools, and an expanding attack surface.

### Attacks by Industry
- **FinServ**: 87.5% attack rate.
- **Healthcare**: 78.5% attack rate.
- **Automotive**: 86% attack rate.
- **Telecom**: 91% attack rate.

![Figure 5 (A-D): Attacks on client-side applications increased across all industries in 2025]

## Threat Perspectives
This section examines attack likelihood from both enterprise and end-user perspectives.
- **Enterprise Perspective**: Focuses on the proportion of affected apps relative to the total number of apps developed.
- **User-Level Perspective**: Measures threats by examining the scale of user exposure across total app instances.

### User Perspective (iOS vs. Android) Across OS Versions
Real-world data shows a bell curve of attacks, with higher frequencies in the middle Android versions (7–11) and Apple versions (13–15). Newer OS versions are typically more challenging to compromise, necessitating greater innovation from threat actors.

## Regional Differences in Attack Rate
Attack rates vary by region:
- **EMEA**: 0.69%
- **North America**: 0.64%
- **LATAM**: 0.42%
- **APAC**: 0.58%

Higher observed attack rates in EMEA and North America may indicate more robust security practices and better preparedness due to stringent regulatory frameworks like GDPR.

## Malware
Throughout January, 1.2% of monitored devices were infected with some type of malware.
- **High Threat Level**: 6.94% (Banking trojans, spyware, viruses, worms)
- **Medium Threat Level**: 10.65%
- **Low Threat Level**: 83.77%

## Conclusion
Attack rates on apps have reached unprecedented levels. Organizations can no longer afford to leave their doors unlocked. Mobile security demands a multi-layered approach, including obfuscation, anti-tamper techniques, strong encryption, and continuous monitoring.

## Appendix
The data was collected in January 2025. For inquiries, contact Daniel.Shugrue@digital.ai.

[^1]: A “client-side app” refers to a software application where most of its code runs on the user’s device.
[^2]: https://table.media/wp-content/uploads/2024/07/30132828/Cost-of-a-Data-Breach-Report-2024.pdf
[^3]: https://42matters.com/stats
[^4]: The OWASP® Word Mark and OWASP & Design™ Logo are registered or unregistered service marks of OWASP Foundation, Inc.