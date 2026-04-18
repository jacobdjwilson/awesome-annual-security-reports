# 2025 MSP Threat Report

## Table of Contents
- [How We Build MSP Threat Reports](#how-we-build-msp-threat-reports)
- [Introduction](#introduction)
- [Ransomware Threat Landscape in 2024: A Shift in Tactics and Power Dynamics](#ransomware-threat-landscape-in-2024-a-shift-in-tactics-and-power-dynamics)
- [Vulnerabilities in 2024](#vulnerabilities-in-2024)
- [Timeline of Top Vulnerabilities in 2024](#timeline-of-top-vulnerabilities-in-2024)
- [Edge Security](#edge-security)
- [EDR Evasion: Current Trends, Tools, and Mitigation Strategies](#edr-evasion-current-trends-tools-and-mitigation-strategies)
- [Drive-by Compromise Still Going Strong](#drive-by-compromise-still-going-strong)
- [Conclusion](#conclusion)

---

## How We Build MSP Threat Reports

The ConnectWise MSP Threat Report was created in 2020 as a tool for managed service providers (MSPs), especially our partners, highlighting the latest cybersecurity information, including threats, mitigations, and solutions.

Our Cybersecurity Threat Reports (annual and quarterly) are made possible by the research and findings from the ConnectWise Cyber Research Unit™ (CRU). This elite team of threat hunters includes seasoned cybersecurity professionals with deep expertise in engineering, IT admin, security operations, incident analysis, and incident response. We use their skills and expertise to gather threat intelligence 24/7 from several sources, digging deep into ConnectWise partner and SMB client network data, ransomware leak sites, and malicious botnets to create this report and other resources.

Our collective goal is to monitor the threat landscape on an ongoing basis and help MSPs navigate the ever-changing cybersecurity landscape. Aside from our annual and quarterly reports, our ongoing findings provide education, context, and action items that will help you strengthen your business’ cybersecurity and your SMB cybersecurity services.

---

## Introduction

Cybersecurity threats evolve rapidly, and MSPs are increasingly in the crosshairs of attackers targeting the IT ecosystem. Instead of risking the attention of attacking large entities, threat actors use MSPs—who may have fewer cybersecurity resources—as a gateway to attack all their small and midsized (SMB) customers. These threat actors aim for several small payloads without the government and media attention associated with large attacks. Additionally, they are shifting tactics more quickly to try and find vulnerabilities faster than MSPs can fix them.

According to the report “The State of SMB Cybersecurity in 2024,” about 78% of MSPs surveyed said they were worried that a serious attack could put them out of business. As a result, about 83% said they plan to invest more in cybersecurity in the next 12 months.

The 2025 MSP Threat Report analyzes the past year’s most significant cyberthreats. Drawing from millions of endpoint detection and response (EDR) and security information and event management (SIEM) alerts across thousands of MSPs and their clients, this report highlights emerging trends, attack vectors, and practical defenses to help MSPs stay ahead of the curve.

The CRU is seeing a shift in the threat landscape, and the report covers three main challenges for MSPs to focus on:

1. **Advanced and evolving threats**: The consistent evolution of the threat landscape highlights the need for MSPs to stay updated on increasingly sophisticated cyberthreats and emerging trends.
2. **Targeted attacks on MSPs**: As prime targets for cybercriminals, MSPs face specific risks and challenges. The right level of awareness and education are critical to MSP defenses.
3. **Proactive security measures**: Adopting a proactive approach to security is a must-have, not a nice-to-have. Continuous monitoring is needed to address potential security gaps.

---

## Ransomware Threat Landscape in 2024: A Shift in Tactics and Power Dynamics

The ransomware landscape in 2024 has experienced significant shifts, influenced by key developments such as the disruption of the Lockbit ransomware group, evolving tactics by adversaries, and changes in target priorities.

### The Fall of Lockbit: A Watershed Moment
Lockbit, long considered one of the most formidable ransomware-as-a-service (RaaS) operations, faced unprecedented challenges in 2024. Law enforcement agencies coordinated efforts to dismantle key elements of the group’s infrastructure, including high-profile arrests and the seizure of servers. Despite this, remnants of the group attempted to pivot operations under different branding, such as “NotLockbit.”

### A Shift in Target Priorities
One notable trend in 2024 was ransomware groups increasingly targeting midsized businesses and less prominent organizations to avoid heightened law enforcement scrutiny. New geographic regions have also come under threat, such as the CosmicBeetle group targeting businesses across Europe and Asia.

### Data Extortion Gains Traction
2024 saw the growth of data extortion as a standalone strategy. Groups such as RansomHub have embraced this model, stealing sensitive data without deploying ransomware payloads. By threatening to release confidential information, these groups bypass the need for encrypting systems altogether, avoiding detection by endpoint and network monitoring tools.

### New Players and Sophistication in Techniques
The void left by Lockbit created an opportunity for new groups like BianLian, which relies on stealth and long-term reconnaissance. Additionally, CosmicBeetle has gained attention for its alliances with other cybercriminal groups, sharing tools and infrastructure.

### Law Enforcement Challenges and Victories
While the takedown of Lockbit represents a landmark achievement, law enforcement faces an uphill battle in combating ransomware globally, particularly when operators are based in jurisdictions with limited international cooperation.

---

## Vulnerabilities in 2024

The CRU identified the most impactful vulnerabilities affecting partner networks. Threat actors frequently targeted unpatched software, misconfigured systems, and known weaknesses in widely used technologies.

### ScreenConnect® Vulnerability
In February 2024, two critical vulnerabilities were disclosed in ScreenConnect: CVE-2024-1708 and CVE-2024-1709.
- **CVE-2024-1708**: A path traversal vulnerability (CVSS 8.4).
- **CVE-2024-1709**: An authentication bypass flaw (CVSS 10).

These were referenced in the media as “SlashandGrab.” MSPs were encouraged to prioritize patch management and implement layered defenses, including strict access controls and EDR solutions.

---

## Timeline of Top Vulnerabilities in 2024

![Visual timeline for top vulnerabilities in 2024]

- **January 2024**: CVE-2024-21887 (Ivanti Connect Secure)
- **February 2024**: CVE-2024-1708 (ScreenConnect)
- **February 2024**: CVE-2024-21893 (Ivanti Connect Secure)
- **February 2024**: CVE-2024-1709 (ScreenConnect)
- **March 2024**: CVE-2023-48788 (Fortinet FortiClient EMS)
- **April 2024**: CVE-2024-3400 (Palo Alto Networks PAN-OS)
- **May 2024**: CVE-2024-24919 (Check Point Quantum Security Gateways)
- **September 2024**: CVE-2024-8963 (Ivanti Cloud Services Appliance)
- **October 2024**: CVE-2024-50623 (Cleo Harmony, VLTrader, LexiCom)
- **November 2024**: CVE-2024-0012 (Palo Alto Networks PAN-OS)

---

## Edge Security

Edge devices such as firewalls and SSL VPN appliances remain high-value targets. Since January 2024, there has been a sharp increase in attempted attacks on edge devices, with over 84,000 recorded alerts targeting major brands.

### Importance of Strong Edge Security
Weak edge defenses can result in financial loss, data breaches, and supply chain risks. Organizations should audit exposure, implement regular patching, secure remote access, and invest in modern solutions like zero-trust architecture.

---

## EDR Evasion: Current Trends, Tools, and Mitigation Strategies

In 2024, the CRU observed a surge in the use of sophisticated EDR evasion techniques and purpose-built “EDR-killer” tools.

### Modern “EDR Killing” Utilities
- **AuKill (AvNeutralizer)**: Abuses vulnerable drivers to escalate privileges and terminate security defenses.
- **EDRKillShifter**: Uses the “bring your own vulnerable driver” (BYOVD) technique to disable EDR processes at the kernel level.
- **Terminator**: Exploits vulnerabilities in legitimate Zemana drivers to send malicious IOCTL commands.
- **EDRSilencer**: Leverages the Windows Filtering Platform (WFP) to block outbound network traffic from EDR processes.
- **PoorTry (BurntCigar)**: A malicious kernel-mode driver that evolved into an EDR wiper.

### Strategies to Mitigate EDR Evasion
- Implement zero-trust principles.
- Enable tamper protection features.
- Block vulnerable or unnecessary drivers.
- Enhance logging and monitoring via SIEM.

---

## Drive-by Compromise Still Going Strong

Drive-by compromise was a component of initial access in 22% of all incidents reviewed in 2024.

### ClickFix
A new social engineering technique emerged in 2024 called "ClickFix." Instead of convincing a victim to download a malicious file, malicious pages suggest an error can be remediated by pasting a command into a Run or admin PowerShell prompt. This executes a chain of malicious payloads.

### Potential Mitigations
- Use an ad blocker.
- Maintain an internal repository of trusted, up-to-date installers.
- Educate employees that browser updates should be enacted via the browser GUI, not through web pages.
- Restrict PowerShell usage for non-admin users where possible.

---

## Conclusion

The data indicates that threat actors will continue to target MSPs and quickly switch tactics. Combating these threats requires a layered approach to protection, prevention, and detection. A comprehensive cybersecurity stack should include awareness training, EDR/MDR, vulnerability and patch management, and SaaS cybersecurity solutions. ConnectWise remains committed to providing the tools and expertise necessary to help MSPs navigate this landscape.