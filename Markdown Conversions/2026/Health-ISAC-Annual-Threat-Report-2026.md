# 2026 Global Health Sector Threat Landscape

**Organization:** Health  
**Report Title:** ISAC-Annual-Threat-Report  
**Year:** 2026  
**TLP:** WHITE (This report may be shared without restriction.)

## Table of Contents
- [Introduction](#introduction)
- [Part I: The Current Threat Landscape](#part-i-the-current-threat-landscape)
  - [Physical Security](#physical-security)
  - [Cybercriminal Activity](#cybercriminal-activity)
  - [Significant Takedowns](#significant-takedowns)
  - [Ransomware Gangs Attacking Health Sector](#ransomware-gangs-attacking-health-sector)
  - [Ransomware Trends in the Health Sector](#ransomware-trends-in-the-health-sector)
  - [Nation-State Activity](#nation-state-activity)
  - [Medical Device Cybersecurity](#medical-device-cybersecurity)
- [Part II: Tactics, Techniques, and Procedures](#part-ii-tactics-techniques-and-procedures)
  - [Social Engineering](#social-engineering)
  - [Malicious Activity Observed by Members](#malicious-activity-observed-by-members)
  - [Notable Vulnerabilities](#notable-vulnerabilities)
  - [Popular Targeted Alerts](#popular-targeted-alerts)
- [Part III: Future Cybersecurity Outlook](#part-iii-future-cybersecurity-outlook)
  - [Business Resilience](#business-resilience)
- [Conclusion](#conclusion)

---

## Introduction

2025 was defined by a critical escalation in the volume, complexity, and systemic risk facing the global health ecosystem. As the digital transformation of the health sector—from advanced medical devices to telehealth platforms—continued to accelerate, it expanded the attack surface, confirming that the health industry remains a primary, high-value target for cybercriminals and nation-state actors alike.

The primary threat facing the health sector remains ransomware, with prolific groups like Qilin, INC Ransom, and the rapidly growing SAFEPAY dominating the threat landscape. However, the most concerning trend is the continued pivot and acceleration by threat actors to supply chain exploitation. Major security incidents throughout the year repeatedly demonstrated that a provider’s security is only as strong as its weakest vendor link, leading to widespread compromises that impacted millions of patient records and forced a significant industry-wide reevaluation of third-party risk management.

Attack methodologies also evolved, requiring more advanced defenses. The proliferation of sophisticated social engineering techniques used in malware, such as ClickFix and FileFix, along with the emergence of QR code phishing (quishing), showcased an increasing reliance on methods that bypass traditional perimeter defenses by exploiting human trust. The evolving attack methodologies were often successfully countered, as demonstrated by the intervention of illegitimate Cobalt Strike usage and the successful takedown of the RaccoonO365 phishing-as-a-service infrastructure.

Compounding these cyber challenges is the unique duality of the health sector: the urgent need to secure life-critical operational technology and the exposure to geopolitical events. The security risks posed by legacy medical devices, particularly those approaching end-of-life, demanded immediate compensating controls to protect patient safety. Furthermore, 2025 saw the continued impact of nation-state cyber activity, from widespread remote IT worker fraud campaigns to hybrid warfare tactics that leveraged cybercriminal elements against geopolitical adversaries.

As we look toward 2026, the focus must shift from incident response to sustained Business Resilience. The lessons learned from massive disruptive events—such as the widespread impact from the faulty CrowdStrike update in July 2024—underscore the necessity for robust planning that goes beyond traditional cybersecurity and addresses operational continuity in the face of widespread third-party failure.

---

## Part I: The Current Threat Landscape

### Physical Security
Throughout 2025, the health sector has maintained an increased focus on workplace violence and the safety of staff. Most recent reporting by the Bureau of Labor Statistics in 2023 states that healthcare was the industry where staff had the highest likelihood of experiencing violence in the workplace.[^1]

#### Physical Security / Violence Legislation – U.S. and Global
From a regulatory perspective in the United States, the Save Healthcare Workers Act (H.R. 3178/S.1600) was reintroduced to Congress for a third time on May 5, 2025. The legislation aims to make assault on a healthcare worker a felony offense.

#### Man-Made and Natural Threats to Security
The 2025 wildfire season in North America was marked by multiple major fires. There were also multiple significant viral outbreaks throughout the year, the largest of which was the resurgence of Chikungunya.

### Cybercriminal Activity
#### Hacktivist Attacks Against the Health Sector
Hacktivism involves using hacking techniques to promote a political or social cause. Attackers are increasingly targeting business associates and third-party vendors that provide critical services to healthcare providers. In June 2025, a Hacktivist group operating on Telegram within a channel dubbed ServerKillers orchestrated a temporary disruption of websites associated with Medical Centers in Israel.

#### Data Breaches — Episource
Data breaches were identified as the fourth most severe concern for global health sector cybersecurity professionals in 2025. A ransomware-driven intrusion between January and February 2025 exposed data from over 5.4 million individuals.

### Significant Takedowns
#### Cybercriminal Cobalt Strike Usage Down 80%
In the first quarter of 2025, Fortra announced abuse by threat actors had dropped by 80%, thanks largely to the joint Cobalt Strike disruption effort started in 2023.

#### RaccoonO365 Disruption
RaccoonO365 is a phishing-as-a-service kit used in cyberattacks to steal user credentials. Starting in 2024, Microsoft’s Digital Crimes Unit (DCU) collaborated with Health-ISAC to take down the RaccoonO365 phishing service. The DCU seized 338 websites associated with RaccoonO365.

### Ransomware Gangs Attacking Health Sector
Health-ISAC tracked 455 ransomware events across the health sector in 2025.

| Ransomware Gang | Number of Health Sector Entities Attacked |
| :--- | :--- |
| Qilin | 77 |
| INC Ransom | 50 |
| SAFEPAY | 23 |
| Sinobi | 21 |
| World Leaks | 18 |

### Ransomware Trends in the Health Sector
SAFEPAY, Qilin, and INC Ransomware have the highest percentage increase in victim count year-over-year. LockBit was the top group attacking the health sector in 2022, 2023, and 2024, but no incidents were observed in 2025.

### Nation-State Activity
#### DPRK Remote IT Worker Campaigns
North Korea has waged a concerted nation-state run operation to secure remote IT jobs to generate revenue for its national weapons development programs.

### Medical Device Cybersecurity
#### Contec CMS 8000 Patient Monitor
On January 30, 2025, CISA issued advisory ICSMA-25-030-01, warning of severe vulnerabilities in Contec CMS8000 patient monitors, including out-of-bounds write, hard-coded backdoor access, and privacy leakage.

---

## Part II: Tactics, Techniques, and Procedures

### Social Engineering
#### ClickFix and FileFix
ClickFix, first seen in 2024, uses phishing emails, malvertising, and SEO poisoning to redirect users to fake error pages. FileFix, a variant that emerged in 2025, utilizes multilingual phishing sites and anti-analysis techniques to evade detection.

#### QR Code Phishing
QR phishing, or “quishing,” is an emerging threat where threat actors embed malicious URLs in QR codes to steal credentials or deliver malware.

### Malicious Activity Observed by Members
- **XWorm**: A remote access trojan (RAT) designed to harvest information.
- **NetSupportRAT**: Malware packaged to look like the legitimate remote management tool NetSupport Manager.
- **njRAT**: Used to remotely control target computers.
- **SocGholish**: A malware loader primarily used for initial access.
- **AsyncRAT**: A malware family used to target Windows systems.

### Notable Vulnerabilities
- **Microsoft SharePoint ToolShell (CVE-2025-53770)**: A Remote Code Execution (RCE) vulnerability.
- **Cisco ASA 5500-X Series**: Under active exploitation by malicious actors as of September 2025.

### Popular Targeted Alerts
Health-ISAC’s Threat Operations Center shared more than 1,200 Targeted Alerts in 2025.

| Vulnerabilities & Exposures | Targeted Alerts Distributed |
| :--- | :--- |
| Dangling DNS | 407 |
| Citrix NetScaler | 98 |
| BeyondTrust | 77 |
| CEO Doxxing | 54 |
| RDP | 41 |

---

## Part III: Future Cybersecurity Outlook

### Business Resilience
The CrowdStrike Faulty Update incident in July 2024 highlighted a significant supply chain risk. Approximately 69% of survey respondents indicated that their organization was affected by the outage. In response, 73% indicated they have reassessed their business resiliency strategy.

---

## Conclusion
In today's interconnected health sector, no organization is alone in facing cyber threats. Information sharing and collaboration through Health-ISAC is the key to building a unified front against cybercrime.

---

[^1]: https://www.bls.gov/iif/factsheets/workplace-violence-2021-2022.htm

---

hreats and proven mitigation strategies from your peers.

 Expertise: Crowdsourced knowledge from industry veterans to strengthen your defenses and elevate
your team’s skills.

 Resilience: Collaborative trust to navigate evolving threats with confidence and maintain a secure,
reliable network.

•

 Innovation: Shared insights that fuel cutting-edge cybersecurity solutions for a safer future.

Take action today:

•

 Visit the Health-ISAC website or contact your Health-ISAC Member Engagement
representative to learn more about the community and membership benefits.

•  For technical guidance, please view Health and Human Services (HHS) and the Health
     Sector Coordinating Council’s (HSCC) joint publication:
     405(d) Health Industry Cybersecurity Practices (HICP)

•  Download Health-ISAC’s white paper on Information Sharing Best Practices in
      healthcare, available here.

•

 Connect with your peers on the Health-ISAC member portal or Secure Chat and
join the conversation.

If you are unaware of these resources, please contact Health-ISAC Member

•
     Engagement, who will help you get access.

Together, we can build a stronger, more resilient health ecosystem where patient
safety is always the top priority. Don’t wait for the next attack. Be part of the solution.
Share, collaborate, and secure the future of health sector.

If you have any comments

or questions about this

report, please reach out

to Health-ISAC at
contact@h-isac.org

24

health-isac.org

2026 Health Sector Cyber Threat LandscapeHealth-ISAC, Inc.
12249 Science Drive, Suite 370
Orlando, FL 32826

Drève Richelle 161 M Box 57
1410 Waterloo, Belgium

Health-ISAC.org

Health-ISAC’s mission is to empower trusted relationships
in the global Health Sector to prevent, detect, and respond
to cybersecurity and physical security events so that
Members can focus on improving health and saving lives.

Together, we are stronger, better, and more resilient  We invite you to join us

Memberships are purchased for your organization (not individuals), with
unlimited seat licenses. To schedule a membership overview, visit
https://health-isac.org/join-h-isac/