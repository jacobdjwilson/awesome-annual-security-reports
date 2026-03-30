# Global Threat Intelligence Report 2025

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Risk Radar](#risk-radar)
- [Threats in Focus](#threats-in-focus)
- [The Threat Landscape in Charts](#the-threat-landscape-in-charts)
- [Tracked Threat Actor Activity](#tracked-threat-actor-activity)
- [Conclusion](#conclusion)

---

## Introduction

In the first nine months of 2025, Mimecast processed more than 24 Trillion data points for its nearly 43,000 customers, flagging more than 9.13 billion threats during the nine-month period. The data reveals trends, including greater usage of trusted services, the preferred attacks against specific industries, and signs of AI usage among cyber threat groups. To best defend business systems, companies need to be aware of what techniques attackers are employing.

In our 2025 Global Threat Intelligence report, Mimecast has collected threat data from across our platform, focusing on the risks posed by business communications, collaboration environments, and workers. Along with insights from our intelligence analysts and open sources, this threat report aims to take vitals of the global threat landscape.

> DEFENDING AGAINST THESE RISKS REQUIRES REFRAMING CYBERSECURITY AS NOT ONLY A TECHNICAL CHALLENGE BUT A HUMAN AND GOVERNANCE ONE. IN GENERAL, COMPANIES NEED TO FOCUS ON SECURITY HYGIENE, INCLUDING AWARENESS TRAINING AND HARDENING SYSTEMS. WHILE TECHNICAL VULNERABILITIES REMAIN IMPORTANT, THREAT ACTORS INCREASINGLY RECOGNIZE THAT PEOPLE AND UNMANAGED SYSTEMS ARE THE WEAKEST LINKS IN ORGANIZATIONAL SECURITY.

---

## Executive Summary

The cybersecurity landscape in 2025 underscores both attackers’ persistence and the iterative improvements in attack techniques. Financial platforms, regulatory agencies, and city governments have all found themselves in the crosshairs, and the adversaries range from profit-driven ransomware operators to disciplined state-aligned teams.

Human workers remain the most consistent point of attack, with shadow IT and AI-driven social engineering providing attackers with both new tools and new targets. Social engineering tactics — from business email compromise (BEC) to credential phishing — are evolving into AI-powered operations that are increasingly able to mimic vendors, partners, and employees with credible email chains. Attackers have also further adopted the tactic of shifting communication channels (from email to voice, for example) and of using legitimate online services as the foundation of their offensive infrastructure.

Shadow IT creates blind spots for defenders, allowing exploitation of tools and services outside of organizations’ managed security controls. Whether through third-party wallet integrations in financial services or personal collaboration tools in corporate environments, attackers weaponize convenience against organizations. Remote work further compounds this challenge, as employees operate from less secure environments, often with minimal oversight or lack of awareness about their colleagues’ identities. Limited visibility enables undetected intrusions until significant damage occurs.

Finally, the rise of generative AI has dramatically lowered the barrier for highly convincing attacks. Threat actors can now automate spear-phishing campaigns, generate synthetic voices and video, and craft messages that evade traditional detection tools. This amplifies the scale and precision of social engineering, turning what were once niche, labor-intensive attacks into scalable operations. As a result, organizations must adapt by ensuring employees are prepared to recognize AI-augmented attacks and by adopting AI internally to improve business workflows and security operations.

---

## Key Findings

1. **HUMAN ELEMENT UNDER ASSAULT**: Threat actors increasingly target the human link in the attack chain as the most vulnerable element, doubling down on phishing attacks and social engineering with schemes such as ClickFix and AI-augmented phishing attacks.
2. **BEC ATTACKS EMBRACE AUTOMATION**: Business email compromise (BEC) has become more sophisticated with attackers using automated conversation chains to further the illusion that a worker is communicating with a legitimate vendor and that a senior executive is taking part.
3. **MULTI-CHANNEL ATTACK STRATEGIES**: Attacks increasingly incorporate a change of communication channels, such as including a phone number for the victim to call in a phishing email, which helps attackers bypass organizational defenses and minimizes visibility into attacks.
4. **LEGITIMATE SERVICES WEAPONIZED AT SCALE**: Continuing the trend of living off the land, living off trusted services (LOTS) has become more common, with attackers finding new ways to incorporate a wider variety of legitimate services — such as Adobe Pay, DocuSign, and Salesforce — into their attack chains.
5. **NOVEL OBFUSCATION METHODS**: Attackers constantly adopt new file formats that allow code execution or better obfuscation, such as hiding JavaScript in Scalable Vector Graphics (SVG) files or using QR codes to make it harder for users and security software to verify links.

---

## Risk Radar

Threat actors continue to evolve in 2025, with major cybercriminals groups targeting a wide swath of industries, such as retail, aviation, insurance, technology, managed service providers (MSPs), and critical infrastructure.

Social engineering and manipulation of human behavior are increasingly important pages in these cyberattackers’ playbooks, as they shift from traditional malware-based attacks to human-oriented tactics targeting messaging and collaboration platforms. Scattered Spider, also known as Storm-0875 or Octo Tempest, is a highly adaptive, well-resourced group that excels at sophisticated social engineering tactics, often impersonating IT teams or help desks. Another group, TA2541, uses virtual private servers to send phishing emails masquerading as requests for quotes and purchase orders, which eventually lead to malicious scripts embedded in files on Google Drive and OneDrive.

These threat actors also embody another shift in tactics: The increase in usage of trusted services as a primary attack vector to deliver their payload and conduct attacks. Trusted services complicate the work of detecting and preventing these threats using traditional security controls. Organizations need to focus on policies, procedures, and user awareness to complement technical security controls and make their workforce more resilient to these human-oriented attacks.

Threat actors have also adopted methods that make reversing their attacks and attribution more challenging. Cyberattackers’ increasingly use compromised systems— especially developing technology hubs in Southeast Asia and Africa — to launch their attacks complicating attempts to trace the origin of attacks, as researchers can only track adversaries to these jumping-off points. The ability to use advanced proxy networks, compromised home routers, and common affiliate networks that distribute an attacker’s workforce further obfuscates the attribution process.

---

## Threats in Focus

Since our 2024 report, cybercriminals and ransomware gangs have greatly expanded the use of trusted services to avoid technical defenses that might otherwise block their attacks — adopting a greater variety of services and using them far more frequently.

### CLICKFIX
Attackers have increasingly shifted toward exploiting user’s trust to bypass technical security precautions. Mimecast has documented the increasing use of the ClickFix technique — a social engineering scam where attackers use fake error messages or verification prompts to trick users into copying and running malicious commands on their own devices. A typical ClickFix attack chain uses website pop-ups or phishing landing pages to urge users to copy-and-paste a script onto the Windows command line or a PowerShell terminal. Doing so typically leads to the installation of infostealers, remote access trojans (RATs), ransomware, and credential stealers.

First detected in March 2024, the use of ClickFix has rapidly proliferated across the threat landscape. Mimecast detected multiple malware campaigns leveraging ClickFix in 2025, which has taken off in popularity, increasing by more than 500% in the first six months of the year. Overall, ClickFix accounted for nearly 8% of attacks reported, second only to phishing.

![900,000 detections of the technique across our customers in the United States and the United Kingdom.]
![2M of malicious SVG files detected, using a variety of social-engineering lures]

### CAPTCHAS FOIL THREAT GATHERING
Legitimate and custom CAPTCHA services allow threat actors to both better trick victims and slow threat researchers’ ability to detect attacks. By embedding CAPTCHAs on landing pages or within attack chains, threat actors block automated security crawlers and threat analysis tools from accessing and analyzing malicious content, simultaneously taking advantage of CAPTCHA’s legitimacy. Sophisticated JavaScript obfuscation further disables functions like right-click or keyboard shortcuts, hampering manual investigation and dynamic analysis by human analysts.

### SVG USAGE ON THE RISE
Phishing campaigns are increasingly exploiting the Scalable Vector Graphics (SVG) format to embed malicious JavaScript and other executable code in seemingly benign images. The malicious SVG files often execute code when opened, redirecting users to phishing pages or malware-download sites. Between mid-February and mid-March, Mimecast detected more than 2 million instances of malicious SVG files, using a variety of social-engineering lures, such as voice messages and multi-step redirections involving fake PDF downloads.

### ABUSE OF NOTIFICATION SERVICES
Email notification services are continuing to be abused to deliver malicious content. Instead of using low-reputation infrastructure, threat actors rely on known providers that organizations already trust, including:
- DocuSign
- Adobe Sign
- Intuit
- PayPal
- HelloSign

### USAGE OF REMOTE MONITORING AND MANAGEMENT
Threat actors are increasingly turning to legitimate Remote Monitoring and Management (RMM) tools— such as ScreenConnect (ConnectWise), TeamViewer, AnyDesk, and LogMeIn—to gain initial access to victim computers. This marks a significant shift from traditional tactics that relied on delivering malicious files or attachments via email.

### CHANGE OF COMMUNICATIONS CHANNEL
Another significant trend this year is the increasing use of multi-channel attacks, where threat actors initiate contact with victims through email and then transition to phone communication to further their schemes.

---

## The Threat Landscape in Charts

The telemetry from Mimecast security services highlights trends in attacker behavior. Not only are threat actors increasingly using trusted services as the foundation for their campaign infrastructure, but the detection shows signs that attackers are increasingly using AI-generated messages to create more phishing attacks.

### 01 LIVING OFF TRUSTED SERVICES (LOTS)
Threat actors continue to weaponize legitimate business services to bypass security controls and exploit organizational trust relationships. 

![Chart 01: The top legitimate domains used by attackers include DocSend, GetResponse, and Sharepoint, which resolve to pages on DocSend, ClkMg.com, and Microsoft SharePoint.]

### 02 COLLABORATION THREATS
Collaboration platforms fundamentally changed communication — and how threat actors operate. The platforms create persistent repositories where nothing truly disappears. When compromised these tools, provide comprehensive organizational visibility, enabling lateral movement and the hosting of malicious content within trusted environments.

![Chart 02: Detections of malware dominate collaboration environments, while spam and phishing make up the second and third-most encountered threats.]

### 03 INDUSTRY SNAPSHOT
Attackers use different techniques against different industries, tailoring their approaches based on what works through experience and understanding of sector-specific vulnerabilities.

![Chart 03: Threats per user (TPUs) for the Top-8 Industries]

### 04 BEC ATTEMPTS RISING AGAIN
Business email compromise (BEC) threats dropped during late February until early April — representing a temporarily shift to malware-based attacks — but quickly picked up in late spring and throughout the summer.

![Chart 04: BEC Threats Common Tags Count per Week]

### 05 TOP VULNERABILITIES OVER TIME
In 2024, nearly 40,000 vulnerabilities were reported to the National Vulnerability Database (NVD), or about 768 security issues every week. In 2025, the rate is on track to surpass an average of 900 vulnerabilities per week.

![Chart 05: Top-10 Vulnerabilities: Age vs. CVSS]

---

## Tracked Threat Actor Activity

Cybercrime-as-a-service models — RaaS, PhaaS, and Initial Access Brokers — enable multiple actors to deploy identical infrastructure, making attribution increasingly unreliable. Rather than focus on malware signatures, Mimecast tracks Tactics, Techniques, and Procedures (TTPs) to systematically categorize threats.

### SCATTERED SPIDER (MCTO3050)
- **First observed**: 2022
- **Goal**: Credential harvesting, data exfiltration, extortion, and ransomware deployment.
- **Targeted**: Broad, including retail, aviation, insurance, technology, managed service providers (MSPs), and critical infrastructure.

### UAC-0050 (DAVINCI GROUP) (MCTO1025)
- **First observed**: 2024
- **Goal**: Information theft, Financial theft, Psychological operations (PSYOP)
- **Targeted**: Government ministries, local authorities, the Ukrainian military, and civilians.

### STORM-1865 (MCTO1020)
- **First observed**: 2020
- **Goal**: Credential and data theft
- **Targeted**: Hospitality industry

---

## Conclusion

Living off trusted services has become standard methodology, with the 500% increase in ClickFix attacks and sophisticated multi-party BEC conversation chains revealing how quickly social engineering techniques proliferate. Industry-specific targeting shows mature threat operations that understand business workflows, creating persistent blind spots where compromised collaboration platforms expose years of strategic intelligence.

Artificial intelligence fundamentally transforms the threat landscape through multiple vectors. AI-generated phishing content leveraging pattern-of-life analysis and deepfake technology creates hyper-targeted spear phishing and whaling campaigns indistinguishable from legitimate communications. Organizations adopting AI technologies face new insider risks from data loss and inappropriate use, potentially exposing personally identifiable information and intellectual property.

Organizations must implement comprehensive security hygiene addressing both technical vulnerabilities and human factors through layered defenses. The convergence of AI-enhanced attacks, expanding shadow IT environments, and sophisticated supply chain targeting demands a fundamental shift from reactive security measures to proactive human risk management strategies that treat people as the first line of defense.