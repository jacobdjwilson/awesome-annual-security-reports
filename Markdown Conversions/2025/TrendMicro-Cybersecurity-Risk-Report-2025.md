# Cybersecurity Risk Report 2025: Outpacing the Adversary

## Table of Contents
- [The Cyber Risk Index](#the-cyber-risk-index)
- [Cyber Risk Index Data](#cyber-risk-index-data)
- [Risk Events and Detections](#risk-events-and-detections)
- [Vulnerabilities, Patch, and Response Data](#vulnerabilities-patch-and-response-data)
- [External Threat Data Sections](#external-threat-data-sections)
- [Ransomware](#ransomware)
- [Notable APT campaigns](#notable-apt-campaigns)
- [Malware](#malware)
- [ZDI](#zdi)

---

## The Cyber Risk Index

The Trend 2025 Cyber Risk Report sustains our shift towards proactive security. Protecting enterprises is no longer about stopping breaches but is now about staying ahead, making cybersecurity a business enabler. This report harnesses data from the Cyber Risk Exposure Management[^1] (CREM) solution of our flagship cybersecurity platform Trend Vision One™[^2].

CREM calculates an enterprise’s Cyber Risk Index (CRI), a metric that quantifies the overall security risk of an organization based on a consolidation of individual assets and risk factor scores. Our research[^4] has found that organizations with a CRI above the average have a greater likelihood to suffer from attacks than those with a lower CRI.

The CRI uses a scale from 0-100:
- **Low Risk (0-30)**: Organizations in this category are considered relatively secure.
- **Medium Risk (31-69)**: Organizations in this category have several risk factors that need to be addressed.
- **High Risk (70-100)**: Organizations in this category are exposed to severe risks.

Learn more with our [Cyber Risk Index Overview](https://example.com)[^5] and our technical report on [how to understand risk score calculations](https://example.com)[^6].

---

## Cyber Risk Index Data

The overall average CRI in 2024 improved consistently per month, ending at 36.3. While this improvement suggests that enterprises have been successfully operationalizing cyber risk management, a 36.3 overall CRI still falls within medium risk.

![Chart showing monthly CRI averages from February to December 2024]

### Regional Average CRI
There is a general downtrend in risk indices among the regions; Europe exhibited the biggest improvement from February to December with a 7-point difference, influenced by the Digital Operational Resilience Act[^7] and the Cyber Resilience Act[^8].

### Top Industries
The education sector had the highest average CRI at the beginning of the year and remained among the highest by the last quarter of 2024. Factors affecting this include legacy systems, remote learning environments, and limited resources.

---

## Risk Events and Detections

We look at the top detections in our telemetry on risky events, misconfigurations, Extended Detection and Response (XDR) model hits, Security Analytics Engine (SAE), and Endpoint Detection and Response (EDR) hits.

### Overall Top 10 Risky Events
1. Risky Cloud App Access
2. Stale Microsoft Entra ID Account
3. Sandbox Detected Email Threat
4. On-Premises AD Account with Weak Sign-In Security Policy - Password Expiration Disabled
5. Advanced Spam Protection - Policy Violation
6. Data Loss Prevention - Email Violation
7. Microsoft Entra ID Account with Weak Sign-In Security Policy - MFA Disabled
8. Microsoft Entra ID Account with Weak Sign-In Security Policy - Password Expiration Disabled
9. Stale On-Premises AD Account
10. On-Premises AD Account with Weak Sign-In Security Policy - Password Not Required

---

## Vulnerabilities, Patch, and Response Data

The most detected unpatched vulnerabilities have patches released in the first half of 2024. Most are classified as high severity related to Elevation of Privilege (EoP), except for the most detected, which is a Remote Code Execution (RCE) vulnerability.

### Average Mean Time To Patch (MTTP)
- **Europe**: 23.5 days
- **Japan**: 27.5 days
- **Americas**: 29.2 days
- **AMEA**: 32.9 days

---

## External Threat Data Sections

### Notable uses of AI in cybercrime
- **LLM risks**[^25]: Vector and embedding weaknesses, misinformation, and unbounded consumption.
- **Rogue AI**[^26]: Malicious rogues or subversion of AI resources.
- **Improved Reconnaissance**[^27]: Using AI to pull vast amounts of information to identify victims.
- **Intensified Disinformation campaigns**[^28]: Deepfake content used to shape public perceptions.
- **Pig butchering**[^29]: Deepfake technology used in extortion schemes.
- **Virtual kidnapping**[^30]: Use of deepfake audio or voice cloning.
- **Malicious digital twins**[^31]: Generative AI used to produce convincing messages and scale operations.

---

## Ransomware

Our leak site monitoring shows that ransomware groups have the most victim enterprises from North America, with 369 successful breaches on companies that did not pay ransom.

![Chart of Top Ransomware Intrusion Sets including RansomHub, Akira, and Medusa]

---

## Notable APT campaigns

- **Earth Kurma**: Targets Southeast Asia governments for espionage.
- **Famous Chollima**: Exploits job listings to propagate malware and steal cryptocurrency.
- **KONNI Group**: Targets Russia for espionage.
- **Earth Koshchei**: Rogue RDP campaign targeting Ukrainian organizations.
- **Pawn Storm**: Clipboard and reCAPTCHA abuse targeting Ukrainian government organizations.
- **Earth Dahu**: Abuses TryCloudFlare for military intelligence activities.
- **Matyoshka**: Disinformation campaign related to US presidential elections.

---

## Malware

Top detected malware families include **CoinMiner**[^34], **Bondat**[^35], **Negasteal**[^36], and **Powload**[^37]. Trend Vision One – Endpoint Security provides prevention and protection capabilities across every stage of the attack chain.

---

## ZDI

Trend Zero-Day Initiative (ZDI) is the world’s largest agnostic bug bounty program. Our monitoring shows an increase in the use of zero-day exploits by ransomware groups. Since 2020, there have been 59 zero-day exploits leveraged by ransomware attacks.

---

[^1]: Cyber Risk Exposure Management
[^2]: Trend Vision One™
[^3]: eXtended Detection and Response
[^4]: Research on CRI and attack likelihood
[^5]: Cyber Risk Index Overview
[^6]: Technical report on risk score calculations
[^7]: Digital Operational Resilience Act
[^8]: Cyber Resilience Act
[^9]: Trend Vision One – Email and Collaboration Protection
[^10]: Trend Vision One™ - Identity Security
[^11]: Trend Vision One™ - Endpoint Security
[^12]: Trend Vision One™ - Cloud Security
[^13]: Hikvision cameras
[^14]: CVE-2021-36260
[^15]: CVE-2024-21357
[^16]: CVE-2024-30086
[^17]: CVE-2024-30082
[^18]: CVE-2024-30087
[^19]: CVE-2024-35250
[^20]: CVE-2024-30091
[^21]: CVE-2024-30049
[^22]: CVE-2024-30084
[^23]: CVE-2024-30050
[^24]: CVE-2024-30037
[^25]: LLM risks
[^26]: Rogue AI
[^27]: Improved Reconnaissance
[^28]: Intensified Disinformation campaigns
[^29]: Pig butchering
[^30]: Virtual kidnapping
[^31]: Malicious digital twins
[^32]: Nemucod
[^33]: Gamarue
[^34]: CoinMiner
[^35]: Bondat
[^36]: Negasteal
[^37]: Powload
[^38]: Prometei
[^39]: Dloader
[^40]: DownAd
[^41]: WebShell

---

day exploits (vulnerabilities exploited after a patch is available). The
lack of alternative markets might also be an influence, in that exploit developers lean more toward taking their wares to underground
auctions.
Trend 2025 Cyber Risk Report 53

External threat monitoring heatmap
Top countries with the most ransomware attacks
240,117
1,347,243 Germany 394,351
181,573
United States 514,019 Japan
South Korea
Turkey
1,134,833
Thailand
474,488
209,282 Taiwan
India
241,511
Brazil
169,211
Singapore
This heatmap presents the regions and countries that our telemetry tracked as having the most ransomware threat activity.
Figures in each map represent ransomware threats that have been detected and blocked by our sensors. It’s important to note that
cybercriminals do not target any country or region specifically. However, these numbers show areas that should take extra precautions
to make enterprise systems more resilient against ransomware attacks.
Trend 2025 Cyber Risk Report 54

Top countries with the most malware detections
101,644,979
188,554,351
United Kingdom
Germany
661,026,169 1,008,580,748
United States Japan
149,799,897 193,155,280
129,207,144
France India
Italy
176,754,704
Taiwan
168,021,421
Brazil
98,987,181
Australia
This heatmap presents the regions and countries that our telemetry tracked as having the most malware threats detected and blocked
by our sensors. It’s important to note that cybercriminals do not target any country or region specifically. However, these numbers
show areas that should take extra precautions to make enterprise systems more resilient against malware attack campaigns.
Trend 2025 Cyber Risk Report 55

Top countries with the most detected email threats
732,679,789
395,609,663
Canada
Russia
644,570,215 534,517,762
United Kingdom Netherlands
4,095,791,263
United States
947,614,419
827,350,062 China
1,022,307,312 Germany
France
398,001,086
1,030,130,818
Indonesia
India
This heatmap presents regions and countries where our telemetry tracked email threats originated from. Email threats detected by
our sensors deployed globally scan for their originating IP addresses and reveal where they come from.
Trend 2025 Cyber Risk Report 56

From Reactive
to Proactive

A risk-based approach to cybersecurity will shift an enterprise’s strategy from being reactive to proactive. By identifying the
weaknesses in the defenses and by understanding how cybercriminals are using these exposures to their benefit, enterprises can take
the necessary countermeasures to create a more secure defense before the inevitable next cyberattack happens. When an enterprise
recalibrates to be more proactive, it can make its time and resource allocation more efficient even as it expands and demands more
security coverage.
Trend’s Cyber Risk Exposure Management enables teams to uncover risks and thereby thwart attacks by prioritizing mitigation actions
to lower organizational risk exposure. Its use of AI empowers security teams to swiftly predict, anticipate, and detect threats with
state-of-the-art cybersecurity solutions. Looking at the trends in the past year’s risk indices and contributing risk factors extracted
from our Cyber Risk Exposure Management data and threat intelligence, enterprises are recommended to do the following:
1. Optimize security settings to maximize product features and be alerted on misconfigurations, vulnerabilities, and other risks.
Leverage native sensors or utilize third-party sources to build a comprehensive view of your attack surface.
2. When a risky event is detected, contact the device and/or account owner to verify the event, and investigate the event using the
Vision One Workbench. Utilize the Vision One Workbench search function to find more information about the event or check the
event details on product management server.
3. Inventory stale accounts to delete inactive and unused ones. Disable risky accounts, or reset their passwords with strong ones, and
enable multi-factor authentication (MFA).
Trend 2025 Cyber Risk Report 58

4. Apply the latest patches or upgrade the version of applications regularly.
5. Apply the latest patches or upgrade the operating system version regularly.
Adopt a risk-based approach to anticipate threats, strategize resource allocation, tailor security measures, and enhance situational
awareness with the continuous discovery, assessment and mitigation of an enterprise’s IT ecosystem. By identifying high, medium, and
low risk components of the attack surface, organizations can create an action plan to prevent attacks before they even happen and
lower their overall risk in the near, medium, and long term.
Trend 2025 Cyber Risk Report 59

Endnotes
1 Trend Micro. (n.d.). Trend Micro. “Cyber Risk Exposure Management”. Accessed on Mar. 21, 2025, at: Link.
2 Trend Micro. (n.d.). Trend Micro. “One Platform”. Accessed on Mar. 21, 2025, at: Link.
3 Trend Micro. (n.d.). Trend Micro. “XDR (Extended Detection and Response)”. Accessed on Mar. 21, 2025, at: Link.
4 Trend Micro. (February 10, 2025). Trend Micro. “From Vulnerable to Resilient: Cutting Ransomware Risk with Proactive Attack Surface
Management”. Accessed on Mar. 21, 2025, at: Link.
5 Trend Micro. (n.d.). Trend Micro. “Trend Vision One Risk Index Overview”. Accessed on Mar. 21, 2025, at: Link.
6 Trend Micro. (n.d.). Trend Micro. “More Than a Number: Your Risk Score Explained”. Accessed on Mar. 21, 2025, at: Link.
7 Digital Operational Resilience Act. (n.d.). Digital Operational Resilience Act. “Official Website”. Accessed on Mar. 21, 2025, at: Link.
8 European Commission. (n.d.). Digital Strategy - European Commission. “Cyber Resilience Act”. Accessed on Mar. 21, 2025, at: Link.
9 Trend Micro. (n.d.). Trend Micro. “Email and Collaboration Security”. Accessed on Mar. 21, 2025, at: Link.
10 Trend Micro. (n.d.). Trend Micro. “Identity and Access Management”. Accessed on Mar. 21, 2025, at: Link.
11 Trend Micro. (n.d.). Trend Micro. “Endpoint Security”. Accessed on Mar. 21, 2025, at: Link.
12 Trend Micro. (n.d.). Trend Micro. “Hybrid Cloud Security”. Accessed on Mar. 21, 2025, at: Link.
13 CISA. (Sep. 28, 2021). Cybersecurity & Infrastructure Security Agency (CISA). “RCE Vulnerability in Hikvision Cameras (CVE-2021-36260)”. Accessed
on Mar. 21, 2025, at: Link.
Trend 2025 Cyber Risk Report 60

14 NIST. (Sep. 22, 2021). National Institute of Standards and Technology (NIST). “CVE-2021-36260 Detail”. Accessed on Mar. 21, 2025, at: Link.
15 NIST. (Feb. 13, 2024)”. National Vulnerability Database (NVD). “CVE-2024-21357”. Accessed on Mar. 21, 2025, at: Link.
16 NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30086”. Accessed on Mar. 21, 2025, at: Link.
17 NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30082”. Accessed on Mar. 21, 2025, at: Link.
18 NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30087”. Accessed on Mar. 21, 2025, at: Link.
19 NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-35250”. Accessed on Mar. 21, 2025, at: Link.
20 NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30091”. Accessed on Mar. 21, 2025, at: Link.
21 NIST. (May 14, 2024). National Vulnerability Database (NVD). “CVE-2024-30049”. Accessed on Mar. 21, 2025, at: Link.
22 NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30084”. Accessed on Mar. 21, 2025, at: Link.
23 NIST. (May 14, 2024). National Vulnerability Database (NVD). “CVE-2024-30050”. Accessed on Mar. 21, 2025, at: Link.
24 NIST. (May 14, 2024). National Vulnerability Database (NVD). “CVE-2024-30037”. Accessed on Mar 21, 2025, at: Link.
25 Gennai Security Project. (Nov. 17, 2024). Gennai Security Project. “OWASP Top 10 for LLM Applications 2025”. Accessed on Mar. 21, 2025, at: Link.
26 AI Team. (Aug. 15, 2024). Trend Micro. “Rogue AI: Part 1”. Accessed on Mar. 21, 2025, at: Link.
27 Nada Elrayes. (Sep. 26, 2024). Trend Micro. “Countering AI-Driven Threats with AI-Powered Defense”. Accessed on Mar. 21, 2025, at: Link.
28 Trend Micro. (Sep. 19, 2024). Trend Micro. “The Illusion of Choice: Uncovering Electoral Deceptions in the Age of AI”. Accessed on Mar. 21, 2025, at:
Link.
Trend 2025 Cyber Risk Report 61

29 Trend Research. (n.d.). Trend Micro. “Unmasking Pig Butchering Scams and Protecting Your Financial Future”. Accessed on Mar. 21, 2025, at: Link.
30 Craig Gibson, Josiah Hagen. (June 28, 2023). Trend Micro. “How Cybercriminals Can Perform Virtual Kidnapping Scams Using AI Voice Cloning
Tools and ChatGPT”. Accessed on Mar. 21, 2025, at: Link.
31 Trend Micro. (Dec. 16, 2024). Trend Micro. “Trend Micro Predicts Emergence of Deepfake-Powered Malicious Digital Twins”. Accessed on Mar. 21,
2025, at: Link.
32 Trend Micro. (n.d.). Trend Micro. “Coinminer.Win32.MalXMR.Ads”. Accessed on Mar. 21, 2025, at: Link.
33 Trend Micro. (n.d.). Trend Micro. “LNK_Bondat.SM”. Accessed on Mar. 21, 2025, at: Link.
34 Trend Micro. (n.d.). Trend Micro. “Tspy_Negasteal”. Accessed on Mar. 21, 2025, at: Link.
35 Trend Micro. (n.d.). Trend Micro. “Trojan.PS1.Powload.JKP”. Accessed on Mar. 21, 2025, at: Link.
36 Trend Micro. (n.d.). Trend Micro. “JS_Nemucod.SMC”. Accessed on Mar. 21, 2025, at: Link.
37 Trend Micro. (n.d.). Trend Micro. “Worm_Gamarue.SMJA”. Accessed on Mar. 21, 2025, at: Link.
38 Trend Micro. (n.d.). Trend Micro. “Trojan.Win32.Prometei.E”. Accessed on Mar. 21, 2025, at: Link.
39 Trend Micro. (n.d.). Trend Micro. “Worm.Win32.Dloader.LGA”. Accessed on Mar. 21, 2025, at: Link.
40T rend Micro. (n.d.).Trend Micro. “Troj_Downad.E”. Accessed on Mar. 21, 2025, at: Link.
41 Trend Micro. (n.d.). Trend Micro. “Trojan.PHP.Webshell.SBJKUC”. Accessed on Mar. 21, 2025, at: Link.
Trend 2025 Cyber Risk Report 62

Trend Micro, a global cybersecurity leader, helps make the world safe for exchanging digital information. Fueled by decades of security expertise, global threat
research, and continuous innovation, Trend’s AI-powered cybersecurity platform protects over 500,000 organizations and millions of individuals across clouds,
networks, devices, and endpoints.
Trend’s platform delivers advanced threat defense techniques, extended detection and response (XDR), attack surface management (ASM), and integration across the
IT ecosystem, including AWS, Microsoft, and Google. This enables organizations to better understand, communicate, and mitigate cyber risk.
Trend’s global threat research team delivers unparalleled intelligence and insights that power the platform and help protect organizations around the world from
hundreds of millions of threats daily.
With 7,000 employees across 70 countries, Trend is singularly focused on cybersecurity by enabling organizations to simplify their connected world. TrendMicro.com.
Trend Micro Standard Copyright Notice
Copyright ©2025 Trend Micro Incorporated. All rights reserved. Trend Micro, the Trend Micro logo, and the t-ball logo are trademarks or registered trademarks of Trend
Micro Incorporated. All other company and/or product names may be trademarks or registered trademarks of their owners. Information contained in this document is
subject to change without notice. Trend Micro, the Trend Micro logo, and the t-ball logo Reg. U.S. Pat. & Tm. Off.
For details about what personal information we collect and why, please see our Privacy Notice on our website at: trendmicro.com/privacy