# 2025 SonicWall Cyber Threat Report

## Table of Contents
- [Letter from CEO, Bob VanKirk](#letter-from-ceo-bob-vankirk)
- [Executive Summary](#executive-summary)
- [The Escalation of Ransomware Attacks in 2024](#the-escalation-of-ransomware-attacks-in-2024)
- [Staggering Spike in Business Email Compromise (BEC) Attacks](#staggering-spike-in-business-email-compromise-bec-attacks)
- [The Speed of Threat Actors](#the-speed-of-threat-actors)
- [Living Off the Land Binaries (LOLBins): No Laughing Matter](#living-off-the-land-binaries-lolbins-no-laughing-matter)
- [AI Automation Tools Lower Barrier for Entry While Increasing Attack Complexity](#ai-automation-tools-lower-barrier-for-entry-while-increasing-attack-complexity)
- [The Internet of Things (IoT) Continues to Expand – And So Do IoT Threats](#the-internet-of-things-iot-continues-to-expand--and-so-do-iot-threats)
- [Increasing Diversity in Attack Types: Cybercriminals Are Getting Creative](#increasing-diversity-in-attack-types-cybercriminals-are-getting-creative)
- [The Hidden Risks in Everyday Life: PDFs, HTML Phishing, and Fake Mobile Apps](#the-hidden-risks-in-everyday-life-pdfs-html-phishing-and-fake-mobile-apps)
- [Challenges to Having an Effective Security Strategy](#challenges-to-having-an-effective-security-strategy)
- [Strategic Actions to Strengthen Your Cybersecurity Defense](#strategic-actions-to-strengthen-your-cybersecurity-defense)
- [Key Takeaways](#key-takeaways)

---

## Letter from CEO, Bob VanKirk

Today, I am proud to introduce the 2025 SonicWall Annual Threat Report. The adversaries we face are relentless and ever-evolving. SonicWall’s data indicates that threat actors are moving at unprecedented speeds, with the majority of hackers exploiting vulnerabilities within just two days after a working example of the exploit is made public.

In 2024, we identified 210,258 never-before-seen malware variants, averaging 637 new threats daily. The U.S. healthcare sector was particularly hard hit, with over 198 million patients impacted by ransomware. It is essential for businesses of all sizes to understand that they should not go it alone; partnering with managed service providers (MSPs) and managed security service providers (MSSPs) is crucial for bolstering defenses.

---

## Executive Summary

![Infographic showing 48-hour exploit window, 68 days of potential downtime saved, and 6 billion critical network attacks defended.]

- **Ransomware**: Intensified in North America (+8%) and exploded in LATAM (+259%).
- **Average Ransomware Cost**: $850,700, with total related losses often exceeding $4.91 million.
- **Malware**: Trended up 8% YoY, with a 92% spike in May.
- **IoT and Encrypted Threats**: IoT attacks rose 124% and encrypted threats climbed 93%.
- **SOC Insights**: Identity, cloud, and credential compromise account for 85% of actionable alerts.
- **BEC**: 33% of reported cyber insurance events are BEC incidents (up from 9% YoY).
- **RTDMI™**: 210,258 new malware variants identified (637 per day).

---

## The Escalation of Ransomware Attacks in 2024

Ransomware remains one of the costliest threats. Threat actors frequently utilize double and triple extortion tactics. In the healthcare industry, ransomware was utilized in 95% of all breaches.

**Key Vulnerabilities:**
- Microsoft Exchange Server flaws (ProxyShell and ProxyLogon) accounted for 60% of exploited healthcare vulnerabilities.
- The MOVEit SQL injection vulnerability (CVE-2023-34362) impacted over 3 million patients at CareSource.

**SOC POV**: Our Managed Security Services (MSS) team saw a 25% increase in ransomware over a 30-day period (late 2024 to early 2025), citing Fog, Akira, and SafePay as the most active groups.

---

## Staggering Spike in Business Email Compromise (BEC) Attacks

Nearly one-third of all reported cyber events were BEC attacks. Global losses from BEC exceeded $2.95 billion in 2024.

**Vendor Email Compromise (VEC)**: VEC attacks spiked by 68% in construction/engineering and 70% in retail/consumer goods manufacturing. Attackers impersonate vendors to exploit trusted relationships and steal payment information.

---

## The Speed of Threat Actors

Most attacks begin within 48 hours of proof-of-concept (PoC) disclosure. 
- **LockBit** exploited CVE-2024-27198 (JetBrains TeamCity) within 24 hours.
- **Cl0p** breached 66 companies within 48 hours of a PoC disclosure.

---

## Living Off the Land Binaries (LOLBins): No Laughing Matter

LOLBins are legitimate system tools used by attackers to evade detection. SonicWall identified `schtasks.exe` (34%), `cmd.exe` (28%), and `powershell.exe` (23%) as the most abused binaries.

**SOC POV**: At a childcare facility, attackers exploited an unpatched check-in kiosk, using pre-existing binaries for lateral movement and establishing persistence via the Group Policy Editor.

---

## AI Automation Tools Lower Barrier for Entry While Increasing Attack Complexity

Server-Side Request Forgery (SSRF) attacks increased by 452% in 2024. AI tools are being used to:
1. Locate unpatched systems.
2. Automate exploit chaining.
3. Evade detection through obfuscation.

---

## The Internet of Things (IoT) Continues to Expand – And So Do IoT Threats

SonicWall prevented over 17 million attacks on IP cameras in 2024. The **Reaper IoT Botnet** is a primary concern, focusing on vulnerabilities rather than just weak passwords.

**OSS Risks**: PHP, Apache (Log4j), and OpenSSL remain frequently exploited in IoT devices due to their widespread use in open-source projects.

---

## Increasing Diversity in Attack Types: Cybercriminals Are Getting Creative

**Strela Stealer**: A persistent threat in Europe that targets email credentials. It uses language and keyboard layout checks to avoid attacking Russia while focusing on Germany, Spain, Poland, and Italy.

---

## The Hidden Risks in Everyday Life: PDFs, HTML Phishing, and Fake Mobile Apps

- **File-based attacks**: 38% of malicious files were HTML-based; 22% were PDFs.
- **QR Codes**: Attackers embed QR codes in PDFs to redirect victims to fraudulent login pages.
- **Fake Android Apps**: Particularly prevalent in the APAC region, these apps request unnecessary permissions (like reading SMS) to intercept one-time passwords (OTPs).

---

## Challenges to Having an Effective Security Strategy

1. **Rapid Exploitation**: 75% of attacks start within four days of PoC disclosure.
2. **Ransomware Costs**: Recovery costs now exceed $4.91 million per incident.
3. **Human Error**: Remains a primary attack vector.
4. **BEC Surge**: Increased reliance on AI-driven deception.
5. **IoT Expansion**: Weak configurations in connected devices.
6. **AI Complexity**: Increased sophistication in SSRF and other automated attacks.
7. **File-based Methods**: Use of PDFs and HTML to bypass filters.

---

## Strategic Actions to Strengthen Your Cybersecurity Defense

- **Real-Time Patch Management**: Close vulnerabilities before they are exploited.
- **Cloud/SaaS Monitoring**: Enforce MFA and least-privilege access.
- **IoT Security**: Change default credentials and restrict network access.
- **Zero Trust**: Assume no implicit trust; validate every request.
- **24/7 SOC Services**: Utilize continuous monitoring for rapid incident response.

---

## Key Takeaways

- **SOC PoV**: Attackers are increasingly using LOLBins and exploiting unpatched internet-facing devices.
- **Cyber Insurance PoV**: Total ransomware costs are over 5x the actual ransom payment due to recovery expenses.
- **AI PoV**: AI is lowering the barrier to entry for complex attacks like SSRF and BEC.
- **Partner PoV**: Proactive monitoring is no longer optional; it is a requirement for survival in the current threat landscape.

---
*© 2025 SonicWall Inc. All rights reserved.*